# -*- coding: utf-8 -*-
import re
class StringParser(object):
	@staticmethod
	def removeCFU(stringToParse):
		updatedString = re.sub('\s?[0-9] CFU.*', '', stringToParse)
		return updatedString