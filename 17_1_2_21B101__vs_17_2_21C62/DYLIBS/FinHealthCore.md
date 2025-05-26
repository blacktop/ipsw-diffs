## FinHealthCore

> `/System/Library/PrivateFrameworks/FinHealthCore.framework/FinHealthCore`

```diff

-1.6.28.1.0
-  __TEXT.__text: 0x1fb94
+1.6.29.1.0
+  __TEXT.__text: 0x1fbec
   __TEXT.__auth_stubs: 0x530
   __TEXT.__objc_methlist: 0x1c60
   __TEXT.__const: 0x1d8
-  __TEXT.__cstring: 0x52b9
+  __TEXT.__cstring: 0x535b
   __TEXT.__gcc_except_tab: 0x380
   __TEXT.__oslogstring: 0xaa5
   __TEXT.__unwind_info: 0x6dc
   __TEXT.__objc_classname: 0x3fe
   __TEXT.__objc_methname: 0x4e94
   __TEXT.__objc_methtype: 0x648
-  __TEXT.__objc_stubs: 0x3ae0
+  __TEXT.__objc_stubs: 0x3b00
   __DATA_CONST.__got: 0x18
-  __DATA_CONST.__const: 0x1030
+  __DATA_CONST.__const: 0x1038
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_const: 0x2910
   __DATA_CONST.__objc_selrefs: 0x1250
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__cfstring: 0x3f20
+  __AUTH_CONST.__cfstring: 0x3f40
   __AUTH_CONST.__objc_const: 0xec8
   __AUTH_CONST.__const: 0x300
   __AUTH_CONST.__objc_intobj: 0x168

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   Functions: 675
-  Symbols:   2813
-  CStrings:  1588
+  Symbols:   2815
+  CStrings:  1589
 
Symbols:
+ _FHDeleteFeaturesPredictedRealTimeForIDInValueRange
+ ___81-[FHDatabaseManager computeRecurringClassesWithMerchantCounts:peerPaymentCounts:]_block_invoke.150
+ ___81-[FHDatabaseManager computeRecurringClassesWithMerchantCounts:peerPaymentCounts:]_block_invoke_2.154
+ ___block_literal_global.153
+ _objc_msgSend$setRepeatingPatternClass:
- ___81-[FHDatabaseManager computeRecurringClassesWithMerchantCounts:peerPaymentCounts:]_block_invoke.149
- ___81-[FHDatabaseManager computeRecurringClassesWithMerchantCounts:peerPaymentCounts:]_block_invoke_2.153
- ___block_literal_global.152
CStrings:
+ "delete from features_predicted_realtime where t_identifier == %@ and t_feature_name == %@ and t_feature_predicted_value >= %d and t_feature_predicted_value <= %d"

```
