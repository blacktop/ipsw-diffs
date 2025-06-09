## NearbyInteraction

> `/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`

```diff

-466.0.4.0.0
-  __TEXT.__text: 0x2eb68
-  __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_methlist: 0x39a0
-  __TEXT.__gcc_except_tab: 0x4fe8
-  __TEXT.__cstring: 0x48d8
-  __TEXT.__const: 0x520
-  __TEXT.__oslogstring: 0x1368
+502.0.0.0.0
+  __TEXT.__text: 0x32038
+  __TEXT.__auth_stubs: 0x870
+  __TEXT.__objc_methlist: 0x3e88
+  __TEXT.__gcc_except_tab: 0x5520
+  __TEXT.__cstring: 0x4d32
+  __TEXT.__const: 0x4e0
+  __TEXT.__oslogstring: 0x132d
   __TEXT.__swift5_typeref: 0x83
   __TEXT.__swift5_reflstr: 0x4b
   __TEXT.__swift5_assocty: 0x48

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x1ce8
-  __TEXT.__objc_classname: 0x588
-  __TEXT.__objc_methname: 0x8461
-  __TEXT.__objc_methtype: 0x1658
-  __TEXT.__objc_stubs: 0x4ba0
-  __DATA_CONST.__got: 0x280
-  __DATA_CONST.__const: 0xcc8
-  __DATA_CONST.__objc_classlist: 0x178
+  __TEXT.__unwind_info: 0x1f00
+  __TEXT.__objc_classname: 0x5fd
+  __TEXT.__objc_methname: 0x8d27
+  __TEXT.__objc_methtype: 0x1629
+  __TEXT.__objc_stubs: 0x4f60
+  __DATA_CONST.__got: 0x290
+  __DATA_CONST.__const: 0xcd8
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bc0
+  __DATA_CONST.__objc_selrefs: 0x1d48
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x160
+  __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x428
+  __AUTH_CONST.__auth_got: 0x448
   __AUTH_CONST.__const: 0x3f8
-  __AUTH_CONST.__cfstring: 0x4f20
-  __AUTH_CONST.__objc_const: 0x6910
-  __AUTH_CONST.__objc_intobj: 0x228
+  __AUTH_CONST.__cfstring: 0x54e0
+  __AUTH_CONST.__objc_const: 0x7158
+  __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_ivar: 0x448
+  __AUTH.__objc_data: 0x460
+  __DATA.__objc_ivar: 0x4a0
   __DATA.__data: 0x4f0
-  __DATA.__bss: 0x5b0
+  __DATA.__bss: 0x5a0
   __DATA.__common: 0x153
-  __DATA_DIRTY.__objc_data: 0xaf0
-  __DATA_DIRTY.__bss: 0x68
+  __DATA_DIRTY.__objc_data: 0xb90
+  __DATA_DIRTY.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ARKitCore.framework/ARKitCore

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 61BC2239-B143-3220-B57D-F145E9D4B705
-  Functions: 1350
-  Symbols:   4844
-  CStrings:  3156
+  UUID: 2CD65620-2A23-342C-89F0-60447BC2F053
+  Functions: 1450
+  Symbols:   5173
+  CStrings:  3346
 
Symbols:
+ +[NIDLTDOAConfiguration supportsSecureCoding]
+ +[NIDLTDOACoordinatesUpdate supportsSecureCoding]
+ +[NIDLTDOAMeasurement supportsSecureCoding]
+ +[NIDiscoveryToken(Finding_Project) generateDiscoveryTokenFromBeaconIdentifier:]
+ +[NIHomePassiveSensingConfiguration new]
+ +[NIHomePassiveSensingConfiguration supportsSecureCoding]
+ +[NIInternalUtils NINearbyPeerUseCaseToString:]
+ +[NIInternalUtils NINearbyPeerUseCaseToString:].cold.1
+ +[NINearbyPeerConfiguration(SOSBeacon) createSOSBeaconSearcherConfigWithSessionKey:selfData:peerData:usingCameraAssistance:]
+ +[NINearbyPeerConfiguration(SOSBeacon) createSOSBeaconSubjectConfigWithSessionKey:selfData:peerData:]
+ +[NISession(Finding) generateDiscoveryTokenFromBeaconIdentifier:]
+ +[NISession(SOSBeacon) generateSOSBeaconSearcherDataMatchingSubjectData:completion:]
+ +[NISession(SOSBeacon) generateSOSBeaconSubjectDataWithCompletion:]
+ -[NIBluetoothSample devicePlacement]
+ -[NIBluetoothSample setDevicePlacement:]
+ -[NIDLTDOAConfiguration .cxx_destruct]
+ -[NIDLTDOAConfiguration _internalIsCameraAssistanceEnabled]
+ -[NIDLTDOAConfiguration copyWithZone:]
+ -[NIDLTDOAConfiguration debugParameters]
+ -[NIDLTDOAConfiguration descriptionInternal]
+ -[NIDLTDOAConfiguration description]
+ -[NIDLTDOAConfiguration encodeWithCoder:]
+ -[NIDLTDOAConfiguration hash]
+ -[NIDLTDOAConfiguration initWithCoder:]
+ -[NIDLTDOAConfiguration initWithConfigParametersOverride:]
+ -[NIDLTDOAConfiguration initWithNetworkIdentifier:]
+ -[NIDLTDOAConfiguration isCameraAssistanceEnabled]
+ -[NIDLTDOAConfiguration isEqual:]
+ -[NIDLTDOAConfiguration networkIdentifier]
+ -[NIDLTDOAConfiguration setCameraAssistanceEnabled:]
+ -[NIDLTDOAConfiguration setDebugParameters:]
+ -[NIDLTDOAConfiguration setNetworkIdentifier:]
+ -[NIDLTDOACoordinatesUpdate coordinatesType]
+ -[NIDLTDOACoordinatesUpdate coordinates]
+ -[NIDLTDOACoordinatesUpdate copyWithZone:]
+ -[NIDLTDOACoordinatesUpdate description]
+ -[NIDLTDOACoordinatesUpdate encodeWithCoder:]
+ -[NIDLTDOACoordinatesUpdate hash]
+ -[NIDLTDOACoordinatesUpdate initWithCoder:]
+ -[NIDLTDOACoordinatesUpdate initWithDLTDOACoordinatesType:coordinates:]
+ -[NIDLTDOACoordinatesUpdate isEqual:]
+ -[NIDLTDOAMeasurement address]
+ -[NIDLTDOAMeasurement carrierFrequencyOffset]
+ -[NIDLTDOAMeasurement coordinatesType]
+ -[NIDLTDOAMeasurement coordinates]
+ -[NIDLTDOAMeasurement copyWithZone:]
+ -[NIDLTDOAMeasurement description]
+ -[NIDLTDOAMeasurement encodeWithCoder:]
+ -[NIDLTDOAMeasurement hash]
+ -[NIDLTDOAMeasurement initWithAnchorAddress:measurementType:coordinatesType:transmitTime:receiveTime:signalStrength:carrierFrequencyOffset:coordinates:]
+ -[NIDLTDOAMeasurement initWithCoder:]
+ -[NIDLTDOAMeasurement isEqual:]
+ -[NIDLTDOAMeasurement measurementType]
+ -[NIDLTDOAMeasurement receiveTime]
+ -[NIDLTDOAMeasurement setAddress:]
+ -[NIDLTDOAMeasurement setCarrierFrequencyOffset:]
+ -[NIDLTDOAMeasurement setCoordinates:]
+ -[NIDLTDOAMeasurement setCoordinatesType:]
+ -[NIDLTDOAMeasurement setMeasurementType:]
+ -[NIDLTDOAMeasurement setReceiveTime:]
+ -[NIDLTDOAMeasurement setSignalStrength:]
+ -[NIDLTDOAMeasurement setTransmitTime:]
+ -[NIDLTDOAMeasurement signalStrength]
+ -[NIDLTDOAMeasurement transmitTime]
+ -[NIDeviceCapabilities supportsDLTDOAMeasurement]
+ -[NIFindingConfiguration _initInternalWithConfigType:isFinder:isObserver:specifiedToken:preferredUpdateRate:requestedMeasurementQuality:]
+ -[NIFindingConfiguration discoveryTokenVariant]
+ -[NIFindingConfiguration initWithDiscoveryToken:requestedUpdateRate:requestedMeasaurementQuality:]
+ -[NIFindingConfiguration monitoredRegions]
+ -[NIFindingConfiguration requestedMeasurementQuality]
+ -[NIFindingConfiguration setDiscoveryTokenVariant:]
+ -[NIFindingConfiguration setMonitoredRegions:]
+ -[NIFindingConfiguration setRequestedMeasurementQuality:]
+ -[NIHomePassiveSensingConfiguration canUpdateToConfiguration:]
+ -[NIHomePassiveSensingConfiguration copyWithZone:]
+ -[NIHomePassiveSensingConfiguration descriptionInternal]
+ -[NIHomePassiveSensingConfiguration description]
+ -[NIHomePassiveSensingConfiguration encodeWithCoder:]
+ -[NIHomePassiveSensingConfiguration hash]
+ -[NIHomePassiveSensingConfiguration initWithCoder:]
+ -[NIHomePassiveSensingConfiguration init]
+ -[NIHomePassiveSensingConfiguration isEqual:]
+ -[NIHomePassiveSensingConfiguration minimumPreferredUpdatedRate]
+ -[NIHomePassiveSensingConfiguration setMinimumPreferredUpdatedRate:]
+ -[NINearbyObject location]
+ -[NINearbyObject setLocation:]
+ -[NINearbyPeerConfiguration _internalIsCameraAssistanceInClientProcess]
+ -[NINearbyPeerConfiguration setUseCase:]
+ -[NINearbyPeerConfiguration setUseCaseCameraAssistanceInClientProcess:]
+ -[NINearbyPeerConfiguration useCaseCameraAssistanceInClientProcess]
+ -[NINearbyPeerConfiguration useCase]
+ -[NISession _configurationSupportsRetry]
+ -[NISession _interruptSessionWithInternalReason:cachedInterruption:nearbydReSuspension:]
+ -[NISession didUpdateDLTDOAMeasurements:]
+ -[NISession didUpdateNICoordinates:]
+ -[NSCoder(NearbyInteraction) decodeDoubleVector3ForKey:]
+ -[NSCoder(NearbyInteraction) encodeDoubleVector3:forKey:]
+ GCC_except_table141
+ GCC_except_table142
+ GCC_except_table143
+ GCC_except_table144
+ GCC_except_table161
+ GCC_except_table169
+ GCC_except_table175
+ GCC_except_table184
+ GCC_except_table190
+ GCC_except_table196
+ GCC_except_table197
+ GCC_except_table198
+ GCC_except_table199
+ GCC_except_table215
+ GCC_except_table216
+ GCC_except_table217
+ GCC_except_table218
+ GCC_except_table219
+ GCC_except_table232
+ GCC_except_table233
+ GCC_except_table236
+ GCC_except_table239
+ GCC_except_table246
+ GCC_except_table249
+ GCC_except_table252
+ GCC_except_table255
+ GCC_except_table258
+ GCC_except_table261
+ GCC_except_table262
+ GCC_except_table268
+ GCC_except_table269
+ GCC_except_table270
+ GCC_except_table276
+ GCC_except_table279
+ GCC_except_table282
+ GCC_except_table286
+ GCC_except_table294
+ GCC_except_table296
+ GCC_except_table298
+ GCC_except_table307
+ GCC_except_table315
+ GCC_except_table318
+ GCC_except_table321
+ GCC_except_table324
+ GCC_except_table325
+ GCC_except_table328
+ GCC_except_table338
+ GCC_except_table339
+ GCC_except_table340
+ GCC_except_table342
+ GCC_except_table343
+ GCC_except_table347
+ GCC_except_table35
+ GCC_except_table350
+ _OBJC_CLASS_$_NIDLTDOAConfiguration
+ _OBJC_CLASS_$_NIDLTDOACoordinatesUpdate
+ _OBJC_CLASS_$_NIDLTDOAMeasurement
+ _OBJC_CLASS_$_NIHomePassiveSensingConfiguration
+ _OBJC_IVAR_$_NIBluetoothSample._devicePlacement
+ _OBJC_IVAR_$_NIDLTDOAConfiguration._cameraAssistanceEnabled
+ _OBJC_IVAR_$_NIDLTDOAConfiguration._debugParameters
+ _OBJC_IVAR_$_NIDLTDOAConfiguration._networkIdentifier
+ _OBJC_IVAR_$_NIDLTDOACoordinatesUpdate._coordinates
+ _OBJC_IVAR_$_NIDLTDOACoordinatesUpdate._coordinatesType
+ _OBJC_IVAR_$_NIDLTDOAMeasurement._address
+ _OBJC_IVAR_$_NIDLTDOAMeasurement._carrierFrequencyOffset
+ _OBJC_IVAR_$_NIDLTDOAMeasurement._coordinates
+ _OBJC_IVAR_$_NIDLTDOAMeasurement._coordinatesType
+ _OBJC_IVAR_$_NIDLTDOAMeasurement._measurementType
+ _OBJC_IVAR_$_NIDLTDOAMeasurement._receiveTime
+ _OBJC_IVAR_$_NIDLTDOAMeasurement._signalStrength
+ _OBJC_IVAR_$_NIDLTDOAMeasurement._transmitTime
+ _OBJC_IVAR_$_NIDeviceCapabilities._supportsDLTDOAMeasurement
+ _OBJC_IVAR_$_NIFindingConfiguration._discoveryTokenVariant
+ _OBJC_IVAR_$_NIFindingConfiguration._monitoredRegions
+ _OBJC_IVAR_$_NIFindingConfiguration._requestedMeasurementQuality
+ _OBJC_IVAR_$_NIHomePassiveSensingConfiguration._minimumPreferredUpdatedRate
+ _OBJC_IVAR_$_NINearbyObject._location
+ _OBJC_IVAR_$_NINearbyPeerConfiguration._useCase
+ _OBJC_IVAR_$_NINearbyPeerConfiguration._useCaseCameraAssistanceInClientProcess
+ _OBJC_METACLASS_$_NIDLTDOAConfiguration
+ _OBJC_METACLASS_$_NIDLTDOACoordinatesUpdate
+ _OBJC_METACLASS_$_NIDLTDOAMeasurement
+ _OBJC_METACLASS_$_NIHomePassiveSensingConfiguration
+ __OBJC_$_CLASS_METHODS_NIDLTDOAConfiguration
+ __OBJC_$_CLASS_METHODS_NIDLTDOACoordinatesUpdate
+ __OBJC_$_CLASS_METHODS_NIDLTDOAMeasurement
+ __OBJC_$_CLASS_METHODS_NIHomePassiveSensingConfiguration
+ __OBJC_$_CLASS_METHODS_NINearbyPeerConfiguration(SOSBeacon)
+ __OBJC_$_CLASS_METHODS_NISession(Internal|CarKey|CarKey_Project|Acwg|SpatialBrowsing|Vision|DevicePresence|Finding|Perf|SystemConfigurator|LocalDeviceInteraction|SOSBeacon)
+ __OBJC_$_CLASS_PROP_LIST_NIDLTDOACoordinatesUpdate
+ __OBJC_$_CLASS_PROP_LIST_NIDLTDOAMeasurement
+ __OBJC_$_INSTANCE_METHODS_NIDLTDOAConfiguration
+ __OBJC_$_INSTANCE_METHODS_NIDLTDOACoordinatesUpdate
+ __OBJC_$_INSTANCE_METHODS_NIDLTDOAMeasurement
+ __OBJC_$_INSTANCE_METHODS_NIHomePassiveSensingConfiguration
+ __OBJC_$_INSTANCE_METHODS_NISession(Internal|CarKey|CarKey_Project|Acwg|SpatialBrowsing|Vision|DevicePresence|Finding|Perf|SystemConfigurator|LocalDeviceInteraction|SOSBeacon)
+ __OBJC_$_INSTANCE_METHODS_NSCoder(NearbyInteraction|NearbyInteraction|NearbyInteraction)
+ __OBJC_$_INSTANCE_VARIABLES_NIDLTDOAConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_NIDLTDOACoordinatesUpdate
+ __OBJC_$_INSTANCE_VARIABLES_NIDLTDOAMeasurement
+ __OBJC_$_INSTANCE_VARIABLES_NIHomePassiveSensingConfiguration
+ __OBJC_$_PROP_LIST_NIDLTDOAConfiguration
+ __OBJC_$_PROP_LIST_NIDLTDOACoordinatesUpdate
+ __OBJC_$_PROP_LIST_NIDLTDOAMeasurement
+ __OBJC_$_PROP_LIST_NIHomePassiveSensingConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_NIDLTDOACoordinatesUpdate
+ __OBJC_CLASS_PROTOCOLS_$_NIDLTDOAMeasurement
+ __OBJC_CLASS_RO_$_NIDLTDOAConfiguration
+ __OBJC_CLASS_RO_$_NIDLTDOACoordinatesUpdate
+ __OBJC_CLASS_RO_$_NIDLTDOAMeasurement
+ __OBJC_CLASS_RO_$_NIHomePassiveSensingConfiguration
+ __OBJC_METACLASS_RO_$_NIDLTDOAConfiguration
+ __OBJC_METACLASS_RO_$_NIDLTDOACoordinatesUpdate
+ __OBJC_METACLASS_RO_$_NIDLTDOAMeasurement
+ __OBJC_METACLASS_RO_$_NIHomePassiveSensingConfiguration
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100ILi0EEEPKc
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorI33UWBSessionInterruptionBookkeepingEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorImEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorItEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__16vectorI33UWBSessionInterruptionBookkeepingNS_9allocatorIS1_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorI33UWBSessionInterruptionBookkeepingNS_9allocatorIS1_EEE18__assign_with_sizeB8ne200100IPS1_S6_EEvT_T0_l
+ __ZNSt3__16vectorI33UWBSessionInterruptionBookkeepingNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE16__init_with_sizeB8ne200100IPKhS6_EEvT_T0_m
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE16__init_with_sizeB8ne200100IPhS5_EEvT_T0_m
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIhNS_9allocatorIhEEEC2B8ne200100Em
+ __ZNSt3__16vectorImNS_9allocatorImEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorImNS_9allocatorImEEE16__init_with_sizeB8ne200100IPKmS6_EEvT_T0_m
+ __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorItNS_9allocatorItEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorItNS_9allocatorItEEE16__init_with_sizeB8ne200100IPtS5_EEvT_T0_m
+ __ZNSt3__16vectorItNS_9allocatorItEEE20__throw_length_errorB8ne200100Ev
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZnwmSt19__type_descriptor_t
+ ___18-[NISession pause]_block_invoke.923
+ ___34-[NISession runWithConfiguration:]_block_invoke.918
+ ___36-[NISession didUpdateNICoordinates:]_block_invoke
+ ___41-[NISession _serverConnectionInterrupted]_block_invoke.958
+ ___41-[NISession didUpdateDLTDOAMeasurements:]_block_invoke
+ ___48-[NISession _initAndConnectToServerWithOptions:]_block_invoke.870
+ ___57-[NISession uwbSessionInterruptionReasonEnded:timestamp:]_block_invoke.982
+ ___88-[NISession _interruptSessionWithInternalReason:cachedInterruption:nearbydReSuspension:]_block_invoke
+ ___88-[NISession _interruptSessionWithInternalReason:cachedInterruption:nearbydReSuspension:]_block_invoke_2
+ ___Block_byref_object_copy_.928
+ ___Block_byref_object_dispose_.929
+ ___block_literal_global.1477
+ ___block_literal_global.1481
+ ___block_literal_global.1489
+ ___block_literal_global.1493
+ ___block_literal_global.1611
+ ___block_literal_global.1613
+ ___block_literal_global.1618
+ ___block_literal_global.1623
+ ___block_literal_global.1625
+ ___block_literal_global.1649
+ ___block_literal_global.1651
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_NearbyInteraction
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_NearbyInteraction
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_NearbyInteraction
+ _objc_msgSend$NINearbyPeerUseCaseToString:
+ _objc_msgSend$_configurationSupportsRetry
+ _objc_msgSend$_initInternalWithConfigType:isFinder:isObserver:specifiedToken:preferredUpdateRate:requestedMeasurementQuality:
+ _objc_msgSend$_interruptSessionWithInternalReason:cachedInterruption:nearbydReSuspension:
+ _objc_msgSend$address
+ _objc_msgSend$carrierFrequencyOffset
+ _objc_msgSend$coordinates
+ _objc_msgSend$coordinatesType
+ _objc_msgSend$decodeDoubleVector3ForKey:
+ _objc_msgSend$decodeObjectForKey:
+ _objc_msgSend$discoveryTokenVariant
+ _objc_msgSend$encodeDoubleVector3:forKey:
+ _objc_msgSend$generateDiscoveryTokenFromBeaconIdentifier:
+ _objc_msgSend$initWithAnchorAddress:measurementType:coordinatesType:transmitTime:receiveTime:signalStrength:carrierFrequencyOffset:coordinates:
+ _objc_msgSend$initWithDLTDOACoordinatesType:coordinates:
+ _objc_msgSend$location
+ _objc_msgSend$measurementType
+ _objc_msgSend$networkIdentifier
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$receiveTime
+ _objc_msgSend$requestedMeasurementQuality
+ _objc_msgSend$session:didUpdateDLTDOAMeasurements:
+ _objc_msgSend$session:didUpdateNICoordinates:
+ _objc_msgSend$setDiscoveryTokenVariant:
+ _objc_msgSend$setNetworkIdentifier:
+ _objc_msgSend$setRequestedMeasurementQuality:
+ _objc_msgSend$setUseCase:
+ _objc_msgSend$setUseCaseCameraAssistanceInClientProcess:
+ _objc_msgSend$tokenVariant
+ _objc_msgSend$transmitTime
+ _objc_msgSend$useCase
+ _objc_msgSend$useCaseCameraAssistanceInClientProcess
+ _objc_retain_x28
+ _objc_sync_enter
+ _objc_sync_exit
- +[NIFindingConfiguration localDeviceConfiguration]
- -[NIFindingConfiguration _initInternalWithConfigType:isFinder:isObserver:specifiedToken:preferredUpdateRate:]
- -[NISession _interruptSessionWithInternalReason:cachedInterruption:]
- GCC_except_table155
- GCC_except_table157
- GCC_except_table158
- GCC_except_table160
- GCC_except_table165
- GCC_except_table173
- GCC_except_table179
- GCC_except_table188
- GCC_except_table194
- GCC_except_table208
- GCC_except_table210
- GCC_except_table211
- GCC_except_table212
- GCC_except_table214
- GCC_except_table221
- GCC_except_table222
- GCC_except_table223
- GCC_except_table224
- GCC_except_table225
- GCC_except_table237
- GCC_except_table238
- GCC_except_table241
- GCC_except_table244
- GCC_except_table251
- GCC_except_table254
- GCC_except_table257
- GCC_except_table260
- GCC_except_table263
- GCC_except_table271
- GCC_except_table273
- GCC_except_table274
- GCC_except_table277
- GCC_except_table281
- GCC_except_table284
- GCC_except_table285
- GCC_except_table291
- GCC_except_table297
- GCC_except_table299
- GCC_except_table303
- GCC_except_table311
- GCC_except_table317
- GCC_except_table320
- GCC_except_table323
- GCC_except_table326
- GCC_except_table333
- GCC_except_table334
- GCC_except_table336
- GCC_except_table341
- GCC_except_table344
- GCC_except_table82
- GCC_except_table96
- __OBJC_$_CLASS_METHODS_NINearbyPeerConfiguration
- __OBJC_$_CLASS_METHODS_NISession(Internal|CarKey|CarKey_Project|Acwg|SpatialBrowsing|Vision|DevicePresence|Finding|Perf|SystemConfigurator|LocalDeviceInteraction)
- __OBJC_$_INSTANCE_METHODS_NISession(Internal|CarKey|CarKey_Project|Acwg|SpatialBrowsing|Vision|DevicePresence|Finding|Perf|SystemConfigurator|LocalDeviceInteraction)
- __OBJC_$_INSTANCE_METHODS_NSCoder(NearbyInteraction|NearbyInteraction)
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI33UWBSessionInterruptionBookkeepingNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorItNS_9allocatorItEEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI33UWBSessionInterruptionBookkeepingEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorItEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIhNS_9allocatorIhEEE16__init_with_sizeB8ne190102IPKhS6_EEvT_T0_m
- __ZNSt3__16vectorIhNS_9allocatorIhEEE16__init_with_sizeB8ne190102IPhS5_EEvT_T0_m
- __ZNSt3__16vectorIhNS_9allocatorIhEEEC2B8ne190102Em
- __ZNSt3__16vectorItNS_9allocatorItEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorItNS_9allocatorItEEE16__init_with_sizeB8ne190102IPtS5_EEvT_T0_m
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- ___18-[NISession pause]_block_invoke.791
- ___34-[NISession runWithConfiguration:]_block_invoke.786
- ___41-[NISession _serverConnectionInterrupted]_block_invoke.826
- ___48-[NISession _initAndConnectToServerWithOptions:]_block_invoke.738
- ___57-[NISession uwbSessionInterruptionReasonEnded:timestamp:]_block_invoke.850
- ___68-[NISession _interruptSessionWithInternalReason:cachedInterruption:]_block_invoke
- ___68-[NISession _interruptSessionWithInternalReason:cachedInterruption:]_block_invoke_2
- ___Block_byref_object_copy_.796
- ___Block_byref_object_dispose_.797
- ___block_literal_global.1337
- ___block_literal_global.1341
- ___block_literal_global.1345
- ___block_literal_global.1349
- ___block_literal_global.1353
- ___block_literal_global.1471
- ___block_literal_global.1473
- ___block_literal_global.1478
- ___block_literal_global.1483
- ___block_literal_global.1508
- ___block_literal_global.1510
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_NearbyInteraction
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_NearbyInteraction
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_NearbyInteraction
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_NearbyInteraction
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_NearbyInteraction
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_NearbyInteraction
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_NearbyInteraction
- _objc_msgSend$_initInternalWithConfigType:isFinder:isObserver:specifiedToken:preferredUpdateRate:
- _objc_msgSend$_interruptSessionWithInternalReason:cachedInterruption:
CStrings:
+ "+[NIInternalUtils NINearbyPeerUseCaseToString:]"
+ ", camera: 0"
+ ", camera: 1 [inClient: %d]"
+ ", devicePlacement: %ld"
+ ", rangingModes: [LR %d, EXT %d]"
+ ", useCase: %s"
+ "0x%lx,  debugParameters:%@, cameraAssistanceEnabled: %@"
+ "<finder: %d [observer %d], cfg-type: %d, ses-token: %@, rate: %s, disc-prio: %s, camera: %d [client %d], debug-params: %@, disc-token-var: %d>, requested-meas-qual: %d"
+ "<min-rate: %s>"
+ "@\"NILocation\""
+ "@104@0:8Q16q24q32d40d48d56d6472"
+ "@40@0:8@16q24q32"
+ "@44@0:8@16@24@32B40"
+ "@56@0:8q1624"
+ "@56@0:8q16B24B28@32q40q48"
+ "AccessoryInUse"
+ "Address"
+ "Address: [%ld], "
+ "AnchorCoordinates"
+ "AnchorCoordinatesType"
+ "ArmsReach"
+ "Beacon resolution failed"
+ "Carrier Frequency Offset: [%f], "
+ "CarrierFrequencyOffset"
+ "Continuation"
+ "Coordinates"
+ "CoordinatesType"
+ "ExtendedReach"
+ "Generic"
+ "KnownDevice"
+ "MeasurementType"
+ "NIDLTDOAConfiguration"
+ "NIDLTDOAConfiguration.mm"
+ "NIDLTDOACoordinatesUpdate"
+ "NIDLTDOACoordinatesUpdate.mm"
+ "NIDLTDOAMeasurement"
+ "NIHomePassiveSensingConfiguration"
+ "NINearbyPeerUseCaseToString:"
+ "NSData must contain enough bytes for simd_double3"
+ "Operation not enabled"
+ "Receive Time: [%f], "
+ "ReceiveTime"
+ "SOSBeacon"
+ "Signal Strength: [%f], "
+ "SignalStrength"
+ "T,R,N,V_coordinates"
+ "T@\"NILocation\",C,N,V_location"
+ "T@\"NSArray\",&,V_monitoredRegions"
+ "TB,N,V_useCaseCameraAssistanceInClientProcess"
+ "TB,R,N,V_supportsDLTDOAMeasurement"
+ "TQ,R,N,V_address"
+ "Td,R,N,V_carrierFrequencyOffset"
+ "Td,R,N,V_receiveTime"
+ "Td,R,N,V_signalStrength"
+ "Td,R,N,V_transmitTime"
+ "Tq,N,V_discoveryTokenVariant"
+ "Tq,N,V_networkIdentifier"
+ "Tq,N,V_requestedMeasurementQuality"
+ "Tq,N,V_useCase"
+ "Tq,R,N,V_coordinatesType"
+ "Tq,R,N,V_measurementType"
+ "Tq,V_devicePlacement"
+ "Transimit Time: [%f], "
+ "TransmitTime"
+ "Type: [Final], "
+ "Type: [Poll], "
+ "Type: [Response], "
+ "UseConfigParametersOverrides"
+ "[Redacted]"
+ "_address"
+ "_carrierFrequencyOffset"
+ "_configurationSupportsRetry"
+ "_coordinates"
+ "_coordinatesType"
+ "_devicePlacement"
+ "_discoveryTokenVariant"
+ "_initInternalWithConfigType:isFinder:isObserver:specifiedToken:preferredUpdateRate:requestedMeasurementQuality:"
+ "_interruptSessionWithInternalReason:cachedInterruption:nearbydReSuspension:"
+ "_location"
+ "_measurementType"
+ "_networkIdentifier"
+ "_receiveTime"
+ "_requestedMeasurementQuality"
+ "_supportsDLTDOAMeasurement"
+ "_transmitTime"
+ "_useCase"
+ "_useCaseCameraAssistanceInClientProcess"
+ "address"
+ "beaconIdentifier"
+ "carrierFrequencyOffset"
+ "configParameters"
+ "coordinates"
+ "coordinatesType"
+ "createSOSBeaconSearcherConfigWithSessionKey:selfData:peerData:usingCameraAssistance:"
+ "createSOSBeaconSubjectConfigWithSessionKey:selfData:peerData:"
+ "debugParamsIdentifier"
+ "decodeDoubleVector3ForKey:"
+ "decodeObjectForKey:"
+ "devicePlacement"
+ "didUpdateDLTDOAMeasurements:"
+ "didUpdateNICoordinates:"
+ "discoveryTokenVariant"
+ "encodeDoubleVector3:forKey:"
+ "generateDiscoveryTokenFromBeaconIdentifier:"
+ "generateSOSBeaconDataForSubject:peerData:reply:"
+ "generateSOSBeaconSearcherDataMatchingSubjectData:completion:"
+ "generateSOSBeaconSubjectDataWithCompletion:"
+ "geodetic coordinates:"
+ "initWithAnchorAddress:measurementType:coordinatesType:transmitTime:receiveTime:signalStrength:carrierFrequencyOffset:coordinates:"
+ "initWithConfigParametersOverride:"
+ "initWithDLTDOACoordinatesType:coordinates:"
+ "initWithDiscoveryToken:requestedUpdateRate:requestedMeasaurementQuality:"
+ "initWithNetworkIdentifier:"
+ "measurementType"
+ "networkIdentifier"
+ "numberWithLongLong:"
+ "peerToken: %@"
+ "peerToken: null"
+ "receiveTime"
+ "relative coordinates:"
+ "requestedMeasurementQuality"
+ "session:didUpdateDLTDOAMeasurements:"
+ "session:didUpdateNICoordinates:"
+ "setAddress:"
+ "setCarrierFrequencyOffset:"
+ "setCoordinates:"
+ "setCoordinatesType:"
+ "setDevicePlacement:"
+ "setDiscoveryTokenVariant:"
+ "setLocation:"
+ "setMeasurementType:"
+ "setNetworkIdentifier:"
+ "setReceiveTime:"
+ "setRequestedMeasurementQuality:"
+ "setTransmitTime:"
+ "setUseCase:"
+ "setUseCaseCameraAssistanceInClientProcess:"
+ "simd_double3 GetDoubleVector3FromNSData(NSData * _Nonnull __strong)"
+ "supportsDLTDOAMeasurement"
+ "transmitTime"
+ "useCase"
+ "useCaseCameraAssistanceInClientProcess"
+ "v24@0:8@\"NIDLTDOACoordinatesUpdate\"16"
+ "v32@0:8q16B24B28"
+ "v36@0:8B16@\"NSData\"20@?<v@?@\"NSData\"@\"NSError\">28"
+ "v48@0:816"
+ "v56@0:816@48"
+ "x: %.6f, "
+ "y: %.6f, "
+ "z: %.6f>"
+ "{AcwgM1MsgStruct={vector<unsigned short, std::allocator<unsigned short>>=^S^S^S}{vector<unsigned char, std::allocator<unsigned char>>=***}CICS}16@0:8"
+ "{vector<UWBSessionInterruptionBookkeeping, std::allocator<UWBSessionInterruptionBookkeeping>>=\"__begin_\"^{UWBSessionInterruptionBookkeeping}\"__end_\"^{UWBSessionInterruptionBookkeeping}\"__cap_\"^{UWBSessionInterruptionBookkeeping}}"
- "#item-loc, _tryToRecoverFromFailure: NIBluetoothDisconnect"
- ", isExtendedDistanceMeasurementEnabled: %s"
- ", isLongRangeEnabled: %s"
- "<finder: %d [observer %d], cfg-type: %d, ses-token: %@, rate: %s, disc-prio: %s, camera: %d [client %d], debug-params: %@>"
- "@48@0:8q16B24B28@32q40"
- "Known Device"
- "Q!41!"
- "Session Continuation"
- "_initInternalWithConfigType:isFinder:isObserver:specifiedToken:preferredUpdateRate:"
- "_interruptSessionWithInternalReason:cachedInterruption:"
- "localDeviceConfiguration"
- "v28@0:8q16B24"
- "{AcwgM1MsgStruct={vector<unsigned short, std::allocator<unsigned short>>=^S^S{__compressed_pair<unsigned short *, std::allocator<unsigned short>>=^S}}{vector<unsigned char, std::allocator<unsigned char>>=**{__compressed_pair<unsigned char *, std::allocator<unsigned char>>=*}}CICS}16@0:8"
- "{vector<UWBSessionInterruptionBookkeeping, std::allocator<UWBSessionInterruptionBookkeeping>>=\"__begin_\"^{UWBSessionInterruptionBookkeeping}\"__end_\"^{UWBSessionInterruptionBookkeeping}\"__end_cap_\"{__compressed_pair<UWBSessionInterruptionBookkeeping *, std::allocator<UWBSessionInterruptionBookkeeping>>=\"__value_\"^{UWBSessionInterruptionBookkeeping}}}"

```
