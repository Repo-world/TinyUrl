class URL:

    def __init__(self, userUrl, tinyUrl="helloworld", upTime=0):
        self.userUrl = userUrl      
        self.tinyUrl = tinyUrl   
        self.upTime = upTime      

    def display_details(self):
        print(f"Car Details: {self.year} {self.make} {self.model}")

    def create_tinyUrl(inputUrl):
        print("Creating tiny url")
        print(inputUrl)
        
    def get_user_url(self):
        pass