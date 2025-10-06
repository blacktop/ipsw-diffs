## AuthKitUIService

> `/Applications/AuthKitUIService.app/AuthKitUIService`

```diff

-458.1.1.7.0
-  __TEXT.__text: 0x6638
-  __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_stubs: 0x17c0
-  __TEXT.__objc_methlist: 0x690
+464.5.0.0.0
+  __TEXT.__text: 0x4b10
+  __TEXT.__auth_stubs: 0x3e0
+  __TEXT.__objc_stubs: 0x1360
+  __TEXT.__objc_methlist: 0x438
   __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0x128
-  __TEXT.__objc_methname: 0x2a75
-  __TEXT.__oslogstring: 0x7a2
-  __TEXT.__cstring: 0x384
-  __TEXT.__objc_classname: 0x229
-  __TEXT.__objc_methtype: 0xfdb
-  __TEXT.__unwind_info: 0x29c
-  __DATA_CONST.__auth_got: 0x218
-  __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0x300
-  __DATA_CONST.__cfstring: 0x140
-  __DATA_CONST.__objc_classlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x50
+  __TEXT.__gcc_except_tab: 0x10c
+  __TEXT.__objc_methname: 0x216b
+  __TEXT.__oslogstring: 0x560
+  __TEXT.__cstring: 0x32f
+  __TEXT.__objc_classname: 0x151
+  __TEXT.__objc_methtype: 0xd07
+  __TEXT.__unwind_info: 0x234
+  __DATA_CONST.__auth_got: 0x200
+  __DATA_CONST.__got: 0x38
+  __DATA_CONST.__const: 0x298
+  __DATA_CONST.__cfstring: 0x100
+  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x2ac0
-  __DATA.__objc_selrefs: 0x758
-  __DATA.__objc_classrefs: 0x130
-  __DATA.__objc_superrefs: 0x30
-  __DATA.__objc_ivar: 0x64
-  __DATA.__objc_data: 0x2d0
-  __DATA.__data: 0x3c0
+  __DATA.__objc_const: 0x1dc8
+  __DATA.__objc_selrefs: 0x5d0
+  __DATA.__objc_classrefs: 0xe8
+  __DATA.__objc_superrefs: 0x28
+  __DATA.__objc_ivar: 0x38
+  __DATA.__objc_data: 0x1e0
+  __DATA.__data: 0x1e0
   __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3EA052DB-609E-3C79-9B7E-E45E32B24F12
-  Functions: 223
-  Symbols:   119
-  CStrings:  589
+  UUID: D7E41316-7991-34F2-8392-27AEC99992FA
+  Functions: 146
+  Symbols:   109
+  CStrings:  460
 
Symbols:
+ __AKLogHme
- _AKPrivateEmailClientAppBundleIdKey
- _OBJC_CLASS_$_AKLoginPresenterHostInterface
- _OBJC_CLASS_$_NSObject
- _OBJC_CLASS_$_UIApplication
- _OBJC_CLASS_$_UIWindow
- _OBJC_CLASS_$_UIWindowScene
- __NSConcreteGlobalBlock
- _exit
- _objc_retain_x23
- _objc_retain_x5
- _objc_storeWeak
CStrings:
+ "AKRemoteBaseViewController"
+ "Calling host proxy (%@) with private email response"
+ "Sending private email failure back to daemon with error: %@"
+ "Sending successful private email selection back to daemon: %@"
+ "setClipsToBounds:"
- "\x02"
- "\x02\x12"
- "!"
- "@\"<AKLoginPresenterHostInterfaceProtocol>\""
- "@\"<AKUIServiceFlowManagerDelegate>\""
- "@\"AKRemoteViewController\""
- "@\"AKUIServiceFlowManager\""
- "@\"AKUIServiceRootViewController\""
- "@\"NSDictionary\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSSet\"48@0:8@\"NSSet\"16@\"FBSScene\"24@\"UIScene\"32@\"FBSSceneTransitionContext\"40"
- "@\"NSUserActivity\"24@0:8@\"UIScene\"16"
- "@\"UIWindow\""
- "@\"_UISceneConnectionOptionsContext\"48@0:8@\"NSSet\"16@\"FBSScene\"24@\"UISceneSession\"32@\"FBSSceneTransitionContext\"40"
- "@48@0:8@16@24@32@40"
- "AKAuthenticationRemoteViewController"
- "AKUIServiceFlowManager"
- "AKUIServiceFlowManagerDelegate"
- "AKUIServiceRootViewController"
- "Authentication context after unarcheving: %@"
- "Authentication context is missing"
- "Authorization context error: %@"
- "Error unarchiving authentication context: %@"
- "Exiting hidden app process."
- "Failed to connect to the session."
- "Final Interactive Context :%@"
- "No remote context found. Failed to launch the flow."
- "Present Basic Login UI with authentication context: %@"
- "Presenting Login Remote View"
- "Presenting Private Email Remote View"
- "Remote context found. Proceeding to launch the authorization flow."
- "Scene will connect to session"
- "SceneDelegate"
- "Sending authentication result to hostproxy: %@"
- "Sending {%@,%@}"
- "T@\"<AKLoginPresenterHostInterfaceProtocol>\",&,N,V_hostProxy"
- "T@\"<AKUIServiceFlowManagerDelegate>\",W,N,V_sceneFlowDelegate"
- "T@\"AKAppleIDAuthenticationContext\",&,N,V_originalContext"
- "T@\"AKAppleIDAuthenticationInAppContext\",&,N,V_interactiveInAppContext"
- "T@\"AKRemoteViewController\",&,N,V_remoteViewController"
- "T@\"AKUIServiceFlowManager\",&,N,V_flowManager"
- "T@\"NSDictionary\",&,N,V_remoteContextInfo"
- "T@\"NSObject<OS_xpc_object>\",&,N,V_xpcEndpoint"
- "T@\"UIViewController\",&,N,V_presentingViewController"
- "T@\"UIWindow\",&,N,V_window"
- "UISceneDelegate"
- "Unknown context received, cancelling..."
- "_UISceneBSActionHandler"
- "_UISceneBSActionResponding"
- "_UISceneConnectionOptionProviding"
- "_callCompletionWithAuthResult:password:additionalData:error:"
- "_flowManager"
- "_inAppContextFromContext:"
- "_interactiveInAppContext"
- "_launchOptionsFromActions:forFBSScene:uiSceneSession:transitionContext:"
- "_originalContext"
- "_presentAuthorizationRemoteViewControllerWithContext:"
- "_presentLoginRemoteViewControllerWithContext:"
- "_presentLoginUI"
- "_presentPrivateEmailRemoteViewControllerWithContext:altDSID:"
- "_presentingViewController"
- "_registerSceneActionsHandlerArray:forKey:"
- "_remoteContextInfo"
- "_remoteViewController"
- "_respondToActions:forFBSScene:inUIScene:fromTransitionContext:"
- "_rootViewController"
- "_sceneFlowDelegate"
- "_window"
- "_xpcEndpoint"
- "authenticationRequestFinishedWithResults:password:additionalData:error:"
- "copy"
- "flowManager"
- "handleCancellation"
- "info"
- "initWithAuthenticationContext:"
- "initWithKey:altDSID:"
- "initWithWindowScene:"
- "interactiveInAppContext"
- "launch_params"
- "makeKeyAndVisible"
- "mutableCopy"
- "notifyFlowCompletionToExitScene"
- "notifyFlowCompletionWithCancellation"
- "objectForSetting:"
- "oopUIMode"
- "openSessions"
- "originalContext"
- "presentAuthorizeFlowWithRootViewController:"
- "presentBasicLoginUIWithCompletion:"
- "remoteContextInfo"
- "remoteViewController"
- "removeObject:"
- "requestSceneSessionDestruction:options:errorHandler:"
- "scene:continueUserActivity:"
- "scene:didFailToContinueUserActivityWithType:error:"
- "scene:didUpdateUserActivity:"
- "scene:openURLContexts:"
- "scene:restoreInteractionStateWithUserActivity:"
- "scene:willConnectToSession:options:"
- "scene:willContinueUserActivityWithType:"
- "sceneDidBecomeActive"
- "sceneDidBecomeActive:"
- "sceneDidDisconnect"
- "sceneDidDisconnect:"
- "sceneDidEnterBackground"
- "sceneDidEnterBackground:"
- "sceneFlowDelegate"
- "sceneWillEnterForeground"
- "sceneWillEnterForeground:"
- "sceneWillResignActive"
- "sceneWillResignActive:"
- "setContentsPosition:"
- "setFlowManager:"
- "setInteractiveInAppContext:"
- "setOriginalContext:"
- "setRemoteContextInfo:"
- "setRemoteViewController:"
- "setRootViewController:"
- "setSceneFlowDelegate:"
- "setXpcEndpoint:"
- "sharedApplication"
- "stateRestorationActivityForScene:"
- "unsignedIntValue"
- "v24@0:8@\"UIScene\"16"
- "v32@0:8@\"UIScene\"16@\"NSSet\"24"
- "v32@0:8@\"UIScene\"16@\"NSString\"24"
- "v32@0:8@\"UIScene\"16@\"NSUserActivity\"24"
- "v40@0:8@\"UIScene\"16@\"NSString\"24@\"NSError\"32"
- "v40@0:8@\"UIScene\"16@\"UISceneSession\"24@\"UISceneConnectionOptions\"32"
- "v40@?0@\"NSString\"8@\"NSString\"16@\"NSDictionary\"24@\"NSError\"32"
- "v48@0:8@16@24@32@40"
- "xpcEndpoint missing"

```
