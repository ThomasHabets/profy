#include <unistd.h>


int
main()
{
	return execl("/sbin/iptables",
		     "iptables", "-L", "-n", "--line", "-v", NULL);
}
