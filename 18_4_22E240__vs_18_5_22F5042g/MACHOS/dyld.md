## dyld

> `/usr/lib/dyld`

```diff

-1284.10.0.0.0
-  __TEXT.__text: 0x86a24
-  __TEXT.__const: 0x22e8
-  __TEXT.__cstring: 0xf95f
-  __TEXT.__unwind_info: 0x4b0
-  __DATA_CONST.__auth_ptr: 0x88
+1285.12.0.0.0
+  __TEXT.__text: 0x86ea4
+  __TEXT.__const: 0x2328
+  __TEXT.__cstring: 0xfa3b
+  __TEXT.__unwind_info: 0x508
+  __DATA_CONST.__auth_ptr: 0x90
   __DATA_CONST.__const: 0x6bc0
   __DATA.__data: 0x2c8
   __DATA.__crash_info: 0x40

   __DATA_DIRTY.__common: 0x1120
   __TPRO_CONST.__data: 0xd0
   __TPRO_CONST.__allocator: 0x20000
-  Functions: 2877
-  Symbols:   3992
-  CStrings:  1944
+  Functions: 2882
+  Symbols:   3997
+  CStrings:  1955
 
Symbols:
+ _ZL22hactivateFileAllocatorbbbPv.cold.1
+ _ZL22hactivateFileAllocatorbbbPv.cold.2
+ _ZL22hactivateFileAllocatorbbbPv.cold.3
+ __ZL22hactivateFileAllocatorbbbPv
+ __ZN6mach_o8Platform5Epoch8fall2025E
CStrings:
+ "\tMTE:  %s\n"
+ "\tTPRO: %s\n"
+ "%s__TPRO_CONST,__allocator = 0x%llx - 0x%llx\n"
+ "1285.12"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Mon Mar 24 19:56:55 PDT 2025; root:libignition-56~61338/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Mon Mar 24 19:56:55 PDT 2025; root:libignition-56~61338/libignition_core/RELEASE_ARM64E"
+ "Off"
+ "On"
+ "Shared Cache "
+ "_DYLD_PRINT_PROTETED_MEMORY_STATUS"
+ "foundCompactTproMapping == true"
+ "hactivateFileAllocator"
+ "kr == KERN_SUCCESS"
+ "tproMappingCount == 1"
- "1284.10"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Sat Mar 15 17:47:48 PDT 2025; root:libignition-56~61187/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Sat Mar 15 17:47:48 PDT 2025; root:libignition-56~61187/libignition_core/RELEASE_ARM64E"

```
