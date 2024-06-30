import numpy as np #this is the numpy library which we have to include 
np.random.seed(0)
import sys
def main():    
 #seeding the numpy library with seed 0

    def get_input():
        return sys.stdin.readline().rstrip()
    # the function give_index_of_word_from_state will generate a random number and returns the index of the word which needs to append the final sentence
    def give_index_of_word_from_state(current_state, cdf_of_B):
        r = np.random.random()
        bin_idx = binary_search_logn(cdf_of_B[current_state], r)
        while(cdf_of_B[current_state][bin_idx]==0):
            bin_idx = bin_idx + 1
        return bin_idx
    

    # the function binary_search_logn will return the index of give target data from the array numbers in log(n) time
    def binary_search_logn(numbers, target_data):
        start=0
        end=len(numbers)-1
        output_index = -1
        while start <= end:
            mid = start + (end - start) // 2
            if numbers[mid] >= target_data:
                output_index = mid
                end = mid - 1
            else:
                start = mid + 1
        return output_index



    # the function give_index_of_next_state will generate a random number and returns the index of the next state 
    def give_index_of_next_state(currentstate, cdf_of_A):
        rndm = np.random.random()
        bin_idx = binary_search_logn(cdf_of_A[currentstate], rndm)
        while(cdf_of_A[currentstate][bin_idx]==0):
            bin_idx = bin_idx + 1
        return bin_idx
    
    # the function give_index_of_initial_state will generate a random number and returns the index of the state (initial state)
    def give_index_of_initial_state(state_pi):
        random_num = np.random.random()
        summ = 0
        if(random_num==0):
            for indx in range(0, len(state_pi)):
                if(state_pi[indx]>0):
                    return indx
            return len(state_pi) - 1
        for idxx in range(0, len(state_pi)):
            summ = summ + state_pi[idxx]
            if(random_num<=summ):
                return idxx
        return len(state_pi) - 1

    m, n, t1 = map(int, get_input().split()) #taking input m,n,t1 from console
    A = [] 
    B = []
    A_cdf = []
    B_cdf = []
    pi = list(map(float, get_input().split())) #assigning pi from input


#assigning A
    for i in range(m):
        A_rows = list(map(float,  get_input().split()))
        A.append(A_rows)
        t = []
        sss = 0
        for i in range(m):
            sss = sss + A_rows[i]
            t.append(sss)
        A_cdf.append(t)

#assigning B
    for i in range(m):
        B_rows = list(map(float,  get_input().split()))
        B.append(B_rows)
        tt = []
        sms = 0
        for i in range(n):
            sms = sms + B_rows[i]
            tt.append(sms)
        B_cdf.append(tt)


    idx = 0
    curr_state = 0
    final_answer = []
    for idx in range(t1):
        if(idx==0):
            curr_state = give_index_of_initial_state(pi) #judging the initial state (starting word for the sentence)
        else:
            curr_state = give_index_of_next_state(curr_state, A_cdf) #next state from current state


        word_index = give_index_of_word_from_state(curr_state, B_cdf) #finding the word number 
        final_answer.append(word_index) #generating the sentence 

    print(*final_answer) #printing the final generated sentence to the console
    # end_time = time.time()
    # execution_time = end_time - start_time
    # print("Execution time:", execution_time, "seconds")

if __name__ == "__main__": #ensuring that file only runs directly to terminal
    main() #the whole main function which contains other function too
