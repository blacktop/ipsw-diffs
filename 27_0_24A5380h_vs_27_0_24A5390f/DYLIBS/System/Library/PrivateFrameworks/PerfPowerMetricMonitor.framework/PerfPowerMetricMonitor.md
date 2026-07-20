## PerfPowerMetricMonitor

> `/System/Library/PrivateFrameworks/PerfPowerMetricMonitor.framework/PerfPowerMetricMonitor`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-3486.0.46.502.1
-  __TEXT.__text: 0x18680
-  __TEXT.__objc_methlist: 0x15a4
+3486.0.81.502.4
+  __TEXT.__text: 0x19d90
+  __TEXT.__objc_methlist: 0x187c
   __TEXT.__const: 0xf8
-  __TEXT.__gcc_except_tab: 0x928
-  __TEXT.__cstring: 0x1157
-  __TEXT.__oslogstring: 0x1be2
-  __TEXT.__ustring: 0x6c0
-  __TEXT.__unwind_info: 0x4c0
+  __TEXT.__gcc_except_tab: 0x998
+  __TEXT.__cstring: 0x1308
+  __TEXT.__oslogstring: 0x1c3b
+  __TEXT.__ustring: 0x77e
+  __TEXT.__unwind_info: 0x510
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x680
-  __DATA_CONST.__objc_classlist: 0x48
+  __DATA_CONST.__const: 0x710
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xee0
+  __DATA_CONST.__objc_selrefs: 0xf40
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x40
-  __DATA_CONST.__objc_arraydata: 0x280
-  __DATA_CONST.__got: 0xf0
-  __AUTH_CONST.__const: 0x1a0
-  __AUTH_CONST.__cfstring: 0x14a0
-  __AUTH_CONST.__objc_const: 0x2308
+  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_arraydata: 0x2e8
+  __DATA_CONST.__got: 0x108
+  __AUTH_CONST.__const: 0x1c0
+  __AUTH_CONST.__cfstring: 0x1640
+  __AUTH_CONST.__objc_const: 0x2898
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0x310
-  __DATA.__objc_ivar: 0x22c
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x280
   __DATA.__data: 0x300
   __DATA.__bss: 0x50
   __DATA_DIRTY.__objc_data: 0x2d0
-  __DATA_DIRTY.__bss: 0x58
+  __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 609
-  Symbols:   1391
-  CStrings:  317
+  Functions: 674
+  Symbols:   1518
+  CStrings:  334
 
