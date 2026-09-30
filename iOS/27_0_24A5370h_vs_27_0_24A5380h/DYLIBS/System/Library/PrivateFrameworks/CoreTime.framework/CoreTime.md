## CoreTime

> `/System/Library/PrivateFrameworks/CoreTime.framework/CoreTime`

```diff

-  __TEXT.__text: 0x684c
+  __TEXT.__text: 0x6ba8
   __TEXT.__objc_methlist: 0x28c
-  __TEXT.__const: 0xf0
+  __TEXT.__const: 0xf8
   __TEXT.__gcc_except_tab: 0x6c
-  __TEXT.__cstring: 0xee9
-  __TEXT.__oslogstring: 0x504
+  __TEXT.__cstring: 0xf1b
+  __TEXT.__oslogstring: 0x518
   __TEXT.__ustring: 0x2c
-  __TEXT.__unwind_info: 0x250
+  __TEXT.__unwind_info: 0x260
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_selrefs: 0x228
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__got: 0xa0
-  __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0xe00
+  __AUTH_CONST.__const: 0x160
+  __AUTH_CONST.__cfstring: 0xe20
   __AUTH_CONST.__objc_const: 0x3c8
-  __AUTH_CONST.__objc_intobj: 0x4e0
+  __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x78
   __DATA.__objc_ivar: 0x28
   __DATA.__data: 0x120
-  __DATA.__bss: 0x68
-  __DATA_DIRTY.__objc_data: 0xa0
+  __DATA.__bss: 0x70
+  __DATA_DIRTY.__objc_data: 0x28
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 195
-  Symbols:   749
-  CStrings:  317
+  Functions: 201
+  Symbols:   762
+  CStrings:  321
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __DATA.__data : content changed
Symbols:
+ GCC_except_table27
+ GCC_except_table35
+ GCC_except_table42
+ _CFAbsoluteTimeGetCurrent
+ _TMGetBestEffortTime
+ _TMIsAutomaticTimeEnabledAsync
+ __TMGetKernelMonotonicClock.onceToken
+ ___TMIsAutomaticTimeEnabledAsync_block_invoke
+ ___TMIsAutomaticTimeEnabledAsync_block_invoke_2
+ ____TMGetKernelMonotonicClock_block_invoke
- GCC_except_table23
- GCC_except_table31
- GCC_except_table38
CStrings:
+ "TMGetBestEffortTime"
+ "TMIsAutomaticTimeEnabledAsync"

```
