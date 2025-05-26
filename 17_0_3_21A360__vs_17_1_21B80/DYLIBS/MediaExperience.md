## MediaExperience

> `/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience`

```diff

-90.77.1.1.5
-  __TEXT.__text: 0x18b848
-  __TEXT.__auth_stubs: 0x1dc0
-  __TEXT.__objc_methlist: 0x364c
-  __TEXT.__cstring: 0x2365e
-  __TEXT.__const: 0x1900
-  __TEXT.__gcc_except_tab: 0x1624
-  __TEXT.__oslogstring: 0x2abe1
+125.13.1.1.0
+  __TEXT.__text: 0x18cef0
+  __TEXT.__auth_stubs: 0x1db0
+  __TEXT.__objc_methlist: 0x36a4
+  __TEXT.__cstring: 0x23934
+  __TEXT.__const: 0x1930
+  __TEXT.__gcc_except_tab: 0x1650
+  __TEXT.__oslogstring: 0x2afd7
   __TEXT.__dlopen_cstrs: 0x503
-  __TEXT.__unwind_info: 0x3830
+  __TEXT.__unwind_info: 0x3870
   __TEXT.__objc_classname: 0x388
-  __TEXT.__objc_methname: 0xef90
+  __TEXT.__objc_methname: 0xf13e
   __TEXT.__objc_methtype: 0x18bc
-  __TEXT.__objc_stubs: 0x9340
-  __DATA_CONST.__got: 0x7f0
-  __DATA_CONST.__const: 0x5a90
+  __TEXT.__objc_stubs: 0x9420
+  __DATA_CONST.__got: 0x7e8
+  __DATA_CONST.__const: 0x5ad0
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5910
-  __DATA_CONST.__objc_selrefs: 0x27c0
+  __DATA_CONST.__objc_const: 0x5970
+  __DATA_CONST.__objc_selrefs: 0x2800
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__cfstring: 0x14c80
-  __AUTH_CONST.__const: 0x3278
+  __AUTH_CONST.__cfstring: 0x14dc0
+  __AUTH_CONST.__const: 0x32a8
   __AUTH_CONST.__objc_const: 0xca0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0xef8
+  __AUTH_CONST.__auth_got: 0xef0
   __AUTH.__data: 0x490
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_classrefs: 0x208
+  __DATA.__objc_classrefs: 0x210
   __DATA.__objc_superrefs: 0xe8
-  __DATA.__objc_ivar: 0x5dc
+  __DATA.__objc_ivar: 0x5e4
   __DATA.__data: 0x1fd8
   __DATA.__common: 0xd0
-  __DATA.__bss: 0x848
+  __DATA.__bss: 0x850
   __DATA_DIRTY.__objc_data: 0x910
   __DATA_DIRTY.__bss: 0x150
   __DATA_DIRTY.__common: 0x60

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4753
-  Symbols:   15367
-  CStrings:  8483
+  Functions: 4768
+  Symbols:   15417
+  CStrings:  8524
 
Symbols:
+ -[AVSystemController clearUplinkMutedCache]
+ -[MXCoreSession prefersConcurrentAirPlayAudio]
+ -[MXCoreSession setPrefersConcurrentAirPlayAudio:]
+ -[MXSessionManager interruptActiveSessionsNotOptedIntoWombat]
+ -[MXSessionManager(Utilities) clearUplinkMutedCache]
+ -[MXSessionManager(Utilities) postStopCommandToSessionsWithAudioMode:]
+ -[MXSystemController clearUplinkMutedCache]
+ -[MXSystemController hasEntitlementToClearCacheForFirstPartyPhoneCalls]
+ -[MXSystemController setHasEntitlementToClearCacheForFirstPartyPhoneCalls:]
+ GCC_except_table30
+ _CMSMNotificationUtility_PostSessionPrefersConcurrentAirPlayAudioDidChange
+ _FigRoutingMangerCreateBluetoothEndpointManager
+ _FigRoutingMangerCreateBluetoothEndpointManager.sBluetoothEndpointManagerSetup
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_IVAR_$_MXCoreSession._prefersConcurrentAirPlayAudio
+ _OBJC_IVAR_$_MXSystemController._hasEntitlementToClearCacheForFirstPartyPhoneCalls
+ ___43-[MXSystemController clearUplinkMutedCache]_block_invoke
+ ___57-[MXSessionManager(Utilities) updateMuteState:muteValue:]_block_invoke.16
+ ___CMSMNotificationUtility_PostSessionPrefersConcurrentAirPlayAudioDidChange_block_invoke
+ ___FigRoutingMangerCreateBluetoothEndpointManager_block_invoke
+ ___FigRoutingMangerCreateBluetoothEndpointManager_block_invoke.cold.1
+ _kFigEndpointUIAgentNotificationPayloadKey_EchoedDictionary
+ _kFigRoutingContextGlobalModificationOption_ShowErrorPromptDictionaryToEcho
+ _kMXSessionAudioCategory_DictationBegin
+ _kMXSessionAudioCategory_DictationCancel
+ _kMXSessionAudioCategory_DictationConfirm
+ _kMXSessionNotificationKey_PrefersConcurrentAirPlayAudio
+ _kMXSessionNotification_PrefersConcurrentAirPlayAudioDidChange
+ _kMXSessionProperty_PrefersConcurrentAirPlayAudio
+ _objc_msgSend$clearUplinkMutedCache
+ _objc_msgSend$hasEntitlementToClearCacheForFirstPartyPhoneCalls
+ _objc_msgSend$interruptActiveSessionsNotOptedIntoWombat
+ _objc_msgSend$prefersConcurrentAirPlayAudio
+ _objc_msgSend$processInfo
+ _objc_msgSend$setHasEntitlementToClearCacheForFirstPartyPhoneCalls:
+ _objc_msgSend$setPrefersConcurrentAirPlayAudio:
+ _objc_msgSend$systemUptime
+ _remoteSystemController_ClearUplinkMutedCache
+ _systemController_ClearUplinkMutedCache
- -[MXSessionManager interruptPlayingSessionsNotOptedIntoWombat]
- GCC_except_table38
- GCC_except_table51
- GCC_except_table70
- _FigEndpointUtility_CopyMatchingEndpointEntities
- _FigEndpointUtility_EndpointManagerPredicate_IsEndpointManagerOfType
- _FigRoutingManagerCreateEndpointManagers.cold.5
- ___57-[MXSessionManager(Utilities) updateMuteState:muteValue:]_block_invoke.13
- _objc_msgSend$interruptPlayingSessionsNotOptedIntoWombat
CStrings:
+ "-CMSMNotificationUtilities- %s: Posting PrefersConcurrentAirPlayAudioDidChange notification,  prefersConcurrentAirPlayAudioDidChange = %{BOOL}u"
+ "-CMSessionMgr- %s: Client %{public}@ [%p] setting %{public}@ to %{BOOL}u"
+ "-CMSessionMgr- %s: Client '%{public}@' resetting WantsToPauseSpokenAudio while it's active"
+ "-CMSessionMgr- %s: Client '%{public}@' setting WantsToPauseSpokenAudio to '%{BOOL}u'"
+ "-CMSessionMgr- %s: SpeechDetectionVADID %{public}@, device sample rate = %{public}@"
+ "-FigRoutingManager- %s: MediaExperience created BluetoothEndpointManager"
+ "-MXSessionManager- %s: Devices sample rates cache is updated"
+ "-MXSessionManager- %s: Unit was rebooted, Clear cache of mutedBundleIDs list"
+ "-MXSessionManagerUtilities- %s: Interrupting session '%{public}@' with audioMode '%{public}@'"
+ "-MXSessionManagerUtilities- %s: Nil audioMode"
+ "-MXSessionManagerUtilities- %s: Updated muted session bundle IDs list after clear mute state: %{private}@"
+ "-MXSystemController- %s: Either Call Management mute control feature is not enabled or missing entitlement to clear cache for first party phonecalls"
+ "-[MXSessionManager init]"
+ "-[MXSessionManager interruptActiveSessionsNotOptedIntoWombat]"
+ "-[MXSessionManager(Utilities) clearUplinkMutedCache]"
+ "-[MXSessionManager(Utilities) postStopCommandToSessionsWithAudioMode:]"
+ "-[MXSystemController clearUplinkMutedCache]"
+ "22:12:26"
+ "CMSMNotificationUtility_PostSessionPrefersConcurrentAirPlayAudioDidChange"
+ "CMSMNotificationUtility_PostSessionPrefersConcurrentAirPlayAudioDidChange_block_invoke"
+ "DictationBegin"
+ "DictationCancel"
+ "DictationConfirm"
+ "FigRoutingMangerCreateBluetoothEndpointManager_block_invoke"
+ "Oct  4 2023"
+ "PrefersConcurrentAirPlayAudio"
+ "PrefersConcurrentAirPlayAudioDidChange"
+ "TB,N,V_hasEntitlementToClearCacheForFirstPartyPhoneCalls"
+ "TB,N,V_prefersConcurrentAirPlayAudio"
+ "_hasEntitlementToClearCacheForFirstPartyPhoneCalls"
+ "_prefersConcurrentAirPlayAudio"
+ "clearUplinkMutedCache"
+ "com.apple"
+ "com.apple.private.mediaexperience.clearmutestatecache.allow"
+ "echoedDictionary"
+ "hasEntitlementToClearCacheForFirstPartyPhoneCalls"
+ "interruptActiveSessionsNotOptedIntoWombat"
+ "postStopCommandToSessionsWithAudioMode:"
+ "prefersConcurrentAirPlayAudio"
+ "prefersConcurrentAirPlayAudio ="
+ "processInfo"
+ "remoteSystemController_ClearUplinkMutedCache"
+ "setHasEntitlementToClearCacheForFirstPartyPhoneCalls:"
+ "setPrefersConcurrentAirPlayAudio:"
+ "showErrorPromptDictionaryToEcho"
+ "systemUptime"
- "-MXSessionManager- %s: Devices sample rates cache has been refreshed"
- "-[MXSessionManager interruptPlayingSessionsNotOptedIntoWombat]"
- "21:33:31"
- "Aug 17 2023"
- "interruptPlayingSessionsNotOptedIntoWombat"

```
