## GenerativeModels

> `/System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels`

```diff

-209.29.0.0.0
-  __TEXT.__text: 0xb06b8
-  __TEXT.__auth_stubs: 0x29d0
-  __TEXT.__objc_methlist: 0x37c
-  __TEXT.__cstring: 0x2963
-  __TEXT.__const: 0xb274
-  __TEXT.__constg_swiftt: 0x1f94
-  __TEXT.__swift5_typeref: 0x2d44
+209.32.0.0.0
+  __TEXT.__text: 0xb3920
+  __TEXT.__auth_stubs: 0x2a50
+  __TEXT.__objc_methlist: 0x39c
+  __TEXT.__cstring: 0x2a93
+  __TEXT.__const: 0xb3a4
+  __TEXT.__constg_swiftt: 0x20b4
+  __TEXT.__swift5_typeref: 0x2d74
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_reflstr: 0x1f88
-  __TEXT.__swift5_fieldmd: 0x2788
-  __TEXT.__swift5_assocty: 0x530
-  __TEXT.__swift5_proto: 0x98c
-  __TEXT.__swift5_types: 0x344
+  __TEXT.__swift5_reflstr: 0x1fd8
+  __TEXT.__swift5_fieldmd: 0x27e4
+  __TEXT.__swift5_assocty: 0x548
+  __TEXT.__swift5_proto: 0x9a0
+  __TEXT.__swift5_types: 0x34c
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__oslogstring: 0x2193
+  __TEXT.__oslogstring: 0x2523
   __TEXT.__swift5_capture: 0x3a8
   __TEXT.__swift_as_entry: 0x184
   __TEXT.__swift_as_ret: 0x198
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x2ed0
-  __TEXT.__eh_frame: 0x4f58
+  __TEXT.__unwind_info: 0x2f70
+  __TEXT.__eh_frame: 0x5068
   __TEXT.__objc_classname: 0x21
-  __TEXT.__objc_methname: 0x977
+  __TEXT.__objc_methname: 0xa18
   __TEXT.__objc_methtype: 0xeb
-  __DATA_CONST.__got: 0x9e8
-  __DATA_CONST.__const: 0x220
-  __DATA_CONST.__objc_classlist: 0x70
+  __DATA_CONST.__got: 0xa08
+  __DATA_CONST.__const: 0x228
+  __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x348
+  __DATA_CONST.__objc_selrefs: 0x398
   __DATA_CONST.__objc_protorefs: 0x28
-  __AUTH_CONST.__auth_got: 0x14e8
-  __AUTH_CONST.__const: 0x6020
-  __AUTH_CONST.__objc_const: 0xa70
-  __AUTH.__objc_data: 0x428
-  __AUTH.__data: 0x7a8
-  __DATA.__data: 0x1db8
-  __DATA.__bss: 0xc600
-  __DATA.__common: 0x8
+  __AUTH_CONST.__auth_got: 0x1528
+  __AUTH_CONST.__const: 0x6100
+  __AUTH_CONST.__objc_const: 0xb00
+  __AUTH.__objc_data: 0x5b8
+  __AUTH.__data: 0x7d0
+  __DATA.__data: 0x1e18
+  __DATA.__bss: 0xc880
+  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x28
   __DATA_DIRTY.__data: 0x1530
   __DATA_DIRTY.__bss: 0x6980
+  - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4409B9F2-0F1D-3DD3-90FB-6746395E5204
-  Functions: 4996
-  Symbols:   206
-  CStrings:  598
+  UUID: CCFB3923-366D-3657-ADFC-BD924067CA40
+  Functions: 5055
+  Symbols:   210
+  CStrings:  630
 
Symbols:
+ _OBJC_CLASS_$_ACAccountStore
+ _OBJC_CLASS_$_NSBundle
+ __swift_FORCE_LOAD_$_swiftCompression
+ _os_variant_has_internal_ui
CStrings:
+ "%s returning %{bool}d"
+ "Bypass is enabled for opt-in, returning true"
+ "Could not create UserDefaults with suiteName, will use .standard: %s"
+ "Device has no DSID, checking if device or previous user has toggle enabled."
+ "Device has primary DSID, using to key opt-in status."
+ "Device has primary account without DSID. Will fallback to device setting."
+ "Device or previous Apple Account has opted-in. Returning true."
+ "Fetched value for opt-in status: %{bool}d"
+ "GenerativeModels.OptIn"
+ "No persistent domain for suite %s, no users have toggled toggle off or on."
+ "No previous device or Apple Account has opted-in. Returning false."
+ "No value for user opt-in key %s. Returning false."
+ "Previous key %s has value %{bool}d"
+ "_TtC16GenerativeModels5OptIn"
+ "aa_personID"
+ "aa_primaryAppleAccount"
+ "boolForKey:"
+ "bundleIdentifier"
+ "com.apple.CloudSubscriptionFeatures.gmBypass"
+ "com.apple.CloudSubscriptionFeatures.optIn"
+ "defaultStore"
+ "deviceOrAnyAppleAccountEverOptedIn"
+ "mainBundle"
+ "optedChangeOSVersion raw value: %s"
+ "opted_change_os_version"
+ "persistentDomainForName:"
+ "shouldBeShownInSetupAssistant - majorVersion: %ld, minorVersion: %ld, Opt In state: %s"
+ "standardUserDefaults"
+ "stringForKey:"
+ "userDefaults"
+ "valueForKey:"

```
