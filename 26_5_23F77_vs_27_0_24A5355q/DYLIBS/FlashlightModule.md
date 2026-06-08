## FlashlightModule

> `/System/Library/ControlCenter/Bundles/FlashlightModule.bundle/FlashlightModule`

```diff

-655.10.5.3.0
-  __TEXT.__text: 0xa68
-  __TEXT.__auth_stubs: 0xe0
-  __TEXT.__objc_methlist: 0x320
+696.0.1.0.0
+  __TEXT.__text: 0xaac
+  __TEXT.__objc_methlist: 0x350
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x36
-  __TEXT.__unwind_info: 0xb0
-  __TEXT.__objc_classname: 0x95
-  __TEXT.__objc_methname: 0x831
-  __TEXT.__objc_methtype: 0x2ee
-  __TEXT.__objc_stubs: 0x500
-  __DATA_CONST.__got: 0x48
+  __TEXT.__cstring: 0x3a
+  __TEXT.__unwind_info: 0xa8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x298
+  __DATA_CONST.__objc_selrefs: 0x2b0
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x78
+  __DATA_CONST.__got: 0x58
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__objc_const: 0x558
+  __AUTH_CONST.__objc_const: 0x560
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x120
   __DATA_DIRTY.__objc_data: 0xf0

   - /System/Library/PrivateFrameworks/SpringBoardUI.framework/SpringBoardUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0AC0D79B-2CC9-35BE-A65B-57720FF896BF
-  Functions: 29
-  Symbols:   40
-  CStrings:  138
+  UUID: B4F100DF-D065-3DFB-9AF5-450E66E13093
+  Functions: 30
+  Symbols:   42
+  CStrings:  6
 
Symbols:
+ _OBJC_CLASS_$_CCUIContentModulePreviewProvider
+ _OBJC_CLASS_$_CCUIContentModuleTemplatePreviewDescription
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x9
+ _objc_retain_x8
- _objc_release_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"CCUIFlashlightBackgroundViewController\""
- "@\"CCUIFlashlightModuleViewController\""
- "@\"NSString\"16@0:8"
- "@\"SBUIFlashlightController\""
- "@\"UIViewController<CCUIContentModuleBackgroundViewController>\"16@0:8"
- "@\"UIViewController<CCUIContentModuleBackgroundViewController>\"24@0:8@\"CCUIContentModulePresentationContext\"16"
- "@\"UIViewController<CCUIContentModuleContentViewController>\"16@0:8"
- "@\"UIViewController<CCUIContentModuleContentViewController>\"24@0:8@\"CCUIContentModulePresentationContext\"16"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "CCUIContentModule"
- "CCUIFlashlightBackgroundViewController"
- "CCUIFlashlightModule"
- "CCUIFlashlightModuleViewController"
- "NSObject"
- "Q16@0:8"
- "SBUIFlashlightObserver"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",?,R,C,N"
- "T@\"NSString\",R,C"
- "T@\"UIViewController<CCUIContentModuleBackgroundViewController>\",?,R,N"
- "T@\"UIViewController<CCUIContentModuleBackgroundViewController>\",?,R,N,V_backgroundViewController"
- "T@\"UIViewController<CCUIContentModuleContentViewController>\",?,R,N"
- "T@\"UIViewController<CCUIContentModuleContentViewController>\",?,R,N,V_viewController"
- "TB,?,R,N"
- "TQ,?,R,N"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_backgroundViewController"
- "_canShowWhileLocked"
- "_flashlight"
- "_sliderValueDidChange:"
- "_updateControls"
- "_updateGlyphForFlashlightLevel:"
- "_updateSliderValue"
- "_viewController"
- "addObserver:"
- "addTarget:action:forControlEvents:"
- "autorelease"
- "backgroundViewController"
- "backgroundViewControllerForContext:"
- "bounds"
- "buttonTapped:forEvent:"
- "buttonView"
- "cancelTouchTracking"
- "ccui_bundleForModuleInstance:"
- "ccui_displayName"
- "class"
- "configurationWithPointSize:weight:scale:"
- "conformsToProtocol:"
- "contentViewController"
- "contentViewControllerForContext:"
- "coolDown"
- "createSliderView"
- "debugDescription"
- "description"
- "deviceSupportsDynamicFlashlightInterface"
- "deviceSupportsFlashlight"
- "dismissViewControllerAnimated:completion:"
- "expandsGridSizeClassesForAccessibility"
- "flashlightAvailabilityDidChange:"
- "flashlightLevelDidChange:"
- "flashlightOverheatedDidChange:"
- "hash"
- "initWithFrame:"
- "initWithNibName:bundle:"
- "isAvailable"
- "isEqual:"
- "isExpanded"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isSelected"
- "level"
- "moduleDescription"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setContentModuleContext:"
- "setEnabled:"
- "setFirstStepIsOff:"
- "setGlyphImage:"
- "setHeaderGlyphImage:unscaledSymbolPointSize:"
- "setLevel:"
- "setNumberOfSteps:"
- "setSelected:"
- "setSelectedGlyphColor:"
- "setSelectedGlyphImage:"
- "setStep:"
- "setTitle:"
- "sharedInstance"
- "shouldBeginTransitionToExpandedContentModule"
- "shouldFinishTransitionToExpandedContentModule"
- "sliderView"
- "step"
- "superclass"
- "supportedGridSizeClasses"
- "systemImageNamed:"
- "systemImageNamed:withConfiguration:"
- "systemIndigoColor"
- "turnFlashlightOffForReason:"
- "turnFlashlightOnForReason:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"CCUIContentModuleContext\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v32@0:8@16@24"
- "view"
- "viewDidDisappear:"
- "viewDidLoad"
- "viewWillAppear:"
- "viewWillLayoutSubviews"
- "zone"

```
