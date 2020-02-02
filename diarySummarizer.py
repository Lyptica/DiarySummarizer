"""
usage:
	python diarySummarizer.py

referances:
	installer
		python-3.8.1-amd64.exe
	exe
		https://techacademy.jp/magazine/18963
		pyinstaller hoge.py --onefile
		dist/hoge.exe
	find
		https://note.nkmk.me/python-glob-usage/
	hash
		https://qiita.com/kenta1984/items/5b61ecc4b96a30a32601
	cast
		https://www.javadrive.jp/python/num/index6.html
	fill
		https://note.nkmk.me/python-zero-padding/
	file
		https://note.nkmk.me/python-file-io-open-with/
	push
		https://note.nkmk.me/python-list-append-extend-insert/
	fopen
		https://qiita.com/Cesaroshun/items/b331844a54d3618c4c3a
	text replace
		https://note.nkmk.me/python-str-replace-translate-re-sub/
	method
		https://www.sejuku.net/blog/72161
	if
		https://note.nkmk.me/python-if-elif-else/
	class
		https://qiita.com/masaru/items/5ebf2e96d6524830511b
	comment
		https://qiita.com/simonritchie/items/49e0813508cad4876b5a
	sort
		https://note.nkmk.me/python-list-sort-sorted/
	sorting technic for Hash-Array
		https://qiita.com/yousuke_yamaguchi/items/23014a3c8d8beb8ba073
"""

import glob
import re
import os
from pprint import pprint

class DiarySummarizer:
	def fileAppend(self, filePath, appendStr):
		"""
		指定されたファイルに文字列を追記する。

		Parameters
		----------
		filepath  : String
		    追記対象のファイルパス
		appendStr : String
		    追記したい文字列
		"""

		file = open(f"{filePath}", 'a')
		file.write(f"{appendStr}")
		file.close()

	def getFileMetaInformations(self, srcInput, dstInput):
		"""
		サマリ対象のファイルを探して精査し、構造体に変換する。

		Parameters
		----------
		srcInput : String
		    コンバート元の日記が入ったフォルダまでのパス
		    ex) Diary/2019/1/2.txt
		dstInput : String
		    サマリを配置したいフォルダまでのパス

		Returns
		-------
		fileHashArray: Array
		    サマリ対象のメタ情報が入った構造体 (ソート済み)
		"""

		fileHashArray = []

		# gather meta data
		for v in glob.glob(f"{srcInput}/[1-2][0-9][0-9][0-9]/[0-9]*/[0-9]*.txt"):
			tmpHash = {
				'originalPath': '',
				'year' : '',
				'month': '',
				'day'  : '',
				'dstPath': '',
				'dateTimeForSortKey': 0,
			}
			# raw filepath (not usable on windows cli)
			tmpHash['originalPath'] = v
			# slash separated filepath (usable on windows cli)
			tmpHash['processedOriginalPath'] = tmpHash['originalPath'].replace('\\','/')
			# file meta information
			tmpName = tmpHash['originalPath'].split('\\')
			tmpHash['year']  = tmpName[1].zfill(4)
			tmpHash['month'] = tmpName[2].zfill(2)
			tmpHash['day']   = tmpName[3].split('.txt')[0].zfill(2)
			# destination of summary texts
			tmpHash['dstPath'] = f"{dstInput}/{tmpHash['year']}{tmpHash['month']}.txt"
			tmpHash['dateTimeForSortKey'] = int(f"{tmpHash['year']}{tmpHash['month']}{tmpHash['day']}")
			# commit
			fileHashArray.append(tmpHash)

		# sort technic
		fileHashArraySorted = sorted(fileHashArray, key=lambda x:x['dateTimeForSortKey'])

		return fileHashArraySorted

	def initializeDestination(self, dstInput, fileHashArray):
		"""
		サマリ格納先のディレクトリやファイルを初期化する。

		Parameters
		----------
		dstInput : String
		    サマリを配置したいフォルダまでのパス
		fileHashArray : Array
		    サマリ対象のメタ情報が入った構造体
		"""

		os.makedirs(f"{dstInput}", exist_ok=True)

		# dstPath initialize
		for v in fileHashArray:
			file = open(f"{v['dstPath']}", 'w')
			file.write("")
			file.close()

	def summarize(self, fileHashArray):
		"""
		メタ情報を使ってサマリファイルを組み上げる。

		Parameters
		----------
		fileHashArray : Array
		    サマリ対象のメタ情報が入った構造体
		"""

		for v in fileHashArray:
			# date on summary
			summaryDate = f"{v['year']}/{v['month']}/{v['day']}\n";
			self.fileAppend(v['dstPath'], summaryDate)

			# cat and process per line
			for vv in open(f"{v['processedOriginalPath']}", "r"):
				self.fileAppend(v['dstPath'], f"\t{vv}")

			# return on section end
			self.fileAppend(v['dstPath'], "\n")

			# end
			print (f"{v['dstPath']} に {v['processedOriginalPath']} の内容を書き出し中...")

	def initialize(self):
		"""
		起動メソッド
		"""

		# hearing src dst
		srcInput = input("日記が入ったフォルダ名を指定してください。(未指定の場合は「SimDiary」フォルダを参照)")
		if srcInput == '':
			srcInput = 'SimDiary'
		dstInput = input("サマリを出力したいフォルダを指定してください。(未指定の場合は「MyDiary」フォルダに書き出し)")
		if dstInput == '':
			dstInput = 'MyDiary'

		# search file and get meta
		fileHashArray = self.getFileMetaInformations(srcInput, dstInput)

		# initialize destination
		self.initializeDestination(dstInput, fileHashArray)

		# summarize
		self.summarize(fileHashArray)

		# logic end
		print ("完了！")
		input ("何かキーを押すと終了します")

# initialize
diarySummarizer = DiarySummarizer().initialize()
