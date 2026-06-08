## EventMetaDataExtractorPlugin

> `/System/Library/PrivateFrameworks/EventMetaDataExtractor.framework/PlugIns/EventMetaDataExtractorPlugin.appex/EventMetaDataExtractorPlugin`

```diff

 17.0.1.2.0
-  __TEXT.__text: 0x8b460
-  __TEXT.__auth_stubs: 0xdc0
+  __TEXT.__text: 0x8bc20
+  __TEXT.__auth_stubs: 0xe20
   __TEXT.__objc_stubs: 0x1300
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x76c
-  __TEXT.__const: 0x245f
-  __TEXT.__gcc_except_tab: 0xa974
+  __TEXT.__const: 0x24b7
+  __TEXT.__gcc_except_tab: 0xa91c
   __TEXT.__objc_methname: 0x1e30
-  __TEXT.__cstring: 0x6dbc
+  __TEXT.__cstring: 0x6d25
   __TEXT.__oslogstring: 0xfd3
-  __TEXT.__objc_classname: 0xa5
+  __TEXT.__objc_classname: 0xa1
   __TEXT.__objc_methtype: 0xcbd
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x3af0
-  __DATA_CONST.__auth_got: 0x6f0
-  __DATA_CONST.__got: 0x240
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x24a8
+  __TEXT.__unwind_info: 0x3b90
+  __DATA_CONST.__const: 0x2488
   __DATA_CONST.__cfstring: 0x12a0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x48
+  __DATA_CONST.__auth_got: 0x720
+  __DATA_CONST.__got: 0x240
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0xc78
   __DATA.__objc_selrefs: 0x780
   __DATA.__objc_ivar: 0x90
   __DATA.__objc_data: 0x230
   __DATA.__data: 0x318
   __DATA.__thread_vars: 0x30
-  __DATA.__thread_bss: 0x9d0
-  __DATA.__bss: 0x231
+  __DATA.__thread_bss: 0x10
+  __DATA.__bss: 0x249
   __DATA.__common: 0x458
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3CF40E1D-AE3B-3FA4-A020-71BE2BDAA06C
-  Functions: 2624
-  Symbols:   373
-  CStrings:  1313
+  UUID: 93CB44E9-28AE-332E-BFE5-463A772DCDD3
+  Functions: 2639
+  Symbols:   379
+  CStrings:  1307
 
Symbols:
+ __ZNSt3__112__get_sp_mutEPKv
+ __ZNSt3__18__sp_mut4lockEv
+ __ZNSt3__18__sp_mut6unlockEv
+ __tlv_atexit
+ _log1p
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x25
+ _objc_retain_x28
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x24
- _objc_retain_x26
- _sprintf
CStrings:
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1111: exception: failed to insert key: negative value"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1113: exception: failed to insert key: zero-length key"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1127: exception: failed to insert key: invalid null character"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1132: exception: failed to insert key: wrong key order"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1344: exception: failed to modify unit: too large offset"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1680: exception: failed to build double-array: invalid null character"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1682: exception: failed to build double-array: negative value"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1697: exception: failed to build double-array: wrong key order"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:748: exception: failed to resize pool: std::bad_alloc"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:864: exception: failed to build rank index: std::bad_alloc"
+ "Failed to build the TRIE for PrefixMatcher"
+ "Trie data size is not divisible by 1024."
+ "could not parse ModelProto from "
+ "could not read "
+ "normalized block must be null terminated."
+ "sentencepiece"
- "!"
- "(0) == (trie_->build(key.size(), const_cast<char **>(&key[0]), nullptr, nullptr))"
- "(index) < (static_cast<int>(symbols.size()))"
- "(index) >= (0)"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SentencePiece/src/bpe_model.cc"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1106: exception: failed to insert key: negative value"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1108: exception: failed to insert key: zero-length key"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1122: exception: failed to insert key: invalid null character"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1127: exception: failed to insert key: wrong key order"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1339: exception: failed to modify unit: too large offset"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1675: exception: failed to build double-array: invalid null character"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1677: exception: failed to build double-array: negative value"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1692: exception: failed to build double-array: wrong key order"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:743: exception: failed to resize pool: std::bad_alloc"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:859: exception: failed to build rank index: std::bad_alloc"
- "@"
- "INTERNAL"
- "OK"
- "_"
- "input->ReadAll(&serialized)"
- "norm_to_orig"
- "normalized"

```
