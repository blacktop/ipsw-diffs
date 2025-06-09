## UARPUpdaterServiceDFU

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceDFU.xpc/UARPUpdaterServiceDFU`

```diff

-1207.120.19.0.0
-  __TEXT.__text: 0x15824
-  __TEXT.__auth_stubs: 0x620
+1338.0.21.0.2
+  __TEXT.__text: 0x16a1c
+  __TEXT.__auth_stubs: 0x630
   __TEXT.__objc_stubs: 0x14c0
-  __TEXT.__objc_methlist: 0xba8
+  __TEXT.__objc_methlist: 0xc60
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x1c79
-  __TEXT.__objc_methname: 0x22bb
+  __TEXT.__cstring: 0x23fa
+  __TEXT.__objc_methname: 0x254f
   __TEXT.__oslogstring: 0xa42
-  __TEXT.__objc_classname: 0x112
-  __TEXT.__objc_methtype: 0x2f25
-  __TEXT.__unwind_info: 0x528
-  __DATA_CONST.__auth_got: 0x318
+  __TEXT.__objc_classname: 0x114
+  __TEXT.__objc_methtype: 0x337c
+  __TEXT.__unwind_info: 0x548
+  __DATA_CONST.__auth_got: 0x320
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x438
+  __DATA_CONST.__const: 0x590
   __DATA_CONST.__cfstring: 0x300
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_intobj: 0x108
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x16d0
-  __DATA.__objc_selrefs: 0x820
+  __DATA.__objc_const: 0x1748
+  __DATA.__objc_selrefs: 0x898
   __DATA.__objc_ivar: 0xd8
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x251

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2F0DB6C1-2A05-3080-BB46-5995EBF35AD5
-  Functions: 575
-  Symbols:   462
-  CStrings:  824
+  UUID: 9406FF33-17DD-3C49-9199-F313A3B9FA71
+  Functions: 610
+  Symbols:   498
+  CStrings:  898
 
