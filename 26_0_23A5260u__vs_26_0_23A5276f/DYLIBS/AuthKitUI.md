## AuthKitUI

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI`

```diff

-512.1.3.0.0
-  __TEXT.__text: 0x6e2bc
+514.2.0.0.0
+  __TEXT.__text: 0x6e4e4
   __TEXT.__auth_stubs: 0xc60
-  __TEXT.__objc_methlist: 0x8244
+  __TEXT.__objc_methlist: 0x826c
   __TEXT.__const: 0x3a6
-  __TEXT.__gcc_except_tab: 0xa0c
-  __TEXT.__cstring: 0x4f08
-  __TEXT.__oslogstring: 0x477a
+  __TEXT.__gcc_except_tab: 0xa14
+  __TEXT.__cstring: 0x4f18
+  __TEXT.__oslogstring: 0x4847
   __TEXT.__ustring: 0x2c
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__dlopen_cstrs: 0x71
-  __TEXT.__unwind_info: 0x1d38
+  __TEXT.__unwind_info: 0x1d40
   __TEXT.__objc_classname: 0x154a
-  __TEXT.__objc_methname: 0x17169
+  __TEXT.__objc_methname: 0x17235
   __TEXT.__objc_methtype: 0x472b
-  __TEXT.__objc_stubs: 0x11fc0
+  __TEXT.__objc_stubs: 0x12060
   __DATA_CONST.__got: 0xcc0
-  __DATA_CONST.__const: 0x1610
+  __DATA_CONST.__const: 0x15f8
   __DATA_CONST.__objc_classlist: 0x388
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5b48
+  __DATA_CONST.__objc_selrefs: 0x5b78
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x2a8
   __DATA_CONST.__objc_arraydata: 0x2b8
   __AUTH_CONST.__auth_got: 0x640
   __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0x4b60
-  __AUTH_CONST.__objc_const: 0x16cb0
+  __AUTH_CONST.__cfstring: 0x4ba0
+  __AUTH_CONST.__objc_const: 0x16ce0
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH.__objc_data: 0x1fe0
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x738
+  __DATA.__objc_ivar: 0x73c
   __DATA.__data: 0x1898
   __DATA.__bss: 0x160
   __DATA_DIRTY.__objc_data: 0x320

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 46617D8B-3DA3-3EC6-8CDE-60D05B72DC26
-  Functions: 2863
-  Symbols:   10904
-  CStrings:  6062
+  UUID: A00DAC33-7BCC-334D-A76C-6F8F9B2B2B54
+  Functions: 2869
+  Symbols:   10916
+  CStrings:  6078
 
Symbols:
+ -[AKAppleIDAuthenticationInAppContext forceModalPresentation]
+ -[AKAppleIDAuthenticationInAppContext setForceModalPresentation:]
+ -[AKAppleIDServerUIDataHarvester _clearPendingDOBFromPrimaryAppleAccount]
+ -[AKAppleIDServerUIDataHarvester _clearPendingDOBFromPrimaryAppleAccount].cold.1
+ -[AKAppleIDServerUIDataHarvester _clearPendingDOBFromPrimaryAppleAccount].cold.2
+ -[AKAppleIDServerUIDataHarvester _clearPendingDOBFromPrimaryAppleAccount].cold.3
+ _OBJC_IVAR_$_AKAppleIDAuthenticationInAppContext._forceModalPresentation
+ ___block_literal_global.143
+ ___block_literal_global.72
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_AuthKitUI
+ _objc_msgSend$_clearPendingDOBFromPrimaryAppleAccount
+ _objc_msgSend$forceModalPresentation
+ _objc_msgSend$primaryiCloudAccount
+ _objc_msgSend$saveAccount:error:
+ _objc_msgSend$setContentSize:
+ _objc_msgSend$setPendingDOB:forAccount:
- ___block_literal_global.142
- ___block_literal_global.71
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_AuthKitUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_AuthKitUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_AuthKitUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_AuthKitUI
- _objc_msgSend$isModalInPresentation
CStrings:
+ "Failed to save Apple Account after clearing pending DOB: %@"
+ "Found birthday updated header: %@."
+ "No primary Apple Account found, skipping pendingDOB clear"
+ "Successfully cleared pending DOB from Apple Account"
+ "TB,N,V_forceModalPresentation"
+ "X-Apple-I-Birthday-Updated"
+ "_clearPendingDOBFromPrimaryAppleAccount"
+ "_forceModalPresentation"
+ "forceModalPresentation"
+ "primaryiCloudAccount"
+ "saveAccount:error:"
+ "setContentSize:"
+ "setForceModalPresentation:"
+ "setPendingDOB:forAccount:"
- "isModalInPresentation"

```
