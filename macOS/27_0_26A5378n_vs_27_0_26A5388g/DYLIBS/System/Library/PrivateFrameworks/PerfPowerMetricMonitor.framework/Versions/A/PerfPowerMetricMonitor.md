## PerfPowerMetricMonitor

> `/System/Library/PrivateFrameworks/PerfPowerMetricMonitor.framework/Versions/A/PerfPowerMetricMonitor`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-3486.0.46.501.1
-  __TEXT.__text: 0x17a50
-  __TEXT.__objc_methlist: 0x1574
+3486.0.81.501.3
+  __TEXT.__text: 0x19238
+  __TEXT.__objc_methlist: 0x1844
   __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0x918
-  __TEXT.__cstring: 0x1039
-  __TEXT.__oslogstring: 0x10d0
-  __TEXT.__ustring: 0x6c0
-  __TEXT.__unwind_info: 0x4b0
+  __TEXT.__gcc_except_tab: 0x988
+  __TEXT.__cstring: 0x11ea
+  __TEXT.__oslogstring: 0x1129
+  __TEXT.__ustring: 0x77e
+  __TEXT.__unwind_info: 0x4f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x188
-  __DATA_CONST.__objc_classlist: 0x48
+  __DATA_CONST.__const: 0x1c8
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe48
+  __DATA_CONST.__objc_selrefs: 0xea0
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x40
-  __DATA_CONST.__objc_arraydata: 0x280
-  __DATA_CONST.__got: 0xe0
-  __AUTH_CONST.__const: 0x710
-  __AUTH_CONST.__cfstring: 0x1280
-  __AUTH_CONST.__objc_const: 0x2308
+  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_arraydata: 0x2e8
+  __DATA_CONST.__got: 0xf8
+  __AUTH_CONST.__const: 0x790
+  __AUTH_CONST.__cfstring: 0x1420
+  __AUTH_CONST.__objc_const: 0x2898
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0x248
-  __DATA.__objc_ivar: 0x22c
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x280
   __DATA.__data: 0x300
   __DATA.__bss: 0x50
   __DATA_DIRTY.__objc_data: 0x2d0
-  __DATA_DIRTY.__bss: 0x58
+  __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/AssertionServices.framework/Versions/A/AssertionServices
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 613
-  Symbols:   1367
-  CStrings:  276
+  Functions: 677
+  Symbols:   1490
+  CStrings:  293
 
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
+ GCC_except_table47
+ GCC_except_table60
+ GCC_except_table72
+ OBJC_IVAR_$_PPSLiteMetricCollection._processMetrics
+ OBJC_IVAR_$_PPSLiteProcessMetricCollection._aneEnergy
+ OBJC_IVAR_$_PPSLiteProcessMetricCollection._aneTime
+ OBJC_IVAR_$_PPSLiteProcessMetricCollection._bundleID
+ OBJC_IVAR_$_PPSLiteProcessMetricCollection._bytesRead
+ OBJC_IVAR_$_PPSLiteProcessMetricCollection._bytesWritten
+ OBJC_IVAR_$_PPSLiteProcessMetricCollection._coalitionID
+ OBJC_IVAR_$_PPSLiteProcessMetricCollection._cpuEnergyWithVouchers
+ OBJC_IVAR_$_PPSLiteProcessMetricCollection._cpuEnergyWithoutVouchers
+ OBJC_IVAR_$_PPSLiteProcessMetricCollection._cpuInstructions
+ OBJC_IVAR_$_PPSLiteProcessMetricCollection._cpuPInstructions
+ OBJC_IVAR_$_PPSLiteProcessMetricCollection._cpuSecondsWithVouchers
+ OBJC_IVAR_$_PPSLiteProcessMetricCollection._cpuSecondsWithoutVouchers
+ OBJC_IVAR_$_PPSLiteProcessMetricCollection._gpuEnergyWithVouchers
+ OBJC_IVAR_$_PPSLiteProcessMetricCollection._gpuEnergyWithoutVouchers
+ OBJC_IVAR_$_PPSLiteProcessMetricCollection._gpuTime
+ OBJC_IVAR_$_PPSLiteProcessMetricCollection._pid
+ OBJC_IVAR_$_PPSLiteProcessMetricCollection._processActive
+ OBJC_IVAR_$_PPSLiteProcessMetricCollection._processName
+ OBJC_IVAR_$_PPSLiteProcessMetricCollection._sampleTime
+ OBJC_IVAR_$_PPSMetricMonitorConfiguration._liteMode
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_PPSLiteMetricCollection
+ _OBJC_CLASS_$_PPSLiteProcessMetricCollection
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
+ ___block_descriptor_40_e8_32s_e53_v32?0"NSNumber"8"PPSProcessMetricCollection"16^B24l
+ ___block_descriptor_40_e8_32s_e57_v32?0"NSNumber"8"PPSLiteProcessMetricCollection"16^B24l
+ _kPPSLiteBundleIDKey
+ _kPPSLiteCoalitionIDKey
+ _kPPSLitePidKey
+ _kPPSLiteProcessActiveKey
+ _kPPSLiteProcessMetricsKey
+ _kPPSLiteProcessNameKey
+ _kPPSLiteSampleTimeKey
+ _kPPSMMConfigLiteMode
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
- GCC_except_table57
- GCC_except_table64
- GCC_except_table69
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
