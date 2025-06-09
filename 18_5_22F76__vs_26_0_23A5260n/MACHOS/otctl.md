## otctl

> `/usr/sbin/otctl`

```diff

-61439.122.1.0.0
-  __TEXT.__text: 0x128b0
+61901.0.9.0.1
+  __TEXT.__text: 0x147dc
   __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_stubs: 0x1fe0
-  __TEXT.__objc_methlist: 0xb44
+  __TEXT.__objc_stubs: 0x2380
+  __TEXT.__objc_methlist: 0xbec
   __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0x65c
-  __TEXT.__objc_methname: 0x329f
-  __TEXT.__cstring: 0x2df8
+  __TEXT.__gcc_except_tab: 0x734
+  __TEXT.__objc_methname: 0x3710
+  __TEXT.__cstring: 0x31f0
   __TEXT.__objc_classname: 0xb5
-  __TEXT.__objc_methtype: 0x443
+  __TEXT.__objc_methtype: 0x497
   __TEXT.__oslogstring: 0xa5
-  __TEXT.__unwind_info: 0x468
+  __TEXT.__unwind_info: 0x4b8
   __DATA_CONST.__auth_got: 0x2c8
-  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__got: 0x188
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x3e8
-  __DATA_CONST.__cfstring: 0xda0
+  __DATA_CONST.__const: 0x460
+  __DATA_CONST.__cfstring: 0xe60
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xd30
-  __DATA.__objc_selrefs: 0xc20
-  __DATA.__objc_ivar: 0xac
+  __DATA_CONST.__objc_arraydata: 0x20
+  __DATA_CONST.__objc_dictobj: 0x50
+  __DATA.__objc_const: 0xdb0
+  __DATA.__objc_selrefs: 0xd30
+  __DATA.__objc_ivar: 0xb4
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x128
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
+  - /System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle
   - /System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F17562E8-5EDC-3F79-B2C5-72F2392C132E
-  Functions: 285
-  Symbols:   148
-  CStrings:  1125
+  UUID: 8E410748-E4A7-3567-AB0B-4FFB30C77DC3
+  Functions: 305
+  Symbols:   149
+  CStrings:  1203
 
Symbols:
+ _OBJC_CLASS_$_AAFAnalyticsEventSecurity
+ _OBJC_CLASS_$_SecAsyncPiper
+ _kSecurityRTCErrorDomain
+ _kSecurityRTCEventCategoryAccountDataAccessRecovery
+ _kSecurityRTCEventNameOctagonTrustLost
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
CStrings:
+ "CLI invoked departure"
+ "Check current peer iCSC validity"
+ "Checking Escrow Check completed."
+ "Error checking escrow check: %s\n"
+ "Error fetching trusted full peer count: %s\n"
+ "Error fetching trusted peer count: %s\n"
+ "Error resetting icsc repair rate-limiting: %s\n"
+ "Failed to remove unreadable CK data: %s\n"
+ "Fetch total trusted peers"
+ "Fetch trusted full peers"
+ "Perform IdMS update as part of health check"
+ "Perform dangling peer cleanup as part of health check"
+ "Remove Unreadable CK Data"
+ "Removed unreadable CK data."
+ "Reset icsc repair rate-limiting"
+ "Simulates receiving a TDL changed push"
+ "Successfully reset icsc repair rate-limiting."
+ "TQ,N,V_lastEscrowRepairSucceeded"
+ "TQ,N,V_lastEscrowRepairTriggered"
+ "Total trusted full peers: %d.\n"
+ "Total trusted peers: %d.\n"
+ "_lastEscrowRepairSucceeded"
+ "_lastEscrowRepairTriggered"
+ "_setError"
+ "danglingPeerCleanup"
+ "data"
+ "deviceSessionID"
+ "dictWithError:"
+ "errorWithDomain:code:description:"
+ "escrowCheck"
+ "escrowCheck:isBackgroundCheck:reply:"
+ "escrowCheck:json:"
+ "fetchTotalTrustedPeersWithArguments:json:"
+ "fetchTrustedFullPeersWithArguments:json:"
+ "flowID"
+ "getBytes:range:"
+ "hasError"
+ "hasLastEscrowRepairSucceeded"
+ "hasLastEscrowRepairTriggered"
+ "hasWalrus"
+ "healthCheck:skipRateLimitingCheck:repair:danglingPeerCleanup:updateIdMS:json:"
+ "healthCheck:skipRateLimitingCheck:repair:danglingPeerCleanup:updateIdMS:reply:"
+ "i44@0:8@16B24B28B32B36B40"
+ "icsc-repair-reset"
+ "icscRepairReset:reply:"
+ "icscRepairResetWithArguments:json:"
+ "initWithError:"
+ "initWithKeychainCircleMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:canSendMetrics:category:"
+ "lastEscrowRepairSucceeded"
+ "lastEscrowRepairTriggered"
+ "length"
+ "performCKServerUnreadableDataRemoval"
+ "performCKServerUnreadableDataRemoval:appleID:isGuitarfish:dsid:"
+ "performCKServerUnreadableDataRemoval:error:"
+ "performCKServerUnreadableDataRemoval:isGuitarfish:accountIsW:altDSID:reply:"
+ "position"
+ "resetAndEstablish:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isGuitarfish:accountIsW:reply:"
+ "sendMetricWithResult:error:"
+ "setHasLastEscrowRepairSucceeded:"
+ "setHasLastEscrowRepairTriggered:"
+ "setLastEscrowRepairSucceeded:"
+ "setLastEscrowRepairTriggered:"
+ "setPosition:"
+ "simulate-receive-tdl-push"
+ "simulateReceiveTDLChangePush:json:"
+ "simulateReceiveTDLChangePush:reply:"
+ "total-trusted-peers"
+ "total_trusted_full_peer_count"
+ "total_trusted_peer_count"
+ "trusted-full-peers"
+ "trustedFullPeers:reply:"
+ "updateIdMS"
+ "v24@?0@\"NSNumber\"8@\"NSError\"16"
+ "v24@?0@\"OTEscrowCheckCallResult\"8@\"NSError\"16"
+ "xpcFd"
+ "{?=\"epoch\"b1\"lastEscrowRepairSucceeded\"b1\"lastEscrowRepairTriggered\"b1\"lastHealthCheckup\"b1\"attemptedJoin\"b1\"cdpState\"b1\"icloudAccountState\"b1\"sendingMetricsPermitted\"b1\"trustState\"b1\"isInheritedAccount\"b1\"warmedEscrowCache\"b1\"warnedTooManyPeers\"b1}"
- "healthCheck:skipRateLimitingCheck:repair:json:"
- "healthCheck:skipRateLimitingCheck:repair:reply:"
- "performCKServerUnreadableDataRemoval:isGuitarfish:altDSID:reply:"
- "resetAndEstablish:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isGuitarfish:reply:"
- "status:reply:"
- "{?=\"epoch\"b1\"lastHealthCheckup\"b1\"attemptedJoin\"b1\"cdpState\"b1\"icloudAccountState\"b1\"sendingMetricsPermitted\"b1\"trustState\"b1\"isInheritedAccount\"b1\"warmedEscrowCache\"b1\"warnedTooManyPeers\"b1}"

```
