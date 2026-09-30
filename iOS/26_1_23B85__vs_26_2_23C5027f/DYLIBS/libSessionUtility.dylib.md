## libSessionUtility.dylib

> `/System/Library/PrivateFrameworks/AudioSession.framework/libSessionUtility.dylib`

```diff

-398.209.0.0.0
-  __TEXT.__text: 0x40928
+398.303.0.0.0
+  __TEXT.__text: 0x4096c
   __TEXT.__auth_stubs: 0x930
   __TEXT.__objc_methlist: 0x800
   __TEXT.__cstring: 0x1c66

   __TEXT.__unwind_info: 0x19c8
   __TEXT.__objc_classname: 0x1f0
   __TEXT.__objc_methname: 0x168a
-  __TEXT.__objc_methtype: 0x15fc
+  __TEXT.__objc_methtype: 0x161a
   __TEXT.__objc_stubs: 0x6c0
   __DATA_CONST.__got: 0x228
   __DATA_CONST.__const: 0x88

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6FBF8100-E51F-3334-A639-7F9B827ECFC9
+  UUID: D122764B-B066-314D-9C62-3DB1F0B3977F
   Functions: 1419
   Symbols:   3121
   CStrings:  726
Functions:
~ __ZNSt3__15dequeINS_10shared_ptrIN4avas12WorkloopPool9BlockInfoEEENS_9allocatorIS5_EEE19__add_back_capacityEv : 468 -> 472
~ __ZNSt3__16vectorIU8__strongP8NSStringNS_9allocatorIS3_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorINS_4pairIU8__strongPU50objcproto39AVAudioNotificationCenterServerDelegate11objc_objectU8__strongP7NSArrayEENS_9allocatorIS8_EEE24__emplace_back_slow_pathIJS8_EEEPS8_DpOT_ : 280 -> 284
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN4avas30NotificationDelegateCollection21NotificationDelegatesEEENS_22__unordered_map_hasherIyS5_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS5_SA_S8_Lb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIyJRKNS_21piecewise_construct_tENS_5tupleIJRKyEEENSL_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_ : 592 -> 600
~ __ZNSt3__16vectorIN5caulk7xstringENS_9allocatorIS2_EEE18__assign_with_sizeB8ne200100IPS2_S7_EEvT_T0_l : 368 -> 372
~ __ZNSt3__16vectorIN5caulk7xstringENS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorIN5caulk7xstringENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJEEEPS2_DpOT_ : 248 -> 260
~ __ZNSt3__114__split_bufferIPNS_10shared_ptrIN4avas12WorkloopPool9BlockInfoEEENS_9allocatorIS6_EEE13emplace_frontIJS6_EEEvDpOT_ : 268 -> 272
~ __ZN4avas6server8HWStream8readFromERN2PB6ReaderE : 2412 -> 2448
~ __ZN4avas6server6Driver8readFromERN2PB6ReaderE : 1952 -> 1964
~ __ZN4avas6server13ChangedObject8readFromERN2PB6ReaderE : 2032 -> 2000
~ __ZNSt3__16vectorIyNS_9allocatorIyEEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorIjNS_9allocatorIjEEE11__vallocateB8ne200100Em : 60 -> 64
CStrings:
+ "{synchronized<avas::NotificationDelegateCollection, caulk::mach::unfair_lock, caulk::empty_atomic_interface<avas::NotificationDelegateCollection>>=\"mMutex\"{unfair_lock=\"m_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}}\"mObject\"{NotificationDelegateCollection=\"_delegates\"{unordered_map<unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>, std::__unordered_map_hasher<unsigned long long, std::__hash_value_type<unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::__hash_value_type<unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::__hash_value_type<unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}\"_currentDelegateID\"Q}}"
- "{synchronized<avas::NotificationDelegateCollection, caulk::mach::unfair_lock, caulk::empty_atomic_interface<avas::NotificationDelegateCollection>>=\"mMutex\"{unfair_lock=\"m_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}}\"mObject\"{NotificationDelegateCollection=\"_delegates\"{unordered_map<unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>, std::__unordered_map_hasher<unsigned long long, std::__hash_value_type<unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::__hash_value_type<unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::__hash_value_type<unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}\"_currentDelegateID\"Q}}"

```
