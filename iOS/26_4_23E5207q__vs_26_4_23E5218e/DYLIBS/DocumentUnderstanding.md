## DocumentUnderstanding

> `/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/DocumentUnderstanding`

```diff

-122.15.0.0.0
-  __TEXT.__text: 0x1dc5e4
+122.18.0.0.0
+  __TEXT.__text: 0x1dc7e4
   __TEXT.__auth_stubs: 0x3370
   __TEXT.__objc_methlist: 0x8e84
   __TEXT.__const: 0xc870

   __TEXT.__swift5_proto: 0x7d0
   __TEXT.__swift5_types: 0x3c0
   __TEXT.__oslogstring: 0x5863
-  __TEXT.__swift5_capture: 0x6c0
+  __TEXT.__swift5_capture: 0x6c4
   __TEXT.__swift_as_entry: 0x28c
   __TEXT.__swift_as_ret: 0x2d0
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__gcc_except_tab: 0x4224
-  __TEXT.__unwind_info: 0x7bd0
-  __TEXT.__eh_frame: 0xacc0
+  __TEXT.__unwind_info: 0x7bc0
+  __TEXT.__eh_frame: 0xaca0
   __TEXT.__objc_classname: 0x230c
   __TEXT.__objc_methname: 0xa179
   __TEXT.__objc_methtype: 0x1094
   __TEXT.__objc_stubs: 0x4740
   __DATA_CONST.__got: 0xe18
-  __DATA_CONST.__const: 0x1028
+  __DATA_CONST.__const: 0x1030
   __DATA_CONST.__objc_classlist: 0x4c8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftRegexBuilder.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CDC6EB6C-60AF-3A4B-8E20-9E370E6AAB97
-  Functions: 13767
-  Symbols:   871
+  UUID: DC35F8E9-2DD0-3ACC-871A-6A231AAE2FF1
+  Functions: 13759
+  Symbols:   872
   CStrings:  4728
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftSpatial
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
+ "/AppleInternal/Library/BuildRoots/4~CJJJugDvFliRrFOlrBRmwIfQWmimNJdEEBn6oYE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
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
- "/AppleInternal/Library/BuildRoots/4~CHqpugB5EQIAIatNpbtiwo8NDKfMRdiRVtBhuu0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
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
