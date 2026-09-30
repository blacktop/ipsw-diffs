## HealthActivityCache

> `/System/Library/Health/Plugins/HealthActivityCache.bundle/HealthActivityCache`

```diff

-5200.5.1.0.0
-  __TEXT.__text: 0x1fc18
+6074.1.2.4.0
+  __TEXT.__text: 0x219e4
   __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_stubs: 0x2fe0
-  __TEXT.__objc_methlist: 0xbcc
-  __TEXT.__cstring: 0xa1d
-  __TEXT.__objc_classname: 0x376
-  __TEXT.__objc_methtype: 0x1f51
+  __TEXT.__objc_stubs: 0x30c0
+  __TEXT.__objc_methlist: 0xc4c
+  __TEXT.__cstring: 0xa3d
+  __TEXT.__objc_classname: 0x38f
+  __TEXT.__objc_methtype: 0x1840
   __TEXT.__const: 0x98
-  __TEXT.__objc_methname: 0x3d43
-  __TEXT.__oslogstring: 0xc8b
-  __TEXT.__gcc_except_tab: 0x31e0
-  __TEXT.__unwind_info: 0xde0
+  __TEXT.__objc_methname: 0x3fe6
+  __TEXT.__oslogstring: 0xe05
+  __TEXT.__gcc_except_tab: 0x3280
+  __TEXT.__unwind_info: 0xe30
   __DATA_CONST.__auth_got: 0x370
-  __DATA_CONST.__got: 0x480
-  __DATA_CONST.__const: 0x550
-  __DATA_CONST.__cfstring: 0x5a0
+  __DATA_CONST.__got: 0x490
+  __DATA_CONST.__const: 0x578
+  __DATA_CONST.__cfstring: 0x5c0
   __DATA_CONST.__objc_classlist: 0x78
-  __DATA_CONST.__objc_protolist: 0x68
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x2370
-  __DATA.__objc_selrefs: 0xe68
-  __DATA.__objc_ivar: 0x23c
+  __DATA.__objc_const: 0x2448
+  __DATA.__objc_selrefs: 0xec8
+  __DATA.__objc_ivar: 0x24c
   __DATA.__objc_data: 0x4b0
-  __DATA.__data: 0x4f8
+  __DATA.__data: 0x558
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 4517F09B-863D-3A38-9A37-35924E0FB60F
-  Functions: 570
-  Symbols:   331
-  CStrings:  953
+  UUID: 9DB63C98-B842-3C5A-A8A2-695265481124
+  Functions: 576
+  Symbols:   333
+  CStrings:  989
 
Symbols:
+ _OBJC_CLASS_$_HDMutableDatabaseTransactionContext
+ _OBJC_CLASS_$_HKHeartRateSummarySleepStatistics
+ __ZnwmSt19__type_descriptor_t
- __Znwm
CStrings:
+ "@\"HDAssertion\""
+ "@\"HKHeartRateSummarySleepStatistics\""
+ "Activity Cache Update"
+ "B16@?0^@8"
+ "Error obtaining database access assertion during active workout: %{public}@"
+ "Error performing transaction with context: %{public}@"
+ "HDCurrentWorkoutObserver"
+ "Updating caches"
+ "Using accessibility assertion context to update caches"
+ "Workout is active taking accessibility assertion to update caches"
+ "Workout manager did update current workout: %{public}@"
+ "Workout no longer active, invalidating access assertion"
+ "_isPeripheralSource"
+ "_isPeripheralSourceCache"
+ "_sleepStatistics"
+ "_workoutAccessAssertion"
+ "_workoutIsActive"
+ "associationsUpdatedForObject:subObject:type:behavior:objects:anchor:"
+ "contextForAccessibilityAssertion:"
+ "heartRate_reportDailyRestingHeartRate:sedentaryHeartRateCount:filteredSedentaryHeartRateCount:hasTimeAsleep:hasBGHRSleepMode:unfilteredRestingHeartRate:profileType:"
+ "initWithActivityCacheIndex:heartRateDateInterval:restingHeartRate:walkingAverageHeartRate:allDayStatistics:workoutStatistics:workoutRecoveryStatistics:breatheStatistics:sleepStatistics:"
+ "invalidateAndWait"
+ "isImprovedHealthAndActivityEnabled"
+ "performWithTransactionContext:error:block:"
+ "registerCurrentWorkoutObserver:"
+ "removeObserver:name:object:"
+ "setHasBGHRSleepMode:"
+ "takeAccessibilityAssertionWithOwnerIdentifier:contextType:error:"
+ "unregisterCurrentWorkoutObserver:"
+ "v32@0:8@\"HDWorkoutManager\"16@\"HDWorkoutSessionServer\"24"
+ "v40@0:8@\"HDWorkoutManager\"16@\"HDWorkoutSessionServer\"24@\"<HDWorkoutDataAccumulator>\"32"
+ "v40@0:8@\"HDWorkoutManager\"16@\"HDWorkoutSessionServer\"24q32"
+ "v40@0:8@16@24@32"
+ "v40@0:8@16@24q32"
+ "v64@0:8@\"<HKAssociatableObject>\"16@\"<HKAssociatableObject>\"24Q32Q40@\"NSArray\"48@\"NSNumber\"56"
+ "v64@0:8@16@24Q32Q40@48@56"
+ "workoutManager"
+ "workoutManager:currentWorkout:didChangeToState:"
+ "workoutManager:currentWorkout:didUpdateDataAccumulator:"
+ "workoutManager:didUpdateCurrentWorkout:"
+ "{HDActivityCacheActiveSource=dq{vector<long long, std::allocator<long long>>=^q^q^q}}16@0:8"
+ "{map<_HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>, std::less<_HKDataTypeCode>, std::allocator<std::pair<const _HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>>>>=\"__tree_\"{__tree<std::__value_type<_HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>>, std::__map_value_compare<_HKDataTypeCode, std::__value_type<_HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>>, std::less<_HKDataTypeCode>>, std::allocator<std::__value_type<_HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
+ "{unordered_map<long long, bool, std::hash<long long>, std::equal_to<long long>, std::allocator<std::pair<const long long, bool>>>=\"__table_\"{__hash_table<std::__hash_value_type<long long, bool>, std::__unordered_map_hasher<long long, std::__hash_value_type<long long, bool>, std::hash<long long>, std::equal_to<long long>>, std::__unordered_map_equal<long long, std::__hash_value_type<long long, bool>, std::equal_to<long long>, std::hash<long long>>, std::allocator<std::__hash_value_type<long long, bool>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{vector<HDActivityCacheActiveSource, std::allocator<HDActivityCacheActiveSource>>=\"__begin_\"^{HDActivityCacheActiveSource}\"__end_\"^{HDActivityCacheActiveSource}\"__cap_\"^{HDActivityCacheActiveSource}}"
+ "{vector<HDActivityCacheActiveSource, std::allocator<HDActivityCacheActiveSource>>=^{HDActivityCacheActiveSource}^{HDActivityCacheActiveSource}^{HDActivityCacheActiveSource}}16@0:8"
+ "{vector<HDActivityCacheHeartRateStatisticsBuilderHeartRateSample, std::allocator<HDActivityCacheHeartRateStatisticsBuilderHeartRateSample>>=\"__begin_\"^{HDActivityCacheHeartRateStatisticsBuilderHeartRateSample}\"__end_\"^{HDActivityCacheHeartRateStatisticsBuilderHeartRateSample}\"__cap_\"^{HDActivityCacheHeartRateStatisticsBuilderHeartRateSample}}"
+ "{vector<HDActivityCacheStatisticsBuilderSample, std::allocator<HDActivityCacheStatisticsBuilderSample>>=\"__begin_\"^{HDActivityCacheStatisticsBuilderSample}\"__end_\"^{HDActivityCacheStatisticsBuilderSample}\"__cap_\"^{HDActivityCacheStatisticsBuilderSample}}"
+ "{vector<HDActivityCacheStatisticsBuilderStandHourSample, std::allocator<HDActivityCacheStatisticsBuilderStandHourSample>>=\"__begin_\"^{HDActivityCacheStatisticsBuilderStandHourSample}\"__end_\"^{HDActivityCacheStatisticsBuilderStandHourSample}\"__cap_\"^{HDActivityCacheStatisticsBuilderStandHourSample}}"
+ "{vector<HDActivityCacheStatisticsBuilderWorkoutSample, std::allocator<HDActivityCacheStatisticsBuilderWorkoutSample>>=\"__begin_\"^{HDActivityCacheStatisticsBuilderWorkoutSample}\"__end_\"^{HDActivityCacheStatisticsBuilderWorkoutSample}\"__cap_\"^{HDActivityCacheStatisticsBuilderWorkoutSample}}"
+ "\xf0\xf0\xe1"
- "_isBTLEServer"
- "heartRate_reportDailyRestingHeartRate:sedentaryHeartRateCount:filteredSedentaryHeartRateCount:profileType:"
- "initWithActivityCacheIndex:heartRateDateInterval:restingHeartRate:walkingAverageHeartRate:allDayStatistics:workoutStatistics:workoutRecoveryStatistics:breatheStatistics:"
- "pauseRings"
- "scheduledGoals"
- "{HDActivityCacheActiveSource=dq{vector<long long, std::allocator<long long>>=^q^q{__compressed_pair<long long *, std::allocator<long long>>=^q}}}16@0:8"
- "{map<_HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>, std::less<_HKDataTypeCode>, std::allocator<std::pair<const _HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>>>>=\"__tree_\"{__tree<std::__value_type<_HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>>, std::__map_value_compare<_HKDataTypeCode, std::__value_type<_HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>>, std::less<_HKDataTypeCode>>, std::allocator<std::__value_type<_HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>>>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<_HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>>, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<_HKDataTypeCode, std::__value_type<_HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>>, std::less<_HKDataTypeCode>>>=\"__value_\"Q}}}"
- "{unordered_map<long long, bool, std::hash<long long>, std::equal_to<long long>, std::allocator<std::pair<const long long, bool>>>=\"__table_\"{__hash_table<std::__hash_value_type<long long, bool>, std::__unordered_map_hasher<long long, std::__hash_value_type<long long, bool>, std::hash<long long>, std::equal_to<long long>>, std::__unordered_map_equal<long long, std::__hash_value_type<long long, bool>, std::equal_to<long long>, std::hash<long long>>, std::allocator<std::__hash_value_type<long long, bool>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<long long, bool>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<long long, std::__hash_value_type<long long, bool>, std::hash<long long>, std::equal_to<long long>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<long long, std::__hash_value_type<long long, bool>, std::equal_to<long long>, std::hash<long long>>>=\"__value_\"f}}}"
- "{vector<HDActivityCacheActiveSource, std::allocator<HDActivityCacheActiveSource>>=\"__begin_\"^{HDActivityCacheActiveSource}\"__end_\"^{HDActivityCacheActiveSource}\"__end_cap_\"{__compressed_pair<HDActivityCacheActiveSource *, std::allocator<HDActivityCacheActiveSource>>=\"__value_\"^{HDActivityCacheActiveSource}}}"
- "{vector<HDActivityCacheActiveSource, std::allocator<HDActivityCacheActiveSource>>=^{HDActivityCacheActiveSource}^{HDActivityCacheActiveSource}{__compressed_pair<HDActivityCacheActiveSource *, std::allocator<HDActivityCacheActiveSource>>=^{HDActivityCacheActiveSource}}}16@0:8"
- "{vector<HDActivityCacheHeartRateStatisticsBuilderHeartRateSample, std::allocator<HDActivityCacheHeartRateStatisticsBuilderHeartRateSample>>=\"__begin_\"^{HDActivityCacheHeartRateStatisticsBuilderHeartRateSample}\"__end_\"^{HDActivityCacheHeartRateStatisticsBuilderHeartRateSample}\"__end_cap_\"{__compressed_pair<HDActivityCacheHeartRateStatisticsBuilderHeartRateSample *, std::allocator<HDActivityCacheHeartRateStatisticsBuilderHeartRateSample>>=\"__value_\"^{HDActivityCacheHeartRateStatisticsBuilderHeartRateSample}}}"
- "{vector<HDActivityCacheStatisticsBuilderSample, std::allocator<HDActivityCacheStatisticsBuilderSample>>=\"__begin_\"^{HDActivityCacheStatisticsBuilderSample}\"__end_\"^{HDActivityCacheStatisticsBuilderSample}\"__end_cap_\"{__compressed_pair<HDActivityCacheStatisticsBuilderSample *, std::allocator<HDActivityCacheStatisticsBuilderSample>>=\"__value_\"^{HDActivityCacheStatisticsBuilderSample}}}"
- "{vector<HDActivityCacheStatisticsBuilderStandHourSample, std::allocator<HDActivityCacheStatisticsBuilderStandHourSample>>=\"__begin_\"^{HDActivityCacheStatisticsBuilderStandHourSample}\"__end_\"^{HDActivityCacheStatisticsBuilderStandHourSample}\"__end_cap_\"{__compressed_pair<HDActivityCacheStatisticsBuilderStandHourSample *, std::allocator<HDActivityCacheStatisticsBuilderStandHourSample>>=\"__value_\"^{HDActivityCacheStatisticsBuilderStandHourSample}}}"
- "{vector<HDActivityCacheStatisticsBuilderWorkoutSample, std::allocator<HDActivityCacheStatisticsBuilderWorkoutSample>>=\"__begin_\"^{HDActivityCacheStatisticsBuilderWorkoutSample}\"__end_\"^{HDActivityCacheStatisticsBuilderWorkoutSample}\"__end_cap_\"{__compressed_pair<HDActivityCacheStatisticsBuilderWorkoutSample *, std::allocator<HDActivityCacheStatisticsBuilderWorkoutSample>>=\"__value_\"^{HDActivityCacheStatisticsBuilderWorkoutSample}}}"
- "\xf0\xf0\x91"

```
