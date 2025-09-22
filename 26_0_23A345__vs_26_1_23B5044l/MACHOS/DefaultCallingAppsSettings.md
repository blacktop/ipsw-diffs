## DefaultCallingAppsSettings

> `/System/Library/Settings/DefaultApps/DefaultCallingAppsSettings.plugin/DefaultCallingAppsSettings`

```diff

-383.100.1.2.1
-  __TEXT.__text: 0x13b8c
-  __TEXT.__auth_stubs: 0xd10
+383.200.21.0.0
+  __TEXT.__text: 0x13594
+  __TEXT.__auth_stubs: 0xcf0
   __TEXT.__objc_methlist: 0x334
-  __TEXT.__const: 0xa62
-  __TEXT.__swift5_typeref: 0x733
+  __TEXT.__const: 0x982
+  __TEXT.__swift5_typeref: 0x721
   __TEXT.__swift5_capture: 0x218
-  __TEXT.__swift5_reflstr: 0x323
-  __TEXT.__swift5_assocty: 0xe0
-  __TEXT.__constg_swiftt: 0x5b0
+  __TEXT.__swift5_reflstr: 0x313
+  __TEXT.__swift5_assocty: 0xc8
+  __TEXT.__constg_swiftt: 0x56c
   __TEXT.__swift5_fieldmd: 0x2b8
-  __TEXT.__cstring: 0x107f
-  __TEXT.__oslogstring: 0x232
-  __TEXT.__objc_methname: 0xa99
-  __TEXT.__swift5_proto: 0x4c
-  __TEXT.__swift5_types: 0x34
-  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__cstring: 0x10bf
+  __TEXT.__oslogstring: 0x2f2
+  __TEXT.__objc_methname: 0xabd
+  __TEXT.__swift5_proto: 0x40
+  __TEXT.__swift5_types: 0x30
   __TEXT.__objc_classname: 0x30
   __TEXT.__objc_methtype: 0x10d
   __TEXT.__swift_as_entry: 0x38
-  __TEXT.__swift_as_ret: 0x38
+  __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x5d0
+  __TEXT.__unwind_info: 0x5c8
   __TEXT.__eh_frame: 0x8c4
-  __DATA_CONST.__auth_got: 0x688
-  __DATA_CONST.__got: 0x1c8
+  __DATA_CONST.__auth_got: 0x678
+  __DATA_CONST.__got: 0x1b8
   __DATA_CONST.__auth_ptr: 0x3a8
   __DATA_CONST.__const: 0x778
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA.__objc_const: 0x710
+  __DATA.__objc_const: 0x730
   __DATA.__objc_selrefs: 0x3f8
-  __DATA.__objc_data: 0x520
-  __DATA.__data: 0x690
-  __DATA.__bss: 0x9f8
-  __DATA.__common: 0x1a0
+  __DATA.__objc_data: 0x528
+  __DATA.__data: 0x658
+  __DATA.__bss: 0x878
+  __DATA.__common: 0x140
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI

   - /System/Library/PrivateFrameworks/DefaultAppsSettings.framework/DefaultAppsSettings
   - /System/Library/PrivateFrameworks/FTServices.framework/FTServices
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
+  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /System/Library/PrivateFrameworks/_IconServices_SwiftUI.framework/_IconServices_SwiftUI

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DD9D142B-0A4B-3E1B-BE0D-CD255BAFAE9A
-  Functions: 422
-  Symbols:   167
-  CStrings:  267
+  UUID: 487496C9-452C-3F54-B453-56568C5B33D4
+  Functions: 414
+  Symbols:   165
+  CStrings:  272
 
Symbols:
+ _OBJC_CLASS_$_MCProfileConnection
+ _TUUserManuallySetDefaultCallingApp
- _OBJC_CLASS_$_TUCallCapabilities
- _OBJC_CLASS_$_TUFeatureFlags
- _defaultAppRelayTelephonySetting
- _setDefaultAppRelayTelephonySetting
CStrings:
+ "CALLING_MDM_RESTRICTION_FOOTER"
+ "Couldn't fetch default %{public}s app: missing workspace or bundle ID"
+ "Couldn't fetch default %{public}s app: no defaultApplication exists"
+ "Fetched nil defaultApp for category %{public}s"
+ "We are on iPad, returning None for default calling app"
+ "isCallingAppMDMAllowed"
+ "isDefaultCallingAppModificationAllowed"
+ "setPreferenceForNoHandlerForCategory:completionHandler:"
+ "sharedConnection"
- "Couldn’t fetch default %{public}s app: missing workspace or bundle ID"
- "callExperiencePhoneAppEnabled"
- "isRelayCallingEnabled"
- "isThumperCallingEnabled"

```
