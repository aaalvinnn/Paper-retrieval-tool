from database import Database
import pachong
import ms

# dbs = ms.Database()
nums = 200000

url = r'https://arxiv.org/list/cs.AI/pastweek?skip=0&show=500'
abc = pachong.pc(url)
for i in range(0,3):
    a = abc.get_arxiv(i)
    # e = abc.get_subject(i)
    # f = abc.get_pdf(i)
    val = (nums,a)
    print(val)

    