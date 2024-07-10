## SiriLiminal

> `/System/Library/PrivateFrameworks/SiriLiminal.framework/Versions/A/SiriLiminal`

```diff

-3400.145.2.0.0
-  __TEXT.__text: 0x570d4
-  __TEXT.__auth_stubs: 0x840
+3400.139.2.0.0
+  __TEXT.__text: 0x566d4
+  __TEXT.__auth_stubs: 0x7f0
   __TEXT.__objc_methlist: 0xea0
-  __TEXT.__gcc_except_tab: 0x43d0
-  __TEXT.__cstring: 0x565a
+  __TEXT.__gcc_except_tab: 0x4314
+  __TEXT.__cstring: 0x561c
   __TEXT.__const: 0xdad
   __TEXT.__oslogstring: 0xc3d
-  __TEXT.__unwind_info: 0x2020
+  __TEXT.__unwind_info: 0x1fd8
   __TEXT.__objc_classname: 0x29f
   __TEXT.__objc_methname: 0x316d
   __TEXT.__objc_methtype: 0x4b1

   __DATA_CONST.__objc_selrefs: 0xb88
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x438
-  __AUTH_CONST.__const: 0x19b0
+  __AUTH_CONST.__auth_got: 0x410
+  __AUTH_CONST.__const: 0x19a8
   __AUTH_CONST.__cfstring: 0x10e0
   __AUTH_CONST.__objc_const: 0x2a80
   __AUTH_CONST.__objc_floatobj: 0xb0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1507
-  Symbols:   3049
-  CStrings:  533
+  Functions: 1500
+  Symbols:   3032
+  CStrings:  535
 
Symbols:
+ GCC_except_table120
+ GCC_except_table163
+ GCC_except_table173
+ GCC_except_table175
+ GCC_except_table190
+ GCC_except_table195
+ GCC_except_table207
+ GCC_except_table214
+ GCC_except_table219
+ GCC_except_table232
+ GCC_except_table234
+ GCC_except_table247
+ GCC_except_table266
+ GCC_except_table270
+ GCC_except_table276
+ GCC_except_table280
+ GCC_except_table286
+ GCC_except_table288
+ GCC_except_table292
+ GCC_except_table296
+ GCC_except_table300
+ GCC_except_table311
+ __ZN13sentencepiece4MmapIcE4openEPKcS3_
- GCC_except_table164
- GCC_except_table170
- GCC_except_table174
- GCC_except_table176
- GCC_except_table209
- GCC_except_table217
- GCC_except_table220
- GCC_except_table233
- GCC_except_table236
- GCC_except_table267
- GCC_except_table272
- GCC_except_table277
- GCC_except_table283
- GCC_except_table287
- GCC_except_table289
- GCC_except_table294
- GCC_except_table298
- GCC_except_table301
- GCC_except_table312
- GCC_except_table317
- __ZN13sentencepiece22SentencePieceProcessor17MMapAuthenticatedENSt3__117basic_string_viewIcNS1_11char_traitsIcEEEE
- __ZN13sentencepiece4MmapIcE4openERKNSt3__14__fs10filesystem4pathEb
- __ZNKSt3__14__fs10filesystem4path10__filenameEv
- __ZNKSt3__14__fs10filesystem4path11parent_pathB8ne180100Ev
- __ZNKSt3__14__fs10filesystem4path13__parent_pathEv
- __ZNKSt3__14__fs10filesystem4path8filenameB8ne180100Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE16__init_with_sizeB8ne180100IPKcS8_EEvT_T0_m
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendB8ne180100IPKcLi0EEERS5_T_SA_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9__grow_byEmmmmmm
- __ZNSt3__115__quoted_outputB8ne180100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_S9_S4_S4_
- __ZNSt3__14__fs10filesystem4pathC2B8ne180100IPKcvEERKT_NS2_6formatE
- __ZNSt3__14__fs10filesystem8__statusERKNS1_4pathEPNS_10error_codeE
- _openat_authenticated_np
CStrings:
+ "(fd = ::open(filename, flag | O_BINARY)) >= 0"
+ "(p = reinterpret_cast<char*>(::mmap( 0, length, prot, MAP_SHARED, fd, 0))) != MAP_FAILED"
+ "(trie_blob.size() %!t(MISSING)rie_->unit_size()) == (0)"
+ "(trie_blob.size()) > (0)"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/bpe_model.cc"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/builtin_pb/sentencepiece.pb.cc"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.cc"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.h"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/filesystem.cc"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/mmap.h"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/model_factory.cc"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/model_interface.cc"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/model_interface.h"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/normalizer.cc"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/sentencepiece_processor.cc"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/unigram_model.cc"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/util.cc"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/util.h"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1106: exception: failed to insert key: negative value"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1108: exception: failed to insert key: zero-length key"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1122: exception: failed to insert key: invalid null character"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1127: exception: failed to insert key: wrong key order"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1339: exception: failed to modify unit: too large offset"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1675: exception: failed to build double-array: invalid null character"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1677: exception: failed to build double-array: negative value"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1692: exception: failed to build double-array: wrong key order"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:743: exception: failed to resize pool: std::bad_alloc"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:859: exception: failed to build rank index: std::bad_alloc"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/arena.cc"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/arenastring.cc"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/coded_stream.cc"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/common.cc"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/extension_set.cc"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/generated_message_util.cc"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arena_impl.h"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arenastring.h"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/extension_set_inl.h"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/io/coded_stream.h"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/parse_context.h"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/message_lite.cc"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/parse_context.cc"
+ "model_->status().ok()"
+ "r"
+ "r+"
+ "unknown open mode: "
- "(fd = ::open(filename.string().data(), mode)) >= 0"
- "(p = reinterpret_cast<char*>( ::mmap(0, length, PROT_READ, MAP_SHARED, fd, 0))) != MAP_FAILED"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/bpe_model.cc"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/builtin_pb/sentencepiece.pb.cc"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.cc"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.h"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/filesystem.cc"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/mmap.h"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/model_factory.cc"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/model_interface.cc"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/model_interface.h"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/normalizer.cc"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/sentencepiece_processor.cc"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/unigram_model.cc"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/util.cc"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/util.h"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1106: exception: failed to insert key: negative value"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1108: exception: failed to insert key: zero-length key"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1122: exception: failed to insert key: invalid null character"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1127: exception: failed to insert key: wrong key order"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1339: exception: failed to modify unit: too large offset"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1675: exception: failed to build double-array: invalid null character"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1677: exception: failed to build double-array: negative value"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1692: exception: failed to build double-array: wrong key order"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:743: exception: failed to resize pool: std::bad_alloc"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:859: exception: failed to build rank index: std::bad_alloc"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/arena.cc"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/arenastring.cc"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/coded_stream.cc"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/common.cc"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/extension_set.cc"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/generated_message_util.cc"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arena_impl.h"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arenastring.h"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/extension_set_inl.h"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/io/coded_stream.h"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/parse_context.h"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/message_lite.cc"
- "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/parse_context.cc"
- "Trie blob is wrongly formatted."
- "Trie data size exceeds the input blob size."
- "fd >= 0"
- "std::filesystem::is_directory(dir) && (dirfd = ::open(dir.string().data(), mode)) >= 0"

```
