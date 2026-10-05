## assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_doubleobj`
- `__DATA_CONST.__objc_floatobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-3605.24.1.1.1
-  __TEXT.__text: 0x377220
-  __TEXT.__auth_stubs: 0x3910
-  __TEXT.__objc_stubs: 0x48560
-  __TEXT.__objc_methlist: 0x240f0
+3605.30.1.1.1
+  __TEXT.__text: 0x37bad4
+  __TEXT.__auth_stubs: 0x3930
+  __TEXT.__objc_stubs: 0x48ac0
+  __TEXT.__objc_methlist: 0x24460
   __TEXT.__const: 0xede8
   __TEXT.__dlopen_cstrs: 0x9e9
-  __TEXT.__gcc_except_tab: 0x3cc0
-  __TEXT.__cstring: 0x54fff
-  __TEXT.__oslogstring: 0x49755
-  __TEXT.__objc_classname: 0x52bc
-  __TEXT.__objc_methname: 0x63aa3
-  __TEXT.__objc_methtype: 0x10250
+  __TEXT.__gcc_except_tab: 0x3e48
+  __TEXT.__cstring: 0x5572e
+  __TEXT.__oslogstring: 0x4b564
+  __TEXT.__objc_classname: 0x532c
+  __TEXT.__objc_methname: 0x6435e
+  __TEXT.__objc_methtype: 0x10465
   __TEXT.__ustring: 0x98
-  __TEXT.__unwind_info: 0xd0e8
+  __TEXT.__unwind_info: 0xd250
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__const: 0x147f8
-  __DATA_CONST.__cfstring: 0x12f40
+  __DATA_CONST.__const: 0x14a30
+  __DATA_CONST.__cfstring: 0x13040
   __DATA_CONST.__objc_classlist: 0xd70
   __DATA_CONST.__objc_catlist: 0x630
-  __DATA_CONST.__objc_protolist: 0x738
+  __DATA_CONST.__objc_protolist: 0x758
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0xb38

   __DATA_CONST.__objc_dictobj: 0x2f8
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA_CONST.__auth_got: 0x1c98
-  __DATA_CONST.__got: 0x3eb8
+  __DATA_CONST.__auth_got: 0x1ca8
+  __DATA_CONST.__got: 0x3ec0
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA.__objc_const: 0x35988
-  __DATA.__objc_selrefs: 0x15b28
-  __DATA.__objc_ivar: 0x2774
+  __DATA.__objc_const: 0x35e28
+  __DATA.__objc_selrefs: 0x15c98
+  __DATA.__objc_ivar: 0x27d8
   __DATA.__objc_data: 0x8660
-  __DATA.__data: 0x5e20
+  __DATA.__data: 0x5fa0
   __DATA.__common: 0xa18
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 14889
-  Symbols:   3024
-  CStrings:  28547
+  Functions: 14975
+  Symbols:   3026
+  CStrings:  28727
 
Symbols:
+ _AFHasMicrophone
+ _OBJC_CLASS_$_SAPhoneClientCoordinationPhoneCall
+ _clock_gettime_nsec_np
+ _dispatch_block_wait
- _AFIsHorseman
- _SAInputOriginScreenGestureValue
CStrings:
+ "%s #SiriAvailability Capabilities computed - changed: %{public,bool}d\n, siriAvailability: %{public}@\n, desiredOrchestrationMode: %{public}@\n, possibleOrchestrationMode: %{public}@\n, missingLinwoodCapabilities: %{public}@\n, missingSAECapabilities: %{public}@"
+ "%s #SiriAvailability Siri is no longer restricted - restoring the pre-restriction setting assistantEnabled=%{bool}d (currently %{bool}d)"
+ "%s #SiriAvailability Siri is not restricted - discarding the pre-restriction setting assistantEnabled=%{bool}d recorded by a previous build without applying it"
+ "%s #SiriAvailability Siri is restricted (%{public}@) - adopting the pre-restriction setting assistantEnabled=%{bool}d recorded by a previous build"
+ "%s #SiriAvailability Siri is restricted (%{public}@) - disabling assistant"
+ "%s #SiriAvailability Siri is restricted (%{public}@) - recording assistantEnabled=%{bool}d as the pre-restriction setting"
+ "%s #SiriAvailability recomputing: Screen Time settings changed (%{public}@)"
+ "%s #multi-user Dropping duplicate shared user %{private}@ (enrollment %{private}@) already present as primary user %{private}@"
+ "%s #multi-user Dropping superseded shared user %{private}@ (enrollment %{private}@) for account %{private}@"
+ "%s %@ - posting sync finished notification for %@"
+ "%s %lu request-group backstops are armed and pending, which needs a sustained request-start rate no real client produces; suspect starts that never balance their group"
+ "%s %{public}s did not finish within %.0f s; completing it and releasing its transaction so the process can still exit -- for a repeating activity this resets its interval, so the next attempt is a full interval away"
+ "%s %{public}s did not finish within %.0f s; releasing its transaction (check-in path -- no activity in flight)"
+ "%s ADSiriCapabilitiesStore built with a nil dispatch queue — falling back to a private serial queue. Serial confinement is intact but this store is NOT on ADCommandCenterQueue, and +sharedStore has latched that for the life of the process. In a test process the usual cause is +[ADCommandCenter sharedCommandCenter] class-mocked without stubbing +sharedQueue."
+ "%s Account changed: no assistant identifier, none reported by the poster, and no rotation in flight. Disabling Recognize My Voice."
+ "%s Adding zone for iCloudAltDSID: %{private}@, ZoneName: %@, ZoneInfo: %@"
+ "%s Already hold an assistant identifier, so there is nothing to decide about Recognize My Voice."
+ "%s An ADSiriCapabilitiesStoreAssetsAvailabilityObserver callback fired after its store was deallocated, so the asset-availability update was dropped. In the daemon the store is an immortal singleton and this should be unreachable; if it fires there, something is constructing a non-singleton store or clearing the shared one."
+ "%s An assistant identifier arrived while the live account was in flight; leaving Recognize My Voice alone."
+ "%s Assistant identifier is absent because a rotation is in flight. Leaving Recognize My Voice alone."
+ "%s Assistant identifier is absent because a rotation is in flight; leaving Recognize My Voice alone."
+ "%s Choosing container for %{private}@ from %{private}@"
+ "%s Cloud sync is not enabled for this account; completing with %@"
+ "%s Created new zone for iCloudAltDSID: %{private}@, ZoneName: %@, ZoneInfo: %@"
+ "%s Dropping %lu deferred command(s); request ended without a connection"
+ "%s Dropping a latched daemon-decided Recognize My Voice disable rather than replaying it: HomeKit was unavailable for %.0f s, past the %.0f s the decision is good for."
+ "%s Enabled bits changed: Siri and Dictation are both off on this me-device, so no companion assistant ID will exist. Disabling Recognize My Voice."
+ "%s Entering request group %@ (%{private}@)..."
+ "%s Error inserting recognition into FeatureStore for id: %{public}@ -- %{public}@ %{public}ld (%lu json bytes)"
+ "%s Existing zones for iCloudAltDSID: %{private}@"
+ "%s HMHomeManager is ready but reports no homes, so the VoiceID=%d request (userInitiated %{bool}d) is being dropped, not written."
+ "%s HMHomeManager not ready (status %ld); latching the VoiceID=%d request (userInitiated %{bool}d) for replay."
+ "%s Ignoring a sync-finished notification for unrelated keys %@; this request asked for %@"
+ "%s Interval %f s at %u fps yields %{public}s frame; using 1"
+ "%s Invalid listeningType %lu passed to _framesPerSecondForOpportuneSpeakListeningType"
+ "%s Invalid listeningType %lu passed to _initializeVoiceThresholdsForOpportuneSpeakListeningType; using the DoAP ratios as a safety floor"
+ "%s Invalid results for %@ : %{private}@"
+ "%s Keeping the user's latched Recognize My Voice request (%ld) rather than overwriting it with a daemon-decided disable."
+ "%s Keychain read returned no assistant identifier, but the poster just saved one. Leaving Recognize My Voice alone."
+ "%s Keychain writes for %{private}@ were not waited on at all: an earlier drain in this batch had already spent the %f s budget. This says nothing about securityd's health. Posting the identifier-change notifications anyway."
+ "%s Keychain writes for %{private}@ were still outstanding when the drain ceiling in force expired (%f s for a lone save, or what was left of the %f s batch budget); posting the identifier-change notifications anyway rather than holding this queue."
+ "%s Leaving RMV alone while disabling Siri-over-iCloud: this is not the me-device (isMeDevice=%{public}@)"
+ "%s Leaving request group %@ (%{private}@)..."
+ "%s Me-device changed: Siri and Dictation are both off, so no companion assistant ID will exist. Disabling Recognize My Voice."
+ "%s Moving average buffer asked for a window of %d frames; clamping to 1"
+ "%s Moving average buffer could not allocate a ring of %d frames"
+ "%s No Command Center yet, so there is no live account to read. Leaving Recognize My Voice alone."
+ "%s No VoiceID setting found for this home, so the VoiceID=%d request (userInitiated %{bool}d) is being dropped, not written."
+ "%s No container found for %{private}@"
+ "%s No longer the me-device by the time the live account arrived; leaving Recognize My Voice alone."
+ "%s No request dispatcher service could be built, but one was expected. Please file a radar on Siri Frameworks."
+ "%s No speech group to enter, so balancing the request group now (%@)..."
+ "%s No valid meDevice determination available, keeping isMeDevice %@"
+ "%s Not opening connection for %{public}@; Linwood handles this request on device"
+ "%s Pre existing zone for iCloudAltDSID: %{private}@, ZoneName: %@, ZoneInfo: %@"
+ "%s Promoting %lu deferred command(s); this session is opening a connection"
+ "%s Refusing to attend: %{public}s"
+ "%s Refusing to start a nil announcement request (state:%{public}@ currentRequest:%{public}@ previousRequest:%{public}@ burstIndex:%lu) -- the upstream _currentRequest defect fired"
+ "%s Refusing to start a nil announcement request before the opportune-time check (state:%{public}@ currentRequest:%{public}@ previousRequest:%{public}@ burstIndex:%lu) -- the upstream _currentRequest defect fired"
+ "%s Replaying the latched VoiceID=%d request (userInitiated %{bool}d) now that HMHomeManager is ready."
+ "%s Request group leave ran on DEALLOC, i.e. a callee dropped the completion that owned it. requestId=%{public}@ (%{private}@)"
+ "%s Request start never balanced the request group within %.0fs, so nothing could interrupt it; leaving the group. requestId=%{public}@ (%{private}@)"
+ "%s Resetting primary iCloud Info %{private}@"
+ "%s Retrieved results for %@ : %{private}@"
+ "%s SASMultilingualSpeechRecognized failed to return speech recognized command for primary language (refId:%{public}@ languageCandidates:%{public}lu)"
+ "%s Saving account info %{private}@"
+ "%s Schema skew: the SiriInstrumentation on this device has no -[SISchemaAnnounceEnabledStatus setAnnounceCallsEnabled:], dropping the property from the daily device-status heartbeat"
+ "%s Schema skew: the SiriInstrumentation on this device has no -[SISchemaEnabledStatus setIsRemoteDarwinHeySiriEnabled:], dropping the property from the daily device-status heartbeat"
+ "%s Schema skew: the SiriInstrumentation on this device has no -[SISchemaVoiceTriggerMetrics setIsJSEnabled:], dropping the property from the daily device-status heartbeat"
+ "%s Sending SACommandSucceeded to the flow SAPhoneClientCoordinationPhoneCall"
+ "%s Setting is already VoiceID=%d, so no write is needed."
+ "%s Siri is off but Dictation is on, so a companion assistant ID still exists. Leaving Recognize My Voice alone."
+ "%s The active account on this me-device holds no account identifier, so it is the unprovisioned placeholder; leaving Recognize My Voice alone."
+ "%s The live active account holds an assistant identifier; leaving Recognize My Voice alone."
+ "%s The live active account holds no assistant identifier. Disabling Recognize My Voice."
+ "%s Unable to remove and save account info %{private}@ because it is read only."
+ "%s Unable to save account info %{private}@ because it is read only."
+ "%s Updated accountInfo and isCloudSyncEnabledForZone = (%d) for %{private}@"
+ "%s Updated listening threshold to: %f (%d frames)"
+ "%s Updated zones for iCloudAltDSID: %{private}@"
+ "%s VoiceID write completed (value %d, error %{public}@ %ld)"
+ "%s Writing VoiceID=%d to HomeKit (userInitiated %{bool}d)."
+ "%s assistantId created: %{private}@ loggingAssistantId: %{private}@ speechId: %{private}@"
+ "%s data present=%d assistantId=%{private}@ language=%{public}@ hasUserAgent=%d siriEnabled=%d fullUod=%d restrictedAppCount=%lu"
+ "%s iCloud AltDSID is specified, choosing container for %{private}@ from %{private}@"
+ "%s iCloud sync is disabled. Voice Trigger setup timer canceled"
+ "%s iCloudAltDSID: %{private}@, accountInfo: %{private}@"
+ "%s missing assistantId=%{private}@ or uniqueId=%{private}@"
+ "*20@0:8i16"
+ "-[ADCommandCenter _saPhoneClientCoordinationPhoneCall:completion:]"
+ "-[ADCommandCenter(SharedDataRemote) getSharedDataForPeer:]_block_invoke_2"
+ "-[ADDailyDeviceStatusActivity _buildDailyVoiceTriggerMetrics:]"
+ "-[ADExternalNotificationRequestHandler _startAnnouncementRequestIfOpportune:]"
+ "-[ADHomeInfoManager _replayPendingVoiceIDRequestIfNeeded]"
+ "-[ADHomeInfoManager _setRecognizeMyVoiceEnabled:userInitiated:decisionTimestampNs:]_block_invoke"
+ "-[ADMultiUserCloudKitSyncer _evaluateRecognizeMyVoiceOnMeDevice]"
+ "-[ADMultiUserCloudKitSyncer _evaluateRecognizeMyVoiceOnMeDevice]_block_invoke"
+ "-[ADMultiUserCloudKitSyncer _evaluateRecognizeMyVoiceOnMeDevice]_block_invoke_2"
+ "-[ADMultiUserCloudKitSyncer _fetchLiveActiveAccount:]"
+ "-[ADMultiUserCloudKitSyncer enabledBitsChanged:]_block_invoke"
+ "-[ADMultiUserService _dropSharedUserDuplicatesOfPrimary:]"
+ "-[ADMultiUserService _dropSupersededSharedUserDuplicates]"
+ "-[ADOpportuneSpeakingModuleEdgeDetector _reportRefusedListenWithReason:failCompletion:]"
+ "-[ADOpportuneSpeakingMovingAverageBuffer initWithSize:]"
+ "-[ADSessionRemoteServerLimited _deferCommandInsteadOfOpeningConnection:]"
+ "-[ADSessionRemoteServerLimited _promoteDeferredCommands]"
+ "-[ADSessionRemoteServerLimited setHasActiveRequest:]"
+ "-[ADSiriCapabilitiesStore initWithDispatchQueue:preferences:assetManager:]"
+ "-[ADSiriCapabilitiesStore reconcileAssistantEnablementForRestrictionReasons:assistantEnabled:]"
+ "@\"<ADCloudKitManagerProviding>\""
+ "@\"<ADHomeInfoManagerProviding>\""
+ "@\"<ADPreferencesProviding>\""
+ "@\"<AFPreferencesInternalProviding>\""
+ "@\"<AFPreferencesProviding>\""
+ "@\"ADSiriCapabilitiesStoreAssetsAvailabilityObserver\""
+ "@\"AFVoiceInfo\"16@0:8"
+ "ADAccountAssistantIdentifierIsRotatingKey"
+ "ADAccountSavedAssistantIdentifierKey"
+ "ADCloudKitManagerProviding"
+ "ADHomeInfoManagerInternalProviding"
+ "ADHomeInfoManagerProviding"
+ "ADOpportuneSpeakingFrameCountForInterval"
+ "ADPreferencesProviding"
+ "Checkpoint could not be written to keychain; the next launch will use a local seed"
+ "Cloud sync is not enabled for this account"
+ "Fixed device identifier could not be written to keychain; it will change during next read"
+ "FullUOD device has no more keys to sync"
+ "HandleScreenTimeSettingsDidChangeNotification"
+ "Host UUID could not be written to keychain! fixedDeviceId will change during next read"
+ "MobileAssistantDaemons-3605.30.1.1.1"
+ "No keys survived filtering"
+ "Nothing to sync"
+ "SiriNetworkConnection.UserInitiated"
+ "T@\"<ADCloudKitManagerProviding>\",&,N,V_cloudKitManager"
+ "T@\"<ADHomeInfoManagerProviding>\",&,N,V_homeInfoManager"
+ "T@\"<ADPreferencesProviding>\",&,N,V_adPreferences"
+ "T@\"<AFPreferencesInternalProviding>\",&,N,V_preferences"
+ "T@\"<AFPreferencesProviding>\",&,N,V_preferences"
+ "T@\"ADCommunalDeviceUserAttributes\",&,N,V_attributes"
+ "T@\"ADSiriCapabilitiesStore\",R,W,N,V_siriCapabilitiesStore"
+ "TQ,V_screenTimeSettingsEdgeCount"
+ "_ADActivityTransactionGuard_block_invoke"
+ "_ADOccupyRequestGroup"
+ "_ADOccupyRequestGroup_block_invoke"
+ "_ADPostSyncFinishedForAbandonedSync"
+ "_ADSiriCapabilitiesStoreWarnIfObserverOutlivedStore_block_invoke"
+ "_allocateRingWithFrameCount:"
+ "_assetsObserver"
+ "_assistantDataClearedForRotation"
+ "_assistantIdentifierRotationInFlight"
+ "_atvRmVEnableGenerationByAltDSID"
+ "_atvRmVEnableGenerationCounter"
+ "_clientLinkReconnectTimer"
+ "_cloudKitManager"
+ "_commandDoesNotJustifyOpeningConnection:"
+ "_commandIsMootWithoutConnection:"
+ "_commandIsSatisfiedOnDevice:"
+ "_deferCommandInsteadOfOpeningConnection:"
+ "_deferredCommandIndexes"
+ "_deferredCommands"
+ "_drainKeychainQueue"
+ "_dropSharedUser:keepingIdentifiersOf:"
+ "_dropSharedUserDuplicatesOfPrimary:"
+ "_dropSupersededSharedUserDuplicates"
+ "_evaluateRecognizeMyVoiceOnMeDevice"
+ "_fetchLiveActiveAccount:"
+ "_forgetDeferredCommands"
+ "_hasRequiredIdentifiers"
+ "_isUserRecordMissingForICloudAltDSID:"
+ "_keychainDataForKey:"
+ "_keychainDrainDeadline"
+ "_messageLinkReconnectTimer"
+ "_pendingVoiceIDRequest"
+ "_pendingVoiceIDRequestTimestampNs"
+ "_promoteDeferredCommands"
+ "_queueConfinementWaivedForInit"
+ "_rapportReconnectTimer"
+ "_reconnectClientLinkIfStillDisconnected"
+ "_reconnectContextLinkIfStillDisconnected"
+ "_removeDeviceOwner"
+ "_replayPendingVoiceIDRequestIfNeeded"
+ "_reportRefusedListenWithReason:failCompletion:"
+ "_saPhoneClientCoordinationPhoneCall:completion:"
+ "_screenTimeSettingsEdgeCount"
+ "_setKeychainData:forKey:"
+ "_setRecognizeMyVoiceEnabled:userInitiated:decisionTimestampNs:"
+ "_siriNetworkConnectionQueueForOrchestrationMode:"
+ "_watchLinwoodModalityDeferralAllowed"
+ "_watchLinwoodModalityDeferralAllowedWithCurrentOrchestrationMode:"
+ "adPreferences"
+ "an undefined"
+ "applyAssistantEnabled:dropPreRestrictionValue:"
+ "applyAssistantEnabledThroughCommandCenter:dropPreRestrictionValue:"
+ "assistantEnabledBeforeRestrictionIsCurrentVersion"
+ "beginKeychainDrainBudget"
+ "clearAssistantDataForRotation"
+ "cloudKitManager"
+ "com.apple.ScreenTimeAgent.SettingsDidChangeNotification"
+ "com.apple.siri.ADSiriCapabilitiesStore.fallback"
+ "com.apple.siri.myriad.falseemergency"
+ "could not allocate the moving-average ring"
+ "destroy-account activity"
+ "dictationOptionsWithoutTextContext"
+ "emergencyCall"
+ "endKeychainDrainBudget"
+ "getSharedUserIdentifiersWithCompletion:"
+ "hasIdentifier"
+ "intersectsSet:"
+ "less than one"
+ "meDeviceValid"
+ "no frame rate for this listeningType"
+ "not-yet-evaluated"
+ "refresh-validation activity"
+ "screenTimeSettingsEdgeCount"
+ "setAdPreferences:"
+ "setByAddingObject:"
+ "setCloudKitManager:"
+ "setPreferences:"
+ "setRecognizeMyVoiceEnabled:userInitiated:"
+ "setScreenTimeSettingsEdgeCount:"
+ "v16@?0@8"
+ "v24@0:8@?<v@?@\"HMHomeManager\">16"
+ "v24@0:8@?<v@?@\"SISchemaMultiUserSetup\">16"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@@\"NSError\">24"
+ "v32@0:8B16B20Q24"
+ "v32@0:8r*16@?24"
+ "v32@?0@8Q16^B24"
+ "v40@0:8@\"NSArray\"16q24@?<v@?@@\"NSError\">32"
+ "v40@0:8@\"NSDictionary\"16@\"NSArray\"24@?<v@?@\"NSError\">32"
+ "\xa1"
- "%s #SiriAvailability Capabilities changed - sending notification: %@\n, siriAvailability: %{public}@\n, desiredOrchestrationMode: %{public}@\n, possibleOrchestrationMode: %{public}@\n, missingLinwoodCapabilities: %{public}@\n, missingSAECapabilities: %{public}@"
- "%s #hal #on-demand invalidate on-demand connection on exit."
- "%s #multi-user-atv primary user existed as shared user. Untracking as shared user."
- "%s Adding zone for iCloudAltDSID: %@, ZoneName: %@, ZoneInfo: %@"
- "%s Choosing container for %{private}@ from %@"
- "%s Created new zone for iCloudAltDSID: %@, ZoneName: %@, ZoneInfo: %@"
- "%s Entering request group %@ (%@)..."
- "%s Error: %@ inserting \"%@\" into FeatureStore for id: %@"
- "%s Existing zones for iCloudAltDSID: %@"
- "%s FullUOD device has no more keys to sync - exiting"
- "%s HMHomeManager not ready"
- "%s Invalid listeningType passed to _framesPerSecondForOpportuneSpeakListeningType"
- "%s Invalid results for %@ : %@"
- "%s Leaving request group %@ (%@)..."
- "%s No container found for %@"
- "%s Nothing to sync"
- "%s Pre existing zone for iCloudAltDSID: %@, ZoneName: %@, ZoneInfo: %@"
- "%s Resetting primary iCloud Info"
- "%s Resetting primary iCloud Info %@"
- "%s Retrieved results for %@ : %@"
- "%s SASMultilingualSpeechRecognized failed to return speech recognized command for primary language\n %@ %@"
- "%s Saving account info %@"
- "%s Setting VoiceID=%d"
- "%s Setting is already VoiceID=%d"
- "%s Settings operation completed with (%@) value (%d)"
- "%s Siri restriction imposed (%@) — disabling assistant"
- "%s Siri restriction lifted - restoring assistant to its pre-restriction state: %d"
- "%s Unable to remove and save account info %@ because it is read only."
- "%s Unable to save account info %@ because it is read only."
- "%s Updated accountInfo and isCloudSyncEnabledForZone = (%d) for %@"
- "%s Updated listening threshold to: %f"
- "%s Updated zones for iCloudAltDSID: %@"
- "%s assistantId created: %@ loggingAssistantId: %@ speechId: %@"
- "%s data=%@"
- "%s iCloud AltDSID is specified, choosing container for %{private}@ from %@"
- "%s iCloud sync is disabled. Voice Trigger setup timer cancelled"
- "%s iCloudAltDSID: %@"
- "%s iCloudAltDSID: %@, accountInfo: %@"
- "%s missing assistantId=%@ or uniqueId=%@"
- "-[ADCommandCenter _startNonSpeechRequest:forDelegate:withInfo:options:suppressAlert:completion:]_block_invoke"
- "-[ADCommandCenter _startSpeechRequestWithDelegate:withOptions:sessionUUID:completion:]_block_invoke_2"
- "-[ADCommandCenter handleSiriAvailabilityDidChange:]_block_invoke"
- "-[ADCommandCenter(SharedDataRemote) getSharedDataForPeer:]_block_invoke"
- "-[ADHomeInfoManager setRecognizeMyVoiceEnabled:]_block_invoke"
- "MobileAssistantDaemons-3605.24.1.1.1"
- "T@\"ADCommunalDeviceUserAttributes\",C,N,V_attributes"
- "_assistantRequestedToTurnOffVoiceID"
- "_checkAndDisableVoiceIDIfRequired"
- "restrictionReasons"
- "syncRequestTime"
- "\x81"
```
