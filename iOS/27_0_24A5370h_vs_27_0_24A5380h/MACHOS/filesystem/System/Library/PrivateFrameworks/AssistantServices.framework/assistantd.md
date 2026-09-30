## assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

-  __TEXT.__text: 0x36ecc4
-  __TEXT.__auth_stubs: 0x37a0
-  __TEXT.__objc_stubs: 0x46fe0
+  __TEXT.__text: 0x36e7c0
+  __TEXT.__auth_stubs: 0x37d0
+  __TEXT.__objc_stubs: 0x47140
   __TEXT.__objc_methlist: 0x234f8
   __TEXT.__const: 0xed40
   __TEXT.__dlopen_cstrs: 0x99d
-  __TEXT.__gcc_except_tab: 0x3a7c
-  __TEXT.__cstring: 0x528d6
-  __TEXT.__oslogstring: 0x45166
-  __TEXT.__objc_classname: 0x5209
-  __TEXT.__objc_methname: 0x612cd
-  __TEXT.__objc_methtype: 0xfe2f
+  __TEXT.__gcc_except_tab: 0x3a70
+  __TEXT.__cstring: 0x528d7
+  __TEXT.__oslogstring: 0x4575a
+  __TEXT.__objc_classname: 0x51f9
+  __TEXT.__objc_methname: 0x61552
+  __TEXT.__objc_methtype: 0xfed8
   __TEXT.__ustring: 0x32
-  __TEXT.__unwind_info: 0xa498
+  __TEXT.__unwind_info: 0xa468
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__const: 0x142f8
+  __DATA_CONST.__const: 0x14338
   __DATA_CONST.__cfstring: 0x12240
-  __DATA_CONST.__objc_classlist: 0xd48
+  __DATA_CONST.__objc_classlist: 0xd40
   __DATA_CONST.__objc_catlist: 0x630
   __DATA_CONST.__objc_protolist: 0x730
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x98
-  __DATA_CONST.__objc_superrefs: 0xb18
-  __DATA_CONST.__objc_arraydata: 0x478
-  __DATA_CONST.__objc_arrayobj: 0x180
-  __DATA_CONST.__objc_intobj: 0x8d0
+  __DATA_CONST.__objc_superrefs: 0xb10
+  __DATA_CONST.__objc_arraydata: 0x480
+  __DATA_CONST.__objc_arrayobj: 0x198
+  __DATA_CONST.__objc_intobj: 0x8b8
   __DATA_CONST.__objc_dictobj: 0x2f8
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA_CONST.__auth_got: 0x1be0
-  __DATA_CONST.__got: 0x3cd8
+  __DATA_CONST.__auth_got: 0x1bf8
+  __DATA_CONST.__got: 0x3e80
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA.__objc_const: 0x34c28
-  __DATA.__objc_selrefs: 0x15440
+  __DATA.__objc_const: 0x34b48
+  __DATA.__objc_selrefs: 0x154a8
   __DATA.__objc_ivar: 0x2670
-  __DATA.__objc_data: 0x84d0
+  __DATA.__objc_data: 0x8480
   __DATA.__data: 0x5da0
-  __DATA.__bss: 0xdc0
+  __DATA.__bss: 0xdb0
   __DATA.__common: 0xa18
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation
   - /System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets
