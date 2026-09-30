## Symbolication

> `/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication`

```diff

-64575.69.1.0.0
-  __TEXT.__text: 0xb99f4
+64575.70.1.0.0
+  __TEXT.__text: 0xb9b9c
   __TEXT.__auth_stubs: 0x20a0
   __TEXT.__objc_methlist: 0x6860
   __TEXT.__const: 0x2f6
   __TEXT.__gcc_except_tab: 0x526c
-  __TEXT.__cstring: 0x108b0
-  __TEXT.__oslogstring: 0x187c
+  __TEXT.__cstring: 0x108f0
+  __TEXT.__oslogstring: 0x18dc
   __TEXT.__ustring: 0x24
   __TEXT.__swift5_typeref: 0x402
   __TEXT.__swift5_capture: 0x120

   __TEXT.__swift5_reflstr: 0x311
   __TEXT.__swift5_fieldmd: 0x2a8
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x2cb8
+  __TEXT.__unwind_info: 0x2cc0
   __TEXT.__objc_classname: 0x910
   __TEXT.__objc_methname: 0x1060a
   __TEXT.__objc_methtype: 0x6971

   __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__objc_arraydata: 0x870
   __AUTH_CONST.__auth_got: 0x1068
-  __AUTH_CONST.__const: 0x11f8
+  __AUTH_CONST.__const: 0x1218
   __AUTH_CONST.__cfstring: 0xe080
   __AUTH_CONST.__objc_const: 0xc540
   __AUTH_CONST.__objc_arrayobj: 0xf0

   __AUTH.__thread_bss: 0x8
   __DATA.__objc_ivar: 0xcf4
   __DATA.__data: 0xd60
-  __DATA.__bss: 0x598
+  __DATA.__bss: 0x5b8
   __DATA.__common: 0xf9
   __DATA_DIRTY.__objc_data: 0x1838
   __DATA_DIRTY.__data: 0x28

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 8C0A7172-6425-32A2-B679-FE01EDB01B97
-  Functions: 3281
-  Symbols:   11068
-  CStrings:  8061
+  UUID: 3591BD87-DD6A-3430-88D8-77AA2A365740
+  Functions: 3284
+  Symbols:   11079
+  CStrings:  8065
 
Symbols:
+ -[VMUSampler sampleThread:withOptions:].cold.1
+ -[VMUSampler sampleThread:withOptions:].cold.2
+ ___39-[VMUSampler sampleThread:withOptions:]_block_invoke
+ ___block_literal_global.27
+ _sampleThread:withOptions:.onceToken
+ _sampleThread:withOptions:.thread_resume2_func
+ _sampleThread:withOptions:.thread_suspend2_func
+ _sampleThread:withOptions:.use2
CStrings:
+ "/usr/lib/system/libsystem_kernel.dylib"
+ "[VMUSampler sampleThread:options:] thread suspension failed for pid %u thread %u, err %d"
+ "thread_resume2"
+ "thread_suspend2"

```
