## shazamd

> `/System/Library/Frameworks/ShazamKit.framework/shazamd`

```diff

-307.2.0.0.0
-  __TEXT.__text: 0x45ea4
-  __TEXT.__auth_stubs: 0x780
-  __TEXT.__objc_stubs: 0xb3e0
-  __TEXT.__objc_methlist: 0x4a70
+312.0.0.0.0
+  __TEXT.__text: 0x4620c
+  __TEXT.__auth_stubs: 0x770
+  __TEXT.__objc_stubs: 0xb960
+  __TEXT.__objc_methlist: 0x578c
   __TEXT.__const: 0x160
-  __TEXT.__gcc_except_tab: 0xcf4
-  __TEXT.__objc_methname: 0xe68f
-  __TEXT.__cstring: 0x24a4
-  __TEXT.__oslogstring: 0x3a93
-  __TEXT.__objc_classname: 0x1236
-  __TEXT.__objc_methtype: 0x2a3b
+  __TEXT.__gcc_except_tab: 0xca0
+  __TEXT.__objc_methname: 0xef2b
+  __TEXT.__cstring: 0x2591
+  __TEXT.__oslogstring: 0x3923
+  __TEXT.__objc_classname: 0x12da
+  __TEXT.__objc_methtype: 0x2bc9
   __TEXT.__ustring: 0x164
-  __TEXT.__unwind_info: 0x1258
-  __DATA_CONST.__auth_got: 0x3d8
-  __DATA_CONST.__got: 0x7c8
-  __DATA_CONST.__const: 0x1648
-  __DATA_CONST.__cfstring: 0x20e0
-  __DATA_CONST.__objc_classlist: 0x468
+  __TEXT.__unwind_info: 0x12b8
+  __DATA_CONST.__auth_got: 0x3d0
+  __DATA_CONST.__got: 0x7d8
+  __DATA_CONST.__const: 0x1698
+  __DATA_CONST.__cfstring: 0x21c0
+  __DATA_CONST.__objc_classlist: 0x480
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x1b8
+  __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x350
-  __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0xd298
-  __DATA.__objc_selrefs: 0x3148
-  __DATA.__objc_ivar: 0x56c
-  __DATA.__objc_data: 0x2c10
-  __DATA.__data: 0x14a0
+  __DATA_CONST.__objc_superrefs: 0x358
+  __DATA_CONST.__objc_intobj: 0xa8
+  __DATA.__objc_const: 0xc058
+  __DATA.__objc_selrefs: 0x3480
+  __DATA.__objc_ivar: 0x574
+  __DATA.__objc_data: 0x2d00
+  __DATA.__data: 0x1500
   __DATA.__bss: 0x100
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1637
-  Symbols:   384
-  CStrings:  3453
+  Functions: 1672
+  Symbols:   385
+  CStrings:  3527
 
Symbols:
+ _OBJC_CLASS_$_SHMusicalFeaturesConfiguration
+ _SHMediaItemConfidence
- _objc_retain_x9
CStrings:
+ "\x13\x11"
+ "\x14\x16"
+ "<%@: %p>\n\tBundle Identifier: %@\n\tConfiguration: %@\n\tLocal Store: %@"
+ "<%@: %p>\n\tDefault CREMA URL: %@\n\tDefault CREPE URL: %@\n\tCREMA URL: %@\n\tCREPE URL: %@"
+ "@\"<SHAudioRecordingBufferValidatorDelegate>\""
+ "@\"SHAudioRecordingBufferValidator\""
+ "@\"SHHapticsServerURLBuilder\""
+ "@\"SHMusicalFeaturesConfiguration\""
+ "@\"SHMusicalFeaturesConfigurationProvider\""
+ "@\"SHMusicalFeaturesModelLocalStore\""
+ "@\"SHMusicalFeaturesModelsConfiguration\""
+ "@32@0:8@16^@24"
+ "@40@0:8q16@24@32"
+ "@48@0:8@16@24q32@40"
+ "@48@0:8@16q24@32@40"
+ "@72@0:8@16@24@32q40d48d56@64"
+ "All recorders are muted or producing invalid audio buffers. Stopping recording."
+ "B24@0:8d16"
+ "B40@0:8@16d24^@32"
+ "Could not initialize musical features configuration: %@"
+ "Fetching haptic song attributes to check for haptics availability with URL %@"
+ "Marking the internal recorder as preferred. External recorder is not producing audio."
+ "Models available for %@ are CREMA %d and CREPE %d"
+ "Recorder failed to produce valid audio & only produced silence for the first %f seconds. Accumulated silence duration: %f"
+ "SHAudioRecordingBufferValidator"
+ "SHAudioRecordingBufferValidatorDelegate"
+ "SHHapticsServerURLBuilder"
+ "SHMusicalFeaturesConfigurationProvider"
+ "SHMusicalFeaturesModelLocalStore"
+ "SHServerHapticsResponseParser"
+ "SHServerHapticsSpatialOffsetsParser"
+ "Server response parser: has no data array"
+ "T@\"<SHAudioRecordingBufferValidatorDelegate>\",W,N,V_delegate"
+ "T@\"NSDate\",&,N,V_recordingStartDate"
+ "T@\"NSMapTable\",R,N,V_recordersState"
+ "T@\"NSMapTable\",R,N,V_silentRecordersDurationAccumulator"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_requestQueue"
+ "T@\"NSURL\",R,N,V_cremaModelURL"
+ "T@\"NSURL\",R,N,V_crepeModelURL"
+ "T@\"SHAudioRecordingBufferValidator\",R,N,V_recordingBufferValidator"
+ "T@\"SHHapticsServerURLBuilder\",R,N,V_urlBuilder"
+ "T@\"SHMusicalFeaturesConfiguration\",R,N"
+ "T@\"SHMusicalFeaturesConfiguration\",R,N,V_musicalFeaturesConfiguration"
+ "T@\"SHMusicalFeaturesConfigurationProvider\",R,N,V_musicalFeaturesProvider"
+ "T@\"SHMusicalFeaturesModelLocalStore\",R,N,V_localModelStore"
+ "T@\"SHMusicalFeaturesModelsConfiguration\",R,N,V_configuration"
+ "_cremaModelURL"
+ "_crepeModelURL"
+ "_localModelStore"
+ "_musicalFeaturesConfiguration"
+ "_musicalFeaturesProvider"
+ "_recordersState"
+ "_recordingBufferValidator"
+ "_recordingStartDate"
+ "_requestQueue"
+ "_silentRecordersDurationAccumulator"
+ "accumulatedSilenceDurationForRecorder:buffer:"
+ "addMutedRecorder:"
+ "availableModelsForClientIdentifier:"
+ "availableModelsPerCurrentIdentifier"
+ "boolValue"
+ "confidence"
+ "createWithManagedTrack:"
+ "crema"
+ "cremaModelURL"
+ "crepe"
+ "crepeModelURL"
+ "d32@0:8@16@24"
+ "data:audio/vnd.shazam.sff;base64,%@"
+ "dataResponseFromServerObjects:error:"
+ "defaultCremaModelURL"
+ "defaultCrepeModelURL"
+ "defaultModelURLWithName:"
+ "durationOfBuffer:"
+ "fetchHapticByAdamIDURL"
+ "fetchHapticByISRCURL"
+ "hapticForMediaItem:completionHandler:"
+ "hapticsEndpointsForStorefront:clientIdentifier:"
+ "hapticsWithCompletion:"
+ "hasHaptics"
+ "hasRecordedAboveInitialThresholdForSilenceDuration:"
+ "i"
+ "initWithAudioTapProvider:attribution:clientType:musicalFeaturesConfiguration:"
+ "initWithClientIdentifier:clientType:installationID:musicalFeaturesConfiguration:"
+ "initWithCremaModelURL:crepeModelURL:error:"
+ "initWithCremaModelURL:error:"
+ "initWithCremaURL:crepeModelURL:"
+ "initWithCrepeModelURL:error:"
+ "initWithGroupMetadata:groupSyncID:"
+ "initWithMinimumSignatureDuration:maximumSignatureDuration:bufferDuration:musicalFeaturesConfiguration:"
+ "initWithRemoteConfiguration:bundleIdentifier:localModelStore:"
+ "initWithSourceBundleIdentifier:"
+ "initWithTrackSyncID:creationDate:releaseDate:groupSyncID:labels:lastUpdatedDate:providerIdentifier:trackMetadata:providerName:shazamKey:recognitionID:title:subtitle:artworkURL:appleMusicID:appleMusicURL:shazamURL:videoURL:isExplicit:albumName:isrc:shazamCount:location:genres:rawSongResponse:"
+ "isHapticTrackAvailableFrom:songDuration:error:"
+ "isRecorderProducingValidAudio:"
+ "isValidBuffer:forRecorder:"
+ "loadHapticsEndpointForClientIdentifier:callback:"
+ "localModelStore"
+ "mlmodelc"
+ "musicalFeaturesConfiguration"
+ "musicalFeaturesConfigurationWithPromise"
+ "musicalFeaturesData"
+ "musicalFeaturesProvider"
+ "musicalFeaturesUri"
+ "now"
+ "payloadForSignature:location:"
+ "payloadForSpectralPeaksData:musicalFeaturesData:audioStartDate:recordingSource:sessionDuration:signatureRecordingOffset:location:"
+ "performAvailabilityRequest:completionHandler:"
+ "performFetchRequest:mediaItem:completionHandler:"
+ "recorderFailedToProduceValidAudio:"
+ "recordersState"
+ "recordingBufferValidator"
+ "recordingStartDate"
+ "reqeustOfType:fromEndpoint:withMediaItem:"
+ "reqeustOfType:withMediaItem:completionHandler:"
+ "requestOfType:forID:ofIDType:"
+ "requestQueue"
+ "resourcesResponseFromServerObjects:error:"
+ "setMusicalFeaturesConfiguration:"
+ "setRecordingStartDate:"
+ "silentRecordersDurationAccumulator"
+ "spectralPeaksData"
+ "strongToStrongObjectsMapTable"
+ "timeIntervalSinceDate:"
+ "v24@0:8@\"<SHAudioRecorder>\"16"
+ "v24@?0@\"NSURLRequest\"8@\"NSError\"16"
+ "v24@?0@\"SHHaptic\"8@\"NSError\"16"
+ "v24@?0@\"SHHapticsConfiguration\"8@\"NSError\"16"
+ "v24@?0@\"SHHapticsEndpointResponse\"8@\"NSError\"16"
+ "v24@?0@\"SHHapticsEndpoints\"8@\"NSError\"16"
+ "v40@0:8q16@24@?32"
+ "validateWithRecordingStartDate:"
- "\x11\x12"
- "\x14\x15"
- "@\"NSURLRequest\""
- "@\"SHHapticsEndpoint\""
- "@\"SHTokenizedURL\""
- "Cannot check if a haptic track is available. Media item: %@ does not have required Apple Music ID or ISRC"
- "Did not find apple music ID or ISRC from media item: %@ to create haptics endpoint request."
- "Error fetching haptics archives %@"
- "Failed to check if a haptic track is available for media item %@. Check that AdamID or ISRC is valid."
- "Failed to fetch haptics for media item %@. Check AdamID or ISRC is valid."
- "Fetching haptic song attributes to check for haptics availability. AdamID:%@ <-> ISRC: %@"
- "Fetching haptic song attributes. AdamID:%@ <-> ISRC: %@"
- "Haptics endpoints: AdamID:%@, ISRC: %@"
- "Haptics fetch request for media item: %@ does not have required Apple Music ID or ISRC"
- "Haptics request URL could not be constructed."
- "Haptics request complete with response data %lu."
- "Making request to fetch song attributes"
- "Not requesting for haptics cause endpoint is missing. Error: %@"
- "Retrieved cached %lu haptic tracks for media item: %@"
- "Returning cached apple archive for request. AppleMusicID: %@, ISRC: %@"
- "SHHapticsEndpoint"
- "SHHapticsEndpointRequest"
- "SHServerSpatialOffsetsParser"
- "Server response parser: has no song haptic resources"
- "T@\"NSMutableSet\",R,N,V_silentRecorders"
- "T@\"NSURLRequest\",R,N,V_urlRequest"
- "T@\"SHHapticsEndpoint\",R,N,V_hapticsEndpoint"
- "T@\"SHShazamKitServerURLBuilder\",R,N,V_urlBuilder"
- "T@\"SHTokenizedURL\",R,N,V_adamIDURL"
- "T@\"SHTokenizedURL\",R,N,V_isrcURL"
- "TB,N,V_allowsCachedAssets"
- "_adamIDURL"
- "_allowsCachedAssets"
- "_hapticsEndpoint"
- "_isrcURL"
- "_silentRecorders"
- "_urlRequest"
- "adamIDURL"
- "allowsCachedAssets"
- "constructURLRequest"
- "hapticsEndpoint"
- "hapticsURLPathForClientIdentifier:songResourceIDType:"
- "hasRequestAppleMusicID"
- "hasRequestISRC"
- "initWithAdamIDURL:isrcURL:"
- "initWithAudioTapProvider:attribution:clientType:"
- "initWithClientIdentifier:clientType:installationID:"
- "initWithManagedGroup:"
- "initWithManagedTrack:"
- "initWithMinimumSignatureDuration:maximumSignatureDuration:bufferDuration:"
- "initWithMinimumSignatureDuration:maximumSignatureDuration:bufferDuration:signatureGenerator:"
- "initWithRequestMediaItem:hapticsEndpoint:"
- "isrcURL"
- "loadHapticsEndpointForClientIdentifier:clientType:callback:"
- "payloadForSignature:withLocation:"
- "performHapticsTrackAvailabilityRequest:completionHandler:"
- "setAllowsCachedAssets:"
- "silentRecorders"
- "urlRequest"
- "v24@?0@\"SHHapticsEndpoint\"8@\"NSError\"16"

```
