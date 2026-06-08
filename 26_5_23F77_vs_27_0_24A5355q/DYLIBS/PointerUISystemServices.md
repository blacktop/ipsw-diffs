## PointerUISystemServices

> `/System/Library/PrivateFrameworks/PointerUISystemServices.framework/PointerUISystemServices`

```diff

-165.0.0.0.0
-  __TEXT.__text: 0x1428
-  __TEXT.__auth_stubs: 0x230
+171.0.0.0.0
+  __TEXT.__text: 0x1258
   __TEXT.__objc_methlist: 0x3d8
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x154
+  __TEXT.__cstring: 0x159
   __TEXT.__oslogstring: 0x21a
-  __TEXT.__unwind_info: 0xc8
-  __TEXT.__objc_classname: 0xcf
-  __TEXT.__objc_methname: 0xafd
-  __TEXT.__objc_methtype: 0x58d
-  __TEXT.__objc_stubs: 0x680
-  __DATA_CONST.__got: 0x78
+  __TEXT.__unwind_info: 0xd0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x378
+  __DATA_CONST.__objc_selrefs: 0x380
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x120
+  __DATA_CONST.__got: 0x78
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0xc0
   __AUTH_CONST.__objc_const: 0x7c0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x240

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3ED70907-DCD4-3E85-9B35-A28C620890E3
-  Functions: 37
-  Symbols:   254
-  CStrings:  201
+  UUID: B7B0B001-D5C7-350F-A58E-399FCC3A0EC8
+  Functions: 35
+  Symbols:   255
+  CStrings:  27
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$process
+ _objc_release_x25
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x3
+ _objc_retain_x8
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x23
- _objc_retain_x27
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<PSPointerSystemClientControllerDelegate>\""
- "@\"FBSceneWorkspace\""
- "@\"NSSet\"32@0:8@\"FBScene\"16@\"NSSet\"24"
- "@\"NSString\"16@0:8"
- "@\"RBSProcessIdentity\""
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
- "FBSceneDelegate"
- "FBSceneObserver"
- "FBSceneWorkspaceDelegate"
- "FBSceneWorkspaceObserver"
- "NSObject"
- "PSPointerSceneExtension"
- "PSPointerSceneSettings"
- "PSPointerSceneSettingsExtension"
- "PSPointerSystemClientController"
- "Q16@0:8"
- "T#,R"
- "T@\"<PSPointerSystemClientControllerDelegate>\",W,N,V_delegate"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "T{CGAffineTransform=dddddd},N"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_delegate"
- "_invalidateSceneForIdentifierPrefix:displayConfiguration:"
- "_pointerUIDProcessIdentity"
- "_prepareSceneForIdentifierPrefix:displayConfiguration:"
- "_sceneIdentifierForIdentifierPrefix:displayConfiguration:"
- "_sceneWorkspace"
- "_setRootWindowTransform:sceneForIdentifierPrefix:displayConfiguration:"
- "activateWithTransitionContext:"
- "addExtension:"
- "allScenes"
- "arrayWithObjects:count:"
- "autorelease"
- "bounds"
- "class"
- "clientComponents"
- "clientSettingsExtensions"
- "configureParameters:"
- "conformsToProtocol:"
- "containsString:"
- "createScene:"
- "debugDescription"
- "delegate"
- "description"
- "enumerateObjectsUsingBlock:"
- "getValue:size:"
- "handle"
- "hardwareIdentifier"
- "hash"
- "hostComponents"
- "identifier"
- "identity"
- "identityForDaemonJobLabel:"
- "identityForProcessIdentity:"
- "init"
- "initWithIdentifier:"
- "invalidate"
- "invalidateScenesForPointerForDisplayConfiguration:"
- "isActive"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "matchesProperty:"
- "objCType"
- "parametersForSpecification:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pointerClientController:sceneDidActivate:"
- "pointerClientController:sceneWillDeactivate:"
- "prepareScenesForPointerForDisplayConfiguration:"
- "protocol"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "rootWindowTransform"
- "rootWindowTransform:"
- "scene:clientDidConnect:"
- "scene:didApplyUpdateWithContext:"
- "scene:didCompleteUpdateWithContext:error:"
- "scene:didPrepareUpdateWithContext:"
- "scene:didReceiveActions:"
- "scene:didUpdateClientSettings:"
- "scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:"
- "scene:didUpdateSettings:"
- "scene:handleActions:"
- "scene:willUpdateSettings:"
- "scene:willUpdateSettings:withTransitionContext:"
- "sceneContentStateDidChange:"
- "sceneDidActivate:"
- "sceneDidDeactivate:withContext:"
- "sceneDidDeactivate:withError:"
- "sceneDidInvalidate:"
- "sceneDidInvalidate:withContext:"
- "sceneWillActivate:"
- "sceneWillDeactivate:withContext:"
- "sceneWillDeactivate:withError:"
- "sceneWithIdentifier:"
- "self"
- "setClientIdentity:"
- "setClientSettings:"
- "setDelegate:"
- "setDisplayConfiguration:"
- "setForeground:"
- "setFrame:"
- "setIdentifier:"
- "setInterfaceOrientation:"
- "setLevel:"
- "setPreferredInterfaceOrientation:"
- "setPreferredLevel:"
- "setRootWindowTransform:"
- "setRootWindowTransform:forDisplayConfiguration:"
- "setSettings:"
- "setSpecification:"
- "setValue:forProperty:"
- "settings"
- "settingsExtensions"
- "specification"
- "stringWithFormat:"
- "superclass"
- "transitionContextExtensions"
- "updateSettingsWithBlock:"
- "v16@0:8"
- "v24@0:8@\"FBScene\"16"
- "v24@0:8@16"
- "v32@0:8@\"FBScene\"16@\"FBSSceneTransitionContext\"24"
- "v32@0:8@\"FBScene\"16@\"FBSSceneUpdate\"24"
- "v32@0:8@\"FBScene\"16@\"FBSceneClientHandle\"24"
- "v32@0:8@\"FBScene\"16@\"FBSceneUpdateContext\"24"
- "v32@0:8@\"FBScene\"16@\"NSError\"24"
- "v32@0:8@\"FBScene\"16@\"NSSet\"24"
- "v32@0:8@\"FBSceneWorkspace\"16@\"FBScene\"24"
- "v32@0:8@\"FBSceneWorkspace\"16@\"FBSceneClientHandshake\"24"
- "v32@0:8@\"FBSceneWorkspace\"16@\"NSSet\"24"
- "v32@0:8@16@24"
- "v40@0:8@\"FBScene\"16@\"FBSMutableSceneSettings\"24@\"FBSSceneTransitionContext\"32"
- "v40@0:8@\"FBScene\"16@\"FBSceneUpdateContext\"24@\"NSError\"32"
- "v40@0:8@16@24@32"
- "v48@0:8@\"FBScene\"16@\"FBSSceneClientSettingsDiff\"24@\"FBSSceneClientSettings\"32@\"FBSSceneTransitionContext\"40"
- "v48@0:8@\"FBSceneWorkspace\"16@\"FBSWorkspaceSceneRequestOptions\"24@\"<FBSceneClientProcess>\"32@?<v@?@\"FBScene\"@\"NSError\">40"
- "v48@0:8@\"FBSceneWorkspace\"16@\"FBScene\"24@\"FBSSceneTransitionContext\"32@\"<FBSceneClientProcess>\"40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32@?40"
- "v64@0:8{CGAffineTransform=dddddd}16"
- "v72@0:8{CGAffineTransform=dddddd}16@64"
- "v80@0:8{CGAffineTransform=dddddd}16@64@72"
- "valueForProperty:expectedClass:"
- "valueForUndefinedSetting:"
- "valueWithBytes:objCType:"
- "workspace:clientDidConnectWithHandshake:"
- "workspace:didAddScene:"
- "workspace:didReceiveActions:"
- "workspace:didReceiveScene:withContext:fromProcess:"
- "workspace:didReceiveSceneRequestWithOptions:fromProcess:completion:"
- "workspace:willRemoveScene:"
- "zone"
- "{CGAffineTransform=dddddd}16@0:8"

```
