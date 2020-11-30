# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".

# Run time = 12 ms
# Memory Usage =13.3 MB

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        str = list(address)
        fstr = ""
        # Goes through array, finds . and subs it with [.]
        for i in range(len(str)):
            if (str[i] == "."):
                str[i] = "[.]"
            fstr += str[i]
        return fstr
