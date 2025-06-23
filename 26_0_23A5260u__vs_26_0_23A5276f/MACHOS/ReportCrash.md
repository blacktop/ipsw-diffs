## ReportCrash

> `/System/Library/CoreServices/ReportCrash`

```diff

-912.0.0.0.0
-  __TEXT.__text: 0x2c530
-  __TEXT.__auth_stubs: 0x1920
-  __TEXT.__objc_stubs: 0x3040
+917.0.0.0.0
+  __TEXT.__text: 0x2ca90
+  __TEXT.__auth_stubs: 0x1940
+  __TEXT.__objc_stubs: 0x30c0
   __TEXT.__objc_methlist: 0xd10
-  __TEXT.__cstring: 0x5341
+  __TEXT.__cstring: 0x54a1
   __TEXT.__const: 0x444
-  __TEXT.__objc_methname: 0x37bf
-  __TEXT.__oslogstring: 0x1a49
-  __TEXT.__objc_classname: 0x104
+  __TEXT.__objc_methname: 0x3830
+  __TEXT.__oslogstring: 0x1ab9
+  __TEXT.__objc_classname: 0x105
   __TEXT.__objc_methtype: 0x805
-  __TEXT.__gcc_except_tab: 0x304
+  __TEXT.__gcc_except_tab: 0x398
   __TEXT.__dlopen_cstrs: 0xa5
   __TEXT.__swift5_typeref: 0x268
   __TEXT.__swift5_capture: 0xe4

   __TEXT.__swift5_types: 0x28
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x728
+  __TEXT.__unwind_info: 0x730
   __TEXT.__eh_frame: 0x248
-  __DATA_CONST.__auth_got: 0xca0
-  __DATA_CONST.__got: 0x3d8
+  __DATA_CONST.__auth_got: 0xcb0
+  __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__auth_ptr: 0x150
-  __DATA_CONST.__const: 0xee8
-  __DATA_CONST.__cfstring: 0x7500
+  __DATA_CONST.__const: 0xef0
+  __DATA_CONST.__cfstring: 0x7620
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_arraydata: 0x358
   __DATA_CONST.__objc_dictobj: 0x1e0
   __DATA_CONST.__objc_arrayobj: 0x1f8
-  __DATA.__objc_const: 0x1e98
-  __DATA.__objc_selrefs: 0xed0
-  __DATA.__objc_ivar: 0x248
+  __DATA.__objc_const: 0x1ef8
+  __DATA.__objc_selrefs: 0xee0
+  __DATA.__objc_ivar: 0x254
   __DATA.__objc_data: 0x888
   __DATA.__data: 0x5e8
   __DATA.__crash_info: 0x148

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 17A3EC6F-D4AE-36CA-BBD7-478DA8E21E20
-  Functions: 623
+  UUID: E0BE9E1E-C129-340A-A295-10ABFFE20832
+  Functions: 624
   Symbols:   587
-  CStrings:  2946
+  CStrings:  2972
 
Symbols:
+ OBJC_IVAR_$_VMUVMRegion.path
+ OBJC_IVAR_$_VMUVMRegion.prot
+ __os_feature_enabled_impl
+ _atoi
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "Bad access in stack guard region for thread %d but crash was associated with thread %d - possible stray access?"
+ "Could not determine thread index for stack guard region"
+ "Thread stack size exceeded"
+ "Thread stack size exceeded due to excessive recursion"
+ "_isStackGuardPageBadAccess"
+ "_recursionOnCrashedThread"
+ "_stackGuardPageBadAccessThreadNumber"
+ "descriptionForRegionTotals:"
+ "elideRecursionInCrashLogs"
+ "keyFrame"
+ "keyPC"
+ "originalLength"
+ "recursionInfoArray"
+ "stack guard for thread "
+ "thread's original recursionInfoArray.count is %zu but after processing inline frames recursionInfoArray.count is %zu"
- "descriptionForRegionTotalsWithOptions:"

```
