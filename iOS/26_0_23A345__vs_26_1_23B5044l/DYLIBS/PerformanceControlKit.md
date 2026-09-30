## PerformanceControlKit

> `/System/Library/PrivateFrameworks/PerformanceControlKit.framework/PerformanceControlKit`

```diff

-1449.2.3.0.0
-  __TEXT.__text: 0x11d6c
+1449.40.32.0.0
+  __TEXT.__text: 0x11d80
   __TEXT.__auth_stubs: 0x810
-  __TEXT.__objc_methlist: 0x5c4
-  __TEXT.__cstring: 0x911
-  __TEXT.__gcc_except_tab: 0x1770
-  __TEXT.__const: 0xe80
-  __TEXT.__unwind_info: 0x748
+  __TEXT.__objc_methlist: 0x5b4
+  __TEXT.__cstring: 0x919
+  __TEXT.__gcc_except_tab: 0x1778
+  __TEXT.__const: 0xe90
+  __TEXT.__unwind_info: 0x740
   __TEXT.__objc_classname: 0x117
-  __TEXT.__objc_methname: 0xb78
+  __TEXT.__objc_methname: 0xb77
   __TEXT.__objc_methtype: 0x4038
-  __TEXT.__objc_stubs: 0x7e0
-  __DATA_CONST.__got: 0x148
+  __TEXT.__objc_stubs: 0x820
+  __DATA_CONST.__got: 0x150
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x340
+  __DATA_CONST.__objc_selrefs: 0x348
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x260
   __AUTH_CONST.__auth_got: 0x418
   __AUTH_CONST.__const: 0x5d0
-  __AUTH_CONST.__cfstring: 0xa80
-  __AUTH_CONST.__objc_const: 0xe00
+  __AUTH_CONST.__cfstring: 0xaa0
+  __AUTH_CONST.__objc_const: 0xdf8
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_dictobj: 0x230
   __AUTH.__objc_data: 0x50

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 1A2C8D96-4FE9-3C70-B3E5-D21C30BDD104
-  Functions: 321
+  UUID: 19F3B19A-BB1C-3F4A-95D8-F05B267990FA
+  Functions: 320
   Symbols:   1299
-  CStrings:  422
+  CStrings:  425
 
Symbols:
+ _OBJC_CLASS_$_NSMutableString
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$string
- -[CLPCPolicyClient setCLPCTrialID:error:]
Functions:
- -[CLPCPolicyClient setCLPCTrialID:error:]
~ -[CLPCReportingClient convertSampleList:error:] : 2788 -> 3024
~ __ZZ47-[CLPCReportingClient convertSampleList:error:]ENK4$_13clE21CLPCReportingSchemaIDmmP11objc_object : 368 -> 452
~ -[CLPCReportingClient decodeTGRawData:delta:error:] : 2648 -> 2644
CStrings:
+ "%02X"
+ "[INVALID_ENCODING:0x%@...]"
+ "appendFormat:"
- "Failed to set trial ID."
- "setCLPCTrialID:error:"

```
