#include <iostream>
#include <GL/glu.h>

int main()
{
	if(const auto str = gluGetString(GLU_VERSION))
	{
		std::cout << "Glu version; " << str << std::endl;
	}
    return 0;
}
