class Adoption_Pool(): 
    """
    Adoption class for defining state of network adoption
    This is class is on the subpopulation level, where each state maitains a count of members
    and a mean of reputation in the addoption funnel
    and threshold transition value
    """  
    def __init__(self, pool):
        """
        Adoption class initialized without a preset reputation
        Unaware state
        """        

        self.state = {'unaware': {'pool': pool, 'reputation': None,},
                      'aware': {'pool': 0, 'reputation': 0},
                      'adopted': {'pool': 0, 'reputation': 0},
                      'loyal': {'pool': 0, 'reputation': 0},
                      'churned': {'pool': 0, 'reputation': 0},
                    }

        self.threshold = 0.5

 # when signal reaches above filtered threshold       
    def apply_signal(self, signal):
        """
        Apply signal to reputation metric
        FILTER HERE OR BEFORE
        """  
        if self.state['unaware']['reputation'] is None:
            self.state['unaware']['reputation'] = 0

        if signal == 0: 
            self.state['unaware']['reputation']  =  0
        elif signal > 0: 
            self.state['unaware']['reputation'] +=  1

        elif signal < 0: 
            self.state['unaware']['reputation'] -=  1
        
            
        
    def apply_experience(self, experience):
        """
        Apply experience to reputation metric
        """  
        if experience > 0: 
            self.reputation +=  1
        
        if experience < 0: 
            self.reputation -=  1
            
    
    def calculate_drip(self, delta):
        """
        Calculate drip for each state
        """  
        for key, value in self.state.items():
            if value['reputation'] is not None:
                if value['reputation'] > self.threshold:
                    value['drip'] = delta * (value['reputation'] * value['pool'] - self.threshold * value['pool']) / value['reputation'] 


                if value['reputation'] < self.threshold:
                    value['neg_drip'] = - delta * (value['reputation'] * value['pool'] - self.threshold * value['pool'])
        

    def update_pools(self, delta):
        """
        Update pool from drip for each state
        """  
        for key, value in self.state.items():
            # print(key)
            if 'drip' in value.keys():
                
                
                if key == 'unaware':
  
                    self.state['aware']['reputation'] = ((self.state['aware']['pool'] * self.state['aware']['reputation']) + (delta * value['reputation'] *  value['drip'])) / (self.state['aware']['pool'] + value['drip'])
                    value['reputation'] = ((value['pool'] * value['reputation']) - (delta * value['reputation'] *  value['drip'])) / (value['pool'] - value['drip'])
                    value['pool'] -= value['drip']
                    self.state['aware']['pool'] += value['drip']

                elif key == 'aware':
                    self.state['adopted']['reputation'] = ((self.state['adopted']['pool'] * self.state['adopted']['reputation']) + (delta * value['reputation'] *  value['drip'])) / (self.state['adopted']['pool'] + value['drip'])
                    value['reputation'] = ((value['pool'] * value['reputation']) - (delta * value['reputation'] *  value['drip'])) / (value['pool'] - value['drip'])

                    value['pool'] -= value['drip']
                    self.state['adopted']['pool'] += value['drip']
                    
                elif key == 'adopted':
                    self.state['loyal']['reputation'] = ((self.state['loyal']['pool'] * self.state['loyal']['reputation']) + (delta * value['reputation'] *  value['drip'])) / (self.state['loyal']['pool'] + value['drip'])
                    value['reputation'] = ((value['pool'] * value['reputation']) - (delta * value['reputation'] *  value['drip'])) / (value['pool'] - value['drip'])

                    value['pool'] -= value['drip']
                    self.state['loyal']['pool'] += value['drip']

                    
                elif key == 'churned':
                    self.state['adopted']['reputation'] = ((self.state['adopted']['pool'] * self.state['adopted']['reputation']) + (delta * value['reputation'] *  value['drip'])) / (self.state['adopted']['pool'] + value['drip'])
                    value['reputation'] = ((value['pool'] * value['reputation']) - (delta * value['reputation'] *  value['drip'])) / (value['pool'] - value['drip'])

                    value['pool'] -= value['drip']
                    self.state['adopted']['pool'] += value['drip']
                
                
                value['drip'] = 0
                
            if 'neg_drip' in value.keys():
                
                                  
                if key == 'adopted':
                    self.state['churned']['pool'] += value['neg_drip']
                    self.state['churned']['reputation'] -= delta * value['reputation']
                    value['pool'] -= value['neg_drip']
                    value['neg_drip'] = 0
                
                elif key == 'loyal':
                    self.state['adopted']['pool'] += value['neg_drip']
                    self.state['adopted']['reputation'] -= delta * value['reputation']
                    value['pool'] -= value['neg_drip']

                    value['neg_drip'] = 0
                

    
    def determine_state(self, reputation=None, threshold= None):
        """
        Uses reputation and threshold to determine state
        """  
        if threshold is None:
            threshold = self.threshold
            
        if reputation is None:
            reputation = self.reputation
        
        if reputation > threshold:
            if self.state == 'aware':
                self.state = 'adopted'
                
            elif self.state == 'adopted':
                self.state = 'loyal'
                       
                
        if reputation < threshold:
            if self.state == 'adopted':
                self.state = 'churned'
        
            elif self.state == 'loyal':
                self.state = 'adopted'
                
    def set_threshold(self, default_threshold=0.5, ext_threshold=None):
        """
        Set threshold to current state
        """  
        if ext_threshold is not None:
            self.threshold = ext_threshold
        if self.state == 'unaware':
            if ext_threshold is not None:
                self.threshold = ext_threshold
            else:
                self.threshold = default_threshold
                
        elif self.state == 'aware':
            if ext_threshold is not None:
                self.threshold = ext_threshold
            else:
                self.threshold = default_threshold
                       
        elif self.state == 'adopted':
            if ext_threshold is not None:
                self.threshold = ext_threshold
            else:
                self.threshold = default_threshold
                
        elif self.state == 'loyal':
            if ext_threshold is not None:
                self.threshold = ext_threshold
            else:
                self.threshold = default_threshold       
                
        elif self.state == 'churned':
            if ext_threshold is not None:
                self.threshold = ext_threshold
            else:
                self.threshold = default_threshold
        
    def __str__(self):
        """
        Print all attributes of an event
        """
        return str(self.__class__) + ": " + str(self.__dict__)