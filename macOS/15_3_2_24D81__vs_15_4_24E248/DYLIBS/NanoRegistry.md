## NanoRegistry

> `/System/iOSSupport/System/Library/PrivateFrameworks/NanoRegistry.framework/Versions/A/NanoRegistry`

```diff

 792.5.0.0.0
-  __TEXT.__text: 0x4e53c
-  __TEXT.__auth_stubs: 0x8f0
-  __TEXT.__objc_methlist: 0x4558
-  __TEXT.__cstring: 0x2edb
+  __TEXT.__text: 0x4e580
+  __TEXT.__auth_stubs: 0x8e0
+  __TEXT.__objc_methlist: 0x4c34
+  __TEXT.__cstring: 0x2ec7
   __TEXT.__const: 0xa0
   __TEXT.__oslogstring: 0x14c9
   __TEXT.__ustring: 0xc
-  __TEXT.__gcc_except_tab: 0xb38
-  __TEXT.__unwind_info: 0x1840
+  __TEXT.__gcc_except_tab: 0xb34
+  __TEXT.__unwind_info: 0x1820
   __TEXT.__objc_classname: 0x8a9
   __TEXT.__objc_methname: 0x70ec
-  __TEXT.__objc_methtype: 0x13f4
+  __TEXT.__objc_methtype: 0x13f2
   __TEXT.__objc_stubs: 0x51c0
   __DATA_CONST.__got: 0x358
   __DATA_CONST.__const: 0x1768

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ce0
+  __DATA_CONST.__objc_selrefs: 0x1d60
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1b0
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x490
+  __AUTH_CONST.__auth_got: 0x488
   __AUTH_CONST.__const: 0x9c0
   __AUTH_CONST.__cfstring: 0x3480
-  __AUTH_CONST.__objc_const: 0x79b8
+  __AUTH_CONST.__objc_const: 0x6cf0
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1860

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C7318853-030D-3225-865B-0103E5B4D8F8
-  Functions: 2059
-  Symbols:   4309
-  CStrings:  2579
+  UUID: 20906D2F-FED4-3AE3-8EB1-9F60EEB06A53
+  Functions: 2056
+  Symbols:   4308
+  CStrings:  2569
 
Symbols:
+ __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- _fmod
Functions:
~ -[NRTermsEvent description] : 404 -> 416
~ -[NRTermsEvent setEventType:] : 100 -> 104
~ -[NRTermsEvent setTermsText:] : 128 -> 132
~ -[NRTermsEvent setDocumentationID:] : 128 -> 132
~ -[NRTermsEvent setPresentationReason:] : 128 -> 132
~ -[NRTermsEvent setPresentationLocation:] : 100 -> 104
~ -[NRTermsEvent setAcknowledgedDeviceName:] : 128 -> 132
~ -[NRTermsEvent setAcknowledgedDeviceSerialNumber:] : 128 -> 132
~ -[NRTermsEvent setDisplayDeviceName:] : 128 -> 132
~ -[NRTermsEvent setDisplayDeviceSerialNumber:] : 128 -> 132
~ -[NRTermsEvent setEventDate:] : 100 -> 104
~ -[NRTermsEvent setLoggingProcessName:] : 128 -> 132
~ -[NRMockXPCProxy forwardInvocation:] : 432 -> 436
~ -[NRMockClientNSXPCConnection _invalidate] : 228 -> 224
~ -[NRMockServerNSXPCConnection _invalidate] : 236 -> 232
~ -[NRReadWriteConcurrentQueue enqueueReadWithBlock:bypassSuspend:async:] : 496 -> 492
~ ___71-[NRReadWriteConcurrentQueue enqueueReadWithBlock:bypassSuspend:async:]_block_invoke : 208 -> 212
~ ___71-[NRReadWriteConcurrentQueue enqueueReadWithBlock:bypassSuspend:async:]_block_invoke_2 : 116 -> 120
~ -[NRReadWriteConcurrentQueue enqueueWriteWithBlockAsync:bypassSuspend:] : 332 -> 320
~ ___71-[NRReadWriteConcurrentQueue enqueueWriteWithBlockAsync:bypassSuspend:]_block_invoke : 240 -> 244
~ ___71-[NRReadWriteConcurrentQueue enqueueWriteWithBlockAsync:bypassSuspend:]_block_invoke_3 : 160 -> 148
~ ___36-[NRReadWriteConcurrentQueue resume]_block_invoke : 572 -> 576
~ __NRIsDemoModeEnabled : 68 -> 72
~ -[NRRegistryClient _getDevicesUpdateCounterNotifyTokenValue] : 172 -> 176
~ -[NRRegistryClient initWithParameters:] : 356 -> 352
~ ___39-[NRRegistryClient initWithParameters:]_block_invoke : 296 -> 292
~ -[NRRegistryClient _connectToDaemon] : 280 -> 276
~ -[NRRegistryClient _queryDataAsyncForce:ifNeededWithBlock:] : 916 -> 920
~ ___59-[NRRegistryClient _queryDataAsyncForce:ifNeededWithBlock:]_block_invoke : 1076 -> 1072
~ _NRPBPropertyValueReadFrom : 1608 -> 1684
- sub_26a8193d8
~ -[NRPBPropertyValue isEqual:] : 580 -> 600
~ _NRPBSwitchRecordReadFrom : 668 -> 676
~ -[NRPBSwitchRecord hash] : 236 -> 244
~ _NRRawVersionFromString : 276 -> 272
~ -[NRMutableStateBase parentDelegate] : 320 -> 316
~ -[NRMutableStateBase notifyObserversWithDiff:] : 688 -> 684
~ -[NRMutableStateBase addObserverQueue:withBlock:] : 396 -> 392
~ -[NRMutableStateBase removeObserver:] : 196 -> 192
~ ___37-[NRMutableStateBase removeObserver:]_block_invoke : 120 -> 108
~ -[NRMiniUUIDSet initWithUUIDSet:] : 968 -> 908
~ __ZNSt3__16vectorIjNS_9allocatorIjEEE7reserveEm : 168 -> 164
~ -[NRMiniUUIDSet initWithData:] : 428 -> 424
~ -[NRMiniUUIDSet copyWithZone:] : 412 -> 348
~ -[NRPBSize hash] : 264 -> 268
~ _NRPBNumberReadFrom : 1412 -> 1448
- sub_26a81ee9c
~ -[NRPBNumber isEqual:] : 420 -> 432
~ -[NRPBNumber hash] : 468 -> 472
~ -[NRPairedDeviceRegistry logCallFrequency] : 208 -> 216
~ ___84-[NRPairedDeviceRegistry setActivePairedDevice:isMagicSwitch:operationHasCompleted:]_block_invoke : 136 -> 140
~ ___81-[NRPairedDeviceRegistry setActivePairedDevice:withActiveDeviceAssertionHandler:]_block_invoke : 136 -> 140
~ -[NRPairedDeviceRegistry supportsWatch] : 80 -> 84
~ -[NRPairedDeviceRegistry initWithBoost:disconnected:] : 600 -> 596
~ ___116-[NRPairedDeviceRegistry companionOOBDiscoverAndPairWithName:withOutOfBandPairingKey:withOptions:operationHasBegun:]_block_invoke : 136 -> 140
~ ___88-[NRPairedDeviceRegistry companionPasscodePairWithDevice:withOptions:operationHasBegun:]_block_invoke : 136 -> 140
~ ___77-[NRPairedDeviceRegistry gizmoOOBAdvertiseAndPairWithName:operationHasBegun:]_block_invoke : 136 -> 140
~ ___82-[NRPairedDeviceRegistry gizmoPasscodeAdvertiseAndPairWithName:operationHasBegun:]_block_invoke : 136 -> 140
~ ___73-[NRPairedDeviceRegistry unpairWithDevice:withOptions:operationHasBegun:]_block_invoke : 136 -> 140
~ ___69-[NRPairedDeviceRegistry pairWithSimulator:withQueue:withCompletion:]_block_invoke : 136 -> 140
~ ___71-[NRPairedDeviceRegistry unpairWithSimulator:withQueue:withCompletion:]_block_invoke : 136 -> 140
~ ___69-[NRPairedDeviceRegistry switchToSimulator:withQueue:withCompletion:]_block_invoke : 136 -> 140
~ ___65-[NRPairedDeviceRegistry fakePairedSyncIsCompleteWithCompletion:]_block_invoke : 136 -> 140
~ ___74-[NRPairedDeviceRegistry completeRTCPairingMetricForMetricID:withSuccess:]_block_invoke : 136 -> 140
~ ___86-[NRPairedDeviceRegistry pairingClientSetAltAccountName:altDSID:forDevice:completion:]_block_invoke : 136 -> 140
~ ___102-[NRPairedDeviceRegistry pairingClientSetPairingParentName:pairingParentAltDSID:forDevice:completion:]_block_invoke : 136 -> 140
~ ___70-[NRPairedDeviceRegistry setMigrationConsented:forDeviceID:withBlock:]_block_invoke : 136 -> 140
~ ___70-[NRPairedDeviceRegistry setMigrationConsented:forDeviceID:withBlock:]_block_invoke_3 : 136 -> 140
~ ___70-[NRPairedDeviceRegistry beginMigrationWithDevice:passcode:withBlock:]_block_invoke : 136 -> 140
~ ___70-[NRPairedDeviceRegistry beginMigrationWithDevice:passcode:withBlock:]_block_invoke_3 : 136 -> 140
~ ___66-[NRPairedDeviceRegistry beginMigrationWithDevice:withCompletion:]_block_invoke : 136 -> 140
~ ___69-[NRPairedDeviceRegistry isPhoneReadyToMigrateDevice:withCompletion:]_block_invoke : 136 -> 140
~ -[NRMigrator devicesFromMigrationConsentRequestData:] : 1600 -> 1604
~ -[NRMigrator migrationConsentRequestData] : 2240 -> 2228
~ __NRIsAutomated : 68 -> 72
~ -[NRDeviceCollectionHistoryEntry initWithCoder:] : 324 -> 328
~ -[NRDeviceCollectionHistoryEntry state] : 672 -> 660
~ -[NRDeviceCollectionHistory initWithCoder:] : 688 -> 692
~ -[NRDeviceCollectionHistory _truncateHistory] : 1216 -> 1208
~ -[NRDeviceCollectionHistory addObserverQueue:withBlock:] : 160 -> 156
~ -[NRDeviceCollectionHistory removeObserver:] : 96 -> 84
~ -[NRDeviceCollectionHistory child:didApplyDiff:] : 308 -> 316
~ -[NRDeviceCollectionHistory notifyHistoryObserversWithEntry:] : 488 -> 484
~ -[NRDeviceCollectionHistory invalidate] : 112 -> 108
~ ___51-[NRRegistryProxy xpcGetDeviceCollectionWithBlock:]_block_invoke_2 : 48 -> 52
~ -[NRRegistryProxy xpcGetDiffSinceTokenValue:getSecureProperties:withBlock:] : 220 -> 216
~ -[NRPBDeviceCollectionHistoryEntry hash] : 232 -> 240
~ -[NRRegistry setQueueCollection:] : 260 -> 256
~ +[NRRegistry registerNotifyTokenWithName:withQueue:withBlock:] : 324 -> 320
~ -[NRXPCProxy hasEntitlement:] : 92 -> 88
~ -[NRXPCProxy _invalidate] : 128 -> 120
~ +[NRDataFileHistoryHelpers archiveDeviceHistory:] : 800 -> 792
~ +[NRDataFileHistoryHelpers createMissingDates:] : 1992 -> 1976
~ +[NSData(NRUtils) dataWithRandomBytesOfSize:] : 168 -> 164
~ -[NRMutableDevice initWithCoder:] : 456 -> 460
~ _NRPBMigrationDeviceInfoReadFrom : 456 -> 472
~ -[NRActiveDeviceAssertion initWithDevice:identifier:] : 252 -> 248
~ _NRPBCompressedDataReadFrom : 580 -> 588
~ -[NRPBCompressedData isEqual:] : 192 -> 188
~ ___46-[NRActiveDeviceAssertionMonitor addObserver:]_block_invoke : 448 -> 444
~ -[NRDeviceDiffType initWithCoder:] : 284 -> 288
~ -[NRDeviceCollectionDiff initWithCoder:] : 440 -> 444
~ -[NRDevice _fireChangeNotificationsForDiff:secureProperties:notify:] : 1732 -> 1736
~ -[NRDevice addPropertyObserver:forPropertyChanges:] : 240 -> 236
~ -[NRDevice removePropertyObserver:forPropertyChanges:] : 240 -> 236
~ ___54-[NRDevice removePropertyObserver:forPropertyChanges:]_block_invoke : 1036 -> 1064
~ -[NRDevice valueForProperty:] : 472 -> 468
~ -[NRDevice propertyNames] : 412 -> 408
~ -[NRDevice registerForPropertyChanges:withBlock:] : 240 -> 236
~ -[NRDevice unregisterForPropertyChanges:withBlock:] : 240 -> 236
~ -[NRDevice setValue:forProperty:] : 244 -> 240
~ -[NRMutableDeviceProperty initWithCoder:] : 312 -> 316
~ -[NRPBDeviceDiffType changeTypeAsString:] : 96 -> 108
~ -[NRMutableDeviceCollection applyDiff:upOnly:notifyParent:unconditional:] : 884 -> 888
~ -[NRMutableDeviceCollection initWithCoder:] : 440 -> 444
~ -[NRMutableDeviceCollection(Diffs) allAltAccount] : 324 -> 316
~ -[NRDevicePropertyDiff initWithCoder:] : 284 -> 288
~ +[NRDevicePropertyDiff packPropertyValue:] : 2728 -> 2708
~ +[NSKeyedArchiver(NRSecure) nr_secureArchiveRootObject:toFile:withOptions:] : 984 -> 976
~ +[NRConnectivitySubscriber getDropoutCounter:] : 100 -> 96
~ _NRPBTermsEventReadFrom : 1020 -> 1096
- sub_26a84d504
~ -[NRPBTermsEvent hash] : 496 -> 512
~ ___23-[NRBypassQueue resume]_block_invoke : 32 -> 36
~ -[NRDevicePropertyDiffType initWithCoder:] : 284 -> 288
~ -[NRDeviceDiff initWithCoder:] : 440 -> 444
~ -[NRPBDevicePropertyDiffType changeTypeAsString:] : 96 -> 108
CStrings:
+ "{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__end_cap_\"{__compressed_pair<unsigned int *, std::allocator<unsigned int>>=\"__value_\"^I}}"
- "C"
- "c"
- "s"
- "{vector<unsigned int, std::allocator<unsigned int> >=\"__begin_\"^I\"__end_\"^I\"__end_cap_\"{__compressed_pair<unsigned int *, std::allocator<unsigned int> >=\"__value_\"^I}}"

```
