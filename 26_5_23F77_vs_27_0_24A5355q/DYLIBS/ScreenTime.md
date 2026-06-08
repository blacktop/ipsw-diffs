## ScreenTime

> `/System/Library/Frameworks/ScreenTime.framework/ScreenTime`

```diff

-605.5.10.0.0
-  __TEXT.__text: 0x4a40
-  __TEXT.__auth_stubs: 0x350
+637.0.102.0.0
+  __TEXT.__text: 0x471c
   __TEXT.__objc_methlist: 0x71c
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x2ea
-  __TEXT.__gcc_except_tab: 0xc8
+  __TEXT.__cstring: 0x2f3
+  __TEXT.__gcc_except_tab: 0xa8
   __TEXT.__oslogstring: 0x4a6
-  __TEXT.__unwind_info: 0x248
-  __TEXT.__objc_classname: 0x105
-  __TEXT.__objc_methname: 0x1657
-  __TEXT.__objc_methtype: 0x544
-  __TEXT.__objc_stubs: 0xfe0
-  __DATA_CONST.__got: 0x150
+  __TEXT.__unwind_info: 0x240
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x348
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_selrefs: 0x5c0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__got: 0x150
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x1e0
   __AUTH_CONST.__objc_const: 0xe80
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x54
   __DATA.__data: 0x240

   - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B61AA4B7-9512-3040-9901-F45C044C8DC6
-  Functions: 169
-  Symbols:   756
-  CStrings:  361
+  UUID: BB56397F-D041-35F2-BE8E-742A35C0644C
+  Functions: 165
+  Symbols:   746
+  CStrings:  60
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x24
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x6
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
- _objc_retain_x26
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<NSCopying>\""
- "@\"NSExtension\""
- "@\"NSObject\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSXPCConnection\""
- "@\"STScreenTimeConfiguration\""
- "@\"STWebRemoteViewController\""
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24^@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16^@24"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "STScreenTimeAgent"
- "STScreenTimeAgentConnection"
- "STScreenTimeBundle"
- "STScreenTimeConfiguration"
- "STScreenTimeConfigurationObserver"
- "STWebHistory"
- "STWebRemoteViewController"
- "STWebService"
- "STWebServiceDelegate"
- "STWebpageController"
- "T#,R"
- "T@\"<NSCopying>\",C,N,V_extensionRequestIdentifier"
- "T@\"<STWebService>\",R"
- "T@\"NSBundle\",R"
- "T@\"NSExtension\",&,N,V_extension"
- "T@\"NSMutableArray\",R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_bundleIdentifier"
- "T@\"NSString\",C,N,V_profileIdentifier"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,V_bundleIdentifier"
- "T@\"NSString\",R,C,V_profileIdentifier"
- "T@\"NSURL\",C,N,V_URL"
- "T@\"NSURL\",R,C"
- "T@\"NSXPCConnection\",R,V_xpcConnection"
- "T@\"STScreenTimeConfiguration\",&,V_configuration"
- "T@\"STWebRemoteViewController\",&,V_remoteViewController"
- "TB,N,V_URLIsPictureInPicture"
- "TB,N,V_URLIsPlayingVideo"
- "TB,N,V_suppressUsageRecording"
- "TB,R"
- "TB,V_URLIsBlocked"
- "TB,V_URLIsVisibleInForeground"
- "TB,V_enforcesChildRestrictions"
- "TQ,R"
- "Ti,V_notificationToken"
- "Tq,N"
- "Tq,R"
- "URL"
- "URLIsPictureInPicture"
- "URLIsPlayingVideo"
- "URLIsPlayingVideoPictureInPicture"
- "URLIsVisibleInForeground"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_URL"
- "_URLIsBlocked"
- "_URLIsBlockedDidChangeFrom:to:"
- "_URLIsPictureInPicture"
- "_URLIsPlayingVideo"
- "_URLIsVisibleInForeground"
- "_applicationDidBecomeActive:"
- "_applicationDidEnterBackground:"
- "_bundleIdentifier"
- "_canShowWhileLocked"
- "_changeUsageStateIfNeeded:completionHandler:"
- "_configuration"
- "_configurationLock"
- "_currentUsageState"
- "_didChangePlaybackState:"
- "_didStopPictureInPicture:"
- "_enforcesChildRestrictions"
- "_extension"
- "_extensionRequestIdentifier"
- "_installRemoteViewController:"
- "_installRemoteViewControllerIfNeededWithCompletionHandler:"
- "_installRemoteViewControllerOnMainThreadIfNeededWithCompletionHandler:"
- "_lp_isHTTPFamilyURL"
- "_notificationToken"
- "_profileIdentifier"
- "_queue"
- "_remoteViewController"
- "_requestConfiguration"
- "_setQueue:"
- "_setURL:bundleIdentifier:profileIdentifier:usageState:errorHandler:"
- "_stScreenTimeConfigurationCommonInitWithEnforcesChildRestrictions:"
- "_startReportingWebUsage"
- "_suppressUsageRecording"
- "_uninstallRemoteViewControllerIfNeeded"
- "_uninstallRemoteViewControllerOnMainThreadIfNeeded"
- "_updateWithConfiguration:"
- "_willStartPictureInPicture:"
- "_xpcConnection"
- "activateConstraints:"
- "addChildViewController:"
- "addObject:"
- "addObserver:forKeyPath:options:context:"
- "addObserver:selector:name:object:"
- "addOperationWithBlock:"
- "addSubview:"
- "arrayByAddingObjectsFromArray:"
- "autorelease"
- "boolValue"
- "bundle"
- "bundleForClass:"
- "bundleIdentifier"
- "bundleURL"
- "cacheWebViewController:"
- "cancelExtensionRequestWithIdentifier:"
- "changeUsageState:replyHandler:"
- "class"
- "clientBundleIdentifier"
- "clientBundleURL"
- "configuration"
- "conformsToProtocol:"
- "constraintsWithVisualFormat:options:metrics:views:"
- "containsObject:"
- "containsValueForKey:"
- "copy"
- "currentHandler"
- "currentUsageState"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "defaultCenter"
- "defaultUsageState"
- "deleteAllHistory"
- "deleteAllWebApplicationHistory:profileIdentifier:clientBundleURLWrapper:replyHandler:"
- "deleteHistoryDuringInterval:"
- "deleteHistoryForURL:"
- "deleteWebHistoryDuringInterval:webApplication:profileIdentifier:clientBundleURLWrapper:replyHandler:"
- "deleteWebHistoryForURL:webApplication:profileIdentifier:clientBundleURLWrapper:replyHandler:"
- "dequeueWebViewController"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "didMoveToParentViewController:"
- "encodeBool:forKey:"
- "encodeWithCoder:"
- "enforcesChildRestrictions"
- "errorWithDomain:code:userInfo:"
- "exportedInterface"
- "extension"
- "extensionRequestIdentifier"
- "extensionsWithMatchingAttributes:error:"
- "fetchAllHistoryWithCompletionHandler:"
- "fetchAllWebApplicationHistory:profileIdentifier:clientBundleURLWrapper:replyHandler:"
- "fetchHistoryDuringInterval:completionHandler:"
- "fetchHistoryDuringInterval:webApplication:profileIdentifier:clientBundleURLWrapper:replyHandler:"
- "firstObject"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hash"
- "i"
- "i16@0:8"
- "init"
- "initWithBundleIdentifier:error:"
- "initWithBundleIdentifier:profileIdentifier:"
- "initWithBundleIdentifier:profileIdentifier:error:"
- "initWithCoder:"
- "initWithEnforcesChildRestrictions:"
- "initWithMachServiceName:options:"
- "initWithObjects:"
- "initWithProfileIdentifier:"
- "initWithURL:readonly:"
- "initWithUpdateQueue:"
- "instantiateViewControllerWithInputItems:connectionHandler:"
- "instantiateWebViewControllerWithConnectionHandler:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMainThread"
- "isMemberOfClass:"
- "isProxy"
- "loadView"
- "localizedStringForKey:value:table:"
- "mainBundle"
- "mainQueue"
- "newConnection"
- "newDelegateInterface"
- "newInterface"
- "newServiceInterface"
- "notificationToken"
- "null"
- "objectForKeyedSubscript:"
- "observeValueForKeyPath:ofObject:change:context:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "processInfo"
- "processName"
- "profileIdentifier"
- "proxyFromConnection:proxyHandler:"
- "q"
- "q16@0:8"
- "release"
- "remoteViewController"
- "removeFromParentViewController"
- "removeFromSuperview"
- "removeObjectAtIndex:"
- "removeObserver:forKeyPath:"
- "removeObserver:name:object:"
- "requestConfigurationWithReplyHandler:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "serviceProxy"
- "serviceViewControllerInterface"
- "serviceViewControllerProxyWithErrorHandler:"
- "setBundleIdentifier:"
- "setBundleIdentifier:error:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setConfiguration:"
- "setCurrentUsageState:"
- "setEnforcesChildRestrictions:"
- "setExtension:"
- "setExtensionRequestIdentifier:"
- "setNotificationToken:"
- "setPreferredContentSize:"
- "setProfileIdentifier:"
- "setRemoteObjectInterface:"
- "setRemoteViewController:"
- "setSuppressUsageRecording:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setURL:"
- "setURL:bundleIdentifier:profileIdentifier:usageState:replyHandler:"
- "setURLIsBlocked:"
- "setURLIsBlocked:replyHandler:"
- "setURLIsPictureInPicture:"
- "setURLIsPlayingVideo:"
- "setURLIsVisibleInForeground:"
- "setUserInteractionEnabled:"
- "setView:"
- "sharedCache"
- "startObserving"
- "stopObserving"
- "stringByAppendingString:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "supportedWebBrowserBundleIdentifiersForDeviceFamily:"
- "supportsSecureCoding"
- "suppressUsageRecording"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"STScreenTimeConfiguration\"@\"NSError\">16"
- "v24@0:8q16"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?>20"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8q16@?24"
- "v32@0:8q16@?<v@?@\"NSError\">24"
- "v32@0:8{CGSize=dd}16"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSSecurityScopedURLWrapper\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSSecurityScopedURLWrapper\"32@?<v@?@\"NSSet\"@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24@32^v40"
- "v56@0:8@\"NSDateInterval\"16@\"NSString\"24@\"NSString\"32@\"NSSecurityScopedURLWrapper\"40@?<v@?@\"NSError\">48"
- "v56@0:8@\"NSDateInterval\"16@\"NSString\"24@\"NSString\"32@\"NSSecurityScopedURLWrapper\"40@?<v@?@\"NSSet\"@\"NSError\">48"
- "v56@0:8@\"NSURL\"16@\"NSString\"24@\"NSString\"32@\"NSSecurityScopedURLWrapper\"40@?<v@?@\"NSError\">48"
- "v56@0:8@\"NSURL\"16@\"NSString\"24@\"NSString\"32q40@?<v@?@\"NSError\">48"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8@16@24@32q40@?48"
- "view"
- "viewDidAppear:"
- "viewDidDisappear:"
- "viewDidLoad"
- "willMoveToParentViewController:"
- "xpcConnection"
- "zone"

```
