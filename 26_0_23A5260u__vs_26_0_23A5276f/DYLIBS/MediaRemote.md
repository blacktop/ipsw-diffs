## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

-4025.110.87.2.0
-  __TEXT.__text: 0x2e5128
+4025.110.97.1.0
+  __TEXT.__text: 0x2e59c0
   __TEXT.__auth_stubs: 0x16d0
-  __TEXT.__objc_methlist: 0x2a380
-  __TEXT.__const: 0x590
-  __TEXT.__cstring: 0x2b12b
+  __TEXT.__objc_methlist: 0x2a398
+  __TEXT.__const: 0x598
+  __TEXT.__cstring: 0x2b182
   __TEXT.__oslogstring: 0xd831
   __TEXT.__gcc_except_tab: 0x6208
   __TEXT.__dlopen_cstrs: 0x514
   __TEXT.__ustring: 0x7a2
-  __TEXT.__unwind_info: 0xaae8
+  __TEXT.__unwind_info: 0xaaf0
   __TEXT.__objc_classname: 0x4c34
-  __TEXT.__objc_methname: 0x4b4ec
+  __TEXT.__objc_methname: 0x4b598
   __TEXT.__objc_methtype: 0x8e62
-  __TEXT.__objc_stubs: 0x27320
+  __TEXT.__objc_stubs: 0x27360
   __DATA_CONST.__got: 0x1420
-  __DATA_CONST.__const: 0xac20
+  __DATA_CONST.__const: 0xac48
   __DATA_CONST.__objc_classlist: 0x1160
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe9f8
+  __DATA_CONST.__objc_selrefs: 0xea18
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0xf98
   __DATA_CONST.__objc_arraydata: 0x260
   __AUTH_CONST.__auth_got: 0xb78
-  __AUTH_CONST.__const: 0x3020
-  __AUTH_CONST.__cfstring: 0x227a0
-  __AUTH_CONST.__objc_const: 0x44808
+  __AUTH_CONST.__const: 0x3040
+  __AUTH_CONST.__cfstring: 0x227c0
+  __AUTH_CONST.__objc_const: 0x44838
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_intobj: 0x4e0
   __AUTH_CONST.__objc_dictobj: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1DA234DB-EE8F-319D-96F4-D642689799AD
-  Functions: 19786
-  Symbols:   54318
-  CStrings:  23887
+  UUID: 048F7BA3-D020-332A-81A4-67A4064A18FE
+  Functions: 19791
+  Symbols:   54332
+  CStrings:  23896
 
