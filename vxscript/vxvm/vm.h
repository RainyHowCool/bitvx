#ifndef VM_H
#define VM_H
struct VMInfo32 {
	int vmMagicNumber;
	int vmVersion32;
	int vmStackSize32;
	int vmCodeOffest32;
	int vmDataOffest32;
	int vmStackOffest32;
	int vmStackSize32;
	int vmHeapMax32;
	int vmGCEnabled;
	int vmGCTolerance32;
};
#endif
