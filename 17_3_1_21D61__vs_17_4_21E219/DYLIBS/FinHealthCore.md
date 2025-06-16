## FinHealthCore

> `/System/Library/PrivateFrameworks/FinHealthCore.framework/FinHealthCore`

```diff

-1.6.29.1.0
-  __TEXT.__text: 0x1fbec
+1.6.31.3.0
+  __TEXT.__text: 0x1fe90
   __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_methlist: 0x1c60
-  __TEXT.__const: 0x1d8
-  __TEXT.__cstring: 0x535b
-  __TEXT.__gcc_except_tab: 0x380
-  __TEXT.__oslogstring: 0xaa5
-  __TEXT.__unwind_info: 0x6dc
+  __TEXT.__objc_methlist: 0x1c70
+  __TEXT.__const: 0x1d0
+  __TEXT.__cstring: 0x52e8
+  __TEXT.__gcc_except_tab: 0x3c8
+  __TEXT.__oslogstring: 0xaea
+  __TEXT.__unwind_info: 0x6e4
   __TEXT.__objc_classname: 0x3fe
-  __TEXT.__objc_methname: 0x4e94
+  __TEXT.__objc_methname: 0x4ec4
   __TEXT.__objc_methtype: 0x648
   __TEXT.__objc_stubs: 0x3b00
   __DATA_CONST.__got: 0x18
-  __DATA_CONST.__const: 0x1038
+  __DATA_CONST.__const: 0x1040
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x2910
-  __DATA_CONST.__objc_selrefs: 0x1250
+  __DATA_CONST.__objc_selrefs: 0x1258
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x1c8
+  __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__cfstring: 0x3f40
+  __AUTH_CONST.__cfstring: 0x3fa0
   __AUTH_CONST.__objc_const: 0xec8
   __AUTH_CONST.__const: 0x300
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x2a8
   __AUTH.__objc_data: 0x320
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x1c8
-  __DATA.__objc_superrefs: 0xd8
   __DATA.__objc_ivar: 0x238
   __DATA.__data: 0x1a0
-  __DATA.__bss: 0x90
+  __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0x5f0
-  __DATA_DIRTY.__bss: 0xd0
+  __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 5A3085D0-43E9-3173-B25E-98A4BE5BCE85
-  Functions: 675
-  Symbols:   2815
-  CStrings:  2095
+  UUID: 1C5E9EF2-4E5E-3684-AF0E-DFA70842097F
+  Functions: 678
+  Symbols:   2819
+  CStrings:  2106
 
Symbols:
+ -[NSMutableDictionary(FHDictionarySafeMethods) setOrAddToDecimalValue:forKey:]
+ -[NSMutableDictionary(FHDictionarySafeMethods) setOrAddToDoubleValue:forKey:]
+ _FHDataDirectory
+ _FHInsightsMerchantCountThreshold
+ _FHMerchantCategoryFromString
+ ___41-[FHDatabaseManager publishEventsToBiome]_block_invoke.220
+ ___48-[FHDatabaseManager init:multiThreadingEnabled:]_block_invoke.61
+ ___67-[FHDatabaseManager _computeAllAggregateFeaturesWithTransactionId:]_block_invoke.121
+ ___81-[FHDatabaseManager computeRecurringClassesWithMerchantCounts:peerPaymentCounts:]_block_invoke.155
+ ___81-[FHDatabaseManager computeRecurringClassesWithMerchantCounts:peerPaymentCounts:]_block_invoke_2.159
+ ___block_literal_global.158
+ ___block_literal_global.235
+ _objc_msgSend$setOrAddToDoubleValue:forKey:
- +[FHTransaction FHMerchantCategoryFromString:]
- _FHDeleteFeaturesPredictedRealTimeForIDInValueRange
- ___41-[FHDatabaseManager publishEventsToBiome]_block_invoke.213
- ___48-[FHDatabaseManager init:multiThreadingEnabled:]_block_invoke.55
- ___67-[FHDatabaseManager _computeAllAggregateFeaturesWithTransactionId:]_block_invoke.115
- ___81-[FHDatabaseManager computeRecurringClassesWithMerchantCounts:peerPaymentCounts:]_block_invoke.150
- ___81-[FHDatabaseManager computeRecurringClassesWithMerchantCounts:peerPaymentCounts:]_block_invoke_2.154
- ___block_literal_global.153
- ___block_literal_global.228
- _objc_msgSend$setRepeatingPatternClass:
CStrings:
+ "(sch_id integer primary key autoincrement, sch_version_id text, sch_upgrade_status integer, sch_date integer, sch_getall_status integer)"
+ "(trend_pid integer primary key autoincrement, trend_date real, trend_direction integer, trend_feature_name text, trend_feature_type text, trend_spend real, trend_window integer, trend_average real, trend_readable_description text)"
+ "0.0"
+ "9.1"
+ "After Journal mode: %@"
+ "Before Journal mode: %@"
+ "PRAGMA journal_mode"
+ "PRAGMA journal_mode=WAL"
+ "T@\"NSString\",?,R,C"
+ "insert into fh_schema (sch_version_id, sch_upgrade_status, sch_date, sch_getall_status) values (%@, %d, %d, %d)"
+ "select sch_getall_status from fh_schema where sch_version_id == %@;"
+ "setOrAddToDecimalValue:forKey:"
+ "setOrAddToDoubleValue:forKey:"
+ "sqlExecuteCommand: %@"
+ "update fh_schema set sch_getall_status = %d where sch_version_id == %@"
- "(sch_id integer primary key autoincrement, sch_version_id integer, sch_upgrade_status integer, sch_date integer, sch_getall_status integer)"
- "(trend_pid integer primary key autoincrement, trend_type integer, trend_date real, trend_direction integer, trend_merchant_category integer, trend_spend real, trend_window integer, trend_window_reference integer, trend_average real)"
- "FHMerchantCategoryFromString:"
- "delete from features_predicted_realtime where t_identifier == %@ and t_feature_name == %@ and t_feature_predicted_value >= %d and t_feature_predicted_value <= %d"
- "insert into fh_schema (sch_version_id, sch_upgrade_status, sch_date, sch_getall_status) values (%d, %d, %d, %d)"
- "select sch_getall_status from fh_schema where sch_version_id == %d;"
- "update fh_schema set sch_getall_status = %d where sch_version_id == %d"

```
