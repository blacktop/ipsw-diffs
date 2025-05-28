## PerfPowerMetricMonitor

> `/System/Library/PrivateFrameworks/PerfPowerMetricMonitor.framework/PerfPowerMetricMonitor`

```diff

-1775.2.1.0.0
-  __TEXT.__text: 0x5000
-  __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__objc_methlist: 0x3c0
+1787.40.67.0.0
+  __TEXT.__text: 0x7f3c
+  __TEXT.__auth_stubs: 0x400
+  __TEXT.__objc_methlist: 0x878
   __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x254
-  __TEXT.__cstring: 0x507
-  __TEXT.__oslogstring: 0x4aa
-  __TEXT.__unwind_info: 0x214
-  __TEXT.__objc_classname: 0xd2
-  __TEXT.__objc_methname: 0xe5e
-  __TEXT.__objc_methtype: 0x3cc
-  __TEXT.__objc_stubs: 0xba0
+  __TEXT.__gcc_except_tab: 0x2d8
+  __TEXT.__cstring: 0xa06
+  __TEXT.__oslogstring: 0x59a
+  __TEXT.__ustring: 0x586
+  __TEXT.__unwind_info: 0x2a8
+  __TEXT.__objc_classname: 0x122
+  __TEXT.__objc_methname: 0x1b09
+  __TEXT.__objc_methtype: 0x43b
+  __TEXT.__objc_stubs: 0x1240
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x1f8
-  __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__const: 0x298
+  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9e0
-  __DATA_CONST.__objc_selrefs: 0x388
-  __AUTH_CONST.__cfstring: 0x180
-  __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__objc_const: 0x1b0
-  __AUTH_CONST.__auth_got: 0x1e0
-  __AUTH.__objc_data: 0xf0
+  __DATA_CONST.__objc_const: 0x1190
+  __DATA_CONST.__objc_selrefs: 0x638
+  __DATA_CONST.__objc_arraydata: 0xe0
+  __AUTH_CONST.__cfstring: 0x7a0
+  __AUTH_CONST.__const: 0xe0
+  __AUTH_CONST.__objc_const: 0x360
+  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__auth_got: 0x210
+  __AUTH.__objc_data: 0x1e0
   __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x60
-  __DATA.__objc_superrefs: 0x20
-  __DATA.__objc_ivar: 0x50
-  __DATA.__data: 0x240
+  __DATA.__objc_classrefs: 0x88
+  __DATA.__objc_superrefs: 0x38
+  __DATA.__objc_ivar: 0xd8
+  __DATA.__data: 0x2a0
+  __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 148
-  Symbols:   594
-  CStrings:  305
+  Functions: 261
+  Symbols:   970
+  CStrings:  536
 
Symbols:
+ +[PPSMetricCollection _metricSamplePropertyKeys]
+ +[PPSMetricCollection supportsSecureCoding]
+ +[PPSMetricSample sampleWithValue:timestamp:]
+ +[PPSMetricSample supportsSecureCoding]
+ +[PPSProcessMetricCollection _metricSamplePropertyKeys]
+ +[PPSProcessMetricCollection supportsSecureCoding]
+ -[PPSMetricCollection .cxx_destruct]
+ -[PPSMetricCollection _stringFromInducedThermalPressure:]
+ -[PPSMetricCollection _stringFromThermalPressure:]
+ -[PPSMetricCollection batteryPower]
+ -[PPSMetricCollection batteryTemperature]
+ -[PPSMetricCollection cellularPower]
+ -[PPSMetricCollection chargingRate]
+ -[PPSMetricCollection copyWithZone:]
+ -[PPSMetricCollection cpuPower]
+ -[PPSMetricCollection dcInputPower]
+ -[PPSMetricCollection description]
+ -[PPSMetricCollection displayAPL]
+ -[PPSMetricCollection displayCost]
+ -[PPSMetricCollection displayPower]
+ -[PPSMetricCollection dramPower]
+ -[PPSMetricCollection encodeWithCoder:]
+ -[PPSMetricCollection gpuPower]
+ -[PPSMetricCollection inducedThermalPressure]
+ -[PPSMetricCollection initWithCoder:]
+ -[PPSMetricCollection init]
+ -[PPSMetricCollection isSystemPowerAvailableWhileCharging]
+ -[PPSMetricCollection otherSocPower]
+ -[PPSMetricCollection processMetrics]
+ -[PPSMetricCollection setBatteryPower:]
+ -[PPSMetricCollection setBatteryTemperature:]
+ -[PPSMetricCollection setCellularPower:]
+ -[PPSMetricCollection setChargingRate:]
+ -[PPSMetricCollection setCpuPower:]
+ -[PPSMetricCollection setDcInputPower:]
+ -[PPSMetricCollection setDisplayAPL:]
+ -[PPSMetricCollection setDisplayCost:]
+ -[PPSMetricCollection setDisplayPower:]
+ -[PPSMetricCollection setDramPower:]
+ -[PPSMetricCollection setGpuPower:]
+ -[PPSMetricCollection setInducedThermalPressure:]
+ -[PPSMetricCollection setIsSystemPowerAvailableWhileCharging:]
+ -[PPSMetricCollection setOtherSocPower:]
+ -[PPSMetricCollection setProcessMetrics:]
+ -[PPSMetricCollection setSkinTemperature:]
+ -[PPSMetricCollection setSystemLoadPower:]
+ -[PPSMetricCollection setThermalPressure:]
+ -[PPSMetricCollection setWifiPower:]
+ -[PPSMetricCollection skinTemperature]
+ -[PPSMetricCollection systemLoadPower]
+ -[PPSMetricCollection thermalPressure]
+ -[PPSMetricCollection wifiPower]
+ -[PPSMetricMonitor setUpdateInterval:error:]
+ -[PPSMetricMonitor setUpdateInterval:error:].cold.1
+ -[PPSMetricMonitor startMonitoringProcessWithName:error:].cold.2
+ -[PPSMetricMonitor startMonitoringProcessWithPID:error:].cold.2
+ -[PPSMetricMonitor startMonitoringSystemMetricsWithError:].cold.2
+ -[PPSMetricMonitor updateWithMetricCollection:]
+ -[PPSMetricMonitor updateWithMetricCollection:].cold.1
+ -[PPSMetricMonitor updateWithMetricCollection:].cold.2
+ -[PPSMetricMonitorService setUpdateInterval:completion:]
+ -[PPSMetricMonitorService setUpdateInterval:completion:].cold.1
+ -[PPSMetricMonitorService updateWithMetricCollection:]
+ -[PPSMetricMonitorService updateWithMetricCollection:].cold.1
+ -[PPSMetricSample .cxx_destruct]
+ -[PPSMetricSample boolValue]
+ -[PPSMetricSample copyWithZone:]
+ -[PPSMetricSample description]
+ -[PPSMetricSample doubleValue]
+ -[PPSMetricSample encodeWithCoder:]
+ -[PPSMetricSample initWithCoder:]
+ -[PPSMetricSample initWithValue:timestamp:]
+ -[PPSMetricSample intValue]
+ -[PPSMetricSample timestamp]
+ -[PPSMetricSample value]
+ -[PPSProcessMetricCollection .cxx_destruct]
+ -[PPSProcessMetricCollection _stringForApplicationState:]
+ -[PPSProcessMetricCollection applicationState]
+ -[PPSProcessMetricCollection cellIn]
+ -[PPSProcessMetricCollection cellOut]
+ -[PPSProcessMetricCollection copyWithZone:]
+ -[PPSProcessMetricCollection cpuCost]
+ -[PPSProcessMetricCollection cpuSeconds]
+ -[PPSProcessMetricCollection description]
+ -[PPSProcessMetricCollection encodeWithCoder:]
+ -[PPSProcessMetricCollection energyCost]
+ -[PPSProcessMetricCollection energyOverhead]
+ -[PPSProcessMetricCollection gpuCost]
+ -[PPSProcessMetricCollection initWithCoder:]
+ -[PPSProcessMetricCollection locationCost]
+ -[PPSProcessMetricCollection networkCost]
+ -[PPSProcessMetricCollection ongoingLocation]
+ -[PPSProcessMetricCollection setApplicationState:]
+ -[PPSProcessMetricCollection setCellIn:]
+ -[PPSProcessMetricCollection setCellOut:]
+ -[PPSProcessMetricCollection setCpuCost:]
+ -[PPSProcessMetricCollection setCpuSeconds:]
+ -[PPSProcessMetricCollection setEnergyCost:]
+ -[PPSProcessMetricCollection setEnergyOverhead:]
+ -[PPSProcessMetricCollection setGpuCost:]
+ -[PPSProcessMetricCollection setLocationCost:]
+ -[PPSProcessMetricCollection setNetworkCost:]
+ -[PPSProcessMetricCollection setOngoingLocation:]
+ -[PPSProcessMetricCollection setWifiIn:]
+ -[PPSProcessMetricCollection setWifiOut:]
+ -[PPSProcessMetricCollection wifiIn]
+ -[PPSProcessMetricCollection wifiOut]
+ GCC_except_table15
+ GCC_except_table26
+ GCC_except_table27
+ GCC_except_table31
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_PPSMetricCollection
+ _OBJC_CLASS_$_PPSMetricSample
+ _OBJC_CLASS_$_PPSProcessMetricCollection
+ _OBJC_IVAR_$_PPSMetricCollection._batteryPower
+ _OBJC_IVAR_$_PPSMetricCollection._batteryTemperature
+ _OBJC_IVAR_$_PPSMetricCollection._cellularPower
+ _OBJC_IVAR_$_PPSMetricCollection._chargingRate
+ _OBJC_IVAR_$_PPSMetricCollection._cpuPower
+ _OBJC_IVAR_$_PPSMetricCollection._dcInputPower
+ _OBJC_IVAR_$_PPSMetricCollection._displayAPL
+ _OBJC_IVAR_$_PPSMetricCollection._displayCost
+ _OBJC_IVAR_$_PPSMetricCollection._displayPower
+ _OBJC_IVAR_$_PPSMetricCollection._dramPower
+ _OBJC_IVAR_$_PPSMetricCollection._gpuPower
+ _OBJC_IVAR_$_PPSMetricCollection._inducedThermalPressure
+ _OBJC_IVAR_$_PPSMetricCollection._isSystemPowerAvailableWhileCharging
+ _OBJC_IVAR_$_PPSMetricCollection._otherSocPower
+ _OBJC_IVAR_$_PPSMetricCollection._processMetrics
+ _OBJC_IVAR_$_PPSMetricCollection._skinTemperature
+ _OBJC_IVAR_$_PPSMetricCollection._systemLoadPower
+ _OBJC_IVAR_$_PPSMetricCollection._thermalPressure
+ _OBJC_IVAR_$_PPSMetricCollection._wifiPower
+ _OBJC_IVAR_$_PPSMetricSample._timestamp
+ _OBJC_IVAR_$_PPSMetricSample._value
+ _OBJC_IVAR_$_PPSProcessMetricCollection._applicationState
+ _OBJC_IVAR_$_PPSProcessMetricCollection._cellIn
+ _OBJC_IVAR_$_PPSProcessMetricCollection._cellOut
+ _OBJC_IVAR_$_PPSProcessMetricCollection._cpuCost
+ _OBJC_IVAR_$_PPSProcessMetricCollection._cpuSeconds
+ _OBJC_IVAR_$_PPSProcessMetricCollection._energyCost
+ _OBJC_IVAR_$_PPSProcessMetricCollection._energyOverhead
+ _OBJC_IVAR_$_PPSProcessMetricCollection._gpuCost
+ _OBJC_IVAR_$_PPSProcessMetricCollection._locationCost
+ _OBJC_IVAR_$_PPSProcessMetricCollection._networkCost
+ _OBJC_IVAR_$_PPSProcessMetricCollection._ongoingLocation
+ _OBJC_IVAR_$_PPSProcessMetricCollection._wifiIn
+ _OBJC_IVAR_$_PPSProcessMetricCollection._wifiOut
+ _OBJC_METACLASS_$_PPSMetricCollection
+ _OBJC_METACLASS_$_PPSMetricSample
+ _OBJC_METACLASS_$_PPSProcessMetricCollection
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _PPSTimeStringFromDate
+ _PPSTimeStringFromDate.dateFormatter
+ _PPSTimeStringFromDate.onceToken
+ __OBJC_$_CLASS_METHODS_PPSMetricCollection
+ __OBJC_$_CLASS_METHODS_PPSMetricSample
+ __OBJC_$_CLASS_METHODS_PPSProcessMetricCollection
+ __OBJC_$_CLASS_PROP_LIST_PPSMetricCollection
+ __OBJC_$_CLASS_PROP_LIST_PPSMetricSample
+ __OBJC_$_CLASS_PROP_LIST_PPSProcessMetricCollection
+ __OBJC_$_INSTANCE_METHODS_PPSMetricCollection
+ __OBJC_$_INSTANCE_METHODS_PPSMetricSample
+ __OBJC_$_INSTANCE_METHODS_PPSProcessMetricCollection
+ __OBJC_$_INSTANCE_VARIABLES_PPSMetricCollection
+ __OBJC_$_INSTANCE_VARIABLES_PPSMetricSample
+ __OBJC_$_INSTANCE_VARIABLES_PPSProcessMetricCollection
+ __OBJC_$_PROP_LIST_PPSMetricCollection
+ __OBJC_$_PROP_LIST_PPSMetricSample
+ __OBJC_$_PROP_LIST_PPSProcessMetricCollection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_CLASS_PROTOCOLS_$_PPSMetricCollection
+ __OBJC_CLASS_PROTOCOLS_$_PPSMetricSample
+ __OBJC_CLASS_PROTOCOLS_$_PPSProcessMetricCollection
+ __OBJC_CLASS_RO_$_PPSMetricCollection
+ __OBJC_CLASS_RO_$_PPSMetricSample
+ __OBJC_CLASS_RO_$_PPSProcessMetricCollection
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_METACLASS_RO_$_PPSMetricCollection
+ __OBJC_METACLASS_RO_$_PPSMetricSample
+ __OBJC_METACLASS_RO_$_PPSProcessMetricCollection
+ __OBJC_PROTOCOL_$_NSCopying
+ ___34-[PPSMetricCollection description]_block_invoke
+ ___42-[PPSMetricMonitor _handleXPCInterruption]_block_invoke.51
+ ___44-[PPSMetricMonitor setUpdateInterval:error:]_block_invoke
+ ___47-[PPSMetricMonitor updateWithMetricCollection:]_block_invoke
+ ___48+[PPSMetricCollection _metricSamplePropertyKeys]_block_invoke
+ ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.40
+ ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.40.cold.1
+ ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.41
+ ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.41.cold.1
+ ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.42
+ ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.46
+ ___54-[PPSMetricMonitorService updateWithMetricCollection:]_block_invoke
+ ___55+[PPSProcessMetricCollection _metricSamplePropertyKeys]_block_invoke
+ ___62-[PPSMetricMonitorService listener:shouldAcceptNewConnection:]_block_invoke.65
+ ___62-[PPSMetricMonitorService listener:shouldAcceptNewConnection:]_block_invoke.66
+ ___PPSTimeStringFromDate_block_invoke
+ ___block_descriptor_40_e8_32r_e53_v32?0"NSNumber"8"PPSProcessMetricCollection"16^B24lr32l8
+ ___block_literal_global.62
+ __metricSamplePropertyKeys.keys
+ __metricSamplePropertyKeys.onceToken
+ __unnamed_array_storage
+ _kPPSInducedThermalStateKey
+ _kPPSIsSystemPowerAvailableKey
+ _kPPSMetricTimestampKey
+ _kPPSMetricValueKey
+ _kPPSProcessMetricsKey
+ _kPPSThermalStateKey
+ _objc_enumerationMutation
+ _objc_msgSend$UTF8String
+ _objc_msgSend$_metricSamplePropertyKeys
+ _objc_msgSend$_stringForApplicationState:
+ _objc_msgSend$_stringFromInducedThermalPressure:
+ _objc_msgSend$_stringFromThermalPressure:
+ _objc_msgSend$allocWithZone:
+ _objc_msgSend$applicationState
+ _objc_msgSend$batteryPower
+ _objc_msgSend$batteryTemperature
+ _objc_msgSend$cellIn
+ _objc_msgSend$cellOut
+ _objc_msgSend$cellularPower
+ _objc_msgSend$changeUpdateInterval:
+ _objc_msgSend$chargingRate
+ _objc_msgSend$copyWithZone:
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$cpuCost
+ _objc_msgSend$cpuPower
+ _objc_msgSend$cpuSeconds
+ _objc_msgSend$dcInputPower
+ _objc_msgSend$decodeDictionaryWithKeysOfClasses:objectsOfClasses:forKey:
+ _objc_msgSend$displayAPL
+ _objc_msgSend$displayCost
+ _objc_msgSend$displayPower
+ _objc_msgSend$dramPower
+ _objc_msgSend$energyCost
+ _objc_msgSend$energyOverhead
+ _objc_msgSend$gpuCost
+ _objc_msgSend$gpuPower
+ _objc_msgSend$inducedThermalPressure
+ _objc_msgSend$init
+ _objc_msgSend$initWithValue:timestamp:
+ _objc_msgSend$isSystemPowerAvailableWhileCharging
+ _objc_msgSend$locationCost
+ _objc_msgSend$metricMonitor:didUpdateWithMetrics:
+ _objc_msgSend$networkCost
+ _objc_msgSend$ongoingLocation
+ _objc_msgSend$otherSocPower
+ _objc_msgSend$processMetrics
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setUpdateInterval:completion:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$skinTemperature
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$systemLoadPower
+ _objc_msgSend$thermalPressure
+ _objc_msgSend$timestamp
+ _objc_msgSend$updateWithMetricCollection:
+ _objc_msgSend$value
+ _objc_msgSend$valueForKey:
+ _objc_msgSend$wifiIn
+ _objc_msgSend$wifiOut
+ _objc_msgSend$wifiPower
+ _objc_release_x28
+ _objc_release_x9
+ _objc_retain
+ _objc_retain_x23
+ _objc_retain_x3
- -[PPSMetricMonitor updateWithMetrics:]
- -[PPSMetricMonitor updateWithMetrics:].cold.1
- -[PPSMetricMonitor updateWithMetrics:].cold.2
- -[PPSMetricMonitorService updateWithMetrics:]
- -[PPSMetricMonitorService updateWithMetrics:].cold.1
- GCC_except_table19
- GCC_except_table28
- ___38-[PPSMetricMonitor updateWithMetrics:]_block_invoke
- ___42-[PPSMetricMonitor _handleXPCInterruption]_block_invoke.48
- ___45-[PPSMetricMonitorService updateWithMetrics:]_block_invoke
- ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.37
- ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.37.cold.1
- ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.38
- ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.38.cold.1
- ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.39
- ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.43
- ___62-[PPSMetricMonitorService listener:shouldAcceptNewConnection:]_block_invoke.62
- ___62-[PPSMetricMonitorService listener:shouldAcceptNewConnection:]_block_invoke.63
- ___block_literal_global.59
- _objc_msgSend$metricMonitor:didUpdateMetrics:
- _objc_msgSend$updateWithMetrics:
CStrings:
+ "\x02"
+ "\n\n-------------- Process %-5d ---------------\n%@"
+ "\r"
+ "\x1d#"
+ "%d"
+ "%s called by client: %d interval: %@"
+ "-[PPSMetricMonitorService setUpdateInterval:completion:]"
+ "-[PPSMetricMonitorService updateWithMetricCollection:]"
+ "@\"NSDate\""
+ "@\"NSDictionary\""
+ "@\"PPSMetricSample\""
+ "@24@0:8^{_NSZone=}16"
+ "@24@0:8q16"
+ "B32@0:8d16^@24"
+ "Background Running"
+ "Background Task Suspended"
+ "Energy Cost        %8.3f     %@\nEnergy Overhead    %8.3f     %@\nCPU Cost           %8.3f     %@\nCPU Seconds        %8.3f s   %@\nGPU Cost           %8.3f     %@\nNetwork Cost       %8d     %@\nWiFi In            %8d B   %@\nWiFi Out           %8d B   %@\nCell In            %8d B   %@\nCell Out           %8d B   %@\nLocation Cost      %8.3f     %@\nOngoing Location   %8s     %@\nApplication State               %@\n%29s"
+ "Foreground Running"
+ "HH:mm:ss.SSS"
+ "Heavy"
+ "Light"
+ "Moderate"
+ "Must implement metricMonitor:didUpdateWithMetrics: if updateDelegate is YES"
+ "NO"
+ "NSCopying"
+ "Nominal"
+ "Not Set"
+ "PPSMetric value: %@ timestamp: %@"
+ "PPSMetricCollection"
+ "PPSMetricSample"
+ "PPSProcessMetricCollection"
+ "Sleeping"
+ "T@\"NSDate\",R,N,V_timestamp"
+ "T@\"NSDictionary\",&,N,V_processMetrics"
+ "T@\"NSNumber\",R,N,V_value"
+ "T@\"PPSMetricSample\",&,N,V_applicationState"
+ "T@\"PPSMetricSample\",&,N,V_batteryPower"
+ "T@\"PPSMetricSample\",&,N,V_batteryTemperature"
+ "T@\"PPSMetricSample\",&,N,V_cellIn"
+ "T@\"PPSMetricSample\",&,N,V_cellOut"
+ "T@\"PPSMetricSample\",&,N,V_cellularPower"
+ "T@\"PPSMetricSample\",&,N,V_chargingRate"
+ "T@\"PPSMetricSample\",&,N,V_cpuCost"
+ "T@\"PPSMetricSample\",&,N,V_cpuPower"
+ "T@\"PPSMetricSample\",&,N,V_cpuSeconds"
+ "T@\"PPSMetricSample\",&,N,V_dcInputPower"
+ "T@\"PPSMetricSample\",&,N,V_displayAPL"
+ "T@\"PPSMetricSample\",&,N,V_displayCost"
+ "T@\"PPSMetricSample\",&,N,V_displayPower"
+ "T@\"PPSMetricSample\",&,N,V_dramPower"
+ "T@\"PPSMetricSample\",&,N,V_energyCost"
+ "T@\"PPSMetricSample\",&,N,V_energyOverhead"
+ "T@\"PPSMetricSample\",&,N,V_gpuCost"
+ "T@\"PPSMetricSample\",&,N,V_gpuPower"
+ "T@\"PPSMetricSample\",&,N,V_locationCost"
+ "T@\"PPSMetricSample\",&,N,V_networkCost"
+ "T@\"PPSMetricSample\",&,N,V_ongoingLocation"
+ "T@\"PPSMetricSample\",&,N,V_otherSocPower"
+ "T@\"PPSMetricSample\",&,N,V_skinTemperature"
+ "T@\"PPSMetricSample\",&,N,V_systemLoadPower"
+ "T@\"PPSMetricSample\",&,N,V_wifiIn"
+ "T@\"PPSMetricSample\",&,N,V_wifiOut"
+ "T@\"PPSMetricSample\",&,N,V_wifiPower"
+ "TB,N,V_isSystemPowerAvailableWhileCharging"
+ "TB,R,N"
+ "Td,R,N"
+ "Terminated"
+ "Ti,R,N"
+ "Tq,N,V_inducedThermalPressure"
+ "Tq,N,V_thermalPressure"
+ "Trapping"
+ "UTF8String"
+ "Unable to change update interval while multiple clients are connected"
+ "Unknown"
+ "YES"
+ "_applicationState"
+ "_batteryPower"
+ "_batteryTemperature"
+ "_cellIn"
+ "_cellOut"
+ "_cellularPower"
+ "_chargingRate"
+ "_cpuCost"
+ "_cpuPower"
+ "_cpuSeconds"
+ "_dcInputPower"
+ "_displayAPL"
+ "_displayCost"
+ "_displayPower"
+ "_dramPower"
+ "_energyCost"
+ "_energyOverhead"
+ "_gpuCost"
+ "_gpuPower"
+ "_inducedThermalPressure"
+ "_isSystemPowerAvailableWhileCharging"
+ "_locationCost"
+ "_metricSamplePropertyKeys"
+ "_networkCost"
+ "_ongoingLocation"
+ "_otherSocPower"
+ "_processMetrics"
+ "_skinTemperature"
+ "_stringForApplicationState:"
+ "_stringFromInducedThermalPressure:"
+ "_stringFromThermalPressure:"
+ "_systemLoadPower"
+ "_thermalPressure"
+ "_timestamp"
+ "_value"
+ "_wifiIn"
+ "_wifiOut"
+ "_wifiPower"
+ "allocWithZone:"
+ "applicationState"
+ "batteryPower"
+ "batteryTemperature"
+ "cellIn"
+ "cellOut"
+ "cellularPower"
+ "changeUpdateInterval:"
+ "chargingRate"
+ "copyWithZone:"
+ "countByEnumeratingWithState:objects:count:"
+ "cpuCost"
+ "cpuPower"
+ "cpuSeconds"
+ "dcInputPower"
+ "decodeDictionaryWithKeysOfClasses:objectsOfClasses:forKey:"
+ "displayAPL"
+ "displayCost"
+ "displayPower"
+ "dramPower"
+ "energyCost"
+ "energyOverhead"
+ "gpuCost"
+ "gpuPower"
+ "inducedThermalPressure"
+ "inducedThermalState"
+ "initWithValue:timestamp:"
+ "isSystemPowerAvailableWhileCharging"
+ "locationCost"
+ "metricMonitor:didUpdateWithMetrics:"
+ "metricMonitor:didUpdateWithMetrics: is not implemented"
+ "networkCost"
+ "ongoingLocation"
+ "otherSocPower"
+ "processMetrics"
+ "r*20@0:8I16"
+ "sampleWithValue:timestamp:"
+ "setApplicationState:"
+ "setBatteryPower:"
+ "setBatteryTemperature:"
+ "setCellIn:"
+ "setCellOut:"
+ "setCellularPower:"
+ "setChargingRate:"
+ "setCpuCost:"
+ "setCpuPower:"
+ "setCpuSeconds:"
+ "setDateFormat:"
+ "setDcInputPower:"
+ "setDisplayAPL:"
+ "setDisplayCost:"
+ "setDisplayPower:"
+ "setDramPower:"
+ "setEnergyCost:"
+ "setEnergyOverhead:"
+ "setGpuCost:"
+ "setGpuPower:"
+ "setInducedThermalPressure:"
+ "setIsSystemPowerAvailableWhileCharging:"
+ "setLocationCost:"
+ "setNetworkCost:"
+ "setOngoingLocation:"
+ "setOtherSocPower:"
+ "setProcessMetrics:"
+ "setSkinTemperature:"
+ "setSystemLoadPower:"
+ "setThermalPressure:"
+ "setUpdateInterval:completion:"
+ "setUpdateInterval:error:"
+ "setValue:forKey:"
+ "setWifiIn:"
+ "setWifiOut:"
+ "setWifiPower:"
+ "setWithArray:"
+ "skinTemperature"
+ "startMonitoringProcessWithName called while already monitoring"
+ "startMonitoringProcessWithPID called while already monitoring"
+ "startMonitoringSystemMetricsWithError called while already monitoring"
+ "stringByAppendingFormat:"
+ "stringFromDate:"
+ "systemLoadPower"
+ "thermalPressure"
+ "thermalState"
+ "timestamp"
+ "updateWithMetricCollection:"
+ "v24@0:8@\"PPSMetricCollection\"16"
+ "v32@?0@\"NSNumber\"8@\"PPSProcessMetricCollection\"16^B24"
+ "value"
+ "valueForKey:"
+ "wifiIn"
+ "wifiOut"
+ "wifiPower"
- "-[PPSMetricMonitorService updateWithMetrics:]"
- "Must implement metricMonitor:didUpdateMetrics: if updateDelegate is YES"
- "metricMonitor:didUpdateMetrics:"
- "metricMonitor:didUpdateMetrics: is not implemented"
- "updateWithMetrics:"
- "v24@0:8@\"NSDictionary\"16"

```
