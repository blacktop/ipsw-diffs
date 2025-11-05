## CoreDuetContext

> `/System/Library/PrivateFrameworks/CoreDuetContext.framework/Versions/A/CoreDuetContext`

```diff

-1892.6.3.0.0
-  __TEXT.__text: 0x3955c
-  __TEXT.__auth_stubs: 0x6e0
-  __TEXT.__objc_methlist: 0x2db4
+1892.20.1.0.0
+  __TEXT.__text: 0x399dc
+  __TEXT.__auth_stubs: 0x720
+  __TEXT.__objc_methlist: 0x33c0
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x2628
-  __TEXT.__oslogstring: 0x325b
-  __TEXT.__gcc_except_tab: 0x10ec
+  __TEXT.__cstring: 0x261d
+  __TEXT.__oslogstring: 0x3426
+  __TEXT.__gcc_except_tab: 0x10e0
   __TEXT.__dlopen_cstrs: 0x51
-  __TEXT.__unwind_info: 0xe70
+  __TEXT.__unwind_info: 0xeb8
   __TEXT.__objc_classname: 0x58d
-  __TEXT.__objc_methname: 0x89e8
+  __TEXT.__objc_methname: 0x8abb
   __TEXT.__objc_methtype: 0x1592
   __TEXT.__objc_stubs: 0x5040
   __DATA_CONST.__got: 0x348

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2010
+  __DATA_CONST.__objc_selrefs: 0x2128
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x380
+  __AUTH_CONST.__auth_got: 0x3a0
   __AUTH_CONST.__const: 0x1990
-  __AUTH_CONST.__cfstring: 0x3180
-  __AUTH_CONST.__objc_const: 0x4dc8
+  __AUTH_CONST.__cfstring: 0x31c0
+  __AUTH_CONST.__objc_const: 0x4358
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x1a4
+  __DATA.__objc_ivar: 0x1a8
   __DATA.__data: 0x840
   __DATA.__bss: 0x4b0
   __DATA_DIRTY.__objc_data: 0x780

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 97B8E19B-5264-3857-8B79-71EFED0067AA
-  Functions: 1445
-  Symbols:   3341
-  CStrings:  2618
+  UUID: D1043AB1-F6C2-355D-855E-8E1B2726B8D1
+  Functions: 1544
+  Symbols:   3446
+  CStrings:  2631
 
Symbols:
+ +[_CDClientContext clientInterface].cold.1
+ +[_CDClientContext serverInterface].cold.1
+ +[_CDClientContext userContext].cold.1
+ +[_CDContextMonitorManager initializeKeyPathEventStreamMapping].cold.1
+ +[_CDContextPredictionQueries keyPathForCellQualityPrediction].cold.1
+ +[_CDContextPredictionQueries keyPathForWiFiQualityPrediction].cold.1
+ +[_CDContextQueries keyPathForActiveComplications].cold.1
+ +[_CDContextQueries keyPathForAirplaneModeStatus].cold.1
+ +[_CDContextQueries keyPathForBacklightOnStatus].cold.1
+ +[_CDContextQueries keyPathForBatteryLevel].cold.1
+ +[_CDContextQueries keyPathForCPUUsageLevel].cold.1
+ +[_CDContextQueries keyPathForCallInProgressStatus].cold.1
+ +[_CDContextQueries keyPathForCarConnectedStatus].cold.1
+ +[_CDContextQueries keyPathForCarplayConnectedStatus].cold.1
+ +[_CDContextQueries keyPathForCellConnectionQuality].cold.1
+ +[_CDContextQueries keyPathForDefaultPairedDeviceBatteryLevel].cold.1
+ +[_CDContextQueries keyPathForDefaultPairedDeviceCellQuality].cold.1
+ +[_CDContextQueries keyPathForDefaultPairedDeviceForegroundApp].cold.1
+ +[_CDContextQueries keyPathForDefaultPairedDeviceNearbyStatus].cold.1
+ +[_CDContextQueries keyPathForDefaultPairedDevicePluginStatus].cold.1
+ +[_CDContextQueries keyPathForDefaultPairedDeviceThermalPressureLevel].cold.1
+ +[_CDContextQueries keyPathForDefaultPairedDeviceWiFiWiredQuality].cold.1
+ +[_CDContextQueries keyPathForDeviceAssertionsHeldStatus].cold.1
+ +[_CDContextQueries keyPathForDeviceID].cold.1
+ +[_CDContextQueries keyPathForDeviceLockStatus].cold.1
+ +[_CDContextQueries keyPathForDeviceName].cold.1
+ +[_CDContextQueries keyPathForDisplayOnBeforeFirstUnlockOfTheDayStatus].cold.1
+ +[_CDContextQueries keyPathForDoNotDisturbStatus].cold.1
+ +[_CDContextQueries keyPathForEnergyBudgetRemainingStatus].cold.1
+ +[_CDContextQueries keyPathForFirstWakeupStatus].cold.1
+ +[_CDContextQueries keyPathForForegroundApp].cold.1
+ +[_CDContextQueries keyPathForInUseStatus].cold.1
+ +[_CDContextQueries keyPathForKeybagLockStatus].cold.1
+ +[_CDContextQueries keyPathForLastUseDate].cold.1
+ +[_CDContextQueries keyPathForLowBattery].cold.1
+ +[_CDContextQueries keyPathForLowPowerModeStatus].cold.1
+ +[_CDContextQueries keyPathForMediaPlayingStatus].cold.1
+ +[_CDContextQueries keyPathForMotionState].cold.1
+ +[_CDContextQueries keyPathForNavigationStatus].cold.1
+ +[_CDContextQueries keyPathForNearbyLOIIdentifiers].cold.1
+ +[_CDContextQueries keyPathForNetworkingBudgetRemainingStatus].cold.1
+ +[_CDContextQueries keyPathForNextUserVisibleWakeDate].cold.1
+ +[_CDContextQueries keyPathForPluginStatus].cold.1
+ +[_CDContextQueries keyPathForSiriActiveStatus].cold.1
+ +[_CDContextQueries keyPathForSystemTime].cold.1
+ +[_CDContextQueries keyPathForThermalPressureLevel].cold.1
+ +[_CDContextQueries keyPathForWatchActiveStatus].cold.1
+ +[_CDContextQueries keyPathForWiFiConnectionQuality].cold.1
+ +[_CDContextQueries keyPathForWiFiConnectionSSID].cold.1
+ +[_CDContextQueries keyPathForWiredConnectionQuality].cold.1
+ +[_CDContextQueries keyPathForWorkoutStatus].cold.1
+ +[_CDContextQueries(Alarm) keyPathForCurrentAlarms].cold.1
+ +[_CDContextQueries(Alarm) keyPathForCurrentTimers].cold.1
+ +[_CDContextQueries(Alarm) keyPathForNextAlarm].cold.1
+ +[_CDContextQueries(AppMediaUsage) keyPathForAppMediaUsageDataDictionaries].cold.1
+ +[_CDContextQueries(AppUsage) keyPathForAppRunningDataDictionaries].cold.1
+ +[_CDContextQueries(AppUsage) keyPathForAppUsageDataDictionaries].cold.1
+ +[_CDContextQueries(AppWebUsage) keyPathForAppWebUsageDataDictionaries].cold.1
+ +[_CDContextQueries(Application) keyPathForAppClipLaunch].cold.1
+ +[_CDContextQueries(Application) keyPathForAppDataDictionary].cold.1
+ +[_CDContextQueries(Audio) keyPathForAudioOutputDataDictionary].cold.1
+ +[_CDContextQueries(BatteryState) keyPathForBatteryStateDataDictionary].cold.1
+ +[_CDContextQueries(Bluetooth) keyPathForBluetoothDataDictionary].cold.1
+ +[_CDContextQueries(Calls) keyPathForActiveCall].cold.1
+ +[_CDContextQueries(DoNotDisturb) keyPathForDoNotDisturbStatusDataDictionary].cold.1
+ +[_CDContextQueries(HomeKitAccessory) keyPathForHomeKitAccessoryDataDictionary].cold.1
+ +[_CDContextQueries(HomeKitAppView) keyPathForHomeKitAppViewDataDictionary].cold.1
+ +[_CDContextQueries(HomeKitScene) keyPathForHomeKitSceneDataDictionary].cold.1
+ +[_CDContextQueries(IDSTrafficPolicy) keyPathForDefaultPairedServicesAppearingForeground].cold.1
+ +[_CDContextQueries(IDSTrafficPolicy) keyPathForServicesAppearingForeground].cold.1
+ +[_CDContextQueries(Intents) keyPathForIntentsDataDictionary].cold.1
+ +[_CDContextQueries(Interactions) keyPathForRecentEmails].cold.1
+ +[_CDContextQueries(Interactions) keyPathForRecentMessages].cold.1
+ +[_CDContextQueries(Location) keyPathForCircularLocationRegions].cold.1
+ +[_CDContextQueries(LocationCoordinates) keyPathForLocationCoordinates].cold.1
+ +[_CDContextQueries(MDCS) keyPathForMDCSProxies].cold.1
+ +[_CDContextQueries(NFC) keyPathForNFCTagIdentifiers].cold.1
+ +[_CDContextQueries(NowPlaying) keyPathForNowPlayingDataDictionary].cold.1
+ +[_CDContextQueries(Routine) keyPathForPredictedLocationOfInterestTransitions].cold.1
+ +[_CDContextQueries(SafariSpotlightDonation) keyPathForMostRecentSafariSpotlightDonation].cold.1
+ +[_CDContextQueries(SiriService) keyPathForSiriServiceDataDictionary].cold.1
+ +[_CDContextQueries(Sleep) keyPathForSleepStateDictionary].cold.1
+ +[_CDContextQueries(SunriseSunset) keyPathForSunriseSunsetDataDictionary].cold.1
+ +[_CDContextQueries(UserActivity) keyPathForUserActivityDataDictionary].cold.1
+ +[_CDContextQueries(Workout) keyPathForWorkoutDataDictionary].cold.1
+ +[_CDContextValue supportedContextValueClasses].cold.1
+ +[_CDDevice localDevice].cold.1
+ +[_CDLogging(CDUserContext) mdcsChannel].cold.1
+ +[_CDMDCSContextualPredicate predicates].cold.1
+ +[_CDNetworkContext keyPathForCellConnectionStatus].cold.1
+ +[_CDNetworkContext keyPathForWiFiConnectionStatus].cold.1
+ +[_CDNetworkContext keyPathForWiredConnectionStatus].cold.1
+ +[_CDSystemTimeCallbackScheduler sharedInstance].cold.1
+ +[_CDUserContextQueries keyPathForUserIsArrivingAtHomeStatus].cold.1
+ +[_CDUserContextQueries keyPathForUserIsAsleepStatus].cold.1
+ +[_CDUserContextQueries keyPathForUserIsAtHomeStatus].cold.1
+ +[_CDUserContextQueries keyPathForUserIsAtWorkStatus].cold.1
+ +[_CDUserContextQueries keyPathForUserIsDrivingStatus].cold.1
+ +[_CDUserContextQueries keyPathForUserIsLeavingHomeStatus].cold.1
+ +[_CDUserContextQueries keyPathForUserIsTravelingStatus].cold.1
+ +[_CDUserContextServerClient clientInterface].cold.1
+ +[_CDUserContextServerClient serverInterface].cold.1
+ -[_CDClientContext concurrentRegistrationCallbackQueue]
+ -[_CDClientContext defaultCallbackQueue].cold.1
+ -[_CDClientContext handleContextualChange:info:handler:].cold.2
+ -[_CDClientContext serialRegistrationCallbackQueue]
+ -[_CDClientContext setConcurrentRegistrationCallbackQueue:]
+ -[_CDClientContext setSerialRegistrationCallbackQueue:]
+ -[_CDContextualKeyPath isMultiDeviceKeyPath].cold.1
+ -[_CDMDCSContextualPredicate initWithCoder:].cold.1
+ GCC_except_table107
+ GCC_except_table112
+ GCC_except_table123
+ GCC_except_table131
+ GCC_except_table139
+ GCC_except_table141
+ GCC_except_table142
+ GCC_except_table147
+ GCC_except_table155
+ GCC_except_table161
+ GCC_except_table168
+ OBJC_IVAR_$__CDClientContext._concurrentRegistrationCallbackQueue
+ OBJC_IVAR_$__CDClientContext._serialRegistrationCallbackQueue
+ __108-[_CDClientContext addObjects:andRemoveObjects:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.177
+ __108-[_CDClientContext addObjects:andRemoveObjects:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.178
+ __108-[_CDClientContext addObjects:andRemoveObjects:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.179
+ __111-[_CDClientContext removeObjectsMatchingPredicate:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.169
+ __111-[_CDClientContext removeObjectsMatchingPredicate:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.170
+ __111-[_CDClientContext removeObjectsMatchingPredicate:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.171
+ __37-[_CDClientContext registerCallback:]_block_invoke.152
+ __37-[_CDClientContext registerCallback:]_block_invoke_2.153
+ __37-[_CDClientContext registerCallback:]_block_invoke_2.153.cold.1
+ __38-[_CDClientContext evaluatePredicate:]_block_invoke.154
+ __43-[_CDClientContext subscribeToEventStreams]_block_invoke.118
+ __43-[_CDClientContext subscribeToEventStreams]_block_invoke.120
+ __47-[_CDUserContextServerClient registerCallback:]_block_invoke.137
+ __47-[_CDUserContextServerClient registerCallback:]_block_invoke.137.cold.1
+ __47-[_CDUserContextServerClient registerCallback:]_block_invoke.139
+ __47-[_CDUserContextServerClient registerCallback:]_block_invoke.139.cold.1
+ __47-[_CDUserContextServerClient registerCallback:]_block_invoke.144
+ __47-[_CDUserContextServerClient registerCallback:]_block_invoke.144.cold.1
+ __52-[_CDClientContext hasKnowledgeOfContextualKeyPath:]_block_invoke.134
+ __54-[_CDUserContextServerClient _valuesForPaths:handler:]_block_invoke.166
+ __56-[_CDClientContext handleContextualChange:info:handler:]_block_invoke.158
+ __66-[_CDClientContext valuesForKeyPaths:inContextsMatchingPredicate:]_block_invoke.180
+ __68-[_CDClientContext setObject:lastModifiedDate:forContextualKeyPath:]_block_invoke.190
+ __69-[_CDUserContextServerClient handlePreviouslyFiredRegistration:info:]_block_invoke.125.cold.1
+ __69-[_CDUserContextServerClient handlePreviouslyFiredRegistration:info:]_block_invoke.128
+ __79-[_CDClientContext valuesForKeyPaths:synchronous:responseQueue:withCompletion:]_block_invoke.183
+ __79-[_CDClientContext valuesForKeyPaths:synchronous:responseQueue:withCompletion:]_block_invoke.184
+ __79-[_CDUserContextServerClient performRegistrationCallbackWithRegistration:info:]_block_invoke.147
+ __79-[_CDUserContextServerClient performRegistrationCallbackWithRegistration:info:]_block_invoke.147.cold.1
+ __79-[_CDUserContextServerClient performRegistrationCallbackWithRegistration:info:]_block_invoke.150
+ __88-[_CDClientContext objectForContextualKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.137
+ __88-[_CDClientContext objectForContextualKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.141
+ __89-[_CDClientContext addObjects:toArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.164
+ __89-[_CDClientContext addObjects:toArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.165
+ __92-[_CDClientContext setObject:forContextualKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.159
+ __92-[_CDClientContext setObject:forContextualKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.161
+ __94-[_CDClientContext removeObjects:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.166
+ __94-[_CDClientContext removeObjects:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.167
+ __94-[_CDClientContext removeObjects:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.168
+ __98-[_CDClientContext lastModifiedDateForContextualKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.144
+ __CDProcessNameForXPCConnection
+ ___54-[_CDUserContextServerClient _valuesForPaths:handler:]_block_invoke_3
+ ___CDCLIENTCONTEXT_IS_CALLING_OUT_TO_CLIENT_BLOCK__
+ ___CDCLIENTCONTEXT_IS_CALLING_OUT_TO_DEPRECATED_CLIENT_BLOCK__
+ ___block_descriptor_72_e8_32s40s48s56bs64bs_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56b64b
+ __block_literal_global.116
+ __block_literal_global.127
+ __block_literal_global.130
+ __block_literal_global.141
+ __block_literal_global.149
+ __block_literal_global.163
+ __cdcontextstore_signpost_deprecated_api
+ _cd_dispatch_async_xpc
+ _dispatch_block_create
- -[_CDClientContext objectForContextualKeyPath:synchronous:responseQueue:withCompletion:].cold.1
- -[_CDClientContext registrationCallbackQueue]
- -[_CDClientContext setRegistrationCallbackQueue:]
- -[_CDContextualPredicate evaluateWithState:previousValue:].cold.3
- GCC_except_table103
- GCC_except_table108
- GCC_except_table120
- GCC_except_table128
- GCC_except_table136
- GCC_except_table137
- GCC_except_table138
- GCC_except_table144
- GCC_except_table151
- GCC_except_table157
- GCC_except_table164
- OBJC_IVAR_$__CDClientContext._registrationCallbackQueue
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- __108-[_CDClientContext addObjects:andRemoveObjects:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.171
- __108-[_CDClientContext addObjects:andRemoveObjects:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.173
- __108-[_CDClientContext addObjects:andRemoveObjects:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.174
- __111-[_CDClientContext removeObjectsMatchingPredicate:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.163
- __111-[_CDClientContext removeObjectsMatchingPredicate:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.164
- __111-[_CDClientContext removeObjectsMatchingPredicate:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.165
- __37-[_CDClientContext registerCallback:]_block_invoke.151
- __37-[_CDClientContext registerCallback:]_block_invoke_2.152
- __37-[_CDClientContext registerCallback:]_block_invoke_2.152.cold.1
- __38-[_CDClientContext evaluatePredicate:]_block_invoke.153
- __43-[_CDClientContext subscribeToEventStreams]_block_invoke.117
- __43-[_CDClientContext subscribeToEventStreams]_block_invoke.119
- __47-[_CDUserContextServerClient registerCallback:]_block_invoke.134
- __47-[_CDUserContextServerClient registerCallback:]_block_invoke.134.cold.1
- __47-[_CDUserContextServerClient registerCallback:]_block_invoke.141
- __47-[_CDUserContextServerClient registerCallback:]_block_invoke.141.cold.1
- __47-[_CDUserContextServerClient registerCallback:]_block_invoke_2.cold.1
- __52-[_CDClientContext hasKnowledgeOfContextualKeyPath:]_block_invoke.133
- __54-[_CDUserContextServerClient _valuesForPaths:handler:]_block_invoke.162
- __66-[_CDClientContext valuesForKeyPaths:inContextsMatchingPredicate:]_block_invoke.175
- __68-[_CDClientContext setObject:lastModifiedDate:forContextualKeyPath:]_block_invoke.184
- __69-[_CDUserContextServerClient handlePreviouslyFiredRegistration:info:]_block_invoke_2.126
- __69-[_CDUserContextServerClient handlePreviouslyFiredRegistration:info:]_block_invoke_2.cold.1
- __79-[_CDClientContext valuesForKeyPaths:synchronous:responseQueue:withCompletion:]_block_invoke.178
- __79-[_CDClientContext valuesForKeyPaths:synchronous:responseQueue:withCompletion:]_block_invoke.179
- __79-[_CDUserContextServerClient performRegistrationCallbackWithRegistration:info:]_block_invoke.146
- __79-[_CDUserContextServerClient performRegistrationCallbackWithRegistration:info:]_block_invoke_2.cold.1
- __88-[_CDClientContext objectForContextualKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.135
- __88-[_CDClientContext objectForContextualKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.139
- __89-[_CDClientContext addObjects:toArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.158
- __89-[_CDClientContext addObjects:toArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.159
- __92-[_CDClientContext setObject:forContextualKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.154
- __92-[_CDClientContext setObject:forContextualKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.155
- __94-[_CDClientContext removeObjects:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.160
- __94-[_CDClientContext removeObjects:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.161
- __94-[_CDClientContext removeObjects:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.162
- __98-[_CDClientContext lastModifiedDateForContextualKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.143
- ___47-[_CDUserContextServerClient registerCallback:]_block_invoke_2
- ___79-[_CDUserContextServerClient performRegistrationCallbackWithRegistration:info:]_block_invoke_2
- ___block_descriptor_80_e8_32s40s48s56s64bs72bs_e5_v8?0l
- ___copy_helper_block_e8_32s40s48s56s64b72b
- __block_literal_global.115
- __block_literal_global.124
- __block_literal_global.129
- __block_literal_global.138
- __block_literal_global.143
- __block_literal_global.145
- __block_literal_global.159
CStrings:
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreDuet/CDUserContext/CDUserContext/_CDUserContextServerClient.m:1104"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreDuet/CDUserContext/CDUserContext/_CDUserContextServerClient.m:156"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreDuet/CDUserContext/CDUserContext/_CDUserContextServerClient.m:343"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreDuet/CDUserContext/CDUserContext/_CDUserContextService.m:540"
+ "CoreDuet: ClientContext activateDevices:remoteUserContextProxySourceDeviceUUID:"
+ "CoreDuet: ClientContext addObjects:andRemoveObjects:fromArrayAtKeyPath:"
+ "CoreDuet: ClientContext addObjects:andRemoveObjects:fromArrayAtKeyPath:responseQueue:withCompletion:"
+ "CoreDuet: ClientContext addObjects:toArrayAtKeyPath:"
+ "CoreDuet: ClientContext addObjects:toArrayAtKeyPath:responseQueue:withCompletion:"
+ "CoreDuet: ClientContext deactivateDevices:remoteUserContextProxySourceDeviceUUID:"
+ "CoreDuet: ClientContext deregisterCallback:"
+ "CoreDuet: ClientContext evaluatePredicate:"
+ "CoreDuet: ClientContext handleContextualChange:info:handler:"
+ "CoreDuet: ClientContext handleRegistrationCompleted:handler:"
+ "CoreDuet: ClientContext lastModifiedDateForContextualKeyPath:"
+ "CoreDuet: ClientContext lastModifiedDateForContextualKeyPath:responseQueue:withCompletion:"
+ "CoreDuet: ClientContext objectForContextualKeyPath:"
+ "CoreDuet: ClientContext objectForContextualKeyPath:responseQueue:withCompletion:"
+ "CoreDuet: ClientContext re-register"
+ "CoreDuet: ClientContext registerCallback:"
+ "CoreDuet: ClientContext removeObjects:fromArrayAtKeyPath:"
+ "CoreDuet: ClientContext removeObjects:fromArrayAtKeyPath:responseQueue:withCompletion:"
+ "CoreDuet: ClientContext removeObjectsMatchingPredicate:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:"
+ "CoreDuet: ClientContext setObject:forContextualKeyPath:"
+ "CoreDuet: ClientContext setObject:forContextualKeyPath:responseQueue:withCompletion:"
+ "CoreDuet: ClientContext setObject:lastModifiedDate:forContextualKeyPath:"
+ "CoreDuet: ClientContext setupXPCConnection:"
+ "CoreDuet: ClientContext valuesForKeyPaths:"
+ "CoreDuet: ClientContext valuesForKeyPaths:inContextsMatchingPredicate:"
+ "CoreDuet: ClientContext valuesForKeyPaths:responseQueue:withCompletion:"
+ "CoreDuet: ContextStore Callback"
+ "CoreDuet: ContextStore Deregister"
+ "CoreDuet: ContextStore Region State Change"
+ "CoreDuet: ContextStore Register"
+ "CoreDuet: ContextStore com.apple.alarm handler"
+ "CoreDuet: ContextStore setObject:forContextualKeyPath:"
+ "Dispatching call to deprecated registration callback for %@, this may lead to priority problems. Switch to non-deprecated _CDContextualChangeRegistration APIs."
+ "Dispatching call to informative registration callback for %@"
+ "Fetching uncached value for %@"
+ "Sending fired registration %@ to %{public}@"
+ "Sending previously fired registration %@ to %{public}@"
+ "Sending registration completed for registration %@ to %{public}@"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_concurrentRegistrationCallbackQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_serialRegistrationCallbackQueue"
+ "_CDContextualChangeRegistration.callback"
+ "_concurrentRegistrationCallbackQueue"
+ "_serialRegistrationCallbackQueue"
+ "com.apple.CoreDuetContext.clientBlock"
+ "com.apple.CoreDuetContext.dispatchingCallback"
+ "com.apple.cdclientcontext.concurrentRegistrationCallbackQueue"
+ "com.apple.cdclientcontext.serialRegistrationCallbackQueue"
+ "com.apple.coreduet"
+ "concurrentRegistrationCallbackQueue"
+ "contextstored.client.activateMonitorQueue [%@]"
+ "contextstored.client.queue [%@]"
+ "serialRegistrationCallbackQueue"
+ "setConcurrentRegistrationCallbackQueue:"
+ "setSerialRegistrationCallbackQueue:"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/CDUserContext/CDUserContext/_CDInMemoryContext.m:651"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/CDUserContext/CDUserContext/_CDUserContextServerClient.m:1098"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/CDUserContext/CDUserContext/_CDUserContextServerClient.m:155"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/CDUserContext/CDUserContext/_CDUserContextServerClient.m:342"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/CDUserContext/CDUserContext/_CDUserContextService.m:540"
- "Duet: ClientContext activateDevices:remoteUserContextProxySourceDeviceUUID:"
- "Duet: ClientContext addObjects:andRemoveObjects:fromArrayAtKeyPath:"
- "Duet: ClientContext addObjects:andRemoveObjects:fromArrayAtKeyPath:responseQueue:withCompletion:"
- "Duet: ClientContext addObjects:toArrayAtKeyPath:"
- "Duet: ClientContext addObjects:toArrayAtKeyPath:responseQueue:withCompletion:"
- "Duet: ClientContext deactivateDevices:remoteUserContextProxySourceDeviceUUID:"
- "Duet: ClientContext deregisterCallback:"
- "Duet: ClientContext evaluatePredicate:"
- "Duet: ClientContext handleContextualChange:info:handler:"
- "Duet: ClientContext handleRegistrationCompleted:handler:"
- "Duet: ClientContext lastModifiedDateForContextualKeyPath:"
- "Duet: ClientContext lastModifiedDateForContextualKeyPath:responseQueue:withCompletion:"
- "Duet: ClientContext objectForContextualKeyPath:"
- "Duet: ClientContext objectForContextualKeyPath:responseQueue:withCompletion:"
- "Duet: ClientContext re-register"
- "Duet: ClientContext registerCallback:"
- "Duet: ClientContext removeObjects:fromArrayAtKeyPath:"
- "Duet: ClientContext removeObjects:fromArrayAtKeyPath:responseQueue:withCompletion:"
- "Duet: ClientContext removeObjectsMatchingPredicate:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:"
- "Duet: ClientContext setObject:forContextualKeyPath:"
- "Duet: ClientContext setObject:forContextualKeyPath:responseQueue:withCompletion:"
- "Duet: ClientContext setObject:lastModifiedDate:forContextualKeyPath:"
- "Duet: ClientContext setupXPCConnection:"
- "Duet: ClientContext valuesForKeyPaths:"
- "Duet: ClientContext valuesForKeyPaths:inContextsMatchingPredicate:"
- "Duet: ClientContext valuesForKeyPaths:responseQueue:withCompletion:"
- "Duet: ContextStore Callback"
- "Duet: ContextStore Deregister"
- "Duet: ContextStore Region State Change"
- "Duet: ContextStore Register"
- "Duet: ContextStore com.apple.alarm handler"
- "Duet: ContextStore setObject:forContextualKeyPath:"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_registrationCallbackQueue"
- "Uncached value for %@"
- "Unexpected NSCompoundPredicateType after already checking (%@)"
- "_registrationCallbackQueue"
- "client"
- "com.apple.cdclientcontext.registrationCallbackQueue"
- "com.apple.coreduet.context"
- "com.apple.coreduetd.contextserverclient.activateMonitorQueue"
- "com.apple.coreduetd.service.client.workQueue"
- "registrationCallbackQueue"
- "setRegistrationCallbackQueue:"

```
