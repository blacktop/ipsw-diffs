## ReportCrash

> `/System/Library/CoreServices/ReportCrash`

```diff

 927.0.2.0.0
-  __TEXT.__text: 0x2cfbc
-  __TEXT.__auth_stubs: 0x1960
-  __TEXT.__objc_stubs: 0x3100
-  __TEXT.__objc_methlist: 0xd38
-  __TEXT.__cstring: 0x5571
+  __TEXT.__text: 0x2ed94
+  __TEXT.__auth_stubs: 0x1990
+  __TEXT.__objc_stubs: 0x3160
+  __TEXT.__objc_methlist: 0xd58
+  __TEXT.__cstring: 0x56d1
   __TEXT.__const: 0x444
-  __TEXT.__objc_methname: 0x3846
-  __TEXT.__oslogstring: 0x1ab9
-  __TEXT.__objc_classname: 0x105
+  __TEXT.__objc_methname: 0x38c1
+  __TEXT.__oslogstring: 0x1ae2
+  __TEXT.__objc_classname: 0x106
   __TEXT.__objc_methtype: 0x806
   __TEXT.__gcc_except_tab: 0x398
   __TEXT.__dlopen_cstrs: 0xa5

   __TEXT.__swift5_types: 0x28
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x7b0
-  __TEXT.__eh_frame: 0x270
-  __DATA_CONST.__auth_got: 0xcc0
+  __TEXT.__unwind_info: 0x820
+  __TEXT.__eh_frame: 0x2d8
+  __DATA_CONST.__auth_got: 0xcd8
   __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__auth_ptr: 0x150
-  __DATA_CONST.__const: 0xf58
-  __DATA_CONST.__cfstring: 0x7680
+  __DATA_CONST.__const: 0xf18
+  __DATA_CONST.__cfstring: 0x77e0
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__objc_intobj: 0x4f8
+  __DATA_CONST.__objc_intobj: 0x528
   __DATA_CONST.__objc_arraydata: 0x358
   __DATA_CONST.__objc_dictobj: 0x1e0
   __DATA_CONST.__objc_arrayobj: 0x1f8
-  __DATA.__objc_const: 0x1f08
-  __DATA.__objc_selrefs: 0xef0
-  __DATA.__objc_ivar: 0x254
+  __DATA.__objc_const: 0x1f38
+  __DATA.__objc_selrefs: 0xf10
+  __DATA.__objc_ivar: 0x258
   __DATA.__objc_data: 0x888
-  __DATA.__data: 0x5f0
+  __DATA.__data: 0x600
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x240
   __DATA.__common: 0x3

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 557554F4-5FBB-3219-8F32-CC9E033EE0B7
-  Functions: 635
-  Symbols:   589
-  CStrings:  2987
+  UUID: C93D3B8A-9B21-3E39-A1E1-E70D7C25B287
+  Functions: 660
+  Symbols:   592
+  CStrings:  3020
 
Symbols:
+ _$sSo17OS_dispatch_queueC8DispatchE4sync7executexxyKXE_tKlF
+ _os_security_config_get_for_task
+ _sanitizers_diagnose_memory_error
CStrings:
+ "EXC_ARM_MTE_TAGCHECK_FAIL"
+ "Error querying if MTE is enabled"
+ "GUARD_EXC_MTE_ASYNC_USER_FAULT"
+ "GUARD_EXC_MTE_SYNC_FAULT"
+ "GUARD_EXC_SEC_ACCESS_FAULT"
+ "GUARD_EXC_SEC_ASYNC_ACCESS_FAULT"
+ "MTE_FAIL"
+ "ReportCrash8"
+ "_extractMemoryErrorReportUsingSymbolicator:usingCatalog:"
+ "_mteTags"
+ "address"
+ "arrayForKey:"
+ "blamedAllocation"
+ "isFreed"
+ "isMTECrash"
+ "kGUARD_EXC_MTE_ASYNC_KERN_FAULT"
+ "libsystem_sanitizers.dylib"
+ "memoryExceptionProcesses"
+ "mtePageTags"
+ "observedMTECrashWithProcessName:"
+ "sanitizers_report_globals"

```
