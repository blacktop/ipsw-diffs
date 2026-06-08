## TranslationUIServices

> `/System/Library/PrivateFrameworks/TranslationUIServices.framework/TranslationUIServices`

```diff

-365.13.0.0.0
-  __TEXT.__text: 0x3af4
-  __TEXT.__auth_stubs: 0x2f0
+380.1.0.0.0
+  __TEXT.__text: 0x378c
   __TEXT.__objc_methlist: 0x604
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x204
+  __TEXT.__cstring: 0x20a
   __TEXT.__oslogstring: 0x349
   __TEXT.__gcc_except_tab: 0x90
-  __TEXT.__unwind_info: 0x188
-  __TEXT.__objc_classname: 0xee
-  __TEXT.__objc_methname: 0x137f
-  __TEXT.__objc_methtype: 0x222
-  __TEXT.__objc_stubs: 0x1160
-  __DATA_CONST.__got: 0x108
+  __TEXT.__unwind_info: 0x158
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x180
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_selrefs: 0x608
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x188
+  __DATA_CONST.__got: 0x108
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x220
   __AUTH_CONST.__objc_const: 0x8b0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x50
   __DATA.__data: 0x188

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7BFDD3D7-3050-358E-B484-3432265B2A52
-  Functions: 134
-  Symbols:   616
-  CStrings:  350
+  UUID: 3E91D81A-5186-3B16-BD11-E0A7190FF9D7
+  Functions: 132
+  Symbols:   617
+  CStrings:  64
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x3
+ _objc_retain_x8
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
- _objc_retain_x23
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@"
- "@\"<LTUIViewServiceExtensionHostProtocol>\""
- "@\"<NSCopying>\""
- "@\"LTUIRemoteViewController\""
- "@\"LTUISourceMeta\""
- "@\"NSArray\""
- "@\"NSAttributedString\""
- "@\"NSExtension\""
- "@\"NSLocale\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"_UIRemoteViewController\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "LTUIErrorViewController"
- "LTUIRemoteViewController"
- "LTUISourceMeta"
- "LTUITranslationViewController"
- "LTUIViewServiceExtension"
- "LTUIViewServiceExtensionHostProtocol"
- "LTUIViewServiceExtensionProtocol"
- "NSObject"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"<LTUIViewServiceExtensionHostProtocol>\",W,N,V_delegate"
- "T@\"<NSCopying>\",&,N,V_requestID"
- "T@\"LTUIRemoteViewController\",&,N,V_remoteViewController"
- "T@\"LTUISourceMeta\",&,N,V_sourceMeta"
- "T@\"NSArray\",C,N,V_ignoredAttributes"
- "T@\"NSArray\",C,N,V_languageHints"
- "T@\"NSAttributedString\",C,N,V_text"
- "T@\"NSExtension\",&,N,V_currentExtension"
- "T@\"NSLocale\",C,N,V_sourceLocale"
- "T@\"NSLocale\",C,N,V_targetLocale"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_context"
- "T@\"NSString\",R,C"
- "T@\"_UIRemoteViewController\",R,N"
- "T@,&,N,V_matchingToken"
- "T@?,C,N,V_dismissCompletionHandler"
- "T@?,C,N,V_replacementHandler"
- "TB,N,V_consentDisplayOnly"
- "TB,N,V_isSourceEditable"
- "TB,N,V_userConsentConfirmed"
- "TB,R,GisAvailable"
- "TQ,N,V_origin"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_UIRemoteViewControllerContaining"
- "__LTUI_viewServiceExtensionHostInterface"
- "__LTUI_viewServiceExtensionInterface"
- "_animateUsingDefaultDampedSpringWithDelay:initialSpringVelocity:options:animations:completion:"
- "_beginDelayingPresentation:cancellationHandler:"
- "_canShowWhileLocked"
- "_cleanUpExtension"
- "_consentDisplayOnly"
- "_containedRemoteViewController"
- "_context"
- "_currentExtension"
- "_delegate"
- "_dismissCompletionHandler"
- "_endDelayingPresentation"
- "_existingPresentationControllerImmediate:effective:"
- "_ignoredAttributes"
- "_insertBackground"
- "_isInPopoverPresentation"
- "_isSourceEditable"
- "_languageHints"
- "_matchingToken"
- "_origin"
- "_presentError:"
- "_presentationController:prepareAdaptivePresentationController:"
- "_presentationControllerDidDismiss:"
- "_refreshExtensionList"
- "_refreshForSystemExtension"
- "_remoteViewController"
- "_removeBackground"
- "_replacementHandler"
- "_requestID"
- "_setBackgroundBlurDisabled:"
- "_setChildController:"
- "_setShouldDismissWhenTappedOutside:"
- "_sheetPresentationController"
- "_sourceLocale"
- "_sourceMeta"
- "_targetLocale"
- "_text"
- "_updateBackground"
- "_userConsentConfirmed"
- "_userInfo"
- "actionWithHandler:"
- "activateConstraints:"
- "adaptForPresentationInPopover:"
- "addChildViewController:"
- "addSubview:"
- "arguments"
- "arrayWithObjects:count:"
- "autorelease"
- "available"
- "beginMatchingExtensionsWithAttributes:completion:"
- "bottomAnchor"
- "bounds"
- "bundleForClass:"
- "cancelExtensionRequestWithIdentifier:"
- "centerYAnchor"
- "class"
- "clearColor"
- "confirmUserConsent"
- "conformsToProtocol:"
- "consentDisplayOnly"
- "constraintEqualToAnchor:"
- "constraintEqualToSystemSpacingAfterAnchor:multiplier:"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "cplID"
- "currentExtension"
- "debugDescription"
- "delegate"
- "description"
- "detents"
- "dictionaryRepresentation"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "didMoveToParentViewController:"
- "didReceiveMemoryWarning"
- "dismiss"
- "dismissCompletionHandler"
- "dismissViewControllerAnimated:completion:"
- "drawCloseButton"
- "effectWithStyle:"
- "endMatchingExtensions:"
- "errorWithDomain:code:userInfo:"
- "expandSheet"
- "exportedInterface"
- "extensionQueryID"
- "finishWithError:"
- "finishWithTranslation:"
- "firstObject"
- "hash"
- "identifier"
- "ignoredAttributes"
- "init"
- "initWithBarButtonSystemItem:primaryAction:"
- "initWithEffect:"
- "initWithError:"
- "initWithFrame:"
- "initWithNibName:bundle:"
- "initWithString:"
- "initialize"
- "insertSubview:atIndex:"
- "instantiateViewControllerWithInputItems:connectionHandler:"
- "interfaceWithProtocol:"
- "invalidate"
- "isAvailable"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isSourceEditable"
- "largeDetent"
- "layoutIfNeeded"
- "leadingAnchor"
- "localeIdentifier"
- "localizedStringForKey:value:table:"
- "matchingToken"
- "mediumDetent"
- "navigationItem"
- "numberWithBool:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performWithoutAnimation:"
- "preferredContentSize"
- "preferredFontForTextStyle:"
- "presentationController"
- "presentingViewController"
- "processInfo"
- "receiveExtensions:"
- "release"
- "remoteIsReady"
- "remoteViewController"
- "removeFromParentViewController"
- "removeFromSuperview"
- "replacementHandler"
- "requestID"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "safeAreaLayoutGuide"
- "secondaryLabelColor"
- "self"
- "serviceViewControllerInterface"
- "serviceViewControllerProxy"
- "setAttributedContentText:"
- "setAutoresizingMask:"
- "setBackgroundColor:"
- "setConsentDisplayOnly:"
- "setContext:"
- "setCurrentExtension:"
- "setDelegate:"
- "setDetents:"
- "setDismissCompletionHandler:"
- "setFont:"
- "setFrame:"
- "setIgnoredAttributes:"
- "setIsSourceEditable:"
- "setLanguageHints:"
- "setLargestUndimmedDetentIdentifier:"
- "setMatchingToken:"
- "setMaximumContentSizeCategory:"
- "setNumberOfLines:"
- "setObject:forKeyedSubscript:"
- "setOrigin:"
- "setPreferredContentSize:"
- "setPrefersGrabberVisible:"
- "setRemoteViewController:"
- "setReplacementHandler:"
- "setRequestID:"
- "setRequestInterruptionBlock:"
- "setRightBarButtonItem:"
- "setSelectedDetentIdentifier:"
- "setSourceLocale:"
- "setSourceMeta:"
- "setTag:"
- "setTargetLocale:"
- "setText:"
- "setTextAlignment:"
- "setTextColor:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setUserConsentConfirmed:"
- "setUserInfo:"
- "setViewControllers:"
- "sourceLocale"
- "sourceMeta"
- "string"
- "subviews"
- "superclass"
- "targetLocale"
- "text"
- "topAnchor"
- "trailingAnchor"
- "userConsentConfirmed"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSAttributedString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v32@0:8@16@24"
- "v40@0:8{CGSize=dd}16@32"
- "view"
- "viewControllers"
- "viewDidAppear:"
- "viewDidDisappear:"
- "viewDidLayoutSubviews"
- "viewDidLoad"
- "viewServiceDidTerminateWithError:"
- "viewWillAppear:"
- "viewWillTransitionToSize:withTransitionCoordinator:"
- "viewWithTag:"
- "willMoveToParentViewController:"
- "window"
- "zone"

```
