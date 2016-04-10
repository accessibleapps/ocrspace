import requests

class APIError(Exception):
	pass


class OCRSpaceAPI(object):

	def __init__(self, key):
		self.key = key
		self.url = 'https://api.ocr.space/parse/image'


	def OCR_URL(self, url, overlay=False):
		payload = {
			'url': url,
			'isOverlayRequired': overlay,
			'apikey': self.key,
		}
		r = requests.post(self.url, data=payload)
		result = r.json()['ParsedResults'][0]
		if result['ErrorMessage']:
			raise APIError(result['ErrorMessage'])
		return result

