## AirPlayMirroringModule

> `/System/Library/ControlCenter/Bundles/AirPlayMirroringModule.bundle/AirPlayMirroringModule`

```diff

-4023.110.7.0.0
-  __TEXT.__text: 0xc8
-  __TEXT.__auth_stubs: 0x40
-  __TEXT.__objc_methlist: 0x50
-  __TEXT.__unwind_info: 0x54
-  __TEXT.__objc_classname: 0x38
-  __TEXT.__objc_methname: 0x339
-  __TEXT.__objc_methtype: 0x28a
-  __TEXT.__objc_stubs: 0x20
-  __DATA_CONST.__objc_classlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x10
+4023.210.1.0.0
+  __TEXT.__text: 0x13ac
+  __TEXT.__auth_stubs: 0x1d0
+  __TEXT.__objc_methlist: 0x1bc
+  __TEXT.__const: 0x18
+  __TEXT.__gcc_except_tab: 0x68
+  __TEXT.__cstring: 0x8b
+  __TEXT.__unwind_info: 0xec
+  __TEXT.__objc_classname: 0x91
+  __TEXT.__objc_methname: 0xb7f
+  __TEXT.__objc_methtype: 0x3ba
+  __TEXT.__objc_stubs: 0x8c0
+  __DATA_CONST.__got: 0x10
+  __DATA_CONST.__const: 0x140
+  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4f0
-  __DATA_CONST.__objc_selrefs: 0x30
-  __AUTH_CONST.__objc_const: 0x48
-  __AUTH_CONST.__auth_got: 0x28
-  __DATA.__objc_classrefs: 0x8
-  __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0xc0
+  __DATA_CONST.__objc_const: 0xa78
+  __DATA_CONST.__objc_selrefs: 0x2c8
+  __AUTH_CONST.__objc_const: 0xd8
+  __AUTH_CONST.__cfstring: 0xc0
+  __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__auth_got: 0xf8
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_classrefs: 0x68
+  __DATA.__objc_superrefs: 0x10
+  __DATA.__objc_ivar: 0x18
+  __DATA.__data: 0x120
   __DATA_DIRTY.__objc_data: 0x50
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/ControlCenterUIKit.framework/ControlCenterUIKit
+  - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/MediaControls.framework/MediaControls
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6
-  Symbols:   11
-  CStrings:  66
+  Functions: 44
+  Symbols:   63
+  CStrings:  184
 
Symbols:
+ _MRUMirroringGlyphStateOff
+ _MRUMirroringGlyphStateOn
+ _MRUMirroringMinimumItems
+ _MRUMirroringVisibleItems
+ _OBJC_CLASS_$_CCUIMenuModuleItem
+ _OBJC_CLASS_$_CCUIMenuModuleViewController
+ _OBJC_CLASS_$_FBSDisplayMonitor
+ _OBJC_CLASS_$_MRUAssetsProvider
+ _OBJC_CLASS_$_MRUMirroringController
+ _OBJC_CLASS_$_MRUMirroringMenuModuleItem
+ _OBJC_CLASS_$_MRUStringsProvider
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_UIAlertAction
+ _OBJC_CLASS_$_UIAlertController
+ _OBJC_CLASS_$_UIDevice
+ _OBJC_CLASS_$_UIImage
+ _OBJC_CLASS_$_UIImageSymbolConfiguration
+ _OBJC_CLASS_$_UIView
+ _OBJC_METACLASS_$_CCUIMenuModuleItem
+ _OBJC_METACLASS_$_CCUIMenuModuleViewController
+ _OBJC_METACLASS_$_MRUMirroringMenuModuleItem
+ _OBJC_METACLASS_$_MRUMirroringViewController
+ __NSConcreteGlobalBlock
+ __NSConcreteStackBlock
+ __Unwind_Resume
+ ___CFConstantStringClassReference
+ ___objc_personality_v0
+ ___stack_chk_fail
+ ___stack_chk_guard
+ _objc_alloc
+ _objc_autoreleaseReturnValue
+ _objc_claimAutoreleasedReturnValue
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_enumerationMutation
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSendSuper2
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_release
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x9
+ _objc_retain
+ _objc_retain_x2
+ _objc_retain_x23
+ _objc_retain_x8
CStrings:
+ "\x01"
+ "\x12"
+ "@\"FBSDisplayMonitor\""
+ "@\"MRUMirroringController\""
+ "@\"NSString\""
+ "B"
+ "B16@?0@\"AVOutputDevice\"8"
+ "B8@?0"
+ "IsDiscoveredOverInfra"
+ "MRUMirroringControllerDelegate"
+ "MRUMirroringMenuModuleItem"
+ "MRUMirroringViewController"
+ "Mirroring"
+ "MirroringNonAnimated"
+ "T@\"FBSDisplayMonitor\",&,N,V_displayMonitor"
+ "T@\"MRUMirroringController\",&,N,V_controller"
+ "T@\"NSString\",&,N,V_symbolName"
+ "TB,N,V_showMoreExpanded"
+ "_canShowWhileLocked"
+ "_controller"
+ "_displayMonitor"
+ "_showMoreExpanded"
+ "_symbolName"
+ "_systemImageNamed:"
+ "actionWithTitle:style:handler:"
+ "addAction:"
+ "addObject:"
+ "airPlayErrorTitle"
+ "airPlayProperties"
+ "airplayErrorExternalDisplay"
+ "alertControllerWithTitle:message:preferredStyle:"
+ "arrayByAddingObjectsFromArray:"
+ "availableOutputDevices"
+ "boolValue"
+ "busyIdentifiers"
+ "buttonView"
+ "ccuiSupportsGroupRendering"
+ "configurationWithPointSize:weight:scale:"
+ "connectedIdentities"
+ "connectionType"
+ "containsObject:"
+ "controller"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "currentDevice"
+ "deviceID"
+ "dismissModule"
+ "displayMonitor"
+ "imageWithConfiguration:"
+ "initWithTitle:identifier:handler:"
+ "isConnectedToExternalDisplay"
+ "isExpanded"
+ "isExternal"
+ "leadingImageForMenuItem:"
+ "mirroringController:didChangeAudioOutputDevice:"
+ "mirroringController:didChangeAvailableAudioOutputDevices:"
+ "mirroringController:didChangeAvailableOutputDevices:"
+ "mirroringController:didChangeOutputDevice:"
+ "mirroringController:didReceiveAuthorizationRequest:"
+ "mirroringController:didUpdateBusyIdenifiers:"
+ "msv_filter:"
+ "name"
+ "objectForKeyedSubscript:"
+ "off"
+ "ok"
+ "on"
+ "packageDescriptionWithName:"
+ "performWithoutAnimation:"
+ "removeFooterButton"
+ "routingFooterShowMoreTitle"
+ "screenMirroring"
+ "selectOutputDevice:"
+ "selectedOutputDevice"
+ "setBusy:"
+ "setController:"
+ "setDelegate:"
+ "setDisplayMonitor:"
+ "setFooterButtonTitle:handler:"
+ "setGlyphPackageDescription:"
+ "setGlyphState:"
+ "setIndentation:"
+ "setMenuItems:"
+ "setMinimumMenuItems:"
+ "setSelected:"
+ "setShowMoreExpanded:"
+ "setSymbolName:"
+ "setTitle:"
+ "setUseTrailingCheckmarkLayout:"
+ "setVisibleMenuItems:"
+ "shouldBeginTransitionToExpandedContentModule"
+ "shouldExpandModuleOnTouch:"
+ "showMoreExpanded"
+ "showViewController:sender:"
+ "showmore"
+ "startDetailedDiscovery"
+ "startMirroringToOutputDevice:completion:"
+ "stopDetailedDiscovery"
+ "stopMirroring"
+ "stopMirroringDismissOnComplete:"
+ "stopMirroringWithCompletion:"
+ "symbolName"
+ "symbolNameForOutputDevice:"
+ "updateFooter"
+ "updateItems"
+ "updateState"
+ "v16@?0@\"UIAlertAction\"8"
+ "v16@?0q8"
+ "v20@0:8B16"
+ "v32@0:8@\"MRUMirroringController\"16@\"AVOutputDevice\"24"
+ "v32@0:8@\"MRUMirroringController\"16@\"MRUMirroringAuthorizationRequest\"24"
+ "v32@0:8@\"MRUMirroringController\"16@\"NSArray\"24"
+ "v32@0:8@\"MRUMirroringController\"16@\"NSSet\"24"
+ "v32@0:8@16@24"
+ "v8@?0"
+ "viewDidLoad"
+ "viewWillAppear:"
+ "viewWillDisappear:"
+ "willTransitionToExpandedContentMode:"

```
