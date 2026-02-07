// Focuses on inheriting from both adaptee and the target and then bringing the adaptee inside the target code
#include<bits/stdc++.h>
using namespace std;
class Target{
    public:
    virtual ~Target()=default;
    virtual std::string Request()const{
        return "Target: the default target's behavior.";
    }
};

class Adaptee{
    public:
    std::string SpecificRequest()const{
        return ".eetpadA eht fo roivaheb laicepS";
    }
};
class Adapter:public Target, public Adaptee{
    public:
    Adapter(){}
    std::string Request()const override{
        std::string to_reverse=SpecificRequest();
        std::reverse(to_reverse.begin(),to_reverse.end());
        return "Adapter:(Translated)"+to_reverse;
    }
};
void ClientCode(const Target*target){
    std::cout<<target->Request();
}
int main(){
    std::cout<<"Client: I can work just fine with the Target Interface";
    Target*target=new Target;
    ClientCode(target);
    std::cout<<"\n\n";
    Adaptee*adaptee=new Adaptee;
    std::cout<<"Client : Adaptee class has a weird interface. See I don't understand it\n";
    std::cout<<"Adaptee "<<adaptee->SpecificRequest();
    std::cout<<"\n\n";
    std::cout<<"Client: But I can work with it via the Adapter\n";
    Adapter*adapter=new Adapter;
    ClientCode(adapter);
    std::cout<<endl;
    delete target;
    delete adaptee;
    delete adapter;
    return 0;
}