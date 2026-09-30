## assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

-3500.120.4.11.1
-  __TEXT.__text: 0x36df64
-  __TEXT.__auth_stubs: 0x34b0
-  __TEXT.__objc_stubs: 0x44740
-  __TEXT.__objc_methlist: 0x22278
-  __TEXT.__const: 0x109e0
+3505.14.3.1.2
+  __TEXT.__text: 0x371b90
+  __TEXT.__auth_stubs: 0x34f0
+  __TEXT.__objc_stubs: 0x44bc0
+  __TEXT.__objc_methlist: 0x223f0
+  __TEXT.__const: 0x10a00
   __TEXT.__dlopen_cstrs: 0xafa
-  __TEXT.__gcc_except_tab: 0x49c4
-  __TEXT.__cstring: 0x512f1
-  __TEXT.__oslogstring: 0x40270
-  __TEXT.__objc_classname: 0x519c
-  __TEXT.__objc_methname: 0x5c516
-  __TEXT.__objc_methtype: 0xf138
+  __TEXT.__gcc_except_tab: 0x4a44
+  __TEXT.__cstring: 0x51675
+  __TEXT.__oslogstring: 0x40c4e
+  __TEXT.__objc_classname: 0x51bb
+  __TEXT.__objc_methname: 0x5cbe2
+  __TEXT.__objc_methtype: 0xf184
   __TEXT.__ustring: 0x2b0
-  __TEXT.__unwind_info: 0xa2f0
-  __DATA_CONST.__auth_got: 0x1a68
-  __DATA_CONST.__got: 0x3a68
+  __TEXT.__unwind_info: 0xa350
+  __DATA_CONST.__auth_got: 0x1a88
+  __DATA_CONST.__got: 0x3a88
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x14d90
-  __DATA_CONST.__cfstring: 0x128c0
+  __DATA_CONST.__const: 0x14db8
+  __DATA_CONST.__cfstring: 0x12920
   __DATA_CONST.__objc_classlist: 0xd20
   __DATA_CONST.__objc_catlist: 0x620
-  __DATA_CONST.__objc_protolist: 0x6e0
+  __DATA_CONST.__objc_protolist: 0x6e8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0xb08

   __DATA_CONST.__objc_dictobj: 0x2f8
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA.__objc_const: 0x33560
-  __DATA.__objc_selrefs: 0x14578
-  __DATA.__objc_ivar: 0x255c
+  __DATA.__objc_const: 0x336e0
+  __DATA.__objc_selrefs: 0x146b0
+  __DATA.__objc_ivar: 0x257c
   __DATA.__objc_data: 0x8340
-  __DATA.__data: 0x5698
+  __DATA.__data: 0x56f8
   __DATA.__bss: 0xe18
   __DATA.__common: 0xa18
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  UUID: B85EA48A-A0FC-3C30-8449-5255A20881DD
-  Functions: 14260
-  Symbols:   2866
-  CStrings:  29348
+  UUID: 133E7307-560D-32CB-8F59-B859F989AEAC
+  Functions: 14300
+  Symbols:   2874
+  CStrings:  29457
 
