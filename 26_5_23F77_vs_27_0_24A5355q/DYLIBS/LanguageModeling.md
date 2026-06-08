## LanguageModeling

> `/System/Library/PrivateFrameworks/LanguageModeling.framework/LanguageModeling`

```diff

-433.5.0.0.0
-  __TEXT.__text: 0x1be208
-  __TEXT.__auth_stubs: 0x1de0
+445.0.0.0.0
+  __TEXT.__text: 0x17d558
   __TEXT.__objc_methlist: 0x14
-  __TEXT.__const: 0xe284
-  __TEXT.__gcc_except_tab: 0x1890c
-  __TEXT.__cstring: 0xe301
+  __TEXT.__const: 0xe580
+  __TEXT.__cstring: 0x11a7a
+  __TEXT.__gcc_except_tab: 0x14f04
   __TEXT.__dlopen_cstrs: 0x2cc
-  __TEXT.__oslogstring: 0x188f
+  __TEXT.__oslogstring: 0x18ae
   __TEXT.__ustring: 0x8ee
-  __TEXT.__unwind_info: 0x7570
-  __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x1a
-  __TEXT.__objc_methname: 0x11e
-  __TEXT.__objc_methtype: 0xb
-  __TEXT.__objc_stubs: 0x1e0
-  __DATA_CONST.__got: 0x308
-  __DATA_CONST.__const: 0x29b0
+  __TEXT.__unwind_info: 0x7a10
+  __TEXT.__eh_frame: 0x48
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x2758
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__weak_got: 0x18
   __DATA_CONST.__objc_selrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0xf00
-  __AUTH_CONST.__const: 0xa470
+  __DATA_CONST.__got: 0x2f8
+  __AUTH_CONST.__const: 0xa5f8
   __AUTH_CONST.__cfstring: 0x3060
   __AUTH_CONST.__objc_const: 0x90
+  __AUTH_CONST.__weak_auth_got: 0x50
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__data: 0x2c0
+  __AUTH_CONST.__auth_got: 0xee8
+  __AUTH.__data: 0x1a0
   __AUTH.__thread_vars: 0x30
-  __AUTH.__thread_bss: 0x9d0
-  __DATA.__data: 0x898
-  __DATA.__bss: 0x618
-  __DATA.__common: 0x30d
+  __AUTH.__thread_bss: 0x10
+  __DATA.__data: 0x970
+  __DATA.__bss: 0x688
+  __DATA.__common: 0x3c5
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0xe8
-  __DATA_DIRTY.__common: 0xb0
-  __DATA_DIRTY.__bss: 0x4e8
+  __DATA_DIRTY.__data: 0x1b8
+  __DATA_DIRTY.__bss: 0x440
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreEmoji.framework/CoreEmoji

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 7B3D3EB5-F123-35C4-86A8-9A818ACFDACD
-  Functions: 5280
-  Symbols:   1222
-  CStrings:  2552
+  UUID: 37FC19FC-C1F6-34B4-A925-8597151C0AFF
+  Functions: 5833
+  Symbols:   1229
+  CStrings:  2594
 
Symbols:
+ __ZN17language_modeling2v116kAutoFillLexiconE
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEmmPKc
+ __ZNSt13runtime_errorC2ERKS_
+ __ZNSt3__112__get_sp_mutEPKv
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE21__grow_by_and_replaceEmmmmmmPKc
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__18__sp_mut4lockEv
+ __ZNSt3__18__sp_mut6unlockEv
+ __ZTINSt3__14__fs10filesystem16filesystem_errorE
+ __tlv_atexit
+ _log1p
- __ZN17language_modeling2v120LanguageModelSession27setDynamicResourceDirectoryERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE
- __ZN17language_modeling2v120LanguageModelSession30removeDynamicResourceDirectoryEv
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_mmRKS4_
- _sprintf
CStrings:
+ " FROM "
+ "-shm"
+ "-wal"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:122: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:127: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:158: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:164: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1156: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:413: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:418: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:441: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:445: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:494: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:297: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:302: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:317: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:2199: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/list:1412: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/list:830: libc++ Hardening assertion !empty() failed: list::front called on empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1121: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1130: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1139: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/span:502: libc++ Hardening assertion __count <= size() failed: span<T>::first(count): count out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/span:508: libc++ Hardening assertion __count <= size() failed: span<T>::last(count): count out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/span:522: libc++ Hardening assertion __offset <= size() failed: span<T>::subspan(offset, count): offset out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/span:537: libc++ Hardening assertion __idx < size() failed: span<T>::operator[](index): index out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/span:550: libc++ Hardening assertion !empty() failed: span<T>::front() on empty span\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/span:555: libc++ Hardening assertion !empty() failed: span<T>::back() on empty span\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:1371: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:1497: libc++ Hardening assertion !empty() failed: string::front(): string is empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:1507: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:3384: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:3393: libc++ Hardening assertion !empty() failed: string::pop_back(): string is already empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBmYRuBCFqqARosQ86FATe-yorTn_lGjco/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string_view:343: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
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
+ "=?"
+ "AppleNeuralEngineSubtype"
+ "CoreLMSuffixCoder"
+ "DefaultRecipientID"
+ "Failed to build the TRIE for PrefixMatcher"
+ "Failed to duplicate file descriptor"
+ "LM_"
+ "Lex_"
+ "SELECT "
+ "SuffixV1"
+ "SuffixV2"
+ "Trie data size is not divisible by 1024."
+ "UniLM"
+ "_U_NT"
+ "_U_NT08"
+ "_U_PRE"
+ "autoFillLexicon"
+ "could not parse ModelProto from "
+ "could not read "
+ "directory iteration failed: %s"
+ "edge.in == fragID"
+ "en_"
+ "getIncomingEdgeIdx"
+ "node < getNrOfNodes()"
+ "normalized block must be null terminated."
+ "s"
+ "sh"
- "%s %s"
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
- "@24@0:8@16"
- "Failed to create dynamicInlineCompletion enumerator"
- "LexiconFilePathExtractor"
- "_dynamicInlineCompletions"
- "allKeys"
- "alloc"
- "bundleForClass:"
- "containsObject:"
- "countByEnumeratingWithState:objects:count:"
- "dictionaryWithContentsOfFile:"
- "eJGhnVvylF3dMOHBKJzeiw"
- "initWithKey:"
- "input->ReadAll(&serialized)"
- "intValue"
- "lexiconFilePath:"
- "norm_to_orig"
- "normalized"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "pathForResource:ofType:"
- "record:"
- "removeDynamicResourceDirectory"
- "setDynamicResourceDirectory"
- "standard output"
- "stringWithUTF8String:"
- "word:atPosition:"
- "wordFragmentWidth"

```
