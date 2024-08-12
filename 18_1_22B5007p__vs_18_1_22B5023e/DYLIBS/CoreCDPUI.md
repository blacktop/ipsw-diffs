## CoreCDPUI

> `/System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI`

```diff

-380.1.0.0.0
-  __TEXT.__text: 0x6fa14
-  __TEXT.__auth_stubs: 0x1ec0
-  __TEXT.__objc_methlist: 0x30e0
-  __TEXT.__const: 0x2b14
-  __TEXT.__cstring: 0x5f98
-  __TEXT.__oslogstring: 0x3272
-  __TEXT.__gcc_except_tab: 0xcd0
+383.0.0.0.0
+  __TEXT.__text: 0x6e7fc
+  __TEXT.__auth_stubs: 0x1ea0
+  __TEXT.__objc_methlist: 0x30c0
+  __TEXT.__const: 0x2b54
+  __TEXT.__cstring: 0x5ec8
+  __TEXT.__oslogstring: 0x3142
+  __TEXT.__gcc_except_tab: 0xcc0
   __TEXT.__dlopen_cstrs: 0x28e
   __TEXT.__constg_swiftt: 0x13e0
-  __TEXT.__swift5_typeref: 0x6bea
+  __TEXT.__swift5_typeref: 0x6c08
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_reflstr: 0xb10
   __TEXT.__swift5_fieldmd: 0xb28
-  __TEXT.__swift5_assocty: 0x2c0
-  __TEXT.__swift5_proto: 0xd4
+  __TEXT.__swift5_assocty: 0x2d8
+  __TEXT.__swift5_proto: 0xd8
   __TEXT.__swift5_types: 0xcc
-  __TEXT.__swift5_capture: 0x474
+  __TEXT.__swift5_capture: 0x424
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x1cd0
+  __TEXT.__unwind_info: 0x1c68
   __TEXT.__eh_frame: 0x488
-  __TEXT.__objc_classname: 0xce6
-  __TEXT.__objc_methname: 0xba2f
-  __TEXT.__objc_methtype: 0x2b71
-  __TEXT.__objc_stubs: 0x8280
-  __DATA_CONST.__got: 0xd28
-  __DATA_CONST.__const: 0x1298
-  __DATA_CONST.__objc_classlist: 0x270
+  __TEXT.__objc_classname: 0xcc6
+  __TEXT.__objc_methname: 0xb8ca
+  __TEXT.__objc_methtype: 0x2b73
+  __TEXT.__objc_stubs: 0x8160
+  __DATA_CONST.__got: 0xd08
+  __DATA_CONST.__const: 0x1280
+  __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_catlist2: 0x10
   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2798
+  __DATA_CONST.__objc_selrefs: 0x2750
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x138
-  __AUTH_CONST.__auth_got: 0xf70
-  __AUTH_CONST.__auth_ptr: 0x9f8
-  __AUTH_CONST.__const: 0x1bf0
-  __AUTH_CONST.__cfstring: 0x29e0
-  __AUTH_CONST.__objc_const: 0x122e8
-  __AUTH.__objc_data: 0x2038
+  __DATA_CONST.__objc_superrefs: 0x130
+  __AUTH_CONST.__auth_got: 0xf60
+  __AUTH_CONST.__auth_ptr: 0xa20
+  __AUTH_CONST.__const: 0x1b58
+  __AUTH_CONST.__cfstring: 0x29c0
+  __AUTH_CONST.__objc_const: 0x121a0
+  __AUTH.__objc_data: 0x1fe8
   __AUTH.__data: 0xf40
   __DATA.__objc_ivar: 0x380
   __DATA.__data: 0x2148
   __DATA.__objc_stublist: 0x18
-  __DATA.__bss: 0x1c40
+  __DATA.__bss: 0x1cc0
   __DATA.__common: 0xc8
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2780
-  Symbols:   2075
-  CStrings:  3079
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 2760
+  Symbols:   2077
+  CStrings:  3060
 
Symbols:
+ _OBJC_CLASS_$_CDPCustodianRecoveryController
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _OBJC_CLASS_$_AACustodianController
- _OBJC_CLASS_$_AACustodianRecoveryRequestContext
- _OBJC_CLASS_$_CDPCustodianRecoveryInfo
- _OBJC_CLASS_$_CDPUICustodianRecoveryController
- _OBJC_METACLASS_$_CDPUICustodianRecoveryController
CStrings:
+ "\x06(!"
+ "\"Custodian recovery session started with sessionID: %!@(MISSING), error: %!@(MISSING)\""
+ "\"No escape options were presented.\""
+ "\"Starting a new recovery recovery session...\""
+ "\"Starting spinner while attempting CDP join\""
+ "\"Stopping spinner: Attempting circle join completed with error %!@(MISSING)\""
+ "@\"CDPUIInfoViewController\""
+ "REMOTE_SECRET_ENTRY_DELETE_ICLOUD_DATA"
+ "_activityIndicator"
+ "_cancelButtonForSwiftUIHostingController"
+ "_resetCompletedView"
+ "_sendEscapeOfferPresentedEventWithOptions:"
+ "_setResetCompletedView:"
+ "isSubsetOfContextTypeSignIn:"
+ "local-secret-entry-view"
+ "remote-secret-entry-view"
+ "startSpinning"
+ "stopSpinning"
+ "\xf0!"
- "\x06&!"
- "\"Custodian recovery session started with success: %!{(MISSING)BOOL}d\""
- "\"Failed to obtain recoverySession with error: %!@(MISSING)\""
- "@\"AACustodianController\""
- "@\"Attempting to fetch custodian recovery keys\""
- "@\"Failed to fetch recovery keys for sessionID: %!@(MISSING) with error: %!@(MISSING)\""
- "@\"Successfuly obtained custodian recovery session: %!@(MISSING)\""
- "@\"Successfuly obtained recovery keys for sessionID: %!@(MISSING)\""
- "@\"Successfuly validated custodian recovery code for custodian with UUID: %!@(MISSING)\""
- "@\"Validation of custodian recovery code for custodian with UUID: %!@(MISSING) failed with error: %!@(MISSING)\""
- "CDPRemoteSecret"
- "CDPUICustodianRecoveryController"
- "Pin Entry View's first responder status: %!{(MISSING)bool}d"
- "Swift/UnsafeRawBufferPointer.swift"
- "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
- "_custodianController"
- "_fetchRecoveryInfoWithCompletion:"
- "_makeEventForEscapeOfferPresentedWithOptions:"
- "_recoverySession"
- "custodianUUID"
- "fetchCustodianRecoveryKeysWithSessionID:completion:"
- "initWithWrappedRKC:wrappingKey:custodianUUID:"
- "initWithWrappedRKC:wrappingKey:custodianUUID:recordBuildVersion:"
- "local_secret_entry_view"
- "recordBuildVersion"
- "remote_secret_entry_view"
- "setOwnerAppleID:"
- "setRecoveryCode:"
- "setRecoverySessionID:"
- "setWritingToolsAllowedInputOptions:"
- "startCustodianRecoveryWithContext:completion:"
- "v24@?0@\"AACustodianDataRecoveryKeys\"8@\"NSError\"16"
- "v24@?0@\"AACustodianRecoveryRequestContext\"8@\"NSError\"16"
- "validateCustodianRecoveryCodeWithContext:completion:"
- "wrappedRKC"
- "wrappingKey"
- "writingToolsAllowedInputOptions"
- "\xf1"

```
