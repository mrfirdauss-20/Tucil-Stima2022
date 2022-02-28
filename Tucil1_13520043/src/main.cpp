#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include <chrono>

using namespace std;
using namespace std::chrono;

void printVec(vector<vector <char>> vect){
    for(int i=0;i<vect.size();i++){
        for(int j=0;j<vect[i].size();j++){
            cout<<vect[i][j]<<" ";
        }
        cout<<endl;
    }
    cout<<"\n";
}

void makeAlp(vector<vector <char>> *vect){
    for(int i=0;i<(*vect).size();i++){
        for(int j=0;j<(*vect)[i].size();j++){
            (*vect)[i][j]='-';
        }
    }
}
bool cekKiri(int row, int col, string word, vector<vector<char>> arrOfAlp){
    bool check = true;

    int k = 0;
    vector<vector <char>> checker (arrOfAlp.size(), vector<char> (arrOfAlp[0].size()));
    makeAlp(&checker);
    int i=row;
    int j=col;
    
    while(k<word.length() and check){
        if(arrOfAlp[i][j]==word[k]){
            checker[i][j]=arrOfAlp[i][j];
            j--;
            k++;
        }else{
            check=false;
        }
    }

    if(check){
        printVec(checker);
    }

    return check;
}

bool cekKiriAtas(int row, int col, string word, vector<vector<char>> arrOfAlp){
    bool check = true;

    int k = 0;
    vector<vector <char>> checker (arrOfAlp.size(), vector<char> (arrOfAlp[0].size()));
    makeAlp(&checker);
    
    int i=row;
    int j=col;
    
    while(k<word.length() and check){
        if(arrOfAlp[i][j]==word[k]){
            checker[i][j]=arrOfAlp[i][j];
            j--;
            i--;
            k++;
        }else{
            check=false;
        }
    }

    if(check){
        printVec(checker);
    }

    return check;
}

bool cekKiriBawah(int row, int col, string word, vector<vector<char>> arrOfAlp){
    bool check = true;

    int k = 0;
    vector<vector <char>> checker (arrOfAlp.size(), vector<char> (arrOfAlp[0].size()));
    makeAlp(&checker);
    
    int i=row;
    int j=col;
    
    while(k<word.length() and check){
        if(arrOfAlp[i][j]==word[k]){
            checker[i][j]=arrOfAlp[i][j];
            j--;
            i++;
            k++;
        }else{
            check=false;
        }
    }

    if(check){
        printVec(checker);
    }

    return check;
}

bool cekKanan(int row, int col, string word, vector<vector<char>> arrOfAlp){
    bool check = true;

    int k = 0;
    vector<vector <char>> checker (arrOfAlp.size(), vector<char> (arrOfAlp[0].size()));
    makeAlp(&checker);
    
    int i=row;
    int j=col;
    while(k<word.length() and check){
        if(arrOfAlp[i][j]==word[k]){
            checker[i][j]=arrOfAlp[i][j];
            j++;
            k++;
        }else{
            check=false;
        }
    }

    if(check){
        printVec(checker);
    }

    return check;
}

bool cekKananAtas(int row, int col, string word, vector<vector<char>> arrOfAlp){
    bool check = true;

    int k = 0;
    vector<vector <char>> checker (arrOfAlp.size(), vector<char> (arrOfAlp[0].size()));
    makeAlp(&checker);
    
    int i=row;
    int j=col;
    
    while(k<word.length() and check){
        if(arrOfAlp[i][j]==word[k]){
            checker[i][j]=arrOfAlp[i][j];
            j++;
            i--;
            k++;
        }else{
            check=false;
        }
    }

    if(check){
        printVec(checker);
    }

    return check;
}

bool cekKananBawah(int row, int col, string word, vector<vector<char>> arrOfAlp){
    bool check = true;

    int k = 0;
    vector<vector <char>> checker (arrOfAlp.size(), vector<char> (arrOfAlp[0].size()));
    makeAlp(&checker);
    
    int i=row;
    int j=col;
    
    while(k<word.length() and check){
        if(arrOfAlp[i][j]==word[k]){
            checker[i][j]=arrOfAlp[i][j];
            j++;
            i++;
            k++;
        }else{
            check=false;
        }
    }

    if(check){
        printVec(checker);
    }

    return check;
}


