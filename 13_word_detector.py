import os         # to get directory content

def isWord(filename):
     with open(filename, 'r') as f:
         fileContent=f.read()

        #Detect all forms of bInOd
         if "binod" in fileContent.lower():
             return True
         else:
             return False

if __name__ == '__main__':
    dir_content = os.listdir()    #Listing the content of this folder
    print(dir_content)

    nWord=0
    for item in dir_content:
       if item.endswith('txt'):
        print(f"Detecting word in {item}")
        flag=isWord(item)
        if(flag==True):
            print(f"Found word in {item}")
            nWord+=1
        else:
            print(f"Not Found word in {item}")

print("\n")
print("Word Detector Summary:")
print(f"{nWord} files found with word you are searching")