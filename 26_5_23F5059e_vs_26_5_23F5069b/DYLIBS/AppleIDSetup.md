## AppleIDSetup

> `/System/Library/PrivateFrameworks/AppleIDSetup.framework/AppleIDSetup`

```diff

-90.575.3.0.0
-  __TEXT.__text: 0x2057d0
-  __TEXT.__auth_stubs: 0x26f0
+90.575.6.0.0
+  __TEXT.__text: 0x205ffc
+  __TEXT.__auth_stubs: 0x2710
   __TEXT.__objc_methlist: 0x14bc
-  __TEXT.__const: 0x2b130
+  __TEXT.__const: 0x2b190
   __TEXT.__cstring: 0x34e3
-  __TEXT.__oslogstring: 0x5420
-  __TEXT.__swift5_typeref: 0x91c4
-  __TEXT.__constg_swiftt: 0x8080
+  __TEXT.__oslogstring: 0x55d0
+  __TEXT.__swift5_typeref: 0x9204
+  __TEXT.__constg_swiftt: 0x80a8
   __TEXT.__swift5_builtin: 0x320
-  __TEXT.__swift5_reflstr: 0x4906
-  __TEXT.__swift5_fieldmd: 0x7c20
+  __TEXT.__swift5_reflstr: 0x4936
+  __TEXT.__swift5_fieldmd: 0x7c3c
   __TEXT.__swift5_assocty: 0x978
-  __TEXT.__swift5_proto: 0x26fc
+  __TEXT.__swift5_proto: 0x2700
   __TEXT.__swift5_types: 0xa24
   __TEXT.__swift_as_entry: 0x6fc
   __TEXT.__swift_as_ret: 0x6e8
   __TEXT.__swift5_capture: 0x1f3c
   __TEXT.__swift5_mpenum: 0xfc
-  __TEXT.__swift5_protos: 0xcc
-  __TEXT.__unwind_info: 0x9d90
+  __TEXT.__swift5_protos: 0xd0
+  __TEXT.__unwind_info: 0x9d98
   __TEXT.__eh_frame: 0x107a8
   __TEXT.__objc_classname: 0xa4a
-  __TEXT.__objc_methname: 0x3fa3
+  __TEXT.__objc_methname: 0x3ff3
   __TEXT.__objc_methtype: 0x1210
-  __TEXT.__objc_stubs: 0x2520
-  __DATA_CONST.__got: 0x950
+  __TEXT.__objc_stubs: 0x2580
+  __DATA_CONST.__got: 0x958
   __DATA_CONST.__const: 0xbd0
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd88
+  __DATA_CONST.__objc_selrefs: 0xda0
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x1380
-  __AUTH_CONST.__const: 0x150b0
+  __AUTH_CONST.__auth_got: 0x1390
+  __AUTH_CONST.__const: 0x150c8
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0x6788
-  __AUTH.__objc_data: 0x1c98
+  __AUTH.__objc_data: 0x1ca0
   __AUTH.__data: 0x30e8
   __DATA.__objc_ivar: 0xe8
   __DATA.__data: 0x9258

   - /System/Library/PrivateFrameworks/AAAFoundationSwift.framework/AAAFoundationSwift
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication
+  - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 40ADB15C-E00E-39DD-9BD0-3DEB7625B058
-  Functions: 13463
-  Symbols:   5772
-  CStrings:  1649
+  UUID: 8D31877E-6010-3CA4-A88C-89CAD50D98B6
+  Functions: 13466
+  Symbols:   5778
+  CStrings:  1659
 
Symbols:
+ _OBJC_CLASS_$_AMSAccountEligibilitySyncTask
+ ___swift_memcpy288_8
+ _objc_msgSend$ams_accountID
+ _objc_msgSend$forceSyncAndUpdateForAccountID:timeout:
+ _objc_msgSend$resultWithTimeout:error:
+ _symbolic $s12AppleIDSetup37AMSAccountEligibilitySyncTaskProtocolP
+ _symbolic ______p 12AppleIDSetup37AMSAccountEligibilitySyncTaskProtocolP
- ___swift_memcpy248_8
CStrings:
+ "Failed to refresh POLUS policies: %@"
+ "No account ID available from iTunes account - skipping POLUS policy refresh"
+ "No matching iTunes account found for primary AuthKit account - skipping POLUS policy refresh"
+ "No primary AuthKit account found - skipping POLUS policy refresh"
+ "Refreshing POLUS policies"
+ "Successfully refreshed POLUS policies"
+ "Waiting for POLUS policy sync to complete"
+ "ams_accountID"
+ "forceSyncAndUpdateForAccountID:timeout:"
+ "resultWithTimeout:error:"

```
