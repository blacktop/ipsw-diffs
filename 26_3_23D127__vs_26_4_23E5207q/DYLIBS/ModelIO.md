## ModelIO

> `/System/Library/Frameworks/ModelIO.framework/ModelIO`

```diff

-268.2.1.0.0
-  __TEXT.__text: 0x120544
-  __TEXT.__auth_stubs: 0x2b50
+268.2.2.0.0
+  __TEXT.__text: 0x128118
+  __TEXT.__auth_stubs: 0x2b00
   __TEXT.__objc_methlist: 0x43dc
-  __TEXT.__gcc_except_tab: 0x170fc
-  __TEXT.__cstring: 0x761a
-  __TEXT.__const: 0x5860
-  __TEXT.__unwind_info: 0x51d8
-  __TEXT.__eh_frame: 0x60
+  __TEXT.__gcc_except_tab: 0x171f8
+  __TEXT.__cstring: 0x9a6b
+  __TEXT.__const: 0x57b8
+  __TEXT.__unwind_info: 0x5350
   __TEXT.__objc_classname: 0x7eb
   __TEXT.__objc_methname: 0x89fe
-  __TEXT.__objc_methtype: 0x2bda
+  __TEXT.__objc_methtype: 0x2bc5
   __TEXT.__objc_stubs: 0x4c20
   __DATA_CONST.__got: 0x5e0
   __DATA_CONST.__const: 0xf98

   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x15b8
+  __AUTH_CONST.__auth_got: 0x1590
   __AUTH_CONST.__const: 0x2cf0
   __AUTH_CONST.__cfstring: 0x37a0
   __AUTH_CONST.__objc_const: 0x7f38

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/usd/libusd_ms.dylib
-  UUID: B9BD84AB-F18F-38B9-B6F8-ABB8AB54E970
-  Functions: 4544
-  Symbols:   1044
-  CStrings:  3335
+  UUID: 3EB94B92-424D-357A-8735-57C0E9A1B3B2
+  Functions: 4598
+  Symbols:   1039
+  CStrings:  3369
 
Symbols:
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9__grow_byEmmmmmm
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_retainAutoreleasedReturnValue
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEcm
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE5rfindEcm
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:301: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1420: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1518: libc++ Hardening assertion this != std::addressof(__c) failed: list::splice(iterator, list) called with this == &list\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/usd/pxr/base/tf/refPtr.h"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/usd/pxr/base/tf/weakPtrFacade.h"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/usd/pxr/base/vt/array.h"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/usd/pxr/usd/usd/object.h"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/usd/pxr/usd/usd/primData.h"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/usd/pxr/usd/usd/primRange.h"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/usd/pxr/usd/usdGeom/primvar.h"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBqj_f5-vmlO9d2gHlEDjqecVDKvt4KAvU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/usd/pxr/usd/usdGeom/xformOp.h"
+ "/Geom"
+ "IESNA91"
+ "IESNA:LM-63-1991"
+ "IESNA:LM-63-1995"
+ "IESNA:LM-63-2002"
+ "TILT"
+ "_ABSOLUTELUMENS"
+ "{unordered_map<unsigned long long, int, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, int>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long long, int>, std::__unordered_map_hasher<unsigned long long, std::pair<const unsigned long long, int>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::pair<const unsigned long long, int>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::pair<const unsigned long long, int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, int>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, int>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, int>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "/AppleInternal/Library/BuildRoots/4~CG6augCeLaxBbzmbSaA5vOHJB5ic86cjMkHTVos/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/usd/pxr/base/tf/refPtr.h"
- "/AppleInternal/Library/BuildRoots/4~CG6augCeLaxBbzmbSaA5vOHJB5ic86cjMkHTVos/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/usd/pxr/base/tf/weakPtrFacade.h"
- "/AppleInternal/Library/BuildRoots/4~CG6augCeLaxBbzmbSaA5vOHJB5ic86cjMkHTVos/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/usd/pxr/base/vt/array.h"
- "/AppleInternal/Library/BuildRoots/4~CG6augCeLaxBbzmbSaA5vOHJB5ic86cjMkHTVos/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/usd/pxr/usd/usd/object.h"
- "/AppleInternal/Library/BuildRoots/4~CG6augCeLaxBbzmbSaA5vOHJB5ic86cjMkHTVos/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/usd/pxr/usd/usd/primData.h"
- "/AppleInternal/Library/BuildRoots/4~CG6augCeLaxBbzmbSaA5vOHJB5ic86cjMkHTVos/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/usd/pxr/usd/usd/primRange.h"
- "/AppleInternal/Library/BuildRoots/4~CG6augCeLaxBbzmbSaA5vOHJB5ic86cjMkHTVos/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/usd/pxr/usd/usdGeom/primvar.h"
- "/AppleInternal/Library/BuildRoots/4~CG6augCeLaxBbzmbSaA5vOHJB5ic86cjMkHTVos/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/usd/pxr/usd/usdGeom/xformOp.h"
- "{unordered_map<unsigned long long, int, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, int>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long long, int>, std::__unordered_map_hasher<unsigned long long, std::__hash_value_type<unsigned long long, int>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::__hash_value_type<unsigned long long, int>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::__hash_value_type<unsigned long long, int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, int>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, int>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, int>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"

```
