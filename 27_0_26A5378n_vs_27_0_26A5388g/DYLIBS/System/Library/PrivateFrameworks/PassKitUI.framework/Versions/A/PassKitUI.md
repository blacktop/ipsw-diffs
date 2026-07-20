## PassKitUI

> `/System/Library/PrivateFrameworks/PassKitUI.framework/Versions/A/PassKitUI`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

 387.0.0.0.0
-  __TEXT.__text: 0x1d1dc
+  __TEXT.__text: 0x1d228
   __TEXT.__objc_methlist: 0x2798
   __TEXT.__const: 0x3d0
   __TEXT.__oslogstring: 0x399

   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22e8
+  __DATA_CONST.__objc_selrefs: 0x22f8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x20
-  __DATA_CONST.__got: 0x6d0
+  __DATA_CONST.__got: 0x6d8
   __AUTH_CONST.__const: 0x760
   __AUTH_CONST.__cfstring: 0x1ac0
   __AUTH_CONST.__objc_const: 0x60a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 699
-  Symbols:   2528
+  Symbols:   2531
   CStrings:  271
 
Symbols:
+ _PKAnalyticsReportReferralSourceTopUp
+ _objc_msgSend$isTopUpRequest
+ _objc_msgSend$serviceProviderPaymentRequest
Functions:
~ ___66-[PKPaymentUIViewController prepareWithPaymentRequest:completion:]_block_invoke_2 : 5808 -> 5884
```
