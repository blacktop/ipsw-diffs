## assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/Support/assistantd`

```diff

-  __TEXT.__text: 0x537098
-  __TEXT.__auth_stubs: 0x3170
-  __TEXT.__objc_stubs: 0x42140
-  __TEXT.__objc_methlist: 0x216ac
-  __TEXT.__cstring: 0x49aa1
-  __TEXT.__const: 0xa2eb0
+  __TEXT.__text: 0x536904
+  __TEXT.__auth_stubs: 0x31b0
+  __TEXT.__objc_stubs: 0x42220
+  __TEXT.__objc_methlist: 0x2168c
+  __TEXT.__cstring: 0x49a2a
+  __TEXT.__const: 0xa2ec0
   __TEXT.__dlopen_cstrs: 0x56f
-  __TEXT.__gcc_except_tab: 0x30b0
-  __TEXT.__oslogstring: 0x3de6c
-  __TEXT.__objc_classname: 0x4dfd
-  __TEXT.__objc_methname: 0x5abae
-  __TEXT.__objc_methtype: 0xeabf
+  __TEXT.__gcc_except_tab: 0x30a0
+  __TEXT.__oslogstring: 0x3e42a
+  __TEXT.__objc_classname: 0x4ded
+  __TEXT.__objc_methname: 0x5ad2e
+  __TEXT.__objc_methtype: 0xeb60
   __TEXT.__ustring: 0x32
-  __TEXT.__unwind_info: 0x9610
+  __TEXT.__unwind_info: 0x95e8
   __TEXT.__eh_frame: 0x140
-  __DATA_CONST.__const: 0x22fb0
+  __DATA_CONST.__const: 0x22ff0
   __DATA_CONST.__cfstring: 0x11280
-  __DATA_CONST.__objc_classlist: 0xcb8
+  __DATA_CONST.__objc_classlist: 0xcb0
   __DATA_CONST.__objc_catlist: 0x630
   __DATA_CONST.__objc_protolist: 0x6a8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0xaa0
-  __DATA_CONST.__objc_arraydata: 0x418
-  __DATA_CONST.__objc_arrayobj: 0x168
-  __DATA_CONST.__objc_intobj: 0x7c8
+  __DATA_CONST.__objc_superrefs: 0xa98
+  __DATA_CONST.__objc_arraydata: 0x420
+  __DATA_CONST.__objc_arrayobj: 0x180
+  __DATA_CONST.__objc_intobj: 0x7b0
   __DATA_CONST.__objc_dictobj: 0x2f8
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA_CONST.__auth_got: 0x18c8
-  __DATA_CONST.__got: 0x3828
+  __DATA_CONST.__auth_got: 0x18e8
+  __DATA_CONST.__got: 0x39b8
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA.__objc_const: 0x320d8
-  __DATA.__objc_selrefs: 0x13c30
-  __DATA.__objc_ivar: 0x2460
-  __DATA.__objc_data: 0x7f30
+  __DATA.__objc_const: 0x31fc8
+  __DATA.__objc_selrefs: 0x13c78
+  __DATA.__objc_ivar: 0x245c
+  __DATA.__objc_data: 0x7ee0
   __DATA.__data: 0x5a38
-  __DATA.__bss: 0x9b8
+  __DATA.__bss: 0x9a8
   __DATA.__common: 0x1420
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/AVRouting.framework/Versions/A/AVRouting

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 13771
-  Symbols:   2748
-  CStrings:  28002
+  Functions: 13759
+  Symbols:   2752
+  CStrings:  28015
 
Sections:
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__data : content changed
Symbols:
+ _AFIsIPad
+ _AFIsLinwoodEnabledAndWasEverAvailable
+ _AFVisualIntelligenceCameraRestricted
+ _CFPreferencesAppValueIsForced
+ _NSStringFromAFSiriVisualIntelligenceCapabilities
+ _OBJC_CLASS_$_AFAuthKitManager
+ _kAFAssistantApplicationAccessDomain
- _AFMyriadMonitorDecisionGetWaitTime
- _OBJC_CLASS_$_AFSpeechConnectionRequestContext
- _kAFStereoPartnerMyriadDataDidChangeDarwinNotification
CStrings:
+ "%012llX"
+ "%s #SiriAvailability CampoInstalled check: SiriApp=%{bool}d"
+ "%s #SiriAvailability GMAvailabilityWrapper class is not loaded — skipping disablement/access checks, treating as UseCaseNotDisabled and NotAccessRestricted"
+ "%s #SiriAvailability GMAvailabilityWrapper class is not loaded — treating GMS as unavailable"
+ "%s #SiriAvailability GMS disablement / access-not-granted use case calls skipped due to nil locale"
+ "%s #SiriAvailability GMS disablement use case call returned true, GMS availability will be reset to 0"
+ "%s #SiriAvailability childAccountRestricted=%{bool}d (isChildAccount=%{bool}d isChildProtoState=%{bool}d NotChildAccount=%{bool}d)"
+ "%s #SiriAvailability done: siriLinwoodCapabilities=%@ (%{public}@)"
+ "%s #SiriAvailability isUseCaseAccessNotGrantedSecure(com.apple.Siri.EnhancedSiriDisablement)=%{bool}d (NotAccessRestricted=%{bool}d)"
+ "%s #SiriAvailability isUseCaseDisabled(com.apple.Siri.EnhancedSiriDisablement)=%{bool}d (UseCaseNotDisabled=%{bool}d)"
+ "%s #SiriAvailability locale is nil for identifier %{public}@ — skipping GMS calls, GMSAvailable stays unavailable"
+ "%s #SiriAvailability useCaseIdentifiers=%{public}@ currentWithUseCaseIdentifiers=%ld (GMSAvailable=%{bool}d) enabledWithUseCaseIdentifiers=%{bool}d (SettingTurnedOn=%{bool}d)"
+ "%s #SiriAvailability userSettingOn=%{bool}d locale=%{public}@ languageCode=%{public}@"
+ "%s #modes Ambient session (Linwood: VoiceOnly)"
+ "%s %p invocationContext=%@"
+ "%s %p sessionId:%@ invocationContext=%@"
+ "%s Async asset fetch timed out after %.1fs; delivering best-known status for '%{public}@'"
+ "%s Locale is nil, not checking AppleIntelligence GMS use case for visual intelligence."
+ "%s Skipping audio session deactivation: overlapping Siri request is taking over"
+ "%s Superseding prior external activation %@ before handling %@"
+ "%s Timed out after %.1fs waiting for asset delegates; returning best-known asset status for '%{public}@'"
+ "%s Updated capabilities visualIntelligenceCapabilities to %@"
+ "%s Wait for device selection decision: %d  with reason: %@"
+ "%s _clearContextAndStartAssistantSessionWithSessionId: called without invocationContext (legacy path), sessionId:%@"
+ "%s clearContext: called without invocationContext (legacy path)"
+ "%s resumeSessionWithId: called without invocationContext (legacy path), sessionId:%@"
+ "-[ADAssetManager fetchAssetsAvailabilityForLanguage:completion:]_block_invoke"
+ "-[ADClientConnection _clearContextAndStartAssistantSessionWithSessionId:invocationContext:]"
+ "-[ADClientConnection clearContextWithInvocationContext:]"
+ "-[ADClientConnection resumeSessionWithId:invocationContext:]"
+ "-[ADCommandCenter _handleServiceCommand:afterDeviceSelectionDecision:executionContext:completion:]"
+ "-[ADCommandCenter _handleServiceCommand:afterDeviceSelectionDecision:executionContext:completion:]_block_invoke"
+ "-[ADCommandCenter _handleServiceCommand:afterDeviceSelectionDecision:executionContext:completion:]_block_invoke_3"
+ "-[ADCommandCenter _requestDispatcherSessionConfigurationWithInvocationContext:]_block_invoke"
+ "-[ADSiriCapabilitiesStore createVisualIntelligenceCapabilitiesForLocale:]"
+ "-[ADSiriCapabilitiesStore updateVisualIntelligenceCapabilities:]"
+ "36"
+ "Assistant Allowed"
+ "External activation request was superseded by a newer one."
+ "MobileAssistantDaemons-3600.68.39"
+ "SISchemaVoiceExpressivityFromAFVoiceExpressivityPreset:"
+ "SISchemaVoicePaceFromAFVoicePacePreset:"
+ "T{ADSiriCapabilitiesState=QQQQ@QQ},V_currentState"
+ "Vv24@0:8@\"AFInvocationContext\"16"
+ "Vv32@0:8@\"NSString\"16@\"AFInvocationContext\"24"
+ "_assetFetchWaitBackstopSeconds"
+ "_clearContextAndStartAssistantSessionWithInvocationContext:"
+ "_clearContextAndStartAssistantSessionWithSessionId:invocationContext:"
+ "_dispatchStopOnSource:event:suppressAlert:hostTime:blockAttending:"
+ "_handleServiceCommand:afterDeviceSelectionDecision:executionContext:completion:"
+ "_injectedAssetManager"
+ "_isLinwoodEnabledAndWasEverAvailable"
+ "_preemptedByOverlappingRequest"
+ "_requestDispatcherSessionConfigurationWithInvocationContext:"
+ "_voiceProfileSyncSupported"
+ "allowAssistant"
+ "blockAttending"
+ "clearContextWithInvocationContext:"
+ "com.apple.Settings.AppleIntelligence"
+ "copyBootSessionUUID"
+ "createVisualIntelligenceCapabilitiesForLocale:"
+ "currentAccountType"
+ "expressivityPreset"
+ "initWithStatus:restrictionReasons:isAvailable:siriLocale:desiredOrchestrationMode:desiredOrchestrationModeIfEnabled:currentOrchestrationMode:unavailabilityReasons:allCapabilities:linwoodEverAvailable:bootUUID:"
+ "invocationContext"
+ "isGreyMatterEligible"
+ "pacePreset"
+ "protoAgeRange"
+ "resumeSessionWithId:invocationContext:"
+ "setAssetManagerForTesting:"
+ "setExpressivity:"
+ "setInvocationContext:"
+ "setPace:"
+ "stopSpeechCaptureForEvent:suppressAlert:hostTime:blockAttending:"
+ "userAggregationId not yet available. Refreshing."
+ "v40@0:8q16B24Q28B36"
+ "v48@0:8@16q24B32Q36B44"
+ "v72@0:8{ADSiriCapabilitiesState=QQQQ@QQ}16"
+ "{ADSiriCapabilitiesState=\"orchestrationMode\"Q\"siriXFullUnderstandingOnDeviceCapabilities\"Q\"siriXHybridUnderstandingOnDeviceCapabilities\"Q\"siriSystemAssistantExperienceCapabilities\"Q\"siriAvailability\"@\"AFSiriAvailability\"\"siriLinwoodCapabilities\"Q\"siriVisualIntelligenceCapabilities\"Q}"
+ "{ADSiriCapabilitiesState=QQQQ@QQ}16@0:8"
- "%2llX"
- "%s CampoInstalled check: SiriApp=%{bool}d"
- "%s Fetching SAE assets availability for %@ locale"
- "%s GMS access not granted use case call returned true, setting capability"
- "%s GMS disablement use case call returned true, GMS availability will be reset to 0"
- "%s GMS disablement use case method call skipped due to nil locale"
- "%s No stereo partner"
- "%s Received malformed lastWin data"
- "%s Received message from device not in stereo pair: %@"
- "%s Received message with unhandled method type: %ld"
- "%s Received message with unknown method name: %@"
- "%s Request failed: %@"
- "%s Stereo partner changed since request initiated"
- "%s Updated capabilities siriLinwoodCapabilities capabilities to %@"
- "%s Wait for Myriad decision: %d  with reason: %@"
- "%s lastWin changed to: %@"
- "%s stereo partner changed to: %@"
- "-[ADCommandCenter _handleServiceCommand:afterMyriadDecision:executionContext:completion:]"
- "-[ADCommandCenter _handleServiceCommand:afterMyriadDecision:executionContext:completion:]_block_invoke"
- "-[ADCommandCenter _handleServiceCommand:afterMyriadDecision:executionContext:completion:]_block_invoke_3"
- "-[ADCommandCenter _requestDispatcherSessionConfiguration]_block_invoke"
- "-[ADMyriadService _handleLastWinRequest:completion:]"
- "-[ADMyriadService _handleMessage:messageType:fromDeviceWithIdentifier:completion:]"
- "-[ADMyriadService _handleRequest:fromDeviceWithIdentifier:completion:]"
- "-[ADMyriadService _setLastTimeStereoPartnerWon:]"
- "-[ADMyriadService _setStereoPartnerIdentifier:]"
- "-[ADMyriadService _stereoConfigurationDidChangeNotification:]"
- "-[ADMyriadService _syncLastWinWithStereoPartner]"
- "-[ADMyriadService _syncLastWinWithStereoPartner]_block_invoke"
- "-[ADMyriadService _syncLastWinWithStereoPartner]_block_invoke_2"
- "-[ADMyriadService setMyriadDecisionResult:]"
- "-[ADSettingsClient areSiriSAEAssetsAvailable:]_block_invoke"
- "2"
- "ADMyriadService"
- "MobileAssistantDaemons-3600.68.16.4.1"
- "Myriad Service Queue"
- "T@\"NSArray\",C,N,V_inlineItemList"
- "T{ADSiriCapabilitiesState=QQQQ@Q},V_currentState"
- "_clearContextAndStartAssistantSession"
- "_handleLastWinRequest:completion:"
- "_handleRequest:fromDeviceWithIdentifier:completion:"
- "_handleServiceCommand:afterMyriadDecision:executionContext:completion:"
- "_inlineItemList"
- "_lastTimeStereoPartnerWon"
- "_lastTimeWon"
- "_setLastMyriadWin:"
- "_setLastTimeStereoPartnerWon:"
- "_setStereoPartnerIdentifier:"
- "_stereoConfigurationDidChangeNotification:"
- "_stereoPartnerIdentifier"
- "_syncLastWinWithStereoPartner"
- "deleteAllDESRecordsForDictationPersonalization"
- "dictionaryWithObjectsAndKeys:"
- "initWithIsAvailable:siriLocale:desiredOrchestrationMode:desiredOrchestrationModeIfEnabled:currentOrchestrationMode:unavailabilityReasons:allCapabilities:linwoodEverAvailable:"
- "initWithRequestId:"
- "isGMEligible"
- "lastMyriadWinForStereoPartner:"
- "lastWin"
- "methodName"
- "methodType"
- "myriad"
- "setMyriadDecisionResult:"
- "userAggregationId not yet available. Dispatching to queue to fetch."
- "v24@?0@\"NSDate\"8@\"NSError\"16"
- "v64@0:8{ADSiriCapabilitiesState=QQQQ@Q}16"
- "{ADSiriCapabilitiesState=\"orchestrationMode\"Q\"siriXFullUnderstandingOnDeviceCapabilities\"Q\"siriXHybridUnderstandingOnDeviceCapabilities\"Q\"siriSystemAssistantExperienceCapabilities\"Q\"siriAvailability\"@\"AFSiriAvailability\"\"siriLinwoodCapabilities\"Q}"
- "{ADSiriCapabilitiesState=QQQQ@Q}16@0:8"

```
