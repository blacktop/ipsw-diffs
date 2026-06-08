## WebApp

> `/System/Library/PrivateFrameworks/WebApp.framework/WebApp`

```diff

-624.2.5.10.4
-  __TEXT.__text: 0x2d40
-  __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_methlist: 0x80c
-  __TEXT.__cstring: 0x1b9
+625.1.18.10.4
+  __TEXT.__text: 0x2f18
+  __TEXT.__objc_methlist: 0x824
+  __TEXT.__cstring: 0x22a
   __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0x30
+  __TEXT.__gcc_except_tab: 0x68
   __TEXT.__oslogstring: 0x156
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x150
-  __TEXT.__objc_classname: 0x147
-  __TEXT.__objc_methname: 0x1dbe
-  __TEXT.__objc_methtype: 0xe39
-  __TEXT.__objc_stubs: 0xf40
-  __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x120
+  __TEXT.__unwind_info: 0x168
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x148
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x758
+  __DATA_CONST.__objc_selrefs: 0x7a8
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x1d0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x1c0
-  __AUTH_CONST.__objc_const: 0x13f8
+  __AUTH_CONST.__objc_const: 0x1420
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x74
+  __DATA.__objc_ivar: 0x78
   __DATA.__data: 0x240
   __DATA.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9A9765C7-0687-3A59-895B-012F86079BD1
-  Functions: 76
-  Symbols:   512
-  CStrings:  442
+  UUID: D564C65F-FEAB-39A0-9BCA-C84D7395FA7C
+  Functions: 78
+  Symbols:   538
+  CStrings:  47
 
Symbols:
+ -[WebAppViewController _rebuildMenuIfNeeded]
+ GCC_except_table2
+ GCC_except_table21
+ GCC_except_table27
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_UITraitActiveAppearance
+ _OBJC_IVAR_$_WebAppSceneDelegate._guidedBrowserSessionIdentifier
+ ___40-[WebAppViewController initWithWebClip:]_block_invoke
+ ___block_descriptor_40_e8_32w_e52_v24?0"<UITraitEnvironment>"8"UITraitCollection"16lw32l8
+ _notify_post
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_rebuildMenuIfNeeded
+ _objc_msgSend$activationState
+ _objc_msgSend$activeAppearance
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$registerForTraitChanges:withHandler:
+ _objc_msgSend$safari_isForGuidedBrowsing
+ _objc_msgSend$statusBarFrame
+ _objc_msgSend$statusBarManager
+ _objc_msgSend$traitCollection
+ _objc_msgSend$window
+ _objc_msgSend$windowScene
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x3
+ _objc_retain_x9
- GCC_except_table19
- GCC_except_table25
- _objc_msgSend$statusBarHeightForOrientation:
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "com.apple.webclip.guidedbrowser.terminated"
+ "v24@?0@\"<UITraitEnvironment>\"8@\"UITraitCollection\"16"
- "#16@0:8"
- ".cxx_destruct"
- "@\"CPSPromise\""
- "@\"LoadingViewController\""
- "@\"NSMutableDictionary\""
- "@\"NSString\"16@0:8"
- "@\"NSTimer\""
- "@\"NSUserActivity\"24@0:8@\"UIScene\"16"
- "@\"UIAlertController\""
- "@\"UIContentUnavailableView\""
- "@\"UIImage\""
- "@\"UIImageView\""
- "@\"UIScene\""
- "@\"UISceneConfiguration\"40@0:8@\"UIApplication\"16@\"UISceneSession\"24@\"UISceneConnectionOptions\"32"
- "@\"UISceneWindowingControlStyle\"24@0:8@\"UIWindowScene\"16"
- "@\"UIView\""
- "@\"UIViewController\"40@0:8@\"UIApplication\"16@\"NSArray\"24@\"NSCoder\"32"
- "@\"UIWebClip\""
- "@\"UIWindow\""
- "@\"UIWindow\"16@0:8"
- "@\"WebAppEligibilityViewController\""
- "@\"WebAppViewController\""
- "@\"_SFWebAppViewController\""
- "@\"_UIAsyncInvocation\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@\"UIApplication\"16@\"INIntent\"24"
- "@32@0:8@16@24"
- "@32@0:8@16q24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@\"UIApplication\"16"
- "B24@0:8@16"
- "B32@0:8@\"UIApplication\"16@\"NSCoder\"24"
- "B32@0:8@\"UIApplication\"16@\"NSDictionary\"24"
- "B32@0:8@\"UIApplication\"16@\"NSString\"24"
- "B32@0:8@\"UIApplication\"16@\"NSURL\"24"
- "B32@0:8@16@24"
- "B40@0:8@\"UIApplication\"16@\"NSURL\"24@\"NSDictionary\"32"
- "B40@0:8@\"UIApplication\"16@\"NSUserActivity\"24@?<v@?@\"NSArray\">32"
- "B40@0:8@16@24@32"
- "B40@0:8@16@24@?32"
- "B48@0:8@\"UIApplication\"16@\"NSURL\"24@\"NSString\"32@40"
- "B48@0:8@16@24@32@40"
- "LoadingViewController"
- "NSObject"
- "Q16@0:8"
- "Q32@0:8@\"UIApplication\"16@\"UIWindow\"24"
- "Q32@0:8@16@24"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"UIWebClip\",R,N,V_webClip"
- "T@\"UIWindow\",?,&,N"
- "TB,N,V_overrideShowAlert"
- "TB,N,V_wasLaunchedForWebPush"
- "TQ,R"
- "UIApplicationDelegate"
- "UISceneDelegate"
- "UIWindowSceneDelegate"
- "UNUserNotificationCenterDelegate"
- "URL"
- "URLContexts"
- "URLWithString:"
- "Vv16@0:8"
- "WebAppCanvasDelegate"
- "WebAppEligibilityViewController"
- "WebAppNotificationCenterDelegate"
- "WebAppSceneDelegate"
- "WebAppViewController"
- "WebApplication"
- "^{_NSZone=}16@0:8"
- "_SFWebAppViewControllerDelegate"
- "_alertController"
- "_cancelHideSnapshotTimer"
- "_cancelViewServiceRequest"
- "_connectToService"
- "_connectionPromiseForPush"
- "_contentViewController"
- "_eligibilityViewController"
- "_hasCustomScheme"
- "_hasPendingDestroyScene"
- "_hasShownLoadingViewController"
- "_hideSnapshotTimer"
- "_image"
- "_imageIsFullScreen"
- "_imageView"
- "_loadingViewController"
- "_openURLAndDestroySceneIfNeeded"
- "_orientation"
- "_overrideShowAlert"
- "_preferredStatusBarStyle"
- "_removeRemoteView"
- "_scene"
- "_sceneHasEverEnteredForeground"
- "_setUpContentViewController:"
- "_sf_destroyScene"
- "_shouldLoadWebApp"
- "_statusBarView"
- "_tearDownWindowAndWebApp"
- "_unavailableView"
- "_wasLaunchedForWebPush"
- "_wasSuspendedUnderLock"
- "_webApp"
- "_webAppViewControllers"
- "_webClip"
- "_window"
- "absoluteString"
- "actionIdentifier"
- "addChildViewController:"
- "addCompletionBlock:"
- "addSubview:"
- "addWebAppViewController:"
- "anyObject"
- "application:configurationForConnectingSceneSession:options:"
- "application:continueUserActivity:restorationHandler:"
- "application:didChangeStatusBarFrame:"
- "application:didChangeStatusBarOrientation:"
- "application:didDecodeRestorableStateWithCoder:"
- "application:didDiscardSceneSessions:"
- "application:didFailToContinueUserActivityWithType:error:"
- "application:didFailToRegisterForRemoteNotificationsWithError:"
- "application:didFinishLaunchingWithOptions:"
- "application:didReceiveLocalNotification:"
- "application:didReceiveRemoteNotification:"
- "application:didReceiveRemoteNotification:fetchCompletionHandler:"
- "application:didRegisterForRemoteNotificationsWithDeviceToken:"
- "application:didRegisterUserNotificationSettings:"
- "application:didUpdateUserActivity:"
- "application:handleActionWithIdentifier:forLocalNotification:completionHandler:"
- "application:handleActionWithIdentifier:forLocalNotification:withResponseInfo:completionHandler:"
- "application:handleActionWithIdentifier:forRemoteNotification:completionHandler:"
- "application:handleActionWithIdentifier:forRemoteNotification:withResponseInfo:completionHandler:"
- "application:handleEventsForBackgroundURLSession:completionHandler:"
- "application:handleIntent:completionHandler:"
- "application:handleOpenURL:"
- "application:handleWatchKitExtensionRequest:reply:"
- "application:handlerForIntent:"
- "application:openURL:options:"
- "application:openURL:sourceApplication:annotation:"
- "application:performActionForShortcutItem:completionHandler:"
- "application:performFetchWithCompletionHandler:"
- "application:shouldAllowExtensionPointIdentifier:"
- "application:shouldRestoreApplicationState:"
- "application:shouldRestoreSecureApplicationState:"
- "application:shouldSaveApplicationState:"
- "application:shouldSaveSecureApplicationState:"
- "application:supportedInterfaceOrientationsForWindow:"
- "application:userDidAcceptCloudKitShareWithMetadata:"
- "application:viewControllerWithRestorationIdentifierPath:coder:"
- "application:willChangeStatusBarFrame:"
- "application:willChangeStatusBarOrientation:duration:"
- "application:willContinueUserActivityWithType:"
- "application:willEncodeRestorableStateWithCoder:"
- "application:willFinishLaunchingWithOptions:"
- "applicationDidBecomeActive:"
- "applicationDidEnterBackground:"
- "applicationDidFinishLaunching:"
- "applicationDidReceiveMemoryWarning:"
- "applicationProtectedDataDidBecomeAvailable:"
- "applicationProtectedDataWillBecomeUnavailable:"
- "applicationShouldAutomaticallyLocalizeKeyCommands:"
- "applicationShouldRequestHealthAuthorization:"
- "applicationSignificantTimeChange:"
- "applicationWillEnterForeground:"
- "applicationWillResignActive:"
- "applicationWillTerminate:"
- "autorelease"
- "blackColor"
- "bounds"
- "buildMenuWithBuilder:"
- "childViewControllerForHomeIndicatorAutoHidden"
- "childViewControllerForScreenEdgesDeferringSystemGestures"
- "childViewControllerForStatusBarHidden"
- "childViewControllerForStatusBarStyle"
- "childViewControllerForWhitePointAdaptivityStyle"
- "class"
- "conformsToProtocol:"
- "connectWebClipIdentifier:toScene:forWebPush:"
- "content"
- "currentHandler"
- "currentNotificationCenter"
- "dealloc"
- "debugDescription"
- "defaultWorkspace"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "didMoveToParentViewController:"
- "dismissViewControllerAnimated:completion:"
- "eligibilityAlert:"
- "eligibilityStatus"
- "emptyConfiguration"
- "finishWithResult:"
- "frame"
- "getStartupImage:"
- "handleFailureInFunction:file:lineNumber:description:"
- "handlePushNotificationActivation:"
- "hasPrefix:"
- "hash"
- "hideLoadingView"
- "init"
- "initWithConfiguration:"
- "initWithNibName:bundle:"
- "initWithWebClip:"
- "initWithWebClip:orientation:"
- "initWithWebClip:scene:"
- "initWithWindowScene:"
- "interfaceOrientation"
- "invalidate"
- "invoke"
- "isEqual:"
- "isEqualToString:"
- "isHSWADisabled"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isSuspendedUnderLock"
- "isWAPEnabled"
- "launchWebClipWithIdentifier:"
- "length"
- "loadView"
- "loadWebAppWithIdentifier:"
- "mainSystem"
- "makeKeyAndVisible"
- "notification"
- "notificationActivated:"
- "objectForKeyedSubscript:"
- "openURL:configuration:completionHandler:"
- "openURLWithCustomSchemeIfNeeded"
- "overrideShowAlert"
- "pageURL"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "persistentIdentifier"
- "preferredStatusBarStyle"
- "preferredWindowingControlStyleForScene:"
- "presentAlertIfNeeded"
- "presentViewController:animated:completion:"
- "presentedViewController"
- "presentingViewController"
- "processWebPushForWebAppWithIdentifier:"
- "processWebPushWithIdentifier:"
- "q"
- "q16@0:8"
- "rebuildMenuIfNeededForPersona:"
- "release"
- "removeFromParentViewController"
- "removeFromSuperview"
- "removeWebAppViewController:"
- "request"
- "requestViewControllerWithConnectionHandler:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "safari_hasCustomScheme"
- "safari_isDataURL"
- "safari_privacyPreservingDescription"
- "scene:continueUserActivity:"
- "scene:didFailToContinueUserActivityWithType:error:"
- "scene:didUpdateUserActivity:"
- "scene:openURLContexts:"
- "scene:restoreInteractionStateWithUserActivity:"
- "scene:willConnectToSession:options:"
- "scene:willContinueUserActivityWithType:"
- "sceneDidBecomeActive:"
- "sceneDidDisconnect:"
- "sceneDidEnterBackground:"
- "sceneWillEnterForeground:"
- "sceneWillResignActive:"
- "scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:"
- "self"
- "session"
- "setAutoresizingMask:"
- "setBackgroundColor:"
- "setDelegate:"
- "setFrame:"
- "setHidden:"
- "setImage:"
- "setMenusIfNecessaryForWebAppWithBuilder:"
- "setModalPresentationCapturesStatusBarAppearance:"
- "setModalPresentationStyle:"
- "setModalTransitionStyle:"
- "setNeedsStatusBarAppearanceUpdate"
- "setNeedsUpdateOfHomeIndicatorAutoHidden"
- "setNeedsUpdateOfScreenEdgesDeferringSystemGestures"
- "setNeedsWhitePointAdaptivityStyleUpdate"
- "setNetworkActivityIndicatorVisible:"
- "setObject:forKeyedSubscript:"
- "setOverrideShowAlert:"
- "setReferrerURL:"
- "setRootViewController:"
- "setView:"
- "setWasLaunchedForWebPush:"
- "setWindow:"
- "sf_isLaunchImageSizedForOrientation:includesStatusBar:"
- "sharedApplication"
- "sharedDelegate"
- "sharedProvider"
- "sourceApplication"
- "stateRestorationActivityForScene:"
- "statusBarHeightForOrientation:"
- "stringWithUTF8String:"
- "substringFromIndex:"
- "superclass"
- "supportedInterfaceOrientations"
- "system"
- "systemBackgroundColor"
- "targetContentIdentifier"
- "timeLimitForLoadCompletionExpired"
- "userInfo"
- "userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:"
- "userNotificationCenter:openSettingsForNotification:"
- "userNotificationCenter:willPresentNotification:withCompletionHandler:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"UIApplication\"16"
- "v24@0:8@\"UIScene\"16"
- "v24@0:8@\"UIWindow\"16"
- "v24@0:8@\"_SFWebAppViewController\"16"
- "v24@0:8@16"
- "v28@0:8@\"_SFWebAppViewController\"16B24"
- "v28@0:8@16B24"
- "v32@0:8@\"UIApplication\"16@\"CKShareMetadata\"24"
- "v32@0:8@\"UIApplication\"16@\"NSCoder\"24"
- "v32@0:8@\"UIApplication\"16@\"NSData\"24"
- "v32@0:8@\"UIApplication\"16@\"NSDictionary\"24"
- "v32@0:8@\"UIApplication\"16@\"NSError\"24"
- "v32@0:8@\"UIApplication\"16@\"NSSet\"24"
- "v32@0:8@\"UIApplication\"16@\"NSUserActivity\"24"
- "v32@0:8@\"UIApplication\"16@\"UILocalNotification\"24"
- "v32@0:8@\"UIApplication\"16@\"UIUserNotificationSettings\"24"
- "v32@0:8@\"UIApplication\"16@?<v@?Q>24"
- "v32@0:8@\"UIApplication\"16q24"
- "v32@0:8@\"UIScene\"16@\"NSSet\"24"
- "v32@0:8@\"UIScene\"16@\"NSString\"24"
- "v32@0:8@\"UIScene\"16@\"NSUserActivity\"24"
- "v32@0:8@\"UIWindowScene\"16@\"CKShareMetadata\"24"
- "v32@0:8@\"UIWindowScene\"16@\"UIWindowSceneGeometry\"24"
- "v32@0:8@\"UNUserNotificationCenter\"16@\"UNNotification\"24"
- "v32@0:8@\"_SFWebAppViewController\"16@\"NSError\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16q24"
- "v36@0:8@16@24B32"
- "v40@0:8@\"UIApplication\"16@\"INIntent\"24@?<v@?@\"INIntentResponse\">32"
- "v40@0:8@\"UIApplication\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\">32"
- "v40@0:8@\"UIApplication\"16@\"NSDictionary\"24@?<v@?Q>32"
- "v40@0:8@\"UIApplication\"16@\"NSString\"24@\"NSError\"32"
- "v40@0:8@\"UIApplication\"16@\"NSString\"24@?<v@?>32"
- "v40@0:8@\"UIApplication\"16@\"UIApplicationShortcutItem\"24@?<v@?B>32"
- "v40@0:8@\"UIApplication\"16q24d32"
- "v40@0:8@\"UIScene\"16@\"NSString\"24@\"NSError\"32"
- "v40@0:8@\"UIScene\"16@\"UISceneSession\"24@\"UISceneConnectionOptions\"32"
- "v40@0:8@\"UIWindowScene\"16@\"UIApplicationShortcutItem\"24@?<v@?B>32"
- "v40@0:8@\"UNUserNotificationCenter\"16@\"UNNotification\"24@?<v@?Q>32"
- "v40@0:8@\"UNUserNotificationCenter\"16@\"UNNotificationResponse\"24@?<v@?>32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16q24d32"
- "v48@0:8@\"UIApplication\"16@\"NSString\"24@\"NSDictionary\"32@?<v@?>40"
- "v48@0:8@\"UIApplication\"16@\"NSString\"24@\"UILocalNotification\"32@?<v@?>40"
- "v48@0:8@\"UIWindowScene\"16@\"<UICoordinateSpace>\"24q32@\"UITraitCollection\"40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24q32@40"
- "v56@0:8@\"UIApplication\"16@\"NSString\"24@\"NSDictionary\"32@\"NSDictionary\"40@?<v@?>48"
- "v56@0:8@\"UIApplication\"16@\"NSString\"24@\"UILocalNotification\"32@\"NSDictionary\"40@?<v@?>48"
- "v56@0:8@\"UIApplication\"16{CGRect={CGPoint=dd}{CGSize=dd}}24"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24"
- "view"
- "viewDidAppear:"
- "viewDidLayoutSubviews"
- "viewWillDisappear:"
- "wasLaunchedForWebPush"
- "webAppViewController:didChangeLoadingState:"
- "webAppViewController:viewServiceDidTerminateWithError:"
- "webAppViewControllerDidFinishInitialLoad:"
- "webClip"
- "webClipStatusBarStyle"
- "webClipWithIdentifier:"
- "window"
- "windowScene:didUpdateCoordinateSpace:interfaceOrientation:traitCollection:"
- "windowScene:didUpdateEffectiveGeometry:"
- "windowScene:performActionForShortcutItem:completionHandler:"
- "windowScene:userDidAcceptCloudKitShareWithMetadata:"
- "zone"

```
