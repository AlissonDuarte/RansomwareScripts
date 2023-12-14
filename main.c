#include <stdio.h>
#include <string.h>

int main() {
    FILE *fp;
    char buffer[128];
    int isVirtualMachine = 0;

    // Checks for the presence of some device files typical of VMs
    if ((fp = fopen("/sys/class/dmi/id/product_name", "r"))) {
        fgets(buffer, sizeof(buffer), fp);
        if (strstr(buffer, "Virtual") != NULL || strstr(buffer, "VMware") != NULL) {
            isVirtualMachine = 1;
        }
        fclose(fp);
    }

    if (isVirtualMachine) {
        printf("Look like a virtual machine.\n");
    } else {
        printf("It doesn't look like a virtual machine.\n");
    }

    return 0;
}
