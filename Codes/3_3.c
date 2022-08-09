#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int x[6] = {1,2,3,4,2,1};
    float y[20] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
    y[0] = 1;
    for(int i =1;i<20;i++)
    {
    	if(i<2)
    	{
    		y[i] = x[i] - (0.5)*y[i-1];
    	}
    	else if(i>=2 && i<6)
    	{
    		y[i] = x[i] + x[i-2] -0.5*y[i-1];	
    	}
    	else if (i>=6 && i<8)
    	{
    		y[i] = -0.5*y[i-1] + x[i-2];
    	}
    	else
    	{
    		y[i] = -0.5*y[i-1];
    	}
    	
    }
    
    FILE *f; 

    f = fopen("x.txt", "w");
    for(int i =0; i<6;i++)
    {
    	fprintf(f,"%d",x[i]);
    	fprintf(f,"\n");
    }
    
    FILE *f1;
    
    f1 = fopen("y.txt","w");
    for(int i =0; i<20;i++)
    {
    	fprintf(f1,"%f",y[i]);
    	fprintf(f1,"\n");
    }
    
}

