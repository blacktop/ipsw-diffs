## UARPUpdaterServiceHID

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceHID.xpc/UARPUpdaterServiceHID`

```diff

-916.80.2.0.1
-  __TEXT.__text: 0x186e8
-  __TEXT.__auth_stubs: 0x740
-  __TEXT.__objc_stubs: 0x24c0
+975.100.86.0.1
+  __TEXT.__text: 0x1a53c
+  __TEXT.__auth_stubs: 0x750
+  __TEXT.__objc_stubs: 0x2500
   __TEXT.__objc_methlist: 0x9f4
   __TEXT.__gcc_except_tab: 0xa4
-  __TEXT.__objc_methname: 0x330d
+  __TEXT.__objc_methname: 0x3377
   __TEXT.__objc_classname: 0x1ac
   __TEXT.__objc_methtype: 0xab3
-  __TEXT.__cstring: 0x1611
-  __TEXT.__oslogstring: 0xec1
-  __TEXT.__const: 0x38
-  __TEXT.__unwind_info: 0x614
-  __DATA_CONST.__auth_got: 0x3b0
+  __TEXT.__cstring: 0x1509
+  __TEXT.__oslogstring: 0xeeb
+  __TEXT.__const: 0x40
+  __TEXT.__unwind_info: 0x6d4
+  __DATA_CONST.__auth_got: 0x3b8
   __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x670
+  __DATA_CONST.__const: 0x698
   __DATA_CONST.__cfstring: 0x420
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0xd8
-  __DATA_CONST.__objc_arraydata: 0x50
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x130
+  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x25e0
-  __DATA.__objc_selrefs: 0xaf8
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x130
-  __DATA.__objc_superrefs: 0x38
+  __DATA.__objc_const: 0x2600
+  __DATA.__objc_selrefs: 0xb08
   __DATA.__objc_ivar: 0xcc
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x30a
-  __DATA.__bss: 0x368
+  __DATA.__bss: 0x1178
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0B2C8C82-602E-301D-9CA3-99B4C2536740
-  Functions: 639
-  Symbols:   445
-  CStrings:  911
+  UUID: 3B277014-5E69-380E-BDDF-AC0C6E376B31
+  Functions: 695
+  Symbols:   497
+  CStrings:  913
 
Symbols:
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
+ __os_log_fault_impl
+ _calloc
+ _fUarpLayer3DownstreamEndpointDiscovery
+ _fUarpLayer3DownstreamEndpointReachable
+ _fUarpLayer3DownstreamEndpointRecvMessage
+ _fUarpLayer3DownstreamEndpointReleased
+ _fUarpLayer3DownstreamEndpointUnreachable
+ _fUarpLayer3NoFirmwareUpdateAvailable
+ _uarpAllocPrepareTransmitBuffer2
+ _uarpAllocateTransmitBuffer2
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
- _malloc_type_calloc
- _uarpCompressBuffer
- _uarpDecompressBuffer
- _uarpPayloadHashFinal
- _uarpPayloadHashInit
- _uarpPayloadHashLog
- _uarpPayloadHashUpdate
- _uarpPlatformAssetProcessingNotification
CStrings:
+ "Accessory"
+ "Controller"
+ "HID Accessory does not support TICS <%@>"
+ "Host Controller"
+ "Mismatch UUID"
+ "Solicit TICS (firmware staging complete) for HID <%@>"
+ "T@\"NSString\",?,R,C"
+ "UARP.LAYER2 <%s> Cannot find downstream endpoint"
+ "assetAvailablityUpdateForAccessory:assetID:"
+ "downstream"
+ "setSuppressInfoQueries:"
+ "streaming"
+ "suppressInfoQueries"
+ "uarpMsgRecvDownstreamEndpointMessage"
- "Hash Final <%c%c%c%c>- Match !"
- "Mismatc hUUID"
- "RX MSG: Length validation failure"
- "Retrying Sync, %d retries left"
- "Retrying Version Discovery, %d retries left"
- "Solicit TICS (firmware staging cmplete) for HID <%@>"
- "Too many retries for Protocol Version Discovery report v1"
- "Too many retries for Sync, move to Protocol Version Discovery"
- "UARP Recv Bytes: Full Message %u"
- "UARP Recv Bytes: Lazy Init"
- "UARP Recv Bytes: Total Length = %u, Type = 0x%04x, Payload Length = %u, ID = %u"
- "unknown"

```
