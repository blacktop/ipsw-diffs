## AppManagedFeaturesUI

> `/System/Library/PrivateFrameworks/AppManagedFeaturesUI.framework/AppManagedFeaturesUI`

```diff

-46.0.15.0.0
-  __TEXT.__text: 0x22220
-  __TEXT.__objc_methlist: 0x35c
-  __TEXT.__const: 0x1258
-  __TEXT.__cstring: 0xc71
-  __TEXT.__oslogstring: 0x8ee
-  __TEXT.__constg_swiftt: 0x840
-  __TEXT.__swift5_typeref: 0x119e
-  __TEXT.__swift5_reflstr: 0x408
-  __TEXT.__swift5_fieldmd: 0x4f4
+58.40.9.0.0
+  __TEXT.__text: 0x22d18
+  __TEXT.__objc_methlist: 0x374
+  __TEXT.__const: 0x12a8
+  __TEXT.__cstring: 0xd31
+  __TEXT.__oslogstring: 0x8fe
+  __TEXT.__constg_swiftt: 0x858
+  __TEXT.__swift5_typeref: 0x11d8
+  __TEXT.__swift5_reflstr: 0x428
+  __TEXT.__swift5_fieldmd: 0x500
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_assocty: 0x170
   __TEXT.__swift5_proto: 0x68
   __TEXT.__swift5_types: 0x6c
-  __TEXT.__swift5_capture: 0x3d8
-  __TEXT.__swift_as_entry: 0x68
+  __TEXT.__swift5_capture: 0x3fc
+  __TEXT.__swift_as_entry: 0x6c
   __TEXT.__swift_as_ret: 0x6c
-  __TEXT.__swift_as_cont: 0x104
-  __TEXT.__unwind_info: 0xb80
-  __TEXT.__eh_frame: 0x1378
+  __TEXT.__swift_as_cont: 0x110
+  __TEXT.__unwind_info: 0xbd8
+  __TEXT.__eh_frame: 0x1400
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xf0
+  __DATA_CONST.__const: 0x100
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4a8
+  __DATA_CONST.__objc_selrefs: 0x4c0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xf50
-  __AUTH_CONST.__objc_const: 0x8b8
-  __AUTH_CONST.__auth_got: 0xb38
-  __AUTH.__objc_data: 0x838
+  __AUTH_CONST.__const: 0xfc8
+  __AUTH_CONST.__objc_const: 0x8f0
+  __AUTH_CONST.__auth_got: 0xb68
+  __AUTH.__objc_data: 0x858
   __AUTH.__data: 0x558
-  __DATA.__data: 0x758
-  __DATA.__common: 0x28
+  __DATA.__data: 0x770
+  __DATA.__common: 0x30
   - /System/Library/Frameworks/AppManagedFeatures.framework/AppManagedFeatures
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents
+  - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 711
-  Symbols:   637
+  Functions: 730
+  Symbols:   651
   CStrings:  106
 
Symbols:
+ _FBSOpenApplicationOptionKeyPromptUnlockDevice
+ _FBSOpenApplicationOptionKeyUnlockDevice
+ _OBJC_CLASS_$__LSOpenConfiguration
+ __PROPERTIES__TtC20AppManagedFeaturesUI28EnrollmentControllerProvider
+ ___swift_closure_destructor.12Tm
+ ___swift_closure_destructor.67Tm
+ __swiftEmptyDictionarySingleton
+ _objc_msgSend$openApplicationWithBundleIdentifier:usingConfiguration:completionHandler:
+ _objc_msgSend$setFrontBoardOptions:
+ _objc_retain_x28
+ _swift_initStackObject
+ _swift_setDeallocating
+ _symbolic SS_ypt
+ _symbolic _____SgXw 20AppManagedFeaturesUI28EnrollmentControllerProviderC
+ _symbolic _____SgXwz_Xx 20AppManagedFeaturesUI28EnrollmentControllerProviderC
+ _symbolic _____ySS_yptG s23_ContiguousArrayStorageC
+ _symbolic _____ySSypG s18_DictionaryStorageC
- ___swift_closure_destructor.29Tm
- ___swift_closure_destructor.66Tm
- _objc_msgSend$openApplicationWithBundleID:
CStrings:
+ " can require and install software updates that fix critical issues and improve device security. \n\nThis app below can’t be removed while your device is under contract, and it may update automatically even if you’ve turned off automatic app updates in Settings."
+ " can require and install software updates that fix critical issues and improve device security. \n\nThis app below can’t be removed while your device is under contract, and it may update automatically even if you’ve turned off automatic app updates in Settings. You can remove the preferred payment app at any time."
+ "Could not open provider app: %{public}@"
- " may require and install software updates to address critical issues and device security. \n\nThis app below cannot be removed while your device is under contract."
- " may require and install software updates to address critical issues and device security. \n\nThis app below cannot be removed while your device is under contract. You may remove the preferred payment app at any time."
- "Could not open provider app"
```
