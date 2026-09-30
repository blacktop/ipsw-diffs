## CoreHaptics

> `/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics`

```diff

 272.202.0.0.0
-  __TEXT.__text: 0x55304
+  __TEXT.__text: 0x55310
   __TEXT.__auth_stubs: 0xce0
   __TEXT.__objc_methlist: 0x23fc
   __TEXT.__const: 0x568

   __TEXT.__oslogstring: 0x8ac9
   __TEXT.__unwind_info: 0x1cc0
   __TEXT.__objc_classname: 0x3b8
-  __TEXT.__objc_methname: 0x4f7d
-  __TEXT.__objc_methtype: 0x1c31
+  __TEXT.__objc_methname: 0x4f89
+  __TEXT.__objc_methtype: 0x1c75
   __TEXT.__objc_stubs: 0x4360
   __DATA_CONST.__got: 0x240
   __DATA_CONST.__const: 0xa60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 633B3694-45A5-35B9-8775-255EDE58515F
+  UUID: 66FD7418-EDC4-38AC-9902-8BD738F0C7DD
   Functions: 1039
   Symbols:   4177
   CStrings:  2868
Functions:
~ __ZNSt3__16vectorIN18CASmartPreferences4PrefENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRPK10__CFStringSA_RNS_8functionIFbPKvEEEEEEPS2_DpOT_ : 328 -> 332
~ __ZNSt3__16vectorImNS_9allocatorImEEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeI23AVHapticPlayerEventTypeU8__strongP8NSStringEENS_22__unordered_map_hasherIS2_S6_NS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S6_SB_S9_Lb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIS2_JRKNS_4pairIKS2_S5_EEEEENSJ_INS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEEbEERKT_DpOT0_ : 612 -> 616
CStrings:
+ "B48@0:8Q16{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{?=^Q}}24"
+ "T{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{?=^Q}},R,V_hapticContinuousNonsustainedIDs"
+ "T{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{?=^Q}},R,V_hapticContinuousSustainedIDs"
+ "T{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{?=^Q}},R,V_hapticTransientIDs"
+ "{map<unsigned long, AVHapticSequenceEntry *, std::less<unsigned long>, std::allocator<std::pair<const unsigned long, AVHapticSequenceEntry *>>>=\"__tree_\"{__tree<std::__value_type<unsigned long, AVHapticSequenceEntry *>, std::__map_value_compare<unsigned long, std::__value_type<unsigned long, AVHapticSequenceEntry *>, std::less<unsigned long>>, std::allocator<std::__value_type<unsigned long, AVHapticSequenceEntry *>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{map<unsigned long, std::pair<NSURL *, NSDictionary *>, std::less<unsigned long>, std::allocator<std::pair<const unsigned long, std::pair<NSURL *, NSDictionary *>>>>=\"__tree_\"{__tree<std::__value_type<unsigned long, std::pair<NSURL *, NSDictionary *>>, std::__map_value_compare<unsigned long, std::__value_type<unsigned long, std::pair<NSURL *, NSDictionary *>>, std::less<unsigned long>>, std::allocator<std::__value_type<unsigned long, std::pair<NSURL *, NSDictionary *>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{unordered_map<AVHapticPlayerEventType, NSString *, std::hash<AVHapticPlayerEventType>, std::equal_to<AVHapticPlayerEventType>, std::allocator<std::pair<const AVHapticPlayerEventType, NSString *>>>=\"__table_\"{__hash_table<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, std::__unordered_map_hasher<AVHapticPlayerEventType, std::__hash_value_type<AVHapticPlayerEventType, NSString *>, std::hash<AVHapticPlayerEventType>, std::equal_to<AVHapticPlayerEventType>>, std::__unordered_map_equal<AVHapticPlayerEventType, std::__hash_value_type<AVHapticPlayerEventType, NSString *>, std::equal_to<AVHapticPlayerEventType>, std::hash<AVHapticPlayerEventType>>, std::allocator<std::__hash_value_type<AVHapticPlayerEventType, NSString *>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{vector<unsigned long, std::allocator<unsigned long>>=\"__begin_\"^Q\"__end_\"^Q\"\"{?=\"__cap_\"^Q}}"
+ "{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{?=^Q}}16@0:8"
- "B48@0:8Q16{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q^Q}24"
- "T{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q^Q},R,V_hapticContinuousNonsustainedIDs"
- "T{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q^Q},R,V_hapticContinuousSustainedIDs"
- "T{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q^Q},R,V_hapticTransientIDs"
- "{map<unsigned long, AVHapticSequenceEntry *, std::less<unsigned long>, std::allocator<std::pair<const unsigned long, AVHapticSequenceEntry *>>>=\"__tree_\"{__tree<std::__value_type<unsigned long, AVHapticSequenceEntry *>, std::__map_value_compare<unsigned long, std::__value_type<unsigned long, AVHapticSequenceEntry *>, std::less<unsigned long>>, std::allocator<std::__value_type<unsigned long, AVHapticSequenceEntry *>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
- "{map<unsigned long, std::pair<NSURL *, NSDictionary *>, std::less<unsigned long>, std::allocator<std::pair<const unsigned long, std::pair<NSURL *, NSDictionary *>>>>=\"__tree_\"{__tree<std::__value_type<unsigned long, std::pair<NSURL *, NSDictionary *>>, std::__map_value_compare<unsigned long, std::__value_type<unsigned long, std::pair<NSURL *, NSDictionary *>>, std::less<unsigned long>>, std::allocator<std::__value_type<unsigned long, std::pair<NSURL *, NSDictionary *>>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
- "{unordered_map<AVHapticPlayerEventType, NSString *, std::hash<AVHapticPlayerEventType>, std::equal_to<AVHapticPlayerEventType>, std::allocator<std::pair<const AVHapticPlayerEventType, NSString *>>>=\"__table_\"{__hash_table<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, std::__unordered_map_hasher<AVHapticPlayerEventType, std::__hash_value_type<AVHapticPlayerEventType, NSString *>, std::hash<AVHapticPlayerEventType>, std::equal_to<AVHapticPlayerEventType>>, std::__unordered_map_equal<AVHapticPlayerEventType, std::__hash_value_type<AVHapticPlayerEventType, NSString *>, std::equal_to<AVHapticPlayerEventType>, std::hash<AVHapticPlayerEventType>>, std::allocator<std::__hash_value_type<AVHapticPlayerEventType, NSString *>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
- "{vector<unsigned long, std::allocator<unsigned long>>=\"__begin_\"^Q\"__end_\"^Q\"__cap_\"^Q}"
- "{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q^Q}16@0:8"

```
