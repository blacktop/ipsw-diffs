## UARPUpdaterServiceLegacyAudio

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/UARPUpdaterServiceLegacyAudio`

```diff

-916.80.2.0.1
-  __TEXT.__text: 0x1f888
-  __TEXT.__auth_stubs: 0xa70
-  __TEXT.__objc_stubs: 0x4240
+975.100.86.0.1
+  __TEXT.__text: 0x222ac
+  __TEXT.__auth_stubs: 0xaa0
+  __TEXT.__objc_stubs: 0x4360
   __TEXT.__objc_methlist: 0x132c
-  __TEXT.__cstring: 0x8005
-  __TEXT.__const: 0x2b8
-  __TEXT.__objc_methname: 0x4d6e
+  __TEXT.__cstring: 0x8128
+  __TEXT.__const: 0x2c0
+  __TEXT.__objc_methname: 0x4e82
   __TEXT.__objc_classname: 0x24e
   __TEXT.__objc_methtype: 0xc8b
-  __TEXT.__oslogstring: 0x6d5
+  __TEXT.__oslogstring: 0x72b
   __TEXT.__gcc_except_tab: 0x104
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0x718
-  __DATA_CONST.__auth_got: 0x548
-  __DATA_CONST.__got: 0xe8
+  __TEXT.__unwind_info: 0x804
+  __DATA_CONST.__auth_got: 0x560
+  __DATA_CONST.__got: 0xf0
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x13b8
-  __DATA_CONST.__cfstring: 0x6500
+  __DATA_CONST.__const: 0x1528
+  __DATA_CONST.__cfstring: 0x68e0
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x90
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x1c0
+  __DATA_CONST.__objc_superrefs: 0x68
+  __DATA_CONST.__objc_intobj: 0xa8
   __DATA.__objc_const: 0x3d88
-  __DATA.__objc_selrefs: 0x13b0
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x1b8
-  __DATA.__objc_superrefs: 0x68
+  __DATA.__objc_selrefs: 0x13f8
   __DATA.__objc_ivar: 0x2a0
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x5c3
-  __DATA.__bss: 0x400
+  __DATA.__bss: 0x1220
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 879
-  Symbols:   1036
-  CStrings:  2213
+  Functions: 949
+  Symbols:   1132
+  CStrings:  2254
 
Symbols:
+ _NSFilePosixPermissions
+ _OBJC_CLASS_$_UARPSupportedAccessory
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
+ _UARPStringPcapFilesFilepath
+ _UARPUtilsCreateTemporaryFolder
+ __os_log_fault_impl
+ _calloc
+ _dataFromHexString
+ _dropboxFileUpdateForAccessoryID
+ _fUarpLayer3DownstreamEndpointDiscovery
+ _fUarpLayer3DownstreamEndpointReachable
+ _fUarpLayer3DownstreamEndpointRecvMessage
+ _fUarpLayer3DownstreamEndpointReleased
+ _fUarpLayer3DownstreamEndpointUnreachable
+ _fUarpLayer3NoFirmwareUpdateAvailable
+ _findPartnerSerialNumberForAccessory
+ _findPartnerSerialNumbersInDatabase
+ _getAccessoryDatabaseForAccessoryID
+ _isOTAUpdateDisabledForAccessoryID
+ _kDropboxVersionKey
+ _kFirmwareDirectoryName
+ _kReleaseNotesDirectoryName
+ _kUARPStringMetadataApplePersonalizationECIDData
+ _kUARPStringMetadataApplePersonalizationFTABPayloadDigestFilename
+ _kUARPStringMetadataApplePersonalizationLife
+ _kUARPStringMetadataApplePersonalizationManifestEpoch
+ _kUARPStringMetadataApplePersonalizationManifestSuffix
+ _kUARPStringMetadataApplePersonalizationPayloadDigestFilename
+ _kUARPStringMetadataApplePersonalizationProvisioning
+ _kUARPStringMetadataApplePersonalizedManifest
+ _kUARPStringMetadataComposePropertyListPayload
+ _kUARPStringMetadataComposeVersionBVERStringFile
+ _kUARPStringMetadataComposeVersionStringFile
+ _kUARPStringPcapFiles
+ _kUARPStringPersonalizationOptionLife
+ _kUARPStringPersonalizationOptionManifestEpoch
+ _kUARPStringPersonalizationOptionProvisioning
+ _kUARPStringTMAPAppleModelNumber
+ _kUARPStringTMAPEventFields
+ _kUARPStringTMAPEventIndex
+ _kUARPStringTMAPEventName
+ _kUARPStringTMAPEvents
+ _kUARPStringTMAPFieldLength
+ _kUARPStringTMAPFieldName
+ _kUARPStringTMAPFieldType
+ _kUARPStringTMAPTypeString
+ _kUARPStringTMAPTypeUnsignedInteger
+ _kUARPStringTMAPVersion
+ _kUARPSupportedAccessoryKeyDFUMode
+ _kUARPSupportedAccessoryKeyIsSimulator
+ _kUARPSupportedAccessoryKeySupportsFriendlyName
+ _objc_retain_x27
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
- _uarpCompressBuffer
- _uarpDecompressBuffer
- _uarpPayloadHashFinal
- _uarpPayloadHashInit
- _uarpPayloadHashLog
- _uarpPayloadHashUpdate
- _uarpPlatformAssetProcessingNotification
CStrings:
+ "Controller"
+ "DFUMode"
+ "DawnE"
+ "EventFields"
+ "EventIndex"
+ "EventName"
+ "Events"
+ "Failed to set permission for location %@: %@"
+ "FieldLength"
+ "FieldName"
+ "FieldType"
+ "Host Controller"
+ "IsSimulator"
+ "Life"
+ "Mismatch UUID"
+ "Personalization ECID Data"
+ "Personalization FTAB Payload Digest Filename"
+ "Personalization Life"
+ "Personalization Manifest Epoch"
+ "Personalization Manifest Suffix"
+ "Personalization Payload Digest Filename"
+ "Personalization Provisioning"
+ "Personalized Manifest"
+ "Property List Payload"
+ "Provisioning"
+ "SupportsFriendlyName"
+ "T@\"NSString\",?,R,C"
+ "UARP.LAYER2 <%s> Cannot find downstream endpoint"
+ "Unable to create directory at %@ with %@"
+ "UnsignedInteger"
+ "Version"
+ "Version BVER File"
+ "Version File"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "dataWithData:"
+ "downstream"
+ "dropboxVersion"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "findByAppleModelNumber:"
+ "firmware"
+ "hwFusingType"
+ "pathWithComponents:"
+ "pcapfiles"
+ "prod"
+ "releasenotes"
+ "setAttributes:ofItemAtPath:error:"
+ "streaming"
+ "supportsInternalSettings"
+ "uarpMsgRecvDownstreamEndpointMessage"
+ "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"
- "DawnD"
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

```
