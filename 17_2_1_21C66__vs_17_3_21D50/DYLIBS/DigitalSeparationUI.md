## DigitalSeparationUI

> `/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`

```diff

-345.0.15.0.0
-  __TEXT.__text: 0x2baa4
-  __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_methlist: 0x2a10
+355.0.3.0.0
+  __TEXT.__text: 0x2fb5c
+  __TEXT.__auth_stubs: 0x650
+  __TEXT.__objc_methlist: 0x2cb8
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x2ace
-  __TEXT.__oslogstring: 0x123b
+  __TEXT.__cstring: 0x2dc8
+  __TEXT.__oslogstring: 0x14c9
   __TEXT.__gcc_except_tab: 0x38c
   __TEXT.__dlopen_cstrs: 0x104
-  __TEXT.__unwind_info: 0xb2c
-  __TEXT.__objc_classname: 0x6a9
-  __TEXT.__objc_methname: 0xa0a7
-  __TEXT.__objc_methtype: 0x1fdf
-  __TEXT.__objc_stubs: 0x7500
-  __DATA_CONST.__got: 0x198
-  __DATA_CONST.__const: 0xad0
-  __DATA_CONST.__objc_classlist: 0x120
+  __TEXT.__unwind_info: 0xbd8
+  __TEXT.__objc_classname: 0x703
+  __TEXT.__objc_methname: 0xa86d
+  __TEXT.__objc_methtype: 0x210a
+  __TEXT.__objc_stubs: 0x7d40
+  __DATA_CONST.__got: 0x1b8
+  __DATA_CONST.__const: 0xb68
+  __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0xc0
+  __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xc578
-  __DATA_CONST.__objc_selrefs: 0x21f0
+  __DATA_CONST.__objc_const: 0xc978
+  __DATA_CONST.__objc_selrefs: 0x2420
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__objc_const: 0xfd8
-  __AUTH_CONST.__cfstring: 0x3440
-  __AUTH_CONST.__const: 0x460
+  __AUTH_CONST.__objc_const: 0x10b0
+  __AUTH_CONST.__cfstring: 0x3820
+  __AUTH_CONST.__const: 0x4a0
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH_CONST.__auth_got: 0x328
-  __AUTH.__objc_data: 0xb40
+  __AUTH_CONST.__objc_intobj: 0x1f8
+  __AUTH_CONST.__auth_got: 0x338
+  __AUTH.__objc_data: 0xbe0
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x478
-  __DATA.__objc_superrefs: 0x108
-  __DATA.__objc_ivar: 0x2ac
-  __DATA.__data: 0x900
-  __DATA.__bss: 0x130
+  __DATA.__objc_classrefs: 0x4e0
+  __DATA.__objc_superrefs: 0x110
+  __DATA.__objc_ivar: 0x2d4
+  __DATA.__data: 0x9c0
+  __DATA.__bss: 0x138
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/ContactsUI.framework/ContactsUI

   - /System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation
   - /System/Library/PrivateFrameworks/FMF.framework/FMF
   - /System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle
+  - /System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice
   - /System/Library/PrivateFrameworks/HealthUI.framework/HealthUI
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A25B7D53-E11E-3977-B9F0-820E820DB689
-  Functions: 1108
-  Symbols:   4433
-  CStrings:  2840
+  UUID: 13FFBE62-E4AB-3057-BE90-472C00BCF45C
+  Functions: 1176
+  Symbols:   4699
+  CStrings:  3016
 
Symbols:
+ +[DSDTOManager isRatchetActiveWithCompletion:]
+ +[DSDTOManager protectUserLocationOnWebDuringDTO]
+ +[DSDTOManager protectUserLocationOnWebDuringDTO].cold.1
+ +[DSPlatterTableView bannerWithPresentingViewController:]
+ +[DSPlatterTableView cellWithPresentingViewController:]
+ +[DSSafetyCheck presentSafetyCheckWithViewController:navigationController:]
+ -[DSEmergencyResetWelcomeController _presentDTOCell]
+ -[DSEmergencyResetWelcomeController cell]
+ -[DSEmergencyResetWelcomeController setCell:]
+ -[DSEmergencyResetWelcomeController viewWillLayoutSubviews]
+ -[DSFaceIDController ratchetViewController:didFinishWithResult:error:]
+ -[DSFaceIDController startRatchetEvalInPresentationContext:]
+ -[DSNavigationController _pushWelcomeControllerAsTopView]
+ -[DSNavigationController _setupRatchetObserver]
+ -[DSNavigationController _welcomeClassForCurrentFlow]
+ -[DSNavigationController classForDeepLink:]
+ -[DSNavigationController deepLinkForCurrentFlowAndPane]
+ -[DSNavigationController deepLinkMatchesPane:]
+ -[DSNavigationController deepLinkPaneType]
+ -[DSNavigationController deepLink]
+ -[DSNavigationController exitFlowForRatchetWait]
+ -[DSNavigationController initStartingWithURL:]
+ -[DSNavigationController isInFamiliarLocation]
+ -[DSNavigationController ratchetStateDidChange:]
+ -[DSNavigationController remoteUIURLFromDeepLink:]
+ -[DSNavigationController remoteUIURL]
+ -[DSNavigationController restoreNavigationOrderForReentry]
+ -[DSNavigationController restoreNavigationOrderForReentry].cold.1
+ -[DSNavigationController sendSummaryAnalyticsWithEventName:]
+ -[DSNavigationController setDeepLink:]
+ -[DSNavigationController setDeepLinkPaneType:]
+ -[DSNavigationController setRemoteUIURL:]
+ -[DSNavigationController updateNavigationOrderAndChapters]
+ -[DSPasscodeController ratchetViewController:didFinishWithResult:error:]
+ -[DSPasscodeController startRatchetEvalInPresentationContext:]
+ -[DSPlatterTableView .cxx_destruct]
+ -[DSPlatterTableView _bannerTextComponents]
+ -[DSPlatterTableView _cellComponents]
+ -[DSPlatterTableView _cellTitleView]
+ -[DSPlatterTableView _descriptionWithAlignment:withPointSizeOffset:]
+ -[DSPlatterTableView _imageView]
+ -[DSPlatterTableView _labelWithText:style:alignment:pointSizeOffset:]
+ -[DSPlatterTableView _learnMoreWithPointSizeOffset:]
+ -[DSPlatterTableView _titleWithPointSizeOffset:]
+ -[DSPlatterTableView didTapLearnMoreLink]
+ -[DSPlatterTableView initWithController:color:axis:]
+ -[DSPlatterTableView preferredHeight]
+ -[DSPlatterTableView presentingViewController]
+ -[DSPlatterTableView setPresentingViewController:]
+ -[DSRemoteUILoader initWithPresenter:delegate:URL:]
+ -[DSSharingWelcomeController _presentDTOCell]
+ -[DSSharingWelcomeController cell]
+ -[DSSharingWelcomeController setCell:]
+ -[DSSharingWelcomeController viewWillLayoutSubviews]
+ -[DSTouchIDController ratchetViewController:didFinishWithResult:error:]
+ -[DSTouchIDController startRatchetEvalInPresentationContext:]
+ GCC_except_table26
+ GCC_except_table42
+ _DSUIDTOLocStringForKey
+ _LARatchetErrorUserInfoKeyState
+ _NSFontAttributeName
+ _NSParagraphStyleAttributeName
+ _OBJC_CLASS_$_AKBiometricRatchetHook
+ _OBJC_CLASS_$_AKDTOBiometryHook
+ _OBJC_CLASS_$_DSDTOManager
+ _OBJC_CLASS_$_DSPlatterTableView
+ _OBJC_CLASS_$_FMDFMIPManager
+ _OBJC_CLASS_$_LARatchetManager
+ _OBJC_CLASS_$_LARatchetViewController
+ _OBJC_CLASS_$_LARatchetViewControllerConfiguration
+ _OBJC_CLASS_$_NSMutableAttributedString
+ _OBJC_CLASS_$_NSMutableParagraphStyle
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_RemoteUIController
+ _OBJC_CLASS_$_UIButton
+ _OBJC_IVAR_$_DSEmergencyResetWelcomeController._cell
+ _OBJC_IVAR_$_DSFaceIDController._ratchetVC
+ _OBJC_IVAR_$_DSNavigationController._deepLink
+ _OBJC_IVAR_$_DSNavigationController._deepLinkPaneType
+ _OBJC_IVAR_$_DSNavigationController._remoteUIURL
+ _OBJC_IVAR_$_DSPasscodeController._ratchetVC
+ _OBJC_IVAR_$_DSPlatterTableView._presentingViewController
+ _OBJC_IVAR_$_DSRemoteUILoader._dynamicURL
+ _OBJC_IVAR_$_DSSharingWelcomeController._cell
+ _OBJC_IVAR_$_DSTouchIDController._ratchetVC
+ _OBJC_METACLASS_$_DSDTOManager
+ _OBJC_METACLASS_$_DSPlatterTableView
+ _OBJC_METACLASS_$_UIStackView
+ _UILayoutFittingCompressedSize
+ __OBJC_$_CLASS_METHODS_DSDTOManager
+ __OBJC_$_CLASS_METHODS_DSPlatterTableView
+ __OBJC_$_INSTANCE_METHODS_DSPlatterTableView
+ __OBJC_$_INSTANCE_VARIABLES_DSPlatterTableView
+ __OBJC_$_PROP_LIST_DSPlatterTableView
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LARatchetObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LARatchetObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LARatchetViewControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LARatchetObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LARatchetViewControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_LARatchetObserver
+ __OBJC_$_PROTOCOL_REFS_LARatchetViewControllerDelegate
+ __OBJC_CLASS_RO_$_DSDTOManager
+ __OBJC_CLASS_RO_$_DSPlatterTableView
+ __OBJC_LABEL_PROTOCOL_$_LARatchetObserver
+ __OBJC_LABEL_PROTOCOL_$_LARatchetViewControllerDelegate
+ __OBJC_METACLASS_RO_$_DSDTOManager
+ __OBJC_METACLASS_RO_$_DSPlatterTableView
+ __OBJC_PROTOCOL_$_LARatchetObserver
+ __OBJC_PROTOCOL_$_LARatchetViewControllerDelegate
+ ___38-[DSTouchIDController beginEnrollment]_block_invoke.268
+ ___43-[DSFaceIDController beginFaceIDEnrollment]_block_invoke.284
+ ___43-[DSFaceIDController beginFaceIDEnrollment]_block_invoke_2.289
+ ___46+[DSDTOManager isRatchetActiveWithCompletion:]_block_invoke
+ ___46-[DSNavigationController willEnterForeground:]_block_invoke.437
+ ___46-[DSNavigationController willEnterForeground:]_block_invoke.437.cold.1
+ ___46-[DSNavigationController willEnterForeground:]_block_invoke.438
+ ___49+[DSDTOManager protectUserLocationOnWebDuringDTO]_block_invoke
+ ___49+[DSDTOManager protectUserLocationOnWebDuringDTO]_block_invoke.cold.1
+ ___52-[DSSharingWelcomeController viewWillLayoutSubviews]_block_invoke
+ ___52-[DSSharingWelcomeController viewWillLayoutSubviews]_block_invoke_2
+ ___59+[DSSafetyCheck startWithPresentingViewController:withURL:]_block_invoke
+ ___59-[DSEmergencyResetWelcomeController viewWillLayoutSubviews]_block_invoke
+ ___59-[DSEmergencyResetWelcomeController viewWillLayoutSubviews]_block_invoke_2
+ ___60-[DSNavigationController sendSummaryAnalyticsWithEventName:]_block_invoke
+ ___70-[DSFaceIDController ratchetViewController:didFinishWithResult:error:]_block_invoke
+ ___71-[DSTouchIDController ratchetViewController:didFinishWithResult:error:]_block_invoke
+ ___75+[DSSafetyCheck presentSafetyCheckWithViewController:navigationController:]_block_invoke
+ ___75+[DSSafetyCheck presentSafetyCheckWithViewController:navigationController:]_block_invoke_2
+ ___83+[DSSafetyCheck showHSA2UpgradeWithPresentingViewController:safetyCheckController:]_block_invoke.323
+ ___83+[DSSafetyCheck showHSA2UpgradeWithPresentingViewController:safetyCheckController:]_block_invoke_2.326
+ ___86+[DSSafetyCheck authForSafetyCheckWithPresentingViewController:safetyCheckController:]_block_invoke.252
+ ___block_descriptor_32_e8_v12?0B8l
+ ___block_descriptor_40_e8_32bs_e36_v24?0"LARatchetState"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e36_v24?0"LARatchetState"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s_e19_"NSDictionary"8?0ls32l8u40l8
+ ___block_descriptor_64_e8_32s40s48s_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
+ ___block_literal_global.238
+ ___block_literal_global.256
+ ___block_literal_global.260
+ ___block_literal_global.278
+ ___block_literal_global.302
+ ___block_literal_global.304
+ ___block_literal_global.328
+ ___block_literal_global.440
+ __unnamed_array_storage.294
+ __unnamed_array_storage.309
+ __unnamed_array_storage.310
+ __unnamed_array_storage.320
+ __unnamed_array_storage.321
+ __unnamed_array_storage.330
+ __unnamed_array_storage.331
+ _dispatch_sync
+ _objc_msgSend$_bannerTextComponents
+ _objc_msgSend$_cellComponents
+ _objc_msgSend$_cellTitleView
+ _objc_msgSend$_descriptionWithAlignment:withPointSizeOffset:
+ _objc_msgSend$_imageView
+ _objc_msgSend$_labelWithText:style:alignment:pointSizeOffset:
+ _objc_msgSend$_learnMoreWithPointSizeOffset:
+ _objc_msgSend$_presentDTOCell
+ _objc_msgSend$_pushWelcomeControllerAsTopView
+ _objc_msgSend$_setupRatchetObserver
+ _objc_msgSend$_titleWithPointSizeOffset:
+ _objc_msgSend$_welcomeClassForCurrentFlow
+ _objc_msgSend$addAttribute:value:range:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$addObserver:
+ _objc_msgSend$appendString:
+ _objc_msgSend$buttonWithType:
+ _objc_msgSend$cell
+ _objc_msgSend$cellWithPresentingViewController:
+ _objc_msgSend$classForDeepLink:
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$containsString:
+ _objc_msgSend$deepLink
+ _objc_msgSend$deepLinkForCurrentFlowAndPane
+ _objc_msgSend$deepLinkMatchesPane:
+ _objc_msgSend$deepLinkPaneType
+ _objc_msgSend$disableLocationDisplayWithCompletion:
+ _objc_msgSend$evaluateAndShowViewController
+ _objc_msgSend$exitFlowForRatchetWait
+ _objc_msgSend$fontWithSize:
+ _objc_msgSend$initStartingWithURL:
+ _objc_msgSend$initWithController:color:axis:
+ _objc_msgSend$initWithPresenter:delegate:URL:
+ _objc_msgSend$initWithString:
+ _objc_msgSend$isInFamiliarLocation
+ _objc_msgSend$isRatchetActiveWithCompletion:
+ _objc_msgSend$makeViewControllerWithOptions:configuration:
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$pointSize
+ _objc_msgSend$popToViewController:animated:
+ _objc_msgSend$preferredHeight
+ _objc_msgSend$presentSafetyCheckWithViewController:navigationController:
+ _objc_msgSend$protectUserLocationOnWebDuringDTO
+ _objc_msgSend$rawValue
+ _objc_msgSend$remoteUIURL
+ _objc_msgSend$remoteUIURLFromDeepLink:
+ _objc_msgSend$restoreNavigationOrderForReentry
+ _objc_msgSend$sendSummaryAnalyticsWithEventName:
+ _objc_msgSend$setAttributedText:
+ _objc_msgSend$setCell:
+ _objc_msgSend$setCornerRadius:
+ _objc_msgSend$setCountdownPrimaryActionTitle:
+ _objc_msgSend$setCustomSpacing:afterView:
+ _objc_msgSend$setDeepLinkPaneType:
+ _objc_msgSend$setSafetyResetNavigationOrder:
+ _objc_msgSend$setSharingActivityNavigationOrder:
+ _objc_msgSend$shouldShowBioRatchetFlow
+ _objc_msgSend$startRatchetEvalInPresentationContext:
+ _objc_msgSend$stateWithCompletion:
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$systemBlackColor
+ _objc_msgSend$systemGray4Color
+ _objc_msgSend$systemGray6Color
+ _objc_msgSend$systemLayoutSizeFittingSize:
+ _objc_msgSend$titleLabel
+ _objc_msgSend$updateNavigationOrderAndChapters
+ _objc_retainAutoreleasedReturnValue
- GCC_except_table39
- ___38-[DSTouchIDController beginEnrollment]_block_invoke.267
- ___43-[DSFaceIDController beginFaceIDEnrollment]_block_invoke.283
- ___43-[DSFaceIDController beginFaceIDEnrollment]_block_invoke_2.288
- ___46-[DSNavigationController willEnterForeground:]_block_invoke.433
- ___46-[DSNavigationController willEnterForeground:]_block_invoke.433.cold.1
- ___46-[DSNavigationController willEnterForeground:]_block_invoke.434
- ___83+[DSSafetyCheck showHSA2UpgradeWithPresentingViewController:safetyCheckController:]_block_invoke.320
- ___83+[DSSafetyCheck showHSA2UpgradeWithPresentingViewController:safetyCheckController:]_block_invoke_2.323
- ___86+[DSSafetyCheck authForSafetyCheckWithPresentingViewController:safetyCheckController:]_block_invoke.251
- ___86+[DSSafetyCheck authForSafetyCheckWithPresentingViewController:safetyCheckController:]_block_invoke_2
- ___86+[DSSafetyCheck authForSafetyCheckWithPresentingViewController:safetyCheckController:]_block_invoke_2.255
- ___block_descriptor_56_e8_32s40s48s_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
- ___block_literal_global.235
- ___block_literal_global.257
- ___block_literal_global.281
- ___block_literal_global.299
- ___block_literal_global.301
- ___block_literal_global.315
- ___block_literal_global.322
- ___block_literal_global.436
- __unnamed_array_storage.291
- __unnamed_array_storage.306
- __unnamed_array_storage.307
- __unnamed_array_storage.317
- __unnamed_array_storage.318
- __unnamed_array_storage.327
- __unnamed_array_storage.328
CStrings:
+ "\x01\x12"
+ "\x01\x14"
+ "\x02\x11\x12"
+ "\x04"
+ "\x17L"
+ "#24@0:8@16"
+ "0`"
+ "4.circle.fill"
+ "@\"DSPlatterTableView\""
+ "@\"LARatchetViewController\""
+ "@\"NSURL\""
+ "@32@0:8q16q24"
+ "@40@0:8@16@24q32"
+ "@48@0:8@16@24q32q40"
+ "A"
+ "Current pane type: %@ not found in navigation order: %@"
+ "DSDTOManager"
+ "DSPlatterTableView"
+ "DTO Location Protection: Does not respondToSelector disableLocationDisplayWithCompletion"
+ "DTO Location Protection: disableLocationDisplay failed with error - %@"
+ "DTO Location Protection: disableLocationDisplay suceeded"
+ "DigitalSeparationUI_DTO"
+ "EMERGENCY_RESET"
+ "EMERGENCY_RESET_BULLET_ACCOUNT"
+ "EMERGENCY_RESET_BULLET_ACCOUNT_DETAIL"
+ "EMERGENCY_RESET_BULLET_DEVICES"
+ "EMERGENCY_RESET_BULLET_DEVICES_DETAIL"
+ "FACEID"
+ "FaceID Change Ratchet initiated, timer counting down. User exiting Safety Check."
+ "FaceID Change Ratchet not armed. Reason: %@"
+ "FlowType"
+ "LARatchetObserver"
+ "LARatchetViewControllerDelegate"
+ "MANAGE_SHARING"
+ "Operation"
+ "PASSCODE"
+ "Passcode Change Ratchet initiated, timer counting down. User exiting Safety Check."
+ "Passcode Change Ratchet not armed. Reason: %@"
+ "RATCHET_ACTION_BUTTON_TITLE"
+ "RATCHET_ENDED_DETAIL_FACEID"
+ "RATCHET_ENDED_DETAIL_PASSCODE"
+ "RATCHET_ENDED_DETAIL_TOUCHID"
+ "RATCHET_REASON_FACEID"
+ "RATCHET_REASON_PASSCODE"
+ "RATCHET_REASON_TOUCHID"
+ "SAFETY_CHECK/"
+ "T#,&,N,V_deepLinkPaneType"
+ "T@\"DSPlatterTableView\",&,N,V_cell"
+ "T@\"NSString\",&,N,V_deepLink"
+ "T@\"NSString\",&,N,V_remoteUIURL"
+ "T@\"UIViewController\",W,N,V_presentingViewController"
+ "TOUCHID"
+ "TouchID Change Ratchet initiated, timer counting down. User exiting Safety Check."
+ "TouchID Change Ratchet not armed. Reason: %@"
+ "WARNING_PLATTER_BODY"
+ "WARNING_PLATTER_LEARN_MORE"
+ "WARNING_PLATTER_LEARN_MORE_URL"
+ "WARNING_PLATTER_TITLE"
+ "_bannerTextComponents"
+ "_cell"
+ "_cellComponents"
+ "_cellTitleView"
+ "_deepLink"
+ "_deepLinkPaneType"
+ "_descriptionWithAlignment:withPointSizeOffset:"
+ "_dynamicURL"
+ "_imageView"
+ "_labelWithText:style:alignment:pointSizeOffset:"
+ "_learnMoreWithPointSizeOffset:"
+ "_presentDTOCell"
+ "_presentingViewController"
+ "_pushWelcomeControllerAsTopView"
+ "_ratchetVC"
+ "_remoteUIURL"
+ "_setupRatchetObserver"
+ "_titleWithPointSizeOffset:"
+ "_welcomeClassForCurrentFlow"
+ "addAttribute:value:range:"
+ "addObjectsFromArray:"
+ "addObserver:"
+ "appendString:"
+ "bannerWithPresentingViewController:"
+ "buttonWithType:"
+ "cell"
+ "cellWithPresentingViewController:"
+ "classForDeepLink:"
+ "com.apple.DigitalSeparation.RatchedEnded"
+ "com.apple.DigitalSeparation.RatchetStarted"
+ "componentsSeparatedByString:"
+ "containsString:"
+ "d16@0:8"
+ "deepLink"
+ "deepLinkForCurrentFlowAndPane"
+ "deepLinkMatchesPane:"
+ "deepLinkPaneType"
+ "didTapLearnMoreLink"
+ "disableLocationDisplayWithCompletion:"
+ "evaluateAndShowViewController"
+ "exitFlowForRatchetWait"
+ "fontWithSize:"
+ "initStartingWithURL:"
+ "initWithController:color:axis:"
+ "initWithPresenter:delegate:URL:"
+ "initWithString:"
+ "isInFamiliarLocation"
+ "isRatchetActiveWithCompletion:"
+ "lock.and.ring.2"
+ "makeViewControllerWithOptions:configuration:"
+ "mutableCopy"
+ "pointSize"
+ "preferredHeight"
+ "prefs:root=Privacy&path=SAFETY_CHECK/"
+ "presentSafetyCheckWithViewController:navigationController:"
+ "protectUserLocationOnWebDuringDTO"
+ "ratchetDidChangeState:"
+ "ratchetStateDidChange:"
+ "ratchetViewController:didFinishWithResult:error:"
+ "ratchetViewControllerDidAppear:"
+ "rawValue"
+ "remoteUIURL"
+ "remoteUIURLFromDeepLink:"
+ "restoreNavigationOrderForReentry"
+ "sendSummaryAnalyticsWithEventName:"
+ "setAttributedText:"
+ "setCell:"
+ "setCornerRadius:"
+ "setCountdownPrimaryActionTitle:"
+ "setCustomSpacing:afterView:"
+ "setDeepLink:"
+ "setDeepLinkPaneType:"
+ "setRemoteUIURL:"
+ "shouldShowBioRatchetFlow"
+ "startRatchetEvalInPresentationContext:"
+ "stateWithCompletion:"
+ "stringWithString:"
+ "systemBlackColor"
+ "systemGray4Color"
+ "systemGray6Color"
+ "systemLayoutSizeFittingSize:"
+ "titleLabel"
+ "updateNavigationOrderAndChapters"
+ "v24@0:8@\"LARatchet\"16"
+ "v24@0:8@\"LARatchetState\"16"
+ "v24@0:8@\"LARatchetViewController\"16"
+ "v24@0:8@\"NSString\"16"
+ "v24@?0@\"LARatchetState\"8@\"NSError\"16"
+ "v40@0:8@\"LARatchetViewController\"16@\"NSDictionary\"24@\"NSError\"32"
+ "viewWillLayoutSubviews"
+ "wasFamiliarLocation"
+ "wasRatchetEnabled"
- "\x02\""
- "\x03"
- "\x14"
- "\x17I"
- "1"

```
