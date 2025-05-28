## IDS

> `/System/Library/PrivateFrameworks/IDS.framework/IDS`

```diff

-1814.100.1.2.2
-  __TEXT.__text: 0x112898
-  __TEXT.__auth_stubs: 0x1a90
-  __TEXT.__objc_methlist: 0x8918
+1814.200.71.2.7
+  __TEXT.__text: 0x113920
+  __TEXT.__auth_stubs: 0x1aa0
+  __TEXT.__objc_methlist: 0x8980
   __TEXT.__const: 0x2b8
-  __TEXT.__gcc_except_tab: 0x3240
-  __TEXT.__oslogstring: 0x15d67
-  __TEXT.__cstring: 0xef54
+  __TEXT.__gcc_except_tab: 0x3230
+  __TEXT.__oslogstring: 0x1604b
+  __TEXT.__cstring: 0xef7a
   __TEXT.__dlopen_cstrs: 0x102
   __TEXT.__ustring: 0xac
-  __TEXT.__unwind_info: 0x40a8
-  __TEXT.__objc_classname: 0x132b
-  __TEXT.__objc_methname: 0x19ee8
-  __TEXT.__objc_methtype: 0x63e8
-  __TEXT.__objc_stubs: 0x10ce0
-  __DATA_CONST.__got: 0x998
-  __DATA_CONST.__const: 0x42b0
+  __TEXT.__unwind_info: 0x40c0
+  __TEXT.__objc_classname: 0x1329
+  __TEXT.__objc_methname: 0x1a056
+  __TEXT.__objc_methtype: 0x63a5
+  __TEXT.__objc_stubs: 0x10dc0
+  __DATA_CONST.__got: 0x9a0
+  __DATA_CONST.__const: 0x4330
   __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2ede0
-  __DATA_CONST.__objc_selrefs: 0x5528
+  __DATA_CONST.__objc_const: 0x2eca0
+  __DATA_CONST.__objc_selrefs: 0x5558
   __AUTH_CONST.__objc_const: 0x31c0
-  __AUTH_CONST.__cfstring: 0x6240
+  __AUTH_CONST.__cfstring: 0x6200
   __AUTH_CONST.__const: 0x1220
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0xd58
+  __AUTH_CONST.__auth_got: 0xd60
   __AUTH.__objc_data: 0x1630
   __DATA.__objc_protorefs: 0xa8
-  __DATA.__objc_classrefs: 0x730
+  __DATA.__objc_classrefs: 0x728
   __DATA.__objc_superrefs: 0x358
-  __DATA.__objc_ivar: 0xa70
+  __DATA.__objc_ivar: 0xa80
   __DATA.__data: 0x1350
   __DATA.__bss: 0x199c
   __DATA_DIRTY.__objc_data: 0x13b0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5440
-  Symbols:   1360
-  CStrings:  7757
+  - /usr/lib/libz.1.dylib
+  Functions: 5454
+  Symbols:   1361
+  CStrings:  7779
 
Symbols:
+ _IDSGlobalLinkMetricEventDirectConnectionAddAttempt
+ _crc32_z
- _OBJC_CLASS_$_IDSDeviceIdentity
CStrings:
+ "\x14S!R\x12\xaf\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\a"
+ "-[_IDSGroupSession updateParticipantInfo:]"
+ "<%@> RX [Final] %f bytes/s %f packets/s"
+ "<%@> TX [Final] %f bytes/s %f packets/s"
+ "<%@> pending outgoing %f bytes/s %f packets/s"
+ "<%@> pending outgoing [Final] %f bytes/s %f packets/s"
+ "<%@> pending outgoing the first data packet (size: %lu)"
+ "HTTP2"
+ "Q32@0:8r^v16Q24"
+ "Recv datagram checksum %uB/%lu"
+ "Send datagram checksum %uB/%lu"
+ "Using client fromID for query: { fromID: %@ }"
+ "_lastPendingOutgoingStatReport"
+ "_logChecksum:length:"
+ "_logFinalStats"
+ "_logPendingSendingStats:"
+ "_pendingOutgoingBytes"
+ "_pendingOutgoingPackets"
+ "_requestRemoteDevicesForDestination:fromID:service:listenerID:waitForReply:completionBlock:"
+ "_requestStatusForDestinations:fromID:service:waitForReply:forceRefresh:bypassLimit:listenerID:completionBlock:"
+ "enableP2PlinksForSession:"
+ "finishedProvisioningPseudonym called - block invoke {pseudonym: %@, success:%@, requestUUID: %@, error:%@}"
+ "finishedRenewingPseudonym called - block invoke {pseudonym: %@, success:%@, requestUUID: %@, error:%@}"
+ "finishedRevokingPseudonymWithSuccess called - block invoke {success:%@, requestUUID: %@, error:%@}"
+ "from"
+ "setForceTCPFallbackOnCellUsingReinitiate:"
+ "setForceTCPFallbackOnCellUsingReinitiate:%@ for session:%@"
+ "setForceTCPFallbackOnCellUsingReinitiate:forSessionWithUniqueID:"
+ "setForceTCPFallbackOnWiFiUsingReinitiate:"
+ "setForceTCPFallbackOnWiFiUsingReinitiate:%@ for session:%@"
+ "setForceTCPFallbackOnWiFiUsingReinitiate:forSessionWithUniqueID:"
+ "triggerKTCDPAccountStatusNotificationWithAccountStatus:"
+ "updateParticipantInfo:"
+ "updateParticipantInfo:forGroup:sessionID:"
+ "v60@0:8@16@24@32@40B48@?52"
+ "v68@0:8@16@24@32B40B44B48@52@?60"
- "\v"
- "\x14S!R\x12\x7f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\a"
- "%d-recv"
- "%d-send"
- "Incoming Registered Identities"
- "_requestRemoteDevicesForDestination:service:listenerID:waitForReply:completionBlock:"
- "_requestStatusForDestinations:service:waitForReply:forceRefresh:bypassLimit:listenerID:completionBlock:"
- "connection:didUpdateDeviceIdentity:error:context:"
- "setCallScreeningModeDisabled:"
- "unarchivedObjectOfClass:fromData:error:"
- "updateDeviceIdentity:error:"
- "v32@0:8@\"NSData\"16@\"NSError\"24"
- "v48@0:8@\"IDSConnection\"16@\"IDSDeviceIdentity\"24@\"NSError\"32@\"IDSMessageContext\"40"
- "v60@0:8@16@24B32B36B40@44@?52"

```
