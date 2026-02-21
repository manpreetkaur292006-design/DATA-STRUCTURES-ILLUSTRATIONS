
# STACK ADT IMPLEMENTATION :

# This is a program implementing the StackADT operations as mentioned.

class StackADT:  # defining the class
    def __init__(self):  # defining the init method
        self.data=[]
    def push(self,x):   # defining the push operation
        self.data.append(x)
    def pop(self):  # defining the pop operation
        if self.isEmpty(): 
            return None
        else:
            return self.data.pop()
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.data[-1]
    def size(self):
        return len(self.data)
    def isEmpty(self):
        return len(self.data)==0
    def display(self):
        return self.data
    
def main():
    stk=StackADT()
    while True:
        print("-----------------------------------")
        print("StackADT Menu ...")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. isEmpty")
        print("5. Display")
        print("6. Size")
        print("7. Exit")
        print("-----------------------------------")
        choice=input("Enter your choice :").strip()
        if choice=="1":
            value=input("Enter your value :")
            stk.push(value)
            print(value, " Pushed Successfully !")
        elif choice=="2":
            if stk.isEmpty():
                print("Stack Underflow !")
            else:
                print(stk.pop()," Popped Successfully !")
        elif choice=="3":
            if stk.isEmpty():
                print("Stack Underflow !")
            else:
                print(stk.peek()," Is the TOP of the Stack !")
        elif choice=="4":
            print("Is the Stack Empty ? : \n",stk.isEmpty())
        elif choice=="5":
            print("The Stack is :", stk.display())
        elif choice=="6":
            print("The length of the stack is : \n",stk.size())
        elif choice=="7":
            print("Exiting .... Thanks FOr visiting 🙏 !!!")
            break
        else:
            print("Invalid Input ❌ ❗❗")
            print("Please enter a valid choice !")

if __name__=="__main__":
    main()