Symbols:
+ _AFIsAttentionAssetAvailableFromUodStatus
+ _AFIsNLRouterAssetAvailableFromUodStatus
+ _AFRequiredAssetsForHybridUOD
+ _AFShouldRunAsrOnServerForUODLanguage
+ _AFSiriLogContextAnalysis
+ _OBJC_CLASS_$_ORCHSchemaORCHMUXBridgeContext
+ _OBJC_CLASS_$_ORCHSchemaORCHMUXRequestEnded
+ _OBJC_CLASS_$_ORCHSchemaORCHMultiUserScore
CStrings:
+ "%s Adding primaryUser with sharedUserId %{private}@ and homeUserUUID %{private}@ and iCloudAltDSID %{private}@ and ephemeralID %{private}@"
+ "%s Adding user with sharedUserId %{private}@ and homeUserUUID %{private}@ and iCloudAltDSID %{private}@ and ephemeralID %{private}@"
+ "%s Already set up"
+ "%s Emitting AIR event isAssistantEnabled: %@, isSiriAvailable: %@, orchestrationModeDesired: %@, orchestrationModeChosen: %@, unavailabilityReasons: %@"
+ "%s Encountered error when retrieving sharedUserId(%{private}@) for iCloudAltDSId(%{private}@): %@"
+ "%s Error decoding json data (wasn't utf8?)"
+ "%s Ignoring siriEnabledStatusDidChange as self is nil"
+ "%s No result candidate to log"
+ "%s Received an Ephemeral & Aggregation ID Update for the device owner: Ephemeral ID: %{private}@, Aggregation ID: %{private}@"
+ "%s Received an Ephemeral & Aggregation ID Update for user with iCloudAltDSId %{private}@ and sharedUserId %{private}@: Ephemeral ID: %{private}@, Aggregation ID: %{private}@"
+ "%s Register ADDailyDeviceStatusActivity as longLivedIdentifierUploadingEnabled is true"
+ "%s Retrieved aggregation IDs - device:%@ user:%@"
+ "%s Retrieving device and user aggregation IDs"
+ "%s SharedUserId is nil for SAUserConfidenceScore, skipping"
+ "%s Siri enabled status changed assistantEnabled: %@"
+ "%s Skipped registering ADDailyDeviceStatusActivity as longLivedIdentifierUploadingEnabled is false"
+ "%s Timed out waiting for aggregation IDs"
+ "%s Updated capabilities siriXFullUnderstandingOnDeviceCapabilities isDeviceCapable:%@ isFFEnabled:%@ isLanguageSupported:%@ areAssetsPresent:%@ capabilities:%@"
+ "%s Updated capabilities siriXHybridUnderstandingOnDeviceCapabilities capabilities to %@"
+ "%s Updated capabilities systemAssistantExperienceCapabilites capabilities to %@"
+ "%s homeMember enrollmentName: %{private}@ sharedUserId: %{private}@, ephemeralId: %{private}@"
+ "%s sharedUserId: %{private}@, voiceIDAllowedByUser: %lu, companionAssistantID: %{private}@, nonCloudSyncedUser: %lu, ephemeralID: %{private}@"
+ "-[ADCommandCenter _emitServerFallbackMessageForMissingAssets:requestId:]"
+ "-[ADCommandCenter _logToFeatureStore:speechRecgonized:]_block_invoke"
+ "-[ADCommandCenter(Instrumentation) _logMURequestEndedWithResultCandidate:]_block_invoke"
+ "-[ADDeviceProperties _populateEventMetadataForClientEvent:withCompletion:]_block_invoke_4"
+ "-[ADMultiUserService didReceiveIDs:forUser:]_block_invoke_2"
+ "-[ADMultiUserService onUserAnalyticsIdsChanged:iCloudAltDSId:sharedUserId:]"
+ "-[ADSiriCapabilitiesStore emitAIR]"
+ "-[ADSiriCapabilitiesStore siriEnabledStatusDidChange:]"
+ "-[ADSiriCapabilitiesStore siriEnabledStatusDidChange:]_block_invoke"
+ "-[ADSiriCapabilitiesStore updateSiriXFullUnderstandingOnDeviceCapabilities:localeIdentifier:]"
+ "-[ADSiriCapabilitiesStore updateSiriXHybridUnderstandingOnDeviceCapabilities:localeIdentifier:]"
+ "2"
+ "ADAnalyticsIdentifierObserver"
+ "ADCommandCenter.CurareDonationQueue"
+ "Adding an observer for user: %@"
+ "Adding an observer to the default user"
+ "Analytics Aggregation ID last refreshed %ld months ago for user %{private}@"
+ "Analytics IDs are not available. Triggering a new refresh for user: %@"
+ "Created home ephemeral identifier for current home; uuid:%{private}@"
+ "Created new Analytics IDs for user: %{private}@ refreshTime: %@ ephemeralCadenceTime: %@"
+ "Default User"
+ "Default User Ephemeral ID: %{private}@"
+ "EphemeralID: %{private}@ AggregationID: %{private}@ AggregationIDEffectiveFrom: %@ AggregationIDExpiration: %@"
+ "Is Ephemeral ID Refresh Required: %d. Is Aggregation ID Refresh Required: %d"
+ "MobileAssistantDaemons-3505.14.3.1.2"
+ "No Analytics Aggregation ID last creation date for user %{private}@"
+ "Notifying observer of available Analytics IDs"
+ "Notifying observers of new Analytics IDs"
+ "Refreshing Analytics IDs for user: %{private}@"
+ "Removing an observer for analytic ID changes"
+ "Removing an observer for user: %@"
+ "Removing an observer to the default user"
+ "Synchronous path won race? %d"
+ "T@\"NSHashTable\",R,N,V_defaultUserObserverList"
+ "T@\"NSMutableDictionary\",R,N,V_iCloudIdToAggregationIdCreationDateMap"
+ "T@\"NSMutableDictionary\",R,N,V_iCloudIdToAnalyticsIdsMap"
+ "T@\"NSMutableDictionary\",R,N,V_iCloudIdToEphemeralIdCreationDateMap"
+ "T@\"NSMutableDictionary\",R,N,V_iCloudIdToObserverListMap"
+ "T@\"NSString\",C,N,V_aggregationID"
+ "T@\"NSString\",C,N,V_ephemeralID"
+ "User(%{private}@) EphemeralID(%{private}@) AggregationID(%{private}@) DeviceAggregationID(%{private}@)"
+ "_aggregationID"
+ "_buildORCHClientEvent:"
+ "_convertToORCHUserIdentityClassification:"
+ "_createAndTestAndSetDefaultUserEphemeralId:expectedValue:expectedValueWasCreatedBySyncPath:withCreationTime:"
+ "_curareQueue"
+ "_defaultUserObserverList"
+ "_ephemeralID"
+ "_iCloudIdToAggregationIdCreationDateMap"
+ "_iCloudIdToAnalyticsIdsMap"
+ "_iCloudIdToEphemeralIdCreationDateMap"
+ "_iCloudIdToObserverListMap"
+ "_isAggregationIdRefreshRequired:forTime:"
+ "_isEphemeralIdRefreshRequired:forTime:"
+ "_logMURequestEndedWithResultCandidate:"
+ "_logToFeatureStore:speechRecgonized:"
+ "_publishAnalyticsIdUpdate:forUser:"
+ "_refreshAnalyticsIds"
+ "_refreshAnalyticsIdsForUser:withTime:"
+ "_retrieveExistingAnalyticsIdsForUser:"
+ "addObserver:foriCloudAltDSId:"
+ "aggregationID"
+ "defaultUserObserverList"
+ "didReceiveIDs:forUser:"
+ "emitAIR"
+ "emitAIREventForSiriAvailabiltyWithLocale:countryCode:isAvailable:orchestrationMode:unavailabilityReasons:"
+ "emitAIREventsForSiriRequestWithRequestId:missingAssets:"
+ "ephemeralID"
+ "ephemeralUserId"
+ "fetchUserAggregationIdWithCallback:"
+ "hashTableWithOptions:"
+ "https://seed.siri.apple.com"
+ "iCloudIdToAggregationIdCreationDateMap"
+ "iCloudIdToAnalyticsIdsMap"
+ "iCloudIdToEphemeralIdCreationDateMap"
+ "iCloudIdToObserverListMap"
+ "isAsrOnServerForUODEnabled"
+ "joana"
+ "month"
+ "onUserAnalyticsIdsChanged:iCloudAltDSId:sharedUserId:"
+ "removeObserver:foriCloudAltDSId:"
+ "setAggregationID:"
+ "setEphemeralID:"
+ "setMuxBridgeContext:"
+ "setORCHUserIdentityClassification:"
+ "setScore:"
+ "setSelectedSharedUserId:"
+ "setUserScores:"
+ "siriEnabledStatusDidChange:"
+ "userIdentityClassification"
+ "v24@?0@\"NSError\"8@\"NSString\"16"
+ "v24@?0@\"NSUUID\"8@\"NSUUID\"16"
+ "v32@0:8@\"ADAnalyticsDeviceAndUserIds\"16@\"NSString\"24"
+ "v52@0:8@16@24B32Q36Q44"
+ "voiceIDConfidenceScores"
- "%s Adding primaryUser with sharedUserId %{private}@ and homeUserUUID %{private}@ and iCloudAltDSID %{private}@"
- "%s Adding user with sharedUserId %{private}@ and homeUserUUID %{private}@ and iCloudAltDSID %{private}@"
- "%s Updated systemAssistantExperienceCapabilites capabilities to %@"
- "%s homeMember enrollmentName: %{private}@ sharedUserId: %{private}@"
- "%s sharedUserId: %{private}@, voiceIDAllowedByUser: %lu, companionAssistantID: %{private}@, nonCloudSyncedUser: %lu"
- "37"
- "MobileAssistantDaemons-3500.120.4.11.1"
- "Synchronous path won race?%d"
- "_EmitServerFallbackMessageForMissingAssets"
- "_createAndTestAndSetDefaultUserEphemeralId:expectedValue:expectedValueWasCreatedBySyncPath:"

```
