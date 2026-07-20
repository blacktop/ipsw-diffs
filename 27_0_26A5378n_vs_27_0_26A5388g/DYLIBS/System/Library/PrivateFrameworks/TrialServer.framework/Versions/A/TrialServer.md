## TrialServer

> `/System/Library/PrivateFrameworks/TrialServer.framework/Versions/A/TrialServer`

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
-  __TEXT.__text: 0x16a49c
+508.0.0.0.0
+  __TEXT.__text: 0x16a4d8
   __TEXT.__delay_stubs: 0x80
-  __TEXT.__delay_helper: 0xb60
+  __TEXT.__delay_helper: 0xa28
+  __TEXT.__lazy_helpers: 0xe8
   __TEXT.__objc_methlist: 0xc73c
   __TEXT.__const: 0xefc
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__cstring: 0x16e9c
+  __TEXT.__cstring: 0x16e2a
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x14
   __TEXT.__swift5_fieldmd: 0x10

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1218
+  __DATA_CONST.__const: 0x1210
   __DATA_CONST.__objc_classlist: 0x9c0
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x268

   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x630
   __DATA_CONST.__objc_arraydata: 0x380
-  __DATA_CONST.__got: 0x1440
+  __DATA_CONST.__got: 0x1430
   __AUTH_CONST.__const: 0x79d0
-  __AUTH_CONST.__cfstring: 0xf0c0
+  __AUTH_CONST.__cfstring: 0xf0a0
   __AUTH_CONST.__objc_const: 0x181e8
+  __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0xe58
   __AUTH_CONST.__objc_arrayobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x1230
+  __AUTH.__objc_data: 0x10f0
   __AUTH.__data: 0x6e0
   __DATA.__objc_ivar: 0x960
   __DATA.__data: 0x2ae8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xf8
+  __DATA.__bss: 0xa0
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_ivar: 0x1fc
-  __DATA_DIRTY.__objc_data: 0x4fb0
+  __DATA_DIRTY.__objc_data: 0x50f0
   __DATA_DIRTY.__data: 0x14
-  __DATA_DIRTY.__bss: 0x3e8
+  __DATA_DIRTY.__bss: 0x440
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /System/Library/PrivateFrameworks/SpeechObjects.framework/Versions/A/Frameworks/DictationServices.framework/Versions/A/DictationServices
   - /System/Library/PrivateFrameworks/SpeechObjects.framework/Versions/A/SpeechObjects
   - /System/Library/PrivateFrameworks/Trial.framework/Versions/A/Trial
-  - /System/Library/PrivateFrameworks/TrialEncryption.framework/Versions/A/TrialEncryption
   - /System/Library/PrivateFrameworks/TrialProto.framework/Versions/A/TrialProto
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libParallelCompression.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   Functions: 5110
-  Symbols:   12417
-  CStrings:  4253
+  Symbols:   12418
+  CStrings:  4251
 
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
~ -[TRIPushNotificationHandler _handleDeploymentNotification:] : 700 -> 732
~ -[TRIPushNotificationHandler _handleRollbackNotification:] : 1236 -> 1264
CStrings:
+ "Jul 10 2026"
+ "TrialXP-508"
- "/System/Library/PrivateFrameworks/TrialEncryption.framework/Versions/A/TrialEncryption"
- "Jun 26 2026"
- "TrialXP-507"
- "com.apple.assistant.public"
```
