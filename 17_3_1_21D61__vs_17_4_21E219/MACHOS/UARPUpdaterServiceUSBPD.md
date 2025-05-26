## UARPUpdaterServiceUSBPD

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceUSBPD.xpc/UARPUpdaterServiceUSBPD`

```diff

-916.80.2.0.1
-  __TEXT.__text: 0x22b2c
-  __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__objc_stubs: 0x35a0
-  __TEXT.__objc_methlist: 0x12f0
-  __TEXT.__oslogstring: 0x25e4
-  __TEXT.__cstring: 0x25e9
-  __TEXT.__objc_classname: 0x203
-  __TEXT.__objc_methname: 0x43d5
-  __TEXT.__objc_methtype: 0x3029
-  __TEXT.__const: 0x40
+975.100.86.0.1
+  __TEXT.__text: 0x25078
+  __TEXT.__auth_stubs: 0x800
+  __TEXT.__objc_stubs: 0x3620
+  __TEXT.__objc_methlist: 0x12f8
+  __TEXT.__oslogstring: 0x275d
+  __TEXT.__cstring: 0x2690
+  __TEXT.__objc_classname: 0x209
+  __TEXT.__objc_methname: 0x453d
+  __TEXT.__objc_methtype: 0x3646
+  __TEXT.__const: 0x50
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0x714
-  __DATA_CONST.__auth_got: 0x3f0
-  __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0x588
+  __TEXT.__unwind_info: 0x7b8
+  __DATA_CONST.__auth_got: 0x410
+  __DATA_CONST.__got: 0x70
+  __DATA_CONST.__const: 0x5d8
   __DATA_CONST.__cfstring: 0x720
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x3f90
-  __DATA.__objc_selrefs: 0xf00
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x150
-  __DATA.__objc_superrefs: 0x58
-  __DATA.__objc_ivar: 0x224
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x150
+  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__objc_intobj: 0x48
+  __DATA.__objc_const: 0x3fd0
+  __DATA.__objc_selrefs: 0xf20
+  __DATA.__objc_ivar: 0x228
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x383
-  __DATA.__bss: 0x38c
+  __DATA.__bss: 0x119c
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libcompression.dylib
   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1100
-  Symbols:   542
-  CStrings:  1474
+  Functions: 1156
+  Symbols:   589
+  CStrings:  1494
 
