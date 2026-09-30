## CarPlaySetup

> `/Applications/CarPlaySetup.app/CarPlaySetup`

```diff

-596.13.0.0.0
-  __TEXT.__text: 0x6500
-  __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_stubs: 0xd80
-  __TEXT.__objc_methlist: 0x44c
-  __TEXT.__const: 0x60
-  __TEXT.__objc_classname: 0x169
-  __TEXT.__objc_methname: 0x24f5
-  __TEXT.__objc_methtype: 0x103d
-  __TEXT.__oslogstring: 0x9cf
-  __TEXT.__cstring: 0x140
+606.14.1.0.0
+  __TEXT.__text: 0x7088
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__objc_stubs: 0x11a0
+  __TEXT.__objc_methlist: 0xb54
+  __TEXT.__const: 0x68
+  __TEXT.__objc_classname: 0x19a
+  __TEXT.__objc_methtype: 0x10e7
+  __TEXT.__objc_methname: 0x28bd
+  __TEXT.__oslogstring: 0xa6d
+  __TEXT.__cstring: 0x1a9
   __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__unwind_info: 0x1e8
-  __DATA_CONST.__auth_got: 0x1a8
-  __DATA_CONST.__got: 0x110
-  __DATA_CONST.__const: 0x3b0
-  __DATA_CONST.__cfstring: 0xe0
-  __DATA_CONST.__objc_classlist: 0x30
+  __TEXT.__unwind_info: 0x208
+  __DATA_CONST.__auth_got: 0x1d0
+  __DATA_CONST.__got: 0x178
+  __DATA_CONST.__const: 0x400
+  __DATA_CONST.__cfstring: 0x160
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x18
-  __DATA.__objc_const: 0x2238
-  __DATA.__objc_selrefs: 0x490
-  __DATA.__objc_ivar: 0x28
-  __DATA.__objc_data: 0x1e0
+  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA.__objc_const: 0x1770
+  __DATA.__objc_selrefs: 0x838
+  __DATA.__objc_ivar: 0x38
+  __DATA.__objc_data: 0x280
   __DATA.__data: 0x3c0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/CarPlaySetup.framework/CarPlaySetup
   - /System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories

   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 161
-  Symbols:   98
-  CStrings:  466
+  Functions: 170
+  Symbols:   118
+  CStrings:  530
 
Symbols:
+ _ASCLockupContextStandard
+ _ASCLockupViewSizeSmall
+ _CGRectZero
+ _OBJC_CLASS_$_ASCLockupView
+ _OBJC_CLASS_$_ASCLockupViewGroup
+ _OBJC_CLASS_$_CARSetupHeadUnitPairingPrompt
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_UIFont
+ _OBJC_CLASS_$_UIFontDescriptor
+ _OBJC_CLASS_$_UILabel
+ _OBJC_CLASS_$_UIStackView
+ _OBJC_CLASS_$_UIView
+ _OBJC_METACLASS_$_UIView
+ _UIFontTextStyleTitle2
+ __os_feature_enabled_impl
+ _objc_release_x24
+ _objc_release_x9
+ _objc_retain_x25
+ _objc_retain_x26
CStrings:
+ "\x04"
+ "@\"ASCLockupViewGroup\""
+ "@\"NSArray\""
+ "@\"UILabel\""
+ "@\"UIStackView\""
+ "App Store response for %{public}@: %@"
+ "AppClips"
+ "CARSetupAppClipsView"
+ "CARSetupPassConfiguration"
+ "CarPlay"
+ "CarPlaySetup"
+ "Localizable-Themed"
+ "READY_CARD_APPS"
+ "T@\"ASCLockupViewGroup\",R,N,V_lockupGroup"
+ "T@\"NSArray\",R,N,V_appClipIDs"
+ "T@\"UILabel\",R,N,V_titleLabel"
+ "T@\"UIStackView\",R,N,V_lockupStack"
+ "_appClipIDs"
+ "_lockupGroup"
+ "_lockupRequestForBundleID:withContext:completionBlock:"
+ "_lockupStack"
+ "_titleLabel"
+ "addArrangedSubview:"
+ "addConstraints:"
+ "addSubview:"
+ "app feature enabled, app IDs: %{public}@"
+ "appClipIDs"
+ "arrayWithObjects:count:"
+ "bottomAnchor"
+ "bundleForClass:"
+ "constraintEqualToAnchor:"
+ "constraintEqualToSystemSpacingBelowAnchor:multiplier:"
+ "count"
+ "failed App Store response for %{public}@: %@"
+ "fontDescriptorWithSymbolicTraits:"
+ "fontWithDescriptor:size:"
+ "initWithAppClipIdentifiers:"
+ "initWithAppsView:doneHandler:"
+ "initWithFrame:"
+ "initWithName:"
+ "labelColor"
+ "leadingAnchor"
+ "localizedStringForKey:value:table:"
+ "lockupGroup"
+ "lockupStack"
+ "passConfigurationFromDigitalCarKeyInfo:vehicleName:"
+ "preferredFontDescriptorWithTextStyle:compatibleWithTraitCollection:"
+ "presentAssetReadyPromptForVehicleName:appClipIDs:confirmationHandler:"
+ "promptDirector:wantsToPresentAssetReadyPromptForVehicleName:appClipIDs:confirmationHandler:"
+ "querying App Store for %{public}@"
+ "safeAreaLayoutGuide"
+ "setAxis:"
+ "setFont:"
+ "setGroup:"
+ "setLockupSize:"
+ "setRequest:"
+ "setText:"
+ "setTextAlignment:"
+ "setTextColor:"
+ "setTranslatesAutoresizingMaskIntoConstraints:"
+ "titleLabel"
+ "topAnchor"
+ "trailingAnchor"
+ "traitCollection"
+ "v24@?0@\"ASCLockupRequest\"8@\"NSError\"16"
+ "v40@0:8@\"NSString\"16@\"NSArray\"24@?<v@?>32"
+ "v48@0:8@\"CARSetupPromptDirector\"16@\"NSString\"24@\"NSArray\"32@?<v@?>40"
- "_passConfigurationFromDigitalCarKeyInfo:vehicleName:"
- "presentAssetReadyPromptForVehicleName:confirmationHandler:"
- "promptDirector:wantsToPresentAssetReadyPromptForVehicleName:confirmationHandler:"

```
