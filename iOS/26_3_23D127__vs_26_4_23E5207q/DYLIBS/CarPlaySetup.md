## CarPlaySetup

> `/System/Library/PrivateFrameworks/CarPlaySetup.framework/CarPlaySetup`

```diff

-746.24.2.0.0
-  __TEXT.__text: 0xb8c0
-  __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_methlist: 0x9a4
-  __TEXT.__const: 0xa0
-  __TEXT.__oslogstring: 0x4ab
-  __TEXT.__cstring: 0xec1
-  __TEXT.__gcc_except_tab: 0x278
-  __TEXT.__unwind_info: 0x2d8
-  __TEXT.__objc_classname: 0x1b0
-  __TEXT.__objc_methname: 0x2282
-  __TEXT.__objc_methtype: 0x485
-  __TEXT.__objc_stubs: 0x1fe0
-  __DATA_CONST.__got: 0x218
+774.8.0.0.0
+  __TEXT.__text: 0xc01c
+  __TEXT.__auth_stubs: 0x430
+  __TEXT.__objc_methlist: 0x984
+  __TEXT.__const: 0x98
+  __TEXT.__gcc_except_tab: 0x210
+  __TEXT.__cstring: 0x10fe
+  __TEXT.__oslogstring: 0x4b2
+  __TEXT.__unwind_info: 0x2f8
+  __TEXT.__objc_classname: 0x1ae
+  __TEXT.__objc_methname: 0x2372
+  __TEXT.__objc_methtype: 0x47b
+  __TEXT.__objc_stubs: 0x2140
+  __DATA_CONST.__got: 0x220
   __DATA_CONST.__const: 0x290
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa20
+  __DATA_CONST.__objc_selrefs: 0xa70
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__auth_got: 0x240
+  __AUTH_CONST.__auth_got: 0x228
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x1540
-  __AUTH_CONST.__objc_const: 0x1368
-  __AUTH_CONST.__objc_doubleobj: 0x10
+  __AUTH_CONST.__cfstring: 0x17e0
+  __AUTH_CONST.__objc_const: 0x12a8
   __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0x9c
+  __DATA.__objc_ivar: 0x8c
   __DATA.__data: 0x180
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ProxCardKit.framework/ProxCardKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 20D66546-2090-3B47-835A-0ED8B8FCE265
-  Functions: 217
-  Symbols:   1024
-  CStrings:  859
+  UUID: C6995ED4-FA53-365B-BD37-E86E6208CF8E
+  Functions: 218
+  Symbols:   1030
+  CStrings:  908
 
Symbols:
+ -[CARSetupOnboardingViewController .cxx_destruct]
+ -[CARSetupOnboardingViewController _continue]
+ -[CARSetupOnboardingViewController _proceedToCarKeySetup]
+ -[CARSetupOnboardingViewController doneHandler]
+ -[CARSetupOnboardingViewController initWithFeatures:doneHandler:]
+ -[CARSetupOnboardingViewController showSetUpCarKey]
+ -[CARSetupOnboardingViewController viewDidLoad]
+ GCC_except_table0
+ _OBJC_CLASS_$_CARSetupOnboardingViewController
+ _OBJC_CLASS_$_OBBoldTrayButton
+ _OBJC_IVAR_$_CARSetupOnboardingViewController._doneHandler
+ _OBJC_IVAR_$_CARSetupOnboardingViewController._showSetUpCarKey
+ _OBJC_METACLASS_$_CARSetupOnboardingViewController
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ __OBJC_$_INSTANCE_METHODS_CARSetupOnboardingViewController
+ __OBJC_$_INSTANCE_VARIABLES_CARSetupOnboardingViewController
+ __OBJC_$_PROP_LIST_CARSetupOnboardingViewController
+ __OBJC_CLASS_RO_$_CARSetupOnboardingViewController
+ __OBJC_METACLASS_RO_$_CARSetupOnboardingViewController
+ ___65-[CARSetupOnboardingViewController initWithFeatures:doneHandler:]_block_invoke
+ ___65-[CARSetupOnboardingViewController initWithFeatures:doneHandler:]_block_invoke_2
+ _objc_msgSend$_continue
+ _objc_msgSend$_proceedToCarKeySetup
+ _objc_msgSend$actionWithHandler:
+ _objc_msgSend$addAction:forControlEvents:
+ _objc_msgSend$addBulletedListItemWithTitle:description:symbolName:tintColor:
+ _objc_msgSend$boldButton
+ _objc_msgSend$configuration
+ _objc_msgSend$initWithTitle:detailText:symbolName:contentLayout:
+ _objc_msgSend$setBaseBackgroundColor:
+ _objc_msgSend$setConfiguration:
+ _objc_msgSend$showSetUpCarKey
+ _objc_msgSend$systemGreenColor
+ _objc_retain_x27
+ _objc_retain_x28
- -[CARSetupAssetReadyViewController .cxx_destruct]
- -[CARSetupAssetReadyViewController _done]
- -[CARSetupAssetReadyViewController appsView]
- -[CARSetupAssetReadyViewController doneButton]
- -[CARSetupAssetReadyViewController doneHandler]
- -[CARSetupAssetReadyViewController iconView]
- -[CARSetupAssetReadyViewController initWithAppsView:doneHandler:]
- -[CARSetupAssetReadyViewController subtitleLabel]
- -[CARSetupAssetReadyViewController titleLabel]
- -[CARSetupAssetReadyViewController viewDidLoad]
- GCC_except_table3
- _OBJC_CLASS_$_CARSetupAssetReadyViewController
- _OBJC_IVAR_$_CARSetupAssetReadyViewController._appsView
- _OBJC_IVAR_$_CARSetupAssetReadyViewController._doneButton
- _OBJC_IVAR_$_CARSetupAssetReadyViewController._doneHandler
- _OBJC_IVAR_$_CARSetupAssetReadyViewController._iconView
- _OBJC_IVAR_$_CARSetupAssetReadyViewController._subtitleLabel
- _OBJC_IVAR_$_CARSetupAssetReadyViewController._titleLabel
- _OBJC_METACLASS_$_CARSetupAssetReadyViewController
- __OBJC_$_INSTANCE_METHODS_CARSetupAssetReadyViewController
- __OBJC_$_INSTANCE_VARIABLES_CARSetupAssetReadyViewController
- __OBJC_$_PROP_LIST_CARSetupAssetReadyViewController
- __OBJC_CLASS_RO_$_CARSetupAssetReadyViewController
- __OBJC_METACLASS_RO_$_CARSetupAssetReadyViewController
- ___47-[CARSetupAssetReadyViewController viewDidLoad]_block_invoke
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$appsView
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x8
CStrings:
+ "@32@0:8Q16@?24"
+ "CARSetupOnboardingViewController"
+ "CONTINUE"
+ "Onboarding/welcome: done"
+ "Onboarding/welcome: proceed to car key setup"
+ "READY_CARD_TITLE_CLASSIC"
+ "READY_CARD_TITLE_ULTRA"
+ "SETUP_CAR_KEY"
+ "TB,R,N,V_showSetUpCarKey"
+ "WELCOME_UI_DOLBY_ATMOS"
+ "WELCOME_UI_DOLBY_ATMOS_DESCRIPTION"
+ "WELCOME_UI_ENHANCED_SIRI"
+ "WELCOME_UI_ENHANCED_SIRI_DESCRIPTION"
+ "WELCOME_UI_LIVE_ACTIVITIES"
+ "WELCOME_UI_LIVE_ACTIVITIES_DESCRIPTION"
+ "WELCOME_UI_ROUTE_SHARE"
+ "WELCOME_UI_ROUTE_SHARE_DESCRIPTION"
+ "WELCOME_UI_SIRI"
+ "WELCOME_UI_SIRI_DESCRIPTION"
+ "WELCOME_UI_SPATIAL_AUDIO"
+ "WELCOME_UI_SPATIAL_AUDIO_DESCRIPTION"
+ "WELCOME_UI_VIDEO_ELIGIBLE"
+ "WELCOME_UI_VIDEO_ELIGIBLE_DESCRIPTION"
+ "WELCOME_UI_WIDGETS"
+ "WELCOME_UI_WIDGETS_DESCRIPTION"
+ "_continue"
+ "_proceedToCarKeySetup"
+ "_showSetUpCarKey"
+ "actionWithHandler:"
+ "addAction:forControlEvents:"
+ "addBulletedListItemWithTitle:description:symbolName:tintColor:"
+ "boldButton"
+ "clock.badge.fill"
+ "configuration"
+ "initWithFeatures:doneHandler:"
+ "initWithTitle:detailText:symbolName:contentLayout:"
+ "microphone.badge.siri.fill"
+ "person.spatialaudio.stereo.fill"
+ "play.tv.fill"
+ "setBaseBackgroundColor:"
+ "setConfiguration:"
+ "showSetUpCarKey"
+ "siri"
+ "systemGreenColor"
+ "widget.small"
- "@\"UIImageView\""
- "@\"UIView\""
- "CARSetupAssetReadyViewController"
- "READY_CARD_DONE"
- "READY_CARD_MESSAGE"
- "READY_CARD_TITLE"
- "SAEIcon"
- "SiriIcon"
- "T@\"UIImageView\",R,N,V_iconView"
- "T@\"UIView\",R,N,V_appsView"
- "_appsView"
- "_iconView"
- "appsView"
- "asset ready: done"
- "iconView"
- "initWithAppsView:doneHandler:"
- "show system experience Siri icon: %{public}@"

```
