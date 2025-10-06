## AACDependencies

> `/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACDependencies.framework/AACDependencies`

```diff

-13.4.3.0.0
-  __TEXT.__text: 0xa08
-  __TEXT.__auth_stubs: 0x1b0
-  __TEXT.__objc_methlist: 0x1d4
-  __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x4f
-  __TEXT.__unwind_info: 0x90
-  __TEXT.__objc_classname: 0x129
-  __TEXT.__objc_methname: 0x7f9
-  __TEXT.__objc_methtype: 0x156
-  __TEXT.__objc_stubs: 0x460
-  __DATA_CONST.__got: 0x10
-  __DATA_CONST.__const: 0xa0
-  __DATA_CONST.__objc_classlist: 0x30
+13.5.10.0.0
+  __TEXT.__text: 0x1e48
+  __TEXT.__auth_stubs: 0x2b0
+  __TEXT.__objc_methlist: 0x278
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0xa3
+  __TEXT.__unwind_info: 0xe8
+  __TEXT.__objc_classname: 0x179
+  __TEXT.__objc_methname: 0xe6f
+  __TEXT.__objc_methtype: 0x207
+  __TEXT.__objc_stubs: 0xc40
+  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__const: 0x1b0
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5e8
-  __DATA_CONST.__objc_selrefs: 0x1a0
-  __DATA_CONST.__objc_classrefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__objc_const: 0x1f0
-  __AUTH_CONST.__auth_got: 0xe0
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x44
-  __DATA.__data: 0x180
+  __DATA_CONST.__objc_const: 0x7f0
+  __DATA_CONST.__objc_selrefs: 0x3a8
+  __DATA_CONST.__objc_classrefs: 0xc0
+  __DATA_CONST.__objc_superrefs: 0x20
+  __AUTH_CONST.__objc_const: 0x2c8
+  __AUTH_CONST.__const: 0x20
+  __AUTH_CONST.__auth_got: 0x160
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0x54
+  __DATA.__data: 0x1e0
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F008FCD3-B146-3E1A-9044-8E9EA9DDB6DC
-  Functions: 39
-  Symbols:   230
-  CStrings:  115
+  UUID: 011D94BA-6EBA-361E-A953-7499E9D51BBC
+  Functions: 62
+  Symbols:   413
+  CStrings:  205
 
Symbols:
+ -[AEDBannerView .cxx_destruct]
+ -[AEDBannerView backgroundView]
+ -[AEDBannerView buildView]
+ -[AEDBannerView initWithTitle:]
+ -[AEDBannerView titleLabel]
+ -[AEDBannerView title]
+ -[AEDConcreteUIPrimitives keyWindow]
+ -[AEDConcreteUIPrimitives presentBannerWithTitle:duration:completion:]
+ -[AEDConcreteUIPrimitives presentChoicePromptWithTitle:message:confirmText:cancelText:completion:]
+ -[AEDConcreteUIPrimitives suitableViewControllerForViewController:]
+ -[AEDSingleAppModeConfiguration setShowsUserConfirmationPromptsAndBanners:]
+ -[AEDSingleAppModeConfiguration showsUserConfirmationPromptsAndBanners]
+ -[AEDUIPrimitivesProvider makePrimitives]
+ _CGRectZero
+ _OBJC_CLASS_$_AEDBannerView
+ _OBJC_CLASS_$_AEDConcreteUIPrimitives
+ _OBJC_CLASS_$_AEDUIPrimitivesProvider
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSAttributedString
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSLayoutConstraint
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSTimer
+ _OBJC_CLASS_$_UIAlertAction
+ _OBJC_CLASS_$_UIAlertController
+ _OBJC_CLASS_$_UIApplication
+ _OBJC_CLASS_$_UIColor
+ _OBJC_CLASS_$_UIFont
+ _OBJC_CLASS_$_UIFontDescriptor
+ _OBJC_CLASS_$_UILabel
+ _OBJC_CLASS_$_UIView
+ _OBJC_CLASS_$__UIBackdropView
+ _OBJC_IVAR_$_AEDBannerView._backgroundView
+ _OBJC_IVAR_$_AEDBannerView._title
+ _OBJC_IVAR_$_AEDBannerView._titleLabel
+ _OBJC_IVAR_$_AEDSingleAppModeConfiguration._showsUserConfirmationPromptsAndBanners
+ _OBJC_METACLASS_$_AEDBannerView
+ _OBJC_METACLASS_$_AEDConcreteUIPrimitives
+ _OBJC_METACLASS_$_AEDUIPrimitivesProvider
+ _OBJC_METACLASS_$_UIView
+ _UIAccessibilityAnnouncementNotification
+ _UIAccessibilityPostNotification
+ _UIAccessibilitySpeechAttributeAnnouncementPriority
+ _UIFontTextStyleFootnote1
+ _UIWindowSceneSessionRoleApplication
+ __NSConcreteGlobalBlock
+ __OBJC_$_INSTANCE_METHODS_AEDBannerView
+ __OBJC_$_INSTANCE_METHODS_AEDConcreteUIPrimitives
+ __OBJC_$_INSTANCE_METHODS_AEDUIPrimitivesProvider
+ __OBJC_$_INSTANCE_VARIABLES_AEDBannerView
+ __OBJC_$_PROP_LIST_AEDBannerView
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AEDUIPrimitives
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AEDUIPrimitives
+ __OBJC_CLASS_PROTOCOLS_$_AEDConcreteUIPrimitives
+ __OBJC_CLASS_RO_$_AEDBannerView
+ __OBJC_CLASS_RO_$_AEDConcreteUIPrimitives
+ __OBJC_CLASS_RO_$_AEDUIPrimitivesProvider
+ __OBJC_LABEL_PROTOCOL_$_AEDUIPrimitives
+ __OBJC_METACLASS_RO_$_AEDBannerView
+ __OBJC_METACLASS_RO_$_AEDConcreteUIPrimitives
+ __OBJC_METACLASS_RO_$_AEDUIPrimitivesProvider
+ __OBJC_PROTOCOL_$_AEDUIPrimitives
+ ___27-[AEDBannerView titleLabel]_block_invoke
+ ___31-[AEDBannerView backgroundView]_block_invoke
+ ___36-[AEDConcreteUIPrimitives keyWindow]_block_invoke
+ ___70-[AEDConcreteUIPrimitives presentBannerWithTitle:duration:completion:]_block_invoke
+ ___70-[AEDConcreteUIPrimitives presentBannerWithTitle:duration:completion:]_block_invoke_2
+ ___70-[AEDConcreteUIPrimitives presentBannerWithTitle:duration:completion:]_block_invoke_3
+ ___70-[AEDConcreteUIPrimitives presentBannerWithTitle:duration:completion:]_block_invoke_4
+ ___98-[AEDConcreteUIPrimitives presentChoicePromptWithTitle:message:confirmText:cancelText:completion:]_block_invoke
+ ___98-[AEDConcreteUIPrimitives presentChoicePromptWithTitle:message:confirmText:cancelText:completion:]_block_invoke_2
+ ___98-[AEDConcreteUIPrimitives presentChoicePromptWithTitle:message:confirmText:cancelText:completion:]_block_invoke_3
+ ___block_descriptor_32_e17_B16?0"UIScene"8l
+ ___block_descriptor_40_e8_32s_e14_"UILabel"8?0ls32l8
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSTimer"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e23_v16?0"UIAlertAction"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e8_v12?0B8ls32l8s40l8
+ ___block_literal_global
+ __dispatch_main_q
+ _dispatch_after
+ _dispatch_time
+ _objc_msgSend$actionWithTitle:style:handler:
+ _objc_msgSend$activateConstraints:
+ _objc_msgSend$activationState
+ _objc_msgSend$addAction:
+ _objc_msgSend$addObject:
+ _objc_msgSend$addSubview:
+ _objc_msgSend$ae_firstMatching:
+ _objc_msgSend$alertControllerWithTitle:message:preferredStyle:
+ _objc_msgSend$allObjects
+ _objc_msgSend$animateWithDuration:animations:
+ _objc_msgSend$animateWithDuration:animations:completion:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$backgroundView
+ _objc_msgSend$bottomAnchor
+ _objc_msgSend$buildView
+ _objc_msgSend$connectedScenes
+ _objc_msgSend$constraintEqualToAnchor:
+ _objc_msgSend$constraintEqualToAnchor:constant:
+ _objc_msgSend$constraintLessThanOrEqualToAnchor:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$copy
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$dismissViewControllerAnimated:completion:
+ _objc_msgSend$fontWithDescriptor:size:
+ _objc_msgSend$fontWithSize:
+ _objc_msgSend$initWithFrame:
+ _objc_msgSend$initWithPrivateStyle:
+ _objc_msgSend$initWithString:attributes:
+ _objc_msgSend$initWithTitle:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$keyWindow
+ _objc_msgSend$layer
+ _objc_msgSend$leadingAnchor
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$pointSize
+ _objc_msgSend$preferredFontDescriptorWithTextStyle:addingSymbolicTraits:options:
+ _objc_msgSend$presentViewController:animated:completion:
+ _objc_msgSend$presentedViewController
+ _objc_msgSend$removeFromSuperview
+ _objc_msgSend$role
+ _objc_msgSend$rootViewController
+ _objc_msgSend$scheduledTimerWithTimeInterval:repeats:block:
+ _objc_msgSend$session
+ _objc_msgSend$setAlpha:
+ _objc_msgSend$setFont:
+ _objc_msgSend$setLineBreakStrategy:
+ _objc_msgSend$setNeedsLayout
+ _objc_msgSend$setNumberOfLines:
+ _objc_msgSend$setShowsUserConfirmationPromptsAndBanners:
+ _objc_msgSend$setText:
+ _objc_msgSend$setTextAlignment:
+ _objc_msgSend$setTextColor:
+ _objc_msgSend$setTranslatesAutoresizingMaskIntoConstraints:
+ _objc_msgSend$setZPosition:
+ _objc_msgSend$sharedApplication
+ _objc_msgSend$showsUserConfirmationPromptsAndBanners
+ _objc_msgSend$title
+ _objc_msgSend$titleLabel
+ _objc_msgSend$topAnchor
+ _objc_msgSend$trailingAnchor
+ _objc_msgSend$view
+ _objc_msgSend$whiteColor
+ _objc_msgSend$window
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x9
+ _objc_retain_x1
+ _objc_retain_x21
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x6
CStrings:
+ "\x03"
+ "@\"UILabel\""
+ "@\"UILabel\"8@?0"
+ "@\"UIView\""
+ "@24@0:8@16"
+ "AEDBannerView"
+ "AEDConcreteUIPrimitives"
+ "AEDUIPrimitives"
+ "AEDUIPrimitivesProvider"
+ "B16@?0@\"UIScene\"8"
+ "T@\"NSString\",R,C,N,V_title"
+ "T@\"UILabel\",R,N,V_titleLabel"
+ "T@\"UIView\",R,N,V_backgroundView"
+ "TB,N,V_showsUserConfirmationPromptsAndBanners"
+ "_backgroundView"
+ "_showsUserConfirmationPromptsAndBanners"
+ "_title"
+ "_titleLabel"
+ "actionWithTitle:style:handler:"
+ "activateConstraints:"
+ "activationState"
+ "addAction:"
+ "addObject:"
+ "addSubview:"
+ "ae_firstMatching:"
+ "alertControllerWithTitle:message:preferredStyle:"
+ "allObjects"
+ "animateWithDuration:animations:"
+ "animateWithDuration:animations:completion:"
+ "arrayWithObjects:count:"
+ "backgroundView"
+ "bottomAnchor"
+ "buildView"
+ "connectedScenes"
+ "constraintEqualToAnchor:"
+ "constraintEqualToAnchor:constant:"
+ "constraintLessThanOrEqualToAnchor:"
+ "containsObject:"
+ "copy"
+ "dictionaryWithObjects:forKeys:count:"
+ "dismissViewControllerAnimated:completion:"
+ "fontWithDescriptor:size:"
+ "fontWithSize:"
+ "initWithFrame:"
+ "initWithPrivateStyle:"
+ "initWithString:attributes:"
+ "initWithTitle:"
+ "isEqualToString:"
+ "keyWindow"
+ "layer"
+ "leadingAnchor"
+ "numberWithUnsignedInt:"
+ "pointSize"
+ "preferredFontDescriptorWithTextStyle:addingSymbolicTraits:options:"
+ "presentBannerWithTitle:duration:completion:"
+ "presentChoicePromptWithTitle:message:confirmText:cancelText:completion:"
+ "presentViewController:animated:completion:"
+ "presentedViewController"
+ "removeFromSuperview"
+ "role"
+ "rootViewController"
+ "scheduledTimerWithTimeInterval:repeats:block:"
+ "session"
+ "setAlpha:"
+ "setFont:"
+ "setLineBreakStrategy:"
+ "setNeedsLayout"
+ "setNumberOfLines:"
+ "setShowsUserConfirmationPromptsAndBanners:"
+ "setText:"
+ "setTextAlignment:"
+ "setTextColor:"
+ "setTranslatesAutoresizingMaskIntoConstraints:"
+ "setZPosition:"
+ "sharedApplication"
+ "showsUserConfirmationPromptsAndBanners"
+ "title"
+ "titleLabel"
+ "topAnchor"
+ "trailingAnchor"
+ "v12@?0B8"
+ "v16@?0@\"NSTimer\"8"
+ "v16@?0@\"UIAlertAction\"8"
+ "v40@0:8@\"NSString\"16d24@?<v@?>32"
+ "v40@0:8@16d24@?32"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@?<v@?q>48"
+ "v56@0:8@16@24@32@40@?48"
+ "view"
+ "whiteColor"
+ "window"

```
