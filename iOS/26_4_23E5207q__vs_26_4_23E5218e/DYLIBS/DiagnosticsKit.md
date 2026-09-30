## DiagnosticsKit

> `/System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit`

```diff

-72.100.3.0.0
-  __TEXT.__text: 0x21448
-  __TEXT.__auth_stubs: 0x5a0
+72.100.4.0.0
+  __TEXT.__text: 0x21580
+  __TEXT.__auth_stubs: 0x5b0
   __TEXT.__objc_methlist: 0x2f94
   __TEXT.__const: 0xe0
   __TEXT.__cstring: 0x1b07
-  __TEXT.__oslogstring: 0x1817
-  __TEXT.__gcc_except_tab: 0xab8
+  __TEXT.__oslogstring: 0x185f
+  __TEXT.__gcc_except_tab: 0xadc
   __TEXT.__unwind_info: 0xae8
   __TEXT.__objc_classname: 0x6c9
   __TEXT.__objc_methname: 0x5b6b
   __TEXT.__objc_methtype: 0x110f
-  __TEXT.__objc_stubs: 0x46a0
+  __TEXT.__objc_stubs: 0x4680
   __DATA_CONST.__got: 0x2d0
   __DATA_CONST.__const: 0x658
   __DATA_CONST.__objc_classlist: 0x160

   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x2e0
+  __AUTH_CONST.__auth_got: 0x2e8
   __AUTH_CONST.__const: 0x420
   __AUTH_CONST.__cfstring: 0xee0
   __AUTH_CONST.__objc_const: 0x5220

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AA464185-F586-3B74-AC5E-6EED554D2BC6
+  UUID: 5AA0E59B-9099-3AE8-9D37-15F8E2951119
   Functions: 946
   Symbols:   3553
-  CStrings:  1696
+  CStrings:  1697
 
Symbols:
+ ___70-[DKReportManager sendRequests:serialRequests:failOnError:completion:]_block_invoke.81
+ _objc_retain_x25
- ___70-[DKReportManager sendRequests:serialRequests:failOnError:completion:]_block_invoke.78
- _objc_msgSend$reportByMergingReport:
Functions:
~ ___67-[DKReportManager reportWithComponentPredicateManifest:completion:]_block_invoke.64 : 460 -> 556
~ -[DKReportManager retryInterruptedRequests:andWithError:] : 1072 -> 1268
~ ___70-[DKReportManager sendRequests:serialRequests:failOnError:completion:]_block_invoke : 576 -> 596
CStrings:
+ "Rerunning interrupted report components in serial order: %@"
+ "Retrying %lu incompleted SystemReport components in serial order..."
- "Rerunning interrupted report components in serial order"

```