Symbols:
+ _NSFilePosixPermissions
+ _UARPLayer2ActiveFirmwareVersion2
+ _UARPLayer2ActiveFirmwareVersionResponse
+ _UARPLayer2ApplyStagedAssets
+ _UARPLayer2ApplyStagedAssetsResponse
+ _UARPLayer2AssetAllHeadersAndMetaDataComplete
+ _UARPLayer2AssetCorrupt
+ _UARPLayer2AssetGetBytesAtOffset2
+ _UARPLayer2AssetMetaDataComplete
+ _UARPLayer2AssetMetaDataProcessingError
+ _UARPLayer2AssetMetaDataTLV
+ _UARPLayer2AssetOrphaned
+ _UARPLayer2AssetPreProcessingNotification
+ _UARPLayer2AssetPreProcessingNotificationAck
+ _UARPLayer2AssetProcessingNotification2
+ _UARPLayer2AssetProcessingNotificationAck
+ _UARPLayer2AssetReady
+ _UARPLayer2AssetReleased2
+ _UARPLayer2AssetRescinded
+ _UARPLayer2AssetRescindedAck
+ _UARPLayer2AssetSetBytesAtOffset2
+ _UARPLayer2AssetSolicitation
+ _UARPLayer2AssetStore
+ _UARPLayer2CompressBuffer
+ _UARPLayer2DataTransferPause
+ _UARPLayer2DataTransferPauseAck
+ _UARPLayer2DataTransferResume
+ _UARPLayer2DataTransferResumeAck
+ _UARPLayer2DecompressBuffer
+ _UARPLayer2DynamicAssetOffered
+ _UARPLayer2FriendlyName
+ _UARPLayer2FriendlyNameResponse
+ _UARPLayer2HardwareVersion
+ _UARPLayer2HardwareVersionResponse
+ _UARPLayer2HashFinal
+ _UARPLayer2HashInfo
+ _UARPLayer2HashInit
+ _UARPLayer2HashLog
+ _UARPLayer2HashUpdate
+ _UARPLayer2LastError
+ _UARPLayer2LastErrorResponse
+ _UARPLayer2LogPacket
+ _UARPLayer2ManufacturerName
+ _UARPLayer2ManufacturerNameResponse
+ _UARPLayer2ModelName
+ _UARPLayer2ModelNameResponse
+ _UARPLayer2PayloadData
+ _UARPLayer2PayloadDataComplete
+ _UARPLayer2PayloadDataComplete2
+ _UARPLayer2PayloadMetaDataComplete
+ _UARPLayer2PayloadMetaDataProcessingError
+ _UARPLayer2PayloadMetaDataTLV
+ _UARPLayer2PayloadReady
+ _UARPLayer2ProtocolVersion
+ _UARPLayer2RequestBuffer
+ _UARPLayer2RequestTransmitMsgBuffer
+ _UARPLayer2RescindAllAssets
+ _UARPLayer2RescindAllAssetsAck
+ _UARPLayer2ReturnBuffer
+ _UARPLayer2ReturnTransmitMsgBuffer
+ _UARPLayer2SendMessage
+ _UARPLayer2SerialNumber
+ _UARPLayer2SerialNumberResponse
+ _UARPLayer2StagedFirmwareVersion2
+ _UARPLayer2StagedFirmwareVersionResponse
+ _UARPLayer2StatisticsResponse
+ _UARPLayer2SuperBinaryOffered
+ _UARPLayer2VendorSpecificCheckExpectedResponse
+ _UARPLayer2VendorSpecificCheckValidToSend
+ _UARPLayer2VendorSpecificExceededRetries
+ _UARPLayer2VendorSpecificRecvMessage
+ _UARPLayer2WatchdogCancel
+ _UARPLayer2WatchdogSet
+ _UARPPlatformDownstreamEndpointByDelegate
+ _UARPPlatformDownstreamEndpointByID
+ _UARPUtilsCreateTemporaryFolder
+ __os_log_fault_impl
+ _dataFromHexString
+ _dispatch_after
+ _dispatch_time
+ _fUarpLayer3DownstreamEndpointDiscovery
+ _fUarpLayer3DownstreamEndpointReachable
+ _fUarpLayer3DownstreamEndpointRecvMessage
+ _fUarpLayer3DownstreamEndpointReleased
+ _fUarpLayer3DownstreamEndpointUnreachable
+ _fUarpLayer3NoFirmwareUpdateAvailable
+ _objc_retain_x27
+ _uarpAllocPrepareTransmitBuffer2
+ _uarpAllocateTransmitBuffer2
+ _uarpApplePlatformEndpointRecvMessage
+ _uarpApplePlatformMessageCheckExpectedResponse
+ _uarpApplePlatformMessageCheckValidToSend
+ _uarpApplePlatformMessageExceededRetries
+ _uarpAssetQueueSolicitation
+ _uarpAssetSuperBinaryVersionForProtocolVersion
+ _uarpCopyDefaultInfoString
+ _uarpDownstreamEndpointGetID
+ _uarpEndpointRoleToString
+ _uarpPlatformCancelPendingTxMessages
+ _uarpPlatformCancelRxDynamicAssets
+ _uarpPlatformDarwinLogDebug
+ _uarpPlatformDarwinLogError
+ _uarpPlatformDarwinLogFault
+ _uarpPlatformDarwinLogInfo
+ _uarpPlatformDownstreamEndpointSendMessageInternal
+ _uarpPlatformEndpointAssetRelease2
+ _uarpPlatformEndpointCleanupAssets2
+ _uarpPlatformEndpointInit2
+ _uarpPlatformEndpointIsMessageTypePending
+ _uarpPlatformEndpointSendMessageCompleteInternal
+ _uarpPlatformNoFirmwareUpdateAvailable
+ _uarpPlatformRemoteEndpointAddEntry
+ _uarpPlatformRemoteEndpointAlloc
+ _uarpPlatformTransmitQueueLogEntry
+ _uarpPrintDataResponseDetails
+ _uarpProcessingFlagsReasonToString
+ _uarpSendDownstreamEndpointDiscovery
+ _uarpSendDownstreamEndpointReachable
+ _uarpSendDownstreamEndpointUnreachable
+ _uarpSendNoFirmwareUpdateAvailable
+ _uarpTransmitBuffer2
+ _uarpTransmitBufferUpstream
+ _uarpTransmitQueueAssetRescinded
+ _uarpTransmitQueuePendingEntryComplete
+ _uarpTransmitQueueProcessRecv
+ _uarpTransmitQueueService
+ _uarpTransmitQueuesCleanup
- _fActiveFirmwareVersion2
- _fActiveFirmwareVersionResponse
- _fApplyStagedAssets
- _fApplyStagedAssetsResponse
- _fAssetAllHeadersAndMetaDataComplete
- _fAssetCorrupt
- _fAssetGetBytesAtOffset2
- _fAssetMetaDataComplete
- _fAssetMetaDataProcessingError
- _fAssetMetaDataTLV
- _fAssetOrphaned
- _fAssetPreProcessingNotification
- _fAssetPreProcessingNotificationAck
- _fAssetProcessingNotification2
- _fAssetProcessingNotificationAck
- _fAssetReady
- _fAssetReleased2
- _fAssetRescinded
- _fAssetRescindedAck
- _fAssetSetBytesAtOffset2
- _fAssetSolicitation
- _fAssetStore
- _fCompressBuffer
- _fDataTransferPause
- _fDataTransferPauseAck
- _fDataTransferResume
- _fDataTransferResumeAck
- _fDecompressBuffer
- _fDynamicAssetOffered
- _fFriendlyName
- _fFriendlyNameResponse
- _fHardwareVersion
- _fHardwareVersionResponse
- _fHashFinal
- _fHashInfo
- _fHashInit
- _fHashLog
- _fHashUpdate
- _fLastError
- _fLastErrorResponse
- _fLayer2WatchdogCancel
- _fLayer2WatchdogSet
- _fManufacturerName
- _fManufacturerNameResponse
- _fModelName
- _fModelNameResponse
- _fPayloadData
- _fPayloadDataComplete
- _fPayloadDataComplete2
- _fPayloadMetaDataComplete
- _fPayloadMetaDataProcessingError
- _fPayloadMetaDataTLV
- _fPayloadReady
- _fProtocolVersion
- _fRequestBuffer
- _fRequestTransmitMsgBuffer
- _fRescindAllAssets
- _fRescindAllAssetsAck
- _fReturnBuffer
- _fReturnTransmitMsgBuffer
- _fSendMessage
- _fSerialNumber
- _fSerialNumberResponse
- _fStagedFirmwareVersion2
- _fStagedFirmwareVersionResponse
- _fStatisticsResponse
- _fSuperBinaryOffered
- _fUARPProtectedCallbackLogPacket
- _uarpCompressBuffer
- _uarpDecompressBuffer
- _uarpPayloadHashFinal
- _uarpPayloadHashInit
- _uarpPayloadHashLog
- _uarpPayloadHashUpdate
- _uarpPlatformAssetProcessingNotification
- _uarpPlatformEndpointPayloadRequestAllHeadersAndMetaData
- _uarpPlatformEndpointRequestInfoProperty
- _uarpPlatformEndpointStreamingRecvBytes
- _uarpPlatformEndpointStreamingRecvDeinit
- _uarpPlatformEndpointStreamingRecvInit
CStrings:
+ "\x02\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x13"
+ "%s: Force check for power adapters because power adapter notification"
+ "%s: Found Power Adapter %@ %@"
+ "%s: Look for power adapters on all HPMs that don't have MagSafe"
+ "%s: No power adapters, disconnection notification"
+ "%s: Power adapter poll already requested"
+ "%s: Requesting Power adapter discovery after %u seconds"
+ "%s: Serial number %s"
+ "%s: USB-PD Accessory Set (%d) is %@"
+ "-[UARPUSBPDUpdater bsdNotificationReceived:]"
+ "-[UARPUSBPDUpdater handleBsdNotificationPowerAdapter]"
+ "-[UARPUSBPDUpdater handleBsdNotificationPowerAdapter]_block_invoke"
+ "-[UARPUSBPDUpdater qBsdNotificationReceivedPowerSource]"
+ "-[UARPUSBPDUpdater qFindPowerAdapterAccessories:]"
+ "-[UARPUSBPDUpdater qRemoveDisconnectedAccessories:]"
+ "-[UARPUpdaterServiceUSBPD matchingService:identifier:]"
+ "@32@0:8@16^{uarpPlatformOptionsObj=IIISCSSSiSS}24"
+ "Accessory"
+ "Controller"
+ "Failed to query serialNumber"
+ "Failed to set permission for location %@: %@"
+ "Found a supported power adapter, check for update %@"
+ "Host Controller"
+ "Ignore matching for %@"
+ "Mismatch UUID"
+ "Not supported power adapter (by hardware id) on this HPM %u"
+ "Power Adapter not supported; ignoring notification on %@"
+ "Querying serial number"
+ "Skip check (MagSafe) for power adapter on HPM %@"
+ "T@\"NSString\",?,R,C"
+ "T^{uarpPlatformEndpoint={uarpPlatformOptionsObj=IIISCSSSiSS}^v{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}^viI^^{uarpPlatformRemoteEndpoint}^{uarpPlatformAsset}iCi^?S},R"
+ "T^{uarpPlatformRemoteEndpoint={uarpPlatformOptionsObj=IIISCSSSiSS}^vSCiCSS{UARPStatistics=IIII}^{UARP4ccTag}^{uarpPlatformStreamingBuffer}S^^{uarpPlatformTransmitBufferEntry}S^^{uarpPlatformTransmitBufferEntry}^{uarpPlatformTransmitBufferEntry}S^{uarpPlatformRemoteEndpoint}},R"
+ "UARP.LAYER2 <%s> Cannot find downstream endpoint"
+ "USB-PD Accessory Set (%d) is %@"
+ "Unable to create directory at %@ with %@"
+ "VUARPQuerySerialNumber"
+ "^{uarpPlatformEndpoint={uarpPlatformOptionsObj=IIISCSSSiSS}^v{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}^viI^^{uarpPlatformRemoteEndpoint}^{uarpPlatformAsset}iCi^?S}16@0:8"
+ "^{uarpPlatformRemoteEndpoint={uarpPlatformOptionsObj=IIISCSSSiSS}^vSCiCSS{UARPStatistics=IIII}^{UARP4ccTag}^{uarpPlatformStreamingBuffer}S^^{uarpPlatformTransmitBufferEntry}S^^{uarpPlatformTransmitBufferEntry}^{uarpPlatformTransmitBufferEntry}S^{uarpPlatformRemoteEndpoint}}16@0:8"
+ "_requestedPowerAdapterDiscovery"
+ "assetAvailablityUpdateForAccessory:assetID:"
+ "count"
+ "dictionaryWithObjects:forKeys:count:"
+ "downstream"
+ "requestedPowerAdapterDiscovery"
+ "setAttributes:ofItemAtPath:error:"
+ "streaming"
+ "uarpMsgRecvDownstreamEndpointMessage"
+ "{uarpPlatformEndpoint=\"_options\"{uarpPlatformOptionsObj=\"maxTxPayloadLength\"I\"maxRxPayloadLength\"I\"payloadWindowLength\"I\"protocolVersion\"S\"reofferFirmwareOnSync\"C\"responseTimeout\"S\"retryLimit\"S\"maxTransmitsInFlight\"S\"endpointType\"i\"solicitationQueueDepth\"S\"txBufferOverhead\"S}\"pVendorExtension\"^v\"protectedCallbacks\"{uarpPlatformEndpointCallbacks=\"fRequestBuffer\"^?\"fReturnBuffer\"^?\"fRequestTransmitMsgBuffer\"^?\"fReturnTransmitMsgBuffer\"^?\"fSendMessage\"^?\"fDataTransferPause\"^?\"fDataTransferPauseAck\"^?\"fDataTransferResume\"^?\"fDataTransferResumeAck\"^?\"fSuperBinaryOffered\"^?\"fDynamicAssetOffered\"^?\"fApplyStagedAssets\"^?\"fApplyStagedAssetsResponse\"^?\"fManufacturerName\"^?\"fManufacturerNameResponse\"^?\"fModelName\"^?\"fModelNameResponse\"^?\"fSerialNumber\"^?\"fSerialNumberResponse\"^?\"fHardwareVersion\"^?\"fHardwareVersionResponse\"^?\"fActiveFirmwareVersion2\"^?\"fActiveFirmwareVersionResponse\"^?\"fStagedFirmwareVersion2\"^?\"fStagedFirmwareVersionResponse\"^?\"fLastError\"^?\"fLastErrorResponse\"^?\"fStatisticsResponse\"^?\"fAssetSolicitation\"^?\"fRescindAllAssets\"^?\"fRescindAllAssetsAck\"^?\"fLayer2WatchdogSet\"^?\"fLayer2WatchdogCancel\"^?\"fProtocolVersion\"^?\"fFriendlyName\"^?\"fFriendlyNameResponse\"^?\"fDecompressBuffer\"^?\"fCompressBuffer\"^?\"fHashInfo\"^?\"fHashInit\"^?\"fHashUpdate\"^?\"fHashFinal\"^?\"fHashLog\"^?\"fLogPacket\"^?\"fLogError\"^?\"fLogInfo\"^?\"fLogDebug\"^?\"fLogFault\"^?\"fDownstreamDiscovery\"^?\"fDownstreamReachable\"^?\"fDownstreamUnreachable\"^?\"fDownstreamReleased\"^?\"fDownstreamRecvMessage\"^?\"fNoFirmwareUpdateAvailable\"^?\"fVendorSpecificRecvMsg\"^?\"fVendorSpecificCheckExpectedResponse\"^?\"fVendorSpecificCheckValidToSend\"^?\"fVendorSpecificExceededRetries\"^?\"fActiveFirmwareVersion\"^?\"fStagedFirmwareVersion\"^?\"fAssetRescinded\"^?\"fAssetCorrupt\"^?\"fAssetOrphaned\"^?\"fAssetReleased\"^?\"fAssetReady\"^?\"fAssetStore\"^?\"fAssetMetaDataTLV\"^?\"fAssetMetaDataComplete\"^?\"fPayloadReady\"^?\"fPayloadMetaDataTLV\"^?\"fPayloadMetaDataComplete\"^?\"fPayloadData\"^?\"fPayloadDataComplete\"^?\"fTxWatchdogSet\"^?\"fTxWatchdogCancel\"^?}\"pDelegate\"^v\"role\"i\"numRemoteEndpointSlots\"I\"pRemoteEPs\"^^{uarpPlatformRemoteEndpoint}\"pAssetList\"^{uarpPlatformAsset}\"nextTxAssetID\"i\"rxLock\"C\"nextRemoteEndpointID\"i\"fVendorSpecific\"^?\"nextDownstreamID\"S}"
+ "{uarpPlatformEndpointApple=\"supportsPersonalization\"C\"supportsHeySiri\"C\"supportsJustSiri\"C\"supportsVoiceAssist\"C\"callbacks\"{uarpPlatformEndpointAppleCallbacks=\"fAppleModelNumber\"^?\"fAppleModelNumberResponse\"^?\"fHwFusingType\"^?\"fHwFusingTypeResponse\"^?\"fManifestPrefix\"^?\"fManifestPrefixResponse\"^?\"fBoardID\"^?\"fBoardIDResponse\"^?\"fChipID\"^?\"fChipIDResponse\"^?\"fChipRevision\"^?\"fChipRevisionResponse\"^?\"fECID\"^?\"fECIDResponse\"^?\"fECIDData\"^?\"fECIDDataResponse\"^?\"fSecurityDomain\"^?\"fSecurityDomainResponse\"^?\"fSecurityMode\"^?\"fSecurityModeResponse\"^?\"fProductionMode\"^?\"fProductionModeResponse\"^?\"fChipEpoch\"^?\"fChipEpochResponse\"^?\"fEnableMixMatch\"^?\"fEnableMixMatchResponse\"^?\"fSoCLiveNonce\"^?\"fSoCLiveNonceResponse\"^?\"fPrefixNeedsLogicalUnitNumber\"^?\"fPrefixNeedsLogicalUnitNumberResponse\"^?\"fSuffixNeedsLogicalUnitNumber\"^?\"fSuffixNeedsLogicalUnitNumberResponse\"^?\"fLogicalUnitNumber\"^?\"fLogicalUnitNumberResponse\"^?\"fTicketLongName\"^?\"fTicketLongNameResponse\"^?\"fRequiresPersonalization\"^?\"fRequiresPersonalizationResponse\"^?\"fApBoardID\"^?\"fApBoardIDResponse\"^?\"fApChipID\"^?\"fApChipIDResponse\"^?\"fApProductionMode\"^?\"fApProductionModeResponse\"^?\"fApSecurityMode\"^?\"fApSecurityModeResponse\"^?\"fHardwareSpecific\"^?\"fHardwareSpecificResponse\"^?\"fNonce\"^?\"fNonceResponse\"^?\"fLife\"^?\"fLifeResponse\"^?\"fProvisioning\"^?\"fProvisioningResponse\"^?\"fManifestEpoch\"^?\"fManifestEpochResponse\"^?\"fManifestSuffix\"^?\"fManifestSuffixResponse\"^?}}"
+ "{uarpPlatformEndpointCallbacks=\"fRequestBuffer\"^?\"fReturnBuffer\"^?\"fRequestTransmitMsgBuffer\"^?\"fReturnTransmitMsgBuffer\"^?\"fSendMessage\"^?\"fDataTransferPause\"^?\"fDataTransferPauseAck\"^?\"fDataTransferResume\"^?\"fDataTransferResumeAck\"^?\"fSuperBinaryOffered\"^?\"fDynamicAssetOffered\"^?\"fApplyStagedAssets\"^?\"fApplyStagedAssetsResponse\"^?\"fManufacturerName\"^?\"fManufacturerNameResponse\"^?\"fModelName\"^?\"fModelNameResponse\"^?\"fSerialNumber\"^?\"fSerialNumberResponse\"^?\"fHardwareVersion\"^?\"fHardwareVersionResponse\"^?\"fActiveFirmwareVersion2\"^?\"fActiveFirmwareVersionResponse\"^?\"fStagedFirmwareVersion2\"^?\"fStagedFirmwareVersionResponse\"^?\"fLastError\"^?\"fLastErrorResponse\"^?\"fStatisticsResponse\"^?\"fAssetSolicitation\"^?\"fRescindAllAssets\"^?\"fRescindAllAssetsAck\"^?\"fLayer2WatchdogSet\"^?\"fLayer2WatchdogCancel\"^?\"fProtocolVersion\"^?\"fFriendlyName\"^?\"fFriendlyNameResponse\"^?\"fDecompressBuffer\"^?\"fCompressBuffer\"^?\"fHashInfo\"^?\"fHashInit\"^?\"fHashUpdate\"^?\"fHashFinal\"^?\"fHashLog\"^?\"fLogPacket\"^?\"fLogError\"^?\"fLogInfo\"^?\"fLogDebug\"^?\"fLogFault\"^?\"fDownstreamDiscovery\"^?\"fDownstreamReachable\"^?\"fDownstreamUnreachable\"^?\"fDownstreamReleased\"^?\"fDownstreamRecvMessage\"^?\"fNoFirmwareUpdateAvailable\"^?\"fVendorSpecificRecvMsg\"^?\"fVendorSpecificCheckExpectedResponse\"^?\"fVendorSpecificCheckValidToSend\"^?\"fVendorSpecificExceededRetries\"^?\"fActiveFirmwareVersion\"^?\"fStagedFirmwareVersion\"^?\"fAssetRescinded\"^?\"fAssetCorrupt\"^?\"fAssetOrphaned\"^?\"fAssetReleased\"^?\"fAssetReady\"^?\"fAssetStore\"^?\"fAssetMetaDataTLV\"^?\"fAssetMetaDataComplete\"^?\"fPayloadReady\"^?\"fPayloadMetaDataTLV\"^?\"fPayloadMetaDataComplete\"^?\"fPayloadData\"^?\"fPayloadDataComplete\"^?\"fTxWatchdogSet\"^?\"fTxWatchdogCancel\"^?}"
+ "{uarpPlatformOptionsObj=\"maxTxPayloadLength\"I\"maxRxPayloadLength\"I\"payloadWindowLength\"I\"protocolVersion\"S\"reofferFirmwareOnSync\"C\"responseTimeout\"S\"retryLimit\"S\"maxTransmitsInFlight\"S\"endpointType\"i\"solicitationQueueDepth\"S\"txBufferOverhead\"S}"
+ "{uarpPlatformRemoteEndpoint=\"_options\"{uarpPlatformOptionsObj=\"maxTxPayloadLength\"I\"maxRxPayloadLength\"I\"payloadWindowLength\"I\"protocolVersion\"S\"reofferFirmwareOnSync\"C\"responseTimeout\"S\"retryLimit\"S\"maxTransmitsInFlight\"S\"endpointType\"i\"solicitationQueueDepth\"S\"txBufferOverhead\"S}\"pDelegate\"^v\"selectedProtocolVersion\"S\"isWatchdogSet\"C\"_remoteEndpointID\"i\"dataTransferAllowed\"C\"txMsgID\"S\"lastRxMsgID\"S\"uarpStats\"{UARPStatistics=\"packetsNoVersionAgreement\"I\"packetsMissed\"I\"packetsDuplicate\"I\"packetsOutOfOrder\"I}\"_solicitationQueue\"^{UARP4ccTag}\"pStreamingCtx\"^{uarpPlatformStreamingBuffer}\"numTxBufferAvailableSlots\"S\"pTxBufferAvailable\"^^{uarpPlatformTransmitBufferEntry}\"numTxBufferPendingSlots\"S\"pTxBufferPending\"^^{uarpPlatformTransmitBufferEntry}\"pTxBufferInFlight\"^{uarpPlatformTransmitBufferEntry}\"downstreamID\"S\"pUpstreamEP\"^{uarpPlatformRemoteEndpoint}}"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0q"
- "\x02\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf03"
- "%s: Power Source %@ %@"
- "%s: USB-PD Accessory Set is %@"
- "@\"NSMutableString\""
- "@32@0:8@16^{uarpPlatformOptionsObj=IIISCSS}24"
- "Dongle notification"
- "Failed to query serial number"
- "Force check for power adapters because power adapter notification"
- "Hash Final <%c%c%c%c>- Match !"
- "Ignore notification for %@"
- "Look for power adapters on all HPMs that don't have magsafe"
- "Mismatc hUUID"
- "No supported power adapter (by hardware id) on this HPM %@"
- "RX MSG: Length validation failure"
- "Retrying Sync, %d retries left"
- "Retrying Version Discovery, %d retries left"
- "Skip check for power adapter on HPM %@"
- "T^{uarpPlatformEndpoint={uarpPlatformOptionsObj=IIISCSS}^v{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}^vi^{uarpPlatformRemoteEndpoint}^{uarpPlatformAsset}iCi^?},R"
- "T^{uarpPlatformRemoteEndpoint={uarpPlatformOptionsObj=IIISCSS}^vSCiSiCSS{UARPStatistics=IIII}^{uarpPlatformStreamingBuffer}^{uarpPlatformRemoteEndpoint}},R"
- "Too many retries for Protocol Version Discovery report v1"
- "Too many retries for Sync, move to Protocol Version Discovery"
- "UARP Recv Bytes: Full Message %u"
- "UARP Recv Bytes: Lazy Init"
- "UARP Recv Bytes: Total Length = %u, Type = 0x%04x, Payload Length = %u, ID = %u"
- "USB-PD Accessory Set is %@"
- "^{uarpPlatformEndpoint={uarpPlatformOptionsObj=IIISCSS}^v{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}^vi^{uarpPlatformRemoteEndpoint}^{uarpPlatformAsset}iCi^?}16@0:8"
- "^{uarpPlatformRemoteEndpoint={uarpPlatformOptionsObj=IIISCSS}^vSCiSiCSS{UARPStatistics=IIII}^{uarpPlatformStreamingBuffer}^{uarpPlatformRemoteEndpoint}}16@0:8"
- "{uarpPlatformEndpoint=\"_options\"{uarpPlatformOptionsObj=\"maxTxPayloadLength\"I\"maxRxPayloadLength\"I\"payloadWindowLength\"I\"protocolVersion\"S\"reofferFirmwareOnSync\"C\"responseTimeout\"S\"retryLimit\"S}\"pVendorExtension\"^v\"protectedCallbacks\"{uarpPlatformEndpointCallbacks=\"fRequestBuffer\"^?\"fReturnBuffer\"^?\"fRequestTransmitMsgBuffer\"^?\"fReturnTransmitMsgBuffer\"^?\"fSendMessage\"^?\"fDataTransferPause\"^?\"fDataTransferPauseAck\"^?\"fDataTransferResume\"^?\"fDataTransferResumeAck\"^?\"fSuperBinaryOffered\"^?\"fDynamicAssetOffered\"^?\"fApplyStagedAssets\"^?\"fApplyStagedAssetsResponse\"^?\"fManufacturerName\"^?\"fManufacturerNameResponse\"^?\"fModelName\"^?\"fModelNameResponse\"^?\"fSerialNumber\"^?\"fSerialNumberResponse\"^?\"fHardwareVersion\"^?\"fHardwareVersionResponse\"^?\"fActiveFirmwareVersion2\"^?\"fActiveFirmwareVersionResponse\"^?\"fStagedFirmwareVersion2\"^?\"fStagedFirmwareVersionResponse\"^?\"fLastError\"^?\"fLastErrorResponse\"^?\"fStatisticsResponse\"^?\"fAssetSolicitation\"^?\"fRescindAllAssets\"^?\"fRescindAllAssetsAck\"^?\"fLayer2WatchdogSet\"^?\"fLayer2WatchdogCancel\"^?\"fProtocolVersion\"^?\"fFriendlyName\"^?\"fFriendlyNameResponse\"^?\"fDecompressBuffer\"^?\"fCompressBuffer\"^?\"fHashInfo\"^?\"fHashInit\"^?\"fHashUpdate\"^?\"fHashFinal\"^?\"fHashLog\"^?\"fLogPacket\"^?\"fActiveFirmwareVersion\"^?\"fStagedFirmwareVersion\"^?\"fAssetRescinded\"^?\"fAssetCorrupt\"^?\"fAssetOrphaned\"^?\"fAssetReleased\"^?\"fAssetReady\"^?\"fAssetStore\"^?\"fAssetMetaDataTLV\"^?\"fAssetMetaDataComplete\"^?\"fPayloadReady\"^?\"fPayloadMetaDataTLV\"^?\"fPayloadMetaDataComplete\"^?\"fPayloadData\"^?\"fPayloadDataComplete\"^?\"fTxWatchdogSet\"^?\"fTxWatchdogCancel\"^?}\"pDelegate\"^v\"role\"i\"pRemoteEPs\"^{uarpPlatformRemoteEndpoint}\"pAssetList\"^{uarpPlatformAsset}\"nextTxAssetID\"i\"rxLock\"C\"nextRemoteEndpointID\"i\"fVendorSpecific\"^?}"
- "{uarpPlatformEndpointApple=\"supportsPersonalization\"C\"supportsHeySiri\"C\"supportsJustSiri\"C\"supportsVoiceAssist\"C\"callbacks\"{uarpPlatformEndpointAppleCallbacks=\"fAppleModelNumber\"^?\"fAppleModelNumberResponse\"^?\"fHwFusingType\"^?\"fHwFusingTypeResponse\"^?\"fManifestPrefix\"^?\"fManifestPrefixResponse\"^?\"fBoardID\"^?\"fBoardIDResponse\"^?\"fChipID\"^?\"fChipIDResponse\"^?\"fChipRevision\"^?\"fChipRevisionResponse\"^?\"fECID\"^?\"fECIDResponse\"^?\"fSecurityDomain\"^?\"fSecurityDomainResponse\"^?\"fSecurityMode\"^?\"fSecurityModeResponse\"^?\"fProductionMode\"^?\"fProductionModeResponse\"^?\"fChipEpoch\"^?\"fChipEpochResponse\"^?\"fEnableMixMatch\"^?\"fEnableMixMatchResponse\"^?\"fSoCLiveNonce\"^?\"fSoCLiveNonceResponse\"^?\"fPrefixNeedsLogicalUnitNumber\"^?\"fPrefixNeedsLogicalUnitNumberResponse\"^?\"fSuffixNeedsLogicalUnitNumber\"^?\"fSuffixNeedsLogicalUnitNumberResponse\"^?\"fLogicalUnitNumber\"^?\"fLogicalUnitNumberResponse\"^?\"fTicketLongName\"^?\"fTicketLongNameResponse\"^?\"fRequiresPersonalization\"^?\"fRequiresPersonalizationResponse\"^?\"fApBoardID\"^?\"fApBoardIDResponse\"^?\"fApChipID\"^?\"fApChipIDResponse\"^?\"fApProductionMode\"^?\"fApProductionModeResponse\"^?\"fApSecurityMode\"^?\"fApSecurityModeResponse\"^?\"fHardwareSpecific\"^?\"fHardwareSpecificResponse\"^?}}"
- "{uarpPlatformEndpointCallbacks=\"fRequestBuffer\"^?\"fReturnBuffer\"^?\"fRequestTransmitMsgBuffer\"^?\"fReturnTransmitMsgBuffer\"^?\"fSendMessage\"^?\"fDataTransferPause\"^?\"fDataTransferPauseAck\"^?\"fDataTransferResume\"^?\"fDataTransferResumeAck\"^?\"fSuperBinaryOffered\"^?\"fDynamicAssetOffered\"^?\"fApplyStagedAssets\"^?\"fApplyStagedAssetsResponse\"^?\"fManufacturerName\"^?\"fManufacturerNameResponse\"^?\"fModelName\"^?\"fModelNameResponse\"^?\"fSerialNumber\"^?\"fSerialNumberResponse\"^?\"fHardwareVersion\"^?\"fHardwareVersionResponse\"^?\"fActiveFirmwareVersion2\"^?\"fActiveFirmwareVersionResponse\"^?\"fStagedFirmwareVersion2\"^?\"fStagedFirmwareVersionResponse\"^?\"fLastError\"^?\"fLastErrorResponse\"^?\"fStatisticsResponse\"^?\"fAssetSolicitation\"^?\"fRescindAllAssets\"^?\"fRescindAllAssetsAck\"^?\"fLayer2WatchdogSet\"^?\"fLayer2WatchdogCancel\"^?\"fProtocolVersion\"^?\"fFriendlyName\"^?\"fFriendlyNameResponse\"^?\"fDecompressBuffer\"^?\"fCompressBuffer\"^?\"fHashInfo\"^?\"fHashInit\"^?\"fHashUpdate\"^?\"fHashFinal\"^?\"fHashLog\"^?\"fLogPacket\"^?\"fActiveFirmwareVersion\"^?\"fStagedFirmwareVersion\"^?\"fAssetRescinded\"^?\"fAssetCorrupt\"^?\"fAssetOrphaned\"^?\"fAssetReleased\"^?\"fAssetReady\"^?\"fAssetStore\"^?\"fAssetMetaDataTLV\"^?\"fAssetMetaDataComplete\"^?\"fPayloadReady\"^?\"fPayloadMetaDataTLV\"^?\"fPayloadMetaDataComplete\"^?\"fPayloadData\"^?\"fPayloadDataComplete\"^?\"fTxWatchdogSet\"^?\"fTxWatchdogCancel\"^?}"
- "{uarpPlatformOptionsObj=\"maxTxPayloadLength\"I\"maxRxPayloadLength\"I\"payloadWindowLength\"I\"protocolVersion\"S\"reofferFirmwareOnSync\"C\"responseTimeout\"S\"retryLimit\"S}"
- "{uarpPlatformRemoteEndpoint=\"_options\"{uarpPlatformOptionsObj=\"maxTxPayloadLength\"I\"maxRxPayloadLength\"I\"payloadWindowLength\"I\"protocolVersion\"S\"reofferFirmwareOnSync\"C\"responseTimeout\"S\"retryLimit\"S}\"pDelegate\"^v\"selectedProtocolVersion\"S\"isWatchdogSet\"C\"pendingResponse\"i\"requestRetries\"S\"_remoteEndpointID\"i\"dataTransferAllowed\"C\"txMsgID\"S\"lastRxMsgID\"S\"uarpStats\"{UARPStatistics=\"packetsNoVersionAgreement\"I\"packetsMissed\"I\"packetsDuplicate\"I\"packetsOutOfOrder\"I}\"pStreamingCtx\"^{uarpPlatformStreamingBuffer}\"pNext\"^{uarpPlatformRemoteEndpoint}}"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x91"

```
