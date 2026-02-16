## MetricMeasurement

> `/System/Library/PrivateFrameworks/MetricMeasurement.framework/MetricMeasurement`

```diff

-294.80.3.0.0
-  __TEXT.__text: 0x1b74c
-  __TEXT.__auth_stubs: 0x8a0
-  __TEXT.__objc_methlist: 0x2744
+297.100.9.0.0
+  __TEXT.__text: 0x1e58c
+  __TEXT.__auth_stubs: 0x850
+  __TEXT.__objc_methlist: 0x28bc
   __TEXT.__const: 0x268
-  __TEXT.__cstring: 0x236f
-  __TEXT.__gcc_except_tab: 0x5b4
-  __TEXT.__oslogstring: 0x77e
+  __TEXT.__cstring: 0x2625
+  __TEXT.__gcc_except_tab: 0x6f0
+  __TEXT.__oslogstring: 0x965
   __TEXT.__ustring: 0x34
-  __TEXT.__unwind_info: 0x900
-  __TEXT.__objc_classname: 0x594
-  __TEXT.__objc_methname: 0x4846
-  __TEXT.__objc_methtype: 0xfe9
-  __TEXT.__objc_stubs: 0x3f80
-  __DATA_CONST.__got: 0x270
-  __DATA_CONST.__const: 0x5f8
-  __DATA_CONST.__objc_classlist: 0x160
+  __TEXT.__unwind_info: 0x9c8
+  __TEXT.__objc_classname: 0x5c5
+  __TEXT.__objc_methname: 0x4b7a
+  __TEXT.__objc_methtype: 0x10f2
+  __TEXT.__objc_stubs: 0x4200
+  __DATA_CONST.__got: 0x288
+  __DATA_CONST.__const: 0x6a0
+  __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_nlclslist: 0x8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14b8
+  __DATA_CONST.__objc_selrefs: 0x1550
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x100
-  __AUTH_CONST.__auth_got: 0x460
+  __DATA_CONST.__objc_superrefs: 0x108
+  __AUTH_CONST.__auth_got: 0x438
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x2440
-  __AUTH_CONST.__objc_const: 0x56d8
+  __AUTH_CONST.__cfstring: 0x27c0
+  __AUTH_CONST.__objc_const: 0x59d8
   __AUTH_CONST.__objc_intobj: 0xa8
-  __AUTH.__objc_data: 0xd70
-  __DATA.__objc_ivar: 0x16c
+  __AUTH.__objc_data: 0xe60
+  __DATA.__objc_ivar: 0x170
   __DATA.__data: 0x7e0
   __DATA.__bss: 0x2b0
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpmsample.dylib
   - /usr/lib/libsysmon.dylib
-  UUID: 69D5E3F8-60DE-3454-A714-5AC147BCBD92
-  Functions: 824
-  Symbols:   3109
-  CStrings:  1781
+  UUID: 47036F8B-5C69-3A0D-8DD0-67B867EBECBF
+  Functions: 870
+  Symbols:   3257
+  CStrings:  1891
 
Symbols:
+ +[MXMEnergyMetric currentProcess]
+ +[MXMEnergySampleTag aneEnergyProcess]
+ +[MXMEnergySampleTag bytesReadProcess]
+ +[MXMEnergySampleTag bytesWrittenProcess]
+ +[MXMEnergySampleTag cpuEnergyProcess]
+ +[MXMEnergySampleTag cpuInstructionsProcess]
+ +[MXMEnergySampleTag energy]
+ +[MXMEnergySampleTag gpuEnergyProcess]
+ +[MXMUnitEnergy baseUnit]
+ +[MXMUnitEnergy nanojoules]
+ -[MXMEnergyMetric .cxx_destruct]
+ -[MXMEnergyMetric _convertMetricsToSampleData:]
+ -[MXMEnergyMetric _shouldAlwaysWrapInProxy]
+ -[MXMEnergyMetric _shouldConstructProbe]
+ -[MXMEnergyMetric appendMetricSample:name:tag:unit:conversionFactor:processName:pidNumber:toData:timestamp:]
+ -[MXMEnergyMetric didStopAtContinuousTime:absoluteTime:stopDate:]
+ -[MXMEnergyMetric harvestData:error:]
+ -[MXMEnergyMetric initWithIdentifier:filter:]
+ -[MXMEnergyMetric initWithProcessNames:]
+ -[MXMEnergyMetric prepareWithOptions:error:]
+ -[MXMEnergyMetric processNames]
+ -[MXMEnergyMetric willStartAtEstimatedTime:]
+ -[MXMInstrument measureAutomatically:options:block:].cold.8
+ -[MXMProxyServiceManager _sampleFromMetricMonitorWithProxyMetric:timeout:stopReason:]
+ -[MXMProxyServiceManager _setupMetricMonitorWithProxyMetric:processNames:response:]
+ -[MXMProxyServiceManager _teardownMetricMonitorWithProxyMetric:response:]
+ GCC_except_table25
+ GCC_except_table27
+ GCC_except_table29
+ _MXMEnergyMetricIdentifier
+ _OBJC_CLASS_$_MXMEnergyMetric
+ _OBJC_CLASS_$_MXMEnergySampleTag
+ _OBJC_CLASS_$_MXMUnitEnergy
+ _OBJC_IVAR_$_MXMEnergyMetric._collectedData
+ _OBJC_METACLASS_$_MXMEnergyMetric
+ _OBJC_METACLASS_$_MXMEnergySampleTag
+ _OBJC_METACLASS_$_MXMUnitEnergy
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ __OBJC_$_CLASS_METHODS_MXMEnergyMetric
+ __OBJC_$_CLASS_METHODS_MXMEnergySampleTag
+ __OBJC_$_CLASS_METHODS_MXMUnitEnergy
+ __OBJC_$_CLASS_PROP_LIST_MXMEnergyMetric
+ __OBJC_$_CLASS_PROP_LIST_MXMEnergySampleTag
+ __OBJC_$_CLASS_PROP_LIST_MXMUnitEnergy
+ __OBJC_$_INSTANCE_METHODS_MXMEnergyMetric
+ __OBJC_$_INSTANCE_VARIABLES_MXMEnergyMetric
+ __OBJC_$_PROP_LIST_MXMEnergyMetric
+ __OBJC_CLASS_RO_$_MXMEnergyMetric
+ __OBJC_CLASS_RO_$_MXMEnergySampleTag
+ __OBJC_CLASS_RO_$_MXMUnitEnergy
+ __OBJC_METACLASS_RO_$_MXMEnergyMetric
+ __OBJC_METACLASS_RO_$_MXMEnergySampleTag
+ __OBJC_METACLASS_RO_$_MXMUnitEnergy
+ ___37-[MXMEnergyMetric harvestData:error:]_block_invoke
+ ___44-[MXMEnergyMetric prepareWithOptions:error:]_block_invoke
+ ___47-[MXMEnergyMetric _convertMetricsToSampleData:]_block_invoke
+ ___73-[MXMProxyServiceManager _teardownMetricMonitorWithProxyMetric:response:]_block_invoke
+ ___83-[MXMProxyServiceManager _setupMetricMonitorWithProxyMetric:processNames:response:]_block_invoke
+ ___85-[MXMProxyServiceManager _sampleFromMetricMonitorWithProxyMetric:timeout:stopReason:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_40_e8_32s_e141_v88?0"PPSMetricSample"8"NSString"16"NSString"24"MXMSampleTag"32"NSDimension"40d48"NSString"56"NSNumber"64"MXMMutableSampleData"72Q80ls32l8
+ ___block_descriptor_56_e8_32r40r48r_e44_v32?0"PPSMetricCollection"8Q16"NSError"24lr32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e20_v20?0B8"NSError"12lr40l8r48l8s32l8
+ ___block_literal_global.278
+ ___block_literal_global.82
+ _objc_msgSend$_convertMetricsToSampleData:
+ _objc_msgSend$_sampleFromMetricMonitorWithProxyMetric:timeout:response:
+ _objc_msgSend$_sampleFromMetricMonitorWithProxyMetric:timeout:stopReason:
+ _objc_msgSend$_setupMetricMonitorWithProxyMetric:processNames:response:
+ _objc_msgSend$_teardownMetricMonitorWithProxyMetric:response:
+ _objc_msgSend$aneEnergyProcess
+ _objc_msgSend$appendMetricSample:name:tag:unit:conversionFactor:processName:pidNumber:toData:timestamp:
+ _objc_msgSend$bytesReadProcess
+ _objc_msgSend$bytesWrittenProcess
+ _objc_msgSend$cpuEnergyProcess
+ _objc_msgSend$cpuInstructionsProcess
+ _objc_msgSend$energy
+ _objc_msgSend$gpuEnergyProcess
+ _objc_msgSend$initWithProcessNames:
+ _objc_msgSend$nanojoules
+ _objc_msgSend$processMetrics
+ _objc_msgSend$processName
+ _objc_msgSend$processNames
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$valueForKey:
+ _objc_release_x2
- ___block_literal_global.275
- ___block_literal_global.75
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x8
- _objc_retain_x9
CStrings:
+ ""
+ "%@ skipped - value is negative (%.2f)"
+ "@\"MXMSampleData\""
+ "@40@0:8Q16r^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v@}24@32"
+ "ANE Energy"
+ "CPU Energy"
+ "CPU Instructions"
+ "Failed to setup PPSMetricMonitor"
+ "Failed to setup PPSMetricMonitor."
+ "GPU Energy"
+ "J"
+ "MXMEnergyMetric"
+ "MXMEnergyMetric needs atleast one process to measure but processNames is nil/empty."
+ "MXMEnergyMetric requires proxy mode"
+ "MXMEnergyMetric requires proxy mode for PPSMetricMonitor access"
+ "MXMEnergyMetric: Failed to teardown PPSMetricMonitor: %@"
+ "MXMEnergySampleTag"
+ "MXMUnitEnergy"
+ "NAND IO Reads"
+ "NAND IO Writes"
+ "No data collected"
+ "No data collected from MetricMonitor!"
+ "No data collected. Nothing to harvest."
+ "No process metrics available yet"
+ "No process names found in filter"
+ "No process names in filter"
+ "No samples available to save."
+ "T@\"MXMEnergyMetric\",R,C,N"
+ "T@\"MXMEnergySampleTag\",R,C,N"
+ "T@\"MXMUnitEnergy\",R,C,D,N"
+ "T@\"MXMUnitEnergy\",R,C,D,N,GbaseUnit"
+ "T@\"MXMUnitEnergy\",R,C,D,N,Gjoules"
+ "T@\"MXMUnitEnergy\",R,C,D,N,Gnanojoules"
+ "T@\"NSSet\",R,C,D,N"
+ "T@\"NSSet\",R,N"
+ "T^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v@},V_currentIteration"
+ "XPC error during MetricMonitor sampling: %@"
+ "^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v@}"
+ "^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v@}16@0:8"
+ "_collectedData"
+ "_convertMetricsToSampleData:"
+ "_sampleFromMetricMonitorWithProxyMetric:timeout:response:"
+ "_sampleFromMetricMonitorWithProxyMetric:timeout:stopReason:"
+ "_setupMetricMonitorWithProxyMetric:processNames:response:"
+ "_teardownMetricMonitorWithProxyMetric:response:"
+ "allEnergyTags"
+ "aneEnergy"
+ "aneEnergyProcess"
+ "appendMetricSample:name:tag:unit:conversionFactor:processName:pidNumber:toData:timestamp:"
+ "bytesRead"
+ "bytesReadProcess"
+ "bytesWritten"
+ "bytesWrittenProcess"
+ "com.apple.metricmeasurement.metrics.energy"
+ "cpuEnergy"
+ "cpuEnergyProcess"
+ "cpuInstructions"
+ "cpuInstructionsProcess"
+ "energy"
+ "energy.ane.process"
+ "energy.bytes.read.process"
+ "energy.bytes.written.process"
+ "energy.cpu.instructions.process"
+ "energy.cpu.process"
+ "energy.gpu.process"
+ "gpuEnergy"
+ "gpuEnergyProcess"
+ "initWithProcessNames:"
+ "isAnimation=YES testName=%@"
+ "joules"
+ "nJ"
+ "nanojoules"
+ "processMetrics"
+ "processNames"
+ "stringWithUTF8String:"
+ "testName=%@"
+ "v24@0:8^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v@}16"
+ "v32@0:8@\"MXMProxyMetric\"16@?<v@?B@\"NSError\">24"
+ "v32@?0@\"PPSMetricCollection\"8Q16@\"NSError\"24"
+ "v40@0:8@\"MXMProxyMetric\"16@\"NSArray\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"MXMProxyMetric\"16d24@?<v@?@\"PPSMetricCollection\"Q@\"NSError\">32"
+ "v40@0:8@16@24@?32"
+ "v40@0:8@16Q24^{vm_statistics64=IIIIQQQQQQQQQIIQQQQIIIIQQQQQQQQQQQQQ}32"
+ "v48@0:8^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v@}16@24@32@40"
+ "v52@0:8^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v@}16B24^{_opaque_pthread_attr_t=q[56c]}28^^{_opaque_pthread_t}36^Q44"
+ "v88@0:8@16@24@32@40d48@56@64@72Q80"
+ "v88@?0@\"PPSMetricSample\"8@\"NSString\"16@\"NSString\"24@\"MXMSampleTag\"32@\"NSDimension\"40d48@\"NSString\"56@\"NSNumber\"64@\"MXMMutableSampleData\"72Q80"
+ "valueForKey:"
- "@40@0:8Q16r^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v}24@32"
- "T^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v},V_currentIteration"
- "^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v}"
- "^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v}16@0:8"
- "isAnimation=YES "
- "v24@0:8^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v}16"
- "v40@0:8@16Q24^{vm_statistics64=IIIIQQQQQQQQQIIQQQQIIIIQQ}32"
- "v48@0:8^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v}16@24@32@40"
- "v52@0:8^{?=QQIQBQQQQ^v^v{?=QQ}{?=QQ}Q^v^v^v^^vB^vdd^v^vB^v}16B24^{_opaque_pthread_attr_t=q[56c]}28^^{_opaque_pthread_t}36^Q44"

```
