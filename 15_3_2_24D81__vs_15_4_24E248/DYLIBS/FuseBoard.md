## FuseBoard

> `/System/iOSSupport/System/Library/PrivateFrameworks/FuseBoard.framework/Versions/A/FuseBoard`

```diff

 610.0.0.0.0
-  __TEXT.__text: 0x19128
-  __TEXT.__auth_stubs: 0x7a0
-  __TEXT.__objc_methlist: 0x8e0
-  __TEXT.__const: 0x3a0
+  __TEXT.__text: 0x19324
+  __TEXT.__auth_stubs: 0x780
+  __TEXT.__objc_methlist: 0xf14
+  __TEXT.__const: 0x360
   __TEXT.__gcc_except_tab: 0x13c
-  __TEXT.__cstring: 0x12da
+  __TEXT.__cstring: 0x12d9
   __TEXT.__oslogstring: 0xef7
   __TEXT.__dlopen_cstrs: 0x1a3
   __TEXT.__unwind_info: 0x338

   __TEXT.__objc_methname: 0x3666
   __TEXT.__objc_methtype: 0x1457
   __TEXT.__objc_stubs: 0x2c40
-  __DATA_CONST.__got: 0x348
+  __DATA_CONST.__got: 0x358
   __DATA_CONST.__const: 0x478
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd08
+  __DATA_CONST.__objc_selrefs: 0xf00
   __DATA_CONST.__objc_superrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x3e0
+  __AUTH_CONST.__auth_got: 0x3d0
   __AUTH_CONST.__const: 0x160
   __AUTH_CONST.__cfstring: 0xda0
-  __AUTH_CONST.__objc_const: 0x4458
+  __AUTH_CONST.__objc_const: 0x3940
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x50

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EB1686D8-F78C-3840-93E4-0E34A7E70DB5
+  UUID: 9B2620C2-637E-3403-BBEF-07C1FF10FDC6
   Functions: 306
   Symbols:   1374
   CStrings:  1093
Functions:
~ -[BSProcessHandle(FuseBoard) fu_versionedPID] : 88 -> 96
~ +[RBSProcessHandle(FuseBoard) fu_handleForIdentifier:] : 296 -> 308
~ -[FBProcess(FuseBoard) fu_isUIKitApplication] : 100 -> 104
~ +[NSArray(USSAccessibilitySoftlinkExtensions) arrayWithCountElements:nilObjectBlock:] : 368 -> 360
~ -[FUAccessibilityServer initWithAppProvider:] : 732 -> 756
~ ___45-[FUAccessibilityServer initWithAppProvider:]_block_invoke : 180 -> 188
~ -[FUAccessibilityServer dealloc] : 120 -> 128
~ -[FUAccessibilityServer _queue_initializeSystemSettings] : 1648 -> 1604
~ ___56-[FUAccessibilityServer _queue_initializeSystemSettings]_block_invoke : 384 -> 372
~ _getkMADisplayFilterSettingsChangedNotification : 260 -> 252
~ _libUAPreferencesLibrary : 304 -> 284
~ _getUADomainScreenPolarityDidChangeNotification : 260 -> 252
~ __56-[FUAccessibilityServer _queue_initializeSystemSettings]_block_invoke.62 : 384 -> 372
~ _getUADomainKeyboardAccessSettingsDidChangeNotification : 260 -> 252
~ _getUADomainAssistiveControlSettingsDidChangeNotification : 260 -> 252
~ _getUADomainVoiceOverSettingsDidChangeNotification : 260 -> 252
~ _getUADomainSpeechSettingsDidChangeNotification : 260 -> 252
~ -[FUAccessibilityServer _queue_applySettingWithKey:] : 1052 -> 936
~ _soft_NXOpenEventStatus : 268 -> 260
~ _soft_NXKeyRepeatInterval : 276 -> 268
~ _soft_NXKeyRepeatThreshold : 276 -> 268
~ _soft_NXCloseEventStatus : 276 -> 268
~ -[FUAccessibilityServer isClassicInvertColorsEnabled] : 44 -> 40
~ -[FUAccessibilityServer isDifferentiateWithoutColorEnabled] : 44 -> 40
~ -[FUAccessibilityServer isIncreaseContrastEnabled] : 44 -> 40
~ -[FUAccessibilityServer isReduceMotionEnabled] : 44 -> 40
~ -[FUAccessibilityServer isReduceTransparencyEnabled] : 44 -> 40
~ -[FUAccessibilityServer isInvertColorsEnabled] : 388 -> 384
~ _UniversalAccessCoreLibrary : 304 -> 284
~ _soft_UAWhiteOnBlackIsEnabled : 272 -> 260
~ -[FUAccessibilityServer _isGrayscaleColorFilterEnabled] : 388 -> 384
~ _soft_UAGrayscaleIsEnabled : 272 -> 260
~ -[FUAccessibilityServer isFullKeyboardAccessEnabled] : 388 -> 384
~ _soft_UAKeyboardAccessIsEnabled : 272 -> 260
~ -[FUAccessibilityServer isSwitchControlEnabled] : 388 -> 384
~ _soft_UASwitchControlIsEnabled : 272 -> 260
~ -[FUAccessibilityServer isVoiceOverEnabled] : 388 -> 384
~ _soft_UAVoiceOverIsEnabled : 272 -> 260
~ -[FUAccessibilityServer isSpeakSelectionEnabled] : 388 -> 384
~ _soft_UASpeakSelectionIsEnabled : 272 -> 260
~ -[FUAccessibilityServer isVoiceControlEnabled] : 132 -> 120
~ -[FUAccessibilityServer _handleAccessibilityInterfaceChangedNotification:] : 260 -> 276
~ ___74-[FUAccessibilityServer _handleAccessibilityInterfaceChangedNotification:]_block_invoke : 924 -> 968
~ -[FUAccessibilityServer _handleApplicationAccessibilityChangedNotification:] : 260 -> 276
~ ___76-[FUAccessibilityServer _handleApplicationAccessibilityChangedNotification:]_block_invoke : 732 -> 740
~ -[FUAccessibilityServer listener:didReceiveConnection:withContext:] : 756 -> 792
~ ___67-[FUAccessibilityServer listener:didReceiveConnection:withContext:]_block_invoke : 412 -> 436
~ _getkMADisplayFilterSettingsChangedNotificationSymbolLoc : 272 -> 264
~ _MediaAccessibilityLibrary : 304 -> 284
~ _MediaAccessibilityLibraryCore : 188 -> 180
~ ___MediaAccessibilityLibraryCore_block_invoke : 152 -> 148
~ _libUAPreferencesLibraryCore : 284 -> 276
~ ___libUAPreferencesLibraryCore_block_invoke : 180 -> 176
~ _getUADomainScreenPolarityDidChangeNotificationSymbolLoc : 272 -> 264
~ _getUADomainKeyboardAccessSettingsDidChangeNotificationSymbolLoc : 272 -> 264
~ _getUADomainAssistiveControlSettingsDidChangeNotificationSymbolLoc : 272 -> 264
~ _getUADomainVoiceOverSettingsDidChangeNotificationSymbolLoc : 272 -> 264
~ _getUADomainSpeechSettingsDidChangeNotificationSymbolLoc : 272 -> 264
~ _getNXOpenEventStatusSymbolLoc : 272 -> 264
~ _IOKitLibrary : 304 -> 284
~ _IOKitLibraryCore : 188 -> 180
~ ___IOKitLibraryCore_block_invoke : 152 -> 148
~ _getNXKeyRepeatIntervalSymbolLoc : 272 -> 264
~ _getNXKeyRepeatThresholdSymbolLoc : 272 -> 264
~ _getNXCloseEventStatusSymbolLoc : 272 -> 264
~ _UniversalAccessCoreLibraryCore : 188 -> 180
~ ___UniversalAccessCoreLibraryCore_block_invoke : 152 -> 148
~ _getUAWhiteOnBlackIsEnabledSymbolLoc : 272 -> 264
~ _getUAGrayscaleIsEnabledSymbolLoc : 272 -> 264
~ _getUAKeyboardAccessIsEnabledSymbolLoc : 272 -> 264
~ _getUASwitchControlIsEnabledSymbolLoc : 272 -> 264
~ _getUAVoiceOverIsEnabledSymbolLoc : 272 -> 264
~ _getUASpeakSelectionIsEnabledSymbolLoc : 272 -> 264
~ -[FUApplicationFullScreenSize initWithBundleInfo:applicationDescription:supportsPhone:supportsPad:supportedOrientations:usableDisplaySize:preferSmaller:useTrueDisplaySize:] : 732 -> 660
~ -[FUApplicationFullScreenSize _computeCompatibleSizes] : 13468 -> 13464
~ ___54-[FUApplicationFullScreenSize _computeCompatibleSizes]_block_invoke : 232 -> 248
~ ___CGSizeEqualToSize : 92 -> 88
~ _BSBitmaskIntersects : 60 -> 56
~ -[FUApplicationFullScreenSize _isBackedByRealImage:extension:size:bundle:] : 1092 -> 1080
~ -[FUApplicationFullScreenSize _sanitizedImageNameFromName:withExtension:actualExtension:] : 384 -> 388
~ -[FUApplicationFullScreenSize _preferredImagePathInBundle:baseResourceName:ofType:forMainScene:size:scale:outScale:] : 444 -> 460
~ _SBFModifiedImageNameForName : 264 -> 280
~ -[FUApplicationFullScreenSize _preferredImagePathByScaleInBundle:resourceName:ofType:scale:outScale:] : 736 -> 712
~ _SBFImageNameModifierSuffix : 432 -> 452
~ -[FUApplicationFullScreenSize isValidImageFileExtension:] : 268 -> 244
~ _FUSharedWorkloop : 140 -> 136
~ ___FUSharedWorkloop_block_invoke : 132 -> 140
~ _FUDispatchQueueCreateSerial : 192 -> 216
~ -[FUApplication initWithProcess:initializationParameters:] : 2568 -> 2608
~ ___BSSafeCast : 212 -> 220
~ ___CGSizeEqualToSize : 92 -> 88
~ -[FUApplication dealloc] : 204 -> 200
~ -[FUApplication createInitializationContextForClientProcess:] : 976 -> 1012
~ +[FUApplication createInitializationContextForClientProcessUnderAppKit] : 240 -> 248
~ -[FUApplication createSceneWithOptions:completion:] : 316 -> 340
~ -[FUApplication destroyScenesWithPersistenceIdentifiers:] : 244 -> 260
~ ___57-[FUApplication destroyScenesWithPersistenceIdentifiers:]_block_invoke : 108 -> 116
~ -[FUApplication invalidate] : 380 -> 384
~ ___27-[FUApplication invalidate]_block_invoke : 576 -> 564
~ -[FUApplication _defaultSceneIdentifier] : 136 -> 144
~ -[FUApplication _createSceneWithOptions:completion:] : 4336 -> 4564
~ -[FUApplication _applyClientSettings:toMutableSettings:] : 1580 -> 1532
~ -[FUApplication _applySceneRequestOptions:toTransitionContext:forNewScene:] : 820 -> 776
~ ___52-[FUApplication _createSceneWithOptions:completion:]_block_invoke_2 : 164 -> 172
~ -[FUApplication _destroyScenesWithPersistenceIdentifiers:] : 1560 -> 1576
~ ___58-[FUApplication _destroyScenesWithPersistenceIdentifiers:]_block_invoke_2 : 580 -> 576
~ -[FUApplication _fullScreenSize] : 132 -> 116
~ -[FUApplication _computeLargestCompatibleScreenSizeIfNeeded] : 476 -> 456
~ _BSBitmaskContains : 64 -> 60
~ -[FUApplication _createConfigurationForSceneSettings:withDisplayID:] : 312 -> 328
~ -[FUApplication debugDescription] : 252 -> 264
~ -[FUApplication copyWithZone:] : 28 -> 36
~ -[FUApplication scene:didReceiveActions:] : 1380 -> 1364
~ -[FUApplication scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:] : 704 -> 748
~ -[FUApplication sceneDidInvalidate:] : 260 -> 276
~ -[FUApplication process:stateDidChangeFromState:toState:] : 440 -> 432
~ +[FBSDisplayConfiguration(FuseBoard) fu_configurationWithCGDisplayID:] : 1232 -> 1220
~ ___70+[FBSDisplayConfiguration(FuseBoard) fu_configurationWithCGDisplayID:]_block_invoke : 108 -> 116
~ -[FBSDisplayConfiguration(FuseBoard) fu_copyWithOverrideSize:] : 344 -> 364
~ -[FBSDisplayConfiguration(FuseBoard) fu_displayID] : 92 -> 100
~ -[FBSDisplayConfiguration(FuseBoard) fu_setDisplayID:] : 112 -> 120
~ -[FBSDisplayConfiguration(FuseBoard) fu_isExternal] : 52 -> 48
~ -[FBSDisplayConfiguration(FuseBoard) fu_setExternal:] : 148 -> 156
~ -[FUApplicationSceneComponent initWithScene:] : 296 -> 312
~ -[FUApplicationSceneComponent _settingsDiffActionsForScene:] : 280 -> 284
~ -[FUApplicationSceneComponent _sceneWillInvalidate:] : 184 -> 200
~ -[FUApplicationSceneComponent _performActionsForUIScene:withUpdatedFBSScene:settingsDiff:fromSettings:transitionContext:lifecycleActionType:] : 472 -> 464
~ +[FUCatalystSceneSpecification initialize] : 180 -> 184
~ -[FUCatalystSceneSpecification initialSettingsDiffActions] : 168 -> 184
~ ___BSSafeCast : 212 -> 220
~ -[FUSystemShellService initWithDelegate:appProvider:] : 420 -> 452
~ ___53-[FUSystemShellService initWithDelegate:appProvider:]_block_invoke : 88 -> 96
~ -[FUSystemShellService systemServiceApplicationInfoProvider:] : 120 -> 128
~ -[FUSystemShellService systemService:handleOpenApplicationRequest:withCompletion:] : 644 -> 684
~ -[FUSystemShellService systemService:handleActions:origin:withResult:] : 648 -> 632
~ -[FUSystemShellService systemServicePrepareForExit:andRelaunch:] : 120 -> 116
~ -[FUApplicationSceneSettingsDiffInspector observeKeepsContextsInBackgroundWithBlock:] : 228 -> 236
~ -[FUApplicationSceneSettingsDiffInspector inspectDiff:withContext:] : 168 -> 160
~ -[FUApplicationSceneSettingsDiffInspector _performActionsForUIScene:withUpdatedFBSScene:settingsDiff:fromSettings:transitionContext:lifecycleActionType:] : 452 -> 476
~ +[FUApplicationDataStore storeForApplication:] : 636 -> 664
~ -[FUApplicationDataStore init] : 216 -> 224
~ -[FUApplicationDataStore synchronize] : 320 -> 324
~ -[FUApplicationDataStore scenePersistenceIdentifiers] : 136 -> 144
~ -[FUApplicationDataStore setScenePersistenceIdentifiers:] : 1468 -> 1532
~ -[FUApplicationDataStore addScenePersistenceIdentifier:] : 1176 -> 1248
~ -[FUApplicationDataStore removeScenePersistenceIdentifier:] : 1176 -> 1248
~ -[FUApplicationDataStore encodeWithCoder:] : 268 -> 272
~ -[FUApplicationDataStore initWithCoder:] : 980 -> 996
~ ___BSSafeCast : 212 -> 220
~ -[FUApplicationManager init] : 624 -> 688
~ -[FUApplicationManager applications] : 196 -> 212
~ -[FUApplicationManager applicationForVersionedPID:] : 204 -> 220
~ -[FUApplicationManager applicationsForUser:] : 536 -> 516
~ -[FUApplicationManager _registerApplicationForProcessIdentifier:initializationParameters:] : 984 -> 964
~ -[FUApplicationManager _removeApplicationForProcess:] : 444 -> 432
~ -[FUApplicationManager sceneManager:didReceiveSceneRequestWithOptions:fromProcess:completion:] : 1100 -> 1120
~ ___94-[FUApplicationManager sceneManager:didReceiveSceneRequestWithOptions:fromProcess:completion:]_block_invoke : 868 -> 880
~ -[FUApplicationManager applicationInfoForBundleIdentifier:] : 952 -> 968
~ -[FUApplicationManager applicationInfoForAuditToken:] : 808 -> 812
~ -[FUApplicationManager service:initializeClient:withParameters:] : 1244 -> 1220
~ -[FUApplicationManager destroyScenesWithPersistentIdentifiers:animationType:destroySessions:forClient:completion:] : 812 -> 820
~ -[FUApplicationWatchdogPolicy init] : 412 -> 444
~ -[FUApplicationWatchdogPolicy watchdogPolicyForProcess:eventContext:] : 188 -> 196
~ +[FUApplicationBundleInfo interfaceOrientationForString:] : 328 -> 296
~ -[FUApplicationBundleInfo _loadFromProxy:] : 1484 -> 1460
~ ___42-[FUApplicationBundleInfo _loadFromProxy:]_block_invoke : 316 -> 328
~ _BSBitmaskContains : 64 -> 60
~ -[FUApplicationSceneClientSettingsDiffInspector observePreferredSceneSettingsWithBlock:] : 404 -> 412
~ -[FUApplicationSceneClientSettingsDiffInspector observePreferredStateWithBlock:] : 228 -> 236
~ ___80-[FUApplicationSceneClientSettingsDiffInspector observePreferredStateWithBlock:]_block_invoke : 156 -> 164
~ -[FUApplicationSceneClientSettingsDiffInspector observePreferredSizeWithBlock:] : 228 -> 236
~ ___79-[FUApplicationSceneClientSettingsDiffInspector observePreferredSizeWithBlock:]_block_invoke : 156 -> 164
~ -[FUApplicationSceneClientSettingsDiffInspector observePreferredFullScreenOrientationsWithBlock:] : 228 -> 236
~ ___97-[FUApplicationSceneClientSettingsDiffInspector observePreferredFullScreenOrientationsWithBlock:]_block_invoke : 156 -> 164
~ -[FUApplicationSceneClientSettingsDiffInspector observePreferredDisplayConfigurationWithBlock:] : 324 -> 332
~ -[FUApplicationSceneClientSettingsDiffInspector observePreferredEdgeInsetsWithBlock:] : 228 -> 236
~ ___85-[FUApplicationSceneClientSettingsDiffInspector observePreferredEdgeInsetsWithBlock:]_block_invoke : 156 -> 164
~ -[FUApplicationSceneClientSettingsDiffInspector inspectDiff:forApplication:scene:transitionContext:] : 468 -> 476
~ -[FuseBoard _init] : 672 -> 704
~ ___18-[FuseBoard _init]_block_invoke : 248 -> 256
~ ___18-[FuseBoard _init]_block_invoke_2 : 196 -> 220
~ -[FuseBoard systemService:handleActions:origin:] : 496 -> 480
~ _FUServerInitialize : 116 -> 112
~ ___FUServerInitialize_block_invoke : 80 -> 88
CStrings:
+ "process != ((void*)0)"
- "process != ((void *)0)"

```
