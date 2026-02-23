## CoreSceneUnderstanding

> `/System/Library/PrivateFrameworks/CoreSceneUnderstanding.framework/CoreSceneUnderstanding`

```diff

-83.1.0.0.0
-  __TEXT.__text: 0xc8948
+87.0.0.0.0
+  __TEXT.__text: 0xc8be8
   __TEXT.__auth_stubs: 0x15a0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x393c
   __TEXT.__const: 0x1ef0
-  __TEXT.__gcc_except_tab: 0xf008
-  __TEXT.__cstring: 0xbece
+  __TEXT.__gcc_except_tab: 0xf058
+  __TEXT.__cstring: 0xbdee
   __TEXT.__oslogstring: 0xed8
   __TEXT.__swift5_typeref: 0x97
   __TEXT.__constg_swiftt: 0xe8

   __DATA_CONST.__objc_arraydata: 0x380
   __AUTH_CONST.__auth_got: 0xae8
   __AUTH_CONST.__const: 0x2778
-  __AUTH_CONST.__cfstring: 0x3740
+  __AUTH_CONST.__cfstring: 0x3780
   __AUTH_CONST.__objc_const: 0x8e28
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_arrayobj: 0x270

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CCC7F3D4-D878-3E1C-885D-EA0D86E5496E
-  Functions: 3118
+  UUID: F71370D3-F976-3AF4-8073-9DE22CDC1BD7
+  Functions: 3119
   Symbols:   590
-  CStrings:  3360
+  CStrings:  3363
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
+ "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:431: libc++ Hardening assertion __n <= size() failed: remove_prefix() can't remove more than size()\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__ranges/view_interface.h:140: libc++ Hardening assertion !empty() failed: Precondition `!empty()` not satisfied. `.back()` called on an empty view.\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRjugATe_CyjDoZCOlPvOF3-9hI1y87zgjoxao/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/bpe_model.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/builtin_pb/sentencepiece.pb.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.h"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/filesystem.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/mmap.h"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/model_factory.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/model_interface.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/model_interface.h"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/normalizer.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/sentencepiece_processor.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/unigram_model.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/util.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/util.h"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/darts_clone/darts.h:1106: exception: failed to insert key: negative value"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/darts_clone/darts.h:1108: exception: failed to insert key: zero-length key"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/darts_clone/darts.h:1122: exception: failed to insert key: invalid null character"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/darts_clone/darts.h:1127: exception: failed to insert key: wrong key order"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/darts_clone/darts.h:1339: exception: failed to modify unit: too large offset"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/darts_clone/darts.h:1675: exception: failed to build double-array: invalid null character"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/darts_clone/darts.h:1677: exception: failed to build double-array: negative value"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/darts_clone/darts.h:1692: exception: failed to build double-array: wrong key order"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/darts_clone/darts.h:743: exception: failed to resize pool: std::bad_alloc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/darts_clone/darts.h:859: exception: failed to build rank index: std::bad_alloc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/arena.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/arenastring.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/coded_stream.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/common.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/extension_set.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/generated_message_util.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arena_impl.h"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arenastring.h"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/extension_set_inl.h"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/io/coded_stream.h"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/parse_context.h"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/repeated_field.h"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/message_lite.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/parse_context.cc"
+ "ImageCaptioningMD8_h74dt6bujy-1560"
+ "VideoCaptioning_v8.0.0_fxfs4chdvb-21620"
- "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
- "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:431: libc++ Hardening assertion __n <= size() failed: remove_prefix() can't remove more than size()\n"
- "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__ranges/view_interface.h:140: libc++ Hardening assertion !empty() failed: Precondition `!empty()` not satisfied. `.back()` called on an empty view.\n"
- "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CInUugDsCpARJYAxr1cxKBZ96mycgyu3NCcYdl0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/bpe_model.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/builtin_pb/sentencepiece.pb.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.h"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/filesystem.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/mmap.h"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/model_factory.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/model_interface.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/model_interface.h"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/normalizer.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/sentencepiece_processor.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/unigram_model.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/util.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/util.h"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:1106: exception: failed to insert key: negative value"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:1108: exception: failed to insert key: zero-length key"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:1122: exception: failed to insert key: invalid null character"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:1127: exception: failed to insert key: wrong key order"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:1339: exception: failed to modify unit: too large offset"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:1675: exception: failed to build double-array: invalid null character"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:1677: exception: failed to build double-array: negative value"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:1692: exception: failed to build double-array: wrong key order"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:743: exception: failed to resize pool: std::bad_alloc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:859: exception: failed to build rank index: std::bad_alloc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/arena.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/arenastring.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/coded_stream.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/common.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/extension_set.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/generated_message_util.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arena_impl.h"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arenastring.h"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/extension_set_inl.h"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/io/coded_stream.h"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/parse_context.h"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/repeated_field.h"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/message_lite.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/parse_context.cc"

```
