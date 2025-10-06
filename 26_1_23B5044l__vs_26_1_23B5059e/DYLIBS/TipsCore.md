## TipsCore

> `/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore`

```diff

-822.1.2.0.0
-  __TEXT.__text: 0x9fd2c
-  __TEXT.__auth_stubs: 0x1ee0
-  __TEXT.__objc_methlist: 0x8360
-  __TEXT.__const: 0x1d84
-  __TEXT.__cstring: 0x6047
+822.1.6.0.0
+  __TEXT.__text: 0xa04f0
+  __TEXT.__auth_stubs: 0x1ef0
+  __TEXT.__objc_methlist: 0x8378
+  __TEXT.__const: 0x1da4
+  __TEXT.__cstring: 0x60c7
   __TEXT.__oslogstring: 0x1222
   __TEXT.__gcc_except_tab: 0xfe4
   __TEXT.__ustring: 0x118
-  __TEXT.__constg_swiftt: 0x135c
-  __TEXT.__swift5_typeref: 0xdfc
+  __TEXT.__constg_swiftt: 0x1378
+  __TEXT.__swift5_typeref: 0xe02
   __TEXT.__swift5_reflstr: 0xd22
-  __TEXT.__swift5_fieldmd: 0xc38
+  __TEXT.__swift5_fieldmd: 0xc48
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_assocty: 0x168
   __TEXT.__swift5_proto: 0xf8
-  __TEXT.__swift5_types: 0xd8
-  __TEXT.__swift5_capture: 0x5f0
+  __TEXT.__swift5_types: 0xdc
+  __TEXT.__swift5_capture: 0x610
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift_as_entry: 0x54
   __TEXT.__swift_as_ret: 0x44
-  __TEXT.__unwind_info: 0x2fa8
-  __TEXT.__eh_frame: 0x16a0
+  __TEXT.__unwind_info: 0x2fd0
+  __TEXT.__eh_frame: 0x16d8
   __TEXT.__objc_classname: 0xded
-  __TEXT.__objc_methname: 0xeeeb
+  __TEXT.__objc_methname: 0xef34
   __TEXT.__objc_methtype: 0x189e
-  __TEXT.__objc_stubs: 0x97e0
+  __TEXT.__objc_stubs: 0x9800
   __DATA_CONST.__got: 0x900
   __DATA_CONST.__const: 0x2060
   __DATA_CONST.__objc_classlist: 0x4d0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a38
+  __DATA_CONST.__objc_selrefs: 0x3a58
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x320
   __DATA_CONST.__objc_arraydata: 0xc0
-  __AUTH_CONST.__auth_got: 0xf80
-  __AUTH_CONST.__const: 0x2fd0
-  __AUTH_CONST.__cfstring: 0x52a0
+  __AUTH_CONST.__auth_got: 0xf88
+  __AUTH_CONST.__const: 0x3138
+  __AUTH_CONST.__cfstring: 0x52c0
   __AUTH_CONST.__objc_const: 0xdda0
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1550
-  __AUTH.__data: 0xbb0
+  __AUTH.__data: 0xbb8
   __DATA.__objc_ivar: 0x7b4
-  __DATA.__data: 0x1000
-  __DATA.__bss: 0x1ba0
+  __DATA.__data: 0x1010
+  __DATA.__bss: 0x1bb0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x2748
   __DATA_DIRTY.__data: 0x718

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FFE56391-DE91-3C78-BC5D-8D49B9465CF8
-  Functions: 4806
-  Symbols:   9873
-  CStrings:  4973
+  UUID: 19B1740A-A859-37CD-92A7-851265188B36
+  Functions: 4830
+  Symbols:   9898
+  CStrings:  4983
 
Symbols:
+ +[TPSCommonDefines supportsEntitlement:]
+ +[TPSCommonDefines supportsOpenSensitiveURL]
+ GCC_except_table55
+ ___44+[TPSCommonDefines supportsOpenSensitiveURL]_block_invoke
+ ___block_literal_global.233
+ ___block_literal_global.242
+ ___block_literal_global.251
+ _block_copy_helper.16
+ _block_copy_helper.19
+ _block_descriptor.18
+ _block_descriptor.21
+ _block_destroy_helper.17
+ _block_destroy_helper.20
+ _objc_msgSend$supportsEntitlement:
+ _supportsOpenSensitiveURL.gSupportsSensitiveURL
+ _supportsOpenSensitiveURL.onceToken
+ _symbolic _____ 8TipsCore11SupportFlowO
- GCC_except_table52
- GCC_except_table65
- GCC_except_table67
- GCC_except_table72
- ___block_literal_global.230
- ___block_literal_global.239
- ___block_literal_global.248
CStrings:
+ "Found matching outgoing call event: "
+ "Intent"
+ "Publisher query completed, found "
+ "Query parameters - numbers: "
+ "Using publisher iterator for App.Intent query"
+ "com.apple.springboard.opensensitiveurl"
+ "com.apple.tips.collection"
+ "com.apple.tips.supportflow"
+ "contentType == \"com.apple.tips.supportflow\""
+ "groupIdentifier"
+ "interactionDirection"
+ "supportsEntitlement:"
+ "supportsOpenSensitiveURL"
- "            SELECT count(*)\n            FROM \"App.Intent\"\n            WHERE absoluteTimestamp BETWEEN \""
- "\"\n            AND groupIdentifier IN ("
- ")\n            AND interactionDirection = 3"
- "domainIdentifier"

```
