## UARPiCloud

> `/System/Library/PrivateFrameworks/UARPiCloud.framework/UARPiCloud`

```diff

-916.80.2.0.1
-  __TEXT.__text: 0x17870
-  __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_methlist: 0x980
-  __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x1b31
-  __TEXT.__oslogstring: 0x146c
+975.100.86.0.1
+  __TEXT.__text: 0x195a4
+  __TEXT.__auth_stubs: 0x690
+  __TEXT.__objc_methlist: 0x98c
+  __TEXT.__const: 0xc0
+  __TEXT.__cstring: 0x1a37
+  __TEXT.__oslogstring: 0x14cc
   __TEXT.__gcc_except_tab: 0x9c
-  __TEXT.__unwind_info: 0x4b8
-  __TEXT.__objc_classname: 0x117
-  __TEXT.__objc_methname: 0x2e87
+  __TEXT.__unwind_info: 0x578
+  __TEXT.__objc_classname: 0x11a
+  __TEXT.__objc_methname: 0x2ed1
   __TEXT.__objc_methtype: 0x409
-  __TEXT.__objc_stubs: 0x2480
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0x690
+  __TEXT.__objc_stubs: 0x24a0
+  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__const: 0x6c0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x13e0
-  __DATA_CONST.__objc_selrefs: 0xa30
+  __DATA_CONST.__objc_const: 0x1410
+  __DATA_CONST.__objc_selrefs: 0xa50
+  __DATA_CONST.__objc_classrefs: 0x150
+  __DATA_CONST.__objc_superrefs: 0x48
   __AUTH_CONST.__cfstring: 0xd80
   __AUTH_CONST.__objc_const: 0x3e0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x350
+  __AUTH_CONST.__auth_got: 0x358
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_classrefs: 0x150
-  __DATA.__objc_superrefs: 0x48
-  __DATA.__objc_ivar: 0x140
+  __DATA.__objc_ivar: 0x144
   __DATA.__data: 0x125
-  __DATA.__bss: 0x340
+  __DATA.__bss: 0x1150
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 579
-  Symbols:   1824
-  CStrings:  883
+  Functions: 636
+  Symbols:   1947
+  CStrings:  889
 
Symbols:
+ -[CHIPAccessoryFirmwareRecord calculateDigestFromCKRecord:]
+ -[CHIPAccessoryFirmwareRecord digest]
+ _OBJC_IVAR_$_CHIPAccessoryFirmwareRecord._digest
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
+ ___60-[UARPiCloudAssetManager handleRemoteFetchCompletion:error:]_block_invoke.259
+ ___60-[UARPiCloudAssetManager handleRemoteFetchCompletion:error:]_block_invoke.260
+ ___64-[UARPiCloudManager fetchZoneChangesInContainer:forAccessories:]_block_invoke.256
+ ___64-[UARPiCloudManager fetchZoneChangesInContainer:forAccessories:]_block_invoke.258
+ ___64-[UARPiCloudManager fetchZoneChangesInContainer:forAccessories:]_block_invoke_2.257
+ ___64-[UARPiCloudManager fetchZoneChangesInContainer:forAccessories:]_block_invoke_2.260
+ ___64-[UARPiCloudManager fetchZoneChangesInContainer:forAccessories:]_block_invoke_3.261
+ ___70-[UARPiCloudManager fetchRemoteDatabaseChangesInContainer:completion:]_block_invoke.240
+ ___70-[UARPiCloudManager fetchRemoteDatabaseChangesInContainer:completion:]_block_invoke_2.241
+ ___72-[UARPiCloudAssetManager handleReleaseNotesDownloadRequestForAccessory:]_block_invoke.270
+ ___74-[UARPiCloudAssetManager handleRemoteFirmwareDownloadRequestForAccessory:]_block_invoke.262
+ __os_log_fault_impl
+ _calloc
+ _fUarpLayer3DownstreamEndpointDiscovery
+ _fUarpLayer3DownstreamEndpointReachable
+ _fUarpLayer3DownstreamEndpointRecvMessage
+ _fUarpLayer3DownstreamEndpointReleased
+ _fUarpLayer3DownstreamEndpointUnreachable
+ _fUarpLayer3NoFirmwareUpdateAvailable
+ _kFirmwareDirectoryName
+ _kReleaseNotesDirectoryName
+ _kUARPAccessoryMetadataAccessoryProductLabelV2
+ _objc_msgSend$allKeys
+ _objc_msgSend$calculateDigestFromCKRecord:
+ _objc_msgSend$dataWithData:
+ _objc_msgSend$digest
+ _objc_msgSend$sortedArrayUsingSelector:
+ _uarpAllocPrepareTransmitBuffer2
+ _uarpAllocateTransmitBuffer2
+ _uarpAssetQueueSolicitation
+ _uarpAssetSuperBinaryVersionForProtocolVersion
+ _uarpAvailableTransmitBuffer
+ _uarpCopyDefaultInfoString
+ _uarpCopyDefaultInfoString.unknown
+ _uarpDownstreamEndpointGetID
+ _uarpEndpointRoleToString
+ _uarpLogDebug.logBuffer
+ _uarpLogError.logBuffer
+ _uarpLogFault.logBuffer
+ _uarpLogInfo.logBuffer
+ _uarpLogToken.tokens
+ _uarpPlatformCancelPendingTxMessages
+ _uarpPlatformCancelRxDynamicAssets
+ _uarpPlatformDarwinLogDebug
+ _uarpPlatformDarwinLogDebug.cold.1
+ _uarpPlatformDarwinLogDebug.logBuffer
+ _uarpPlatformDarwinLogError
+ _uarpPlatformDarwinLogError.cold.1
+ _uarpPlatformDarwinLogError.logBuffer
+ _uarpPlatformDarwinLogFault
+ _uarpPlatformDarwinLogFault.cold.1
+ _uarpPlatformDarwinLogFault.logBuffer
+ _uarpPlatformDarwinLogInfo
+ _uarpPlatformDarwinLogInfo.logBuffer
+ _uarpPlatformDownstreamEndpointAdd
+ _uarpPlatformDownstreamEndpointAddWithID
+ _uarpPlatformDownstreamEndpointDiscovery
+ _uarpPlatformDownstreamEndpointRemove
+ _uarpPlatformDownstreamEndpointSendMessage
+ _uarpPlatformDownstreamEndpointSendMessageInternal
+ _uarpPlatformEndpointAssetRelease2
+ _uarpPlatformEndpointCleanupAssets2
+ _uarpPlatformEndpointInit2
+ _uarpPlatformEndpointIsMessageTypePending
+ _uarpPlatformEndpointSendMessageCompleteInternal
+ _uarpPlatformEndpointServiceTransmitQueues
+ _uarpPlatformNoFirmwareUpdateAvailable
+ _uarpPlatformRemoteEndpointAddEntry
+ _uarpPlatformRemoteEndpointAlloc
+ _uarpPlatformTransmitQueueAddMessage
+ _uarpPlatformTransmitQueueLogEntry
+ _uarpPlatformTransmitQueueRecvMessage
+ _uarpPlatformTransmitQueueSendCompleteByBuffer
+ _uarpPlatformTransmitQueueServiceTxQueue
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
- -[UARPiCloudManager(CHIP) calculateDigestFromCHIPFirmwareRecord:]
- ___60-[UARPiCloudAssetManager handleRemoteFetchCompletion:error:]_block_invoke.241
- ___60-[UARPiCloudAssetManager handleRemoteFetchCompletion:error:]_block_invoke.242
- ___64-[UARPiCloudManager fetchZoneChangesInContainer:forAccessories:]_block_invoke.232
- ___64-[UARPiCloudManager fetchZoneChangesInContainer:forAccessories:]_block_invoke.234
- ___64-[UARPiCloudManager fetchZoneChangesInContainer:forAccessories:]_block_invoke_2.233
- ___64-[UARPiCloudManager fetchZoneChangesInContainer:forAccessories:]_block_invoke_2.236
- ___64-[UARPiCloudManager fetchZoneChangesInContainer:forAccessories:]_block_invoke_3.237
- ___70-[UARPiCloudManager fetchRemoteDatabaseChangesInContainer:completion:]_block_invoke.216
- ___70-[UARPiCloudManager fetchRemoteDatabaseChangesInContainer:completion:]_block_invoke_2.217
- ___72-[UARPiCloudAssetManager handleReleaseNotesDownloadRequestForAccessory:]_block_invoke.252
- ___74-[UARPiCloudAssetManager handleRemoteFirmwareDownloadRequestForAccessory:]_block_invoke.244
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
- _gUarpLogBuffer
- _malloc_type_calloc
- _objc_msgSend$calculateDigestFromCHIPFirmwareRecord:
- _objc_msgSend$cdVersionNumber
- _objc_msgSend$maxFirmwareVersionNumber
- _objc_msgSend$minFirmwareVersionNumber
- _uarpCompressBuffer
- _uarpDecompressBuffer
- _uarpLogToken.logTokenAccessory
- _uarpLogToken.logTokenAssert
- _uarpLogToken.logTokenController
- _uarpLogToken.logTokenMemory
- _uarpLogToken.logTokenPlatform
- _uarpLogToken.logTokenProduct
- _uarpLogToken.logTokenUnknown
- _uarpPayloadHashFinal
- _uarpPayloadHashInit
- _uarpPayloadHashLog
- _uarpPayloadHashUpdate
- _uarpPlatformAssetProcessingNotification
CStrings:
+ "\x0f\x04"
+ "Accessory"
+ "CHIPAccessory record digest: %@"
+ "CHIPAccessoryFirmware record digest: %@"
+ "Controller"
+ "Host Controller"
+ "Mismatch UUID"
+ "T@\"NSData\",R,V_digest"
+ "UARP.LAYER2 <%s> Cannot find downstream endpoint"
+ "_digest"
+ "accessoryProductLabelV2"
+ "allKeys"
+ "calculateDigestFromCKRecord:"
+ "calculatedHash: %{public}@, expectedHash:%{public}@, error:%{public}@"
+ "dataWithData:"
+ "digest"
+ "downstream"
+ "signatureV2"
+ "sortedArrayUsingSelector:"
+ "streaming"
+ "uarpMsgRecvDownstreamEndpointMessage"
- "Hash Final <%c%c%c%c>- Match !"
- "Mismatc hUUID"
- "RX MSG: Length validation failure"
- "Retrying Sync, %d retries left"
- "Retrying Version Discovery, %d retries left"
- "Too many retries for Protocol Version Discovery report v1"
- "Too many retries for Sync, move to Protocol Version Discovery"
- "UARP Recv Bytes: Full Message %u"
- "UARP Recv Bytes: Lazy Init"
- "UARP Recv Bytes: Total Length = %u, Type = 0x%04x, Payload Length = %u, ID = %u"
- "calculateDigestFromCHIPFirmwareRecord:"
- "calculatedHash: %@, expectedHash:%@, error:%@"
- "firmware"
- "releasenotes"
- "unknown"

```
