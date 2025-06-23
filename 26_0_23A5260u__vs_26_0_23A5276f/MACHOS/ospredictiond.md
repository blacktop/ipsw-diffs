## ospredictiond

> `/usr/libexec/ospredictiond`

```diff

-198.0.0.0.1
-  __TEXT.__text: 0x59c44
-  __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_stubs: 0x85a0
-  __TEXT.__objc_methlist: 0x8670
+206.0.0.0.0
+  __TEXT.__text: 0x5a0d8
+  __TEXT.__auth_stubs: 0x7f0
+  __TEXT.__objc_stubs: 0x8500
+  __TEXT.__objc_methlist: 0x85b8
   __TEXT.__const: 0x2d8
-  __TEXT.__cstring: 0x499b
-  __TEXT.__objc_methname: 0x13649
-  __TEXT.__oslogstring: 0x51bf
-  __TEXT.__objc_classname: 0xcf8
-  __TEXT.__objc_methtype: 0x225d
-  __TEXT.__gcc_except_tab: 0x8d0
-  __TEXT.__unwind_info: 0x11b8
-  __DATA_CONST.__auth_got: 0x3f8
-  __DATA_CONST.__got: 0x3b0
-  __DATA_CONST.__const: 0xea0
-  __DATA_CONST.__cfstring: 0x5600
+  __TEXT.__cstring: 0x48c4
+  __TEXT.__objc_methname: 0x13257
+  __TEXT.__oslogstring: 0x529d
+  __TEXT.__objc_classname: 0xcfa
+  __TEXT.__objc_methtype: 0x21f6
+  __TEXT.__gcc_except_tab: 0x8dc
+  __TEXT.__unwind_info: 0x11e8
+  __DATA_CONST.__auth_got: 0x408
+  __DATA_CONST.__got: 0x3b8
+  __DATA_CONST.__const: 0xec0
+  __DATA_CONST.__cfstring: 0x54c0
   __DATA_CONST.__objc_classlist: 0x380
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x300
-  __DATA_CONST.__objc_arraydata: 0x13d8
+  __DATA_CONST.__objc_arraydata: 0x1378
   __DATA_CONST.__objc_arrayobj: 0x420
   __DATA_CONST.__objc_intobj: 0x1b0
   __DATA_CONST.__objc_dictobj: 0x140
-  __DATA.__objc_const: 0xf190
-  __DATA.__objc_selrefs: 0x3700
-  __DATA.__objc_ivar: 0xcec
+  __DATA_CONST.__objc_doubleobj: 0x60
+  __DATA.__objc_const: 0xef80
+  __DATA.__objc_selrefs: 0x3680
+  __DATA.__objc_ivar: 0xcc0
   __DATA.__objc_data: 0x2300
   __DATA.__data: 0x720
   __DATA.__bss: 0x1a0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7B61CCCA-7DD5-31EA-9C49-0B7DF396B658
-  Functions: 2975
-  Symbols:   249
-  CStrings:  5049
+  UUID: 828CF691-B232-310B-B34D-86E65B2D15C8
+  Functions: 2960
+  Symbols:   253
+  CStrings:  4996
 
Symbols:
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ ___NSArray0__struct
+ _random
+ _srandom
CStrings:
+ "12HourOnlyDrainBeforePercentileCategory"
+ "24HourOnlyDrainBeforePercentileCategory"
+ "24HourOnlyDrainBeforePercentileCategoryByUser"
+ "@48@0:8{_NSRange=QQ}16q32Q40"
+ "@60@0:8@16q24@32@40d48B56"
+ "Array count %ld"
+ "Array count %ld, less than look back index %ld for %ld days, returning unsliced array"
+ "Date %@, Slot %ld, battery level %ld"
+ "Not enough history for slicing last %d days data, available days: %lf days"
+ "PPS Response first %@: %@, last %@: %@, total %ld"
+ "PPS Response is %lu objects for startDate %@, endDate %@"
+ "Td,N,V__12HourOnlyDrainBeforePercentileCategory"
+ "Td,N,V__24HourOnlyDrainBeforePercentileCategory"
+ "Td,N,V__24HourOnlyDrainBeforePercentileCategoryByUser"
+ "Td,N,V_countsPast24hour_only_drain_before_90_last30Days"
+ "Td,N,V_countsPast24hour_only_drain_before_90_last7Days"
+ "Td,N,V_rolling30DaysAvgOf24hourOnlyDrainBefore"
+ "_12HourOnlyDrainBeforePercentileCategory"
+ "_24HourOnlyDrainBeforePercentileCategory"
+ "_24HourOnlyDrainBeforePercentileCategoryByUser"
+ "__12HourOnlyDrainBeforePercentileCategory"
+ "__24HourOnlyDrainBeforePercentileCategory"
+ "__24HourOnlyDrainBeforePercentileCategoryByUser"
+ "_countsPast24hour_only_drain_before_90_last30Days"
+ "_countsPast24hour_only_drain_before_90_last7Days"
+ "_rolling30DaysAvgOf24hourOnlyDrainBefore"
+ "countBatteryDrainIn:moreThanEqualTo:overPastDays:startingAtDate:endingAtDate:withDataSamplingInterval:"
+ "countsPast24hour_only_drain_before_90_last30Days"
+ "countsPast24hour_only_drain_before_90_last7Days"
+ "d56@0:8@16q24@32@40d48"
+ "durationPerIntervalFromBatteryTimeStampData:"
+ "generateRandomIntegersInRange:count:seed:"
+ "handleCallback:"
+ "initWithCurrentCapacity:drainOnly:_12hour_only_drain_before:_24hour_only_drain_before:_6hour_only_drain_before:_3hour_only_drain_before:total_drain_before:rolling_mean_24hour_drain_before:rolling_median_24hour_drain_before:rolling_mean_12hour_drain_before:rolling_median_12hour_drain_before:mean_12hour_drain_before:_24HourOnlyDrainBeforePercentileCategoryByUser:rolling30DaysAvgOf24hourOnlyDrainBefore:countsPast24hour_only_drain_before_90_last7Days:countsPast24hour_only_drain_before_90_last30Days:_12HourOnlyDrainBeforePercentileCategory:_24HourOnlyDrainBeforePercentileCategory:"
+ "meanOfRollingDrains:overPastDays:startingAtDate:endingAtDate:withDataSamplingInterval:"
+ "percentileCategoryForBatteryDrain:inRollingDrainData:"
+ "percentileCategoryForBatteryDrain:withFirstQuartile:withSecondQuartile:withThirdQuartile:"
+ "predictionFromCurrentCapacity:drainOnly:_12hour_only_drain_before:_24hour_only_drain_before:_6hour_only_drain_before:_3hour_only_drain_before:total_drain_before:rolling_mean_24hour_drain_before:rolling_median_24hour_drain_before:rolling_mean_12hour_drain_before:rolling_median_12hour_drain_before:mean_12hour_drain_before:_24HourOnlyDrainBeforePercentileCategoryByUser:rolling30DaysAvgOf24hourOnlyDrainBefore:countsPast24hour_only_drain_before_90_last7Days:countsPast24hour_only_drain_before_90_last30Days:_12HourOnlyDrainBeforePercentileCategory:_24HourOnlyDrainBeforePercentileCategory:error:"
+ "q32@0:8q16@24"
+ "q48@0:8q16@24@32@40"
+ "q64@0:8@16q24q32@40@48d56"
+ "rolling30DaysAvgOf24hourOnlyDrainBefore"
+ "setCountsPast24hour_only_drain_before_90_last30Days:"
+ "setCountsPast24hour_only_drain_before_90_last7Days:"
+ "setRolling30DaysAvgOf24hourOnlyDrainBefore:"
+ "set_12HourOnlyDrainBeforePercentileCategory:"
+ "set_24HourOnlyDrainBeforePercentileCategory:"
+ "set_24HourOnlyDrainBeforePercentileCategoryByUser:"
+ "sliceArray:overPastDays:startingAtDate:endingAtDate:withDataSamplingInterval:includeLastIndex:"
- "12hour_net_drain_before"
- "24hour_net_drain_before"
- "3hour_net_drain_before"
- "6hour_net_drain_before"
- "@256@0:8d16d24d32d40d48d56d64d72d80d88d96d104d112d120d128d136d144d152d160d168d176d184d192d200d208d216d224d232d240d248"
- "@264@0:8d16d24d32d40d48d56d64d72d80d88d96d104d112d120d128d136d144d152d160d168d176d184d192d200d208d216d224d232d240d248^@256"
- "Insufficient battery level data"
- "PPS Response first %@: %@, last %@: %@"
- "Slot %ld, battery level %ld"
- "Td,N,V_IsCharging"
- "Td,N,V_Model"
- "Td,N,V__12hour_net_drain_before"
- "Td,N,V__24hour_net_drain_before"
- "Td,N,V__3hour_net_drain_before"
- "Td,N,V__6hour_net_drain_before"
- "Td,N,V_rolling_mean_3hour_drain_before"
- "Td,N,V_rolling_mean_6hour_drain_before"
- "Td,N,V_rolling_median_3hour_drain_before"
- "Td,N,V_rolling_median_6hour_drain_before"
- "Td,N,V_rolling_std_12hour_drain_before"
- "Td,N,V_rolling_std_24hour_drain_before"
- "Td,N,V_rolling_std_3hour_drain_before"
- "Td,N,V_rolling_std_6hour_drain_before"
- "Td,N,V_rolling_var_12hour_drain_before"
- "Td,N,V_rolling_var_24hour_drain_before"
- "Td,N,V_rolling_var_3hour_drain_before"
- "Td,N,V_rolling_var_6hour_drain_before"
- "_12hour_net_drain_before"
- "_24hour_net_drain_before"
- "_3hour_net_drain_before"
- "_6hour_net_drain_before"
- "_IsCharging"
- "_Model"
- "__12hour_net_drain_before"
- "__24hour_net_drain_before"
- "__3hour_net_drain_before"
- "__6hour_net_drain_before"
- "_rolling_mean_3hour_drain_before"
- "_rolling_mean_6hour_drain_before"
- "_rolling_median_3hour_drain_before"
- "_rolling_median_6hour_drain_before"
- "_rolling_std_12hour_drain_before"
- "_rolling_std_24hour_drain_before"
- "_rolling_std_3hour_drain_before"
- "_rolling_std_6hour_drain_before"
- "_rolling_var_12hour_drain_before"
- "_rolling_var_24hour_drain_before"
- "_rolling_var_3hour_drain_before"
- "_rolling_var_6hour_drain_before"
- "initWithIsCharging:CurrentCapacity:Model:_12hour_net_drain_before:drainOnly:_12hour_only_drain_before:_24hour_only_drain_before:_6hour_only_drain_before:_3hour_only_drain_before:_24hour_net_drain_before:_6hour_net_drain_before:_3hour_net_drain_before:total_drain_before:rolling_mean_24hour_drain_before:rolling_median_24hour_drain_before:rolling_var_24hour_drain_before:rolling_std_24hour_drain_before:rolling_mean_12hour_drain_before:rolling_median_12hour_drain_before:rolling_var_12hour_drain_before:rolling_std_12hour_drain_before:rolling_mean_6hour_drain_before:rolling_median_6hour_drain_before:rolling_var_6hour_drain_before:rolling_std_6hour_drain_before:rolling_mean_3hour_drain_before:rolling_median_3hour_drain_before:rolling_var_3hour_drain_before:rolling_std_3hour_drain_before:mean_12hour_drain_before:"
- "predictionFromIsCharging:CurrentCapacity:Model:_12hour_net_drain_before:drainOnly:_12hour_only_drain_before:_24hour_only_drain_before:_6hour_only_drain_before:_3hour_only_drain_before:_24hour_net_drain_before:_6hour_net_drain_before:_3hour_net_drain_before:total_drain_before:rolling_mean_24hour_drain_before:rolling_median_24hour_drain_before:rolling_var_24hour_drain_before:rolling_std_24hour_drain_before:rolling_mean_12hour_drain_before:rolling_median_12hour_drain_before:rolling_var_12hour_drain_before:rolling_std_12hour_drain_before:rolling_mean_6hour_drain_before:rolling_median_6hour_drain_before:rolling_var_6hour_drain_before:rolling_std_6hour_drain_before:rolling_mean_3hour_drain_before:rolling_median_3hour_drain_before:rolling_var_3hour_drain_before:rolling_std_3hour_drain_before:mean_12hour_drain_before:error:"
- "rolling_mean_3hour_drain_before"
- "rolling_mean_6hour_drain_before"
- "rolling_median_3hour_drain_before"
- "rolling_median_6hour_drain_before"
- "rolling_std_12hour_drain_before"
- "rolling_std_24hour_drain_before"
- "rolling_std_3hour_drain_before"
- "rolling_std_6hour_drain_before"
- "rolling_var_12hour_drain_before"
- "rolling_var_24hour_drain_before"
- "rolling_var_3hour_drain_before"
- "rolling_var_6hour_drain_before"
- "setIsCharging:"
- "setModel:"
- "setRolling_mean_3hour_drain_before:"
- "setRolling_mean_6hour_drain_before:"
- "setRolling_median_3hour_drain_before:"
- "setRolling_median_6hour_drain_before:"
- "setRolling_std_12hour_drain_before:"
- "setRolling_std_24hour_drain_before:"
- "setRolling_std_3hour_drain_before:"
- "setRolling_std_6hour_drain_before:"
- "setRolling_var_12hour_drain_before:"
- "setRolling_var_24hour_drain_before:"
- "setRolling_var_3hour_drain_before:"
- "setRolling_var_6hour_drain_before:"
- "set_12hour_net_drain_before:"
- "set_24hour_net_drain_before:"
- "set_3hour_net_drain_before:"
- "set_6hour_net_drain_before:"

```
