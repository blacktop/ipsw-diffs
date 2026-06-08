## HearingAidUIServer

> `/System/Library/AccessibilityBundles/HearingAidUIServer.axuiservice/HearingAidUIServer`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0x1e58
-  __TEXT.__auth_stubs: 0x200
-  __TEXT.__objc_methlist: 0x3cc
-  __TEXT.__const: 0x28
-  __TEXT.__cstring: 0x18e
-  __TEXT.__gcc_except_tab: 0x24
+3229.1.6.0.0
+  __TEXT.__text: 0x2900
+  __TEXT.__objc_methlist: 0x4c4
   __TEXT.__dlopen_cstrs: 0x69
-  __TEXT.__unwind_info: 0x100
-  __TEXT.__objc_classname: 0xaf
-  __TEXT.__objc_methname: 0x1067
-  __TEXT.__objc_methtype: 0x46c
-  __TEXT.__objc_stubs: 0xac0
-  __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0x138
-  __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x20
+  __TEXT.__const: 0x28
+  __TEXT.__gcc_except_tab: 0x8c
+  __TEXT.__cstring: 0x23d
+  __TEXT.__unwind_info: 0x118
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x160
+  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x468
-  __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x110
-  __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x220
-  __AUTH_CONST.__objc_const: 0x610
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x28
-  __DATA.__data: 0x180
-  __DATA.__bss: 0x18
+  __DATA_CONST.__objc_selrefs: 0x590
+  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__got: 0x178
+  __AUTH_CONST.__const: 0xe0
+  __AUTH_CONST.__cfstring: 0x340
+  __AUTH_CONST.__objc_const: 0x748
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x2c
+  __DATA.__data: 0x1e0
+  __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/AXSoundDetection.framework/AXSoundDetection
   - /System/Library/PrivateFrameworks/AccessibilityUIService.framework/AccessibilityUIService
   - /System/Library/PrivateFrameworks/AccessibilityUIShared.framework/AccessibilityUIShared
+  - /System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/AccessibilityUIUtilities
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/HearingUI.framework/HearingUI
   - /System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 015566C9-E3BC-3149-AD85-FE81F867540E
-  Functions: 42
-  Symbols:   319
-  CStrings:  261
+  UUID: 6358E256-7F70-35C4-9A44-1585FF12CACF
+  Functions: 55
+  Symbols:   408
+  CStrings:  60
 
