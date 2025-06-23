## TelephonyUtilities

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`

```diff

-1562.100.3.2.4
-  __TEXT.__text: 0x168f0c
-  __TEXT.__auth_stubs: 0x2350
-  __TEXT.__objc_methlist: 0x19e50
-  __TEXT.__cstring: 0x12de8
-  __TEXT.__const: 0x1034
-  __TEXT.__oslogstring: 0x11cf2
-  __TEXT.__gcc_except_tab: 0x1830
+1566.100.4.0.0
+  __TEXT.__text: 0x16a8c8
+  __TEXT.__auth_stubs: 0x2360
+  __TEXT.__objc_methlist: 0x19fc8
+  __TEXT.__cstring: 0x13028
+  __TEXT.__const: 0x1044
+  __TEXT.__oslogstring: 0x11f52
+  __TEXT.__gcc_except_tab: 0x18e0
   __TEXT.__ustring: 0xde
   __TEXT.__dlopen_cstrs: 0x8df
   __TEXT.__constg_swiftt: 0x578

   __TEXT.__swift_as_ret: 0x84
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5920
+  __TEXT.__unwind_info: 0x5968
   __TEXT.__eh_frame: 0x1340
   __TEXT.__objc_classname: 0x2705
-  __TEXT.__objc_methname: 0x3b5aa
-  __TEXT.__objc_methtype: 0x7e54
-  __TEXT.__objc_stubs: 0x207a0
-  __DATA_CONST.__got: 0xe48
-  __DATA_CONST.__const: 0x35d0
+  __TEXT.__objc_methname: 0x3ba83
+  __TEXT.__objc_methtype: 0x7e8e
+  __TEXT.__objc_stubs: 0x20a20
+  __DATA_CONST.__got: 0xe50
+  __DATA_CONST.__const: 0x35a8
   __DATA_CONST.__objc_classlist: 0x828
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x408
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xad98
+  __DATA_CONST.__objc_selrefs: 0xae50
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x6a8
-  __DATA_CONST.__objc_arraydata: 0x6a8
-  __AUTH_CONST.__auth_got: 0x11b8
-  __AUTH_CONST.__const: 0x31f0
-  __AUTH_CONST.__cfstring: 0x11a40
-  __AUTH_CONST.__objc_const: 0x27e58
+  __DATA_CONST.__objc_arraydata: 0x6f8
+  __AUTH_CONST.__auth_got: 0x11c0
+  __AUTH_CONST.__const: 0x3090
+  __AUTH_CONST.__cfstring: 0x11b20
+  __AUTH_CONST.__objc_const: 0x27f68
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH.__objc_data: 0x2738
-  __AUTH.__data: 0x5d8
-  __DATA.__objc_ivar: 0x17c4
-  __DATA.__data: 0x3300
-  __DATA.__bss: 0x1910
+  __AUTH.__data: 0x5e8
+  __DATA.__objc_ivar: 0x17cc
+  __DATA.__data: 0x3320
+  __DATA.__bss: 0x1890
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x2b20
   __DATA_DIRTY.__data: 0x30

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1A3FBB6E-A0AF-3F52-82F9-6EADA03F4A5F
-  Functions: 9934
-  Symbols:   29737
-  CStrings:  16249
+  UUID: BE282E53-BE34-309F-81CC-DFE892566212
+  Functions: 9957
+  Symbols:   29779
+  CStrings:  16315
 
