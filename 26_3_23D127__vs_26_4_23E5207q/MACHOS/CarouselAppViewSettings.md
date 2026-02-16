## CarouselAppViewSettings

> `/System/Library/NanoPreferenceBundles/Customization/CarouselAppViewSettings.bundle/CarouselAppViewSettings`

```diff

-1114.2.10.0.0
-  __TEXT.__text: 0x24690
+1114.4.41.0.0
+  __TEXT.__text: 0x24fa0
   __TEXT.__auth_stubs: 0x7d0
   __TEXT.__objc_stubs: 0x4000
   __TEXT.__objc_methlist: 0x1a7c
-  __TEXT.__const: 0x3a8
-  __TEXT.__cstring: 0xa3d
+  __TEXT.__const: 0x398
+  __TEXT.__cstring: 0x1a0d
   __TEXT.__oslogstring: 0x1750
   __TEXT.__objc_classname: 0x398
   __TEXT.__objc_methname: 0x4793
-  __TEXT.__objc_methtype: 0x2137
-  __TEXT.__gcc_except_tab: 0x2ec0
-  __TEXT.__unwind_info: 0xfb8
+  __TEXT.__objc_methtype: 0x210d
+  __TEXT.__gcc_except_tab: 0x2f00
+  __TEXT.__unwind_info: 0xff8
   __DATA_CONST.__auth_got: 0x400
   __DATA_CONST.__got: 0x488
   __DATA_CONST.__const: 0x748

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DA45C50D-1BFF-39BC-A384-C588C905367B
-  Functions: 766
+  UUID: 9060BD5A-0C0C-36F6-B093-0C81305ACA57
+  Functions: 774
   Symbols:   354
-  CStrings:  1471
+  CStrings:  1482
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _bzero
+ _objc_retain_x27
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x9
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CH5lugB3n_slVkLQtcxAX5U-xmr41Wf3Dee3Fog/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH5lugB3n_slVkLQtcxAX5U-xmr41Wf3Dee3Fog/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH5lugB3n_slVkLQtcxAX5U-xmr41Wf3Dee3Fog/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH5lugB3n_slVkLQtcxAX5U-xmr41Wf3Dee3Fog/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH5lugB3n_slVkLQtcxAX5U-xmr41Wf3Dee3Fog/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH5lugB3n_slVkLQtcxAX5U-xmr41Wf3Dee3Fog/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH5lugB3n_slVkLQtcxAX5U-xmr41Wf3Dee3Fog/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH5lugB3n_slVkLQtcxAX5U-xmr41Wf3Dee3Fog/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH5lugB3n_slVkLQtcxAX5U-xmr41Wf3Dee3Fog/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH5lugB3n_slVkLQtcxAX5U-xmr41Wf3Dee3Fog/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CH5lugB3n_slVkLQtcxAX5U-xmr41Wf3Dee3Fog/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "{unordered_map<CSL::Hex, CSLHexAppNode *__unsafe_unretained, std::hash<CSL::Hex>, std::equal_to<CSL::Hex>, std::allocator<std::pair<const CSL::Hex, CSLHexAppNode *__unsafe_unretained>>>=\"__table_\"{__hash_table<std::__hash_value_type<CSL::Hex, CSLHexAppNode *__unsafe_unretained>, std::__unordered_map_hasher<CSL::Hex, std::pair<const CSL::Hex, CSLHexAppNode *__unsafe_unretained>, std::hash<CSL::Hex>, std::equal_to<CSL::Hex>>, std::__unordered_map_equal<CSL::Hex, std::pair<const CSL::Hex, CSLHexAppNode *__unsafe_unretained>, std::equal_to<CSL::Hex>, std::hash<CSL::Hex>>, std::allocator<std::pair<const CSL::Hex, CSLHexAppNode *__unsafe_unretained>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<CSL::Hex, CSLHexAppNode *__unsafe_unretained>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<CSL::Hex, CSLHexAppNode *__unsafe_unretained>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<CSL::Hex, CSLHexAppNode *__unsafe_unretained>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<CSL::Hex, CSLHexAppNode *__unsafe_unretained>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{unordered_map<CSL::Hex, int, std::hash<CSL::Hex>, std::equal_to<CSL::Hex>, std::allocator<std::pair<const CSL::Hex, int>>>=\"__table_\"{__hash_table<std::__hash_value_type<CSL::Hex, int>, std::__unordered_map_hasher<CSL::Hex, std::pair<const CSL::Hex, int>, std::hash<CSL::Hex>, std::equal_to<CSL::Hex>>, std::__unordered_map_equal<CSL::Hex, std::pair<const CSL::Hex, int>, std::equal_to<CSL::Hex>, std::hash<CSL::Hex>>, std::allocator<std::pair<const CSL::Hex, int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<CSL::Hex, int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<CSL::Hex, int>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<CSL::Hex, int>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<CSL::Hex, int>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "{unordered_map<CSL::Hex, CSLHexAppNode *__unsafe_unretained, std::hash<CSL::Hex>, std::equal_to<CSL::Hex>, std::allocator<std::pair<const CSL::Hex, CSLHexAppNode *__unsafe_unretained>>>=\"__table_\"{__hash_table<std::__hash_value_type<CSL::Hex, CSLHexAppNode *__unsafe_unretained>, std::__unordered_map_hasher<CSL::Hex, std::__hash_value_type<CSL::Hex, CSLHexAppNode *__unsafe_unretained>, std::hash<CSL::Hex>, std::equal_to<CSL::Hex>>, std::__unordered_map_equal<CSL::Hex, std::__hash_value_type<CSL::Hex, CSLHexAppNode *__unsafe_unretained>, std::equal_to<CSL::Hex>, std::hash<CSL::Hex>>, std::allocator<std::__hash_value_type<CSL::Hex, CSLHexAppNode *__unsafe_unretained>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<CSL::Hex, CSLHexAppNode *__unsafe_unretained>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<CSL::Hex, CSLHexAppNode *__unsafe_unretained>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<CSL::Hex, CSLHexAppNode *__unsafe_unretained>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<CSL::Hex, CSLHexAppNode *__unsafe_unretained>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "{unordered_map<CSL::Hex, int, std::hash<CSL::Hex>, std::equal_to<CSL::Hex>, std::allocator<std::pair<const CSL::Hex, int>>>=\"__table_\"{__hash_table<std::__hash_value_type<CSL::Hex, int>, std::__unordered_map_hasher<CSL::Hex, std::__hash_value_type<CSL::Hex, int>, std::hash<CSL::Hex>, std::equal_to<CSL::Hex>>, std::__unordered_map_equal<CSL::Hex, std::__hash_value_type<CSL::Hex, int>, std::equal_to<CSL::Hex>, std::hash<CSL::Hex>>, std::allocator<std::__hash_value_type<CSL::Hex, int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<CSL::Hex, int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<CSL::Hex, int>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<CSL::Hex, int>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<CSL::Hex, int>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"

```
