## UARPUpdaterServiceLegacyAudio

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/Contents/MacOS/UARPUpdaterServiceLegacyAudio`

```diff

-1163.0.0.0.0
-  __TEXT.__text: 0x18f04
-  __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_stubs: 0x4140
+1155.0.0.0.0
+  __TEXT.__text: 0x25130
+  __TEXT.__auth_stubs: 0x980
+  __TEXT.__objc_stubs: 0x43c0
   __TEXT.__objc_methlist: 0x1330
-  __TEXT.__cstring: 0x7efc
-  __TEXT.__const: 0x2e0
-  __TEXT.__objc_methname: 0x4cd6
+  __TEXT.__cstring: 0x87a1
+  __TEXT.__const: 0x320
+  __TEXT.__objc_methname: 0x4eb3
   __TEXT.__objc_classname: 0x24e
   __TEXT.__objc_methtype: 0xc8b
-  __TEXT.__oslogstring: 0x6eb
+  __TEXT.__oslogstring: 0x8ca
   __TEXT.__gcc_except_tab: 0x114
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0x578
-  __DATA_CONST.__auth_got: 0x428
-  __DATA_CONST.__got: 0x238
+  __TEXT.__unwind_info: 0x888
+  __DATA_CONST.__auth_got: 0x4d0
+  __DATA_CONST.__got: 0x250
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1560
-  __DATA_CONST.__cfstring: 0x6fe0
+  __DATA_CONST.__const: 0x1848
+  __DATA_CONST.__cfstring: 0x7020
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
-  __DATA_CONST.__objc_intobj: 0x90
+  __DATA_CONST.__objc_intobj: 0xa8
   __DATA.__objc_const: 0x3dc8
-  __DATA.__objc_selrefs: 0x1388
+  __DATA.__objc_selrefs: 0x1418
   __DATA.__objc_ivar: 0x2a0
   __DATA.__objc_data: 0x460
-  __DATA.__data: 0x5a0
-  __DATA.__bss: 0x108
+  __DATA.__data: 0x5e5
+  __DATA.__bss: 0x1288
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/Versions/A/CoreTelephony
   - /System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreUARP.framework/Versions/A/CoreUARP
   - /System/Library/PrivateFrameworks/IASUtilities.framework/Versions/A/IASUtilities

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 574
-  Symbols:   778
-  CStrings:  1073
+  Functions: 1006
+  Symbols:   1186
+  CStrings:  1182
 
