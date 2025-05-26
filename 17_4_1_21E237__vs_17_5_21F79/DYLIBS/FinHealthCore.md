## FinHealthCore

> `/System/Library/PrivateFrameworks/FinHealthCore.framework/FinHealthCore`

```diff

-1.6.31.3.0
-  __TEXT.__text: 0x1fe90
+1.6.32.2.0
+  __TEXT.__text: 0x1fee8
   __TEXT.__auth_stubs: 0x530
   __TEXT.__objc_methlist: 0x1c70
   __TEXT.__const: 0x1d0
-  __TEXT.__cstring: 0x52e8
+  __TEXT.__cstring: 0x538a
   __TEXT.__gcc_except_tab: 0x3c8
   __TEXT.__oslogstring: 0xaea
   __TEXT.__unwind_info: 0x6e4
   __TEXT.__objc_classname: 0x3fe
   __TEXT.__objc_methname: 0x4ec4
   __TEXT.__objc_methtype: 0x648
-  __TEXT.__objc_stubs: 0x3b00
+  __TEXT.__objc_stubs: 0x3b20
   __DATA_CONST.__got: 0x18
-  __DATA_CONST.__const: 0x1040
+  __DATA_CONST.__const: 0x1048
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_classrefs: 0x1c8
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__cfstring: 0x3fa0
+  __AUTH_CONST.__cfstring: 0x3fc0
   __AUTH_CONST.__objc_const: 0xec8
   __AUTH_CONST.__const: 0x300
   __AUTH_CONST.__objc_intobj: 0x168

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   Functions: 678
-  Symbols:   2819
-  CStrings:  1597
+  Symbols:   2821
+  CStrings:  1598
 
Symbols:
+ _FHDeleteFeaturesPredictedRealTimeForIDInValueRange
+ ___81-[FHDatabaseManager computeRecurringClassesWithMerchantCounts:peerPaymentCounts:]_block_invoke.156
+ ___81-[FHDatabaseManager computeRecurringClassesWithMerchantCounts:peerPaymentCounts:]_block_invoke_2.160
+ ___block_literal_global.159
+ _objc_msgSend$setRepeatingPatternClass:
- ___81-[FHDatabaseManager computeRecurringClassesWithMerchantCounts:peerPaymentCounts:]_block_invoke.155
- ___81-[FHDatabaseManager computeRecurringClassesWithMerchantCounts:peerPaymentCounts:]_block_invoke_2.159
- ___block_literal_global.158
CStrings:
+ "delete from features_predicted_realtime where t_identifier == %@ and t_feature_name == %@ and t_feature_predicted_value >= %d and t_feature_predicted_value <= %d"

```
