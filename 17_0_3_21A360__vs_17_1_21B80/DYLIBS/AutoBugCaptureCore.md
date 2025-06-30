## AutoBugCaptureCore

> `/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore`

```diff

-300.0.0.0.0
-  __TEXT.__text: 0x739b4
+308.0.0.0.0
+  __TEXT.__text: 0x73c9c
   __TEXT.__auth_stubs: 0xf00
-  __TEXT.__objc_methlist: 0x543c
-  __TEXT.__cstring: 0x4bc4
-  __TEXT.__oslogstring: 0xe7a6
+  __TEXT.__objc_methlist: 0x544c
+  __TEXT.__cstring: 0x4c22
+  __TEXT.__oslogstring: 0xe817
   __TEXT.__gcc_except_tab: 0xb38
-  __TEXT.__const: 0x128
+  __TEXT.__const: 0x158
   __TEXT.__ustring: 0x8
   __TEXT.diag_actions: 0x4706
-  __TEXT.__unwind_info: 0x1468
+  __TEXT.__unwind_info: 0x146c
   __TEXT.__objc_classname: 0x926
-  __TEXT.__objc_methname: 0xde79
+  __TEXT.__objc_methname: 0xdef1
   __TEXT.__objc_methtype: 0x1f15
-  __TEXT.__objc_stubs: 0x9da0
+  __TEXT.__objc_stubs: 0x9de0
   __DATA_CONST.__got: 0x260
-  __DATA_CONST.__const: 0x24f8
+  __DATA_CONST.__const: 0x2508
   __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xab58
-  __DATA_CONST.__objc_selrefs: 0x32d0
+  __DATA_CONST.__objc_const: 0xab88
+  __DATA_CONST.__objc_selrefs: 0x32e0
   __DATA_CONST.__objc_arraydata: 0x470
   __AUTH_CONST.__const: 0x5c0
-  __AUTH_CONST.__cfstring: 0x62c0
+  __AUTH_CONST.__cfstring: 0x6380
   __AUTH_CONST.__objc_const: 0x1c50
   __AUTH_CONST.__objc_dictobj: 0x370
   __AUTH_CONST.__objc_intobj: 0x2b8

   __DATA.__objc_protorefs: 0x18
   __DATA.__objc_classrefs: 0x3a8
   __DATA.__objc_superrefs: 0x1d8
-  __DATA.__objc_ivar: 0x660
+  __DATA.__objc_ivar: 0x664
   __DATA.__data: 0xb18
   __DATA.__bss: 0x1f8
   __DATA_DIRTY.__objc_data: 0x4b0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FA931451-31F3-3F3B-8905-F2B3B06D5535
-  Functions: 2115
-  Symbols:   7761
-  CStrings:  5639
+  UUID: 361894C7-3E1A-3AB5-A5F3-4408D7CE4D06
+  Functions: 2117
+  Symbols:   7768
+  CStrings:  5657
 
Symbols:
+ -[DiagnosticPipelineOutlet logRequiresUploadConsent:]
+ -[SystemProperties basebandFirmwareVersion]
+ _OBJC_IVAR_$_SystemProperties._basebandFirmwareVersion
+ ___block_descriptor_57_e8_32s40r48r_e25_v32?0"NSString"8Q16^B24ls32l8r40l8r48l8
+ _objc_msgSend$basebandFirmwareVersion
+ _objc_msgSend$logRequiresUploadConsent:
- ___block_descriptor_49_e8_32r40r_e25_v32?0"NSString"8Q16^B24lr32l8r40l8
CStrings:
+ " Log file at %@ is privacy sensitive and requires user consent for automatic upload"
+ "(%@)"
+ "."
+ "BasebandFirmwareVersion"
+ "ComputeModule"
+ "No baseband firmware version"
+ "Reality"
+ "T@\"NSString\",R,N,V_basebandFirmwareVersion"
+ "Unknown FW Version"
+ "_basebandFirmwareVersion"
+ "basebandFirmwareVersion"
+ "logRequiresUploadConsent:"

```
