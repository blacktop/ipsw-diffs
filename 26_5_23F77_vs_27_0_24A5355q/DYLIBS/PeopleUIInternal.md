## PeopleUIInternal

> `/System/Library/PrivateFrameworks/PeopleUIInternal.framework/PeopleUIInternal`

```diff

-121.475.3.0.0
-  __TEXT.__text: 0x3a58
-  __TEXT.__auth_stubs: 0x340
+142.1.0.0.0
+  __TEXT.__text: 0x34f4
   __TEXT.__objc_methlist: 0x6e8
   __TEXT.__const: 0x20
-  __TEXT.__cstring: 0x263
+  __TEXT.__cstring: 0x26c
   __TEXT.__oslogstring: 0x1c2
   __TEXT.__gcc_except_tab: 0xcc
-  __TEXT.__unwind_info: 0x1b8
-  __TEXT.__objc_classname: 0x1a5
-  __TEXT.__objc_methname: 0x154f
-  __TEXT.__objc_methtype: 0x695
-  __TEXT.__objc_stubs: 0x1320
-  __DATA_CONST.__got: 0x110
+  __TEXT.__unwind_info: 0x178
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x208
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x6b8
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x1b0
+  __DATA_CONST.__got: 0x110
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0xb90
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x3c
   __DATA.__data: 0x2a0

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FF93B81C-6ECC-3B58-AFA1-6426A8D3FDBA
+  UUID: 3E10B80E-F4B1-3A77-B674-38F772E352EC
   Functions: 104
-  Symbols:   591
-  CStrings:  375
+  Symbols:   597
+  CStrings:  50
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x3
+ _objc_retain_x5
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
- _objc_retain_x25
Functions:
~ -[PPLPeopleEntityViewController initWithMetadata:] : 108 -> 104
~ -[PPLPeopleEntityViewController initWithMetadata:sceneManager:] : 168 -> 176
~ -[PPLPeopleEntityViewController viewWillAppear:] : 112 -> 108
~ -[PPLPeopleEntityViewController viewDidDisappear:] : 112 -> 108
~ -[PPLPeopleEntityViewController initialSceneFrame] : 112 -> 108
~ -[PPLPeopleEntityViewController personURL] : 84 -> 76
~ -[PPLPeopleEntityViewController sceneManager:didGrantOwnershipOfScene:] : 888 -> 788
~ ___71-[PPLPeopleEntityViewController sceneManager:didGrantOwnershipOfScene:]_block_invoke : 84 -> 76
~ -[PPLPeopleEntityViewController sceneManager:didRevokeOwnershipOfScene:] : 132 -> 124
~ -[PPLPeopleEntityViewController sceneManager:sceneDidRequestDismissal:] : 144 -> 136
~ -[PPLPeopleEntityViewController viewDidLayoutSubviews] : 528 -> 504
~ ___54-[PPLPeopleEntityViewController viewDidLayoutSubviews]_block_invoke : 116 -> 108
~ -[PPLPeopleEntityViewController sceneSettingsFrameFromRect:] : 164 -> 160
~ -[PPLPeopleEntityViewController sceneSafeAreaInsetPortrait] : 304 -> 284
~ -[PPLPeopleEntityViewController safeAreaInsetFromSceneSettings:] : 128 -> 124
~ -[PPLPeopleEntityViewController scene] : 16 -> 20
~ -[PPLPeopleEntityViewController setScene:] : 80 -> 20
~ -[PPLPeopleEntityViewController hostView] : 16 -> 20
~ -[PPLPeopleEntityViewController setHostView:] : 80 -> 20
~ -[PPLPeopleEntityViewController presenter] : 16 -> 20
~ -[PPLPeopleEntityViewController setPresenter:] : 80 -> 20
~ -[PPLPeopleEntityViewController metadata] : 16 -> 20
~ -[PPLPeopleEntityViewController setMetadata:] : 80 -> 20
~ -[PPLPeopleEntityViewController sceneManager] : 16 -> 20
~ _PPLPeopleViewServiceLog : 84 -> 68
~ +[PPLPeopleAppLauncher sharedLauncher] : 176 -> 160
~ -[PPLPeopleAppLauncher init] : 136 -> 132
~ -[PPLPeopleAppLauncher launchPeopleAppIfNeededWithForegroundPriority:] : 188 -> 184
~ ___70-[PPLPeopleAppLauncher launchPeopleAppIfNeededWithForegroundPriority:]_block_invoke : 1084 -> 1016
~ ___70-[PPLPeopleAppLauncher launchPeopleAppIfNeededWithForegroundPriority:]_block_invoke.12 : 84 -> 80
~ -[PPLPeopleAppLauncher setQueue:] : 64 -> 12
~ -[PPLPeopleAppLauncher setPeopleAppProcessHandle:] : 64 -> 12
~ -[PPLPeopleAppLauncher setInitializationAssertion:] : 64 -> 12
~ -[PPLPeopleEntitySceneSettings url] : 88 -> 80
~ -[PPLPeopleEntitySceneSettings keyDescriptionForSetting:] : 116 -> 112
~ -[PPLPeopleEntitySceneSettings valueDescriptionForFlag:object:ofSetting:] : 116 -> 108
~ _PPLPeopleEntitySceneSettingValueDescription : 84 -> 80
~ -[PPLMutablePeopleEntitySceneSettings url] : 88 -> 80
~ -[PPLMutablePeopleEntitySceneSettings setUrl:] : 104 -> 100
~ -[PPLMutablePeopleEntitySceneSettings keyDescriptionForSetting:] : 116 -> 112
~ -[PPLMutablePeopleEntitySceneSettings valueDescriptionForFlag:object:ofSetting:] : 116 -> 108
~ -[PPLPeopleEntitySceneTransitionContext shouldDismiss] : 64 -> 60
~ -[PPLPeopleEntitySceneTransitionContext setShouldDismiss:] : 100 -> 96
~ -[PPLPeopleEntityMetadata initWithURL:] : 224 -> 220
~ -[PPLPeopleEntityMetadata _isValidURL:] : 480 -> 464
~ -[PPLPeopleEntityMetadata setUrl:] : 64 -> 12
~ +[PPLPeopleAppSceneManager sharedSceneManager] : 176 -> 160
~ ___46+[PPLPeopleAppSceneManager sharedSceneManager]_block_invoke : 124 -> 120
~ -[PPLPeopleAppSceneManager initWithAppLauncher:] : 152 -> 156
~ -[PPLPeopleAppSceneManager addSceneRequester:] : 248 -> 224
~ -[PPLPeopleAppSceneManager removeSceneRequester:] : 320 -> 292
~ -[PPLPeopleAppSceneManager transaction:didCreateScene:] : 200 -> 184
~ -[PPLPeopleAppSceneManager sceneDidInvalidate:] : 372 -> 340
~ -[PPLPeopleAppSceneManager scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:] : 352 -> 288
~ -[PPLPeopleAppSceneManager watchdogPolicyForProcess:eventContext:] : 280 -> 264
~ -[PPLPeopleAppSceneManager _launchPeopleAppIfNeededWithForegroundPriority:] : 84 -> 80
~ -[PPLPeopleAppSceneManager _configureSceneForRequester:] : 312 -> 252
~ -[PPLPeopleAppSceneManager _createSceneForRequester:] : 1744 -> 1684
~ ___53-[PPLPeopleAppSceneManager _createSceneForRequester:]_block_invoke_2 : 316 -> 312
~ -[PPLPeopleAppSceneManager _updateTraitCollection] : 76 -> 72
~ ___50-[PPLPeopleAppSceneManager _updateTraitCollection]_block_invoke : 164 -> 156
~ ___61-[PPLPeopleAppSceneManager _updateSceneSettingsForRequester:]_block_invoke : 268 -> 260
~ ___61-[PPLPeopleAppSceneManager _updateSceneSettingsForRequester:]_block_invoke_2 : 188 -> 172
~ -[PPLPeopleAppSceneManager _sendSceneToBackground] : 148 -> 140
~ -[PPLPeopleAppSceneManager setScene:] : 64 -> 12
~ -[PPLPeopleAppSceneManager setTransaction:] : 64 -> 12
~ ___70-[PPLPeopleAppLauncher launchPeopleAppIfNeededWithForegroundPriority:]_block_invoke.cold.1 : 120 -> 76
~ -[PPLPeopleEntityMetadata initWithURL:].cold.1 : 128 -> 124
~ -[PPLPeopleEntityMetadata initWithURL:].cold.2 : 120 -> 76
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<PPLPeopleAppLauncherDelegate>\""
- "@\"<PPLPeopleEntityViewControllerDelegate>\""
- "@\"<UIScenePresenter>\""
- "@\"FBApplicationUpdateScenesTransaction\""
- "@\"FBSProcessTerminationRequest\"32@0:8@\"FBProcess\"16@\"NSError\"24"
- "@\"FBSProcessWatchdogPolicy\"32@0:8@\"FBProcess\"16@\"FBProcessWatchdogEventContext\"24"
- "@\"FBScene\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSPointerArray\""
- "@\"NSSet\"32@0:8@\"FBScene\"16@\"NSSet\"24"
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSURL\"16@0:8"
- "@\"PPLPeopleAppLauncher\""
- "@\"PPLPeopleAppSceneManager\""
- "@\"PPLPeopleEntityMetadata\""
- "@\"RBSAssertion\""
- "@\"RBSProcessHandle\""
- "@\"UIView<UIScenePresentation>\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8q16@24Q32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "BSTransactionObserver"
- "FBApplicationUpdateScenesTransactionObserver"
- "FBProcessWatchdogProviding"
- "FBSceneObserver"
- "NSObject"
- "PPLMutablePeopleEntitySceneSettings"
- "PPLPeopleAppLauncher"
- "PPLPeopleAppLauncherDelegate"
- "PPLPeopleAppSceneManager"
- "PPLPeopleAppSceneRequester"
- "PPLPeopleEntityMetadata"
- "PPLPeopleEntitySceneSettings"
- "PPLPeopleEntitySceneSpecification"
- "PPLPeopleEntitySceneTransitionContext"
- "PPLPeopleEntityViewController"
- "Q16@0:8"
- "T#,R"
- "T@\"<PPLPeopleAppLauncherDelegate>\",W,N,V_delegate"
- "T@\"<PPLPeopleEntityViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<UIScenePresenter>\",&,N,V_presenter"
- "T@\"FBApplicationUpdateScenesTransaction\",&,N,V_transaction"
- "T@\"FBScene\",&,N,V_scene"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSPointerArray\",R,C,N,V_sceneRequesters"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSURL\",&,N"
- "T@\"NSURL\",&,N,V_url"
- "T@\"NSURL\",R,N"
- "T@\"PPLPeopleAppLauncher\",R,N,V_peopleAppLauncher"
- "T@\"PPLPeopleAppSceneManager\",R,N,V_sceneManager"
- "T@\"PPLPeopleEntityMetadata\",&,N,V_metadata"
- "T@\"RBSAssertion\",&,N,V_initializationAssertion"
- "T@\"RBSProcessHandle\",&,N,V_peopleAppProcessHandle"
- "T@\"UIView<UIScenePresentation>\",&,N,V_hostView"
- "TB,N"
- "TQ,R"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N"
- "T{UIEdgeInsets=dddd},R,N"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_configureSceneForRequester:"
- "_createSceneForRequester:"
- "_delegate"
- "_hostView"
- "_initializationAssertion"
- "_isValidURL:"
- "_launchPeopleAppIfNeededWithForegroundPriority:"
- "_metadata"
- "_peopleAppLauncher"
- "_peopleAppProcessHandle"
- "_presenter"
- "_queue"
- "_scene"
- "_sceneManager"
- "_sceneRequesters"
- "_sendSceneToBackground"
- "_transaction"
- "_updateSceneSettingsForRequester:"
- "_updateTraitCollection"
- "_url"
- "activate"
- "addObserver:"
- "addObserver:selector:name:object:"
- "addPointer:"
- "addSceneRequester:"
- "addSubview:"
- "allObjects"
- "arrayWithObjects:count:"
- "attributeWithCompletionPolicy:"
- "autorelease"
- "begin"
- "boolForSetting:"
- "bottomAnchor"
- "bounds"
- "class"
- "clientSettingsClass"
- "conformsToProtocol:"
- "constraintEqualToAnchor:"
- "containsObject:"
- "contextWithIdentity:"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createPresenterWithIdentifier:"
- "currentHandler"
- "currentState"
- "debugDescription"
- "defaultCenter"
- "delegate"
- "description"
- "event"
- "execute:assertion:error:"
- "frame"
- "grantUserInitiated"
- "grantWithBackgroundPriority"
- "grantWithForegroundPriority"
- "grantWithUserInteractivity"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hash"
- "hostView"
- "identifier"
- "identityForEmbeddedApplicationIdentifier:"
- "identityForIdentifier:workspaceIdentifier:"
- "indexOfObject:"
- "init"
- "initWithAppLauncher:"
- "initWithContext:"
- "initWithMetadata:"
- "initWithMetadata:sceneManager:"
- "initWithNibName:bundle:"
- "initWithProcessIdentity:executionContextProvider:"
- "initWithSettings:"
- "initWithSpecification:"
- "initWithURL:"
- "initWithURL:resolvingAgainstBaseURL:"
- "initialSceneFrame"
- "initializationAssertion"
- "invalidate"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isRunning"
- "isUISubclass"
- "isValid"
- "keyDescriptionForSetting:"
- "lastObject"
- "launchPeopleAppIfNeededWithForegroundPriority:"
- "layoutIfNeeded"
- "leadingAnchor"
- "mainConfiguration"
- "mainScreen"
- "metadata"
- "modifyPresentationContext:"
- "mutableCopy"
- "mutableCopyWithZone:"
- "name"
- "objectForSetting:"
- "otherSettings"
- "peopleAppLauncher"
- "peopleAppProcessHandle"
- "peopleEntityViewControllerDidRequestDismissal:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performUpdate:withCompletion:"
- "personURL"
- "policyWithProvisions:"
- "presentationView"
- "presenter"
- "provisionWithAllowance:"
- "queryItems"
- "queue"
- "release"
- "removeFromSuperview"
- "removeObserver:"
- "removePointerAtIndex:"
- "removeSceneRequester:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "safeAreaInsetFromSceneSettings:"
- "safeAreaInsetsPortrait"
- "scene"
- "scene:clientDidConnect:"
- "scene:didApplyUpdateWithContext:"
- "scene:didCompleteUpdateWithContext:error:"
- "scene:didPrepareUpdateWithContext:"
- "scene:didUpdateClientSettings:"
- "scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:"
- "scene:didUpdateSettings:"
- "scene:handleActions:"
- "sceneContentStateDidChange:"
- "sceneDidActivate:"
- "sceneDidInvalidate:"
- "sceneDidInvalidate:withContext:"
- "sceneManager"
- "sceneManager:didGrantOwnershipOfScene:"
- "sceneManager:didRevokeOwnershipOfScene:"
- "sceneManager:sceneDidRequestDismissal:"
- "sceneRequesters"
- "sceneSafeAreaInsetPortrait"
- "sceneSettingsFrameFromRect:"
- "sceneWillActivate:"
- "sceneWillDeactivate:withContext:"
- "sceneWillDeactivate:withError:"
- "scheme"
- "self"
- "setActions:"
- "setActive:"
- "setAttributes:"
- "setBackgroundColorWhileHosting:"
- "setClientSettings:"
- "setCompletionBlock:"
- "setDefaultStatusBarHeight:forOrientation:"
- "setDelegate:"
- "setDisplayConfiguration:"
- "setExplanation:"
- "setFlag:forSetting:"
- "setForcedStatusBarForegroundTransparent:"
- "setForeground:"
- "setFrame:"
- "setHostView:"
- "setInitializationAssertion:"
- "setInterfaceOrientation:"
- "setInterfaceOrientationMode:"
- "setLaunchIntent:"
- "setMetadata:"
- "setObject:forSetting:"
- "setPeopleAppProcessHandle:"
- "setPresentedLayerTypes:"
- "setPresenter:"
- "setQueue:"
- "setSafeAreaInsetsPortrait:"
- "setScene:"
- "setSettings:"
- "setShouldDismiss:"
- "setStatusBarHidden:"
- "setSupportedInterfaceOrientations:"
- "setTransaction:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setUrl:"
- "setUserInterfaceStyle:"
- "setWaitsForSceneCommits:"
- "setWatchdogProvider:"
- "setWithObject:"
- "settings"
- "settingsClass"
- "sharedLauncher"
- "sharedSceneManager"
- "shouldDismiss"
- "stringWithFormat:"
- "superclass"
- "topAnchor"
- "trailingAnchor"
- "traitCollection"
- "transaction"
- "transaction:didCommitSceneUpdate:"
- "transaction:didCreateScene:"
- "transaction:didLaunchProcess:"
- "transaction:willCommitSceneUpdate:"
- "transaction:willLaunchProcess:"
- "transaction:willUpdateScene:"
- "transactionDidBegin:"
- "transactionDidComplete:"
- "transactionDidFinishWork:"
- "transactionWillBegin:"
- "transitionContextClass"
- "uiPresentationManager"
- "updateSceneWithIdentity:parameters:transitionContext:"
- "updateSettingsWithBlock:"
- "updateSettingsWithTransitionBlock:"
- "userInterfaceStyle"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"BSTransaction\"16"
- "v24@0:8@\"FBScene\"16"
- "v24@0:8@\"PPLPeopleAppLauncher\"16"
- "v24@0:8@16"
- "v32@0:8@\"FBApplicationUpdateScenesTransaction\"16@\"FBApplicationProcess\"24"
- "v32@0:8@\"FBApplicationUpdateScenesTransaction\"16@\"FBScene\"24"
- "v32@0:8@\"FBScene\"16@\"FBSSceneTransitionContext\"24"
- "v32@0:8@\"FBScene\"16@\"FBSSceneUpdate\"24"
- "v32@0:8@\"FBScene\"16@\"FBSceneClientHandle\"24"
- "v32@0:8@\"FBScene\"16@\"FBSceneUpdateContext\"24"
- "v32@0:8@\"FBScene\"16@\"NSError\"24"
- "v32@0:8@\"PPLPeopleAppSceneManager\"16@\"FBScene\"24"
- "v32@0:8@16@24"
- "v40@0:8@\"FBScene\"16@\"FBSceneUpdateContext\"24@\"NSError\"32"
- "v40@0:8@16@24@32"
- "v48@0:8@\"FBScene\"16@\"FBSSceneClientSettingsDiff\"24@\"FBSSceneClientSettings\"32@\"FBSSceneTransitionContext\"40"
- "v48@0:8@16@24@32@40"
- "valueDescriptionForFlag:object:ofSetting:"
- "view"
- "viewDidDisappear:"
- "viewDidLayoutSubviews"
- "viewWillAppear:"
- "watchdogPolicyForProcess:eventContext:"
- "watchdogTerminationRequestForProcess:error:"
- "weakObjectsPointerArray"
- "willLaunchPeopleAppInBackground:"
- "window"
- "zone"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{CGRect={CGPoint=dd}{CGSize=dd}}48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "{UIEdgeInsets=dddd}16@0:8"
- "{UIEdgeInsets=dddd}24@0:8@16"

```
