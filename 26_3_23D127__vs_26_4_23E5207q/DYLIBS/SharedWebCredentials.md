## SharedWebCredentials

> `/System/Library/PrivateFrameworks/SharedWebCredentials.framework/SharedWebCredentials`

```diff

 1021.2.0.0.0
-  __TEXT.__text: 0x14d5c
-  __TEXT.__auth_stubs: 0x7d0
+  __TEXT.__text: 0x15660
+  __TEXT.__auth_stubs: 0x7b0
   __TEXT.__objc_methlist: 0xf8c
   __TEXT.__const: 0xb8
-  __TEXT.__gcc_except_tab: 0x2574
-  __TEXT.__cstring: 0x14e2
+  __TEXT.__gcc_except_tab: 0x2550
+  __TEXT.__cstring: 0x17f3
   __TEXT.__oslogstring: 0x7e9
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0xa18
+  __TEXT.__unwind_info: 0xa08
   __TEXT.__objc_classname: 0x214
   __TEXT.__objc_methname: 0x2b23
   __TEXT.__objc_methtype: 0xb39

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x3f8
+  __AUTH_CONST.__auth_got: 0x3e8
   __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__cfstring: 0x15a0
   __AUTH_CONST.__objc_const: 0x1548

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 165C327E-4C70-3C74-8E7B-836A9D615D46
-  Functions: 397
+  UUID: 13FC388B-6722-3E6E-92FD-DC56906EC83E
+  Functions: 398
   Symbols:   1614
-  CStrings:  1019
+  CStrings:  1021
 
Symbols:
+ GCC_except_table60
+ GCC_except_table64
+ GCC_except_table66
+ GCC_except_table73
+ GCC_except_table78
+ __ZN17SWCPatternStorage11_NextStringEPPKc
+ __ZNKSt3__117basic_string_viewIcNS_11char_traitsIcEEE4findB9fon210106EPKcm
+ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB9fon210106EPKvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_17basic_string_viewIcNS_11char_traitsIcEEEEPK23SWCSubstitutionVariableEENS_22__unordered_map_hasherIS5_NS_4pairIKS5_S8_EENS_4hashIS5_EENS_8equal_toIS5_EELb1EEENS_21__unordered_map_equalIS5_SD_SH_SF_Lb1EEENS_9allocatorISD_EEED2Ev
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__16vectorIcNS_9allocatorIcEEE20__throw_length_errorB9fon210106Ev
+ __ZSt28__throw_bad_array_new_lengthB9fon210106v
+ ___block_literal_global.275
+ _objc_retainAutoreleasedReturnValue
- GCC_except_table58
- GCC_except_table63
- GCC_except_table65
- GCC_except_table71
- GCC_except_table77
- __ZNKSt3__117basic_string_viewIcNS_11char_traitsIcEEE4findB8nn200100EPKcm
- __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8nn200100EPKvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_17basic_string_viewIcNS_11char_traitsIcEEEEPK23SWCSubstitutionVariableEENS_22__unordered_map_hasherIS5_S9_NS_4hashIS5_EENS_8equal_toIS5_EELb1EEENS_21__unordered_map_equalIS5_S9_SE_SC_Lb1EEENS_9allocatorIS9_EEED2Ev
- __ZNSt3__16vectorIcNS_9allocatorIcEEE20__throw_length_errorB8nn200100Ev
- __ZSt28__throw_bad_array_new_lengthB8nn200100v
- ___block_literal_global.273
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x9
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHodugDWKNy3QfVkm72YZGluDeyEsJahzVJZyJQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
+ "/AppleInternal/Library/BuildRoots/4~CHodugDWKNy3QfVkm72YZGluDeyEsJahzVJZyJQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:412: libc++ Hardening assertion __pos < size() failed: string_view[] index out of bounds\n"
+ "void SWCWithFastBuffer(NSUInteger, const FunctionType &) [ElementType = char, ArraySize = 128UL, FunctionType = (lambda at /Library/Caches/com.apple.xbs/AACFCAD3-1867-4ADF-8E09-FE6303B657A2/TemporaryDirectory.L6ZFfW/Sources/EmbeddedSharedWebCredentials/Sources/SWCPattern.mm:2001:65)]"
- "void SWCWithFastBuffer(NSUInteger, const FunctionType &) [ElementType = char, ArraySize = 128UL, FunctionType = (lambda at /Library/Caches/com.apple.xbs/Sources/EmbeddedSharedWebCredentials/Sources/SWCPattern.mm:2001:65)]"

```
