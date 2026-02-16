## AutoLoop

> `/System/Library/PrivateFrameworks/AutoLoop.framework/AutoLoop`

```diff

 58.0.0.0.0
-  __TEXT.__text: 0x3dfd8
-  __TEXT.__auth_stubs: 0x1030
+  __TEXT.__text: 0x41414
+  __TEXT.__auth_stubs: 0x1000
   __TEXT.__objc_methlist: 0x1450
-  __TEXT.__const: 0x5a8
-  __TEXT.__gcc_except_tab: 0x423c
-  __TEXT.__cstring: 0x660d
+  __TEXT.__const: 0x4e8
+  __TEXT.__gcc_except_tab: 0x4230
+  __TEXT.__cstring: 0x7d4b
   __TEXT.__oslogstring: 0x47
-  __TEXT.__unwind_info: 0x1318
+  __TEXT.__unwind_info: 0x1370
   __TEXT.__objc_classname: 0x164
   __TEXT.__objc_methname: 0x4741
   __TEXT.__objc_methtype: 0xec9

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1178
   __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x830
+  __AUTH_CONST.__auth_got: 0x818
   __AUTH_CONST.__const: 0x720
   __AUTH_CONST.__cfstring: 0x50c0
   __AUTH_CONST.__objc_const: 0x27d8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 17504127-72F2-3B46-AD20-AB2042F78689
-  Functions: 1084
-  Symbols:   486
-  CStrings:  2415
+  UUID: 9C83F823-3C99-3F10-BC6D-8FC6674076B2
+  Functions: 1097
+  Symbols:   483
+  CStrings:  2432
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHocugBjlZi-HLQl2CWkJzn6qjwkGjEi7q-4e0k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHocugBjlZi-HLQl2CWkJzn6qjwkGjEi7q-4e0k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHocugBjlZi-HLQl2CWkJzn6qjwkGjEi7q-4e0k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHocugBjlZi-HLQl2CWkJzn6qjwkGjEi7q-4e0k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHocugBjlZi-HLQl2CWkJzn6qjwkGjEi7q-4e0k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHocugBjlZi-HLQl2CWkJzn6qjwkGjEi7q-4e0k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHocugBjlZi-HLQl2CWkJzn6qjwkGjEi7q-4e0k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHocugBjlZi-HLQl2CWkJzn6qjwkGjEi7q-4e0k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHocugBjlZi-HLQl2CWkJzn6qjwkGjEi7q-4e0k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHocugBjlZi-HLQl2CWkJzn6qjwkGjEi7q-4e0k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CHocugBjlZi-HLQl2CWkJzn6qjwkGjEi7q-4e0k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHocugBjlZi-HLQl2CWkJzn6qjwkGjEi7q-4e0k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHocugBjlZi-HLQl2CWkJzn6qjwkGjEi7q-4e0k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHocugBjlZi-HLQl2CWkJzn6qjwkGjEi7q-4e0k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHocugBjlZi-HLQl2CWkJzn6qjwkGjEi7q-4e0k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHocugBjlZi-HLQl2CWkJzn6qjwkGjEi7q-4e0k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:286: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHocugBjlZi-HLQl2CWkJzn6qjwkGjEi7q-4e0k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:301: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"

```
