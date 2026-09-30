## Lexicon

> `/System/Library/PrivateFrameworks/Lexicon.framework/Versions/A/Lexicon`

```diff

-170.0.0.0.0
-  __TEXT.__text: 0xd5294
-  __TEXT.__auth_stubs: 0x13f0
-  __TEXT.__gcc_except_tab: 0xa5d4
-  __TEXT.__const: 0xe473
-  __TEXT.__cstring: 0xa5c7
-  __TEXT.__oslogstring: 0x1966
+173.8.0.0.0
+  __TEXT.__text: 0xddde8
+  __TEXT.__auth_stubs: 0x15a0
+  __TEXT.__objc_methlist: 0x94
+  __TEXT.__const: 0xe51f
+  __TEXT.__gcc_except_tab: 0xb09c
+  __TEXT.__cstring: 0xa943
+  __TEXT.__oslogstring: 0x198f
   __TEXT.__ustring: 0x98e
-  __TEXT.__unwind_info: 0x4ca0
-  __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0xdd8
-  __AUTH_CONST.__auth_got: 0xa00
-  __AUTH_CONST.__const: 0xa428
-  __AUTH_CONST.__cfstring: 0xe60
+  __TEXT.__unwind_info: 0x4d10
+  __TEXT.__objc_classname: 0x28
+  __TEXT.__objc_methname: 0x21c
+  __TEXT.__objc_methtype: 0x237
+  __TEXT.__objc_stubs: 0x1e0
+  __DATA_CONST.__got: 0x228
+  __DATA_CONST.__const: 0x10c0
+  __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_selrefs: 0xa8
+  __DATA_CONST.__objc_superrefs: 0x10
+  __AUTH_CONST.__auth_got: 0xae0
+  __AUTH_CONST.__const: 0xa410
+  __AUTH_CONST.__cfstring: 0x1360
+  __AUTH_CONST.__objc_const: 0x1e0
+  __AUTH.__objc_data: 0xa0
   __AUTH.__thread_vars: 0xa8
   __AUTH.__thread_bss: 0x2300
+  __DATA.__objc_ivar: 0x10
   __DATA.__data: 0x89
+  __DATA.__bss: 0x868
   __DATA.__common: 0x10
-  __DATA.__bss: 0xa78
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
+  - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/LinguisticData.framework/Versions/A/LinguisticData
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
+  - /usr/lib/libgermantok.dylib
   - /usr/lib/libicucore.A.dylib
+  - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: CB56B935-5BA1-3433-8A90-4C19028119BA
-  Functions: 4263
-  Symbols:   540
-  CStrings:  1336
+  UUID: 1D87ACA5-293A-3745-9DBB-D6D341190BD2
+  Functions: 4318
+  Symbols:   580
+  CStrings:  1465
 
Symbols:
+ _CFArrayCreate
+ _CFStringAppend
+ _CFStringGetCharacterAtIndex
+ _LXAnalyzerSetSupplementalLexicons
+ _LXErrorDomain
+ _NSLocaleCountryCode
+ _NSLocaleLanguageCode
+ _NSLocaleScriptCode
+ _OBJC_CLASS_$_LXLanguageIdentifier
+ _OBJC_CLASS_$_LXLexiconChecker
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSObject
+ _OBJC_METACLASS_$_LXLanguageIdentifier
+ _OBJC_METACLASS_$_LXLexiconChecker
+ _OBJC_METACLASS_$_NSObject
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ ___NSArray0__struct
+ __objc_empty_cache
+ __sl_dlopen
+ _abort_report_np
+ _dlerror
+ _dlsym
+ _germantok_tokenize
+ _kCFLocaleIdentifier
+ _kLXAnalyzerLexiconDataFileKey
+ _objc_alloc
+ _objc_autorelease
+ _objc_autoreleaseReturnValue
+ _objc_enumerationMutation
+ _objc_msgSend
+ _objc_msgSendSuper2
+ _objc_release
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_storeStrong
+ _u_getNumericValue
+ _u_hasBinaryProperty
+ _u_isWhitespace
+ _u_ispunct
+ _ubrk_close
+ _ubrk_getRuleStatus
+ _ubrk_next
+ _ubrk_open
+ _ubrk_setUText
+ _utext_char32At
+ _utext_close
+ _utext_openUChars
+ _utext_openUTF8
- __ZNKSt9exception4whatEv
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev
- __ZNSt3__112strstreambufC1El
- __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEED0Ev
- __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEED1Ev
- __ZNSt3__19strstreamD1Ev
- __ZTINSt3__113basic_istreamIcNS_11char_traitsIcEEEE
- __ZTTNSt3__19strstreamE
- __ZTVNSt3__19strstreamE
- __ZTv0_n24_NSt3__113basic_istreamIcNS_11char_traitsIcEEED0Ev
- __ZTv0_n24_NSt3__113basic_istreamIcNS_11char_traitsIcEEED1Ev
- ___cxa_atexit
CStrings:
+ "!localeIdentifier.empty() && \"Invalid locale. Failed to obtain locale identifier from the locale.\""
+ "-d "
+ ".cxx_construct"
+ ".cxx_destruct"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/include/trie/cedarpp.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/include/trie/darts_clone.h:1146: exception: failed to insert key: negative value"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/include/trie/darts_clone.h:1148: exception: failed to insert key: zero-length key"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/include/trie/darts_clone.h:1162: exception: failed to insert key: invalid null character"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/include/trie/darts_clone.h:1167: exception: failed to insert key: wrong key order"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/include/trie/darts_clone.h:1385: exception: failed to modify unit: too large offset"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/include/trie/darts_clone.h:1731: exception: failed to build double-array: invalid null character"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/include/trie/darts_clone.h:1733: exception: failed to build double-array: negative value"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/include/trie/darts_clone.h:1748: exception: failed to build double-array: wrong key order"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/include/trie/darts_clone.h:708: exception: failed to resize pool: std::bad_alloc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/include/trie/darts_clone.h:847: exception: failed to build rank index: std::bad_alloc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Lexicon/Source/MeCab/char_property.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Lexicon/Source/MeCab/compressed_connector.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Lexicon/Source/MeCab/dictionary.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Lexicon/Source/MeCab/lattice_impl.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Lexicon/Source/MeCab/mmap.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Lexicon/Source/MeCab/param.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Lexicon/Source/MeCab/tagger.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Lexicon/Source/MeCab/tokenizer.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Lexicon/Source/MeCab/viterbi.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Lexicon/Source/MeCab/writer.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/mapper.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/mapper.cc:115: MARISA_STATE_ERROR: !is_open()"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/mapper.cc:116: MARISA_IO_ERROR: size > avail_"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/mapper.cc:80: MARISA_NULL_ERROR: (ptr == NULL) && (size != 0)"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/mapper.cc:89: MARISA_STATE_ERROR: !is_open()"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/mapper.cc:90: MARISA_IO_ERROR: size > avail_"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/mapper.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/mapper.h:31: MARISA_NULL_ERROR: (objs == NULL) && (num_objs != 0)"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/mapper.h:32: MARISA_SIZE_ERROR: num_objs > (MARISA_SIZE_MAX / sizeof(T))"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/writer.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/writer.cc:118: MARISA_STATE_ERROR: !is_open()"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/writer.cc:132: MARISA_IO_ERROR: size_written <= 0"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/writer.cc:137: MARISA_IO_ERROR: ::fwrite(data, 1, size, file_) != size"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/writer.cc:138: MARISA_IO_ERROR: ::fflush(file_) != 0"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/writer.cc:143: MARISA_IO_ERROR: !stream_->write(static_cast<const char*>(data), static_cast<std::streamsize>(size))"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/writer.cc:145: MARISA_IO_ERROR: std::ios_base::failure"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/writer.cc:79: MARISA_STATE_ERROR: !is_open()"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/writer.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/writer.h:33: MARISA_NULL_ERROR: (objs == NULL) && (num_objs != 0)"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/writer.h:34: MARISA_SIZE_ERROR: num_objs > (MARISA_SIZE_MAX / sizeof(T))"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/config.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/config.h:117: MARISA_CODE_ERROR: undefined tail mode"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/config.h:138: MARISA_CODE_ERROR: undefined node order"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/config.h:52: MARISA_CODE_ERROR: (config_flags & ~MARISA_CONFIG_MASK) != 0"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/config.h:96: MARISA_CODE_ERROR: undefined cache level"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/header.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/header.h:21: MARISA_FORMAT_ERROR: !test_header(ptr)"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/louds-trie.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/louds-trie.cc:198: MARISA_BOUND_ERROR: payload_id >= size()"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/louds-trie.cc:467: MARISA_MEMORY_ERROR: std::bad_alloc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/louds-trie.cc:491: MARISA_MEMORY_ERROR: next_trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/louds-trie.cc:509: MARISA_MEMORY_ERROR: next_trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/louds-trie.cc:585: MARISA_MEMORY_ERROR: next_trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/tail.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/tail.cc:172: MARISA_RANGE_ERROR: current.length() == 0"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/tail.cc:17: MARISA_NULL_ERROR: offsets == NULL"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/tail.cc:194: MARISA_SIZE_ERROR: buf_.size() > MARISA_UINT32_MAX"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/tail.cc:40: MARISA_CODE_ERROR: undefined tail mode"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/vector/bit-vector.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/vector/bit-vector.h:134: MARISA_FORMAT_ERROR: temp_num_1s > size_"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/vector/bit-vector.h:58: MARISA_SIZE_ERROR: size_ == MARISA_UINT32_MAX"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/vector/flat-vector.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/vector/flat-vector.h:132: MARISA_FORMAT_ERROR: temp_value_size > 32"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/vector/vector.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/vector/vector.h:114: MARISA_STATE_ERROR: fixed_"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/vector/vector.h:122: MARISA_STATE_ERROR: fixed_"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/vector/vector.h:210: MARISA_FORMAT_ERROR: (total_size % sizeof(T)) != 0"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc:100: MARISA_STATE_ERROR: trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc:109: MARISA_STATE_ERROR: trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc:115: MARISA_STATE_ERROR: trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc:121: MARISA_STATE_ERROR: trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc:127: MARISA_STATE_ERROR: trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc:134: MARISA_STATE_ERROR: trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc:140: MARISA_STATE_ERROR: trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc:147: MARISA_STATE_ERROR: trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc:153: MARISA_STATE_ERROR: trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc:195: MARISA_STATE_ERROR: trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc:20: MARISA_MEMORY_ERROR: temp.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc:41: MARISA_NULL_ERROR: (ptr == NULL) && (size != 0)"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc:44: MARISA_MEMORY_ERROR: temp.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/word_trie/UnigramTrieNode.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/word_trie/UnigramsCompiler.cpp"
+ "/usr/lib/libmecab.dylib"
+ "/usr/local/lib/libmecab.dylib"
+ "@\"NSArray\""
+ "@16@0:8"
+ "@32@0:8@16^@24"
+ "@40@0:8@16@24^@32"
+ "Array should contains dictionaries"
+ "B48@0:8@16@24@32^@40"
+ "Failed to load lexicon"
+ "Failed to set additional lexicons"
+ "LXAnalyzer not provided"
+ "LXLanguageIdentifier"
+ "LXLexiconChecker"
+ "LanguageIdentifierImpl"
+ "LanguageIdentifierImpl.cpp"
+ "LexiconCheckerImpl"
+ "LexiconCheckerImpl.cpp"
+ "Locale was not provided"
+ "No available lexicon found for the locales: ["
+ "No available lexicon found."
+ "RuleBasedTokenizer.cpp"
+ "ScopedUText"
+ "StaticLexiconRepository.cpp"
+ "T@\"NSArray\",R,C,N,V_availableLocales"
+ "Tagger does not exist"
+ "Unable to load the lexicon for locale %s"
+ "_availableLocales"
+ "_impl"
+ "addObject:"
+ "availableLocales"
+ "canonicalLanguageIdentifierFromString:"
+ "checkValidityOfString:locales:allowlist:error:"
+ "componentsFromLocaleIdentifier:"
+ "costFactor"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "detectLanguagesInString:constraints:error:"
+ "detectLanguagesInString:error:"
+ "dictionary"
+ "en-AU"
+ "en-CA"
+ "en-GB"
+ "en-IN"
+ "en-JP"
+ "en-NZ"
+ "en-SG"
+ "en-US"
+ "en-ZA"
+ "es-419"
+ "es-ES"
+ "es-MX"
+ "false && \"Failed to create UText from UTF-8 string\""
+ "fr-CA"
+ "fr-FR"
+ "hasPrefix:"
+ "initWithCapacity:"
+ "initWithLocaleIdentifier:"
+ "ja"
+ "length"
+ "length > 0"
+ "loadLexicons"
+ "localeIdentifier"
+ "localeIdentifierFromComponents:"
+ "locales must be an array of NSLocale objects."
+ "m_tokenizer->isValid() && \"Failed to construct the rule based tokenizer.\""
+ "mecab_destroy"
+ "mecab_new2"
+ "mecab_sparse_tonode2"
+ "objectForKeyedSubscript:"
+ "primary-locale"
+ "primary_locale_sysdic_->type() == MECAB_SYS_DIC"
+ "pt-BR"
+ "pt-PT"
+ "secondary-locale"
+ "setObject:forKeyedSubscript:"
+ "toLogProb"
+ "tokenize"
+ "use STR as the locale of primary lexicon"
+ "use STR as the locale of secondary lexicon"
+ "usr/share/tokenizer"
+ "utf-16"
+ "v16@0:8"
+ "yue-Hant"
+ "yue-Hant-HK"
+ "yue_HK"
+ "zh"
+ "zh-Hans"
+ "zh-Hans-CN"
+ "zh-Hant"
+ "zh-Hant-HK"
+ "zh-Hant-TW"
+ "zh_CN"
+ "zh_HK"
+ "zh_TW"
+ "{unique_ptr<lexicon::LanguageIdentifierImpl, std::default_delete<lexicon::LanguageIdentifierImpl>>=\"__ptr_\"{__compressed_pair<lexicon::LanguageIdentifierImpl *, std::default_delete<lexicon::LanguageIdentifierImpl>>=\"__value_\"^{LanguageIdentifierImpl}}}"
+ "{unique_ptr<lexicon::LexiconCheckerImpl, std::default_delete<lexicon::LexiconCheckerImpl>>=\"__ptr_\"{__compressed_pair<lexicon::LexiconCheckerImpl *, std::default_delete<lexicon::LexiconCheckerImpl>>=\"__value_\"^{LexiconCheckerImpl}}}"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/include/trie/cedarpp.h"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/include/trie/darts_clone.h:1146: exception: failed to insert key: negative value"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/include/trie/darts_clone.h:1148: exception: failed to insert key: zero-length key"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/include/trie/darts_clone.h:1162: exception: failed to insert key: invalid null character"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/include/trie/darts_clone.h:1167: exception: failed to insert key: wrong key order"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/include/trie/darts_clone.h:1385: exception: failed to modify unit: too large offset"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/include/trie/darts_clone.h:1731: exception: failed to build double-array: invalid null character"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/include/trie/darts_clone.h:1733: exception: failed to build double-array: negative value"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/include/trie/darts_clone.h:1748: exception: failed to build double-array: wrong key order"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/include/trie/darts_clone.h:708: exception: failed to resize pool: std::bad_alloc"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/include/trie/darts_clone.h:847: exception: failed to build rank index: std::bad_alloc"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Lexicon/Source/MeCab/char_property.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Lexicon/Source/MeCab/compressed_connector.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Lexicon/Source/MeCab/dictionary.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Lexicon/Source/MeCab/lattice_impl.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Lexicon/Source/MeCab/mmap.h"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Lexicon/Source/MeCab/param.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Lexicon/Source/MeCab/tagger.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Lexicon/Source/MeCab/tokenizer.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Lexicon/Source/MeCab/viterbi.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/Lexicon/Source/MeCab/writer.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/mapper.cc"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/mapper.cc:115: MARISA_STATE_ERROR: !is_open()"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/mapper.cc:116: MARISA_IO_ERROR: size > avail_"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/mapper.cc:80: MARISA_NULL_ERROR: (ptr == NULL) && (size != 0)"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/mapper.cc:89: MARISA_STATE_ERROR: !is_open()"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/mapper.cc:90: MARISA_IO_ERROR: size > avail_"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/mapper.h"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/mapper.h:31: MARISA_NULL_ERROR: (objs == NULL) && (num_objs != 0)"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/mapper.h:32: MARISA_SIZE_ERROR: num_objs > (MARISA_SIZE_MAX / sizeof(T))"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/writer.cc"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/writer.cc:118: MARISA_STATE_ERROR: !is_open()"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/writer.cc:132: MARISA_IO_ERROR: size_written <= 0"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/writer.cc:137: MARISA_IO_ERROR: ::fwrite(data, 1, size, file_) != size"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/writer.cc:138: MARISA_IO_ERROR: ::fflush(file_) != 0"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/writer.cc:143: MARISA_IO_ERROR: !stream_->write(static_cast<const char*>(data), static_cast<std::streamsize>(size))"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/writer.cc:145: MARISA_IO_ERROR: std::ios_base::failure"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/writer.cc:79: MARISA_STATE_ERROR: !is_open()"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/writer.h"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/writer.h:33: MARISA_NULL_ERROR: (objs == NULL) && (num_objs != 0)"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/io/writer.h:34: MARISA_SIZE_ERROR: num_objs > (MARISA_SIZE_MAX / sizeof(T))"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/config.h"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/config.h:117: MARISA_CODE_ERROR: undefined tail mode"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/config.h:138: MARISA_CODE_ERROR: undefined node order"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/config.h:52: MARISA_CODE_ERROR: (config_flags & ~MARISA_CONFIG_MASK) != 0"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/config.h:96: MARISA_CODE_ERROR: undefined cache level"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/header.h"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/header.h:21: MARISA_FORMAT_ERROR: !test_header(ptr)"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/louds-trie.cc"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/louds-trie.cc:198: MARISA_BOUND_ERROR: payload_id >= size()"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/louds-trie.cc:467: MARISA_MEMORY_ERROR: std::bad_alloc"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/louds-trie.cc:491: MARISA_MEMORY_ERROR: next_trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/louds-trie.cc:509: MARISA_MEMORY_ERROR: next_trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/louds-trie.cc:585: MARISA_MEMORY_ERROR: next_trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/tail.cc"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/tail.cc:172: MARISA_RANGE_ERROR: current.length() == 0"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/tail.cc:17: MARISA_NULL_ERROR: offsets == NULL"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/tail.cc:194: MARISA_SIZE_ERROR: buf_.size() > MARISA_UINT32_MAX"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/trie/tail.cc:40: MARISA_CODE_ERROR: undefined tail mode"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/vector/bit-vector.h"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/vector/bit-vector.h:134: MARISA_FORMAT_ERROR: temp_num_1s > size_"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/vector/bit-vector.h:58: MARISA_SIZE_ERROR: size_ == MARISA_UINT32_MAX"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/vector/flat-vector.h"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/vector/flat-vector.h:132: MARISA_FORMAT_ERROR: temp_value_size > 32"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/vector/vector.h"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/vector/vector.h:114: MARISA_STATE_ERROR: fixed_"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/vector/vector.h:122: MARISA_STATE_ERROR: fixed_"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/grimoire/vector/vector.h:210: MARISA_FORMAT_ERROR: (total_size % sizeof(T)) != 0"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc:100: MARISA_STATE_ERROR: trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc:109: MARISA_STATE_ERROR: trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc:115: MARISA_STATE_ERROR: trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc:121: MARISA_STATE_ERROR: trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc:127: MARISA_STATE_ERROR: trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc:134: MARISA_STATE_ERROR: trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc:140: MARISA_STATE_ERROR: trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc:147: MARISA_STATE_ERROR: trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc:153: MARISA_STATE_ERROR: trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc:195: MARISA_STATE_ERROR: trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc:20: MARISA_MEMORY_ERROR: temp.get() == NULL"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc:41: MARISA_NULL_ERROR: (ptr == NULL) && (size != 0)"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/third_party/marisa/lib/marisa/trie.cc:44: MARISA_MEMORY_ERROR: temp.get() == NULL"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/word_trie/UnigramTrieNode.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TrieUtils/src/word_trie/UnigramsCompiler.cpp"
- "Unknown collator failure "
- "additional-dictionary-locale"
- "baseline_byte < 0x100 || delta_byte < 0x100"
- "child_bytes"
- "dictionary-locale"
- "has_more_patricia_key_bytes()"
- "peek_next_byte"
- "stem_child_bytes"
- "suffix_byte < 0x100 || subcursor_byte < 0x100"
- "sysdic_->type() == MECAB_SYS_DIC"
- "ta"
- "use STR as the locale of the additional lexicon"
- "use STR as the locale of the lexicon"

```
