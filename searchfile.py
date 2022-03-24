def split(word):#this helper function splits the word into two strings, left and right or the '*'
    x = 0#x keeps track of index in word
    for i in word:
        if i == '*':# if found '*' save the string to the left as lquery
            lquery = word[0:x]
            rquery = word[x+1:]#and the string to the right as rquery
            break
        x+=1
    #return [lquery,rquery]#returns list of two strings
    return lquery,rquery#returns two strings

def search(word):#searches word list for word
    
    searchkey1, searchkey2 = split(word)#split returns two strings,left and right of '*'
    file = open("wordlist.txt","r")#opens wordlist
    answer = list()#answer's stored in list
    while True :#keeps looping until the end of file
        entry = file.readline()#entry = next line of file
        if entry:
            searchentry1 = entry[0:len(searchkey1)]#splits entry into left and right side, same size as the searchkeys
            searchentry2 = entry[len(entry)-1-len(searchkey2):len(entry)-1]
            if ((searchentry1 == searchkey1) and (searchentry2 == searchkey2)#if searchkeys and entries are equal,
                 and (len(entry) > (len(searchentry1)+len(searchentry2)))):#and the len(entry) > searchkeys, we found an answer
                answer.append(entry)#appends entry to list of answers
        else: break#if not entry, we've reached the end of the file, and we break
    file.close()#closes file
    return answer
