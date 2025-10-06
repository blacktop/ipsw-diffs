## securityd

> `/usr/libexec/securityd`

```diff

-61040.62.1.0.0
-  __TEXT.__text: 0x22a708
+61040.80.10.0.1
+  __TEXT.__text: 0x22c1b0
   __TEXT.__auth_stubs: 0x38c0
-  __TEXT.__objc_stubs: 0x1a880
-  __TEXT.__objc_methlist: 0x12b6c
-  __TEXT.__const: 0x62d
-  __TEXT.__cstring: 0x1f9f7
-  __TEXT.__oslogstring: 0x28208
-  __TEXT.__gcc_except_tab: 0x6c00
-  __TEXT.__objc_classname: 0x2281
-  __TEXT.__objc_methname: 0x29786
-  __TEXT.__objc_methtype: 0x94f6
+  __TEXT.__objc_stubs: 0x1aaa0
+  __TEXT.__objc_methlist: 0x12cfc
+  __TEXT.__const: 0x635
+  __TEXT.__cstring: 0x1faec
+  __TEXT.__oslogstring: 0x28432
+  __TEXT.__gcc_except_tab: 0x6c9c
+  __TEXT.__objc_classname: 0x2282
+  __TEXT.__objc_methname: 0x29c62
+  __TEXT.__objc_methtype: 0x95d6
   __TEXT.__dlopen_cstrs: 0x26a
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x62d4
+  __TEXT.__unwind_info: 0x6318
   __DATA_CONST.__auth_got: 0x1c70
-  __DATA_CONST.__got: 0x8f0
+  __DATA_CONST.__got: 0x8f8
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x135c8
-  __DATA_CONST.__cfstring: 0x1ab20
+  __DATA_CONST.__const: 0x135e0
+  __DATA_CONST.__cfstring: 0x1acc0
   __DATA_CONST.__objc_classlist: 0x890
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x208

   __DATA_CONST.__objc_arraydata: 0x468
   __DATA_CONST.__objc_arrayobj: 0x3d8
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x23710
-  __DATA.__objc_selrefs: 0x8870
+  __DATA.__objc_const: 0x238e0
+  __DATA.__objc_selrefs: 0x8948
   __DATA.__objc_protorefs: 0x60
   __DATA.__objc_classrefs: 0xcf8
   __DATA.__objc_superrefs: 0x7e8
-  __DATA.__objc_ivar: 0x1888
+  __DATA.__objc_ivar: 0x18a8
   __DATA.__objc_data: 0x55a0
   __DATA.__data: 0x1fe8
   __DATA.__thread_vars: 0xc0

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 73F32207-8A8D-3CA5-9AA3-C3927D4A02C3
-  Functions: 9146
-  Symbols:   1367
-  CStrings:  18593
+  UUID: 5A55498A-C62A-3E4F-A07A-E46EBA59FADF
+  Functions: 9182
+  Symbols:   1368
+  CStrings:  18677
 
Symbols:
+ _kSecAttrViewHintManatee
CStrings:
+ "\x03\x12\x11\x11\x1f\x0f\f"
+ "\x1c\x15"
+ "!\"\x12\x12"
+ "%llu"
+ "-[CuttlefishXPCWrapper joinWithSpecificUser:voucherData:voucherSig:ckksKeys:tlkShares:preapprovedKeys:flowID:deviceSessionID:canSendMetrics:reply:]_block_invoke"
+ "-[CuttlefishXPCWrapper vouchWithSpecificUser:peerID:permanentInfo:permanentInfoSig:stableInfo:stableInfoSig:ckksKeys:flowID:deviceSessionID:canSendMetrics:reply:]_block_invoke"
+ "@\"NSString\"52@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32B40^@44"
+ "@148@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136B144"
+ "@164@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120#128#136@144@152B160"
+ "@52@0:8@16#24@32@40B48"
+ "@52@0:8@16@24@32B40^@44"
+ "@56@0:8@16@24@32B40@44B52"
+ "@72@0:8@16@24@32@40@48B56B60@64"
+ "@80@0:8@16#24@32@40@48B56@60@68B76"
+ "Added check-on-metrics flag to the state machine"
+ "B20@0:8i16"
+ "B40@0:8@16@24^q32"
+ "B52@0:8@16@24@32B40^^{__CFError}44"
+ "Checking metrics"
+ "Error persisting sendingMetricsPermitted value: %@"
+ "Metrics now switching to OFF"
+ "Metrics now switching to ON"
+ "NOTPERMITTED"
+ "Not Permitted"
+ "PERMITTED"
+ "Permitted"
+ "Rejecting a fetchSendingMetricsPermitted for arguments (%@): %@"
+ "StringAsSendingMetricsPermitted:"
+ "Successfully persisted state to disable metrics"
+ "T@\"CKKSNearFutureScheduler\",&,N,V_checkMetricsTrigger"
+ "TB,N,V_permittedToSendMetrics"
+ "TB,V_canSendMetrics"
+ "TB,V_sendMetric"
+ "Ti,N,V_sendingMetricsPermitted"
+ "Ti,N,V_shouldSendMetricsForOctagon"
+ "_canSendMetrics"
+ "_checkMetricsTrigger"
+ "_permittedToSendMetrics"
+ "_sendMetric"
+ "_sendingMetricsPermitted"
+ "_shouldSendMetricsForOctagon"
+ "avgCKRecords"
+ "avgErrorItemsProcessed"
+ "avgRemoteKeys"
+ "avgSuccessfulItemsProcessed"
+ "canSendMetrics"
+ "canSendMetricsUsingAccountState:"
+ "check-on-metrics"
+ "checkMetricsTrigger"
+ "check_on_rtc_metrics"
+ "circleJoiningBlob:flowID:deviceSessionID:canSendMetrics:applicant:complete:"
+ "current metrics setting set to: %@"
+ "ensure-metrics-off"
+ "fetchSendingMetricsPermitted:"
+ "fetchSendingMetricsPermitted:error:"
+ "hasSendingMetricsPermitted"
+ "initForContainer:contextID:activeAccount:stateHolder:flagHandler:sosAdapter:octagonAdapter:accountsAdapter:authKitAdapter:personaAdapter:deviceInfoAdapter:ckksAccountSync:lockStateTracker:cuttlefishXPCWrapper:escrowRequestClass:notifierClass:flowID:deviceSessionID:permittedToSendMetrics:"
+ "initWithCKKSMetrics:altDSID:eventName:testsAreEnabled:category:sendMetric:"
+ "initWithContainer:fetchClass:clientMap:fetchReasons:apnsPushes:forceResync:ckoperationGroup:altDSID:sendMetric:"
+ "initWithContainer:fetchClass:reachabilityTracker:altDSID:sendMetric:"
+ "initWithKeychainCircleMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:canSendMetrics:category:"
+ "initWithViewStates:contextID:activeAccount:zoneModifier:ckdatabase:cloudKitClassDependencies:ckoperationGroup:flagHandler:overallLaunch:accountStateTracker:lockStateTracker:reachabilityTracker:peerProviders:databaseProvider:savedTLKNotifier:personaAdapter:sendMetric:"
+ "initialSyncCredentials:altDSID:flowID:deviceSessionID:canSendMetrics:complete:"
+ "isAppleTV"
+ "isWatch"
+ "joinCircleWithBlob:altDSID:flowID:deviceSessionID:canSendMetrics:version:complete:"
+ "joinWithSpecificUser:voucherData:voucherSig:ckksKeys:tlkShares:preapprovedKeys:flowID:deviceSessionID:canSendMetrics:reply:"
+ "loadAndProcessEntries:withActionFilter:totalQueueEntries:"
+ "machineID:flowID:deviceSessionID:canSendMetrics:error:"
+ "myPeerInfo:flowID:deviceSessionID:canSendMetrics:complete:"
+ "octagon-metrics, failed to fetch metrics setting: %@"
+ "octagon-metrics: failed to fetch account metadata: %@"
+ "octagon-metrics: failed to persist metrics setting: %@"
+ "permittedToSendMetrics"
+ "persistSendingMetricsPermitted:error:"
+ "persistSendingMetricsPermitted:sendingMetricsPermitted:error:"
+ "persisted metrics setting set to not permitted"
+ "sendMetric"
+ "sendingMetricsPermitted"
+ "sendingMetricsPermittedAsString:"
+ "setCanSendMetrics:"
+ "setCheckMetricsTrigger:"
+ "setHasSendingMetricsPermitted:"
+ "setMetricsStateToActive"
+ "setMetricsStateToInactive"
+ "setMetricsToState:"
+ "setPermittedToSendMetrics:"
+ "setSendMetric:"
+ "setSendingMetricsPermitted:"
+ "setShouldSendMetricsForOctagon:"
+ "shouldSendMetricsForOctagon"
+ "stashAccountCredential:altDSID:flowID:deviceSessionID:canSendMetrics:complete:"
+ "syncWaitAndFlush:flowID:deviceSessionID:canSendMetrics:error:"
+ "totalCKRecords"
+ "totalRemoteKeys"
+ "triggered metrics check"
+ "v100@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSData\"32@\"NSData\"40@\"NSData\"48@\"NSData\"56@\"NSArray\"64@\"NSString\"72@\"NSString\"80B88@?<v@?@\"NSData\"@\"NSData\"@\"NSError\">92"
+ "v100@0:8@16@24@32@40@48@56@64@72@80B88@?92"
+ "v52@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32B40@?<v@?@\"NSData\"@\"NSError\">44"
+ "v56@0:8I16@\"NSString\"20@\"NSString\"28@\"NSString\"36B44@?<v@?@\"NSArray\"@\"NSError\">48"
+ "v56@0:8I16@20@28@36B44@?48"
+ "v60@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40B48@?<v@?B@\"NSError\">52"
+ "v60@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32B40@\"NSData\"44@?<v@?@\"NSData\"@\"NSError\">52"
+ "v60@0:8@16@24@32@40B48@?52"
+ "v60@0:8@16@24@32B40@44@?52"
+ "v64@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40B48i52@?<v@?B@\"NSError\">56"
+ "v64@0:8@16@24@32@40B48i52@?56"
+ "v92@0:8@\"TPSpecificUser\"16@\"NSData\"24@\"NSData\"32@\"NSArray\"40@\"NSArray\"48@\"NSArray\"56@\"NSString\"64@\"NSString\"72B80@?<v@?@\"NSString\"@\"NSArray\"@\"TPSyncingPolicy\"@\"NSError\">84"
+ "v92@0:8@16@24@32@40@48@56@64@72B80@?84"
+ "validatedStashedAccountCredential:flowID:deviceSessionID:canSendMetrics:complete:"
+ "versionNumber"
+ "vouchWithSpecificUser:peerID:permanentInfo:permanentInfoSig:stableInfo:stableInfoSig:ckksKeys:flowID:deviceSessionID:canSendMetrics:reply:"
+ "{?=\"epoch\"b1\"lastHealthCheckup\"b1\"attemptedJoin\"b1\"cdpState\"b1\"icloudAccountState\"b1\"sendingMetricsPermitted\"b1\"trustState\"b1\"isInheritedAccount\"b1\"warmedEscrowCache\"b1\"warnedTooManyPeers\"b1}"
+ "\xd1"
- "\x03\x12\x11\x11\x1f\x0f\v"
- "\f\x15"
- "!$\x12"
- "-[CuttlefishXPCWrapper joinWithSpecificUser:voucherData:voucherSig:ckksKeys:tlkShares:preapprovedKeys:flowID:deviceSessionID:reply:]_block_invoke"
- "-[CuttlefishXPCWrapper vouchWithSpecificUser:peerID:permanentInfo:permanentInfoSig:stableInfo:stableInfoSig:ckksKeys:flowID:deviceSessionID:reply:]_block_invoke"
- "@\"NSString\"48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32^@40"
- "@144@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136"
- "@160@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120#128#136@144@152"
- "@48@0:8@16#24@32@40"
- "@52@0:8@16@24@32B40@44"
- "@76@0:8@16#24@32@40@48B56@60@68"
- "B48@0:8@16@24@32^^{__CFError}40"
- "circleJoiningBlob:flowID:deviceSessionID:applicant:complete:"
- "initForContainer:contextID:activeAccount:stateHolder:flagHandler:sosAdapter:octagonAdapter:accountsAdapter:authKitAdapter:personaAdapter:deviceInfoAdapter:ckksAccountSync:lockStateTracker:cuttlefishXPCWrapper:escrowRequestClass:notifierClass:flowID:deviceSessionID:"
- "initWithCKKSMetrics:altDSID:eventName:testsAreEnabled:category:"
- "initWithContainer:fetchClass:clientMap:fetchReasons:apnsPushes:forceResync:ckoperationGroup:altDSID:"
- "initWithContainer:fetchClass:reachabilityTracker:altDSID:"
- "initWithKeychainCircleMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:category:"
- "initWithViewStates:contextID:activeAccount:zoneModifier:ckdatabase:cloudKitClassDependencies:ckoperationGroup:flagHandler:overallLaunch:accountStateTracker:lockStateTracker:reachabilityTracker:peerProviders:databaseProvider:savedTLKNotifier:personaAdapter:"
- "initialSyncCredentials:altDSID:flowID:deviceSessionID:complete:"
- "joinCircleWithBlob:altDSID:flowID:deviceSessionID:version:complete:"
- "joinWithSpecificUser:voucherData:voucherSig:ckksKeys:tlkShares:preapprovedKeys:flowID:deviceSessionID:reply:"
- "loadAndProcessEntries:withActionFilter:"
- "machineID:flowID:deviceSessionID:error:"
- "myPeerInfo:flowID:deviceSessionID:complete:"
- "numCKRecords"
- "numRemoteKeys"
- "stashAccountCredential:altDSID:flowID:deviceSessionID:complete:"
- "syncWaitAndFlush:flowID:deviceSessionID:error:"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSData\"@\"NSError\">40"
- "v52@0:8I16@\"NSString\"20@\"NSString\"28@\"NSString\"36@?<v@?@\"NSArray\"@\"NSError\">44"
- "v52@0:8I16@20@28@36@?44"
- "v56@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@?<v@?B@\"NSError\">48"
- "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40@?<v@?@\"NSData\"@\"NSError\">48"
- "v60@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40i48@?<v@?B@\"NSError\">52"
- "v60@0:8@16@24@32@40i48@?52"
- "v88@0:8@\"TPSpecificUser\"16@\"NSData\"24@\"NSData\"32@\"NSArray\"40@\"NSArray\"48@\"NSArray\"56@\"NSString\"64@\"NSString\"72@?<v@?@\"NSString\"@\"NSArray\"@\"TPSyncingPolicy\"@\"NSError\">80"
- "v88@0:8@16@24@32@40@48@56@64@72@?80"
- "v96@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSData\"32@\"NSData\"40@\"NSData\"48@\"NSData\"56@\"NSArray\"64@\"NSString\"72@\"NSString\"80@?<v@?@\"NSData\"@\"NSData\"@\"NSError\">88"
- "v96@0:8@16@24@32@40@48@56@64@72@80@?88"
- "validatedStashedAccountCredential:flowID:deviceSessionID:complete:"
- "vouchWithSpecificUser:peerID:permanentInfo:permanentInfoSig:stableInfo:stableInfoSig:ckksKeys:flowID:deviceSessionID:reply:"
- "{?=\"epoch\"b1\"lastHealthCheckup\"b1\"attemptedJoin\"b1\"cdpState\"b1\"icloudAccountState\"b1\"trustState\"b1\"isInheritedAccount\"b1\"warmedEscrowCache\"b1\"warnedTooManyPeers\"b1}"
- "\xc1"

```
