## dyld

> `/usr/lib/dyld`

```diff

-1284.1.1.0.0
-  __TEXT.__text: 0x868d8
+1284.8.0.0.0
+  __TEXT.__text: 0x86a24
   __TEXT.__const: 0x22e8
-  __TEXT.__cstring: 0xf931
+  __TEXT.__cstring: 0xf95e
   __TEXT.__unwind_info: 0x4b0
   __DATA_CONST.__auth_ptr: 0x88
-  __DATA_CONST.__const: 0x6be8
+  __DATA_CONST.__const: 0x6bc0
   __DATA.__data: 0x2c8
   __DATA.__crash_info: 0x40
   __DATA.__common: 0x8f0

   __DATA_DIRTY.__common: 0x1120
   __TPRO_CONST.__data: 0xd0
   __TPRO_CONST.__allocator: 0x20000
-  Functions: 2878
-  Symbols:   3994
-  CStrings:  1943
+  Functions: 2877
+  Symbols:   3992
+  CStrings:  1944
 
Symbols:
+ __ZN5dyld39MachOFile15compatibleSliceER11DiagnosticsRyS3_PKvmPKcN6mach_o8PlatformEbRKNS_11GradedArchsEb
+ ___ZN5dyld4L19getObjCPatchClassesEPKN5dyld313MachOAnalyzerERNS0_3MapIPKvbNS_11HashPointerENS_12EqualPointerEEE_block_invoke.91
+ __block_descriptor_tmp.233
+ __block_descriptor_tmp.234
+ __block_descriptor_tmp.84
- __ZN5dyld39MachOFile15compatibleSliceER11DiagnosticsRyPKvmPKcN6mach_o8PlatformEbRKNS_11GradedArchsEb
- ___ZN5dyld4L19getObjCPatchClassesEPKN5dyld313MachOAnalyzerERNS0_3MapIPKvbNS_11HashPointerENS_12EqualPointerEEE_block_invoke.92
- ____ZN5dyld416JustInTimeLoader24makeJustInTimeLoaderDiskER11DiagnosticsRNS_12RuntimeStateEPKcRKNS_6Loader11LoadOptionsEbjPKN6mach_o6LayoutE_block_invoke_2
- __block_descriptor_tmp.157
- __block_descriptor_tmp.179
CStrings:
+ "1284.8"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Tue Mar  4 21:39:55 PST 2025; root:libignition-56~61013/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Tue Mar  4 21:39:55 PST 2025; root:libignition-56~61013/libignition_core/RELEASE_ARM64E"
+ "mmap for %s (size=0x%0lX) failed with errno=%d"
- "1284.1.1"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Tue Feb 25 20:54:23 PST 2025; root:libignition-56~60824/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Tue Feb 25 20:54:23 PST 2025; root:libignition-56~60824/libignition_core/RELEASE_ARM64E"

```
