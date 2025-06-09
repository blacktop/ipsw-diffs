## OnBoardingKit

> `/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit`

```diff

-3941.4.0.0.0
-  __TEXT.__text: 0x38a6c
-  __TEXT.__auth_stubs: 0x710
-  __TEXT.__objc_methlist: 0x5424
-  __TEXT.__const: 0x446
-  __TEXT.__cstring: 0x173d
+3962.0.0.0.0
+  __TEXT.__text: 0x3c514
+  __TEXT.__auth_stubs: 0x8c0
+  __TEXT.__objc_methlist: 0x577c
+  __TEXT.__const: 0x3b6
+  __TEXT.__cstring: 0x18dd
   __TEXT.__oslogstring: 0xe63
   __TEXT.__ustring: 0x4
   __TEXT.__gcc_except_tab: 0x74
+  __TEXT.__swift5_typeref: 0xe
   __TEXT.__constg_swiftt: 0x50
-  __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xd80
-  __TEXT.__objc_classname: 0xad3
-  __TEXT.__objc_methname: 0xe41c
-  __TEXT.__objc_methtype: 0x1ce7
-  __TEXT.__objc_stubs: 0x9d00
-  __DATA_CONST.__got: 0x458
-  __DATA_CONST.__const: 0x680
-  __DATA_CONST.__objc_classlist: 0x2d0
-  __DATA_CONST.__objc_catlist: 0x28
+  __TEXT.__unwind_info: 0xe40
+  __TEXT.__objc_classname: 0xb0a
+  __TEXT.__objc_methname: 0xef93
+  __TEXT.__objc_methtype: 0x1e14
+  __TEXT.__objc_stubs: 0xa640
+  __DATA_CONST.__got: 0x498
+  __DATA_CONST.__const: 0x6a8
+  __DATA_CONST.__objc_classlist: 0x2d8
+  __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x34d0
+  __DATA_CONST.__objc_selrefs: 0x3790
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0x398
-  __AUTH_CONST.__const: 0x1c0
-  __AUTH_CONST.__cfstring: 0x1e60
-  __AUTH_CONST.__objc_const: 0xcae8
+  __AUTH_CONST.__auth_got: 0x470
+  __AUTH_CONST.__const: 0x1e0
+  __AUTH_CONST.__cfstring: 0x2020
+  __AUTH_CONST.__objc_const: 0xcec8
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x1108
+  __AUTH.__objc_data: 0x1158
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x540
-  __DATA.__data: 0x720
-  __DATA.__bss: 0x60
+  __DATA.__objc_ivar: 0x578
+  __DATA.__data: 0x728
+  __DATA.__bss: 0x70
   __DATA.__common: 0x60
   __DATA_DIRTY.__objc_data: 0xac8
   __DATA_DIRTY.__bss: 0x40

   - /System/Library/Frameworks/DeveloperToolsSupport.framework/DeveloperToolsSupport
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
+  - /System/Library/Frameworks/Symbols.framework/Symbols
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: D68FD141-4574-3531-9614-CD2FD4903BBE
-  Functions: 1574
-  Symbols:   5991
-  CStrings:  3218
+  UUID: EB5D5B91-2C12-3A95-800D-B20A92F2953D
+  Functions: 1650
+  Symbols:   6234
+  CStrings:  3373
 
Symbols:
+ +[OBFeatureFlags isNaturalUIEnabled]
+ +[OBFeatureFlags isNaturalUIEnabled].cold.1
+ -[OBBoldTrayButton usesWhiteTintColor]
+ -[OBButtonTray addScrollPocketToScrollView:]
+ -[OBButtonTray buttonTrayButtonSpacing]
+ -[OBButtonTray isEmpty]
+ -[OBButtonTray privacyLinkCallback]
+ -[OBButtonTray removeScrollPocket]
+ -[OBButtonTray scrollPocketInteraction]
+ -[OBButtonTray setPrivacyLinkCallback:]
+ -[OBButtonTray setScrollPocketInteraction:]
+ -[OBButtonTray updatePrivacyLinkControllerBottomConstraint]
+ -[OBHeaderView _createImageView:withAnimatedSymbol:]
+ -[OBHeaderView _setImage:accessibilityLabel:withAnimatedSymbol:]
+ -[OBHeaderView forceCenterAlignment]
+ -[OBHeaderView initWithTitle:detailText:symbolName:animated:]
+ -[OBHeaderView initWithTitle:symbolName:animated:]
+ -[OBHeaderView setAttributedDetailText:]
+ -[OBHeaderView setForceCenterAlignment:]
+ -[OBHeaderView setSymbol:accessibilityLabel:animated:]
+ -[OBHeaderView setSymbolName:]
+ -[OBHeaderView startSymbolAnimation]
+ -[OBHeaderView symbolName]
+ -[OBPrivacyCombinedController displayDeviceType]
+ -[OBPrivacyCombinedController setDisplayDeviceType:]
+ -[OBPrivacyFlow _platformOfPreferredDeviceType:]
+ -[OBPrivacyFlow _showInCombinedListWithDeviceClass:]
+ -[OBPrivacyFlow _supportsPlatform:]
+ -[OBPrivacyFlow showInCombinedListForPreferredDeviceType:]
+ -[OBPrivacyFlow supportsPlatformForPreferredDeviceType:]
+ -[OBPrivacyLinkButton _iconToTextSpacingLarge]
+ -[OBPrivacyLinkController privacyLinkCallback]
+ -[OBPrivacyLinkController setPrivacyLinkCallback:]
+ -[OBPrivacyPresenter displayDeviceType]
+ -[OBPrivacyPresenter setDisplayDeviceType:]
+ -[OBSetupAssistantDynamicLayoutController _invokeConstraintForLayoutFactoryBlock]
+ -[OBSetupAssistantDynamicLayoutController addChildViewController:]
+ -[OBSetupAssistantMultitaskingViewController viewDidAppear:]
+ -[OBSetupAssistantSpinnerController initWithSpinnerText:title:]
+ -[OBSetupAssistantSpinnerController setSpinnerText:]
+ -[OBSetupAssistantSpinnerController setSpinnerTitle:]
+ -[OBSetupAssistantSpinnerController setTextLabel:]
+ -[OBSetupAssistantSpinnerController setTitleLabel:]
+ -[OBSetupAssistantSpinnerController spinnerText]
+ -[OBSetupAssistantSpinnerController spinnerTitle]
+ -[OBSetupAssistantSpinnerController textLabel]
+ -[OBSetupAssistantSpinnerController titleLabel]
+ -[OBTemplateHeaderDetailLabel forceCenterAlignment]
+ -[OBTemplateHeaderDetailLabel setForceCenterAlignment:]
+ -[OBTemplateLabel forceCenterAlignment]
+ -[OBTemplateLabel setForceCenterAlignment:]
+ -[OBWelcomeController _safelyAddConstraint:to:]
+ -[OBWelcomeController _usesAboveHeaderFullWidthLayout]
+ -[OBWelcomeController callbacks]
+ -[OBWelcomeController contentViewHeightConstraintsBlock]
+ -[OBWelcomeController didSetContentOffsetOnInitialAppearance]
+ -[OBWelcomeController initWithTitle:attributedDetailText:contentLayout:]
+ -[OBWelcomeController setCallbacks:]
+ -[OBWelcomeController setContentViewHeightConstraintsBlock:]
+ -[OBWelcomeController setDidSetContentOffsetOnInitialAppearance:]
+ -[OBWelcomeController viewDidLoad]
+ -[OBWelcomeController viewWillLayoutSubviews]
+ -[OBWelcomeController(SoftlinkCallbacks) _assertViewControllerIsNotASubclass]
+ -[OBWelcomeController(SoftlinkCallbacks) setCallbackForLifeCyclePhase:callback:]
+ -[OBWelcomeController(SoftlinkCallbacks) triggerCallbackForLifeCyclePhase:]
+ -[UIButton(InfoIcon) addInfoIcon]
+ _NSAttachmentAttributeName
+ _NSLog
+ _OBJC_CLASS_$_NSSymbolDisappearEffect
+ _OBJC_CLASS_$_NSSymbolDrawOnEffect
+ _OBJC_CLASS_$_NSSymbolEffectOptions
+ _OBJC_CLASS_$_OBFeatureFlags
+ _OBJC_CLASS_$__UIScrollPocketInteraction
+ _OBJC_IVAR_$_OBButtonTray._privacyLinkCallback
+ _OBJC_IVAR_$_OBButtonTray._scrollPocketInteraction
+ _OBJC_IVAR_$_OBHeaderView._forceCenterAlignment
+ _OBJC_IVAR_$_OBHeaderView._symbolName
+ _OBJC_IVAR_$_OBPrivacyCombinedController._displayDeviceType
+ _OBJC_IVAR_$_OBPrivacyLinkController._privacyLinkCallback
+ _OBJC_IVAR_$_OBPrivacyPresenter._displayDeviceType
+ _OBJC_IVAR_$_OBSetupAssistantSpinnerController._spinnerText
+ _OBJC_IVAR_$_OBSetupAssistantSpinnerController._spinnerTitle
+ _OBJC_IVAR_$_OBSetupAssistantSpinnerController._textLabel
+ _OBJC_IVAR_$_OBSetupAssistantSpinnerController._titleLabel
+ _OBJC_IVAR_$_OBTemplateHeaderDetailLabel._forceCenterAlignment
+ _OBJC_IVAR_$_OBTemplateLabel._forceCenterAlignment
+ _OBJC_IVAR_$_OBWelcomeController._callbacks
+ _OBJC_IVAR_$_OBWelcomeController._contentViewHeightConstraintsBlock
+ _OBJC_IVAR_$_OBWelcomeController._didSetContentOffsetOnInitialAppearance
+ _OBJC_METACLASS_$_OBFeatureFlags
+ _UIFontTextStyleTitle2
+ _UIFontTextStyleTitle3
+ __CATEGORY_CLASS_METHODS_UIImage_$_OnBoardingKit
+ __CATEGORY_UIImage_$_OnBoardingKit
+ __OBJC_$_CATEGORY_UIButton_$_InfoIcon
+ __OBJC_$_CLASS_METHODS_OBFeatureFlags
+ __OBJC_$_INSTANCE_METHODS_OBWelcomeController(SoftlinkCallbacks|ScrollView|BulletedList|Transition)
+ __OBJC_$_INSTANCE_METHODS_UIButton(InfoIcon|AXFont|OnBoardingKit)
+ __OBJC_$_INSTANCE_METHODS_UIView(BuddyPinAutoLayout|OnBoardingKit)
+ __OBJC_CLASS_RO_$_OBFeatureFlags
+ __OBJC_METACLASS_RO_$_OBFeatureFlags
+ __UISolariumEnabled
+ ___35-[OBPrivacyFlow _supportsPlatform:]_block_invoke
+ ___36+[OBFeatureFlags isNaturalUIEnabled]_block_invoke
+ ___38-[OBWelcomeController viewWillAppear:]_block_invoke_2
+ ___40-[OBHeaderView setAttributedDetailText:]_block_invoke
+ ___75-[OBPrivacySplashListView textView:primaryActionForTextItem:defaultAction:]_block_invoke.20
+ ___81-[OBSetupAssistantDynamicLayoutController _invokeConstraintForLayoutFactoryBlock]_block_invoke
+ ___block_descriptor_40_e8_32s_e25_"NSLayoutConstraint"8?0ls32l8
+ ___block_descriptor_40_e8_32s_e41_v40?0"NSDictionary"8{_NSRange=QQ}16^B32ls32l8
+ ___block_literal_global.96
+ ___chkstk_darwin
+ ___swift_allocate_boxed_opaque_existential_1
+ ___swift_instantiateConcreteTypeFromMangledName
+ __dispatch_main_q
+ __os_feature_enabled_impl
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_OnBoardingKit
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_OnBoardingKit
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_OnBoardingKit
+ _dispatch_async
+ _isNaturalUIEnabled.allowFeature
+ _isNaturalUIEnabled.predicate
+ _objc_msgSend$_assertViewControllerIsNotASubclass
+ _objc_msgSend$_createImageView:withAnimatedSymbol:
+ _objc_msgSend$_iconToTextSpacingLarge
+ _objc_msgSend$_invokeConstraintForLayoutFactoryBlock
+ _objc_msgSend$_obk_applyGlassGroup
+ _objc_msgSend$_obk_applyGlassTinted:
+ _objc_msgSend$_platformOfPreferredDeviceType:
+ _objc_msgSend$_safelyAddConstraint:to:
+ _objc_msgSend$_setError
+ _objc_msgSend$_setImage:accessibilityLabel:withAnimatedSymbol:
+ _objc_msgSend$_showInCombinedListWithDeviceClass:
+ _objc_msgSend$_supportsPlatform:
+ _objc_msgSend$_usesAboveHeaderFullWidthLayout
+ _objc_msgSend$addAttributes:range:
+ _objc_msgSend$addInfoIcon
+ _objc_msgSend$addInteraction:
+ _objc_msgSend$addScrollPocketToScrollView:
+ _objc_msgSend$addSymbolEffect:options:animated:
+ _objc_msgSend$borderlessButtonConfiguration
+ _objc_msgSend$buttonTrayButtonSpacing
+ _objc_msgSend$callbacks
+ _objc_msgSend$childViewControllers
+ _objc_msgSend$configurationByApplyingConfiguration:
+ _objc_msgSend$configurationPreferringMonochrome
+ _objc_msgSend$configurationWithColorRenderingMode:
+ _objc_msgSend$contentInsetAdjustmentBehavior
+ _objc_msgSend$contentViewHeightConstraintsBlock
+ _objc_msgSend$currentImage
+ _objc_msgSend$darkTextColor
+ _objc_msgSend$data
+ _objc_msgSend$detailLabelToAccessoryButtonPadding
+ _objc_msgSend$didSetContentOffsetOnInitialAppearance
+ _objc_msgSend$effect
+ _objc_msgSend$enumerateAttributesInRange:options:usingBlock:
+ _objc_msgSend$forceCenterAlignment
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$getRed:green:blue:alpha:
+ _objc_msgSend$hasError
+ _objc_msgSend$imageWithRenderingMode:
+ _objc_msgSend$initWithScrollView:edge:style:
+ _objc_msgSend$initWithSpinnerText:
+ _objc_msgSend$initWithTitle:detailText:symbolName:animated:
+ _objc_msgSend$initWithTitle:symbolName:animated:
+ _objc_msgSend$isEmpty
+ _objc_msgSend$isNaturalUIEnabled
+ _objc_msgSend$options
+ _objc_msgSend$privacyLinkCallback
+ _objc_msgSend$removeInteraction:
+ _objc_msgSend$removeScrollPocket
+ _objc_msgSend$scrollPocketInteraction
+ _objc_msgSend$setAttributedDetailText:
+ _objc_msgSend$setAttributedString:
+ _objc_msgSend$setBaseForegroundColor:
+ _objc_msgSend$setCallbacks:
+ _objc_msgSend$setContentOffset:
+ _objc_msgSend$setContentViewHeightConstraintsBlock:
+ _objc_msgSend$setCornerStyle:
+ _objc_msgSend$setDidSetContentOffsetOnInitialAppearance:
+ _objc_msgSend$setForceCenterAlignment:
+ _objc_msgSend$setImage:forState:
+ _objc_msgSend$setImagePadding:
+ _objc_msgSend$setImagePlacement:
+ _objc_msgSend$setMaximumLineHeight:
+ _objc_msgSend$setMinimumLineHeight:
+ _objc_msgSend$setParagraphSpacing:
+ _objc_msgSend$setPrivacyLinkCallback:
+ _objc_msgSend$setScrollPocketInteraction:
+ _objc_msgSend$setSymbol:accessibilityLabel:animated:
+ _objc_msgSend$setSymbolName:
+ _objc_msgSend$showInCombinedListForPreferredDeviceType:
+ _objc_msgSend$startSymbolAnimation
+ _objc_msgSend$string
+ _objc_msgSend$supportsPlatformForPreferredDeviceType:
+ _objc_msgSend$systemGray6Color
+ _objc_msgSend$triggerCallbackForLifeCyclePhase:
+ _objc_msgSend$updatePrivacyLinkControllerBottomConstraint
+ _objc_msgSend$updatedConfigurationForButton:
+ _objc_msgSend$usesWhiteTintColor
+ _swift_allocBox
+ _swift_bridgeObjectRelease
+ _swift_getTypeByMangledNameInContext2
+ _swift_release
+ _swift_task_isCurrentExecutor
+ _swift_task_reportUnexpectedExecutor
+ _symbolic _____Sg So8UIButtonC5UIKitE13ConfigurationV
- -[OBHeaderView _createImageView:]
- -[OBSetupAssistantSpinnerController label]
- -[OBSetupAssistantSpinnerController setLabel:]
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _OBButtonTrayButtonSpacing
- _OBJC_IVAR_$_OBHeaderView._usingSymbolImage
- _OBJC_IVAR_$_OBSetupAssistantSpinnerController._label
- __OBJC_$_CATEGORY_INSTANCE_METHODS_UIButton_$_AXFont
- __OBJC_$_CATEGORY_INSTANCE_METHODS_UIView_$_BuddyPinAutoLayout
- __OBJC_$_CATEGORY_UIButton_$_AXFont
- __OBJC_$_INSTANCE_METHODS_OBWelcomeController(ScrollView|BulletedList|Transition)
- ___34-[OBPrivacyFlow platformSupported]_block_invoke
- ___75-[OBPrivacySplashListView textView:primaryActionForTextItem:defaultAction:]_block_invoke.18
- ___block_literal_global.89
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swiftDataDetection_$_OnBoardingKit
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_OnBoardingKit
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_OnBoardingKit
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_OnBoardingKit
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_OnBoardingKit
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_OnBoardingKit
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_OnBoardingKit
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_OnBoardingKit
- _objc_msgSend$_createImageView:
- _objc_msgSend$initWithTitle:detailText:symbolName:
- _objc_msgSend$label
- _objc_msgSend$showInCombinedList
CStrings:
+ "%@\n%@"
+ "-seed"
+ "@\"NSLayoutConstraint\"8@?0"
+ "@\"NSMutableDictionary\""
+ "@\"UIMenu\"40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSArray\"32"
+ "@\"UIMenu\"40@0:8@\"UITextView\"16@\"NSArray\"24@\"NSArray\"32"
+ "@\"_UIScrollPocketInteraction\""
+ "@20@0:8B16"
+ "@28@0:8@16B24"
+ "AppleTV"
+ "AudioAccessory"
+ "B24@0:8Q16"
+ "B40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSString\"32"
+ "B40@0:8@\"UITextView\"16@\"NSArray\"24@\"NSString\"32"
+ "InfoIcon"
+ "Mac"
+ "NaturalUI"
+ "OBFeatureFlags"
+ "OnBoardingKit"
+ "OnBoardingKit/SwiftUIKitExtras.swift"
+ "RealityDevice"
+ "SoftlinkCallbacks"
+ "T@\"NSMutableDictionary\",&,N,V_callbacks"
+ "T@\"NSString\",&,N,V_symbolName"
+ "T@\"NSString\",C,N,V_spinnerText"
+ "T@\"NSString\",C,N,V_spinnerTitle"
+ "T@\"UILabel\",&,N,V_textLabel"
+ "T@\"_UIScrollPocketInteraction\",&,N,V_scrollPocketInteraction"
+ "T@?,C,N,V_contentViewHeightConstraintsBlock"
+ "T@?,C,N,V_privacyLinkCallback"
+ "TB,N,V_didSetContentOffsetOnInitialAppearance"
+ "TB,N,V_forceCenterAlignment"
+ "TQ,N,V_displayDeviceType"
+ "Warning: Attempted to add a nil constraint!"
+ "Watch"
+ "_assertViewControllerIsNotASubclass"
+ "_callbacks"
+ "_contentViewHeightConstraintsBlock"
+ "_createImageView:withAnimatedSymbol:"
+ "_didSetContentOffsetOnInitialAppearance"
+ "_forceCenterAlignment"
+ "_iconToTextSpacingLarge"
+ "_invokeConstraintForLayoutFactoryBlock"
+ "_obk_applyGlassGroup"
+ "_obk_applyGlassTinted:"
+ "_platformOfPreferredDeviceType:"
+ "_privacyLinkCallback"
+ "_safelyAddConstraint:to:"
+ "_scrollPocketInteraction"
+ "_setError"
+ "_setImage:accessibilityLabel:withAnimatedSymbol:"
+ "_showInCombinedListWithDeviceClass:"
+ "_spinnerText"
+ "_spinnerTitle"
+ "_supportsPlatform:"
+ "_textLabel"
+ "_usesAboveHeaderFullWidthLayout"
+ "addAttributes:range:"
+ "addInfoIcon"
+ "addInteraction:"
+ "addScrollPocketToScrollView:"
+ "addSymbolEffect:options:animated:"
+ "borderlessButtonConfiguration"
+ "buttonTrayButtonSpacing"
+ "callbacks"
+ "chevron.down.circle.fill"
+ "chevron.forward.circle.fill"
+ "childViewControllers"
+ "configurationByApplyingConfiguration:"
+ "configurationPreferringMonochrome"
+ "configurationWithColorRenderingMode:"
+ "configurationWithHierarchicalColor:"
+ "contentInsetAdjustmentBehavior"
+ "contentViewHeightConstraintsBlock"
+ "currentImage"
+ "darkTextColor"
+ "data"
+ "didSetContentOffsetOnInitialAppearance"
+ "disclosureChevronImageWithExpandedState:"
+ "effect"
+ "enumerateAttributesInRange:options:usingBlock:"
+ "forceCenterAlignment"
+ "getBytes:range:"
+ "getRed:green:blue:alpha:"
+ "hasError"
+ "iPhone"
+ "iPod"
+ "imageWithRenderingMode:"
+ "imageWithSymbolConfiguration:"
+ "info.circle.fill"
+ "initWithScrollView:edge:style:"
+ "initWithSpinnerText:title:"
+ "initWithTitle:attributedDetailText:contentLayout:"
+ "initWithTitle:detailText:symbolName:animated:"
+ "initWithTitle:symbolName:animated:"
+ "isEmpty"
+ "isNaturalUIEnabled"
+ "macOS"
+ "options"
+ "privacyLinkCallback"
+ "removeInteraction:"
+ "removeScrollPocket"
+ "scrollPocketInteraction"
+ "setAttributedDetailText:"
+ "setAttributedString:"
+ "setBaseForegroundColor:"
+ "setCallbackForLifeCyclePhase:callback:"
+ "setCallbacks:"
+ "setContentOffset:"
+ "setContentViewHeightConstraintsBlock:"
+ "setCornerStyle:"
+ "setDidSetContentOffsetOnInitialAppearance:"
+ "setForceCenterAlignment:"
+ "setImage:forState:"
+ "setImagePadding:"
+ "setImagePlacement:"
+ "setMaximumLineHeight:"
+ "setMinimumLineHeight:"
+ "setParagraphSpacing:"
+ "setPrivacyLinkCallback:"
+ "setScrollPocketInteraction:"
+ "setSpinnerText:"
+ "setSpinnerTitle:"
+ "setSymbol:accessibilityLabel:animated:"
+ "setTextLabel:"
+ "showInCombinedListForPreferredDeviceType:"
+ "spinnerText"
+ "spinnerTitle"
+ "startSymbolAnimation"
+ "string"
+ "supportsPlatformForPreferredDeviceType:"
+ "systemGray6Color"
+ "textField:editMenuForCharactersInRanges:suggestedActions:"
+ "textField:shouldChangeCharactersInRanges:replacementString:"
+ "textView:editMenuForTextInRanges:suggestedActions:"
+ "textView:shouldChangeTextInRanges:replacementText:"
+ "triggerCallbackForLifeCyclePhase:"
+ "tvOS"
+ "updatePrivacyLinkControllerBottomConstraint"
+ "updatedConfigurationForButton:"
+ "usesWhiteTintColor"
+ "v32@0:8Q16@?24"
+ "v40@?0@\"NSDictionary\"8{_NSRange=QQ}16^B32"
+ "viewWillLayoutSubviews"
+ "watchOS"
+ "xrOS"
- " %@\n%@"
- "T@\"UILabel\",&,N,V_label"
- "_createImageView:"
- "_label"
- "_usingSymbolImage"
- "label"
- "setLabel:"

```
