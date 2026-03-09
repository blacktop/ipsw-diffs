## SharedWebCredentials

> `/System/Library/PrivateFrameworks/SharedWebCredentials.framework/SharedWebCredentials`

```diff

 1021.2.0.0.0
-  __TEXT.__text: 0x15660
-  __TEXT.__auth_stubs: 0x7b0
+  __TEXT.__text: 0x15508
+  __TEXT.__auth_stubs: 0x7a0
   __TEXT.__objc_methlist: 0xf8c
   __TEXT.__const: 0xb8
-  __TEXT.__gcc_except_tab: 0x2550
-  __TEXT.__cstring: 0x17f3
+  __TEXT.__gcc_except_tab: 0x2548
+  __TEXT.__cstring: 0x1521
   __TEXT.__oslogstring: 0x7e9
   __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0xa08

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x3e8
+  __AUTH_CONST.__auth_got: 0x3e0
   __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__cfstring: 0x15a0
   __AUTH_CONST.__objc_const: 0x1548

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 28DBD716-039B-3F14-81C3-3D765F17415E
-  Functions: 398
-  Symbols:   1614
-  CStrings:  1021
+  UUID: 300BE0CC-43D6-3F46-B9E5-1F3EFD9AFA22
+  Functions: 397
+  Symbols:   1611
+  CStrings:  1019
 
Symbols:
+ GCC_except_table58
+ GCC_except_table63
+ GCC_except_table65
+ GCC_except_table71
+ GCC_except_table77
+ __ZNKSt3__117basic_string_viewIcNS_11char_traitsIcEEE4findB9nqn210106EPKcm
+ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB9nqn210106EPKvm
+ __ZNSt3__16vectorIcNS_9allocatorIcEEE20__throw_length_errorB9nqn210106Ev
+ __ZSt28__throw_bad_array_new_lengthB9nqn210106v
+ ___block_literal_global.273
- GCC_except_table60
- GCC_except_table64
- GCC_except_table66
- GCC_except_table73
- GCC_except_table78
- __ZN17SWCPatternStorage11_NextStringEPPKc
- __ZNKSt3__117basic_string_viewIcNS_11char_traitsIcEEE4findB9fon210106EPKcm
- __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB9fon210106EPKvm
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNSt3__16vectorIcNS_9allocatorIcEEE20__throw_length_errorB9fon210106Ev
- __ZSt28__throw_bad_array_new_lengthB9fon210106v
- ___block_literal_global.275
Functions:
~ -[_SWCPattern requiredEntitlement] : 244 -> 236
~ __ZNK17SWCPatternStorage8evaluateEP15NSURLComponentsPK10SWCFNMatchPK13audit_token_t : 1880 -> 1876
~ -[_SWCPattern hash] : 104 -> 80
~ -[_SWCPatternList hash] : 156 -> 116
~ ___68+[_SWCSubstitutionVariableList cheapBuiltInSubstitutionVariableList]_block_invoke : 648 -> 624
~ -[_SWCSubstitutionVariableList hash] : 136 -> 104
~ __ZNK23SWCSubstitutionVariable15getValuesNoCopyEv : 368 -> 332
~ +[_SWCPattern(Private) _debug:descriptionOfStorage:forObject:redacted:] : 1260 -> 1264
- __ZN17SWCPatternStorage11_NextStringEPPKc
~ __ZNK10SWCFNMatch8_executeERKNSt3__117basic_string_viewIcNS0_11char_traitsIcEEEES6_i : 2136 -> 2080
~ __ZZNK10SWCFNMatch20_tryMatchingVariableEPK23SWCSubstitutionVariableRKNSt3__117basic_string_viewIcNS3_11char_traitsIcEEEES9_iENK3$_0clES9_Pb : 968 -> 940
CStrings:
+ "void SWCWithFastBuffer(NSUInteger, const FunctionType &) [ElementType = char, ArraySize = 128UL, FunctionType = (lambda at /Library/Caches/com.apple.xbs/BDA777E7-5B85-46A3-9C98-183407764F70/TemporaryDirectory.FweIkT/Sources/EmbeddedSharedWebCredentials/Sources/SWCPattern.mm:2001:65)]"
- "/AppleInternal/Library/BuildRoots/4~CJlSugBy9c3pEocOD9yCdUZRFcdVtPrTeBhBWdo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
- "/AppleInternal/Library/BuildRoots/4~CJlSugBy9c3pEocOD9yCdUZRFcdVtPrTeBhBWdo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:412: libc++ Hardening assertion __pos < size() failed: string_view[] index out of bounds\n"
- "void SWCWithFastBuffer(NSUInteger, const FunctionType &) [ElementType = char, ArraySize = 128UL, FunctionType = (lambda at /Library/Caches/com.apple.xbs/6FA5B00B-F3C0-4A94-B19C-8A3E7D8EFBAB/TemporaryDirectory.2uqhKF/Sources/EmbeddedSharedWebCredentials/Sources/SWCPattern.mm:2001:65)]"

```
