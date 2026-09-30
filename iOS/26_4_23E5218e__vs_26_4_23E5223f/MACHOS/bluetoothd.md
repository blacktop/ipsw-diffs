## bluetoothd

> `/usr/sbin/bluetoothd`

```diff

-194.24.0.0.0
-  __TEXT.__text: 0x863864
-  __TEXT.__auth_stubs: 0x4cf0
+194.25.0.0.0
+  __TEXT.__text: 0x861648
+  __TEXT.__auth_stubs: 0x4ce0
   __TEXT.__objc_stubs: 0x17080
-  __TEXT.__init_offsets: 0x60
+  __TEXT.__init_offsets: 0x64
   __TEXT.__objc_methlist: 0x876c
   __TEXT.__const: 0x250cc
   __TEXT.__gcc_except_tab: 0x6c128
-  __TEXT.__cstring: 0xb62bb
+  __TEXT.__cstring: 0xb3657
   __TEXT.__objc_classname: 0x9aa
   __TEXT.__objc_methname: 0x1bac1
   __TEXT.__objc_methtype: 0x47bd
-  __TEXT.__oslogstring: 0xae63a
+  __TEXT.__oslogstring: 0xae646
   __TEXT.__swift5_typeref: 0x9c
   __TEXT.__swift5_capture: 0x68
   __TEXT.__constg_swiftt: 0x48

   __TEXT.__swift_as_ret: 0x8
   __TEXT.__ustring: 0x34
   __TEXT.__dlopen_cstrs: 0xd4
-  __TEXT.__unwind_info: 0x23120
+  __TEXT.__unwind_info: 0x23100
   __TEXT.__eh_frame: 0x1b0
-  __DATA_CONST.__auth_got: 0x2690
+  __DATA_CONST.__auth_got: 0x2688
   __DATA_CONST.__got: 0xe30
   __DATA_CONST.__auth_ptr: 0x228
-  __DATA_CONST.__const: 0x30708
-  __DATA_CONST.__cfstring: 0x236c0
+  __DATA_CONST.__const: 0x30718
+  __DATA_CONST.__cfstring: 0x23720
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xb8

   __DATA.__objc_data: 0x1a58
   __DATA.__data: 0x4928
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x727fa
+  __DATA.__bss: 0x72952
   __DATA.__common: 0x6f80
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 872D3E71-FF77-3FB7-B3CE-FBF0B098D5C9
-  Functions: 34241
-  Symbols:   1722
-  CStrings:  43890
+  UUID: 56FDF3A7-FEF8-3C8D-964D-4213573080D1
+  Functions: 34233
+  Symbols:   1721
+  CStrings:  43879
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
+ "23:31:49"
+ "2c1877ad4ff80c066ea059b6fa73641767e9cd390213e77850886054489440cc"
+ "7817522da74b3aead8649e502aa25cfb5cbb3bbf0fd7944747ab14b4457afa60"
+ "Apple N1"
+ "B3 BT"
+ "B6 Connect"
+ "BP3GX1-4BPBX"
+ "BP3GY1-2N"
+ "BP3KR1-4BCVS"
+ "BP3KT1-4BRA"
+ "BP3KT1-4DLDR"
+ "BP3KV1-5WPC"
+ "BP3KX1-1BCVS"
+ "BP3KY1-3BCVS"
+ "Device %@ allowed to drop 0 IRK IRKSize:%zu"
+ "DropZeroIRK"
+ "Dropping 0 IRK for device %@"
+ "Feb 26 2026"
+ "LEPhyWorkaroundList"
+ "LEPhyWorkaroundList: set tag for %s"
+ "PF200 BT"
+ "WatchBP Home"
+ "WatchBP O3"
+ "WatchBP Office"
+ "com.Microlife."
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/iterator_operations.h:209: libc++ Hardening assertion __count == 0 || (__dist < 0) == (__count < 0) failed: __sentinel must precede __iter when __count < 0\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1553: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2438: libc++ Hardening assertion __f != end() failed: deque::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1402: libc++ Hardening assertion !empty() failed: list::pop_front() called with empty list\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1411: libc++ Hardening assertion !empty() failed: list::pop_back() called on an empty list\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1420: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1518: libc++ Hardening assertion this != std::addressof(__c) failed: list::splice(iterator, list) called with this == &list\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:828: libc++ Hardening assertion !empty() failed: list::front called on empty list\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:836: libc++ Hardening assertion !empty() failed: list::back called on empty list\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugA_tFIbazpDWF3rRpNUdyTfZGR320YI8Tg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3371: libc++ Hardening assertion !empty() failed: string::pop_back(): string is already empty\n"
- "22:26:35"
- "Feb 17 2026"
- "Warning: Dropping 0 IRK and public identity for address %s"
- "Warning: Dropping 0 IRK for device %@"

```
