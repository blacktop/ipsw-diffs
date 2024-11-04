## storekitd

> `/System/Library/Frameworks/StoreKit.framework/Support/storekitd`

```diff

-814.2.7.0.0
-  __TEXT.__text: 0x2c3fcc
-  __TEXT.__auth_stubs: 0x3410
-  __TEXT.__objc_stubs: 0xcd00
-  __TEXT.__objc_methlist: 0x6d74
-  __TEXT.__const: 0x1e000
-  __TEXT.__cstring: 0xfc15
-  __TEXT.__oslogstring: 0xc95a
+814.2.15.0.0
+  __TEXT.__text: 0x2c6154
+  __TEXT.__auth_stubs: 0x3470
+  __TEXT.__objc_stubs: 0xcd60
+  __TEXT.__objc_methlist: 0x6dac
+  __TEXT.__const: 0x1e020
+  __TEXT.__cstring: 0xfde5
+  __TEXT.__oslogstring: 0xc99a
   __TEXT.__objc_classname: 0x10b0
-  __TEXT.__objc_methname: 0x12495
+  __TEXT.__objc_methname: 0x1256e
   __TEXT.__objc_methtype: 0x3488
   __TEXT.__gcc_except_tab: 0x23d8
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x26e4
   __TEXT.__swift5_typeref: 0x29d9
-  __TEXT.__swift5_reflstr: 0x17c1
-  __TEXT.__swift5_fieldmd: 0x26d4
+  __TEXT.__swift5_reflstr: 0x17d1
+  __TEXT.__swift5_fieldmd: 0x26e0
   __TEXT.__swift5_builtin: 0x1a4
   __TEXT.__swift5_assocty: 0x4e0
   __TEXT.__swift5_proto: 0x7f0
   __TEXT.__swift5_types: 0x330
-  __TEXT.__swift5_capture: 0xff8
+  __TEXT.__swift5_capture: 0x1010
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_protos: 0x1c
-  __TEXT.__unwind_info: 0x70c8
-  __TEXT.__eh_frame: 0xbd08
-  __DATA_CONST.__auth_got: 0x1a18
-  __DATA_CONST.__got: 0xc28
-  __DATA_CONST.__auth_ptr: 0xa50
-  __DATA_CONST.__const: 0x15530
-  __DATA_CONST.__cfstring: 0x66a0
+  __TEXT.__unwind_info: 0x7108
+  __TEXT.__eh_frame: 0xbd88
+  __DATA_CONST.__auth_got: 0x1a48
+  __DATA_CONST.__got: 0xc50
+  __DATA_CONST.__auth_ptr: 0xa78
+  __DATA_CONST.__const: 0x15550
+  __DATA_CONST.__cfstring: 0x66e0
   __DATA_CONST.__objc_classlist: 0x558
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x2d0

   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_intobj: 0x210
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x1b768
-  __DATA.__objc_selrefs: 0x4720
-  __DATA.__objc_ivar: 0x6e4
+  __DATA.__objc_const: 0x1b848
+  __DATA.__objc_selrefs: 0x4748
+  __DATA.__objc_ivar: 0x6ec
   __DATA.__objc_data: 0x4628
-  __DATA.__data: 0x66c8
+  __DATA.__data: 0x66e8
   __DATA.__bss: 0x10a28
   __DATA.__common: 0xdc0
   - /System/Library/Frameworks/Accounts.framework/Accounts
+  - /System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10053
-  Symbols:   1434
-  CStrings:  6434
+  Functions: 10081
+  Symbols:   1445
+  CStrings:  6457
 
Symbols:
+ _$s16AdAttributionKit14PurchaseIntakeO012processInAppD0_9appItemIDyAC0ghD0V_s6UInt64VtYaKFZ
+ _$s16AdAttributionKit14PurchaseIntakeO012processInAppD0_9appItemIDyAC0ghD0V_s6UInt64VtYaKFZTu
+ _$s16AdAttributionKit14PurchaseIntakeO05InAppD0V0fgD4TypeO10consumableyA2GmFWC
+ _$s16AdAttributionKit14PurchaseIntakeO05InAppD0V0fgD4TypeO13nonConsumableyA2GmFWC
+ _$s16AdAttributionKit14PurchaseIntakeO05InAppD0V0fgD4TypeO23nonRenewingSubscriptionyA2GmFWC
+ _$s16AdAttributionKit14PurchaseIntakeO05InAppD0V0fgD4TypeO25autoRenewableSubscriptionyA2GmFWC
+ _$s16AdAttributionKit14PurchaseIntakeO05InAppD0V0fgD4TypeOMa
+ _$s16AdAttributionKit14PurchaseIntakeO05InAppD0V13amountCharged12currencyCode10storefront12purchaseDate0M4Type20subscriptionDurationAESo9NSDecimala_S2S10Foundation0N0VAE0fgdO0OSSSgtcfC
+ _$s16AdAttributionKit14PurchaseIntakeO05InAppD0VMa
+ _$sSo9NSDecimala10FoundationEyABSdcfC
+ _NSDecimalRound
CStrings:
+ "\x11#\x1f\a"
+ "13:04:28"
+ "Error processing purchase intake: "
+ "Free Subscription"
+ "Invalid product type for purchase intake"
+ "Invalid store item ID for purchase intake"
+ "Invalid value for purchase intake"
+ "Missing link out type from request to present the sheet for "
+ "Missing product type for purchase intake"
+ "Missing storefront for purchase intake"
+ "Missing token type in request for "
+ "Oct 26 2024"
+ "Processing ad attribution purchase intake"
+ "Skpping ad attribution purchase intake for non-production environment"
+ "Subscription Bundle"
+ "T@\"NSString\",&,N,V_productKind"
+ "T@\"NSString\",&,N,V_subscriptionPeriod"
+ "[%!{(MISSING)public}@[%!{(MISSING)public}@] No response metrics for purchase intake"
+ "_productKind"
+ "_subscriptionPeriod"
+ "externalPurchasesSheetURL"
+ "presentingWindow"
+ "productKind"
+ "purchaseIntakeWithMetrics:"
+ "setProductKind:"
+ "setSubscriptionPeriod:"
+ "sub-period"
+ "subscriptionPeriod"
- "\x11#\x1f\x05"
- "16:28:41"
- "Missing link out type value from request to present the sheet for mode "
- "Missing token type in request to generete the token for mode "
- "Oct 16 2024"
- "externalPurchaseSheetURL"

```
