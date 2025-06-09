## STExtractionService

> `/System/Library/PrivateFrameworks/StreamingExtractor.framework/XPCServices/STExtractionService.xpc/STExtractionService`

```diff

-35.0.0.0.0
-  __TEXT.__text: 0x3be4
-  __TEXT.__stubs: 0x30c
-  __TEXT.__objc_stubs: 0x940
-  __TEXT.__objc_methlist: 0x404
+43.0.0.0.1
+  __TEXT.__text: 0x3c24
+  __TEXT.__stubs: 0x300
+  __TEXT.__objc_stubs: 0x9a0
+  __TEXT.__objc_methlist: 0x424
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0xbb5
-  __TEXT.__oslogstring: 0x2de
+  __TEXT.__cstring: 0xc03
+  __TEXT.__oslogstring: 0x29e
   __TEXT.__objc_classname: 0xbd
-  __TEXT.__objc_methname: 0xa85
-  __TEXT.__objc_methtype: 0x341
+  __TEXT.__objc_methname: 0xb19
+  __TEXT.__objc_methtype: 0x34c
   __TEXT.__gcc_except_tab: 0xb0
-  __TEXT.__unwind_info: 0x150
-  __DATA_CONST.__got: 0x2b8
-  __DATA_CONST.__const: 0x2a8
-  __DATA_CONST.__cfstring: 0x560
+  __TEXT.__unwind_info: 0x148
+  __DATA_CONST.__got: 0x2b0
+  __DATA_CONST.__const: 0x2b8
+  __DATA_CONST.__cfstring: 0x5a0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x948
-  __DATA.__objc_selrefs: 0x348
-  __DATA.__objc_ivar: 0x28
+  __DATA.__objc_const: 0x990
+  __DATA.__objc_selrefs: 0x368
+  __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x258
   __DATA.__bss: 0x18

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FB3DAB7B-7B5F-3750-8847-353DFE5A5079
-  Functions: 103
+  UUID: 6BE1F3D8-27DE-31D4-A67E-27158F059FA6
+  Functions: 102
   Symbols:   114
-  CStrings:  325
+  CStrings:  336
 
Symbols:
+ _STRemoteExtractorEntitlement
+ _STRemoteExtractorOptionsUsesReservePolicy
- _STGetLoggingCategory
- _csops_audittoken
CStrings:
+ "%{public}s: Rejecting process %@ since it is not properly entitled."
+ "03:09:57"
+ "May 23 2025"
+ "STRemoteExtractorOptionsUsesReservePolicy"
+ "TB,?,R,N"
+ "TB,N,V_usesReserveAccessPolicy"
+ "_usesReserveAccessPolicy"
+ "boolValue"
+ "com.apple.private.STRemoteExtractor"
+ "setUsesReserveAccessPolicy:"
+ "usesReserveAccessPolicy"
+ "v20@0:8B16"
+ "valueForEntitlement:"
- "%{public}s: Rejecting process %@ since csops_audittoken failed."
- "%{public}s: Rejecting process %@ since it is not a platform binary."
- "01:25:24"
- "Apr 19 2025"

```
