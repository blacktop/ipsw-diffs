## PowerlogLiteOperators

> `/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`

```diff

 2964.2.4.0.0
-  __TEXT.__text: 0x51907c
-  __TEXT.__auth_stubs: 0x2d80
-  __TEXT.__objc_methlist: 0x3022c
+  __TEXT.__text: 0x521a88
+  __TEXT.__auth_stubs: 0x2da0
+  __TEXT.__objc_methlist: 0x30624
   __TEXT.__const: 0x1ef8
   __TEXT.__swift5_typeref: 0x4ce
   __TEXT.__constg_swiftt: 0x364
   __TEXT.__swift5_reflstr: 0x2be
   __TEXT.__swift5_fieldmd: 0x51c
-  __TEXT.__cstring: 0x849d1
+  __TEXT.__cstring: 0x853d8
   __TEXT.__swift5_proto: 0x108
   __TEXT.__swift5_types: 0x34
-  __TEXT.__oslogstring: 0x12599
+  __TEXT.__oslogstring: 0x126ca
   __TEXT.__swift5_capture: 0x4f4
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8

   __TEXT.__swift_as_ret: 0x58
   __TEXT.__gcc_except_tab: 0x2d50
   __TEXT.__ustring: 0x22
-  __TEXT.__unwind_info: 0x8178
+  __TEXT.__unwind_info: 0x8200
   __TEXT.__eh_frame: 0x10f0
-  __TEXT.__objc_classname: 0x2837
-  __TEXT.__objc_methname: 0x66f42
-  __TEXT.__objc_methtype: 0x832b
-  __TEXT.__objc_stubs: 0x35780
-  __DATA_CONST.__got: 0x1af0
-  __DATA_CONST.__const: 0xa708
-  __DATA_CONST.__objc_classlist: 0xa60
+  __TEXT.__objc_classname: 0x2872
+  __TEXT.__objc_methname: 0x670f1
+  __TEXT.__objc_methtype: 0x8354
+  __TEXT.__objc_stubs: 0x358a0
+  __DATA_CONST.__got: 0x1b00
+  __DATA_CONST.__const: 0xa810
+  __DATA_CONST.__objc_classlist: 0xa70
   __DATA_CONST.__objc_nlclslist: 0x258
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14f68
+  __DATA_CONST.__objc_selrefs: 0x14fc8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xb50
+  __DATA_CONST.__objc_superrefs: 0xb60
   __DATA_CONST.__objc_arraydata: 0x15f60
-  __AUTH_CONST.__auth_got: 0x16d8
+  __AUTH_CONST.__auth_got: 0x16e8
   __AUTH_CONST.__const: 0x2418
-  __AUTH_CONST.__cfstring: 0x745c0
-  __AUTH_CONST.__objc_const: 0x3a7f0
-  __AUTH_CONST.__objc_intobj: 0x7530
+  __AUTH_CONST.__cfstring: 0x75660
+  __AUTH_CONST.__objc_const: 0x3ac80
+  __AUTH_CONST.__objc_intobj: 0x7608
   __AUTH_CONST.__objc_arrayobj: 0x2d18
   __AUTH_CONST.__objc_dictobj: 0x4e70
   __AUTH_CONST.__objc_doubleobj: 0x1430
-  __AUTH.__objc_data: 0x2c08
+  __AUTH.__objc_data: 0x2ca8
   __AUTH.__data: 0x760
-  __DATA.__objc_ivar: 0x1f14
+  __DATA.__objc_ivar: 0x1f4c
   __DATA.__data: 0xef0
   __DATA.__common: 0x220
   __DATA.__bss: 0x1ff0

   - /System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices
   - /System/Library/PrivateFrameworks/BatteryIntelligence.framework/BatteryIntelligence
   - /System/Library/PrivateFrameworks/CPMS.framework/CPMS
+  - /System/Library/PrivateFrameworks/Centauri.framework/Centauri
   - /System/Library/PrivateFrameworks/CloudKitCode.framework/CloudKitCode
   - /System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures
   - /System/Library/PrivateFrameworks/ComputeSafeguards.framework/ComputeSafeguards

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 5DF5BDCF-1BE0-36C2-BE45-FFE67F4000BB
-  Functions: 20381
-  Symbols:   55008
-  CStrings:  52716
+  UUID: 42414077-238D-37AE-929A-3D3D3945794D
+  Functions: 20469
+  Symbols:   55222
+  CStrings:  53006
 
Symbols:
+ +[AWDMETRICSCellularPowerLog cellularRfTunerHistType]
+ +[AWDMETRICSCellularRfTunerHist tunerStateDurationType]
+ +[PLBluetoothAgent entryEventBackwardDefinitionEnhancedPowerStatsPerCore]
+ +[PLWifiAgent entryEventBackwardDefinitionControlCPUPowerStats]
+ -[AWDMETRICSCellularPowerLog addCellularRfTunerHist:]
+ -[AWDMETRICSCellularPowerLog cellularRfTunerHistAtIndex:]
+ -[AWDMETRICSCellularPowerLog cellularRfTunerHistsCount]
+ -[AWDMETRICSCellularPowerLog cellularRfTunerHists]
+ -[AWDMETRICSCellularPowerLog clearCellularRfTunerHists]
+ -[AWDMETRICSCellularPowerLog setCellularRfTunerHists:]
+ -[AWDMETRICSCellularRfTunerHist .cxx_destruct]
+ -[AWDMETRICSCellularRfTunerHist addTunerStateDuration:]
+ -[AWDMETRICSCellularRfTunerHist clearTunerStateDurations]
+ -[AWDMETRICSCellularRfTunerHist copyTo:]
+ -[AWDMETRICSCellularRfTunerHist copyWithZone:]
+ -[AWDMETRICSCellularRfTunerHist description]
+ -[AWDMETRICSCellularRfTunerHist dictionaryRepresentation]
+ -[AWDMETRICSCellularRfTunerHist ftQualInd]
+ -[AWDMETRICSCellularRfTunerHist hasFtQualInd]
+ -[AWDMETRICSCellularRfTunerHist hasSubsId]
+ -[AWDMETRICSCellularRfTunerHist hasTimestamp]
+ -[AWDMETRICSCellularRfTunerHist hash]
+ -[AWDMETRICSCellularRfTunerHist isEqual:]
+ -[AWDMETRICSCellularRfTunerHist mergeFrom:]
+ -[AWDMETRICSCellularRfTunerHist readFrom:]
+ -[AWDMETRICSCellularRfTunerHist setFtQualInd:]
+ -[AWDMETRICSCellularRfTunerHist setHasFtQualInd:]
+ -[AWDMETRICSCellularRfTunerHist setHasSubsId:]
+ -[AWDMETRICSCellularRfTunerHist setHasTimestamp:]
+ -[AWDMETRICSCellularRfTunerHist setSubsId:]
+ -[AWDMETRICSCellularRfTunerHist setTimestamp:]
+ -[AWDMETRICSCellularRfTunerHist setTunerStateDurations:]
+ -[AWDMETRICSCellularRfTunerHist subsId]
+ -[AWDMETRICSCellularRfTunerHist timestamp]
+ -[AWDMETRICSCellularRfTunerHist tunerStateDurationAtIndex:]
+ -[AWDMETRICSCellularRfTunerHist tunerStateDurationsCount]
+ -[AWDMETRICSCellularRfTunerHist tunerStateDurations]
+ -[AWDMETRICSCellularRfTunerHist writeTo:]
+ -[AWDMETRICSTunerStateDuration StringAsRat:]
+ -[AWDMETRICSTunerStateDuration StringAsScenarioDecision:]
+ -[AWDMETRICSTunerStateDuration StringAsTxBand:]
+ -[AWDMETRICSTunerStateDuration copyTo:]
+ -[AWDMETRICSTunerStateDuration copyWithZone:]
+ -[AWDMETRICSTunerStateDuration description]
+ -[AWDMETRICSTunerStateDuration dictionaryRepresentation]
+ -[AWDMETRICSTunerStateDuration duration]
+ -[AWDMETRICSTunerStateDuration ftQualInd]
+ -[AWDMETRICSTunerStateDuration hasDuration]
+ -[AWDMETRICSTunerStateDuration hasFtQualInd]
+ -[AWDMETRICSTunerStateDuration hasPort]
+ -[AWDMETRICSTunerStateDuration hasRat]
+ -[AWDMETRICSTunerStateDuration hasScenarioDecision]
+ -[AWDMETRICSTunerStateDuration hasTxBand]
+ -[AWDMETRICSTunerStateDuration hasWorkMode]
+ -[AWDMETRICSTunerStateDuration hash]
+ -[AWDMETRICSTunerStateDuration isEqual:]
+ -[AWDMETRICSTunerStateDuration mergeFrom:]
+ -[AWDMETRICSTunerStateDuration port]
+ -[AWDMETRICSTunerStateDuration ratAsString:]
+ -[AWDMETRICSTunerStateDuration rat]
+ -[AWDMETRICSTunerStateDuration readFrom:]
+ -[AWDMETRICSTunerStateDuration scenarioDecisionAsString:]
+ -[AWDMETRICSTunerStateDuration scenarioDecision]
+ -[AWDMETRICSTunerStateDuration setDuration:]
+ -[AWDMETRICSTunerStateDuration setFtQualInd:]
+ -[AWDMETRICSTunerStateDuration setHasDuration:]
+ -[AWDMETRICSTunerStateDuration setHasFtQualInd:]
+ -[AWDMETRICSTunerStateDuration setHasPort:]
+ -[AWDMETRICSTunerStateDuration setHasRat:]
+ -[AWDMETRICSTunerStateDuration setHasScenarioDecision:]
+ -[AWDMETRICSTunerStateDuration setHasTxBand:]
+ -[AWDMETRICSTunerStateDuration setHasWorkMode:]
+ -[AWDMETRICSTunerStateDuration setPort:]
+ -[AWDMETRICSTunerStateDuration setRat:]
+ -[AWDMETRICSTunerStateDuration setScenarioDecision:]
+ -[AWDMETRICSTunerStateDuration setTxBand:]
+ -[AWDMETRICSTunerStateDuration setWorkMode:]
+ -[AWDMETRICSTunerStateDuration txBandAsString:]
+ -[AWDMETRICSTunerStateDuration txBand]
+ -[AWDMETRICSTunerStateDuration workMode]
+ -[AWDMETRICSTunerStateDuration writeTo:]
+ -[PLBluetoothAgent logEventBackwardPowerStatsPerCore]
+ -[PLWifiAgent logEventBackwardControlCPUPowerStats]
+ GCC_except_table106
+ GCC_except_table144
+ GCC_except_table37
+ GCC_except_table47
+ OBJC_IVAR_$_AWDMETRICSCellularPowerLog._cellularRfTunerHists
+ OBJC_IVAR_$_AWDMETRICSCellularRfTunerHist._ftQualInd
+ OBJC_IVAR_$_AWDMETRICSCellularRfTunerHist._has
+ OBJC_IVAR_$_AWDMETRICSCellularRfTunerHist._subsId
+ OBJC_IVAR_$_AWDMETRICSCellularRfTunerHist._timestamp
+ OBJC_IVAR_$_AWDMETRICSCellularRfTunerHist._tunerStateDurations
+ OBJC_IVAR_$_AWDMETRICSTunerStateDuration._duration
+ OBJC_IVAR_$_AWDMETRICSTunerStateDuration._ftQualInd
+ OBJC_IVAR_$_AWDMETRICSTunerStateDuration._has
+ OBJC_IVAR_$_AWDMETRICSTunerStateDuration._port
+ OBJC_IVAR_$_AWDMETRICSTunerStateDuration._rat
+ OBJC_IVAR_$_AWDMETRICSTunerStateDuration._scenarioDecision
+ OBJC_IVAR_$_AWDMETRICSTunerStateDuration._txBand
+ OBJC_IVAR_$_AWDMETRICSTunerStateDuration._workMode
+ _AWDMETRICSCellularRfTunerHistReadFrom
+ _AWDMETRICSTunerStateDurationReadFrom
+ _BTLocalDeviceReadEnhancedPowerStatsPerCore
+ _CENGetPowerStats
+ _OBJC_CLASS_$_AWDMETRICSCellularRfTunerHist
+ _OBJC_CLASS_$_AWDMETRICSTunerStateDuration
+ _OBJC_METACLASS_$_AWDMETRICSCellularRfTunerHist
+ _OBJC_METACLASS_$_AWDMETRICSTunerStateDuration
+ __OBJC_$_CLASS_METHODS_AWDMETRICSCellularRfTunerHist
+ __OBJC_$_INSTANCE_METHODS_AWDMETRICSCellularRfTunerHist
+ __OBJC_$_INSTANCE_METHODS_AWDMETRICSTunerStateDuration
+ __OBJC_$_INSTANCE_VARIABLES_AWDMETRICSCellularRfTunerHist
+ __OBJC_$_INSTANCE_VARIABLES_AWDMETRICSTunerStateDuration
+ __OBJC_$_PROP_LIST_AWDMETRICSCellularRfTunerHist
+ __OBJC_$_PROP_LIST_AWDMETRICSTunerStateDuration
+ __OBJC_CLASS_PROTOCOLS_$_AWDMETRICSCellularRfTunerHist
+ __OBJC_CLASS_PROTOCOLS_$_AWDMETRICSTunerStateDuration
+ __OBJC_CLASS_RO_$_AWDMETRICSCellularRfTunerHist
+ __OBJC_CLASS_RO_$_AWDMETRICSTunerStateDuration
+ __OBJC_METACLASS_RO_$_AWDMETRICSCellularRfTunerHist
+ __OBJC_METACLASS_RO_$_AWDMETRICSTunerStateDuration
+ ___22-[PLBatteryAgent init]_block_invoke.3350
+ ___22-[PLBatteryAgent init]_block_invoke.3354
+ ___22-[PLBatteryAgent init]_block_invoke_2.3376
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5105
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5114
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5123
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5132
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5138
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5144
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5150
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5159
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5165
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5171
+ ___29-[PLWifiAgent findWifiDevice]_block_invoke.878
+ ___29-[PLWifiAgent findWifiDevice]_block_invoke.884
+ ___29-[PLWifiAgent findWifiDevice]_block_invoke.890
+ ___29-[PLWifiAgent findWifiDevice]_block_invoke.896
+ ___29-[PLWifiAgent findWifiDevice]_block_invoke.902
+ ___30-[PLWifiAgent modelWiFiPower:]_block_invoke.2685
+ ___30-[PLWifiAgent modelWiFiPower:]_block_invoke.2688
+ ___32-[PLBatteryAgent aggdTimerFired]_block_invoke.4792
+ ___32-[PLBatteryAgent getIOPSDevices]_block_invoke.3475
+ ___32-[PLBatteryAgent getIOPSDevices]_block_invoke.3481
+ ___33-[PLBatteryAgent cancelEALogging]_block_invoke.3466
+ ___33-[PLBatteryAgent setupCSMLogging]_block_invoke.5184
+ ___33-[PLBluetoothAgent attachSession]_block_invoke.711
+ ___33-[PLWifiAgent logEventPointWake:]_block_invoke.1021
+ ___33-[PLWifiAgent logEventPointWake:]_block_invoke.1027
+ ___33-[PLWifiAgent logEventPointWake:]_block_invoke.1066
+ ___33-[PLWifiAgent logEventPointWake:]_block_invoke.1082
+ ___33-[PLWifiAgent logEventPointWake:]_block_invoke.1094
+ ___33-[PLWifiAgent setWiFiAWDLDevice:]_block_invoke.866
+ ___36-[PLWifiAgent setWiFiHotspotDevice:]_block_invoke.857
+ ___36-[PLWifiAgent wifiManufacturerQuery]_block_invoke.2622
+ ___38-[PLBatteryAgent handleBDCAMALogging:]_block_invoke.3845
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.934
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.942
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.950
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.951
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.959
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.972
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke_2.935
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke_2.946
+ ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.1021
+ ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.1027
+ ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.1034
+ ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.1038
+ ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.1044
+ ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.1052
+ ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.1057
+ ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.1064
+ ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.1070
+ ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.1076
+ ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.1082
+ ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.1085
+ ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.1088
+ ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.1091
+ ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.1094
+ ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.1100
+ ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.1115
+ ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.1118
+ ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.1121
+ ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.1128
+ ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke_2.1058
+ ___40-[PLWifiAgent logEventForwardAWDLState:]_block_invoke.1289
+ ___40-[PLWifiAgent logEventForwardModuleInfo]_block_invoke.1248
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.4180
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.4187
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.4183
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.4190
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3553
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3559
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3575
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3608
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3668
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3685
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3696
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3700
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3708
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3715
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3724
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3730
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3737
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3744
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3758
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3763
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3770
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3794
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3836
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3560
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3605
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3620
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3692
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3709
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3719
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3727
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3738
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3745
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3802
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_3.3810
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_4.3818
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_5.3822
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_6.3826
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_7.3830
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5335
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5343
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke_2.5337
+ ___42-[PLBatteryAgent logEventIntervalGasGauge]_block_invoke.4051
+ ___42-[PLBluetoothAgent modelBluetoothOffPower]_block_invoke.1137
+ ___43-[PLWifiAgent logEventForwardHotspotState:]_block_invoke.1298
+ ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.548
+ ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.564
+ ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.573
+ ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.585
+ ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.597
+ ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.604
+ ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.616
+ ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.625
+ ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.634
+ ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.635
+ ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.664
+ ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.676
+ ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke_2.549
+ ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke_2.565
+ ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke_2.574
+ ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke_2.586
+ ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke_2.598
+ ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke_2.617
+ ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke_2.626
+ ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke_2.656
+ ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke_2.665
+ ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke_2.677
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5375
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5376
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5377
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5418
+ ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1343
+ ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1349
+ ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1357
+ ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1363
+ ___47-[PLBluetoothAgent sessionAttached:withResult:]_block_invoke.721
+ ___47-[PLBluetoothAgent sessionAttached:withResult:]_block_invoke.725
+ ___48-[PLBluetoothAgent logEventForwardPairedDevices]_block_invoke.765
+ ___48-[PLBluetoothAgent logEventForwardPairedDevices]_block_invoke.771
+ ___48-[PLBluetoothAgent logEventForwardPairedDevices]_block_invoke.777
+ ___49-[PLBluetoothAgent sessionTerminated:withResult:]_block_invoke.733
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5360
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5361
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5365
+ ___51-[PLWifiAgent logFromLinkChangeCallback:withStats:]_block_invoke.1005
+ ___52-[PLBluetoothAgent logEventIntervalConnectedDevices]_block_invoke.827
+ ___52-[PLBluetoothAgent logEventIntervalConnectedDevices]_block_invoke.838
+ ___52-[PLBluetoothAgent logEventIntervalConnectedDevices]_block_invoke.844
+ ___52-[PLBluetoothAgent logEventIntervalConnectedDevices]_block_invoke.850
+ ___52-[PLBluetoothAgent logEventIntervalConnectedDevices]_block_invoke.854
+ ___52-[PLBluetoothAgent logEventIntervalConnectedDevices]_block_invoke.860
+ ___53-[PLBluetoothAgent logEventBackwardPowerProfileStats]_block_invoke.869
+ ___53-[PLBluetoothAgent logEventBackwardPowerProfileStats]_block_invoke.873
+ ___53-[PLBluetoothAgent logEventBackwardPowerProfileStats]_block_invoke.876
+ ___53-[PLBluetoothAgent logEventBackwardPowerProfileStats]_block_invoke.882
+ ___53-[PLBluetoothAgent logEventBackwardPowerProfileStats]_block_invoke.886
+ ___53-[PLBluetoothAgent logEventBackwardPowerProfileStats]_block_invoke.890
+ ___53-[PLBluetoothAgent logEventBackwardPowerProfileStats]_block_invoke.896
+ ___53-[PLBluetoothAgent logEventBackwardPowerProfileStats]_block_invoke.897
+ ___53-[PLBluetoothAgent logEventBackwardPowerProfileStats]_block_invoke_2.887
+ ___53-[PLBluetoothAgent logEventBackwardPowerProfileStats]_block_invoke_2.898
+ ___53-[PLBluetoothAgent logEventBackwardPowerStatsPerCore]_block_invoke
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5048
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5052
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5057
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5061
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.5053
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.5058
+ ___55-[PLWifiAgent logEventPointWakePNO:withParams:toEntry:]_block_invoke.1200
+ ___55-[PLWifiAgent logEventPointWakePNO:withParams:toEntry:]_block_invoke.1209
+ ___56-[PLWifiAgent logEventPointWakeLink:withParams:toEntry:]_block_invoke.1236
+ ___59-[PLBatteryAgent setupEALoggingTriggeredByConnectionEvent:]_block_invoke.3446
+ ___61-[PLBluetoothAgent bluetoothDeviceEvent:onDevice:withResult:]_block_invoke.743
+ ___61-[PLBluetoothAgent bluetoothDeviceEvent:onDevice:withResult:]_block_invoke.749
+ ___61-[PLBluetoothAgent bluetoothDeviceEvent:onDevice:withResult:]_block_invoke.755
+ ___61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.1122
+ ___61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.1128
+ ___61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.1191
+ ___65-[PLBatteryAgent logEventBackwardHeatMapCallback:andHeatMapType:]_block_invoke.4443
+ ___67-[PLBluetoothAgent logEventIntervalLeConnectedDevices:withRequest:]_block_invoke.792
+ ___75-[PLBatteryAgent showOrHideTLCNotification:meetsTLCNotificationConditions:]_block_invoke.3418
+ ___78-[PLWifiAgent logFromWiFiNoAvailableCallback:withAvailability:withWakeParams:]_block_invoke.999
+ ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2505
+ ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2517
+ ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2526
+ ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2532
+ ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2538
+ ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2544
+ ___block_literal_global.3392
+ ___block_literal_global.3405
+ ___block_literal_global.3420
+ ___block_literal_global.3521
+ ___block_literal_global.3578
+ ___block_literal_global.3622
+ ___block_literal_global.3631
+ ___block_literal_global.3640
+ ___block_literal_global.3652
+ ___block_literal_global.3765
+ ___block_literal_global.3838
+ ___block_literal_global.3844
+ ___block_literal_global.3854
+ ___block_literal_global.4495
+ ___block_literal_global.4748
+ ___block_literal_global.4760
+ ___block_literal_global.4810
+ ___block_literal_global.5309
+ ___block_literal_global.5370
+ ___block_literal_global.961
+ _kPLBluetoothAgentEventBackwardEnhancedPowerStatsPerCore
+ _kPLWifiAgentEventBackwardNameControlCPUPowerStats
+ _objc_msgSend$addCellularRfTunerHist:
+ _objc_msgSend$cellularRfTunerHistAtIndex:
+ _objc_msgSend$cellularRfTunerHistsCount
+ _objc_msgSend$clearCellularRfTunerHists
+ _objc_msgSend$entryEventBackwardDefinitionControlCPUPowerStats
+ _objc_msgSend$entryEventBackwardDefinitionEnhancedPowerStatsPerCore
+ _objc_msgSend$isBasebandDale
+ _objc_msgSend$logEventBackwardControlCPUPowerStats
+ _objc_msgSend$logEventBackwardPowerStatsPerCore
- GCC_except_table105
- GCC_except_table141
- GCC_except_table36
- GCC_except_table46
- GCC_except_table79
- ___22-[PLBatteryAgent init]_block_invoke.3347
- ___22-[PLBatteryAgent init]_block_invoke.3351
- ___22-[PLBatteryAgent init]_block_invoke_2.3373
- ___24-[PLBatteryAgent xFlags]_block_invoke.5102
- ___24-[PLBatteryAgent xFlags]_block_invoke.5111
- ___24-[PLBatteryAgent xFlags]_block_invoke.5120
- ___24-[PLBatteryAgent xFlags]_block_invoke.5129
- ___24-[PLBatteryAgent xFlags]_block_invoke.5135
- ___24-[PLBatteryAgent xFlags]_block_invoke.5141
- ___24-[PLBatteryAgent xFlags]_block_invoke.5147
- ___24-[PLBatteryAgent xFlags]_block_invoke.5156
- ___24-[PLBatteryAgent xFlags]_block_invoke.5162
- ___24-[PLBatteryAgent xFlags]_block_invoke.5168
- ___29-[PLWifiAgent findWifiDevice]_block_invoke.776
- ___29-[PLWifiAgent findWifiDevice]_block_invoke.782
- ___29-[PLWifiAgent findWifiDevice]_block_invoke.788
- ___29-[PLWifiAgent findWifiDevice]_block_invoke.794
- ___29-[PLWifiAgent findWifiDevice]_block_invoke.800
- ___30-[PLWifiAgent modelWiFiPower:]_block_invoke.2577
- ___30-[PLWifiAgent modelWiFiPower:]_block_invoke.2580
- ___32-[PLBatteryAgent aggdTimerFired]_block_invoke.4789
- ___32-[PLBatteryAgent getIOPSDevices]_block_invoke.3472
- ___32-[PLBatteryAgent getIOPSDevices]_block_invoke.3478
- ___33-[PLBatteryAgent cancelEALogging]_block_invoke.3463
- ___33-[PLBatteryAgent setupCSMLogging]_block_invoke.5181
- ___33-[PLBluetoothAgent attachSession]_block_invoke.582
- ___33-[PLWifiAgent logEventPointWake:]_block_invoke.919
- ___33-[PLWifiAgent logEventPointWake:]_block_invoke.925
- ___33-[PLWifiAgent logEventPointWake:]_block_invoke.964
- ___33-[PLWifiAgent logEventPointWake:]_block_invoke.980
- ___33-[PLWifiAgent logEventPointWake:]_block_invoke.992
- ___33-[PLWifiAgent setWiFiAWDLDevice:]_block_invoke.764
- ___36-[PLWifiAgent setWiFiHotspotDevice:]_block_invoke.755
- ___36-[PLWifiAgent wifiManufacturerQuery]_block_invoke.2511
- ___38-[PLBatteryAgent handleBDCAMALogging:]_block_invoke.3842
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.832
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.840
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.848
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.849
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.857
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.870
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke_2.833
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke_2.844
- ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.889
- ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.895
- ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.902
- ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.906
- ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.912
- ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.920
- ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.925
- ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.932
- ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.938
- ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.944
- ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.950
- ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.953
- ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.956
- ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.959
- ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.962
- ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.968
- ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.983
- ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.986
- ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.989
- ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke.996
- ___40-[PLBluetoothAgent modelBluetoothPower:]_block_invoke_2.926
- ___40-[PLWifiAgent logEventForwardAWDLState:]_block_invoke.1178
- ___40-[PLWifiAgent logEventForwardModuleInfo]_block_invoke.1146
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.4177
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.4184
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.4180
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.4187
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3550
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3556
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3572
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3605
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3665
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3682
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3693
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3697
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3705
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3712
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3721
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3727
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3734
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3741
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3755
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3760
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3767
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3791
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3833
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3557
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3602
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3617
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3689
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3706
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3716
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3724
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3735
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3742
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3799
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_3.3807
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_4.3815
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_5.3819
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_6.3823
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_7.3827
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5332
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5340
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke_2.5334
- ___42-[PLBatteryAgent logEventIntervalGasGauge]_block_invoke.4048
- ___42-[PLBluetoothAgent modelBluetoothOffPower]_block_invoke.1005
- ___43-[PLWifiAgent logEventForwardHotspotState:]_block_invoke.1187
- ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.419
- ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.435
- ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.444
- ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.456
- ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.468
- ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.475
- ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.487
- ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.496
- ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.505
- ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.506
- ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.535
- ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.547
- ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke_2.420
- ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke_2.436
- ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke_2.445
- ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke_2.457
- ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke_2.469
- ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke_2.488
- ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke_2.497
- ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke_2.527
- ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke_2.536
- ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke_2.548
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5368
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5369
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5370
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5415
- ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1232
- ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1238
- ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1246
- ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1252
- ___47-[PLBluetoothAgent sessionAttached:withResult:]_block_invoke.592
- ___47-[PLBluetoothAgent sessionAttached:withResult:]_block_invoke.596
- ___48-[PLBluetoothAgent logEventForwardPairedDevices]_block_invoke.636
- ___48-[PLBluetoothAgent logEventForwardPairedDevices]_block_invoke.642
- ___48-[PLBluetoothAgent logEventForwardPairedDevices]_block_invoke.648
- ___49-[PLBluetoothAgent sessionTerminated:withResult:]_block_invoke.604
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5357
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5358
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5362
- ___51-[PLWifiAgent logFromLinkChangeCallback:withStats:]_block_invoke.903
- ___52-[PLBluetoothAgent logEventIntervalConnectedDevices]_block_invoke.698
- ___52-[PLBluetoothAgent logEventIntervalConnectedDevices]_block_invoke.709
- ___52-[PLBluetoothAgent logEventIntervalConnectedDevices]_block_invoke.715
- ___52-[PLBluetoothAgent logEventIntervalConnectedDevices]_block_invoke.721
- ___52-[PLBluetoothAgent logEventIntervalConnectedDevices]_block_invoke.725
- ___52-[PLBluetoothAgent logEventIntervalConnectedDevices]_block_invoke.731
- ___53-[PLBluetoothAgent logEventBackwardPowerProfileStats]_block_invoke.740
- ___53-[PLBluetoothAgent logEventBackwardPowerProfileStats]_block_invoke.744
- ___53-[PLBluetoothAgent logEventBackwardPowerProfileStats]_block_invoke.747
- ___53-[PLBluetoothAgent logEventBackwardPowerProfileStats]_block_invoke.753
- ___53-[PLBluetoothAgent logEventBackwardPowerProfileStats]_block_invoke.757
- ___53-[PLBluetoothAgent logEventBackwardPowerProfileStats]_block_invoke.761
- ___53-[PLBluetoothAgent logEventBackwardPowerProfileStats]_block_invoke.767
- ___53-[PLBluetoothAgent logEventBackwardPowerProfileStats]_block_invoke.768
- ___53-[PLBluetoothAgent logEventBackwardPowerProfileStats]_block_invoke_2.758
- ___53-[PLBluetoothAgent logEventBackwardPowerProfileStats]_block_invoke_2.769
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5045
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5049
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5054
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5058
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.5050
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.5055
- ___55-[PLWifiAgent logEventPointWakePNO:withParams:toEntry:]_block_invoke.1098
- ___55-[PLWifiAgent logEventPointWakePNO:withParams:toEntry:]_block_invoke.1107
- ___56-[PLWifiAgent logEventPointWakeLink:withParams:toEntry:]_block_invoke.1134
- ___59-[PLBatteryAgent setupEALoggingTriggeredByConnectionEvent:]_block_invoke.3443
- ___61-[PLBluetoothAgent bluetoothDeviceEvent:onDevice:withResult:]_block_invoke.614
- ___61-[PLBluetoothAgent bluetoothDeviceEvent:onDevice:withResult:]_block_invoke.620
- ___61-[PLBluetoothAgent bluetoothDeviceEvent:onDevice:withResult:]_block_invoke.626
- ___61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.1020
- ___61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.1026
- ___61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.1089
- ___65-[PLBatteryAgent logEventBackwardHeatMapCallback:andHeatMapType:]_block_invoke.4440
- ___67-[PLBluetoothAgent logEventIntervalLeConnectedDevices:withRequest:]_block_invoke.663
- ___75-[PLBatteryAgent showOrHideTLCNotification:meetsTLCNotificationConditions:]_block_invoke.3415
- ___78-[PLWifiAgent logFromWiFiNoAvailableCallback:withAvailability:withWakeParams:]_block_invoke.897
- ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2394
- ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2406
- ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2415
- ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2421
- ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2427
- ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2433
- ___block_literal_global.3389
- ___block_literal_global.3402
- ___block_literal_global.3417
- ___block_literal_global.3518
- ___block_literal_global.3575
- ___block_literal_global.3619
- ___block_literal_global.3628
- ___block_literal_global.3637
- ___block_literal_global.3649
- ___block_literal_global.3762
- ___block_literal_global.3835
- ___block_literal_global.3841
- ___block_literal_global.3851
- ___block_literal_global.4492
- ___block_literal_global.4745
- ___block_literal_global.4757
- ___block_literal_global.4807
- ___block_literal_global.5306
- ___block_literal_global.5367
- ___block_literal_global.859
CStrings:
+ "1452-5026"
+ "AT"
+ "AWDMETRICSCellularRfTunerHist"
+ "AWDMETRICSTunerStateDuration"
+ "AwakeCount"
+ "AwakeDuration"
+ "AwakeL3Count"
+ "AwakeL3Duration"
+ "BTMainIdleDuration"
+ "BTPHY2GIdleDuration"
+ "BTPHY5GIdleDuration"
+ "BTScanIdleDuration"
+ "BTSecondaryIdleDuration"
+ "CCCI"
+ "CCPUIdleDuration"
+ "Call to fetch Control CPU stats was successful."
+ "ControlCPUPowerStats"
+ "DeepSleepCount"
+ "ERROR: could not read enhanced power statistics per core (error: %u)"
+ "EnhancedPowerStatsPerCore"
+ "Error: Call to fetch Control CPU stats failed."
+ "Getting Enhanced BT stats per core"
+ "IDLE_MODE_SCENARIO"
+ "IQ"
+ "MCU"
+ "MD"
+ "MIPC"
+ "MUMTAS"
+ "MainCoreElnaOffPercentage"
+ "MainCoreElnaOnPercentage"
+ "MainCoreEpaTxPercentage"
+ "MainCoreEpaTxbfTxPercentage"
+ "MainCoreIpaTxPercentage"
+ "MainCoreM154ReceivePercentage"
+ "MainCoreM154TransmitPercentage"
+ "MainCoreMrcRxPercentage"
+ "MainCoreOtherPower"
+ "MainCoreRXPower"
+ "MainCoreRxScanPercentage"
+ "MainCoreSleepPower"
+ "MainCoreTXPower"
+ "MainCoreTxbfTxPercentage"
+ "NVRAM"
+ "PASSTHROUGH"
+ "PCIeL0Duration"
+ "PCIeL0EntryCount"
+ "PCIeL1Dot1Duration"
+ "PCIeL1Dot1EntryCount"
+ "PCIeL1Dot2Duration"
+ "PCIeL1Dot2EntryCount"
+ "PCIeL1Duration"
+ "PCIeL1EntryCount"
+ "PCIeL3Duration"
+ "PCIeL3EntryCount"
+ "SYS_BAND_BC0"
+ "SYS_BAND_BC1"
+ "SYS_BAND_BC10"
+ "SYS_BAND_BC11"
+ "SYS_BAND_BC12"
+ "SYS_BAND_BC13"
+ "SYS_BAND_BC14"
+ "SYS_BAND_BC15"
+ "SYS_BAND_BC16"
+ "SYS_BAND_BC17"
+ "SYS_BAND_BC18"
+ "SYS_BAND_BC19"
+ "SYS_BAND_BC3"
+ "SYS_BAND_BC4"
+ "SYS_BAND_BC5"
+ "SYS_BAND_BC6"
+ "SYS_BAND_BC7"
+ "SYS_BAND_BC8"
+ "SYS_BAND_BC9"
+ "SYS_BAND_LTE_EUTRAN_BAND125"
+ "SYS_BAND_LTE_EUTRAN_BAND126"
+ "SYS_BAND_LTE_EUTRAN_BAND127"
+ "SYS_BAND_LTE_EUTRAN_BAND250"
+ "SYS_BAND_LTE_EUTRAN_BAND252"
+ "SYS_BAND_LTE_EUTRAN_BAND255"
+ "SYS_BAND_LTE_EUTRAN_BAND32"
+ "SYS_BAND_LTE_EUTRAN_BAND47"
+ "SYS_BAND_RESERVED_1"
+ "SYS_BAND_UMTS_BAND1"
+ "SYS_BAND_UMTS_BAND2"
+ "SYS_BAND_UMTS_BAND3"
+ "SYS_BAND_UMTS_BAND4"
+ "SYS_BAND_UMTS_BAND5"
+ "SYS_BAND_UMTS_BAND6"
+ "SYS_MODE_CDMA_HDR"
+ "SYS_MODE_NR5G"
+ "SYS_MODE_SUSPENDED"
+ "ScanCoreElnaOffPercentage"
+ "ScanCoreElnaOnPercentage"
+ "ScanCoreEpaTxPercentage"
+ "ScanCoreEpaTxbfTxPercentage"
+ "ScanCoreIpaTxPercentage"
+ "ScanCoreM154ReceivePercentage"
+ "ScanCoreM154TransmitPercentage"
+ "ScanCoreMrcRxPercentage"
+ "ScanCoreOtherPower"
+ "ScanCoreRXPower"
+ "ScanCoreRxScanPercentage"
+ "ScanCoreSleepPower"
+ "ScanCoreTXPower"
+ "ScanCoreTxbfTxPercentage"
+ "SecondaryCoreElnaOffPercentage"
+ "SecondaryCoreElnaOnPercentage"
+ "SecondaryCoreEpaTxPercentage"
+ "SecondaryCoreEpaTxbfTxPercentage"
+ "SecondaryCoreIpaTxPercentage"
+ "SecondaryCoreM154ReceivePercentage"
+ "SecondaryCoreM154TransmitPercentage"
+ "SecondaryCoreMrcRxPercentage"
+ "SecondaryCoreOtherPower"
+ "SecondaryCoreRXPower"
+ "SecondaryCoreRxScanPercentage"
+ "SecondaryCoreSleepPower"
+ "SecondaryCoreTXPower"
+ "SecondaryCoreTxbfTxPercentage"
+ "T@\"NSMutableArray\",&,N,V_cellularRfTunerHists"
+ "V=u"
+ "WarmSleepCount"
+ "WarmSleepDuration"
+ "WiFi Chipset is an empty string."
+ "WiFi Chipset: %@"
+ "WiFiLMAC2GIdleDuration"
+ "WiFiLMAC5GIdleDuration"
+ "WiFiLMACCommonIdleDuration"
+ "WiFiPHY2GIdleDuration"
+ "WiFiPHY5GIdleDuration"
+ "WiFiRXIdleDuration"
+ "WiFiScanIdleDuration"
+ "WiFiTXIdleDuration"
+ "WiFiUMACIdleDuration"
+ "WifiChipset"
+ "_cellularRfTunerHists"
+ "addCellularRfTunerHist:"
+ "cellularRfTunerHist"
+ "cellularRfTunerHistAtIndex:"
+ "cellularRfTunerHistType"
+ "cellularRfTunerHists"
+ "cellularRfTunerHistsCount"
+ "clearCellularRfTunerHists"
+ "entryEventBackwardDefinitionControlCPUPowerStats"
+ "entryEventBackwardDefinitionEnhancedPowerStatsPerCore"
+ "isBasebandDale"
+ "kKeyMIPCClientID"
+ "kKeyMIPCLength"
+ "kKeyMIPCMsgID"
+ "kKeyMIPCMsgStr"
+ "kKeyMIPCTrxID"
+ "logEventBackwardControlCPUPowerStats"
+ "logEventBackwardPowerStatsPerCore"
+ "setCellularRfTunerHists:"
+ "{?=\"timestamp\"b1\"ftQualInd\"b1\"subsId\"b1}"

```
