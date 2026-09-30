## NanoRegistry

> `/System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry`

```diff

-1027.29.0.0.0
-  __TEXT.__text: 0x569f0
-  __TEXT.__auth_stubs: 0x940
+1027.31.0.0.0
+  __TEXT.__text: 0x56914
+  __TEXT.__auth_stubs: 0x920
   __TEXT.__objc_methlist: 0x499c
   __TEXT.__const: 0xd4
-  __TEXT.__cstring: 0x4374
+  __TEXT.__cstring: 0x40a7
   __TEXT.__gcc_except_tab: 0xddc
-  __TEXT.__oslogstring: 0x1fef
+  __TEXT.__oslogstring: 0x1fee
   __TEXT.__ustring: 0xc
   __TEXT.__unwind_info: 0x1a10
   __TEXT.__objc_classname: 0x8e3

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0xc0
-  __AUTH_CONST.__auth_got: 0x4b8
+  __AUTH_CONST.__auth_got: 0x4a8
   __AUTH_CONST.__const: 0xb20
-  __AUTH_CONST.__cfstring: 0x4a80
+  __AUTH_CONST.__cfstring: 0x4a40
   __AUTH_CONST.__objc_const: 0x6d58
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BA72D308-9D08-3C3A-AE7F-69D3F26693D8
+  UUID: BF981673-5241-33AA-935E-E0FD70F6CC0F
   Functions: 2066
-  Symbols:   6473
-  CStrings:  3007
+  Symbols:   6471
+  CStrings:  2999
 
Symbols:
+ __ZNSt12length_errorC1B9nqe210106EPKc
+ __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB9nqe210106EPKc
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB9nqe210106Ev
+ __ZSt28__throw_bad_array_new_lengthB9nqe210106v
+ ___53-[NRPairedDeviceRegistry initWithBoost:disconnected:]_block_invoke.341
+ ___block_literal_global.318
+ ___block_literal_global.353
+ ___block_literal_global.355
+ ___block_literal_global.357
+ ___block_literal_global.359
+ ___block_literal_global.373
+ ___block_literal_global.377
+ ___block_literal_global.423
+ ___block_literal_global.425
+ ___block_literal_global.428
+ ___block_literal_global.432
+ ___block_literal_global.435
+ ___block_literal_global.437
+ ___block_literal_global.620
+ ___block_literal_global.642
+ ___block_literal_global.644
+ ___block_literal_global.648
+ ___block_literal_global.699
- __ZNSt12length_errorC1B9foe210106EPKc
- __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB9foe210106EPKc
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB9foe210106Ev
- __ZSt28__throw_bad_array_new_lengthB9foe210106v
- ___53-[NRPairedDeviceRegistry initWithBoost:disconnected:]_block_invoke.349
- ___block_literal_global.326
- ___block_literal_global.365
- ___block_literal_global.369
- ___block_literal_global.409
- ___block_literal_global.415
- ___block_literal_global.427
- ___block_literal_global.429
- ___block_literal_global.431
- ___block_literal_global.433
- ___block_literal_global.436
- ___block_literal_global.443
- ___block_literal_global.445
- ___block_literal_global.448
- ___block_literal_global.628
- ___block_literal_global.650
- ___block_literal_global.652
- ___block_literal_global.656
- ___block_literal_global.707
- __os_feature_enabled_impl
CStrings:
+ "Revlock is set to shipping behavior"
- "/AppleInternal/Library/BuildRoots/4~CI63ugBLxEzEGsOjsDiscsDvg8OTJEuUvcDbo1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CI63ugBLxEzEGsOjsDiscsDvg8OTJEuUvcDbo1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "NanoRegistry"
- "Revlock feature flag is currently %@"
- "disabled"
- "enabled"
- "revlock_shipping_behavior"

```
