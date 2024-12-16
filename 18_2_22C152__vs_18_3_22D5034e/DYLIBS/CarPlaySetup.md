## CarPlaySetup

> `/System/Library/PrivateFrameworks/CarPlaySetup.framework/CarPlaySetup`

```diff

-596.10.0.0.0
-  __TEXT.__text: 0x9c64
-  __TEXT.__auth_stubs: 0x430
-  __TEXT.__objc_methlist: 0x6e8
-  __TEXT.__const: 0x98
-  __TEXT.__oslogstring: 0x3dd
-  __TEXT.__cstring: 0xbdb
-  __TEXT.__gcc_except_tab: 0x1a4
-  __TEXT.__unwind_info: 0x290
-  __TEXT.__objc_classname: 0x146
-  __TEXT.__objc_methname: 0x1f3a
-  __TEXT.__objc_methtype: 0x46d
-  __TEXT.__objc_stubs: 0x1dc0
+596.13.0.0.0
+  __TEXT.__text: 0xb15c
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__objc_methlist: 0x7c0
+  __TEXT.__const: 0xa0
+  __TEXT.__oslogstring: 0x472
+  __TEXT.__cstring: 0xc4f
+  __TEXT.__gcc_except_tab: 0x278
+  __TEXT.__unwind_info: 0x2c8
+  __TEXT.__objc_classname: 0x183
+  __TEXT.__objc_methname: 0x20f1
+  __TEXT.__objc_methtype: 0x47b
+  __TEXT.__objc_stubs: 0x1ee0
   __DATA_CONST.__got: 0x210
   __DATA_CONST.__const: 0x240
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8c8
+  __DATA_CONST.__objc_selrefs: 0x920
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__auth_got: 0x228
+  __AUTH_CONST.__auth_got: 0x238
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x1200
-  __AUTH_CONST.__objc_const: 0x12b8
+  __AUTH_CONST.__cfstring: 0x12c0
+  __AUTH_CONST.__objc_const: 0x1518
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x7c
+  __AUTH.__objc_data: 0x320
+  __DATA.__objc_ivar: 0x94
   __DATA.__data: 0x180
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/BaseBoardUI.framework/BaseBoardUI
   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit
   - /System/Library/PrivateFrameworks/ProxCardKit.framework/ProxCardKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 190
-  Symbols:   345
-  CStrings:  624
+  Functions: 207
+  Symbols:   369
+  CStrings:  657
 
Symbols:
+ _AFDeviceSupportsSystemAssistantExperience
+ _OBJC_CLASS_$_CARSetupAssetPrompt
+ _OBJC_CLASS_$_CARSetupAssetUnavailableViewController
+ _OBJC_METACLASS_$_CARSetupAssetPrompt
+ _OBJC_METACLASS_$_CARSetupAssetUnavailableViewController
+ _objc_retain_x24
CStrings:
+ "\x02"
+ "\n\n\n%@"
+ "CARSetupAssetPrompt"
+ "CARSetupAssetUnavailableViewController"
+ "CarPlayProgressSAE"
+ "CarPlayProgressSiri"
+ "SAEIcon"
+ "T@\"NSString\",R,C,N,V_assetDescription"
+ "T@\"UIButton\",R,N,V_primaryButton"
+ "T@\"UIButton\",R,N,V_secondaryButton"
+ "T@?,R,C,N,V_responseHandler"
+ "UNAVAILABLE_CARD_CHECK_UPDATES"
+ "UNAVAILABLE_CARD_MESSAGE"
+ "UNAVAILABLE_CARD_TITLE"
+ "_assetDescription"
+ "_checkForUpdates"
+ "_primaryButton"
+ "_responseHandler"
+ "_secondaryButton"
+ "addConstraint:"
+ "addPrimaryAction:secondaryAction:"
+ "addSubtitleLabelForText:"
+ "addTitleLabelForText:"
+ "asset ready: cancel"
+ "asset ready: check for updates"
+ "assetDescription"
+ "initWithDescription:responseHandler:"
+ "primaryButton"
+ "responseHandler"
+ "secondaryButton"
+ "show system experience CarPlay animation: %{public}@"
+ "show system experience Siri icon: %{public}@"
+ "stringByAppendingFormat:"
+ "v32@0:8@16@24"
- "CarPlayProgress"

```
