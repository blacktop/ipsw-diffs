## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-1064.0.0.0.0
-  __TEXT.__text: 0x1a8e0c
+1067.0.0.0.0
+  __TEXT.__text: 0x1a99b4
   __TEXT.__lazy_helpers: 0xa8
-  __TEXT.__objc_methlist: 0xb5c4
+  __TEXT.__objc_methlist: 0xb5ec
   __TEXT.__cstring: 0x11472
-  __TEXT.__const: 0x10d30
+  __TEXT.__const: 0x10db0
   __TEXT.__gcc_except_tab: 0x1bf8
-  __TEXT.__oslogstring: 0x138ed
+  __TEXT.__oslogstring: 0x1397d
   __TEXT.__dlopen_cstrs: 0x325
   __TEXT.__swift5_typeref: 0x3a66
-  __TEXT.__constg_swiftt: 0x2a68
-  __TEXT.__swift5_reflstr: 0x161a
-  __TEXT.__swift5_fieldmd: 0x2630
+  __TEXT.__constg_swiftt: 0x2a74
+  __TEXT.__swift5_reflstr: 0x163a
+  __TEXT.__swift5_fieldmd: 0x2654
   __TEXT.__swift5_builtin: 0x190
-  __TEXT.__swift5_assocty: 0x3c0
-  __TEXT.__swift5_proto: 0xc70
+  __TEXT.__swift5_assocty: 0x3d8
+  __TEXT.__swift5_proto: 0xc74
   __TEXT.__swift5_types: 0x350
   __TEXT.__swift5_mpenum: 0x6c
   __TEXT.__swift5_protos: 0x4c

   __TEXT.__swift_as_cont: 0x510
   __TEXT.__swift5_capture: 0x848
   __TEXT.__unwind_info: 0x6500
-  __TEXT.__eh_frame: 0x7768
+  __TEXT.__eh_frame: 0x77a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3f80
+  __DATA_CONST.__const: 0x3f90
   __DATA_CONST.__objc_classlist: 0x8a8
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5278
+  __DATA_CONST.__objc_selrefs: 0x52a0
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x588
   __DATA_CONST.__objc_arraydata: 0xe0
   __DATA_CONST.__got: 0x1150
-  __AUTH_CONST.__const: 0xd330
-  __AUTH_CONST.__cfstring: 0xd620
-  __AUTH_CONST.__objc_const: 0x26aa0
+  __AUTH_CONST.__const: 0xd3a0
+  __AUTH_CONST.__cfstring: 0xd640
+  __AUTH_CONST.__objc_const: 0x26ad0
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1538
-  __AUTH.__objc_data: 0x1128
+  __AUTH_CONST.__auth_got: 0x1508
+  __AUTH.__objc_data: 0x1130
   __AUTH.__data: 0xc38
   __DATA.__objc_ivar: 0xbd4
-  __DATA.__data: 0x4114
-  __DATA.__bss: 0x17640
-  __DATA.__common: 0xa8
-  __DATA_DIRTY.__objc_data: 0x4b78
+  __DATA.__data: 0x4104
+  __DATA.__bss: 0x176c0
+  __DATA.__common: 0xc0
+  __DATA_DIRTY.__objc_data: 0x4b80
   __DATA_DIRTY.__data: 0xad8
   __DATA_DIRTY.__bss: 0x1a28
   __DATA_DIRTY.__common: 0x48

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9148
-  Symbols:   11664
-  CStrings:  3731
+  Functions: 9165
+  Symbols:   11669
+  CStrings:  3735
 
Symbols:
+ +[AAAppStateProvider appStateForBundleID:appRecord:]
+ +[AAPreferences isWalrusPreEncryptionBlobLoggingEnabled]
+ -[NSError(AppleAccount) aa_isTermsOfServiceUpdateRequired]
+ _kAAProtocolPrefWalrusLogPreEncryptionBlob
+ _objc_msgSend$appStateForBundleID:appRecord:
+ _objc_msgSend$isInternalBuildForSecurityPolicy
+ _objc_msgSend$restrictionReason
- _CGRectEqualToRect
- _CGRectStandardize
CStrings:
+ "AAAppStateProvider: %{public}@ installed=%@ restricted=%@ (rawRestricted=%@ reason=%ld)"
+ "AAWalrusLogPreEncryptionBlob"
+ "Extracted device list ETag: %{private,mask.hash}s"
+ "com.apple.appleaccount.recoveryContact.custodian.privateChannelCreated"
+ "com.apple.appleaccount.recoveryContact.owner.CustodianCountMatchServerCount"
+ "com.apple.appleaccount.recoveryContact.owner.GetCodeLanding"
+ "com.apple.appleaccount.recoveryContact.owner.RecoveryLanding"
+ "cropRect"
+ "imageData"
- "com.apple.appleaccount.recoveryContact.owner.custodianCountMatchServerCount"
- "com.apple.appleaccount.recoveryContact.owner.getCodeLanding"
- "com.apple.appleaccount.recoveryContact.owner.privateChannelCreated"
- "com.apple.appleaccount.recoveryContact.owner.recoveryLanding"
- "com.apple.appleaccount.setupbase"
```
