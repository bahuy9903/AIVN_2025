#Ex1 - Page 31 - AIVN
# Input: tp,fp,fn
# Output: precision, recall, f1-score
def calculate(tp,fp,fn):
    for name, value in [("tp",tp),("fp",fp),("fn",fn)]:
        if not isinstance(value, int):
            print(f"{name} must be int")
            return None
    for name, value in [("tp",tp),("fp",fp),("fn",fn)]:
        if value < 0:
            print(f"{name} must be greater than or equal zero")
            return None
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1_score = 2*(precision*recall)/(precision+recall)
    print(f"precision is {precision}")
    print(f"recall is {recall}")
    print(f"f1_score is {f1_score}")
    

def main():
    calculate(tp=2,fp=3,fn=4)
    calculate(tp="a",fp=3,fn=4)   
    calculate(tp=2,fp="a",fn=4)   
    calculate(tp=2,fp=4,fn="a")       
    calculate(tp=2.1,fp=3,fn=0)   
    
if __name__ == "__main__":
    main()