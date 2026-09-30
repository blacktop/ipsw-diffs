## MetricMeasurementHelper

> `/System/Library/PrivateFrameworks/MetricMeasurement.framework/XPCServices/MetricMeasurementHelper.xpc/MetricMeasurementHelper`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-361.0.0.0.0
-  __TEXT.__text: 0x58e8
+367.0.0.0.0
+  __TEXT.__text: 0x58f4
   __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_stubs: 0xe60
+  __TEXT.__objc_stubs: 0xe80
   __TEXT.__objc_methlist: 0x6cc
   __TEXT.__const: 0xb0
   __TEXT.__objc_classname: 0x229
-  __TEXT.__objc_methname: 0x111d
-  __TEXT.__objc_methtype: 0x5da
+  __TEXT.__objc_methname: 0x112e
+  __TEXT.__objc_methtype: 0x5de
   __TEXT.__cstring: 0x6e1
   __TEXT.__oslogstring: 0xa4e
   __TEXT.__gcc_except_tab: 0x118

   __DATA_CONST.__got: 0x148
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x1190
-  __DATA.__objc_selrefs: 0x568
+  __DATA.__objc_selrefs: 0x570
   __DATA.__objc_ivar: 0x64
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x4e0

   - /usr/lib/libsysmon.dylib
   Functions: 111
   Symbols:   186
-  CStrings:  416
+  CStrings:  417
 
Functions:
~ sub_10000201c : 188 -> 200
CStrings:
+ "collectLiteMetricsOnSnapshot:"
+ "setLiteMode:"
+ "v40@0:8@\"MXMProxyMetric\"16d24@?<v@?@\"PPSLiteMetricCollection\"Q@\"NSError\">32"
- "collectMetricsOnSnapshot:"
- "v40@0:8@\"MXMProxyMetric\"16d24@?<v@?@\"PPSMetricCollection\"Q@\"NSError\">32"
```
