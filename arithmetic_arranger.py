def arithmetic_arranger(problems, showAnswers =  None):
    if len(problems) > 5:
        return("Error: Too many problems.")
    firstLine = str()
    secondLine = str()
    dashLine  =str()
    answerLine = str()
    for i in problems:
        probArray = i.split()
        if probArray[1] != "+":
            if probArray[1] != "-" :
                return ("Error: Operator must be '+' or '-'.")
        if not probArray[0].isnumeric() or not probArray[2].isnumeric():
            return ("Error: Numbers must only contain digits.")
        if len(probArray[0]) > 4 or len(probArray[2])> 4:
            return "Error: Numbers cannot be more than four digits."

        if probArray[1] == '+':
            answer = str(int(probArray[0]) + int(probArray[2]))
        else:
            answer = str(int(probArray[0]) - int(probArray[2]))
            if int(answer) < 0 :
                answer = str ( int(answer) * -1)
        
        longestNumber = max(len(probArray[0]), len(probArray[2]) , len(answer)) +2
        firstLine = firstLine + (probArray[0].rjust(longestNumber)) + "    "
        secondLine = secondLine + (probArray[1] + probArray[2].rjust(longestNumber-1)) + "    "
        dashLine = dashLine + ("-" * (longestNumber)) + "    "
        if probArray[1] == '+':
            answerLine = answerLine + str(int(probArray[0]) + int(probArray[2])).rjust(longestNumber) + "    "
        else:
            answerLine = answerLine +  str(int(probArray[0]) - int(probArray[2])).rjust(longestNumber) + "    "


    firstLine = firstLine[:-4]
    secondLine = secondLine[:-4]
    dashLine = dashLine[:-4]
    answerLine = answerLine[:-4]
    if(showAnswers):
        return firstLine + "\n" + secondLine + "\n" + dashLine + "\n" + answerLine
    else:
        return firstLine + "\n" + secondLine + "\n" + dashLine


   # return arranged_problems