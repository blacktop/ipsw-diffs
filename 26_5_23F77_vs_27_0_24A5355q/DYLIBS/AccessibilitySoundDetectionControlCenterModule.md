## AccessibilitySoundDetectionControlCenterModule

> `/System/Library/ControlCenter/Bundles/AccessibilitySoundDetectionControlCenterModule.bundle/AccessibilitySoundDetectionControlCenterModule`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0x39ac
-  __TEXT.__auth_stubs: 0x250
-  __TEXT.__objc_methlist: 0x36c
+3229.1.6.0.0
+  __TEXT.__text: 0x3b80
+  __TEXT.__objc_methlist: 0x384
   __TEXT.__const: 0x18
-  __TEXT.__cstring: 0x251
-  __TEXT.__gcc_except_tab: 0x448
+  __TEXT.__gcc_except_tab: 0x4ac
+  __TEXT.__cstring: 0x272
   __TEXT.__oslogstring: 0x263
-  __TEXT.__unwind_info: 0x128
-  __TEXT.__objc_classname: 0x8e
-  __TEXT.__objc_methname: 0xbb3
-  __TEXT.__objc_methtype: 0x2ff
-  __TEXT.__objc_stubs: 0x920
-  __DATA_CONST.__got: 0x118
+  __TEXT.__unwind_info: 0x118
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x378
+  __DATA_CONST.__objc_selrefs: 0x390
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x138
+  __DATA_CONST.__got: 0x130
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x380
-  __AUTH_CONST.__objc_const: 0x468
+  __AUTH_CONST.__cfstring: 0x3a0
+  __AUTH_CONST.__objc_const: 0x450
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x14
+  __DATA.__objc_ivar: 0x10
   __DATA.__data: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities
   - /System/Library/PrivateFrameworks/AXSoundDetection.framework/AXSoundDetection
-  - /System/Library/PrivateFrameworks/AXSoundDetectionUI.framework/AXSoundDetectionUI
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/ControlCenterUIKit.framework/ControlCenterUIKit

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 25D77184-41F4-3D29-A436-2B4F82299741
-  Functions: 63
-  Symbols:   85
-  CStrings:  231
+  UUID: 5E25FCF1-7620-31EA-A509-EA8898A264D1
+  Functions: 61
+  Symbols:   94
+  CStrings:  71
 
