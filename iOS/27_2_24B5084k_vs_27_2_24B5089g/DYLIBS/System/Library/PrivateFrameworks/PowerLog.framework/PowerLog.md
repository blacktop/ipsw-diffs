## PowerLog

> `/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog`

```diff

-3486.40.92.0.0
-  __TEXT.__text: 0x1e878
+3486.40.98.0.0
+  __TEXT.__text: 0x1e8b4
   __TEXT.__objc_methlist: 0x150c
   __TEXT.__const: 0xf78
-  __TEXT.__gcc_except_tab: 0x6c8
+  __TEXT.__gcc_except_tab: 0x6a0
   __TEXT.__cstring: 0x2420
   __TEXT.__oslogstring: 0x3a4a
-  __TEXT.__unwind_info: 0xae8
+  __TEXT.__unwind_info: 0xaf0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x198
   __DATA_CONST.__got: 0x1c8
-  __AUTH_CONST.__const: 0x540
+  __AUTH_CONST.__const: 0x560
   __AUTH_CONST.__cfstring: 0x29e0
   __AUTH_CONST.__objc_const: 0x22c8
   __AUTH_CONST.__objc_intobj: 0x4c8

   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__auth_got: 0x4c0
-  __AUTH.__objc_data: 0x550
+  __AUTH.__objc_data: 0x4d8
   __DATA.__objc_ivar: 0x1b4
-  __DATA.__data: 0x1e8
+  __DATA.__data: 0x1ec
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0xf0
+  __DATA_DIRTY.__objc_data: 0x168
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x88
+  __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 836
-  Symbols:   1664
+  Functions: 838
+  Symbols:   1667
   CStrings:  689
 
Symbols:
+ _PLClientPPSBatchSize.onceToken
+ _PLClientPPSBatchSize.sPPSBatchSize
+ ___PLClientPPSBatchSize_block_invoke
Functions:
~ -[PLClientLogger addToBatchedTaskCacheForType:forClientID:forKey:withPayload:] : 1200 -> 1112
+ ___PLClientPPSBatchSize_block_invoke
+ -[PLClientLogger addToBatchedTaskCacheForType:forClientID:forKey:withPayload:].cold.2
```
