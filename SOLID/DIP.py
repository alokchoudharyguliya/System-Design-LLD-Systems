from abc import ABC, abstractmethod
# Interface for version control system
class IVersionControl(ABC):
    @abstractmethod
    def commit(self,message): pass
    
    @abstractmethod
    def push(self):pass
    
    @abstractmethod
    def pull(self):pass
# Git version control implementation
class GitVersionControl(IVersionControl):
    def commit(self, message):
        print(f"Commiting changes to Git with message: {message}")
        
    def push(self):
        print("Pushing changes to remote Git repository.")
        
    def pull(self):
        print("Pulling changes from remote Git repository")
        
class DevelopmentItem:
    def __init__(self,vc:IVersionControl):
        self.versionControl=vc
        
    def makeCommit(self, message):
        self.versionControl.commit(message)
        
    def performPush(self):
        self.versionControl.push()
        
    def performPull(self):
        self.versionControl.pull()
        
def main():
    git=GitVersionControl()
    team=DevelopmentItem()
    team.makeCommit("Initial Commit")
    team.performPush()
    team.performPull()
    
if __name__=="__main__":
    main()
        