bool cekBawah(int row, int col, string word, vector<vector<char>> arrOfAlp){
    bool check = true;

    int k = 0;
    vector<vector <char>> checker (arrOfAlp.size(), vector<char> (arrOfAlp[0].size()));
    makeAlp(&checker);
    
    int i=row;
    int j=col;
    
    while(k<word.length() and check){
        if(arrOfAlp[i][j]==word[k]){
            checker[i][j]=arrOfAlp[i][j];
            i++;
            k++;
        }else{
            check=false;
        }
    }

    if(check){
        printVec(checker);
    }

    return check;
}

bool cekAtas(int row, int col, string word, vector<vector<char>> arrOfAlp){
    bool check = true;

    int k = 0;
    vector<vector <char>> checker (arrOfAlp.size(), vector<char> (arrOfAlp[0].size()));
    makeAlp(&checker);
    
    int i=row;
    int j=col;
    
    while(k<word.length() and check){
        if(arrOfAlp[i][j]==word[k]){
            checker[i][j]=arrOfAlp[i][j];
            i--;
            k++;
        }else{
            check=false;
        }
    }

    if(check){
        printVec(checker);
    }

    return check;
}

int main(){
    string input;
    cout<<"Masukkan namafile: ";
    cin>>input;
    ifstream f(input);
    string str;
    vector<string> arrOfWords;
    vector<vector<char>> arrOfAlp;
    int i=0;
    while(getline(f,str)&&str!=""){
        int col=0;
        vector<char> row;
        row=vector<char> ((str.length()+1)/2);
        for(int j=0; j<str.length();j++){
            if(str[j]!=' '){
                row[col]=str[j];
                col++;
            }
        }
        arrOfAlp.push_back(row);
    }

    //printVec(arrOfAlp);
    while(getline(f,str)){
        arrOfWords.push_back(str);
    }
    
    f.close();
    auto start = high_resolution_clock::now();

    for(int i=0;i<arrOfWords.size();i++){
        int itc=0;
        int itr =0;
        bool found = false;
        while(itr<arrOfAlp.size() and !found){
            if(arrOfAlp[itr][itc]==arrOfWords[i][0]){
                if(itc+1>=arrOfWords[i].size()){
                    found = cekKiri(itr,itc,arrOfWords[i],arrOfAlp);
                    if(itr+1>=arrOfWords[i].length() && !found){
                        found=cekKiriAtas(itr,itc,arrOfWords[i],arrOfAlp);
                    }

                    if(arrOfAlp.size()-itr>arrOfWords[i].length() && !found){
                        found=cekKiriBawah(itr,itc,arrOfWords[i],arrOfAlp);
                    }
                }
                if(arrOfAlp[itr].size()-itc>=arrOfWords[i].length() && !found){
                    found = cekKanan(itr,itc,arrOfWords[i],arrOfAlp);
                    if(itr+1>=arrOfWords[i].length() && !found){
                        found=cekKananAtas(itr,itc,arrOfWords[i],arrOfAlp);
                    }

                    if(arrOfAlp.size()-itr>=arrOfWords[i].length() && !found){
                        found=cekKananBawah(itr,itc,arrOfWords[i],arrOfAlp);
                    }
                }
                
                if(itr>=arrOfWords[i].length()-1 && !found){
                    found = cekAtas(itr,itc,arrOfWords[i],arrOfAlp);
                }

                if(arrOfAlp.size()-itr>arrOfWords[i].length() && !found){
                    found = cekBawah(itr,itc,arrOfWords[i],arrOfAlp);                    
                }

                if(itc==arrOfAlp[itr].size()-1){
                    itc=0;
                    itr++;
                }else{
                    itc++;
                }
                
            }else{
                if(itc==arrOfAlp[itr].size()-1){
                    itc=0;
                    itr++;
                }else{
                    itc++;
                }
            }
        }
    }
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
  
    cout << "Time taken by function: "
         << duration.count() << " microseconds" << endl;
    return 0;
}