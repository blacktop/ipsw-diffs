## nanoregistryd

> `/usr/libexec/nanoregistryd`

```diff

-985.0.0.0.0
-  __TEXT.__text: 0xf5b48
+988.0.0.0.0
+  __TEXT.__text: 0xf55b8
   __TEXT.__auth_stubs: 0x10a0
-  __TEXT.__objc_stubs: 0x106e0
-  __TEXT.__objc_methlist: 0xbc98
+  __TEXT.__objc_stubs: 0x106a0
+  __TEXT.__objc_methlist: 0xbc30
   __TEXT.__const: 0x678
-  __TEXT.__gcc_except_tab: 0x248c
-  __TEXT.__objc_methname: 0x1b3f9
-  __TEXT.__cstring: 0xcfe6
-  __TEXT.__oslogstring: 0x131a7
-  __TEXT.__objc_classname: 0x2177
-  __TEXT.__objc_methtype: 0x493f
+  __TEXT.__gcc_except_tab: 0x24d8
+  __TEXT.__objc_methname: 0x1b3a9
+  __TEXT.__cstring: 0xcfc0
+  __TEXT.__oslogstring: 0x13211
+  __TEXT.__objc_classname: 0x214f
+  __TEXT.__objc_methtype: 0x490b
   __TEXT.__dlopen_cstrs: 0xef
   __TEXT.__ustring: 0x4ac
-  __TEXT.__unwind_info: 0x3870
+  __TEXT.__unwind_info: 0x3848
   __DATA_CONST.__auth_got: 0x860
   __DATA_CONST.__got: 0xc18
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x4928
-  __DATA_CONST.__cfstring: 0xb960
-  __DATA_CONST.__objc_classlist: 0x7a0
+  __DATA_CONST.__cfstring: 0xb940
+  __DATA_CONST.__objc_classlist: 0x798
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x470
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x1f8
-  __DATA.__objc_const: 0x1bf58
-  __DATA.__objc_selrefs: 0x58a0
-  __DATA.__objc_ivar: 0x1140
-  __DATA.__objc_data: 0x4c40
+  __DATA.__objc_const: 0x1bdd0
+  __DATA.__objc_selrefs: 0x5888
+  __DATA.__objc_ivar: 0x1130
+  __DATA.__objc_data: 0x4bf0
   __DATA.__data: 0x19d8
   __DATA.__bss: 0x498
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 5564
+  Functions: 5551
   Symbols:   677
-  CStrings:  8412
+  CStrings:  8407
 
CStrings:
+ "99"
+ "_watchMigrationNotification, race mitigation check"
+ "_watchMigrationNotification, race mitigation completed"
+ "NanoRegistry-988"
- "_watchMigrationNotification:"
- "NanoRegistry-985"
- "_watchTimedOut:"
- "Migration timed out waiting for watch"
- "@\"<EPSagaTransactionWaitForWatchCompletionService>\""
- "_firstToCleanup"
- "_completionService"
- "77"
- "EPSagaTransactionWaitForWatchCompletion"

```
