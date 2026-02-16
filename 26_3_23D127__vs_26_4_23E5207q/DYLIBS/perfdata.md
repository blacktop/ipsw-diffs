## perfdata

> `/System/Library/PrivateFrameworks/perfdata.framework/perfdata`

```diff

-122.0.0.0.0
-  __TEXT.__text: 0x75dc
-  __TEXT.__auth_stubs: 0x760
+129.0.0.0.0
+  __TEXT.__text: 0x7ef8
+  __TEXT.__auth_stubs: 0x730
   __TEXT.__objc_methlist: 0x680
   __TEXT.__const: 0x60
   __TEXT.__cstring: 0xfe8
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0x220
+  __TEXT.__unwind_info: 0x2e8
   __TEXT.__objc_classname: 0x73
   __TEXT.__objc_methname: 0x12a0
   __TEXT.__objc_methtype: 0x208

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x520
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x3c0
+  __AUTH_CONST.__auth_got: 0x3a8
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0xa60
   __AUTH_CONST.__objc_const: 0xbb0

   - /usr/lib/libSMC.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7D6E06C2-F5FA-3BBD-A126-F34A2A295F2A
+  UUID: F5F2BC7F-426F-36CD-9C01-2B26C248B6A3
   Functions: 228
-  Symbols:   1256
+  Symbols:   1253
   CStrings:  806
 
Symbols:
+ _objc_retain_x23
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x2
- _objc_retain_x24
- _objc_retain_x25
- _objc_retain_x3
Functions:
~ _config_emit : 2340 -> 2368
~ _json_printf_s : 344 -> 360
~ _json_value_dbl : 84 -> 80
~ _json_value_int : 48 -> 44
~ _json_value_uint : 48 -> 44
~ _json_value_bool : 72 -> 68
~ _json_member_int : 104 -> 100
~ _json_member_uint : 104 -> 100
~ _json_member_bool : 136 -> 132
~ -[PDAggregateMeasurement initWithContainer:metric:unitString:] : 312 -> 304
~ -[PDAggregateMeasurement updateWithMeasurement:] : 1776 -> 1936
~ -[PDAggregateMeasurement measurement] : 1072 -> 1136
~ -[PDAggregateMeasurement setLabels:] : 12 -> 64
~ -[PDAggregateMeasurement setContainer:] : 12 -> 64
~ -[PDAggregateMeasurement setMetric:] : 12 -> 64
~ -[PDAggregateMeasurement setUnitString:] : 12 -> 64
~ -[PDAggregateMeasurement setVariables:] : 12 -> 64
~ _handle_malformed_data : 220 -> 228
~ -[PDMeasurement(PDContainerAdditions) initWithContainer:dictionary:group:error:] : 2324 -> 2496
~ _not_a_number : 136 -> 132
~ -[PDContainer initWithPath:error:] : 96 -> 100
~ -[PDContainer initWithFileURL:error:] : 244 -> 248
~ -[PDContainer initWithJSONDictionary:error:] : 1596 -> 1752
~ _expect_dictionary : 180 -> 184
~ -[PDContainer description] : 128 -> 136
~ -[PDContainer isComparableTo:] : 148 -> 156
~ -[PDContainer enumerateMeasurementsMatchingNullableFilter:error:usingBlock:] : 1072 -> 1084
~ -[PDContainer enumerateAggregatedMeasurementsMatchingNullableFilter:ignoringVariables:error:usingBlock:] : 596 -> 584
~ ___104-[PDContainer enumerateAggregatedMeasurementsMatchingNullableFilter:ignoringVariables:error:usingBlock:]_block_invoke : 284 -> 312
~ -[PDContainer aggregateMeasurementsMatchingFilter:error:] : 312 -> 316
~ ___57-[PDContainer aggregateMeasurementsMatchingFilter:error:]_block_invoke : 220 -> 228
~ -[PDContainer setName:] : 12 -> 64
~ -[PDContainer setConfiguration:] : 12 -> 64
~ -[PDContainer setExtensions:] : 12 -> 64
~ -[PDContainer setTestDescription:] : 12 -> 64
~ -[PDContainer setNotes:] : 12 -> 64
~ -[PDContainer setPrimaryMetricFilter:] : 12 -> 64
~ -[PDContainer setGenerator:] : 12 -> 64
~ -[PDContainer setVariables:] : 12 -> 64
~ -[PDContainer setLabels:] : 12 -> 64
~ -[PDContainer setPerfdata:] : 12 -> 64
~ -[PDBucket(PDMeasurementAdditions) initWithDictionary:error:] : 472 -> 504
~ _strip_container_prefix : 220 -> 236
~ _get_metric_filter_metric : 116 -> 128
~ _get_metric_filter_variables : 728 -> 760
~ -[PDMeasurement description] : 140 -> 152
~ -[PDMeasurement matchesMetricFilter:] : 228 -> 248
~ -[PDMeasurement matchesVariables:ignoringMissing:] : 384 -> 392
~ -[PDMeasurement metricFilter] : 108 -> 116
~ -[PDMeasurement metricFilterIgnoringNullableVariables:] : 496 -> 528
~ -[PDMeasurement isComparableTo:ignoringNullableVariables:] : 376 -> 404
~ -[PDMeasurement histogramBucketCount] : 272 -> 284
~ -[PDMeasurement enumerateHistogramBucketsWithError:usingBlock:] : 856 -> 860
~ -[PDMeasurement percentileCount] : 124 -> 132
~ -[PDMeasurement enumeratePercentilesWithError:usingBlock:] : 720 -> 740
~ -[PDMeasurement setMetric:] : 12 -> 64
~ -[PDMeasurement setUnitString:] : 12 -> 64
~ -[PDMeasurement setVariables:] : 12 -> 64
~ -[PDMeasurement setLabels:] : 12 -> 64
~ -[PDMeasurement setValue:] : 12 -> 64
~ -[PDMeasurement setSampleCount:] : 12 -> 64
~ -[PDMeasurement setMean:] : 12 -> 64
~ -[PDMeasurement setStandardDeviation:] : 12 -> 64
~ -[PDMeasurement setMinimum:] : 12 -> 64
~ -[PDMeasurement setMaximum:] : 12 -> 64
~ -[PDMeasurement setMeasurement:] : 12 -> 64
~ -[PDMeasurement setCachedMetricFilter:] : 12 -> 64
~ -[PDBucket setLabel:] : 12 -> 64
CStrings:
+ "129"
- "122"

```
