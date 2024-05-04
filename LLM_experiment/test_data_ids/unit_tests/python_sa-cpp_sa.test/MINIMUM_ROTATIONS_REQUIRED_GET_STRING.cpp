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
int f_gold ( string str ) {
  string tmp = str + str;
  int n = str . length ( );
  for ( int i = 1;
  i <= n;
  i ++ ) {
    string substring = tmp . substr ( i, str . size ( ) );
    if ( str == substring ) return i;
  }
  return n;
}


string f_filled ( string str ) {
  size_t tmp = str . length ( ) * 2 + str . length ( ) ;
  size_t n = str . length ( ) ;
  for ( size_t i = 1 ;
  i <= n + 1 ;
  ++ i ) if ( str == string ( tmp . substr ( i , n ) ) ) return i ;
  return n ;
}

int main() {
    int n_success = 0;
    vector<string> param0 {"vdevdNdQSopPtj","5","100010101011","tlDOvJHAyMllu","06","101","DYgtU","4","00","Dt"};
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