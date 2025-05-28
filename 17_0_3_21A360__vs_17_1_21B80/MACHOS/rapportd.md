## rapportd

> `/usr/libexec/rapportd`

```diff

-500.60.4.0.0
-  __TEXT.__text: 0x9a04c
-  __TEXT.__auth_stubs: 0x14a0
+510.71.1.0.0
+  __TEXT.__text: 0x9a218
+  __TEXT.__auth_stubs: 0x14e0
   __TEXT.__objc_stubs: 0xd560
-  __TEXT.__objc_methlist: 0x508c
-  __TEXT.__cstring: 0x229ea
-  __TEXT.__objc_classname: 0x847
-  __TEXT.__objc_methname: 0x117bb
-  __TEXT.__objc_methtype: 0x31c8
-  __TEXT.__const: 0x1b26
-  __TEXT.__gcc_except_tab: 0x159c
+  __TEXT.__objc_methlist: 0x50dc
+  __TEXT.__cstring: 0x229d3
+  __TEXT.__objc_classname: 0x848
+  __TEXT.__objc_methname: 0x1185d
+  __TEXT.__objc_methtype: 0x32db
+  __TEXT.__const: 0x1b0e
+  __TEXT.__gcc_except_tab: 0x1548
   __TEXT.__oslogstring: 0x1a8
-  __TEXT.__unwind_info: 0x193c
-  __DATA_CONST.__auth_got: 0xa60
+  __TEXT.__unwind_info: 0x1954
+  __DATA_CONST.__auth_got: 0xa80
   __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0x3380
-  __DATA_CONST.__cfstring: 0x4820
+  __DATA_CONST.__const: 0x3368
+  __DATA_CONST.__cfstring: 0x4840
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x2e8
+  __DATA_CONST.__objc_intobj: 0x318
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0xb758
+  __DATA.__objc_const: 0xb888
   __DATA.__objc_selrefs: 0x3b90
   __DATA.__objc_protorefs: 0x70
-  __DATA.__objc_classrefs: 0x408
+  __DATA.__objc_classrefs: 0x400
   __DATA.__objc_superrefs: 0x148
-  __DATA.__objc_ivar: 0xaf0
+  __DATA.__objc_ivar: 0xb10
   __DATA.__objc_data: 0x10e0
-  __DATA.__data: 0x1b28
-  __DATA.__bss: 0x350
+  __DATA.__data: 0x1b30
+  __DATA.__bss: 0x360
   __DATA.__common: 0x8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2381
-  Symbols:   455
-  CStrings:  7097
+  Functions: 2393
+  Symbols:   458
+  CStrings:  7111
 
Symbols:
+ _CUMetricsLog
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_attr_make_with_qos_class
+ _objc_release_x10
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- _OBJC_CLASS_$_IDSAccountController
- _dispatch_get_global_queue
- _nw_parameters_get_local_only
CStrings:
+ "\x011C\x14\x11"
+ "\x11\x14\x12X$\x13$\x13#\x12\x12\x12\x14\x11\x11\x14\x15\x15\x12=\x14\x111\x11\x11\x18"
+ "\x12\x12'!\x12!\x11\xf0!82"
+ "### Received invalidation from unexpected controller:%@"
+ "### isWiFiSingleBandModeRequired = Invalid, Fail to fetch WiFiP2PAWDLState"
+ "* roleBroadcastInBackground overwrote"
+ "-[RPCompanionLinkDaemon _clientBLENeedsCLinkAdvertiserRestart]"
+ "-[RPCompanionLinkDaemon _clientBLENeedsCLinkAdvertiserUpdate]"
+ "-[RPCompanionLinkDaemon _updateForXPCClientChange]"
+ "-[RPNFCTransactionController _releasePowerAssertion]"
+ "-[RPNFCTransactionController _requestPowerAssertion]"
+ "-[RPNWPeer resolvePeer:controlFlags:applicationService:clientPublicKey:resolveHandler:]"
+ "-[RPNWPeer resolvePeer:controlFlags:applicationService:clientPublicKey:resolveHandler:]_block_invoke"
+ "-[RPNWPeer sendWithRequestID:data:status:applicationService:clientPublicKey:listenerID:automapListener:connectionID:responseHandler:]"
+ "-[RPNWPeer sendWithRequestID:data:status:applicationService:clientPublicKey:listenerID:automapListener:connectionID:responseHandler:]_block_invoke"
+ "-[RPPeopleDaemon reportIRKMetrics]"
+ "/System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit"
+ "510.71.1"
+ "Acquired power assertion %d"
+ "AirDropFeatureFlags"
+ "AirDropPrivateContactDiscovery"
+ "BLE NeedsCLink advertiser started. ScreenOff: %s, targeting %@ \n"
+ "BLE NeedsCLink advertiser updating target data <%.3@> -> <%.3@>\n"
+ "BOOL __RPNearFieldRoleBroadcastInBackground(NFConnectionHandoverReceiver *__strong)"
+ "BOOL __isWiFiSingleBandModeRequired(void)"
+ "Could not find device to target authTag advertisement to, not starting NeedsCLink advertiser"
+ "DisableSelfIdentityRolling: %s -> %s\n"
+ "Friend sync: submitting IRK metrics to Core Analytics %@"
+ "Friend sync: updated accounts: Total %d, Removed %d, Refresh %d, One-Time Refresh %d, Missing SendersKnownAlias %d, Retry %d, Later %d, Request %d, Failed %d, OverMax %d\n"
+ "Ignoring BLE device lost for BLE device ID %@ cached device %@\n"
+ "Ignoring unsupported BLE device for Laguna: %@\n"
+ "MSDKDemoState"
+ "Needs AWDL Transaction: %s -> %s\n"
+ "Press demo mode enabled, not rolling self identity"
+ "RPMetricsSubmission"
+ "RX RESP from '%@': requestID=%@ appSvc=%@ response=%s serverPublicKey=%zu bytes bonjourServiceID=%@ listener=%@ error=%@\n"
+ "Receive handler response code=%@, serverPublicKey=%zu bytes, bonjourServiceID=%@"
+ "Released power assertion %d"
+ "Removing stale connection %@, replacing with new connection %@ for device identifier %@\n"
+ "Restarting BLE NeedsCLink advertiser with a new device %@\n"
+ "TI,N,V_powerAssertionID"
+ "_bleNeedsCLinkDevice"
+ "_clientBLEDiscoveryShouldRun"
+ "_clientBLENeedsCLinkAdvertiserRestart"
+ "_clientBLENeedsCLinkAdvertiserUpdate"
+ "_clientBLENeedsCLinkTargetDevice"
+ "_irkMetrics"
+ "_irkMetricsReportLock"
+ "_irkMetricsSetup"
+ "_metricsReportQueue"
+ "_metricsReportTimer"
+ "_metricsSubmissionSetup"
+ "_powerAssertionID"
+ "_prefDisableSelfIdentityRolling"
+ "_releasePowerAssertion"
+ "_requestPowerAssertion"
+ "_sendIRKMetricsReport"
+ "com.apple.rapport.RPNFCTransactionController.potentialInitiator"
+ "com.apple.rapport.metrics.irkexchange"
+ "controllerDidDetectPotentialInitiator:"
+ "did receive field notification:%@\n"
+ "duetNotQueried"
+ "field info: auto-negotiation initiator detected"
+ "field info: auto-negotiation receiver detected"
+ "field info: initiator detected an other initiator in the field"
+ "field info: initiator polling detected"
+ "field info: request to start initiator"
+ "i96@?0@\"NSData\"8@\"NSNumber\"16@\"RPCompanionLinkDevice\"24i32@\"NSString\"36@\"NSData\"44^@52^@60@\"NSUUID\"68B76@\"NSUUID\"80^@88"
+ "isDeviceEnrolledWithDeKOTA:"
+ "isEqualToDeviceBasic:"
+ "isWiFiSingleBandModeRequired = %s"
+ "numDuetSuggestions"
+ "numFriendAccounts"
+ "numFriendDevices"
+ "powerAssertionID"
+ "reportIRKMetrics"
+ "request to start initiator\n"
+ "requestsAcked"
+ "requestsIgnored"
+ "requestsIgnoredNoIDSDevice"
+ "requestsIgnoredSelfIdentReq"
+ "requestsIgnoredUnknownPeer"
+ "requestsSent"
+ "resolvePeer:controlFlags:applicationService:clientPublicKey:resolveHandler:"
+ "resumePassiveNearbyDeviceDiscovery"
+ "selfIdentRolled"
+ "selfIdentRolledBlocked"
+ "sendWithRequestID:data:status:applicationService:clientPublicKey:listenerID:automapListener:connectionID:responseHandler:"
+ "setPowerAssertionID:"
+ "unknown CH field type. Ignoring it"
+ "v28@?0i8@\"NSData\"12@\"NSUUID\"20"
+ "v36@?0i8@\"NSData\"12@\"NSUUID\"20@\"NSUUID\"28"
+ "v56@0:8@16Q24@32@40@?48"
+ "v80@0:8@16@24i32@36@44@52B60@64@?72"
+ "{?=\"selfIdentRolled\"I\"selfIdentRolledBlocked\"I\"duetNotQueried\"I\"numDuetSuggestions\"I\"requestsSent\"I\"numFriendAccounts\"I\"numFriendDevices\"I\"requestsIgnored\"I\"requestsIgnoredNoIDSDevice\"I\"requestsIgnoredSelfIdentReq\"I\"requestsIgnoredUnknownPeer\"I\"requestsAcked\"I}"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "\x011C\x12\x11"
- "\x11\x14\x12W$\x13$\x13#\x12\x12\x12\x14\x11\x11\x14\x15\x15\x12=\x14\x111\x11\x11\x18"
- "\x12\x12'!\x12!\x11\xb182"
- " clientPseudonym=%@"
- " clientPushToken=%@"
- "%02lx"
- "-[RPCompanionLinkDaemon _clientBLENeedsCLinkTargetAuthTag]"
- "-[RPNFCTransactionController controller:didInvalidated:]"
- "-[RPNWNetworkAgent _localPseudonym]"
- "-[RPNWNetworkAgent _localPushTokenEncodedAsHex]"
- "-[RPNWNetworkAgent _updateCurrentPseudonym]"
- "-[RPNWNetworkAgent _updateCurrentPseudonym]_block_invoke"
- "-[RPNWNetworkAgent _updateTXTRecordForEndpoint:pushToken:pseudonym:idsSessionID:]"
- "-[RPNWPeer resolvePeer:controlFlags:applicationService:clientPublicKey:clientPushToken:clientPseudonym:resolveHandler:]"
- "-[RPNWPeer resolvePeer:controlFlags:applicationService:clientPublicKey:clientPushToken:clientPseudonym:resolveHandler:]_block_invoke"
- "-[RPNWPeer sendWithRequestID:data:status:applicationService:clientPublicKey:clientPushToken:clientPseudonym:listenerID:automapListener:connectionID:responseHandler:]"
- "-[RPNWPeer sendWithRequestID:data:status:applicationService:clientPublicKey:clientPushToken:clientPseudonym:listenerID:automapListener:connectionID:responseHandler:]_block_invoke"
- "500.60.4"
- "B48@0:8@16@24@32@40"
- "BLE NeedsCLink advertiser started. ScreenOff: %s \n"
- "Changing target AuthTag for NeedsCLink advertiser to <%@>\n"
- "Current pseudonym is nil"
- "Deprecated: did invalidate controller:%@ error:%@\n"
- "Failed to find active IDS account"
- "Failed to find push token for active IDS account=%@"
- "Failed to provision pseudonym with error=%@"
- "Friend sync: updated accounts: Total %d, Removed %d, Refresh %d, One-Time Refresh %d, Nil Date Requested %d, Retry %d, Later %d, Request %d, Failed %d, OverMax %d\n"
- "Ignoring BLE device ( ipad ) with old OS: %d.%d.%d, %@\n"
- "Ignoring BLE device lost: stale ID, %@ vs %@\n"
- "Ignoring unsupported Laguna BLE device found: %@\n"
- "NearbyInfo"
- "NearbyInfoV2"
- "Provisioned new pseudonym=%@, service=%@, properties=%@"
- "RESOLVE: IDS session requested by agent_client=%@\n"
- "RESOLVE: Skipped IDS session request for agent_client=%@\n"
- "RESOLVE: Skipping IDS session request for agent_client=%@\n"
- "RESOLVE: Skipping IDS session request for appSvc='%@' from sender %@"
- "RX RESP from '%@': requestID=%@ appSvc=%@ response=%s serverPublicKey=%zu bytes serverPushToken=%@ serverPseudonym=%@ bonjourServiceID=%@ idsSessionID=%@ listener=%@ error=%@\n"
- "Receive handler response code=%@, serverPublicKey=%zu bytes, serverPushToken=%@, serverPseudonym=%@\n, bonjourServiceID=%@, idsSessionID=%@"
- "Removing stale connection: %@, %@\n"
- "Skip using target AuthTag since multiple clients requested for it\n"
- "Skipping updating TXT Record for endpoint=%@, pushToken=%@, pseudonym=%@, idsSessionID=%@"
- "URI"
- "Updating pseudonym for service=%@, properties=%@"
- "Using target AuthTag <%@> for NeedsCLink from %@ device\n"
- "WalkAway"
- "_clientBLENeedsCLinkTargetAuthTag"
- "_localPseudonym"
- "_localPushTokenEncodedAsHex"
- "_updateCurrentPseudonym"
- "_updateTXTRecordForEndpoint:pushToken:pseudonym:idsSessionID:"
- "at"
- "clientPseudonym"
- "clientPushToken"
- "com.apple.private.alloy.airdrop.walkaway"
- "did receive field:%@\n"
- "i136@?0@\"NSData\"8@\"NSNumber\"16@\"RPCompanionLinkDevice\"24i32@\"NSString\"36@\"NSData\"44@\"NSString\"52@\"NSString\"60^@68^@76^@84^@92^@100@\"NSUUID\"108B116@\"NSUUID\"120^@128"
- "idsSessionID"
- "idstool"
- "initiator detected an other initiator in the field:%@\n"
- "isCHAutoNegotiationField"
- "isCHInitiatorDetected"
- "isCHReceiverDetected"
- "prefixedURI"
- "provisionPseudonymWithProperties:completion:"
- "ps:0"
- "pseudonymPropertiesWithFeatureID:expiryDurationInSeconds:"
- "pt:0"
- "pushToken"
- "resolvePeer:controlFlags:applicationService:clientPublicKey:clientPushToken:clientPseudonym:resolveHandler:"
- "sendWithRequestID:data:status:applicationService:clientPublicKey:clientPushToken:clientPseudonym:listenerID:automapListener:connectionID:responseHandler:"
- "serverPseudonym"
- "serverPushToken"
- "si:0"
- "skipping received field because of unsupported type for field:%@\n"
- "start initiator\n"
- "v24@?0@\"IDSPseudonym\"8@\"NSError\"16"
- "v24@?0@8^B16"
- "v52@?0i8@\"NSData\"12@\"NSString\"20@\"NSString\"28@\"NSUUID\"36@\"NSUUID\"44"
- "v60@?0i8@\"NSData\"12@\"NSString\"20@\"NSString\"28@\"NSUUID\"36@\"NSUUID\"44@\"NSUUID\"52"
- "v72@0:8@16Q24@32@40@48@56@?64"
- "v96@0:8@16@24i32@36@44@52@60@68B76@80@?88"

```