Symbols:
+ +[PPSLiteMetricCollection extractLiteMetrics:]
+ +[PPSLiteMetricCollection supportsSecureCoding]
+ +[PPSLiteProcessMetricCollection _metricSamplePropertyKeys]
+ +[PPSLiteProcessMetricCollection supportsSecureCoding]
+ -[PPSLiteMetricCollection .cxx_destruct]
+ -[PPSLiteMetricCollection description]
+ -[PPSLiteMetricCollection encodeWithCoder:]
+ -[PPSLiteMetricCollection initWithCoder:]
+ -[PPSLiteMetricCollection init]
+ -[PPSLiteMetricCollection processMetrics]
+ -[PPSLiteMetricCollection setProcessMetrics:]
+ -[PPSLiteProcessMetricCollection .cxx_destruct]
+ -[PPSLiteProcessMetricCollection aneEnergy]
+ -[PPSLiteProcessMetricCollection aneTime]
+ -[PPSLiteProcessMetricCollection bundleID]
+ -[PPSLiteProcessMetricCollection bytesRead]
+ -[PPSLiteProcessMetricCollection bytesWritten]
+ -[PPSLiteProcessMetricCollection coalitionID]
+ -[PPSLiteProcessMetricCollection cpuEnergyWithVouchers]
+ -[PPSLiteProcessMetricCollection cpuEnergyWithoutVouchers]
+ -[PPSLiteProcessMetricCollection cpuInstructions]
+ -[PPSLiteProcessMetricCollection cpuPInstructions]
+ -[PPSLiteProcessMetricCollection cpuSecondsWithVouchers]
+ -[PPSLiteProcessMetricCollection cpuSecondsWithoutVouchers]
+ -[PPSLiteProcessMetricCollection description]
+ -[PPSLiteProcessMetricCollection encodeWithCoder:]
+ -[PPSLiteProcessMetricCollection gpuEnergyWithVouchers]
+ -[PPSLiteProcessMetricCollection gpuEnergyWithoutVouchers]
+ -[PPSLiteProcessMetricCollection gpuTime]
+ -[PPSLiteProcessMetricCollection initWithCoder:]
+ -[PPSLiteProcessMetricCollection initWithProcessMetricCollection:]
+ -[PPSLiteProcessMetricCollection pid]
+ -[PPSLiteProcessMetricCollection processActive]
+ -[PPSLiteProcessMetricCollection processName]
+ -[PPSLiteProcessMetricCollection sampleTime]
+ -[PPSLiteProcessMetricCollection setAneEnergy:]
+ -[PPSLiteProcessMetricCollection setAneTime:]
+ -[PPSLiteProcessMetricCollection setBundleID:]
+ -[PPSLiteProcessMetricCollection setBytesRead:]
+ -[PPSLiteProcessMetricCollection setBytesWritten:]
+ -[PPSLiteProcessMetricCollection setCoalitionID:]
+ -[PPSLiteProcessMetricCollection setCpuEnergyWithVouchers:]
+ -[PPSLiteProcessMetricCollection setCpuEnergyWithoutVouchers:]
+ -[PPSLiteProcessMetricCollection setCpuInstructions:]
+ -[PPSLiteProcessMetricCollection setCpuPInstructions:]
+ -[PPSLiteProcessMetricCollection setCpuSecondsWithVouchers:]
+ -[PPSLiteProcessMetricCollection setCpuSecondsWithoutVouchers:]
+ -[PPSLiteProcessMetricCollection setGpuEnergyWithVouchers:]
+ -[PPSLiteProcessMetricCollection setGpuEnergyWithoutVouchers:]
+ -[PPSLiteProcessMetricCollection setGpuTime:]
+ -[PPSLiteProcessMetricCollection setPid:]
+ -[PPSLiteProcessMetricCollection setProcessActive:]
+ -[PPSLiteProcessMetricCollection setProcessName:]
+ -[PPSLiteProcessMetricCollection setSampleTime:]
+ -[PPSMetricMonitor collectLiteMetricsOnSnapshot:]
+ -[PPSMetricMonitorConfiguration liteMode]
+ -[PPSMetricMonitorConfiguration setLiteMode:]
+ -[PPSMetricMonitorService _emitSystemMetricsSignpost:beginMct:endMct:deltaTime:]
+ GCC_except_table111
+ GCC_except_table33
+ GCC_except_table44
+ GCC_except_table47
+ GCC_except_table49
+ GCC_except_table54
+ GCC_except_table65
+ GCC_except_table70
+ GCC_except_table74
+ GCC_except_table78
+ GCC_except_table89
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_PPSLiteMetricCollection
+ _OBJC_CLASS_$_PPSLiteProcessMetricCollection
+ _OBJC_IVAR_$_PPSLiteMetricCollection._processMetrics
+ _OBJC_IVAR_$_PPSLiteProcessMetricCollection._aneEnergy
+ _OBJC_IVAR_$_PPSLiteProcessMetricCollection._aneTime
+ _OBJC_IVAR_$_PPSLiteProcessMetricCollection._bundleID
+ _OBJC_IVAR_$_PPSLiteProcessMetricCollection._bytesRead
+ _OBJC_IVAR_$_PPSLiteProcessMetricCollection._bytesWritten
+ _OBJC_IVAR_$_PPSLiteProcessMetricCollection._coalitionID
+ _OBJC_IVAR_$_PPSLiteProcessMetricCollection._cpuEnergyWithVouchers
+ _OBJC_IVAR_$_PPSLiteProcessMetricCollection._cpuEnergyWithoutVouchers
+ _OBJC_IVAR_$_PPSLiteProcessMetricCollection._cpuInstructions
+ _OBJC_IVAR_$_PPSLiteProcessMetricCollection._cpuPInstructions
+ _OBJC_IVAR_$_PPSLiteProcessMetricCollection._cpuSecondsWithVouchers
+ _OBJC_IVAR_$_PPSLiteProcessMetricCollection._cpuSecondsWithoutVouchers
+ _OBJC_IVAR_$_PPSLiteProcessMetricCollection._gpuEnergyWithVouchers
+ _OBJC_IVAR_$_PPSLiteProcessMetricCollection._gpuEnergyWithoutVouchers
+ _OBJC_IVAR_$_PPSLiteProcessMetricCollection._gpuTime
+ _OBJC_IVAR_$_PPSLiteProcessMetricCollection._pid
+ _OBJC_IVAR_$_PPSLiteProcessMetricCollection._processActive
+ _OBJC_IVAR_$_PPSLiteProcessMetricCollection._processName
+ _OBJC_IVAR_$_PPSLiteProcessMetricCollection._sampleTime
+ _OBJC_IVAR_$_PPSMetricMonitorConfiguration._liteMode
+ _OBJC_METACLASS_$_PPSLiteMetricCollection
+ _OBJC_METACLASS_$_PPSLiteProcessMetricCollection
+ __OBJC_$_CLASS_METHODS_PPSLiteMetricCollection
+ __OBJC_$_CLASS_METHODS_PPSLiteProcessMetricCollection
+ __OBJC_$_CLASS_PROP_LIST_PPSLiteMetricCollection
+ __OBJC_$_CLASS_PROP_LIST_PPSLiteProcessMetricCollection
+ __OBJC_$_INSTANCE_METHODS_PPSLiteMetricCollection
+ __OBJC_$_INSTANCE_METHODS_PPSLiteProcessMetricCollection
+ __OBJC_$_INSTANCE_VARIABLES_PPSLiteMetricCollection
+ __OBJC_$_INSTANCE_VARIABLES_PPSLiteProcessMetricCollection
+ __OBJC_$_PROP_LIST_PPSLiteMetricCollection
+ __OBJC_$_PROP_LIST_PPSLiteProcessMetricCollection
+ __OBJC_CLASS_PROTOCOLS_$_PPSLiteMetricCollection
+ __OBJC_CLASS_PROTOCOLS_$_PPSLiteProcessMetricCollection
+ __OBJC_CLASS_RO_$_PPSLiteMetricCollection
+ __OBJC_CLASS_RO_$_PPSLiteProcessMetricCollection
+ __OBJC_METACLASS_RO_$_PPSLiteMetricCollection
+ __OBJC_METACLASS_RO_$_PPSLiteProcessMetricCollection
+ ___38-[PPSLiteMetricCollection description]_block_invoke
+ ___46+[PPSLiteMetricCollection extractLiteMetrics:]_block_invoke
+ ___49-[PPSMetricMonitor collectLiteMetricsOnSnapshot:]_block_invoke
+ ___49-[PPSMetricMonitor collectLiteMetricsOnSnapshot:]_block_invoke_2
+ ___59+[PPSLiteProcessMetricCollection _metricSamplePropertyKeys]_block_invoke
+ ___block_descriptor_40_e8_32s_e53_v32?0"NSNumber"8"PPSProcessMetricCollection"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e57_v32?0"NSNumber"8"PPSLiteProcessMetricCollection"16^B24ls32l8
+ _kPPSLiteBundleIDKey
+ _kPPSLiteCoalitionIDKey
+ _kPPSLitePidKey
+ _kPPSLiteProcessActiveKey
+ _kPPSLiteProcessMetricsKey
+ _kPPSLiteProcessNameKey
+ _kPPSLiteSampleTimeKey
+ _kPPSMMConfigLiteMode
+ _objc_msgSend$_emitSystemMetricsSignpost:beginMct:endMct:deltaTime:
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appendString:
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$extractLiteMetrics:
+ _objc_msgSend$initWithProcessMetricCollection:
+ _objc_msgSend$isSetUp
+ _objc_msgSend$liteMode
+ _objc_msgSend$setUpForMonitoringWithLiteMode:
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$upgradeToFullSetup
- GCC_except_table110
- GCC_except_table41
- GCC_except_table46
- GCC_except_table51
- GCC_except_table64
- GCC_except_table69
- GCC_except_table73
- GCC_except_table77
- GCC_except_table88
- _objc_msgSend$setUpForMonitoring
CStrings:
+ "  %@\n"
+ ")"
+ "Cannot call collectMetricsOnSnapshot: in lite mode — use collectLiteMetricsOnSnapshot: instead"
+ "Cannot collect lite metrics when interrupted"
+ "Cannot collect lite metrics when not monitoring"
+ "PPSLiteMetricCollection(\n"
+ "PPSLiteProcessMetricCollection(pid=%d name=%@ cpuEnergyWithVouchers=%@ gpuEnergyWithVouchers=%@ cpuSeconds=%@ aneEnergy=%@ bytesRead=%@ cpuInstructions=%@ sampleTime=%@)"
+ "PPSMetricMonitorConfig(mode: %ld updateInterval: %f updateDelegate: %d includeBackBoardUsage: %d isHeadless: %d emitTracingSignposts: %d emitSignposts: %d liteMode: %d))"
+ "bundleID"
+ "coalitionID"
+ "collectLiteMetricsOnSnapshot error %@"
+ "collecting lite snapshot"
+ "lite metrics collected %@"
+ "liteMode"
+ "pid"
+ "processActive"
+ "processName"
+ "v32@?0@\"NSNumber\"8@\"PPSLiteProcessMetricCollection\"16^B24"
- "PPSMetricMonitorConfig(mode: %ld updateInterval: %f updateDelegate: %d includeBackBoardUsage: %d isHeadless: %d emitTracingSignposts: %d emitSignposts: %d))"
```
