## MetricMeasurement

> `/System/Library/PrivateFrameworks/MetricMeasurement.framework/MetricMeasurement`

```diff

-297.100.9.0.0
-  __TEXT.__text: 0x1e58c
+297.100.10.0.0
+  __TEXT.__text: 0x1e538
   __TEXT.__auth_stubs: 0x850
   __TEXT.__objc_methlist: 0x28bc
   __TEXT.__const: 0x268
-  __TEXT.__cstring: 0x2625
-  __TEXT.__gcc_except_tab: 0x6f0
-  __TEXT.__oslogstring: 0x965
+  __TEXT.__cstring: 0x2613
+  __TEXT.__gcc_except_tab: 0x6f4
+  __TEXT.__oslogstring: 0x9d5
   __TEXT.__ustring: 0x34
   __TEXT.__unwind_info: 0x9c8
   __TEXT.__objc_classname: 0x5c5

   __DATA_CONST.__objc_superrefs: 0x108
   __AUTH_CONST.__auth_got: 0x438
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x27c0
+  __AUTH_CONST.__cfstring: 0x27a0
   __AUTH_CONST.__objc_const: 0x59d8
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH.__objc_data: 0xe60

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpmsample.dylib
   - /usr/lib/libsysmon.dylib
-  UUID: 47036F8B-5C69-3A0D-8DD0-67B867EBECBF
+  UUID: 7BD0723C-C7A7-34BA-B85D-41EE6C924706
   Functions: 870
   Symbols:   3257
-  CStrings:  1891
+  CStrings:  1889
 
Functions:
~ -[MXMEnergyMetric _convertMetricsToSampleData:] : 1580 -> 1616
~ -[MXMEnergyMetric appendMetricSample:name:tag:unit:conversionFactor:processName:pidNumber:toData:timestamp:] : 660 -> 644
~ -[MXMEnergyMetric harvestData:error:] : 832 -> 728
CStrings:
+ "MXMEnergyMetric: %@ skipped appending metric - value is negative (%.2f)"
+ "MXMEnergyMetric: Failed to setup PPSMetricMonitor."
+ "MXMEnergyMetric: MXMEnergyMetric requires at least one process to measure."
+ "MXMEnergyMetric: MXMEnergyMetric requires proxy mode."
+ "MXMEnergyMetric: No data collected."
+ "MXMEnergyMetric: No process metrics found for (%@)."
+ "MXMEnergyMetric: No process names found in filter."
+ "MXMEnergyMetric: No samples available to save."
- "%@ skipped - value is negative (%.2f)"
- "Failed to setup PPSMetricMonitor"
- "MXMEnergyMetric needs atleast one process to measure but processNames is nil/empty."
- "MXMEnergyMetric requires proxy mode"
- "No data collected"
- "No data collected. Nothing to harvest."
- "No process metrics available yet"
- "No process names found in filter"
- "No samples available to save."

```
