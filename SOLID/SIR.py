class BreadBaker:
    def bakeBread(self):
        print("Baking Bread")

class InventoryManager:
    def manageInventory(self):
        print("Inventory")

class SupplyOrder:
    def orderSupplies(self):
        print("Ordering")
        
class CustomerService:
    def serveCustomer(self):
        print("Serving")

class BakeryCleaner:
    def cleanBakery(self):
        print("Cleaning")

def main():
    baker=BreadBaker()
    inventoryManager=InventoryManager()
    supplyOrder=SupplyOrder()
    customerService=CustomerService()
    cleaner=BakeryCleaner()
    
    baker.bakeBread()
    inventoryManager.manageInventory()
    supplyOrder.orderSupplies()
    customerService.serveCustomer()
    cleaner.cleanBakery()
    
if __name__=="__main__":
    main()