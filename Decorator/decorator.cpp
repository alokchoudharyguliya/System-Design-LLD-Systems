#include<bits/stdc++.h>
using namespace std;
class Coffee{
    public:
    virtual string getDescription();
    virtual double getCost();
};

class PlainCoffee:public Coffee{
    public:
    string getDescription()override{
        return "Plain Coffee";
    }
    double getCost override{
        return 2.0;
    }
};
class CoffeeDecorator:public Coffee{
    protected:
     Coffee* decoratedCoffee;
     public:
     CoffeeDecorator(Coffee*coffee):decoratedCoffee(coffee){}
     virtual string getDescription() const override{
        return decoratedCoffee->getDescription();
     }
     virtual double getCost()const override{
        return decoratedCoffee->getCost();
     }
};
class MilkDecorator:public CoffeeDecorator{
    public:
    MilkDecorator(Coffee*coffee):CoffeeDecorator(coffee){}
    string getDescription()const override{
        return CoffeeDecorator::getDescription()+",Milk";
    }
    double getCost()const override{
        return CoffeeDecorator::getCost()+0.5;
    }
};
class SugarDecorator:public CoffeeDecorator{
    public:
    SugarDecorator(Coffee*coffee):CoffeeDecorator(coffee){}
    string getDescription()const override{
        return CoffeeDecorator::getDescription()+", Sugar";
    }
    double getCost()const override{
        return CoffeeDecorator::getCost()+0.2;
    }
};
int main(){
    Coffee*coffee=new PlainCoffee();
    cout<<"Description "<<coffee->getDescription()<<endl;
    cout<<"Cost $"<<coffee->getCost()<<endl;

    Coffee*milkCoffee=new MilkDecorator(new PlainCoffee());
    cout<<"\nDescription"<<milkCoffee->getDescription()<<endl;
    cout<<"Cost $"<<milkCoffee->getCost()<<endl;

    Coffee*sugarMilkCoffee=new SugarDecorator(new MilkDecorator(new PlainCoffee()));
    cout<<"\n Description "<<sugarMilkCoffee->getDescription()<<endl;
    cout<<"Cost $"<<sugarMilkCoffee->getCost()<<endl;
    delete coffee;
    delete milkCoffee;
    delete sugarMilkCoffee;
    return 0;
}
