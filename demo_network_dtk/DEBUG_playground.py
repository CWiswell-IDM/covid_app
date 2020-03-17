import json
import random
NUM_DIGITS = 10

class NetworkPlayground():
    def __init__(self):
        self.buckets = None

    def build_buckets(self, num_buckets):
        # num_buckets is the length of the int
        all_buckets = {}
        for i in range(num_buckets):
            these_buckets = {}
            for j in range(NUM_DIGITS):
                these_buckets[j] = []
                pass
            all_buckets[i] = these_buckets
            pass
        self.buckets = all_buckets
        pass

    def rand_to_preprended_string(self, expected_length=None):
        if not expected_length:
            if self.buckets:
                expected_length = len(self.buckets)
            else:
                raise ValueError("Going to need a length here")
            pass
        max_range = NUM_DIGITS**expected_length
        my_random = random.randrange(max_range)
        my_rand_string = str(my_random)

        tmp_splits = list(my_rand_string)
        # Make sure it is prepended
        my_splits = []
        if len(my_rand_string) < expected_length: # Calculate digits to prepend
            my_diff = expected_length - len(my_rand_string)
            my_splits = []
            for i in range(my_diff):
                my_splits.append(0)
                pass
            pass
        for tmp_str in tmp_splits:
            my_splits.append(int(tmp_str))
            pass
        return my_splits

    def make_some_people(self, num_people, do_it=False):
        for n in range(num_people):
            bucket_list = self.rand_to_preprended_string()
            str_identity = "".join(str(x) for x in bucket_list)
            for i in range(len(bucket_list)):
                big_bucket = i
                little_bucket = bucket_list[i]
                self.buckets[big_bucket][little_bucket].append(str_identity)
                pass
            pass
        pass
    pass

pg = NetworkPlayground()
pg.build_buckets(5)
pg.make_some_people(1000)
#for x in range(20):
#    print(pg.rand_to_preprended_string())
with open("DEBUG_buckets.json","w") as outfile:
    json.dump(pg.buckets, outfile, indent=4, sort_keys=True)
    pass



