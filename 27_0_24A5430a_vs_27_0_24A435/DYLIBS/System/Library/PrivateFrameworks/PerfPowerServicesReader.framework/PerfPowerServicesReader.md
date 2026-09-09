## PerfPowerServicesReader

> `/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/PerfPowerServicesReader`

```diff

 3486.2.4.0.0
-  __TEXT.__text: 0x14b03c
+  __TEXT.__text: 0x15871c
   __TEXT.__init_offsets: 0xdc
-  __TEXT.__objc_methlist: 0x12d94
+  __TEXT.__objc_methlist: 0x13994
   __TEXT.__const: 0x5fd2
-  __TEXT.__cstring: 0xd0f4
+  __TEXT.__cstring: 0xe092
   __TEXT.__gcc_except_tab: 0x4adc
   __TEXT.__oslogstring: 0xda1
-  __TEXT.__unwind_info: 0x49b0
+  __TEXT.__unwind_info: 0x4b68
   __TEXT.__eh_frame: 0x98
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2a40
-  __DATA_CONST.__objc_classlist: 0x558
+  __DATA_CONST.__const: 0x2bd8
+  __DATA_CONST.__objc_classlist: 0x590
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x368
-  __DATA_CONST.__objc_selrefs: 0x5ea0
+  __DATA_CONST.__objc_selrefs: 0x60a8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x4d0
+  __DATA_CONST.__objc_superrefs: 0x508
   __DATA_CONST.__objc_arraydata: 0x110
-  __DATA_CONST.__got: 0x720
+  __DATA_CONST.__got: 0x758
   __AUTH_CONST.__const: 0x3090
-  __AUTH_CONST.__cfstring: 0xf0c0
-  __AUTH_CONST.__objc_const: 0x16c28
+  __AUTH_CONST.__cfstring: 0x10b80
+  __AUTH_CONST.__objc_const: 0x179e0
   __AUTH_CONST.__weak_auth_got: 0xb0
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x6e0
-  __AUTH.__objc_data: 0x29e0
+  __AUTH.__objc_data: 0x2c10
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x1118
+  __DATA.__objc_ivar: 0x11b0
   __DATA.__data: 0x521
   __DATA_DIRTY.__objc_data: 0xb90
   __DATA_DIRTY.__data: 0xad8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 7905
-  Symbols:   12938
-  CStrings:  2144
+  Functions: 8164
+  Symbols:   13309
+  CStrings:  2358
 
Symbols:
+ +[AWDMETRICSKCellularPowerLogDcsPerfStates binType]
+ +[AWDMETRICSKCellularPowerLogNRAntennaElement antennaElementsType]
+ +[AWDMETRICSKCellularPowerLogNRmmWaveBeamID binType]
+ +[AWDMETRICSMetricLogPower kCellularPowerLogDcsPerfStatesType]
+ +[AWDMETRICSMetricLogPower kCellularPowerLogNRAntennaElementType]
+ +[AWDMETRICSMetricLogPower kCellularPowerLogNRDCEventType]
+ +[AWDMETRICSMetricLogPower kCellularPowerLogNRmmWaveBeamIDType]
+ -[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState StringAsMode:]
+ -[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState hasMode]
+ -[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState modeAsString:]
+ -[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState mode]
+ -[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState setHasMode:]
+ -[AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState setMode:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates .cxx_destruct]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates StringAsLastSdmState:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates addBin:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates binAtIndex:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates binsCount]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates bins]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates clearBins]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates copyTo:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates copyWithZone:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates description]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates dictionaryRepresentation]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates durationMs]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates hasDurationMs]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates hasLastSdmState]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates hasTimestamp]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates hash]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates isEqual:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates lastSdmStateAsString:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates lastSdmState]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates mergeFrom:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates readFrom:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates setBins:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates setDurationMs:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates setHasDurationMs:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates setHasLastSdmState:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates setHasTimestamp:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates setLastSdmState:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates setTimestamp:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates timestamp]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStates writeTo:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStatesMBin StringAsBinId:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStatesMBin binIdAsString:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStatesMBin binId]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStatesMBin copyTo:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStatesMBin copyWithZone:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStatesMBin count]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStatesMBin description]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStatesMBin dictionaryRepresentation]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStatesMBin duration]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStatesMBin hasBinId]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStatesMBin hasCount]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStatesMBin hasDuration]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStatesMBin hash]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStatesMBin isEqual:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStatesMBin mergeFrom:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStatesMBin readFrom:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStatesMBin setBinId:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStatesMBin setCount:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStatesMBin setDuration:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStatesMBin setHasBinId:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStatesMBin setHasCount:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStatesMBin setHasDuration:]
+ -[AWDMETRICSKCellularPowerLogDcsPerfStatesMBin writeTo:]
+ -[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin StringAsCellGroup:]
+ -[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin StringAsDeployment:]
+ -[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin appliedDrxdMs]
+ -[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin cellGroupAsString:]
+ -[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin cellGroup]
+ -[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin deploymentAsString:]
+ -[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin deployment]
+ -[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin hasAppliedDrxdMs]
+ -[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin hasCellGroup]
+ -[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin hasDeployment]
+ -[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setAppliedDrxdMs:]
+ -[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setCellGroup:]
+ -[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setDeployment:]
+ -[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setHasAppliedDrxdMs:]
+ -[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setHasCellGroup:]
+ -[AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin setHasDeployment:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement .cxx_destruct]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement addAntennaElements:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement antennaElementsAtIndex:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement antennaElementsCount]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement antennaElements]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement clearAntennaElements]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement copyTo:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement copyWithZone:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement description]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement dictionaryRepresentation]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement hasSubsId]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement hasTimestamp]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement hasTotalDurationMs]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement hash]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement isEqual:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement mergeFrom:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement readFrom:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement setAntennaElements:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement setHasSubsId:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement setHasTimestamp:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement setHasTotalDurationMs:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement setSubsId:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement setTimestamp:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement setTotalDurationMs:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement subsId]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement timestamp]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement totalDurationMs]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElement writeTo:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement StringAsDirection:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement StringAsElements:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement binDurationMs]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement copyTo:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement copyWithZone:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement description]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement dictionaryRepresentation]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement directionAsString:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement direction]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement elementsAsString:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement elements]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement hasBinDurationMs]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement hasDirection]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement hasElements]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement hash]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement isEqual:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement mergeFrom:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement readFrom:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement setBinDurationMs:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement setDirection:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement setElements:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement setHasBinDurationMs:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement setHasDirection:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement setHasElements:]
+ -[AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement writeTo:]
+ -[AWDMETRICSKCellularPowerLogNRDCEvent StringAsEvent:]
+ -[AWDMETRICSKCellularPowerLogNRDCEvent copyTo:]
+ -[AWDMETRICSKCellularPowerLogNRDCEvent copyWithZone:]
+ -[AWDMETRICSKCellularPowerLogNRDCEvent description]
+ -[AWDMETRICSKCellularPowerLogNRDCEvent dictionaryRepresentation]
+ -[AWDMETRICSKCellularPowerLogNRDCEvent eventAsString:]
+ -[AWDMETRICSKCellularPowerLogNRDCEvent event]
+ -[AWDMETRICSKCellularPowerLogNRDCEvent hasEvent]
+ -[AWDMETRICSKCellularPowerLogNRDCEvent hasSubsId]
+ -[AWDMETRICSKCellularPowerLogNRDCEvent hasTimestamp]
+ -[AWDMETRICSKCellularPowerLogNRDCEvent hash]
+ -[AWDMETRICSKCellularPowerLogNRDCEvent isEqual:]
+ -[AWDMETRICSKCellularPowerLogNRDCEvent mergeFrom:]
+ -[AWDMETRICSKCellularPowerLogNRDCEvent readFrom:]
+ -[AWDMETRICSKCellularPowerLogNRDCEvent setEvent:]
+ -[AWDMETRICSKCellularPowerLogNRDCEvent setHasEvent:]
+ -[AWDMETRICSKCellularPowerLogNRDCEvent setHasSubsId:]
+ -[AWDMETRICSKCellularPowerLogNRDCEvent setHasTimestamp:]
+ -[AWDMETRICSKCellularPowerLogNRDCEvent setSubsId:]
+ -[AWDMETRICSKCellularPowerLogNRDCEvent setTimestamp:]
+ -[AWDMETRICSKCellularPowerLogNRDCEvent subsId]
+ -[AWDMETRICSKCellularPowerLogNRDCEvent timestamp]
+ -[AWDMETRICSKCellularPowerLogNRDCEvent writeTo:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID .cxx_destruct]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID addBin:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID binAtIndex:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID binsCount]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID bins]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID clearBins]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID copyTo:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID copyWithZone:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID description]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID dictionaryRepresentation]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID durationMs]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID hasDurationMs]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID hasSubsId]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID hasTimestamp]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID hash]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID isEqual:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID mergeFrom:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID readFrom:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID setBins:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID setDurationMs:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID setHasDurationMs:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID setHasSubsId:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID setHasTimestamp:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID setSubsId:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID setTimestamp:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID subsId]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID timestamp]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamID writeTo:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin StringAsBinId:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin binIdAsString:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin binId]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin copyTo:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin copyWithZone:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin description]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin dictionaryRepresentation]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin duration]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin hasBinId]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin hasDuration]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin hash]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin isEqual:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin mergeFrom:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin readFrom:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin setBinId:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin setDuration:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin setHasBinId:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin setHasDuration:]
+ -[AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin writeTo:]
+ -[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin areScellsScheduled]
+ -[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin hasAreScellsScheduled]
+ -[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin hasIsSpcellScheduled]
+ -[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin hasScheduledScellCount]
+ -[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin isSpcellScheduled]
+ -[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin scheduledScellCount]
+ -[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin setAreScellsScheduled:]
+ -[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin setHasAreScellsScheduled:]
+ -[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin setHasIsSpcellScheduled:]
+ -[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin setHasScheduledScellCount:]
+ -[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin setIsSpcellScheduled:]
+ -[AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin setScheduledScellCount:]
+ -[AWDMETRICSKCellularRfTunerHistTunerStateDuration StringAsDeviceMode:]
+ -[AWDMETRICSKCellularRfTunerHistTunerStateDuration deviceModeAsString:]
+ -[AWDMETRICSKCellularRfTunerHistTunerStateDuration deviceMode]
+ -[AWDMETRICSKCellularRfTunerHistTunerStateDuration hasDeviceMode]
+ -[AWDMETRICSKCellularRfTunerHistTunerStateDuration setDeviceMode:]
+ -[AWDMETRICSKCellularRfTunerHistTunerStateDuration setHasDeviceMode:]
+ -[AWDMETRICSMetricLogPower addKCellularPowerLogDcsPerfStates:]
+ -[AWDMETRICSMetricLogPower addKCellularPowerLogNRAntennaElement:]
+ -[AWDMETRICSMetricLogPower addKCellularPowerLogNRDCEvent:]
+ -[AWDMETRICSMetricLogPower addKCellularPowerLogNRmmWaveBeamID:]
+ -[AWDMETRICSMetricLogPower clearKCellularPowerLogDcsPerfStates]
+ -[AWDMETRICSMetricLogPower clearKCellularPowerLogNRAntennaElements]
+ -[AWDMETRICSMetricLogPower clearKCellularPowerLogNRDCEvents]
+ -[AWDMETRICSMetricLogPower clearKCellularPowerLogNRmmWaveBeamIDs]
+ -[AWDMETRICSMetricLogPower kCellularPowerLogDcsPerfStatesAtIndex:]
+ -[AWDMETRICSMetricLogPower kCellularPowerLogDcsPerfStatesCount]
+ -[AWDMETRICSMetricLogPower kCellularPowerLogDcsPerfStates]
+ -[AWDMETRICSMetricLogPower kCellularPowerLogNRAntennaElementAtIndex:]
+ -[AWDMETRICSMetricLogPower kCellularPowerLogNRAntennaElementsCount]
+ -[AWDMETRICSMetricLogPower kCellularPowerLogNRAntennaElements]
+ -[AWDMETRICSMetricLogPower kCellularPowerLogNRDCEventAtIndex:]
+ -[AWDMETRICSMetricLogPower kCellularPowerLogNRDCEventsCount]
+ -[AWDMETRICSMetricLogPower kCellularPowerLogNRDCEvents]
+ -[AWDMETRICSMetricLogPower kCellularPowerLogNRmmWaveBeamIDAtIndex:]
+ -[AWDMETRICSMetricLogPower kCellularPowerLogNRmmWaveBeamIDsCount]
+ -[AWDMETRICSMetricLogPower kCellularPowerLogNRmmWaveBeamIDs]
+ -[AWDMETRICSMetricLogPower setKCellularPowerLogDcsPerfStates:]
+ -[AWDMETRICSMetricLogPower setKCellularPowerLogNRAntennaElements:]
+ -[AWDMETRICSMetricLogPower setKCellularPowerLogNRDCEvents:]
+ -[AWDMETRICSMetricLogPower setKCellularPowerLogNRmmWaveBeamIDs:]
+ OBJC_IVAR_$_AWDMETRICSKCellularPlatformApBbSleepStatsPlatformState._mode
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogDcsPerfStates._bins
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogDcsPerfStates._durationMs
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogDcsPerfStates._has
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogDcsPerfStates._lastSdmState
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogDcsPerfStates._timestamp
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogDcsPerfStatesMBin._binId
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogDcsPerfStatesMBin._count
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogDcsPerfStatesMBin._duration
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogDcsPerfStatesMBin._has
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin._appliedDrxdMs
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin._cellGroup
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogLteNrRxDiversityHistRxdBin._deployment
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogNRAntennaElement._antennaElements
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogNRAntennaElement._has
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogNRAntennaElement._subsId
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogNRAntennaElement._timestamp
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogNRAntennaElement._totalDurationMs
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement._binDurationMs
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement._direction
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement._elements
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement._has
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogNRDCEvent._event
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogNRDCEvent._has
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogNRDCEvent._subsId
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogNRDCEvent._timestamp
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogNRmmWaveBeamID._bins
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogNRmmWaveBeamID._durationMs
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogNRmmWaveBeamID._has
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogNRmmWaveBeamID._subsId
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogNRmmWaveBeamID._timestamp
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin._binId
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin._duration
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin._has
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin._areScellsScheduled
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin._isSpcellScheduled
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogNrCaConfigActivateStatsMBin._scheduledScellCount
+ OBJC_IVAR_$_AWDMETRICSKCellularRfTunerHistTunerStateDuration._deviceMode
+ _AWDMETRICSKCellularPowerLogDcsPerfStatesMBinReadFrom
+ _AWDMETRICSKCellularPowerLogDcsPerfStatesReadFrom
+ _AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElementReadFrom
+ _AWDMETRICSKCellularPowerLogNRAntennaElementReadFrom
+ _AWDMETRICSKCellularPowerLogNRDCEventReadFrom
+ _AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBinReadFrom
+ _AWDMETRICSKCellularPowerLogNRmmWaveBeamIDReadFrom
+ _OBJC_CLASS_$_AWDMETRICSKCellularPowerLogDcsPerfStates
+ _OBJC_CLASS_$_AWDMETRICSKCellularPowerLogDcsPerfStatesMBin
+ _OBJC_CLASS_$_AWDMETRICSKCellularPowerLogNRAntennaElement
+ _OBJC_CLASS_$_AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement
+ _OBJC_CLASS_$_AWDMETRICSKCellularPowerLogNRDCEvent
+ _OBJC_CLASS_$_AWDMETRICSKCellularPowerLogNRmmWaveBeamID
+ _OBJC_CLASS_$_AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin
+ _OBJC_METACLASS_$_AWDMETRICSKCellularPowerLogDcsPerfStates
+ _OBJC_METACLASS_$_AWDMETRICSKCellularPowerLogDcsPerfStatesMBin
+ _OBJC_METACLASS_$_AWDMETRICSKCellularPowerLogNRAntennaElement
+ _OBJC_METACLASS_$_AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement
+ _OBJC_METACLASS_$_AWDMETRICSKCellularPowerLogNRDCEvent
+ _OBJC_METACLASS_$_AWDMETRICSKCellularPowerLogNRmmWaveBeamID
+ _OBJC_METACLASS_$_AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin
+ __OBJC_$_CLASS_METHODS_AWDMETRICSKCellularPowerLogDcsPerfStates
+ __OBJC_$_CLASS_METHODS_AWDMETRICSKCellularPowerLogNRAntennaElement
+ __OBJC_$_CLASS_METHODS_AWDMETRICSKCellularPowerLogNRmmWaveBeamID
+ __OBJC_$_INSTANCE_METHODS_AWDMETRICSKCellularPowerLogDcsPerfStates
+ __OBJC_$_INSTANCE_METHODS_AWDMETRICSKCellularPowerLogDcsPerfStatesMBin
+ __OBJC_$_INSTANCE_METHODS_AWDMETRICSKCellularPowerLogNRAntennaElement
+ __OBJC_$_INSTANCE_METHODS_AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement
+ __OBJC_$_INSTANCE_METHODS_AWDMETRICSKCellularPowerLogNRDCEvent
+ __OBJC_$_INSTANCE_METHODS_AWDMETRICSKCellularPowerLogNRmmWaveBeamID
+ __OBJC_$_INSTANCE_METHODS_AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin
+ __OBJC_$_INSTANCE_VARIABLES_AWDMETRICSKCellularPowerLogDcsPerfStates
+ __OBJC_$_INSTANCE_VARIABLES_AWDMETRICSKCellularPowerLogDcsPerfStatesMBin
+ __OBJC_$_INSTANCE_VARIABLES_AWDMETRICSKCellularPowerLogNRAntennaElement
+ __OBJC_$_INSTANCE_VARIABLES_AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement
+ __OBJC_$_INSTANCE_VARIABLES_AWDMETRICSKCellularPowerLogNRDCEvent
+ __OBJC_$_INSTANCE_VARIABLES_AWDMETRICSKCellularPowerLogNRmmWaveBeamID
+ __OBJC_$_INSTANCE_VARIABLES_AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin
+ __OBJC_$_PROP_LIST_AWDMETRICSKCellularPowerLogDcsPerfStates
+ __OBJC_$_PROP_LIST_AWDMETRICSKCellularPowerLogDcsPerfStatesMBin
+ __OBJC_$_PROP_LIST_AWDMETRICSKCellularPowerLogNRAntennaElement
+ __OBJC_$_PROP_LIST_AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement
+ __OBJC_$_PROP_LIST_AWDMETRICSKCellularPowerLogNRDCEvent
+ __OBJC_$_PROP_LIST_AWDMETRICSKCellularPowerLogNRmmWaveBeamID
+ __OBJC_$_PROP_LIST_AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin
+ __OBJC_CLASS_PROTOCOLS_$_AWDMETRICSKCellularPowerLogDcsPerfStates
+ __OBJC_CLASS_PROTOCOLS_$_AWDMETRICSKCellularPowerLogDcsPerfStatesMBin
+ __OBJC_CLASS_PROTOCOLS_$_AWDMETRICSKCellularPowerLogNRAntennaElement
+ __OBJC_CLASS_PROTOCOLS_$_AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement
+ __OBJC_CLASS_PROTOCOLS_$_AWDMETRICSKCellularPowerLogNRDCEvent
+ __OBJC_CLASS_PROTOCOLS_$_AWDMETRICSKCellularPowerLogNRmmWaveBeamID
+ __OBJC_CLASS_PROTOCOLS_$_AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin
+ __OBJC_CLASS_RO_$_AWDMETRICSKCellularPowerLogDcsPerfStates
+ __OBJC_CLASS_RO_$_AWDMETRICSKCellularPowerLogDcsPerfStatesMBin
+ __OBJC_CLASS_RO_$_AWDMETRICSKCellularPowerLogNRAntennaElement
+ __OBJC_CLASS_RO_$_AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement
+ __OBJC_CLASS_RO_$_AWDMETRICSKCellularPowerLogNRDCEvent
+ __OBJC_CLASS_RO_$_AWDMETRICSKCellularPowerLogNRmmWaveBeamID
+ __OBJC_CLASS_RO_$_AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin
+ __OBJC_METACLASS_RO_$_AWDMETRICSKCellularPowerLogDcsPerfStates
+ __OBJC_METACLASS_RO_$_AWDMETRICSKCellularPowerLogDcsPerfStatesMBin
+ __OBJC_METACLASS_RO_$_AWDMETRICSKCellularPowerLogNRAntennaElement
+ __OBJC_METACLASS_RO_$_AWDMETRICSKCellularPowerLogNRAntennaElementMNRAntennaElement
+ __OBJC_METACLASS_RO_$_AWDMETRICSKCellularPowerLogNRDCEvent
+ __OBJC_METACLASS_RO_$_AWDMETRICSKCellularPowerLogNRmmWaveBeamID
+ __OBJC_METACLASS_RO_$_AWDMETRICSKCellularPowerLogNRmmWaveBeamIDMBin
+ _objc_msgSend$addAntennaElements:
+ _objc_msgSend$addKCellularPowerLogDcsPerfStates:
+ _objc_msgSend$addKCellularPowerLogNRAntennaElement:
+ _objc_msgSend$addKCellularPowerLogNRDCEvent:
+ _objc_msgSend$addKCellularPowerLogNRmmWaveBeamID:
+ _objc_msgSend$antennaElementsAtIndex:
+ _objc_msgSend$antennaElementsCount
+ _objc_msgSend$clearAntennaElements
+ _objc_msgSend$clearKCellularPowerLogDcsPerfStates
+ _objc_msgSend$clearKCellularPowerLogNRAntennaElements
+ _objc_msgSend$clearKCellularPowerLogNRDCEvents
+ _objc_msgSend$clearKCellularPowerLogNRmmWaveBeamIDs
+ _objc_msgSend$kCellularPowerLogDcsPerfStatesAtIndex:
+ _objc_msgSend$kCellularPowerLogDcsPerfStatesCount
+ _objc_msgSend$kCellularPowerLogNRAntennaElementAtIndex:
+ _objc_msgSend$kCellularPowerLogNRAntennaElementsCount
+ _objc_msgSend$kCellularPowerLogNRDCEventAtIndex:
+ _objc_msgSend$kCellularPowerLogNRDCEventsCount
+ _objc_msgSend$kCellularPowerLogNRmmWaveBeamIDAtIndex:
+ _objc_msgSend$kCellularPowerLogNRmmWaveBeamIDsCount
CStrings:
+ "DCS_PERF_STATE0_BYPASS"
+ "DCS_PERF_STATE1_WARM_BOOT0"
+ "DCS_PERF_STATE2_WARM_BOOT1"
+ "DCS_PERF_STATE3_F0"
+ "DCS_PERF_STATE4_F1"
+ "DCS_PERF_STATE5_F2"
+ "DCS_PERF_STATE6_F3"
+ "DCS_PERF_STATE7_F4"
+ "DCS_PERF_STATE8_F5"
+ "DEPLOYMENT_NSA_FR2"
+ "DEVICE_MODE_A"
+ "DEVICE_MODE_B"
+ "DEVICE_MODE_NOT_YET_UPDATED"
+ "DEVICE_MODE_UNKNOWN"
+ "DPL_NR1_NRDC"
+ "DPL_NR2_ENDC"
+ "DPL_NR2_NRDC"
+ "E1P1"
+ "E1P2"
+ "E2P1"
+ "E2P2"
+ "E3P1"
+ "E3P2"
+ "E4P1"
+ "E4P2"
+ "E5P1"
+ "E5P2"
+ "ENDC_FR2"
+ "HOR_NR_BEAM_ID_1"
+ "HOR_NR_BEAM_ID_10"
+ "HOR_NR_BEAM_ID_11"
+ "HOR_NR_BEAM_ID_12"
+ "HOR_NR_BEAM_ID_13"
+ "HOR_NR_BEAM_ID_14"
+ "HOR_NR_BEAM_ID_15"
+ "HOR_NR_BEAM_ID_16"
+ "HOR_NR_BEAM_ID_17"
+ "HOR_NR_BEAM_ID_18"
+ "HOR_NR_BEAM_ID_19"
+ "HOR_NR_BEAM_ID_2"
+ "HOR_NR_BEAM_ID_20"
+ "HOR_NR_BEAM_ID_21"
+ "HOR_NR_BEAM_ID_22"
+ "HOR_NR_BEAM_ID_23"
+ "HOR_NR_BEAM_ID_24"
+ "HOR_NR_BEAM_ID_25"
+ "HOR_NR_BEAM_ID_26"
+ "HOR_NR_BEAM_ID_27"
+ "HOR_NR_BEAM_ID_28"
+ "HOR_NR_BEAM_ID_29"
+ "HOR_NR_BEAM_ID_3"
+ "HOR_NR_BEAM_ID_30"
+ "HOR_NR_BEAM_ID_31"
+ "HOR_NR_BEAM_ID_32"
+ "HOR_NR_BEAM_ID_33"
+ "HOR_NR_BEAM_ID_34"
+ "HOR_NR_BEAM_ID_35"
+ "HOR_NR_BEAM_ID_36"
+ "HOR_NR_BEAM_ID_37"
+ "HOR_NR_BEAM_ID_38"
+ "HOR_NR_BEAM_ID_39"
+ "HOR_NR_BEAM_ID_4"
+ "HOR_NR_BEAM_ID_40"
+ "HOR_NR_BEAM_ID_41"
+ "HOR_NR_BEAM_ID_42"
+ "HOR_NR_BEAM_ID_43"
+ "HOR_NR_BEAM_ID_44"
+ "HOR_NR_BEAM_ID_45"
+ "HOR_NR_BEAM_ID_46"
+ "HOR_NR_BEAM_ID_47"
+ "HOR_NR_BEAM_ID_48"
+ "HOR_NR_BEAM_ID_49"
+ "HOR_NR_BEAM_ID_5"
+ "HOR_NR_BEAM_ID_50"
+ "HOR_NR_BEAM_ID_51"
+ "HOR_NR_BEAM_ID_52"
+ "HOR_NR_BEAM_ID_53"
+ "HOR_NR_BEAM_ID_54"
+ "HOR_NR_BEAM_ID_55"
+ "HOR_NR_BEAM_ID_56"
+ "HOR_NR_BEAM_ID_57"
+ "HOR_NR_BEAM_ID_58"
+ "HOR_NR_BEAM_ID_59"
+ "HOR_NR_BEAM_ID_6"
+ "HOR_NR_BEAM_ID_60"
+ "HOR_NR_BEAM_ID_61"
+ "HOR_NR_BEAM_ID_62"
+ "HOR_NR_BEAM_ID_63"
+ "HOR_NR_BEAM_ID_64"
+ "HOR_NR_BEAM_ID_7"
+ "HOR_NR_BEAM_ID_8"
+ "HOR_NR_BEAM_ID_9"
+ "IDLE_SCENARIO"
+ "Invalid"
+ "LTE_ONLY"
+ "MCG"
+ "MODE_A"
+ "MODE_B"
+ "MODE_UNKNOWN"
+ "NO_RX_NO_TX_NO_DCI_DECODING"
+ "NO_RX_NO_TX_WITHOUT_DCI"
+ "NRRC_CAUSE_REEST_INVALID_CSI_BWP_REF_CONFIG"
+ "NRRC_CAUSE_REEST_INVALID_PUCCH_SYMBOL_CONFIG"
+ "NRRC_CAUSE_REEST_INVALID_SCELL_UL_CONFIG"
+ "NRRC_CAUSE_REEST_INVALID_SRS_AS_PATTERN_CONFIG"
+ "NRRC_CAUSE_REEST_INVALID_TAG_ASSIGNMENT_CONFIG"
+ "NRRC_CAUSE_REEST_INVALID_UL_PATHLOSS_VALUE"
+ "NRRC_CAUSE_REEST_L1_CONFIG_VALIDATION_FAILED"
+ "NRRC_CAUSE_REL_INVALID_CSI_BWP_REF_CONFIG"
+ "NRRC_CAUSE_REL_INVALID_PUCCH_SYMBOL_CONFIG"
+ "NRRC_CAUSE_REL_INVALID_SCELL_UL_CONFIG"
+ "NRRC_CAUSE_REL_INVALID_SRS_AS_PATTERN_CONFIG"
+ "NRRC_CAUSE_REL_INVALID_TAG_ASSIGNMENT_CONFIG"
+ "NRRC_CAUSE_REL_INVALID_UL_PATHLOSS_VALUE"
+ "NRRC_CAUSE_REL_L1_CONFIG_VALIDATION_FAILED"
+ "NRSA"
+ "NR_FR2"
+ "NR_MMWAVE_ENDC_CONNECTED"
+ "NR_MMWAVE_NRDC_CONNECTED"
+ "S1_MUTE"
+ "SCC9"
+ "SCENARIO_1_MODE_B"
+ "SCENARIO_2_MODE_B"
+ "SCENARIO_3_MODE_B"
+ "SCENARIO_4_MODE_B"
+ "SCENARIO_5_MODE_B"
+ "SCENARIO_6_MODE_B"
+ "SCENARIO_E85_MODE_B"
+ "SCENARIO_FREESPACE_MODE_B"
+ "SCENARIO_IDLE_MODE_B"
+ "SCENARIO_INVALID"
+ "SCENARIO_R5_MODE_B"
+ "SCG"
+ "SDM_TRIGGER_VONR"
+ "SOCSLP_SLP_OFL"
+ "SUB6_NRDC_MMW_ON"
+ "USLEEP_ALL"
+ "USLEEP_ANY"
+ "VDD_SOC_PERFSTATE_7"
+ "VER_NR_BEAM_ID_1"
+ "VER_NR_BEAM_ID_10"
+ "VER_NR_BEAM_ID_11"
+ "VER_NR_BEAM_ID_12"
+ "VER_NR_BEAM_ID_13"
+ "VER_NR_BEAM_ID_14"
+ "VER_NR_BEAM_ID_15"
+ "VER_NR_BEAM_ID_16"
+ "VER_NR_BEAM_ID_17"
+ "VER_NR_BEAM_ID_18"
+ "VER_NR_BEAM_ID_19"
+ "VER_NR_BEAM_ID_2"
+ "VER_NR_BEAM_ID_20"
+ "VER_NR_BEAM_ID_21"
+ "VER_NR_BEAM_ID_22"
+ "VER_NR_BEAM_ID_23"
+ "VER_NR_BEAM_ID_24"
+ "VER_NR_BEAM_ID_25"
+ "VER_NR_BEAM_ID_26"
+ "VER_NR_BEAM_ID_27"
+ "VER_NR_BEAM_ID_28"
+ "VER_NR_BEAM_ID_29"
+ "VER_NR_BEAM_ID_3"
+ "VER_NR_BEAM_ID_30"
+ "VER_NR_BEAM_ID_31"
+ "VER_NR_BEAM_ID_32"
+ "VER_NR_BEAM_ID_33"
+ "VER_NR_BEAM_ID_34"
+ "VER_NR_BEAM_ID_35"
+ "VER_NR_BEAM_ID_36"
+ "VER_NR_BEAM_ID_37"
+ "VER_NR_BEAM_ID_38"
+ "VER_NR_BEAM_ID_39"
+ "VER_NR_BEAM_ID_4"
+ "VER_NR_BEAM_ID_40"
+ "VER_NR_BEAM_ID_41"
+ "VER_NR_BEAM_ID_42"
+ "VER_NR_BEAM_ID_43"
+ "VER_NR_BEAM_ID_44"
+ "VER_NR_BEAM_ID_45"
+ "VER_NR_BEAM_ID_46"
+ "VER_NR_BEAM_ID_47"
+ "VER_NR_BEAM_ID_48"
+ "VER_NR_BEAM_ID_49"
+ "VER_NR_BEAM_ID_5"
+ "VER_NR_BEAM_ID_50"
+ "VER_NR_BEAM_ID_51"
+ "VER_NR_BEAM_ID_52"
+ "VER_NR_BEAM_ID_53"
+ "VER_NR_BEAM_ID_54"
+ "VER_NR_BEAM_ID_55"
+ "VER_NR_BEAM_ID_56"
+ "VER_NR_BEAM_ID_57"
+ "VER_NR_BEAM_ID_58"
+ "VER_NR_BEAM_ID_59"
+ "VER_NR_BEAM_ID_6"
+ "VER_NR_BEAM_ID_60"
+ "VER_NR_BEAM_ID_61"
+ "VER_NR_BEAM_ID_62"
+ "VER_NR_BEAM_ID_63"
+ "VER_NR_BEAM_ID_64"
+ "VER_NR_BEAM_ID_7"
+ "VER_NR_BEAM_ID_8"
+ "VER_NR_BEAM_ID_9"
+ "antenna_elements"
+ "applied_drxd_ms"
+ "bin_duration_ms"
+ "cell_group"
+ "device_mode"
+ "elements"
+ "kCellularPowerLogDcsPerfStates"
+ "kCellularPowerLogNRAntennaElement"
+ "kCellularPowerLogNRDCEvent"
+ "kCellularPowerLogNRmmWaveBeamID"
+ "total_duration_ms"
```
