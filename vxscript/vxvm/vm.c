#include <stdlib.h>
#include "vm.h"
#include "exception.h"

void vm_load(void *vmMemory) {
	// Read VMInfo
	struct VMInfo32 *vmInfo32 = (int*) vmInfo;
	// Check magic number
	if (vmInfo32->vmMagicNumber != 123456789) {
		throw("InvaildArgumentException", "Invaild Magic number!");
	}
}
