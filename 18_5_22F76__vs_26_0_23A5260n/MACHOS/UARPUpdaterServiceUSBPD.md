## UARPUpdaterServiceUSBPD

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceUSBPD.xpc/UARPUpdaterServiceUSBPD`

```diff

-1207.120.19.0.0
-  __TEXT.__text: 0x24064
-  __TEXT.__auth_stubs: 0x810
-  __TEXT.__objc_stubs: 0x3360
-  __TEXT.__objc_methlist: 0x18f0
-  __TEXT.__const: 0xc0
-  __TEXT.__oslogstring: 0x25a1
-  __TEXT.__cstring: 0x272b
-  __TEXT.__objc_classname: 0x205
-  __TEXT.__objc_methtype: 0x338e
-  __TEXT.__objc_methname: 0x42d9
-  __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0x770
-  __DATA_CONST.__auth_got: 0x418
-  __DATA_CONST.__got: 0x168
-  __DATA_CONST.__const: 0x5c0
-  __DATA_CONST.__cfstring: 0x600
+1338.0.21.0.2
+  __TEXT.__text: 0x259c8
+  __TEXT.__auth_stubs: 0x870
+  __TEXT.__objc_stubs: 0x33c0
+  __TEXT.__objc_methlist: 0x19c0
+  __TEXT.__const: 0xd0
+  __TEXT.__oslogstring: 0x26a9
+  __TEXT.__cstring: 0x2f45
+  __TEXT.__objc_classname: 0x209
+  __TEXT.__objc_methtype: 0x37e9
+  __TEXT.__gcc_except_tab: 0x24
+  __TEXT.__objc_methname: 0x45ba
+  __TEXT.__unwind_info: 0x798
+  __DATA_CONST.__auth_got: 0x448
+  __DATA_CONST.__got: 0x1a0
+  __DATA_CONST.__const: 0x718
+  __DATA_CONST.__cfstring: 0x620
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x3528
-  __DATA.__objc_selrefs: 0xfb0
-  __DATA.__objc_ivar: 0x228
+  __DATA.__objc_const: 0x35b0
+  __DATA.__objc_selrefs: 0x1030
+  __DATA.__objc_ivar: 0x22c
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x375
   __DATA.__bss: 0x1174

   - /usr/lib/libcompression.dylib
   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 22548900-3EDD-3AE6-8EF7-61890A4EF32C
-  Functions: 1029
-  Symbols:   529
-  CStrings:  1504
+  UUID: 870441B0-D504-3EEE-91FC-5129B881DD63
+  Functions: 1066
+  Symbols:   571
+  CStrings:  1591
 
