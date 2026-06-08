## WatchControlSettings

> `/System/Library/PrivateFrameworks/WatchControlSettings.framework/WatchControlSettings`

```diff

-183.11.0.0.0
-  __TEXT.__text: 0xa848
-  __TEXT.__auth_stubs: 0x4f0
+191.0.0.0.0
+  __TEXT.__text: 0x9efc
   __TEXT.__objc_methlist: 0x874
   __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x1944
+  __TEXT.__cstring: 0x1901
   __TEXT.__gcc_except_tab: 0x54
   __TEXT.__oslogstring: 0x606
   __TEXT.__dlopen_cstrs: 0x128
-  __TEXT.__unwind_info: 0x400
-  __TEXT.__objc_classname: 0x1e3
-  __TEXT.__objc_methname: 0x1a2a
-  __TEXT.__objc_methtype: 0x219
-  __TEXT.__objc_stubs: 0x1420
-  __DATA_CONST.__got: 0x198
+  __TEXT.__unwind_info: 0x3b0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2c8
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x850
+  __DATA_CONST.__objc_selrefs: 0x858
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x140
-  __AUTH_CONST.__auth_got: 0x288
+  __DATA_CONST.__got: 0x190
   __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0x2060
+  __AUTH_CONST.__cfstring: 0x2020
   __AUTH_CONST.__objc_const: 0x8b0
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_arrayobj: 0xf0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x24
   __DATA.__data: 0x100

   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6BB6C249-8DDA-3F52-AA30-1C045FD46AF3
-  Functions: 281
-  Symbols:   925
-  CStrings:  933
+  UUID: 0DEDE290-A364-317C-9A5B-CB68758659B5
+  Functions: 280
+  Symbols:   926
+  CStrings:  573
 
Symbols:
+ _OBJC_CLASS_$_PDRRegistry
+ _PDRDevicePropertyKeyIsArchived
+ _WCInputSourceTypeIsSupportedOnPDRDevice
+ ___block_literal_global.650
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$getActivePairedDeviceExcludingAltAccount
+ _objc_msgSend$getActivePairedDeviceIncludingAltAccount
+ _objc_msgSend$initWithDomain:pdrDevice:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- _NRDevicePropertyIsAltAccount
- _NRDevicePropertyIsArchived
- _OBJC_CLASS_$_NRPairedDeviceRegistry
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- ___block_literal_global.588
- _objc_msgSend$getActivePairedDevice
- _objc_msgSend$initWithDomain:pairedDevice:
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "0e581e21-36ba-4770-9408-0467585e8495"
- "15bf559d-d50b-44fe-ac84-dfba323ec985"
- "@\"<WCOnboardingObserver>\""
- "@\"CAShapeLayer\""
- "@\"NSHashTable\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8q16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "ActionMenuCustomization"
- "AutoScroll"
- "Automation"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "CGColor"
- "CGPath"
- "DwellControl"
- "Experimental"
- "FocusMovement"
- "GreyEventCustomization"
- "GreyInternal"
- "GreyQuickActions"
- "GreySupportClients"
- "GreySupportFeatures"
- "HapticFeedback"
- "InputSourceManaging"
- "LoggingModes"
- "NSObject"
- "Onboarding"
- "Private"
- "Q16@0:8"
- "QuickActionsV2"
- "T#,R"
- "T@\"<WCOnboardingObserver>\",W,N,V_onboardingObserver"
- "T@\"CAShapeLayer\",&,N,V_innerFocusOutlineLayer"
- "T@\"CAShapeLayer\",&,N,V_outerFocusOutlineLayer"
- "T@\"NSArray\",&,N"
- "T@\"NSArray\",R,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TB,N"
- "TB,N,V_increasedContrast"
- "TB,R,N"
- "TQ,N"
- "TQ,R"
- "Tf,N"
- "Tf,R,N"
- "Tq,N"
- "Tq,N,V_focusRingColor"
- "Visuals"
- "Vv16@0:8"
- "WCFocusRingShapeLayer"
- "WCGesturesOverviewViewController_iOS"
- "WCOnboardingPresenter"
- "WCOnboardingViewController_iOS"
- "WatchControlSettings"
- "WatchControlSettingsObserver"
- "WatchControlUtilities"
- "^{_NSZone=}16@0:8"
- "_accessibilityFocusRingTintColor"
- "_axScaleTransformForFocusLayerLineWidth"
- "_cancelOnboarding"
- "_focusRingColor"
- "_increasedContrast"
- "_init"
- "_innerFocusOutlineLayer"
- "_localObserverQueue"
- "_observers"
- "_observersLock"
- "_onboardingObserver"
- "_outerFocusOutlineLayer"
- "_systemImageNamed:withConfiguration:"
- "_tryItOut"
- "_tryItOutOnAppleWatch"
- "_turnOn"
- "_updateInputSourceType:enable:"
- "accessibilityDomainAccessor"
- "accessibilityDomainBoolForKey:"
- "actionMenuFavorites"
- "actionMenuLargerSize"
- "actionMenuPosition"
- "addBulletedListItemWithTitle:description:image:"
- "addButton:"
- "addEntriesFromDictionary:"
- "addObject:"
- "addSettingsObserver:"
- "addSublayer:"
- "addTarget:action:forControlEvents:"
- "allObjects"
- "applyTransform:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "array"
- "arrayByAddingObjectsFromArray:"
- "arrayForKey:"
- "arrayWithObjects:count:"
- "autoFocusNavigationSpeed"
- "automaticDigitalCrownEnablementInWaterLock"
- "automationServerEnabled"
- "autorelease"
- "bezierPathWithCGPath:"
- "boldButton"
- "boolForKey:"
- "boolForKey:keyExistsAndHasValidFormat:"
- "boolValue"
- "bounds"
- "bundleForClass:"
- "buttonTray"
- "class"
- "clearColor"
- "clearLayer"
- "closePath"
- "colorWithCGColor:"
- "colorWithHue:saturation:brightness:alpha:"
- "configurationWithTextStyle:"
- "conformsToProtocol:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createGesturesOverviewViewController"
- "d24@0:8d16"
- "dataForKey:"
- "dealloc"
- "debugDescription"
- "defaultAutoScrollSpeed"
- "description"
- "dictionary"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "didCancelOnboarding"
- "didConfirmFromOnboarding"
- "disableActiveGreySupportClients"
- "disableAllGreySupportFeatures"
- "disableInputSourceType:"
- "disablePPGDataSource"
- "dismissOnboarding"
- "dismissViewControllerAnimated:completion:"
- "domain"
- "dwellControlEnabled"
- "dwellControlShakeToStart"
- "dwellControlTimerAction"
- "eligibleGreyActivationGestures"
- "enableInputSourceType:"
- "enabledGreyFeatures"
- "enabledInputSourceTypes"
- "f16@0:8"
- "falsePositiveLoggingEnabled"
- "featureEnabled"
- "featureEnabledNPS"
- "firstObject"
- "floatForKey:keyExistsAndHasValidFormat:"
- "focusLayerForUserInterfaceStyle:"
- "focusMovementStyle"
- "focusRingColor"
- "focusRingHighContrastEnabled"
- "getActivePairedDevice"
- "getHue:saturation:brightness:alpha:"
- "glyphCharacter"
- "greyActivationGesture"
- "greyEventActionCustomizations"
- "greyEventCustomActionCustomizations"
- "greyQuickActionAutoScrollNotificationsEnabled"
- "greyQuickActionsEnabled"
- "hasGreySupportFeatureEnabled"
- "hasShownInitialOnboarding"
- "hash"
- "imageWithTintColor:renderingMode:"
- "increasedContrast"
- "informLocalObservers"
- "informObservers"
- "init"
- "initWithBarButtonSystemItem:target:action:"
- "initWithDomain:pairedDevice:"
- "initWithRootViewController:"
- "initWithTitle:detailText:icon:"
- "initWithUUIDString:"
- "innerFocusOutlineLayer"
- "inputSourcesRequireFocusRing"
- "insertObject:atIndex:"
- "intValue"
- "integerForKey:keyExistsAndHasValidFormat:"
- "integerValue"
- "isEqual:"
- "isKindOfClass:"
- "isLoaded"
- "isMemberOfClass:"
- "isProxy"
- "isVoiceOverGreySupportOn"
- "isZoomGreySupportOn"
- "lastObject"
- "layer"
- "length"
- "lineWidth"
- "load"
- "localizedStringForKey:value:table:"
- "motionPointerActivationDuration"
- "motionPointerActivationDurationMax"
- "motionPointerActivationDurationMin"
- "motionPointerEdgeActionCustomizations"
- "motionPointerMovementTolerance"
- "motionPointerSensitivity"
- "motionPointerSensitivityMax"
- "motionPointerSensitivityMin"
- "mutableCopy"
- "navigationController"
- "navigationItem"
- "numberWithBool:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "onboardingObserver"
- "outerFocusOutlineLayer"
- "parentLayerForUserInterfaceStyle:"
- "path"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "playDetectedGestureHapticFeedback"
- "presentGesturesOverviewFromViewController:withObserver:"
- "presentOnboardingFromViewController:withObserver:"
- "presentViewController:animated:completion:"
- "pushViewController:animated:"
- "q16@0:8"
- "quickActionsV2Enabled"
- "quickActionsV2EnabledNPS"
- "quickActionsV2State"
- "receivedActivationGesture"
- "release"
- "removeCustomActionForGreyEvent:"
- "removeObject:"
- "removeObjectForKey:"
- "removeSettingsObserver:"
- "requestToShowPracticeGrey"
- "resetGreyEventActionCustomizations"
- "resetMotionPointerEdgeActionCustomizations"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "safeValueForKey:"
- "scaledOutlineWidth:"
- "selectedLayerForUserInterfaceStyle:"
- "selectedParentLayerForUserInterfaceStyle:"
- "self"
- "setAccessibilityDomainBool:forKey:"
- "setAction:forGreyEvent:"
- "setAction:forMotionPointerEdge:"
- "setActionMenuFavorites:"
- "setActionMenuLargerSize:"
- "setActionMenuPosition:"
- "setAutoFocusNavigationSpeed:"
- "setAutomaticDigitalCrownEnablementInWaterLock:"
- "setAutomationServerEnabled:"
- "setBool:forKey:"
- "setCustomActionType:withCustomActionIdentifier:forGreyEvent:"
- "setDefaultAutoScrollSpeed:"
- "setDisablePPGDataSource:"
- "setDwellControlEnabled:"
- "setDwellControlShakeToStart:"
- "setDwellControlTimerAction:"
- "setFalsePositiveLoggingEnabled:"
- "setFeatureEnabled:"
- "setFillColor:"
- "setFloat:forKey:"
- "setFocusMovementStyle:"
- "setFocusRingColor:"
- "setFocusRingHighContrastEnabled:"
- "setGreyActivationGesture:"
- "setGreyQuickActionAutoScrollNotificationsEnabled:"
- "setGreyQuickActionsEnabled:"
- "setHasShownInitialOnboarding:"
- "setIncreasedContrast:"
- "setInnerFocusOutlineLayer:"
- "setInputSourcesRequireFocusRing:"
- "setInteger:forKey:"
- "setLeftBarButtonItem:"
- "setLineWidth:"
- "setMotionPointerActivationDuration:"
- "setMotionPointerMovementTolerance:"
- "setMotionPointerSensitivity:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOnboardingObserver:"
- "setOuterFocusOutlineLayer:"
- "setPath:"
- "setPlayDetectedGestureHapticFeedback:"
- "setQuickActionsV2State:"
- "setReceivedActivationGesture:"
- "setRequestToShowPracticeGrey:"
- "setShowDetectedGestureBanner:"
- "setShowGestureRecognizerIndicator:"
- "setStrokeColor:"
- "setTitle:forState:"
- "setVoiceOverHandGestures:"
- "setWatchControlHandGeturesEnabled:"
- "setWithArray:"
- "setZoomDomainBool:forKey:"
- "setZoomHandGestures:"
- "sharedInstance"
- "sharedManager"
- "shortcutForIdentifier:"
- "shortcutName"
- "showDetectedGestureBanner"
- "showGestureRecognizerIndicator"
- "stringByAppendingString:"
- "stringWithFormat:"
- "strokeColorForFocusOutline"
- "superclass"
- "superlayer"
- "supportsCapability:"
- "synchronize"
- "synchronizeNanoDomain:keys:"
- "unarchivedDictionaryWithKeysOfClass:objectsOfClass:fromData:error:"
- "unarchivedObjectOfClasses:fromData:error:"
- "unsignedIntegerValue"
- "updateAppearance"
- "updateCachedSettings"
- "updateFocusOutlinePath"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8f16"
- "v24@0:8@\"WatchControlSettings\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8^{CGPath=}16"
- "v24@0:8q16"
- "v28@0:8B16@20"
- "v28@0:8Q16B24"
- "v32@0:8@16@24"
- "v32@0:8Q16q24"
- "v40@0:8q16@24q32"
- "valueForProperty:"
- "viewControllers"
- "viewDidLoad"
- "viewTintColor"
- "voiceOverGreySupportEnabled"
- "voiceOverHandGesturesEnabled"
- "watchControlDomainAccessor"
- "watchControlGreySupportEnabled"
- "watchControlHandGesturesEnabled"
- "watchControlSettingsDidChange:"
- "weakObjectsHashTable"
- "whiteColor"
- "zone"
- "zoomDomainAccessor"
- "zoomDomainBoolForKey:"
- "zoomGreySupportEnabled"
- "zoomHandGesturesEnabled"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
