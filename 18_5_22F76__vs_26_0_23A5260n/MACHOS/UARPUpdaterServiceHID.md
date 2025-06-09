## UARPUpdaterServiceHID

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceHID.xpc/UARPUpdaterServiceHID`

```diff

-1207.120.19.0.0
-  __TEXT.__text: 0x1c0bc
+1338.0.21.0.2
+  __TEXT.__text: 0x1d6ac
   __TEXT.__auth_stubs: 0x780
-  __TEXT.__objc_stubs: 0x27a0
-  __TEXT.__objc_methlist: 0x10b0
+  __TEXT.__objc_stubs: 0x2800
+  __TEXT.__objc_methlist: 0x1180
   __TEXT.__gcc_except_tab: 0xe4
-  __TEXT.__objc_methname: 0x35d0
+  __TEXT.__objc_methname: 0x369a
   __TEXT.__objc_classname: 0x1ac
-  __TEXT.__objc_methtype: 0xb29
-  __TEXT.__cstring: 0x182f
+  __TEXT.__objc_methtype: 0xb8d
+  __TEXT.__cstring: 0x1fb0
   __TEXT.__oslogstring: 0x1037
   __TEXT.__const: 0xb0
-  __TEXT.__unwind_info: 0x750
+  __TEXT.__unwind_info: 0x780
   __DATA_CONST.__auth_got: 0x3d0
   __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0x738
+  __DATA_CONST.__const: 0x890
   __DATA_CONST.__cfstring: 0x580
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x1b70
-  __DATA.__objc_selrefs: 0xd00
+  __DATA.__objc_const: 0x1be8
+  __DATA.__objc_selrefs: 0xd28
   __DATA.__objc_ivar: 0xd4
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x315

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6096989B-3F25-3A2A-9551-24C15C5C6092
-  Functions: 715
-  Symbols:   522
-  CStrings:  981
+  UUID: C1D09097-F85A-3272-B237-3C1B1AD47581
+  Functions: 758
+  Symbols:   559
+  CStrings:  1043
 
Symbols:
+ _AUSandboxPlatformInitWithBundleIdentifierHomeDirectory
+ _AUSandboxPlatformInitWithHomeDirectory
+ _UARPLayer2EndpointBulkInformationQuery
+ _UARPLayer2EndpointBulkInformationResponse
+ _UARPLayer2EndpointIDComponents
+ _UARPLayer2EndpointIDs
+ _UARPLayer2MonotonicClockTime
+ _UARPProtocolVersionRequiresDownstreamMessageACK
+ _UARPProtocolVersionResponseAdjustByProtocolVersion
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
+ "initWithURL:serialNumber:"
+ "queryCompleteForAccessory:nonceHash:error:"
+ "queryCompleteForAccessory:nonceSeed:error:"
+ "queryCompleteForAccessoryID:nonceHash:error:"
+ "queryCompleteForAccessoryID:nonceSeed:error:"
+ "uarpMsgRecvDownstreamEndpointReachable"
+ "uarpMsgRecvDownstreamEndpointUnreachable"
+ "uarpMsgRecvDownstreamEndpointUnreachableAck"
+ "uarpPlatformEndpointRecvMessage"
+ "uarpTransmitEntryIsValidToSend"
+ "v40@0:8@\"UARPAccessory\"16@\"NSData\"24@\"NSError\"32"
+ "v40@0:8@\"UARPAccessoryID\"16@\"NSData\"24@\"NSError\"32"
- "<ROLE=%s> UARP.LAYER2.DATA.RESP Outstanding Data Request <%s>, offset=0x%08x, requestedlength=%u"

```
