#include<iostream>
using namespace std;

class Vehicle{
    public:
    virtual void printVehicle()=0; // abstract method
    virtual ~Vehicle(){}
};

class TwoWheeler:public Vehicle{
    public:
    void printVehicle()override{
        cout<<"Two Wheeler"<<endl;
    }
};
class FourWheeler:public Vehicle{
    public:
    void printVehicle()override{
        cout<<"Four Wheeler"<<endl;
    }
};
class VehicleFactory{
    public:
    virtual Vehicle*createVehicle()=0;
    virtual ~VehicleFactory() {}
};
// Concrete Factory for Two Wheeler
class TwoWheelerFactory:public VehicleFactory{
    public:
    Vehicle*createVehicle()override{
        return new TwoWheeler();
    }
};
class FourWheelerFactory:public VehicleFactory{
    public:
    Vehicle*createVehicle()override{
        return new FourWheeler();
    }   
};
class Client{
    private:
    Vehicle*pVehicle;
    public:
    Client(VehicleFactory*factory){
        pVehicle=factory->createVehicle();
    }
    Vehicle*getVehicle(){
        return pVehicle;
    }
    ~Client(){
        delete pVehicle;
    }
};
int main(){
    VehicleFactory*twoWheelerFactory=new TwoWheelerFactory();
    Client twoWheelerClient(twoWheelerFactory);
    Vehicle*twoWheeler=twoWheelerClient.getVehicle();
    twoWheeler->printVehicle();
    delete twoWheelerFactory;

    VehicleFactory*fourWheelerFactory=new FourWheelerFactory();
    Client fourWheelerClient(fourWheelerFactory);
    Vehicle*fourWheeler=fourWheelerClient.getVehicle();
    fourWheeler->printVehicle();
    delete fourWheelerFactory;
}