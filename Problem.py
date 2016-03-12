class Problem:
	__DEFAULT_ENCODING__ = "euc-kr"
	def __init__(self, problem_no=0, auth_by_key=False, cookie=None):
		self.__PROBLEM_NO__ = problem_no
		self.__AUTH_BY_KEY__ = auth_by_key
		if "PHPSESSID=" in cookie:
			self.cookie = cookie
		else:
			self.cookie = "PHPSESSID="+cookie+";"
		self.AUTH_KEY = None
		from urllib import request, error
		try:
			request.urlopen(request.Request("http://webhacking.kr/index.php", headers={"Cookie":self.cookie}))
		except error.HTTPError:
			print("[ERROR] Invalid cookie")
			exit(0)

	def login(self, user_id, user_pass):
		from urllib import request
		from urllib.parse import urlencode
		res = request.urlopen("http://webhacking.kr/index.html?enter=1", urlencode({"id": user_id, "pw": user_pass}).encode())
		print(res.getheader("Set-Cookie").split(";")[0])

	def solve(self):
		result = True
		if self.__AUTH_BY_KEY__:
			result = self.__auth__()
		if result:
			print("Solved Problem "+str(self.__PROBLEM_NO__))
		else:
			print("Failed to solve Problem "+str(self.__PROBLEM_NO__))

	def __auth__(self):
		from urllib import request
		from urllib.parse import urlencode
		from urllib.error import URLError

		if type(self.AUTH_KEY) is not str:
			print("Invalid Auth key...")
			return False
		try:
			res = request.urlopen(request.Request(
				"http://webhacking.kr/index.php?mode=auth_go",
				urlencode({"answer":self.AUTH_KEY}).encode(),
				{"Cookie":self.cookie}
			)).read().decode(self.__DEFAULT_ENCODING__)
			if "<script>alert('Wrong!');location.href='index.php';</script>" in res:
				return False
		except URLError:
			return False
		return True