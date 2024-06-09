#include<iostream>
#include<stdio.h>
using namespace std;


int partition(int a[20],int low,int high)
{
	int i=low+1;
	int j=high;
	int pivot=low;
	int temp;
	while(i<=j)
	{
		
		while(a[i] < a[pivot])
		{
			i++;	
		}
		while(a[j] > a[pivot])
		{
			j--;
		}
		if(i<j)
		{
			temp=a[i];
			a[i]=a[j];
			a[j]=temp;
		}
	}
	temp=a[pivot];
	a[pivot]=a[j];
	a[j]=temp;
	
	return j;
	
}

void quicksort(int a[20],int low,int high)
{

	int p;
	if(low < high)
	{
		p=partition(a,low, high);
		quicksort(a,low,p-1);
		quicksort(a,p+1,high);
	}
}

int main()
{
 	int a[20];
 	int n;
 	cout<<"Enter number of elements you want in your array"<<endl;
 	cin>>n;
 	
 	for(int i=0;i<n;i++)
 	{
 		cout<<"Enter element in array at position ="<<i+1<<endl;
 	 	cin>>a[i];	
 	}
 	cout<<endl;
 	cout<<endl;
 	cout<<endl;
 	for(int i=0;i<n;i++)
 	{
 		cout<<a[i]<<endl;
 	}
 	
 	cout<<endl;cout<<endl;
 	
 	int low=0;
 	int high=n-1;
 	
 	quicksort(a,low,high);
 	
 	
 	
 	for(int i=0;i<n;i++)
 	{
 		cout<<a[i]<<endl;
 	}
 	
 	cout<<endl;cout<<endl;
 	
}
