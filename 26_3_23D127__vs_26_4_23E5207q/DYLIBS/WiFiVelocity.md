## WiFiVelocity

> `/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`

```diff

-1166.1.0.0.0
-  __TEXT.__text: 0x2d9cc
-  __TEXT.__auth_stubs: 0x740
+1180.12.0.0.0
+  __TEXT.__text: 0x2e084
+  __TEXT.__auth_stubs: 0x700
   __TEXT.__objc_methlist: 0x2b7c
-  __TEXT.__cstring: 0x7261
+  __TEXT.__cstring: 0x72ad
   __TEXT.__const: 0xc8
   __TEXT.__gcc_except_tab: 0x2ac
-  __TEXT.__oslogstring: 0x122e
+  __TEXT.__oslogstring: 0x1275
   __TEXT.__ustring: 0x656
-  __TEXT.__unwind_info: 0xad0
+  __TEXT.__unwind_info: 0xb28
   __TEXT.__objc_classname: 0x25e
   __TEXT.__objc_methname: 0x5da6
   __TEXT.__objc_methtype: 0xe09
-  __TEXT.__objc_stubs: 0x4bc0
+  __TEXT.__objc_stubs: 0x4be0
   __DATA_CONST.__got: 0x288
   __DATA_CONST.__const: 0x1768
   __DATA_CONST.__objc_classlist: 0xe8

   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0x3b0
+  __AUTH_CONST.__auth_got: 0x390
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0xa160
+  __AUTH_CONST.__cfstring: 0xa1c0
   __AUTH_CONST.__objc_const: 0x4668
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x78

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AE3E06A5-2E57-3ECE-A879-B287386B264E
-  Functions: 1172
-  Symbols:   3725
-  CStrings:  3996
+  UUID: 85F78F95-0888-3EB8-95BB-751C1ABC1FF9
+  Functions: 1173
+  Symbols:   3722
+  CStrings:  4004
 
Symbols:
+ ___45-[W5Client queryDatabaseForPeer:fetch:reply:]_block_invoke.26
+ ___65-[W5Client startMonitoringFaultEventsForPeer:eventHandler:error:]_block_invoke.186
+ ___block_literal_global.173
+ ___block_literal_global.38
+ ___block_literal_global.40
+ _objc_msgSend$version
+ _objc_retainAutoreleasedReturnValue
- ___45-[W5Client queryDatabaseForPeer:fetch:reply:]_block_invoke_5
- ___65-[W5Client startMonitoringFaultEventsForPeer:eventHandler:error:]_block_invoke.182
- ___block_literal_global.169
- ___block_literal_global.34
- ___block_literal_global.36
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x24
- _objc_retain_x3
Functions:
+ sub_29d7323a8
~ +[W5FeatureAvailability _featureAvailabilityDefaults] : 112 -> 128
~ ___96+[NSTask(WiFiVelocity) runTaskWithLaunchPath:arguments:timeout:startBlock:updateBlock:endBlock:]_block_invoke.63 : 444 -> 484
~ ___96+[NSTask(WiFiVelocity) runTaskWithLaunchPath:arguments:timeout:startBlock:updateBlock:endBlock:]_block_invoke_2.66 : 416 -> 456
~ -[W5PeerDiscoveryConfiguration description] : 176 -> 188
~ -[W5PeerDiscoveryConfiguration encodeWithCoder:] : 108 -> 116
~ -[W5BluetoothDevice hash] : 236 -> 228
~ ___W5ArchiveAddURLToArchive : 1496 -> 1476
~ ___W5ArchiveAddFileURLToArchive : 1280 -> 1272
~ -[W5SummaryFaults initWithSummaryFaults:] : 316 -> 320
~ -[W5SummaryFaults description] : 496 -> 516
~ -[W5SummaryFaults isEqualToFaults:] : 524 -> 528
~ -[W5SummaryFaults initWithCoder:] : 284 -> 292
~ -[W5SummaryFaults setLastHrFaults:] : 12 -> 64
~ -[W5PeerDiscoveryEvent initWithPeersFound:peersLost:info:] : 384 -> 376
~ -[W5PeerDiscoveryEvent copyWithZone:] : 160 -> 172
~ -[W5PeerDiscoveryEvent encodeWithCoder:] : 128 -> 136
~ -[W5PeerDiscoveryEvent initWithCoder:] : 496 -> 520
~ -[W5PeerDiscoveryEvent setPeersFound:] : 12 -> 64
~ -[W5PeerDiscoveryEvent setPeersLost:] : 12 -> 64
~ -[W5PeerDiscoveryEvent setInfo:] : 12 -> 64
~ +[W5ActivityManager sharedActivityManager] : 84 -> 100
~ -[W5ActivityManager init] : 236 -> 244
~ -[W5ActivityManager debugTimerEnabled] : 184 -> 196
~ ___31-[W5ActivityManager debugTimer]_block_invoke : 160 -> 164
~ ___53-[W5ActivityManager osTransactionCreate:transaction:]_block_invoke : 420 -> 424
~ ___43-[W5ActivityManager osTransactionComplete:]_block_invoke : 896 -> 908
~ ___43-[W5ActivityManager osTransactionComplete:]_block_invoke.17 : 164 -> 168
~ ___43-[W5ActivityManager osTransactionComplete:]_block_invoke_2 : 392 -> 396
~ -[W5ActivityManager _executeTimerBlock] : 124 -> 132
~ -[W5ActivityManager setQueue:] : 12 -> 64
~ -[W5DiagnosticsModePeer initWithRole:peer:info:] : 356 -> 348
~ -[W5DiagnosticsModePeer copyWithZone:] : 148 -> 156
~ -[W5DiagnosticsModePeer encodeWithCoder:] : 128 -> 136
~ -[W5DiagnosticsModePeer initWithCoder:] : 456 -> 472
~ -[W5DiagnosticsModePeer description] : 140 -> 148
~ -[W5DiagnosticsModePeer setPeer:] : 12 -> 64
~ -[W5DiagnosticsModePeer setInfo:] : 12 -> 64
~ -[W5DiagnosticsMode initWithConfiguration:uuid:] : 860 -> 888
~ -[W5DiagnosticsMode updatePeer:] : 416 -> 432
~ -[W5DiagnosticsMode setState:] : 148 -> 156
~ -[W5DiagnosticsMode copyWithZone:] : 212 -> 228
~ -[W5DiagnosticsMode encodeWithCoder:] : 168 -> 176
~ -[W5DiagnosticsMode initWithCoder:] : 668 -> 696
~ -[W5DiagnosticsMode description] : 1080 -> 1144
~ ___32-[W5DiagnosticsMode description]_block_invoke : 152 -> 160
~ -[W5DiagnosticsMode isEqualToDiagnosticsMode:] : 112 -> 120
~ -[W5DiagnosticsMode hash] : 56 -> 60
~ -[W5DiagnosticsMode compareCollectionTimeLatestFirst:] : 176 -> 192
~ -[W5DiagnosticsMode timestampFor:] : 160 -> 176
~ -[W5DiagnosticsMode setUuid:] : 12 -> 64
~ -[W5DiagnosticsMode setPeers:] : 12 -> 64
~ -[W5DiagnosticsMode setInfo:] : 12 -> 64
~ -[W5DiagnosticsMode setTimestamps:] : 12 -> 64
~ -[W5DebugConfiguration initDiagnosticsMode:wifiState:megaWiFiProfileState:noLoggingWiFiProfileState:eapolState:bluetoothState:] : 364 -> 368
~ -[W5DebugConfiguration initDiagnosticsMode:wifiState:megaWiFiProfileState:noLoggingWiFiProfileState:eapolState:bluetoothState:stbcState:] : 368 -> 372
~ -[W5DebugConfiguration description] : 396 -> 428
~ -[W5DebugConfiguration isEqualToDebugConfiguration:] : 180 -> 184
~ -[W5DebugConfiguration hash] : 280 -> 304
~ -[W5DebugConfiguration encodeWithCoder:] : 208 -> 216
~ -[W5DebugConfiguration initWithCoder:] : 408 -> 416
~ -[W5DebugConfiguration setDiagnosticsMode:] : 12 -> 64
~ -[W5WiFiScanResult supportsSecurity:] : 436 -> 428
~ _W5XPCRequestDelegateInterface : 7936 -> 7896
~ -[W5Peer initWithCompanionLinkDevice:] : 288 -> 496
~ _W5DescriptionForBluetoothDeviceType : 668 -> 628
~ ___41-[W5Client __stopMonitoringEvents:reply:]_block_invoke : 244 -> 240
~ ___45-[W5Client queryDatabaseForPeer:fetch:reply:]_block_invoke : 248 -> 456
~ ___54-[W5Client runDiagnostics:configuration:update:reply:]_block_invoke : 476 -> 480
~ ___51-[W5Client collectLogs:configuration:update:reply:]_block_invoke : 860 -> 856
~ ___51-[W5Client collectLogsDiagnosticMode:update:reply:]_block_invoke : 572 -> 568
~ ___57-[W5Client runWiFiSnifferOnChannels:duration:peer:reply:]_block_invoke : 336 -> 340
~ ___68-[W5Client runWiFiSnifferWithTCPDumpOnChannels:duration:peer:reply:]_block_invoke : 336 -> 340
~ -[W5SummaryRecoveries initWithSummaryRecoveries:] : 316 -> 320
~ -[W5SummaryRecoveries description] : 452 -> 468
~ -[W5SummaryRecoveries isEqualToRecoveries:] : 524 -> 528
~ -[W5SummaryRecoveries initWithCoder:] : 284 -> 292
~ -[W5SummaryRecoveries setLastHrRecoveries:] : 12 -> 64
~ -[W5SummaryLinkTests initWithSummaryLinkTests:] : 316 -> 320
~ -[W5SummaryLinkTests description] : 452 -> 468
~ -[W5SummaryLinkTests isEqualToLinkTests:] : 524 -> 528
~ -[W5SummaryLinkTests initWithCoder:] : 284 -> 292
~ -[W5SummaryLinkTests setLastHrLinkTests:] : 12 -> 64
CStrings:
+ "%u.%u%@"
+ "-[W5Client queryDatabaseForPeer:fetch:reply:]_block_invoke"
+ ".%u"
+ "26.4"
+ "[wifivelocity] %s - Peer version: %@ - Fetch type forced to Dictionary"

```
