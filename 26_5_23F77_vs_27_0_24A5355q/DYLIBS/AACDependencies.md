## AACDependencies

> `/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACDependencies.framework/AACDependencies`

```diff

-28.122.2.0.0
-  __TEXT.__text: 0x1d80
-  __TEXT.__auth_stubs: 0x240
-  __TEXT.__objc_methlist: 0x344
+50.0.0.0.0
+  __TEXT.__text: 0x1c8c
+  __TEXT.__objc_methlist: 0x35c
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x79
-  __TEXT.__unwind_info: 0xf0
-  __TEXT.__objc_classname: 0x17a
-  __TEXT.__objc_methname: 0xffa
-  __TEXT.__objc_methtype: 0x1a9
-  __TEXT.__objc_stubs: 0xd00
-  __DATA_CONST.__got: 0xd8
+  __TEXT.__cstring: 0x80
+  __TEXT.__unwind_info: 0xf8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x160
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3f0
+  __DATA_CONST.__objc_selrefs: 0x408
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x128
-  __AUTH_CONST.__objc_const: 0xac0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__objc_const: 0xaf0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x64
+  __DATA.__objc_ivar: 0x68
   __DATA.__data: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1F26B126-BA38-3504-9B89-1139B82C7BC5
-  Functions: 70
-  Symbols:   429
-  CStrings:  215
+  UUID: A69B8E63-A627-3D33-99DC-4AF4AB86389D
+  Functions: 71
+  Symbols:   439
+  CStrings:  6
 
Symbols:
+ -[AEDSingleAppModeConfiguration allowsAccessibilityVoiceOver]
+ -[AEDSingleAppModeConfiguration setAllowsAccessibilityVoiceOver:]
+ _OBJC_IVAR_$_AEDSingleAppModeConfiguration._allowsAccessibilityVoiceOver
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$allowsAccessibilityVoiceOver
+ _objc_msgSend$setAllowKeyboardPeriodShortcut:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
CStrings:
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSDictionary\"16@0:8"
- "@\"NSNotificationCenter\""
- "@\"NSObject\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"UIAutonomousSingleAppModeSession\""
- "@\"UILabel\""
- "@\"UIView\""
- "@16@0:8"
- "@24@0:8@16"
- "@?"
- "AEDBannerView"
- "AEDConcreteSingleAppModePrimitives"
- "AEDConcreteSingleAppModeSession"
- "AEDConcreteUIPrimitives"
- "AEDDictionaryEncodable"
- "AEDNotificationObservation"
- "AEDObservation"
- "AEDSingleAppModeConfiguration"
- "AEDSingleAppModePrimitives"
- "AEDSingleAppModePrimitivesProvider"
- "AEDSingleAppModeSession"
- "AEDUIPrimitives"
- "AEDUIPrimitivesProvider"
- "AEDUnionObservation"
- "B"
- "B16@0:8"
- "MCConfigurationAdditions"
- "MCSingleAppModeConfigurationRepresentation"
- "T@\"MCSingleAppModeConfiguration\",R,N"
- "T@\"NSDictionary\",R,C,N"
- "T@\"NSString\",R,C,N,V_title"
- "T@\"UILabel\",R,N,V_titleLabel"
- "T@\"UIView\",R,N,V_backgroundView"
- "TB,N,V_allowsAccessibilityLiveCaptions"
- "TB,N,V_allowsAccessibilityReader"
- "TB,N,V_allowsAccessibilitySpeech"
- "TB,N,V_allowsAccessibilityTypingFeedback"
- "TB,N,V_allowsActivityContinuation"
- "TB,N,V_allowsAutoCorrection"
- "TB,N,V_allowsContinuousPathKeyboard"
- "TB,N,V_allowsDictation"
- "TB,N,V_allowsEmojiKeyboard"
- "TB,N,V_allowsKeyboardShortcuts"
- "TB,N,V_allowsPasswordAutoFill"
- "TB,N,V_allowsPredictiveKeyboard"
- "TB,N,V_allowsSmartPunctuation"
- "TB,N,V_allowsSpellCheck"
- "TB,N,V_showsUserConfirmationPromptsAndBanners"
- "_allowsAccessibilityLiveCaptions"
- "_allowsAccessibilityReader"
- "_allowsAccessibilitySpeech"
- "_allowsAccessibilityTypingFeedback"
- "_allowsActivityContinuation"
- "_allowsAutoCorrection"
- "_allowsContinuousPathKeyboard"
- "_allowsDictation"
- "_allowsEmojiKeyboard"
- "_allowsKeyboardShortcuts"
- "_allowsPasswordAutoFill"
- "_allowsPredictiveKeyboard"
- "_allowsSmartPunctuation"
- "_allowsSpellCheck"
- "_backgroundView"
- "_notificationCenter"
- "_notificationHandler"
- "_notificationName"
- "_object"
- "_observations"
- "_queue"
- "_session"
- "_showsUserConfirmationPromptsAndBanners"
- "_title"
- "_titleLabel"
- "activateConstraints:"
- "activateSingleAppModeSessionWithConfiguration:completion:"
- "activationState"
- "addObject:"
- "addSubview:"
- "ae_firstMatching:"
- "allObjects"
- "allowsAccessibilityLiveCaptions"
- "allowsAccessibilityReader"
- "allowsAccessibilitySpeech"
- "allowsAccessibilityTypingFeedback"
- "allowsActivityContinuation"
- "allowsAutoCorrection"
- "allowsContinuousPathKeyboard"
- "allowsDictation"
- "allowsEmojiKeyboard"
- "allowsKeyboardShortcuts"
- "allowsPasswordAutoFill"
- "allowsPredictiveKeyboard"
- "allowsSmartPunctuation"
- "allowsSpellCheck"
- "animateWithDuration:animations:"
- "animateWithDuration:animations:completion:"
- "arrayWithObjects:count:"
- "backgroundView"
- "bottomAnchor"
- "buildView"
- "connectedScenes"
- "constraintEqualToAnchor:"
- "constraintEqualToAnchor:constant:"
- "constraintLessThanOrEqualToAnchor:"
- "containsObject:"
- "copy"
- "countByEnumeratingWithState:objects:count:"
- "deactivateWithCompletion:"
- "dealloc"
- "defaultConfigurationForStyle:"
- "dictionaryValue"
- "dictionaryWithObjects:forKeys:count:"
- "endWithCompletion:"
- "fontWithDescriptor:size:"
- "fontWithSize:"
- "init"
- "initWithFrame:"
- "initWithPrivateStyle:"
- "initWithString:attributes:"
- "initWithTitle:"
- "invalidate"
- "isEqualToString:"
- "keyWindow"
- "layer"
- "leadingAnchor"
- "makePrimitives"
- "mutableCopy"
- "notificationDidFire:"
- "numberWithUnsignedInt:"
- "pointSize"
- "preferredFontDescriptorWithTextStyle:addingSymbolicTraits:options:"
- "presentBannerWithTitle:duration:completion:"
- "presentedViewController"
- "removeFromSuperview"
- "removeObserver:name:object:"
- "requestSessionWithConfiguration:completion:"
- "role"
- "rootViewController"
- "serializedConfiguration"
- "session"
- "setAllowAccessibilityLiveCaptions:"
- "setAllowAccessibilityReader:"
- "setAllowAccessibilityReaderSuggestions:"
- "setAllowAccessibilitySpeech:"
- "setAllowAccessibilityTypingFeedback:"
- "setAllowAccessibilityVoiceOver:"
- "setAllowActivityContinuation:"
- "setAllowAutoCorrection:"
- "setAllowContinuousPathKeyboard:"
- "setAllowDefinitionLookup:"
- "setAllowDictation:"
- "setAllowEmojiKeyboard:"
- "setAllowKeyboardShortcuts:"
- "setAllowPasswordAutoFill:"
- "setAllowPredictiveKeyboard:"
- "setAllowQuickNote:"
- "setAllowScreenShot:"
- "setAllowSmartPunctuation:"
- "setAllowSpellCheck:"
- "setAllowTranslationLookup:"
- "setAllowsAccessibilityLiveCaptions:"
- "setAllowsAccessibilityReader:"
- "setAllowsAccessibilitySpeech:"
- "setAllowsAccessibilityTypingFeedback:"
- "setAllowsActivityContinuation:"
- "setAllowsAutoCorrection:"
- "setAllowsContinuousPathKeyboard:"
- "setAllowsDictation:"
- "setAllowsEmojiKeyboard:"
- "setAllowsKeyboardShortcuts:"
- "setAllowsPasswordAutoFill:"
- "setAllowsPredictiveKeyboard:"
- "setAllowsSmartPunctuation:"
- "setAllowsSpellCheck:"
- "setAlpha:"
- "setAutomaticallyRelaunchesAfterAppCrash:"
- "setFont:"
- "setLineBreakMode:"
- "setManagedConfigurationSettings:"
- "setNeedsLayout"
- "setNumberOfLines:"
- "setObject:forKeyedSubscript:"
- "setShowsUserConfirmationPromptsAndBanners:"
- "setText:"
- "setTextAlignment:"
- "setTextColor:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setZPosition:"
- "sharedApplication"
- "showsUserConfirmationPromptsAndBanners"
- "title"
- "titleLabel"
- "topAnchor"
- "trailingAnchor"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v32@0:8@\"AEDSingleAppModeConfiguration\"16@?<v@?@\"<AEDSingleAppModeSession>\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "v40@0:8@\"NSString\"16d24@?<v@?>32"
- "v40@0:8@16d24@?32"
- "view"
- "whiteColor"
- "window"

```
