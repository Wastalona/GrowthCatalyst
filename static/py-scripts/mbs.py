import sqlite3
import json

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import requests
from bs4 import BeautifulSoup


class SQLiteController:
	def __init__(self):
		self.__cursor = None
		self.headers = {
			"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
			"User-Agent":"Mozilla/5.0 (Windows NT 10.5;) AppleWebKit/600.34 (KHTML, like Gecko) Chrome/55.0.1393.349 Safari/600.1 Edge/17.37298",
		}


	def __del__(self): pass


class CurrencyParser:
	def __init__(self, city:str="Бобруйск"):
		self.url = "https://belarusbank.by/api/kursExchange"


	def get(self, mode:str="file"):
		"""
		Function makes a request to the site and 
		receives a response from it
		"""
		
		response = requests.get(self.url)
		try:
			if mode == "file":
				with open("currency.json", "w") as file:
					file.write(response)
				return "[ + ] file is recorded"
			else:
				response = response.json()
				return response[0]["USD_out"], response[0]["USD_in"]
		except ConnectionError as e:
			return f"Error: {e}"

	def __del__(self): pass


class PrivateBank:
	def __init__(self):
		self.__neccessary = None
		self.__unneccessary = None
		self.__storage = None
		self.__debts = None
		self.__near = None
		self.__usd = None


	# main methods
	def _add(self, value:float, percent:float) -> str:
		return ""

	def _remove(self, value:float, date:str) -> str:
		return ""

	def _clear(self) -> str:
		return ""

	def _history(self) -> str:
		return ""

	# backups
	def _backup(self, name:str) -> str:
		return f"Backup with name: {name} was created"

	def _backup_list(self, amount:int) -> str:
		return ""

	def __del__(self): pass


__all__ = ["PrivateBank"]