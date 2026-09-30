## CoreSceneUnderstanding

> `/System/Library/PrivateFrameworks/CoreSceneUnderstanding.framework/CoreSceneUnderstanding`

```diff

-83.0.0.0.0
-  __TEXT.__text: 0xc542c
+83.1.0.0.0
+  __TEXT.__text: 0xc8948
   __TEXT.__auth_stubs: 0x15a0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x393c
-  __TEXT.__const: 0x1fd0
-  __TEXT.__gcc_except_tab: 0xefe8
-  __TEXT.__cstring: 0x8c9d
+  __TEXT.__const: 0x1ef0
+  __TEXT.__gcc_except_tab: 0xf008
+  __TEXT.__cstring: 0xbece
   __TEXT.__oslogstring: 0xed8
   __TEXT.__swift5_typeref: 0x97
   __TEXT.__constg_swiftt: 0xe8

   __TEXT.__swift5_fieldmd: 0x9c
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x4448
+  __TEXT.__unwind_info: 0x45c0
   __TEXT.__eh_frame: 0x80
-  __TEXT.__objc_classname: 0xb41
-  __TEXT.__objc_methname: 0xb266
-  __TEXT.__objc_methtype: 0x3df9
-  __TEXT.__objc_stubs: 0x49e0
+  __TEXT.__objc_classname: 0xb94
+  __TEXT.__objc_methname: 0xb2ad
+  __TEXT.__objc_methtype: 0x3d96
+  __TEXT.__objc_stubs: 0x4a00
   __DATA_CONST.__got: 0x4e0
   __DATA_CONST.__const: 0x6f0
   __DATA_CONST.__objc_classlist: 0x310

   __AUTH.__thread_bss: 0x9d0
   __DATA.__objc_ivar: 0x6c4
   __DATA.__data: 0x398
-  __DATA.__bss: 0x211
+  __DATA.__bss: 0x221
   __DATA.__common: 0x3d5
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A85E3B47-C85B-3375-A4A7-817B1964985C
-  Functions: 3075
-  Symbols:   589
-  CStrings:  3330
+  UUID: CCC7F3D4-D878-3E1C-885D-EA0D86E5496E
+  Functions: 3118
+  Symbols:   590
+  CStrings:  3360
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_release_x2
+ _objc_release_x3
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
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
+ "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__ranges/view_interface.h:140: libc++ Hardening assertion !empty() failed: Precondition `!empty()` not satisfied. `.back()` called on an empty view.\n"
+ "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
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
+ "CSUModelCatalogVisualGenerationBase"
+ "CSUModelCatalogVisualGenerationBaseLock"
+ "T{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::pair<const std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::pair<const std::string, std::vector<float>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}},R,N,V_stateInputEspressoBuffers"
+ "T{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::pair<const std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::pair<const std::string, std::vector<float>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}},R,N,V_stateOutputEspressoBuffers"
+ "T{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>={__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::pair<const std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}},R,N,V_stateInputEspressoBuffersShape"
+ "{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>=\"__tree_\"{__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::pair<const std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::pair<const std::string, std::vector<float>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::pair<const std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::pair<const std::string, std::vector<float>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}16@0:8"
+ "{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>=\"__tree_\"{__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::pair<const std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>={__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::pair<const std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}16@0:8"
+ "{unordered_map<std::string, ik::EspressoTensor, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, ik::EspressoTensor>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, ik::EspressoTensor>, std::__unordered_map_hasher<std::string, std::pair<const std::string, ik::EspressoTensor>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::pair<const std::string, ik::EspressoTensor>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::pair<const std::string, ik::EspressoTensor>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::EspressoTensor>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::EspressoTensor>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::EspressoTensor>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::EspressoTensor>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{unordered_map<std::string, ik::Tensor, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, ik::Tensor>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, ik::Tensor>, std::__unordered_map_hasher<std::string, std::pair<const std::string, ik::Tensor>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::pair<const std::string, ik::Tensor>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::pair<const std::string, ik::Tensor>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{unordered_map<std::string, ik::Tensor, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, ik::Tensor>>>={__hash_table<std::__hash_value_type<std::string, ik::Tensor>, std::__unordered_map_hasher<std::string, std::pair<const std::string, ik::Tensor>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::pair<const std::string, ik::Tensor>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::pair<const std::string, ik::Tensor>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>>={?=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>={?=Q}}}}{?={__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *>=^v}}{?=Q}{?=f}}}24@0:8@16"
+ "{unordered_map<std::string, ik::Tensor, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, ik::Tensor>>>={__hash_table<std::__hash_value_type<std::string, ik::Tensor>, std::__unordered_map_hasher<std::string, std::pair<const std::string, ik::Tensor>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::pair<const std::string, ik::Tensor>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::pair<const std::string, ik::Tensor>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>>={?=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>={?=Q}}}}{?={__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *>=^v}}{?=Q}{?=f}}}40@0:8{vector<unsigned int, std::allocator<unsigned int>>=^I^I{?=^I}}16"
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
- "T{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}},R,N,V_stateInputEspressoBuffers"
- "T{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}},R,N,V_stateOutputEspressoBuffers"
- "T{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>={__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<unsigned long>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}},R,N,V_stateInputEspressoBuffersShape"
- "{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>=\"__tree_\"{__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
- "{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}16@0:8"
- "{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>=\"__tree_\"{__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<unsigned long>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
- "{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>={__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<unsigned long>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}16@0:8"
- "{unordered_map<std::string, ik::EspressoTensor, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, ik::EspressoTensor>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, ik::EspressoTensor>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, ik::EspressoTensor>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, ik::EspressoTensor>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, ik::EspressoTensor>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::EspressoTensor>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::EspressoTensor>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::EspressoTensor>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::EspressoTensor>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "{unordered_map<std::string, ik::Tensor, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, ik::Tensor>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, ik::Tensor>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, ik::Tensor>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, ik::Tensor>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, ik::Tensor>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "{unordered_map<std::string, ik::Tensor, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, ik::Tensor>>>={__hash_table<std::__hash_value_type<std::string, ik::Tensor>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, ik::Tensor>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, ik::Tensor>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, ik::Tensor>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>>={?=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>={?=Q}}}}{?={__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *>=^v}}{?=Q}{?=f}}}24@0:8@16"
- "{unordered_map<std::string, ik::Tensor, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, ik::Tensor>>>={__hash_table<std::__hash_value_type<std::string, ik::Tensor>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, ik::Tensor>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, ik::Tensor>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, ik::Tensor>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>>={?=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>={?=Q}}}}{?={__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *>=^v}}{?=Q}{?=f}}}40@0:8{vector<unsigned int, std::allocator<unsigned int>>=^I^I{?=^I}}16"

```
