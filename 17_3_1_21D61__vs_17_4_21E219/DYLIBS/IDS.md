## IDS

> `/System/Library/PrivateFrameworks/IDS.framework/IDS`

```diff

-1814.400.21.2.1
-  __TEXT.__text: 0x11484c
+1814.500.141.0.0
+  __TEXT.__text: 0x117134
   __TEXT.__auth_stubs: 0x1aa0
-  __TEXT.__objc_methlist: 0x8ab0
+  __TEXT.__objc_methlist: 0x8e38
   __TEXT.__const: 0x2b8
-  __TEXT.__gcc_except_tab: 0x3240
-  __TEXT.__oslogstring: 0x1611a
-  __TEXT.__cstring: 0xefc3
+  __TEXT.__gcc_except_tab: 0x3254
+  __TEXT.__oslogstring: 0x16585
+  __TEXT.__cstring: 0xeff3
   __TEXT.__dlopen_cstrs: 0x102
   __TEXT.__ustring: 0xac
-  __TEXT.__unwind_info: 0x4100
-  __TEXT.__objc_classname: 0x132b
-  __TEXT.__objc_methname: 0x1a94a
-  __TEXT.__objc_methtype: 0x6487
-  __TEXT.__objc_stubs: 0x11020
-  __DATA_CONST.__got: 0x9a0
-  __DATA_CONST.__const: 0x4390
-  __DATA_CONST.__objc_classlist: 0x430
+  __TEXT.__unwind_info: 0x41e4
+  __TEXT.__objc_classname: 0x13ec
+  __TEXT.__objc_methname: 0x1adcc
+  __TEXT.__objc_methtype: 0x65a9
+  __TEXT.__objc_stubs: 0x11320
+  __DATA_CONST.__got: 0x9c0
+  __DATA_CONST.__const: 0x4408
+  __DATA_CONST.__objc_classlist: 0x460
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x188
+  __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2ed20
-  __DATA_CONST.__objc_selrefs: 0x5638
-  __AUTH_CONST.__objc_const: 0x31c0
-  __AUTH_CONST.__cfstring: 0x6240
+  __DATA_CONST.__objc_const: 0x2f850
+  __DATA_CONST.__objc_selrefs: 0x5720
+  __DATA_CONST.__objc_protorefs: 0xb0
+  __DATA_CONST.__objc_classrefs: 0x760
+  __DATA_CONST.__objc_superrefs: 0x380
+  __AUTH_CONST.__objc_const: 0x3490
+  __AUTH_CONST.__cfstring: 0x62a0
   __AUTH_CONST.__const: 0x1220
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__auth_got: 0xd60
-  __AUTH.__objc_data: 0x1630
-  __DATA.__objc_protorefs: 0xa8
-  __DATA.__objc_classrefs: 0x738
-  __DATA.__objc_superrefs: 0x358
-  __DATA.__objc_ivar: 0xa7c
-  __DATA.__data: 0x1350
-  __DATA.__bss: 0x199c
+  __AUTH.__objc_data: 0x1810
+  __DATA.__objc_ivar: 0xab8
+  __DATA.__data: 0x13b0
+  __DATA.__bss: 0x1994
   __DATA_DIRTY.__objc_data: 0x13b0
-  __DATA_DIRTY.__bss: 0x1f8
+  __DATA_DIRTY.__bss: 0x200
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: B4525511-7042-349D-897F-BBC7B483ECB0
-  Functions: 5483
-  Symbols:   1365
-  CStrings:  8606
+  UUID: 6F79A07D-9104-3056-B470-D56D0EABA60A
+  Functions: 5577
+  Symbols:   1382
+  CStrings:  8690
 
Symbols:
+ OBJC_IVAR_$_IDSDaemonListener._serviceToRestrictionReason
+ _IDSDataChannelLastPacketReceivedTimeKey
+ _IDSDataChannelLastPacketSentTimeKey
+ _IDSOpenSocketOptionClientNameKey
+ _OBJC_CLASS_$_IDSFeatureToggleRetrievalOptions
+ _OBJC_CLASS_$_IDSFeatureToggleRetrievalResult
+ _OBJC_CLASS_$_IDSFeatureToggleUpdateOptions
+ _OBJC_CLASS_$_IDSFeatureToggleUpdateResult
+ _OBJC_CLASS_$_IDSFeatureToggler
+ _OBJC_CLASS_$_IDSXPCFeatureTogglerInterface
+ _OBJC_METACLASS_$_IDSFeatureToggleRetrievalOptions
+ _OBJC_METACLASS_$_IDSFeatureToggleRetrievalResult
+ _OBJC_METACLASS_$_IDSFeatureToggleUpdateOptions
+ _OBJC_METACLASS_$_IDSFeatureToggleUpdateResult
+ _OBJC_METACLASS_$_IDSFeatureToggler
+ _OBJC_METACLASS_$_IDSXPCFeatureTogglerInterface
+ _kIDSListenerCapConsumesLaunchOnDemandRestrictionUpdates
CStrings:
+ "\r"
+ "\x0f\x04"
+ "-[_IDSService registrationRestrictionReason]"
+ "<%p> Init connection socket %d with options: %@ (streamName:%@, connectionUUID:%@ active connections:%d), device: %@"
+ "@24@0:8^{?=*QqqICBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@iIS[0C]}16"
+ "@32@0:8@16Q24"
+ "Bad parameters. No valid IDSDevice found."
+ "Calling out to IDSService delegate %p for registrationRestrictionReason if it responds."
+ "Client attempted to initialize feature toggler with nil service identifier or nil queue"
+ "Client is leaking sockets (%d active connection, service %@)."
+ "Client retrieving feature toggle with no completion block"
+ "Client retrieving feature toggle with no feature ID"
+ "Client setting feature toggle to invalid state %lu"
+ "Client setting feature toggle with no feature ID"
+ "Client updating feature toggle with no completion block"
+ "Done for IDSService delegate %p for registrationRestrictionReason - doesRespondToSelector? %@"
+ "Error fetching feature toggler collaborator {error: %@}"
+ "FeatureToggler"
+ "IDSFeatureToggleRetrievalOptions"
+ "IDSFeatureToggleRetrievalResult"
+ "IDSFeatureToggleUpdateOptions"
+ "IDSFeatureToggleUpdateResult"
+ "IDSFeatureToggler"
+ "IDSXPCFeatureToggler"
+ "IDSXPCFeatureTogglerInterface"
+ "QueryWithBoost"
+ "Restriction reason %@ for service %@"
+ "Service %@ received restriction reason %lu"
+ "T@\"NSString\",&,N,V_featureID"
+ "T@\"NSString\",?,R,C"
+ "TQ,N,V_error"
+ "TQ,N,V_state"
+ "Td,V_lastPacketReceivedTime"
+ "Td,V_lastPacketReportedTime"
+ "Td,V_lastPacketSentTime"
+ "Too many active connections. Client is leaking sockets."
+ "Warning. Setting active connection %@ without closing existing %@ for key %@"
+ "^{?=*QqqICBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@iIS[0C]}20@0:8B16"
+ "^{?=*QqqICBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@iIS[0C]}54@0:8r^v16I24C28C32{?=cSCSC}36^{?=IQSCc[12S]CS{?=SSSSS}dQBQ[16C]BB}46"
+ "^{?=*QqqICBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@iIS[0C]}62@0:8r^v16I24C28C32{?=cSCSC}36^{?=IQSCc[12S]CS{?=SSSSS}dQBQ[16C]BB}46@54"
+ "_IDSDeviceConnection cannot be created: client is leaking sockets (%d active connection, service %@)."
+ "_clientName"
+ "_featureID"
+ "_lastPacketReceivedTime"
+ "_lastPacketReportedTime"
+ "_lastPacketSentTime"
+ "_linkIDToParticipantMapLock"
+ "_openConnections"
+ "_reportLinkMetricsForLinkContext:"
+ "_serviceToRestrictionReason"
+ "err"
+ "featureTogglerCollaboratorForService:withErrorHandler:"
+ "featureTogglerForService:withCompletion:"
+ "featuretoggler"
+ "fid"
+ "forwardMethodWithBoostedPriority:"
+ "getOpenConnectionCount"
+ "initWithFeatureID:"
+ "initWithFeatureID:state:"
+ "initWithState:error:"
+ "lastPacketReceivedTime"
+ "lastPacketReportedTime"
+ "lastPacketSentTime"
+ "optionsWithFeatureID:"
+ "optionsWithFeatureID:state:"
+ "registrationRestrictionReason"
+ "reportLastPacketReceivedTime:lastPacketSentTime:linkID:"
+ "restrictionReasonForService:"
+ "restrictionReasons"
+ "resultWithError:"
+ "resultWithState:"
+ "retrieveFeatureToggleStateForOptions:completion:"
+ "service:registrationRestrictionReasonChanged:"
+ "service:restrictionReasonChanged:"
+ "setFeatureID:"
+ "setLastPacketReceivedTime:"
+ "setLastPacketReportedTime:"
+ "setLastPacketSentTime:"
+ "setShouldBoost:"
+ "st"
+ "successfulResult"
+ "updateFeatureToggleStateWithOptions:completion:"
+ "v16@?0@\"IDSFeatureToggleRetrievalResult\"8"
+ "v16@?0@\"IDSFeatureToggleUpdateResult\"8"
+ "v24@0:8^{?=*QqqICBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@iIS[0C]}16"
+ "v32@0:8@\"IDSFeatureToggleRetrievalOptions\"16@?<v@?@\"IDSFeatureToggleRetrievalResult\">24"
+ "v32@0:8@\"IDSFeatureToggleUpdateOptions\"16@?<v@?@\"IDSFeatureToggleUpdateResult\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"<IDSXPCFeatureToggler>\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16Q24"
+ "v36@0:8d16d24C32"
- "\f"
- "\x0f\x03"
- "%s:%d %{private}@"
- "<%p> Init connection socket %d with options: %@  device: %@  (%@)  (name %@) service %@ connectionUUID %@ timeout %@"
- "@24@0:8^{?=*QqqIBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@iIS[0C]}16"
- "^{?=*QqqIBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@iIS[0C]}20@0:8B16"
- "^{?=*QqqIBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@iIS[0C]}54@0:8r^v16I24C28C32{?=cSCSC}36^{?=IQSCc[12S]CS{?=SSSSS}dQBQ[16C]BB}46"
- "^{?=*QqqIBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@iIS[0C]}62@0:8r^v16I24C28C32{?=cSCSC}36^{?=IQSCc[12S]CS{?=SSSSS}dQBQ[16C]BB}46@54"
- "v24@0:8^{?=*QqqIBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@iIS[0C]}16"

```
