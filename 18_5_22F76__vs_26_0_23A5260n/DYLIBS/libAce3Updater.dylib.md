## libAce3Updater.dylib

> `/usr/lib/updaters/libAce3Updater.dylib`

```diff

-1207.120.19.0.0
-  __TEXT.__text: 0x1da0c
-  __TEXT.__auth_stubs: 0x8a0
+1338.0.21.0.2
+  __TEXT.__text: 0x1efd0
+  __TEXT.__auth_stubs: 0x8b0
   __TEXT.__objc_methlist: 0x384
-  __TEXT.__cstring: 0x54e2
+  __TEXT.__cstring: 0x5df3
   __TEXT.__const: 0x240
   __TEXT.__oslogstring: 0x7
-  __TEXT.__unwind_info: 0x760
+  __TEXT.__unwind_info: 0x790
   __TEXT.__objc_classname: 0x84
   __TEXT.__objc_methname: 0x9f0
-  __TEXT.__objc_methtype: 0x7d4
-  __TEXT.__objc_stubs: 0x960
+  __TEXT.__objc_methtype: 0x83c
+  __TEXT.__objc_stubs: 0x940
   __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0x488
+  __DATA_CONST.__const: 0x5e0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x298
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x458
-  __AUTH_CONST.__cfstring: 0xe60
+  __AUTH_CONST.__auth_got: 0x460
+  __AUTH_CONST.__cfstring: 0xf00
   __AUTH_CONST.__objc_const: 0x918
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x98

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8A19A21B-D2A0-3B7E-AEB2-3F9997D9845B
-  Functions: 901
-  Symbols:   1602
-  CStrings:  914
+  UUID: D0387728-317F-38FB-A467-870CB4653DAD
+  Functions: 940
+  Symbols:   1643
+  CStrings:  982
 
Symbols:
+ _CoreUARPRestoreQueryOutstandingInfoProperties
+ _UARPLayer2EndpointBulkInformationQuery
+ _UARPLayer2EndpointBulkInformationResponse
+ _UARPLayer2EndpointIDComponents
+ _UARPLayer2EndpointIDs
+ _UARPLayer2MonotonicClockTime
+ _UARPProtocolVersionRequiresDownstreamMessageACK
+ _UARPProtocolVersionResponseAdjustByProtocolVersion
+ _UarpRestoreInitializeCommon
+ _UarpRestoreInitializeEndpoint3
+ _clock_gettime
+ _fRestoreUARPMonotonicClock
+ _uarpAllocateTransmitBuffers
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
- _objc_msgSend$verboseLog:
- _uarpAssetQueueSolicitation
- _uarpAvailableTransmitBuffer
- _uarpPlatformAssetApproveOfferVersion
- _uarpPlatformEndpointIsMessageTypePending
- _uarpPlatformTransmitQueueLogEntry
- _uarpTransmitQueuePendingEntryComplete
- _uarpTransmitQueueProcessRecv
CStrings:
+ "%@: Don't Offer / Stage Firmware"
+ "%@: Maybe Offer / Stage Firmware"
+ "%@: Really Offer / Stage Firmware"
+ "%s: <ROLE=%s> : Add Downstream Endpoint <Local=%p> <Remote=%p> DS.ID <%hu>"
+ "%s: <ROLE=%s> : RemoveDownstream Endpoint <Local=%p> <Remote=%p> DS.ID <%hu>"
+ "%s: Don't offer IM4M Asset to Updater(LUN:%d,RouterID:%d); is done"
+ "%s: ESPRESSO Corrupt Entry ? pBuffer = %p, pMsg = %p"
+ "%s: ESPRESSO:Bonus Message <type=0x%04x, length=x0x%04x, id=0x%04x>"
+ "%s: ESPRESSO:Message <type=0x%04x, id=0x%04x> Length too big ! expected <%u>, got <%u>"
+ "%s: ESPRESSO:Message <type=0x%04x, id=0x%04x> Length too small ! expected <%u>, got <%u>"
+ "%s: Maybe Offer IM4M Asset to Updater(LUN:%d,RouterID:%d); %@"
+ "%s: More TSS Request for Updater(LUN:%d,RouterID:%d)"
+ "%s: Offer IM4M Asset to Updater(LUN:%d,RouterID:%d)"
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
+ "CoreUARPRestoreQueryOutstandingInfoProperties"
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
+ "UARP Restore: %s: Asset fully transfered; %c%c%c%c"
+ "UARP Restore: %s: Firmware Asset fully transfered"
+ "UARP Restore: %s: Protocol Version Not Selected; defer info queries"
+ "UARP Restore: %s: Protocol Version Selected %d, was previously %d"
+ "UARP Restore: %s: Query %d info properties and %d Apple properties"
+ "UARP Restore: %s: uarpPlatformEndpointRequestInfoProperty( Apple - %d )"
+ "UARP Restore: %s: uarpPlatformEndpointRequestInfoProperty( Info - %d )"
+ "UARP Restore: UARP RX: Asset Available Notification; Asset ID %u"
+ "UARP Restore: UARP RX: Asset Processing Notification ACK; Asset ID %u"
+ "UARP Restore: UARP RX: Asset Processing Notification; Asset ID %u"
+ "UARPSoCUpdaterApplyComplete"
+ "UARPSoCUpdaterFirmwareTssRequest"
+ "UARPSoCUpdaterLayer4ApplePropertyUpdate"
+ "UARPSoCUpdaterLayer4PropertiesComplete"
+ "UARPSoCUpdaterLayer4UARPPropertyUpdate"
+ "UARPSoCUpdaterStagingComplete"
+ "Vendor Specific"
+ "Version Discovery Request"
+ "Version Discovery Response"
+ "^{_uarpRestoreEndpoint={uarpRestoreLayer3Callbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}{uarpPlatformOptionsObj=IIISCSSSiSSCSCC}{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}{uarpPlatformEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSCSCC}^v{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}^viI^^{uarpPlatformRemoteEndpoint}^{uarpPlatformAsset}iCi^?S^{uarpLayer2EndpointIDInfo}S^{uarpDownstreamEndpointObj}I^{uarpMemoryTracker}}{uarpPlatformEndpointApple=CCCC{uarpPlatformEndpointAppleCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}}{uarpPlatformRemoteEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSCSCC}^vSSSCiCCSS{UARPStatistics=IIII}^{UARP4ccTag}^{uarpPlatformStreamingBuffer}^{uarpPlatformTransmitBufferEntry}^{uarpPlatformTransmitBufferEntry}S{UARPVersion=IIII}{UARPVersion=IIII}^{uarpPlatformRemoteEndpoint}}^{_uarpRestoreAsset}^{_uarpRestoreAsset}^vCSi^ii^i****{UARPVersion=IIII}{UARPVersion=IIII}@@****(?=IQ)IIQ*IIIIICCCCI*CIIII^vI*ICCC*I}"
+ "fRestoreUARPProtocolVersion"
+ "uarpMsgRecvDownstreamEndpointReachable"
+ "uarpMsgRecvDownstreamEndpointUnreachable"
+ "uarpMsgRecvDownstreamEndpointUnreachableAck"
+ "uarpPlatformEndpointRecvMessage"
+ "uarpTransmitEntryIsValidToSend"
- "%s: %@"
- "%s: NULL fSolicitProgress"
- "%s: Skipping Offer Tss Response. Updater(LUN:%d,RouterID:%d) has finished."
- "<ROLE=%s> UARP.LAYER2.DATA.RESP Outstanding Data Request <%s>, offset=0x%08x, requestedlength=%u"
- "NO"
- "UARP Restore (Asset Solicitation): %s: Get %u Bytes from offset %u"
- "UARP Restore (Asset Solicitation): %s: Set %u Bytes from offset %u"
- "UARP Restore (IM4M): Get %u Bytes from offset %u"
- "UARP Restore: Get %u Bytes from offset %u"
- "UARP Restore: UARP TX: Buffer = %p, Payload Length = %u, Type = 0x%04x, Total Length = %u, ID = %u"
- "UarpRestoreLayer3AssetSolicitationProgress"
- "YES"
- "^{_uarpRestoreEndpoint={uarpRestoreLayer3Callbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}{uarpPlatformOptionsObj=IIISCSSSiSSC}{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}{uarpPlatformEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSC}^v{uarpPlatformEndpointCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}^viI^^{uarpPlatformRemoteEndpoint}^{uarpPlatformAsset}iCi^?S}{uarpPlatformEndpointApple=CCCC{uarpPlatformEndpointAppleCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}}{uarpPlatformRemoteEndpoint={uarpPlatformOptionsObj=IIISCSSSiSSC}^vSCiCCSS{UARPStatistics=IIII}^{UARP4ccTag}^{uarpPlatformStreamingBuffer}S^^{uarpPlatformTransmitBufferEntry}S^^{uarpPlatformTransmitBufferEntry}^{uarpPlatformTransmitBufferEntry}S{UARPVersion=IIII}{UARPVersion=IIII}^{uarpPlatformRemoteEndpoint}}^{_uarpRestoreAsset}^{_uarpRestoreAsset}^vCS****{UARPVersion=IIII}{UARPVersion=IIII}@@****(?=IQ)IIQ*IIIIICCCCI*CIIII^vI*ICCC*I}"
- "void UARPSoCUpdaterApplyComplete(void *, uint32_t, uint32_t)"
- "void UARPSoCUpdaterFirmwareTssRequest(void *, void *, void *, char *, UARPBool)"
- "void UARPSoCUpdaterLayer4ApplePropertyUpdate(void *, uint32_t)"
- "void UARPSoCUpdaterLayer4PropertiesComplete(void *)"
- "void UARPSoCUpdaterLayer4UARPPropertyUpdate(void *, uint32_t)"
- "void UARPSoCUpdaterStagingComplete(void *, uint32_t, uint32_t)"

```
