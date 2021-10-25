## https://leetcode.com/problems/subdomain-visit-count/
from typing import Collection, List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
    	D = {}
    	for c in cpdomains:
    		s = c.replace('.',' ').split()
    		n = int(s[0]) ## count (int)
            # for loop backward
    		for i in range(len(s)-1,0,-1):
    			t = ".".join(s[i:])
    			D[t] = D[t] + n if t in D else n
    	return [str(D[i])+" "+i for i in D]



