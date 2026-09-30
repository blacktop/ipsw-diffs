## FamilyOutOfProcessUIExtension

> `/System/Library/ExtensionKit/Extensions/FamilyOutOfProcessUIExtension.appex/FamilyOutOfProcessUIExtension`

```diff

-245.0.0.0.0
-  __TEXT.__text: 0x15590
-  __TEXT.__auth_stubs: 0x10a0
-  __TEXT.__objc_methlist: 0x700
-  __TEXT.__const: 0xb58
-  __TEXT.__cstring: 0x1137
-  __TEXT.__objc_methname: 0x1a17
-  __TEXT.__constg_swiftt: 0x4e8
-  __TEXT.__swift5_typeref: 0x6a4
-  __TEXT.__swift5_reflstr: 0x483
-  __TEXT.__swift5_fieldmd: 0x418
-  __TEXT.__swift5_capture: 0x20c
-  __TEXT.__oslogstring: 0x81c
+247.1.0.0.0
+  __TEXT.__text: 0x13b54
+  __TEXT.__auth_stubs: 0x1150
+  __TEXT.__objc_methlist: 0x6f8
+  __TEXT.__const: 0xe02
+  __TEXT.__cstring: 0x1275
+  __TEXT.__objc_methname: 0x197f
+  __TEXT.__constg_swiftt: 0x4f8
+  __TEXT.__swift5_typeref: 0x78a
+  __TEXT.__swift5_reflstr: 0x4e7
+  __TEXT.__swift5_fieldmd: 0x494
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_assocty: 0xe0
-  __TEXT.__swift5_proto: 0x58
-  __TEXT.__swift5_types: 0x44
+  __TEXT.__swift5_assocty: 0x128
+  __TEXT.__oslogstring: 0x315
+  __TEXT.__swift5_capture: 0x238
+  __TEXT.__swift5_proto: 0x7c
+  __TEXT.__swift5_types: 0x48
   __TEXT.__objc_classname: 0x48
   __TEXT.__objc_methtype: 0x99c
-  __TEXT.__swift_as_entry: 0x2c
-  __TEXT.__swift_as_ret: 0x3c
+  __TEXT.__swift_as_entry: 0x30
+  __TEXT.__swift_as_ret: 0x30
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x5b8
-  __TEXT.__eh_frame: 0x928
-  __DATA_CONST.__auth_got: 0x850
-  __DATA_CONST.__got: 0x2c8
-  __DATA_CONST.__auth_ptr: 0x320
-  __DATA_CONST.__const: 0x988
+  __TEXT.__unwind_info: 0x620
+  __TEXT.__eh_frame: 0x9c8
+  __DATA_CONST.__auth_got: 0x8a8
+  __DATA_CONST.__got: 0x2e8
+  __DATA_CONST.__auth_ptr: 0x3f0
+  __DATA_CONST.__const: 0x908
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA.__objc_const: 0x16e0
-  __DATA.__objc_selrefs: 0x770
-  __DATA.__objc_data: 0x608
-  __DATA.__data: 0x7a8
-  __DATA.__common: 0x8
-  __DATA.__bss: 0xb10
+  __DATA.__objc_const: 0x17a0
+  __DATA.__objc_selrefs: 0x730
+  __DATA.__objc_data: 0x610
+  __DATA.__data: 0x850
+  __DATA.__bss: 0xf90
+  __DATA.__common: 0x18
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/ExtensionKit.framework/ExtensionKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/AAAFoundationSwift.framework/AAAFoundationSwift
   - /System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle
   - /System/Library/PrivateFrameworks/FamilyCircleUI.framework/FamilyCircleUI
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6FFFBDDD-7490-31B8-9D4F-7657639B3E78
-  Functions: 424
-  Symbols:   187
-  CStrings:  465
+  UUID: 8F4D0B64-0B75-335A-9E3E-3EEDC5430074
+  Functions: 437
+  Symbols:   184
+  CStrings:  451
 
Symbols:
+ _FAAgeRangeErrorDomain
+ _swift_retain_n
- _swift_arrayInitWithCopy
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
- _swift_errorRetain
- _swift_getErrorValue
CStrings:
+ "AGE_FOR_CONFIRMATION_SCREEN_IOS"
+ "Can't pass a nil ageRangeRequestModel!"
+ "Can't pass a nil alertModel for requestType .ageRange"
+ "Continue tapped in onboarding - ST enabled - call PIN UI"
+ "Entry type is: %s"
+ "FamilyOutOfProcessUIExtension/FamilyOutOfProcessUIExtension.swift"
+ "Flow type is: %s"
+ "OnboardingIntroViewController - ST pin succeeded - Updating global state to askFirst"
+ "Request type is: %s"
+ "Using altDSID: %s from model"
+ "Using primary account altDSID: %s"
+ "appleAccountSettings"
+ "com.apple.onboarding.agerange"
+ "fetchAltDSIDWithCompletionHandler:"
+ "fetchFamilyCircleWithCompletionHandler:"
+ "isPartOfFamily: %{bool}d, isChildOrTeen: %{bool}d"
+ "privacyBundleId"
+ "setAgeRangeSharingGlobalState"
+ "setPrivacyLinkForBundles:"
+ "unconfiguredAlert"
+ "v24@?0@\"FAFamilyCircle\"8@\"NSError\"16"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
- " bundleID: %s,\n lowerBound:  %@,\n upperBound: %@"
- "Age sharing global state is set to .always, show the notification instead of the alert"
- "Age sharing global state is set to .never, don't show the age range sharing attestation UI alert"
- "Age sharing global state is set to askFirst, show the UI alert"
- "Age sharing global state shouldn't be unknown here - this is an error"
- "CHILD_AGE_RANGE_ABOUT_LINK_BUTTON_TITLE"
- "Can't post age range notiication, bundleID is nil"
- "Continue tapped, setting age sharing global state for altDSID: %s to askFirst"
- "Didn't find an altDSID, should be the parentCFU flow."
- "Entry Point can't be nil"
- "Entry point unexpectedly found nil"
- "Error saving age sharing global state from extension: %s"
- "Error saving age sharing global state from extension: %s for altDSID: %s"
- "Error saving age sharing global state to askFirst from extension: %s"
- "OnboardingIntroViewController - ST pin succeeded - Updating global state for altDSID: %s to askFirst"
- "OnboardingIntroViewController - ST pin succeeded, for entryPoint: %s"
- "Outside family teen or adult - continue tapped in onboarding - ST enabled - call PIN UI"
- "Setting age sharing global state for kid with altDSID: %s"
- "addAccessoryButton:"
- "ageRange"
- "bundleID"
- "com.apple.ageattestation"
- "continue action isn't handled for this entry point!"
- "continueTapped"
- "globalStateForAltDSID:completion:"
- "handleSetAgeSharingGlobalStateAction: entry point is %s, altDSIDs count is %ld, altDSIDs is %s"
- "headerView"
- "lowerbound"
- "postAgeRangeNotificationWith:lowerAgeBound:upperAgeBound:completion:"
- "selected share type is nil"
- "setGlobalStateForAltDSID:forAltDSID:completion:"
- "settings outside family teen or adult - continue tapped - Updating global state for altDSID: %s to askFirst"
- "showPrivacyLink"
- "thirdPartyApp outside family teen or adult - continue tapped - Updating global state for altDSID: %s to askFirst"
- "upperbound"
- "v16@?0@\"NSError\"8"
- "v20@?0i8@\"NSError\"12"

```
