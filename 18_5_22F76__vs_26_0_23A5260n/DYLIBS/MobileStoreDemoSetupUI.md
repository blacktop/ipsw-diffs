## MobileStoreDemoSetupUI

> `/System/Library/PrivateFrameworks/MobileStoreDemoSetupUI.framework/MobileStoreDemoSetupUI`

```diff

-1445.122.3.0.0
-  __TEXT.__text: 0x1690c
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x2108
+1604.0.0.0.0
+  __TEXT.__text: 0x16e14
+  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__objc_methlist: 0x2160
   __TEXT.__const: 0x140
   __TEXT.__gcc_except_tab: 0x2f4
-  __TEXT.__cstring: 0x13ae
-  __TEXT.__oslogstring: 0x1169
+  __TEXT.__cstring: 0x13d7
+  __TEXT.__oslogstring: 0x11a2
   __TEXT.__ustring: 0xc
   __TEXT.__unwind_info: 0x5a8
-  __TEXT.__objc_classname: 0x4e4
-  __TEXT.__objc_methname: 0x61cb
+  __TEXT.__objc_classname: 0x4e6
+  __TEXT.__objc_methname: 0x6290
   __TEXT.__objc_methtype: 0x1a70
-  __TEXT.__objc_stubs: 0x48a0
-  __DATA_CONST.__got: 0x3e0
-  __DATA_CONST.__const: 0x328
+  __TEXT.__objc_stubs: 0x49a0
+  __DATA_CONST.__got: 0x3e8
+  __DATA_CONST.__const: 0x350
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ac8
+  __DATA_CONST.__objc_selrefs: 0x1b08
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x2e8
+  __AUTH_CONST.__auth_got: 0x2f0
   __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__cfstring: 0x17a0
-  __AUTH_CONST.__objc_const: 0x6d98
+  __AUTH_CONST.__objc_const: 0x6dc8
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x134
+  __DATA.__objc_ivar: 0x138
   __DATA.__data: 0x7e0
   __DATA.__bss: 0xc8
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/Frameworks/MapKit.framework/MapKit
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/EmbeddedDataReset.framework/EmbeddedDataReset
   - /System/Library/PrivateFrameworks/IntlPreferences.framework/IntlPreferences

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8077B1E8-601C-3076-8A1A-7FB507B7E41D
-  Functions: 523
-  Symbols:   2396
-  CStrings:  1773
+  UUID: 56B26BEF-F36A-397A-A1B7-AAF92C91E4D1
+  Functions: 531
+  Symbols:   2424
+  CStrings:  1789
 
Symbols:
+ -[MSDDemoSetupViewController viewDidLoad]
+ -[MSDLanguageAndRegionHelper isSiriEnabled]
+ -[MSDLanguageAndRegionHelper setSiriIsEnabled:]
+ -[MSDLanguageAndRegionManager isSiriEnabled]
+ -[MSDLanguageAndRegionManager setSiriIsEnabled:]
+ -[MSDSupportViewController setSolariumEnabled:]
+ -[MSDSupportViewController solariumEnabled]
+ _OBJC_IVAR_$_MSDSupportViewController._solariumEnabled
+ _UIFontTextStyleTitle2
+ ___36-[MSDWelcomeViewController _checkIn]_block_invoke_2
+ ___36-[MSDWelcomeViewController _checkIn]_block_invoke_2.cold.1
+ ___block_descriptor_50_e8_32s40s_e5_v8?0ls32l8s40l8
+ __os_feature_enabled_impl
+ _objc_msgSend$assistantIsEnabled
+ _objc_msgSend$isSiriEnabled
+ _objc_msgSend$preferredFontForTextStyle:
+ _objc_msgSend$secondaryLabelColor
+ _objc_msgSend$setAssistantIsEnabled:
+ _objc_msgSend$setSiriIsEnabled:
+ _objc_msgSend$setSolariumEnabled:
+ _objc_msgSend$solariumEnabled
- ___36-[MSDWelcomeViewController _checkIn]_block_invoke.cold.1
CStrings:
+ "Enabling Siri"
+ "NaturalUI"
+ "OBK/Solarium feature flag is toggled to %d"
+ "OnBoardingKit"
+ "Solarium"
+ "SwiftUI"
+ "TB,N,V_solariumEnabled"
+ "_solariumEnabled"
+ "assistantIsEnabled"
+ "isSiriEnabled"
+ "preferredFontForTextStyle:"
+ "secondaryLabelColor"
+ "setAssistantIsEnabled:"
+ "setSiriIsEnabled:"
+ "setSolariumEnabled:"
+ "solariumEnabled"

```
