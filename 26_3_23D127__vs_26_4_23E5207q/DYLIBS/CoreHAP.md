## CoreHAP

> `/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP`

```diff

-1388.4.13.0.0
-  __TEXT.__text: 0x1ab288
+1418.5.4.0.0
+  __TEXT.__text: 0x1e6550
   __TEXT.__auth_stubs: 0x1590
-  __TEXT.__objc_methlist: 0x13a58
-  __TEXT.__const: 0x710
+  __TEXT.__objc_methlist: 0x162e8
+  __TEXT.__const: 0x770
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__gcc_except_tab: 0x63dc
-  __TEXT.__cstring: 0x1123b
-  __TEXT.__oslogstring: 0x202d8
-  __TEXT.__unwind_info: 0x5de8
-  __TEXT.__objc_classname: 0x2e37
-  __TEXT.__objc_methname: 0x26bd3
-  __TEXT.__objc_methtype: 0x8fe8
-  __TEXT.__objc_stubs: 0x189c0
-  __DATA_CONST.__got: 0xb40
-  __DATA_CONST.__const: 0x5138
-  __DATA_CONST.__objc_classlist: 0x960
+  __TEXT.__gcc_except_tab: 0x67c8
+  __TEXT.__cstring: 0x128bb
+  __TEXT.__oslogstring: 0x20d41
+  __TEXT.__unwind_info: 0x74d8
+  __TEXT.__objc_classname: 0x3444
+  __TEXT.__objc_methname: 0x28f5c
+  __TEXT.__objc_methtype: 0x94ef
+  __TEXT.__objc_stubs: 0x1a160
+  __DATA_CONST.__got: 0xcf8
+  __DATA_CONST.__const: 0x5448
+  __DATA_CONST.__objc_classlist: 0xb10
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x340
+  __DATA_CONST.__objc_protolist: 0x348
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6fc8
-  __DATA_CONST.__objc_protorefs: 0xc0
-  __DATA_CONST.__objc_superrefs: 0x7e0
+  __DATA_CONST.__objc_selrefs: 0x7620
+  __DATA_CONST.__objc_protorefs: 0xc8
+  __DATA_CONST.__objc_superrefs: 0x980
   __DATA_CONST.__objc_arraydata: 0x208
-  __AUTH_CONST.__auth_got: 0xad8
-  __AUTH_CONST.__const: 0x800
-  __AUTH_CONST.__cfstring: 0xde80
-  __AUTH_CONST.__objc_const: 0x222c0
-  __AUTH_CONST.__objc_intobj: 0x6c0
+  __AUTH_CONST.__auth_got: 0xae0
+  __AUTH_CONST.__const: 0x7e0
+  __AUTH_CONST.__cfstring: 0xedc0
+  __AUTH_CONST.__objc_const: 0x27258
+  __AUTH_CONST.__objc_intobj: 0x6f0
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH.__objc_data: 0x4e70
-  __DATA.__objc_ivar: 0x1504
-  __DATA.__data: 0x2722
-  __DATA.__bss: 0x479
+  __AUTH.__objc_data: 0x5f50
+  __DATA.__objc_ivar: 0x1704
+  __DATA.__data: 0x2782
+  __DATA.__bss: 0x4a9
   __DATA_DIRTY.__objc_data: 0xf50
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0xd8
+  __DATA_DIRTY.__bss: 0x98
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CloudServices.framework/CloudServices
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate
   - /System/Library/PrivateFrameworks/EasyConfig.framework/EasyConfig

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/WirelessProximity.framework/WirelessProximity
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 4A01F4E5-1AE0-379D-8819-352D5A82B2BF
-  Functions: 7534
-  Symbols:   24478
-  CStrings:  13010
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 06004434-7F7F-3EF6-91FB-122F755D46A8
+  Functions: 8356
+  Symbols:   26944
+  CStrings:  13733
 
Symbols:
+ +[HAP2ThreadNetworkUtil _addressToCIDR:withNetmask:]
+ +[HAP2ThreadNetworkUtil _interface:hasAddressesWithPrefix:]
+ +[HAP2ThreadNetworkUtil _sharedThreadClient]
+ +[HAP2ThreadNetworkUtil getCurrentNetworkInterfaces]
+ +[HAP2ThreadNetworkUtil isAddress:inNetwork:]
+ +[HAP2ThreadNetworkUtil isThreadIPv6Address:fromInterfaces:]
+ +[HAP2ThreadNetworkUtil isThreadInterface:]
+ +[HAP2ThreadNetworkUtil isThreadRadioAvailable]
+ +[HAP2ThreadNetworkUtil threadMeshLocalPrefix]
+ +[HAPAudioCodecBitDepthWrapper parsedFromData:error:]
+ +[HAPAudioStreamTier parsedFromData:error:]
+ +[HAPCameraBufferEvent parsedFromData:error:]
+ +[HAPCameraBufferEventCMAFSessionStart parsedFromData:error:]
+ +[HAPCameraBufferEventCMAFSessionStop parsedFromData:error:]
+ +[HAPCameraBufferEventCommandRequest parsedFromData:error:]
+ +[HAPCameraBufferEventCommandResponse parsedFromData:error:]
+ +[HAPCameraBufferEventCommandTypeWrapper parsedFromData:error:]
+ +[HAPCameraBufferEventMotion parsedFromData:error:]
+ +[HAPCameraBufferEventTypeWrapper parsedFromData:error:]
+ +[HAPCameraBufferInfo parsedFromData:error:]
+ +[HAPCameraBufferInfoResponse parsedFromData:error:]
+ +[HAPCameraBufferInterval parsedFromData:error:]
+ +[HAPCameraBufferTypeWrapper parsedFromData:error:]
+ +[HAPCameraBufferUploadCommandRequest parsedFromData:error:]
+ +[HAPCameraBufferUploadCommandResponse parsedFromData:error:]
+ +[HAPCameraBufferUploadCommandTypeWrapper parsedFromData:error:]
+ +[HAPCameraBufferUploadStopActionWrapper parsedFromData:error:]
+ +[HAPCameraCapabilitiesResponse parsedFromData:error:]
+ +[HAPCameraClientCSR parsedFromData:error:]
+ +[HAPCameraClientCertificate parsedFromData:error:]
+ +[HAPCameraClientCertificateStatus parsedFromData:error:]
+ +[HAPCameraKey parsedFromData:error:]
+ +[HAPCameraKeyID parsedFromData:error:]
+ +[HAPCameraRecordingPublishingPoint parsedFromData:error:]
+ +[HAPCameraSensors parsedFromData:error:]
+ +[HAPCameraVideoQualityWrapper parsedFromData:error:]
+ +[HAPCameraVideoStreamCapabilities parsedFromData:error:]
+ +[HAPCameraZones parsedFromData:error:]
+ +[HAPPolygon parsedFromData:error:]
+ +[HAPRTPStreamingControlCommandWrapper parsedFromData:error:]
+ +[HAPRTPStreamingControlRequest parsedFromData:error:]
+ +[HAPRTPStreamingControlResponse parsedFromData:error:]
+ +[HAPRTPStreamingControlStatusWrapper parsedFromData:error:]
+ +[HAPSensorConfiguration parsedFromData:error:]
+ +[HAPSensorDimensions parsedFromData:error:]
+ +[HAPSupportedAudioStreamTiers parsedFromData:error:]
+ +[HAPSupportedVideoStreamTiers parsedFromData:error:]
+ +[HAPSystemKeychainStore _systemKeychainStoreSingleton]
+ +[HAPSystemKeychainStore keyCountProvider]
+ +[HAPSystemKeychainStore keyStore]
+ +[HAPVideoCodecTypeWrapper parsedFromData:error:]
+ +[HAPVideoStreamTier parsedFromData:error:]
+ +[HAPWebRTCICECandidate parsedFromData:error:]
+ +[HAPWebRTCOfferStatusWrapper parsedFromData:error:]
+ +[HAPWebRTCProvideAnswerRequest parsedFromData:error:]
+ +[HAPWebRTCReofferRequest parsedFromData:error:]
+ +[HAPWebRTCReofferResponse parsedFromData:error:]
+ +[HAPWebRTCSFrameConfiguration parsedFromData:error:]
+ +[HAPWebRTCSolicitOfferRequest parsedFromData:error:]
+ +[HAPWebRTCSolicitOfferResponse parsedFromData:error:]
+ +[HAPWebRTCStreamingControlRequest parsedFromData:error:]
+ +[HAPWebRTCStreamingControlResponse parsedFromData:error:]
+ +[HAPWebRTCStreamingControlStatusWrapper parsedFromData:error:]
+ +[HAPWebRTCStreamingStatusWrapper parsedFromData:error:]
+ +[HAPZoneDataV2 parsedFromData:error:]
+ +[NSError(HAPError) hapErrorWithCode:OSStatus:]
+ -[HAP2AccessoryServer _directlyUpdateConnectionState:withError:]
+ -[HAP2AccessoryServer _handleDiscoveredAccessories:withCompletionHandler:]
+ -[HAP2AccessoryServer _onDemandConnectionsAreEnabled]
+ -[HAP2AccessoryServer removedAccessoryKey]
+ -[HAP2AccessoryServer setRemovedAccessoryKey:]
+ -[HAP2AccessoryServer(Paired) _updateAccessories:]
+ -[HAP2AccessoryServer(Paired) updateConnectionState:withError:]
+ -[HAP2AccessoryServer(Unpaired) getPairingsWithRemovedAccessoryKey:completion:]
+ -[HAP2AccessoryServer(Unpaired) removeUnpairedAccessoryPairing:accessoryKey:completion:]
+ -[HAP2AccessoryServer(Unpaired) updateRemovedAccessoriesWithReason:accessoryKey:completion:]
+ -[HAP2AccessoryServerController _getPairingsCharacteristicForAccessory:error:]
+ -[HAP2AccessoryServerController managesConnectionStateExternally]
+ -[HAP2AccessoryServerCoordinator allowsRemovedAccessoryKeys]
+ -[HAP2AccessoryServerSecureTransportPairVerify _createStandardSecuritySession]
+ -[HAPAccessoryServer enableRemovedAccessoryKey:completionQueue:completion:]
+ -[HAPAccessoryServer removePairingsWithRemovedAccessoryKey:queue:completion:]
+ -[HAPAccessoryServer removedAccessoryKey]
+ -[HAPAccessoryServer setRemovedAccessoryKey:]
+ -[HAPAccessoryServerBrowser clearRemovedFromHome:]
+ -[HAPAccessoryServerBrowser removedAccessoryIdentifiers]
+ -[HAPAccessoryServerBrowser setRemovedAccessoryIdentifiers:]
+ -[HAPAccessoryServerBrowser wasRemovedFromHome:]
+ -[HAPAccessoryServerHAP2Adapter discoverRemovedAccessoriesWithCompletion:]
+ -[HAPAccessoryServerHAP2Adapter enableRemovedAccessoryKey:completionQueue:completion:]
+ -[HAPAccessoryServerIP _establishSecureSessionAndListPairings:queue:completion:]
+ -[HAPAccessoryServerIP _establishSecureSessionAndListPairingsWithCompletionQueue:completion:]
+ -[HAPAccessoryServerIP _sendListPairingsWithData:queue:completion:]
+ -[HAPAccessoryServerIP pendingBonjourAdd]
+ -[HAPAccessoryServerIP setPendingBonjourAdd:]
+ -[HAPAudioCodecBitDepthWrapper copyWithZone:]
+ -[HAPAudioCodecBitDepthWrapper description]
+ -[HAPAudioCodecBitDepthWrapper initWithValue:]
+ -[HAPAudioCodecBitDepthWrapper init]
+ -[HAPAudioCodecBitDepthWrapper isEqual:]
+ -[HAPAudioCodecBitDepthWrapper parseFromData:error:]
+ -[HAPAudioCodecBitDepthWrapper serializeWithError:]
+ -[HAPAudioCodecBitDepthWrapper setValue:]
+ -[HAPAudioCodecBitDepthWrapper value]
+ -[HAPAudioStreamTier .cxx_destruct]
+ -[HAPAudioStreamTier bitDepth]
+ -[HAPAudioStreamTier copyWithZone:]
+ -[HAPAudioStreamTier description]
+ -[HAPAudioStreamTier identifier]
+ -[HAPAudioStreamTier initWithIdentifier:targetAverageBitrate:sampleRate:bitDepth:packetTime:numberOfChannels:]
+ -[HAPAudioStreamTier init]
+ -[HAPAudioStreamTier isEqual:]
+ -[HAPAudioStreamTier numberOfChannels]
+ -[HAPAudioStreamTier packetTime]
+ -[HAPAudioStreamTier parseFromData:error:]
+ -[HAPAudioStreamTier sampleRate]
+ -[HAPAudioStreamTier serializeWithError:]
+ -[HAPAudioStreamTier setBitDepth:]
+ -[HAPAudioStreamTier setIdentifier:]
+ -[HAPAudioStreamTier setNumberOfChannels:]
+ -[HAPAudioStreamTier setPacketTime:]
+ -[HAPAudioStreamTier setSampleRate:]
+ -[HAPAudioStreamTier setTargetAverageBitrate:]
+ -[HAPAudioStreamTier targetAverageBitrate]
+ -[HAPCameraBufferEvent .cxx_destruct]
+ -[HAPCameraBufferEvent CMAFSessionStart]
+ -[HAPCameraBufferEvent CMAFSessionStop]
+ -[HAPCameraBufferEvent copyWithZone:]
+ -[HAPCameraBufferEvent description]
+ -[HAPCameraBufferEvent initWithSequenceNumber:type:CMAFSessionStart:CMAFSessionStop:motion:]
+ -[HAPCameraBufferEvent init]
+ -[HAPCameraBufferEvent isEqual:]
+ -[HAPCameraBufferEvent motion]
+ -[HAPCameraBufferEvent parseFromData:error:]
+ -[HAPCameraBufferEvent sequenceNumber]
+ -[HAPCameraBufferEvent serializeWithError:]
+ -[HAPCameraBufferEvent setCMAFSessionStart:]
+ -[HAPCameraBufferEvent setCMAFSessionStop:]
+ -[HAPCameraBufferEvent setMotion:]
+ -[HAPCameraBufferEvent setSequenceNumber:]
+ -[HAPCameraBufferEvent setType:]
+ -[HAPCameraBufferEvent type]
+ -[HAPCameraBufferEventCMAFSessionStart .cxx_destruct]
+ -[HAPCameraBufferEventCMAFSessionStart CMAFSessionID]
+ -[HAPCameraBufferEventCMAFSessionStart copyWithZone:]
+ -[HAPCameraBufferEventCMAFSessionStart description]
+ -[HAPCameraBufferEventCMAFSessionStart initWithCMAFSessionID:]
+ -[HAPCameraBufferEventCMAFSessionStart init]
+ -[HAPCameraBufferEventCMAFSessionStart isEqual:]
+ -[HAPCameraBufferEventCMAFSessionStart parseFromData:error:]
+ -[HAPCameraBufferEventCMAFSessionStart serializeWithError:]
+ -[HAPCameraBufferEventCMAFSessionStart setCMAFSessionID:]
+ -[HAPCameraBufferEventCMAFSessionStop .cxx_destruct]
+ -[HAPCameraBufferEventCMAFSessionStop CMAFSessionID]
+ -[HAPCameraBufferEventCMAFSessionStop copyWithZone:]
+ -[HAPCameraBufferEventCMAFSessionStop description]
+ -[HAPCameraBufferEventCMAFSessionStop initWithCMAFSessionID:]
+ -[HAPCameraBufferEventCMAFSessionStop init]
+ -[HAPCameraBufferEventCMAFSessionStop isEqual:]
+ -[HAPCameraBufferEventCMAFSessionStop parseFromData:error:]
+ -[HAPCameraBufferEventCMAFSessionStop serializeWithError:]
+ -[HAPCameraBufferEventCMAFSessionStop setCMAFSessionID:]
+ -[HAPCameraBufferEventCommandRequest .cxx_destruct]
+ -[HAPCameraBufferEventCommandRequest command]
+ -[HAPCameraBufferEventCommandRequest copyWithZone:]
+ -[HAPCameraBufferEventCommandRequest description]
+ -[HAPCameraBufferEventCommandRequest initWithCommand:sequenceNumber:limit:]
+ -[HAPCameraBufferEventCommandRequest init]
+ -[HAPCameraBufferEventCommandRequest isEqual:]
+ -[HAPCameraBufferEventCommandRequest limit]
+ -[HAPCameraBufferEventCommandRequest parseFromData:error:]
+ -[HAPCameraBufferEventCommandRequest sequenceNumber]
+ -[HAPCameraBufferEventCommandRequest serializeWithError:]
+ -[HAPCameraBufferEventCommandRequest setCommand:]
+ -[HAPCameraBufferEventCommandRequest setLimit:]
+ -[HAPCameraBufferEventCommandRequest setSequenceNumber:]
+ -[HAPCameraBufferEventCommandResponse .cxx_destruct]
+ -[HAPCameraBufferEventCommandResponse copyWithZone:]
+ -[HAPCameraBufferEventCommandResponse description]
+ -[HAPCameraBufferEventCommandResponse events]
+ -[HAPCameraBufferEventCommandResponse initWithEvents:]
+ -[HAPCameraBufferEventCommandResponse init]
+ -[HAPCameraBufferEventCommandResponse isEqual:]
+ -[HAPCameraBufferEventCommandResponse parseFromData:error:]
+ -[HAPCameraBufferEventCommandResponse serializeWithError:]
+ -[HAPCameraBufferEventCommandResponse setEvents:]
+ -[HAPCameraBufferEventCommandTypeWrapper copyWithZone:]
+ -[HAPCameraBufferEventCommandTypeWrapper description]
+ -[HAPCameraBufferEventCommandTypeWrapper initWithValue:]
+ -[HAPCameraBufferEventCommandTypeWrapper init]
+ -[HAPCameraBufferEventCommandTypeWrapper isEqual:]
+ -[HAPCameraBufferEventCommandTypeWrapper parseFromData:error:]
+ -[HAPCameraBufferEventCommandTypeWrapper serializeWithError:]
+ -[HAPCameraBufferEventCommandTypeWrapper setValue:]
+ -[HAPCameraBufferEventCommandTypeWrapper value]
+ -[HAPCameraBufferEventMotion .cxx_destruct]
+ -[HAPCameraBufferEventMotion active]
+ -[HAPCameraBufferEventMotion copyWithZone:]
+ -[HAPCameraBufferEventMotion description]
+ -[HAPCameraBufferEventMotion initWithActive:]
+ -[HAPCameraBufferEventMotion init]
+ -[HAPCameraBufferEventMotion isEqual:]
+ -[HAPCameraBufferEventMotion parseFromData:error:]
+ -[HAPCameraBufferEventMotion serializeWithError:]
+ -[HAPCameraBufferEventMotion setActive:]
+ -[HAPCameraBufferEventTypeWrapper copyWithZone:]
+ -[HAPCameraBufferEventTypeWrapper description]
+ -[HAPCameraBufferEventTypeWrapper initWithValue:]
+ -[HAPCameraBufferEventTypeWrapper init]
+ -[HAPCameraBufferEventTypeWrapper isEqual:]
+ -[HAPCameraBufferEventTypeWrapper parseFromData:error:]
+ -[HAPCameraBufferEventTypeWrapper serializeWithError:]
+ -[HAPCameraBufferEventTypeWrapper setValue:]
+ -[HAPCameraBufferEventTypeWrapper value]
+ -[HAPCameraBufferInfo .cxx_destruct]
+ -[HAPCameraBufferInfo copyWithZone:]
+ -[HAPCameraBufferInfo description]
+ -[HAPCameraBufferInfo identifier]
+ -[HAPCameraBufferInfo initWithIdentifier:type:intervals:]
+ -[HAPCameraBufferInfo init]
+ -[HAPCameraBufferInfo intervals]
+ -[HAPCameraBufferInfo isEqual:]
+ -[HAPCameraBufferInfo parseFromData:error:]
+ -[HAPCameraBufferInfo serializeWithError:]
+ -[HAPCameraBufferInfo setIdentifier:]
+ -[HAPCameraBufferInfo setIntervals:]
+ -[HAPCameraBufferInfo setType:]
+ -[HAPCameraBufferInfo type]
+ -[HAPCameraBufferInfoResponse .cxx_destruct]
+ -[HAPCameraBufferInfoResponse buffers]
+ -[HAPCameraBufferInfoResponse copyWithZone:]
+ -[HAPCameraBufferInfoResponse description]
+ -[HAPCameraBufferInfoResponse initWithVersion:buffers:]
+ -[HAPCameraBufferInfoResponse init]
+ -[HAPCameraBufferInfoResponse isEqual:]
+ -[HAPCameraBufferInfoResponse parseFromData:error:]
+ -[HAPCameraBufferInfoResponse serializeWithError:]
+ -[HAPCameraBufferInfoResponse setBuffers:]
+ -[HAPCameraBufferInfoResponse setVersion:]
+ -[HAPCameraBufferInfoResponse version]
+ -[HAPCameraBufferInterval .cxx_destruct]
+ -[HAPCameraBufferInterval copyWithZone:]
+ -[HAPCameraBufferInterval count]
+ -[HAPCameraBufferInterval description]
+ -[HAPCameraBufferInterval initWithSequenceNumber:count:]
+ -[HAPCameraBufferInterval init]
+ -[HAPCameraBufferInterval isEqual:]
+ -[HAPCameraBufferInterval parseFromData:error:]
+ -[HAPCameraBufferInterval sequenceNumber]
+ -[HAPCameraBufferInterval serializeWithError:]
+ -[HAPCameraBufferInterval setCount:]
+ -[HAPCameraBufferInterval setSequenceNumber:]
+ -[HAPCameraBufferTypeWrapper copyWithZone:]
+ -[HAPCameraBufferTypeWrapper description]
+ -[HAPCameraBufferTypeWrapper initWithValue:]
+ -[HAPCameraBufferTypeWrapper init]
+ -[HAPCameraBufferTypeWrapper isEqual:]
+ -[HAPCameraBufferTypeWrapper parseFromData:error:]
+ -[HAPCameraBufferTypeWrapper serializeWithError:]
+ -[HAPCameraBufferTypeWrapper setValue:]
+ -[HAPCameraBufferTypeWrapper value]
+ -[HAPCameraBufferUploadCommandRequest .cxx_destruct]
+ -[HAPCameraBufferUploadCommandRequest command]
+ -[HAPCameraBufferUploadCommandRequest copyWithZone:]
+ -[HAPCameraBufferUploadCommandRequest description]
+ -[HAPCameraBufferUploadCommandRequest initWithSessionID:command:start:stop:stopAction:]
+ -[HAPCameraBufferUploadCommandRequest init]
+ -[HAPCameraBufferUploadCommandRequest isEqual:]
+ -[HAPCameraBufferUploadCommandRequest parseFromData:error:]
+ -[HAPCameraBufferUploadCommandRequest serializeWithError:]
+ -[HAPCameraBufferUploadCommandRequest sessionID]
+ -[HAPCameraBufferUploadCommandRequest setCommand:]
+ -[HAPCameraBufferUploadCommandRequest setSessionID:]
+ -[HAPCameraBufferUploadCommandRequest setStart:]
+ -[HAPCameraBufferUploadCommandRequest setStop:]
+ -[HAPCameraBufferUploadCommandRequest setStopAction:]
+ -[HAPCameraBufferUploadCommandRequest start]
+ -[HAPCameraBufferUploadCommandRequest stopAction]
+ -[HAPCameraBufferUploadCommandRequest stop]
+ -[HAPCameraBufferUploadCommandResponse .cxx_destruct]
+ -[HAPCameraBufferUploadCommandResponse clipID]
+ -[HAPCameraBufferUploadCommandResponse copyWithZone:]
+ -[HAPCameraBufferUploadCommandResponse description]
+ -[HAPCameraBufferUploadCommandResponse initWithClipID:]
+ -[HAPCameraBufferUploadCommandResponse init]
+ -[HAPCameraBufferUploadCommandResponse isEqual:]
+ -[HAPCameraBufferUploadCommandResponse parseFromData:error:]
+ -[HAPCameraBufferUploadCommandResponse serializeWithError:]
+ -[HAPCameraBufferUploadCommandResponse setClipID:]
+ -[HAPCameraBufferUploadCommandTypeWrapper copyWithZone:]
+ -[HAPCameraBufferUploadCommandTypeWrapper description]
+ -[HAPCameraBufferUploadCommandTypeWrapper initWithValue:]
+ -[HAPCameraBufferUploadCommandTypeWrapper init]
+ -[HAPCameraBufferUploadCommandTypeWrapper isEqual:]
+ -[HAPCameraBufferUploadCommandTypeWrapper parseFromData:error:]
+ -[HAPCameraBufferUploadCommandTypeWrapper serializeWithError:]
+ -[HAPCameraBufferUploadCommandTypeWrapper setValue:]
+ -[HAPCameraBufferUploadCommandTypeWrapper value]
+ -[HAPCameraBufferUploadStopActionWrapper copyWithZone:]
+ -[HAPCameraBufferUploadStopActionWrapper description]
+ -[HAPCameraBufferUploadStopActionWrapper initWithValue:]
+ -[HAPCameraBufferUploadStopActionWrapper init]
+ -[HAPCameraBufferUploadStopActionWrapper isEqual:]
+ -[HAPCameraBufferUploadStopActionWrapper parseFromData:error:]
+ -[HAPCameraBufferUploadStopActionWrapper serializeWithError:]
+ -[HAPCameraBufferUploadStopActionWrapper setValue:]
+ -[HAPCameraBufferUploadStopActionWrapper value]
+ -[HAPCameraCapabilitiesResponse .cxx_destruct]
+ -[HAPCameraCapabilitiesResponse cameraSensors]
+ -[HAPCameraCapabilitiesResponse copyWithZone:]
+ -[HAPCameraCapabilitiesResponse description]
+ -[HAPCameraCapabilitiesResponse initWithVersion:videoStreamCapabilities:cameraSensors:]
+ -[HAPCameraCapabilitiesResponse init]
+ -[HAPCameraCapabilitiesResponse isEqual:]
+ -[HAPCameraCapabilitiesResponse parseFromData:error:]
+ -[HAPCameraCapabilitiesResponse serializeWithError:]
+ -[HAPCameraCapabilitiesResponse setCameraSensors:]
+ -[HAPCameraCapabilitiesResponse setVersion:]
+ -[HAPCameraCapabilitiesResponse setVideoStreamCapabilities:]
+ -[HAPCameraCapabilitiesResponse version]
+ -[HAPCameraCapabilitiesResponse videoStreamCapabilities]
+ -[HAPCameraClientCSR .cxx_destruct]
+ -[HAPCameraClientCSR CSR]
+ -[HAPCameraClientCSR copyWithZone:]
+ -[HAPCameraClientCSR description]
+ -[HAPCameraClientCSR initWithCSR:]
+ -[HAPCameraClientCSR init]
+ -[HAPCameraClientCSR isEqual:]
+ -[HAPCameraClientCSR parseFromData:error:]
+ -[HAPCameraClientCSR serializeWithError:]
+ -[HAPCameraClientCSR setCSR:]
+ -[HAPCameraClientCertificate .cxx_destruct]
+ -[HAPCameraClientCertificate CA]
+ -[HAPCameraClientCertificate clientCertificate]
+ -[HAPCameraClientCertificate copyWithZone:]
+ -[HAPCameraClientCertificate description]
+ -[HAPCameraClientCertificate initWithClientCertificate:CA:]
+ -[HAPCameraClientCertificate init]
+ -[HAPCameraClientCertificate isEqual:]
+ -[HAPCameraClientCertificate parseFromData:error:]
+ -[HAPCameraClientCertificate serializeWithError:]
+ -[HAPCameraClientCertificate setCA:]
+ -[HAPCameraClientCertificate setClientCertificate:]
+ -[HAPCameraClientCertificateStatus .cxx_destruct]
+ -[HAPCameraClientCertificateStatus copyWithZone:]
+ -[HAPCameraClientCertificateStatus description]
+ -[HAPCameraClientCertificateStatus initWithNeedsUpdate:]
+ -[HAPCameraClientCertificateStatus init]
+ -[HAPCameraClientCertificateStatus isEqual:]
+ -[HAPCameraClientCertificateStatus needsUpdate]
+ -[HAPCameraClientCertificateStatus parseFromData:error:]
+ -[HAPCameraClientCertificateStatus serializeWithError:]
+ -[HAPCameraClientCertificateStatus setNeedsUpdate:]
+ -[HAPCameraKey .cxx_destruct]
+ -[HAPCameraKey copyWithZone:]
+ -[HAPCameraKey description]
+ -[HAPCameraKey initWithKey:keyNumber:]
+ -[HAPCameraKey init]
+ -[HAPCameraKey isEqual:]
+ -[HAPCameraKey keyNumber]
+ -[HAPCameraKey key]
+ -[HAPCameraKey parseFromData:error:]
+ -[HAPCameraKey serializeWithError:]
+ -[HAPCameraKey setKey:]
+ -[HAPCameraKey setKeyNumber:]
+ -[HAPCameraKeyID .cxx_destruct]
+ -[HAPCameraKeyID copyWithZone:]
+ -[HAPCameraKeyID description]
+ -[HAPCameraKeyID initWithKeyID:]
+ -[HAPCameraKeyID init]
+ -[HAPCameraKeyID isEqual:]
+ -[HAPCameraKeyID keyID]
+ -[HAPCameraKeyID parseFromData:error:]
+ -[HAPCameraKeyID serializeWithError:]
+ -[HAPCameraKeyID setKeyID:]
+ -[HAPCameraRecordingPublishingPoint .cxx_destruct]
+ -[HAPCameraRecordingPublishingPoint URL]
+ -[HAPCameraRecordingPublishingPoint copyWithZone:]
+ -[HAPCameraRecordingPublishingPoint description]
+ -[HAPCameraRecordingPublishingPoint initWithURL:serverCertificate:]
+ -[HAPCameraRecordingPublishingPoint init]
+ -[HAPCameraRecordingPublishingPoint isEqual:]
+ -[HAPCameraRecordingPublishingPoint parseFromData:error:]
+ -[HAPCameraRecordingPublishingPoint serializeWithError:]
+ -[HAPCameraRecordingPublishingPoint serverCertificate]
+ -[HAPCameraRecordingPublishingPoint setServerCertificate:]
+ -[HAPCameraRecordingPublishingPoint setURL:]
+ -[HAPCameraSensors .cxx_destruct]
+ -[HAPCameraSensors cameraSensors]
+ -[HAPCameraSensors copyWithZone:]
+ -[HAPCameraSensors description]
+ -[HAPCameraSensors initWithCameraSensors:]
+ -[HAPCameraSensors init]
+ -[HAPCameraSensors isEqual:]
+ -[HAPCameraSensors parseFromData:error:]
+ -[HAPCameraSensors serializeWithError:]
+ -[HAPCameraSensors setCameraSensors:]
+ -[HAPCameraVideoQualityWrapper copyWithZone:]
+ -[HAPCameraVideoQualityWrapper description]
+ -[HAPCameraVideoQualityWrapper initWithValue:]
+ -[HAPCameraVideoQualityWrapper init]
+ -[HAPCameraVideoQualityWrapper isEqual:]
+ -[HAPCameraVideoQualityWrapper parseFromData:error:]
+ -[HAPCameraVideoQualityWrapper serializeWithError:]
+ -[HAPCameraVideoQualityWrapper setValue:]
+ -[HAPCameraVideoQualityWrapper value]
+ -[HAPCameraVideoStreamCapabilities .cxx_destruct]
+ -[HAPCameraVideoStreamCapabilities averageBitrate]
+ -[HAPCameraVideoStreamCapabilities copyWithZone:]
+ -[HAPCameraVideoStreamCapabilities description]
+ -[HAPCameraVideoStreamCapabilities framesPerSecond]
+ -[HAPCameraVideoStreamCapabilities height]
+ -[HAPCameraVideoStreamCapabilities identifier]
+ -[HAPCameraVideoStreamCapabilities initWithIdentifier:quality:width:height:framesPerSecond:averageBitrate:peakBitrate:]
+ -[HAPCameraVideoStreamCapabilities init]
+ -[HAPCameraVideoStreamCapabilities isEqual:]
+ -[HAPCameraVideoStreamCapabilities parseFromData:error:]
+ -[HAPCameraVideoStreamCapabilities peakBitrate]
+ -[HAPCameraVideoStreamCapabilities quality]
+ -[HAPCameraVideoStreamCapabilities serializeWithError:]
+ -[HAPCameraVideoStreamCapabilities setAverageBitrate:]
+ -[HAPCameraVideoStreamCapabilities setFramesPerSecond:]
+ -[HAPCameraVideoStreamCapabilities setHeight:]
+ -[HAPCameraVideoStreamCapabilities setIdentifier:]
+ -[HAPCameraVideoStreamCapabilities setPeakBitrate:]
+ -[HAPCameraVideoStreamCapabilities setQuality:]
+ -[HAPCameraVideoStreamCapabilities setWidth:]
+ -[HAPCameraVideoStreamCapabilities width]
+ -[HAPCameraZones .cxx_destruct]
+ -[HAPCameraZones copyWithZone:]
+ -[HAPCameraZones description]
+ -[HAPCameraZones initWithZoneDataVersion:zoneData:]
+ -[HAPCameraZones init]
+ -[HAPCameraZones isEqual:]
+ -[HAPCameraZones parseFromData:error:]
+ -[HAPCameraZones serializeWithError:]
+ -[HAPCameraZones setZoneData:]
+ -[HAPCameraZones setZoneDataVersion:]
+ -[HAPCameraZones zoneDataVersion]
+ -[HAPCameraZones zoneData]
+ -[HAPKeychainItem revision]
+ -[HAPPolygon .cxx_destruct]
+ -[HAPPolygon copyWithZone:]
+ -[HAPPolygon count]
+ -[HAPPolygon description]
+ -[HAPPolygon identifier]
+ -[HAPPolygon initWithIdentifier:count:vertices:]
+ -[HAPPolygon init]
+ -[HAPPolygon isEqual:]
+ -[HAPPolygon parseFromData:error:]
+ -[HAPPolygon serializeWithError:]
+ -[HAPPolygon setCount:]
+ -[HAPPolygon setIdentifier:]
+ -[HAPPolygon setVertices:]
+ -[HAPPolygon vertices]
+ -[HAPRTPStreamingControlCommandWrapper copyWithZone:]
+ -[HAPRTPStreamingControlCommandWrapper description]
+ -[HAPRTPStreamingControlCommandWrapper initWithValue:]
+ -[HAPRTPStreamingControlCommandWrapper init]
+ -[HAPRTPStreamingControlCommandWrapper isEqual:]
+ -[HAPRTPStreamingControlCommandWrapper parseFromData:error:]
+ -[HAPRTPStreamingControlCommandWrapper serializeWithError:]
+ -[HAPRTPStreamingControlCommandWrapper setValue:]
+ -[HAPRTPStreamingControlCommandWrapper value]
+ -[HAPRTPStreamingControlRequest .cxx_destruct]
+ -[HAPRTPStreamingControlRequest audioSSRC]
+ -[HAPRTPStreamingControlRequest audioTier]
+ -[HAPRTPStreamingControlRequest command]
+ -[HAPRTPStreamingControlRequest copyWithZone:]
+ -[HAPRTPStreamingControlRequest description]
+ -[HAPRTPStreamingControlRequest initWithSessionIdentifier:command:videoTier:videoSSRC:audioTier:audioSSRC:]
+ -[HAPRTPStreamingControlRequest init]
+ -[HAPRTPStreamingControlRequest isEqual:]
+ -[HAPRTPStreamingControlRequest parseFromData:error:]
+ -[HAPRTPStreamingControlRequest serializeWithError:]
+ -[HAPRTPStreamingControlRequest sessionIdentifier]
+ -[HAPRTPStreamingControlRequest setAudioSSRC:]
+ -[HAPRTPStreamingControlRequest setAudioTier:]
+ -[HAPRTPStreamingControlRequest setCommand:]
+ -[HAPRTPStreamingControlRequest setSessionIdentifier:]
+ -[HAPRTPStreamingControlRequest setVideoSSRC:]
+ -[HAPRTPStreamingControlRequest setVideoTier:]
+ -[HAPRTPStreamingControlRequest videoSSRC]
+ -[HAPRTPStreamingControlRequest videoTier]
+ -[HAPRTPStreamingControlResponse .cxx_destruct]
+ -[HAPRTPStreamingControlResponse copyWithZone:]
+ -[HAPRTPStreamingControlResponse description]
+ -[HAPRTPStreamingControlResponse initWithSessionIdentifier:status:]
+ -[HAPRTPStreamingControlResponse init]
+ -[HAPRTPStreamingControlResponse isEqual:]
+ -[HAPRTPStreamingControlResponse parseFromData:error:]
+ -[HAPRTPStreamingControlResponse serializeWithError:]
+ -[HAPRTPStreamingControlResponse sessionIdentifier]
+ -[HAPRTPStreamingControlResponse setSessionIdentifier:]
+ -[HAPRTPStreamingControlResponse setStatus:]
+ -[HAPRTPStreamingControlResponse status]
+ -[HAPRTPStreamingControlStatusWrapper copyWithZone:]
+ -[HAPRTPStreamingControlStatusWrapper description]
+ -[HAPRTPStreamingControlStatusWrapper initWithValue:]
+ -[HAPRTPStreamingControlStatusWrapper init]
+ -[HAPRTPStreamingControlStatusWrapper isEqual:]
+ -[HAPRTPStreamingControlStatusWrapper parseFromData:error:]
+ -[HAPRTPStreamingControlStatusWrapper serializeWithError:]
+ -[HAPRTPStreamingControlStatusWrapper setValue:]
+ -[HAPRTPStreamingControlStatusWrapper value]
+ -[HAPSensorConfiguration .cxx_destruct]
+ -[HAPSensorConfiguration copyWithZone:]
+ -[HAPSensorConfiguration description]
+ -[HAPSensorConfiguration initWithSensorDimensions:]
+ -[HAPSensorConfiguration init]
+ -[HAPSensorConfiguration isEqual:]
+ -[HAPSensorConfiguration parseFromData:error:]
+ -[HAPSensorConfiguration sensorDimensions]
+ -[HAPSensorConfiguration serializeWithError:]
+ -[HAPSensorConfiguration setSensorDimensions:]
+ -[HAPSensorDimensions .cxx_destruct]
+ -[HAPSensorDimensions copyWithZone:]
+ -[HAPSensorDimensions description]
+ -[HAPSensorDimensions height]
+ -[HAPSensorDimensions initWithWidth:height:]
+ -[HAPSensorDimensions init]
+ -[HAPSensorDimensions isEqual:]
+ -[HAPSensorDimensions parseFromData:error:]
+ -[HAPSensorDimensions serializeWithError:]
+ -[HAPSensorDimensions setHeight:]
+ -[HAPSensorDimensions setWidth:]
+ -[HAPSensorDimensions width]
+ -[HAPSupportedAudioStreamTiers .cxx_destruct]
+ -[HAPSupportedAudioStreamTiers codec]
+ -[HAPSupportedAudioStreamTiers copyWithZone:]
+ -[HAPSupportedAudioStreamTiers description]
+ -[HAPSupportedAudioStreamTiers initWithCodec:payloadType:tiers:]
+ -[HAPSupportedAudioStreamTiers init]
+ -[HAPSupportedAudioStreamTiers isEqual:]
+ -[HAPSupportedAudioStreamTiers parseFromData:error:]
+ -[HAPSupportedAudioStreamTiers payloadType]
+ -[HAPSupportedAudioStreamTiers serializeWithError:]
+ -[HAPSupportedAudioStreamTiers setCodec:]
+ -[HAPSupportedAudioStreamTiers setPayloadType:]
+ -[HAPSupportedAudioStreamTiers setTiers:]
+ -[HAPSupportedAudioStreamTiers tiers]
+ -[HAPSupportedVideoStreamTiers .cxx_destruct]
+ -[HAPSupportedVideoStreamTiers codec]
+ -[HAPSupportedVideoStreamTiers copyWithZone:]
+ -[HAPSupportedVideoStreamTiers description]
+ -[HAPSupportedVideoStreamTiers initWithCodec:payloadType:tiers:]
+ -[HAPSupportedVideoStreamTiers init]
+ -[HAPSupportedVideoStreamTiers isEqual:]
+ -[HAPSupportedVideoStreamTiers parseFromData:error:]
+ -[HAPSupportedVideoStreamTiers payloadType]
+ -[HAPSupportedVideoStreamTiers serializeWithError:]
+ -[HAPSupportedVideoStreamTiers setCodec:]
+ -[HAPSupportedVideoStreamTiers setPayloadType:]
+ -[HAPSupportedVideoStreamTiers setTiers:]
+ -[HAPSupportedVideoStreamTiers tiers]
+ -[HAPSystemKeychainStore _newLowestUUIDUsernameForHH2ControllerKey]
+ -[HAPSystemKeychainStore _preferredHH2ControllerKey]
+ -[HAPSystemKeychainStore allowsRemovedAccessoryKeys]
+ -[HAPSystemKeychainStore clearRemovedAccessoryKeysPriorToTime:error:]
+ -[HAPSystemKeychainStore cloneRemovedAccessoryKeyForName:iCloudIdentifier:error:]
+ -[HAPSystemKeychainStore dataSource]
+ -[HAPSystemKeychainStore deleteRemovedAccessoryKeyForName:error:]
+ -[HAPSystemKeychainStore hh2KeychainItemWithIdentifier:]
+ -[HAPSystemKeychainStore initWithDataSource:]
+ -[HAPSystemKeychainStore readPublicKeyForRemovedAccessoryName:iCloudIdentifier:error:]
+ -[HAPSystemKeychainStoreDefaultDataSource isHH2KeyRollEnabled]
+ -[HAPVideoCodecTypeWrapper copyWithZone:]
+ -[HAPVideoCodecTypeWrapper description]
+ -[HAPVideoCodecTypeWrapper initWithValue:]
+ -[HAPVideoCodecTypeWrapper init]
+ -[HAPVideoCodecTypeWrapper isEqual:]
+ -[HAPVideoCodecTypeWrapper parseFromData:error:]
+ -[HAPVideoCodecTypeWrapper serializeWithError:]
+ -[HAPVideoCodecTypeWrapper setValue:]
+ -[HAPVideoCodecTypeWrapper value]
+ -[HAPVideoStreamTier .cxx_destruct]
+ -[HAPVideoStreamTier copyWithZone:]
+ -[HAPVideoStreamTier description]
+ -[HAPVideoStreamTier frameRate]
+ -[HAPVideoStreamTier height]
+ -[HAPVideoStreamTier identifier]
+ -[HAPVideoStreamTier initWithIdentifier:quality:targetAverageBitrate:width:height:frameRate:]
+ -[HAPVideoStreamTier init]
+ -[HAPVideoStreamTier isEqual:]
+ -[HAPVideoStreamTier parseFromData:error:]
+ -[HAPVideoStreamTier quality]
+ -[HAPVideoStreamTier serializeWithError:]
+ -[HAPVideoStreamTier setFrameRate:]
+ -[HAPVideoStreamTier setHeight:]
+ -[HAPVideoStreamTier setIdentifier:]
+ -[HAPVideoStreamTier setQuality:]
+ -[HAPVideoStreamTier setTargetAverageBitrate:]
+ -[HAPVideoStreamTier setWidth:]
+ -[HAPVideoStreamTier targetAverageBitrate]
+ -[HAPVideoStreamTier width]
+ -[HAPWACAccessoryBrowser _completeRefreshScanWithResult:]
+ -[HAPWACAccessoryBrowser _handleRefreshScanResults:status:]
+ -[HAPWACAccessoryBrowser _refreshScanResultForSSID:completion:]
+ -[HAPWACAccessoryBrowser lastScanUptime]
+ -[HAPWACAccessoryBrowser refreshScanCompletion]
+ -[HAPWACAccessoryBrowser refreshScanResultForSSID:completion:]
+ -[HAPWACAccessoryBrowser refreshingScanSSID]
+ -[HAPWACAccessoryBrowser setLastScanUptime:]
+ -[HAPWACAccessoryBrowser setRefreshScanCompletion:]
+ -[HAPWACAccessoryBrowser setRefreshingScanSSID:]
+ -[HAPWACAccessoryBrowser timeSinceLastScan]
+ -[HAPWACAccessoryClient _performWiFiJoinWithScanResult:completion:]
+ -[HAPWACAccessoryClient _restoreNetworkWithNetworkInfo:completion:]
+ -[HAPWebRTCICECandidate .cxx_destruct]
+ -[HAPWebRTCICECandidate SDPMLineIndex]
+ -[HAPWebRTCICECandidate SDPMid]
+ -[HAPWebRTCICECandidate candidate]
+ -[HAPWebRTCICECandidate copyWithZone:]
+ -[HAPWebRTCICECandidate description]
+ -[HAPWebRTCICECandidate initWithCandidate:SDPMid:SDPMLineIndex:]
+ -[HAPWebRTCICECandidate init]
+ -[HAPWebRTCICECandidate isEqual:]
+ -[HAPWebRTCICECandidate parseFromData:error:]
+ -[HAPWebRTCICECandidate serializeWithError:]
+ -[HAPWebRTCICECandidate setCandidate:]
+ -[HAPWebRTCICECandidate setSDPMLineIndex:]
+ -[HAPWebRTCICECandidate setSDPMid:]
+ -[HAPWebRTCOfferStatusWrapper copyWithZone:]
+ -[HAPWebRTCOfferStatusWrapper description]
+ -[HAPWebRTCOfferStatusWrapper initWithValue:]
+ -[HAPWebRTCOfferStatusWrapper init]
+ -[HAPWebRTCOfferStatusWrapper isEqual:]
+ -[HAPWebRTCOfferStatusWrapper parseFromData:error:]
+ -[HAPWebRTCOfferStatusWrapper serializeWithError:]
+ -[HAPWebRTCOfferStatusWrapper setValue:]
+ -[HAPWebRTCOfferStatusWrapper value]
+ -[HAPWebRTCProvideAnswerRequest .cxx_destruct]
+ -[HAPWebRTCProvideAnswerRequest SDPAnswer]
+ -[HAPWebRTCProvideAnswerRequest additionalCandidates]
+ -[HAPWebRTCProvideAnswerRequest copyWithZone:]
+ -[HAPWebRTCProvideAnswerRequest description]
+ -[HAPWebRTCProvideAnswerRequest initWithSessionIdentifier:SDPAnswer:additionalCandidates:]
+ -[HAPWebRTCProvideAnswerRequest init]
+ -[HAPWebRTCProvideAnswerRequest isEqual:]
+ -[HAPWebRTCProvideAnswerRequest parseFromData:error:]
+ -[HAPWebRTCProvideAnswerRequest serializeWithError:]
+ -[HAPWebRTCProvideAnswerRequest sessionIdentifier]
+ -[HAPWebRTCProvideAnswerRequest setAdditionalCandidates:]
+ -[HAPWebRTCProvideAnswerRequest setSDPAnswer:]
+ -[HAPWebRTCProvideAnswerRequest setSessionIdentifier:]
+ -[HAPWebRTCReofferRequest .cxx_destruct]
+ -[HAPWebRTCReofferRequest SDPOffer]
+ -[HAPWebRTCReofferRequest SFrameConfiguration]
+ -[HAPWebRTCReofferRequest copyWithZone:]
+ -[HAPWebRTCReofferRequest description]
+ -[HAPWebRTCReofferRequest initWithSessionIdentifier:SDPOffer:SFrameConfiguration:]
+ -[HAPWebRTCReofferRequest init]
+ -[HAPWebRTCReofferRequest isEqual:]
+ -[HAPWebRTCReofferRequest parseFromData:error:]
+ -[HAPWebRTCReofferRequest serializeWithError:]
+ -[HAPWebRTCReofferRequest sessionIdentifier]
+ -[HAPWebRTCReofferRequest setSDPOffer:]
+ -[HAPWebRTCReofferRequest setSFrameConfiguration:]
+ -[HAPWebRTCReofferRequest setSessionIdentifier:]
+ -[HAPWebRTCReofferResponse .cxx_destruct]
+ -[HAPWebRTCReofferResponse SDPAnswer]
+ -[HAPWebRTCReofferResponse copyWithZone:]
+ -[HAPWebRTCReofferResponse description]
+ -[HAPWebRTCReofferResponse initWithSessionIdentifier:SDPAnswer:status:]
+ -[HAPWebRTCReofferResponse init]
+ -[HAPWebRTCReofferResponse isEqual:]
+ -[HAPWebRTCReofferResponse parseFromData:error:]
+ -[HAPWebRTCReofferResponse serializeWithError:]
+ -[HAPWebRTCReofferResponse sessionIdentifier]
+ -[HAPWebRTCReofferResponse setSDPAnswer:]
+ -[HAPWebRTCReofferResponse setSessionIdentifier:]
+ -[HAPWebRTCReofferResponse setStatus:]
+ -[HAPWebRTCReofferResponse status]
+ -[HAPWebRTCSFrameConfiguration .cxx_destruct]
+ -[HAPWebRTCSFrameConfiguration audioCipherSuite]
+ -[HAPWebRTCSFrameConfiguration baseKey]
+ -[HAPWebRTCSFrameConfiguration copyWithZone:]
+ -[HAPWebRTCSFrameConfiguration description]
+ -[HAPWebRTCSFrameConfiguration initWithAudioCipherSuite:videoCipherSuite:baseKey:keyID:ratchetBits:ratchetTime:]
+ -[HAPWebRTCSFrameConfiguration init]
+ -[HAPWebRTCSFrameConfiguration isEqual:]
+ -[HAPWebRTCSFrameConfiguration keyID]
+ -[HAPWebRTCSFrameConfiguration parseFromData:error:]
+ -[HAPWebRTCSFrameConfiguration ratchetBits]
+ -[HAPWebRTCSFrameConfiguration ratchetTime]
+ -[HAPWebRTCSFrameConfiguration serializeWithError:]
+ -[HAPWebRTCSFrameConfiguration setAudioCipherSuite:]
+ -[HAPWebRTCSFrameConfiguration setBaseKey:]
+ -[HAPWebRTCSFrameConfiguration setKeyID:]
+ -[HAPWebRTCSFrameConfiguration setRatchetBits:]
+ -[HAPWebRTCSFrameConfiguration setRatchetTime:]
+ -[HAPWebRTCSFrameConfiguration setVideoCipherSuite:]
+ -[HAPWebRTCSFrameConfiguration videoCipherSuite]
+ -[HAPWebRTCSolicitOfferRequest .cxx_destruct]
+ -[HAPWebRTCSolicitOfferRequest SFrameConfiguration]
+ -[HAPWebRTCSolicitOfferRequest copyWithZone:]
+ -[HAPWebRTCSolicitOfferRequest description]
+ -[HAPWebRTCSolicitOfferRequest initWithSFrameConfiguration:]
+ -[HAPWebRTCSolicitOfferRequest init]
+ -[HAPWebRTCSolicitOfferRequest isEqual:]
+ -[HAPWebRTCSolicitOfferRequest parseFromData:error:]
+ -[HAPWebRTCSolicitOfferRequest serializeWithError:]
+ -[HAPWebRTCSolicitOfferRequest setSFrameConfiguration:]
+ -[HAPWebRTCSolicitOfferResponse .cxx_destruct]
+ -[HAPWebRTCSolicitOfferResponse KID]
+ -[HAPWebRTCSolicitOfferResponse SDPOffer]
+ -[HAPWebRTCSolicitOfferResponse additionalCandidates]
+ -[HAPWebRTCSolicitOfferResponse copyWithZone:]
+ -[HAPWebRTCSolicitOfferResponse description]
+ -[HAPWebRTCSolicitOfferResponse initWithSessionIdentifier:SDPOffer:additionalCandidates:status:KID:]
+ -[HAPWebRTCSolicitOfferResponse init]
+ -[HAPWebRTCSolicitOfferResponse isEqual:]
+ -[HAPWebRTCSolicitOfferResponse parseFromData:error:]
+ -[HAPWebRTCSolicitOfferResponse serializeWithError:]
+ -[HAPWebRTCSolicitOfferResponse sessionIdentifier]
+ -[HAPWebRTCSolicitOfferResponse setAdditionalCandidates:]
+ -[HAPWebRTCSolicitOfferResponse setKID:]
+ -[HAPWebRTCSolicitOfferResponse setSDPOffer:]
+ -[HAPWebRTCSolicitOfferResponse setSessionIdentifier:]
+ -[HAPWebRTCSolicitOfferResponse setStatus:]
+ -[HAPWebRTCSolicitOfferResponse status]
+ -[HAPWebRTCStreamingControlRequest .cxx_destruct]
+ -[HAPWebRTCStreamingControlRequest copyWithZone:]
+ -[HAPWebRTCStreamingControlRequest description]
+ -[HAPWebRTCStreamingControlRequest initWithSessionIdentifier:]
+ -[HAPWebRTCStreamingControlRequest init]
+ -[HAPWebRTCStreamingControlRequest isEqual:]
+ -[HAPWebRTCStreamingControlRequest parseFromData:error:]
+ -[HAPWebRTCStreamingControlRequest serializeWithError:]
+ -[HAPWebRTCStreamingControlRequest sessionIdentifier]
+ -[HAPWebRTCStreamingControlRequest setSessionIdentifier:]
+ -[HAPWebRTCStreamingControlResponse .cxx_destruct]
+ -[HAPWebRTCStreamingControlResponse copyWithZone:]
+ -[HAPWebRTCStreamingControlResponse description]
+ -[HAPWebRTCStreamingControlResponse initWithSessionIdentifier:status:]
+ -[HAPWebRTCStreamingControlResponse init]
+ -[HAPWebRTCStreamingControlResponse isEqual:]
+ -[HAPWebRTCStreamingControlResponse parseFromData:error:]
+ -[HAPWebRTCStreamingControlResponse serializeWithError:]
+ -[HAPWebRTCStreamingControlResponse sessionIdentifier]
+ -[HAPWebRTCStreamingControlResponse setSessionIdentifier:]
+ -[HAPWebRTCStreamingControlResponse setStatus:]
+ -[HAPWebRTCStreamingControlResponse status]
+ -[HAPWebRTCStreamingControlStatusWrapper copyWithZone:]
+ -[HAPWebRTCStreamingControlStatusWrapper description]
+ -[HAPWebRTCStreamingControlStatusWrapper initWithValue:]
+ -[HAPWebRTCStreamingControlStatusWrapper init]
+ -[HAPWebRTCStreamingControlStatusWrapper isEqual:]
+ -[HAPWebRTCStreamingControlStatusWrapper parseFromData:error:]
+ -[HAPWebRTCStreamingControlStatusWrapper serializeWithError:]
+ -[HAPWebRTCStreamingControlStatusWrapper setValue:]
+ -[HAPWebRTCStreamingControlStatusWrapper value]
+ -[HAPWebRTCStreamingStatusWrapper copyWithZone:]
+ -[HAPWebRTCStreamingStatusWrapper description]
+ -[HAPWebRTCStreamingStatusWrapper initWithValue:]
+ -[HAPWebRTCStreamingStatusWrapper init]
+ -[HAPWebRTCStreamingStatusWrapper isEqual:]
+ -[HAPWebRTCStreamingStatusWrapper parseFromData:error:]
+ -[HAPWebRTCStreamingStatusWrapper serializeWithError:]
+ -[HAPWebRTCStreamingStatusWrapper setValue:]
+ -[HAPWebRTCStreamingStatusWrapper value]
+ -[HAPZoneDataV2 .cxx_destruct]
+ -[HAPZoneDataV2 copyWithZone:]
+ -[HAPZoneDataV2 count]
+ -[HAPZoneDataV2 description]
+ -[HAPZoneDataV2 initWithInverted:count:polygons:]
+ -[HAPZoneDataV2 init]
+ -[HAPZoneDataV2 inverted]
+ -[HAPZoneDataV2 isEqual:]
+ -[HAPZoneDataV2 parseFromData:error:]
+ -[HAPZoneDataV2 polygons]
+ -[HAPZoneDataV2 serializeWithError:]
+ -[HAPZoneDataV2 setCount:]
+ -[HAPZoneDataV2 setInverted:]
+ -[HAPZoneDataV2 setPolygons:]
+ -[_HAPAccessoryServerBTLE200 enableRemovedAccessoryKey:completionQueue:completion:]
+ -[_HAPAccessoryServerBTLE200 removedAccessoryDiscoveryCompletionHandlers]
+ GCC_except_table1098
+ GCC_except_table1102
+ GCC_except_table1115
+ GCC_except_table1120
+ GCC_except_table1129
+ GCC_except_table1131
+ GCC_except_table1133
+ GCC_except_table1135
+ GCC_except_table1261
+ GCC_except_table1265
+ GCC_except_table1267
+ GCC_except_table1480
+ GCC_except_table1688
+ GCC_except_table1690
+ GCC_except_table1695
+ GCC_except_table1701
+ GCC_except_table1703
+ GCC_except_table1709
+ GCC_except_table1711
+ GCC_except_table1715
+ GCC_except_table1719
+ GCC_except_table1721
+ GCC_except_table1726
+ GCC_except_table1730
+ GCC_except_table1740
+ GCC_except_table1748
+ GCC_except_table1755
+ GCC_except_table1759
+ GCC_except_table1763
+ GCC_except_table1767
+ GCC_except_table1803
+ GCC_except_table1927
+ GCC_except_table1928
+ GCC_except_table1930
+ GCC_except_table1942
+ GCC_except_table1951
+ GCC_except_table1953
+ GCC_except_table1973
+ GCC_except_table1980
+ GCC_except_table1982
+ GCC_except_table1984
+ GCC_except_table1988
+ GCC_except_table1991
+ GCC_except_table1995
+ GCC_except_table1997
+ GCC_except_table2000
+ GCC_except_table2003
+ GCC_except_table2005
+ GCC_except_table2007
+ GCC_except_table201
+ GCC_except_table2011
+ GCC_except_table2015
+ GCC_except_table2023
+ GCC_except_table2034
+ GCC_except_table2078
+ GCC_except_table208
+ GCC_except_table2084
+ GCC_except_table210
+ GCC_except_table213
+ GCC_except_table216
+ GCC_except_table218
+ GCC_except_table221
+ GCC_except_table224
+ GCC_except_table2251
+ GCC_except_table2258
+ GCC_except_table226
+ GCC_except_table2264
+ GCC_except_table2268
+ GCC_except_table2272
+ GCC_except_table2275
+ GCC_except_table2278
+ GCC_except_table2280
+ GCC_except_table2283
+ GCC_except_table2289
+ GCC_except_table2291
+ GCC_except_table2295
+ GCC_except_table2296
+ GCC_except_table2298
+ GCC_except_table235
+ GCC_except_table239
+ GCC_except_table2394
+ GCC_except_table2402
+ GCC_except_table2403
+ GCC_except_table2404
+ GCC_except_table2405
+ GCC_except_table2406
+ GCC_except_table2407
+ GCC_except_table2422
+ GCC_except_table2436
+ GCC_except_table2516
+ GCC_except_table2528
+ GCC_except_table2554
+ GCC_except_table2562
+ GCC_except_table2573
+ GCC_except_table2587
+ GCC_except_table2590
+ GCC_except_table2595
+ GCC_except_table2603
+ GCC_except_table2609
+ GCC_except_table2611
+ GCC_except_table2836
+ GCC_except_table2852
+ GCC_except_table2855
+ GCC_except_table2869
+ GCC_except_table2870
+ GCC_except_table2877
+ GCC_except_table2892
+ GCC_except_table2904
+ GCC_except_table2905
+ GCC_except_table2907
+ GCC_except_table2913
+ GCC_except_table2920
+ GCC_except_table2923
+ GCC_except_table2933
+ GCC_except_table2989
+ GCC_except_table2992
+ GCC_except_table2997
+ GCC_except_table2999
+ GCC_except_table3013
+ GCC_except_table3029
+ GCC_except_table3033
+ GCC_except_table3041
+ GCC_except_table3049
+ GCC_except_table3098
+ GCC_except_table3106
+ GCC_except_table3108
+ GCC_except_table3109
+ GCC_except_table3132
+ GCC_except_table3376
+ GCC_except_table3442
+ GCC_except_table3443
+ GCC_except_table3450
+ GCC_except_table3452
+ GCC_except_table3455
+ GCC_except_table3456
+ GCC_except_table3458
+ GCC_except_table3465
+ GCC_except_table3475
+ GCC_except_table3478
+ GCC_except_table3489
+ GCC_except_table3490
+ GCC_except_table3492
+ GCC_except_table3494
+ GCC_except_table3497
+ GCC_except_table3500
+ GCC_except_table3502
+ GCC_except_table3508
+ GCC_except_table3520
+ GCC_except_table3522
+ GCC_except_table3526
+ GCC_except_table3530
+ GCC_except_table3534
+ GCC_except_table3560
+ GCC_except_table3578
+ GCC_except_table3582
+ GCC_except_table3585
+ GCC_except_table3587
+ GCC_except_table3589
+ GCC_except_table3677
+ GCC_except_table3678
+ GCC_except_table3679
+ GCC_except_table3680
+ GCC_except_table3681
+ GCC_except_table3682
+ GCC_except_table3683
+ GCC_except_table3684
+ GCC_except_table3685
+ GCC_except_table3686
+ GCC_except_table3687
+ GCC_except_table3688
+ GCC_except_table3689
+ GCC_except_table3690
+ GCC_except_table3727
+ GCC_except_table3753
+ GCC_except_table3844
+ GCC_except_table3851
+ GCC_except_table3893
+ GCC_except_table3906
+ GCC_except_table3915
+ GCC_except_table3918
+ GCC_except_table3921
+ GCC_except_table3926
+ GCC_except_table3941
+ GCC_except_table3943
+ GCC_except_table3946
+ GCC_except_table3957
+ GCC_except_table3969
+ GCC_except_table3976
+ GCC_except_table3977
+ GCC_except_table3981
+ GCC_except_table3982
+ GCC_except_table4000
+ GCC_except_table4002
+ GCC_except_table4004
+ GCC_except_table4005
+ GCC_except_table4008
+ GCC_except_table4014
+ GCC_except_table4017
+ GCC_except_table4019
+ GCC_except_table4025
+ GCC_except_table4027
+ GCC_except_table4030
+ GCC_except_table4042
+ GCC_except_table4053
+ GCC_except_table4055
+ GCC_except_table4064
+ GCC_except_table4070
+ GCC_except_table4330
+ GCC_except_table4336
+ GCC_except_table4353
+ GCC_except_table4357
+ GCC_except_table4374
+ GCC_except_table4380
+ GCC_except_table4393
+ GCC_except_table4407
+ GCC_except_table4411
+ GCC_except_table443
+ GCC_except_table4524
+ GCC_except_table453
+ GCC_except_table475
+ GCC_except_table4932
+ GCC_except_table4940
+ GCC_except_table4950
+ GCC_except_table4992
+ GCC_except_table4995
+ GCC_except_table4996
+ GCC_except_table4997
+ GCC_except_table4998
+ GCC_except_table505
+ GCC_except_table5080
+ GCC_except_table5081
+ GCC_except_table5082
+ GCC_except_table5083
+ GCC_except_table5084
+ GCC_except_table5085
+ GCC_except_table5091
+ GCC_except_table5092
+ GCC_except_table5094
+ GCC_except_table5101
+ GCC_except_table5104
+ GCC_except_table5106
+ GCC_except_table5111
+ GCC_except_table5114
+ GCC_except_table5117
+ GCC_except_table5121
+ GCC_except_table5125
+ GCC_except_table513
+ GCC_except_table527
+ GCC_except_table528
+ GCC_except_table530
+ GCC_except_table533
+ GCC_except_table536
+ GCC_except_table5472
+ GCC_except_table5473
+ GCC_except_table548
+ GCC_except_table5492
+ GCC_except_table5502
+ GCC_except_table5505
+ GCC_except_table5510
+ GCC_except_table5513
+ GCC_except_table552
+ GCC_except_table555
+ GCC_except_table562
+ GCC_except_table568
+ GCC_except_table5778
+ GCC_except_table5782
+ GCC_except_table5816
+ GCC_except_table5820
+ GCC_except_table5822
+ GCC_except_table5824
+ GCC_except_table596
+ GCC_except_table5993
+ GCC_except_table5999
+ GCC_except_table6003
+ GCC_except_table6004
+ GCC_except_table6005
+ GCC_except_table6006
+ GCC_except_table6012
+ GCC_except_table6028
+ GCC_except_table606
+ GCC_except_table6060
+ GCC_except_table6061
+ GCC_except_table6062
+ GCC_except_table6082
+ GCC_except_table6094
+ GCC_except_table6097
+ GCC_except_table6102
+ GCC_except_table6104
+ GCC_except_table6118
+ GCC_except_table613
+ GCC_except_table6341
+ GCC_except_table6354
+ GCC_except_table6359
+ GCC_except_table6362
+ GCC_except_table6363
+ GCC_except_table6368
+ GCC_except_table6398
+ GCC_except_table640
+ GCC_except_table6420
+ GCC_except_table6428
+ GCC_except_table6433
+ GCC_except_table6437
+ GCC_except_table644
+ GCC_except_table6441
+ GCC_except_table6459
+ GCC_except_table647
+ GCC_except_table649
+ GCC_except_table6523
+ GCC_except_table6524
+ GCC_except_table6525
+ GCC_except_table6526
+ GCC_except_table6527
+ GCC_except_table6528
+ GCC_except_table6529
+ GCC_except_table655
+ GCC_except_table657
+ GCC_except_table6587
+ GCC_except_table6591
+ GCC_except_table6592
+ GCC_except_table6604
+ GCC_except_table6610
+ GCC_except_table6623
+ GCC_except_table6626
+ GCC_except_table6627
+ GCC_except_table6632
+ GCC_except_table6635
+ GCC_except_table6642
+ GCC_except_table6645
+ GCC_except_table6659
+ GCC_except_table6666
+ GCC_except_table6672
+ GCC_except_table6683
+ GCC_except_table6687
+ GCC_except_table6688
+ GCC_except_table6705
+ GCC_except_table6707
+ GCC_except_table6716
+ GCC_except_table6731
+ GCC_except_table6732
+ GCC_except_table6737
+ GCC_except_table674
+ GCC_except_table6741
+ GCC_except_table6742
+ GCC_except_table6745
+ GCC_except_table6751
+ GCC_except_table6755
+ GCC_except_table6759
+ GCC_except_table6761
+ GCC_except_table6763
+ GCC_except_table6767
+ GCC_except_table678
+ GCC_except_table688
+ GCC_except_table6882
+ GCC_except_table689
+ GCC_except_table6919
+ GCC_except_table694
+ GCC_except_table697
+ GCC_except_table6975
+ GCC_except_table6978
+ GCC_except_table6982
+ GCC_except_table6988
+ GCC_except_table6995
+ GCC_except_table6996
+ GCC_except_table700
+ GCC_except_table7012
+ GCC_except_table7016
+ GCC_except_table7017
+ GCC_except_table7018
+ GCC_except_table705
+ GCC_except_table7067
+ GCC_except_table7068
+ GCC_except_table7070
+ GCC_except_table7073
+ GCC_except_table709
+ GCC_except_table7100
+ GCC_except_table7101
+ GCC_except_table7106
+ GCC_except_table7143
+ GCC_except_table7145
+ GCC_except_table715
+ GCC_except_table7159
+ GCC_except_table716
+ GCC_except_table7160
+ GCC_except_table7161
+ GCC_except_table7176
+ GCC_except_table7179
+ GCC_except_table7186
+ GCC_except_table7193
+ GCC_except_table7198
+ GCC_except_table7204
+ GCC_except_table721
+ GCC_except_table7216
+ GCC_except_table7217
+ GCC_except_table722
+ GCC_except_table7222
+ GCC_except_table7238
+ GCC_except_table7244
+ GCC_except_table7250
+ GCC_except_table7271
+ GCC_except_table7273
+ GCC_except_table7274
+ GCC_except_table7300
+ GCC_except_table7464
+ GCC_except_table749
+ GCC_except_table7527
+ GCC_except_table7559
+ GCC_except_table756
+ GCC_except_table7562
+ GCC_except_table763
+ GCC_except_table764
+ GCC_except_table7728
+ GCC_except_table7767
+ GCC_except_table7804
+ GCC_except_table7868
+ GCC_except_table7874
+ GCC_except_table7920
+ GCC_except_table7922
+ GCC_except_table7924
+ GCC_except_table7926
+ GCC_except_table7928
+ GCC_except_table7930
+ GCC_except_table7932
+ GCC_except_table7934
+ GCC_except_table7936
+ GCC_except_table7938
+ GCC_except_table7940
+ GCC_except_table7943
+ GCC_except_table7945
+ GCC_except_table7947
+ GCC_except_table7953
+ GCC_except_table7959
+ GCC_except_table7964
+ GCC_except_table7967
+ GCC_except_table7970
+ GCC_except_table798
+ GCC_except_table7996
+ GCC_except_table7999
+ GCC_except_table8000
+ GCC_except_table8039
+ GCC_except_table8040
+ GCC_except_table8041
+ GCC_except_table8043
+ GCC_except_table8044
+ GCC_except_table8046
+ GCC_except_table8047
+ GCC_except_table8048
+ GCC_except_table8050
+ GCC_except_table8051
+ GCC_except_table8053
+ GCC_except_table8057
+ GCC_except_table8058
+ GCC_except_table8062
+ GCC_except_table8110
+ GCC_except_table8117
+ GCC_except_table821
+ GCC_except_table8211
+ GCC_except_table8227
+ GCC_except_table8229
+ GCC_except_table8231
+ GCC_except_table8234
+ GCC_except_table8236
+ GCC_except_table8238
+ GCC_except_table8240
+ GCC_except_table8241
+ GCC_except_table8243
+ GCC_except_table8247
+ GCC_except_table8252
+ GCC_except_table840
+ GCC_except_table864
+ GCC_except_table868
+ GCC_except_table882
+ GCC_except_table887
+ GCC_except_table990
+ GCC_except_table992
+ _CFPreferencesCopyAppValue
+ _HAPAudioCodecBitDepthAsString
+ _HAPCameraBufferEventCommandTypeAsString
+ _HAPCameraBufferEventTypeAsString
+ _HAPCameraBufferTypeAsString
+ _HAPCameraBufferUploadCommandTypeAsString
+ _HAPCameraBufferUploadStopActionAsString
+ _HAPCameraVideoQualityAsString
+ _HAPRTPStreamingControlCommandAsString
+ _HAPRTPStreamingControlStatusAsString
+ _HAPUpdateReasonToString
+ _HAPVideoCodecTypeAsString
+ _HAPWebRTCOfferStatusAsString
+ _HAPWebRTCStreamingControlStatusAsString
+ _HAPWebRTCStreamingStatusAsString
+ _OBJC_CLASS_$_CtrClient
+ _OBJC_CLASS_$_HAP2ThreadNetworkUtil
+ _OBJC_CLASS_$_HAPAudioCodecBitDepthWrapper
+ _OBJC_CLASS_$_HAPAudioStreamTier
+ _OBJC_CLASS_$_HAPCameraBufferEvent
+ _OBJC_CLASS_$_HAPCameraBufferEventCMAFSessionStart
+ _OBJC_CLASS_$_HAPCameraBufferEventCMAFSessionStop
+ _OBJC_CLASS_$_HAPCameraBufferEventCommandRequest
+ _OBJC_CLASS_$_HAPCameraBufferEventCommandResponse
+ _OBJC_CLASS_$_HAPCameraBufferEventCommandTypeWrapper
+ _OBJC_CLASS_$_HAPCameraBufferEventMotion
+ _OBJC_CLASS_$_HAPCameraBufferEventTypeWrapper
+ _OBJC_CLASS_$_HAPCameraBufferInfo
+ _OBJC_CLASS_$_HAPCameraBufferInfoResponse
+ _OBJC_CLASS_$_HAPCameraBufferInterval
+ _OBJC_CLASS_$_HAPCameraBufferTypeWrapper
+ _OBJC_CLASS_$_HAPCameraBufferUploadCommandRequest
+ _OBJC_CLASS_$_HAPCameraBufferUploadCommandResponse
+ _OBJC_CLASS_$_HAPCameraBufferUploadCommandTypeWrapper
+ _OBJC_CLASS_$_HAPCameraBufferUploadStopActionWrapper
+ _OBJC_CLASS_$_HAPCameraCapabilitiesResponse
+ _OBJC_CLASS_$_HAPCameraClientCSR
+ _OBJC_CLASS_$_HAPCameraClientCertificate
+ _OBJC_CLASS_$_HAPCameraClientCertificateStatus
+ _OBJC_CLASS_$_HAPCameraKey
+ _OBJC_CLASS_$_HAPCameraKeyID
+ _OBJC_CLASS_$_HAPCameraRecordingPublishingPoint
+ _OBJC_CLASS_$_HAPCameraSensors
+ _OBJC_CLASS_$_HAPCameraVideoQualityWrapper
+ _OBJC_CLASS_$_HAPCameraVideoStreamCapabilities
+ _OBJC_CLASS_$_HAPCameraZones
+ _OBJC_CLASS_$_HAPPolygon
+ _OBJC_CLASS_$_HAPRTPStreamingControlCommandWrapper
+ _OBJC_CLASS_$_HAPRTPStreamingControlRequest
+ _OBJC_CLASS_$_HAPRTPStreamingControlResponse
+ _OBJC_CLASS_$_HAPRTPStreamingControlStatusWrapper
+ _OBJC_CLASS_$_HAPSensorConfiguration
+ _OBJC_CLASS_$_HAPSensorDimensions
+ _OBJC_CLASS_$_HAPSupportedAudioStreamTiers
+ _OBJC_CLASS_$_HAPSupportedVideoStreamTiers
+ _OBJC_CLASS_$_HAPSystemKeychainStoreDefaultDataSource
+ _OBJC_CLASS_$_HAPVideoCodecTypeWrapper
+ _OBJC_CLASS_$_HAPVideoStreamTier
+ _OBJC_CLASS_$_HAPWebRTCICECandidate
+ _OBJC_CLASS_$_HAPWebRTCOfferStatusWrapper
+ _OBJC_CLASS_$_HAPWebRTCProvideAnswerRequest
+ _OBJC_CLASS_$_HAPWebRTCReofferRequest
+ _OBJC_CLASS_$_HAPWebRTCReofferResponse
+ _OBJC_CLASS_$_HAPWebRTCSFrameConfiguration
+ _OBJC_CLASS_$_HAPWebRTCSolicitOfferRequest
+ _OBJC_CLASS_$_HAPWebRTCSolicitOfferResponse
+ _OBJC_CLASS_$_HAPWebRTCStreamingControlRequest
+ _OBJC_CLASS_$_HAPWebRTCStreamingControlResponse
+ _OBJC_CLASS_$_HAPWebRTCStreamingControlStatusWrapper
+ _OBJC_CLASS_$_HAPWebRTCStreamingStatusWrapper
+ _OBJC_CLASS_$_HAPZoneDataV2
+ _OBJC_CLASS_$_HMFIDSDate
+ _OBJC_IVAR_$_HAP2AccessoryServer._removedAccessoryKey
+ _OBJC_IVAR_$_HAPAccessoryServer._removedAccessoryKey
+ _OBJC_IVAR_$_HAPAccessoryServerBrowser._removedAccessoryIdentifiers
+ _OBJC_IVAR_$_HAPAccessoryServerIP._pendingBonjourAdd
+ _OBJC_IVAR_$_HAPAudioCodecBitDepthWrapper._value
+ _OBJC_IVAR_$_HAPAudioStreamTier._bitDepth
+ _OBJC_IVAR_$_HAPAudioStreamTier._identifier
+ _OBJC_IVAR_$_HAPAudioStreamTier._numberOfChannels
+ _OBJC_IVAR_$_HAPAudioStreamTier._packetTime
+ _OBJC_IVAR_$_HAPAudioStreamTier._sampleRate
+ _OBJC_IVAR_$_HAPAudioStreamTier._targetAverageBitrate
+ _OBJC_IVAR_$_HAPCameraBufferEvent._CMAFSessionStart
+ _OBJC_IVAR_$_HAPCameraBufferEvent._CMAFSessionStop
+ _OBJC_IVAR_$_HAPCameraBufferEvent._motion
+ _OBJC_IVAR_$_HAPCameraBufferEvent._sequenceNumber
+ _OBJC_IVAR_$_HAPCameraBufferEvent._type
+ _OBJC_IVAR_$_HAPCameraBufferEventCMAFSessionStart._CMAFSessionID
+ _OBJC_IVAR_$_HAPCameraBufferEventCMAFSessionStop._CMAFSessionID
+ _OBJC_IVAR_$_HAPCameraBufferEventCommandRequest._command
+ _OBJC_IVAR_$_HAPCameraBufferEventCommandRequest._limit
+ _OBJC_IVAR_$_HAPCameraBufferEventCommandRequest._sequenceNumber
+ _OBJC_IVAR_$_HAPCameraBufferEventCommandResponse._events
+ _OBJC_IVAR_$_HAPCameraBufferEventCommandTypeWrapper._value
+ _OBJC_IVAR_$_HAPCameraBufferEventMotion._active
+ _OBJC_IVAR_$_HAPCameraBufferEventTypeWrapper._value
+ _OBJC_IVAR_$_HAPCameraBufferInfo._identifier
+ _OBJC_IVAR_$_HAPCameraBufferInfo._intervals
+ _OBJC_IVAR_$_HAPCameraBufferInfo._type
+ _OBJC_IVAR_$_HAPCameraBufferInfoResponse._buffers
+ _OBJC_IVAR_$_HAPCameraBufferInfoResponse._version
+ _OBJC_IVAR_$_HAPCameraBufferInterval._count
+ _OBJC_IVAR_$_HAPCameraBufferInterval._sequenceNumber
+ _OBJC_IVAR_$_HAPCameraBufferTypeWrapper._value
+ _OBJC_IVAR_$_HAPCameraBufferUploadCommandRequest._command
+ _OBJC_IVAR_$_HAPCameraBufferUploadCommandRequest._sessionID
+ _OBJC_IVAR_$_HAPCameraBufferUploadCommandRequest._start
+ _OBJC_IVAR_$_HAPCameraBufferUploadCommandRequest._stop
+ _OBJC_IVAR_$_HAPCameraBufferUploadCommandRequest._stopAction
+ _OBJC_IVAR_$_HAPCameraBufferUploadCommandResponse._clipID
+ _OBJC_IVAR_$_HAPCameraBufferUploadCommandTypeWrapper._value
+ _OBJC_IVAR_$_HAPCameraBufferUploadStopActionWrapper._value
+ _OBJC_IVAR_$_HAPCameraCapabilitiesResponse._cameraSensors
+ _OBJC_IVAR_$_HAPCameraCapabilitiesResponse._version
+ _OBJC_IVAR_$_HAPCameraCapabilitiesResponse._videoStreamCapabilities
+ _OBJC_IVAR_$_HAPCameraClientCSR._CSR
+ _OBJC_IVAR_$_HAPCameraClientCertificate._CA
+ _OBJC_IVAR_$_HAPCameraClientCertificate._clientCertificate
+ _OBJC_IVAR_$_HAPCameraClientCertificateStatus._needsUpdate
+ _OBJC_IVAR_$_HAPCameraKey._key
+ _OBJC_IVAR_$_HAPCameraKey._keyNumber
+ _OBJC_IVAR_$_HAPCameraKeyID._keyID
+ _OBJC_IVAR_$_HAPCameraRecordingPublishingPoint._URL
+ _OBJC_IVAR_$_HAPCameraRecordingPublishingPoint._serverCertificate
+ _OBJC_IVAR_$_HAPCameraSensors._cameraSensors
+ _OBJC_IVAR_$_HAPCameraVideoQualityWrapper._value
+ _OBJC_IVAR_$_HAPCameraVideoStreamCapabilities._averageBitrate
+ _OBJC_IVAR_$_HAPCameraVideoStreamCapabilities._framesPerSecond
+ _OBJC_IVAR_$_HAPCameraVideoStreamCapabilities._height
+ _OBJC_IVAR_$_HAPCameraVideoStreamCapabilities._identifier
+ _OBJC_IVAR_$_HAPCameraVideoStreamCapabilities._peakBitrate
+ _OBJC_IVAR_$_HAPCameraVideoStreamCapabilities._quality
+ _OBJC_IVAR_$_HAPCameraVideoStreamCapabilities._width
+ _OBJC_IVAR_$_HAPCameraZones._zoneData
+ _OBJC_IVAR_$_HAPCameraZones._zoneDataVersion
+ _OBJC_IVAR_$_HAPPolygon._count
+ _OBJC_IVAR_$_HAPPolygon._identifier
+ _OBJC_IVAR_$_HAPPolygon._vertices
+ _OBJC_IVAR_$_HAPRTPStreamingControlCommandWrapper._value
+ _OBJC_IVAR_$_HAPRTPStreamingControlRequest._audioSSRC
+ _OBJC_IVAR_$_HAPRTPStreamingControlRequest._audioTier
+ _OBJC_IVAR_$_HAPRTPStreamingControlRequest._command
+ _OBJC_IVAR_$_HAPRTPStreamingControlRequest._sessionIdentifier
+ _OBJC_IVAR_$_HAPRTPStreamingControlRequest._videoSSRC
+ _OBJC_IVAR_$_HAPRTPStreamingControlRequest._videoTier
+ _OBJC_IVAR_$_HAPRTPStreamingControlResponse._sessionIdentifier
+ _OBJC_IVAR_$_HAPRTPStreamingControlResponse._status
+ _OBJC_IVAR_$_HAPRTPStreamingControlStatusWrapper._value
+ _OBJC_IVAR_$_HAPSensorConfiguration._sensorDimensions
+ _OBJC_IVAR_$_HAPSensorDimensions._height
+ _OBJC_IVAR_$_HAPSensorDimensions._width
+ _OBJC_IVAR_$_HAPService._lock
+ _OBJC_IVAR_$_HAPSupportedAudioStreamTiers._codec
+ _OBJC_IVAR_$_HAPSupportedAudioStreamTiers._payloadType
+ _OBJC_IVAR_$_HAPSupportedAudioStreamTiers._tiers
+ _OBJC_IVAR_$_HAPSupportedVideoStreamTiers._codec
+ _OBJC_IVAR_$_HAPSupportedVideoStreamTiers._payloadType
+ _OBJC_IVAR_$_HAPSupportedVideoStreamTiers._tiers
+ _OBJC_IVAR_$_HAPSystemKeychainStore._dataSource
+ _OBJC_IVAR_$_HAPVideoCodecTypeWrapper._value
+ _OBJC_IVAR_$_HAPVideoStreamTier._frameRate
+ _OBJC_IVAR_$_HAPVideoStreamTier._height
+ _OBJC_IVAR_$_HAPVideoStreamTier._identifier
+ _OBJC_IVAR_$_HAPVideoStreamTier._quality
+ _OBJC_IVAR_$_HAPVideoStreamTier._targetAverageBitrate
+ _OBJC_IVAR_$_HAPVideoStreamTier._width
+ _OBJC_IVAR_$_HAPWACAccessoryBrowser._lastScanUptime
+ _OBJC_IVAR_$_HAPWACAccessoryBrowser._refreshScanCompletion
+ _OBJC_IVAR_$_HAPWACAccessoryBrowser._refreshingScanSSID
+ _OBJC_IVAR_$_HAPWebRTCICECandidate._SDPMLineIndex
+ _OBJC_IVAR_$_HAPWebRTCICECandidate._SDPMid
+ _OBJC_IVAR_$_HAPWebRTCICECandidate._candidate
+ _OBJC_IVAR_$_HAPWebRTCOfferStatusWrapper._value
+ _OBJC_IVAR_$_HAPWebRTCProvideAnswerRequest._SDPAnswer
+ _OBJC_IVAR_$_HAPWebRTCProvideAnswerRequest._additionalCandidates
+ _OBJC_IVAR_$_HAPWebRTCProvideAnswerRequest._sessionIdentifier
+ _OBJC_IVAR_$_HAPWebRTCReofferRequest._SDPOffer
+ _OBJC_IVAR_$_HAPWebRTCReofferRequest._SFrameConfiguration
+ _OBJC_IVAR_$_HAPWebRTCReofferRequest._sessionIdentifier
+ _OBJC_IVAR_$_HAPWebRTCReofferResponse._SDPAnswer
+ _OBJC_IVAR_$_HAPWebRTCReofferResponse._sessionIdentifier
+ _OBJC_IVAR_$_HAPWebRTCReofferResponse._status
+ _OBJC_IVAR_$_HAPWebRTCSFrameConfiguration._audioCipherSuite
+ _OBJC_IVAR_$_HAPWebRTCSFrameConfiguration._baseKey
+ _OBJC_IVAR_$_HAPWebRTCSFrameConfiguration._keyID
+ _OBJC_IVAR_$_HAPWebRTCSFrameConfiguration._ratchetBits
+ _OBJC_IVAR_$_HAPWebRTCSFrameConfiguration._ratchetTime
+ _OBJC_IVAR_$_HAPWebRTCSFrameConfiguration._videoCipherSuite
+ _OBJC_IVAR_$_HAPWebRTCSolicitOfferRequest._SFrameConfiguration
+ _OBJC_IVAR_$_HAPWebRTCSolicitOfferResponse._KID
+ _OBJC_IVAR_$_HAPWebRTCSolicitOfferResponse._SDPOffer
+ _OBJC_IVAR_$_HAPWebRTCSolicitOfferResponse._additionalCandidates
+ _OBJC_IVAR_$_HAPWebRTCSolicitOfferResponse._sessionIdentifier
+ _OBJC_IVAR_$_HAPWebRTCSolicitOfferResponse._status
+ _OBJC_IVAR_$_HAPWebRTCStreamingControlRequest._sessionIdentifier
+ _OBJC_IVAR_$_HAPWebRTCStreamingControlResponse._sessionIdentifier
+ _OBJC_IVAR_$_HAPWebRTCStreamingControlResponse._status
+ _OBJC_IVAR_$_HAPWebRTCStreamingControlStatusWrapper._value
+ _OBJC_IVAR_$_HAPWebRTCStreamingStatusWrapper._value
+ _OBJC_IVAR_$_HAPZoneDataV2._count
+ _OBJC_IVAR_$_HAPZoneDataV2._inverted
+ _OBJC_IVAR_$_HAPZoneDataV2._polygons
+ _OBJC_IVAR_$__HAPAccessoryServerBTLE200._removedAccessoryDiscoveryCompletionHandlers
+ _OBJC_METACLASS_$_HAP2ThreadNetworkUtil
+ _OBJC_METACLASS_$_HAPAudioCodecBitDepthWrapper
+ _OBJC_METACLASS_$_HAPAudioStreamTier
+ _OBJC_METACLASS_$_HAPCameraBufferEvent
+ _OBJC_METACLASS_$_HAPCameraBufferEventCMAFSessionStart
+ _OBJC_METACLASS_$_HAPCameraBufferEventCMAFSessionStop
+ _OBJC_METACLASS_$_HAPCameraBufferEventCommandRequest
+ _OBJC_METACLASS_$_HAPCameraBufferEventCommandResponse
+ _OBJC_METACLASS_$_HAPCameraBufferEventCommandTypeWrapper
+ _OBJC_METACLASS_$_HAPCameraBufferEventMotion
+ _OBJC_METACLASS_$_HAPCameraBufferEventTypeWrapper
+ _OBJC_METACLASS_$_HAPCameraBufferInfo
+ _OBJC_METACLASS_$_HAPCameraBufferInfoResponse
+ _OBJC_METACLASS_$_HAPCameraBufferInterval
+ _OBJC_METACLASS_$_HAPCameraBufferTypeWrapper
+ _OBJC_METACLASS_$_HAPCameraBufferUploadCommandRequest
+ _OBJC_METACLASS_$_HAPCameraBufferUploadCommandResponse
+ _OBJC_METACLASS_$_HAPCameraBufferUploadCommandTypeWrapper
+ _OBJC_METACLASS_$_HAPCameraBufferUploadStopActionWrapper
+ _OBJC_METACLASS_$_HAPCameraCapabilitiesResponse
+ _OBJC_METACLASS_$_HAPCameraClientCSR
+ _OBJC_METACLASS_$_HAPCameraClientCertificate
+ _OBJC_METACLASS_$_HAPCameraClientCertificateStatus
+ _OBJC_METACLASS_$_HAPCameraKey
+ _OBJC_METACLASS_$_HAPCameraKeyID
+ _OBJC_METACLASS_$_HAPCameraRecordingPublishingPoint
+ _OBJC_METACLASS_$_HAPCameraSensors
+ _OBJC_METACLASS_$_HAPCameraVideoQualityWrapper
+ _OBJC_METACLASS_$_HAPCameraVideoStreamCapabilities
+ _OBJC_METACLASS_$_HAPCameraZones
+ _OBJC_METACLASS_$_HAPPolygon
+ _OBJC_METACLASS_$_HAPRTPStreamingControlCommandWrapper
+ _OBJC_METACLASS_$_HAPRTPStreamingControlRequest
+ _OBJC_METACLASS_$_HAPRTPStreamingControlResponse
+ _OBJC_METACLASS_$_HAPRTPStreamingControlStatusWrapper
+ _OBJC_METACLASS_$_HAPSensorConfiguration
+ _OBJC_METACLASS_$_HAPSensorDimensions
+ _OBJC_METACLASS_$_HAPSupportedAudioStreamTiers
+ _OBJC_METACLASS_$_HAPSupportedVideoStreamTiers
+ _OBJC_METACLASS_$_HAPSystemKeychainStoreDefaultDataSource
+ _OBJC_METACLASS_$_HAPVideoCodecTypeWrapper
+ _OBJC_METACLASS_$_HAPVideoStreamTier
+ _OBJC_METACLASS_$_HAPWebRTCICECandidate
+ _OBJC_METACLASS_$_HAPWebRTCOfferStatusWrapper
+ _OBJC_METACLASS_$_HAPWebRTCProvideAnswerRequest
+ _OBJC_METACLASS_$_HAPWebRTCReofferRequest
+ _OBJC_METACLASS_$_HAPWebRTCReofferResponse
+ _OBJC_METACLASS_$_HAPWebRTCSFrameConfiguration
+ _OBJC_METACLASS_$_HAPWebRTCSolicitOfferRequest
+ _OBJC_METACLASS_$_HAPWebRTCSolicitOfferResponse
+ _OBJC_METACLASS_$_HAPWebRTCStreamingControlRequest
+ _OBJC_METACLASS_$_HAPWebRTCStreamingControlResponse
+ _OBJC_METACLASS_$_HAPWebRTCStreamingControlStatusWrapper
+ _OBJC_METACLASS_$_HAPWebRTCStreamingStatusWrapper
+ _OBJC_METACLASS_$_HAPZoneDataV2
+ _WiFiScan_b
+ __CopyPairingIdentityDelegateCallback_f.17255
+ __CopyPairingIdentityDelegateCallback_f.24228
+ __CopyPairingIdentityDelegateCallback_f.3021
+ __FindPairedPeerDelegateCallback_f.3020
+ __OBJC_$_CLASS_METHODS_HAP2ThreadNetworkUtil
+ __OBJC_$_CLASS_METHODS_HAPAudioCodecBitDepthWrapper
+ __OBJC_$_CLASS_METHODS_HAPAudioStreamTier
+ __OBJC_$_CLASS_METHODS_HAPCameraBufferEvent
+ __OBJC_$_CLASS_METHODS_HAPCameraBufferEventCMAFSessionStart
+ __OBJC_$_CLASS_METHODS_HAPCameraBufferEventCMAFSessionStop
+ __OBJC_$_CLASS_METHODS_HAPCameraBufferEventCommandRequest
+ __OBJC_$_CLASS_METHODS_HAPCameraBufferEventCommandResponse
+ __OBJC_$_CLASS_METHODS_HAPCameraBufferEventCommandTypeWrapper
+ __OBJC_$_CLASS_METHODS_HAPCameraBufferEventMotion
+ __OBJC_$_CLASS_METHODS_HAPCameraBufferEventTypeWrapper
+ __OBJC_$_CLASS_METHODS_HAPCameraBufferInfo
+ __OBJC_$_CLASS_METHODS_HAPCameraBufferInfoResponse
+ __OBJC_$_CLASS_METHODS_HAPCameraBufferInterval
+ __OBJC_$_CLASS_METHODS_HAPCameraBufferTypeWrapper
+ __OBJC_$_CLASS_METHODS_HAPCameraBufferUploadCommandRequest
+ __OBJC_$_CLASS_METHODS_HAPCameraBufferUploadCommandResponse
+ __OBJC_$_CLASS_METHODS_HAPCameraBufferUploadCommandTypeWrapper
+ __OBJC_$_CLASS_METHODS_HAPCameraBufferUploadStopActionWrapper
+ __OBJC_$_CLASS_METHODS_HAPCameraCapabilitiesResponse
+ __OBJC_$_CLASS_METHODS_HAPCameraClientCSR
+ __OBJC_$_CLASS_METHODS_HAPCameraClientCertificate
+ __OBJC_$_CLASS_METHODS_HAPCameraClientCertificateStatus
+ __OBJC_$_CLASS_METHODS_HAPCameraKey
+ __OBJC_$_CLASS_METHODS_HAPCameraKeyID
+ __OBJC_$_CLASS_METHODS_HAPCameraRecordingPublishingPoint
+ __OBJC_$_CLASS_METHODS_HAPCameraSensors
+ __OBJC_$_CLASS_METHODS_HAPCameraVideoQualityWrapper
+ __OBJC_$_CLASS_METHODS_HAPCameraVideoStreamCapabilities
+ __OBJC_$_CLASS_METHODS_HAPCameraZones
+ __OBJC_$_CLASS_METHODS_HAPPolygon
+ __OBJC_$_CLASS_METHODS_HAPRTPStreamingControlCommandWrapper
+ __OBJC_$_CLASS_METHODS_HAPRTPStreamingControlRequest
+ __OBJC_$_CLASS_METHODS_HAPRTPStreamingControlResponse
+ __OBJC_$_CLASS_METHODS_HAPRTPStreamingControlStatusWrapper
+ __OBJC_$_CLASS_METHODS_HAPSensorConfiguration
+ __OBJC_$_CLASS_METHODS_HAPSensorDimensions
+ __OBJC_$_CLASS_METHODS_HAPSupportedAudioStreamTiers
+ __OBJC_$_CLASS_METHODS_HAPSupportedVideoStreamTiers
+ __OBJC_$_CLASS_METHODS_HAPVideoCodecTypeWrapper
+ __OBJC_$_CLASS_METHODS_HAPVideoStreamTier
+ __OBJC_$_CLASS_METHODS_HAPWebRTCICECandidate
+ __OBJC_$_CLASS_METHODS_HAPWebRTCOfferStatusWrapper
+ __OBJC_$_CLASS_METHODS_HAPWebRTCProvideAnswerRequest
+ __OBJC_$_CLASS_METHODS_HAPWebRTCReofferRequest
+ __OBJC_$_CLASS_METHODS_HAPWebRTCReofferResponse
+ __OBJC_$_CLASS_METHODS_HAPWebRTCSFrameConfiguration
+ __OBJC_$_CLASS_METHODS_HAPWebRTCSolicitOfferRequest
+ __OBJC_$_CLASS_METHODS_HAPWebRTCSolicitOfferResponse
+ __OBJC_$_CLASS_METHODS_HAPWebRTCStreamingControlRequest
+ __OBJC_$_CLASS_METHODS_HAPWebRTCStreamingControlResponse
+ __OBJC_$_CLASS_METHODS_HAPWebRTCStreamingControlStatusWrapper
+ __OBJC_$_CLASS_METHODS_HAPWebRTCStreamingStatusWrapper
+ __OBJC_$_CLASS_METHODS_HAPZoneDataV2
+ __OBJC_$_CLASS_PROP_LIST_HAPSystemKeychainStore
+ __OBJC_$_INSTANCE_METHODS_HAPAudioCodecBitDepthWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPAudioStreamTier
+ __OBJC_$_INSTANCE_METHODS_HAPCameraBufferEvent
+ __OBJC_$_INSTANCE_METHODS_HAPCameraBufferEventCMAFSessionStart
+ __OBJC_$_INSTANCE_METHODS_HAPCameraBufferEventCMAFSessionStop
+ __OBJC_$_INSTANCE_METHODS_HAPCameraBufferEventCommandRequest
+ __OBJC_$_INSTANCE_METHODS_HAPCameraBufferEventCommandResponse
+ __OBJC_$_INSTANCE_METHODS_HAPCameraBufferEventCommandTypeWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPCameraBufferEventMotion
+ __OBJC_$_INSTANCE_METHODS_HAPCameraBufferEventTypeWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPCameraBufferInfo
+ __OBJC_$_INSTANCE_METHODS_HAPCameraBufferInfoResponse
+ __OBJC_$_INSTANCE_METHODS_HAPCameraBufferInterval
+ __OBJC_$_INSTANCE_METHODS_HAPCameraBufferTypeWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPCameraBufferUploadCommandRequest
+ __OBJC_$_INSTANCE_METHODS_HAPCameraBufferUploadCommandResponse
+ __OBJC_$_INSTANCE_METHODS_HAPCameraBufferUploadCommandTypeWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPCameraBufferUploadStopActionWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPCameraCapabilitiesResponse
+ __OBJC_$_INSTANCE_METHODS_HAPCameraClientCSR
+ __OBJC_$_INSTANCE_METHODS_HAPCameraClientCertificate
+ __OBJC_$_INSTANCE_METHODS_HAPCameraClientCertificateStatus
+ __OBJC_$_INSTANCE_METHODS_HAPCameraKey
+ __OBJC_$_INSTANCE_METHODS_HAPCameraKeyID
+ __OBJC_$_INSTANCE_METHODS_HAPCameraRecordingPublishingPoint
+ __OBJC_$_INSTANCE_METHODS_HAPCameraSensors
+ __OBJC_$_INSTANCE_METHODS_HAPCameraVideoQualityWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPCameraVideoStreamCapabilities
+ __OBJC_$_INSTANCE_METHODS_HAPCameraZones
+ __OBJC_$_INSTANCE_METHODS_HAPPolygon
+ __OBJC_$_INSTANCE_METHODS_HAPRTPStreamingControlCommandWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPRTPStreamingControlRequest
+ __OBJC_$_INSTANCE_METHODS_HAPRTPStreamingControlResponse
+ __OBJC_$_INSTANCE_METHODS_HAPRTPStreamingControlStatusWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPSensorConfiguration
+ __OBJC_$_INSTANCE_METHODS_HAPSensorDimensions
+ __OBJC_$_INSTANCE_METHODS_HAPSupportedAudioStreamTiers
+ __OBJC_$_INSTANCE_METHODS_HAPSupportedVideoStreamTiers
+ __OBJC_$_INSTANCE_METHODS_HAPSystemKeychainStoreDefaultDataSource
+ __OBJC_$_INSTANCE_METHODS_HAPVideoCodecTypeWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPVideoStreamTier
+ __OBJC_$_INSTANCE_METHODS_HAPWebRTCICECandidate
+ __OBJC_$_INSTANCE_METHODS_HAPWebRTCOfferStatusWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPWebRTCProvideAnswerRequest
+ __OBJC_$_INSTANCE_METHODS_HAPWebRTCReofferRequest
+ __OBJC_$_INSTANCE_METHODS_HAPWebRTCReofferResponse
+ __OBJC_$_INSTANCE_METHODS_HAPWebRTCSFrameConfiguration
+ __OBJC_$_INSTANCE_METHODS_HAPWebRTCSolicitOfferRequest
+ __OBJC_$_INSTANCE_METHODS_HAPWebRTCSolicitOfferResponse
+ __OBJC_$_INSTANCE_METHODS_HAPWebRTCStreamingControlRequest
+ __OBJC_$_INSTANCE_METHODS_HAPWebRTCStreamingControlResponse
+ __OBJC_$_INSTANCE_METHODS_HAPWebRTCStreamingControlStatusWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPWebRTCStreamingStatusWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPZoneDataV2
+ __OBJC_$_INSTANCE_VARIABLES_HAPAudioCodecBitDepthWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPAudioStreamTier
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraBufferEvent
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraBufferEventCMAFSessionStart
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraBufferEventCMAFSessionStop
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraBufferEventCommandRequest
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraBufferEventCommandResponse
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraBufferEventCommandTypeWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraBufferEventMotion
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraBufferEventTypeWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraBufferInfo
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraBufferInfoResponse
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraBufferInterval
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraBufferTypeWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraBufferUploadCommandRequest
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraBufferUploadCommandResponse
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraBufferUploadCommandTypeWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraBufferUploadStopActionWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraCapabilitiesResponse
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraClientCSR
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraClientCertificate
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraClientCertificateStatus
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraKey
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraKeyID
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraRecordingPublishingPoint
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraSensors
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraVideoQualityWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraVideoStreamCapabilities
+ __OBJC_$_INSTANCE_VARIABLES_HAPCameraZones
+ __OBJC_$_INSTANCE_VARIABLES_HAPPolygon
+ __OBJC_$_INSTANCE_VARIABLES_HAPRTPStreamingControlCommandWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPRTPStreamingControlRequest
+ __OBJC_$_INSTANCE_VARIABLES_HAPRTPStreamingControlResponse
+ __OBJC_$_INSTANCE_VARIABLES_HAPRTPStreamingControlStatusWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPSensorConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_HAPSensorDimensions
+ __OBJC_$_INSTANCE_VARIABLES_HAPSupportedAudioStreamTiers
+ __OBJC_$_INSTANCE_VARIABLES_HAPSupportedVideoStreamTiers
+ __OBJC_$_INSTANCE_VARIABLES_HAPVideoCodecTypeWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPVideoStreamTier
+ __OBJC_$_INSTANCE_VARIABLES_HAPWebRTCICECandidate
+ __OBJC_$_INSTANCE_VARIABLES_HAPWebRTCOfferStatusWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPWebRTCProvideAnswerRequest
+ __OBJC_$_INSTANCE_VARIABLES_HAPWebRTCReofferRequest
+ __OBJC_$_INSTANCE_VARIABLES_HAPWebRTCReofferResponse
+ __OBJC_$_INSTANCE_VARIABLES_HAPWebRTCSFrameConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_HAPWebRTCSolicitOfferRequest
+ __OBJC_$_INSTANCE_VARIABLES_HAPWebRTCSolicitOfferResponse
+ __OBJC_$_INSTANCE_VARIABLES_HAPWebRTCStreamingControlRequest
+ __OBJC_$_INSTANCE_VARIABLES_HAPWebRTCStreamingControlResponse
+ __OBJC_$_INSTANCE_VARIABLES_HAPWebRTCStreamingControlStatusWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPWebRTCStreamingStatusWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPZoneDataV2
+ __OBJC_$_PROP_LIST_HAP2Accessory.303
+ __OBJC_$_PROP_LIST_HAP2AccessoryServerBrowser.423
+ __OBJC_$_PROP_LIST_HAP2AccessoryServerCoordinator.186
+ __OBJC_$_PROP_LIST_HAP2AccessoryServerDelegate
+ __OBJC_$_PROP_LIST_HAP2AccessoryServerPairingDriver.289
+ __OBJC_$_PROP_LIST_HAPAudioCodecBitDepthWrapper
+ __OBJC_$_PROP_LIST_HAPAudioStreamTier
+ __OBJC_$_PROP_LIST_HAPCameraBufferEvent
+ __OBJC_$_PROP_LIST_HAPCameraBufferEventCMAFSessionStart
+ __OBJC_$_PROP_LIST_HAPCameraBufferEventCMAFSessionStop
+ __OBJC_$_PROP_LIST_HAPCameraBufferEventCommandRequest
+ __OBJC_$_PROP_LIST_HAPCameraBufferEventCommandResponse
+ __OBJC_$_PROP_LIST_HAPCameraBufferEventCommandTypeWrapper
+ __OBJC_$_PROP_LIST_HAPCameraBufferEventMotion
+ __OBJC_$_PROP_LIST_HAPCameraBufferEventTypeWrapper
+ __OBJC_$_PROP_LIST_HAPCameraBufferInfo
+ __OBJC_$_PROP_LIST_HAPCameraBufferInfoResponse
+ __OBJC_$_PROP_LIST_HAPCameraBufferInterval
+ __OBJC_$_PROP_LIST_HAPCameraBufferTypeWrapper
+ __OBJC_$_PROP_LIST_HAPCameraBufferUploadCommandRequest
+ __OBJC_$_PROP_LIST_HAPCameraBufferUploadCommandResponse
+ __OBJC_$_PROP_LIST_HAPCameraBufferUploadCommandTypeWrapper
+ __OBJC_$_PROP_LIST_HAPCameraBufferUploadStopActionWrapper
+ __OBJC_$_PROP_LIST_HAPCameraCapabilitiesResponse
+ __OBJC_$_PROP_LIST_HAPCameraClientCSR
+ __OBJC_$_PROP_LIST_HAPCameraClientCertificate
+ __OBJC_$_PROP_LIST_HAPCameraClientCertificateStatus
+ __OBJC_$_PROP_LIST_HAPCameraKey
+ __OBJC_$_PROP_LIST_HAPCameraKeyID
+ __OBJC_$_PROP_LIST_HAPCameraRecordingPublishingPoint
+ __OBJC_$_PROP_LIST_HAPCameraSensors
+ __OBJC_$_PROP_LIST_HAPCameraVideoQualityWrapper
+ __OBJC_$_PROP_LIST_HAPCameraVideoStreamCapabilities
+ __OBJC_$_PROP_LIST_HAPCameraZones
+ __OBJC_$_PROP_LIST_HAPPolygon
+ __OBJC_$_PROP_LIST_HAPRTPStreamingControlCommandWrapper
+ __OBJC_$_PROP_LIST_HAPRTPStreamingControlRequest
+ __OBJC_$_PROP_LIST_HAPRTPStreamingControlResponse
+ __OBJC_$_PROP_LIST_HAPRTPStreamingControlStatusWrapper
+ __OBJC_$_PROP_LIST_HAPSensorConfiguration
+ __OBJC_$_PROP_LIST_HAPSensorDimensions
+ __OBJC_$_PROP_LIST_HAPSupportedAudioStreamTiers
+ __OBJC_$_PROP_LIST_HAPSupportedVideoStreamTiers
+ __OBJC_$_PROP_LIST_HAPSystemKeychainStoreDataSource
+ __OBJC_$_PROP_LIST_HAPSystemKeychainStoreDefaultDataSource
+ __OBJC_$_PROP_LIST_HAPVideoCodecTypeWrapper
+ __OBJC_$_PROP_LIST_HAPVideoStreamTier
+ __OBJC_$_PROP_LIST_HAPWebRTCICECandidate
+ __OBJC_$_PROP_LIST_HAPWebRTCOfferStatusWrapper
+ __OBJC_$_PROP_LIST_HAPWebRTCProvideAnswerRequest
+ __OBJC_$_PROP_LIST_HAPWebRTCReofferRequest
+ __OBJC_$_PROP_LIST_HAPWebRTCReofferResponse
+ __OBJC_$_PROP_LIST_HAPWebRTCSFrameConfiguration
+ __OBJC_$_PROP_LIST_HAPWebRTCSolicitOfferRequest
+ __OBJC_$_PROP_LIST_HAPWebRTCSolicitOfferResponse
+ __OBJC_$_PROP_LIST_HAPWebRTCStreamingControlRequest
+ __OBJC_$_PROP_LIST_HAPWebRTCStreamingControlResponse
+ __OBJC_$_PROP_LIST_HAPWebRTCStreamingControlStatusWrapper
+ __OBJC_$_PROP_LIST_HAPWebRTCStreamingStatusWrapper
+ __OBJC_$_PROP_LIST_HAPZoneDataV2
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HAPSystemKeychainStoreDataSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HAPSystemKeychainStoreDataSource
+ __OBJC_$_PROTOCOL_REFS_HAPSystemKeychainStoreDataSource
+ __OBJC_CLASS_PROTOCOLS_$_HAPAudioCodecBitDepthWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPAudioStreamTier
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraBufferEvent
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraBufferEventCMAFSessionStart
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraBufferEventCMAFSessionStop
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraBufferEventCommandRequest
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraBufferEventCommandResponse
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraBufferEventCommandTypeWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraBufferEventMotion
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraBufferEventTypeWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraBufferInfo
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraBufferInfoResponse
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraBufferInterval
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraBufferTypeWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraBufferUploadCommandRequest
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraBufferUploadCommandResponse
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraBufferUploadCommandTypeWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraBufferUploadStopActionWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraCapabilitiesResponse
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraClientCSR
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraClientCertificate
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraClientCertificateStatus
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraKey
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraKeyID
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraRecordingPublishingPoint
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraSensors
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraVideoQualityWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraVideoStreamCapabilities
+ __OBJC_CLASS_PROTOCOLS_$_HAPCameraZones
+ __OBJC_CLASS_PROTOCOLS_$_HAPPolygon
+ __OBJC_CLASS_PROTOCOLS_$_HAPRTPStreamingControlCommandWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPRTPStreamingControlRequest
+ __OBJC_CLASS_PROTOCOLS_$_HAPRTPStreamingControlResponse
+ __OBJC_CLASS_PROTOCOLS_$_HAPRTPStreamingControlStatusWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPSensorConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_HAPSensorDimensions
+ __OBJC_CLASS_PROTOCOLS_$_HAPSupportedAudioStreamTiers
+ __OBJC_CLASS_PROTOCOLS_$_HAPSupportedVideoStreamTiers
+ __OBJC_CLASS_PROTOCOLS_$_HAPSystemKeychainStoreDefaultDataSource
+ __OBJC_CLASS_PROTOCOLS_$_HAPVideoCodecTypeWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPVideoStreamTier
+ __OBJC_CLASS_PROTOCOLS_$_HAPWebRTCICECandidate
+ __OBJC_CLASS_PROTOCOLS_$_HAPWebRTCOfferStatusWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPWebRTCProvideAnswerRequest
+ __OBJC_CLASS_PROTOCOLS_$_HAPWebRTCReofferRequest
+ __OBJC_CLASS_PROTOCOLS_$_HAPWebRTCReofferResponse
+ __OBJC_CLASS_PROTOCOLS_$_HAPWebRTCSFrameConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_HAPWebRTCSolicitOfferRequest
+ __OBJC_CLASS_PROTOCOLS_$_HAPWebRTCSolicitOfferResponse
+ __OBJC_CLASS_PROTOCOLS_$_HAPWebRTCStreamingControlRequest
+ __OBJC_CLASS_PROTOCOLS_$_HAPWebRTCStreamingControlResponse
+ __OBJC_CLASS_PROTOCOLS_$_HAPWebRTCStreamingControlStatusWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPWebRTCStreamingStatusWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPZoneDataV2
+ __OBJC_CLASS_RO_$_HAP2ThreadNetworkUtil
+ __OBJC_CLASS_RO_$_HAPAudioCodecBitDepthWrapper
+ __OBJC_CLASS_RO_$_HAPAudioStreamTier
+ __OBJC_CLASS_RO_$_HAPCameraBufferEvent
+ __OBJC_CLASS_RO_$_HAPCameraBufferEventCMAFSessionStart
+ __OBJC_CLASS_RO_$_HAPCameraBufferEventCMAFSessionStop
+ __OBJC_CLASS_RO_$_HAPCameraBufferEventCommandRequest
+ __OBJC_CLASS_RO_$_HAPCameraBufferEventCommandResponse
+ __OBJC_CLASS_RO_$_HAPCameraBufferEventCommandTypeWrapper
+ __OBJC_CLASS_RO_$_HAPCameraBufferEventMotion
+ __OBJC_CLASS_RO_$_HAPCameraBufferEventTypeWrapper
+ __OBJC_CLASS_RO_$_HAPCameraBufferInfo
+ __OBJC_CLASS_RO_$_HAPCameraBufferInfoResponse
+ __OBJC_CLASS_RO_$_HAPCameraBufferInterval
+ __OBJC_CLASS_RO_$_HAPCameraBufferTypeWrapper
+ __OBJC_CLASS_RO_$_HAPCameraBufferUploadCommandRequest
+ __OBJC_CLASS_RO_$_HAPCameraBufferUploadCommandResponse
+ __OBJC_CLASS_RO_$_HAPCameraBufferUploadCommandTypeWrapper
+ __OBJC_CLASS_RO_$_HAPCameraBufferUploadStopActionWrapper
+ __OBJC_CLASS_RO_$_HAPCameraCapabilitiesResponse
+ __OBJC_CLASS_RO_$_HAPCameraClientCSR
+ __OBJC_CLASS_RO_$_HAPCameraClientCertificate
+ __OBJC_CLASS_RO_$_HAPCameraClientCertificateStatus
+ __OBJC_CLASS_RO_$_HAPCameraKey
+ __OBJC_CLASS_RO_$_HAPCameraKeyID
+ __OBJC_CLASS_RO_$_HAPCameraRecordingPublishingPoint
+ __OBJC_CLASS_RO_$_HAPCameraSensors
+ __OBJC_CLASS_RO_$_HAPCameraVideoQualityWrapper
+ __OBJC_CLASS_RO_$_HAPCameraVideoStreamCapabilities
+ __OBJC_CLASS_RO_$_HAPCameraZones
+ __OBJC_CLASS_RO_$_HAPPolygon
+ __OBJC_CLASS_RO_$_HAPRTPStreamingControlCommandWrapper
+ __OBJC_CLASS_RO_$_HAPRTPStreamingControlRequest
+ __OBJC_CLASS_RO_$_HAPRTPStreamingControlResponse
+ __OBJC_CLASS_RO_$_HAPRTPStreamingControlStatusWrapper
+ __OBJC_CLASS_RO_$_HAPSensorConfiguration
+ __OBJC_CLASS_RO_$_HAPSensorDimensions
+ __OBJC_CLASS_RO_$_HAPSupportedAudioStreamTiers
+ __OBJC_CLASS_RO_$_HAPSupportedVideoStreamTiers
+ __OBJC_CLASS_RO_$_HAPSystemKeychainStoreDefaultDataSource
+ __OBJC_CLASS_RO_$_HAPVideoCodecTypeWrapper
+ __OBJC_CLASS_RO_$_HAPVideoStreamTier
+ __OBJC_CLASS_RO_$_HAPWebRTCICECandidate
+ __OBJC_CLASS_RO_$_HAPWebRTCOfferStatusWrapper
+ __OBJC_CLASS_RO_$_HAPWebRTCProvideAnswerRequest
+ __OBJC_CLASS_RO_$_HAPWebRTCReofferRequest
+ __OBJC_CLASS_RO_$_HAPWebRTCReofferResponse
+ __OBJC_CLASS_RO_$_HAPWebRTCSFrameConfiguration
+ __OBJC_CLASS_RO_$_HAPWebRTCSolicitOfferRequest
+ __OBJC_CLASS_RO_$_HAPWebRTCSolicitOfferResponse
+ __OBJC_CLASS_RO_$_HAPWebRTCStreamingControlRequest
+ __OBJC_CLASS_RO_$_HAPWebRTCStreamingControlResponse
+ __OBJC_CLASS_RO_$_HAPWebRTCStreamingControlStatusWrapper
+ __OBJC_CLASS_RO_$_HAPWebRTCStreamingStatusWrapper
+ __OBJC_CLASS_RO_$_HAPZoneDataV2
+ __OBJC_LABEL_PROTOCOL_$_HAPSystemKeychainStoreDataSource
+ __OBJC_METACLASS_RO_$_HAP2ThreadNetworkUtil
+ __OBJC_METACLASS_RO_$_HAPAudioCodecBitDepthWrapper
+ __OBJC_METACLASS_RO_$_HAPAudioStreamTier
+ __OBJC_METACLASS_RO_$_HAPCameraBufferEvent
+ __OBJC_METACLASS_RO_$_HAPCameraBufferEventCMAFSessionStart
+ __OBJC_METACLASS_RO_$_HAPCameraBufferEventCMAFSessionStop
+ __OBJC_METACLASS_RO_$_HAPCameraBufferEventCommandRequest
+ __OBJC_METACLASS_RO_$_HAPCameraBufferEventCommandResponse
+ __OBJC_METACLASS_RO_$_HAPCameraBufferEventCommandTypeWrapper
+ __OBJC_METACLASS_RO_$_HAPCameraBufferEventMotion
+ __OBJC_METACLASS_RO_$_HAPCameraBufferEventTypeWrapper
+ __OBJC_METACLASS_RO_$_HAPCameraBufferInfo
+ __OBJC_METACLASS_RO_$_HAPCameraBufferInfoResponse
+ __OBJC_METACLASS_RO_$_HAPCameraBufferInterval
+ __OBJC_METACLASS_RO_$_HAPCameraBufferTypeWrapper
+ __OBJC_METACLASS_RO_$_HAPCameraBufferUploadCommandRequest
+ __OBJC_METACLASS_RO_$_HAPCameraBufferUploadCommandResponse
+ __OBJC_METACLASS_RO_$_HAPCameraBufferUploadCommandTypeWrapper
+ __OBJC_METACLASS_RO_$_HAPCameraBufferUploadStopActionWrapper
+ __OBJC_METACLASS_RO_$_HAPCameraCapabilitiesResponse
+ __OBJC_METACLASS_RO_$_HAPCameraClientCSR
+ __OBJC_METACLASS_RO_$_HAPCameraClientCertificate
+ __OBJC_METACLASS_RO_$_HAPCameraClientCertificateStatus
+ __OBJC_METACLASS_RO_$_HAPCameraKey
+ __OBJC_METACLASS_RO_$_HAPCameraKeyID
+ __OBJC_METACLASS_RO_$_HAPCameraRecordingPublishingPoint
+ __OBJC_METACLASS_RO_$_HAPCameraSensors
+ __OBJC_METACLASS_RO_$_HAPCameraVideoQualityWrapper
+ __OBJC_METACLASS_RO_$_HAPCameraVideoStreamCapabilities
+ __OBJC_METACLASS_RO_$_HAPCameraZones
+ __OBJC_METACLASS_RO_$_HAPPolygon
+ __OBJC_METACLASS_RO_$_HAPRTPStreamingControlCommandWrapper
+ __OBJC_METACLASS_RO_$_HAPRTPStreamingControlRequest
+ __OBJC_METACLASS_RO_$_HAPRTPStreamingControlResponse
+ __OBJC_METACLASS_RO_$_HAPRTPStreamingControlStatusWrapper
+ __OBJC_METACLASS_RO_$_HAPSensorConfiguration
+ __OBJC_METACLASS_RO_$_HAPSensorDimensions
+ __OBJC_METACLASS_RO_$_HAPSupportedAudioStreamTiers
+ __OBJC_METACLASS_RO_$_HAPSupportedVideoStreamTiers
+ __OBJC_METACLASS_RO_$_HAPSystemKeychainStoreDefaultDataSource
+ __OBJC_METACLASS_RO_$_HAPVideoCodecTypeWrapper
+ __OBJC_METACLASS_RO_$_HAPVideoStreamTier
+ __OBJC_METACLASS_RO_$_HAPWebRTCICECandidate
+ __OBJC_METACLASS_RO_$_HAPWebRTCOfferStatusWrapper
+ __OBJC_METACLASS_RO_$_HAPWebRTCProvideAnswerRequest
+ __OBJC_METACLASS_RO_$_HAPWebRTCReofferRequest
+ __OBJC_METACLASS_RO_$_HAPWebRTCReofferResponse
+ __OBJC_METACLASS_RO_$_HAPWebRTCSFrameConfiguration
+ __OBJC_METACLASS_RO_$_HAPWebRTCSolicitOfferRequest
+ __OBJC_METACLASS_RO_$_HAPWebRTCSolicitOfferResponse
+ __OBJC_METACLASS_RO_$_HAPWebRTCStreamingControlRequest
+ __OBJC_METACLASS_RO_$_HAPWebRTCStreamingControlResponse
+ __OBJC_METACLASS_RO_$_HAPWebRTCStreamingControlStatusWrapper
+ __OBJC_METACLASS_RO_$_HAPWebRTCStreamingStatusWrapper
+ __OBJC_METACLASS_RO_$_HAPZoneDataV2
+ __OBJC_PROTOCOL_$_HAPSystemKeychainStoreDataSource
+ __OBJC_PROTOCOL_REFERENCE_$_HAP2UnpairedAccessoryServer
+ __PairSetupPromptForSetupCodeDelegateCallback_f.24230
+ __SavePairedPeerDelegateCallback_f.17247
+ __SavePairedPeerDelegateCallback_f.24224
+ ___103-[_HAPAccessoryServerBTLE100 _handlePairingsReadForCharacteristic:readError:removing:queue:completion:]_block_invoke.334
+ ___106-[_HAPAccessoryServerBTLE200 removePairingForCurrentControllerOnQueue:completion:serverPairingCompletion:]_block_invoke.732
+ ___106-[_HAPAccessoryServerBTLE200 removePairingForCurrentControllerOnQueue:completion:serverPairingCompletion:]_block_invoke.733
+ ___108-[HAP2AccessoryServerController _removePairingCompletionWithIdentity:cleanupLocalData:operation:completion:]_block_invoke.296
+ ___108-[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:expiry:queue:completionHandler:]_block_invoke.246
+ ___108-[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:expiry:queue:completionHandler:]_block_invoke.247
+ ___112-[HAPWACAccessoryClient _performEasyConfigWithPairingPrompt:performPairSetup:isSplit:pairingRequest:completion:]_block_invoke.106
+ ___112-[HAPWACAccessoryClient _performEasyConfigWithPairingPrompt:performPairSetup:isSplit:pairingRequest:completion:]_block_invoke.120
+ ___112-[HAPWACAccessoryClient _performEasyConfigWithPairingPrompt:performPairSetup:isSplit:pairingRequest:completion:]_block_invoke.125
+ ___112-[HAPWACAccessoryClient _performEasyConfigWithPairingPrompt:performPairSetup:isSplit:pairingRequest:completion:]_block_invoke.97
+ ___112-[HAPWACAccessoryClient _performEasyConfigWithPairingPrompt:performPairSetup:isSplit:pairingRequest:completion:]_block_invoke.99
+ ___112-[HAPWACAccessoryClient _performEasyConfigWithPairingPrompt:performPairSetup:isSplit:pairingRequest:completion:]_block_invoke_2.107
+ ___115-[HAPAccessoryServerIP _handleWriteECONNResetError:writeRequests:responses:timeout:expiry:queue:completionHandler:]_block_invoke.228
+ ___120-[HAPAccessoryServerIP _handleReadECONNRESETError:readCharacteristics:responses:timeout:expiry:queue:completionHandler:]_block_invoke.184
+ ___41-[HAPAccessoryServerIP getAccessoryInfo:]_block_invoke.478
+ ___44-[HAPAccessoryServerIP _pairVerifyStartWAC:]_block_invoke.104
+ ___45-[HAP2AccessoryServerController closeSession]_block_invoke.312
+ ___45-[HAP2AccessoryServerController closeSession]_block_invoke.316
+ ___45-[HAPAccessoryServerIP _pairSetupContinueWAC]_block_invoke.102
+ ___45-[HAPAccessoryServerIP stopPairingWithError:]_block_invoke.145
+ ___45-[_HAPAccessoryServerBTLE100 _pairSetupStart]_block_invoke.319
+ ___47-[HAPAccessoryServerIP identifyWithCompletion:]_block_invoke.595
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.105
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.106
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.108
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.109
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.111
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke_2.107
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke_2.110
+ ___48-[HAPAccessoryServerIP startPairingWithRequest:]_block_invoke.143
+ ___48-[HAPAccessoryServerIP startPairingWithRequest:]_block_invoke_4
+ ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.112
+ ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.117
+ ___49-[HAPAccessoryServerIP authSession:authComplete:]_block_invoke.521
+ ___49-[HAPWACAccessoryClient _joinCompleteWithStatus:]_block_invoke.65
+ ___50-[HAP2AccessoryServer(Paired) _updateAccessories:]_block_invoke
+ ___50-[HAPAccessoryServerIP networkMonitorIsReachable:]_block_invoke.473
+ ___50-[_HAPAccessoryServerBTLE200 _checkForAuthPrompt:]_block_invoke.632
+ ___50-[_HAPAccessoryServerBTLE200 _checkForAuthPrompt:]_block_invoke.639
+ ___50-[_HAPAccessoryServerBTLE200 _checkForAuthPrompt:]_block_invoke.643
+ ___50-[_HAPAccessoryServerBTLE200 isReadyForOperation:]_block_invoke.833
+ ___52-[HAP2AccessoryServer(Paired) unpairWithCompletion:]_block_invoke.66
+ ___52-[HAP2AccessoryServer(Paired) unpairWithCompletion:]_block_invoke.67
+ ___53-[HAPAccessoryServerHAP2Adapter _printMissingValues:]_block_invoke.251
+ ___53-[HAPAccessoryServerHAP2Adapter _printMissingValues:]_block_invoke.259
+ ___53-[HAPAccessoryServerIP setPairVerifyCompletionBlock:]_block_invoke.377
+ ___53-[_HAPAccessoryServerBTLE200 identifyWithCompletion:]_block_invoke.760
+ ___53-[_HAPAccessoryServerBTLE200 identifyWithCompletion:]_block_invoke.767
+ ___54-[HAP2AccessoryServer(Paired) _getSleepIntervalValue:]_block_invoke.238
+ ___54-[HAPWACAccessoryClient restoreNetworkWithCompletion:]_block_invoke.90
+ ___54-[HAPWACAccessoryClient restoreNetworkWithCompletion:]_block_invoke_2.91
+ ___54-[_HAPAccessoryServerBTLE200 startPairingWithRequest:]_block_invoke.621
+ ___55+[HAPSystemKeychainStore _systemKeychainStoreSingleton]_block_invoke
+ ___55-[HAP2AccessoryServerController addPairing:completion:]_block_invoke.300
+ ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.511
+ ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.516
+ ___55-[_HAPAccessoryServerBTLE200 authSession:authComplete:]_block_invoke.993
+ ___56-[HAP2AccessoryServer(Paired) removePairing:completion:]_block_invoke.71
+ ___56-[HAP2AccessoryServer(Paired) removePairing:completion:]_block_invoke.72
+ ___56-[HAP2AccessoryServerController _scheduleRestartSession]_block_invoke.388
+ ___56-[HAPSystemKeychainStore hh2KeychainItemWithIdentifier:]_block_invoke
+ ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke.505
+ ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke_2.509
+ ___59-[HAP2AccessoryServer(Paired) updateAccessoriesWithReason:]_block_invoke.82
+ ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke.436
+ ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke_2.437
+ ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.414
+ ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.419
+ ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.420
+ ___59-[_HAPAccessoryServerBTLE200 peripheral:didModifyServices:]_block_invoke.958
+ ___60-[HAPAccessoryServerIP _validatePairingAuthMethod:activity:]_block_invoke.489
+ ___60-[HAPWACAccessoryClient joinAccessoryNetworkWithCompletion:]_block_invoke.78
+ ___60-[HAPWACAccessoryClient joinAccessoryNetworkWithCompletion:]_block_invoke.79
+ ___60-[_HAPAccessoryServerBTLE200 continuePairingAfterAuthPrompt]_block_invoke.662
+ ___62-[HAP2AccessoryServer(Paired) _updateAccessoriesWithActivity:]_block_invoke
+ ___62-[HAP2AccessoryServer(Paired) _updateAccessoriesWithActivity:]_block_invoke_2
+ ___62-[HAPWACAccessoryBrowser refreshScanResultForSSID:completion:]_block_invoke
+ ___63-[HAPAccessoryServerBrowserIP startDiscoveringAccessoryServers]_block_invoke.45
+ ___63-[HAPWACAccessoryBrowser _refreshScanResultForSSID:completion:]_block_invoke
+ ___63-[_HAPAccessoryServerBTLE100 _handlePairSetupExchangeWithData:]_block_invoke.320
+ ___63-[_HAPAccessoryServerBTLE200 authSession:sendAuthExchangeData:]_block_invoke.986
+ ___63-[_HAPAccessoryServerBTLE200 authSession:sendAuthExchangeData:]_block_invoke_2.989
+ ___64-[HAP2AccessoryServer _directlyUpdateConnectionState:withError:]_block_invoke
+ ___64-[HAP2AccessoryServer(Paired) _pollAccessoryOnQueueWithOptions:]_block_invoke.250
+ ___64-[HAP2AccessoryServer(Paired) _pollAccessoryOnQueueWithOptions:]_block_invoke.251
+ ___64-[HAP2AccessoryServer(Paired) _pollAccessoryOnQueueWithOptions:]_block_invoke_2.252
+ ___64-[HAP2AccessoryServerController unpairedIdentifyWithCompletion:]_block_invoke.310
+ ___64-[_HAPAccessoryServerBTLE200 securitySession:didCloseWithError:]_block_invoke.1011
+ ___65-[HAP2AccessoryServer(Unpaired) _handleUpdatedRemovedAccessories]_block_invoke
+ ___65-[HAPAccessoryServerBrowserIP wacBrowser:didFindHAPWACAccessory:]_block_invoke.72
+ ___65-[HAPAccessoryServerIP _continuePairingAfterAuthPromptWithRetry:]_block_invoke.428
+ ___65-[HAPAccessoryServerIP _httpClientDidCloseConnectionDueToServer:]_block_invoke.382
+ ___66-[HAPSystemKeychainStore _allAccessoryPairingKeysIncludingHH2Key:]_block_invoke.389
+ ___66-[_HAPAccessoryServerBTLE200 _handlePairSetupSessionExchangeData:]_block_invoke.677
+ ___67-[HAP2AccessoryServerCoordinator _didDiscoverAccessory:completion:]_block_invoke.16
+ ___67-[HAPAccessoryServerBrowserIP wacBrowser:didRemoveHAPWACAccessory:]_block_invoke.73
+ ___67-[HAPAccessoryServerIP _sendListPairingsWithData:queue:completion:]_block_invoke
+ ___67-[HAPWACAccessoryClient _performWiFiJoinWithScanResult:completion:]_block_invoke
+ ___67-[HAPWACAccessoryClient _restoreNetworkWithNetworkInfo:completion:]_block_invoke
+ ___67-[_HAPAccessoryServerBTLE200 _reallySendRequest:completionHandler:]_block_invoke.781
+ ___69-[HAP2AccessoryServer(Unpaired) _handleDiscoveredRemovedAccessories:]_block_invoke
+ ___69-[HAP2AccessoryServer(Unpaired) _handleDiscoveredRemovedAccessories:]_block_invoke_2
+ ___71-[_HAPAccessoryServerBTLE200 _getPairingFeaturesWithCompletionHandler:]_block_invoke.652
+ ___72-[HAP2AccessoryServerController _disableAllCharacteristicsNotification:]_block_invoke.357
+ ___72-[HAP2AccessoryServerController _disableAllCharacteristicsNotification:]_block_invoke_2.358
+ ___74-[HAPAccessoryServerHAP2Adapter discoverRemovedAccessoriesWithCompletion:]_block_invoke
+ ___75-[HAPAccessoryServer enableRemovedAccessoryKey:completionQueue:completion:]_block_invoke
+ ___75-[_HAPAccessoryServerBTLE100 peripheral:didUpdateValueForDescriptor:error:]_block_invoke.315
+ ___75-[_HAPAccessoryServerBTLE200 addPairing:completionQueue:completionHandler:]_block_invoke.699
+ ___75-[_HAPAccessoryServerBTLE200 addPairing:completionQueue:completionHandler:]_block_invoke.706
+ ___75-[_HAPAccessoryServerBTLE200 addPairing:completionQueue:completionHandler:]_block_invoke.710
+ ___75-[_HAPAccessoryServerBTLE200 addPairing:completionQueue:completionHandler:]_block_invoke_2.714
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.554
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.556
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.555
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.557
+ ___76-[HAPSystemKeychainStore allKeychainItemsForType:identifier:syncable:error:]_block_invoke.343
+ ___76-[_HAPAccessoryServerBTLE200 _sendRequest:shouldPrioritize:responseHandler:]_block_invoke.772
+ ___76-[_HAPAccessoryServerBTLE200 discoverAccessoriesAndReadCharacteristicTypes:]_block_invoke.196
+ ___76-[_HAPAccessoryServerBTLE200 discoverAccessoriesAndReadCharacteristicTypes:]_block_invoke.201
+ ___76-[_HAPAccessoryServerBTLE200 discoverAccessoriesAndReadCharacteristicTypes:]_block_invoke_2.205
+ ___77-[HAP2AccessoryServerController _handleAttributeDatabaseResponse:completion:]_block_invoke.213
+ ___77-[HAPAccessoryServer removePairingsWithRemovedAccessoryKey:queue:completion:]_block_invoke
+ ___77-[HAPAccessoryServer removePairingsWithRemovedAccessoryKey:queue:completion:]_block_invoke.121
+ ___77-[HAPAccessoryServer removePairingsWithRemovedAccessoryKey:queue:completion:]_block_invoke.123
+ ___77-[HAPAccessoryServer removePairingsWithRemovedAccessoryKey:queue:completion:]_block_invoke.127
+ ___77-[HAPAccessoryServer removePairingsWithRemovedAccessoryKey:queue:completion:]_block_invoke_2
+ ___77-[HAPAccessoryServer removePairingsWithRemovedAccessoryKey:queue:completion:]_block_invoke_2.128
+ ___77-[HAPAccessoryServer removePairingsWithRemovedAccessoryKey:queue:completion:]_block_invoke_3
+ ___77-[_HAPAccessoryServerBTLE200 handleDisconnectionWithError:completionHandler:]_block_invoke.842
+ ___77-[_HAPAccessoryServerBTLE200 handleDisconnectionWithError:completionHandler:]_block_invoke.847
+ ___78-[HAP2AccessoryServerController _getPairingsCharacteristicForAccessory:error:]_block_invoke
+ ___78-[HAP2AccessoryServerController _getPairingsCharacteristicForAccessory:error:]_block_invoke.275
+ ___78-[_HAPAccessoryServerBTLE200 removePairing:completionQueue:completionHandler:]_block_invoke.716
+ ___78-[_HAPAccessoryServerBTLE200 removePairing:completionQueue:completionHandler:]_block_invoke.723
+ ___78-[_HAPAccessoryServerBTLE200 removePairing:completionQueue:completionHandler:]_block_invoke.727
+ ___78-[_HAPAccessoryServerBTLE200 removePairing:completionQueue:completionHandler:]_block_invoke_2.731
+ ___79-[HAP2AccessoryServer(Unpaired) getPairingsWithRemovedAccessoryKey:completion:]_block_invoke
+ ___79-[HAP2AccessoryServer(Unpaired) getPairingsWithRemovedAccessoryKey:completion:]_block_invoke_2
+ ___79-[HAPAccessoryServerIP _queueListPairingWithCompletionQueue:completionHandler:]_block_invoke.167
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1227
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1228
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1230
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1229
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1231
+ ___79-[_HAPAccessoryServerBTLE200 generateBroadcastKey:queue:withCompletionHandler:]_block_invoke.854
+ ___80-[HAP2AccessoryServerController _callCharacteristicCompletion:operations:error:]_block_invoke.384
+ ___80-[HAP2AccessoryServerController _callCharacteristicCompletion:operations:error:]_block_invoke.386
+ ___80-[HAP2AccessoryServerController _callCharacteristicCompletion:operations:error:]_block_invoke.387
+ ___80-[HAPAccessoryServerIP _establishSecureSessionAndListPairings:queue:completion:]_block_invoke
+ ___80-[HAPAccessoryServerIP _establishSecureSessionAndListPairings:queue:completion:]_block_invoke_2
+ ___80-[HAPAccessoryServerIP _establishSecureSessionAndListPairings:queue:completion:]_block_invoke_3
+ ___80-[_HAPAccessoryServerBTLE200 _generateBroadcastKey:queue:withCompletionHandler:]_block_invoke.864
+ ___80-[_HAPAccessoryServerBTLE200 listPairingsWithCompletionQueue:completionHandler:]_block_invoke.734
+ ___80-[_HAPAccessoryServerBTLE200 listPairingsWithCompletionQueue:completionHandler:]_block_invoke.735
+ ___80-[_HAPAccessoryServerBTLE200 listPairingsWithCompletionQueue:completionHandler:]_block_invoke.742
+ ___81-[HAP2AccessoryServer(Unpaired) _handleUpdatedRemovedProtocolInformationService:]_block_invoke
+ ___82-[HAP2AccessoryServer(Unpaired) _handleUpdatedRemovedAccessoryInformationService:]_block_invoke
+ ___82-[HAPAccessoryServerHAP2Adapter accessoryServer:doesRequirePermission:completion:]_block_invoke.285
+ ___82-[_HAPAccessoryServerBTLE100 removePairingForCurrentControllerOnQueue:completion:]_block_invoke.342
+ ___82-[_HAPAccessoryServerBTLE100 removePairingForCurrentControllerOnQueue:completion:]_block_invoke.343
+ ___83-[HAPAccessoryServerBrowserIP wacBrowser:didFindUnconfiguredPairedHAPWACAccessory:]_block_invoke.76
+ ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.229
+ ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.237
+ ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.238
+ ___83-[_HAPAccessoryServerBTLE200 enableRemovedAccessoryKey:completionQueue:completion:]_block_invoke
+ ___83-[_HAPAccessoryServerBTLE200 enableRemovedAccessoryKey:completionQueue:completion:]_block_invoke.743
+ ___83-[_HAPAccessoryServerBTLE200 enableRemovedAccessoryKey:completionQueue:completion:]_block_invoke.744
+ ___83-[_HAPAccessoryServerBTLE200 enableRemovedAccessoryKey:completionQueue:completion:]_block_invoke.745
+ ___84-[_HAPAccessoryServerBTLE200 _configureCharacteristics:queue:withCompletionHandler:]_block_invoke.604
+ ___84-[_HAPAccessoryServerBTLE200 _configureCharacteristics:queue:withCompletionHandler:]_block_invoke.605
+ ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.303
+ ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.304
+ ___86-[HAPAccessoryServerHAP2Adapter enableRemovedAccessoryKey:completionQueue:completion:]_block_invoke
+ ___86-[HAPAccessoryServerHAP2Adapter enableRemovedAccessoryKey:completionQueue:completion:]_block_invoke.277
+ ___86-[HAPAccessoryServerHAP2Adapter enableRemovedAccessoryKey:completionQueue:completion:]_block_invoke.278
+ ___86-[HAPAccessoryServerHAP2Adapter enableRemovedAccessoryKey:completionQueue:completion:]_block_invoke.279
+ ___86-[HAPAccessoryServerIP _establishSecureConnectionAndFetchAttributeDatabaseWithReason:]_block_invoke.141
+ ___86-[_HAPAccessoryServerBTLE100 _removePairingWithIdentifier:publicKey:queue:completion:]_block_invoke.341
+ ___88-[HAP2AccessoryServer(Unpaired) removeUnpairedAccessoryPairing:accessoryKey:completion:]_block_invoke
+ ___88-[HAP2AccessoryServer(Unpaired) removeUnpairedAccessoryPairing:accessoryKey:completion:]_block_invoke.18
+ ___88-[HAP2AccessoryServer(Unpaired) removeUnpairedAccessoryPairing:accessoryKey:completion:]_block_invoke.19
+ ___88-[HAP2AccessoryServer(Unpaired) removeUnpairedAccessoryPairing:accessoryKey:completion:]_block_invoke_2
+ ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.239
+ ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.240
+ ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.241
+ ___88-[HAPAccessoryServerIP _queueAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.166
+ ___88-[HAPAccessoryServerIP _startAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.532
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.185
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.187
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.196
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.206
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.207
+ ___89-[_HAPAccessoryServerBTLE100 _addPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.331
+ ___90-[HAP2AccessoryServerController enableNotificationsForCharacteristics:options:completion:]_block_invoke.241
+ ___90-[HAP2AccessoryServerController enableNotificationsForCharacteristics:options:completion:]_block_invoke.252
+ ___90-[HAP2AccessoryServerController enableNotificationsForCharacteristics:options:completion:]_block_invoke.256
+ ___90-[HAP2AccessoryServerController enableNotificationsForCharacteristics:options:completion:]_block_invoke.261
+ ___90-[HAP2AccessoryServerController enableNotificationsForCharacteristics:options:completion:]_block_invoke_2.262
+ ___90-[HAP2AccessoryServerController writeValuesForCharacteristics:timeout:options:completion:]_block_invoke.237
+ ___90-[HAPAccessoryServerIP _queueEnableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.168
+ ___90-[HAPAccessoryServerIP _writeCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.226
+ ___91-[HAP2AccessoryServerController disableNotificationsForCharacteristics:options:completion:]_block_invoke.263
+ ___91-[HAP2AccessoryServerController disableNotificationsForCharacteristics:options:completion:]_block_invoke.268
+ ___92-[HAP2AccessoryServer(Unpaired) updateRemovedAccessoriesWithReason:accessoryKey:completion:]_block_invoke
+ ___92-[HAP2AccessoryServer(Unpaired) updateRemovedAccessoriesWithReason:accessoryKey:completion:]_block_invoke.23
+ ___92-[HAP2AccessoryServer(Unpaired) updateRemovedAccessoriesWithReason:accessoryKey:completion:]_block_invoke_2
+ ___92-[HAP2AccessoryServer(Unpaired) updateRemovedAccessoriesWithReason:accessoryKey:completion:]_block_invoke_3
+ ___93-[HAPAccessoryServerHAP2Adapter enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.210
+ ___93-[HAPAccessoryServerIP _establishSecureSessionAndListPairingsWithCompletionQueue:completion:]_block_invoke
+ ___94-[HAP2AccessoryServerController _createOperationsToReadCharacteristics:timeout:options:error:]_block_invoke.232
+ ___94-[HAPAccessoryServerHAP2Adapter _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.218
+ ___94-[HAPAccessoryServerHAP2Adapter _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke_2.219
+ ___97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke.225
+ ___97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke_2.226
+ ___97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke_3.227
+ ___99-[HAPAccessoryServerIP writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.225
+ ___Block_byref_object_copy_.11068
+ ___Block_byref_object_copy_.11465
+ ___Block_byref_object_copy_.12296
+ ___Block_byref_object_copy_.12493
+ ___Block_byref_object_copy_.125
+ ___Block_byref_object_copy_.14403
+ ___Block_byref_object_copy_.15156
+ ___Block_byref_object_copy_.15945
+ ___Block_byref_object_copy_.17156
+ ___Block_byref_object_copy_.18518
+ ___Block_byref_object_copy_.19422
+ ___Block_byref_object_copy_.19642
+ ___Block_byref_object_copy_.20647
+ ___Block_byref_object_copy_.21266
+ ___Block_byref_object_copy_.22395
+ ___Block_byref_object_copy_.2303
+ ___Block_byref_object_copy_.23210
+ ___Block_byref_object_copy_.26225
+ ___Block_byref_object_copy_.27505
+ ___Block_byref_object_copy_.27672
+ ___Block_byref_object_copy_.2971
+ ___Block_byref_object_copy_.382
+ ___Block_byref_object_copy_.4552
+ ___Block_byref_object_copy_.5439
+ ___Block_byref_object_copy_.5736
+ ___Block_byref_object_copy_.6166
+ ___Block_byref_object_copy_.6816
+ ___Block_byref_object_copy_.7001
+ ___Block_byref_object_copy_.7798
+ ___Block_byref_object_copy_.850
+ ___Block_byref_object_copy_.9399
+ ___Block_byref_object_copy_.9742
+ ___Block_byref_object_copy_.9946
+ ___Block_byref_object_dispose_.11069
+ ___Block_byref_object_dispose_.11466
+ ___Block_byref_object_dispose_.12297
+ ___Block_byref_object_dispose_.12494
+ ___Block_byref_object_dispose_.126
+ ___Block_byref_object_dispose_.14404
+ ___Block_byref_object_dispose_.15157
+ ___Block_byref_object_dispose_.15946
+ ___Block_byref_object_dispose_.17157
+ ___Block_byref_object_dispose_.18519
+ ___Block_byref_object_dispose_.19423
+ ___Block_byref_object_dispose_.19643
+ ___Block_byref_object_dispose_.20648
+ ___Block_byref_object_dispose_.21267
+ ___Block_byref_object_dispose_.22396
+ ___Block_byref_object_dispose_.2304
+ ___Block_byref_object_dispose_.23211
+ ___Block_byref_object_dispose_.26226
+ ___Block_byref_object_dispose_.27506
+ ___Block_byref_object_dispose_.27673
+ ___Block_byref_object_dispose_.2972
+ ___Block_byref_object_dispose_.383
+ ___Block_byref_object_dispose_.4553
+ ___Block_byref_object_dispose_.5440
+ ___Block_byref_object_dispose_.5737
+ ___Block_byref_object_dispose_.6167
+ ___Block_byref_object_dispose_.6817
+ ___Block_byref_object_dispose_.7002
+ ___Block_byref_object_dispose_.7799
+ ___Block_byref_object_dispose_.851
+ ___Block_byref_object_dispose_.9400
+ ___Block_byref_object_dispose_.9743
+ ___Block_byref_object_dispose_.9947
+ ___block_descriptor_40_e8_32s_e51_q24?0"HAPPairingIdentity"8"HAPPairingIdentity"16ls32l8
+ ___block_descriptor_48_e8_32bs40w_e22_v16?0"NSDictionary"8lw40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e23_v20?0i8^{__CFArray=}12lw40l8s32l8
+ ___block_descriptor_48_e8_32r40w_e5_v8?0lw40l8r32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48w_e17_v16?0"NSError"8lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e22_v16?0"NSDictionary"8lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e23_"<HAP2Cancelable>"8?0lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40r48w_e5_v8?0lw48l8s32l8r40l8
+ ___block_descriptor_64_e8_32s40bs48r56w_e5_v8?0lw56l8s40l8s32l8r48l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e17_v16?0"NSError"8lw56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e23_"<HAP2Cancelable>"8?0lw56l8s32l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s40l8s56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e40_v24?0"HAPPairingIdentity"8"NSError"16ls32l8s40l8s56l8s48l8
+ ___block_descriptor_72_e8_32s40s48bs56r64r_e17_v16?0"NSError"8ls32l8s40l8s48l8r56l8r64l8
+ ___block_literal_global.10091
+ ___block_literal_global.1020
+ ___block_literal_global.10737
+ ___block_literal_global.11519
+ ___block_literal_global.12292
+ ___block_literal_global.1247
+ ___block_literal_global.12662
+ ___block_literal_global.1284
+ ___block_literal_global.14693
+ ___block_literal_global.1516
+ ___block_literal_global.17276
+ ___block_literal_global.175
+ ___block_literal_global.17706
+ ___block_literal_global.19075
+ ___block_literal_global.19432
+ ___block_literal_global.20805
+ ___block_literal_global.216
+ ___block_literal_global.2208
+ ___block_literal_global.22138
+ ___block_literal_global.22417
+ ___block_literal_global.22863
+ ___block_literal_global.23816
+ ___block_literal_global.240
+ ___block_literal_global.247
+ ___block_literal_global.25260
+ ___block_literal_global.255
+ ___block_literal_global.25599
+ ___block_literal_global.264
+ ___block_literal_global.265
+ ___block_literal_global.27278
+ ___block_literal_global.273
+ ___block_literal_global.27901
+ ___block_literal_global.3036
+ ___block_literal_global.339
+ ___block_literal_global.399
+ ___block_literal_global.3993
+ ___block_literal_global.401
+ ___block_literal_global.403
+ ___block_literal_global.405
+ ___block_literal_global.407
+ ___block_literal_global.409
+ ___block_literal_global.421
+ ___block_literal_global.5521
+ ___block_literal_global.5732
+ ___block_literal_global.6287
+ ___block_literal_global.6827
+ ___block_literal_global.6975
+ ___block_literal_global.8113
+ ___block_literal_global.835
+ ___block_literal_global.902
+ ___block_literal_global.9027
+ ___block_literal_global.9498
+ ___gxx_personality_v0
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_CoreHAP
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_CoreHAP
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_CoreHAP
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_CoreHAP
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_CoreHAP
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_CoreHAP
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_CoreHAP
+ __systemKeychainStoreSingleton.systemStore
+ __systemKeychainStoreSingleton.systemStoreAllocated
+ _freeifaddrs
+ _getifaddrs
+ _hkConfig.23800
+ _kCFPreferencesCurrentApplication
+ _logCategory._hmf_once_t340
+ _logCategory._hmf_once_t43
+ _logCategory._hmf_once_t434
+ _logCategory._hmf_once_t52
+ _logCategory._hmf_once_t58
+ _logCategory._hmf_once_t99
+ _logCategory._hmf_once_v100
+ _logCategory._hmf_once_v341
+ _logCategory._hmf_once_v435
+ _logCategory._hmf_once_v44
+ _logCategory._hmf_once_v53
+ _logCategory._hmf_once_v59
+ _objc_msgSend$CA
+ _objc_msgSend$CMAFSessionID
+ _objc_msgSend$CMAFSessionStart
+ _objc_msgSend$CMAFSessionStop
+ _objc_msgSend$CSR
+ _objc_msgSend$KID
+ _objc_msgSend$SDPAnswer
+ _objc_msgSend$SDPMLineIndex
+ _objc_msgSend$SDPMid
+ _objc_msgSend$SDPOffer
+ _objc_msgSend$SFrameConfiguration
+ _objc_msgSend$URL
+ _objc_msgSend$_completeRefreshScanWithResult:
+ _objc_msgSend$_createStandardSecuritySession
+ _objc_msgSend$_establishSecureSessionAndListPairings:queue:completion:
+ _objc_msgSend$_establishSecureSessionAndListPairingsWithCompletionQueue:completion:
+ _objc_msgSend$_handleRefreshScanResults:status:
+ _objc_msgSend$_interface:hasAddressesWithPrefix:
+ _objc_msgSend$_newLowestUUIDUsernameForHH2ControllerKey
+ _objc_msgSend$_performWiFiJoinWithScanResult:completion:
+ _objc_msgSend$_preferredHH2ControllerKey
+ _objc_msgSend$_refreshScanResultForSSID:completion:
+ _objc_msgSend$_restoreNetworkWithNetworkInfo:completion:
+ _objc_msgSend$_sendListPairingsWithData:queue:completion:
+ _objc_msgSend$_systemKeychainStoreSingleton
+ _objc_msgSend$_updateServerMetadata:controller:
+ _objc_msgSend$active
+ _objc_msgSend$additionalCandidates
+ _objc_msgSend$allowsRemovedAccessoryKeys
+ _objc_msgSend$audioCipherSuite
+ _objc_msgSend$audioSSRC
+ _objc_msgSend$audioTier
+ _objc_msgSend$averageBitrate
+ _objc_msgSend$baseKey
+ _objc_msgSend$bitDepth
+ _objc_msgSend$buffers
+ _objc_msgSend$cameraSensors
+ _objc_msgSend$candidate
+ _objc_msgSend$clientCertificate
+ _objc_msgSend$clipID
+ _objc_msgSend$codec
+ _objc_msgSend$dataSource
+ _objc_msgSend$deleteRemovedAccessoryKeyForName:error:
+ _objc_msgSend$discoverRemovedAccessoriesWithCompletion:
+ _objc_msgSend$enableRemovedAccessoryKey:completionQueue:completion:
+ _objc_msgSend$events
+ _objc_msgSend$frameRate
+ _objc_msgSend$framesPerSecond
+ _objc_msgSend$getPairingsWithRemovedAccessoryKey:completion:
+ _objc_msgSend$hapErrorWithCode:OSStatus:
+ _objc_msgSend$height
+ _objc_msgSend$initWithActive:
+ _objc_msgSend$initWithAudioCipherSuite:videoCipherSuite:baseKey:keyID:ratchetBits:ratchetTime:
+ _objc_msgSend$initWithCMAFSessionID:
+ _objc_msgSend$initWithCSR:
+ _objc_msgSend$initWithCameraSensors:
+ _objc_msgSend$initWithCandidate:SDPMid:SDPMLineIndex:
+ _objc_msgSend$initWithClientCertificate:CA:
+ _objc_msgSend$initWithClipID:
+ _objc_msgSend$initWithCodec:payloadType:tiers:
+ _objc_msgSend$initWithCommand:sequenceNumber:limit:
+ _objc_msgSend$initWithDataSource:
+ _objc_msgSend$initWithEvents:
+ _objc_msgSend$initWithIdentifier:count:vertices:
+ _objc_msgSend$initWithIdentifier:quality:targetAverageBitrate:width:height:frameRate:
+ _objc_msgSend$initWithIdentifier:quality:width:height:framesPerSecond:averageBitrate:peakBitrate:
+ _objc_msgSend$initWithIdentifier:targetAverageBitrate:sampleRate:bitDepth:packetTime:numberOfChannels:
+ _objc_msgSend$initWithIdentifier:type:intervals:
+ _objc_msgSend$initWithInverted:count:polygons:
+ _objc_msgSend$initWithKey:keyNumber:
+ _objc_msgSend$initWithKeyID:
+ _objc_msgSend$initWithNeedsUpdate:
+ _objc_msgSend$initWithSFrameConfiguration:
+ _objc_msgSend$initWithSensorDimensions:
+ _objc_msgSend$initWithSequenceNumber:count:
+ _objc_msgSend$initWithSequenceNumber:type:CMAFSessionStart:CMAFSessionStop:motion:
+ _objc_msgSend$initWithSessionID:command:start:stop:stopAction:
+ _objc_msgSend$initWithSessionIdentifier:
+ _objc_msgSend$initWithSessionIdentifier:SDPAnswer:additionalCandidates:
+ _objc_msgSend$initWithSessionIdentifier:SDPAnswer:status:
+ _objc_msgSend$initWithSessionIdentifier:SDPOffer:SFrameConfiguration:
+ _objc_msgSend$initWithSessionIdentifier:SDPOffer:additionalCandidates:status:KID:
+ _objc_msgSend$initWithSessionIdentifier:command:videoTier:videoSSRC:audioTier:audioSSRC:
+ _objc_msgSend$initWithSessionIdentifier:status:
+ _objc_msgSend$initWithURL:serverCertificate:
+ _objc_msgSend$initWithVersion:buffers:
+ _objc_msgSend$initWithVersion:videoStreamCapabilities:cameraSensors:
+ _objc_msgSend$initWithWidth:height:
+ _objc_msgSend$initWithZoneDataVersion:zoneData:
+ _objc_msgSend$intervals
+ _objc_msgSend$inverted
+ _objc_msgSend$isHH2KeyRollEnabled
+ _objc_msgSend$isThreadRadioAvailable
+ _objc_msgSend$keyID
+ _objc_msgSend$keyNumber
+ _objc_msgSend$lastScanUptime
+ _objc_msgSend$limit
+ _objc_msgSend$listPairingsWithCompletionQueue:completionHandler:
+ _objc_msgSend$managesConnectionStateExternally
+ _objc_msgSend$motion
+ _objc_msgSend$needsUpdate
+ _objc_msgSend$numberOfChannels
+ _objc_msgSend$payloadType
+ _objc_msgSend$peakBitrate
+ _objc_msgSend$pendingBonjourAdd
+ _objc_msgSend$polygons
+ _objc_msgSend$quality
+ _objc_msgSend$ratchetBits
+ _objc_msgSend$ratchetTime
+ _objc_msgSend$refreshScanCompletion
+ _objc_msgSend$refreshScanResultForSSID:completion:
+ _objc_msgSend$refreshingScanSSID
+ _objc_msgSend$removeUnpairedAccessoryPairing:accessoryKey:completion:
+ _objc_msgSend$removedAccessoryDiscoveryCompletionHandlers
+ _objc_msgSend$removedAccessoryIdentifiers
+ _objc_msgSend$removedAccessoryKey
+ _objc_msgSend$revision
+ _objc_msgSend$sensorDimensions
+ _objc_msgSend$sequenceNumber
+ _objc_msgSend$serverCertificate
+ _objc_msgSend$sessionID
+ _objc_msgSend$setActive:
+ _objc_msgSend$setAdditionalCandidates:
+ _objc_msgSend$setAudioCipherSuite:
+ _objc_msgSend$setAudioSSRC:
+ _objc_msgSend$setAudioTier:
+ _objc_msgSend$setAverageBitrate:
+ _objc_msgSend$setBaseKey:
+ _objc_msgSend$setBitDepth:
+ _objc_msgSend$setBuffers:
+ _objc_msgSend$setCA:
+ _objc_msgSend$setCMAFSessionID:
+ _objc_msgSend$setCMAFSessionStart:
+ _objc_msgSend$setCMAFSessionStop:
+ _objc_msgSend$setCSR:
+ _objc_msgSend$setCameraSensors:
+ _objc_msgSend$setCandidate:
+ _objc_msgSend$setClientCertificate:
+ _objc_msgSend$setClipID:
+ _objc_msgSend$setCodec:
+ _objc_msgSend$setCount:
+ _objc_msgSend$setEvents:
+ _objc_msgSend$setFrameRate:
+ _objc_msgSend$setFramesPerSecond:
+ _objc_msgSend$setHeight:
+ _objc_msgSend$setIntervals:
+ _objc_msgSend$setInverted:
+ _objc_msgSend$setKID:
+ _objc_msgSend$setKeyID:
+ _objc_msgSend$setKeyNumber:
+ _objc_msgSend$setLastScanUptime:
+ _objc_msgSend$setLimit:
+ _objc_msgSend$setMotion:
+ _objc_msgSend$setNeedsUpdate:
+ _objc_msgSend$setNumberOfChannels:
+ _objc_msgSend$setPayloadType:
+ _objc_msgSend$setPeakBitrate:
+ _objc_msgSend$setPendingBonjourAdd:
+ _objc_msgSend$setPolygons:
+ _objc_msgSend$setQuality:
+ _objc_msgSend$setRatchetBits:
+ _objc_msgSend$setRatchetTime:
+ _objc_msgSend$setRefreshScanCompletion:
+ _objc_msgSend$setRefreshingScanSSID:
+ _objc_msgSend$setRemovedAccessoryKey:
+ _objc_msgSend$setSDPAnswer:
+ _objc_msgSend$setSDPMLineIndex:
+ _objc_msgSend$setSDPMid:
+ _objc_msgSend$setSDPOffer:
+ _objc_msgSend$setSFrameConfiguration:
+ _objc_msgSend$setSensorDimensions:
+ _objc_msgSend$setSequenceNumber:
+ _objc_msgSend$setServerCertificate:
+ _objc_msgSend$setSessionID:
+ _objc_msgSend$setStart:
+ _objc_msgSend$setStop:
+ _objc_msgSend$setStopAction:
+ _objc_msgSend$setTargetAverageBitrate:
+ _objc_msgSend$setTiers:
+ _objc_msgSend$setURL:
+ _objc_msgSend$setVertices:
+ _objc_msgSend$setVideoCipherSuite:
+ _objc_msgSend$setVideoSSRC:
+ _objc_msgSend$setVideoStreamCapabilities:
+ _objc_msgSend$setVideoTier:
+ _objc_msgSend$setWidth:
+ _objc_msgSend$setZoneData:
+ _objc_msgSend$setZoneDataVersion:
+ _objc_msgSend$stopAction
+ _objc_msgSend$targetAverageBitrate
+ _objc_msgSend$threadMeshLocalPrefix
+ _objc_msgSend$tiers
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$timeSinceLastScan
+ _objc_msgSend$updateRemovedAccessoriesWithReason:accessoryKey:completion:
+ _objc_msgSend$vertices
+ _objc_msgSend$videoCipherSuite
+ _objc_msgSend$videoSSRC
+ _objc_msgSend$videoStreamCapabilities
+ _objc_msgSend$videoTier
+ _objc_msgSend$wasRemovedFromHome:
+ _objc_msgSend$width
+ _objc_msgSend$zoneData
+ _objc_msgSend$zoneDataVersion
+ _objc_release_x2
+ _sharedInstance.onceToken.17705
+ _strcmp
+ _userInfoFromOSStatus
- +[HAPAccessoryServerIPCacheData logCategory]
- -[HAP2AccessoryServerController _getPairingsCharacteristicForServer:error:]
- -[HAPAccessoryServerBrowserIP _doStartDiscoveringAccessoryServers]
- -[HAPAccessoryServerBrowserIP _prePopulateBrowserFromCacheWithCompletion:]
- -[HAPAccessoryServerBrowserIP cache]
- -[HAPAccessoryServerBrowserIP initWithQueue:cache:]
- -[HAPAccessoryServerBrowserIP isInitialCacheRestored]
- -[HAPAccessoryServerBrowserIP setIsInitialCacheRestored:]
- -[HAPAccessoryServerBrowserIP updateCacheForDeviceID:ipData:]
- -[HAPAccessoryServerIP _updateCacheForDevice:socketInfo:bonjour:]
- -[HAPAccessoryServerIPCacheData .cxx_destruct]
- -[HAPAccessoryServerIPCacheData bonjourDeviceInfo]
- -[HAPAccessoryServerIPCacheData debugDescription]
- -[HAPAccessoryServerIPCacheData dictionaryRepresentation]
- -[HAPAccessoryServerIPCacheData initFromDictionary:]
- -[HAPAccessoryServerIPCacheData initWithCachedIp:bonjourRecord:]
- -[HAPAccessoryServerIPCacheData setBonjourDeviceInfo:]
- -[HAPAccessoryServerIPCacheData setSocketInfo:]
- -[HAPAccessoryServerIPCacheData socketInfo]
- GCC_except_table1053
- GCC_except_table1057
- GCC_except_table1070
- GCC_except_table1075
- GCC_except_table1084
- GCC_except_table1086
- GCC_except_table1088
- GCC_except_table1090
- GCC_except_table1216
- GCC_except_table1220
- GCC_except_table1222
- GCC_except_table1435
- GCC_except_table1641
- GCC_except_table1644
- GCC_except_table1652
- GCC_except_table1654
- GCC_except_table1660
- GCC_except_table1662
- GCC_except_table1666
- GCC_except_table1670
- GCC_except_table1672
- GCC_except_table1677
- GCC_except_table1681
- GCC_except_table1691
- GCC_except_table1699
- GCC_except_table1706
- GCC_except_table1710
- GCC_except_table1714
- GCC_except_table1718
- GCC_except_table1720
- GCC_except_table1869
- GCC_except_table1873
- GCC_except_table1874
- GCC_except_table1876
- GCC_except_table1878
- GCC_except_table1887
- GCC_except_table1889
- GCC_except_table1893
- GCC_except_table1896
- GCC_except_table1898
- GCC_except_table1901
- GCC_except_table1918
- GCC_except_table1921
- GCC_except_table1925
- GCC_except_table1929
- GCC_except_table1936
- GCC_except_table1938
- GCC_except_table1941
- GCC_except_table1946
- GCC_except_table1952
- GCC_except_table1964
- GCC_except_table1975
- GCC_except_table199
- GCC_except_table2013
- GCC_except_table2019
- GCC_except_table206
- GCC_except_table209
- GCC_except_table212
- GCC_except_table215
- GCC_except_table217
- GCC_except_table219
- GCC_except_table2190
- GCC_except_table2197
- GCC_except_table2203
- GCC_except_table2209
- GCC_except_table2212
- GCC_except_table2215
- GCC_except_table2218
- GCC_except_table2224
- GCC_except_table2226
- GCC_except_table223
- GCC_except_table2230
- GCC_except_table2231
- GCC_except_table2233
- GCC_except_table225
- GCC_except_table2329
- GCC_except_table2337
- GCC_except_table2338
- GCC_except_table2339
- GCC_except_table234
- GCC_except_table2340
- GCC_except_table2341
- GCC_except_table2342
- GCC_except_table2357
- GCC_except_table2371
- GCC_except_table238
- GCC_except_table2451
- GCC_except_table2463
- GCC_except_table2489
- GCC_except_table2497
- GCC_except_table2508
- GCC_except_table2522
- GCC_except_table2525
- GCC_except_table2530
- GCC_except_table2538
- GCC_except_table2544
- GCC_except_table2546
- GCC_except_table2720
- GCC_except_table2770
- GCC_except_table2789
- GCC_except_table2803
- GCC_except_table2804
- GCC_except_table2811
- GCC_except_table2826
- GCC_except_table2838
- GCC_except_table2839
- GCC_except_table2841
- GCC_except_table2847
- GCC_except_table2854
- GCC_except_table2857
- GCC_except_table2862
- GCC_except_table2918
- GCC_except_table2921
- GCC_except_table2926
- GCC_except_table2942
- GCC_except_table2956
- GCC_except_table2958
- GCC_except_table2962
- GCC_except_table2970
- GCC_except_table2978
- GCC_except_table3035
- GCC_except_table3037
- GCC_except_table3038
- GCC_except_table3061
- GCC_except_table3305
- GCC_except_table3369
- GCC_except_table3370
- GCC_except_table3374
- GCC_except_table3377
- GCC_except_table3379
- GCC_except_table3380
- GCC_except_table3382
- GCC_except_table3383
- GCC_except_table3385
- GCC_except_table3392
- GCC_except_table3402
- GCC_except_table3405
- GCC_except_table3416
- GCC_except_table3417
- GCC_except_table3419
- GCC_except_table3421
- GCC_except_table3424
- GCC_except_table3427
- GCC_except_table3429
- GCC_except_table3432
- GCC_except_table3435
- GCC_except_table3449
- GCC_except_table3457
- GCC_except_table3461
- GCC_except_table3487
- GCC_except_table3509
- GCC_except_table3512
- GCC_except_table3514
- GCC_except_table3516
- GCC_except_table3591
- GCC_except_table3592
- GCC_except_table3593
- GCC_except_table3594
- GCC_except_table3595
- GCC_except_table3599
- GCC_except_table3600
- GCC_except_table3601
- GCC_except_table3602
- GCC_except_table3603
- GCC_except_table3604
- GCC_except_table3644
- GCC_except_table3670
- GCC_except_table3770
- GCC_except_table3777
- GCC_except_table3795
- GCC_except_table3799
- GCC_except_table3802
- GCC_except_table3805
- GCC_except_table3808
- GCC_except_table3811
- GCC_except_table3814
- GCC_except_table3817
- GCC_except_table3820
- GCC_except_table3823
- GCC_except_table3828
- GCC_except_table3838
- GCC_except_table3841
- GCC_except_table3852
- GCC_except_table3860
- GCC_except_table3864
- GCC_except_table3871
- GCC_except_table3872
- GCC_except_table3876
- GCC_except_table3877
- GCC_except_table3895
- GCC_except_table3899
- GCC_except_table3914
- GCC_except_table3920
- GCC_except_table3922
- GCC_except_table3925
- GCC_except_table3948
- GCC_except_table3950
- GCC_except_table3959
- GCC_except_table405
- GCC_except_table421
- GCC_except_table4225
- GCC_except_table4231
- GCC_except_table4248
- GCC_except_table4252
- GCC_except_table4269
- GCC_except_table4275
- GCC_except_table4288
- GCC_except_table429
- GCC_except_table4302
- GCC_except_table4306
- GCC_except_table4419
- GCC_except_table4483
- GCC_except_table4491
- GCC_except_table4501
- GCC_except_table4543
- GCC_except_table4546
- GCC_except_table4547
- GCC_except_table4548
- GCC_except_table4549
- GCC_except_table459
- GCC_except_table4631
- GCC_except_table4632
- GCC_except_table4633
- GCC_except_table4634
- GCC_except_table4635
- GCC_except_table4636
- GCC_except_table4642
- GCC_except_table4643
- GCC_except_table4645
- GCC_except_table4652
- GCC_except_table4655
- GCC_except_table4657
- GCC_except_table4662
- GCC_except_table4665
- GCC_except_table4668
- GCC_except_table4672
- GCC_except_table4676
- GCC_except_table4705
- GCC_except_table4706
- GCC_except_table4725
- GCC_except_table4735
- GCC_except_table4738
- GCC_except_table4743
- GCC_except_table4746
- GCC_except_table481
- GCC_except_table482
- GCC_except_table484
- GCC_except_table487
- GCC_except_table490
- GCC_except_table5010
- GCC_except_table5014
- GCC_except_table502
- GCC_except_table5059
- GCC_except_table506
- GCC_except_table5063
- GCC_except_table5065
- GCC_except_table5067
- GCC_except_table509
- GCC_except_table516
- GCC_except_table522
- GCC_except_table5234
- GCC_except_table5240
- GCC_except_table5244
- GCC_except_table5245
- GCC_except_table5246
- GCC_except_table5247
- GCC_except_table5253
- GCC_except_table5287
- GCC_except_table5288
- GCC_except_table5289
- GCC_except_table5309
- GCC_except_table5321
- GCC_except_table5324
- GCC_except_table5329
- GCC_except_table5331
- GCC_except_table5345
- GCC_except_table550
- GCC_except_table5568
- GCC_except_table5581
- GCC_except_table5586
- GCC_except_table5589
- GCC_except_table5590
- GCC_except_table5592
- GCC_except_table5593
- GCC_except_table5595
- GCC_except_table560
- GCC_except_table5625
- GCC_except_table5647
- GCC_except_table5651
- GCC_except_table5655
- GCC_except_table5660
- GCC_except_table5664
- GCC_except_table5668
- GCC_except_table567
- GCC_except_table5672
- GCC_except_table5676
- GCC_except_table5684
- GCC_except_table5686
- GCC_except_table5688
- GCC_except_table5748
- GCC_except_table5749
- GCC_except_table5750
- GCC_except_table5751
- GCC_except_table5752
- GCC_except_table5810
- GCC_except_table5814
- GCC_except_table5815
- GCC_except_table5827
- GCC_except_table5833
- GCC_except_table5846
- GCC_except_table5849
- GCC_except_table5850
- GCC_except_table5855
- GCC_except_table5858
- GCC_except_table5865
- GCC_except_table5868
- GCC_except_table5882
- GCC_except_table5889
- GCC_except_table5895
- GCC_except_table5904
- GCC_except_table5906
- GCC_except_table5910
- GCC_except_table5911
- GCC_except_table5927
- GCC_except_table5929
- GCC_except_table5938
- GCC_except_table594
- GCC_except_table5953
- GCC_except_table5954
- GCC_except_table5959
- GCC_except_table5963
- GCC_except_table5964
- GCC_except_table5967
- GCC_except_table5973
- GCC_except_table5977
- GCC_except_table598
- GCC_except_table5981
- GCC_except_table5983
- GCC_except_table5985
- GCC_except_table5989
- GCC_except_table601
- GCC_except_table603
- GCC_except_table609
- GCC_except_table611
- GCC_except_table6141
- GCC_except_table6197
- GCC_except_table6200
- GCC_except_table6204
- GCC_except_table6210
- GCC_except_table6217
- GCC_except_table6218
- GCC_except_table6234
- GCC_except_table6238
- GCC_except_table6239
- GCC_except_table624
- GCC_except_table6240
- GCC_except_table628
- GCC_except_table6289
- GCC_except_table6290
- GCC_except_table6292
- GCC_except_table6295
- GCC_except_table632
- GCC_except_table6322
- GCC_except_table6323
- GCC_except_table6328
- GCC_except_table6348
- GCC_except_table6367
- GCC_except_table6375
- GCC_except_table6380
- GCC_except_table6381
- GCC_except_table6382
- GCC_except_table6396
- GCC_except_table6399
- GCC_except_table6405
- GCC_except_table6411
- GCC_except_table642
- GCC_except_table6423
- GCC_except_table6429
- GCC_except_table643
- GCC_except_table6438
- GCC_except_table6444
- GCC_except_table6463
- GCC_except_table6467
- GCC_except_table648
- GCC_except_table6488
- GCC_except_table6490
- GCC_except_table6491
- GCC_except_table651
- GCC_except_table6517
- GCC_except_table654
- GCC_except_table659
- GCC_except_table663
- GCC_except_table669
- GCC_except_table6744
- GCC_except_table675
- GCC_except_table676
- GCC_except_table6776
- GCC_except_table6779
- GCC_except_table6945
- GCC_except_table7008
- GCC_except_table702
- GCC_except_table7072
- GCC_except_table7078
- GCC_except_table710
- GCC_except_table7124
- GCC_except_table7128
- GCC_except_table7130
- GCC_except_table7132
- GCC_except_table7134
- GCC_except_table7136
- GCC_except_table7138
- GCC_except_table7140
- GCC_except_table7142
- GCC_except_table7147
- GCC_except_table7149
- GCC_except_table7151
- GCC_except_table717
- GCC_except_table718
- GCC_except_table7180
- GCC_except_table7183
- GCC_except_table7184
- GCC_except_table7223
- GCC_except_table7224
- GCC_except_table7225
- GCC_except_table7227
- GCC_except_table7228
- GCC_except_table7230
- GCC_except_table7232
- GCC_except_table7234
- GCC_except_table7235
- GCC_except_table7241
- GCC_except_table7294
- GCC_except_table7301
- GCC_except_table7395
- GCC_except_table7411
- GCC_except_table7413
- GCC_except_table7415
- GCC_except_table7418
- GCC_except_table7420
- GCC_except_table7422
- GCC_except_table7424
- GCC_except_table7425
- GCC_except_table7427
- GCC_except_table7431
- GCC_except_table7436
- GCC_except_table752
- GCC_except_table775
- GCC_except_table794
- GCC_except_table818
- GCC_except_table822
- GCC_except_table836
- GCC_except_table841
- GCC_except_table945
- GCC_except_table947
- _HAPErrorCodeFromHAPBLEStatusErrorCode
- _OBJC_CLASS_$_HAPAccessoryServerIPCacheData
- _OBJC_IVAR_$_HAPAccessoryServerBrowserIP._cache
- _OBJC_IVAR_$_HAPAccessoryServerBrowserIP._isInitialCacheRestored
- _OBJC_IVAR_$_HAPAccessoryServerIPCacheData._bonjourDeviceInfo
- _OBJC_IVAR_$_HAPAccessoryServerIPCacheData._socketInfo
- _OBJC_METACLASS_$_HAPAccessoryServerIPCacheData
- __CopyPairingIdentityDelegateCallback_f.15247
- __CopyPairingIdentityDelegateCallback_f.22071
- __CopyPairingIdentityDelegateCallback_f.2810
- __FindPairedPeerDelegateCallback_f.2809
- __OBJC_$_CLASS_METHODS_HAPAccessoryServerIPCacheData
- __OBJC_$_INSTANCE_METHODS_HAPAccessoryServerIPCacheData
- __OBJC_$_INSTANCE_VARIABLES_HAPAccessoryServerIPCacheData
- __OBJC_$_PROP_LIST_HAP2Accessory.289
- __OBJC_$_PROP_LIST_HAP2AccessoryServerBrowser.400
- __OBJC_$_PROP_LIST_HAP2AccessoryServerCoordinator.182
- __OBJC_$_PROP_LIST_HAP2AccessoryServerPairingDriver.268
- __OBJC_$_PROP_LIST_HAPAccessoryServerIPCacheData
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_HAP2AccessoryServerDelegate
- __OBJC_CLASS_RO_$_HAPAccessoryServerIPCacheData
- __OBJC_METACLASS_RO_$_HAPAccessoryServerIPCacheData
- __PairSetupPromptForSetupCodeDelegateCallback_f.22073
- __SavePairedPeerDelegateCallback_f.15238
- __SavePairedPeerDelegateCallback_f.22067
- ___103-[_HAPAccessoryServerBTLE100 _handlePairingsReadForCharacteristic:readError:removing:queue:completion:]_block_invoke.337
- ___106-[_HAPAccessoryServerBTLE200 removePairingForCurrentControllerOnQueue:completion:serverPairingCompletion:]_block_invoke.735
- ___106-[_HAPAccessoryServerBTLE200 removePairingForCurrentControllerOnQueue:completion:serverPairingCompletion:]_block_invoke.736
- ___108-[HAP2AccessoryServerController _removePairingCompletionWithIdentity:cleanupLocalData:operation:completion:]_block_invoke.268
- ___108-[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:expiry:queue:completionHandler:]_block_invoke.283
- ___108-[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:expiry:queue:completionHandler:]_block_invoke.284
- ___112-[HAPWACAccessoryClient _performEasyConfigWithPairingPrompt:performPairSetup:isSplit:pairingRequest:completion:]_block_invoke.108
- ___112-[HAPWACAccessoryClient _performEasyConfigWithPairingPrompt:performPairSetup:isSplit:pairingRequest:completion:]_block_invoke.110
- ___112-[HAPWACAccessoryClient _performEasyConfigWithPairingPrompt:performPairSetup:isSplit:pairingRequest:completion:]_block_invoke.117
- ___112-[HAPWACAccessoryClient _performEasyConfigWithPairingPrompt:performPairSetup:isSplit:pairingRequest:completion:]_block_invoke.131
- ___112-[HAPWACAccessoryClient _performEasyConfigWithPairingPrompt:performPairSetup:isSplit:pairingRequest:completion:]_block_invoke.136
- ___112-[HAPWACAccessoryClient _performEasyConfigWithPairingPrompt:performPairSetup:isSplit:pairingRequest:completion:]_block_invoke_2.118
- ___115-[HAPAccessoryServerIP _handleWriteECONNResetError:writeRequests:responses:timeout:expiry:queue:completionHandler:]_block_invoke.265
- ___120-[HAPAccessoryServerIP _handleReadECONNRESETError:readCharacteristics:responses:timeout:expiry:queue:completionHandler:]_block_invoke.209
- ___37+[HAPSystemKeychainStore systemStore]_block_invoke
- ___41-[HAPAccessoryServerIP getAccessoryInfo:]_block_invoke.524
- ___44+[HAPAccessoryServerIPCacheData logCategory]_block_invoke
- ___44-[HAPAccessoryServerIP _pairVerifyStartWAC:]_block_invoke.119
- ___45-[HAP2AccessoryServerController closeSession]_block_invoke.287
- ___45-[HAP2AccessoryServerController closeSession]_block_invoke.291
- ___45-[HAPAccessoryServerIP _pairSetupContinueWAC]_block_invoke.117
- ___45-[HAPAccessoryServerIP stopPairingWithError:]_block_invoke.164
- ___45-[_HAPAccessoryServerBTLE100 _pairSetupStart]_block_invoke.322
- ___47-[HAPAccessoryServerIP identifyWithCompletion:]_block_invoke.653
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.120
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.121
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.123
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.124
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.126
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke_2.122
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke_2.125
- ___48-[HAPAccessoryServerIP startPairingWithRequest:]_block_invoke.162
- ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.127
- ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.132
- ___49-[HAPAccessoryServerIP authSession:authComplete:]_block_invoke.570
- ___49-[HAPWACAccessoryClient _joinCompleteWithStatus:]_block_invoke.77
- ___50-[HAPAccessoryServerIP networkMonitorIsReachable:]_block_invoke.519
- ___50-[_HAPAccessoryServerBTLE200 _checkForAuthPrompt:]_block_invoke.635
- ___50-[_HAPAccessoryServerBTLE200 _checkForAuthPrompt:]_block_invoke.642
- ___50-[_HAPAccessoryServerBTLE200 _checkForAuthPrompt:]_block_invoke.646
- ___50-[_HAPAccessoryServerBTLE200 isReadyForOperation:]_block_invoke.834
- ___52-[HAP2AccessoryServer(Paired) unpairWithCompletion:]_block_invoke.64
- ___52-[HAP2AccessoryServer(Paired) unpairWithCompletion:]_block_invoke.65
- ___53-[HAPAccessoryServerHAP2Adapter _printMissingValues:]_block_invoke.230
- ___53-[HAPAccessoryServerHAP2Adapter _printMissingValues:]_block_invoke.238
- ___53-[HAPAccessoryServerIP setPairVerifyCompletionBlock:]_block_invoke.423
- ___53-[_HAPAccessoryServerBTLE200 identifyWithCompletion:]_block_invoke.758
- ___53-[_HAPAccessoryServerBTLE200 identifyWithCompletion:]_block_invoke.765
- ___54-[HAP2AccessoryServer(Paired) _getSleepIntervalValue:]_block_invoke.252
- ___54-[HAPWACAccessoryClient restoreNetworkWithCompletion:]_block_invoke.101
- ___54-[HAPWACAccessoryClient restoreNetworkWithCompletion:]_block_invoke_2.102
- ___54-[_HAPAccessoryServerBTLE200 startPairingWithRequest:]_block_invoke.624
- ___55-[HAP2AccessoryServerController addPairing:completion:]_block_invoke.272
- ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.560
- ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.565
- ___55-[_HAPAccessoryServerBTLE200 authSession:authComplete:]_block_invoke.994
- ___56-[HAP2AccessoryServer _updateConnectionState:withError:]_block_invoke
- ___56-[HAP2AccessoryServer(Paired) removePairing:completion:]_block_invoke.69
- ___56-[HAP2AccessoryServer(Paired) removePairing:completion:]_block_invoke.70
- ___56-[HAP2AccessoryServerController _scheduleRestartSession]_block_invoke.363
- ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke.554
- ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke_2.558
- ___59-[HAP2AccessoryServer(Paired) updateAccessoriesWithReason:]_block_invoke.80
- ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke.482
- ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke_2.483
- ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.460
- ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.465
- ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.466
- ___59-[_HAPAccessoryServerBTLE200 peripheral:didModifyServices:]_block_invoke.959
- ___60-[HAPAccessoryServerIP _validatePairingAuthMethod:activity:]_block_invoke.538
- ___60-[HAPWACAccessoryClient joinAccessoryNetworkWithCompletion:]_block_invoke.90
- ___60-[HAPWACAccessoryClient joinAccessoryNetworkWithCompletion:]_block_invoke.91
- ___60-[_HAPAccessoryServerBTLE200 continuePairingAfterAuthPrompt]_block_invoke.665
- ___63-[HAPAccessoryServerBrowserIP startDiscoveringAccessoryServers]_block_invoke_2
- ___63-[HAPAccessoryServerBrowserIP startDiscoveringAccessoryServers]_block_invoke_3
- ___63-[_HAPAccessoryServerBTLE100 _handlePairSetupExchangeWithData:]_block_invoke.323
- ___63-[_HAPAccessoryServerBTLE200 authSession:sendAuthExchangeData:]_block_invoke.987
- ___63-[_HAPAccessoryServerBTLE200 authSession:sendAuthExchangeData:]_block_invoke_2.990
- ___64-[HAP2AccessoryServer(Paired) _pollAccessoryOnQueueWithOptions:]_block_invoke.267
- ___64-[HAP2AccessoryServer(Paired) _pollAccessoryOnQueueWithOptions:]_block_invoke.268
- ___64-[HAP2AccessoryServer(Paired) _pollAccessoryOnQueueWithOptions:]_block_invoke_2.272
- ___64-[HAP2AccessoryServerController unpairedIdentifyWithCompletion:]_block_invoke.282
- ___64-[_HAPAccessoryServerBTLE200 securitySession:didCloseWithError:]_block_invoke.1012
- ___65-[HAPAccessoryServerBrowserIP wacBrowser:didFindHAPWACAccessory:]_block_invoke.74
- ___65-[HAPAccessoryServerIP _continuePairingAfterAuthPromptWithRetry:]_block_invoke.474
- ___65-[HAPAccessoryServerIP _httpClientDidCloseConnectionDueToServer:]_block_invoke.428
- ___66-[HAPAccessoryServerBrowserIP _doStartDiscoveringAccessoryServers]_block_invoke
- ___66-[HAPSystemKeychainStore _allAccessoryPairingKeysIncludingHH2Key:]_block_invoke.356
- ___66-[_HAPAccessoryServerBTLE200 _handlePairSetupSessionExchangeData:]_block_invoke.680
- ___67-[HAP2AccessoryServerCoordinator _didDiscoverAccessory:completion:]_block_invoke.13
- ___67-[HAPAccessoryServerBrowserIP wacBrowser:didRemoveHAPWACAccessory:]_block_invoke.75
- ___67-[_HAPAccessoryServerBTLE200 _reallySendRequest:completionHandler:]_block_invoke.779
- ___69-[HAP2AccessoryServer(Paired) _updateAccessoriesWithActivity:reason:]_block_invoke
- ___69-[HAP2AccessoryServer(Paired) _updateAccessoriesWithActivity:reason:]_block_invoke_2
- ___71-[_HAPAccessoryServerBTLE200 _getPairingFeaturesWithCompletionHandler:]_block_invoke.655
- ___72-[HAP2AccessoryServerController _disableAllCharacteristicsNotification:]_block_invoke.332
- ___72-[HAP2AccessoryServerController _disableAllCharacteristicsNotification:]_block_invoke_2.333
- ___74-[HAPAccessoryServerBrowserIP _prePopulateBrowserFromCacheWithCompletion:]_block_invoke
- ___74-[HAPAccessoryServerBrowserIP _prePopulateBrowserFromCacheWithCompletion:]_block_invoke_2
- ___74-[HAPAccessoryServerBrowserIP _prePopulateBrowserFromCacheWithCompletion:]_block_invoke_3
- ___75-[HAP2AccessoryServerController _getPairingsCharacteristicForServer:error:]_block_invoke
- ___75-[HAP2AccessoryServerController _getPairingsCharacteristicForServer:error:]_block_invoke.262
- ___75-[_HAPAccessoryServerBTLE100 peripheral:didUpdateValueForDescriptor:error:]_block_invoke.318
- ___75-[_HAPAccessoryServerBTLE200 addPairing:completionQueue:completionHandler:]_block_invoke.702
- ___75-[_HAPAccessoryServerBTLE200 addPairing:completionQueue:completionHandler:]_block_invoke.709
- ___75-[_HAPAccessoryServerBTLE200 addPairing:completionQueue:completionHandler:]_block_invoke.713
- ___75-[_HAPAccessoryServerBTLE200 addPairing:completionQueue:completionHandler:]_block_invoke_2.717
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.609
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.611
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.610
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.612
- ___76-[HAPSystemKeychainStore allKeychainItemsForType:identifier:syncable:error:]_block_invoke.310
- ___76-[_HAPAccessoryServerBTLE200 _sendRequest:shouldPrioritize:responseHandler:]_block_invoke.770
- ___76-[_HAPAccessoryServerBTLE200 discoverAccessoriesAndReadCharacteristicTypes:]_block_invoke.200
- ___76-[_HAPAccessoryServerBTLE200 discoverAccessoriesAndReadCharacteristicTypes:]_block_invoke_2.204
- ___76-[_HAPAccessoryServerBTLE200 discoverAccessoriesAndReadCharacteristicTypes:]_block_invoke_3.205
- ___77-[HAP2AccessoryServerController _handleAttributeDatabaseResponse:completion:]_block_invoke.200
- ___77-[_HAPAccessoryServerBTLE200 handleDisconnectionWithError:completionHandler:]_block_invoke.843
- ___77-[_HAPAccessoryServerBTLE200 handleDisconnectionWithError:completionHandler:]_block_invoke.848
- ___78-[_HAPAccessoryServerBTLE200 removePairing:completionQueue:completionHandler:]_block_invoke.719
- ___78-[_HAPAccessoryServerBTLE200 removePairing:completionQueue:completionHandler:]_block_invoke.726
- ___78-[_HAPAccessoryServerBTLE200 removePairing:completionQueue:completionHandler:]_block_invoke.730
- ___78-[_HAPAccessoryServerBTLE200 removePairing:completionQueue:completionHandler:]_block_invoke_2.734
- ___79-[HAPAccessoryServerIP _queueListPairingWithCompletionQueue:completionHandler:]_block_invoke.186
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1284
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1285
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1287
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1286
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1288
- ___79-[_HAPAccessoryServerBTLE200 generateBroadcastKey:queue:withCompletionHandler:]_block_invoke.855
- ___80-[HAP2AccessoryServerController _callCharacteristicCompletion:operations:error:]_block_invoke.359
- ___80-[HAP2AccessoryServerController _callCharacteristicCompletion:operations:error:]_block_invoke.361
- ___80-[HAP2AccessoryServerController _callCharacteristicCompletion:operations:error:]_block_invoke.362
- ___80-[_HAPAccessoryServerBTLE200 _generateBroadcastKey:queue:withCompletionHandler:]_block_invoke.865
- ___80-[_HAPAccessoryServerBTLE200 listPairingsWithCompletionQueue:completionHandler:]_block_invoke.737
- ___80-[_HAPAccessoryServerBTLE200 listPairingsWithCompletionQueue:completionHandler:]_block_invoke.738
- ___80-[_HAPAccessoryServerBTLE200 listPairingsWithCompletionQueue:completionHandler:]_block_invoke.745
- ___82-[HAPAccessoryServerHAP2Adapter accessoryServer:doesRequirePermission:completion:]_block_invoke.262
- ___82-[_HAPAccessoryServerBTLE100 removePairingForCurrentControllerOnQueue:completion:]_block_invoke.345
- ___82-[_HAPAccessoryServerBTLE100 removePairingForCurrentControllerOnQueue:completion:]_block_invoke.346
- ___83-[HAPAccessoryServerBrowserIP wacBrowser:didFindUnconfiguredPairedHAPWACAccessory:]_block_invoke.78
- ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.266
- ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.274
- ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.275
- ___84-[_HAPAccessoryServerBTLE200 _configureCharacteristics:queue:withCompletionHandler:]_block_invoke.607
- ___84-[_HAPAccessoryServerBTLE200 _configureCharacteristics:queue:withCompletionHandler:]_block_invoke.608
- ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.340
- ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.344
- ___86-[HAPAccessoryServerIP _establishSecureConnectionAndFetchAttributeDatabaseWithReason:]_block_invoke.160
- ___86-[_HAPAccessoryServerBTLE100 _removePairingWithIdentifier:publicKey:queue:completion:]_block_invoke.344
- ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.276
- ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.277
- ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.278
- ___88-[HAPAccessoryServerIP _queueAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.185
- ___88-[HAPAccessoryServerIP _startAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.584
- ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.210
- ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.215
- ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.224
- ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.234
- ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.235
- ___89-[_HAPAccessoryServerBTLE100 _addPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.334
- ___90-[HAP2AccessoryServerController enableNotificationsForCharacteristics:options:completion:]_block_invoke.226
- ___90-[HAP2AccessoryServerController enableNotificationsForCharacteristics:options:completion:]_block_invoke.228
- ___90-[HAP2AccessoryServerController enableNotificationsForCharacteristics:options:completion:]_block_invoke.243
- ___90-[HAP2AccessoryServerController enableNotificationsForCharacteristics:options:completion:]_block_invoke.248
- ___90-[HAP2AccessoryServerController enableNotificationsForCharacteristics:options:completion:]_block_invoke_2.249
- ___90-[HAP2AccessoryServerController writeValuesForCharacteristics:timeout:options:completion:]_block_invoke.224
- ___90-[HAPAccessoryServerIP _queueEnableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.187
- ___90-[HAPAccessoryServerIP _writeCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.254
- ___91-[HAP2AccessoryServerController disableNotificationsForCharacteristics:options:completion:]_block_invoke.250
- ___91-[HAP2AccessoryServerController disableNotificationsForCharacteristics:options:completion:]_block_invoke.255
- ___93-[HAPAccessoryServerHAP2Adapter enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.189
- ___94-[HAP2AccessoryServerController _createOperationsToReadCharacteristics:timeout:options:error:]_block_invoke.219
- ___94-[HAPAccessoryServerHAP2Adapter _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.197
- ___94-[HAPAccessoryServerHAP2Adapter _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke_2.198
- ___97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke.239
- ___97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke_2.240
- ___97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke_3.241
- ___99-[HAPAccessoryServerIP writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.253
- ___Block_byref_object_copy_.10715
- ___Block_byref_object_copy_.11014
- ___Block_byref_object_copy_.11832
- ___Block_byref_object_copy_.12029
- ___Block_byref_object_copy_.13030
- ___Block_byref_object_copy_.13791
- ___Block_byref_object_copy_.14018
- ___Block_byref_object_copy_.15147
- ___Block_byref_object_copy_.17367
- ___Block_byref_object_copy_.17588
- ___Block_byref_object_copy_.18569
- ___Block_byref_object_copy_.19150
- ___Block_byref_object_copy_.20254
- ___Block_byref_object_copy_.2091
- ___Block_byref_object_copy_.21062
- ___Block_byref_object_copy_.25217
- ___Block_byref_object_copy_.25383
- ___Block_byref_object_copy_.2760
- ___Block_byref_object_copy_.374
- ___Block_byref_object_copy_.4312
- ___Block_byref_object_copy_.5199
- ___Block_byref_object_copy_.5458
- ___Block_byref_object_copy_.5918
- ___Block_byref_object_copy_.6548
- ___Block_byref_object_copy_.6728
- ___Block_byref_object_copy_.742
- ___Block_byref_object_copy_.7549
- ___Block_byref_object_copy_.9116
- ___Block_byref_object_copy_.9439
- ___Block_byref_object_copy_.9643
- ___Block_byref_object_dispose_.10716
- ___Block_byref_object_dispose_.11015
- ___Block_byref_object_dispose_.11833
- ___Block_byref_object_dispose_.12030
- ___Block_byref_object_dispose_.13031
- ___Block_byref_object_dispose_.13792
- ___Block_byref_object_dispose_.14019
- ___Block_byref_object_dispose_.15148
- ___Block_byref_object_dispose_.17368
- ___Block_byref_object_dispose_.17589
- ___Block_byref_object_dispose_.18570
- ___Block_byref_object_dispose_.19151
- ___Block_byref_object_dispose_.20255
- ___Block_byref_object_dispose_.2092
- ___Block_byref_object_dispose_.21063
- ___Block_byref_object_dispose_.25218
- ___Block_byref_object_dispose_.25384
- ___Block_byref_object_dispose_.2761
- ___Block_byref_object_dispose_.375
- ___Block_byref_object_dispose_.4313
- ___Block_byref_object_dispose_.5200
- ___Block_byref_object_dispose_.5459
- ___Block_byref_object_dispose_.5919
- ___Block_byref_object_dispose_.6549
- ___Block_byref_object_dispose_.6729
- ___Block_byref_object_dispose_.743
- ___Block_byref_object_dispose_.7550
- ___Block_byref_object_dispose_.9117
- ___Block_byref_object_dispose_.9440
- ___Block_byref_object_dispose_.9644
- ___block_descriptor_40_e8_32s_e56_v32?0"NSString"8"HAPAccessoryServerIPCacheData"16^B24ls32l8
- ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls40l8s32l8
- ___block_descriptor_56_e8_32s40bs48w_e17_v16?0"NSError"8lw48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40bs48w_e23_"<HAP2Cancelable>"8?0lw48l8s40l8s32l8
- ___block_descriptor_56_e8_32s40r48w_e5_v8?0lw48l8r40l8s32l8
- ___block_descriptor_64_e8_32s40s48bs56w_e17_v16?0"NSError"8lw56l8s32l8s48l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e40_v24?0"HAPPairingIdentity"8"NSError"16ls32l8s56l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56s_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8s56l8
- ___block_literal_global.1021
- ___block_literal_global.10389
- ___block_literal_global.11076
- ___block_literal_global.11828
- ___block_literal_global.12200
- ___block_literal_global.1304
- ___block_literal_global.13329
- ___block_literal_global.1341
- ___block_literal_global.14960
- ___block_literal_global.1513
- ___block_literal_global.15271
- ___block_literal_global.15703
- ___block_literal_global.17028
- ___block_literal_global.17377
- ___block_literal_global.18724
- ___block_literal_global.194
- ___block_literal_global.1996
- ___block_literal_global.19996
- ___block_literal_global.20276
- ___block_literal_global.203
- ___block_literal_global.20730
- ___block_literal_global.21687
- ___block_literal_global.219
- ___block_literal_global.223
- ___block_literal_global.226
- ___block_literal_global.23068
- ___block_literal_global.233
- ___block_literal_global.23404
- ___block_literal_global.242
- ___block_literal_global.24991
- ___block_literal_global.25603
- ___block_literal_global.260
- ___block_literal_global.2825
- ___block_literal_global.306
- ___block_literal_global.374
- ___block_literal_global.376
- ___block_literal_global.3774
- ___block_literal_global.378
- ___block_literal_global.380
- ___block_literal_global.382
- ___block_literal_global.384
- ___block_literal_global.386.7620
- ___block_literal_global.5279
- ___block_literal_global.5454
- ___block_literal_global.6016
- ___block_literal_global.6560
- ___block_literal_global.6705
- ___block_literal_global.7860
- ___block_literal_global.800
- ___block_literal_global.836
- ___block_literal_global.8791
- ___block_literal_global.9208
- ___block_literal_global.9757
- _hkConfig.21671
- _logCategory._hmf_once_t2
- _logCategory._hmf_once_t333
- _logCategory._hmf_once_t37
- _logCategory._hmf_once_t432
- _logCategory._hmf_once_t49
- _logCategory._hmf_once_t55
- _logCategory._hmf_once_t93
- _logCategory._hmf_once_v3
- _logCategory._hmf_once_v334
- _logCategory._hmf_once_v38
- _logCategory._hmf_once_v433
- _logCategory._hmf_once_v50
- _logCategory._hmf_once_v56
- _logCategory._hmf_once_v94
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_doStartDiscoveringAccessoryServers
- _objc_msgSend$_prePopulateBrowserFromCacheWithCompletion:
- _objc_msgSend$_updateCacheForDevice:socketInfo:bonjour:
- _objc_msgSend$cache
- _objc_msgSend$deleteDataForDevice:
- _objc_msgSend$dictionaryRepresentation
- _objc_msgSend$initWithCachedIp:bonjourRecord:
- _objc_msgSend$initWithDictionary:
- _objc_msgSend$isInitialCacheRestored
- _objc_msgSend$retrieveCachedData:
- _objc_msgSend$saveData:forDevice:
- _objc_msgSend$setIsInitialCacheRestored:
- _objc_msgSend$socketInfo
- _objc_msgSend$systemStore
- _objc_msgSend$updateCacheForDeviceID:ipData:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
- _sharedInstance.onceToken.15702
- _systemStore.systemStore
- _systemStore.systemStoreAllocated
CStrings:
+ "!A"
+ "%@ Accessory server discovered accessories of a removed accessory server - moving on enabling removed key"
+ "%@ Accessory server failed to discover accessories of a removed accessory server with error: %@"
+ "%@ Accessory server prepared removed accessory key with error: %@"
+ "%@ Cannot call add pairing on an unpaired accessory"
+ "%@ Cannot call list pairings on an unpaired accessory"
+ "%@ Ignoring updateAccessories request with reason=%{public}@ one already running"
+ "%@ Removed accessory server does not own unpaired server"
+ "%@ Removed accessory server requested to discover accessories"
+ "%s/%ld"
+ "%{public}@Bonjour has already added, continuing with pairing."
+ "%{public}@Cannot establish session to list pairings without accessory key: %@"
+ "%{public}@Cloned removed accessory key %@ with error %u"
+ "%{public}@Could not retrieve controller identity to determine which pairing to remove last from accessory - it might fail to remove all pairings from removed accessory completely"
+ "%{public}@Discovered accessories of a removed accessory server - moving on enabling removed key"
+ "%{public}@Enabled removed accessory key with error: %@"
+ "%{public}@Error in establishing secure session, failing list pairings block with %@"
+ "%{public}@Existing HH2 pairing key is potentially compromised. Creating a new HH2 pairing key."
+ "%{public}@Failed to discover accessories of a removed accessory server with error: %@"
+ "%{public}@Failed to initiate refresh scan: %d"
+ "%{public}@Found fresh scan result for SSID: %@"
+ "%{public}@IP Accessory server %@ matches setupID %{public}@ and is paired/hasPairings/wasRemoved: (%{public}@/%{public}@/%{public}@)"
+ "%{public}@IP Accessory server %@ matches setupID %{public}@ but was removed, so allow pairing to continue"
+ "%{public}@Invalid number of keychain items(%tu) for removed accessory '%@'"
+ "%{public}@No IDS Date provider to set time for cloned removed accessory key"
+ "%{public}@Not reading removed accessory key as feature is disabled"
+ "%{public}@Not starting reachability poll for unpaired accessory"
+ "%{public}@Refresh scan failed with status: %d"
+ "%{public}@Refresh scan returned no results for SSID: %@"
+ "%{public}@Refreshing scan result for SSID: %@"
+ "%{public}@Removed accessory discovery completed with error: %@"
+ "%{public}@Removed accessory key not cloned as feature is disabled"
+ "%{public}@Retrieving removed accessoy key for identifier: %@"
+ "%{public}@Returning local pairing identity for pair setup session: %@"
+ "%{public}@Returning local pairing identity for security session: %@"
+ "%{public}@SSID %@ not found in %lu scan results"
+ "%{public}@Scan result is stale (time since last scan: %.1fs), refreshing"
+ "%{public}@Scan result is stale (time since last scan: %.1fs), refreshing before join"
+ "%{public}@Step value adjustment: %.2f -> %.2f (min=%.2f, step=%.2f) for characteristic %@/%@"
+ "%{public}@Treating OSStatus as Generic error: %@"
+ "%{public}@Using existing network info (time since last scan: %.1fs)"
+ "%{public}@Using existing scan result for join (time since last scan: %.1fs)"
+ "%{public}@Using fresh scan result for join"
+ "%{public}@listPairingsOfRemovedAccessory failed with no error"
+ "%{public}@refreshScanResultForSSID called completion after self had been destroyed"
+ "/Library/Caches/com.apple.xbs/18652000-8B39-4326-A300-B98DEAA6F05D/TemporaryDirectory.8myVbR/Sources/HomeKit/Sources/CoreHAP/Accessories/HAPSuspendedAccessory.m"
+ "/Library/Caches/com.apple.xbs/18652000-8B39-4326-A300-B98DEAA6F05D/TemporaryDirectory.8myVbR/Sources/HomeKit/Sources/CoreHAP/HAP2/HAPAdapter/HAPAccessoryServerHAP2Adapter.m"
+ "/Library/Caches/com.apple.xbs/18652000-8B39-4326-A300-B98DEAA6F05D/TemporaryDirectory.8myVbR/Sources/HomeKit/Sources/CoreHAP/HAP2/Pairing/HAP2AccessoryServerPairingDriver.m"
+ "/Library/Caches/com.apple.xbs/18652000-8B39-4326-A300-B98DEAA6F05D/TemporaryDirectory.8myVbR/Sources/HomeKit/Sources/CoreHAP/HAPHTTPClient.m"
+ "/Library/Caches/com.apple.xbs/18652000-8B39-4326-A300-B98DEAA6F05D/TemporaryDirectory.8myVbR/Sources/HomeKit/Sources/CoreHAP/Servers/HAPAccessoryServerIP.m"
+ "/Library/Caches/com.apple.xbs/18652000-8B39-4326-A300-B98DEAA6F05D/TemporaryDirectory.8myVbR/Sources/HomeKit/Sources/CoreHAP/Servers/_HAPAccessoryServerBTLE200.m"
+ "<HAPAudioCodecBitDepthWrapper value=%@>"
+ "<HAPAudioStreamTier identifier=%@, targetAverageBitrate=%@, sampleRate=%@, bitDepth=%@, packetTime=%@, numberOfChannels=%@>"
+ "<HAPCameraBufferEvent sequenceNumber=%@, type=%@, CMAFSessionStart=%@, CMAFSessionStop=%@, motion=%@>"
+ "<HAPCameraBufferEventCMAFSessionStart CMAFSessionID=%@>"
+ "<HAPCameraBufferEventCMAFSessionStop CMAFSessionID=%@>"
+ "<HAPCameraBufferEventCommandRequest command=%@, sequenceNumber=%@, limit=%@>"
+ "<HAPCameraBufferEventCommandResponse events=%@>"
+ "<HAPCameraBufferEventCommandTypeWrapper value=%@>"
+ "<HAPCameraBufferEventMotion active=%@>"
+ "<HAPCameraBufferEventTypeWrapper value=%@>"
+ "<HAPCameraBufferInfo identifier=%@, type=%@, intervals=%@>"
+ "<HAPCameraBufferInfoResponse version=%@, buffers=%@>"
+ "<HAPCameraBufferInterval sequenceNumber=%@, count=%@>"
+ "<HAPCameraBufferTypeWrapper value=%@>"
+ "<HAPCameraBufferUploadCommandRequest sessionID=%@, command=%@, start=%@, stop=%@, stopAction=%@>"
+ "<HAPCameraBufferUploadCommandResponse clipID=%@>"
+ "<HAPCameraBufferUploadCommandTypeWrapper value=%@>"
+ "<HAPCameraBufferUploadStopActionWrapper value=%@>"
+ "<HAPCameraCapabilitiesResponse version=%@, videoStreamCapabilities=%@, cameraSensors=%@>"
+ "<HAPCameraClientCSR CSR=%@>"
+ "<HAPCameraClientCertificate clientCertificate=%@, CA=%@>"
+ "<HAPCameraClientCertificateStatus needsUpdate=%@>"
+ "<HAPCameraKey key=%@, keyNumber=%@>"
+ "<HAPCameraKeyID keyID=%@>"
+ "<HAPCameraRecordingPublishingPoint URL=%@, serverCertificate=%@>"
+ "<HAPCameraSensors cameraSensors=%@>"
+ "<HAPCameraVideoQualityWrapper value=%@>"
+ "<HAPCameraVideoStreamCapabilities identifier=%@, quality=%@, width=%@, height=%@, framesPerSecond=%@, averageBitrate=%@, peakBitrate=%@>"
+ "<HAPCameraZones zoneDataVersion=%@, zoneData=%@>"
+ "<HAPPolygon identifier=%@, count=%@, vertices=%@>"
+ "<HAPRTPStreamingControlCommandWrapper value=%@>"
+ "<HAPRTPStreamingControlRequest sessionIdentifier=%@, command=%@, videoTier=%@, videoSSRC=%@, audioTier=%@, audioSSRC=%@>"
+ "<HAPRTPStreamingControlResponse sessionIdentifier=%@, status=%@>"
+ "<HAPRTPStreamingControlStatusWrapper value=%@>"
+ "<HAPSensorConfiguration sensorDimensions=%@>"
+ "<HAPSensorDimensions width=%@, height=%@>"
+ "<HAPSupportedAudioStreamTiers codec=%@, payloadType=%@, tiers=%@>"
+ "<HAPSupportedVideoStreamTiers codec=%@, payloadType=%@, tiers=%@>"
+ "<HAPVideoCodecTypeWrapper value=%@>"
+ "<HAPVideoStreamTier identifier=%@, quality=%@, targetAverageBitrate=%@, width=%@, height=%@, frameRate=%@>"
+ "<HAPWebRTCICECandidate candidate=%@, SDPMid=%@, SDPMLineIndex=%@>"
+ "<HAPWebRTCOfferStatusWrapper value=%@>"
+ "<HAPWebRTCProvideAnswerRequest sessionIdentifier=%@, SDPAnswer=%@, additionalCandidates=%@>"
+ "<HAPWebRTCReofferRequest sessionIdentifier=%@, SDPOffer=%@, SFrameConfiguration=%@>"
+ "<HAPWebRTCReofferResponse sessionIdentifier=%@, SDPAnswer=%@, status=%@>"
+ "<HAPWebRTCSFrameConfiguration audioCipherSuite=%@, videoCipherSuite=%@, baseKey=%@, keyID=%@, ratchetBits=%@, ratchetTime=%@>"
+ "<HAPWebRTCSolicitOfferRequest SFrameConfiguration=%@>"
+ "<HAPWebRTCSolicitOfferResponse sessionIdentifier=%@, SDPOffer=%@, additionalCandidates=%@, status=%@, KID=%@>"
+ "<HAPWebRTCStreamingControlRequest sessionIdentifier=%@>"
+ "<HAPWebRTCStreamingControlResponse sessionIdentifier=%@, status=%@>"
+ "<HAPWebRTCStreamingControlStatusWrapper value=%@>"
+ "<HAPWebRTCStreamingStatusWrapper value=%@>"
+ "<HAPZoneDataV2 inverted=%@, count=%@, polygons=%@>"
+ "@\"<HAP2Cancelable>\"24@0:8q16"
+ "@\"<HAP2Cancelable>\"32@0:8@\"NSData\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "@\"<HAP2Cancelable>\"40@0:8@\"HAPPairingIdentity\"16@\"NSData\"24@?<v@?@\"NSError\">32"
+ "@\"<HAP2Cancelable>\"40@0:8q16@\"NSData\"24@?<v@?@\"NSError\">32"
+ "@\"<HAPSystemKeychainStoreDataSource>\""
+ "@\"HAPAudioCodecBitDepthWrapper\""
+ "@\"HAPCameraBufferEventCMAFSessionStart\""
+ "@\"HAPCameraBufferEventCMAFSessionStop\""
+ "@\"HAPCameraBufferEventCommandTypeWrapper\""
+ "@\"HAPCameraBufferEventMotion\""
+ "@\"HAPCameraBufferEventTypeWrapper\""
+ "@\"HAPCameraBufferTypeWrapper\""
+ "@\"HAPCameraBufferUploadCommandTypeWrapper\""
+ "@\"HAPCameraBufferUploadStopActionWrapper\""
+ "@\"HAPCameraSensors\""
+ "@\"HAPCameraVideoQualityWrapper\""
+ "@\"HAPKeychainItem\"24@0:8@\"NSString\"16"
+ "@\"HAPRTPStreamingControlCommandWrapper\""
+ "@\"HAPRTPStreamingControlStatusWrapper\""
+ "@\"HAPSensorDimensions\""
+ "@\"HAPVideoCodecTypeWrapper\""
+ "@\"HAPWebRTCOfferStatusWrapper\""
+ "@\"HAPWebRTCStreamingControlStatusWrapper\""
+ "@\"HAPWebRTCStreamingStatusWrapper\""
+ "@\"NSArray\"24@0:8@\"NSDictionary\"16"
+ "@\"NSData\"40@0:8@\"NSString\"16@\"NSString\"24^@32"
+ "@28@0:8q16i24"
+ "@32@0:8^{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}16^{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}24"
+ "@40@0:8q16@24@?32"
+ "@64@0:8@16@24Q32q40@48@56"
+ "Accessory server died when removed accessories are discovered"
+ "B32@0:8d16^@24"
+ "B32@0:8r^{sockaddr=CC[14c]}16@24"
+ "CA"
+ "CMAFSessionID"
+ "CMAFSessionStart"
+ "CMAFSessionStop"
+ "CSR"
+ "Cannot remove pairing if not paired"
+ "DataStream"
+ "HAP2ThreadNetworkUtil"
+ "HAPAudioCodecBitDepth16"
+ "HAPAudioCodecBitDepth24"
+ "HAPAudioCodecBitDepth8"
+ "HAPAudioCodecBitDepthWrapper"
+ "HAPAudioCodecSampleRate32kHz"
+ "HAPAudioCodecSampleRate48kHz"
+ "HAPAudioStreamTier"
+ "HAPCameraBufferEvent"
+ "HAPCameraBufferEventCMAFSessionStart"
+ "HAPCameraBufferEventCMAFSessionStop"
+ "HAPCameraBufferEventCommandRequest"
+ "HAPCameraBufferEventCommandResponse"
+ "HAPCameraBufferEventCommandTypeAcknowledge"
+ "HAPCameraBufferEventCommandTypeQuery"
+ "HAPCameraBufferEventCommandTypeWrapper"
+ "HAPCameraBufferEventMotion"
+ "HAPCameraBufferEventTypeCMAFSessionStart"
+ "HAPCameraBufferEventTypeCMAFSessionStop"
+ "HAPCameraBufferEventTypeMotion"
+ "HAPCameraBufferEventTypeWrapper"
+ "HAPCameraBufferInfo"
+ "HAPCameraBufferInfoResponse"
+ "HAPCameraBufferInterval"
+ "HAPCameraBufferTypeAudio"
+ "HAPCameraBufferTypeMetadata"
+ "HAPCameraBufferTypeVideo"
+ "HAPCameraBufferTypeWrapper"
+ "HAPCameraBufferUploadCommandRequest"
+ "HAPCameraBufferUploadCommandResponse"
+ "HAPCameraBufferUploadCommandTypeStart"
+ "HAPCameraBufferUploadCommandTypeStartAndStop"
+ "HAPCameraBufferUploadCommandTypeStop"
+ "HAPCameraBufferUploadCommandTypeWrapper"
+ "HAPCameraBufferUploadStopActionFinalize"
+ "HAPCameraBufferUploadStopActionPause"
+ "HAPCameraBufferUploadStopActionWrapper"
+ "HAPCameraCapabilitiesResponse"
+ "HAPCameraClientCSR"
+ "HAPCameraClientCertificate"
+ "HAPCameraClientCertificateStatus"
+ "HAPCameraKey"
+ "HAPCameraKeyID"
+ "HAPCameraRecordingPublishingPoint"
+ "HAPCameraSensors"
+ "HAPCameraVideoQualityHigh"
+ "HAPCameraVideoQualityHighest"
+ "HAPCameraVideoQualityLow"
+ "HAPCameraVideoQualityMedium"
+ "HAPCameraVideoQualityTimeLapse"
+ "HAPCameraVideoQualityWrapper"
+ "HAPCameraVideoStreamCapabilities"
+ "HAPCameraZones"
+ "HAPPolygon"
+ "HAPRTPStreamingControlCommandEnd"
+ "HAPRTPStreamingControlCommandStart"
+ "HAPRTPStreamingControlCommandWrapper"
+ "HAPRTPStreamingControlRequest"
+ "HAPRTPStreamingControlResponse"
+ "HAPRTPStreamingControlStatusBusy"
+ "HAPRTPStreamingControlStatusError"
+ "HAPRTPStreamingControlStatusNoSuchStream"
+ "HAPRTPStreamingControlStatusSuccess"
+ "HAPRTPStreamingControlStatusUnknownSessionIdentifier"
+ "HAPRTPStreamingControlStatusWrapper"
+ "HAPSensorConfiguration"
+ "HAPSensorDimensions"
+ "HAPSupportedAudioStreamTiers"
+ "HAPSupportedVideoStreamTiers"
+ "HAPSystemKeychainStoreDataSource"
+ "HAPSystemKeychainStoreDefaultDataSource"
+ "HAPVideoCodecTypeH_264"
+ "HAPVideoCodecTypeH_265"
+ "HAPVideoCodecTypeWrapper"
+ "HAPVideoStreamTier"
+ "HAPWebRTCICECandidate"
+ "HAPWebRTCOfferStatusError"
+ "HAPWebRTCOfferStatusPrivacyModeActive"
+ "HAPWebRTCOfferStatusSuccess"
+ "HAPWebRTCOfferStatusWrapper"
+ "HAPWebRTCProvideAnswerRequest"
+ "HAPWebRTCReofferRequest"
+ "HAPWebRTCReofferResponse"
+ "HAPWebRTCSFrameConfiguration"
+ "HAPWebRTCSolicitOfferRequest"
+ "HAPWebRTCSolicitOfferResponse"
+ "HAPWebRTCStreamingControlRequest"
+ "HAPWebRTCStreamingControlResponse"
+ "HAPWebRTCStreamingControlStatusBusy"
+ "HAPWebRTCStreamingControlStatusError"
+ "HAPWebRTCStreamingControlStatusSuccess"
+ "HAPWebRTCStreamingControlStatusUnknownSessionIdentifier"
+ "HAPWebRTCStreamingControlStatusWrapper"
+ "HAPWebRTCStreamingStatusBusy"
+ "HAPWebRTCStreamingStatusError"
+ "HAPWebRTCStreamingStatusSuccess"
+ "HAPWebRTCStreamingStatusUnknownSessionIdentifier"
+ "HAPWebRTCStreamingStatusWrapper"
+ "HAPZoneDataV2"
+ "HH2KeyRoll"
+ "KID"
+ "Keepalive"
+ "Removed HomeKit Accessory"
+ "Removed HomeKit Accessory which used to be paired with this account."
+ "Removed accessory server died when updating accessories"
+ "RemovedAccessoryKey"
+ "SDPAnswer"
+ "SDPMLineIndex"
+ "SDPMid"
+ "SDPOffer"
+ "SFrameConfiguration"
+ "Secure Transport: Opening standard security session"
+ "T@\"<HAPKeyStore>\",R"
+ "T@\"<HAPSystemKeyCountProvider>\",R"
+ "T@\"<HAPSystemKeychainStore>\",R"
+ "T@\"<HAPSystemKeychainStoreDataSource>\",R,N,V_dataSource"
+ "T@\"HAPAudioCodecBitDepthWrapper\",&,N,V_bitDepth"
+ "T@\"HAPAudioCodecTypeWrapper\",&,N,V_codec"
+ "T@\"HAPCameraBufferEventCMAFSessionStart\",&,N,V_CMAFSessionStart"
+ "T@\"HAPCameraBufferEventCMAFSessionStop\",&,N,V_CMAFSessionStop"
+ "T@\"HAPCameraBufferEventCommandTypeWrapper\",&,N,V_command"
+ "T@\"HAPCameraBufferEventMotion\",&,N,V_motion"
+ "T@\"HAPCameraBufferEventTypeWrapper\",&,N,V_type"
+ "T@\"HAPCameraBufferTypeWrapper\",&,N,V_type"
+ "T@\"HAPCameraBufferUploadCommandTypeWrapper\",&,N,V_command"
+ "T@\"HAPCameraBufferUploadStopActionWrapper\",&,N,V_stopAction"
+ "T@\"HAPCameraSensors\",&,N,V_cameraSensors"
+ "T@\"HAPCameraVideoQualityWrapper\",&,N,V_quality"
+ "T@\"HAPRTPStreamingControlCommandWrapper\",&,N,V_command"
+ "T@\"HAPRTPStreamingControlStatusWrapper\",&,N,V_status"
+ "T@\"HAPSensorDimensions\",&,N,V_sensorDimensions"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_CMAFSessionID"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_SDPMLineIndex"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_active"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_audioCipherSuite"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_audioSSRC"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_audioTier"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_averageBitrate"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_clipID"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_count"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_frameRate"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_framesPerSecond"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_height"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_inverted"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_keyID"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_keyNumber"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_limit"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_needsUpdate"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_numberOfChannels"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_payloadType"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_peakBitrate"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_ratchetBits"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_ratchetTime"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_sequenceNumber"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_sessionID"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_start"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_stop"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_targetAverageBitrate"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_version"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_videoCipherSuite"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_videoSSRC"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_videoTier"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_width"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_zoneDataVersion"
+ "T@\"HAPVideoCodecTypeWrapper\",&,N,V_codec"
+ "T@\"HAPWebRTCOfferStatusWrapper\",&,N,V_status"
+ "T@\"HAPWebRTCStreamingControlStatusWrapper\",&,N,V_status"
+ "T@\"HAPWebRTCStreamingStatusWrapper\",&,N,V_status"
+ "T@\"NSData\",&"
+ "T@\"NSData\",&,N,V_CA"
+ "T@\"NSData\",&,N,V_CSR"
+ "T@\"NSData\",&,N,V_KID"
+ "T@\"NSData\",&,N,V_SDPAnswer"
+ "T@\"NSData\",&,N,V_SDPMid"
+ "T@\"NSData\",&,N,V_SDPOffer"
+ "T@\"NSData\",&,N,V_baseKey"
+ "T@\"NSData\",&,N,V_candidate"
+ "T@\"NSData\",&,N,V_clientCertificate"
+ "T@\"NSData\",&,N,V_keyID"
+ "T@\"NSData\",&,N,V_serverCertificate"
+ "T@\"NSData\",&,N,V_sessionIdentifier"
+ "T@\"NSData\",&,N,V_vertices"
+ "T@\"NSData\",&,N,V_zoneData"
+ "T@\"NSData\",&,V_removedAccessoryKey"
+ "T@\"NSMutableArray\",&,N,V_SFrameConfiguration"
+ "T@\"NSMutableArray\",&,N,V_additionalCandidates"
+ "T@\"NSMutableArray\",&,N,V_buffers"
+ "T@\"NSMutableArray\",&,N,V_cameraSensors"
+ "T@\"NSMutableArray\",&,N,V_events"
+ "T@\"NSMutableArray\",&,N,V_intervals"
+ "T@\"NSMutableArray\",&,N,V_polygons"
+ "T@\"NSMutableArray\",&,N,V_tiers"
+ "T@\"NSMutableArray\",&,N,V_videoStreamCapabilities"
+ "T@\"NSMutableArray\",R,N,V_removedAccessoryDiscoveryCompletionHandlers"
+ "T@\"NSMutableSet\",&,N,V_removedAccessoryIdentifiers"
+ "T@\"NSString\",&,N,V_URL"
+ "T@\"NSString\",C,N,V_refreshingScanSSID"
+ "T@?,C,N,V_refreshScanCompletion"
+ "TB,?,R,N"
+ "TB,N,V_pendingBonjourAdd"
+ "TB,R,GisHH2KeyRollEnabled"
+ "Td,N,V_lastScanUptime"
+ "The delegate is missing"
+ "Tq,N,V_metric_pairVerifyReason"
+ "Tq,N,V_reachabilityChangedReason"
+ "Tq,R,N"
+ "Tq,R,N,V_reason"
+ "URL"
+ "Undefined"
+ "Unknown HAPAudioCodecBitDepth %ld"
+ "Unknown HAPCameraBufferEventCommandType %ld"
+ "Unknown HAPCameraBufferEventType %ld"
+ "Unknown HAPCameraBufferType %ld"
+ "Unknown HAPCameraBufferUploadCommandType %ld"
+ "Unknown HAPCameraBufferUploadStopAction %ld"
+ "Unknown HAPCameraVideoQuality %ld"
+ "Unknown HAPRTPStreamingControlCommand %ld"
+ "Unknown HAPRTPStreamingControlStatus %ld"
+ "Unknown HAPVideoCodecType %ld"
+ "Unknown HAPWebRTCOfferStatus %ld"
+ "Unknown HAPWebRTCStreamingControlStatus %ld"
+ "Unknown HAPWebRTCStreamingStatus %ld"
+ "_CA"
+ "_CMAFSessionID"
+ "_CMAFSessionStart"
+ "_CMAFSessionStop"
+ "_CSR"
+ "_KID"
+ "_SDPAnswer"
+ "_SDPMLineIndex"
+ "_SDPMid"
+ "_SDPOffer"
+ "_SFrameConfiguration"
+ "_URL"
+ "_active"
+ "_additionalCandidates"
+ "_addressToCIDR:withNetmask:"
+ "_audioCipherSuite"
+ "_audioSSRC"
+ "_audioTier"
+ "_averageBitrate"
+ "_baseKey"
+ "_bitDepth"
+ "_buffers"
+ "_cameraSensors"
+ "_candidate"
+ "_clientCertificate"
+ "_clipID"
+ "_codec"
+ "_completeRefreshScanWithResult:"
+ "_count"
+ "_createStandardSecuritySession"
+ "_dataSource"
+ "_establishSecureSessionAndListPairings:queue:completion:"
+ "_establishSecureSessionAndListPairingsWithCompletionQueue:completion:"
+ "_events"
+ "_frameRate"
+ "_framesPerSecond"
+ "_handleRefreshScanResults:status:"
+ "_height"
+ "_interface:hasAddressesWithPrefix:"
+ "_intervals"
+ "_inverted"
+ "_keyID"
+ "_keyNumber"
+ "_lastScanUptime"
+ "_limit"
+ "_motion"
+ "_needsUpdate"
+ "_newLowestUUIDUsernameForHH2ControllerKey"
+ "_numberOfChannels"
+ "_payloadType"
+ "_peakBitrate"
+ "_pendingBonjourAdd"
+ "_performWiFiJoinWithScanResult:completion:"
+ "_polygons"
+ "_preferredHH2ControllerKey"
+ "_quality"
+ "_ratchetBits"
+ "_ratchetTime"
+ "_refreshScanCompletion"
+ "_refreshScanResultForSSID:completion:"
+ "_refreshingScanSSID"
+ "_removedAccessoryDiscoveryCompletionHandlers"
+ "_removedAccessoryIdentifiers"
+ "_removedAccessoryKey"
+ "_restoreNetworkWithNetworkInfo:completion:"
+ "_sendListPairingsWithData:queue:completion:"
+ "_sensorDimensions"
+ "_sequenceNumber"
+ "_serverCertificate"
+ "_sessionID"
+ "_sharedThreadClient"
+ "_start"
+ "_stopAction"
+ "_systemKeychainStoreSingleton"
+ "_targetAverageBitrate"
+ "_tiers"
+ "_updateServerMetadata:controller:"
+ "_vertices"
+ "_videoCipherSuite"
+ "_videoSSRC"
+ "_videoStreamCapabilities"
+ "_videoTier"
+ "_width"
+ "_zoneData"
+ "_zoneDataVersion"
+ "active"
+ "additionalCandidates"
+ "allowsRemovedAccessoryKeys"
+ "audioCipherSuite"
+ "audioSSRC"
+ "audioTier"
+ "averageBitrate"
+ "baseKey"
+ "bitDepth"
+ "buffers"
+ "cameraSensors"
+ "candidate"
+ "clearRemovedAccessoryKeysPriorToTime:error:"
+ "clearRemovedFromHome:"
+ "clientCertificate"
+ "clipID"
+ "cloneRemovedAccessoryKeyForName:iCloudIdentifier:error:"
+ "codec"
+ "creationTime"
+ "dataSource"
+ "deleteRemovedAccessoryKeyForName:error:"
+ "discoverRemovedAccessoriesWithCompletion:"
+ "enableRemovedAccessoryKey:completionQueue:completion:"
+ "events"
+ "frameRate"
+ "framesPerSecond"
+ "getCurrentNetworkInterfaces"
+ "getPairingsWithRemovedAccessoryKey:completion:"
+ "hapErrorWithCode:OSStatus:"
+ "hapR"
+ "height"
+ "hh2KeyRollEnabled"
+ "hh2KeychainItemWithIdentifier:"
+ "homeutil"
+ "iCloudID"
+ "initWithActive:"
+ "initWithAudioCipherSuite:videoCipherSuite:baseKey:keyID:ratchetBits:ratchetTime:"
+ "initWithCMAFSessionID:"
+ "initWithCSR:"
+ "initWithCameraSensors:"
+ "initWithCandidate:SDPMid:SDPMLineIndex:"
+ "initWithClientCertificate:CA:"
+ "initWithClipID:"
+ "initWithCodec:payloadType:tiers:"
+ "initWithCommand:sequenceNumber:limit:"
+ "initWithDataSource:"
+ "initWithEvents:"
+ "initWithIdentifier:count:vertices:"
+ "initWithIdentifier:quality:targetAverageBitrate:width:height:frameRate:"
+ "initWithIdentifier:quality:width:height:framesPerSecond:averageBitrate:peakBitrate:"
+ "initWithIdentifier:targetAverageBitrate:sampleRate:bitDepth:packetTime:numberOfChannels:"
+ "initWithIdentifier:type:intervals:"
+ "initWithInverted:count:polygons:"
+ "initWithKey:keyNumber:"
+ "initWithKeyID:"
+ "initWithNeedsUpdate:"
+ "initWithSFrameConfiguration:"
+ "initWithSensorDimensions:"
+ "initWithSequenceNumber:count:"
+ "initWithSequenceNumber:type:CMAFSessionStart:CMAFSessionStop:motion:"
+ "initWithSessionID:command:start:stop:stopAction:"
+ "initWithSessionIdentifier:"
+ "initWithSessionIdentifier:SDPAnswer:additionalCandidates:"
+ "initWithSessionIdentifier:SDPAnswer:status:"
+ "initWithSessionIdentifier:SDPOffer:SFrameConfiguration:"
+ "initWithSessionIdentifier:SDPOffer:additionalCandidates:status:KID:"
+ "initWithSessionIdentifier:command:videoTier:videoSSRC:audioTier:audioSSRC:"
+ "initWithSessionIdentifier:status:"
+ "initWithURL:serverCertificate:"
+ "initWithVersion:buffers:"
+ "initWithVersion:videoStreamCapabilities:cameraSensors:"
+ "initWithWidth:height:"
+ "initWithZoneDataVersion:zoneData:"
+ "intervals"
+ "inverted"
+ "isAddress:inNetwork:"
+ "isHH2KeyRollEnabled"
+ "isThreadIPv6Address:fromInterfaces:"
+ "isThreadInterface:"
+ "isThreadRadioAvailable"
+ "keyCountProvider"
+ "keyID"
+ "keyNumber"
+ "lastScanUptime"
+ "limit"
+ "managesConnectionStateExternally"
+ "motion"
+ "needsUpdate"
+ "numberOfChannels"
+ "observe"
+ "payloadType"
+ "peakBitrate"
+ "pendingBonjourAdd"
+ "polygons"
+ "q24@?0@\"HAPPairingIdentity\"8@\"HAPPairingIdentity\"16"
+ "quality"
+ "ratchetBits"
+ "ratchetTime"
+ "readPublicKeyForRemovedAccessoryName:iCloudIdentifier:error:"
+ "reasonEnum"
+ "refreshScanCompletion"
+ "refreshScanResultForSSID:completion:"
+ "refreshingScanSSID"
+ "removePairingsWithRemovedAccessoryKey:queue:completion:"
+ "removeUnpairedAccessoryPairing:accessoryKey:completion:"
+ "removedAccessoryDiscoveryCompletionHandlers"
+ "removedAccessoryIdentifiers"
+ "removedAccessoryKey"
+ "rev"
+ "revision"
+ "scanDwellTime"
+ "sensorDimensions"
+ "sequenceNumber"
+ "serverCertificate"
+ "sessionID"
+ "setActive:"
+ "setAdditionalCandidates:"
+ "setAudioCipherSuite:"
+ "setAudioSSRC:"
+ "setAudioTier:"
+ "setAverageBitrate:"
+ "setBaseKey:"
+ "setBitDepth:"
+ "setBuffers:"
+ "setCA:"
+ "setCMAFSessionID:"
+ "setCMAFSessionStart:"
+ "setCMAFSessionStop:"
+ "setCSR:"
+ "setCameraSensors:"
+ "setCandidate:"
+ "setClientCertificate:"
+ "setClipID:"
+ "setCodec:"
+ "setCount:"
+ "setEvents:"
+ "setFrameRate:"
+ "setFramesPerSecond:"
+ "setHeight:"
+ "setIntervals:"
+ "setInverted:"
+ "setKID:"
+ "setKeyID:"
+ "setKeyNumber:"
+ "setLastScanUptime:"
+ "setLimit:"
+ "setMotion:"
+ "setNeedsUpdate:"
+ "setNumberOfChannels:"
+ "setPayloadType:"
+ "setPeakBitrate:"
+ "setPendingBonjourAdd:"
+ "setPolygons:"
+ "setQuality:"
+ "setRatchetBits:"
+ "setRatchetTime:"
+ "setRefreshScanCompletion:"
+ "setRefreshingScanSSID:"
+ "setRemovedAccessoryIdentifiers:"
+ "setRemovedAccessoryKey:"
+ "setSDPAnswer:"
+ "setSDPMLineIndex:"
+ "setSDPMid:"
+ "setSDPOffer:"
+ "setSFrameConfiguration:"
+ "setSensorDimensions:"
+ "setSequenceNumber:"
+ "setServerCertificate:"
+ "setSessionID:"
+ "setStart:"
+ "setStop:"
+ "setStopAction:"
+ "setTargetAverageBitrate:"
+ "setTiers:"
+ "setURL:"
+ "setVertices:"
+ "setVideoCipherSuite:"
+ "setVideoSSRC:"
+ "setVideoStreamCapabilities:"
+ "setVideoTier:"
+ "setWidth:"
+ "setZoneData:"
+ "setZoneDataVersion:"
+ "stopAction"
+ "targetAverageBitrate"
+ "threadMeshLocalPrefix"
+ "tiers"
+ "timeIntervalSince1970"
+ "timeSinceLastScan"
+ "unchanged"
+ "updateConnectionState:withError:"
+ "updateRemovedAccessoriesWithReason:accessoryKey:completion:"
+ "utun"
+ "v20@?0i8^{__CFArray=}12"
+ "v24@0:8@\"NSData\"16"
+ "v28@0:8@16i24"
+ "v32@0:8@\"<HAP2AccessoryServerMetadata>\"16@\"<HAP2AccessoryServerControllerPrivate>\"24"
+ "v32@0:8Q16@\"NSError\"24"
+ "v32@0:8Q16@24"
+ "vertices"
+ "videoCipherSuite"
+ "videoSSRC"
+ "videoStreamCapabilities"
+ "videoTier"
+ "wasRemovedFromHome:"
+ "width"
+ "zoneData"
+ "zoneDataVersion"
- "!!"
- "%@ Ignoring updateAccessories request with reason:%@ one already running"
- "%{public}@Cannot save cache for nil deviceID"
- "%{public}@Could not init socket info for device %@ from dictionary %@"
- "%{public}@IP Accessory server %@ matches setupID %{public}@ and is paired/hasPairings: (%{public}@/%{public}@)"
- "%{public}@Ignoring cache entry with null fields"
- "%{public}@Invalid input dictionary %@"
- "%{public}@No cached IP addresses"
- "%{public}@Pre-populate browser with cached IP Addresses"
- "%{public}@Request to save cache with nil bonjour info ignored %@"
- "%{public}@Retrieve data %@ for device %@"
- "%{public}@Treating OSStatus %d (%s) as Generic error"
- "/Library/Caches/com.apple.xbs/Sources/HomeKit/Sources/CoreHAP/Accessories/HAPSuspendedAccessory.m"
- "/Library/Caches/com.apple.xbs/Sources/HomeKit/Sources/CoreHAP/HAP2/HAPAdapter/HAPAccessoryServerHAP2Adapter.m"
- "/Library/Caches/com.apple.xbs/Sources/HomeKit/Sources/CoreHAP/HAP2/Pairing/HAP2AccessoryServerPairingDriver.m"
- "/Library/Caches/com.apple.xbs/Sources/HomeKit/Sources/CoreHAP/HAPHTTPClient.m"
- "/Library/Caches/com.apple.xbs/Sources/HomeKit/Sources/CoreHAP/Servers/HAPAccessoryServerIP.m"
- "/Library/Caches/com.apple.xbs/Sources/HomeKit/Sources/CoreHAP/Servers/_HAPAccessoryServerBTLE200.m"
- "@\"<HAP2Cancelable>\"24@0:8@\"NSString\"16"
- "@\"<HAPAccessoryServerIPCache>\""
- "@64@0:8@16@24Q32@40@48@56"
- "AccessoryServerIPCache"
- "HAPAccessoryServerIPCacheData"
- "HAPAccessoryServerIPCacheData: socketInfo %@, bonjour %@"
- "Secure Transport: Opening security session"
- "T@\"<HAPAccessoryServerIPCache>\",R,N,V_cache"
- "T@\"NSDictionary\",&,N,V_socketInfo"
- "T@\"NSString\",C,N,V_metric_pairVerifyReason"
- "T@\"NSString\",C,N,V_reachabilityChangedReason"
- "T@\"NSString\",R,C,N,V_reason"
- "TB,N,V_isInitialCacheRestored"
- "The delegate is mising"
- "_doStartDiscoveringAccessoryServers"
- "_isInitialCacheRestored"
- "_prePopulateBrowserFromCacheWithCompletion:"
- "_socketInfo"
- "_updateCacheForDevice:socketInfo:bonjour:"
- "cache"
- "coap_get_block"
- "deleteDataForDevice:"
- "initFromDictionary:"
- "initWithCachedIp:bonjourRecord:"
- "initWithQueue:cache:"
- "isInitialCacheRestored"
- "len"
- "oi"
- "pattern"
- "result"
- "retrieveCachedData:"
- "saveData:forDevice:"
- "setIsInitialCacheRestored:"
- "setSocketInfo:"
- "socketInfo"
- "updateCacheForDeviceID:ipData:"
- "v32@?0@\"NSString\"8@\"HAPAccessoryServerIPCacheData\"16^B24"

```
