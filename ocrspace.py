import requests

class APIError(Exception):
	pass


class OCRSpaceAPI(object):

	def __init__(self, key, url='https://api.ocr.space/parse/image'):
		self.key = key
		self.url = url

	def OCR_URL(self, url, overlay=False):
		payload = {
			'url': url,
			'isOverlayRequired': overlay,
			'apikey': self.key,
		}
		response = requests.post(self.url, data=payload)
		response.raise_for_status()
		response_data = response.json()
		if response_data.get('IsErroredOnProcessing') and not response_data.get('ParsedResults'):
			raise APIError(response_data.get('ErrorMessage'))
		result = response_data['ParsedResults'][0]
		if result['ErrorMessage']:
			raise APIError(result['ErrorMessage'])
		return result

	def OCR_file(self, fileobj, overlay=False):
		payload = {
			'isOverlayRequired': overlay,
			'apikey': self.key,
		}
		response = requests.post(self.url, data=payload, files={'file': fileobj})
		response.raise_for_status()
		response_data = response.json()
		if response_data.get('IsErroredOnProcessing') and not response_data.get('ParsedResults'):
			raise APIError(response_data.get('ErrorMessage'))
		results = response_data['ParsedResults']
		if results[0]['ErrorMessage']:
			raise APIError(results[0]['ErrorMessage'])
		return results

