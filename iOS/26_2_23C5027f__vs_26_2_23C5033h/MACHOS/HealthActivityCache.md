## HealthActivityCache

> `/System/Library/Health/Plugins/HealthActivityCache.bundle/HealthActivityCache`

```diff

-6200.3.4.0.0
-  __TEXT.__text: 0x21858
+6200.3.8.0.0
+  __TEXT.__text: 0x218d4
   __TEXT.__auth_stubs: 0x6b0
   __TEXT.__objc_stubs: 0x3060
   __TEXT.__objc_methlist: 0xc54
   __TEXT.__cstring: 0xa3d
   __TEXT.__objc_classname: 0x38f
-  __TEXT.__objc_methtype: 0x1805
+  __TEXT.__objc_methtype: 0x1855
   __TEXT.__const: 0x98
   __TEXT.__objc_methname: 0x3f97
   __TEXT.__oslogstring: 0xe05
-  __TEXT.__gcc_except_tab: 0x320c
+  __TEXT.__gcc_except_tab: 0x3214
   __TEXT.__unwind_info: 0xe50
   __DATA_CONST.__auth_got: 0x370
   __DATA_CONST.__got: 0x490

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 75F28B1E-F1FB-3550-BBC5-001140EFCCE9
+  UUID: A3115C9C-4A57-38A8-BFD1-89B59F877B9B
   Functions: 576
   Symbols:   333
   CStrings:  986
Functions:
~ sub_3884 : 1040 -> 1044
~ sub_9cf8 -> sub_9cfc : 1492 -> 1500
~ sub_a558 -> sub_a564 : 60 -> 64
~ sub_a7e4 -> sub_a7f4 : 60 -> 64
~ sub_a868 -> sub_a87c : 372 -> 376
~ sub_aa1c -> sub_aa34 : 76 -> 80
~ sub_adc0 -> sub_addc : 76 -> 80
~ sub_c69c -> sub_c6bc : 328 -> 332
~ sub_c9d8 -> sub_c9fc : 328 -> 332
~ sub_feb4 -> sub_fedc : 1704 -> 1736
~ sub_11f10 -> sub_11f58 : 472 -> 476
~ sub_12a84 -> sub_12ad0 : 60 -> 64
~ sub_12d44 -> sub_12d94 : 76 -> 80
~ sub_187c4 -> sub_18818 : 728 -> 732
~ sub_1abc0 -> sub_1ac18 : 328 -> 332
~ sub_1ccac -> sub_1cd08 : 220 -> 236
~ sub_1cd88 -> sub_1cdf4 : 464 -> 460
~ sub_1d0a4 -> sub_1d10c : 188 -> 192
~ sub_1f83c -> sub_1f8a8 : 168 -> 176
~ sub_20bbc -> sub_20c30 : 92 -> 88
~ sub_21aa0 -> sub_21b10 : 148 -> 156
~ sub_21c08 -> sub_21c80 : 120 -> 116
~ sub_225b0 -> sub_22624 : 80 -> 88
CStrings:
+ "{HDActivityCacheActiveSource=dq{vector<long long, std::allocator<long long>>=^q^q{?=^q}}}16@0:8"
+ "{map<_HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>, std::less<_HKDataTypeCode>, std::allocator<std::pair<const _HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>>>>=\"__tree_\"{__tree<std::__value_type<_HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>>, std::__map_value_compare<_HKDataTypeCode, std::__value_type<_HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>>, std::less<_HKDataTypeCode>>, std::allocator<std::__value_type<_HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{unordered_map<long long, bool, std::hash<long long>, std::equal_to<long long>, std::allocator<std::pair<const long long, bool>>>=\"__table_\"{__hash_table<std::__hash_value_type<long long, bool>, std::__unordered_map_hasher<long long, std::__hash_value_type<long long, bool>, std::hash<long long>, std::equal_to<long long>>, std::__unordered_map_equal<long long, std::__hash_value_type<long long, bool>, std::equal_to<long long>, std::hash<long long>>, std::allocator<std::__hash_value_type<long long, bool>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{vector<HDActivityCacheActiveSource, std::allocator<HDActivityCacheActiveSource>>=\"__begin_\"^{HDActivityCacheActiveSource}\"__end_\"^{HDActivityCacheActiveSource}\"\"{?=\"__cap_\"^{HDActivityCacheActiveSource}}}"
+ "{vector<HDActivityCacheActiveSource, std::allocator<HDActivityCacheActiveSource>>=^{HDActivityCacheActiveSource}^{HDActivityCacheActiveSource}{?=^{HDActivityCacheActiveSource}}}16@0:8"
+ "{vector<HDActivityCacheHeartRateStatisticsBuilderHeartRateSample, std::allocator<HDActivityCacheHeartRateStatisticsBuilderHeartRateSample>>=\"__begin_\"^{HDActivityCacheHeartRateStatisticsBuilderHeartRateSample}\"__end_\"^{HDActivityCacheHeartRateStatisticsBuilderHeartRateSample}\"\"{?=\"__cap_\"^{HDActivityCacheHeartRateStatisticsBuilderHeartRateSample}}}"
+ "{vector<HDActivityCacheStatisticsBuilderSample, std::allocator<HDActivityCacheStatisticsBuilderSample>>=\"__begin_\"^{HDActivityCacheStatisticsBuilderSample}\"__end_\"^{HDActivityCacheStatisticsBuilderSample}\"\"{?=\"__cap_\"^{HDActivityCacheStatisticsBuilderSample}}}"
+ "{vector<HDActivityCacheStatisticsBuilderStandHourSample, std::allocator<HDActivityCacheStatisticsBuilderStandHourSample>>=\"__begin_\"^{HDActivityCacheStatisticsBuilderStandHourSample}\"__end_\"^{HDActivityCacheStatisticsBuilderStandHourSample}\"\"{?=\"__cap_\"^{HDActivityCacheStatisticsBuilderStandHourSample}}}"
+ "{vector<HDActivityCacheStatisticsBuilderWorkoutSample, std::allocator<HDActivityCacheStatisticsBuilderWorkoutSample>>=\"__begin_\"^{HDActivityCacheStatisticsBuilderWorkoutSample}\"__end_\"^{HDActivityCacheStatisticsBuilderWorkoutSample}\"\"{?=\"__cap_\"^{HDActivityCacheStatisticsBuilderWorkoutSample}}}"
- "{HDActivityCacheActiveSource=dq{vector<long long, std::allocator<long long>>=^q^q^q}}16@0:8"
- "{map<_HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>, std::less<_HKDataTypeCode>, std::allocator<std::pair<const _HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>>>>=\"__tree_\"{__tree<std::__value_type<_HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>>, std::__map_value_compare<_HKDataTypeCode, std::__value_type<_HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>>, std::less<_HKDataTypeCode>>, std::allocator<std::__value_type<_HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
- "{unordered_map<long long, bool, std::hash<long long>, std::equal_to<long long>, std::allocator<std::pair<const long long, bool>>>=\"__table_\"{__hash_table<std::__hash_value_type<long long, bool>, std::__unordered_map_hasher<long long, std::__hash_value_type<long long, bool>, std::hash<long long>, std::equal_to<long long>>, std::__unordered_map_equal<long long, std::__hash_value_type<long long, bool>, std::equal_to<long long>, std::hash<long long>>, std::allocator<std::__hash_value_type<long long, bool>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
- "{vector<HDActivityCacheActiveSource, std::allocator<HDActivityCacheActiveSource>>=\"__begin_\"^{HDActivityCacheActiveSource}\"__end_\"^{HDActivityCacheActiveSource}\"__cap_\"^{HDActivityCacheActiveSource}}"
- "{vector<HDActivityCacheActiveSource, std::allocator<HDActivityCacheActiveSource>>=^{HDActivityCacheActiveSource}^{HDActivityCacheActiveSource}^{HDActivityCacheActiveSource}}16@0:8"
- "{vector<HDActivityCacheHeartRateStatisticsBuilderHeartRateSample, std::allocator<HDActivityCacheHeartRateStatisticsBuilderHeartRateSample>>=\"__begin_\"^{HDActivityCacheHeartRateStatisticsBuilderHeartRateSample}\"__end_\"^{HDActivityCacheHeartRateStatisticsBuilderHeartRateSample}\"__cap_\"^{HDActivityCacheHeartRateStatisticsBuilderHeartRateSample}}"
- "{vector<HDActivityCacheStatisticsBuilderSample, std::allocator<HDActivityCacheStatisticsBuilderSample>>=\"__begin_\"^{HDActivityCacheStatisticsBuilderSample}\"__end_\"^{HDActivityCacheStatisticsBuilderSample}\"__cap_\"^{HDActivityCacheStatisticsBuilderSample}}"
- "{vector<HDActivityCacheStatisticsBuilderStandHourSample, std::allocator<HDActivityCacheStatisticsBuilderStandHourSample>>=\"__begin_\"^{HDActivityCacheStatisticsBuilderStandHourSample}\"__end_\"^{HDActivityCacheStatisticsBuilderStandHourSample}\"__cap_\"^{HDActivityCacheStatisticsBuilderStandHourSample}}"
- "{vector<HDActivityCacheStatisticsBuilderWorkoutSample, std::allocator<HDActivityCacheStatisticsBuilderWorkoutSample>>=\"__begin_\"^{HDActivityCacheStatisticsBuilderWorkoutSample}\"__end_\"^{HDActivityCacheStatisticsBuilderWorkoutSample}\"__cap_\"^{HDActivityCacheStatisticsBuilderWorkoutSample}}"

```
