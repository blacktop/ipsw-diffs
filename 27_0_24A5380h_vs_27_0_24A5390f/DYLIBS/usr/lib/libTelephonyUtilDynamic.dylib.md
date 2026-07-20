## libTelephonyUtilDynamic.dylib

> `/usr/lib/libTelephonyUtilDynamic.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-6562.0.0.0.0
-  __TEXT.__text: 0x856b8
+6565.0.0.0.0
+  __TEXT.__text: 0x857e0
   __TEXT.__init_offsets: 0x10
   __TEXT.__objc_methlist: 0x2a4
   __TEXT.__const: 0xa138
-  __TEXT.__cstring: 0x3673
-  __TEXT.__gcc_except_tab: 0x8b38
+  __TEXT.__cstring: 0x368f
+  __TEXT.__gcc_except_tab: 0x8b58
   __TEXT.__oslogstring: 0x21c6
-  __TEXT.__unwind_info: 0x44c8
+  __TEXT.__unwind_info: 0x44d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x20
-  __DATA_CONST.__objc_selrefs: 0x368
+  __DATA_CONST.__objc_selrefs: 0x370
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__got: 0x308
-  __AUTH_CONST.__const: 0x6d80
+  __AUTH_CONST.__const: 0x6da8
   __AUTH_CONST.__cfstring: 0x6e0
   __AUTH_CONST.__objc_const: 0x2e8
   __AUTH_CONST.__weak_auth_got: 0x18

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3363
-  Symbols:   5303
-  CStrings:  729
+  Functions: 3366
+  Symbols:   5309
+  CStrings:  730
 
Symbols:
+ GCC_except_table107
+ GCC_except_table114
+ GCC_except_table126
+ GCC_except_table139
+ GCC_except_table148
+ __ZN15MockHttpRequest27setCompanionProxyPreferenceEb
+ __ZN3ctu4Http16HttpSession_impl27setCompanionProxyPreferenceEb
+ __ZN3ctu4Http18HttpSessionRequest27setCompanionProxyPreferenceEb
+ _objc_msgSend$set_companionProxyPreference:
- GCC_except_table120
- GCC_except_table124
- GCC_except_table151
Functions:
+ __ZN3ctu4Http16HttpSession_impl27setCompanionProxyPreferenceEb
~ ____ZN3ctu4Http18HttpSessionRequest5startENSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE_block_invoke : 2980 -> 3020
+ __ZN3ctu4Http18HttpSessionRequest27setCompanionProxyPreferenceEb
~ __ZN15MockHttpRequestC2EN3ctu4Http11RequestTypeEONSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEONS3_3mapIS9_S9_NS1_29case_insensitive_key_comparerENS7_INS3_4pairIKS9_S9_EEEEEE : 1044 -> 1068
+ __ZN15MockHttpRequest27setCompanionProxyPreferenceEb
~ __ZN15MockHttpRequestD2Ev : 696 -> 716
CStrings:
+ "setCompanionProxyPreference"
```
