total_round = 10
total_steps = 1000
num_batches = 20
training_gap = 30


# judge if current step should update the NN
def isTraining(stepIndex: int) -> bool:
    if stepIndex % training_gap == 0:
        return True
    else:
        return False


def dealwithReward():
    pass


class ExpPool:
    def __init__(self) -> None:
        pass

    def query(self, num_batches):
        pass


class Agent:
    def __init__(self) -> None:
        pass

    def takeAction(self, state):
        pass

    def reset():
        pass


for i in range(total_round):
    # for each round, reset the state
    state = Agent.reset()
    for n in range(total_steps):
        # print(n)
        # take the action
        action = Agent.takeAction(state)
        # execute the action
        state, reward, done = env.transState(action)

        if done:
            break
        else:
            dealwithReward(reward)

        if isTraining(n):
            memories = ExpPool.query(num_batches)
            agent.updateNN(memories)

doSomething()
