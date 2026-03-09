## CostModelSegmenter

> `/System/Library/PrivateFrameworks/CoreMLOdie.framework/XPCServices/CostModelSegmenter.xpc/CostModelSegmenter`

```diff

 3520.10.1.0.0
-  __TEXT.__text: 0x2f9598
-  __TEXT.__auth_stubs: 0x10c0
+  __TEXT.__text: 0x32673c
+  __TEXT.__auth_stubs: 0x10b0
   __TEXT.__objc_stubs: 0x40
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x16f8
-  __TEXT.__cstring: 0x16f27
+  __TEXT.__cstring: 0x1504b
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x264
   __TEXT.__swift5_typeref: 0x130

   __TEXT.__swift5_proto: 0x2c
   __TEXT.__objc_methname: 0x3b
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x71e8
+  __TEXT.__unwind_info: 0x72b0
   __TEXT.__eh_frame: 0x220
-  __DATA_CONST.__auth_got: 0x868
+  __DATA_CONST.__auth_got: 0x860
   __DATA_CONST.__got: 0x5960
   __DATA_CONST.__auth_ptr: 0x160
   __DATA_CONST.__const: 0xf238

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  UUID: B6741CD0-5A28-32AA-8744-ECCEBE70EA00
-  Functions: 12017
-  Symbols:   6758
-  CStrings:  2432
+  UUID: 4A9669F3-ED4F-3AED-A699-0A6B8FB6BF15
+  Functions: 12046
+  Symbols:   6756
+  CStrings:  2409
 
Symbols:
- __ZN4mlir25SimpleAffineExprFlattener12visitAddExprENS_18AffineBinaryOpExprE
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJlVugD6ORTTwsrIeclsMJzCIobQ85QTZvhB18w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugD6ORTTwsrIeclsMJzCIobQ85QTZvhB18w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugD6ORTTwsrIeclsMJzCIobQ85QTZvhB18w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugD6ORTTwsrIeclsMJzCIobQ85QTZvhB18w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugD6ORTTwsrIeclsMJzCIobQ85QTZvhB18w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugD6ORTTwsrIeclsMJzCIobQ85QTZvhB18w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugD6ORTTwsrIeclsMJzCIobQ85QTZvhB18w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugD6ORTTwsrIeclsMJzCIobQ85QTZvhB18w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugD6ORTTwsrIeclsMJzCIobQ85QTZvhB18w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugD6ORTTwsrIeclsMJzCIobQ85QTZvhB18w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugD6ORTTwsrIeclsMJzCIobQ85QTZvhB18w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugD6ORTTwsrIeclsMJzCIobQ85QTZvhB18w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugD6ORTTwsrIeclsMJzCIobQ85QTZvhB18w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugD6ORTTwsrIeclsMJzCIobQ85QTZvhB18w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugD6ORTTwsrIeclsMJzCIobQ85QTZvhB18w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1553: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugD6ORTTwsrIeclsMJzCIobQ85QTZvhB18w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugD6ORTTwsrIeclsMJzCIobQ85QTZvhB18w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugD6ORTTwsrIeclsMJzCIobQ85QTZvhB18w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugD6ORTTwsrIeclsMJzCIobQ85QTZvhB18w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugD6ORTTwsrIeclsMJzCIobQ85QTZvhB18w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugD6ORTTwsrIeclsMJzCIobQ85QTZvhB18w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:412: libc++ Hardening assertion __pos < size() failed: string_view[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugD6ORTTwsrIeclsMJzCIobQ85QTZvhB18w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:424: libc++ Hardening assertion !empty() failed: string_view::back(): string is empty\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugD6ORTTwsrIeclsMJzCIobQ85QTZvhB18w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:431: libc++ Hardening assertion __n <= size() failed: remove_prefix() can't remove more than size()\n"

```
