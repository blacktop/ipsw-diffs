## CarPlayTemplateUIHost

> `/System/Library/CoreServices/CarPlayTemplateUIHost.app/CarPlayTemplateUIHost`

```diff

-385.24.1.0.0
-  __TEXT.__text: 0xd0d4
-  __TEXT.__auth_stubs: 0x3c0
-  __TEXT.__objc_stubs: 0x2a00
-  __TEXT.__objc_methlist: 0x13ac
+512.2.4.0.0
+  __TEXT.__text: 0xd308
+  __TEXT.__auth_stubs: 0x3e0
+  __TEXT.__objc_stubs: 0x2b20
+  __TEXT.__objc_methlist: 0x1354
   __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0x310
-  __TEXT.__objc_methname: 0x3c92
-  __TEXT.__oslogstring: 0xc78
-  __TEXT.__cstring: 0x58d
-  __TEXT.__objc_classname: 0x31d
-  __TEXT.__objc_methtype: 0xf00
-  __TEXT.__unwind_info: 0x318
-  __DATA_CONST.__auth_got: 0x1f0
-  __DATA_CONST.__got: 0x1d8
+  __TEXT.__gcc_except_tab: 0x340
+  __TEXT.__objc_methname: 0x3c74
+  __TEXT.__oslogstring: 0xc74
+  __TEXT.__cstring: 0x5f2
+  __TEXT.__objc_classname: 0x339
+  __TEXT.__objc_methtype: 0xc9a
+  __TEXT.__unwind_info: 0x328
+  __DATA_CONST.__auth_got: 0x200
+  __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__const: 0x3d0
-  __DATA_CONST.__cfstring: 0x3e0
+  __DATA_CONST.__cfstring: 0x420
   __DATA_CONST.__objc_classlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x78
+  __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x50
-  __DATA.__objc_const: 0x39a8
-  __DATA.__objc_selrefs: 0xec8
+  __DATA.__objc_const: 0x3a48
+  __DATA.__objc_selrefs: 0xef0
   __DATA.__objc_ivar: 0x144
   __DATA.__objc_data: 0x370
-  __DATA.__data: 0x5a0
-  __DATA.__bss: 0xe4
+  __DATA.__data: 0x600
+  __DATA.__bss: 0x104
   - /System/Library/Frameworks/CarPlay.framework/CarPlay
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1CA580E4-B7E1-3883-8823-794345E96F41
-  Functions: 360
-  Symbols:   133
-  CStrings:  936
+  UUID: C41ED73B-FB15-38AB-BF6D-6DB64D16AF3E
+  Functions: 365
+  Symbols:   136
+  CStrings:  940
 
Symbols:
+ _UINavigationControllerHideShowBarDuration
+ _objc_retainBlock
+ _objc_retain_x26
CStrings:
+ "@\"NSSet\""
+ "@\"UISceneWindowingControlStyle\"24@0:8@\"UIWindowScene\"16"
+ "AppLink"
+ "CPMapTemplateWillHideNotification"
+ "CPMapTemplateWillShowNotification"
+ "CPSTemplateInstanceDelegate"
+ "DisplayScale"
+ "Focus"
+ "Icons"
+ "Installing presentation view for scene %@"
+ "Not installing presentation view for scene %@"
+ "T@\"NSSet\",&,N,V_pendingOpenURLContexts"
+ "URLContexts"
+ "_installScenePresentationViewIfNeeded"
+ "_pendingOpenURLContexts"
+ "_removeScenePresentationView"
+ "animateWithDuration:delay:options:animations:completion:"
+ "applicationWindowSceneConnected:options:"
+ "boolValue"
+ "clientApplicationSceneIsConnected"
+ "dashboardGuidanceWindowSceneConnected:options:"
+ "dashboardMapWindowSceneConnected:options:"
+ "didAddScene: %@"
+ "didConnectScene:options:"
+ "initWithWindowScene:templateInstance:options:"
+ "instrumentClusterWindowSceneConnected:options:"
+ "invalidate:"
+ "mapTemplateWillHide:"
+ "mapTemplateWillShow:"
+ "pendingOpenURLContexts"
+ "preferredWindowingControlStyleForScene:"
+ "removeObserver:"
+ "requiresApplicationScenePresenter"
+ "scene: (%@) didUpdateSettings: (%@)"
+ "sceneDidInvalidate: %@ withContext: %@"
+ "sceneWillDeactivate: %@ withContext: %@. Invalidating associated view controller"
+ "setPendingOpenURLContexts:"
+ "templateInstanceClientDidConnectApplicationScene:"
+ "templateInstanceClientDidDisconnectApplicationScene:"
+ "v32@0:8@\"UIWindowScene\"16@\"UIWindowSceneGeometry\"24"
+ "windowScene:didUpdateEffectiveGeometry:"
+ "\xf1"
- "@\"FBSSceneTransitionContext\"32@0:8@\"FBSceneManager\"16@\"FBScene\"24"
- "@\"_UICanvasDefinition\"40@0:8@\"UIApplication\"16@\"_UICanvasDefinition\"24@\"NSDictionary\"32"
- "T@\"UIWindowScene\",&,N,V_windowScene"
- "_application:didDiscardCanvasDefinitions:"
- "_application:didReceiveViewServiceRequestForViewControllerClassName:"
- "_application:willConnectCanvas:"
- "_application:willCreateCanvasWithDefinition:withOptions:"
- "destroyScene:withTransitionContext:"
- "didConnectScene:"
- "didCreateScene: %@"
- "didDestroyScene: %@"
- "didReceiveActions: %@"
- "initWithWindowScene:templateInstance:"
- "instrumentClusterWindowSceneConnected:"
- "sceneManager:createDefaultTransitionContextForScene:"
- "sceneManager:didCommitUpdateForScene:transactionID:success:"
- "sceneManager:didCreateScene:"
- "sceneManager:didCreateScene:withClient:"
- "sceneManager:scene:didReceiveActions:"
- "sceneManager:scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:"
- "sceneManager:updateForScene:appliedWithContext:"
- "sceneManager:updateForScene:completedWithContext:error:"
- "sceneManager:updateForScene:preparedWithContext:"
- "sceneManager:willDestroyScene:"
- "updateForScene: (%@) appliedWithContext: (%@)"
- "updateForScene: (%@) completedWithContext: (%@)"
- "updateForScene: (%@) preparedWithContext: (%@)"
- "v32@0:8@\"UIApplication\"16@\"NSSet\"24"
- "v32@0:8@\"UIApplication\"16@\"NSString\"24"
- "v32@0:8@\"UIApplication\"16@\"UICanvas\"24"
- "v40@0:8@\"FBSceneManager\"16@\"FBScene\"24@\"<FBSceneClient>\"32"
- "v40@0:8@\"FBSceneManager\"16@\"FBScene\"24@\"FBSceneUpdateContext\"32"
- "v40@0:8@\"FBSceneManager\"16@\"FBScene\"24@\"NSSet\"32"
- "v44@0:8@\"FBSceneManager\"16@\"FBScene\"24Q32B40"
- "v44@0:8@16@24Q32B40"
- "v48@0:8@\"FBSceneManager\"16@\"FBScene\"24@\"FBSceneUpdateContext\"32@\"NSError\"40"
- "v56@0:8@\"FBSceneManager\"16@\"FBScene\"24@\"FBSSceneClientSettingsDiff\"32@\"FBSSceneClientSettings\"40@\"FBSSceneTransitionContext\"48"
- "v56@0:8@16@24@32@40@48"
- "willDestroyScene: %@. Invalidating associated view controller"
- "\xe1"

```
