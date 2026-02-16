## PerfPowerMetricMonitor

> `/System/Library/PrivateFrameworks/PerfPowerMetricMonitor.framework/PerfPowerMetricMonitor`

```diff

-2973.80.185.0.0
-  __TEXT.__text: 0x18378
-  __TEXT.__auth_stubs: 0x600
+3031.100.213.502.1
+  __TEXT.__text: 0x1a7c8
+  __TEXT.__auth_stubs: 0x5b0
   __TEXT.__objc_methlist: 0x14b4
   __TEXT.__const: 0xf8
-  __TEXT.__gcc_except_tab: 0x9a0
+  __TEXT.__gcc_except_tab: 0x984
   __TEXT.__cstring: 0xf2c
-  __TEXT.__oslogstring: 0x1b9a
+  __TEXT.__oslogstring: 0x1bae
   __TEXT.__ustring: 0x6c0
-  __TEXT.__unwind_info: 0x4d0
+  __TEXT.__unwind_info: 0x760
   __TEXT.__objc_classname: 0x185
-  __TEXT.__objc_methname: 0x3c60
-  __TEXT.__objc_methtype: 0x660
+  __TEXT.__objc_methname: 0x3c70
+  __TEXT.__objc_methtype: 0x66e
   __TEXT.__objc_stubs: 0x3140
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0x678

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x240
-  __AUTH_CONST.__auth_got: 0x310
+  __AUTH_CONST.__auth_got: 0x2e8
   __AUTH_CONST.__const: 0x1a0
   __AUTH_CONST.__cfstring: 0x1340
   __AUTH_CONST.__objc_const: 0x2128

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0EA3EFA5-367C-37D7-8E8E-E834799AE134
-  Functions: 587
-  Symbols:   2074
-  CStrings:  1269
+  UUID: 2E330F85-88EC-33B2-B2F7-BA693F0B82EB
+  Functions: 597
+  Symbols:   2103
+  CStrings:  1270
 
Symbols:
+ -[PPSMetricMonitorService _collectMetricsWithTimeout:forceCollection:]
+ -[PPSMetricMonitorService _collectMetricsWithTimeout:forceCollection:].cold.1
+ -[PPSMetricMonitorService _collectMetricsWithTimeout:forceCollection:].cold.2
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_9
+ ___70-[PPSMetricMonitorService _collectMetricsWithTimeout:forceCollection:]_block_invoke
+ ___70-[PPSMetricMonitorService _collectMetricsWithTimeout:forceCollection:]_block_invoke.cold.1
+ ___70-[PPSMetricMonitorService _collectMetricsWithTimeout:forceCollection:]_block_invoke.cold.2
+ _objc_msgSend$_collectMetricsWithTimeout:forceCollection:
+ _objc_retain_x28
- -[PPSMetricMonitorService _collectMetricsWithTimeout:]
- -[PPSMetricMonitorService _collectMetricsWithTimeout:].cold.1
- -[PPSMetricMonitorService _collectMetricsWithTimeout:].cold.2
- ___54-[PPSMetricMonitorService _collectMetricsWithTimeout:]_block_invoke
- ___54-[PPSMetricMonitorService _collectMetricsWithTimeout:]_block_invoke.cold.1
- ___54-[PPSMetricMonitorService _collectMetricsWithTimeout:]_block_invoke.cold.2
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_collectMetricsWithTimeout:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x25
- _objc_retain_x3
- _objc_retain_x4
CStrings:
+ "Collecting metrics with timeout %d, forceCollection %d"
+ "_collectMetricsWithTimeout:forceCollection:"
+ "v24@0:8i16B20"
- "Collecting metrics with timeout %d"
- "_collectMetricsWithTimeout:"

```
