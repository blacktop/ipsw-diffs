## CVNLP

> `/System/Library/PrivateFrameworks/CVNLP.framework/CVNLP`

```diff

 120.0.0.0.0
-  __TEXT.__text: 0xce760
-  __TEXT.__auth_stubs: 0x1660
+  __TEXT.__text: 0xd2d10
+  __TEXT.__auth_stubs: 0x15f0
   __TEXT.__objc_methlist: 0x1a2c
-  __TEXT.__const: 0x1e01
-  __TEXT.__gcc_except_tab: 0xe4bc
-  __TEXT.__cstring: 0x64f4
+  __TEXT.__const: 0x1db1
+  __TEXT.__gcc_except_tab: 0xe41c
+  __TEXT.__cstring: 0xa85f
   __TEXT.__oslogstring: 0x7ec
   __TEXT.__dlopen_cstrs: 0xc9
-  __TEXT.__unwind_info: 0x4188
+  __TEXT.__unwind_info: 0x4268
   __TEXT.__objc_classname: 0x440
-  __TEXT.__objc_methname: 0x5d6a
-  __TEXT.__objc_methtype: 0x226d
+  __TEXT.__objc_methname: 0x5d5e
+  __TEXT.__objc_methtype: 0x2255
   __TEXT.__objc_stubs: 0x2f00
   __DATA_CONST.__got: 0x3a8
   __DATA_CONST.__const: 0x8d8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1168
   __DATA_CONST.__objc_superrefs: 0x118
-  __AUTH_CONST.__auth_got: 0xb48
+  __AUTH_CONST.__auth_got: 0xb10
   __AUTH_CONST.__const: 0x3248
   __AUTH_CONST.__cfstring: 0x10c0
   __AUTH_CONST.__objc_const: 0x3cf8

   __AUTH.__data: 0x118
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x9d0
-  __DATA.__objc_ivar: 0x19c
+  __DATA.__objc_ivar: 0x1b0
   __DATA.__data: 0x3e0
   __DATA.__bss: 0xc8
   __DATA.__common: 0x408
-  __DATA_DIRTY.__objc_ivar: 0x18c
+  __DATA_DIRTY.__objc_ivar: 0x178
   __DATA_DIRTY.__objc_data: 0x3c0
   __DATA_DIRTY.__bss: 0x228
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  UUID: 2B803587-888D-3F9E-B8F7-950B6A937A69
-  Functions: 2664
-  Symbols:   633
-  CStrings:  2079
+  UUID: 943730AA-F21E-373D-A423-88F47BCB3868
+  Functions: 2685
+  Symbols:   626
+  CStrings:  2121
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEPKc
- _memset_pattern16
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x4
- _objc_retain_x6
- _objc_retain_x9
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:431: libc++ Hardening assertion __n <= size() failed: remove_prefix() can't remove more than size()\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:122: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:127: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:158: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:164: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:301: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:333: libc++ Hardening assertion !empty() failed: vector<bool>::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1553: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInTugCd59oNGggJp867EXrqH-Gvkpvh73DzHmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/bpe_model.cc"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/builtin_pb/sentencepiece.pb.cc"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.cc"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.h"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/filesystem.cc"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/mmap.h"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/model_factory.cc"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/model_interface.cc"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/model_interface.h"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/normalizer.cc"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/sentencepiece_processor.cc"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/unigram_model.cc"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/util.cc"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/util.h"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:1106: exception: failed to insert key: negative value"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:1108: exception: failed to insert key: zero-length key"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:1122: exception: failed to insert key: invalid null character"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:1127: exception: failed to insert key: wrong key order"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:1339: exception: failed to modify unit: too large offset"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:1675: exception: failed to build double-array: invalid null character"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:1677: exception: failed to build double-array: negative value"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:1692: exception: failed to build double-array: wrong key order"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:743: exception: failed to resize pool: std::bad_alloc"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:859: exception: failed to build rank index: std::bad_alloc"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/arena.cc"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/arenastring.cc"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/coded_stream.cc"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/common.cc"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/extension_set.cc"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/generated_message_util.cc"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arena_impl.h"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arenastring.h"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/extension_set_inl.h"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/io/coded_stream.h"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/parse_context.h"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/repeated_field.h"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/message_lite.cc"
+ "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/parse_context.cc"
+ "T{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::pair<const std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::pair<const std::string, std::vector<float>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}},N,V_stateInputEspressoBuffers"
+ "T{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::pair<const std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::pair<const std::string, std::vector<float>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}},N,V_stateOutputEspressoBuffers"
+ "T{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>={__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::pair<const std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}},N,V_stateInputEspressoBuffersShape"
+ "v40@0:8{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::pair<const std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::pair<const std::string, std::vector<float>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}16"
+ "v40@0:8{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>={__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::pair<const std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}16"
+ "{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>=\"__tree_\"{__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::pair<const std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::pair<const std::string, std::vector<float>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::pair<const std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::pair<const std::string, std::vector<float>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}16@0:8"
+ "{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>=\"__tree_\"{__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::pair<const std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>={__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::pair<const std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}16@0:8"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/bpe_model.cc"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/builtin_pb/sentencepiece.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.h"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/filesystem.cc"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/mmap.h"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/model_factory.cc"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/model_interface.cc"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/model_interface.h"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/normalizer.cc"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/sentencepiece_processor.cc"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/unigram_model.cc"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/util.cc"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/util.h"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1106: exception: failed to insert key: negative value"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1108: exception: failed to insert key: zero-length key"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1122: exception: failed to insert key: invalid null character"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1127: exception: failed to insert key: wrong key order"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1339: exception: failed to modify unit: too large offset"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1675: exception: failed to build double-array: invalid null character"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1677: exception: failed to build double-array: negative value"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1692: exception: failed to build double-array: wrong key order"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:743: exception: failed to resize pool: std::bad_alloc"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:859: exception: failed to build rank index: std::bad_alloc"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/arena.cc"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/arenastring.cc"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/coded_stream.cc"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/common.cc"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/extension_set.cc"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/generated_message_util.cc"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arena_impl.h"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arenastring.h"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/extension_set_inl.h"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/io/coded_stream.h"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/parse_context.h"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/repeated_field.h"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/message_lite.cc"
- "/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/parse_context.cc"
- "T{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}},N,V_stateInputEspressoBuffers"
- "T{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}},N,V_stateOutputEspressoBuffers"
- "T{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>={__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<unsigned long>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}},N,V_stateInputEspressoBuffersShape"
- "v40@0:8{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}16"
- "v40@0:8{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>={__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<unsigned long>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}16"
- "{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>=\"__tree_\"{__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
- "{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}16@0:8"
- "{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>=\"__tree_\"{__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<unsigned long>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
- "{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>={__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<unsigned long>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}16@0:8"

```
