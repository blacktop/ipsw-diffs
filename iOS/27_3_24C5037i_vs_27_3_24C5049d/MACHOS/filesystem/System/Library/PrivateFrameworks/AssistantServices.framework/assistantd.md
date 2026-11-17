## assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3610.11.2.0.0
-  __TEXT.__text: 0x3a0864
-  __TEXT.__auth_stubs: 0x3ad0
-  __TEXT.__objc_stubs: 0x4ba80
-  __TEXT.__objc_methlist: 0x251e8
+3610.19.4.0.0
+  __TEXT.__text: 0x3a4e70
+  __TEXT.__auth_stubs: 0x3b00
+  __TEXT.__objc_stubs: 0x4c180
+  __TEXT.__objc_methlist: 0x25470
   __TEXT.__const: 0xedf8
   __TEXT.__dlopen_cstrs: 0x86a
-  __TEXT.__gcc_except_tab: 0x51fc
-  __TEXT.__cstring: 0x58dae
-  __TEXT.__oslogstring: 0x513c7
-  __TEXT.__objc_classname: 0x52d2
-  __TEXT.__objc_methname: 0x68962
-  __TEXT.__objc_methtype: 0x10691
-  __TEXT.__ustring: 0x98
-  __TEXT.__unwind_info: 0xddf0
+  __TEXT.__gcc_except_tab: 0x5278
+  __TEXT.__cstring: 0x593a9
+  __TEXT.__oslogstring: 0x51eb0
+  __TEXT.__objc_classname: 0x52de
+  __TEXT.__objc_methname: 0x695f1
+  __TEXT.__objc_methtype: 0x10712
+  __TEXT.__ustring: 0xb6
+  __TEXT.__unwind_info: 0xdeb8
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__const: 0x15688
-  __DATA_CONST.__cfstring: 0x13600
+  __DATA_CONST.__const: 0x15740
+  __DATA_CONST.__cfstring: 0x137c0
   __DATA_CONST.__objc_classlist: 0xd78
   __DATA_CONST.__objc_catlist: 0x638
   __DATA_CONST.__objc_protolist: 0x738

   __DATA_CONST.__objc_superrefs: 0xb30
   __DATA_CONST.__objc_arraydata: 0x520
   __DATA_CONST.__objc_arrayobj: 0x1c8
-  __DATA_CONST.__objc_intobj: 0x8a0
+  __DATA_CONST.__objc_intobj: 0x8b8
   __DATA_CONST.__objc_dictobj: 0x2f8
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA_CONST.__auth_got: 0x1d78
-  __DATA_CONST.__got: 0x4000
+  __DATA_CONST.__auth_got: 0x1d90
+  __DATA_CONST.__got: 0x4008
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA.__objc_const: 0x36908
-  __DATA.__objc_selrefs: 0x168a8
-  __DATA.__objc_ivar: 0x2940
+  __DATA.__objc_const: 0x36bc8
+  __DATA.__objc_selrefs: 0x16a88
+  __DATA.__objc_ivar: 0x2988
   __DATA.__objc_data: 0x86b0
   __DATA.__data: 0x5e40
   __DATA.__common: 0xa18

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 15524
-  Symbols:   3095
-  CStrings:  29776
+  Functions: 15588
+  Symbols:   3099
+  CStrings:  29933
 
