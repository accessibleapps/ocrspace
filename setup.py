from setuptools import setup

__version__ = "0.1"
__doc__ = """Requests-based wrapper over the ocr.space API"""

setup(
 name = "ocrspace",
 version = __version__,
 description = __doc__,
 py_modules = ["ocrspace"],
 install_requires = [
  'requests',
 ],
 classifiers = [
  'Development Status :: 3 - Alpha',
  'Intended Audience :: Developers',
  'Programming Language :: Python',
  'Topic :: Software Development :: Libraries',
 ],
)
