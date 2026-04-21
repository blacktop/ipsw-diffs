## FitnessSettings

> `/System/Library/PreferenceBundles/FitnessSettings.bundle/FitnessSettings`

```diff

-2026.5.2.0.0
-  __TEXT.__text: 0x1cdcc
+2026.5.4.0.0
+  __TEXT.__text: 0x1cdd0
   __TEXT.__auth_stubs: 0x14a0
-  __TEXT.__objc_stubs: 0x600
+  __TEXT.__objc_stubs: 0x620
   __TEXT.__objc_methlist: 0x24c
   __TEXT.__const: 0x11d2
   __TEXT.__cstring: 0x6ec
-  __TEXT.__objc_methname: 0x926
+  __TEXT.__objc_methname: 0x996
   __TEXT.__oslogstring: 0x20a
-  __TEXT.__objc_classname: 0x163
-  __TEXT.__objc_methtype: 0x240
+  __TEXT.__objc_classname: 0x173
+  __TEXT.__objc_methtype: 0x270
   __TEXT.__swift5_typeref: 0x1fdd
   __TEXT.__constg_swiftt: 0x648
   __TEXT.__swift5_builtin: 0x14

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x638
+  __DATA.__objc_const: 0x630
   __DATA.__objc_selrefs: 0x288
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x160

   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/AppSystemSettingsUI.framework/AppSystemSettingsUI
   - /System/Library/PrivateFrameworks/Blackbeard.framework/Blackbeard
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/Fitness.framework/Fitness

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BE056CC7-DDE0-3569-BFDD-E9147F89C850
-  Functions: 654
+  UUID: A4EFD15D-D1AC-30DF-A8A1-14FDD925D011
+  Functions: 656
   Symbols:   198
   CStrings:  215
 
Symbols:
+ _OBJC_CLASS_$_AUSystemSettingsSpecifiersProvider
- _OBJC_CLASS_$_PSSystemPolicyForApp
CStrings:
+ "@\"AUSystemSettingsSpecifiersProvider\""
+ "AUSystemSettingsSpecifiersProviderDelegate"
+ "T@\"AUSystemSettingsSpecifiersProvider\",&,N,V_systemSpecifiersProvider"
+ "_systemSpecifiersProvider"
+ "initWithApplicationBundleIdentifier:"
+ "presentViewController:animated:completion:"
+ "setSystemSpecifiersProvider:"
+ "systemSettingsSpecifiersProvider:presentViewController:animated:"
+ "systemSettingsSpecifiersProviderDidReloadSpecifiers:"
+ "systemSpecifiersProvider"
+ "v24@0:8@\"AUSystemSettingsSpecifiersProvider\"16"
+ "v36@0:8@\"AUSystemSettingsSpecifiersProvider\"16@\"UIViewController\"24B32"
+ "v36@0:8@16@24B32"
- "@\"PSSystemPolicyForApp\""
- "PSSystemPolicyForAppDelegate"
- "T@\"PSSystemPolicyForApp\",&,N,V_appPolicy"
- "_appPolicy"
- "appPolicy"
- "initWithBundleIdentifier:"
- "setAppPolicy:"
- "showController:animate:"
- "specifiersForPolicyOptions:force:"
- "systemPolicyForApp:didUpdateForSystemPolicyOptions:withValue:"
- "v28@0:8@\"UIViewController\"16B24"
- "v40@0:8@\"PSSystemPolicyForApp\"16Q24@32"
- "v40@0:8@16Q24@32"

```