Symbols:
+ +[AXHearingAidBannerViewController sharedInstance]
+ -[AXHearingAidBannerViewController .cxx_destruct]
+ -[AXHearingAidBannerViewController bannerManager]
+ -[AXHearingAidBannerViewController dismissBanner]
+ -[AXHearingAidBannerViewController init]
+ -[AXHearingAidBannerViewController setBannerManager:]
+ -[AXHearingAidBannerViewController showConnectedBanner:]
+ -[AXHearingAidBannerViewController showConnectionMovedBanner:deviceName:actionBlock:]
+ -[HearingAidUIServer init]
+ GCC_except_table28
+ _OBJC_CLASS_$_AXAlertBannerContent
+ _OBJC_CLASS_$_AXAlertBannerManager
+ _OBJC_CLASS_$_AXHearingAidBannerViewController
+ _OBJC_CLASS_$_HUAudioRoutesManager
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_UIButtonConfiguration
+ _OBJC_CLASS_$_UIImage
+ _OBJC_CLASS_$_UIImageSymbolConfiguration
+ _OBJC_IVAR_$_AXHearingAidBannerViewController._bannerManager
+ _OBJC_METACLASS_$_AXHearingAidBannerViewController
+ _SBUIIsSystemApertureEnabled
+ __OBJC_$_CLASS_METHODS_AXHearingAidBannerViewController
+ __OBJC_$_INSTANCE_METHODS_AXHearingAidBannerViewController
+ __OBJC_$_INSTANCE_VARIABLES_AXHearingAidBannerViewController
+ __OBJC_$_PROP_LIST_AXHearingAidBannerViewController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HUAudioRoutesManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HUAudioRoutesManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_HUAudioRoutesManagerDelegate
+ __OBJC_CLASS_RO_$_AXHearingAidBannerViewController
+ __OBJC_LABEL_PROTOCOL_$_HUAudioRoutesManagerDelegate
+ __OBJC_METACLASS_RO_$_AXHearingAidBannerViewController
+ __OBJC_PROTOCOL_$_HUAudioRoutesManagerDelegate
+ ___49-[AXHearingAidBannerViewController dismissBanner]_block_invoke
+ ___50+[AXHearingAidBannerViewController sharedInstance]_block_invoke
+ ___56-[AXHearingAidBannerViewController showConnectedBanner:]_block_invoke
+ ___83-[HearingAidUIServer processMessage:withIdentifier:fromClientWithIdentifier:error:]_block_invoke_5
+ ___83-[HearingAidUIServer processMessage:withIdentifier:fromClientWithIdentifier:error:]_block_invoke_6
+ ___85-[AXHearingAidBannerViewController showConnectionMovedBanner:deviceName:actionBlock:]_block_invoke
+ ___85-[AXHearingAidBannerViewController showConnectionMovedBanner:deviceName:actionBlock:]_block_invoke_2
+ ___NSDictionary0__struct
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_literal_global.365
+ ___block_literal_global.380
+ ___block_literal_global.385
+ ___block_literal_global.391
+ ___block_literal_global.409
+ ___block_literal_global.73
+ ___kCFBooleanTrue
+ _dispatch_async
+ _dispatch_once
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$background
+ _objc_msgSend$bannerManager
+ _objc_msgSend$configurationWithPointSize:weight:
+ _objc_msgSend$dismissAlertBanner:
+ _objc_msgSend$imageWithRenderingMode:
+ _objc_msgSend$initWithIdentifier:title:subtitle:iconImage:userInfo:actionBlock:
+ _objc_msgSend$isHearingAidRouteSelected
+ _objc_msgSend$postAlertBanner:
+ _objc_msgSend$registerForAudioUpdates:
+ _objc_msgSend$setActionButtonConfiguration:
+ _objc_msgSend$setBannerManager:
+ _objc_msgSend$setContentInsets:
+ _objc_msgSend$setImage:
+ _objc_msgSend$setIsSystemApertureExpandable:
+ _objc_msgSend$setPreferredSymbolConfigurationForImage:
+ _objc_msgSend$setShouldExpandSystemApertureAlertByDefault:
+ _objc_msgSend$setSystemApertureActionButtonConfiguration:
+ _objc_msgSend$shared
+ _objc_msgSend$showConnectedBanner:
+ _objc_msgSend$showConnectionMovedBanner:deviceName:actionBlock:
+ _objc_msgSend$state
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$systemBlueColor
+ _objc_msgSend$systemImageNamed:
+ _objc_msgSend$tintedButtonConfiguration
+ _objc_msgSend$unregisterFromAudioUpdates:
+ _objc_release_x1
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x28
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x4
+ _sharedInstance.onceToken
+ _sharedInstance.sharedInstance
- GCC_except_table3
- _ControlCenterServicesLibrary
- ___block_literal_global.352
- ___block_literal_global.371
- ___getCCSControlCenterServiceClass_block_invoke.cold.1
- ___getCCSModulePresentationOptionsClass_block_invoke.cold.1
- _hearingAidStreamSelected
- _objc_autorelease
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x23
CStrings:
+ "%@"
+ "HUHearingAidBannerManagerIdentifier"
+ "HearingAidConnected"
+ "HearingAidMovedToDeviceTitle"
+ "User requested dismissal"
+ "arrow.uturn.backward"
+ "device"
+ "hearingAid"
+ "hearingaid.ear"
- "#16@0:8"
- ".cxx_destruct"
- "@\"AXAccessQueue\"24@0:8Q16"
- "@\"AXAssertion\""
- "@\"AXDispatchTimer\""
- "@\"AXHearingAidDisplayController\""
- "@\"HACCShortcutViewController\""
- "@\"HearingAidUIServer\""
- "@\"NSDictionary\"48@0:8@\"NSDictionary\"16Q24@\"NSString\"32^@40"
- "@\"NSDictionary\"52@0:8@\"NSDictionary\"16Q24@\"NSString\"32i40^@44"
- "@\"NSSet\"24@0:8Q16"
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8Q16"
- "@\"UIAlertController\""
- "@\"UILabel\""
- "@\"UIViewController\""
- "@\"UNUserNotificationCenter\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@48@0:8@16Q24@32^@40"
- "@52@0:8@16Q24@32i40^@44"
- "AXHAShortcutUpdateProtocol"
- "AXHearingAidDisplayController"
- "AXUIContentViewControllerDelegate"
- "AXUIService"
- "AXUltronStatusProviderViewController"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "CGColor"
- "HearingAidUIServer"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"AXAssertion\",&,N,V_disableSystemGestureAssertion"
- "T@\"AXHearingAidDisplayController\",&,N,V_displayController"
- "T@\"HACCShortcutViewController\",&,N,V_moduleUIController"
- "T@\"HearingAidUIServer\",N,V_parentController"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"UNUserNotificationCenter\",R,N,V_userNotificationCenter"
- "TQ,R"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_clearTimer"
- "_confidence"
- "_disableSystemGestureAssertion"
- "_displayController"
- "_emptyViewController"
- "_handoffAlertController"
- "_listenType"
- "_moduleUIController"
- "_parentController"
- "_shouldForwardViewWillTransitionToSize"
- "_userNotificationCenter"
- "accessQueueForProcessingMessageWithIdentifier:"
- "actionWithTitle:style:handler:"
- "addAction:"
- "addConstraint:"
- "addContentViewController:withUserInteractionEnabled:forService:"
- "addSubview:"
- "afterDelay:processBlock:"
- "alertControllerWithTitle:message:preferredStyle:"
- "animateWithDuration:animations:"
- "assertionWithType:identifier:"
- "autorelease"
- "backgroundAccessQueue"
- "blackColor"
- "blueColor"
- "boolValue"
- "cancel"
- "cancelHearingAidConnectionRequest"
- "class"
- "clientMessengerWithIdentifier:"
- "colorWithAlphaComponent:"
- "conformsToProtocol:"
- "connectionWillBeInterruptedForClientWithIdentifier:"
- "constraintWithItem:attribute:relatedBy:toItem:attribute:multiplier:constant:"
- "createUserNotificationRequest:"
- "d28@0:8@\"UIViewController\"16B24"
- "d28@0:8@16B24"
- "dealloc"
- "debugDescription"
- "defaultExpandedOptions"
- "defaultSound"
- "description"
- "desiredWindowLevelForContentViewController:userInteractionEnabled:"
- "dictionaryWithObject:forKey:"
- "didMoveToParentViewController:"
- "disableSystemGestureAssertion"
- "dismissViewControllerAnimated:completion:"
- "dismissViewControllerWithTransition:completion:"
- "dismissWithCompletion:"
- "displayController"
- "externalDisplaySceneConnected:"
- "externalDisplaySceneConnected:forSceneClientIdentifier:"
- "externalDisplaySceneDisconnected:"
- "externalDisplaySceneDisconnected:forSceneClientIdentifier:"
- "fontWithDescriptor:size:"
- "hash"
- "hearingAidControlPanelCount"
- "i24@0:8@\"NSString\"16"
- "i24@0:8@16"
- "initWithDelegate:"
- "initWithFrame:"
- "initWithTargetSerialQueue:"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isSafeToProcessMessageFromUnentitledProcessWithIdentifier:"
- "isScreenLockedWithPasscode:"
- "layer"
- "loadView"
- "mainDisplaySceneConnected:"
- "messageWithIdentifierRequiresWritingBlock:"
- "messageWithIdentifierShouldBeProcessedAsynchronously:"
- "moduleUIController"
- "numberWithBool:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "parentController"
- "parentViewController"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pointSize"
- "possibleRequiredEntitlementsForProcessingMessageWithIdentifier:"
- "preferredFontDescriptorWithTextStyle:addingSymbolicTraits:options:"
- "presentModuleWithIdentifier:options:completionHandler:"
- "presentViewController:animated:completion:"
- "presentedViewController"
- "processInitializationMessage:"
- "processMessage:withIdentifier:fromClientWithIdentifier:error:"
- "processMessage:withIdentifier:fromClientWithIdentifier:pid:error:"
- "processMessageAsynchronously:withIdentifier:fromClientWithIdentifier:completion:"
- "processMessageAsynchronously:withIdentifier:fromClientWithIdentifier:pid:completion:"
- "release"
- "remoteSceneDidHandleHomeGesture:"
- "removeContentViewController:withUserInteractionEnabled:forService:"
- "removeFromParentViewController"
- "removeFromSuperview"
- "requestWithIdentifier:content:trigger:destinations:"
- "requiredEntitlementForProcessingMessageWithIdentifier:"
- "respondsToSelector:"
- "resumeMedia"
- "retain"
- "retainCount"
- "self"
- "sendAsynchronousMessage:withIdentifier:targetAccessQueue:completion:"
- "server"
- "serviceTypeForClientWithIdentifier:"
- "serviceWasFullyInitialized"
- "setBackgroundColor:"
- "setBody:"
- "setBorderColor:"
- "setBorderWidth:"
- "setCategoryIdentifier:"
- "setClipsToBounds:"
- "setCornerRadius:"
- "setDelegate:"
- "setDisableSystemGestureAssertion:"
- "setDisplayController:"
- "setFont:"
- "setHearingAidControlIsVisible:"
- "setHearingAidControlPanelCount:"
- "setHidden:"
- "setModuleUIController:"
- "setNewDisplayController:"
- "setNumberOfLines:"
- "setParentController:"
- "setSound:"
- "setText:"
- "setTextAlignment:"
- "setTextColor:"
- "setTitle:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setUserInfo:"
- "sharedDisplayManager"
- "sharedInstance"
- "shortcutDidChangeSize:"
- "shouldPreventAutorotatingAllContentViewControllers"
- "sizeToFit"
- "superclass"
- "unregisterUpdateListener:"
- "updateDisplay:confidence:"
- "userNotificationCenter"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"HACCShortcutViewController\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"UIWindowScene\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8@\"UIWindowScene\"16@\"NSString\"24"
- "v32@0:8@16@24"
- "v32@0:8@16d24"
- "v48@0:8@\"NSDictionary\"16Q24@\"NSString\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@16Q24@32@?40"
- "v52@0:8@\"NSDictionary\"16Q24@\"NSString\"32i40@?<v@?@\"NSDictionary\"@\"NSError\">44"
- "v52@0:8@16Q24@32i40@?44"
- "view"
- "viewDidAppear:"
- "viewDidLoad"
- "viewWillAppear:"
- "window"
- "yellowColor"
- "zone"

```
