## com.apple.SpeechRecognitionCore.speechrecognitiond

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond`

```diff

-6.3.68.7.0
-  __TEXT.__text: 0xca614
-  __TEXT.__auth_stubs: 0x2740
-  __TEXT.__objc_stubs: 0x34a0
+6.7.0.0.0
+  __TEXT.__text: 0xcf5fc
+  __TEXT.__auth_stubs: 0x26e0
+  __TEXT.__objc_stubs: 0x3ae0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x190c
-  __TEXT.__const: 0x6016
-  __TEXT.__gcc_except_tab: 0xa558
-  __TEXT.__objc_methname: 0x4aaa
-  __TEXT.__cstring: 0x4136
+  __TEXT.__const: 0x5f76
+  __TEXT.__gcc_except_tab: 0xa530
+  __TEXT.__objc_methname: 0x50d7
+  __TEXT.__cstring: 0x5c50
   __TEXT.__oslogstring: 0x56f4
-  __TEXT.__objc_classname: 0x348
-  __TEXT.__objc_methtype: 0x1012
+  __TEXT.__objc_classname: 0x796
+  __TEXT.__objc_methtype: 0x146d
   __TEXT.__dlopen_cstrs: 0x6a
   __TEXT.__ustring: 0x4
   __TEXT.__constg_swiftt: 0xbdc
-  __TEXT.__swift5_typeref: 0x7c8
+  __TEXT.__swift5_typeref: 0x7b8
   __TEXT.__swift5_reflstr: 0x508
   __TEXT.__swift5_fieldmd: 0x534
   __TEXT.__swift5_types: 0x60

   __TEXT.__swift5_capture: 0x49c
   __TEXT.__swift_as_entry: 0x5c
   __TEXT.__swift_as_ret: 0x5c
-  __TEXT.__unwind_info: 0x48c0
-  __TEXT.__eh_frame: 0x2f64
-  __DATA_CONST.__auth_got: 0x13c0
+  __TEXT.__unwind_info: 0x4b38
+  __TEXT.__eh_frame: 0x3058
+  __DATA_CONST.__auth_got: 0x1390
   __DATA_CONST.__got: 0x778
-  __DATA_CONST.__auth_ptr: 0x1e0
+  __DATA_CONST.__auth_ptr: 0x1d8
   __DATA_CONST.__const: 0x7130
   __DATA_CONST.__cfstring: 0x1d20
   __DATA_CONST.__objc_classlist: 0xf8

   __DATA.__objc_selrefs: 0x1310
   __DATA.__objc_ivar: 0x140
   __DATA.__objc_data: 0x1560
-  __DATA.__data: 0xfd8
+  __DATA.__data: 0xfe8
   __DATA.__bss: 0x470
   __DATA.__common: 0xa6
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E4F0A6F2-E21B-3CA1-8BE8-5854004791FF
-  Functions: 3615
-  Symbols:   1129
-  CStrings:  2507
+  UUID: 0A48C6FC-F34B-3631-976F-27B53F0F8209
+  Functions: 3664
+  Symbols:   1125
+  CStrings:  2512
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _wmemchr
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEcm
- _malloc
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x4
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
CStrings:
+ "-_"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:286: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:301: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1559: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1572: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1420: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:828: libc++ Hardening assertion !empty() failed: list::front called on empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/regex:4739: libc++ Hardening assertion ready() failed: match_results::format() called when not ready\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHqzugALd5Sp8VBytJD83ukH3_ILVTOORCueY8o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
+ "/Library/Caches/com.apple.xbs/2F2F537C-7169-4E08-97FB-EF0649177E73/TemporaryDirectory.jBSeeC/Sources/SpeechRecognitionCore/Daemon/RDQSRResult.mm"
+ "BuiltInLM."
- "/Library/Caches/com.apple.xbs/Sources/SpeechRecognitionCore/Daemon/RDQSRResult.mm"

```
