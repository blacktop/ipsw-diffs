## TrialServer

> `/System/Library/PrivateFrameworks/TrialServer.framework/TrialServer`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-507.0.0.0.0
-  __TEXT.__text: 0x151730
+508.0.0.0.0
+  __TEXT.__text: 0x151768
   __TEXT.__delay_stubs: 0x80
-  __TEXT.__delay_helper: 0x8cc
+  __TEXT.__delay_helper: 0x794
+  __TEXT.__lazy_helpers: 0xe8
   __TEXT.__objc_methlist: 0xc7b4
   __TEXT.__const: 0xeec
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__cstring: 0x1698c
+  __TEXT.__cstring: 0x16925
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x14
   __TEXT.__swift5_fieldmd: 0x10

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6940
+  __DATA_CONST.__const: 0x6938
   __DATA_CONST.__objc_classlist: 0x9c0
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x270

   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x630
   __DATA_CONST.__objc_arraydata: 0x388
-  __DATA_CONST.__got: 0x1440
+  __DATA_CONST.__got: 0x1430
   __AUTH_CONST.__const: 0x1320
-  __AUTH_CONST.__cfstring: 0xeea0
+  __AUTH_CONST.__cfstring: 0xee80
   __AUTH_CONST.__objc_const: 0x182e0
+  __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0xe40
   __AUTH_CONST.__objc_arrayobj: 0x378
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x1398
+  __AUTH.__objc_data: 0x1258
   __AUTH.__data: 0x6e0
   __DATA.__objc_ivar: 0x968
   __DATA.__data: 0x2b40
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x118
+  __DATA.__bss: 0xb8
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_ivar: 0x1fc
-  __DATA_DIRTY.__objc_data: 0x4e48
+  __DATA_DIRTY.__objc_data: 0x4f88
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x3d8
+  __DATA_DIRTY.__bss: 0x438
   __DATA_DIRTY.__common: 0x38
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
-  - /System/Library/PrivateFrameworks/TrialEncryption.framework/TrialEncryption
   - /System/Library/PrivateFrameworks/TrialProto.framework/TrialProto
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libParallelCompression.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   Functions: 4979
-  Symbols:   12209
-  CStrings:  4228
+  Symbols:   12210
+  CStrings:  4226
 
Symbols:
+ _OBJC_CLASS_$_TRICryptoKitBridge$lazyGOT
+ _OBJC_CLASS_$_TRICryptoKitBridge$lazyGOT$loadHelper_x8
+ _OBJC_CLASS_$_TRICryptoKitBridge$lazyGOT$loadHelper_x8$for$+[TRIAES256GCMCrypto _decryptDataWithCryptoKit:withKey:aad:error:]+0
+ _OBJC_CLASS_$_TRISelfSignedCertificateGenerator$lazyGOT
+ _OBJC_CLASS_$_TRISelfSignedCertificateGenerator$lazyGOT$loadHelper_x8
+ __dyld_lazy_load
+ _lazyLoadFlag$TrialEncryption
- _OBJC_CLASS_$_TRICryptoKitBridge$loadHelper_x8
- _OBJC_CLASS_$_TRICryptoKitBridge$loadHelper_x8$for$+[TRIAES256GCMCrypto _decryptDataWithCryptoKit:withKey:aad:error:]+0
- _OBJC_CLASS_$_TRISelfSignedCertificateGenerator$loadHelper_x8
- _dlopenHelper$TrialEncryption
- _dlopenHelperFlag$TrialEncryption
- _kAssistantPublicPreferenceDomain
Functions:
~ -[TRIPushNotificationHandler _handleDeploymentNotification:] : 644 -> 676
~ -[TRIPushNotificationHandler _handleRollbackNotification:] : 1168 -> 1192
CStrings:
+ "Jul 10 2026"
+ "TrialXP-508"
- "/System/Library/PrivateFrameworks/TrialEncryption.framework/TrialEncryption"
- "Jun 26 2026"
- "TrialXP-507"
- "com.apple.assistant.public"
```
