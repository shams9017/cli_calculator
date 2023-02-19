from services.solution_service_abc import SolutionServiceABC
import math

class SolutionService(SolutionServiceABC):
    
    def solve_expressions(self, args):
        result = self.__process_expression(args)
        return result

    def __process_expression(self,exp):
       
        try:
            # addition block
            if(exp[1] =='a'):
                return self.__process_operation("add",5,exp)

            # multiplication block
            elif(exp[1] == 'm'):
                return self.__process_operation("multiply",10,exp)
            
            # add additional operation blocks here if needed

        except Exception as e:
            print("An error has occured while solving the expression.")
            print(e.with_traceback)
    
    # private methods

    def __process_operation(self,opType, index,exp):
        firstIndexOfExpr = index
        leftBrackets = 1
        rightBrackets = 0
        expressionValues=[]

        while(leftBrackets != rightBrackets or leftBrackets == rightBrackets == 0):                   
            if(exp[firstIndexOfExpr].isdigit()):
                data = self.__eval_exp_if_digit(firstIndexOfExpr,exp)
                expressionValues.append(int(data["expression"]))
                firstIndexOfExpr = data["firstIndexOfNextExpr"]
            else:
                leftBrackets += 1
                data = self.__eval_exp_if_function(firstIndexOfExpr,exp)
                firstIndexOfExpr = data["firstIndexOfNextExpr"]
                retrievedExp = self.__process_expression(data["expression"])
                expressionValues.append(int(retrievedExp))
                rightBrackets += 1
            
            if(firstIndexOfExpr > len(exp)-1):
                rightBrackets += 1
            else:
                if(exp[firstIndexOfExpr] == ')'):
                    rightBrackets += 1                    
        
        if(opType == "add"):
            res = sum(expressionValues)
        elif(opType == "multiply"):
            res = math.prod(expressionValues)
        
        return res

    def __eval_exp_if_digit(self,index,exp):
        firstIndexOfNextExpr = None
        expDigits = ''
        for i in range(index, len(exp)):
            if(exp[i] == ' '):
                firstIndexOfNextExpr = i+1
                break
            elif((exp[i] == ')')):
                firstIndexOfNextExpr = i
                break
            expDigits += exp[i]
      
        return {"expression":expDigits, "firstIndexOfNextExpr":firstIndexOfNextExpr}

    def __eval_exp_if_function(self,index, exp):
        expChars = ''
        leftBrackets = 0
        rightBrackets = 0
        for i in range(index, len(exp)):              
            if(leftBrackets == rightBrackets):
                if(leftBrackets != 0):
                    break   
            expChars += exp[i]
            firstIndexOfNextExpr = i+2                  
            if(exp[i] == '('):
                leftBrackets += 1
            elif(exp[i] == ')'):
                rightBrackets += 1

        return {"expression":expChars, "firstIndexOfNextExpr":firstIndexOfNextExpr}



                    