Symbols:
+ _AUSandboxPlatformInitWithBundleIdentifierHomeDirectory
+ _AUSandboxPlatformInitWithHomeDirectory
+ _OBJC_CLASS_$_UARPServiceUpdaterDASMatchingRule
+ _UARPLayer2EndpointBulkInformationQuery
+ _UARPLayer2EndpointBulkInformationResponse
+ _UARPLayer2EndpointIDComponents
+ _UARPLayer2EndpointIDs
+ _UARPLayer2MonotonicClockTime
+ _UARPProtocolVersionRequiresDownstreamMessageACK
+ _UARPProtocolVersionResponseAdjustByProtocolVersion
+ _XPC_ACTIVITY_DELAY
+ _XPC_ACTIVITY_INTERVAL_1_DAY
+ _XPC_ACTIVITY_PRIORITY
+ _XPC_ACTIVITY_PRIORITY_MAINTENANCE
+ _XPC_ACTIVITY_REPEATING
+ _XPC_ACTIVITY_REQUIRE_NETWORK_CONNECTIVITY
+ __CFXPCCreateCFObjectFromXPCObject
+ _calloc
+ _uarpAllocateTransmitBuffers
+ _uarpMessageAdjustedForEndpointID
+ _uarpMessagePrintToBuffer
+ _uarpMessageTypeToString
+ _uarpPlatformAssetFindFirmware
+ _uarpPlatformCleanupAssets
+ _uarpPlatformConfigureEndpointIDs
+ _uarpPlatformConfigureEndpointTags
+ _uarpPlatformDownstreamEndpointAddToList
+ _uarpPlatformDownstreamEndpointDelegateFindOnListByID
+ _uarpPlatformDownstreamEndpointFindOnList
+ _uarpPlatformDownstreamEndpointFindOnListByDelegate
+ _uarpPlatformDownstreamEndpointIDFindOnListByDelegate
+ _uarpPlatformDownstreamEndpointRemoveFromList
+ _uarpPlatformEndpointBulkInfoResponse
+ _uarpPlatformEndpointBulkInfoResponseAddTLV
+ _uarpPlatformEndpointDeinit
+ _uarpPlatformGetSupportsBulkInfoQueries
+ _uarpPlatformGetUseHostPushModel
+ _uarpPlatformReleaseEndpointIDs
+ _uarpPlatformReleaseEndpointTags
+ _uarpPlatformSendDownstreamMessageWithDownstreamID
+ _uarpRemoteEndpointForAsset
+ _uarpTransmitMessageToDownstreamEndpointID
+ _uarpTransmitQueuePurge
+ _uarpTransmitQueueReclaimEntries
+ _xpc_dictionary_create
+ _xpc_dictionary_set_bool
+ _xpc_dictionary_set_int64
+ _xpc_dictionary_set_string
- _uarpAssetQueueSolicitation
- _uarpPlatformAssetApproveOfferVersion
- _uarpPlatformEndpointIsMessageTypePending
- _uarpPlatformTransmitQueueLogEntry
- _uarpTransmitQueuePendingEntryComplete
- _uarpTransmitQueueProcessRecv
CStrings:
+ "%s: 4cc operation failed <0x%02x>, taskResult <0x%X>, iteration %d. %@"
+ "%s: <ROLE=%s> : Add Downstream Endpoint <Local=%p> <Remote=%p> DS.ID <%hu>"
+ "%s: <ROLE=%s> : RemoveDownstream Endpoint <Local=%p> <Remote=%p> DS.ID <%hu>"
+ "%s: Accessories: %@"
+ "%s: DAS Matching Rules are %@"
+ "%s: ESPRESSO:Bonus Message <type=0x%04x, length=x0x%04x, id=0x%04x>"
+ "%s: ESPRESSO:Message <type=0x%04x, id=0x%04x> Length too big ! expected <%u>, got <%u>"
+ "%s: ESPRESSO:Message <type=0x%04x, id=0x%04x> Length too small ! expected <%u>, got <%u>"
+ "%s: Look for power adapters on all HPMs"
+ "%s: Solicit dynamic assets for tracked devices"
+ "%s: atomic command failed <0x%08x>, taskResult <0x%X>, iteration %d. %@"
+ "%s: doAtomic4CC failed with taskResult: 0x%08x"
+ "-[UARPUSBPDUpdater dasActivityReceived]_block_invoke"
+ "-[UARPUSBPDUpdater handlePeriodicAssetSolicitation]"
+ "-[UARPUpdaterServiceUSBPD dasActivityReceived:]"
+ "-[UARPUpdaterServiceUSBPD getDASActivityListWithReply:]"
+ "<ROLE=%s> ESPRESSO: UARP.LAYER2.RECV.MSG: Length too small <%u>"
+ "<ROLE=%s> UARP.LAYER2.DATA.RESP offset=0x%08x, requestedlength=%u"
+ "@\"UARPUSBPDAccessory\""
+ "@32@0:8@16^{uarpPlatformOptionsObj=IIISCSSSiSSCSCC}24"
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
+ "B40@0:8@16^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?IIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}24^@32"
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
+ "Found a supported power adapter on MagSafe port, check for cable first %@"
+ "Hold update for MagSafe accessory %@ until Power Adapter notifications completes"
+ "Information Request"
+ "Information Response"
+ "Invalid EndpointID"
+ "No Firmware Update Available"
+ "No Firmware Update Available Ack"
+ "Sync"
+ "T^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?IIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}},R"
+ "T^{uarpPlatformEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSCSCC}^v{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}^viI^^{uarpPlatformRemoteEndpoint}^{uarpPlatformAsset}iCi^?S^{uarpLayer2EndpointIDInfo}S^{uarpDownstreamEndpointObj}I^{uarpMemoryTracker}},R"
+ "T^{uarpPlatformRemoteEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSCSCC}^vSSSCiCCSS{UARPStatistics=IIII}^{UARP4ccTag}^{uarpPlatformStreamingBuffer}^{uarpPlatformTransmitBufferEntry}^{uarpPlatformTransmitBufferEntry}S{UARPVersion=IIII}{UARPVersion=IIII}^{uarpPlatformRemoteEndpoint}},R"
+ "USBPDPeriodicLaunchActivity"
+ "Vendor Specific"
+ "Version Discovery Request"
+ "Version Discovery Response"
+ "^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?IIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}"
+ "^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?IIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}16@0:8"
+ "^{uarpPlatformEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSCSCC}^v{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}^viI^^{uarpPlatformRemoteEndpoint}^{uarpPlatformAsset}iCi^?S^{uarpLayer2EndpointIDInfo}S^{uarpDownstreamEndpointObj}I^{uarpMemoryTracker}}16@0:8"
+ "^{uarpPlatformRemoteEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSCSCC}^vSSSCiCCSS{UARPStatistics=IIII}^{UARP4ccTag}^{uarpPlatformStreamingBuffer}^{uarpPlatformTransmitBufferEntry}^{uarpPlatformTransmitBufferEntry}S{UARPVersion=IIII}{UARPVersion=IIII}^{uarpPlatformRemoteEndpoint}}16@0:8"
+ "dasActivityReceived"
+ "handlePeriodicAssetSolicitation"
+ "initWithIdentifier:matchingDictionary:"
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
+ "uarpMsgRecvDownstreamEndpointReachable"
+ "uarpMsgRecvDownstreamEndpointUnreachable"
+ "uarpMsgRecvDownstreamEndpointUnreachableAck"
+ "uarpPlatformEndpointRecvMessage"
+ "v36@0:8@\"UARPAccessory\"16B24@\"NSError\"28"
+ "v36@0:8@16B24@28"
+ "v40@0:8@\"UARPAccessory\"16@\"NSData\"24@\"NSError\"32"
+ "v40@0:8@\"UARPAccessory\"16Q24@\"NSError\"32"
+ "v40@0:8@16Q24@32"
+ "{uarpPlatformEndpoint=\"_options\"{uarpPlatformOptionsObj=\"maxTxPayloadLength\"I\"maxRxPayloadLength\"I\"payloadWindowLength\"I\"protocolVersion\"S\"reofferFirmwareOnSync\"C\"responseTimeout\"S\"retryLimit\"S\"maxTransmitsInFlight\"S\"endpointType\"i\"solicitationQueueDepth\"S\"txBufferOverhead\"S\"upgradeOnly\"C\"numPreallocatedBuffers\"S\"supportsBulkInfoQueries\"C\"useHostPushModel\"C}\"pVendorExtension\"^v\"protectedCallbacks\"{uarpPlatformEndpointCallbacks=\"fRequestBuffer\"^?\"fReturnBuffer\"^?\"fRequestTransmitMsgBuffer\"^?\"fReturnTransmitMsgBuffer\"^?\"fSendMessage\"^?\"fDataTransferPause\"^?\"fDataTransferPauseAck\"^?\"fDataTransferResume\"^?\"fDataTransferResumeAck\"^?\"fSuperBinaryOffered\"^?\"fDynamicAssetOffered\"^?\"fApplyStagedAssets\"^?\"fApplyStagedAssetsResponse\"^?\"fManufacturerName\"^?\"fManufacturerNameResponse\"^?\"fModelName\"^?\"fModelNameResponse\"^?\"fSerialNumber\"^?\"fSerialNumberResponse\"^?\"fHardwareVersion\"^?\"fHardwareVersionResponse\"^?\"fActiveFirmwareVersion2\"^?\"fActiveFirmwareVersionResponse\"^?\"fStagedFirmwareVersion2\"^?\"fStagedFirmwareVersionResponse\"^?\"fLastError\"^?\"fLastErrorResponse\"^?\"fStatisticsResponse\"^?\"fAssetSolicitation\"^?\"fRescindAllAssets\"^?\"fRescindAllAssetsAck\"^?\"fLayer2WatchdogSet\"^?\"fLayer2WatchdogCancel\"^?\"fMonotonicClockTime\"^?\"fProtocolVersion\"^?\"fFriendlyName\"^?\"fFriendlyNameResponse\"^?\"fDiscoveredEndpointID\"^?\"fDiscoveredComponent\"^?\"fBulkInfoQuery\"^?\"fBulkInfoResponse\"^?\"fDecompressBuffer\"^?\"fCompressBuffer\"^?\"fHashInfo\"^?\"fHashInit\"^?\"fHashUpdate\"^?\"fHashFinal\"^?\"fHashLog\"^?\"fLogPacket\"^?\"fLogError\"^?\"fLogInfo\"^?\"fLogDebug\"^?\"fLogFault\"^?\"fDownstreamDiscovery\"^?\"fDownstreamReachable2\"^?\"fDownstreamUnreachable2\"^?\"fDownstreamReleased2\"^?\"fDownstreamRecvMessage\"^?\"fNoFirmwareUpdateAvailable\"^?\"fVendorSpecificRecvMsg\"^?\"fVendorSpecificCheckExpectedResponse\"^?\"fVendorSpecificCheckValidToSend\"^?\"fVendorSpecificExceededRetries\"^?\"fActiveFirmwareVersion\"^?\"fStagedFirmwareVersion\"^?\"fTxWatchdogSet\"^?\"fTxWatchdogCancel\"^?\"fDownstreamReachable\"^?\"fDownstreamUnreachable\"^?\"fDownstreamReleased\"^?}\"pDelegate\"^v\"role\"i\"numRemoteEndpointSlots\"I\"pRemoteEPs\"^^{uarpPlatformRemoteEndpoint}\"pAssetList\"^{uarpPlatformAsset}\"nextTxAssetID\"i\"rxLock\"C\"nextRemoteEndpointID\"i\"fVendorSpecific\"^?\"numEndpointIDs\"S\"pEndpointIDInfo\"^{uarpLayer2EndpointIDInfo}\"nextDownstreamID\"S\"pDownstreamEndpoints\"^{uarpDownstreamEndpointObj}\"numMemoryTrackers\"I\"pMemoryTracker\"^{uarpMemoryTracker}}"
+ "{uarpPlatformEndpointApple=\"supportsPersonalization\"C\"supportsHeySiri\"C\"supportsJustSiri\"C\"supportsVoiceAssist\"C\"callbacks\"{uarpPlatformEndpointAppleCallbacks=\"fAppleModelNumber\"^?\"fAppleModelNumberResponse\"^?\"fHwFusingType\"^?\"fHwFusingTypeResponse\"^?\"fManifestPrefix\"^?\"fManifestPrefixResponse\"^?\"fBoardID\"^?\"fBoardIDResponse\"^?\"fChipID\"^?\"fChipIDResponse\"^?\"fChipRevision\"^?\"fChipRevisionResponse\"^?\"fECID\"^?\"fECIDResponse\"^?\"fECIDData\"^?\"fECIDDataResponse\"^?\"fSecurityDomain\"^?\"fSecurityDomainResponse\"^?\"fSecurityMode\"^?\"fSecurityModeResponse\"^?\"fProductionMode\"^?\"fProductionModeResponse\"^?\"fChipEpoch\"^?\"fChipEpochResponse\"^?\"fEnableMixMatch\"^?\"fEnableMixMatchResponse\"^?\"fSoCLiveNonce\"^?\"fSoCLiveNonceResponse\"^?\"fPrefixNeedsLogicalUnitNumber\"^?\"fPrefixNeedsLogicalUnitNumberResponse\"^?\"fSuffixNeedsLogicalUnitNumber\"^?\"fSuffixNeedsLogicalUnitNumberResponse\"^?\"fLogicalUnitNumber\"^?\"fLogicalUnitNumberResponse\"^?\"fTicketLongName\"^?\"fTicketLongNameResponse\"^?\"fRequiresPersonalization\"^?\"fRequiresPersonalizationResponse\"^?\"fApBoardID\"^?\"fApBoardIDResponse\"^?\"fApChipID\"^?\"fApChipIDResponse\"^?\"fApProductionMode\"^?\"fApProductionModeResponse\"^?\"fApSecurityMode\"^?\"fApSecurityModeResponse\"^?\"fHardwareSpecific\"^?\"fHardwareSpecificResponse\"^?\"fNonce\"^?\"fNonceResponse\"^?\"fLife\"^?\"fLifeResponse\"^?\"fProvisioning\"^?\"fProvisioningResponse\"^?\"fManifestEpoch\"^?\"fManifestEpochResponse\"^?\"fManifestSuffix\"^?\"fManifestSuffixResponse\"^?\"fNonceSeed\"^?\"fNonceSeedResponse\"^?\"fNonceHash\"^?\"fNonceHashResponse\"^?\"fRealHdcpKeyPresent\"^?\"fRealHdcpKeyPresentResponse\"^?\"fFTABGeneration\"^?\"fFTABGenerationResponse\"^?}}"
+ "{uarpPlatformEndpointCallbacks=\"fRequestBuffer\"^?\"fReturnBuffer\"^?\"fRequestTransmitMsgBuffer\"^?\"fReturnTransmitMsgBuffer\"^?\"fSendMessage\"^?\"fDataTransferPause\"^?\"fDataTransferPauseAck\"^?\"fDataTransferResume\"^?\"fDataTransferResumeAck\"^?\"fSuperBinaryOffered\"^?\"fDynamicAssetOffered\"^?\"fApplyStagedAssets\"^?\"fApplyStagedAssetsResponse\"^?\"fManufacturerName\"^?\"fManufacturerNameResponse\"^?\"fModelName\"^?\"fModelNameResponse\"^?\"fSerialNumber\"^?\"fSerialNumberResponse\"^?\"fHardwareVersion\"^?\"fHardwareVersionResponse\"^?\"fActiveFirmwareVersion2\"^?\"fActiveFirmwareVersionResponse\"^?\"fStagedFirmwareVersion2\"^?\"fStagedFirmwareVersionResponse\"^?\"fLastError\"^?\"fLastErrorResponse\"^?\"fStatisticsResponse\"^?\"fAssetSolicitation\"^?\"fRescindAllAssets\"^?\"fRescindAllAssetsAck\"^?\"fLayer2WatchdogSet\"^?\"fLayer2WatchdogCancel\"^?\"fMonotonicClockTime\"^?\"fProtocolVersion\"^?\"fFriendlyName\"^?\"fFriendlyNameResponse\"^?\"fDiscoveredEndpointID\"^?\"fDiscoveredComponent\"^?\"fBulkInfoQuery\"^?\"fBulkInfoResponse\"^?\"fDecompressBuffer\"^?\"fCompressBuffer\"^?\"fHashInfo\"^?\"fHashInit\"^?\"fHashUpdate\"^?\"fHashFinal\"^?\"fHashLog\"^?\"fLogPacket\"^?\"fLogError\"^?\"fLogInfo\"^?\"fLogDebug\"^?\"fLogFault\"^?\"fDownstreamDiscovery\"^?\"fDownstreamReachable2\"^?\"fDownstreamUnreachable2\"^?\"fDownstreamReleased2\"^?\"fDownstreamRecvMessage\"^?\"fNoFirmwareUpdateAvailable\"^?\"fVendorSpecificRecvMsg\"^?\"fVendorSpecificCheckExpectedResponse\"^?\"fVendorSpecificCheckValidToSend\"^?\"fVendorSpecificExceededRetries\"^?\"fActiveFirmwareVersion\"^?\"fStagedFirmwareVersion\"^?\"fTxWatchdogSet\"^?\"fTxWatchdogCancel\"^?\"fDownstreamReachable\"^?\"fDownstreamUnreachable\"^?\"fDownstreamReleased\"^?}"
+ "{uarpPlatformOptionsObj=\"maxTxPayloadLength\"I\"maxRxPayloadLength\"I\"payloadWindowLength\"I\"protocolVersion\"S\"reofferFirmwareOnSync\"C\"responseTimeout\"S\"retryLimit\"S\"maxTransmitsInFlight\"S\"endpointType\"i\"solicitationQueueDepth\"S\"txBufferOverhead\"S\"upgradeOnly\"C\"numPreallocatedBuffers\"S\"supportsBulkInfoQueries\"C\"useHostPushModel\"C}"
+ "{uarpPlatformRemoteEndpoint=\"_options\"{uarpPlatformOptionsObj=\"maxTxPayloadLength\"I\"maxRxPayloadLength\"I\"payloadWindowLength\"I\"protocolVersion\"S\"reofferFirmwareOnSync\"C\"responseTimeout\"S\"retryLimit\"S\"maxTransmitsInFlight\"S\"endpointType\"i\"solicitationQueueDepth\"S\"txBufferOverhead\"S\"upgradeOnly\"C\"numPreallocatedBuffers\"S\"supportsBulkInfoQueries\"C\"useHostPushModel\"C}\"pDelegate\"^v\"selectedProtocolVersion\"S\"supportsBulkInfoQueries\"S\"useHostPushModel\"S\"isWatchdogSet\"C\"_remoteEndpointID\"i\"dataTransferAllowed\"C\"dataTransferAllowedLocal\"C\"txMsgID\"S\"lastRxMsgID\"S\"uarpStats\"{UARPStatistics=\"packetsNoVersionAgreement\"I\"packetsMissed\"I\"packetsDuplicate\"I\"packetsOutOfOrder\"I}\"_solicitationQueue\"^{UARP4ccTag}\"pStreamingCtx\"^{uarpPlatformStreamingBuffer}\"pTxQueueAvailable\"^{uarpPlatformTransmitBufferEntry}\"pTxQueuePendingResponses\"^{uarpPlatformTransmitBufferEntry}\"downstreamID\"S\"activeFirmwareVersion\"{UARPVersion=\"major\"I\"minor\"I\"release\"I\"build\"I}\"stagedFirmwareVersion\"{UARPVersion=\"major\"I\"minor\"I\"release\"I\"build\"I}\"pUpstreamEP\"^{uarpPlatformRemoteEndpoint}}"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xc1"
- "%s: 4cc operation failed <0x%02x>, iteration %d. %@"
- "%s: Look for power adapters on all HPMs that don't have MagSafe"
- "%s: atomic command failed <0x%08x>, iteration %d. %@"
- "<ROLE=%s> UARP.LAYER2.DATA.RESP Outstanding Data Request <%s>, offset=0x%08x, requestedlength=%u"
- "@32@0:8@16^{uarpPlatformOptionsObj=IIISCSSSiSSC}24"
- "@32@0:8^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?CIIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}16@24"
- "B40@0:8@16^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?CIIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}24^@32"
- "Skip check (MagSafe) for power adapter on HPM %@"
- "T^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?CIIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}},R"
- "T^{uarpPlatformEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSC}^v{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}^viI^^{uarpPlatformRemoteEndpoint}^{uarpPlatformAsset}iCi^?S},R"
- "T^{uarpPlatformRemoteEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSC}^vSCiCCSS{UARPStatistics=IIII}^{UARP4ccTag}^{uarpPlatformStreamingBuffer}S^^{uarpPlatformTransmitBufferEntry}S^^{uarpPlatformTransmitBufferEntry}^{uarpPlatformTransmitBufferEntry}S{UARPVersion=IIII}{UARPVersion=IIII}^{uarpPlatformRemoteEndpoint}},R"
- "^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?CIIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}"
- "^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?CIIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}16@0:8"
- "^{uarpPlatformEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSC}^v{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}^viI^^{uarpPlatformRemoteEndpoint}^{uarpPlatformAsset}iCi^?S}16@0:8"
- "^{uarpPlatformRemoteEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSC}^vSCiCCSS{UARPStatistics=IIII}^{UARP4ccTag}^{uarpPlatformStreamingBuffer}S^^{uarpPlatformTransmitBufferEntry}S^^{uarpPlatformTransmitBufferEntry}^{uarpPlatformTransmitBufferEntry}S{UARPVersion=IIII}{UARPVersion=IIII}^{uarpPlatformRemoteEndpoint}}16@0:8"
- "{uarpPlatformEndpoint=\"_options\"{uarpPlatformOptionsObj=\"maxTxPayloadLength\"I\"maxRxPayloadLength\"I\"payloadWindowLength\"I\"protocolVersion\"S\"reofferFirmwareOnSync\"C\"responseTimeout\"S\"retryLimit\"S\"maxTransmitsInFlight\"S\"endpointType\"i\"solicitationQueueDepth\"S\"txBufferOverhead\"S\"upgradeOnly\"C}\"pVendorExtension\"^v\"protectedCallbacks\"{uarpPlatformEndpointCallbacks=\"fRequestBuffer\"^?\"fReturnBuffer\"^?\"fRequestTransmitMsgBuffer\"^?\"fReturnTransmitMsgBuffer\"^?\"fSendMessage\"^?\"fDataTransferPause\"^?\"fDataTransferPauseAck\"^?\"fDataTransferResume\"^?\"fDataTransferResumeAck\"^?\"fSuperBinaryOffered\"^?\"fDynamicAssetOffered\"^?\"fApplyStagedAssets\"^?\"fApplyStagedAssetsResponse\"^?\"fManufacturerName\"^?\"fManufacturerNameResponse\"^?\"fModelName\"^?\"fModelNameResponse\"^?\"fSerialNumber\"^?\"fSerialNumberResponse\"^?\"fHardwareVersion\"^?\"fHardwareVersionResponse\"^?\"fActiveFirmwareVersion2\"^?\"fActiveFirmwareVersionResponse\"^?\"fStagedFirmwareVersion2\"^?\"fStagedFirmwareVersionResponse\"^?\"fLastError\"^?\"fLastErrorResponse\"^?\"fStatisticsResponse\"^?\"fAssetSolicitation\"^?\"fRescindAllAssets\"^?\"fRescindAllAssetsAck\"^?\"fLayer2WatchdogSet\"^?\"fLayer2WatchdogCancel\"^?\"fProtocolVersion\"^?\"fFriendlyName\"^?\"fFriendlyNameResponse\"^?\"fDecompressBuffer\"^?\"fCompressBuffer\"^?\"fHashInfo\"^?\"fHashInit\"^?\"fHashUpdate\"^?\"fHashFinal\"^?\"fHashLog\"^?\"fLogPacket\"^?\"fLogError\"^?\"fLogInfo\"^?\"fLogDebug\"^?\"fLogFault\"^?\"fDownstreamDiscovery\"^?\"fDownstreamReachable\"^?\"fDownstreamUnreachable\"^?\"fDownstreamReleased\"^?\"fDownstreamRecvMessage\"^?\"fNoFirmwareUpdateAvailable\"^?\"fVendorSpecificRecvMsg\"^?\"fVendorSpecificCheckExpectedResponse\"^?\"fVendorSpecificCheckValidToSend\"^?\"fVendorSpecificExceededRetries\"^?\"fActiveFirmwareVersion\"^?\"fStagedFirmwareVersion\"^?\"fTxWatchdogSet\"^?\"fTxWatchdogCancel\"^?}\"pDelegate\"^v\"role\"i\"numRemoteEndpointSlots\"I\"pRemoteEPs\"^^{uarpPlatformRemoteEndpoint}\"pAssetList\"^{uarpPlatformAsset}\"nextTxAssetID\"i\"rxLock\"C\"nextRemoteEndpointID\"i\"fVendorSpecific\"^?\"nextDownstreamID\"S}"
- "{uarpPlatformEndpointApple=\"supportsPersonalization\"C\"supportsHeySiri\"C\"supportsJustSiri\"C\"supportsVoiceAssist\"C\"callbacks\"{uarpPlatformEndpointAppleCallbacks=\"fAppleModelNumber\"^?\"fAppleModelNumberResponse\"^?\"fHwFusingType\"^?\"fHwFusingTypeResponse\"^?\"fManifestPrefix\"^?\"fManifestPrefixResponse\"^?\"fBoardID\"^?\"fBoardIDResponse\"^?\"fChipID\"^?\"fChipIDResponse\"^?\"fChipRevision\"^?\"fChipRevisionResponse\"^?\"fECID\"^?\"fECIDResponse\"^?\"fECIDData\"^?\"fECIDDataResponse\"^?\"fSecurityDomain\"^?\"fSecurityDomainResponse\"^?\"fSecurityMode\"^?\"fSecurityModeResponse\"^?\"fProductionMode\"^?\"fProductionModeResponse\"^?\"fChipEpoch\"^?\"fChipEpochResponse\"^?\"fEnableMixMatch\"^?\"fEnableMixMatchResponse\"^?\"fSoCLiveNonce\"^?\"fSoCLiveNonceResponse\"^?\"fPrefixNeedsLogicalUnitNumber\"^?\"fPrefixNeedsLogicalUnitNumberResponse\"^?\"fSuffixNeedsLogicalUnitNumber\"^?\"fSuffixNeedsLogicalUnitNumberResponse\"^?\"fLogicalUnitNumber\"^?\"fLogicalUnitNumberResponse\"^?\"fTicketLongName\"^?\"fTicketLongNameResponse\"^?\"fRequiresPersonalization\"^?\"fRequiresPersonalizationResponse\"^?\"fApBoardID\"^?\"fApBoardIDResponse\"^?\"fApChipID\"^?\"fApChipIDResponse\"^?\"fApProductionMode\"^?\"fApProductionModeResponse\"^?\"fApSecurityMode\"^?\"fApSecurityModeResponse\"^?\"fHardwareSpecific\"^?\"fHardwareSpecificResponse\"^?\"fNonce\"^?\"fNonceResponse\"^?\"fLife\"^?\"fLifeResponse\"^?\"fProvisioning\"^?\"fProvisioningResponse\"^?\"fManifestEpoch\"^?\"fManifestEpochResponse\"^?\"fManifestSuffix\"^?\"fManifestSuffixResponse\"^?}}"
- "{uarpPlatformEndpointCallbacks=\"fRequestBuffer\"^?\"fReturnBuffer\"^?\"fRequestTransmitMsgBuffer\"^?\"fReturnTransmitMsgBuffer\"^?\"fSendMessage\"^?\"fDataTransferPause\"^?\"fDataTransferPauseAck\"^?\"fDataTransferResume\"^?\"fDataTransferResumeAck\"^?\"fSuperBinaryOffered\"^?\"fDynamicAssetOffered\"^?\"fApplyStagedAssets\"^?\"fApplyStagedAssetsResponse\"^?\"fManufacturerName\"^?\"fManufacturerNameResponse\"^?\"fModelName\"^?\"fModelNameResponse\"^?\"fSerialNumber\"^?\"fSerialNumberResponse\"^?\"fHardwareVersion\"^?\"fHardwareVersionResponse\"^?\"fActiveFirmwareVersion2\"^?\"fActiveFirmwareVersionResponse\"^?\"fStagedFirmwareVersion2\"^?\"fStagedFirmwareVersionResponse\"^?\"fLastError\"^?\"fLastErrorResponse\"^?\"fStatisticsResponse\"^?\"fAssetSolicitation\"^?\"fRescindAllAssets\"^?\"fRescindAllAssetsAck\"^?\"fLayer2WatchdogSet\"^?\"fLayer2WatchdogCancel\"^?\"fProtocolVersion\"^?\"fFriendlyName\"^?\"fFriendlyNameResponse\"^?\"fDecompressBuffer\"^?\"fCompressBuffer\"^?\"fHashInfo\"^?\"fHashInit\"^?\"fHashUpdate\"^?\"fHashFinal\"^?\"fHashLog\"^?\"fLogPacket\"^?\"fLogError\"^?\"fLogInfo\"^?\"fLogDebug\"^?\"fLogFault\"^?\"fDownstreamDiscovery\"^?\"fDownstreamReachable\"^?\"fDownstreamUnreachable\"^?\"fDownstreamReleased\"^?\"fDownstreamRecvMessage\"^?\"fNoFirmwareUpdateAvailable\"^?\"fVendorSpecificRecvMsg\"^?\"fVendorSpecificCheckExpectedResponse\"^?\"fVendorSpecificCheckValidToSend\"^?\"fVendorSpecificExceededRetries\"^?\"fActiveFirmwareVersion\"^?\"fStagedFirmwareVersion\"^?\"fTxWatchdogSet\"^?\"fTxWatchdogCancel\"^?}"
- "{uarpPlatformOptionsObj=\"maxTxPayloadLength\"I\"maxRxPayloadLength\"I\"payloadWindowLength\"I\"protocolVersion\"S\"reofferFirmwareOnSync\"C\"responseTimeout\"S\"retryLimit\"S\"maxTransmitsInFlight\"S\"endpointType\"i\"solicitationQueueDepth\"S\"txBufferOverhead\"S\"upgradeOnly\"C}"
- "{uarpPlatformRemoteEndpoint=\"_options\"{uarpPlatformOptionsObj=\"maxTxPayloadLength\"I\"maxRxPayloadLength\"I\"payloadWindowLength\"I\"protocolVersion\"S\"reofferFirmwareOnSync\"C\"responseTimeout\"S\"retryLimit\"S\"maxTransmitsInFlight\"S\"endpointType\"i\"solicitationQueueDepth\"S\"txBufferOverhead\"S\"upgradeOnly\"C}\"pDelegate\"^v\"selectedProtocolVersion\"S\"isWatchdogSet\"C\"_remoteEndpointID\"i\"dataTransferAllowed\"C\"dataTransferAllowedLocal\"C\"txMsgID\"S\"lastRxMsgID\"S\"uarpStats\"{UARPStatistics=\"packetsNoVersionAgreement\"I\"packetsMissed\"I\"packetsDuplicate\"I\"packetsOutOfOrder\"I}\"_solicitationQueue\"^{UARP4ccTag}\"pStreamingCtx\"^{uarpPlatformStreamingBuffer}\"numTxBufferAvailableSlots\"S\"pTxBufferAvailable\"^^{uarpPlatformTransmitBufferEntry}\"numTxBufferPendingSlots\"S\"pTxBufferPending\"^^{uarpPlatformTransmitBufferEntry}\"pTxBufferInFlight\"^{uarpPlatformTransmitBufferEntry}\"downstreamID\"S\"activeFirmwareVersion\"{UARPVersion=\"major\"I\"minor\"I\"release\"I\"build\"I}\"stagedFirmwareVersion\"{UARPVersion=\"major\"I\"minor\"I\"release\"I\"build\"I}\"pUpstreamEP\"^{uarpPlatformRemoteEndpoint}}"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xd1"

```
