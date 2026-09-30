## ContextSync

> `/System/Library/PrivateFrameworks/ContextSync.framework/ContextSync`

```diff

-209.18.0.0.0
-  __TEXT.__text: 0x1115c
+209.19.0.0.0
+  __TEXT.__text: 0x11870
   __TEXT.__auth_stubs: 0x420
-  __TEXT.__objc_methlist: 0xcbc
+  __TEXT.__objc_methlist: 0xccc
   __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0x430
-  __TEXT.__cstring: 0xc0e
+  __TEXT.__gcc_except_tab: 0x45c
+  __TEXT.__cstring: 0xcf7
   __TEXT.__oslogstring: 0x1017
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x4c8
+  __TEXT.__unwind_info: 0x4e0
   __TEXT.__objc_classname: 0x279
-  __TEXT.__objc_methname: 0x2ebf
+  __TEXT.__objc_methname: 0x2fab
   __TEXT.__objc_methtype: 0x1101
-  __TEXT.__objc_stubs: 0x1d20
+  __TEXT.__objc_stubs: 0x1e80
   __DATA_CONST.__got: 0x178
   __DATA_CONST.__const: 0x380
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xab0
+  __DATA_CONST.__objc_selrefs: 0xb08
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x50
   __AUTH_CONST.__auth_got: 0x220

   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0xa4
   __DATA.__data: 0x240
-  __DATA.__bss: 0x98
+  __DATA.__bss: 0xb0
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 63738FA5-3FA8-3E1F-A7E4-4ACB0E3039F3
-  Functions: 331
-  Symbols:   1307
-  CStrings:  842
+  UUID: 09819850-1D27-3C66-89B1-BEB5732CFFEC
+  Functions: 340
+  Symbols:   1341
+  CStrings:  859
 
Symbols:
+ -[BMDistributedContextEventTranslation contextSyncWorkoutFromEvent:]
+ GCC_except_table16
+ GCC_except_table18
+ GCC_except_table23
+ GCC_except_table25
+ ___getBMContextSyncHealthWorkoutIdentifierSymbolLoc_block_invoke
+ ___getBMContextSyncWorkoutClass_block_invoke
+ ___getBMContextSyncWorkoutClass_block_invoke.cold.1
+ ___getBMHealthWorkoutClass_block_invoke
+ ___getBMHealthWorkoutClass_block_invoke.cold.1
+ _getBMContextSyncHealthWorkoutIdentifier
+ _getBMContextSyncHealthWorkoutIdentifier.cold.1
+ _getBMContextSyncHealthWorkoutIdentifierSymbolLoc.ptr
+ _getBMContextSyncWorkoutClass
+ _getBMContextSyncWorkoutClass.softClass
+ _getBMHealthWorkoutClass.softClass
+ _objc_msgSend$activityType
+ _objc_msgSend$activityUUID
+ _objc_msgSend$contextSyncWorkoutFromEvent:
+ _objc_msgSend$eventType
+ _objc_msgSend$hasIsFirstPartyDonation
+ _objc_msgSend$hasIsIndoor
+ _objc_msgSend$hasIsUpdate
+ _objc_msgSend$initWithIsFirstPartyDonation:isIndoor:activityType:eventType:activityUUID:isUpdate:
+ _objc_msgSend$isFirstPartyDonation
+ _objc_msgSend$isIndoor
+ _objc_msgSend$isUpdate
- GCC_except_table19
- GCC_except_table22
- GCC_except_table26
- GCC_except_table30
CStrings:
+ "BMContextSyncHealthWorkoutIdentifier"
+ "BMContextSyncWorkout"
+ "BMHealthWorkout"
+ "Class getBMContextSyncWorkoutClass(void)_block_invoke"
+ "Class getBMHealthWorkoutClass(void)_block_invoke"
+ "NSString *getBMContextSyncHealthWorkoutIdentifier(void)"
+ "activityType"
+ "activityUUID"
+ "contextSyncWorkoutFromEvent:"
+ "eventType"
+ "hasIsFirstPartyDonation"
+ "hasIsIndoor"
+ "hasIsUpdate"
+ "initWithIsFirstPartyDonation:isIndoor:activityType:eventType:activityUUID:isUpdate:"
+ "isFirstPartyDonation"
+ "isIndoor"
+ "isUpdate"

```
