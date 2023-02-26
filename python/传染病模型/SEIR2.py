import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


class WordleDynamic(object):
    def __init__(self) -> None:
        """
        Dynamic:
        twitters = twitter_rate x player
        没玩过的用户: playing_t1 = playing x (1 - leaving_rate) + twitters x new_player_rate x (new_users / all_users)
        正在玩的用户: new_users_t1 = new_users - new_playing + refresh_rate x played x twitter
        玩腻了的用户: played_t1 = played + new_played - new_refresh
        """
        # need to be optimized
        self.all_users = 4500000
        self.twitter_rate = 0.25
        self.twitter_spread_rate = 3.3
        self.new_player_rate = 0.2
        self.old_player_rate = 0.1
        self.leaving_rate = 0.1
        # status
        self._player = 0
        self._played = 0
        self._new_users = self.all_users
        self._twitters = 0
        self._played_and_xinxian = 0

    def initialize(self, player:int) -> None:
        self._player = player
        self._played = 0
        self._new_users = self.all_users - player
        return None

    def update_status(self) -> None:
        current_tired = self._player * self.leaving_rate
        current_new_player = (
            min(self._twitters * self.twitter_spread_rate, self.all_users)
            * (self._new_users / self.all_users)
            * self.new_player_rate
        )
        self._new_users -= current_new_player
        current_refreshed = (
            min(self._twitters * self.twitter_spread_rate, self.all_users)
            * (self._played / self.all_users)
            * self.old_player_rate
        )
        self._new_users += current_refreshed
        self._player += current_new_player - current_tired
        self._played += current_tired
        self._played -= current_refreshed
        self._twitters = self._player * self.twitter_rate
        return None

    @property
    def twitters(self) -> None:
        return self._twitters

def sigmoid(X,useStatus):
    if useStatus:
        return 1.0 / (1 + np.exp(-float(X)))
    else:
        return float(X)

filename = 'c_wordle_一元.csv'
df = pd.read_csv(filename)
a = np.array(df["2 tries"])
print(a)
m=np.median(a)
print(m)
result=[]
for d in a:
    result.append(sigmoid(d-m,1))
print(result)

wordle = WordleDynamic()
wordle.initialize(10)
tws = []
x=200
R=359+x
num=0
add_spread_rate=0.005
t=300
for i in range(R+60):
    if i >= x and i<R:
        wordle.twitter_rate = (df['Difficulty'][i - x]+(result[i-x] - 0.5) / 10)/10
        # wordle.twitter_rate = () + wordle.twitter_rate
    if i > 335 and i<=400:
        t+=0.9
        add_spread_rate*=(300/t)
        wordle.twitter_spread_rate+=add_spread_rate
        # print("spread_rate:",wordle.twitter_spread_rate)
    if i>400:
        wordle.twitter_spread_rate=3.35
        wordle.old_player_rate = 0.1005
        wordle.leaving_rate = 0.093
    if i > 550:
        wordle.twitter_spread_rate = 3.2
    wordle.update_status()
    tws.append(wordle.twitters)
    # if i>=R:
        # print(f"{i} - {wordle.twitters} - {wordle._played}")
    print(f"{i} - {wordle.twitters} - {wordle._played}")
x=x-7
tws = tws[x:x+359+60]
plt.plot(range(len(df['Number of  reported results'])), df['Number of  reported results'], "-")
plt.plot(range(len(tws)), tws, "-")
print(len(tws))
plt.show()