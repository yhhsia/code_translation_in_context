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
bool f_gold ( string s ) {
  int n = s . length ( );
  for ( int i = 1;
  i < n;
  i ++ ) if ( s [ i ] != s [ 0 ] ) return false;
  return true;
}


bool f_filled ( const std :: string & s ) {
  for ( int i = 1 ;
  i < s . length ( ) ;
  ++ i ) if ( s [ i ] != s [ 0 ] ) return false ;
  return true ;
}

int main() {
    int n_success = 0;
    vector<string> param0 {"","ggg","11","KoYIHns","232","10111000011101","DDDD","11","11111","ewJvixQzu"};
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