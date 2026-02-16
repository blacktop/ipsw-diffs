## HealthActivityCache

> `/System/Library/Health/Plugins/HealthActivityCache.bundle/HealthActivityCache`

```diff

-6200.4.9.0.0
-  __TEXT.__text: 0x218d4
-  __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_stubs: 0x3060
-  __TEXT.__objc_methlist: 0xc54
-  __TEXT.__cstring: 0xa3d
-  __TEXT.__objc_classname: 0x38f
-  __TEXT.__objc_methtype: 0x1855
+6200.5.77.2.6
+  __TEXT.__text: 0x22450
+  __TEXT.__auth_stubs: 0x6a0
+  __TEXT.__objc_stubs: 0x30c0
+  __TEXT.__objc_methlist: 0xc84
+  __TEXT.__gcc_except_tab: 0x3234
   __TEXT.__const: 0x98
-  __TEXT.__objc_methname: 0x3f97
+  __TEXT.__objc_methname: 0x4091
   __TEXT.__oslogstring: 0xe05
-  __TEXT.__gcc_except_tab: 0x3214
-  __TEXT.__unwind_info: 0xe50
-  __DATA_CONST.__auth_got: 0x370
-  __DATA_CONST.__got: 0x490
-  __DATA_CONST.__const: 0x578
-  __DATA_CONST.__cfstring: 0x5c0
+  __TEXT.__objc_classname: 0x38f
+  __TEXT.__objc_methtype: 0x18be
+  __TEXT.__cstring: 0x1ec3
+  __TEXT.__unwind_info: 0xe78
+  __DATA_CONST.__auth_got: 0x368
+  __DATA_CONST.__got: 0x498
+  __DATA_CONST.__const: 0x558
+  __DATA_CONST.__cfstring: 0x6a0
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x2448
-  __DATA.__objc_selrefs: 0xeb0
-  __DATA.__objc_ivar: 0x24c
+  __DATA.__objc_const: 0x2480
+  __DATA.__objc_selrefs: 0xee0
+  __DATA.__objc_ivar: 0x250
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x558
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: AB1E7741-23F0-3652-AE80-5DEAE4A65401
-  Functions: 576
+  UUID: 53761D40-BAE7-377A-B9C1-D2577464EA45
+  Functions: 586
   Symbols:   333
-  CStrings:  986
+  CStrings:  1026
 
Symbols:
+ _OBJC_CLASS_$_NSAssertionHandler
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _bzero
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x5
- _objc_retain_x8
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CIsgugCVryBf389iM77mqQYic07pCKE7zT5enFU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsgugCVryBf389iM77mqQYic07pCKE7zT5enFU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsgugCVryBf389iM77mqQYic07pCKE7zT5enFU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsgugCVryBf389iM77mqQYic07pCKE7zT5enFU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsgugCVryBf389iM77mqQYic07pCKE7zT5enFU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsgugCVryBf389iM77mqQYic07pCKE7zT5enFU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsgugCVryBf389iM77mqQYic07pCKE7zT5enFU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsgugCVryBf389iM77mqQYic07pCKE7zT5enFU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsgugCVryBf389iM77mqQYic07pCKE7zT5enFU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsgugCVryBf389iM77mqQYic07pCKE7zT5enFU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsgugCVryBf389iM77mqQYic07pCKE7zT5enFU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsgugCVryBf389iM77mqQYic07pCKE7zT5enFU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsgugCVryBf389iM77mqQYic07pCKE7zT5enFU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsgugCVryBf389iM77mqQYic07pCKE7zT5enFU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "@24@0:8d16"
+ "@32@0:8@16d24"
+ "B32@0:8@\"NSString\"16@?<v@?>24"
+ "B32@0:8@16@?24"
+ "HDActivityCacheHeartRateStatisticsBuilder.mm"
+ "HDActivityCacheStatisticsBuilder.mm"
+ "HKVectorIsSorted(activationLogSamples)"
+ "HKVectorIsSorted(breatheSessions)"
+ "HKVectorIsSorted(heartRateSamples)"
+ "HKVectorIsSorted(workouts)"
+ "Invalid parameter not satisfying: %@"
+ "_activityCacheDelay"
+ "_activityCacheManagerWithUpdateDelay:"
+ "currentHandler"
+ "daemonDidReceiveRapportEvent:completion:"
+ "handleFailureInMethod:object:file:lineNumber:description:"
+ "initWithActivityCacheDelay:"
+ "initWithProfile:activityCacheUpdateDelay:"
+ "samplesMapWereRemoved:anchor:"
+ "v32@0:8@\"<HDActivityCacheManagerInterface>\"16@\"HKActivityCache\"24"
+ "v32@0:8@\"NSDictionary\"16@\"NSNumber\"24"
+ "v36@0:8@\"<HDActivityCacheManagerInterface>\"16@\"HKHeartRateSummary\"24B32"
+ "{map<_HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>, std::less<_HKDataTypeCode>, std::allocator<std::pair<const _HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>>>>=\"__tree_\"{__tree<std::__value_type<_HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>>, std::__map_value_compare<_HKDataTypeCode, std::pair<const _HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>>, std::less<_HKDataTypeCode>>, std::allocator<std::pair<const _HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{unordered_map<long long, bool, std::hash<long long>, std::equal_to<long long>, std::allocator<std::pair<const long long, bool>>>=\"__table_\"{__hash_table<std::__hash_value_type<long long, bool>, std::__unordered_map_hasher<long long, std::pair<const long long, bool>, std::hash<long long>, std::equal_to<long long>>, std::__unordered_map_equal<long long, std::pair<const long long, bool>, std::equal_to<long long>, std::hash<long long>>, std::allocator<std::pair<const long long, bool>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "_activityCacheManager"
- "v32@0:8@\"HDActivityCacheManager\"16@\"HKActivityCache\"24"
- "v36@0:8@\"HDActivityCacheManager\"16@\"HKHeartRateSummary\"24B32"
- "{map<_HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>, std::less<_HKDataTypeCode>, std::allocator<std::pair<const _HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>>>>=\"__tree_\"{__tree<std::__value_type<_HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>>, std::__map_value_compare<_HKDataTypeCode, std::__value_type<_HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>>, std::less<_HKDataTypeCode>>, std::allocator<std::__value_type<_HKDataTypeCode, std::map<long long, _HDActivityCacheSourceTotal>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
- "{unordered_map<long long, bool, std::hash<long long>, std::equal_to<long long>, std::allocator<std::pair<const long long, bool>>>=\"__table_\"{__hash_table<std::__hash_value_type<long long, bool>, std::__unordered_map_hasher<long long, std::__hash_value_type<long long, bool>, std::hash<long long>, std::equal_to<long long>>, std::__unordered_map_equal<long long, std::__hash_value_type<long long, bool>, std::equal_to<long long>, std::hash<long long>>, std::allocator<std::__hash_value_type<long long, bool>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<long long, bool>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"

```
