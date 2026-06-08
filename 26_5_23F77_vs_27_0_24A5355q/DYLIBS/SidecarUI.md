## SidecarUI

> `/System/Library/PrivateFrameworks/SidecarUI.framework/SidecarUI`

```diff

-380.1.0.0.0
-  __TEXT.__text: 0xdc8
-  __TEXT.__auth_stubs: 0x1a0
-  __TEXT.__objc_methlist: 0x444
+400.34.0.0.0
+  __TEXT.__text: 0xdb0
+  __TEXT.__objc_methlist: 0x48c
   __TEXT.__const: 0x50
   __TEXT.__oslogstring: 0x94
-  __TEXT.__cstring: 0x2b
-  __TEXT.__unwind_info: 0xd0
-  __TEXT.__objc_classname: 0x9a
-  __TEXT.__objc_methname: 0x948
-  __TEXT.__objc_methtype: 0x20d
-  __TEXT.__objc_stubs: 0x460
-  __DATA_CONST.__got: 0x30
+  __TEXT.__cstring: 0x2e
+  __TEXT.__unwind_info: 0xe0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c0
+  __DATA_CONST.__objc_selrefs: 0x2d8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xd8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0x4c8
+  __AUTH_CONST.__objc_const: 0x4e0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x1e0

   - /System/Library/PrivateFrameworks/SidecarCore.framework/SidecarCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3FDA55B8-E660-3833-908C-4231924F9F24
-  Functions: 53
-  Symbols:   236
-  CStrings:  164
+  UUID: B8454C4A-8854-38DA-9FD7-DC24B00497E2
+  Functions: 56
+  Symbols:   245
+  CStrings:  9
 
Symbols:
+ -[SidecarServiceViewController sidecarServiceGoHome]
+ -[SidecarServiceViewController sidecarServiceOpenControlCenter]
+ -[SidecarServiceViewController sidecarServiceShowAppSwitcher]
+ ___block_literal_global.159
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$sidecarServiceGoHome
+ _objc_msgSend$sidecarServiceOpenControlCenter
+ _objc_msgSend$sidecarServiceShowAppSwitcher
+ _objc_release_x24
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
- ___block_literal_global.157
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_autoreleaseReturnValue
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"FBSSceneIdentityToken\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"SidecarRequest\""
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "Q16@0:8"
- "SidecarRequestDelegate"
- "SidecarServiceHostInterface"
- "SidecarServiceProviderDelegate"
- "SidecarServiceServiceInterface"
- "SidecarServiceViewController"
- "T#,R"
- "T@\"<SidecarServiceHostInterface>\",R"
- "T@\"FBSSceneIdentityToken\",C,N,V_sceneIdentityToken"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_sceneIdentifier"
- "T@\"NSString\",R,C"
- "T@\"SidecarRequest\",R"
- "TB,N,V_active"
- "TB,N,V_allowsDisplaySleep"
- "TB,N,V_backgrounded"
- "TB,N,V_waitForReconnect"
- "TB,N,V_wantsVolumeButtonEvents"
- "TB,R"
- "TQ,R"
- "Tq,N,V_backgroundStyle"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_UUID"
- "_active"
- "_allowsDisplaySleep"
- "_backgroundStyle"
- "_backgrounded"
- "_calledServiceReady"
- "_exportedInterface"
- "_isSecureForRemoteViewService"
- "_notifyServiceAndTerminate:"
- "_remoteViewControllerInterface"
- "_remoteViewControllerProxy"
- "_request"
- "_sceneIdentifier"
- "_sceneIdentityToken"
- "_supportedInterfaceOrientationsDidChange"
- "_terminationRequested"
- "_waitForReconnect"
- "_wantsVolumeButtonEvents"
- "active"
- "addObserver:forKeyPath:options:context:"
- "allowsDisplaySleep"
- "autorelease"
- "backgroundStyle"
- "backgrounded"
- "bundleIdentifier"
- "cancel"
- "class"
- "completeRequest:"
- "conformsToProtocol:"
- "copy"
- "debugDescription"
- "description"
- "extensionContext"
- "hash"
- "hostProxy"
- "initWithNibName:bundle:"
- "interfaceWithProtocol:"
- "isEqual:"
- "isEqualToString:"
- "isFinished"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "mainBundle"
- "observeValueForKeyPath:ofObject:change:context:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "q"
- "q16@0:8"
- "receivedItems:"
- "release"
- "removeObserver:forKeyPath:"
- "request"
- "requestCompleted"
- "requestDidFinish:"
- "requestDidStart:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "sceneIdentifier"
- "sceneIdentityToken"
- "self"
- "serviceReady"
- "session"
- "setActive:"
- "setAllowsDisplaySleep:"
- "setBackgroundStyle:"
- "setBackgrounded:"
- "setDelegate:"
- "setRequest:"
- "setSceneIdentifier:"
- "setSceneIdentityToken:"
- "setWaitForReconnect:"
- "setWantsVolumeButtonEvents:"
- "sidecarRequest:receivedItems:"
- "sidecarServiceActive"
- "sidecarServiceCancel"
- "sidecarServiceDisableDisplaySleep:"
- "sidecarServiceOrientationChanged"
- "sidecarServiceProviderHandleRequest:"
- "sidecarServiceProviderTerminate"
- "sidecarServiceSetActive:"
- "sidecarServiceSetBackgrounded:"
- "sidecarServiceSetSceneIdentifier:"
- "sidecarServiceSetSceneIdentityToken:"
- "sidecarServiceShouldPresentWithCompletion:"
- "sidecarServiceUpdateSupportedOrientations"
- "sidecarServiceViewControllerAnimate:completion:"
- "sidecarServiceViewControllerBackgroundStyle:"
- "sidecarServiceViewControllerWantsVolumeButtonEvents:"
- "sidecarServiceVolumeDownButtonPressed:"
- "sidecarServiceVolumeUpButtonPressed:"
- "superclass"
- "terminateWithSuccess"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"FBSSceneIdentityToken\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"SidecarRequest\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8q16"
- "v32@0:8@\"SidecarRequest\"16@\"NSArray\"24"
- "v32@0:8@16@24"
- "v32@0:8q16@?24"
- "v32@0:8q16@?<v@?>24"
- "v48@0:8@16@24@32^v40"
- "viewDidLoad"
- "waitForReconnect"
- "waitForServiceReady"
- "wantsVolumeButtonEvents"
- "zone"

```
