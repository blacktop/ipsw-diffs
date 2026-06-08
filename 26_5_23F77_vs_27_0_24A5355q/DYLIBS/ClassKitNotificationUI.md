## ClassKitNotificationUI

> `/System/Library/PrivateFrameworks/ClassKitNotificationUI.framework/ClassKitNotificationUI`

```diff

-151.5.0.0.0
-  __TEXT.__text: 0x3e14
-  __TEXT.__auth_stubs: 0x350
+152.0.10.0.0
+  __TEXT.__text: 0x3964
   __TEXT.__objc_methlist: 0x56c
   __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0x13b
+  __TEXT.__cstring: 0x144
   __TEXT.__gcc_except_tab: 0x28
   __TEXT.__oslogstring: 0x94
-  __TEXT.__unwind_info: 0x1f0
-  __TEXT.__objc_classname: 0x101
-  __TEXT.__objc_methname: 0x12d7
-  __TEXT.__objc_methtype: 0x29e
-  __TEXT.__objc_stubs: 0x1200
-  __DATA_CONST.__got: 0x140
+  __TEXT.__unwind_info: 0x198
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1a0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_selrefs: 0x5f8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__got: 0x138
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0x860
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x44
   __DATA.__data: 0x120

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F4A808E2-E6DC-3B10-A1F2-D52F6BA799B6
+  UUID: 9005FF67-E6A9-3DC9-81B4-942BD806130F
   Functions: 106
-  Symbols:   107
-  CStrings:  298
+  Symbols:   112
+  CStrings:  15
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x22
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- _OBJC_CLASS_$_UIScreen
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"CLSNotificationBannerView\""
- "@\"CLSNotificationBannerViewController\""
- "@\"NSDate\""
- "@\"NSLayoutConstraint\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"NSString\"16@0:8"
- "@\"UIImageView\""
- "@\"UILabel\""
- "@\"UIStackView\""
- "@\"UIWindow\""
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24@?32"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B40@0:8{CGPoint=dd}16@32"
- "CLSNotificationBanner"
- "CLSNotificationBannerDisplayManager"
- "CLSNotificationBannerView"
- "CLSNotificationBannerViewController"
- "CLSNotificationBannerWindow"
- "CLSRemoteViewController"
- "CLSRemoteViewControllerInterface"
- "CLSServiceViewControllerInterface"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"CLSNotificationBannerView\",&,N,V_bannerView"
- "T@\"CLSNotificationBannerViewController\",&,N,V_currentBannerViewController"
- "T@\"NSDate\",&,N,V_lastBannerTime"
- "T@\"NSLayoutConstraint\",&,N,V_bannerWidthConstraint"
- "T@\"NSLayoutConstraint\",&,N,V_bannerYPositionConstraint"
- "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_bannerSemaphore"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"UIImageView\",&,N,V_imageView"
- "T@\"UILabel\",&,N,V_messageLabel"
- "T@\"UILabel\",&,N,V_titleLabel"
- "T@\"UIStackView\",&,N,V_labelsStackView"
- "T@\"UIWindow\",&,N,V_previousKeyWindow"
- "T@\"UIWindow\",&,N,V_window"
- "T@?,C,N,V_completionHandler"
- "TB,N,V_bannerAnimating"
- "TB,N,V_bannerVisible"
- "TQ,R"
- "Td,N,V_duration"
- "Td,R,N,V_preferredWidthPad"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_bannerAnimating"
- "_bannerSemaphore"
- "_bannerView"
- "_bannerVisible"
- "_bannerWidthConstraint"
- "_bannerYPositionConstraint"
- "_canAffectStatusBarAppearance"
- "_completionHandler"
- "_currentBannerViewController"
- "_duration"
- "_hiddenBannerPosition:"
- "_hideBanner:quickly:"
- "_imageView"
- "_includeInDefaultImageSnapshot"
- "_labelsStackView"
- "_lastBannerTime"
- "_messageLabel"
- "_preferredWidthPad"
- "_preventsAppearanceProxyCustomization"
- "_previousKeyWindow"
- "_showBanner:"
- "_titleLabel"
- "_visibleBannerCenterPosition:"
- "_window"
- "activateConstraints:"
- "activationState"
- "addArrangedSubview:"
- "addBannerView:"
- "addConstraint:"
- "addConstraintsForBannerView"
- "addGestureRecognizer:"
- "addSubview:"
- "animateAlongsideTransition:completion:"
- "animateWithDuration:delay:options:animations:completion:"
- "applyConstraints"
- "arrayWithObjects:count:"
- "autorelease"
- "bannerAnimating"
- "bannerMessageAttributes"
- "bannerSemaphore"
- "bannerTitleAttributes"
- "bannerView"
- "bannerVisible"
- "bannerWidthConstraint"
- "bannerWidthForViewSize:"
- "bannerWindow"
- "bannerYPositionConstraint"
- "bottomAnchor"
- "bounds"
- "bundle"
- "bundleForClass:"
- "callCompletionHandler"
- "centerYAnchor"
- "class"
- "clearColor"
- "code"
- "completionHandler"
- "conformsToProtocol:"
- "connectedScenes"
- "constant"
- "constraintEqualToAnchor:"
- "constraintEqualToAnchor:constant:"
- "constraintWithItem:attribute:relatedBy:toItem:attribute:multiplier:constant:"
- "containsObject:"
- "countByEnumeratingWithState:objects:count:"
- "currentBannerViewController"
- "currentDevice"
- "currentTraitCollection"
- "d"
- "d16@0:8"
- "d32@0:8{CGSize=dd}16"
- "date"
- "debugDescription"
- "description"
- "dictionaryWithObject:forKey:"
- "dictionaryWithObjects:forKeys:count:"
- "dismissViewControllerAnimated:completion:"
- "duration"
- "enqueBanner:"
- "exportedInterface"
- "extensionsWithMatchingAttributes:error:"
- "firstObject"
- "frame"
- "handlePan:"
- "handleWindowPan:"
- "hash"
- "hideBanner"
- "hideBannerQuickly:"
- "hitTest:"
- "imageNamed:inBundle:"
- "imageView"
- "init"
- "initWithFrame:"
- "initWithImage:"
- "initWithPrivateStyle:"
- "initWithString:attributes:"
- "initWithTarget:action:"
- "initWithTitle:image:message:"
- "initWithTitle:imageView:message:"
- "initWithTitle:message:"
- "initWithWindowScene:"
- "instantiateViewControllerWithInputItems:identifier:connectionHandler:"
- "instantiateViewControllerWithInputItems:listenerEndpoint:connectionHandler:"
- "interfaceWithProtocol:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "keyWindow"
- "labelColor"
- "labelsStackView"
- "lastBannerTime"
- "layer"
- "layoutIfNeeded"
- "leadingAnchor"
- "mainScreen"
- "makeKeyAndVisible"
- "messageLabel"
- "objectsPassingTest:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pointInside:withEvent:"
- "preferredFontForTextStyle:"
- "preferredWidthPad"
- "presentModallyInNewWindowWithCompletion:"
- "presentViewController:animated:completion:"
- "presentationLayer"
- "previousKeyWindow"
- "queue"
- "release"
- "removeFromSuperview"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "rootViewController"
- "self"
- "serviceViewControllerInterface"
- "serviceViewControllerProxy"
- "setAdjustsFontSizeToFitWidth:"
- "setAlignment:"
- "setAlpha:"
- "setAttributedText:"
- "setAxis:"
- "setBackgroundColor:"
- "setBannerAnimating:"
- "setBannerSemaphore:"
- "setBannerView:"
- "setBannerVisible:"
- "setBannerWidthConstraint:"
- "setBannerYPositionConstraint:"
- "setClipsToBounds:"
- "setCompletionHandler:"
- "setConstant:"
- "setContentMode:"
- "setCornerRadius:"
- "setCurrentBannerViewController:"
- "setDistribution:"
- "setDuration:"
- "setHidden:"
- "setImageView:"
- "setLabelsStackView:"
- "setLastBannerTime:"
- "setLineBreakMode:"
- "setMasksToBounds:"
- "setMessageLabel:"
- "setMinimumScaleFactor:"
- "setModalPresentationStyle:"
- "setNumberOfLines:"
- "setOpaque:"
- "setPreviousKeyWindow:"
- "setRootViewController:"
- "setTextAlignment:"
- "setTitleLabel:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setUserInteractionEnabled:"
- "setWindow:"
- "setWindowLevel:"
- "shared"
- "sharedApplication"
- "showBannerWithTitle:message:"
- "showBannerWithTitle:message:completionHandler:"
- "showCurrentBanner"
- "showPrivacyModalViewWithInfo:"
- "showWithCompletionHandler:"
- "sizeToFit"
- "statusBarFrame"
- "statusBarManager"
- "subviews"
- "superclass"
- "superview"
- "supportedInterfaceOrientations"
- "supportedInterfaceOrientationsForWindow:"
- "systemBackgroundColor"
- "timeIntervalSinceNow"
- "titleLabel"
- "topAnchor"
- "trailingAnchor"
- "traitCollection"
- "translationInView:"
- "userInterfaceIdiom"
- "userInterfaceStyle"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8d16"
- "v28@0:8@16B24"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?>20"
- "v32@0:8@16@24"
- "v40@0:8@16@24@?32"
- "v40@0:8{CGSize=dd}16@32"
- "view"
- "viewDidInvalidateIntrinsicContentSize"
- "viewServiceDidTerminateWithError:"
- "viewWillTransitionToSize:withTransitionCoordinator:"
- "window"
- "windowPointInside:withEvent:"
- "windowScene"
- "zone"
- "{CGPoint=dd}32@0:8{CGSize=dd}16"

```
