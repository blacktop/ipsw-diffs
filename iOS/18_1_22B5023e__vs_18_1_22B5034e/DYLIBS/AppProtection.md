## AppProtection

> `/System/Library/PrivateFrameworks/AppProtection.framework/AppProtection`

```diff

-35.0.0.0.0
-  __TEXT.__text: 0x9108c
-  __TEXT.__auth_stubs: 0x1e80
-  __TEXT.__objc_methlist: 0xd08
-  __TEXT.__const: 0x3670
-  __TEXT.__oslogstring: 0x3408
-  __TEXT.__cstring: 0x4b64
-  __TEXT.__swift5_typeref: 0x26d2
+35.1.1.0.0
+  __TEXT.__text: 0x94c4c
+  __TEXT.__auth_stubs: 0x1ed0
+  __TEXT.__delay_helper: 0xc8
+  __TEXT.__objc_methlist: 0xd60
+  __TEXT.__const: 0x3660
+  __TEXT.__oslogstring: 0x34c8
+  __TEXT.__cstring: 0x4d54
+  __TEXT.__swift5_typeref: 0x2798
   __TEXT.__swift5_fieldmd: 0x1a14
-  __TEXT.__constg_swiftt: 0x2f2c
+  __TEXT.__constg_swiftt: 0x2f4c
   __TEXT.__swift5_reflstr: 0x16ff
   __TEXT.__swift5_builtin: 0x154
   __TEXT.__swift5_assocty: 0x420
-  __TEXT.__swift5_capture: 0x1234
+  __TEXT.__swift5_capture: 0x12a0
   __TEXT.__swift5_protos: 0xa4
   __TEXT.__swift5_proto: 0x290
   __TEXT.__swift5_types: 0x22c
   __TEXT.__swift5_mpenum: 0x50
-  __TEXT.__unwind_info: 0x2048
-  __TEXT.__eh_frame: 0x2778
-  __TEXT.__objc_classname: 0x1f6
-  __TEXT.__objc_methname: 0x1e75
-  __TEXT.__objc_methtype: 0x628
-  __TEXT.__objc_stubs: 0x440
-  __DATA_CONST.__got: 0x558
-  __DATA_CONST.__const: 0x338
-  __DATA_CONST.__objc_classlist: 0x220
-  __DATA_CONST.__objc_protolist: 0x180
+  __TEXT.__unwind_info: 0x20f8
+  __TEXT.__eh_frame: 0x28a8
+  __TEXT.__objc_classname: 0x230
+  __TEXT.__objc_methname: 0x1f23
+  __TEXT.__objc_methtype: 0x65f
+  __TEXT.__objc_stubs: 0x4a0
+  __DATA_CONST.__got: 0x560
+  __DATA_CONST.__const: 0x348
+  __DATA_CONST.__objc_classlist: 0x228
+  __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x878
+  __DATA_CONST.__objc_selrefs: 0x8a8
   __DATA_CONST.__objc_protorefs: 0xf8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xf48
-  __AUTH_CONST.__auth_ptr: 0x938
-  __AUTH_CONST.__const: 0x5e68
-  __AUTH_CONST.__cfstring: 0x4e0
-  __AUTH_CONST.__objc_const: 0x4000
-  __AUTH.__objc_data: 0x19f0
-  __AUTH.__data: 0x1de8
-  __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x1f00
-  __DATA.__bss: 0x3ab0
-  __DATA.__common: 0xd8
+  __DATA_CONST.__objc_superrefs: 0x10
+  __AUTH_CONST.__auth_got: 0xf70
+  __AUTH_CONST.__auth_ptr: 0x940
+  __AUTH_CONST.__const: 0x6000
+  __AUTH_CONST.__cfstring: 0x520
+  __AUTH_CONST.__objc_const: 0x4158
+  __AUTH.__objc_data: 0x1a40
+  __AUTH.__data: 0x1dd8
+  __DATA.__objc_ivar: 0x10
+  __DATA.__data: 0x1f90
+  __DATA.__bss: 0x3ac0
+  __DATA.__common: 0xe0
   __DATA_DIRTY.__objc_data: 0x408
-  __DATA_DIRTY.__data: 0x800
+  __DATA_DIRTY.__data: 0x808
   __DATA_DIRTY.__bss: 0x2f0
   __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
+  - /System/Library/PrivateFrameworks/PrivacyDisclosureCore.framework/PrivacyDisclosureCore
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libAccessibility.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3125
-  Symbols:   813
-  CStrings:  1205
+  Functions: 3178
+  Symbols:   831
+  CStrings:  1231
 
Symbols:
+ _dispatch_queue_create
+ _OBJC_CLASS_$_PDCPreflightManager
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dlopen
CStrings:
+ "/System/Library/PrivateFrameworks/PrivacyDisclosureCore.framework/PrivacyDisclosureCore"
+ "com.apple.appprotection.disclosure"
+ "errorPreventingMutatingHiddenState(ofAppRecord:isHidden:)"
+ "fileExistsAtPath:"
+ "@\"PDCPreflightManager\""
+ "isAppHidingAvailable"
+ "initWithPreflightManger:"
+ "errorPreventingMutatingLockedState(ofAppRecord:isHidden:isLocked:)"
+ "_preflightManager"
+ "Backup does not exist on disk, writing one out now"
+ "Can't construct Array with count < 0"
+ "APPrivacyDisclosureAdapter"
+ "applicationRequiresPreflight:"
+ "couldn't get records for %!s(MISSING): %!@(MISSING)"
+ "Swift/Array.swift"
+ "APPrivacyDisclosureInterface"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "cannot be locked when app requires privacy preflight"
+ "cannot be hidden when app requires privacy preflight"
+ "B24@0:8@\"LSApplicationRecord\"16"
+ "initWithTargetQueue:"
+ "could not write backup: %!@(MISSING)"
+ "Cannot lock or hide an app that requires privacy preflight"
+ "Successfully wrote backup."
+ "\x01"
+ "requiresPreflightForApplicationRecord:"
+ "isAppLockingAvailable"
+ "%!l(MISSING)d users for service %!s(MISSING)"
+ "fetchUsersForRecord:completion:"
+ "Cannot hide a critical alert app"
- "errorPreventingMutatingLockedState(ofAppRecord:isHidden:)"
- "setOptionMaxBiometryFailures:"
- "errorPreventingMutatingHiddenState(ofAppRecord:)"
- "setOptionNoFailureUI:"

```