Symbols:
+ -[MRAVEndpoint isVisualProxyGroupPlayer]
+ -[MRAVEndpoint supportsVisualProxyGroupPlayer]
+ -[MRPlaybackSessionMigrateRequest innerErrorForEvent:]
+ -[MRSyncOutputDevicesMessage initWithOutputDevices:forClientWithDeviceInfo:]
+ -[MRUserSettings supportTwoStageMove]
+ -[NSError(MRAdditions) mr_errorByEnvelopingWithMRError:format:]
+ GCC_except_table100
+ GCC_except_table219
+ GCC_except_table248
+ GCC_except_table249
+ GCC_except_table333
+ ___105+[MRAVEndpoint prepareGroupForPlaybackWithOutputDeviceUIDs:forBundleID:timeout:details:queue:completion:]_block_invoke.626
+ ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.658
+ ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.663
+ ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.670
+ ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke_2.659
+ ___106+[MRAVEndpoint sendCommand:withOptions:toEachEndpointContainingOutputDeviceUIDs:timeout:queue:completion:]_block_invoke.597
+ ___122+[MRAVEndpoint sendCommand:withOptions:toNewEndpointContainingOutputDeviceUIDs:nowPlayingClient:timeout:queue:completion:]_block_invoke.608
+ ___122-[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:]_block_invoke.639
+ ___122-[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:]_block_invoke.646
+ ___34-[MRAVEndpoint isProxyGroupPlayer]_block_invoke
+ ___35-[MRAVEndpoint syncedOutputDevices]_block_invoke_2
+ ___35-[MRAVEndpoint syncedOutputDevices]_block_invoke_3
+ ___40-[MRAVOutputContext containsLocalDevice]_block_invoke
+ ___52-[MRAVEndpoint outputDeviceVolume:queue:completion:]_block_invoke.473
+ ___57-[MRAVEndpoint outputDeviceVolumeMuted:queue:completion:]_block_invoke.505
+ ___60-[MRAVEndpoint waitForPlaybackWithTimeout:queue:completion:]_block_invoke.514
+ ___63+[MRAVEndpoint pauseOutputDeviceUIDs:details:queue:completion:]_block_invoke.588
+ ___64-[MRAVEndpoint requestGroupSessionWithDetails:queue:completion:]_block_invoke.433
+ ___67+[MRAVEndpoint directEndpointForOutputDeviceUIDs:queue:completion:]_block_invoke.561
+ ___67+[MRAVEndpoint hostedEndpointForOutputDeviceUIDs:queue:completion:]_block_invoke.554
+ ___68-[MRAVEndpoint performMigrationToEndpoint:request:queue:completion:]_block_invoke.387
+ ___68-[MRAVEndpoint performMigrationToEndpoint:request:queue:completion:]_block_invoke.395
+ ___70+[MRAVEndpoint findMyGroupLeaderWithTimeout:details:queue:completion:]_block_invoke.612
+ ___71-[MRAVEndpoint outputDeviceVolumeControlCapabilities:queue:completion:]_block_invoke.446
+ ___72-[MRAVEndpoint requestMicrophoneConnectionWithDetails:queue:completion:]_block_invoke.439
+ ___76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:details:queue:completion:]_block_invoke.571
+ ___76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:details:queue:completion:]_block_invoke.572
+ ___76-[MRAVEndpoint setOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.466
+ ___77-[MRAVEndpoint muteOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.491
+ ___78-[MRAVConcreteOutputDevice _loadLocalOverridesWithOutputContext:outputDevice:]_block_invoke_3
+ ___79-[MRAVEndpoint adjustOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.481
+ ___80-[MRAVEndpoint migrateToOrAddOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.214
+ ___80-[MRAVEndpoint migrateToOrAddOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.224
+ ___80-[MRAVEndpoint migrateToOrSetOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.233
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.253
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.257
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.266
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.273
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.303
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.307
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.314
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.325
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.342
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.352
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.371
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.258
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.280
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.308
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.318
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.331
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.355
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.382
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_3.287
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_3.332
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_3.358
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_4.290
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_4.360
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_5.294
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_5.361
+ ___84+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:details:queue:groupUIDCompletion:]_block_invoke.582
+ ___86+[MRAVEndpoint connectToEndpointContainingOutputDeviceUID:options:details:completion:]_block_invoke.206
+ ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.163
+ ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.166
+ ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke_2.164
+ ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke_2.164.cold.1
+ ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke_2.167
+ ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.447
+ ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.448
+ ___block_descriptor_40_e8_32s_e22_B16?0"MRDeviceInfo"8ls32l8
+ ___block_literal_global.127
+ ___block_literal_global.154
+ ___block_literal_global.166
+ ___block_literal_global.226
+ ___block_literal_global.310
+ ___block_literal_global.317
+ ___block_literal_global.327
+ ___block_literal_global.345
+ ___block_literal_global.354
+ ___block_literal_global.357
+ ___block_literal_global.363
+ ___block_literal_global.373
+ ___block_literal_global.397
+ ___block_literal_global.445
+ ___block_literal_global.495
+ ___block_literal_global.521
+ ___block_literal_global.586
+ ___block_literal_global.601
+ ___block_literal_global.613
+ ___block_literal_global.648
+ _objc_msgSend$supportTwoStageMove
+ _objc_msgSend$supportsVisualProxyGroupPlayer
- -[MRAVDistantEndpoint isProxyGroupPlayer]
- -[MRAVOutputContextEndpoint isProxyGroupPlayer]
- -[MRConcreteEndpoint isProxyGroupPlayer]
- -[MRSyncOutputDevicesMessage initWithOutputDevices:]
- GCC_except_table214
- GCC_except_table243
- GCC_except_table244
- GCC_except_table328
- ___105+[MRAVEndpoint prepareGroupForPlaybackWithOutputDeviceUIDs:forBundleID:timeout:details:queue:completion:]_block_invoke.624
- ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.654
- ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.661
- ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.668
- ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke_2.657
- ___106+[MRAVEndpoint sendCommand:withOptions:toEachEndpointContainingOutputDeviceUIDs:timeout:queue:completion:]_block_invoke.595
- ___122+[MRAVEndpoint sendCommand:withOptions:toNewEndpointContainingOutputDeviceUIDs:nowPlayingClient:timeout:queue:completion:]_block_invoke.606
- ___122-[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:]_block_invoke.637
- ___122-[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:]_block_invoke.644
- ___40-[MRConcreteEndpoint isProxyGroupPlayer]_block_invoke
- ___52-[MRAVEndpoint outputDeviceVolume:queue:completion:]_block_invoke.471
- ___57-[MRAVEndpoint outputDeviceVolumeMuted:queue:completion:]_block_invoke.503
- ___60-[MRAVEndpoint waitForPlaybackWithTimeout:queue:completion:]_block_invoke.512
- ___63+[MRAVEndpoint pauseOutputDeviceUIDs:details:queue:completion:]_block_invoke.586
- ___64-[MRAVEndpoint requestGroupSessionWithDetails:queue:completion:]_block_invoke.431
- ___67+[MRAVEndpoint directEndpointForOutputDeviceUIDs:queue:completion:]_block_invoke.559
- ___67+[MRAVEndpoint hostedEndpointForOutputDeviceUIDs:queue:completion:]_block_invoke.552
- ___68-[MRAVEndpoint performMigrationToEndpoint:request:queue:completion:]_block_invoke.385
- ___68-[MRAVEndpoint performMigrationToEndpoint:request:queue:completion:]_block_invoke.393
- ___70+[MRAVEndpoint findMyGroupLeaderWithTimeout:details:queue:completion:]_block_invoke.610
- ___71-[MRAVEndpoint outputDeviceVolumeControlCapabilities:queue:completion:]_block_invoke.444
- ___72-[MRAVEndpoint requestMicrophoneConnectionWithDetails:queue:completion:]_block_invoke.437
- ___76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:details:queue:completion:]_block_invoke.569
- ___76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:details:queue:completion:]_block_invoke.570
- ___76-[MRAVEndpoint setOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.464
- ___77-[MRAVEndpoint muteOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.489
- ___78-[MRAVConcreteOutputDevice _loadLocalOverridesWithOutputContext:outputDevice:]_block_invoke
- ___79-[MRAVEndpoint adjustOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.479
- ___80-[MRAVEndpoint migrateToOrAddOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.211
- ___80-[MRAVEndpoint migrateToOrAddOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.221
- ___80-[MRAVEndpoint migrateToOrSetOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.230
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.250
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.254
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.263
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.270
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.300
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.304
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.311
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.322
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.340
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.350
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.369
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.255
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.277
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.305
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.315
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.329
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.353
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.380
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_3.284
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_3.330
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_3.356
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_4.287
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_4.358
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_5.291
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_5.359
- ___84+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:details:queue:groupUIDCompletion:]_block_invoke.580
- ___86+[MRAVEndpoint connectToEndpointContainingOutputDeviceUID:options:details:completion:]_block_invoke.203
- ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.162
- ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.165
- ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke_2.163
- ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke_2.163.cold.1
- ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke_2.166
- ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.444
- ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.445
- ___block_literal_global.124
- ___block_literal_global.152
- ___block_literal_global.163
- ___block_literal_global.165
- ___block_literal_global.223
- ___block_literal_global.314
- ___block_literal_global.325
- ___block_literal_global.343
- ___block_literal_global.352
- ___block_literal_global.355
- ___block_literal_global.361
- ___block_literal_global.371
- ___block_literal_global.395
- ___block_literal_global.442
- ___block_literal_global.491
- ___block_literal_global.519
- ___block_literal_global.580
- ___block_literal_global.599
- ___block_literal_global.645
CStrings:
+ "05AC:110C"
+ "B16@?0@\"MRDeviceInfo\"8"
+ "TB,R,D,N,GisProxyGroupPlayer"
+ "TB,R,D,N,GisVisualProxyGroupPlayer"
+ "The component may still be valid but it is not longer a UGL"
+ "initWithOutputDevices:forClientWithDeviceInfo:"
+ "isVisualProxyGroupPlayer"
+ "mr_errorByEnvelopingWithMRError:format:"
+ "playerCommand:%@"
+ "supportTwoStageMove"
+ "supportsVisualProxyGroupPlayer"
+ "visualProxyGroupPlayer"
- "05ac:110"
- "TB,R,N,GisProxyGroupPlayer"
- "_loadLocalOverridesWithOutputContext:outputDevice:"
- "playerCommand"

```
