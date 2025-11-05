## HealthDiagnosticExtensionCore

> `/System/Library/PrivateFrameworks/HealthDiagnosticExtensionCore.framework/Versions/A/HealthDiagnosticExtensionCore`

```diff

-5200.3.6.0.0
-  __TEXT.__text: 0xde10
+5200.4.25.0.0
+  __TEXT.__text: 0xe014
   __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_methlist: 0x6f4
+  __TEXT.__objc_methlist: 0x72c
   __TEXT.__const: 0x3a
-  __TEXT.__cstring: 0x28e5
+  __TEXT.__cstring: 0x298e
   __TEXT.__oslogstring: 0x34
   __TEXT.__gcc_except_tab: 0x310
-  __TEXT.__unwind_info: 0x378
+  __TEXT.__unwind_info: 0x380
   __TEXT.__objc_classname: 0x1b2
-  __TEXT.__objc_methname: 0x22c3
+  __TEXT.__objc_methname: 0x2345
   __TEXT.__objc_methtype: 0x241
-  __TEXT.__objc_stubs: 0x2680
-  __DATA_CONST.__got: 0x3e8
+  __TEXT.__objc_stubs: 0x26e0
+  __DATA_CONST.__got: 0x3f0
   __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa00
+  __DATA_CONST.__objc_selrefs: 0xa18
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x1e8
   __AUTH_CONST.__auth_got: 0x2d0
-  __AUTH_CONST.__const: 0x630
-  __AUTH_CONST.__cfstring: 0x29a0
-  __AUTH_CONST.__objc_const: 0x8f8
+  __AUTH_CONST.__const: 0x660
+  __AUTH_CONST.__cfstring: 0x2a00
+  __AUTH_CONST.__objc_const: 0x8b8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH.__objc_data: 0x370

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: E585C807-4781-3EE0-AF1D-5473E6DBA3A6
-  Functions: 210
-  Symbols:   911
-  CStrings:  1092
+  UUID: CBC36795-7804-3D16-9625-8B07A8D206F2
+  Functions: 212
+  Symbols:   918
+  CStrings:  1102
 
Symbols:
+ -[HDDatabaseDiagnosticOperation _reportSamplePruningStateDescriptionWithHealthStore:]
+ _OBJC_CLASS_$_HKDatabaseControl
+ __107-[HDDatabaseDiagnosticOperation _reportMissingSourceOrderEntriesWithUnprotectedDatabase:protectedDatabase:]_block_invoke.413
+ ___85-[HDDatabaseDiagnosticOperation _reportSamplePruningStateDescriptionWithHealthStore:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e28_v24?0"NSData"8"NSError"16l
+ _objc_msgSend$_reportSamplePruningStateDescriptionWithHealthStore:
+ _objc_msgSend$initWithData:encoding:
+ _objc_msgSend$showAndDeletedSampleInfoWithReferenceDate:completion:
- __107-[HDDatabaseDiagnosticOperation _reportMissingSourceOrderEntriesWithUnprotectedDatabase:protectedDatabase:]_block_invoke.412
CStrings:
+ "ERROR: Failed to get pruning state description: %@"
+ "ERROR: Timed out attempting collect pruning state description"
+ "Pruning State Description:"
+ "_reportSamplePruningStateDescriptionWithHealthStore:"
+ "initWithData:encoding:"
+ "showAndDeletedSampleInfoWithReferenceDate:completion:"
+ "v24@?0@\"NSData\"8@\"NSError\"16"

```
