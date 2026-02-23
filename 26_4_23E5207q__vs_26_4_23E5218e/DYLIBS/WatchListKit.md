## WatchListKit

> `/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit`

```diff

-907.40.26.0.0
-  __TEXT.__text: 0x6baf4
+907.40.28.0.0
+  __TEXT.__text: 0x6bc64
   __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_methlist: 0x708c
+  __TEXT.__objc_methlist: 0x709c
   __TEXT.__const: 0x1a4
   __TEXT.__cstring: 0x7c65
-  __TEXT.__oslogstring: 0x645c
-  __TEXT.__gcc_except_tab: 0x11b0
-  __TEXT.__unwind_info: 0x1fa8
+  __TEXT.__oslogstring: 0x64a2
+  __TEXT.__gcc_except_tab: 0x11c8
+  __TEXT.__unwind_info: 0x1fb8
   __TEXT.__objc_classname: 0x1321
   __TEXT.__objc_methname: 0x10870
   __TEXT.__objc_methtype: 0x1da5

   __AUTH_CONST.__auth_got: 0x3f8
   __AUTH_CONST.__const: 0xe80
   __AUTH_CONST.__cfstring: 0xa520
-  __AUTH_CONST.__objc_const: 0x11bf8
+  __AUTH_CONST.__objc_const: 0x11c18
   __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0x19f0
-  __DATA.__objc_ivar: 0xa38
+  __DATA.__objc_ivar: 0xa3c
   __DATA.__data: 0x7a0
   __DATA.__bss: 0xf8
   __DATA_DIRTY.__objc_data: 0x1bd0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 33B3E7B4-9548-385D-A075-85E234636593
-  Functions: 2764
-  Symbols:   10129
-  CStrings:  6493
+  UUID: 6EA1CBFC-E825-33C2-A1A5-2B0B33AAC250
+  Functions: 2765
+  Symbols:   10133
+  CStrings:  6494
 
Symbols:
+ -[WLKOfferManager _invalidationHandler]
+ GCC_except_table9
+ _OBJC_IVAR_$_WLKOfferManager._xpcLock
+ ___30-[WLKOfferManager _connection]_block_invoke.78
+ ___31-[WLKOfferManager clearOffers:]_block_invoke.70
+ ___31-[WLKOfferManager clearOffers:]_block_invoke.71
+ ___42-[WLKOfferManager fetchOffers:completion:]_block_invoke.60
+ ___58-[WLKOfferManager removeOfferByBadgeId:completionHandler:]_block_invoke.62
+ ___58-[WLKOfferManager removeOfferByBadgeId:completionHandler:]_block_invoke.66
+ ___58-[WLKOfferManager removeOfferByBadgeId:completionHandler:]_block_invoke.67
+ ___block_descriptor_48_e8_32bs40w_e29_v24?0"NSArray"8"NSError"16lw40l8s32l8
+ ___block_literal_global.77
- ___30-[WLKOfferManager _connection]_block_invoke.76
- ___31-[WLKOfferManager clearOffers:]_block_invoke.66
- ___31-[WLKOfferManager clearOffers:]_block_invoke.69
- ___42-[WLKOfferManager fetchOffers:completion:]_block_invoke.58
- ___58-[WLKOfferManager removeOfferByBadgeId:completionHandler:]_block_invoke.60
- ___58-[WLKOfferManager removeOfferByBadgeId:completionHandler:]_block_invoke.64
- ___58-[WLKOfferManager removeOfferByBadgeId:completionHandler:]_block_invoke.65
- ___block_descriptor_48_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls40l8s32l8
- ___block_literal_global.108
- ___block_literal_global.75
CStrings:
+ "WLKOfferManager - Connection to daemon not available to fetch offers."

```
