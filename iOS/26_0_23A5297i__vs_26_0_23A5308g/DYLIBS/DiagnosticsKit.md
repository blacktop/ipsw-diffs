## DiagnosticsKit

> `/System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit`

```diff

-72.0.1.0.0
-  __TEXT.__text: 0x1f750
-  __TEXT.__auth_stubs: 0x640
+72.0.2.0.0
+  __TEXT.__text: 0x1f704
+  __TEXT.__auth_stubs: 0x630
   __TEXT.__objc_methlist: 0x2eac
   __TEXT.__const: 0xe8
-  __TEXT.__cstring: 0x1ac9
+  __TEXT.__cstring: 0x1a99
   __TEXT.__oslogstring: 0x17c0
   __TEXT.__gcc_except_tab: 0xbc4
   __TEXT.__dlopen_cstrs: 0x173

   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x330
+  __AUTH_CONST.__auth_got: 0x328
   __AUTH_CONST.__const: 0x400
   __AUTH_CONST.__cfstring: 0xe20
   __AUTH_CONST.__objc_const: 0x5190

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D4144ED6-9770-3F8C-A467-BAB47CC5ADBB
+  UUID: 8661FC8E-8FE7-3AF7-B2E4-594AA25BB654
   Functions: 940
-  Symbols:   3538
-  CStrings:  1672
+  Symbols:   3537
+  CStrings:  1670
 
Symbols:
+ ___70-[DKReportManager sendRequests:serialRequests:failOnError:completion:]_block_invoke.78
- ___70-[DKReportManager sendRequests:serialRequests:failOnError:completion:]_block_invoke.80
- __os_feature_enabled_impl
Functions:
~ ___67-[DKReportManager reportWithComponentPredicateManifest:completion:]_block_invoke.64 : 472 -> 448
~ -[DKReportManager sendRequests:serialRequests:failOnError:completion:] : 2420 -> 2392
~ ___70-[DKReportManager sendRequests:serialRequests:failOnError:completion:]_block_invoke : 588 -> 564
CStrings:
- "ConcurrentSystemReportGeneration"
- "DiagnosticsKit"

```
