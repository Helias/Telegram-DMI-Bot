# -*- coding: utf-8 -*-
import re
class StringParser(object):
	@staticmethod
	def removeCFU(stringToParse):
		updatedString = re.sub('\s?[0-9] CFU.*', '', stringToParse)
		return updatedString
	@staticmethod
	def startsWithUpper(stringToParse):
		stringToParse = stringToParse[0].upper()+stringToParse[1:]
		return stringToParse