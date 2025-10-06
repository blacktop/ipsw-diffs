## assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

-3300.120.3.1.2
-  __TEXT.__text: 0x31e21c
+3301.21.2.1.2
+  __TEXT.__text: 0x31f5d4
   __TEXT.__auth_stubs: 0x3230
-  __TEXT.__objc_stubs: 0x3ecc0
-  __TEXT.__objc_methlist: 0x1b0fc
+  __TEXT.__objc_stubs: 0x3ee40
+  __TEXT.__objc_methlist: 0x1b184
   __TEXT.__const: 0xe788
-  __TEXT.__gcc_except_tab: 0x2a80
-  __TEXT.__objc_classname: 0x4d02
-  __TEXT.__objc_methname: 0x55570
-  __TEXT.__objc_methtype: 0xe38e
-  __TEXT.__cstring: 0x4ada4
-  __TEXT.__oslogstring: 0x37093
+  __TEXT.__gcc_except_tab: 0x2a4c
+  __TEXT.__objc_classname: 0x4ce7
+  __TEXT.__objc_methname: 0x5577c
+  __TEXT.__objc_methtype: 0xe3b9
+  __TEXT.__cstring: 0x4b01f
+  __TEXT.__oslogstring: 0x3772c
   __TEXT.__dlopen_cstrs: 0x71c
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x9598
+  __TEXT.__unwind_info: 0x95b8
   __TEXT.__eh_frame: 0x50
   __DATA_CONST.__auth_got: 0x1928
   __DATA_CONST.__got: 0x1ea0
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x14598
-  __DATA_CONST.__cfstring: 0x10620
+  __DATA_CONST.__const: 0x14590
+  __DATA_CONST.__cfstring: 0x10720
   __DATA_CONST.__objc_classlist: 0xc10
   __DATA_CONST.__objc_catlist: 0x620
-  __DATA_CONST.__objc_protolist: 0x698
+  __DATA_CONST.__objc_protolist: 0x690
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x3c8
   __DATA_CONST.__objc_arrayobj: 0x1b0

   __DATA_CONST.__objc_dictobj: 0x2f8
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA.__objc_const: 0x393e0
-  __DATA.__objc_selrefs: 0x11ff8
+  __DATA.__objc_const: 0x39458
+  __DATA.__objc_selrefs: 0x12060
   __DATA.__objc_protorefs: 0x80
-  __DATA.__objc_classrefs: 0x23c8
+  __DATA.__objc_classrefs: 0x23d0
   __DATA.__objc_superrefs: 0xa60
-  __DATA.__objc_ivar: 0x23bc
+  __DATA.__objc_ivar: 0x23c8
   __DATA.__objc_data: 0x78a0
-  __DATA.__data: 0x5c60
-  __DATA.__common: 0x2c
-  __DATA.__bss: 0xd20
+  __DATA.__data: 0x5c08
+  __DATA.__common: 0x30
+  __DATA.__bss: 0xd28
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/Frameworks/MediaSetup.framework/MediaSetup
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/Speech.framework/Speech
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AIMLExperimentationAnalytics.framework/AIMLExperimentationAnalytics
   - /System/Library/PrivateFrameworks/AppConduit.framework/AppConduit

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  UUID: CA416C2C-F87F-34D2-9D68-2BC8A0470F9E
-  Functions: 13277
-  Symbols:   2746
-  CStrings:  26745
+  UUID: 6428C0DA-8EC1-3425-BE00-18D6E2E3594E
+  Functions: 13288
+  Symbols:   2747
+  CStrings:  26813
 
