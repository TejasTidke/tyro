#include<stdio.h>


int main()
{
    int i,max_modulo=0,count=0,flag=0;
    int modulo[10]={0,1,2,3,4,5,6,9,9,9};
    for(i=0;i<10;i++)
    {
            if(modulo[i]>max_modulo)
            {
                max_modulo=modulo[i];
                if(flag==0)
                {
                    count=1;
                }
            }
            else if(max_modulo==modulo[i])
            {
                count++;
                flag=1;
            }
    }
    printf("No of repeated occurrences:%d\n",count);
    printf("Maximum Number:%d",max_modulo);
}
