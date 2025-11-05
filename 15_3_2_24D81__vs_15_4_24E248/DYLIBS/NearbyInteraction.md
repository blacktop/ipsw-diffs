## NearbyInteraction

> `/System/Library/Frameworks/NearbyInteraction.framework/Versions/A/NearbyInteraction`

```diff

-462.0.1.0.0
-  __TEXT.__text: 0x2d6e0
-  __TEXT.__auth_stubs: 0x660
-  __TEXT.__objc_methlist: 0x2f74
-  __TEXT.__gcc_except_tab: 0x48fc
-  __TEXT.__cstring: 0x4492
+465.0.18.0.0
+  __TEXT.__text: 0x2fea8
+  __TEXT.__auth_stubs: 0x670
+  __TEXT.__objc_methlist: 0x3710
+  __TEXT.__gcc_except_tab: 0x4d2c
+  __TEXT.__cstring: 0x4800
   __TEXT.__const: 0x470
-  __TEXT.__oslogstring: 0xbe4
+  __TEXT.__oslogstring: 0xe6e
   __TEXT.__swift5_typeref: 0x83
   __TEXT.__swift5_reflstr: 0x4b
   __TEXT.__swift5_assocty: 0x48

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x1ae8
-  __TEXT.__objc_classname: 0x4e9
-  __TEXT.__objc_methname: 0x780c
-  __TEXT.__objc_methtype: 0x1387
-  __TEXT.__objc_stubs: 0x4300
-  __DATA_CONST.__got: 0x260
-  __DATA_CONST.__const: 0x540
-  __DATA_CONST.__objc_classlist: 0x160
+  __TEXT.__unwind_info: 0x1c20
+  __TEXT.__objc_classname: 0x532
+  __TEXT.__objc_methname: 0x7dce
+  __TEXT.__objc_methtype: 0x1409
+  __TEXT.__objc_stubs: 0x45e0
+  __DATA_CONST.__got: 0x270
+  __DATA_CONST.__const: 0x578
+  __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1898
+  __DATA_CONST.__objc_selrefs: 0x1a30
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x148
-  __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x340
+  __DATA_CONST.__objc_superrefs: 0x158
+  __DATA_CONST.__objc_arraydata: 0x30
+  __AUTH_CONST.__auth_got: 0x348
   __AUTH_CONST.__const: 0xb38
-  __AUTH_CONST.__cfstring: 0x49c0
-  __AUTH_CONST.__objc_const: 0x6a88
-  __AUTH_CONST.__objc_intobj: 0x1f8
+  __AUTH_CONST.__cfstring: 0x4e60
+  __AUTH_CONST.__objc_const: 0x6650
+  __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0xdc0
-  __DATA.__objc_ivar: 0x3ec
-  __DATA.__data: 0x3c0
+  __AUTH.__objc_data: 0xe60
+  __DATA.__objc_ivar: 0x42c
+  __DATA.__data: 0x3d0
   __DATA.__bss: 0x5c0
   __DATA.__common: 0x12d
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 64527A1F-25AB-3A4C-83D8-46A51A3E2F90
-  Functions: 1258
-  Symbols:   3234
-  CStrings:  2878
+  UUID: 4B245217-F22E-3F56-9CF8-EAB70B1BC7C5
+  Functions: 1324
+  Symbols:   3384
+  CStrings:  3032
 
Symbols:
+ +[NIAcwgSFZoneUpdate supportsSecureCoding]
+ +[NIDiscoveryToken(ItemLocalizer_Project) generateTokenWithUUID:]
+ +[NIInternalUtils NINearbyObjectDiscoveryPriorityToString:]
+ +[NIInternalUtils NINearbyObjectDiscoveryPriorityToString:].cold.1
+ +[NIInternalUtils isIntValidNearbyObjectDiscoveryPriority:]
+ +[NIItemLocalizerConfiguration supportsSecureCoding]
+ +[NILocalization _niFrameworkBundle].cold.1
+ +[NIPlatformInfo isInternalBuild].cold.1
+ +[NISession(LocalDeviceInteraction) _localDeviceLogger].cold.1
+ -[NIAcwgM1Msg initWithSupportedUwbConfigIds:supportedPulseShapeCombos:channelBitmask:uwbSessionId:finalData2Bitmask:selectedProtocolVersion:]
+ -[NIAcwgM1Msg selectedProtocolVersion]
+ -[NIAcwgSFZoneUpdate btConnHandle]
+ -[NIAcwgSFZoneUpdate copyWithZone:]
+ -[NIAcwgSFZoneUpdate currentSFInBubble]
+ -[NIAcwgSFZoneUpdate currentZone]
+ -[NIAcwgSFZoneUpdate description]
+ -[NIAcwgSFZoneUpdate encodeWithCoder:]
+ -[NIAcwgSFZoneUpdate explicitPAITriggered]
+ -[NIAcwgSFZoneUpdate initWithCoder:]
+ -[NIAcwgSFZoneUpdate initWithSFZone:btConnHandle:lastBtRssiValue:ioStateDisplacing:explicitPAITriggered:currentSFInBubble:]
+ -[NIAcwgSFZoneUpdate ioStateDisplacing]
+ -[NIAcwgSFZoneUpdate lastBtRssiValue]
+ -[NIConfiguration _internalIsMemoryAssertionRequired]
+ -[NIConfiguration _internalIsPowerAssertionRequired]
+ -[NIExportedObjectForwarder initWithExportedObject:].cold.1
+ -[NIFindingConfiguration preferredDiscoveryPriority]
+ -[NIFindingConfiguration setPreferredDiscoveryPriority:]
+ -[NIItemLocalizerConfiguration .cxx_destruct]
+ -[NIItemLocalizerConfiguration _internalIsCameraAssistanceEnabled]
+ -[NIItemLocalizerConfiguration canUpdateToConfiguration:]
+ -[NIItemLocalizerConfiguration copyWithZone:]
+ -[NIItemLocalizerConfiguration debugParameters]
+ -[NIItemLocalizerConfiguration descriptionInternal]
+ -[NIItemLocalizerConfiguration description]
+ -[NIItemLocalizerConfiguration discoveryToken]
+ -[NIItemLocalizerConfiguration encodeWithCoder:]
+ -[NIItemLocalizerConfiguration hash]
+ -[NIItemLocalizerConfiguration initWithCoder:]
+ -[NIItemLocalizerConfiguration initWithItemUUID:preferredUpdateRate:]
+ -[NIItemLocalizerConfiguration isCameraAssistanceEnabled]
+ -[NIItemLocalizerConfiguration isEqual:]
+ -[NIItemLocalizerConfiguration itemUUID]
+ -[NIItemLocalizerConfiguration preferredUpdateRate]
+ -[NIItemLocalizerConfiguration setCameraAssistanceEnabled:]
+ -[NIItemLocalizerConfiguration setDebugParameters:]
+ -[NIItemLocalizerConfiguration setDiscoveryToken:]
+ -[NIItemLocalizerConfiguration setItemUUID:]
+ -[NIItemLocalizerConfiguration setPreferredUpdateRate:]
+ -[NINearbyAccessoryConfiguration _internalIsPowerAssertionRequired]
+ -[NINearbyObject horizontalDistance]
+ -[NINearbyObject itemState]
+ -[NINearbyObject setHorizontalDistance:]
+ -[NINearbyObject setItemState:]
+ -[NINearbyPeerConfiguration _internalIsPowerAssertionRequired]
+ -[NIServerConnection initWithSessionID:queue:exportedObject:options:].cold.1
+ -[NISession _internalRunWithConfiguration:]
+ -[NISession _sendRemoteDevice:changedState:]
+ -[NISession _shouldReConnectToDaemonAfterCrash]
+ -[NISession _shouldReRunSessionAfterSessionInterruptionEnded]
+ -[NISession _tryToRecoverFromFailure:]
+ -[NISession didReceiveAopSFZoneUpdate:]
+ -[NISession didUpdateState:forItem:]
+ -[NISession didUpdateState:forItem:].cold.1
+ -[NISystemConfiguration _internalIsMemoryAssertionRequired]
+ GCC_except_table105
+ GCC_except_table128
+ GCC_except_table133
+ GCC_except_table142
+ GCC_except_table148
+ GCC_except_table150
+ GCC_except_table151
+ GCC_except_table152
+ GCC_except_table153
+ GCC_except_table154
+ GCC_except_table156
+ GCC_except_table157
+ GCC_except_table158
+ GCC_except_table159
+ GCC_except_table188
+ GCC_except_table191
+ GCC_except_table207
+ GCC_except_table210
+ GCC_except_table213
+ GCC_except_table219
+ GCC_except_table221
+ GCC_except_table222
+ GCC_except_table224
+ GCC_except_table225
+ GCC_except_table228
+ GCC_except_table229
+ GCC_except_table239
+ GCC_except_table253
+ GCC_except_table255
+ GCC_except_table257
+ GCC_except_table260
+ GCC_except_table265
+ GCC_except_table271
+ GCC_except_table274
+ GCC_except_table277
+ GCC_except_table28
+ GCC_except_table280
+ GCC_except_table283
+ GCC_except_table288
+ GCC_except_table289
+ GCC_except_table29
+ GCC_except_table294
+ GCC_except_table298
+ GCC_except_table299
+ GCC_except_table303
+ GCC_except_table304
+ GCC_except_table306
+ GCC_except_table308
+ GCC_except_table309
+ GCC_except_table313
+ GCC_except_table318
+ GCC_except_table65
+ GCC_except_table68
+ GCC_except_table69
+ OBJC_IVAR_$_NIAcwgM1Msg._selectedProtocolVersion
+ OBJC_IVAR_$_NIAcwgSFZoneUpdate._btConnHandle
+ OBJC_IVAR_$_NIAcwgSFZoneUpdate._currentSFInBubble
+ OBJC_IVAR_$_NIAcwgSFZoneUpdate._currentZone
+ OBJC_IVAR_$_NIAcwgSFZoneUpdate._explicitPAITriggered
+ OBJC_IVAR_$_NIAcwgSFZoneUpdate._ioStateDisplacing
+ OBJC_IVAR_$_NIAcwgSFZoneUpdate._lastBtRssiValue
+ OBJC_IVAR_$_NIFindingConfiguration._preferredDiscoveryPriority
+ OBJC_IVAR_$_NIItemLocalizerConfiguration._cameraAssistanceEnabled
+ OBJC_IVAR_$_NIItemLocalizerConfiguration._debugParameters
+ OBJC_IVAR_$_NIItemLocalizerConfiguration._discoveryToken
+ OBJC_IVAR_$_NIItemLocalizerConfiguration._itemUUID
+ OBJC_IVAR_$_NIItemLocalizerConfiguration._preferredUpdateRate
+ OBJC_IVAR_$_NINearbyObject._horizontalDistance
+ OBJC_IVAR_$_NINearbyObject._itemState
+ OBJC_IVAR_$_NISession._itemLocalizerDidPrewarmRanging
+ _NomininalRetryTimeMilliseconds
+ _OBJC_CLASS_$_NIAcwgSFZoneUpdate
+ _OBJC_CLASS_$_NIItemLocalizerConfiguration
+ _OBJC_METACLASS_$_NIAcwgSFZoneUpdate
+ _OBJC_METACLASS_$_NIItemLocalizerConfiguration
+ _OUTLINED_FUNCTION_1
+ __18-[NISession pause]_block_invoke.752
+ __41-[NISession _serverConnectionInterrupted]_block_invoke.785
+ __47-[NISession didUpdateAlgorithmState:forObject:]_block_invoke.875
+ __56-[NISession(CarKey) processDCKMessage:responseCallback:]_block_invoke.1300
+ __OBJC_$_CLASS_METHODS_NIAcwgSFZoneUpdate
+ __OBJC_$_CLASS_METHODS_NIDiscoveryToken(Finding_Project|ItemLocalizer_Project)
+ __OBJC_$_CLASS_METHODS_NIItemLocalizerConfiguration
+ __OBJC_$_CLASS_PROP_LIST_NIAcwgSFZoneUpdate
+ __OBJC_$_INSTANCE_METHODS_NIAcwgSFZoneUpdate
+ __OBJC_$_INSTANCE_METHODS_NIItemLocalizerConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_NIAcwgSFZoneUpdate
+ __OBJC_$_INSTANCE_VARIABLES_NIItemLocalizerConfiguration
+ __OBJC_$_PROP_LIST_NIAcwgSFZoneUpdate
+ __OBJC_$_PROP_LIST_NIItemLocalizerConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_NIAcwgSFZoneUpdate
+ __OBJC_CLASS_RO_$_NIAcwgSFZoneUpdate
+ __OBJC_CLASS_RO_$_NIItemLocalizerConfiguration
+ __OBJC_METACLASS_RO_$_NIAcwgSFZoneUpdate
+ __OBJC_METACLASS_RO_$_NIItemLocalizerConfiguration
+ __Z20NIAcwgSFZoneToString12NIAcwgSFZone
+ __ZL30NISessionInternalStateToString22NISessionInternalState
+ __ZL53InternalInterruptionReasonToNISessionSuspensionReason36UWBSessionInterruptionReasonInternal
+ __ZN4rose6alisha15AcwgM1MsgStructC2ERKNSt3__16vectorItNS2_9allocatorItEEEERKNS3_IhNS4_IhEEEEhjht
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI33UWBSessionInterruptionBookkeepingNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorItNS_9allocatorItEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI33UWBSessionInterruptionBookkeepingEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorItEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE16__init_with_sizeB8ne190102IPKhS6_EEvT_T0_m
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE16__init_with_sizeB8ne190102IPhS5_EEvT_T0_m
+ __ZNSt3__16vectorIhNS_9allocatorIhEEEC2B8ne190102Em
+ __ZNSt3__16vectorItNS_9allocatorItEEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorItNS_9allocatorItEEE16__init_with_sizeB8ne190102IPtS5_EEvT_T0_m
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___38-[NISession _tryToRecoverFromFailure:]_block_invoke
+ ___39-[NISession didReceiveAopSFZoneUpdate:]_block_invoke
+ ___41-[NISession _serverConnectionInterrupted]_block_invoke
+ ___43-[NISession _internalRunWithConfiguration:]_block_invoke
+ __block_literal_global.1258
+ __block_literal_global.1262
+ __block_literal_global.1266
+ __block_literal_global.1270
+ __block_literal_global.1274
+ __block_literal_global.1406
+ __block_literal_global.1408
+ __block_literal_global.1413
+ __block_literal_global.1418
+ __block_literal_global.1420
+ __block_literal_global.1443
+ __block_literal_global.1445
+ _dispatch_after
+ _objc_msgSend$NINearbyObjectDiscoveryPriorityToString:
+ _objc_msgSend$_internalRunWithConfiguration:
+ _objc_msgSend$_sendRemoteDevice:changedState:
+ _objc_msgSend$_shouldReConnectToDaemonAfterCrash
+ _objc_msgSend$_shouldReRunSessionAfterSessionInterruptionEnded
+ _objc_msgSend$_tryToRecoverFromFailure:
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$didUpdateNearbyObjects:
+ _objc_msgSend$generateTokenWithUUID:
+ _objc_msgSend$horizontalDistance
+ _objc_msgSend$initWithSFZone:btConnHandle:lastBtRssiValue:ioStateDisplacing:explicitPAITriggered:currentSFInBubble:
+ _objc_msgSend$initWithSupportedUwbConfigIds:supportedPulseShapeCombos:channelBitmask:uwbSessionId:finalData2Bitmask:selectedProtocolVersion:
+ _objc_msgSend$isIntValidNearbyObjectDiscoveryPriority:
+ _objc_msgSend$itemState
+ _objc_msgSend$itemUUID
+ _objc_msgSend$preferredDiscoveryPriority
+ _objc_msgSend$session:didReceiveAopSFZoneUpdate:
+ _objc_msgSend$setDiscoveryToken:
+ _objc_msgSend$setItemState:
+ _objc_msgSend$setItemUUID:
+ _objc_msgSend$setPreferredDiscoveryPriority:
+ _objc_msgSend$uwbSessionInterruptedWithReason:timestamp:
+ _objc_msgSend$uwbSessionInterruptionReasonEnded:timestamp:
- -[NIConfiguration _internalOsTransactionRequired]
- -[NISystemConfiguration _internalOsTransactionRequired]
- GCC_except_table108
- GCC_except_table135
- GCC_except_table140
- GCC_except_table162
- GCC_except_table163
- GCC_except_table164
- GCC_except_table165
- GCC_except_table166
- GCC_except_table174
- GCC_except_table180
- GCC_except_table181
- GCC_except_table182
- GCC_except_table183
- GCC_except_table197
- GCC_except_table211
- GCC_except_table226
- GCC_except_table230
- GCC_except_table236
- GCC_except_table237
- GCC_except_table240
- GCC_except_table242
- GCC_except_table247
- GCC_except_table248
- GCC_except_table252
- GCC_except_table254
- GCC_except_table258
- GCC_except_table259
- GCC_except_table264
- GCC_except_table268
- GCC_except_table270
- GCC_except_table273
- GCC_except_table278
- GCC_except_table279
- GCC_except_table290
- GCC_except_table293
- GCC_except_table296
- GCC_except_table300
- GCC_except_table40
- GCC_except_table62
- GCC_except_table71
- __18-[NISession pause]_block_invoke.756
- __34-[NISession runWithConfiguration:]_block_invoke.752
- __47-[NISession didUpdateAlgorithmState:forObject:]_block_invoke.873
- __56-[NISession(CarKey) processDCKMessage:responseCallback:]_block_invoke.1282
- __OBJC_$_CLASS_METHODS_NIDiscoveryToken(Finding_Project)
- __ZN4rose6alisha15AcwgM1MsgStructC2ERKNSt3__16vectorItNS2_9allocatorItEEEERKNS3_IhNS4_IhEEEEhjh
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI33UWBSessionInterruptionBookkeepingNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorItNS_9allocatorItEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100ILi0EEEPKc
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI33UWBSessionInterruptionBookkeepingEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorItEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIhNS_9allocatorIhEEE16__init_with_sizeB8ne180100IPKhS6_EEvT_T0_m
- __ZNSt3__16vectorIhNS_9allocatorIhEEE16__init_with_sizeB8ne180100IPhS5_EEvT_T0_m
- __ZNSt3__16vectorIhNS_9allocatorIhEEEC2Em
- __ZNSt3__16vectorItNS_9allocatorItEEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorItNS_9allocatorItEEE16__init_with_sizeB8ne180100IPtS5_EEvT_T0_m
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- __block_literal_global.1240
- __block_literal_global.1244
- __block_literal_global.1248
- __block_literal_global.1252
- __block_literal_global.1256
- __block_literal_global.1390
- __block_literal_global.1392
- __block_literal_global.1397
- __block_literal_global.1402
- __block_literal_global.1404
- __block_literal_global.1427
- __block_literal_global.1429
CStrings:
+ "#item-loc, Remote device Reconnected"
+ "#item-loc, Remote device findable"
+ "#item-loc, Unexpected update rate"
+ "#item-loc, _tryToRecoverFromFailure: NIBluetoothDisconnect"
+ "#item-loc, _tryToRecoverFromFailure: UWB session not interrupted (xpc connection intact), trying to run session again"
+ "#item-loc, _tryToRecoverFromFailure: Waiting for interruption to end"
+ "#item-loc, didUpdateState:forItem: Configuration not of item localizer type"
+ "%0.2fm"
+ "+[NIInternalUtils NINearbyObjectDiscoveryPriorityToString:]"
+ ", Horiz Distance: %@"
+ ", Item State: %@"
+ "-[NISession _sendRemoteDevice:changedState:]"
+ "<ItemUUID: %@, discoveryToken: %@, updateRate: %s, camera: %d, debug-params: %@>>"
+ "<finder: %d [observer %d], cfg-type: %d, ses-token: %@, rate: %s, disc-prio: %s, camera: %d [client %d], debug-params: %@>"
+ "@44@0:8q16S24c28B32B36B40"
+ "@48@0:8@16@24C32I36C40S44"
+ "Bluetooth errored out"
+ "Calling _internalRunWithConfiguration with Config: %@, internal state: %@"
+ "Change tag cell"
+ "Check localized description"
+ "Closer"
+ "Configuration supports nearbyd relaunch after crash"
+ "DaemonCrashed"
+ "Findable"
+ "Further"
+ "InUse"
+ "ItemLocalizer_Project"
+ "Low"
+ "NIAcwgSFZoneUpdate"
+ "NIItemLocalizerConfiguration"
+ "NIItemLocalizerSupport.mm"
+ "NIItemStateToString"
+ "NINearbyObjectDiscoveryPriorityToString:"
+ "NISession trying to re-activate nearbyd [%@]"
+ "NoUpdate"
+ "Q!41!"
+ "Reconfigure errored out"
+ "Reconnected"
+ "Reconnecting"
+ "T@\"NSUUID\",C,N,V_itemUUID"
+ "TB,R,N,V_currentSFInBubble"
+ "TB,R,N,V_explicitPAITriggered"
+ "TB,R,N,V_ioStateDisplacing"
+ "TS,R,N,V_btConnHandle"
+ "TS,R,N,V_selectedProtocolVersion"
+ "Tag cell low power"
+ "Tag errored out"
+ "Tc,R,N,V_lastBtRssiValue"
+ "Tf,N,V_horizontalDistance"
+ "Tq,N,V_itemState"
+ "Tq,N,V_preferredDiscoveryPriority"
+ "Tq,R,N,V_currentZone"
+ "_btConnHandle"
+ "_currentSFInBubble"
+ "_currentZone"
+ "_explicitPAITriggered"
+ "_horizontalDistance"
+ "_internalIsMemoryAssertionRequired"
+ "_internalIsPowerAssertionRequired"
+ "_internalRunWithConfiguration:"
+ "_ioStateDisplacing"
+ "_itemLocalizerDidPrewarmRanging"
+ "_itemState"
+ "_itemUUID"
+ "_lastBtRssiValue"
+ "_preferredDiscoveryPriority"
+ "_selectedProtocolVersion"
+ "_sendRemoteDevice:changedState:"
+ "_shouldReConnectToDaemonAfterCrash"
+ "_shouldReRunSessionAfterSessionInterruptionEnded"
+ "_shouldReRunSessionAfterSessionInterruptionEnded %d"
+ "_tryToRecoverFromFailure:"
+ "btConnHandle"
+ "btConnHandle:(0x%04x)\n"
+ "c"
+ "c16@0:8"
+ "currentSFInBubble"
+ "currentSFInBubble:%d>\n"
+ "currentZone"
+ "currentZone:%@\n"
+ "dataUsingEncoding:"
+ "dicoveryTokenFromUUID != nil"
+ "didReceiveAopSFZoneUpdate:"
+ "didUpdateState:forItem:"
+ "explicitPAITriggered"
+ "explicitPAITriggered:%d\n"
+ "finalData2Bitmask:0x%02x\n"
+ "generateTokenWithUUID:"
+ "horizontalDistance"
+ "initWithItemUUID:preferredUpdateRate:"
+ "initWithSFZone:btConnHandle:lastBtRssiValue:ioStateDisplacing:explicitPAITriggered:currentSFInBubble:"
+ "initWithSupportedUwbConfigIds:supportedPulseShapeCombos:channelBitmask:uwbSessionId:finalData2Bitmask:selectedProtocolVersion:"
+ "ioStateDisplacing"
+ "ioStateDisplacing:%d\n"
+ "isIntValidNearbyObjectDiscoveryPriority:"
+ "itemState"
+ "itemUUID"
+ "lastBtRssiValue"
+ "lastBtRssiValue:%d\n"
+ "preferredDiscoveryPriority"
+ "selectedProtocolVersion"
+ "selectedProtocolVersion:0x%04x>\n"
+ "session:didReceiveAopSFZoneUpdate:"
+ "setHorizontalDistance:"
+ "setItemState:"
+ "setItemUUID:"
+ "setPreferredDiscoveryPriority:"
+ "v24@0:8@\"NIAcwgSFZoneUpdate\"16"
+ "v32@0:8q16@\"NSUUID\"24"
+ "v32@0:8q16@24"
+ "{AcwgM1MsgStruct={vector<unsigned short, std::allocator<unsigned short>>=^S^S{__compressed_pair<unsigned short *, std::allocator<unsigned short>>=^S}}{vector<unsigned char, std::allocator<unsigned char>>=**{__compressed_pair<unsigned char *, std::allocator<unsigned char>>=*}}CICS}16@0:8"
- "2"
- "<finder: %d [observer %d], cfg-type: %d, ses-token: %@, rate: %s, camera: %d [client %d], debug-params: %@>"
- "A!41!"
- "_internalOsTransactionRequired"
- "finalData2Bitmask:0x%02x>"
- "{AcwgM1MsgStruct={vector<unsigned short, std::allocator<unsigned short>>=^S^S{__compressed_pair<unsigned short *, std::allocator<unsigned short>>=^S}}{vector<unsigned char, std::allocator<unsigned char>>=**{__compressed_pair<unsigned char *, std::allocator<unsigned char>>=*}}CIC}16@0:8"

```
