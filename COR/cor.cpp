#include<iostream>
using namespace std;
class MoneyHandler{
    protected:
    MoneyHandler*nextHandler;
    public:
    MoneyHandler(){
        this->nextHanlder=nullptr;
    }
    void setNextHandler(MoneyHandler*next){
        nextHandler=next;
    }
    virtual void dispense(int amount)=0;
};
class ThousandHandler: public MoneyHandler{
    private:
    int numNotes;
    public:
    ThousanHanlder(int numNotes){
        this->numNotes=numNotes;
    }
    void dispense(int amount)override{
        int notesNeeded=amount/1000;
        if(notesNeeded>numNotes){
            notesNeeded=numNotes;
            numNotes=0;
        }
        else{
            numNotes-=notesNeeded;
        }
        if(notesNeeded>0)
        cout<<"Dispensing "<<notesNeeded<<" x $1000 notes\n";
        int remainingAmount=amount-(notesNeeded*1000);
        if(remainingAmount)=a
    }
}