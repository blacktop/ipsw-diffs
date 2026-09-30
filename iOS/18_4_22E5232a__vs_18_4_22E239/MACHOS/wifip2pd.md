## wifip2pd

> `/usr/libexec/wifip2pd`

```diff

 780.43.0.0.0
-  __TEXT.__text: 0x3b1c34
-  __TEXT.__auth_stubs: 0x3880
+  __TEXT.__text: 0x3cc478
+  __TEXT.__auth_stubs: 0x38f0
   __TEXT.__objc_methlist: 0x13ec
-  __TEXT.__const: 0x31530
-  __TEXT.__cstring: 0xac6a
-  __TEXT.__swift5_typeref: 0x9362
+  __TEXT.__const: 0x31ca0
+  __TEXT.__cstring: 0xb30a
+  __TEXT.__swift5_typeref: 0x968c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__oslogstring: 0xc7a3
-  __TEXT.__objc_methname: 0x2d3e
-  __TEXT.__constg_swiftt: 0xb2c0
-  __TEXT.__swift5_reflstr: 0xea36
-  __TEXT.__swift5_fieldmd: 0x10a54
-  __TEXT.__swift5_builtin: 0x11f8
-  __TEXT.__swift5_assocty: 0x2610
-  __TEXT.__swift5_protos: 0xcc
-  __TEXT.__swift5_proto: 0x27a8
-  __TEXT.__swift5_types: 0xe2c
+  __TEXT.__oslogstring: 0xd393
+  __TEXT.__objc_methname: 0x2d61
+  __TEXT.__constg_swiftt: 0xbdbc
+  __TEXT.__swift5_reflstr: 0xf326
+  __TEXT.__swift5_fieldmd: 0x1105c
+  __TEXT.__swift5_builtin: 0x1234
+  __TEXT.__swift5_assocty: 0x2640
+  __TEXT.__swift5_protos: 0xdc
+  __TEXT.__swift5_proto: 0x27d4
+  __TEXT.__swift5_types: 0xe58
   __TEXT.__objc_classname: 0x2a6
   __TEXT.__objc_methtype: 0xd1d
-  __TEXT.__swift5_capture: 0x4c18
+  __TEXT.__swift5_capture: 0x5a7c
   __TEXT.__swift5_mpenum: 0x164
-  __TEXT.__unwind_info: 0xc290
-  __TEXT.__eh_frame: 0x14dc8
-  __DATA_CONST.__auth_got: 0x1c40
-  __DATA_CONST.__got: 0xc40
-  __DATA_CONST.__auth_ptr: 0x1c30
-  __DATA_CONST.__const: 0x2a898
+  __TEXT.__unwind_info: 0xc5a0
+  __TEXT.__eh_frame: 0x151b8
+  __DATA_CONST.__auth_got: 0x1c78
+  __DATA_CONST.__got: 0xc48
+  __DATA_CONST.__auth_ptr: 0x1cc0
+  __DATA_CONST.__const: 0x2ceb8
   __DATA_CONST.__cfstring: 0x20
-  __DATA_CONST.__objc_classlist: 0xe0
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xd8
-  __DATA.__objc_const: 0x5fb0
-  __DATA.__objc_selrefs: 0xc58
-  __DATA.__objc_data: 0xdb8
-  __DATA.__data: 0xd848
-  __DATA.__common: 0x628
-  __DATA.__bss: 0x4d610
+  __DATA.__objc_const: 0x6ad0
+  __DATA.__objc_selrefs: 0xc68
+  __DATA.__objc_data: 0xe58
+  __DATA.__data: 0xe130
+  __DATA.__common: 0x6b0
+  __DATA.__bss: 0x4d990
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 18651
-  Symbols:   1755
-  CStrings:  2763
+  Functions: 19110
+  Symbols:   1762
+  CStrings:  2886
 
Symbols:
+ _$s8Dispatch0A4TimeV17uptimeNanosecondss6UInt64Vvg
+ _$sSLsE1goiySbx_xtFZ
+ _$sSLsE2geoiySbx_xtFZ
+ _$sSLsE2leoiySbx_xtFZ
+ _$ss22_ContiguousArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtFyXl_Ts5
+ _log10
+ _swift_unknownObjectUnownedDestroy
CStrings:
+ "$__lazy_storage_$_linkStatsAccumulator"
+ "Cannot add more multicast receiver because no more instance IDs were available"
+ "Cannot add multicast receiver since receiver is already added"
+ "Checking link stats on timer prev rate is %hhu current rate %hhu"
+ "Current DW %ld rxPackets 0 txPackets %u snr 0 with per 100 & mcs %hhu"
+ "Current peers with stats available is %ld"
+ "Current per %f and snr %hhu"
+ "Current rate update: MCS=%hhu, per is %f"
+ "Deferring transmission of out of band action frame to: %s"
+ "Did not find a service to notify multicast receiver error"
+ "Did not find a service to notify multicast sender error"
+ "Did not find a service to notify receiving data blob"
+ "Error %@ while starting GCR session)"
+ "Error %@ while terminating multicast MAC address)"
+ "Error %@ while updating multicast MAC address"
+ "Error %@ while updating multicast MAC address)"
+ "Error %@ while updating multicast rate information)"
+ "Error while starting GCR session)"
+ "Fail to restore multicast session"
+ "Failed to transmit data blob to %s because %@"
+ "Failed to transmit multicast link condition request to %s because %@"
+ "Failed to transmit multicast link condition response to %s because %@"
+ "Finish sending link condition request for %s of peers"
+ "Incoming Tx stats DW %ld does not match current DW %ld"
+ "Invalid channel information provided %@"
+ "Invalid: channel %@ belongs to 2.4G Band"
+ "Invalid: channel %@ belongs to 2.4G Band or is a DFS channel"
+ "Link stats timer fired"
+ "Marking peer %s as unrecoverable"
+ "Multicast peer %s added with instance ID %hu"
+ "Multicast peer %s removed with instance ID %hu"
+ "Multicast session not started, nothing to restore"
+ "Multicast session not started, nothing to terminate"
+ "Multicast stats: TSF[%s], %s, activePeers[%ld], totalUptime s[%llu]"
+ "Multicast stats: TSF[%s], %s, totalUptime s[%llu]"
+ "No blob data from %s"
+ "No multicast peer found with %s"
+ "No response from peer %s marking it as inactive"
+ "No valid peer with %s"
+ "Peer %s not present in database"
+ "Peer %s reporting PER= %f for mcs= %hhu"
+ "Rate adapter max tolerable PER= %f"
+ "Received Link condition feedback from %s"
+ "Received Link condition request from %s"
+ "Received link condition feedback from inactive peer. Discarding......."
+ "Received stats mcs: %hhu, current mcs %hhu"
+ "Received stats snr: %hhu txPkts %u rxPkts %u txMPDU %u rxMPDU %u cca %hhu"
+ "Sending MCS: %hhu, txPkts: %u, rxPkts: %u, snr: %hhu"
+ "Sending heart beat ......."
+ "Sent link condition feedback to %s"
+ "Starting multicast rate adaptor"
+ "WiFiP2P-780.43 Mar 17 2025 19:03:48"
+ "_TtC12wifip2pdCore13MulticastPeer"
+ "_TtC12wifip2pdCore17NANMulticastPeers"
+ "cca"
+ "chan info is nil"
+ "channeListsUpdated"
+ "channel %u, band %s, BW %s"
+ "channelInfo"
+ "create GCR session with %s"
+ "currentHeartBeatTransmissionTime"
+ "currentTransmissionParams"
+ "currentpingPongDeferralCount"
+ "discardForRateAdapter"
+ "dwIndex"
+ "enableHeartBeatMonitoring"
+ "handleForNoResponseReceiver"
+ "heartBeatTransmissionInterval"
+ "heartBeatTransmissionTimer"
+ "heartbeatRequestCounter"
+ "highPERInformProbability"
+ "highPERReportForLowTxRateCount"
+ "instances"
+ "invalid multicast address"
+ "invalid peer MAC address"
+ "invalid peer MAC address %s"
+ "isPaused"
+ "isPeerActive"
+ "isPeerUpdated"
+ "lastModified"
+ "linkConditionCheckTimeInSeconds"
+ "linkConditionTimer"
+ "linkConditonFeedbackTimer"
+ "macAddress"
+ "maxNumPeerForLinkStats"
+ "maxRetryForNoResponsePeer"
+ "maximumTolerablePER"
+ "multicastConfiguration"
+ "multicastMACAddress"
+ "multicastManager"
+ "multicastReceiverManager"
+ "multicastSenderManager"
+ "multicastServiceInstanceIDPool"
+ "multicastServiceType"
+ "multicastSessionStarted"
+ "multicastSessionStats"
+ "multicastStartTime"
+ "peerID"
+ "peerInformation"
+ "per"
+ "pingPongMaxDefferal"
+ "publishInstanceID"
+ "rate update with per %f, snr %hhu"
+ "rateAdapter"
+ "rateAdapterEnabled"
+ "receiveStats"
+ "received an unexpected %s"
+ "receiverHeartBeatIntervalInSeconds"
+ "receiverHeartBeatTimer"
+ "receiverResponseTimeoutInSeconds"
+ "responderMACAddress"
+ "restoring GCR session with %s"
+ "senderTxStatsTimeoutInSeconds"
+ "senderTxStatsTimer"
+ "signalPowerBase"
+ "snr"
+ "subscribeInstanceID"
+ "transmitStats"
+ "transmitterMACAddress"
+ "tsf"
+ "unrecoverablePeerStatsCount"
+ "watchDogComplete"
+ "watchdogStatus"
- "WiFiP2P-780.43 Mar 12 2025 21:03:12"

```
