// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <fstream>
#include <iomanip>
#include <bits/stdc++.h>
using namespace std;
int f_gold ( int N ) {
  return ceil ( log2 ( N + 1 ) ) - 1;
}


static int f_filled ( int N ) {
  return static_cast < int > ( ceil ( log ( N + 1 ) / log ( 2 ) ) ) - 1 ;
}

int main() {
    int n_success = 0;
    vector<int> param0 {65,94,52,31,9,1,41,98,45,24};
    for(int i = 0; i < param0.size(); ++i)
    {
        if(f_filled(param0[i]) == f_gold(param0[i]))
        {
            n_success+=1;
        }
    }
    cout << "#Results:" << " " << n_success << ", " << param0.size();
    return 0;
}