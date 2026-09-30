## PDUIApp

> `/Applications/PDUIApp.app/PDUIApp`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`

```diff

-49.0.0.0.0
-  __TEXT.__text: 0x7d8
-  __TEXT.__auth_stubs: 0x210
-  __TEXT.__objc_stubs: 0x440
-  __TEXT.__objc_methlist: 0x46c
+49.0.1.0.0
+  __TEXT.__text: 0xa54
+  __TEXT.__auth_stubs: 0x1f0
+  __TEXT.__objc_stubs: 0x560
+  __TEXT.__objc_methlist: 0x5c0
   __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x1a
-  __TEXT.__objc_classname: 0x61
-  __TEXT.__objc_methname: 0xf5d
-  __TEXT.__objc_methtype: 0x999
-  __TEXT.__unwind_info: 0x90
+  __TEXT.__cstring: 0x34
+  __TEXT.__objc_classname: 0xa1
+  __TEXT.__objc_methname: 0x12db
+  __TEXT.__objc_methtype: 0xc36
+  __TEXT.__unwind_info: 0x98
   __DATA_CONST.__const: 0x88
-  __DATA_CONST.__objc_classlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x18
+  __DATA_CONST.__cfstring: 0x20
+  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x110
-  __DATA_CONST.__got: 0x48
-  __DATA.__objc_const: 0x820
-  __DATA.__objc_selrefs: 0x3b0
-  __DATA.__objc_ivar: 0xc
-  __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x120
+  __DATA_CONST.__auth_got: 0x100
+  __DATA_CONST.__got: 0x60
+  __DATA.__objc_const: 0xd78
+  __DATA.__objc_selrefs: 0x490
+  __DATA.__objc_ivar: 0x14
+  __DATA.__objc_data: 0xf0
+  __DATA.__data: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/AppRestrictionsCore.framework/AppRestrictionsCore
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices

   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 16
-  Symbols:   52
-  CStrings:  209
+  Functions: 21
+  Symbols:   55
+  CStrings:  261
 
Symbols:
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_UISceneConfiguration
+ _OBJC_CLASS_$_UIWindow
+ _OBJC_CLASS_$_UIWindowScene
+ ___CFConstantStringClassReference
+ _objc_autoreleaseReturnValue
- _DMGetUserDataDisposition
- _PDCGlobalDeviceSettings
- _PDCPerformOneTimeImplicitConsentGrant
CStrings:
+ "@\"ALRPreflightRequest\""
+ "@\"NSUserActivity\"24@0:8@\"UIScene\"16"
+ "@\"UISceneWindowingControlStyle\"24@0:8@\"UIWindowScene\"16"
+ "@\"UIWindow\""
+ "@24@0:8@16"
+ "PDUPreflightConfiguration"
+ "PDUPreflightSceneDelegate"
+ "Q24@0:8@\"UIWindowScene\"16"
+ "Q24@0:8@16"
+ "UISceneDelegate"
+ "UIWindowSceneDelegate"
+ "_preflightRequest"
+ "_window"
+ "alr_preflightRequest"
+ "application"
+ "configurationWithName:sessionRole:"
+ "confirm"
+ "initWithWindowScene:"
+ "makeKeyAndVisible"
+ "preferredWindowingControlStyleForScene:"
+ "reject:"
+ "role"
+ "scene:continueUserActivity:"
+ "scene:didFailToContinueUserActivityWithType:error:"
+ "scene:didUpdateUserActivity:"
+ "scene:openURLContexts:"
+ "scene:restoreInteractionStateWithUserActivity:"
+ "scene:willConnectToSession:options:"
+ "scene:willContinueUserActivityWithType:"
+ "sceneDidBecomeActive:"
+ "sceneDidDisconnect:"
+ "sceneDidEnterBackground:"
+ "sceneWillEnterForeground:"
+ "sceneWillResignActive:"
+ "setRootViewController:"
+ "stateRestorationActivityForScene:"
+ "supportedInterfaceOrientationsForWindowScene:"
+ "v24@0:8@\"UIScene\"16"
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