Symbols:
+ _AXDeviceIsKShotMedinaEnabled
+ _AXRuntimeCheck_SoundRecognitionMedinaKShotEnrollmentEnabled
+ _OBJC_CLASS_$_CCUIContentModulePreviewProvider
+ _OBJC_CLASS_$_CCUIContentModuleTemplatePreviewDescription
+ ___NSArray0__struct
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x24
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
CStrings:
+ "waveform.badge.magnifyingglass"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<AXCCSoundDetectionModuleViewControllerDelegate>\""
- "@\"AXCCSoundDetectionModuleViewController\""
- "@\"CCUIContentModuleContext\""
- "@\"CCUIToggleModule\""
- "@\"NSString\"16@0:8"
- "@\"UIViewController<CCUIContentModuleBackgroundViewController>\"16@0:8"
- "@\"UIViewController<CCUIContentModuleBackgroundViewController>\"24@0:8@\"CCUIContentModulePresentationContext\"16"
- "@\"UIViewController<CCUIContentModuleContentViewController>\"16@0:8"
- "@\"UIViewController<CCUIContentModuleContentViewController>\"24@0:8@\"CCUIContentModulePresentationContext\"16"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "AXCCSoundDetectionModule"
- "AXCCSoundDetectionModuleViewController"
- "AXCCSoundDetectionModuleViewControllerDelegate"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "CCUIContentModule"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<AXCCSoundDetectionModuleViewControllerDelegate>\",W,N,V_soundDetectionDelegate"
- "T@\"AXCCSoundDetectionModuleViewController\",&,N,V_contentViewController"
- "T@\"CCUIContentModuleContext\",&,N,V_contentModuleContext"
- "T@\"CCUIToggleModule\",W,N,V_module"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",?,R,C,N"
- "T@\"NSString\",R,C"
- "T@\"UIViewController<CCUIContentModuleBackgroundViewController>\",?,R,N"
- "T@\"UIViewController<CCUIContentModuleContentViewController>\",?,R,N"
- "TB,?,R,N"
- "TQ,?,R,N"
- "TQ,R"
- "URLWithString:"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_axSettingsDidChange"
- "_calculateAmountOfVisibleItems"
- "_canShowWhileLocked"
- "_configureMenuItems"
- "_confirmationAlertController"
- "_confirmedEnableSoundDetection:"
- "_confirmedToggleSoundDetectionStatusForCustomType:"
- "_confirmedToggleSoundDetectionStatusForType:"
- "_contentModuleContext"
- "_contentViewController"
- "_initializeViewContent"
- "_isHeySiriRunning"
- "_module"
- "_needsHeySiriConfirmationAlert"
- "_showConfirmationAlertForCustomType:"
- "_showConfirmationAlertForType:"
- "_soundDetectionDelegate"
- "_toggleSoundDetectionStatusForCustomType:"
- "_toggleSoundDetectionStatusForType:"
- "_updateSoundDetectionState"
- "actionWithTitle:style:handler:"
- "addAction:"
- "addObject:"
- "addSoundDetectionType:"
- "alertControllerWithTitle:message:preferredStyle:"
- "allValues"
- "autorelease"
- "axFilterObjectsUsingBlock:"
- "backgroundViewController"
- "backgroundViewControllerForContext:"
- "bundleForClass:"
- "buttonTapped:forEvent:"
- "buttonTouchDown:forEvent:"
- "category"
- "class"
- "conformsToProtocol:"
- "containsObject:"
- "contentModuleContext"
- "contentViewController"
- "contentViewControllerForContext:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d16@0:8"
- "debugDescription"
- "decodedKShotDetectors"
- "description"
- "enabledKShotDetectorIdentifiers"
- "enabledSoundDetectionTypes"
- "enqueueStatusUpdate:"
- "expandModule"
- "expandsGridSizeClassesForAccessibility"
- "hash"
- "identifier"
- "imageNamed:inBundle:"
- "init"
- "initWithNibName:bundle:"
- "initWithTitle:identifier:handler:"
- "isEqual:"
- "isEqualToString:"
- "isExpanded"
- "isKindOfClass:"
- "isMainThread"
- "isMemberOfClass:"
- "isModelReady"
- "isProxy"
- "isSelected"
- "localizedStringForKey:value:table:"
- "module"
- "moduleDescription"
- "name"
- "openSoundDetectionSettings"
- "openURL:completionHandler:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "presentViewController:animated:completion:"
- "registerUpdateBlock:forRetrieveSelector:withListener:"
- "release"
- "removeSoundDetectionType:"
- "requestExpandModule"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setContentModuleContext:"
- "setContentViewController:"
- "setFooterButtonTitle:handler:"
- "setGlyphImage:"
- "setIndentation:"
- "setKShotDetectorIsEnabled:isEnabled:"
- "setMenuItems:"
- "setModule:"
- "setSelected:"
- "setSelectedGlyphColor:"
- "setSelectedGlyphImage:"
- "setSoundDetectionDelegate:"
- "setSoundDetectionState:source:"
- "setTitle:"
- "setUseTrailingCheckmarkLayout:"
- "setVisibleMenuItems:"
- "sharedInstance"
- "sharedPreferences"
- "shouldBeginTransitionToExpandedContentModule"
- "soundDetectionDelegate"
- "soundDetectionState"
- "statusUpdateWithMessage:type:"
- "superclass"
- "supportedGridSizeClasses"
- "supportedSoundDetectionTypes"
- "systemPinkColor"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"CCUIContentModuleContext\"16"
- "v24@0:8@16"
- "v32@0:8@16@24"
- "viewDidLoad"
- "voiceTriggerEnabled"
- "willTransitionToExpandedContentMode:"
- "zone"

```