Symbols:
+ -[TUCall configurationProvider]
+ -[TUCallServicesInterface fetchRoutesAsyncForRouteController:completionHandler:]
+ -[TUConfigurationProvider isCallRecordingEnabled]
+ -[TUConfigurationProvider isHoldAssistAvailable]
+ -[TUConfigurationProvider isHoldAssistDetectionEnabled]
+ -[TUConfigurationProvider isSpamFilterEnabledForFaceTime]
+ -[TUConfigurationProvider setCallRecordingEnabled:]
+ -[TUConfigurationProvider setHoldAssistDetectionEnabled:]
+ -[TUConfigurationProvider setSpamFilterEnabledForFaceTime:]
+ -[TUConversationActivity initWithCreationRequest:bundleIdentifier:systemActivity:requiresParticipantTranslation:]
+ -[TUConversationActivity requiresParticipantTranslation]
+ -[TUConversationActivity setRequiresParticipantTranslation:]
+ -[TUConversationManager createActivitySession:onConversation:options:]
+ -[TUConversationManagerXPCClient createActivitySession:onConversation:options:]
+ -[TUCoreTelephonyClient(TTY) isRTTRelaySupportedForSubscription:]
+ -[TUCoreTelephonyClient(TTY) isRTTRelaySupportedForSubscriptionUUID:]
+ -[TUFeatureFlags phoneClassicNewFavoritesEnabled]
+ -[TUFeatureFlags sharePlayInCallsForRelayEnabled]
+ -[TURouteController fetchRoutesWithCompletionHandler:]
+ -[TUSenderIdentityClient(TTY) isRTTRelaySupportedForSenderIdentityUUID:]
+ -[TUSmartHoldingSession initWithUUID:state:events:requiresUserAttentionReason:hostedOnCurrentDevice:]
+ -[TUSmartHoldingSession isHostedOnCurrentDevice]
+ -[TUUserConfiguration isCallRecordingEnabled]
+ -[TUUserConfiguration isHoldAssistDetectionEnabled]
+ -[TUUserConfiguration isSpamFilterEnabledForFaceTime]
+ -[TUUserConfiguration setCallRecordingEnabled:]
+ -[TUUserConfiguration setHoldAssistDetectionEnabled:]
+ -[TUUserConfiguration setSpamFilterEnabledForFaceTime:]
+ GCC_except_table148
+ GCC_except_table150
+ GCC_except_table153
+ GCC_except_table156
+ GCC_except_table159
+ GCC_except_table162
+ GCC_except_table165
+ GCC_except_table59
+ GCC_except_table78
+ _OBJC_IVAR_$_TUConversationActivity._requiresParticipantTranslation
+ _OBJC_IVAR_$_TUSmartHoldingSession._hostedOnCurrentDevice
+ _TUActionScreenUnknownCallers
+ _TUCallFilteringPreferencesFaceTimeSpamFilterDisabledKey
+ _TUHoldAssistDetectionEnabledKey
+ __OBJC_$_CLASS_PROP_LIST_TUFeatureFlags.661
+ __OBJC_$_PROP_LIST_TUFeatureFlags.665
+ ___69-[TUCallHistoryController callHistoryManagerRecentCallsDispatchBlock]_block_invoke.64
+ ___78-[TUCallHistoryController callHistoryManagerLoadOlderRecentCallsDispatchBlock]_block_invoke.66
+ ___79-[TUConversationManagerXPCClient createActivitySession:onConversation:options:]_block_invoke
+ ___79-[TUConversationManagerXPCClient createActivitySession:onConversation:options:]_block_invoke.cold.1
+ ___83-[TUCall initWithUniqueProxyIdentifier:endpointOnCurrentDevice:notificationCenter:]_block_invoke.263
+ ___83-[TUCall initWithUniqueProxyIdentifier:endpointOnCurrentDevice:notificationCenter:]_block_invoke_2.266
+ ___block_literal_global.118
+ ___block_literal_global.120
+ ___block_literal_global.122
+ ___block_literal_global.156
+ ___block_literal_global.181
+ ___block_literal_global.187
+ ___block_literal_global.193
+ ___block_literal_global.1990
+ ___block_literal_global.1996
+ ___block_literal_global.232
+ ___block_literal_global.252
+ ___block_literal_global.265
+ ___block_literal_global.268
+ ___block_literal_global.271
+ ___block_literal_global.333
+ ___block_literal_global.370
+ ___block_literal_global.375
+ ___block_literal_global.380
+ ___getkCHCoalescingStrategyCollapseIfEqualContactsSymbolLoc_block_invoke
+ ___getkCHCoalescingStrategyCollapseIfEqualSymbolLoc_block_invoke
+ ___getkCHCoalescingStrategyFaceTimeRecentsSymbolLoc_block_invoke
+ ___getkCHCoalescingStrategyRecentsSymbolLoc_block_invoke
+ ___getkCHLimitMediaTypeKeySymbolLoc_block_invoke
+ ___getkCHLimitServiceProviderKeySymbolLoc_block_invoke
+ ___getkCHLimitTTYTypeKeySymbolLoc_block_invoke
+ _defaultAppRelayTelephonySettingUserDefaultForPad
+ _getkCHCoalescingStrategyCollapseIfEqualContactsSymbolLoc.ptr
+ _getkCHCoalescingStrategyCollapseIfEqualSymbolLoc.ptr
+ _getkCHCoalescingStrategyFaceTimeRecentsSymbolLoc.ptr
+ _getkCHCoalescingStrategyRecents
+ _getkCHCoalescingStrategyRecents.cold.1
+ _getkCHCoalescingStrategyRecentsSymbolLoc.ptr
+ _getkCHLimitMediaTypeKeySymbolLoc.ptr
+ _getkCHLimitServiceProviderKeySymbolLoc.ptr
+ _getkCHLimitTTYTypeKeySymbolLoc.ptr
+ _getkCHServiceProviderFaceTime
+ _getkCHServiceProviderFaceTime.cold.1
+ _objc_msgSend$callExperiencePhoneAppEnabled
+ _objc_msgSend$configurationProvider
+ _objc_msgSend$createActivitySession:onConversation:options:
+ _objc_msgSend$createActivitySession:onConversationWithUUID:options:
+ _objc_msgSend$fetchRoutesAsyncForRouteController:completionHandler:
+ _objc_msgSend$getLocalRouteControllerRoutes:
+ _objc_msgSend$getPairedHostDeviceRouteControllerRoutes:
+ _objc_msgSend$initWithCreationRequest:bundleIdentifier:systemActivity:requiresParticipantTranslation:
+ _objc_msgSend$isCallRecordingAvailable
+ _objc_msgSend$isCallRecordingEnabled
+ _objc_msgSend$isHoldAssistAvailable
+ _objc_msgSend$isHoldAssistDetectionEnabled
+ _objc_msgSend$isRTTRelaySupportedForSubscription:
+ _objc_msgSend$isRTTRelaySupportedForSubscriptionUUID:
+ _objc_msgSend$isSpamFilterEnabledForFaceTime
+ _objc_msgSend$relayIsSupported
+ _objc_msgSend$relayIsSupportedForContext:
+ _objc_msgSend$requiresParticipantTranslation
+ _objc_msgSend$setCallRecordingEnabled:
+ _objc_msgSend$setHoldAssistDetectionEnabled:
+ _objc_msgSend$setRequiresParticipantTranslation:
+ _objc_msgSend$setSpamFilterEnabledForFaceTime:
- -[TUCallHistoryController _callHistoryCoalescingStrategyForCoalescingStrategy:].cold.4
- -[TUCallHistoryController _updateCallHistoryManagerUsingCurrentOptions].cold.5
- -[TUConversationManagerXPCClient createActivitySession:onConversation:]
- -[TUSmartHoldingSession initWithUUID:state:events:requiresUserAttentionReason:]
- GCC_except_table147
- GCC_except_table149
- GCC_except_table152
- GCC_except_table155
- GCC_except_table158
- GCC_except_table161
- GCC_except_table76
- __OBJC_$_CLASS_PROP_LIST_TUFeatureFlags.655
- __OBJC_$_PROP_LIST_TUFeatureFlags.659
- ___69-[TUCallHistoryController callHistoryManagerRecentCallsDispatchBlock]_block_invoke.61
- ___69-[TUCallHistoryController callHistoryManagerRecentCallsDispatchBlock]_block_invoke.71
- ___69-[TUCallHistoryController callHistoryManagerRecentCallsDispatchBlock]_block_invoke.cold.1
- ___71-[TUCallHistoryController _updateCallHistoryManagerUsingCurrentOptions]_block_invoke
- ___71-[TUCallHistoryController _updateCallHistoryManagerUsingCurrentOptions]_block_invoke_2
- ___71-[TUCallHistoryController _updateCallHistoryManagerUsingCurrentOptions]_block_invoke_3
- ___71-[TUCallHistoryController _updateCallHistoryManagerUsingCurrentOptions]_block_invoke_4
- ___71-[TUCallHistoryController _updateCallHistoryManagerUsingCurrentOptions]_block_invoke_5
- ___71-[TUConversationManagerXPCClient createActivitySession:onConversation:]_block_invoke
- ___71-[TUConversationManagerXPCClient createActivitySession:onConversation:]_block_invoke.cold.1
- ___72-[TUCallHistoryController callHistoryManagerInitializationDispatchBlock]_block_invoke.cold.1
- ___72-[TUCallHistoryController callHistoryManagerInitializationDispatchBlock]_block_invoke_2
- ___78-[TUCallHistoryController callHistoryManagerLoadOlderRecentCallsDispatchBlock]_block_invoke.73
- ___78-[TUCallHistoryController callHistoryManagerLoadOlderRecentCallsDispatchBlock]_block_invoke.76
- ___78-[TUCallHistoryController callHistoryManagerLoadOlderRecentCallsDispatchBlock]_block_invoke.cold.1
- ___79-[TUCallHistoryController _callHistoryCoalescingStrategyForCoalescingStrategy:]_block_invoke
- ___79-[TUCallHistoryController _callHistoryCoalescingStrategyForCoalescingStrategy:]_block_invoke_2
- ___79-[TUCallHistoryController _callHistoryCoalescingStrategyForCoalescingStrategy:]_block_invoke_3
- ___79-[TUCallHistoryController _callHistoryCoalescingStrategyForCoalescingStrategy:]_block_invoke_4
- ___83-[TUCall initWithUniqueProxyIdentifier:endpointOnCurrentDevice:notificationCenter:]_block_invoke_4
- ___block_literal_global.117
- ___block_literal_global.177
- ___block_literal_global.183
- ___block_literal_global.189
- ___block_literal_global.1975
- ___block_literal_global.1981
- ___block_literal_global.230
- ___block_literal_global.248
- ___block_literal_global.260
- ___block_literal_global.330
- ___block_literal_global.367
- ___block_literal_global.372
- ___block_literal_global.377
- ___block_literal_global.75
- ___block_literal_global.98
- __callHistoryCoalescingStrategyForCoalescingStrategy:._kCHCoalescingStrategyCollapseIfEqual
- __callHistoryCoalescingStrategyForCoalescingStrategy:._kCHCoalescingStrategyCollapseIfEqualContacts
- __callHistoryCoalescingStrategyForCoalescingStrategy:._kCHCoalescingStrategyFaceTimeRecents
- __callHistoryCoalescingStrategyForCoalescingStrategy:._kCHCoalescingStrategyRecents
- __callHistoryCoalescingStrategyForCoalescingStrategy:._pred__kCHCoalescingStrategyCollapseIfEqual
- __callHistoryCoalescingStrategyForCoalescingStrategy:._pred__kCHCoalescingStrategyCollapseIfEqualContacts
- __callHistoryCoalescingStrategyForCoalescingStrategy:._pred__kCHCoalescingStrategyFaceTimeRecents
- __callHistoryCoalescingStrategyForCoalescingStrategy:._pred__kCHCoalescingStrategyRecents
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_TelephonyUtilities
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_TelephonyUtilities
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_TelephonyUtilities
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_TelephonyUtilities
- __updateCallHistoryManagerUsingCurrentOptions._kCHLimitMediaTypeKey
- __updateCallHistoryManagerUsingCurrentOptions._kCHLimitServiceProviderKey
- __updateCallHistoryManagerUsingCurrentOptions._kCHLimitTTYTypeKey
- __updateCallHistoryManagerUsingCurrentOptions._kCHServiceProviderFaceTime
- __updateCallHistoryManagerUsingCurrentOptions._kCHServiceProviderTelephony
- __updateCallHistoryManagerUsingCurrentOptions._pred__kCHLimitMediaTypeKey
- __updateCallHistoryManagerUsingCurrentOptions._pred__kCHLimitServiceProviderKey
- __updateCallHistoryManagerUsingCurrentOptions._pred__kCHLimitTTYTypeKey
- __updateCallHistoryManagerUsingCurrentOptions._pred__kCHServiceProviderFaceTime
- __updateCallHistoryManagerUsingCurrentOptions._pred__kCHServiceProviderTelephony
- _defaultAppRelayTelephonySettingUserDefault
- _gSharedCallHistoryInstance_block_invoke._kCHCoalescingStrategyRecents
- _gSharedCallHistoryInstance_block_invoke._pred__kCHCoalescingStrategyRecents
- _gSharedCallHistoryInstance_block_invoke_2._kCHServiceProviderFaceTime
- _gSharedCallHistoryInstance_block_invoke_2._pred__kCHServiceProviderFaceTime
- _gSharedCallHistoryInstance_block_invoke_3._kCHServiceProviderFaceTime
- _gSharedCallHistoryInstance_block_invoke_3._pred__kCHServiceProviderFaceTime
- _objc_msgSend$createActivitySession:onConversation:
- _objc_msgSend$createActivitySession:onConversationWithUUID:
CStrings:
+ " hostedOnCurrentDevice=%i"
+ " rC=%d"
+ " self.requiresParticipantTranslation=%d"
+ "%@ isCallRecordingEnabled called"
+ "%@ isHoldAssistDetectionEnabled called"
+ "%@ isSpamFilterEnabledForFaceTime called"
+ "%@ setCallRecordingEnabled called %d"
+ "%@ setHoldAssistDetectionEnabled called %d"
+ "%@ setSpamFilterEnabledForFaceTime called %d"
+ "@52@0:8@16Q24@32Q40B48"
+ "Default is not set but relay/thumper is enabled, AND we have PhoneApp, so returning TUDefaultAppRelayTelephonySettingNotApplicable"
+ "Default is not set but relay/thumper is enabled, also NO PhoneApp, so returning TUDefaultAppRelayTelephonySettingCallsFromIPhone"
+ "HoldAssistDetectionEnabled"
+ "NSString *getkCHCoalescingStrategyCollapseIfEqual(void)"
+ "NSString *getkCHCoalescingStrategyCollapseIfEqualContacts(void)"
+ "NSString *getkCHCoalescingStrategyFaceTimeRecents(void)"
+ "NSString *getkCHCoalescingStrategyRecents(void)"
+ "NSString *getkCHLimitMediaTypeKey(void)"
+ "NSString *getkCHLimitServiceProviderKey(void)"
+ "NSString *getkCHLimitTTYTypeKey(void)"
+ "PhoneClassicNewFavorites"
+ "Proxying localRouteControllerRoutes asynchronously"
+ "Proxying pairedHostDeviceRouteControllerRotes asynchronously"
+ "SharePlayInCallsForRelay"
+ "T@\"TUConfigurationProvider\",R,N"
+ "TB,N,GisCallRecordingEnabled,SsetCallRecordingEnabled:"
+ "TB,N,GisHoldAssistDetectionEnabled,SsetHoldAssistDetectionEnabled:"
+ "TB,N,GisSpamFilterEnabledForFaceTime,SsetSpamFilterEnabledForFaceTime:"
+ "TB,N,V_requiresParticipantTranslation"
+ "TB,R,N,GisHostedOnCurrentDevice,V_hostedOnCurrentDevice"
+ "TUActionScreenUnknownCallers"
+ "Vv40@0:8@\"TUConversationActivity\"16@\"NSUUID\"24Q32"
+ "_isAppleIntelligenceEnabled defaults to YES"
+ "_requiresParticipantTranslation"
+ "configurationProvider"
+ "createActivitySession:onConversation:options:"
+ "createActivitySession:onConversationWithUUID:options:"
+ "fetchRoutesAsyncForRouteController:completionHandler:"
+ "fetchRoutesWithCompletionHandler:"
+ "getLocalRouteControllerRoutes:"
+ "getPairedHostDeviceRouteControllerRoutes:"
+ "holdAssistDetectionEnabled"
+ "initWithCreationRequest:bundleIdentifier:systemActivity:requiresParticipantTranslation:"
+ "initWithUUID:state:events:requiresUserAttentionReason:hostedOnCurrentDevice:"
+ "isCallRecordingEnabled"
+ "isHoldAssistAvailable"
+ "isHoldAssistDetectionEnabled"
+ "isInternalBypassAIForCalls"
+ "isRTTRelaySupportedForSenderIdentityUUID:"
+ "isRTTRelaySupportedForSubscription:"
+ "isRTTRelaySupportedForSubscriptionUUID:"
+ "isSpamFilterEnabledForFaceTime"
+ "phoneClassicNewFavoritesEnabled"
+ "relayIsSupported"
+ "relayIsSupportedForContext:"
+ "requiresParticipantTranslation"
+ "setCallRecordingEnabled:"
+ "setHoldAssistDetectionEnabled:"
+ "setRequiresParticipantTranslation:"
+ "setSpamFilterEnabledForFaceTime:"
+ "sharePlayInCallsForRelayEnabled"
+ "smartHoldingHoldDetectionAvailability=%i, isHoldAssistDetectionEnabled=%i, isTelephonyProvider=%i, lowPowerModeEnabledBlock=%i, smartHoldingAvailability=%i, isOutgoing=%i, isEmergency=%i"
+ "spamFilterEnabledForFaceTime"
+ "spamFilterFaceTimeDisabled"
+ "v32@0:8@\"TURouteController\"16@?<v@?@\"NSArray\">24"
+ "v40@0:8@\"TUConversationActivity\"16@\"TUConversation\"24Q32"
- "@48@0:8@16Q24@32Q40"
- "Default is not set but relay/thumper is enabled, returning TUDefaultAppRelayTelephonySettingCallsFromIPhone"
- "Vv32@0:8@\"TUConversationActivity\"16@\"NSUUID\"24"
- "createActivitySession:onConversationWithUUID:"
- "initWithUUID:state:events:requiresUserAttentionReason:"
- "smartHoldingHoldDetectionAvailability=%i, isTelephonyProvider=%i, lowPowerModeEnabledBlock=%i, smartHoldingAvailability=%i"
- "v32@0:8@\"TUConversationActivity\"16@\"TUConversation\"24"

```
