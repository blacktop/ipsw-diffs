## iCloud

> `/Applications/iCloud.app/iCloud`

```diff

-2360.120.2.0.0
-  __TEXT.__text: 0x17178
-  __TEXT.__auth_stubs: 0x560
-  __TEXT.__objc_stubs: 0x3140
-  __TEXT.__objc_methlist: 0xf20
+2710.108.20.0.0
+  __TEXT.__text: 0x16568
+  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__objc_stubs: 0x3220
+  __TEXT.__objc_methlist: 0x1098
   __TEXT.__const: 0xd8
-  __TEXT.__gcc_except_tab: 0x654
-  __TEXT.__cstring: 0x294d
-  __TEXT.__oslogstring: 0x1bf0
-  __TEXT.__objc_classname: 0xc9
-  __TEXT.__objc_methname: 0x40da
-  __TEXT.__objc_methtype: 0xd88
+  __TEXT.__gcc_except_tab: 0x53c
+  __TEXT.__cstring: 0x2a0c
+  __TEXT.__objc_methname: 0x44fa
+  __TEXT.__oslogstring: 0x1c7c
+  __TEXT.__objc_classname: 0x122
+  __TEXT.__objc_methtype: 0x1057
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x458
-  __DATA_CONST.__auth_got: 0x2c0
-  __DATA_CONST.__got: 0x3a8
-  __DATA_CONST.__const: 0x728
-  __DATA_CONST.__cfstring: 0x1f60
-  __DATA_CONST.__objc_classlist: 0x30
+  __TEXT.__unwind_info: 0x420
+  __DATA_CONST.__const: 0x720
+  __DATA_CONST.__cfstring: 0x2020
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0xd0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xff0
-  __DATA.__objc_selrefs: 0xf48
-  __DATA.__objc_ivar: 0xb4
-  __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x180
-  __DATA.__bss: 0x78
+  __DATA_CONST.__auth_got: 0x2e8
+  __DATA_CONST.__got: 0x3d8
+  __DATA.__objc_const: 0x12f8
+  __DATA.__objc_selrefs: 0x1018
+  __DATA.__objc_ivar: 0xbc
+  __DATA.__objc_data: 0x280
+  __DATA.__data: 0x2a0
+  __DATA.__bss: 0x88
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
+  - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 484793A1-37B7-3327-8BCE-731F1B25C491
-  Functions: 288
-  Symbols:   216
-  CStrings:  1375
+  UUID: BD4446F0-6C4D-308D-A05A-AF9EB885AE59
+  Functions: 294
+  Symbols:   227
+  CStrings:  1441
 
Symbols:
+ _CKFreeformFolderShareType
+ _OBJC_CLASS_$_UISceneConfiguration
+ _OBJC_CLASS_$_UIWindowScene
+ _kCKFreeformFolderShareURLSlug
+ _kCKPhotosSharedCollectionsShareHostURLSlug
+ _kCKPhotosSharedCollectionsSharedAlbumURLSlug
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x9
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "@\"<CKAppStoreDataProvider>\""
+ "@\"NSDictionary\"32@0:8@\"NSURL\"16^@24"
+ "@\"NSUserActivity\"24@0:8@\"UIScene\"16"
+ "@\"UISceneWindowingControlStyle\"24@0:8@\"UIWindowScene\"16"
+ "@\"UIScreen\""
+ "CKAppStoreDataProvider"
+ "CKExtractSubdomain"
+ "CKLiveAppStoreDataProvider"
+ "CLOUDKIT_VETTING_ACCESS_REQUEST_SENT_MESSAGE_SHARED_ALBUM"
+ "Default Configuration"
+ "Delegate object is not an instance of AppDelegate"
+ "Failed to construct alertTitle: %@ and/or alertBody: %@ for generic share"
+ "Fallback flow: User either not logged into iCloud or need to update Apple Account settings, error: %{public}@"
+ "Fallback flow: none of the registered apps installed: %@. Prompting to open the AppStore link for one of them"
+ "Filtering account %@ from share acceptance — not provisioned for dataclass %@"
+ "ITEM_UNAVAILABLE_REQUEST_ACCESS_BODY_%@_SHARED_ALBUM"
+ "Multiple logged-in accounts are invited on share %{public}@. Dismissing the retrieving dialog and prompting the user to choose."
+ "Opening the share URL %{public}@%{mask.hash}@ explicitly"
+ "Passed in scene is not a UIWindowScene"
+ "Q24@0:8@\"UIWindowScene\"16"
+ "Q24@0:8@16"
+ "SHARED_ALBUM_JOIN_BUTTON"
+ "SHARED_ALBUM_OPEN_BODY"
+ "SHARED_ALBUM_OPEN_TITLE"
+ "SceneDelegate"
+ "T@\"<CKAppStoreDataProvider>\",R,N,V_appStoreDataProvider"
+ "T@\"NSMutableDictionary\",R,N,V_activeVettingURLToVettingAcceptor"
+ "T@\"NSMutableSet\",R,N,V_activeSharingURLs"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_acceptQueue"
+ "T@\"NSString\",R,N,V_countryCode"
+ "T@\"UIScreen\",&,N,V_screen"
+ "UISceneDelegate"
+ "UIWindowSceneDelegate"
+ "URLContexts"
+ "_appStoreDataProvider"
+ "_countryCode"
+ "_filterAccountsNotProvisioned:acAccountsByID:accountIDsByUsername:primaryAccountID:"
+ "_screen"
+ "alertContentForRequestAccessConfirmationForURLSlug:"
+ "alertContentForRequestAccessWithHandle:urlSlug:"
+ "appStoreDataProvider"
+ "countryCode"
+ "initWithCloudKitURL:countryCode:appStoreDataProvider:"
+ "initWithName:sessionRole:"
+ "lookUpPropertiesForURL:outError:"
+ "preferredWindowingControlStyleForScene:"
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
+ "screen"
+ "setDelegateClass:"
+ "setScreen:"
+ "stateRestorationActivityForScene:"
+ "supportedInterfaceOrientationsForWindowScene:"
+ "userActivities"
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
+ "v48@0:8@16@24@32@40"
+ "v48@0:8@16@24q32@40"
+ "windowScene:didUpdateCoordinateSpace:interfaceOrientation:traitCollection:"
+ "windowScene:didUpdateEffectiveGeometry:"
+ "windowScene:performActionForShortcutItem:completionHandler:"
+ "windowScene:userDidAcceptCloudKitShareWithMetadata:"
- "EPPCapable"
- "Fallback flow: User either not logged into iCloud or need to update Apple ID settings, error: %{public}@"
- "Fallback flow: none of the registered apps installed: %@. Prompting to opening the AppStore link for one of them"
- "Filed to construct alertTitle: %@ and/or alertBody: %@ for generic share"
- "Multiple logged-in accounts are invited on share %{public}@. Dismissing the retrieving diaglog and prompting the user to choose."
- "Opening the share URL %{public}@%{mask.hash}@ explicilty"
- "ShareBear/AppDelegate/openURL"
- "T@\"NSMutableDictionary\",&,N,V_activeVettingURLToVettingAcceptor"
- "T@\"NSMutableSet\",&,N,V_activeSharingURLs"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_acceptQueue"
- "TB,N,V_isInitialized"
- "_isInitialized"
- "alertContentForRequestAccessConfirmation"
- "alertContentForRequestAccessWithHandle:"
- "initOnce"
- "isInitialized"
- "setAcceptQueue:"
- "setActiveSharingURLs:"
- "setActiveVettingURLToVettingAcceptor:"
- "setIsInitialized:"
- "v16@?0@\"NSURL\"8"

```
