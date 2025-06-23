## SoftwareUpdateSettingsUI

> `/System/Library/PrivateFrameworks/SoftwareUpdateSettingsUI.framework/SoftwareUpdateSettingsUI`

```diff

-486.0.0.0.4
-  __TEXT.__text: 0x107ce4
+492.0.0.0.5
+  __TEXT.__text: 0x107d28
   __TEXT.__auth_stubs: 0x990
   __TEXT.__objc_methlist: 0x4b0c
   __TEXT.__cstring: 0x9ee9
-  __TEXT.__oslogstring: 0x158e4
+  __TEXT.__oslogstring: 0x15904
   __TEXT.__gcc_except_tab: 0x4bb0
   __TEXT.__dlopen_cstrs: 0x658
   __TEXT.__const: 0x62

   __TEXT.__unwind_info: 0x1798
   __TEXT.__eh_frame: 0xf0
   __TEXT.__objc_classname: 0x6f5
-  __TEXT.__objc_methname: 0xe4c0
-  __TEXT.__objc_methtype: 0x246f
+  __TEXT.__objc_methname: 0xe4e0
+  __TEXT.__objc_methtype: 0x247c
   __TEXT.__objc_stubs: 0x9740
   __DATA_CONST.__got: 0x6d8
-  __DATA_CONST.__const: 0x99d8
+  __DATA_CONST.__const: 0x99b8
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x88

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B399D687-C213-31B4-87B8-15620E66C5B2
+  UUID: BB8EA75E-BAD6-3A45-9560-68418180F0FB
   Functions: 2100
-  Symbols:   10910
+  Symbols:   10902
   CStrings:  4236
 
Symbols:
+ -[SUSUIMockedTipsManager contentDidBecomeAvailableWithTitle:andContent:learnMoreLinkUrl:imageSystemName:]
+ ___os_log_helper_16_2_5_8_64_8_66_8_66_8_66_8_66
+ _objc_msgSend$configureManualComingSoonTipWithTitle:andContent:learnMoreLink:imageSystemName:
- -[SUSUIMockedTipsManager contentDidBecomeAvailableWithTitle:andContent:learnMoreLinkUrl:]
- ___os_log_helper_16_2_4_8_64_8_66_8_66_8_66
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_SoftwareUpdateSettingsUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_SoftwareUpdateSettingsUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_SoftwareUpdateSettingsUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_SoftwareUpdateSettingsUI
- _objc_msgSend$configureManualComingSoonTipWithTitle:andContent:learnMoreLink:
Functions:
~ -[SUSUIMockedTipsManager contentDidBecomeAvailableWithTitle:andContent:learnMoreLinkUrl:] -> -[SUSUIMockedTipsManager contentDidBecomeAvailableWithTitle:andContent:learnMoreLinkUrl:imageSystemName:] : 528 -> 576
~ ___os_log_helper_16_2_4_8_64_8_66_8_66_8_66 -> ___os_log_helper_16_2_5_8_64_8_66_8_66_8_66_8_66 : 128 -> 148
CStrings:
+ "[XCUI correlationId: %@] XCUI Testing - Displaying Coming Soon Tip:\n\tTitle: %{public}@\n\tContent: %{public}@\n\tLearn More URL: %{public}@\n\tImage System Name: %{public}@"
+ "configureManualComingSoonTipWithTitle:andContent:learnMoreLink:imageSystemName:"
+ "contentDidBecomeAvailableWithTitle:andContent:learnMoreLinkUrl:imageSystemName:"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40"
- "[XCUI correlationId: %@] XCUI Testing - Displaying Coming Soon Tip:\n\tTitle: %{public}@\n\tContent: %{public}@\n\tLearn More URL: %{public}@"
- "configureManualComingSoonTipWithTitle:andContent:learnMoreLink:"
- "contentDidBecomeAvailableWithTitle:andContent:learnMoreLinkUrl:"
- "v40@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32"

```
