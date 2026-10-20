"""Check provider response contracts with mocked HTTP and local fixtures."""

from io import BytesIO
import unittest
from unittest.mock import Mock, patch

import ocrspace


class OCRSpaceResponseTests(unittest.TestCase):
    def setUp(self):
        self.api = ocrspace.OCRSpaceAPI("example-key")
        self.response = Mock()
        post = patch.object(ocrspace.requests, "post", return_value=self.response)
        post.start()
        self.addCleanup(post.stop)

    def test_provider_error_without_page_results_raises_api_error(self):
        # Provider-documented error schema, also reported in its support forum:
        # https://forum.ui.vision/t/internal-processing-error/5180
        messages = ["Some internal processing error occurred."]
        self.response.json.return_value = {
            "OCRExitCode": 99,
            "IsErroredOnProcessing": True,
            "ErrorMessage": messages,
            "ErrorDetails": "",
        }
        with BytesIO(b"local fixture") as image:
            calls = (
                (self.api.OCR_URL, "https://example.test/image.png"),
                (self.api.OCR_file, image),
            )
            for method, argument in calls:
                with self.subTest(method=method.__name__):
                    with self.assertRaises(ocrspace.APIError) as caught:
                        method(argument)
                    self.assertEqual(caught.exception.args[0], messages)

    def test_success_retains_url_and_file_return_shapes(self):
        pages = [
            {"ErrorMessage": "", "ParsedText": "first page"},
            {"ErrorMessage": "", "ParsedText": "second page"},
        ]
        self.response.json.return_value = {
            "IsErroredOnProcessing": False, "ParsedResults": pages
        }

        self.assertEqual(self.api.OCR_URL("https://example.test/image.png"), pages[0])
        with BytesIO(b"local fixture") as image:
            self.assertEqual(self.api.OCR_file(image), pages)

    def test_page_error_still_raises_api_error(self):
        self.response.json.return_value = {
            "IsErroredOnProcessing": False,
            "ParsedResults": [{"ErrorMessage": "page parse failed"}],
        }
        with self.assertRaises(ocrspace.APIError):
            self.api.OCR_URL("https://example.test/image.png")
        with BytesIO(b"local fixture") as image:
            with self.assertRaises(ocrspace.APIError):
                self.api.OCR_file(image)


if __name__ == "__main__":
    unittest.main()
