#include <bits/stdc++.h>
using namespace std;
class Product1
{
public:
    std::vector<std::string> parts_;
    void ListParts() const
    {
        std::cout << "Product parts ";
        for (size_t i = 0; i < parts_.size(); i++)
        {
            if (parts_[i] == parts_.back())
            {
                std::cout << parts_[i];
            }
            else
            {
                std::cout << parts_[i] << ",";
            }
        }
        std::cout << "\n\n";
    }
};
class Builder{
    public:
    virtual ~Builder(){}
    virtual void ProductPartA()const=0;
    virtual void ProductPartB()const=0;
    virtual void ProductPartC()const=0;
};

class ConcreteBuilder1:public Builder{
    private:
    Product1*product;
    public:
    ConcreteBuilder1(){
        this->Reset();
    }
    ~ConcreteBuilder1(){
        delete product;
    }
    void Reset(){
        this->product=new Product1();
    }
    void ProductPartA()const override{
        this->product->parts_.push_back("PartA1");
    }
    void ProductPartB()const override{
        this->product->parts_.push_back("PartB1");
    }
    void ProductPartC()const override{
        this->product->parts_.push_back("PartC1");
    }
    Product1*GetProduct(){
        Product1*result=this->product;
        this->Reset();
        return result;
    }
};
class Director{
    private:
    Builder*builder;
    public:
    void set_builder(Builder*builder){
        this->builder=builder;
    }
    void BuildMinimalViableProduct(){
        this->builder->ProductPartA();
    }
    void BuildFullFeaturedProduct(){
        this->builder->ProductPartA();
        this->builder->ProductPartB();
        this->builder->ProductPartC();
    }
};
void ClientCode(Director&director){
    ConcreteBuilder1*builder=new ConcreteBuilder1();
    director.set_builder(builder);
    std::cout<<"Standard basic product\n";
    director.BuildMinimalViableProduct();
    Product1*p=builder->GetProduct();
    p->ListParts();
    delete p;
    std::cout<<"Standard full featured product\n";
    director.BuildFullFeaturedProduct();
    p=builder->GetProduct();
    p->ListParts();
    delete p;
    std::cout<<"Custom product\n";
    builder->ProductPartA();
    builder->ProductPartC();
    p=builder->GetProduct();
    p->ListParts();
    delete p;
    delete builder;
}
int main(){
    Director*director=new Director();
    ClientCode(*director);
    delete director;
}

// director, will create builder say of type1, will product having parts array, now we can decide what we want to add to parts, using the builder methods, builder -> Part1, Part2, etc, director will store reference to the builder