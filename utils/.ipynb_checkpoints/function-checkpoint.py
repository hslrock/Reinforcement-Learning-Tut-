def set_mu_policy(grid):
    policy_mu=grid.policy.copy()

    mid_hpoint=(policy_mu.shape[1]-1)/2
    mid_wpoint=(policy_mu.shape[2]-1)/2
    for i in range(policy_mu.shape[1]):
        for j in range(policy_mu.shape[2]):

            if j < mid_wpoint:
                if i < mid_hpoint:
                    policy_mu[0:4,i,j]=0.0,0.5,0.0,0.5
                elif i == mid_hpoint:
                    policy_mu[0:4,i,j]=0.0,0.5,0.0,0.5
                elif i > mid_hpoint:
                    policy_mu[0:4,i,j]=0.25,0.25,0.25,0.25
                if i==0:
                    policy_mu[0:4,i,j]=0.0,0.0,0.0,1.0
                elif i==policy_mu.shape[1]-1:
                    policy_mu[0:4,i,j]=0.0,0.0,1.0,0.0

            elif j == mid_wpoint:

                if i < mid_hpoint:
                    policy_mu[0:4,i,j]=0.5,0.0,0.0,0.5
                elif i == mid_hpoint:
                    policy_mu[0:4,i,j]=0.25,0.25,0.25,0.25
                elif i > mid_hpoint:
                    policy_mu[0:4,i,j]=0.0,0.5,0.5,0.0
                if i==0:
                    policy_mu[0:4,i,j]=0.0,0.0,0.0,1.0
                elif i==policy_mu.shape[1]-1:
                    policy_mu[0:4,i,j]=0.0,0.0,1.0,0.0
            elif j > mid_wpoint :

                if i < mid_hpoint:
                    policy_mu[0:4,i,j]=0.25,0.25,0.25,0.25
                elif i == mid_hpoint:
                    policy_mu[0:4,i,j]=0.0,0.5,0.5,0.0
                elif i > mid_hpoint:
                    policy_mu[0:4,i,j]=0.0,0.5,0.5,0.0
                if i==0:
                    policy_mu[0:4,i,j]=0.0,0.0,0.0,1.0
                elif i==policy_mu.shape[1]-1:
                    policy_mu[0:4,i,j]=0.5,0.0,0.0,0.5
            if j==0:

                if i < mid_hpoint:
                    policy_mu[0:4,i,j]=1.0,0.0,0.0,0.0
                elif i == mid_hpoint:
                    policy_mu[0:4,i,j]=1.0,0.0,0.0,0.0
                elif i > mid_hpoint:
                    policy_mu[0:4,i,j]=1.0,0.0,0.0,0.0
                if i==0:
                    policy_mu[0:4,i,j]=0.5,0.0,0.0,0.5
                elif i==policy_mu.shape[1]-1:
                    policy_mu[0:4,i,j]=0.5,0.0,0.5,0.0

            elif j==policy_mu.shape[2]-1:

                if i < mid_hpoint:
                    policy_mu[0:4,i,j]=0.0,1.0,0.0,0.0
                elif i == mid_hpoint:
                    policy_mu[0:4,i,j]=0.0,1.0,0.0,0.0
                elif i > mid_hpoint:
                    policy_mu[0:4,i,j]=0.0,1.0,0.0,0.0
                if i==0:
                    policy_mu[0:4,i,j]=0.0,0.5,0.0,0.5
                elif i==policy_mu.shape[1]-1:
                    policy_mu[0:4,i,j]=0.0,0.5,0.5,0.0
    return policy_mu
