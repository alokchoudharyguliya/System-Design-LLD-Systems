#include<iostream>
#include<string>

using namespace std;

// Forward declaration
class VendingMachine;

// Forward Declarations for concrete states
class NoCoinState;
class HasCoinState;
class DispenseState;
class SoldOutState;

class VendingState{

};

class VendingMachine{
    private:
    VendingState*currentState;
    int itemCount;
    int itemPrice;
    int insertedCoins;
    VendingState* noCoinState;
    VendingState* hasCoinState;
    VendingState* dispenseState;
    VendingState* soldOutState;

    public:
    VendingMachine(int itemCount, int itemPrice);

    void insertCoint(int coin);
    void selectItem();
    void dispense();
    void returnCount();
    void refill(int quantity);

    void printStatus();

    VendingState* getNoCoinState(){
        return noCoinState;
    }

    VendingState* getHasCoinState(){
        return hasCoinState;
    }

    VendingState* getDispenseState(){
        return dispenseState;
    }

    VendingState* getSoldOutState(){
        return soldOutState;
    }

    int getItemCount(){
        return itemCount;
    }

    void decrementItemCount(){
        return itemCount--;
    }
    
    void incrementItemCount(int count=1){
        itemCount+=count;
    }

    int getInsertedCount(){
        return insertedCount;
    }

    void setInsertedCoin(int coin){
        insertedCoins=coin;
    }

    void addCoin(int coin){
        insertedCoins+=coin;
    }

    int getPrice(){
        return this->itemPrice;
    }

    void setPrice(int itemPrice){
        this->itemPrice=itemPrice;
    }
};
