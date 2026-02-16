## PeopleUIInternal

> `/System/Library/PrivateFrameworks/PeopleUIInternal.framework/PeopleUIInternal`

```diff

-121.325.1.0.0
-  __TEXT.__text: 0x3594
-  __TEXT.__auth_stubs: 0x3a0
+132.0.0.0.0
+  __TEXT.__text: 0x3a58
+  __TEXT.__auth_stubs: 0x340
   __TEXT.__objc_methlist: 0x6e8
   __TEXT.__const: 0x20
   __TEXT.__cstring: 0x263
   __TEXT.__oslogstring: 0x1c2
   __TEXT.__gcc_except_tab: 0xcc
-  __TEXT.__unwind_info: 0x178
+  __TEXT.__unwind_info: 0x1b8
   __TEXT.__objc_classname: 0x1a5
   __TEXT.__objc_methname: 0x154f
   __TEXT.__objc_methtype: 0x695

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x6b8
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x1e0
+  __AUTH_CONST.__auth_got: 0x1b0
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0xb90

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8BE45026-108C-37B9-8C8D-54529D4BBA68
-  Functions: 103
-  Symbols:   595
+  UUID: 8BC0A7B4-39BF-3C81-9C2B-FB9033F821A0
+  Functions: 104
+  Symbols:   591
   CStrings:  375
 
Symbols:
+ _OUTLINED_FUNCTION_1
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x23
+ _objc_retain_x25
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x21
- _objc_retain_x22
- _objc_retain_x3
- _objc_retain_x5
- _objc_retain_x8
Functions:
~ -[PPLPeopleEntityViewController initWithMetadata:] : 104 -> 108
~ -[PPLPeopleEntityViewController initWithMetadata:sceneManager:] : 176 -> 168
~ -[PPLPeopleEntityViewController viewWillAppear:] : 108 -> 112
~ -[PPLPeopleEntityViewController viewDidDisappear:] : 108 -> 112
~ -[PPLPeopleEntityViewController initialSceneFrame] : 108 -> 112
~ -[PPLPeopleEntityViewController personURL] : 76 -> 84
~ -[PPLPeopleEntityViewController sceneManager:didGrantOwnershipOfScene:] : 788 -> 888
~ ___71-[PPLPeopleEntityViewController sceneManager:didGrantOwnershipOfScene:]_block_invoke : 76 -> 84
~ -[PPLPeopleEntityViewController sceneManager:didRevokeOwnershipOfScene:] : 124 -> 132
~ -[PPLPeopleEntityViewController sceneManager:sceneDidRequestDismissal:] : 136 -> 144
~ -[PPLPeopleEntityViewController viewDidLayoutSubviews] : 504 -> 528
~ ___54-[PPLPeopleEntityViewController viewDidLayoutSubviews]_block_invoke : 108 -> 116
~ -[PPLPeopleEntityViewController sceneSettingsFrameFromRect:] : 160 -> 164
~ -[PPLPeopleEntityViewController sceneSafeAreaInsetPortrait] : 284 -> 304
~ -[PPLPeopleEntityViewController safeAreaInsetFromSceneSettings:] : 124 -> 128
~ -[PPLPeopleEntityViewController setScene:] : 20 -> 80
~ -[PPLPeopleEntityViewController setHostView:] : 20 -> 80
~ -[PPLPeopleEntityViewController setPresenter:] : 20 -> 80
~ -[PPLPeopleEntityViewController setMetadata:] : 20 -> 80
~ _PPLPeopleViewServiceLog : 68 -> 84
~ +[PPLPeopleAppLauncher sharedLauncher] : 160 -> 176
~ -[PPLPeopleAppLauncher init] : 132 -> 136
~ -[PPLPeopleAppLauncher launchPeopleAppIfNeededWithForegroundPriority:] : 184 -> 188
~ ___70-[PPLPeopleAppLauncher launchPeopleAppIfNeededWithForegroundPriority:]_block_invoke : 1016 -> 1084
~ ___70-[PPLPeopleAppLauncher launchPeopleAppIfNeededWithForegroundPriority:]_block_invoke.12 : 80 -> 84
~ -[PPLPeopleAppLauncher setQueue:] : 12 -> 64
~ -[PPLPeopleAppLauncher setPeopleAppProcessHandle:] : 12 -> 64
~ -[PPLPeopleAppLauncher setInitializationAssertion:] : 12 -> 64
~ -[PPLPeopleEntitySceneSettings url] : 80 -> 88
~ -[PPLPeopleEntitySceneSettings keyDescriptionForSetting:] : 112 -> 116
~ -[PPLPeopleEntitySceneSettings valueDescriptionForFlag:object:ofSetting:] : 108 -> 116
~ _PPLPeopleEntitySceneSettingValueDescription : 80 -> 84
~ -[PPLMutablePeopleEntitySceneSettings url] : 80 -> 88
~ -[PPLMutablePeopleEntitySceneSettings setUrl:] : 100 -> 104
~ -[PPLMutablePeopleEntitySceneSettings keyDescriptionForSetting:] : 112 -> 116
~ -[PPLMutablePeopleEntitySceneSettings valueDescriptionForFlag:object:ofSetting:] : 108 -> 116
~ -[PPLPeopleEntitySceneTransitionContext shouldDismiss] : 60 -> 64
~ -[PPLPeopleEntitySceneTransitionContext setShouldDismiss:] : 96 -> 100
~ -[PPLPeopleEntityMetadata initWithURL:] : 220 -> 224
~ -[PPLPeopleEntityMetadata _isValidURL:] : 460 -> 480
~ -[PPLPeopleEntityMetadata setUrl:] : 12 -> 64
~ +[PPLPeopleAppSceneManager sharedSceneManager] : 160 -> 176
~ ___46+[PPLPeopleAppSceneManager sharedSceneManager]_block_invoke : 120 -> 124
~ -[PPLPeopleAppSceneManager initWithAppLauncher:] : 156 -> 152
~ -[PPLPeopleAppSceneManager addSceneRequester:] : 224 -> 248
~ -[PPLPeopleAppSceneManager removeSceneRequester:] : 292 -> 320
~ -[PPLPeopleAppSceneManager transaction:didCreateScene:] : 184 -> 200
~ -[PPLPeopleAppSceneManager sceneDidInvalidate:] : 340 -> 372
~ -[PPLPeopleAppSceneManager scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:] : 332 -> 352
~ -[PPLPeopleAppSceneManager watchdogPolicyForProcess:eventContext:] : 264 -> 280
~ -[PPLPeopleAppSceneManager _launchPeopleAppIfNeededWithForegroundPriority:] : 80 -> 84
~ -[PPLPeopleAppSceneManager _configureSceneForRequester:] : 296 -> 312
~ -[PPLPeopleAppSceneManager _createSceneForRequester:] : 1676 -> 1744
~ ___53-[PPLPeopleAppSceneManager _createSceneForRequester:]_block_invoke_2 : 312 -> 316
~ -[PPLPeopleAppSceneManager _updateTraitCollection] : 72 -> 76
~ ___50-[PPLPeopleAppSceneManager _updateTraitCollection]_block_invoke : 156 -> 164
~ ___61-[PPLPeopleAppSceneManager _updateSceneSettingsForRequester:]_block_invoke : 260 -> 268
~ ___61-[PPLPeopleAppSceneManager _updateSceneSettingsForRequester:]_block_invoke_2 : 172 -> 188
~ -[PPLPeopleAppSceneManager _sendSceneToBackground] : 140 -> 148
~ -[PPLPeopleAppSceneManager setScene:] : 12 -> 64
~ -[PPLPeopleAppSceneManager setTransaction:] : 12 -> 64
~ _OUTLINED_FUNCTION_0 : 28 -> 20
+ _OUTLINED_FUNCTION_1
~ -[PPLPeopleEntityMetadata initWithURL:].cold.1 : 124 -> 128
~ -[PPLPeopleAppSceneManager sceneDidInvalidate:].cold.1 : 56 -> 44
~ -[PPLPeopleAppSceneManager _createSceneForRequester:].cold.1 : 56 -> 44
~ ___53-[PPLPeopleAppSceneManager _createSceneForRequester:]_block_invoke_2.cold.1 : 56 -> 44

```