Symbols:
+ _OBJC_CLASS_$_ORCHSchemaORCHAssistantDaemonLaunchMetadataReported
+ _OBJC_CLASS_$_SFEntitledAssetConfig
+ _OBJC_CLASS_$_SFEntitledAssetManager
+ _OBJC_CLASS_$_SFUtilities
- _OBJC_CLASS_$_CESRAssetConfig
- _OBJC_CLASS_$_CESRAssetManager
- _OBJC_CLASS_$_CESRTrialAssetManager
CStrings:
+ "\x04\x19"
+ "\x0f\x0f\x1c\x11\x11\x12+4\x12\x11\x13\x15\x13\x16\x14\x13\x13\x12\x15"
+ "%s #hal Not updating requestDate or currentRequestInfoUUID for requestInfo: %@, origin: %@"
+ "%s BLE discovery is disabled, discovery type is valid."
+ "%s Device does not have status flags. Return true if local device is sidekick and target device is homehub. "
+ "%s Discovery type is invalid."
+ "%s Event has already been logged once for %@"
+ "%s Found the matching device using homeKitAccessoryIdentifier"
+ "%s Found the matching device using ids id."
+ "%s Found the matching device using rapportEffectiveIdentifier"
+ "%s Found the matching device using uniqueIdentifier"
+ "%s Language component is empty"
+ "%s Logging event for: %@"
+ "%s Looking for device with ids id: %@, homekitID : %@, rapportEffectiveID: %@"
+ "%s Modified %zd Key Value Records, %zd Voice Records"
+ "%s Received nil execution id, skip logging discovery event."
+ "%s Searching using HomeKit Identifier"
+ "%s Searching using Rapport Identifier"
+ "%s Searching using uniqueIdentifierForPeer"
+ "%s Setting Siri Phrase Options for the home to %@"
+ "%s Siri language setting is nil"
+ "%s Skipping attempt to sync com.apple.ShortcutsActions bundleId for app intent sync"
+ "%s Skipping manatee update of sync metadata because device has no ATV or Homepod in Home"
+ "%s Speech asset for %@ does not support Assistant."
+ "%s Sync disallowed dictation enabled=%d, dictation only sync allowed=%d, assistant enabled=%d, assistant sync enabled=%d"
+ "%s Sync not allowed - posting sync finished notification for %@"
+ "%s Target Device has ProxyHost status flag. Return true if local device is HomePod and target device is Sidekick."
+ "%s Updating value for disabling assistant sync config for enUS -> %d"
+ "%s _primaryUser companionAssistantID: %{private}@, sharedUserID: %{private}@, voiceIDAllowedByUser=%lu, nonCloudSyncedUser=%lu"
+ "%s _primaryUser is nil"
+ "%s _usersWithAvailableVoiceProfiles: %lu, _sharedUsersBySharedUserID: %lu, multiUsersPreviousCount: %lu"
+ "%s adding _saUnknownUser: %{private}@"
+ "%s currentHome is nil"
+ "%s homeMembers: %lu"
+ "%s isLocalDeviceAnAudioAccessory: %@, isTargetDeviceHomeHubDevice: %@"
+ "%s isLocalDeviceHomeHubDevice: %@, isTargetDeviceAnAudioAccessory: %@."
+ "%s no saved account - fetching from ADAccount"
+ "%s optedOut: %d, fullUodCapable: %d, deviceHasAtvOrHomepodInHome: %d, deviceHasPairedWatch: %d, assistantSyncDisabledViaAssets: %d"
+ "%s routeIdentifier: %@"
+ "%s sharedUserId: %{private}@, voiceIDAllowedByUser: %lu, companionAssistantID: %{private}@, nonCloudSyncedUser: %lu"
+ "-[ADAudioSessionCoordinator relinquishLocalAssertions]"
+ "-[ADCommandCenter _account]"
+ "-[ADCommandCenter getAssistantIdentifier]"
+ "-[ADCommandCenter(Sync) _fetchAllAppSourcesForSyncingWithCustomVocabInfo:completion:]_block_invoke"
+ "-[ADCompanionService _companionLinkDeviceForPeer:allowsDeviceCircleLookup:error:logDiscoveryContextFor:]"
+ "-[ADCompanionService _shouldLogDiscoveryContextForRequestId:]"
+ "-[ADHomeInfoManager(VoiceActivation) setAllowJustSiriHomeKitSetting:withCompletion:queue:]_block_invoke"
+ "-[ADHomeInfoManager(VoiceActivation) setAllowJustSiriHomeKitSetting:withCompletion:queue:]_block_invoke_2"
+ "-[RPCompanionLinkDevice(AssistantAdditions) checkIfHomeHubDeviceIsLookingForItsHubWithLocalDevice:]"
+ "-[RPCompanionLinkDevice(AssistantAdditions) checkIfHubIsLookingForAHomeHubDeviceItIsHostingWithLocalDevice:]"
+ "@\"SFEntitledAssetManager\""
+ "@36@0:8@16B24@28"
+ "@44@0:8@16B24^@28@36"
+ "ADShouldAllowAssistantSync"
+ "HS"
+ "HS+JS"
+ "MobileAssistantDaemons-3301.21.2.1.2"
+ "Relinquish all local assertions"
+ "SFEntitledAssetDelegate"
+ "TB,N,V_disableAssistantSyncForEnUS"
+ "_EmitDaemonLaunchMetadataReportedForRequestId"
+ "_augmentUserPropertiesWithHomeInfoForUser:"
+ "_companionLinkDeviceForPeer:allowsDeviceCircleLookup:error:logDiscoveryContextFor:"
+ "_companionLinkDeviceForPeer:allowsDeviceCircleLookup:logDiscoveryContextFor:"
+ "_disableAssistantSyncForEnUS"
+ "_getExecutionIdFromRequest:"
+ "_hasReceivedFirstRequest"
+ "_logCompanionDeviceDiscoveryContextFor:executionId:"
+ "_shouldLogDiscoveryContextForRequestId:"
+ "_speechAssetStatusForLocale"
+ "_speechAssetTasksForLocale"
+ "_stopObservingRouteChanges"
+ "assistantSyncDisabledForEnUS"
+ "checkIfHomeHubDeviceIsLookingForItsHubWithLocalDevice:"
+ "checkIfHubIsLookingForAHomeHubDeviceItIsHostingWithLocalDevice:"
+ "com.apple.ShortcutsActions"
+ "d24@0:8q16"
+ "disableAssistantSyncForEnUS"
+ "disable_enUS_sync.enablement_status"
+ "hasPresentedCompactVoiceTriggerDisclosure"
+ "homeName"
+ "isCompanionLinkDeviceAProxyHost"
+ "isSiriFullUODSupported"
+ "languageStringForLocaleString:"
+ "modelTasksForLocaleWithInstallationStatus:"
+ "processLoadedMachTime"
+ "relinquishLocalAssertions"
+ "setAssistantDaemonLoadedTimestampInNs:"
+ "setAssistantDaemonSpawnTimestampInNs:"
+ "setAssistantdLaunchMetadataReported:"
+ "setDisableAssistantSyncForEnUS:"
+ "setIsFirstRequest:"
+ "siri_locale_change"
+ "supportsAssistant"
+ "\xf0\xf0\xf0\xf0\xf0\xf0a"
- "\x04\x18"
- "\x0f\x0f\x1c\x11\x11\x12+4\x12\x11\x13\x18\x16\x14\x13\x13\x12\x15"
- "%s Assets for %@ already exist at %@"
- "%s Could not purge assets: %{public}@"
- "%s Error fetching assets for %{public}@: %{public}@"
- "%s Looking for device with ids id: %@"
- "%s On assistant enabling tried to fetch offline models, got %@, error: %@"
- "%s On dictation enabling tried to fetch offline models, got %@ into %@"
- "%s Started fetching assets for %@"
- "%s Sync disallowed dictation enabled=%d, dictation only sync allowed=%d, assistant enabled=%d"
- "%s _logCompanionDeviceDiscoveryContextFor event has already been logged once for %@"
- "%s _logCompanionDeviceDiscoveryContextFor logging event for: %@"
- "%s target device has no statusFlags, isLocalDeviceHomeHubDevice: %@, isTargetDeviceAnAudioAccessory: %@."
- "-[ADCompanionService _companionLinkDeviceForPeer:allowsDeviceCircleLookup:error:shouldLogDiscoveryContext:]"
- "-[ADCompanionService _shouldLogDiscoveryContextForRequest:]"
- "-[ADSettingsClient setDictationEnabled:]_block_invoke"
- "-[ADSpeechManager _fetchAssetsForLanguageOrEnablementNotification:]_block_invoke"
- "-[ADSpeechManager _fetchAssetsForLanguageOrEnablementNotification:]_block_invoke_2"
- "@40@0:8@16B24^@28B36"
- "CESRTrialAssetDelegate"
- "MobileAssistantDaemons-3300.120.3.1.2"
- "SFEntitledTrialAssetDelegate"
- "_companionLinkDeviceForPeer:allowsDeviceCircleLookup:error:shouldLogDiscoveryContext:"
- "_companionLinkDeviceForPeer:allowsDeviceCircleLookup:shouldLogDiscoveryContext:"
- "_fetchAssetsForLanguageOrEnablementNotification:"
- "_logCompanionDeviceDiscoveryContextFor:"
- "_shouldLogDiscoveryContextForRequest:"
- "_speechAssetStatus"
- "activeDictationLanguages"
- "f24@0:8q16"
- "fetchAssetsForAssetConfig:completion:"
- "getOfflineAssetStatusIgnoringCache:assetType:withCompletion:"
- "isASRAdoptingUAFEnabled"
- "offlineDictationStatusIgnoringCache:error:"
- "purgeInstalledAssetsExceptLanguages:assetType:error:"
- "\xf0\xf0\xf0\xf0\xf0\xf0Q"

```
