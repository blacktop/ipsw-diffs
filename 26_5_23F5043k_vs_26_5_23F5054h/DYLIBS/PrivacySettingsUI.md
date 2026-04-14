## PrivacySettingsUI

> `/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI`

```diff

-1238.4.8.0.0
-  __TEXT.__text: 0x6a7bc
+1238.5.1.0.0
+  __TEXT.__text: 0x6af98
   __TEXT.__auth_stubs: 0x10a0
-  __TEXT.__objc_methlist: 0x40f4
+  __TEXT.__objc_methlist: 0x4104
   __TEXT.__const: 0x334
-  __TEXT.__gcc_except_tab: 0x1334
-  __TEXT.__cstring: 0x80af
-  __TEXT.__oslogstring: 0x2c90
+  __TEXT.__gcc_except_tab: 0x1354
+  __TEXT.__cstring: 0x81cf
+  __TEXT.__oslogstring: 0x2d10
   __TEXT.__dlopen_cstrs: 0xf41
   __TEXT.__swift5_typeref: 0x188
   __TEXT.__swift5_capture: 0x1ac

   __TEXT.__swift5_types: 0xc
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x34
-  __TEXT.__unwind_info: 0x1b90
+  __TEXT.__unwind_info: 0x1bb0
   __TEXT.__eh_frame: 0x640
   __TEXT.__objc_classname: 0xa21
-  __TEXT.__objc_methname: 0xd467
+  __TEXT.__objc_methname: 0xd557
   __TEXT.__objc_methtype: 0x1170
-  __TEXT.__objc_stubs: 0xa260
-  __DATA_CONST.__got: 0x968
-  __DATA_CONST.__const: 0x1ac0
+  __TEXT.__objc_stubs: 0xa3a0
+  __DATA_CONST.__got: 0x988
+  __DATA_CONST.__const: 0x1b78
   __DATA_CONST.__objc_classlist: 0x228
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3228
+  __DATA_CONST.__objc_selrefs: 0x3280
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x180
   __AUTH_CONST.__auth_got: 0x860
-  __AUTH_CONST.__const: 0xa10
-  __AUTH_CONST.__cfstring: 0x6f20
+  __AUTH_CONST.__const: 0xa50
+  __AUTH_CONST.__cfstring: 0x6f80
   __AUTH_CONST.__objc_const: 0x62f0
-  __AUTH_CONST.__objc_intobj: 0x330
+  __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x1208

   - /System/Library/Frameworks/PhotosUI.framework/PhotosUI
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/AccessorySetupKitCore.framework/AccessorySetupKitCore
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
   - /System/Library/PrivateFrameworks/AppConduit.framework/AppConduit
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: ACF04DA9-B35C-3698-8465-5D96C86A2023
-  Functions: 2031
-  Symbols:   7073
-  CStrings:  4579
+  UUID: FC99159D-9A03-3D14-ABAB-0EAA3733812D
+  Functions: 2039
+  Symbols:   7113
+  CStrings:  4605
 
Symbols:
+ -[PUIAccessoriesController findAccessories]
+ _OBJC_CLASS_$_ASAccessoryExperenceRequest
+ _OBJC_CLASS_$_ASAccessoryExperienceLauncher
+ _OBJC_CLASS_$_DAAppAssetManager
+ _OBJC_CLASS_$_UIGraphicsImageRenderer
+ ___43-[PUIAccessoriesController findAccessories]_block_invoke
+ ___43-[PUIAccessoriesController findAccessories]_block_invoke.172
+ ___44-[PUIAccessoriesController specifierForApp:]_block_invoke
+ ___44-[PUIAccessoriesController specifierForApp:]_block_invoke.133
+ ___44-[PUIAccessoriesController specifierForApp:]_block_invoke.cold.1
+ ___44-[PUIAccessoriesController specifierForApp:]_block_invoke_2
+ ___block_descriptor_32_e36_v16?0"ASAccessoryExperienceEvent"8l
+ ___block_descriptor_32_e50_v24?0"ASAccessoryExperienceSession"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s48w_e32_v24?0"DAAppAsset"8"NSError"16ls32l8s40l8w48l8
+ ___block_descriptor_56_e8_32s_e40_v16?0"UIGraphicsImageRendererContext"8ls32l8
+ ___block_descriptor_64_e8_32s40s48s56w_e5_v8?0ls32l8s40l8s48l8w56l8
+ ___block_literal_global.171
+ _objc_msgSend$appName
+ _objc_msgSend$drawInRect:
+ _objc_msgSend$getAppAssetForBundleID:completion:
+ _objc_msgSend$iconData
+ _objc_msgSend$imageWithActions:
+ _objc_msgSend$imageWithData:
+ _objc_msgSend$initWithSize:
+ _objc_msgSend$initWithType:customTitle:customSubtitle:assetDescriptor:
+ _objc_msgSend$isPlaceholder
+ _objc_msgSend$launchExperienceWithRequest:eventHandler:completion:
CStrings:
+ "%s: Failed to get app asset for %@: %@"
+ "-[PUIAccessoriesController specifierForApp:]_block_invoke"
+ "ACCESSORY_SETUP_DISCOVER_BUTTON"
+ "AccessoryExperienceEvent %@\n"
+ "AccessoryExperienceSession %@ error %@\n"
+ "DISCOVER_BUTTON"
+ "DISCOVER_BUTTON_GROUP"
+ "Find accessories tapped"
+ "appName"
+ "drawInRect:"
+ "findAccessories"
+ "getAppAssetForBundleID:completion:"
+ "iconData"
+ "imageWithActions:"
+ "imageWithData:"
+ "initWithSize:"
+ "initWithType:customTitle:customSubtitle:assetDescriptor:"
+ "isPlaceholder"
+ "launchExperienceWithRequest:eventHandler:completion:"
+ "v16@?0@\"ASAccessoryExperienceEvent\"8"
+ "v16@?0@\"UIGraphicsImageRendererContext\"8"
+ "v24@?0@\"ASAccessoryExperienceSession\"8@\"NSError\"16"
+ "v24@?0@\"DAAppAsset\"8@\"NSError\"16"

```
