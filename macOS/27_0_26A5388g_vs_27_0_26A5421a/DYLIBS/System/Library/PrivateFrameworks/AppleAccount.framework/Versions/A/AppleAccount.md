## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/Versions/A/AppleAccount`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-1064.0.0.0.0
-  __TEXT.__text: 0x28390c
-  __TEXT.__objc_methlist: 0xb32c
+1067.0.0.0.0
+  __TEXT.__text: 0x284144
+  __TEXT.__objc_methlist: 0xb354
   __TEXT.__cstring: 0x104d1
-  __TEXT.__const: 0x48480
+  __TEXT.__const: 0x484f0
   __TEXT.__gcc_except_tab: 0x1aa8
-  __TEXT.__oslogstring: 0x1265d
+  __TEXT.__oslogstring: 0x126ad
   __TEXT.__dlopen_cstrs: 0x2d3
   __TEXT.__swift5_typeref: 0x336a
-  __TEXT.__constg_swiftt: 0x26b8
-  __TEXT.__swift5_reflstr: 0x122a
-  __TEXT.__swift5_fieldmd: 0x2230
+  __TEXT.__constg_swiftt: 0x26c4
+  __TEXT.__swift5_reflstr: 0x123a
+  __TEXT.__swift5_fieldmd: 0x2248
   __TEXT.__swift5_builtin: 0x118
-  __TEXT.__swift5_assocty: 0x328
-  __TEXT.__swift5_proto: 0xb2c
+  __TEXT.__swift5_assocty: 0x340
+  __TEXT.__swift5_proto: 0xb30
   __TEXT.__swift5_types: 0x2f4
   __TEXT.__swift5_mpenum: 0x4c
   __TEXT.__swift5_protos: 0x40

   __TEXT.__swift_as_ret: 0x244
   __TEXT.__swift_as_cont: 0x450
   __TEXT.__swift5_capture: 0x7b8
-  __TEXT.__unwind_info: 0x5fa0
-  __TEXT.__eh_frame: 0x6930
+  __TEXT.__unwind_info: 0x5f98
+  __TEXT.__eh_frame: 0x6938
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2660
+  __DATA_CONST.__const: 0x2670
   __DATA_CONST.__objc_classlist: 0x888
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x50d0
+  __DATA_CONST.__objc_selrefs: 0x50f8
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x580
   __DATA_CONST.__objc_arraydata: 0xe0
   __DATA_CONST.__got: 0x1020
-  __AUTH_CONST.__const: 0x10920
-  __AUTH_CONST.__cfstring: 0xcea0
-  __AUTH_CONST.__objc_const: 0x261e8
+  __AUTH_CONST.__const: 0x10990
+  __AUTH_CONST.__cfstring: 0xcec0
+  __AUTH_CONST.__objc_const: 0x26218
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x12f8
-  __AUTH.__objc_data: 0xfc8
+  __AUTH_CONST.__auth_got: 0x12c8
+  __AUTH.__objc_data: 0xfd0
   __AUTH.__data: 0xb60
   __DATA.__objc_ivar: 0xba4
   __DATA.__data: 0x3fb8
-  __DATA.__bss: 0x14c70
-  __DATA.__common: 0xa48
-  __DATA_DIRTY.__objc_data: 0x4bc8
+  __DATA.__bss: 0x14cf0
+  __DATA.__common: 0xa60
+  __DATA_DIRTY.__objc_data: 0x4bd0
   __DATA_DIRTY.__data: 0xa80
   __DATA_DIRTY.__bss: 0x1af0
   __DATA_DIRTY.__common: 0x50

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8759
-  Symbols:   11422
-  CStrings:  3503
+  Functions: 8772
+  Symbols:   11427
+  CStrings:  3506
 
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
