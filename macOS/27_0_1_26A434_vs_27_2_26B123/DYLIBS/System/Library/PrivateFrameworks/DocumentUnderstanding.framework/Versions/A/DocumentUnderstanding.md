## DocumentUnderstanding

> `/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/Versions/A/DocumentUnderstanding`

```diff

-176.3.0.1.0
-  __TEXT.__text: 0x19c308
+192.1.0.0.0
+  __TEXT.__text: 0x1a2518
   __TEXT.__objc_methlist: 0x893c
-  __TEXT.__const: 0xc500
+  __TEXT.__const: 0xc510
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__constg_swiftt: 0x4e50
   __TEXT.__swift5_typeref: 0x2604

   __TEXT.__swift5_fieldmd: 0x393c
   __TEXT.__swift5_builtin: 0x118
   __TEXT.__swift5_assocty: 0x9a8
-  __TEXT.__cstring: 0xaba5
+  __TEXT.__cstring: 0xad77
   __TEXT.__swift5_proto: 0x73c
   __TEXT.__swift5_types: 0x348
-  __TEXT.__swift5_capture: 0x7cc
+  __TEXT.__swift5_capture: 0xa6c
   __TEXT.__oslogstring: 0x4667
   __TEXT.__swift_as_entry: 0x260
   __TEXT.__swift_as_ret: 0x298
   __TEXT.__swift_as_cont: 0x3cc
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__gcc_except_tab: 0x40ac
-  __TEXT.__unwind_info: 0x72d0
-  __TEXT.__eh_frame: 0x994c
+  __TEXT.__gcc_except_tab: 0x4134
+  __TEXT.__unwind_info: 0x72f0
+  __TEXT.__eh_frame: 0x9970
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__got: 0xd50
-  __AUTH_CONST.__const: 0x8b58
+  __AUTH_CONST.__const: 0x91e8
   __AUTH_CONST.__cfstring: 0x260
   __AUTH_CONST.__objc_const: 0x8550
   __AUTH_CONST.__weak_auth_got: 0x38
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1858
-  __AUTH_CONST.__auth_ptr: 0xbe8
+  __AUTH_CONST.__auth_got: 0x1860
+  __AUTH_CONST.__auth_ptr: 0xbd8
   __AUTH.__objc_data: 0x3160
   __AUTH.__data: 0x2b70
   __AUTH.__thread_vars: 0x48

   __DATA.__bss: 0xad99
   __DATA.__common: 0x749
   __DATA_DIRTY.__objc_data: 0x1990
-  __DATA_DIRTY.__data: 0x3000
+  __DATA_DIRTY.__data: 0x2ff8
   __DATA_DIRTY.__bss: 0x1bc0
   __DATA_DIRTY.__common: 0x2d0
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12747
+  Functions: 12809
   Symbols:   786
-  CStrings:  1021
+  CStrings:  1031
 
CStrings:
+ "!pieces_blob.empty()"
+ "(piece_offsets_[i]) < (pieces_blob.size())"
+ "(pieces_blob.back()) == ('\\0')"
+ "(unk_id_) < (GetPieceSize())"
+ "(unk_id_) >= (0)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/src/mmap_model_proto.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1161: exception: failed to insert key: negative value"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1163: exception: failed to insert key: zero-length key"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1177: exception: failed to insert key: invalid null character"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1182: exception: failed to insert key: wrong key order"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1394: exception: failed to modify unit: too large offset"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1730: exception: failed to build double-array: invalid null character"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1732: exception: failed to build double-array: negative value"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1747: exception: failed to build double-array: wrong key order"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:798: exception: failed to resize pool: std::bad_alloc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:914: exception: failed to build rank index: std::bad_alloc"
+ "The trie of the pieces is invalid."
+ "The trie of the reserved ids is invalid."
+ "pieces_.validate(GetPieceSize())"
+ "precompiled_charsmap is invalid."
+ "reserved_id_map_.validate(GetPieceSize())"
- "(num_nodes) < (trie_results.size())"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1111: exception: failed to insert key: negative value"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1113: exception: failed to insert key: zero-length key"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1127: exception: failed to insert key: invalid null character"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1132: exception: failed to insert key: wrong key order"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1344: exception: failed to modify unit: too large offset"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1680: exception: failed to build double-array: invalid null character"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1682: exception: failed to build double-array: negative value"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1697: exception: failed to build double-array: wrong key order"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:748: exception: failed to resize pool: std::bad_alloc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:864: exception: failed to build rank index: std::bad_alloc"
```
