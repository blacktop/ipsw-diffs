## uarpd

> `/usr/libexec/uarpd`

```diff

-  __TEXT.__text: 0x9d0ec
-  __TEXT.__auth_stubs: 0xa40
-  __TEXT.__objc_stubs: 0xa0a0
-  __TEXT.__objc_methlist: 0x8218
-  __TEXT.__objc_methname: 0xee96
-  __TEXT.__objc_classname: 0x1a8a
-  __TEXT.__cstring: 0xa96b
-  __TEXT.__objc_methtype: 0x29e9
-  __TEXT.__const: 0x148
-  __TEXT.__oslogstring: 0x8c29
-  __TEXT.__gcc_except_tab: 0x1c4
-  __TEXT.__unwind_info: 0x21f0
-  __DATA_CONST.__const: 0x1078
-  __DATA_CONST.__cfstring: 0x5280
-  __DATA_CONST.__objc_classlist: 0x5a0
+  __TEXT.__text: 0xa02bc
+  __TEXT.__auth_stubs: 0xa20
+  __TEXT.__objc_stubs: 0xa360
+  __TEXT.__objc_methlist: 0x8678
+  __TEXT.__objc_methname: 0xf377
+  __TEXT.__objc_classname: 0x1ce4
+  __TEXT.__cstring: 0xac00
+  __TEXT.__objc_methtype: 0x2a49
+  __TEXT.__const: 0x140
+  __TEXT.__oslogstring: 0x8cec
+  __TEXT.__gcc_except_tab: 0x19c
+  __TEXT.__unwind_info: 0x2318
+  __DATA_CONST.__const: 0x10a0
+  __DATA_CONST.__cfstring: 0x53e0
+  __DATA_CONST.__objc_classlist: 0x600
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x588
+  __DATA_CONST.__objc_superrefs: 0x5e8
   __DATA_CONST.__objc_intobj: 0x3d8
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x530
-  __DATA_CONST.__got: 0x568
-  __DATA.__objc_const: 0xfeb0
-  __DATA.__objc_selrefs: 0x3028
-  __DATA.__objc_ivar: 0xb4c
-  __DATA.__objc_data: 0x3840
+  __DATA_CONST.__auth_got: 0x520
+  __DATA_CONST.__got: 0x640
+  __DATA.__objc_const: 0x10918
+  __DATA.__objc_selrefs: 0x30e8
+  __DATA.__objc_ivar: 0xb90
+  __DATA.__objc_data: 0x3c00
   __DATA.__data: 0x548
-  __DATA.__bss: 0x1180
+  __DATA.__bss: 0x1178
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 3816
-  Symbols:   230
-  CStrings:  5517
+  Functions: 3910
+  Symbols:   228
+  CStrings:  5609
 
Sections:
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA.__data : content changed
Symbols:
- _IOPMAssertionCreateWithName
- _IOPMAssertionRelease
CStrings:
+ "%s: %@ does not share manifest with direct endpoint %@"
+ "%s: ESPRESSO: Message <type=0x%04x, id=0x%04x> Length too big ! expected <%u>, got <%u>"
+ "%s: Endpoint %@, Staging asset URL is %@"
+ "%s: Error creating payload at index %lu"
+ "%s: Failed to create payload at index %lu"
+ "%s: Moving %@ to %@"
+ "%s: Not a downstream endpoint; %@"
+ "%s: Skip offering asset %@ to %@"
+ "%s: Staged Firmware Asset %@ for %@"
+ "%s: Staging Firmware Asset %@ for %@"
+ "%s: check if we accept asset manager notifications endpoint %@"
+ "%s: endpoint %@ has behavioral TLV %@"
+ "%s: no staging / staged asset to offer %@ from direct endpoint %@"
+ "%s: offer %@ from direct endpoint %@ to %@"
+ "%s: we do accept asset manager notifications endpoint %@"
+ "%s: we do not accept asset manager notifications endpoint %@"
+ "-[UARPEndpointLayer3 downstreamEndpointReachable:downstreamEndpointID:tlvs:]_block_invoke"
+ "-[UARPEndpointLayer3 notifyDownstreamEndpointReachable:tlvs:]"
+ "-[UARPHostEndpoint downstreamEndpointReachableInternal:tlvs:]"
+ "-[UARPHostEndpoint handleSharedManifest]"
+ "-[UARPHostEndpoint hostEndpointAcceptsAssetManagerNotification]_block_invoke"
+ "-[UARPHostEndpoint hostEndpointDeviceUnavailableInternal]"
+ "-[UARPHostEndpoint hostEndpointTransportUnavailableInternal]"
+ "-[UARPHostEndpoint layer3DownstreamEndpointReachable:downstreamID:tlvs:]"
+ "-[UARPHostEndpoint sharesManifestWithDirectEndpoint]"
+ "-[UARPHostEndpoint subscribeToAssetManager:oldEntry:]"
+ "-[UARPSuperBinaryLayer3 addPayloadWith4cc:payloadVersion:payloadIndex:]"
+ "@60@0:8@16S24@28@36@44@52"
+ "Endpoint %@: Downstream Endpoint Reachable, ID = %u, TLVs = %@"
+ "Personalization Board ID (64 bits)"
+ "Personalization Digest List Size"
+ "Personalization FTAB Payload Production Mode Host Override"
+ "Personalization FTAB Payload Security Mode Host Override"
+ "Personalization Matching Data"
+ "Personalization Matching Data Payload Tags"
+ "Personalization Matching Data Product Revision Maximum"
+ "Personalization Matching Data Product Revision Minimum"
+ "Personalization More Requests to Follow"
+ "Personalization Payload Demotion Production Mode"
+ "Personalization Payload Demotion Security Mode"
+ "Shared Manifest"
+ "Starting downstream endpoint id (%u) %@, with TLVs %@ on upstream endpoint %@ with database entry filename %@"
+ "T@\"NSData\",R,V_matchingData"
+ "T@\"NSString\",R,V_payloadTags"
+ "TC,R,V_moreRequestsToFollow"
+ "TC,R,V_sharedManifest"
+ "TI,R,V_demotionProductionMode"
+ "TI,R,V_demotionSecurityMode"
+ "TI,R,V_digestListSize"
+ "TI,R,V_productRevisionMax"
+ "TI,R,V_productRevisionMin"
+ "TQ,R,V_boardID"
+ "TS,R,V_productionModeHostOverride"
+ "TS,R,V_securityModeHostOverride"
+ "UARPMetaDataPersonalizationBoardID64"
+ "UARPMetaDataPersonalizationDemotionProductionMode"
+ "UARPMetaDataPersonalizationDemotionSecurityMode"
+ "UARPMetaDataPersonalizationDigestListSize"
+ "UARPMetaDataPersonalizationFTABPayloadProductionModeHostOverride"
+ "UARPMetaDataPersonalizationFTABPayloadSecurityModeHostOverride"
+ "UARPMetaDataPersonalizationMatchingData"
+ "UARPMetaDataPersonalizationMatchingDataPayloadTags"
+ "UARPMetaDataPersonalizationMatchingDataProductRevisionMax"
+ "UARPMetaDataPersonalizationMatchingDataProductRevisionMin"
+ "UARPMetaDataPersonalizationMoreRequestsToFollow"
+ "UARPMetaDataPersonalizationSharedManifest"
+ "^{uarpPlatformEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSCSCC}^v{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}C^viI^^{uarpPlatformRemoteEndpoint}^{uarpPlatformAsset}iCi^?S^{uarpLayer2EndpointIDInfo}S^{uarpDownstreamEndpointObj}I^{uarpMemoryTracker}}"
+ "_behavioralTLVs"
+ "_demotionProductionMode"
+ "_demotionSecurityMode"
+ "_digestListSize"
+ "_matchingData"
+ "_moreRequestsToFollow"
+ "_packetQueue"
+ "_payloadTags"
+ "_productRevisionMax"
+ "_productRevisionMin"
+ "_productionModeHostOverride"
+ "_securityModeHostOverride"
+ "_sharedManifest"
+ "_stagedAsset"
+ "_stagingAsset"
+ "adjustSubfileLengthsAndOffsets"
+ "com.apple.uarp.endpoint.packet.parser"
+ "dataWithLength:"
+ "demotionProductionMode"
+ "demotionSecurityMode"
+ "digestListSize"
+ "downstreamEndpointReachable:downstreamEndpointID:tlvs:"
+ "downstreamEndpointReachableInternal:tlvs:"
+ "handleSharedManifest"
+ "hostEndpointAcceptsAssetManagerNotification"
+ "hostEndpointDeviceUnavailableInternal"
+ "hostEndpointTransportUnavailableInternal"
+ "initWithUpstreamEndpoint:downstreamID:tlvs:uuid:hostManager:tempFolderPath:"
+ "layer2CallbackDownstreamReachable:tlvs:"
+ "layer3DownstreamEndpointReachable:downstreamID:tlvs:"
+ "matchingData"
+ "moreRequestsToFollow"
+ "notifyDownstreamEndpointReachable:tlvs:"
+ "packetTracking:packetDirection:inFunction:"
+ "payloadTags"
+ "productRevisionMax"
+ "productRevisionMin"
+ "productionModeHostOverride"
+ "securityModeHostOverride"
+ "sharedManifest"
+ "sharesManifestWithDirectEndpoint"
+ "stagedAssetURL"
+ "stagingAssetURL"
+ "subscribeToAssetManager:oldEntry:"
+ "updateSubfileOffset:"
+ "v36@0:8@\"UARPEndpointLayer3\"16S24@\"NSArray\"28"
+ "v36@0:8@16S24@28"
+ "v40@0:8@16q24r*32"
+ "{uarpPlatformEndpointCallbacks=\"fRequestBuffer\"^?\"fReturnBuffer\"^?\"fRequestTransmitMsgBuffer\"^?\"fReturnTransmitMsgBuffer\"^?\"fSendMessage\"^?\"fDataTransferPause\"^?\"fDataTransferPauseAck\"^?\"fDataTransferResume\"^?\"fDataTransferResumeAck\"^?\"fSuperBinaryOffered\"^?\"fDynamicAssetOffered\"^?\"fApplyStagedAssets\"^?\"fApplyStagedAssetsResponse\"^?\"fManufacturerName\"^?\"fManufacturerNameResponse\"^?\"fModelName\"^?\"fModelNameResponse\"^?\"fSerialNumber\"^?\"fSerialNumberResponse\"^?\"fHardwareVersion\"^?\"fHardwareVersionResponse\"^?\"fActiveFirmwareVersion2\"^?\"fActiveFirmwareVersionResponse\"^?\"fStagedFirmwareVersion2\"^?\"fStagedFirmwareVersionResponse\"^?\"fLastError\"^?\"fLastErrorResponse\"^?\"fStatisticsResponse\"^?\"fAssetSolicitation\"^?\"fRescindAllAssets\"^?\"fRescindAllAssetsAck\"^?\"fLayer2WatchdogSet\"^?\"fLayer2WatchdogCancel\"^?\"fMonotonicClockTime\"^?\"fProtocolVersion\"^?\"fFriendlyName\"^?\"fFriendlyNameResponse\"^?\"fDiscoveredEndpointID\"^?\"fDiscoveredComponent\"^?\"fBulkInfoQuery\"^?\"fBulkInfoResponse\"^?\"fDecompressBuffer\"^?\"fCompressBuffer\"^?\"fHashInfo\"^?\"fHashInit\"^?\"fHashUpdate\"^?\"fHashFinal\"^?\"fHashLog\"^?\"fLogPacket\"^?\"fLogError\"^?\"fLogInfo\"^?\"fLogDebug\"^?\"fLogFault\"^?\"fDownstreamDiscovery\"^?\"fDownstreamReachable3\"^?\"fDownstreamUnreachable2\"^?\"fDownstreamReleased2\"^?\"fDownstreamRecvMessage\"^?\"fNoFirmwareUpdateAvailable\"^?\"fVendorSpecificRecvMsg\"^?\"fVendorSpecificCheckExpectedResponse\"^?\"fVendorSpecificCheckValidToSend\"^?\"fVendorSpecificExceededRetries\"^?\"fActiveFirmwareVersion\"^?\"fStagedFirmwareVersion\"^?\"fTxWatchdogSet\"^?\"fTxWatchdogCancel\"^?\"fDownstreamReachable\"^?\"fDownstreamReachable2\"^?\"fDownstreamUnreachable\"^?\"fDownstreamReleased\"^?}"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x831"
- "%s: Created power assertion for %@"
- "%s: ESPRESSO:Bonus Message <type=0x%04x, length=x0x%04x, id=0x%04x>"
- "%s: ESPRESSO:Message <type=0x%04x, id=0x%04x> Length too big ! expected <%u>, got <%u>"
- "%s: Failed to create power assertion for %@; error %d"
- "%s: Failed to release power assertion for %@; error %d"
- "%s: Firmware Asset %@ for %@"
- "%s: No power assertion to release for %@"
- "%s: Padding before subfiles is off by %d bytes; adjust %d to %d"
- "%s: Padding subfile %c%c%c%c is off by %d bytes; pad from %d to %d"
- "%s: Previous power assertion created for %@"
- "%s: Released power assertion for %@"
- "%s: Releasing power assertion for %@"
- "%s: Taking power assertion for %@"
- "-[UARPEndpointLayer3 downstreamEndpointReachable:downstreamEndpointID:]_block_invoke"
- "-[UARPEndpointLayer3 notifyDownstreamEndpointReachable:]"
- "-[UARPHostEndpoint downstreamEndpointReachableInternal:]"
- "-[UARPHostEndpoint hostEndpointUnavailableInternal]"
- "-[UARPHostEndpoint layer3DownstreamEndpointReachable:downstreamID:]"
- "-[UARPHostEndpoint powerAssertionCreate]"
- "-[UARPHostEndpoint powerAssertionRelease]"
- "-[UARPHostManager pauseAssetManager:]_block_invoke"
- "-[UARPHostManager resumeAssetManager:]_block_invoke"
- "@52@0:8@16S24@28@36@44"
- "Endpoint %@: Downstream Endpoint Reachable, ID = %u"
- "PreventUserIdleSystemSleep"
- "Starting downstream endpoint id (%u) %@ on upstream endpoint %@ with database entry filename %@"
- "^{uarpPlatformEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSCSCC}^v{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}C^viI^^{uarpPlatformRemoteEndpoint}^{uarpPlatformAsset}iCi^?S^{uarpLayer2EndpointIDInfo}S^{uarpDownstreamEndpointObj}I^{uarpMemoryTracker}}"
- "_stagingAssets"
- "downstreamEndpointReachableInternal:"
- "hostEndpointUnavailableInternal"
- "initWithUpstreamEndpoint:downstreamID:uuid:hostManager:tempFolderPath:"
- "notifyDownstreamEndpointReachable:"
- "packetTracking:inFunction:"
- "v32@0:8@16r*24"
- "{uarpPlatformEndpointCallbacks=\"fRequestBuffer\"^?\"fReturnBuffer\"^?\"fRequestTransmitMsgBuffer\"^?\"fReturnTransmitMsgBuffer\"^?\"fSendMessage\"^?\"fDataTransferPause\"^?\"fDataTransferPauseAck\"^?\"fDataTransferResume\"^?\"fDataTransferResumeAck\"^?\"fSuperBinaryOffered\"^?\"fDynamicAssetOffered\"^?\"fApplyStagedAssets\"^?\"fApplyStagedAssetsResponse\"^?\"fManufacturerName\"^?\"fManufacturerNameResponse\"^?\"fModelName\"^?\"fModelNameResponse\"^?\"fSerialNumber\"^?\"fSerialNumberResponse\"^?\"fHardwareVersion\"^?\"fHardwareVersionResponse\"^?\"fActiveFirmwareVersion2\"^?\"fActiveFirmwareVersionResponse\"^?\"fStagedFirmwareVersion2\"^?\"fStagedFirmwareVersionResponse\"^?\"fLastError\"^?\"fLastErrorResponse\"^?\"fStatisticsResponse\"^?\"fAssetSolicitation\"^?\"fRescindAllAssets\"^?\"fRescindAllAssetsAck\"^?\"fLayer2WatchdogSet\"^?\"fLayer2WatchdogCancel\"^?\"fMonotonicClockTime\"^?\"fProtocolVersion\"^?\"fFriendlyName\"^?\"fFriendlyNameResponse\"^?\"fDiscoveredEndpointID\"^?\"fDiscoveredComponent\"^?\"fBulkInfoQuery\"^?\"fBulkInfoResponse\"^?\"fDecompressBuffer\"^?\"fCompressBuffer\"^?\"fHashInfo\"^?\"fHashInit\"^?\"fHashUpdate\"^?\"fHashFinal\"^?\"fHashLog\"^?\"fLogPacket\"^?\"fLogError\"^?\"fLogInfo\"^?\"fLogDebug\"^?\"fLogFault\"^?\"fDownstreamDiscovery\"^?\"fDownstreamReachable2\"^?\"fDownstreamUnreachable2\"^?\"fDownstreamReleased2\"^?\"fDownstreamRecvMessage\"^?\"fNoFirmwareUpdateAvailable\"^?\"fVendorSpecificRecvMsg\"^?\"fVendorSpecificCheckExpectedResponse\"^?\"fVendorSpecificCheckValidToSend\"^?\"fVendorSpecificExceededRetries\"^?\"fActiveFirmwareVersion\"^?\"fStagedFirmwareVersion\"^?\"fTxWatchdogSet\"^?\"fTxWatchdogCancel\"^?\"fDownstreamReachable\"^?\"fDownstreamUnreachable\"^?\"fDownstreamReleased\"^?}"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0c1"

```
