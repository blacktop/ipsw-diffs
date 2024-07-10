## CoreSceneUnderstanding

> `/System/Library/PrivateFrameworks/CoreSceneUnderstanding.framework/Versions/A/CoreSceneUnderstanding`

```diff

-50.2.0.0.0
-  __TEXT.__text: 0xc3eec
-  __TEXT.__auth_stubs: 0x1290
+48.0.0.0.0
+  __TEXT.__text: 0xc28ec
+  __TEXT.__auth_stubs: 0x1260
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0x3308
-  __TEXT.__const: 0x1c20
-  __TEXT.__gcc_except_tab: 0xe20c
-  __TEXT.__cstring: 0x9189
-  __TEXT.__oslogstring: 0x888
+  __TEXT.__objc_methlist: 0x3300
+  __TEXT.__const: 0x1990
+  __TEXT.__gcc_except_tab: 0xdfa0
+  __TEXT.__cstring: 0x90db
+  __TEXT.__oslogstring: 0x788
   __TEXT.__swift5_typeref: 0x4b
   __TEXT.__constg_swiftt: 0x70
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_fieldmd: 0x5c
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x42e8
+  __TEXT.__unwind_info: 0x4288
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0xabd
-  __TEXT.__objc_methname: 0xa8a3
+  __TEXT.__objc_methname: 0xa852
   __TEXT.__objc_methtype: 0x59d7
-  __TEXT.__objc_stubs: 0x42a0
+  __TEXT.__objc_stubs: 0x4260
   __DATA_CONST.__got: 0x468
-  __DATA_CONST.__const: 0x328
+  __DATA_CONST.__const: 0x300
   __DATA_CONST.__objc_classlist: 0x2e0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1888
+  __DATA_CONST.__objc_selrefs: 0x1870
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x300
-  __AUTH_CONST.__auth_got: 0x958
+  __AUTH_CONST.__auth_got: 0x940
   __AUTH_CONST.__auth_ptr: 0x90
-  __AUTH_CONST.__const: 0x2948
-  __AUTH_CONST.__cfstring: 0x3080
+  __AUTH_CONST.__const: 0x27f0
+  __AUTH_CONST.__cfstring: 0x3000
   __AUTH_CONST.__objc_const: 0x8778
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x1f8

   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
-  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2877
-  Symbols:   528
-  CStrings:  937
+  Functions: 2843
+  Symbols:   524
+  CStrings:  935
 
Symbols:
- __ZNKSt3__14__fs10filesystem4path13__parent_pathEv
- __ZNSt3__14__fs10filesystem8__statusERKNS1_4pathEPNS_10error_codeE
- __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
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
+ "ImageCaptioning.config"
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
- "ImageCaptioning.config.json"
- "Non FP32 or FP16 datatype encountered!"
- "Trie blob is wrongly formatted."
- "Trie data size exceeds the input blob size."
- "fd >= 0"
- "image_captioning"
- "input cannot be nil!"
- "input has no tokens ids!"
- "std::filesystem::is_directory(dir) && (dirfd = ::open(dir.string().data(), mode)) >= 0"

```
