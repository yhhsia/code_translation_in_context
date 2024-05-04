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
int f_gold ( int m, int n ) {
  int dp [ n ] = {
    1 };
    dp [ 0 ] = 1;
    for ( int i = 0;
    i < m;
    i ++ ) {
      for ( int j = 1;
      j < n;
      j ++ ) {
        dp [ j ] += dp [ j - 1 ];
      }
    }
    return dp [ n - 1 ];
  }
  

int f_filled ( int p , int q ) {
  int dp [ q ] ;
  std :: fill ( dp , dp + q , 1 ) ;
  for ( int i = p - 1 ;
  i >= 0 ;
  -- i ) for ( int j = 1 ;
  j < q ;
  ++ j ) dp [ j ] += dp [ j - 1 ] ;
  return dp [ q - 1 ] ;
}

int main() {
    int n_success = 0;
    vector<int> param0 {73,70,53,80,9,38,41,80,42,54};
    vector<int> param1 {75,5,62,70,59,48,49,72,52,1};
    for(int i = 0; i < param0.size(); ++i)
    {
        if(f_filled(param0[i],param1[i]) == f_gold(param0[i],param1[i]))
        {
            n_success+=1;
        }
    }
    cout << "#Results:" << " " << n_success << ", " << param0.size();
    return 0;
}