+  - /System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices
   - /System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures
   - /System/Library/PrivateFrameworks/ContactsAssistantServices.framework/ContactsAssistantServices
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 14573
-  Symbols:   2994
-  CStrings:  30385
+  Functions: 14562
+  Symbols:   2998
+  CStrings:  30406
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_ivar : content changed
~ __DATA.__data : content changed
~ __DATA.__common : content changed
Symbols:
+ _AFIsIPad
+ _AFIsLinwoodEnabledAndWasEverAvailable
+ _AFVisualIntelligenceCameraRestricted
+ _MCFeatureAssistantAllowed
+ _NSStringFromAFSiriVisualIntelligenceCapabilities
+ _OBJC_CLASS_$_AFAuthKitManager
+ _OBJC_CLASS_$_CHSControlService
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
+ "%s #TypeToSiriWidget #Availability reloading controls"
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
+ "+[AFRequestInfo(ADAnnouncementRequestBuilder) entityIdentifierTuplesForRequestStack:types:bundleIDs:instanceIDs:notifications:notificationAppIDs:]"
+ "-[ADAssetManager fetchAssetsAvailabilityForLanguage:completion:]_block_invoke_2"
+ "-[ADClientConnection _clearContextAndStartAssistantSessionWithSessionId:invocationContext:]"
+ "-[ADClientConnection clearContextWithInvocationContext:]"
+ "-[ADClientConnection resumeSessionWithId:invocationContext:]"
+ "-[ADCommandCenter _handleServiceCommand:afterDeviceSelectionDecision:executionContext:completion:]"
+ "-[ADCommandCenter _handleServiceCommand:afterDeviceSelectionDecision:executionContext:completion:]_block_invoke"
+ "-[ADCommandCenter _handleServiceCommand:afterDeviceSelectionDecision:executionContext:completion:]_block_invoke_3"
+ "-[ADCommandCenter _requestDispatcherSessionConfigurationWithInvocationContext:]_block_invoke"
+ "-[ADSiriCapabilitiesStore createVisualIntelligenceCapabilitiesForLocale:]"
+ "-[ADSiriCapabilitiesStore updateVisualIntelligenceCapabilities:]"
+ "External activation request was superseded by a newer one."
+ "MobileAssistantDaemons-3600.68.39.1.1"
+ "ReloadControlCenterControls"
+ "Request reload due to siriAvailability runtime change"
+ "SISchemaVoiceExpressivityFromAFVoiceExpressivityPreset:"
+ "SISchemaVoicePaceFromAFVoicePacePreset:"
+ "TB,V_osEligibilitySiriModeCached"
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
+ "_osEligibilitySiriModeCached"
+ "_preemptedByOverlappingRequest"
+ "_requestDispatcherSessionConfigurationWithInvocationContext:"
+ "_voiceProfileSyncSupported"
+ "blockAttending"
+ "clearContextWithInvocationContext:"
+ "com.apple.Settings.AppleIntelligence"
+ "com.apple.siri.TypeToSiriWidget"
+ "copyBootSessionUUID"
+ "createVisualIntelligenceCapabilitiesForLocale:"
+ "currentAccountType"
+ "encodeUserNotificationEntityValuesWithNotifications:appIDs:error:"
+ "entityIdentifierTuplesForRequestStack:types:bundleIDs:instanceIDs:notifications:notificationAppIDs:"
+ "expressivityPreset"
+ "initWithStatus:restrictionReasons:isAvailable:siriLocale:desiredOrchestrationMode:desiredOrchestrationModeIfEnabled:currentOrchestrationMode:unavailabilityReasons:allCapabilities:linwoodEverAvailable:bootUUID:"
+ "invocationContext"
+ "isGreyMatterEligible"
+ "osEligibilitySiriModeCached"
+ "pacePreset"
+ "protoAgeRange"
+ "reloadControlsForExtension:kind:reason:"
+ "resumeSessionWithId:invocationContext:"
+ "setAssetManagerForTesting:"
+ "setExpressivity:"
+ "setInvocationContext:"
+ "setOsEligibilitySiriModeCached:"
+ "setPace:"
+ "stopSpeechCaptureForEvent:suppressAlert:hostTime:blockAttending:"
+ "userAggregationId not yet available. Refreshing."
+ "v40@0:8q16B24Q28B36"
+ "v48@0:8@16q24B32Q36B44"
+ "v64@0:8@16^@24^@32^@40^@48^@56"
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
- "+[AFRequestInfo(ADAnnouncementRequestBuilder) entityIdentifierTuplesForRequestStack:types:bundleIDs:instanceIDs:]"
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
- "ADMyriadService"
- "MobileAssistantDaemons-3600.68.16.1.1"
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
- "entityIdentifierTuplesForRequestStack:types:bundleIDs:instanceIDs:"
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
- "v48@0:8@16^@24^@32^@40"
- "v64@0:8{ADSiriCapabilitiesState=QQQQ@Q}16"
- "{ADSiriCapabilitiesState=\"orchestrationMode\"Q\"siriXFullUnderstandingOnDeviceCapabilities\"Q\"siriXHybridUnderstandingOnDeviceCapabilities\"Q\"siriSystemAssistantExperienceCapabilities\"Q\"siriAvailability\"@\"AFSiriAvailability\"\"siriLinwoodCapabilities\"Q}"
- "{ADSiriCapabilitiesState=QQQQ@Q}16@0:8"

```