Symbols:
+ _AFIsLinwoodCandidateHomePodWithoutLinwood
+ _AFPreferencesSetRecognizedSpeakerTwentyFourHourTimeDisplay
+ _AFRecognizedSpeakerHasNoTwentyFourHourTimeChoice
+ _AFUsesRecognizedSpeakerTwentyFourHourTime
+ _OBJC_CLASS_$_AFDisambiguationOutcomeDescriptor
- _OBJC_CLASS_$_FTSnippetServiceManager
CStrings:
+ "%s #SiriAvailability candidate HomePod cannot run Linwood: skipping GMS and AuthKit checks, siriLinwoodCapabilities=%{public}@"
+ "%s #rdar191712659 [%{public}s] Siri classic does not support this HomePod locale and Linwood is not supported: dismissing Siri with reason AFDismissalAssetsNotReady"
+ "%s Activating a peer's selection on request %@"
+ "%s Called off ADCommandCenterQueue, ending there. context = %@"
+ "%s Cancelling the stall retry of zone %@ for a new fetch"
+ "%s Cloud sync is off; skipping mirror sync for (%@)"
+ "%s Companion Siri availability record saved %{public}@, before the companion's last upload at %{public}@: left by an earlier companion, read as absent"
+ "%s Could not archive the selection: %@"
+ "%s Deferred releasing audio session until recording stops (speechState = %@)."
+ "%s Deferred service reset still waiting for %lu newer remote execution context(s)"
+ "%s Deferring service reset until %lu remote execution context(s) end"
+ "%s Fetch for zone %@ abandoned; retrying in %.0f seconds"
+ "%s FlowToolsSnippetService is not installed, not starting the snippet service manager"
+ "%s Ignoring a selection for request %@ from %{private}@, which it was not relayed to"
+ "%s Ignoring a selection for request %@, which this device is not relaying"
+ "%s Ignoring a selection for request %@, which was cancelled"
+ "%s Last remote execution context ended, running the deferred service reset if idle"
+ "%s Malformed selection from a peer"
+ "%s Not noting relayed views for request %@: no IDS id for the target"
+ "%s Not noting relayed views: peer id %d, request id %d"
+ "%s Not retrying zone %@ after %lu retries"
+ "%s Not retrying zone %@: another account's fetch kept it busy"
+ "%s Not retrying zone %@: its account is no longer tracked"
+ "%s Not sending %@ with refId=%@: this command is not associated with the current SASMUXStartAsrOnServerRequest"
+ "%s Peer did not take the selection: %@"
+ "%s Peer's selection for request %@ activated: %d, error: %@"
+ "%s Recognized speaker twentyFourHourTimeDisplay changed to %@"
+ "%s Refusing a remote peer's request with text (%d) or an unshowable name (name length %lu)"
+ "%s Relayed views expired; starting the selection here"
+ "%s Relaying views for request %@ to %{private}@"
+ "%s Remote execution context still active %.0fs after a service reset was deferred behind it; ending it. executionID=%{public}@"
+ "%s Remote peer is not owned by the current user; asking the user before starting its request (it asked itself: %d)"
+ "%s Request %@ cancelled (%ld); holding the selection for %@ until another request takes over"
+ "%s Request %@ ended; no longer taking a selection for %@"
+ "%s Request %@ took over from cancelled request %@"
+ "%s Scheduling mirrored zone setup for (%@)"
+ "%s Sending ASR request to server with requestId = %@, inputOrigin = %{public}@"
+ "%s Sending the selection back to the peer for request %@"
+ "%s Showing views relayed by %@ for request %@"
+ "%s remote request %@: sender owned by the current user %d, named by Rapport %d"
+ "+[ADAccount _accountForIdentifier:infoDictionary:instanceContext:isReadOnly:isCoupledToHost:keychainIsReadable:]"
+ "-[ADCloudKitManager _scheduleMirroredZoneSetupIfNeededForZoneInfo:]"
+ "-[ADCloudKitManager _scheduleStalledFetchCheckForZoneInfo:account:generation:delay:retryFetch:completion:]_block_invoke"
+ "-[ADCloudKitManager _scheduleStalledFetchRetryForZoneInfo:account:afterGeneration:delay:waitsLeft:retryFetch:]_block_invoke"
+ "-[ADCommandCenter _commandShouldNotBeSentForHomePodServerAsrRequest:]"
+ "-[ADCommandCenter _handleExternalActivationRequest:fromRemotePeer:ownedByCurrentUser:solicitedReply:completion:]"
+ "-[ADCommandCenter _performDeferredServicesResetBackstopForGeneration:executionIDs:]"
+ "-[ADCommandCenter _publishSelectedSpeakerTwentyFourHourTimeDisplay]"
+ "-[ADCommandCenter _resetServicesIfIdle]"
+ "-[ADCommandCenter sendMuxAsrRequestToServer:inputOrigin:]_block_invoke"
+ "-[ADCommandCenter(RelayedPick) _relayedPick_currentRequestDidChangeFrom:to:]"
+ "-[ADCommandCenter(RelayedPick) _relayedPick_forwardRequestIfNeeded:delegate:completion:]"
+ "-[ADCommandCenter(RelayedPick) _relayedPick_noteOutgoingRemoteRequest:executionContext:]"
+ "-[ADCommandCenter(RelayedPick) _relayedPick_noteRemoteCommand:fromPeer:remoteExecutionInfo:]"
+ "-[ADCommandCenter(RelayedPick) _relayedPick_requestWasCancelledWithRequestID:reason:successorInfo:]"
+ "-[ADCommandCenter(RelayedPick) _relayedPick_startSelection:forRequestID:fromPeerWithIDSIdentifier:]"
+ "-[ADCommandCenter(RelayedPick) _relayedPick_startSelection:forRequestID:fromPeerWithIDSIdentifier:]_block_invoke"
+ "-[ADCommandCenter(RelayedPick) handleMessage:messageType:fromDeviceWithIdentifier:completion:]"
+ "-[ADDaemon _setupFlowToolsSnippetService]"
+ "-[ADSpeechManager _handleCoordinatorReleaseRequestFromCoordinator:]"
+ "-[ADSpeechManager _releaseSessionIfDeferredUntilRecordingStopped]"
+ "34"
+ "ADMultiUserExplicitContentDidChangeNotification"
+ "ADMultiUserTwentyFourHourTimeDisplayDidChangeNotification"
+ "AddViews"
+ "FTSnippetServiceManager"
+ "Hk"
+ "MobileAssistantDaemons-3610.19.4"
+ "RelayedPick"
+ "Remote request is not allowed."
+ "T@\"NSDictionary\",C,V_twentyFourHourTimeDisplayBySharedUserID"
+ "T@\"NSMutableDictionary\",&,N,V_fetchGenerationByAccount"
+ "T@\"NSMutableDictionary\",&,N,V_stalledFetchRetryCountByAccount"
+ "T@\"NSString\",C,N,V_stalledFetchRetryAccount"
+ "T@?,C,N,V_stalledFetchRetryFetch"
+ "TB,V_siriClassicUnsupportedInLocale"
+ "TQ,N,V_stalledFetchRetryGeneration"
+ "This device does not take its Siri AI access from a companion"
+ "_ADRelayedPickSendMessage_block_invoke"
+ "_accountForIdentifier:infoDictionary:instanceContext:isReadOnly:isCoupledToHost:"
+ "_accountForIdentifier:infoDictionary:instanceContext:isReadOnly:isCoupledToHost:keychainIsReadable:"
+ "_accountOfFetchContainer:"
+ "_allowExplicitContentForUser:homeKitValue:"
+ "_commandShouldNotBeSentForHomePodServerAsrRequest:"
+ "_deferredServicesResetGeneration"
+ "_fetchGenerationByAccount"
+ "_firingSleepTimerIDsInTimers:"
+ "_handleCoordinatorReleaseRequestFromCoordinator:"
+ "_handleExternalActivationRequest:fromRemotePeer:ownedByCurrentUser:solicitedReply:completion:"
+ "_hasActiveRemoteExecutionContext"
+ "_heldEndpointFeaturesDelivery"
+ "_isContainerTracked:"
+ "_isHomePodLocaleWithoutSiriClassicForRequest"
+ "_needsServicesResetAfterRemoteExecution"
+ "_performDeferredServicesResetBackstopForGeneration:executionIDs:"
+ "_publishSelectedSpeakerTwentyFourHourTimeDisplay"
+ "_publishTwentyFourHourTimeDisplayBySharedUserID"
+ "_publishedSpeakerTwentyFourHourTimeDisplay"
+ "_relayedPickNotedTime"
+ "_relayedPickOutgoingCancelled"
+ "_relayedPickOutgoingPeerIDSIdentifier"
+ "_relayedPickOutgoingRequestID"
+ "_relayedPickOutgoingTime"
+ "_relayedPickPeerIDSIdentifier"
+ "_relayedPickPeerRequestID"
+ "_relayedPick_clear"
+ "_relayedPick_clearOutgoing"
+ "_relayedPick_currentRequestDidChangeFrom:to:"
+ "_relayedPick_forwardRequestIfNeeded:delegate:completion:"
+ "_relayedPick_noteOutgoingRemoteRequest:executionContext:"
+ "_relayedPick_noteRemoteCommand:fromPeer:remoteExecutionInfo:"
+ "_relayedPick_requestWasCancelledWithRequestID:reason:successorInfo:"
+ "_relayedPick_startListening"
+ "_relayedPick_startSelection:forRequestID:fromPeerWithIDSIdentifier:"
+ "_releaseSessionIfDeferredUntilRecordingStopped"
+ "_resetServicesIfIdle"
+ "_scheduleDeferredServicesResetBackstop"
+ "_scheduleMirroredZoneSetupIfNeededForZoneInfo:"
+ "_scheduleStalledFetchCheckForZoneInfo:account:generation:delay:retryFetch:completion:"
+ "_scheduleStalledFetchRetryForZoneInfo:account:afterGeneration:delay:waitsLeft:retryFetch:"
+ "_serverHeardNothingWithEndpointFeatures:"
+ "_siriClassicUnsupportedInLocale"
+ "_speakerTwentyFourHourTimeDisplayForSharedUserID:bySharedUserID:"
+ "_stalledFetchRetryAccount"
+ "_stalledFetchRetryCountByAccount"
+ "_stalledFetchRetryFetch"
+ "_stalledFetchRetryGeneration"
+ "_stalledFetchRetryLimit"
+ "_twentyFourHourTimeDisplayBySharedUserID"
+ "_twentyFourHourTimeDisplayBySharedUserIDForUsers:"
+ "_twentyFourHourTimeDisplayDidChange:"
+ "_twentyFourHourTimeDisplayForRegion:"
+ "_twentyFourHourTimeDisplayForSettings:"
+ "addCharactersInRange:"
+ "addCharactersInString:"
+ "characterSetWithCharactersInString:"
+ "com.apple.assistantd/voiceid.mirror.cache"
+ "controlCharacterSet"
+ "dateFormatFromTemplate:options:locale:"
+ "descriptor"
+ "fetchAvailabilityEnsuringCompanionAvailability:completion:"
+ "fetchCompanionSiriAvailabilityForSetup:completion:"
+ "fetchGenerationByAccount"
+ "formUnionWithCharacterSet:"
+ "homeDidUpdateUnrecognizedUserSettings:"
+ "interruptAudio"
+ "invertedSet"
+ "isHomePodLocaleWithoutSiriClassic:"
+ "isLinwoodCandidateHomePodWithoutLinwood"
+ "j"
+ "newlineCharacterSet"
+ "rangeOfCharacterFromSet:"
+ "relayedpick"
+ "removeCharactersInString:"
+ "sendMuxAsrRequestToServer:inputOrigin:"
+ "setFetchGenerationByAccount:"
+ "setSiriClassicUnsupportedInLocale:"
+ "setStalledFetchRetryAccount:"
+ "setStalledFetchRetryCountByAccount:"
+ "setStalledFetchRetryFetch:"
+ "setStalledFetchRetryGeneration:"
+ "setTwentyFourHourTimeDisplayBySharedUserID:"
+ "siriClassicUnsupportedInLocale"
+ "stalledFetchRetryAccount"
+ "stalledFetchRetryCountByAccount"
+ "stalledFetchRetryFetch"
+ "stalledFetchRetryGeneration"
+ "twentyFourHourTimeDisplayBySharedUserID"
+ "v16@?0@\"AFSiriAvailability\"8"
+ "v32@0:8@\"AFSiriAvailability\"16@?<v@?@\"AFSiriAvailability\"@\"NSError\">24"
+ "v44@0:8@16B24B28B32@?36"
+ "v64@0:8@16@24Q32d40@?48@?56"
+ "v64@0:8@16@24Q32d40Q48@?56"
+ "͏ᅟᅠ឴឵⠀ㅤﾠ"
+ "\u200c\u200d\u200e\u200f\u061c"
- "%s #SiriAvailability Migrating implicit Linwood opt-in: writing @NO to Enable Offline Mode For Apple Intelligence"
- "+[ADAccount _accountForIdentifier:infoDictionary:intanceContext:isReadOnly:isCoupledToHost:keychainIsReadable:]"
- "-[ADCloudKitManager _fetchChangesWithZoneInfo:retryCount:useSharedDatabase:activity:container:mirror:completion:]_block_invoke_3"
- "-[ADCloudKitManager _scheduleStalledFetchCheckForZoneInfo:generation:delay:completion:]_block_invoke"
- "-[ADCloudKitManager _setUpMirroredZoneWithZoneInfo:]_block_invoke_2"
- "-[ADCommandCenter _handleExternalActivationRequest:fromRemotePeer:ownedByCurrentUser:completion:]"
- "-[ADCommandCenter sendMuxAsrRequestToServer:]_block_invoke"
- "-[ADSpeechManager audioSessionCoordinator:releaseAudioSessionWithContext:]_block_invoke"
- "16"
- "MobileAssistantDaemons-3610.11.2"
- "_accountForIdentifier:infoDictionary:intanceContext:isReadOnly:isCoupledToHost:"
- "_accountForIdentifier:infoDictionary:intanceContext:isReadOnly:isCoupledToHost:keychainIsReadable:"
- "_handleExternalActivationRequest:fromRemotePeer:ownedByCurrentUser:completion:"
- "_scheduleStalledFetchCheckForZoneInfo:generation:delay:completion:"
- "appleIntelligenceFallbackExplicitlySet"
- "sendMuxAsrRequestToServer:"
- "setAppleIntelligenceFallback:"
- "v48@0:8@16Q24d32@?40"
```
