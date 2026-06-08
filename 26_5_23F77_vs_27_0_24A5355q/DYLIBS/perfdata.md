## perfdata

> `/System/Library/PrivateFrameworks/perfdata.framework/perfdata`

```diff

-130.0.0.0.0
-  __TEXT.__text: 0x7ef8
-  __TEXT.__auth_stubs: 0x730
+135.0.0.0.0
+  __TEXT.__text: 0x779c
   __TEXT.__objc_methlist: 0x680
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0xfe8
+  __TEXT.__cstring: 0x103c
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0x2e8
-  __TEXT.__objc_classname: 0x73
-  __TEXT.__objc_methname: 0x12a0
-  __TEXT.__objc_methtype: 0x208
-  __TEXT.__objc_stubs: 0x10e0
-  __DATA_CONST.__got: 0xb0
+  __TEXT.__unwind_info: 0x228
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xe80
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x520
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x3a8
+  __DATA_CONST.__got: 0xb0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0xa60
   __AUTH_CONST.__objc_const: 0xbb0
+  __AUTH_CONST.__auth_got: 0x3c8
   __DATA.__objc_ivar: 0xb8
   __DATA.__data: 0x90
   __DATA.__bss: 0x10

   - /usr/lib/libSMC.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 942A4F85-DB52-32A1-B49E-1A7FC5438A52
-  Functions: 228
-  Symbols:   1253
-  CStrings:  806
+  UUID: 8105D9C5-93C6-34C2-A5EC-C70567222FFB
+  Functions: 233
+  Symbols:   1265
+  CStrings:  518
 
Symbols:
+ _emit_lazy_fields
+ _emit_local_time_field
+ _gettimeofday
+ _localtime_r
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x3
+ _pdwriter_set_end_date
+ _pdwriter_set_end_date.cold.1
+ _pdwriter_set_start_date
+ _pdwriter_set_start_date.cold.1
- _emit_curtime_field
- _gmtime
- _objc_retain_x28
- _time
CStrings:
+ "%FT%T.%%06llu%z"
+ "135"
+ "end_date has already been set"
+ "start_date has already been set"
- "%FT%TZ"
- ".cxx_destruct"
- "130"
- "@\"NSDictionary\""
- "@\"NSMutableDictionary\""
- "@\"NSNumber\""
- "@\"NSString\""
- "@\"PDContainer\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16^@24"
- "@40@0:8@16@24@32"
- "@48@0:8@16@24Q32^@40"
- "B16@0:8"
- "B24@0:8@16"
- "B28@0:8@16B24"
- "B32@0:8@16@24"
- "B32@0:8^@16@?24"
- "B40@0:8@16^@24@?32"
- "B48@0:8@16@24^@32@?40"
- "JSONObjectWithData:options:error:"
- "JSONObjectWithStream:options:error:"
- "PDAggregateMeasurement"
- "PDBucket"
- "PDContainer"
- "PDContainerAdditions"
- "PDMeasurement"
- "PDMeasurementAdditions"
- "Q"
- "Q16@0:8"
- "T@\"NSDictionary\",&,N,V_configuration"
- "T@\"NSDictionary\",&,N,V_labels"
- "T@\"NSDictionary\",&,N,V_measurement"
- "T@\"NSDictionary\",&,N,V_variables"
- "T@\"NSMutableDictionary\",&,N,V_extensions"
- "T@\"NSMutableDictionary\",&,N,V_labels"
- "T@\"NSMutableDictionary\",&,N,V_perfdata"
- "T@\"NSMutableDictionary\",&,N,V_variables"
- "T@\"NSNumber\",&,N,V_maximum"
- "T@\"NSNumber\",&,N,V_mean"
- "T@\"NSNumber\",&,N,V_minimum"
- "T@\"NSNumber\",&,N,V_sampleCount"
- "T@\"NSNumber\",&,N,V_standardDeviation"
- "T@\"NSNumber\",&,N,V_value"
- "T@\"NSString\",&,N"
- "T@\"NSString\",&,N,V_cachedMetricFilter"
- "T@\"NSString\",&,N,V_generator"
- "T@\"NSString\",&,N,V_label"
- "T@\"NSString\",&,N,V_metric"
- "T@\"NSString\",&,N,V_name"
- "T@\"NSString\",&,N,V_notes"
- "T@\"NSString\",&,N,V_primaryMetricFilter"
- "T@\"NSString\",&,N,V_testDescription"
- "T@\"NSString\",&,N,V_unitString"
- "T@\"PDContainer\",&,N,V_container"
- "T@\"PDContainer\",W,N,V_container"
- "T@\"PDMeasurement\",R,N"
- "TB,N"
- "TB,N,GisContext,V_context"
- "TB,N,GisSummary,V_summary"
- "TB,N,V_hasInclusiveUpperBound"
- "TB,N,V_largerBetter"
- "TB,N,V_validMax"
- "TB,N,V_validMin"
- "TQ,N"
- "TQ,N,V_count"
- "TQ,N,V_group"
- "TQ,N,V_samples"
- "TQ,N,V_version"
- "TQ,R,N"
- "T^{pooled_mean={sum=dd}{sum=dd}QQ},N,V_stats_mean"
- "T^{running_mean=ddQ},N,V_values_mean"
- "Td,N"
- "Td,N,V_lowerInclusiveBound"
- "Td,N,V_max"
- "Td,N,V_min"
- "Td,N,V_upperBound"
- "UTF8String"
- "^{pooled_mean={sum=dd}{sum=dd}QQ}"
- "^{pooled_mean={sum=dd}{sum=dd}QQ}16@0:8"
- "^{running_mean=ddQ}"
- "^{running_mean=ddQ}16@0:8"
- "_cachedMetricFilter"
- "_configuration"
- "_container"
- "_context"
- "_count"
- "_extensions"
- "_generator"
- "_group"
- "_hasInclusiveUpperBound"
- "_label"
- "_labels"
- "_largerBetter"
- "_lowerInclusiveBound"
- "_max"
- "_maximum"
- "_mean"
- "_measurement"
- "_metric"
- "_min"
- "_minimum"
- "_name"
- "_notes"
- "_perfdata"
- "_primaryMetricFilter"
- "_sampleCount"
- "_samples"
- "_standardDeviation"
- "_stats_mean"
- "_summary"
- "_testDescription"
- "_unitString"
- "_upperBound"
- "_validMax"
- "_validMin"
- "_value"
- "_values_mean"
- "_variables"
- "_version"
- "addObject:"
- "aggregateMeasurementsMatchingFilter:error:"
- "allKeys"
- "appendFormat:"
- "boolValue"
- "bytes"
- "cachedMetricFilter"
- "close"
- "compare:"
- "componentsSeparatedByString:"
- "container"
- "containerWithFileURL:error:"
- "containerWithJSONData:error:"
- "containerWithJSONDictionary:error:"
- "containerWithPath:error:"
- "containsObject:"
- "countByEnumeratingWithState:objects:count:"
- "d"
- "d16@0:8"
- "dealloc"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "doubleValue"
- "enumerateAggregatedMeasurementsIgnoringVariables:error:usingBlock:"
- "enumerateAggregatedMeasurementsMatchingFilter:ignoringVariables:error:usingBlock:"
- "enumerateAggregatedMeasurementsMatchingNullableFilter:ignoringVariables:error:usingBlock:"
- "enumerateHistogramBucketsWithError:usingBlock:"
- "enumerateMeasurementsMatchingFilter:error:usingBlock:"
- "enumerateMeasurementsMatchingNullableFilter:error:usingBlock:"
- "enumerateMeasurementsWithError:usingBlock:"
- "enumeratePercentilesWithError:usingBlock:"
- "errorWithDomain:code:userInfo:"
- "fileURLWithPath:isDirectory:"
- "group"
- "hasInclusiveUpperBound"
- "hasPrefix:"
- "histogramBucketCount"
- "init"
- "initWithContainer:dictionary:group:error:"
- "initWithContainer:metric:unitString:"
- "initWithDictionary:error:"
- "initWithFileURL:error:"
- "initWithJSONData:error:"
- "initWithJSONDictionary:error:"
- "initWithPath:error:"
- "inputStreamWithFileAtPath:"
- "inputStreamWithURL:"
- "intValue"
- "isComparableTo:"
- "isComparableTo:ignoringNullableVariables:"
- "isComparableTo:ignoringVariables:"
- "isContext"
- "isEqual:"
- "isEqualToDictionary:"
- "isEqualToString:"
- "isLike:"
- "isSummary"
- "largerBetter"
- "length"
- "lowerInclusiveBound"
- "matchesMetricFilter:"
- "matchesVariables:ignoringMissing:"
- "max"
- "measurement"
- "measurementCount"
- "metricFilter"
- "metricFilterIgnoringNullableVariables:"
- "metricFilterIgnoringVariables:"
- "min"
- "mutableCopy"
- "numberFromString:"
- "numberWithDouble:"
- "numberWithUnsignedLongLong:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "open"
- "percentileCount"
- "perfdata"
- "primaryMetricFilter"
- "propertyListWithStream:options:format:error:"
- "rangeOfString:"
- "removeObjectForKey:"
- "removeObjectsForKeys:"
- "sampleCount"
- "setCachedMetricFilter:"
- "setConfiguration:"
- "setContainer:"
- "setContext:"
- "setCount:"
- "setExtensions:"
- "setGenerator:"
- "setGroup:"
- "setHasInclusiveUpperBound:"
- "setLabel:"
- "setLabels:"
- "setLargerBetter:"
- "setLowerInclusiveBound:"
- "setMax:"
- "setMaximum:"
- "setMean:"
- "setMeasurement:"
- "setMetric:"
- "setMin:"
- "setMinimum:"
- "setName:"
- "setNotes:"
- "setNumberStyle:"
- "setObject:forKeyedSubscript:"
- "setPerfdata:"
- "setPrimaryMetricFilter:"
- "setSampleCount:"
- "setSamples:"
- "setStandardDeviation:"
- "setStats_mean:"
- "setSummary:"
- "setTestDescription:"
- "setUnitString:"
- "setUpperBound:"
- "setValidMax:"
- "setValidMin:"
- "setValue:"
- "setValue:forKey:"
- "setValuesForKeysWithDictionary:"
- "setValues_mean:"
- "setVariables:"
- "setVersion:"
- "setWithObject:"
- "setWithSet:"
- "sortedArrayUsingSelector:"
- "standardDeviation"
- "stats_mean"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "subarrayWithRange:"
- "substringWithRange:"
- "testDescription"
- "unionSet:"
- "unitString"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "updateWithMeasurement:"
- "upperBound"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8^{pooled_mean={sum=dd}{sum=dd}QQ}16"
- "v24@0:8^{running_mean=ddQ}16"
- "v24@0:8d16"
- "validMax"
- "validMin"
- "values_mean"

```
