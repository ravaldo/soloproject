



class MemberType:
    def __init__(self, name, id=None):
        self.name = name
        self.id = id
    
    def __repr__(self):
    	return f"(MemberType_{self.id}: {self.name})"
