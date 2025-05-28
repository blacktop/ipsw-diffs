## ScreenshotServices

> `/System/Library/PrivateFrameworks/ScreenshotServices.framework/ScreenshotServices`

```diff

-345.0.1.0.0
-  __TEXT.__text: 0x16e20
-  __TEXT.__auth_stubs: 0x7d0
+345.3.0.0.0
+  __TEXT.__text: 0x17128
+  __TEXT.__auth_stubs: 0x7e0
   __TEXT.__objc_methlist: 0x1d28
   __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x1574
-  __TEXT.__oslogstring: 0xbe4
-  __TEXT.__gcc_except_tab: 0x21c
+  __TEXT.__cstring: 0x1586
+  __TEXT.__oslogstring: 0xd39
+  __TEXT.__gcc_except_tab: 0x228
   __TEXT.__dlopen_cstrs: 0x3b4
-  __TEXT.__unwind_info: 0x838
+  __TEXT.__unwind_info: 0x83c
   __TEXT.__objc_classname: 0x7ec
-  __TEXT.__objc_methname: 0x561b
+  __TEXT.__objc_methname: 0x563f
   __TEXT.__objc_methtype: 0xec0
-  __TEXT.__objc_stubs: 0x4e20
+  __TEXT.__objc_stubs: 0x4e40
   __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__const: 0x958
   __DATA_CONST.__objc_classlist: 0x1d0

   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x3360
-  __DATA_CONST.__objc_selrefs: 0x1630
+  __DATA_CONST.__objc_selrefs: 0x1638
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x3a0
+  __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x38
   __AUTH_CONST.__objc_const: 0x18a0
   __AUTH_CONST.__cfstring: 0x1100

   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x3f8
+  __AUTH_CONST.__auth_got: 0x400
   __AUTH.__objc_data: 0x690
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x3a0
-  __DATA.__objc_superrefs: 0xe0
   __DATA.__objc_ivar: 0x220
-  __DATA.__data: 0x6e8
-  __DATA.__bss: 0xd8
+  __DATA.__data: 0x718
+  __DATA.__bss: 0xa8
   __DATA_DIRTY.__objc_data: 0xb90
   __DATA_DIRTY.__bss: 0xb0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 762
-  Symbols:   3199
-  CStrings:  1456
+  Symbols:   3201
+  CStrings:  1464
 
Symbols:
+ _CACurrentMediaTime
+ ___77+[SSScreenshotMetadataHarvester harvestScreenshotMetadataAndRespondToAction:]_block_invoke.27
+ ___77+[SSScreenshotMetadataHarvester harvestScreenshotMetadataAndRespondToAction:]_block_invoke.28
+ ___block_descriptor_80_e8_32s40s48s56r_e53_v56?0"NSData"8q16{CGRect={CGPoint=dd}{CGSize=dd}}24ls32l8r56l8s40l8s48l8
+ _objc_msgSend$canSendResponse
- ___77+[SSScreenshotMetadataHarvester harvestScreenshotMetadataAndRespondToAction:]_block_invoke_2
- ___77+[SSScreenshotMetadataHarvester harvestScreenshotMetadataAndRespondToAction:]_block_invoke_3
- ___block_descriptor_64_e8_32s40s48r_e53_v56?0"NSData"8q16{CGRect={CGPoint=dd}{CGSize=dd}}24lr48l8s32l8s40l8
CStrings:
+ "Grab PDF representation for identifier: %{private}@"
+ "MetadataHarvester"
+ "Send response for action with key: %lu"
+ "T@\"NSString\",?,R,C"
+ "Unable to send response for action with key: %lu"
+ "canSendResponse"
+ "did grab PDF representation for identifier: %{private}@, data length: %lu, page: %ld, rect: %{private}@, elapsed time: %f, didSendResponse: %{BOOL}d"
+ "pdf harvesting timed out! didSendResponse: %{BOOL}d"

```
