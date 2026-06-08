## iOSDiagnostics

> `/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iOSDiagnostics`

```diff

-1066.122.1.0.0
-  __TEXT.__text: 0x593c
-  __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__objc_methlist: 0x97c
+1351.0.0.0.0
+  __TEXT.__text: 0x5418
+  __TEXT.__objc_methlist: 0x9e4
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0xa81
-  __TEXT.__oslogstring: 0x396
-  __TEXT.__gcc_except_tab: 0xbc
-  __TEXT.__unwind_info: 0x238
-  __TEXT.__objc_classname: 0x29d
-  __TEXT.__objc_methname: 0x17ee
-  __TEXT.__objc_methtype: 0x588
-  __TEXT.__objc_stubs: 0x13e0
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0x340
+  __TEXT.__cstring: 0xb07
+  __TEXT.__oslogstring: 0x402
+  __TEXT.__gcc_except_tab: 0xa8
+  __TEXT.__unwind_info: 0x208
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x380
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6a0
+  __DATA_CONST.__objc_selrefs: 0x6f8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x1e0
-  __AUTH_CONST.__const: 0x60
+  __DATA_CONST.__got: 0x140
+  __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x5a0
-  __AUTH_CONST.__objc_const: 0x1b18
+  __AUTH_CONST.__objc_const: 0x1b98
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x6c
+  __DATA.__objc_ivar: 0x78
   __DATA.__data: 0x4e0
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/CheckerBoardServices.framework/CheckerBoardServices
+  - /System/Library/PrivateFrameworks/DiagnosticsCheckup.framework/DiagnosticsCheckup
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 767B9C94-990C-356F-BC60-E616B6E947E8
-  Functions: 178
-  Symbols:   842
-  CStrings:  480
+  UUID: 75EBC7CD-BC0E-387D-A056-15DC2B1CBA0F
+  Functions: 188
+  Symbols:   892
+  CStrings:  133
 
Symbols:
+ -[DADiagnosticsLauncher _establishDaemonConnection]
+ -[DADiagnosticsLauncher _establishDiagnosticsAppConnection]
+ -[DADiagnosticsLauncher _establishDiagnosticsAppConnection].cold.1
+ -[DADiagnosticsLauncher _establishDiagnosticsAppConnection].cold.2
+ -[DADiagnosticsLauncher diagnosticsCheckupServiceProvider]
+ -[DADiagnosticsLauncher fbsOpenApplicationServiceProvider]
+ -[DADiagnosticsLauncher initForTestingWithDelegate:checkupServiceProvider:fbsOpenApplicationServiceProvider:daemonFeatureFlagOverride:]
+ -[DADiagnosticsLauncher launchDiagnosticsApp]
+ -[DADiagnosticsLauncher launchDiagnosticsApp].cold.1
+ -[DADiagnosticsLauncher launchDiagnosticsApp].cold.2
+ -[DADiagnosticsLauncher launchDiagnosticsCheckupDaemon]
+ -[DADiagnosticsLauncher setDiagnosticsCheckupServiceProvider:]
+ -[DADiagnosticsLauncher setFbsOpenApplicationServiceProvider:]
+ -[DADiagnosticsLauncher setupWithDelegate:]
+ GCC_except_table14
+ _OBJC_CLASS_$_DiagnosticsCheckupService
+ _OBJC_IVAR_$_DADiagnosticsLauncher._diagnosticsCheckupServiceProvider
+ _OBJC_IVAR_$_DADiagnosticsLauncher._fbsOpenApplicationServiceProvider
+ _OBJC_IVAR_$_DADiagnosticsLauncher._useDaemonForInboxUpdaterFlow
+ ___42-[DADiagnosticsLauncher initWithDelegate:]_block_invoke
+ ___42-[DADiagnosticsLauncher initWithDelegate:]_block_invoke_2
+ ___45-[DADiagnosticsLauncher launchDiagnosticsApp]_block_invoke
+ ___45-[DADiagnosticsLauncher launchDiagnosticsApp]_block_invoke_2
+ ___45-[DADiagnosticsLauncher launchDiagnosticsApp]_block_invoke_3
+ ___45-[DADiagnosticsLauncher launchDiagnosticsApp]_block_invoke_3.cold.1
+ ___45-[DADiagnosticsLauncher launchDiagnosticsApp]_block_invoke_3.cold.2
+ ___59-[DADiagnosticsLauncher _establishDiagnosticsAppConnection]_block_invoke
+ ___59-[DADiagnosticsLauncher _establishDiagnosticsAppConnection]_block_invoke.68
+ ___block_descriptor_32_e32_"FBSOpenApplicationService"8?0l
+ ___block_descriptor_32_e43_"<DiagnosticsCheckupServiceInterface>"8?0l
+ ___block_literal_global.6
+ ___block_literal_global.64
+ __os_feature_enabled_impl
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_establishDaemonConnection
+ _objc_msgSend$_establishDiagnosticsAppConnection
+ _objc_msgSend$diagnosticsCheckupServiceProvider
+ _objc_msgSend$fbsOpenApplicationServiceProvider
+ _objc_msgSend$launchDaemon
+ _objc_msgSend$launchDiagnosticsApp
+ _objc_msgSend$launchDiagnosticsCheckupDaemon
+ _objc_msgSend$setDiagnosticsCheckupServiceProvider:
+ _objc_msgSend$setFbsOpenApplicationServiceProvider:
+ _objc_msgSend$setupWithDelegate:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_setProperty_nonatomic_copy
- -[DADiagnosticsLauncher _establishConnection]
- -[DADiagnosticsLauncher _establishConnection].cold.1
- -[DADiagnosticsLauncher _establishConnection].cold.2
- -[DADiagnosticsLauncher launchDiagnostics].cold.1
- -[DADiagnosticsLauncher launchDiagnostics].cold.2
- GCC_except_table7
- _OUTLINED_FUNCTION_5
- ___42-[DADiagnosticsLauncher launchDiagnostics]_block_invoke
- ___42-[DADiagnosticsLauncher launchDiagnostics]_block_invoke_2
- ___42-[DADiagnosticsLauncher launchDiagnostics]_block_invoke_3
- ___42-[DADiagnosticsLauncher launchDiagnostics]_block_invoke_3.cold.1
- ___42-[DADiagnosticsLauncher launchDiagnostics]_block_invoke_3.cold.2
- ___45-[DADiagnosticsLauncher _establishConnection]_block_invoke
- ___45-[DADiagnosticsLauncher _establishConnection]_block_invoke.61
- ___block_literal_global.22
- _objc_release_x9
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "@\"<DiagnosticsCheckupServiceInterface>\"8@?0"
+ "@\"FBSOpenApplicationService\"8@?0"
+ "Diagnostics"
+ "UseDaemonForInboxUpdaterFlow"
+ "launchDiagnostics called; launching diagnostics app"
+ "launchDiagnostics called; launching diagnosticscheckupd"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<DADiagnosticsLauncherDelegate>\""
- "@\"<DADiagnosticsLauncherServerProtocol>\""
- "@\"<DADiagnosticsRemoteRunnerDelegate>\""
- "@\"<DADiagnosticsRemoteViewControllerDelegate>\""
- "@\"<DARemoteRunnerServerProtocol>\""
- "@\"BSProcessHandle\""
- "@\"DADiagnosticFlow\""
- "@\"DADiagnosticResponder\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@\"RBSProcessMonitor\""
- "@\"_UISceneHostingController\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"<BSXPCDecoding>\"16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8q16"
- "@32@0:8:16@24"
- "@32@0:8q16@24"
- "@40@0:8:16@24@32"
- "@40@0:8Q16@24@32"
- "@48@0:8Q16@24@32@40"
- "@56@0:8Q16@24@32@40@48"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "BSXPCSecureCoding"
- "DADiagnosticFlow"
- "DADiagnosticResponder"
- "DADiagnosticsLauncher"
- "DADiagnosticsLauncherClientProtocol"
- "DADiagnosticsLauncherServerProtocol"
- "DADiagnosticsRemoteHostViewController"
- "DADiagnosticsRemoteViewController"
- "DADiagnosticsRemoteViewControllerHostToServiceAction"
- "DADiagnosticsRemoteViewControllerInterface"
- "DADiagnosticsRemoteViewControllerSceneSpecification"
- "DADiagnosticsRemoteViewControllerServiceToHostAction"
- "DADiagnosticsViewServiceInterface"
- "DARemoteRunnerClientProtocol"
- "DARemoteRunnerServerProtocol"
- "DKBrightnessResponder"
- "DKVolumeHUDResponder"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"<DADiagnosticsLauncherDelegate>\",&,N,V_delegate"
- "T@\"<DADiagnosticsLauncherServerProtocol>\",&,V_diagnosticsLauncherServer"
- "T@\"<DADiagnosticsRemoteRunnerDelegate>\",W,V_delegate"
- "T@\"<DADiagnosticsRemoteViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<DARemoteRunnerServerProtocol>\",&,V_remoteRunnerServer"
- "T@\"BSProcessHandle\",&,N,V_diagsProcess"
- "T@\"DADiagnosticFlow\",&,N,V_startingFlow"
- "T@\"DADiagnosticResponder\",&,N,V_responder"
- "T@\"NSNumber\",&,N,V_autoBrightnessEnabledUserSetting"
- "T@\"NSNumber\",&,N,V_screenBrightnessUserSetting"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_diagsAliveCheckQueue"
- "T@\"NSString\",&,N,V_countryCode"
- "T@\"NSString\",&,N,V_hostApplicationBundleIdentifier"
- "T@\"NSString\",&,N,V_passcode"
- "T@\"NSString\",&,N,V_serialNumber"
- "T@\"NSString\",&,N,V_sessionID"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSXPCConnection\",&,V_xpcConnection"
- "T@\"RBSProcessMonitor\",&,N,V_processMonitor"
- "T@\"_UISceneHostingController\",&,N,V_hostingController"
- "TB,R"
- "TB,V_finished"
- "TB,V_isDiagsRunning"
- "TQ,N,V_destination"
- "TQ,R"
- "Tf,N,V_originalScreenBrightness"
- "Tq,N,V_exitReason"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_UISceneHostingControllerDelegate"
- "_autoBrightnessEnabledUserSetting"
- "_beginDelayingPresentation:cancellationHandler:"
- "_countryCode"
- "_deinitProcessMonitor"
- "_delegate"
- "_destination"
- "_diagnosticsLauncherServer"
- "_diagsAliveCheckQueue"
- "_diagsProcess"
- "_endDelayingPresentation"
- "_establishConnection"
- "_exitReason"
- "_finished"
- "_hostApplicationBundleIdentifier"
- "_hostingController"
- "_initProcessMonitor"
- "_isDiagsRunning"
- "_originalScreenBrightness"
- "_passcode"
- "_processMonitor"
- "_remoteRunnerServer"
- "_responder"
- "_screenBrightnessUserSetting"
- "_serialNumber"
- "_sessionID"
- "_setSystemVolumeHUDEnabled:"
- "_startingFlow"
- "_stringForReason:"
- "_xpcConnection"
- "actionToString:"
- "actionWithType:object:"
- "activate"
- "activateConstraints:"
- "addChildViewController:"
- "addSubview:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "arrayWithObjects:count:"
- "autoBrightnessEnabledUserSetting"
- "autorelease"
- "boolValue"
- "bottomAnchor"
- "cancelTestWithID:completion:"
- "class"
- "clientIsReady"
- "conformsToProtocol:"
- "connectedScenes"
- "constraintEqualToAnchor:"
- "context"
- "countByEnumeratingWithState:objects:count:"
- "createRemoteRunnerDeviceWithSerialNumber:completion:"
- "dealloc"
- "debugDescription"
- "decodeInt64ForKey:"
- "decodeIntForKey:"
- "decodeObjectOfClass:forKey:"
- "defaultFlow"
- "delegate"
- "description"
- "descriptor"
- "destroyRemoteRunnerDeviceWithCompletion:"
- "diagnosticsAppDidExitWithReason:"
- "diagnosticsAppLaunchedWithResult:"
- "diagnosticsExitingForReason:"
- "diagnosticsLauncherServer"
- "diagsAliveCheckQueue"
- "diagsProcess"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "didMoveToParentViewController:"
- "didTerminateWithError:"
- "disconnect"
- "enableVolumeHUD:"
- "encodeInt64:forKey:"
- "encodeInt:forKey:"
- "encodeObject:forKey:"
- "encodeWithBSXPCCoder:"
- "encodeWithCoder:"
- "errorWithDomain:code:userInfo:"
- "exitEvent"
- "exitReason"
- "f"
- "f16@0:8"
- "finished"
- "floatValue"
- "getReportWithCompletion:"
- "getReportWithComponents:completion:"
- "hash"
- "hostingController"
- "identityForEmbeddedApplicationIdentifier:"
- "info"
- "init"
- "initWithActivityType:"
- "initWithBSXPCCoder:"
- "initWithCoder:"
- "initWithDelegate:"
- "initWithDestination:"
- "initWithDestination:serialNumber:sessionID:"
- "initWithDestination:serialNumber:sessionID:passcode:"
- "initWithDestination:serialNumber:sessionID:passcode:countryCode:"
- "initWithInfo:responder:"
- "initWithMachServiceName:options:"
- "initWithProcessIdentity:sceneSpecification:"
- "integerValue"
- "interfaceWithProtocol:"
- "invalidate"
- "isCheckerBoardActive"
- "isDiagsRunning"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "launchDiagnostics"
- "leadingAnchor"
- "length"
- "localizedDescription"
- "monitorWithConfiguration:"
- "numberWithBool:"
- "numberWithFloat:"
- "numberWithInteger:"
- "objectForKeyedSubscript:"
- "objectForSetting:"
- "openApplication:withOptions:completion:"
- "optionsWithDictionary:"
- "originalScreenBrightness"
- "performActionForHostedWindowScene:"
- "performActionForSceneController:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pid"
- "ping:"
- "predicateMatchingBundleIdentifier:"
- "prefersStatusBarHidden"
- "processMonitor"
- "q"
- "q16@0:8"
- "release"
- "remoteRunnerConnectionEndedWithError:"
- "remoteRunnerDeviceEnded"
- "remoteRunnerServer"
- "remoteViewController:didFinishWithReason:"
- "remoteViewControllerDidDisappear"
- "remoteViewControllerDidSetRequiredSerialNumbers:"
- "remoteViewControllerDidSetSelectableSerialNumbers:"
- "remoteViewControllerDidSetSessionToken:"
- "remoteViewControllerDidSetStartingFlow:"
- "requestAsset:completion:"
- "requestDiagnosticsRemoteViewControllerWithConnectionHandler:"
- "requestUploadAssets:completion:"
- "requestViewControllerWithConnectionHandler:"
- "requestViewControllerWithHostBundleID:flow:handler:"
- "requestViewControllerWithHostBundleID:handler:"
- "requiredSerialNumbers:"
- "resetScreenBrightness:"
- "responder"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "runTestWithID:name:description:parameters:completion:"
- "sceneViewController"
- "screen"
- "screenBrightnessUserSetting"
- "selectableSerialNumbers:"
- "self"
- "sendAction:"
- "serviceWithDefaultShellEndpoint"
- "sessionToken:"
- "setAutoBrightness:"
- "setAutoBrightnessEnabledUserSetting:"
- "setBrightness:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setCountryCode:"
- "setDelegate:"
- "setDestination:"
- "setDiagnosticsLauncherServer:"
- "setDiagsAliveCheckQueue:"
- "setDiagsProcess:"
- "setEvents:"
- "setExitReason:"
- "setExportedInterface:"
- "setExportedObject:"
- "setFinished:"
- "setHostApplicationBundleIdentifier:"
- "setHostingController:"
- "setIdleTimerDisabled:"
- "setIsDiagsRunning:"
- "setModalPresentationStyle:"
- "setObject:forKeyedSubscript:"
- "setObject:forSetting:"
- "setOriginalScreenBrightness:"
- "setPasscode:"
- "setPredicates:"
- "setProcessMonitor:"
- "setRemoteObjectInterface:"
- "setRemoteRunnerServer:"
- "setResponder:"
- "setScreenBrightnessUserSetting:"
- "setScreenToBrightness:animate:"
- "setSerialNumber:"
- "setSessionID:"
- "setStartingFlow:"
- "setStateDescriptor:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setUpdateHandler:"
- "setUserInfo:"
- "setWithArray:"
- "setXpcConnection:"
- "sharedApplication"
- "sharedInstance"
- "startingFlow"
- "stringWithFormat:"
- "superclass"
- "supportsBSXPCSecureCoding"
- "supportsSecureCoding"
- "suspend"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "topAnchor"
- "trailingAnchor"
- "type"
- "userActivity"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8f16"
- "v24@0:8@\"<BSXPCEncoding>\"16"
- "v24@0:8@\"DADiagnosticFlow\"16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v24@0:8@?<v@?@\"NSDictionary\">16"
- "v24@0:8@?<v@?@\"NSNumber\">16"
- "v24@0:8Q16"
- "v24@0:8f16B20"
- "v24@0:8q16"
- "v32@0:8@\"DKAssetUploadItems\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSDictionary\">24"
- "v32@0:8@\"NSNumber\"16@?<v@?@\"NSNumber\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSData\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSNumber\">24"
- "v32@0:8@16@?24"
- "v40@0:8@16@24@?32"
- "v56@0:8@\"NSNumber\"16@\"NSString\"24@\"NSString\"32@\"DKDiagnosticParameters\"40@?<v@?@\"DKDiagnosticResult\"@\"NSError\">48"
- "v56@0:8@16@24@32@40@?48"
- "view"
- "viewDidDisappear:"
- "viewDidLoad"
- "viewServiceDidEnableVolumeHUD:"
- "viewServiceDidFinishWithReason:"
- "viewServiceDidSetScreenToBrightness:animate:"
- "viewServiceDidSuspend"
- "window"
- "windowScene"
- "xpcConnection"
- "zone"

```
