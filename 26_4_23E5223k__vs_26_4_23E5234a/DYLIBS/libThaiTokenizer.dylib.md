## libThaiTokenizer.dylib

> `/usr/lib/libThaiTokenizer.dylib`

```diff

 28.0.0.0.0
-  __TEXT.__text: 0x4ca0
-  __TEXT.__auth_stubs: 0x370
+  __TEXT.__text: 0x4c58
+  __TEXT.__auth_stubs: 0x360
   __TEXT.__const: 0x8e0
-  __TEXT.__cstring: 0x1bf9
-  __TEXT.__gcc_except_tab: 0x290
+  __TEXT.__cstring: 0x17e9
+  __TEXT.__gcc_except_tab: 0x288
   __TEXT.__unwind_info: 0x298
   __DATA_CONST.__got: 0x58
-  __AUTH_CONST.__auth_got: 0x1c0
+  __AUTH_CONST.__auth_got: 0x1b8
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: DF9DD050-A845-3A56-9FFA-FCB37592FAD5
+  UUID: 8214B0E1-D845-3322-9D78-0FF9FD465839
   Functions: 135
-  Symbols:   427
-  CStrings:  51
+  Symbols:   426
+  CStrings:  48
 
Symbols:
+ __ZNSt12length_errorC1B9nqe210106EPKc
+ __ZNSt3__110unique_ptrIN4trie10MarisaTrieIfcEENS_14default_deleteIS3_EEE5resetB9nqe210106EPS3_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqe210106ILi0EEEPKc
+ __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB9nqe210106EPKc
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB9nqe210106Ev
+ __ZSt28__throw_bad_array_new_lengthB9nqe210106v
- __ZNSt12length_errorC1B9foe210106EPKc
- __ZNSt3__110unique_ptrIN4trie10MarisaTrieIfcEENS_14default_deleteIS3_EEE5resetB9foe210106EPS3_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9foe210106ILi0EEEPKc
- __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB9foe210106EPKc
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB9foe210106Ev
- __ZSt28__throw_bad_array_new_lengthB9foe210106v
Functions:
~ __ZN5Utils17MarisaTrieWrapperC2EPK10__CFString : 1680 -> 1640
~ __ZNK5Utils17MarisaTrieWrapper6lookupEPK10__CFString7CFRangeRf : 412 -> 380
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJk6ugB2rYQlVnRiFRfKPaKg3DPWiUrOTCSBOgw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugB2rYQlVnRiFRfKPaKg3DPWiUrOTCSBOgw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugB2rYQlVnRiFRfKPaKg3DPWiUrOTCSBOgw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:431: libc++ Hardening assertion __n <= size() failed: remove_prefix() can't remove more than size()\n"

```
