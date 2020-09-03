import googletrans

'''
    ---------------------------------------
    Author: Runquan(Jerry) Ye
    Date: February, 2019
    ---------------------------------------
'''
def main(inputFile, outputFile="outputFile.txt"):
    #open file in the read mode
    file1 = open(inputFile, "r", encoding="utf8")

    file2 = open(outputFile, "w")

    #declare the Translator object
    translator = googletrans.Translator()

    #load all the language option
    TransOption = googletrans.LANGCODES
    
    #read the file content lines by lines
    article = file1.readlines()

    #translate article lines by lines and write into the outputFile
    for sentence in article:
        file2.write(translator.translate(sentence, dest='ja').text + "\n")

    #close the files
    file1.close()
    file2.close()



if __name__ == "__main__":
    main("inputFile.txt", "outputFile.txt")
