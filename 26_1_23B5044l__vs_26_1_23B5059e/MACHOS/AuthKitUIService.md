## AuthKitUIService

> `/Applications/AuthKitUIService.app/AuthKitUIService`

```diff

-525.125.2.1.0
-  __TEXT.__text: 0x7ce8
-  __TEXT.__auth_stubs: 0x290
-  __TEXT.__objc_stubs: 0x13c0
-  __TEXT.__objc_methlist: 0x8cc
+525.126.1.1.0
+  __TEXT.__text: 0x8db0
+  __TEXT.__auth_stubs: 0x2f0
+  __TEXT.__objc_stubs: 0x1580
+  __TEXT.__objc_methlist: 0xa9c
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x19c
-  __TEXT.__cstring: 0x472
-  __TEXT.__objc_methname: 0x218b
-  __TEXT.__oslogstring: 0x560
-  __TEXT.__objc_classname: 0x151
-  __TEXT.__objc_methtype: 0xd07
+  __TEXT.__cstring: 0x522
+  __TEXT.__objc_methname: 0x2617
+  __TEXT.__oslogstring: 0x689
+  __TEXT.__objc_classname: 0x187
+  __TEXT.__objc_methtype: 0xf96
   __TEXT.__dlopen_cstrs: 0x34
-  __TEXT.__unwind_info: 0x1d8
-  __DATA_CONST.__auth_got: 0x158
-  __DATA_CONST.__got: 0x130
-  __DATA_CONST.__const: 0x3e8
-  __DATA_CONST.__cfstring: 0x220
-  __DATA_CONST.__objc_classlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x28
+  __TEXT.__unwind_info: 0x200
+  __DATA_CONST.__auth_got: 0x188
+  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__const: 0x498
+  __DATA_CONST.__cfstring: 0x240
+  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA.__objc_const: 0x1510
-  __DATA.__objc_selrefs: 0x850
-  __DATA.__objc_ivar: 0x38
-  __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x1e0
-  __DATA.__bss: 0x28
+  __DATA.__objc_const: 0x1a48
+  __DATA.__objc_selrefs: 0x950
+  __DATA.__objc_ivar: 0x44
+  __DATA.__objc_data: 0x230
+  __DATA.__data: 0x2a0
+  __DATA.__bss: 0x38
+  - /System/Library/Frameworks/Accessibility.framework/Accessibility
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI
+  - /System/Library/PrivateFrameworks/ClarityFoundation.framework/ClarityFoundation
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6F244BC8-ED73-353E-A5BF-40EC421E1E5D
-  Functions: 127
-  Symbols:   91
-  CStrings:  483
+  UUID: F3253B0F-7747-3AD8-AD85-423991F363CA
+  Functions: 149
+  Symbols:   103
+  CStrings:  552
 
Symbols:
+ _AXAssistiveAccessEnabled
+ _CFNotificationCenterAddObserver
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _CFNotificationCenterRemoveObserver
+ _CLFApplicationDidChangeNotification
+ _OBJC_CLASS_$_AKRemoteViewSessionController
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_UIWindow
+ _OBJC_CLASS_$_UIWindowScene
+ __NSConcreteGlobalBlock
+ _dispatch_once
+ _objc_setProperty_nonatomic_copy
CStrings:
+ "@\"AKAuthorizationRemoteViewController\"32@?0@\"AKAuthorizationPresentationContext\"8@\"<AKAuthorizationPresenterHostProtocol>\"16@?<v@?@\"AKAuthorization\"@\"NSError\">24"
+ "@\"AKRemoteViewSessionController\""
+ "@\"NSUserActivity\"24@0:8@\"UIScene\"16"
+ "@\"UISceneWindowingControlStyle\"24@0:8@\"UIWindowScene\"16"
+ "@\"UIWindow\""
+ "@?"
+ "@?16@0:8"
+ "Failed to connect scene (%@) to the session: %@"
+ "Scene (%@) will connect to session (%@) with options (%@)"
+ "SceneDelegate"
+ "T@\"UIWindow\",&,N,V_window"
+ "T@?,C,N,V_completionHandler"
+ "UISceneDelegate"
+ "UIWindowSceneDelegate"
+ "[visionOS] Calling XPC reply block: %@"
+ "_completionHandler"
+ "_registerBSActionResponderArray:forKey:"
+ "_shouldRegisterForClarityBoardApplicationChange"
+ "_shouldUseFrontBoardServices"
+ "_viewSessionController"
+ "_window"
+ "completionHandler"
+ "handleCancellation"
+ "initWithHost:presentationContext:"
+ "initWithRootViewController:sceneSession:"
+ "initWithWindowScene:"
+ "launch_params"
+ "makeKeyAndVisible"
+ "preferredWindowingControlStyleForScene:"
+ "scene:continueUserActivity:"
+ "scene:didFailToContinueUserActivityWithType:error:"
+ "scene:didUpdateUserActivity:"
+ "scene:openURLContexts:"
+ "scene:restoreInteractionStateWithUserActivity:"
+ "scene:willConnectToSession:options:"
+ "scene:willContinueUserActivityWithType:"
+ "sceneDidBecomeActive"
+ "sceneDidBecomeActive:"
+ "sceneDidDisconnect invalidating view session controller: %@"
+ "sceneDidDisconnect:"
+ "sceneDidEnterBackground"
+ "sceneDidEnterBackground:"
+ "sceneWillEnterForeground"
+ "sceneWillEnterForeground:"
+ "sceneWillResignActive"
+ "sceneWillResignActive:"
+ "setCompletionHandler:"
+ "setNewAuthorizationViewController:"
+ "setPreferredContentSize:"
+ "setRootViewController:"
+ "setWindowBlock:"
+ "stateRestorationActivityForScene:"
+ "v24@0:8@\"UIScene\"16"
+ "v24@0:8@?16"
+ "v32@0:8@\"UIScene\"16@\"NSSet\"24"
+ "v32@0:8@\"UIScene\"16@\"NSString\"24"
+ "v32@0:8@\"UIScene\"16@\"NSUserActivity\"24"
+ "v32@0:8@\"UIWindowScene\"16@\"CKShareMetadata\"24"
+ "v32@0:8@\"UIWindowScene\"16@\"UIWindowSceneGeometry\"24"
+ "v40@0:8@\"UIScene\"16@\"NSString\"24@\"NSError\"32"
+ "v40@0:8@\"UIScene\"16@\"UISceneSession\"24@\"UISceneConnectionOptions\"32"
+ "v40@0:8@\"UIWindowScene\"16@\"UIApplicationShortcutItem\"24@?<v@?B>32"
+ "v48@0:8@\"UIWindowScene\"16@\"<UICoordinateSpace>\"24q32@\"UITraitCollection\"40"
+ "v48@0:8@16@24q32@40"
+ "windowScene:didUpdateCoordinateSpace:interfaceOrientation:traitCollection:"
+ "windowScene:didUpdateEffectiveGeometry:"
+ "windowScene:performActionForShortcutItem:completionHandler:"
+ "windowScene:userDidAcceptCloudKitShareWithMetadata:"

```
