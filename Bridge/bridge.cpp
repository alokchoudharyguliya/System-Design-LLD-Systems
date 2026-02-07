#include<bits/stdc++.h>
#include<string>
// using std::string;
// using namespace std;
class Implementation{
    public:
    virtual ~Implementation(){}
    virtual std::string OperationImplementation()const = 0;
};

class ConcreteImplementationA:public Implementation{
public:
std::string OperationImplementation()const override{
    return "ConcreteImplementationA";
}   
};
class ConcreteImplementationB:public Implementation{
    public:
std::string OperationImplementation()const override{
    return "ConcreteImplementationB";
}
};
class Abstraction{
    protected:
    Implementation*implementation_;
    public:
    Abstraction(Implementation*implementation){
        this->implementation_=implementation;
    }
    virtual ~Abstraction(){}
    virtual std::string Operation()const{
        return "Abstraction"+this->implementation_->OperationImplementation();
    }
};
class ExtendedAbstraction:public Abstraction{
    public:
    // ExtendedAbstraction(Implementation*implementation){
    //     Abstraction(implementation);
    // }
    ExtendedAbstraction(Implementation*implementation):Abstraction(implementation){}
    std::string Operation()const override{
        return "ExtendedAbstraction"+this->implementation_->OperationImplementation();
    }
};
void ClientCode(const Abstraction&abstraction){
    std::cout<<abstraction.Operation();
}
int main(){
    Implementation*implementation=new ConcreteImplementationA;
    Abstraction*abstraction=new Abstraction(implementation);
    ClientCode(*abstraction);

    std::cout<<std::endl;
    delete implementation;
    delete abstraction;

    implementation=new ConcreteImplementationB;
    abstraction=new ExtendedAbstraction(implementation);
    ClientCode(*abstraction);

    delete implementation;
    delete abstraction;
    return 0;
}
