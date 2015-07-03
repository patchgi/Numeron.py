# coding: utf-8

# Python2.X encoding wrapper (Windows dedicated processing)
import codecs
import sys
import random
import time
sys.stdout = codecs.getwriter('cp932')(sys.stdout)
turn=True
turnCount=0

exitList=[]
SCALE=4

def createNum(_num,_m,_M):
	seed=range(_m,_M+1)
	random.shuffle(seed)
	data=[]
	for i in range(_num):
		data.append(seed.pop())
	return data

if __name__=="__main__":
	
	haveNum=createNum(SCALE,0,9)
	ehaveNum=createNum(SCALE,0,9)
	eHitList=[]
	eBiteList=[]

	print haveNum
	print ehaveNum
	while (True):
		time.sleep(1)
		if turn:

			Hit=0
			Bite=0
			print "Your Turn"
			data=raw_input()
			if data!=None:
				
				ques=[]
				if int(len(data))==4:
					for i in data:
						ques.append(int(i))

					for i in range(SCALE):
						if ehaveNum[i]==ques[i]:
							Hit+=1

						if ques[i] in ehaveNum:
							if ques[i]!=ehaveNum[i]:
								Bite+=1

					print str(Hit)+"H"+str(Bite)+"B"

					if Hit==4:
						break

					turn =not turn


		else:
			print "Enemy Turn"

			eHit=0
			eBite=0
			eresult=""

			edata=createNum(SCALE,0,9)


			for i in edata:
				eresult+=str(i)

			print eresult

			for i in range(SCALE):
				if haveNum[i]==edata[i]:
					eHit+=1

				if edata[i] in haveNum:
					if edata[i]!=ehaveNum[i]:
						eBite+=1

			eHitList.append(eHit)
			eBiteList.append(eBite)

			print str(eHit)+"H"+str(eBite)+"B"

			if eHit==4:
				break
			turnCount+=1
			turn =not turn
