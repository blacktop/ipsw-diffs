## PassKitUIFoundation

> `/System/Library/PrivateFrameworks/PassKitUIFoundation.framework/PassKitUIFoundation`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1689.3.0.0.0
-  __TEXT.__text: 0x265c4
-  __TEXT.__objc_methlist: 0x1d0c
+1695.1.2.0.0
+  __TEXT.__text: 0x266f4
+  __TEXT.__objc_methlist: 0x1d1c
   __TEXT.__const: 0x680
   __TEXT.__cstring: 0xe9a
   __TEXT.__oslogstring: 0x138d
   __TEXT.__gcc_except_tab: 0x794
-  __TEXT.__unwind_info: 0xa08
+  __TEXT.__unwind_info: 0xa18
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bf0
+  __DATA_CONST.__objc_selrefs: 0x1c10
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0xa8
-  __DATA_CONST.__got: 0x5c8
+  __DATA_CONST.__got: 0x5e0
   __AUTH_CONST.__const: 0x160
   __AUTH_CONST.__cfstring: 0x1000
-  __AUTH_CONST.__objc_const: 0x4690
+  __AUTH_CONST.__objc_const: 0x46a0
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 825
-  Symbols:   2662
+  Functions: 827
+  Symbols:   2671
   CStrings:  254
 
Symbols:
+ -[PKAuthenticatorEvaluationContext successfulAuthenticationMethod]
+ GCC_except_table163
+ GCC_except_table171
+ GCC_except_table175
+ GCC_except_table183
+ GCC_except_table185
+ _PKAnalyticsReportEventTypeSuccessfulFaceID
+ _PKAnalyticsReportEventTypeSuccessfulPasscode
+ _PKAnalyticsReportEventTypeSuccessfulTouchID
+ _PKMapsDisplayNameForMerchant
+ _objc_msgSend$displayName
+ _objc_msgSend$name
+ _objc_msgSend$setSuccessfulAuthenticationMethod:
+ _objc_msgSend$successfulAuthenticationMethod
- GCC_except_table162
- GCC_except_table170
- GCC_except_table174
- GCC_except_table182
- GCC_except_table184
Functions:
+ _PKMapsDisplayNameForMerchant
+ -[PKAuthenticatorEvaluationContext successfulAuthenticationMethod]
~ ___46-[PKAuthenticator _evaluateEvaluationContext:]_block_invoke : 700 -> 732
```