Symbols:
+ _UARPLayer2EndpointBulkInformationQuery
+ _UARPLayer2EndpointBulkInformationResponse
+ _UARPLayer2EndpointIDComponents
+ _UARPLayer2EndpointIDs
+ _UARPLayer2MonotonicClockTime
+ _UARPProtocolVersionRequiresDownstreamMessageACK
+ _UARPProtocolVersionResponseAdjustByProtocolVersion
+ _objc_retain_x1
+ _uarpAllocateTransmitBuffers
+ _uarpMessageAdjustedForEndpointID
+ _uarpMessagePrintToBuffer
+ _uarpMessageTypeToString
+ _uarpPlatformAssetFindFirmware
+ _uarpPlatformCleanupAssets
+ _uarpPlatformConfigureEndpointIDs
+ _uarpPlatformConfigureEndpointTags
+ _uarpPlatformDelegateForDownstreamID
+ _uarpPlatformDownstreamEndpointAddToList
+ _uarpPlatformDownstreamEndpointDelegateFindOnListByID
+ _uarpPlatformDownstreamEndpointFindOnList
+ _uarpPlatformDownstreamEndpointFindOnListByDelegate
+ _uarpPlatformDownstreamEndpointIDFindOnListByDelegate
+ _uarpPlatformDownstreamEndpointReachable
+ _uarpPlatformDownstreamEndpointRemoveFromList
+ _uarpPlatformDownstreamEndpointUnreachable
+ _uarpPlatformEndpointBulkInfoQuery
+ _uarpPlatformEndpointBulkInfoResponse
+ _uarpPlatformEndpointBulkInfoResponseAddTLV
+ _uarpPlatformEndpointDeinit
+ _uarpPlatformEndpointDiscoverEndpointIDs
+ _uarpPlatformGetSupportsBulkInfoQueries
+ _uarpPlatformGetUseHostPushModel
+ _uarpPlatformQueryEndpointComponentDiscovery
+ _uarpPlatformReleaseEndpointIDs
+ _uarpPlatformReleaseEndpointTags
+ _uarpPlatformSendDownstreamMessageWithDownstreamID
+ _uarpPlatformSendMessageFromDownstreamEndpointID
+ _uarpPlatformSendMessageToDownstreamEndpointID
+ _uarpRemoteEndpointForAsset
+ _uarpTransmitMessageToDownstreamEndpointID
+ _uarpTransmitQueuePurge
+ _uarpTransmitQueueReclaimEntries
- _uarpAssetQueueSolicitation
- _uarpPlatformAssetApproveOfferVersion
- _uarpPlatformEndpointIsMessageTypePending
- _uarpPlatformTransmitQueueLogEntry
- _uarpTransmitQueuePendingEntryComplete
- _uarpTransmitQueueProcessRecv
CStrings:
+ "%s: <ROLE=%s> : Add Downstream Endpoint <Local=%p> <Remote=%p> DS.ID <%hu>"
+ "%s: <ROLE=%s> : RemoveDownstream Endpoint <Local=%p> <Remote=%p> DS.ID <%hu>"
+ "%s: ESPRESSO Corrupt Entry ? pBuffer = %p, pMsg = %p"
+ "%s: ESPRESSO:Bonus Message <type=0x%04x, length=x0x%04x, id=0x%04x>"
+ "%s: ESPRESSO:Message <type=0x%04x, id=0x%04x> Length too big ! expected <%u>, got <%u>"
+ "%s: ESPRESSO:Message <type=0x%04x, id=0x%04x> Length too small ! expected <%u>, got <%u>"
+ "<ROLE=%s> ESPRESSO: UARP.LAYER2.RECV.MSG: Length too small <%u>"
+ "<ROLE=%s> UARP.LAYER2.DATA.RESP offset=0x%08x, requestedlength=%u"
+ "@32@0:8^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?IIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}16@24"
+ "Apply Staged Assets Request"
+ "Apply Staged Assets Response"
+ "Asset Available Notification"
+ "Asset Available Notification Ack"
+ "Asset Data Transfer Notification"
+ "Asset Data Transfer Notification Ack"
+ "Asset Processing Notification"
+ "Asset Processing Notification Ack"
+ "Asset Rescinded Notification"
+ "Asset Rescinded Notification Ack"
+ "Buffer Overflow"
+ "Buffer Would Overflow"
+ "Data Request"
+ "Data Response"
+ "Downstream Endpoint Discovery"
+ "Downstream Endpoint Discovery Ack"
+ "Downstream Endpoint Message"
+ "Downstream Endpoint Message Ack"
+ "Downstream Endpoint Reachable"
+ "Downstream Endpoint Reachable Ack"
+ "Downstream Endpoint Unreachable"
+ "Downstream Endpoint Unreachable Ack"
+ "Dynamic Asset PreProcessing Notification"
+ "Dynamic Asset PreProcessing Notification Ack"
+ "Dynamic Asset Solicitation"
+ "Dynamic Asset Solicitation Ack"
+ "Endpoint Bulk Information Request"
+ "Endpoint Bulk Information Request Ack"
+ "Endpoint Bulk Information Response"
+ "Endpoint Bulk Information Response Ack"
+ "Endpoint Component Discovery Request"
+ "Endpoint Component Discovery Response"
+ "Endpoint Discovery Request"
+ "Endpoint Discovery Response"
+ "I32@0:8@16^{uarpPlatformOptionsObj=IIISCSSSiSSCSCC}24"
+ "Information Request"
+ "Information Response"
+ "Invalid EndpointID"
+ "No Firmware Update Available"
+ "No Firmware Update Available Ack"
+ "Sync"
+ "T^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?IIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}},R,V_pAsset"
+ "Vendor Specific"
+ "Version Discovery Request"
+ "Version Discovery Response"
+ "^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?IIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}"
+ "^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?IIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}16@0:8"
+ "^{uarpPlatformEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSCSCC}^v{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}^viI^^{uarpPlatformRemoteEndpoint}^{uarpPlatformAsset}iCi^?S^{uarpLayer2EndpointIDInfo}S^{uarpDownstreamEndpointObj}I^{uarpMemoryTracker}}16@0:8"
+ "^{uarpPlatformRemoteEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSCSCC}^vSSSCiCCSS{UARPStatistics=IIII}^{UARP4ccTag}^{uarpPlatformStreamingBuffer}^{uarpPlatformTransmitBufferEntry}^{uarpPlatformTransmitBufferEntry}S{UARPVersion=IIII}{UARPVersion=IIII}^{uarpPlatformRemoteEndpoint}}16@0:8"
+ "queryCompleteForAccessory:boardID:error:"
+ "queryCompleteForAccessory:chipID:error:"
+ "queryCompleteForAccessory:chipRevision:error:"
+ "queryCompleteForAccessory:ecid:error:"
+ "queryCompleteForAccessory:enableMixMatch:error:"
+ "queryCompleteForAccessory:epoch:error:"
+ "queryCompleteForAccessory:liveNonce:error:"
+ "queryCompleteForAccessory:manifestPrefix:error:"
+ "queryCompleteForAccessory:nonceHash:error:"
+ "queryCompleteForAccessory:nonceSeed:error:"
+ "queryCompleteForAccessory:productionMode:error:"
+ "queryCompleteForAccessory:securityDomain:error:"
+ "queryCompleteForAccessory:securityMode:error:"
+ "queryCompleteForAccessoryID:nonceHash:error:"
+ "queryCompleteForAccessoryID:nonceSeed:error:"
+ "uarpMsgRecvDownstreamEndpointReachable"
+ "uarpMsgRecvDownstreamEndpointUnreachable"
+ "uarpMsgRecvDownstreamEndpointUnreachableAck"
+ "uarpPlatformEndpointRecvMessage"
+ "uarpTransmitEntryIsValidToSend"
+ "v36@0:8@\"UARPAccessory\"16B24@\"NSError\"28"
+ "v40@0:8@\"UARPAccessory\"16@\"NSData\"24@\"NSError\"32"
+ "v40@0:8@\"UARPAccessory\"16Q24@\"NSError\"32"
+ "v40@0:8@\"UARPAccessoryID\"16@\"NSData\"24@\"NSError\"32"
+ "{uarpPlatformEndpoint=\"_options\"{uarpPlatformOptionsObj=\"maxTxPayloadLength\"I\"maxRxPayloadLength\"I\"payloadWindowLength\"I\"protocolVersion\"S\"reofferFirmwareOnSync\"C\"responseTimeout\"S\"retryLimit\"S\"maxTransmitsInFlight\"S\"endpointType\"i\"solicitationQueueDepth\"S\"txBufferOverhead\"S\"upgradeOnly\"C\"numPreallocatedBuffers\"S\"supportsBulkInfoQueries\"C\"useHostPushModel\"C}\"pVendorExtension\"^v\"protectedCallbacks\"{uarpPlatformEndpointCallbacks=\"fRequestBuffer\"^?\"fReturnBuffer\"^?\"fRequestTransmitMsgBuffer\"^?\"fReturnTransmitMsgBuffer\"^?\"fSendMessage\"^?\"fDataTransferPause\"^?\"fDataTransferPauseAck\"^?\"fDataTransferResume\"^?\"fDataTransferResumeAck\"^?\"fSuperBinaryOffered\"^?\"fDynamicAssetOffered\"^?\"fApplyStagedAssets\"^?\"fApplyStagedAssetsResponse\"^?\"fManufacturerName\"^?\"fManufacturerNameResponse\"^?\"fModelName\"^?\"fModelNameResponse\"^?\"fSerialNumber\"^?\"fSerialNumberResponse\"^?\"fHardwareVersion\"^?\"fHardwareVersionResponse\"^?\"fActiveFirmwareVersion2\"^?\"fActiveFirmwareVersionResponse\"^?\"fStagedFirmwareVersion2\"^?\"fStagedFirmwareVersionResponse\"^?\"fLastError\"^?\"fLastErrorResponse\"^?\"fStatisticsResponse\"^?\"fAssetSolicitation\"^?\"fRescindAllAssets\"^?\"fRescindAllAssetsAck\"^?\"fLayer2WatchdogSet\"^?\"fLayer2WatchdogCancel\"^?\"fMonotonicClockTime\"^?\"fProtocolVersion\"^?\"fFriendlyName\"^?\"fFriendlyNameResponse\"^?\"fDiscoveredEndpointID\"^?\"fDiscoveredComponent\"^?\"fBulkInfoQuery\"^?\"fBulkInfoResponse\"^?\"fDecompressBuffer\"^?\"fCompressBuffer\"^?\"fHashInfo\"^?\"fHashInit\"^?\"fHashUpdate\"^?\"fHashFinal\"^?\"fHashLog\"^?\"fLogPacket\"^?\"fLogError\"^?\"fLogInfo\"^?\"fLogDebug\"^?\"fLogFault\"^?\"fDownstreamDiscovery\"^?\"fDownstreamReachable2\"^?\"fDownstreamUnreachable2\"^?\"fDownstreamReleased2\"^?\"fDownstreamRecvMessage\"^?\"fNoFirmwareUpdateAvailable\"^?\"fVendorSpecificRecvMsg\"^?\"fVendorSpecificCheckExpectedResponse\"^?\"fVendorSpecificCheckValidToSend\"^?\"fVendorSpecificExceededRetries\"^?\"fActiveFirmwareVersion\"^?\"fStagedFirmwareVersion\"^?\"fTxWatchdogSet\"^?\"fTxWatchdogCancel\"^?\"fDownstreamReachable\"^?\"fDownstreamUnreachable\"^?\"fDownstreamReleased\"^?}\"pDelegate\"^v\"role\"i\"numRemoteEndpointSlots\"I\"pRemoteEPs\"^^{uarpPlatformRemoteEndpoint}\"pAssetList\"^{uarpPlatformAsset}\"nextTxAssetID\"i\"rxLock\"C\"nextRemoteEndpointID\"i\"fVendorSpecific\"^?\"numEndpointIDs\"S\"pEndpointIDInfo\"^{uarpLayer2EndpointIDInfo}\"nextDownstreamID\"S\"pDownstreamEndpoints\"^{uarpDownstreamEndpointObj}\"numMemoryTrackers\"I\"pMemoryTracker\"^{uarpMemoryTracker}}"
+ "{uarpPlatformEndpointApple=\"supportsPersonalization\"C\"supportsHeySiri\"C\"supportsJustSiri\"C\"supportsVoiceAssist\"C\"callbacks\"{uarpPlatformEndpointAppleCallbacks=\"fAppleModelNumber\"^?\"fAppleModelNumberResponse\"^?\"fHwFusingType\"^?\"fHwFusingTypeResponse\"^?\"fManifestPrefix\"^?\"fManifestPrefixResponse\"^?\"fBoardID\"^?\"fBoardIDResponse\"^?\"fChipID\"^?\"fChipIDResponse\"^?\"fChipRevision\"^?\"fChipRevisionResponse\"^?\"fECID\"^?\"fECIDResponse\"^?\"fECIDData\"^?\"fECIDDataResponse\"^?\"fSecurityDomain\"^?\"fSecurityDomainResponse\"^?\"fSecurityMode\"^?\"fSecurityModeResponse\"^?\"fProductionMode\"^?\"fProductionModeResponse\"^?\"fChipEpoch\"^?\"fChipEpochResponse\"^?\"fEnableMixMatch\"^?\"fEnableMixMatchResponse\"^?\"fSoCLiveNonce\"^?\"fSoCLiveNonceResponse\"^?\"fPrefixNeedsLogicalUnitNumber\"^?\"fPrefixNeedsLogicalUnitNumberResponse\"^?\"fSuffixNeedsLogicalUnitNumber\"^?\"fSuffixNeedsLogicalUnitNumberResponse\"^?\"fLogicalUnitNumber\"^?\"fLogicalUnitNumberResponse\"^?\"fTicketLongName\"^?\"fTicketLongNameResponse\"^?\"fRequiresPersonalization\"^?\"fRequiresPersonalizationResponse\"^?\"fApBoardID\"^?\"fApBoardIDResponse\"^?\"fApChipID\"^?\"fApChipIDResponse\"^?\"fApProductionMode\"^?\"fApProductionModeResponse\"^?\"fApSecurityMode\"^?\"fApSecurityModeResponse\"^?\"fHardwareSpecific\"^?\"fHardwareSpecificResponse\"^?\"fNonce\"^?\"fNonceResponse\"^?\"fLife\"^?\"fLifeResponse\"^?\"fProvisioning\"^?\"fProvisioningResponse\"^?\"fManifestEpoch\"^?\"fManifestEpochResponse\"^?\"fManifestSuffix\"^?\"fManifestSuffixResponse\"^?\"fNonceSeed\"^?\"fNonceSeedResponse\"^?\"fNonceHash\"^?\"fNonceHashResponse\"^?\"fRealHdcpKeyPresent\"^?\"fRealHdcpKeyPresentResponse\"^?\"fFTABGeneration\"^?\"fFTABGenerationResponse\"^?}}"
+ "{uarpPlatformEndpointCallbacks=\"fRequestBuffer\"^?\"fReturnBuffer\"^?\"fRequestTransmitMsgBuffer\"^?\"fReturnTransmitMsgBuffer\"^?\"fSendMessage\"^?\"fDataTransferPause\"^?\"fDataTransferPauseAck\"^?\"fDataTransferResume\"^?\"fDataTransferResumeAck\"^?\"fSuperBinaryOffered\"^?\"fDynamicAssetOffered\"^?\"fApplyStagedAssets\"^?\"fApplyStagedAssetsResponse\"^?\"fManufacturerName\"^?\"fManufacturerNameResponse\"^?\"fModelName\"^?\"fModelNameResponse\"^?\"fSerialNumber\"^?\"fSerialNumberResponse\"^?\"fHardwareVersion\"^?\"fHardwareVersionResponse\"^?\"fActiveFirmwareVersion2\"^?\"fActiveFirmwareVersionResponse\"^?\"fStagedFirmwareVersion2\"^?\"fStagedFirmwareVersionResponse\"^?\"fLastError\"^?\"fLastErrorResponse\"^?\"fStatisticsResponse\"^?\"fAssetSolicitation\"^?\"fRescindAllAssets\"^?\"fRescindAllAssetsAck\"^?\"fLayer2WatchdogSet\"^?\"fLayer2WatchdogCancel\"^?\"fMonotonicClockTime\"^?\"fProtocolVersion\"^?\"fFriendlyName\"^?\"fFriendlyNameResponse\"^?\"fDiscoveredEndpointID\"^?\"fDiscoveredComponent\"^?\"fBulkInfoQuery\"^?\"fBulkInfoResponse\"^?\"fDecompressBuffer\"^?\"fCompressBuffer\"^?\"fHashInfo\"^?\"fHashInit\"^?\"fHashUpdate\"^?\"fHashFinal\"^?\"fHashLog\"^?\"fLogPacket\"^?\"fLogError\"^?\"fLogInfo\"^?\"fLogDebug\"^?\"fLogFault\"^?\"fDownstreamDiscovery\"^?\"fDownstreamReachable2\"^?\"fDownstreamUnreachable2\"^?\"fDownstreamReleased2\"^?\"fDownstreamRecvMessage\"^?\"fNoFirmwareUpdateAvailable\"^?\"fVendorSpecificRecvMsg\"^?\"fVendorSpecificCheckExpectedResponse\"^?\"fVendorSpecificCheckValidToSend\"^?\"fVendorSpecificExceededRetries\"^?\"fActiveFirmwareVersion\"^?\"fStagedFirmwareVersion\"^?\"fTxWatchdogSet\"^?\"fTxWatchdogCancel\"^?\"fDownstreamReachable\"^?\"fDownstreamUnreachable\"^?\"fDownstreamReleased\"^?}"
+ "{uarpPlatformOptionsObj=\"maxTxPayloadLength\"I\"maxRxPayloadLength\"I\"payloadWindowLength\"I\"protocolVersion\"S\"reofferFirmwareOnSync\"C\"responseTimeout\"S\"retryLimit\"S\"maxTransmitsInFlight\"S\"endpointType\"i\"solicitationQueueDepth\"S\"txBufferOverhead\"S\"upgradeOnly\"C\"numPreallocatedBuffers\"S\"supportsBulkInfoQueries\"C\"useHostPushModel\"C}"
+ "{uarpPlatformRemoteEndpoint=\"_options\"{uarpPlatformOptionsObj=\"maxTxPayloadLength\"I\"maxRxPayloadLength\"I\"payloadWindowLength\"I\"protocolVersion\"S\"reofferFirmwareOnSync\"C\"responseTimeout\"S\"retryLimit\"S\"maxTransmitsInFlight\"S\"endpointType\"i\"solicitationQueueDepth\"S\"txBufferOverhead\"S\"upgradeOnly\"C\"numPreallocatedBuffers\"S\"supportsBulkInfoQueries\"C\"useHostPushModel\"C}\"pDelegate\"^v\"selectedProtocolVersion\"S\"supportsBulkInfoQueries\"S\"useHostPushModel\"S\"isWatchdogSet\"C\"_remoteEndpointID\"i\"dataTransferAllowed\"C\"dataTransferAllowedLocal\"C\"txMsgID\"S\"lastRxMsgID\"S\"uarpStats\"{UARPStatistics=\"packetsNoVersionAgreement\"I\"packetsMissed\"I\"packetsDuplicate\"I\"packetsOutOfOrder\"I}\"_solicitationQueue\"^{UARP4ccTag}\"pStreamingCtx\"^{uarpPlatformStreamingBuffer}\"pTxQueueAvailable\"^{uarpPlatformTransmitBufferEntry}\"pTxQueuePendingResponses\"^{uarpPlatformTransmitBufferEntry}\"downstreamID\"S\"activeFirmwareVersion\"{UARPVersion=\"major\"I\"minor\"I\"release\"I\"build\"I}\"stagedFirmwareVersion\"{UARPVersion=\"major\"I\"minor\"I\"release\"I\"build\"I}\"pUpstreamEP\"^{uarpPlatformRemoteEndpoint}}"
- "<ROLE=%s> UARP.LAYER2.DATA.RESP Outstanding Data Request <%s>, offset=0x%08x, requestedlength=%u"
- "@32@0:8^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?CIIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}16@24"
- "I32@0:8@16^{uarpPlatformOptionsObj=IIISCSSSiSSC}24"
- "T^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?CIIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}},R,V_pAsset"
- "^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?CIIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}"
- "^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?CIIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}16@0:8"
- "^{uarpPlatformEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSC}^v{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}^viI^^{uarpPlatformRemoteEndpoint}^{uarpPlatformAsset}iCi^?S}16@0:8"
- "^{uarpPlatformRemoteEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSC}^vSCiCCSS{UARPStatistics=IIII}^{UARP4ccTag}^{uarpPlatformStreamingBuffer}S^^{uarpPlatformTransmitBufferEntry}S^^{uarpPlatformTransmitBufferEntry}^{uarpPlatformTransmitBufferEntry}S{UARPVersion=IIII}{UARPVersion=IIII}^{uarpPlatformRemoteEndpoint}}16@0:8"
- "{uarpPlatformEndpoint=\"_options\"{uarpPlatformOptionsObj=\"maxTxPayloadLength\"I\"maxRxPayloadLength\"I\"payloadWindowLength\"I\"protocolVersion\"S\"reofferFirmwareOnSync\"C\"responseTimeout\"S\"retryLimit\"S\"maxTransmitsInFlight\"S\"endpointType\"i\"solicitationQueueDepth\"S\"txBufferOverhead\"S\"upgradeOnly\"C}\"pVendorExtension\"^v\"protectedCallbacks\"{uarpPlatformEndpointCallbacks=\"fRequestBuffer\"^?\"fReturnBuffer\"^?\"fRequestTransmitMsgBuffer\"^?\"fReturnTransmitMsgBuffer\"^?\"fSendMessage\"^?\"fDataTransferPause\"^?\"fDataTransferPauseAck\"^?\"fDataTransferResume\"^?\"fDataTransferResumeAck\"^?\"fSuperBinaryOffered\"^?\"fDynamicAssetOffered\"^?\"fApplyStagedAssets\"^?\"fApplyStagedAssetsResponse\"^?\"fManufacturerName\"^?\"fManufacturerNameResponse\"^?\"fModelName\"^?\"fModelNameResponse\"^?\"fSerialNumber\"^?\"fSerialNumberResponse\"^?\"fHardwareVersion\"^?\"fHardwareVersionResponse\"^?\"fActiveFirmwareVersion2\"^?\"fActiveFirmwareVersionResponse\"^?\"fStagedFirmwareVersion2\"^?\"fStagedFirmwareVersionResponse\"^?\"fLastError\"^?\"fLastErrorResponse\"^?\"fStatisticsResponse\"^?\"fAssetSolicitation\"^?\"fRescindAllAssets\"^?\"fRescindAllAssetsAck\"^?\"fLayer2WatchdogSet\"^?\"fLayer2WatchdogCancel\"^?\"fProtocolVersion\"^?\"fFriendlyName\"^?\"fFriendlyNameResponse\"^?\"fDecompressBuffer\"^?\"fCompressBuffer\"^?\"fHashInfo\"^?\"fHashInit\"^?\"fHashUpdate\"^?\"fHashFinal\"^?\"fHashLog\"^?\"fLogPacket\"^?\"fLogError\"^?\"fLogInfo\"^?\"fLogDebug\"^?\"fLogFault\"^?\"fDownstreamDiscovery\"^?\"fDownstreamReachable\"^?\"fDownstreamUnreachable\"^?\"fDownstreamReleased\"^?\"fDownstreamRecvMessage\"^?\"fNoFirmwareUpdateAvailable\"^?\"fVendorSpecificRecvMsg\"^?\"fVendorSpecificCheckExpectedResponse\"^?\"fVendorSpecificCheckValidToSend\"^?\"fVendorSpecificExceededRetries\"^?\"fActiveFirmwareVersion\"^?\"fStagedFirmwareVersion\"^?\"fTxWatchdogSet\"^?\"fTxWatchdogCancel\"^?}\"pDelegate\"^v\"role\"i\"numRemoteEndpointSlots\"I\"pRemoteEPs\"^^{uarpPlatformRemoteEndpoint}\"pAssetList\"^{uarpPlatformAsset}\"nextTxAssetID\"i\"rxLock\"C\"nextRemoteEndpointID\"i\"fVendorSpecific\"^?\"nextDownstreamID\"S}"
- "{uarpPlatformEndpointApple=\"supportsPersonalization\"C\"supportsHeySiri\"C\"supportsJustSiri\"C\"supportsVoiceAssist\"C\"callbacks\"{uarpPlatformEndpointAppleCallbacks=\"fAppleModelNumber\"^?\"fAppleModelNumberResponse\"^?\"fHwFusingType\"^?\"fHwFusingTypeResponse\"^?\"fManifestPrefix\"^?\"fManifestPrefixResponse\"^?\"fBoardID\"^?\"fBoardIDResponse\"^?\"fChipID\"^?\"fChipIDResponse\"^?\"fChipRevision\"^?\"fChipRevisionResponse\"^?\"fECID\"^?\"fECIDResponse\"^?\"fECIDData\"^?\"fECIDDataResponse\"^?\"fSecurityDomain\"^?\"fSecurityDomainResponse\"^?\"fSecurityMode\"^?\"fSecurityModeResponse\"^?\"fProductionMode\"^?\"fProductionModeResponse\"^?\"fChipEpoch\"^?\"fChipEpochResponse\"^?\"fEnableMixMatch\"^?\"fEnableMixMatchResponse\"^?\"fSoCLiveNonce\"^?\"fSoCLiveNonceResponse\"^?\"fPrefixNeedsLogicalUnitNumber\"^?\"fPrefixNeedsLogicalUnitNumberResponse\"^?\"fSuffixNeedsLogicalUnitNumber\"^?\"fSuffixNeedsLogicalUnitNumberResponse\"^?\"fLogicalUnitNumber\"^?\"fLogicalUnitNumberResponse\"^?\"fTicketLongName\"^?\"fTicketLongNameResponse\"^?\"fRequiresPersonalization\"^?\"fRequiresPersonalizationResponse\"^?\"fApBoardID\"^?\"fApBoardIDResponse\"^?\"fApChipID\"^?\"fApChipIDResponse\"^?\"fApProductionMode\"^?\"fApProductionModeResponse\"^?\"fApSecurityMode\"^?\"fApSecurityModeResponse\"^?\"fHardwareSpecific\"^?\"fHardwareSpecificResponse\"^?\"fNonce\"^?\"fNonceResponse\"^?\"fLife\"^?\"fLifeResponse\"^?\"fProvisioning\"^?\"fProvisioningResponse\"^?\"fManifestEpoch\"^?\"fManifestEpochResponse\"^?\"fManifestSuffix\"^?\"fManifestSuffixResponse\"^?}}"
- "{uarpPlatformEndpointCallbacks=\"fRequestBuffer\"^?\"fReturnBuffer\"^?\"fRequestTransmitMsgBuffer\"^?\"fReturnTransmitMsgBuffer\"^?\"fSendMessage\"^?\"fDataTransferPause\"^?\"fDataTransferPauseAck\"^?\"fDataTransferResume\"^?\"fDataTransferResumeAck\"^?\"fSuperBinaryOffered\"^?\"fDynamicAssetOffered\"^?\"fApplyStagedAssets\"^?\"fApplyStagedAssetsResponse\"^?\"fManufacturerName\"^?\"fManufacturerNameResponse\"^?\"fModelName\"^?\"fModelNameResponse\"^?\"fSerialNumber\"^?\"fSerialNumberResponse\"^?\"fHardwareVersion\"^?\"fHardwareVersionResponse\"^?\"fActiveFirmwareVersion2\"^?\"fActiveFirmwareVersionResponse\"^?\"fStagedFirmwareVersion2\"^?\"fStagedFirmwareVersionResponse\"^?\"fLastError\"^?\"fLastErrorResponse\"^?\"fStatisticsResponse\"^?\"fAssetSolicitation\"^?\"fRescindAllAssets\"^?\"fRescindAllAssetsAck\"^?\"fLayer2WatchdogSet\"^?\"fLayer2WatchdogCancel\"^?\"fProtocolVersion\"^?\"fFriendlyName\"^?\"fFriendlyNameResponse\"^?\"fDecompressBuffer\"^?\"fCompressBuffer\"^?\"fHashInfo\"^?\"fHashInit\"^?\"fHashUpdate\"^?\"fHashFinal\"^?\"fHashLog\"^?\"fLogPacket\"^?\"fLogError\"^?\"fLogInfo\"^?\"fLogDebug\"^?\"fLogFault\"^?\"fDownstreamDiscovery\"^?\"fDownstreamReachable\"^?\"fDownstreamUnreachable\"^?\"fDownstreamReleased\"^?\"fDownstreamRecvMessage\"^?\"fNoFirmwareUpdateAvailable\"^?\"fVendorSpecificRecvMsg\"^?\"fVendorSpecificCheckExpectedResponse\"^?\"fVendorSpecificCheckValidToSend\"^?\"fVendorSpecificExceededRetries\"^?\"fActiveFirmwareVersion\"^?\"fStagedFirmwareVersion\"^?\"fTxWatchdogSet\"^?\"fTxWatchdogCancel\"^?}"
- "{uarpPlatformOptionsObj=\"maxTxPayloadLength\"I\"maxRxPayloadLength\"I\"payloadWindowLength\"I\"protocolVersion\"S\"reofferFirmwareOnSync\"C\"responseTimeout\"S\"retryLimit\"S\"maxTransmitsInFlight\"S\"endpointType\"i\"solicitationQueueDepth\"S\"txBufferOverhead\"S\"upgradeOnly\"C}"
- "{uarpPlatformRemoteEndpoint=\"_options\"{uarpPlatformOptionsObj=\"maxTxPayloadLength\"I\"maxRxPayloadLength\"I\"payloadWindowLength\"I\"protocolVersion\"S\"reofferFirmwareOnSync\"C\"responseTimeout\"S\"retryLimit\"S\"maxTransmitsInFlight\"S\"endpointType\"i\"solicitationQueueDepth\"S\"txBufferOverhead\"S\"upgradeOnly\"C}\"pDelegate\"^v\"selectedProtocolVersion\"S\"isWatchdogSet\"C\"_remoteEndpointID\"i\"dataTransferAllowed\"C\"dataTransferAllowedLocal\"C\"txMsgID\"S\"lastRxMsgID\"S\"uarpStats\"{UARPStatistics=\"packetsNoVersionAgreement\"I\"packetsMissed\"I\"packetsDuplicate\"I\"packetsOutOfOrder\"I}\"_solicitationQueue\"^{UARP4ccTag}\"pStreamingCtx\"^{uarpPlatformStreamingBuffer}\"numTxBufferAvailableSlots\"S\"pTxBufferAvailable\"^^{uarpPlatformTransmitBufferEntry}\"numTxBufferPendingSlots\"S\"pTxBufferPending\"^^{uarpPlatformTransmitBufferEntry}\"pTxBufferInFlight\"^{uarpPlatformTransmitBufferEntry}\"downstreamID\"S\"activeFirmwareVersion\"{UARPVersion=\"major\"I\"minor\"I\"release\"I\"build\"I}\"stagedFirmwareVersion\"{UARPVersion=\"major\"I\"minor\"I\"release\"I\"build\"I}\"pUpstreamEP\"^{uarpPlatformRemoteEndpoint}}"

```
