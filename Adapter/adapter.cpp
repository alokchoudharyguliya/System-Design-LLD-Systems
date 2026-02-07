#include<bits/stdc++.h>
using namespace std;

class Target
{
public:
    virtual ~Target() = default;
    virtual std::string Request() const
    {
        return "Target";
    }
};
class Adaptee
{
public:
    std::string SpecificRequest() const
    {
        return ".eetpadA eht fo roivaheb laicepS";
    }
};
class Adapter : public Target
{
    private:
    Adaptee *adaptee_;

public:
    Adapter(Adaptee *adaptee) : adaptee_(adaptee) {}
    std::string Request() const override
    {
        std::string to_reverse = this->adaptee_->SpecificRequest();
        std::reverse(to_reverse.begin(), to_reverse.end());
        return "Adapter Translated " + to_reverse;
    }
};

void ClientCode(const Target *target)
{
    std::cout << target->Request();
}
int main()
{
    std::cout << "Client I can work just fine with Target objects(those entites with whom the client is comfortable)";
    Target *target = new Target;
    ClientCode(target);
    std::cout << "\n\n";
    Adaptee *adaptee = new Adaptee;
    std::cout << "Adaptee comes into the game, now i want adaptee to behave just like Target to ensure compatibility";
    std::cout << "Adaptee" << adaptee->SpecificRequest();
    std::cout << "\n\n";
    std::cout<<"After going through the adapter";
    Adapter *adapter = new Adapter(adaptee);
    ClientCode(adapter);
    std::cout << "\n";
}
