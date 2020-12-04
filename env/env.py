import numpy as np
import random

class Grid_game(object):
    def __init__(self,grid_x,grid_y,initial_pos=[2,0],TERMIN_STATE_POS =[[0,0],[3,3]]):
        
        self.initial_pos=initial_pos
        self.TERMINAL_STATE_POS=TERMIN_STATE_POS
        self.grid_x=grid_x
        self.grid_y=grid_y
        
        self.reset()
        
        
        self.policy=np.zeros((4,grid_x,grid_y))+0.25
        for i in self.TERMINAL_STATE_POS:

            self.policy[0:4,i[0],i[1]]=0
        self.vst=np.zeros((grid_x,grid_y))   #Action State Value
        
        self.ast=np.zeros((4,grid_x,grid_y))
        
        self.fix_reward_val=-1
        
        class Agent(object):
            def __init__(self,initial_pos,max_grid=grid_x):
                self.oldpos=initial_pos[:]
                self.curpos=initial_pos[:]
                self.max_grid=max_grid
            def north(self):
                self.curpos[0]-=1
            def south(self):
                self.curpos[0]+=1
            def east(self):
                self.curpos[1]+=1
            def west(self):
                self.curpos[1]-=1
                
        self.grid_x=grid_x
        self.grid_y=grid_y
        self.player=Agent(self.initial_pos)        
        self.update_state()
        self.state=False
    def reset(self):
        self.current_state=np.zeros((self.grid_x,self.grid_y))
        
    def update_state(self):
        self.reset()
        self.current_state[self.player.curpos[0]][self.player.curpos[1]]=1
    def set_pos(self,y,x):
        self.player.curpos=[y,x]
        self.update_state()
        self.state=self.end_condition()
    def check_valid(self):
        if self.player.curpos[0]==self.grid_y:
            self.player.curpos[0]=self.grid_y-1
        if self.player.curpos[0]==-1:
            self.player.curpos[0]=0
        if self.player.curpos[1]==self.grid_x:
            self.player.curpos[1]=self.grid_x-1
        if self.player.curpos[1]==-1:
            self.player.curpos[1]=0
    def end_condition(self):
        for state_pos in self.TERMINAL_STATE_POS:
            if self.player.curpos== state_pos:
                return True
        return False
    def transition(self,action=None):

        move = {  0: self.player.north,
                          1: self.player.south,
                        2:self.player.east,
                        3:self.player.west}
        if action==None:

            x,y=self.player.curpos
            action_index=random.choice(list(enumerate(self.policy[0:4,x,y])))[0]
            self.player.oldpos=self.player.curpos
            move[action_index]()
            action=action_index
        else:
            move[action]()
        self.check_valid()
        self.update_state()
        self.state=self.end_condition()
        return self.state,self.player.curpos,self.fix_reward_val,action
            
        
    def get_asv():
        return self.ast
    def get_vst():
        return self.vst