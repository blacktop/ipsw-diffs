## LowPowerModule

> `/System/Library/ControlCenter/Bundles/LowPowerModule.bundle/LowPowerModule`

```diff

-655.10.5.3.0
-  __TEXT.__text: 0x15bc
-  __TEXT.__auth_stubs: 0x270
-  __TEXT.__objc_methlist: 0x2dc
+696.0.1.0.0
+  __TEXT.__text: 0x15d0
+  __TEXT.__objc_methlist: 0x30c
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x88
-  __TEXT.__cstring: 0x1d3
+  __TEXT.__cstring: 0x1e0
   __TEXT.__oslogstring: 0x52
   __TEXT.__dlopen_cstrs: 0x4c
-  __TEXT.__unwind_info: 0x108
-  __TEXT.__objc_classname: 0x54
-  __TEXT.__objc_methname: 0x83c
-  __TEXT.__objc_methtype: 0x2c3
-  __TEXT.__objc_stubs: 0x640
-  __DATA_CONST.__got: 0x98
+  __TEXT.__unwind_info: 0x110
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xd8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c0
+  __DATA_CONST.__objc_selrefs: 0x2d8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x148
+  __DATA_CONST.__got: 0xa8
   __AUTH_CONST.__cfstring: 0x1c0
-  __AUTH_CONST.__objc_const: 0x3d8
+  __AUTH_CONST.__objc_const: 0x3e0
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0xa0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FFD4B9CF-7C77-3B4D-B2CB-BA31FB98506A
-  Functions: 46
-  Symbols:   73
-  CStrings:  170
+  UUID: 9CA12ADB-00D4-383B-959E-92502694D59E
+  Functions: 48
+  Symbols:   75
+  CStrings:  38
 
Symbols:
+ _OBJC_CLASS_$_CCUIContentModulePreviewProvider
+ _OBJC_CLASS_$_CCUIContentModuleTemplatePreviewDescription
+ _objc_claimAutoreleasedReturnValue
+ _objc_opt_self
+ _objc_release_x24
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_autorelease
- _objc_release_x23
- _objc_release_x25
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
- _objc_retain_x21
- _objc_retain_x25
CStrings:
+ "DeviceSupportsInductiveCharging"
- "#16@0:8"
- ".cxx_destruct"
- "@\"CCUIContentModuleContext\""
- "@\"NSString\"16@0:8"
- "@\"PowerUISmartChargeClient\""
- "@\"UIViewController<CCUIContentModuleBackgroundViewController>\"16@0:8"
- "@\"UIViewController<CCUIContentModuleBackgroundViewController>\"24@0:8@\"CCUIContentModulePresentationContext\"16"
- "@\"UIViewController<CCUIContentModuleContentViewController>\"16@0:8"
- "@\"UIViewController<CCUIContentModuleContentViewController>\"24@0:8@\"CCUIContentModulePresentationContext\"16"
- "@\"_PMLowPowerMode\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@?24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "CCUIContentModule"
- "CCUILowPowerModule"
- "CCUILowPowerModuleViewController"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",?,R,C,N"
- "T@\"NSString\",R,C"
- "T@\"UIViewController<CCUIContentModuleBackgroundViewController>\",?,R,N"
- "T@\"UIViewController<CCUIContentModuleContentViewController>\",?,R,N"
- "TB,?,R,N"
- "TQ,?,R,N"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_canShowWhileLocked"
- "_configureMenu"
- "_contentModuleContext"
- "_lowPowerMode"
- "_makeLocalizedMenuItem:handler:"
- "_observeSystemNotifications"
- "_smartChargeClient"
- "_unobserveSystemNotifications"
- "_updateForDarkerSystemColorsChange"
- "_updateState"
- "addObject:"
- "addObserver:selector:name:object:"
- "appearsSelected"
- "autorelease"
- "backgroundViewController"
- "backgroundViewControllerForContext:"
- "bundleForClass:"
- "buttonTapped:forEvent:"
- "class"
- "conformsToProtocol:"
- "contentModuleContext"
- "contentViewController"
- "contentViewControllerForContext:"
- "currentHandler"
- "dealloc"
- "debugDescription"
- "defaultCenter"
- "description"
- "descriptionForPackageNamed:inBundle:"
- "enableMCM:"
- "enqueueStatusUpdate:"
- "expandsGridSizeClassesForAccessibility"
- "getPowerMode"
- "glyphPackageDescription"
- "glyphState"
- "handleFailureInFunction:file:lineNumber:description:"
- "hash"
- "init"
- "initWithClientName:"
- "initWithTitle:identifier:handler:"
- "isEAconnected"
- "isEqual:"
- "isExpanded"
- "isKindOfClass:"
- "isMCMCurrentlyEnabled:"
- "isMemberOfClass:"
- "isProxy"
- "isSelected"
- "localizedStringForKey:value:table:"
- "moduleDescription"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performWithoutAnimation:"
- "performWithoutAnimationWhileHiddenInWindow:actions:"
- "reconfigureView"
- "refreshStateAnimated:"
- "release"
- "removeObserver:name:object:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "s7nuHoZIYNoOHCqT9iyZkQ"
- "self"
- "setContentModuleContext:"
- "setFlipsForRightToLeftLayoutDirection:"
- "setGlyphPackageDescription:"
- "setGlyphState:"
- "setIndentation:"
- "setLowPowerMode:"
- "setMenuItems:"
- "setMobileChargeMode:"
- "setPowerMode:fromSource:withCompletion:"
- "setSelected:"
- "setTitle:"
- "setUseTrailingCheckmarkLayout:"
- "shouldBeginTransitionToExpandedContentModule"
- "shouldExpandModuleOnTouch:"
- "shouldMCMBeDisplayed:"
- "statusUpdateWithMessage:type:"
- "stringWithUTF8String:"
- "superclass"
- "supportedGridSizeClasses"
- "temporarilyDisableMCM:"
- "toggleLowPowerMode"
- "toggleMobileChargeMode"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"CCUIContentModuleContext\"16"
- "v24@0:8@16"
- "v32@0:8@16@24"
- "viewDidLoad"
- "viewIfLoaded"
- "willTransitionToExpandedContentMode:"
- "window"
- "zone"

```
