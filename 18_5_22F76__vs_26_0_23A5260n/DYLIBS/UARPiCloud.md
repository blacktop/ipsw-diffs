## UARPiCloud

> `/System/Library/PrivateFrameworks/UARPiCloud.framework/UARPiCloud`

```diff

-1207.120.19.0.0
-  __TEXT.__text: 0x1ae14
-  __TEXT.__auth_stubs: 0x690
+1338.0.21.0.2
+  __TEXT.__text: 0x1c05c
+  __TEXT.__auth_stubs: 0x6a0
   __TEXT.__objc_methlist: 0xa0c
   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x1c58
-  __TEXT.__oslogstring: 0x158d
+  __TEXT.__cstring: 0x23d9
+  __TEXT.__oslogstring: 0x15d9
   __TEXT.__gcc_except_tab: 0x13c
-  __TEXT.__unwind_info: 0x5c8
+  __TEXT.__unwind_info: 0x5e8
   __TEXT.__objc_classname: 0x11c
   __TEXT.__objc_methname: 0x2ff7
   __TEXT.__objc_methtype: 0x4ac
   __TEXT.__objc_stubs: 0x25c0
   __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0x788
+  __DATA_CONST.__const: 0x8e0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa90
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x358
+  __AUTH_CONST.__auth_got: 0x360
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0xdc0
   __AUTH_CONST.__objc_const: 0x17a8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 287ECE14-4F21-3C65-B5AA-70181B46290C
-  Functions: 649
-  Symbols:   2024
-  CStrings:  1029
+  UUID: 5E401245-9F0E-3E98-AC57-0A0951BE6CCF
+  Functions: 683
+  Symbols:   2094
+  CStrings:  1086
 
Symbols:
+ _UARPLayer2EndpointBulkInformationQuery
+ _UARPLayer2EndpointBulkInformationResponse
+ _UARPLayer2EndpointIDComponents
+ _UARPLayer2EndpointIDs
+ _UARPLayer2MonotonicClockTime
+ _UARPProtocolVersionRequiresDownstreamMessageACK
+ _UARPProtocolVersionResponseAdjustByProtocolVersion
+ ___60-[UARPiCloudAssetManager handleRemoteFetchCompletion:error:]_block_invoke.308
+ ___60-[UARPiCloudAssetManager handleRemoteFetchCompletion:error:]_block_invoke.309
+ ___64-[UARPiCloudManager fetchZoneChangesInContainer:forAccessories:]_block_invoke.303
+ ___64-[UARPiCloudManager fetchZoneChangesInContainer:forAccessories:]_block_invoke.305
+ ___64-[UARPiCloudManager fetchZoneChangesInContainer:forAccessories:]_block_invoke_2.307
+ ___64-[UARPiCloudManager fetchZoneChangesInContainer:forAccessories:]_block_invoke_3.308
+ ___70-[UARPiCloudManager fetchRemoteDatabaseChangesInContainer:completion:]_block_invoke.286
+ ___70-[UARPiCloudManager fetchRemoteDatabaseChangesInContainer:completion:]_block_invoke_2.287
+ ___72-[UARPiCloudAssetManager handleReleaseNotesDownloadRequestForAccessory:]_block_invoke.319
+ ___74-[UARPiCloudAssetManager handleRemoteFirmwareDownloadRequestForAccessory:]_block_invoke.311
+ _getuid
+ _isRunningAsAccessoryUpdaterDaemonRoleAccount
+ _uarpAllocateTransmitBuffers
+ _uarpFilepathForRemotePath.cold.3
+ _uarpMessageAdjustedForEndpointID
+ _uarpMessagePrintToBuffer
+ _uarpMessageTypeToString
+ _uarpMsgRecvDownstreamEndpointMessageSendAck
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
- ___60-[UARPiCloudAssetManager handleRemoteFetchCompletion:error:]_block_invoke.305
- ___60-[UARPiCloudAssetManager handleRemoteFetchCompletion:error:]_block_invoke.306
- ___64-[UARPiCloudManager fetchZoneChangesInContainer:forAccessories:]_block_invoke.300
- ___64-[UARPiCloudManager fetchZoneChangesInContainer:forAccessories:]_block_invoke.302
- ___64-[UARPiCloudManager fetchZoneChangesInContainer:forAccessories:]_block_invoke_2.301
- ___64-[UARPiCloudManager fetchZoneChangesInContainer:forAccessories:]_block_invoke_3.305
- ___70-[UARPiCloudManager fetchRemoteDatabaseChangesInContainer:completion:]_block_invoke.283
- ___70-[UARPiCloudManager fetchRemoteDatabaseChangesInContainer:completion:]_block_invoke_2.284
- ___72-[UARPiCloudAssetManager handleReleaseNotesDownloadRequestForAccessory:]_block_invoke.316
- ___74-[UARPiCloudAssetManager handleRemoteFirmwareDownloadRequestForAccessory:]_block_invoke.308
- _uarpAssetQueueSolicitation
- _uarpAvailableTransmitBuffer
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
+ "%s: Failed to remove local file with error %@"
+ "%s: Removing stale file at %@"
+ "<ROLE=%s> ESPRESSO: UARP.LAYER2.RECV.MSG: Length too small <%u>"
+ "<ROLE=%s> UARP.LAYER2.DATA.RESP offset=0x%08x, requestedlength=%u"
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
+ "Information Request"
+ "Information Response"
+ "Invalid EndpointID"
+ "No Firmware Update Available"
+ "No Firmware Update Available Ack"
+ "Sync"
+ "Vendor Specific"
+ "Version Discovery Request"
+ "Version Discovery Response"
+ "uarpMsgRecvDownstreamEndpointReachable"
+ "uarpMsgRecvDownstreamEndpointUnreachable"
+ "uarpMsgRecvDownstreamEndpointUnreachableAck"
+ "uarpPlatformEndpointRecvMessage"
+ "uarpTransmitEntryIsValidToSend"
- "<ROLE=%s> UARP.LAYER2.DATA.RESP Outstanding Data Request <%s>, offset=0x%08x, requestedlength=%u"

```
