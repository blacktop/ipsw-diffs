## shazamd

> `/System/Library/Frameworks/ShazamKit.framework/shazamd`

```diff

-307.2.0.0.0
-  __TEXT.__text: 0x45ea4
+316.0.0.0.0
+  __TEXT.__text: 0x466ec
   __TEXT.__auth_stubs: 0x780
-  __TEXT.__objc_stubs: 0xb3e0
-  __TEXT.__objc_methlist: 0x4a70
+  __TEXT.__objc_stubs: 0xba40
+  __TEXT.__objc_methlist: 0x57e4
   __TEXT.__const: 0x160
-  __TEXT.__gcc_except_tab: 0xcf4
-  __TEXT.__objc_methname: 0xe68f
-  __TEXT.__cstring: 0x24a4
-  __TEXT.__oslogstring: 0x3a93
-  __TEXT.__objc_classname: 0x1236
-  __TEXT.__objc_methtype: 0x2a3b
+  __TEXT.__gcc_except_tab: 0xca0
+  __TEXT.__objc_methname: 0xf06b
+  __TEXT.__cstring: 0x25f2
+  __TEXT.__oslogstring: 0x39be
+  __TEXT.__objc_classname: 0x12f1
+  __TEXT.__objc_methtype: 0x2c88
   __TEXT.__ustring: 0x164
-  __TEXT.__unwind_info: 0x1258
+  __TEXT.__unwind_info: 0x12e0
   __DATA_CONST.__auth_got: 0x3d8
-  __DATA_CONST.__got: 0x7c8
-  __DATA_CONST.__const: 0x1648
-  __DATA_CONST.__cfstring: 0x20e0
-  __DATA_CONST.__objc_classlist: 0x468
+  __DATA_CONST.__got: 0x7e0
+  __DATA_CONST.__const: 0x1698
+  __DATA_CONST.__cfstring: 0x21e0
+  __DATA_CONST.__objc_classlist: 0x488
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x1b8
+  __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x350
-  __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0xd298
-  __DATA.__objc_selrefs: 0x3148
-  __DATA.__objc_ivar: 0x56c
-  __DATA.__objc_data: 0x2c10
-  __DATA.__data: 0x14a0
+  __DATA_CONST.__objc_intobj: 0xa8
+  __DATA.__objc_const: 0xc108
+  __DATA.__objc_selrefs: 0x34c8
+  __DATA.__objc_ivar: 0x574
+  __DATA.__objc_data: 0x2d50
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
+  Functions: 1679
+  Symbols:   387
+  CStrings:  3543
 
Symbols:
+ _CLLocationCoordinate2DMake
+ _OBJC_CLASS_$_SHLocationTransformer
+ _OBJC_CLASS_$_SHMusicalFeaturesConfiguration
+ _SHMediaItemConfidence
+ _SHMediaItemMatchLocationCoordinate
- _SHMediaItemMatchLocation
- _objc_retain_x9
CStrings:
+ "\x13\x11"
+ "\x14\x16"
+ "<%@: %p>\n\tBundle Identifier: %@\n\tConfiguration: %@\n\tLocal Store: %@"
+ "<%@: %p>\n\tDefault CREMA URL: %@\n\tDefault CREPE URL: %@\n\tCREMA URL: %@\n\tCREPE URL: %@"
+ "@\"<SHAudioRecordingBufferValidatorDelegate>\""
+ "@\"SHAudioRecordingBufferValidator\""
+ "@\"SHHapticsServerURLBuilder\""
+ "@\"SHMusicalFeaturesBagConfiguration\""
+ "@\"SHMusicalFeaturesConfiguration\""
+ "@\"SHMusicalFeaturesConfigurationProvider\""
+ "@\"SHMusicalFeaturesModelLocalStore\""
+ "@32@0:8@16^@24"
+ "@32@0:8{CLLocationCoordinate2D=dd}16"
+ "@40@0:8q16@24@32"
+ "@48@0:8@16@24q32@40"
+ "@48@0:8@16q24@32@40"
+ "@72@0:8@16@24@32q40d48d56@64"
+ "All recorders are muted or producing invalid audio buffers. Stopping recording."
+ "B24@0:8d16"
+ "B40@0:8@16d24^@32"
+ "Could not initialize musical features configuration: %@"
+ "Error occured with serializing raw response %@"
+ "Error occured with serializing song response for AdamID %@. Error: %@"
+ "Fetching haptic song attributes to check for haptics availability with URL %@"
+ "Marking the internal recorder as preferred. External recorder is not producing audio."
+ "Models available for %@ are CREMA %d and CREPE %d with minimum signature duration of %f"
+ "Recorder failed to produce valid audio & only produced silence for the first %f seconds. Accumulated silence duration: %f"
+ "SHAudioRecordingBufferValidator"
+ "SHAudioRecordingBufferValidatorDelegate"
+ "SHHapticsServerURLBuilder"
+ "SHLLibraryTrackLocationLatitude"
+ "SHLLibraryTrackLocationLongitude"
+ "SHLLocationTransformer"
+ "SHMediaLibraryDataStoreRawResponseSongsData"
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
+ "T@\"SHAudioRecordingBufferValidator\",R,N,V_recordingBufferValidator"
+ "T@\"SHHapticsServerURLBuilder\",R,N,V_urlBuilder"
+ "T@\"SHMusicalFeaturesBagConfiguration\",R,N,V_configuration"
+ "T@\"SHMusicalFeaturesConfiguration\",R,N"
+ "T@\"SHMusicalFeaturesConfiguration\",R,N,V_musicalFeaturesConfiguration"
+ "T@\"SHMusicalFeaturesConfigurationProvider\",R,N,V_musicalFeaturesProvider"
+ "T@\"SHMusicalFeaturesModelLocalStore\",R,N,V_localModelStore"
+ "T{CLLocationCoordinate2D=dd},D,N"
+ "T{CLLocationCoordinate2D=dd},N,V_locationCoordinate"
+ "_localModelStore"
+ "_locationCoordinate"
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
+ "coordinateFromLocation:"
+ "coordinateValueFromLocation:"
+ "createWithManagedTrack:"
+ "cremaModelURL"
+ "crepeModelURL"
+ "d32@0:8@16@24"
+ "data:audio/vnd.shazam.sff;base64,%@"
+ "dataFromManagedObjectRawResponseDictionary:"
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
+ "initWithCremaModelURL:crepeModelURL:minimumDuration:error:"
+ "initWithCremaModelURL:minimumDuration:error:"
+ "initWithCrepeModelURL:minimumDuration:error:"
+ "initWithGroupMetadata:groupSyncID:"
+ "initWithMinimumSignatureDuration:maximumSignatureDuration:bufferDuration:musicalFeaturesConfiguration:"
+ "initWithRemoteConfiguration:bundleIdentifier:localModelStore:"
+ "initWithSourceBundleIdentifier:"
+ "initWithTrackSyncID:creationDate:releaseDate:groupSyncID:labels:lastUpdatedDate:providerIdentifier:trackMetadata:providerName:shazamKey:recognitionID:title:subtitle:artworkURL:appleMusicID:appleMusicURL:shazamURL:videoURL:isExplicit:albumName:isrc:shazamCount:locationCoordinate:genres:rawSongResponse:"
+ "isHapticTrackAvailableFrom:songDuration:error:"
+ "isRecorderProducingValidAudio:"
+ "isValidBuffer:forRecorder:"
+ "loadHapticsEndpointForClientIdentifier:callback:"
+ "localModelStore"
+ "locationCoordinate"
+ "locationCoordinateFromCoder:"
+ "locationFromCoordinate:"
+ "minimumDurationInSecondsForClientIdentifier:"
+ "minimumDurationPerCurrentIdentifier"
+ "mlmodelc"
+ "musicalFeaturesBagConfigurationWithPromise"
+ "musicalFeaturesConfiguration"
+ "musicalFeaturesData"
+ "musicalFeaturesProvider"
+ "musicalFeaturesUri"
+ "now"
+ "payloadForSignature:location:"
+ "payloadForSpectralPeaksData:musicalFeaturesData:audioStartDate:recordingSource:sessionDuration:signatureRecordingOffset:location:"
+ "performAvailabilityRequest:completionHandler:"
+ "performFetchRequest:mediaItem:completionHandler:"
+ "rawResponseDataWithCampaignToken:"
+ "recorderFailedToProduceValidAudio:"
+ "recordersState"
+ "recordingBufferValidator"
+ "recordingStartDate"
+ "reqeustOfType:fromEndpoint:withMediaItem:"
+ "reqeustOfType:withMediaItem:completionHandler:"
+ "requestOfType:forID:ofIDType:"
+ "requestQueue"
+ "resourcesResponseFromServerObjects:error:"
+ "setLocationCoordinate:"
+ "setMusicalFeaturesConfiguration:"
+ "setRecordingStartDate:"
+ "set_rawResponseSongsData:"
+ "sh_ShazamKitBundle"
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
+ "v32@0:8{CLLocationCoordinate2D=dd}16"
+ "v40@0:8q16@24@?32"
+ "validateWithRecordingStartDate:"
+ "{CLLocationCoordinate2D=\"latitude\"d\"longitude\"d}"
+ "{CLLocationCoordinate2D=dd}16@0:8"
+ "{CLLocationCoordinate2D=dd}24@0:8@16"
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
- "T@\"CLLocation\",&,D,N"
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
- "rawResponseWithCampaignToken:"
- "setAllowsCachedAssets:"
- "set_rawResponseSongs:"
- "silentRecorders"
- "urlRequest"
- "v24@?0@\"SHHapticsEndpoint\"8@\"NSError\"16"

```
