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
int f_gold ( int n ) {
  return ( 1 << n );
}


int i = 1 ;
i <= n ;
i ++ ) : INDENT f_filled ( f_filled + ( binomialCoeff ( n , i ) * binomialCoeff ( n - i , i - 1 ) ) DEDENT f_filled ;
unsigned int binomialCoeffSum ( unsigned int n ) {
  unsigned int f_filledValue = ( 1U << n ) ;
  for ( unsigned int i =

int main() {
    int n_success = 0;
    vector<int> param0 {48,42,15,75,23,41,46,99,36,53};
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