Symbols:
+ _CC_SHA256_Final
+ _CC_SHA256_Init
+ _CC_SHA256_Update
+ _CC_SHA384_Final
+ _CC_SHA384_Init
+ _CC_SHA384_Update
+ _CC_SHA512_Final
+ _CC_SHA512_Init
+ _CC_SHA512_Update
+ _IOPMAssertionCreateWithName
+ _IOPMAssertionRelease
+ _NSFilePosixPermissions
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$_UARPSuperBinaryAsset
+ _UARPAccessoryHardwareFusingToString
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
+ _UARPSuperBinaryAddMetaData
+ _UARPSuperBinaryAddPayload
+ _UARPSuperBinaryAddPayload2
+ _UARPSuperBinaryAddPayloadData
+ _UARPSuperBinaryAddPayloadDataLarge
+ _UARPSuperBinaryAddPayloadMetaData
+ _UARPSuperBinaryAddSuperBinaryMetaData
+ _UARPSuperBinaryAppendPayloadMetaData
+ _UARPSuperBinaryAppendPayloadMetaDataBlob
+ _UARPSuperBinaryBuildMetaData
+ _UARPSuperBinaryFinalizeDynamicAsset
+ _UARPSuperBinaryFinalizeHeader
+ _UARPSuperBinaryGetInternalPayloadMetaData
+ _UARPSuperBinaryGetInternalSuperBinaryMetaData
+ _UARPSuperBinaryPrepareDynamicAsset
+ _UARPSuperBinaryPreparePayload
+ _UARPSuperBinaryQueryAssetLength
+ _UARPSuperBinarySetupHeader
+ _UARPUtilsBuildURLForTemporaryFile
+ _UARPUtilsCreateTemporaryFolder
+ __os_log_fault_impl
+ _appendFirstUarpFilenameToFilepath
+ _calloc
+ _compression_decode_buffer
+ _createPowerAssertion
+ _currentTrainName
+ _dataFromHexString
+ _fUarpLayer3DownstreamEndpointDiscovery
+ _fUarpLayer3DownstreamEndpointReachable
+ _fUarpLayer3DownstreamEndpointRecvMessage
+ _fUarpLayer3DownstreamEndpointReleased
+ _fUarpLayer3DownstreamEndpointUnreachable
+ _fUarpLayer3NoFirmwareUpdateAvailable
+ _isDynamicAssetAnalytics
+ _isDynamicAssetHeySiri
+ _isDynamicAssetLogs
+ _isDynamicAssetMappedAnalytics
+ _isDynamicAssetPersonalization
+ _isDynamicAssetSysConfig
+ _isDynamicAssetVoiceAssist
+ _memcmp
+ _notify_post
+ _notify_register_check
+ _notify_set_state
+ _nullableObjectsEqual
+ _postStagingStatusForModelIdentifier
+ _releasePowerAssertion
+ _snprintf
+ _uarp4ccCompare
+ _uarpAllocPrepareTransmitBuffer2
+ _uarpAllocateTransmitBuffer2
+ _uarpAnalyticsAssetFinalize
+ _uarpAnalyticsAssetInitialize
+ _uarpApplyFlagsToString
+ _uarpAssetCompare
+ _uarpAssetProcessingComplete
+ _uarpAssetQueryPayloadInfo
+ _uarpAssetQueryPayloadMetaData
+ _uarpAssetQuerySuperBinaryMetaData
+ _uarpAssetQueueSolicitation
+ _uarpAssetRescind
+ _uarpAssetSuperBinaryVersionForProtocolVersion
+ _uarpAssetTagAnalytics
+ _uarpAssetTagAnalytics4cc
+ _uarpAssetTagChdr
+ _uarpAssetTagChdr4cc
+ _uarpAssetTagCompare
+ _uarpAssetTagHeySiriModel
+ _uarpAssetTagHeySiriModel4cc
+ _uarpAssetTagIsValid
+ _uarpAssetTagLogs
+ _uarpAssetTagLogs4cc
+ _uarpAssetTagMappedAnalytics
+ _uarpAssetTagMappedAnalytics4cc
+ _uarpAssetTagPersonalization
+ _uarpAssetTagPersonalization4cc
+ _uarpAssetTagPersonalizedFirmware
+ _uarpAssetTagPersonalizedFirmware4cc
+ _uarpAssetTagStructAnalytics
+ _uarpAssetTagStructChdr
+ _uarpAssetTagStructHeySiriModel
+ _uarpAssetTagStructLogs
+ _uarpAssetTagStructMappedAnalytics
+ _uarpAssetTagStructPersonalization
+ _uarpAssetTagStructPersonalizedFirmware
+ _uarpAssetTagStructSuperBinary
+ _uarpAssetTagStructSysconfig
+ _uarpAssetTagStructVoiceAssist
+ _uarpAssetTagSysconfig
+ _uarpAssetTagSysconfig4cc
+ _uarpAssetTagVoiceAssist
+ _uarpAssetTagVoiceAssist4cc
+ _uarpBuildMappedAnalyticsAsset
+ _uarpCallbackUpdateInformationTLV
+ _uarpCompressionHeaderEndianSwap
+ _uarpCopyDefaultInfoString
+ _uarpDownstreamEndpointGetID
+ _uarpDynamicAssetComponentURL
+ _uarpDynamicAssetURL
+ _uarpEndpointRoleToString
+ _uarpFirmwareForAccessory
+ _uarpFree
+ _uarpHtonl
+ _uarpHtonll
+ _uarpHtons
+ _uarpLogDebug
+ _uarpLogError
+ _uarpLogFault
+ _uarpLogInfo
+ _uarpLoggingCategoryToString
+ _uarpNtohl
+ _uarpNtohll
+ _uarpNtohs
+ _uarpOfferAssetToRemoteEP
+ _uarpOuiAnalytics
+ _uarpOuiCompare
+ _uarpOuiHeySiriModel
+ _uarpOuiLogs
+ _uarpOuiMappedAnalytics
+ _uarpOuiPersonalization
+ _uarpOuiSysconfig
+ _uarpOuiVoiceAssist
+ _uarpPayloadHeader2EndianSwap
+ _uarpPayloadHeaderEndianSwap
+ _uarpPayloadTagPack
+ _uarpPayloadTagStructPack
+ _uarpPayloadTagStructUnpack
+ _uarpPayloadTagUnpack
+ _uarpPersonalizationRequestAddBoardID
+ _uarpPersonalizationRequestAddBoardID64
+ _uarpPersonalizationRequestAddChipEpoch
+ _uarpPersonalizationRequestAddChipID
+ _uarpPersonalizationRequestAddChipRevision
+ _uarpPersonalizationRequestAddDigest
+ _uarpPersonalizationRequestAddECID
+ _uarpPersonalizationRequestAddEnableMixMatch
+ _uarpPersonalizationRequestAddLogicalUnitNumber
+ _uarpPersonalizationRequestAddManifestPrefix
+ _uarpPersonalizationRequestAddMeasurement
+ _uarpPersonalizationRequestAddMeasurementWithOverrides
+ _uarpPersonalizationRequestAddNonce
+ _uarpPersonalizationRequestAddNonceHash
+ _uarpPersonalizationRequestAddPayloadTag
+ _uarpPersonalizationRequestAddPrefixLUN
+ _uarpPersonalizationRequestAddPrefixNeedsLUN
+ _uarpPersonalizationRequestAddProductionMode
+ _uarpPersonalizationRequestAddRemoteAssetID
+ _uarpPersonalizationRequestAddRemoteAssetPayloadIndex
+ _uarpPersonalizationRequestAddSecurityDomain
+ _uarpPersonalizationRequestAddSecurityMode
+ _uarpPersonalizationRequestAddSoCLiveNonce
+ _uarpPersonalizationRequestAddSuffixLUN
+ _uarpPersonalizationRequestAddTicketPrefixLUN
+ _uarpPersonalizationRequestAssetFinalize
+ _uarpPersonalizationRequestAssetInitialize
+ _uarpPersonalizationRequestMoreRequestsToFollow
+ _uarpPersonalizationRequestPreparePayload
+ _uarpPlatformAssetApproveOfferVersion
+ _uarpPlatformAssetCleanup
+ _uarpPlatformAssetDataRequest
+ _uarpPlatformAssetFindByAssetContext
+ _uarpPlatformAssetFindByAssetContextAndList
+ _uarpPlatformAssetFindByAssetID
+ _uarpPlatformAssetFindByTag
+ _uarpPlatformAssetIsKnown
+ _uarpPlatformAssetOrphan
+ _uarpPlatformAssetPayloadHeaderProcess
+ _uarpPlatformAssetPayloadPullData
+ _uarpPlatformAssetPayloadPullMetaData
+ _uarpPlatformAssetProcessingCompleteInternal
+ _uarpPlatformAssetPullAllMetaData
+ _uarpPlatformAssetPullAllPayloadHeaders
+ _uarpPlatformAssetQueryAssetID
+ _uarpPlatformAssetQueryAssetVersion
+ _uarpPlatformAssetRelease
+ _uarpPlatformAssetRequestData
+ _uarpPlatformAssetRescind
+ _uarpPlatformAssetRescinded
+ _uarpPlatformAssetResponseData
+ _uarpPlatformAssetSelectedPayloadInfo
+ _uarpPlatformAssetSuperBinaryPullHeader
+ _uarpPlatformAssetSuperBinaryPullMetaData
+ _uarpPlatformAssetSuperBinaryPullPayloadHeader
+ _uarpPlatformAssetUpdateMetaData
+ _uarpPlatformCancelPendingTxMessages
+ _uarpPlatformCancelRxDynamicAssets
+ _uarpPlatformCleanupAssetsForRemoteEndpoint
+ _uarpPlatformCompareHash
+ _uarpPlatformCreateRxAsset
+ _uarpPlatformDarwinCompressBuffer
+ _uarpPlatformDarwinDecompressBuffer
+ _uarpPlatformDarwinHashFinal
+ _uarpPlatformDarwinHashInfo
+ _uarpPlatformDarwinHashInit
+ _uarpPlatformDarwinHashLog
+ _uarpPlatformDarwinHashUpdate
+ _uarpPlatformDarwinLogDebug
+ _uarpPlatformDarwinLogError
+ _uarpPlatformDarwinLogFault
+ _uarpPlatformDarwinLogInfo
+ _uarpPlatformDataTransferResume
+ _uarpPlatformDownstreamEndpointAdd
+ _uarpPlatformDownstreamEndpointAddWithID
+ _uarpPlatformDownstreamEndpointDiscovery
+ _uarpPlatformDownstreamEndpointRemove
+ _uarpPlatformDownstreamEndpointSendMessage
+ _uarpPlatformDownstreamEndpointSendMessageInternal
+ _uarpPlatformEndpointApplyStagedAssets
+ _uarpPlatformEndpointAssetAbandon
+ _uarpPlatformEndpointAssetAccept
+ _uarpPlatformEndpointAssetAcceptWithPayloadAndDecompressionWindows
+ _uarpPlatformEndpointAssetAcceptWithPayloadWindow
+ _uarpPlatformEndpointAssetCorrupt
+ _uarpPlatformEndpointAssetDeny
+ _uarpPlatformEndpointAssetFullyStaged
+ _uarpPlatformEndpointAssetGetBytesAtOffset
+ _uarpPlatformEndpointAssetIsAcceptable
+ _uarpPlatformEndpointAssetPayloadTag
+ _uarpPlatformEndpointAssetPayloadVersion
+ _uarpPlatformEndpointAssetQueryAssetLength
+ _uarpPlatformEndpointAssetQueryAssetVersion
+ _uarpPlatformEndpointAssetQueryFormatVersion
+ _uarpPlatformEndpointAssetQueryNumberOfPayloads
+ _uarpPlatformEndpointAssetQueryTag
+ _uarpPlatformEndpointAssetRelease
+ _uarpPlatformEndpointAssetRelease2
+ _uarpPlatformEndpointAssetRequestMetaData
+ _uarpPlatformEndpointAssetSetBytesAtOffset
+ _uarpPlatformEndpointAssetSetCallbacks
+ _uarpPlatformEndpointAssetSetPayloadIndex
+ _uarpPlatformEndpointAssetSetPayloadIndex2
+ _uarpPlatformEndpointAssetSetPayloadOffset
+ _uarpPlatformEndpointAssetStore
+ _uarpPlatformEndpointCleanupAssets
+ _uarpPlatformEndpointCleanupAssets2
+ _uarpPlatformEndpointDynamicAssetSolicitationDeny
+ _uarpPlatformEndpointInit
+ _uarpPlatformEndpointInit2
+ _uarpPlatformEndpointIsMessageTypePending
+ _uarpPlatformEndpointOfferAsset
+ _uarpPlatformEndpointPauseAssetTransfers
+ _uarpPlatformEndpointPayloadRequestAllHeadersAndMetaData
+ _uarpPlatformEndpointPayloadRequestData
+ _uarpPlatformEndpointPayloadRequestDataPause
+ _uarpPlatformEndpointPayloadRequestDataResume
+ _uarpPlatformEndpointPayloadRequestMetaData
+ _uarpPlatformEndpointPrepareDynamicAsset
+ _uarpPlatformEndpointPrepareSolicitedDynamicAsset
+ _uarpPlatformEndpointPrepareSuperBinary
+ _uarpPlatformEndpointProvideAssetPayloadWindow
+ _uarpPlatformEndpointQueryActiveFirmwareVersion
+ _uarpPlatformEndpointQueryStagedFirmwareVersion
+ _uarpPlatformEndpointRecvMessage
+ _uarpPlatformEndpointRemoveAssetPayloadWindow
+ _uarpPlatformEndpointRequestInfoProperty
+ _uarpPlatformEndpointRescindAllAssets
+ _uarpPlatformEndpointRescindAsset
+ _uarpPlatformEndpointResumeAssetTransfers
+ _uarpPlatformEndpointSendMessageComplete
+ _uarpPlatformEndpointSendMessageCompleteInternal
+ _uarpPlatformEndpointSendSyncMsg
+ _uarpPlatformEndpointSendVendorSpecific
+ _uarpPlatformEndpointSolicitDynamicAsset
+ _uarpPlatformEndpointStreamingRecvBytes
+ _uarpPlatformEndpointStreamingRecvDeinit
+ _uarpPlatformEndpointStreamingRecvInit
+ _uarpPlatformEndpointSuperBinaryMerge
+ _uarpPlatformEndpointWatchDogExpired
+ _uarpPlatformFindPreparedAsset
+ _uarpPlatformGarbageCollection
+ _uarpPlatformNoFirmwareUpdateAvailable
+ _uarpPlatformPayloadCleanup
+ _uarpPlatformPrepareAsset
+ _uarpPlatformQueryAccessoryInfo
+ _uarpPlatformReOfferFirmware
+ _uarpPlatformRemoteDelegateForAssetDelegate
+ _uarpPlatformRemoteEndpointAdd
+ _uarpPlatformRemoteEndpointAddEntry
+ _uarpPlatformRemoteEndpointAlloc
+ _uarpPlatformRemoteEndpointRemove
+ _uarpPlatformResponseAccessoryInfo
+ _uarpPlatformTransmitQueueLogEntry
+ _uarpPrintDataResponseDetails
+ _uarpProcessPayloadTLVInternal
+ _uarpProcessTLV
+ _uarpProcessingFlagsReasonToString
+ _uarpProcessingFlagsToString
+ _uarpProcessingStatusToString
+ _uarpRemoteEndpointID
+ _uarpRemoteEndpointIDForAsset
+ _uarpSendAssetAvailableNotificationAck
+ _uarpSendAssetProcessingNotificationAck
+ _uarpSendAssetRequestData
+ _uarpSendDataTransferNotificationPause
+ _uarpSendDataTransferNotificationResume
+ _uarpSendDownstreamEndpointDiscovery
+ _uarpSendDownstreamEndpointReachable
+ _uarpSendDownstreamEndpointUnreachable
+ _uarpSendDynamicAssetPreProcessingStatus
+ _uarpSendDynamicAssetPreProcessingStatusAck
+ _uarpSendInformationRequest
+ _uarpSendNoFirmwareUpdateAvailable
+ _uarpSendVendorSpecific
+ _uarpSendVersionDiscoveryRequest
+ _uarpSendVersionDiscoveryResponse
+ _uarpSolicitDynamicAsset
+ _uarpStageStatusToString
+ _uarpStatusCodeToString
+ _uarpSuperBinaryHeaderEndianSwap
+ _uarpTagStructPack32
+ _uarpTagStructUnpack32
+ _uarpTransmitBuffer2
+ _uarpTransmitBufferUpstream
+ _uarpTransmitQueueAssetRescinded
+ _uarpTransmitQueuePendingEntryComplete
+ _uarpTransmitQueueProcessRecv
+ _uarpTransmitQueueService
+ _uarpTransmitQueuesCleanup
+ _uarpUtilsConcatenateURLs
+ _uarpVersionCompare
+ _uarpVersionCompareStrings
+ _uarpVersionEndianSwap
+ _uarpZalloc
+ _uarpZero
+ _vsnprintf
- _UARPStringCrashAnalyticsDirectoryFilePath
- _UARPStringTapToRadarFilePath
- _kUARPStringBsdNotificationPersonalizationNeededBTLEServer
- _kUARPStringCMAPDecoderId
- _kUARPStringCrashAnalyticsDirectory
- _kUARPStringTapToRadar
CStrings:
+ "%!@(MISSING)/%!@(MISSING)-%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)"
+ "%!s(MISSING) (%!s(MISSING))"
+ "%!s(MISSING)%!@(MISSING)"
+ "-%!@(MISSING)"
+ ".uarp"
+ "/%!@(MISSING)"
+ "<unknown>"
+ "Active Firmware Version Equal to Asset"
+ "Active Firmware Version Greater than Asset"
+ "Asset Corrupt"
+ "Asset Data Paused"
+ "Asset Decompression Failure"
+ "Asset Id Unknown"
+ "Asset In Flight"
+ "Asset Invalid Compression"
+ "Asset No Bytes Remaining"
+ "Asset Not Found"
+ "Asset Transfer Complete"
+ "BOOL createPowerAssertion(NSString *__strong, IOPMAssertionID *)"
+ "BOOL releasePowerAssertion(IOPMAssertionID)"
+ "Better Transport"
+ "Cancelled Asset Tag"
+ "Controller"
+ "Corrupt SuperBinary"
+ "Data Transfer Paused"
+ "Device Error"
+ "Duplicate Accessory"
+ "Duplicate Controller"
+ "Duplicate Message ID"
+ "Error decompressing buffer for payload"
+ "Exceeded Packet Retry"
+ "Failure"
+ "Higher Version Active"
+ "HigherVersion"
+ "Host Controller"
+ "In Progress"
+ "In Use"
+ "Incompatible Protocol Version"
+ "Invalid Argument"
+ "Invalid Asset Tag"
+ "Invalid Asset Type"
+ "Invalid Data Request Length"
+ "Invalid Data Request Offset"
+ "Invalid Data Request Type"
+ "Invalid Data Response"
+ "Invalid Data Response Length"
+ "Invalid Data Transfer Notification"
+ "Invalid Function Pointer"
+ "Invalid Length"
+ "Invalid Message"
+ "Invalid Message Length"
+ "Invalid Object"
+ "Invalid Offset"
+ "Invalid Payload"
+ "Invalid Payload Header"
+ "Invalid Super Binary Header"
+ "Invalid TLV"
+ "Low Battery"
+ "MetaData Corrupt"
+ "MetaData Overflow"
+ "MetaData Type Not Found"
+ "Mid Upload"
+ "Mismatch Data Offset"
+ "Mismatch Personalization Option"
+ "Mismatch UUID"
+ "Needs Restart"
+ "No MetaData"
+ "No Resources"
+ "No Version Agreement"
+ "Nothing Staged"
+ "Out Of Order Message ID"
+ "Personalization Failure"
+ "PreventUserIdleSystemSleep"
+ "Priority Activity"
+ "Processing Error"
+ "Processing Incomplete"
+ "Same Version Active"
+ "Same Version Staged"
+ "Staged Firmware Version Equal to Asset"
+ "Staged Firmware Version Greater than Asset"
+ "Success"
+ "UARP.LAYER2 <%!s(MISSING)> Cannot find downstream endpoint"
+ "Unknown Accessory"
+ "Unknown Asset"
+ "Unknown Controller"
+ "Unknown Data Transfer State"
+ "Unknown Downstream Endpoint"
+ "Unknown Failure"
+ "Unknown Information Option"
+ "Unknown Message Type"
+ "Unknown Payload"
+ "Unknown Personalization Option"
+ "Unsupported"
+ "Unsupported Asset Tag"
+ "Unsupported Hardware Revision"
+ "Unsupported Message Type"
+ "Upload Abandoned"
+ "Upload Complete"
+ "Upload Denied"
+ "assert"
+ "com.apple.uarp.embedded"
+ "com.apple.uarp.stagingstatus."
+ "downstream"
+ "memory"
+ "platform"
+ "product"
+ "protocolaccessory"
+ "protocolcontroller"
+ "streaming"
+ "success"
+ "transmitqueue"
+ "uarpFirmwareForAccessory"
+ "uarpMsgRecvDownstreamEndpointMessage"
- "com.apple.uarp.BTLEServer.personalizationNeeded"
- "crsh"
- "decoderId"
- "taptoradar"

```
