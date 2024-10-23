## FinHealthCore

> `/System/Library/PrivateFrameworks/FinHealthCore.framework/FinHealthCore`

```diff

-1.7.2.2.0
-  __TEXT.__text: 0x2bb14
+1.7.3.3.0
+  __TEXT.__text: 0x2c28c
   __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_methlist: 0x28a4
+  __TEXT.__objc_methlist: 0x28cc
   __TEXT.__const: 0x318
-  __TEXT.__cstring: 0x6e90
-  __TEXT.__gcc_except_tab: 0x860
+  __TEXT.__cstring: 0x712b
+  __TEXT.__gcc_except_tab: 0x884
   __TEXT.__oslogstring: 0x107c
-  __TEXT.__unwind_info: 0x968
+  __TEXT.__unwind_info: 0x978
   __TEXT.__objc_classname: 0x593
-  __TEXT.__objc_methname: 0x6eb8
-  __TEXT.__objc_methtype: 0x7ad
-  __TEXT.__objc_stubs: 0x4fc0
+  __TEXT.__objc_methname: 0x6fa3
+  __TEXT.__objc_methtype: 0x7e4
+  __TEXT.__objc_stubs: 0x5040
   __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0x13f8
+  __DATA_CONST.__const: 0x1450
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19a8
+  __DATA_CONST.__objc_selrefs: 0x19c0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x140
-  __DATA_CONST.__objc_arraydata: 0x18
+  __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x308
   __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0x51a0
-  __AUTH_CONST.__objc_const: 0x5468
+  __AUTH_CONST.__cfstring: 0x5300
+  __AUTH_CONST.__objc_const: 0x5498
   __AUTH_CONST.__objc_intobj: 0x168
-  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0x348
+  __DATA.__objc_ivar: 0x34c
   __DATA.__data: 0x260
   __DATA.__bss: 0x90
   __DATA_DIRTY.__objc_data: 0x820

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 952
-  Symbols:   1625
-  CStrings:  2170
+  Functions: 959
+  Symbols:   1638
+  CStrings:  2188
 
Symbols:
+ _FHComparisonOperatorLike
+ _FHGetReceiptData
+ _FHInsertNewReceiptData
+ _FHReceiptDataTableCreateSchema
+ _FHReceiptDataTableName
+ _FHTransactionAssociatedReceiptUniqueIDKey
CStrings:
+ "%!@(MISSING)%!@(MISSING)"
+ "(fhr_id integer primary key autoincrement, receiptIdentifier text, line_item_index text, title text, subtitle text, quantity integer, amount integer, currencyCode text, adamIdentifier integer, UNIQUE(receiptIdentifier, line_item_index))"
+ "(t_tid integer primary key autoincrement, t_identifier text, t_service_identifier text, t_finance_transaction_id text, t_payment_hash text, t_source_identifier text, t_amount integer, t_currencycode text, t_timezone integer, t_date integer, t_status integer, t_status_changed_date integer, t_source integer, t_card_type integer, t_type integer, a_type integer, t_altDSID text, t_receipt_identifier text, t_associated_receipt_unique_id text, t_fh_internal_state integer, m_merchant_identifier text, m_industrycode integer, m_name text, m_raw_name text, m_category integer, m_detailed_category text, m_displayname text, m_street text, m_city text, m_state text, m_zip text, m_country_code text, m_country text, m_maps_merchant_id text, m_maps_merchant_result_id integer, m_maps_merchant_brand_id text, m_maps_merchant_brand_result_id integer, lat real, long real, v_accuracy real, h_accuracy real, dispute_type integer, dispute_status integer, peer_pay_counterpart text, peer_pay_type integer, t_description text, peer_pay_is_recurring integer, dispute_open_date integer, dispute_last_updated_date integer)"
+ ")U\"\x19\x11#\x11\x11"
+ "10.72"
+ "@56@0:8@16@24q32q40@48"
+ "B80@0:8@16@24@32@40Q48@56@64Q72"
+ "LIKE"
+ "T@\"NSString\",C,N,V_associatedReceiptUniqueID"
+ "_associatedReceiptUniqueID"
+ "associatedReceiptUniqueID"
+ "fh_receipt_data"
+ "fh_receipt_data.amount"
+ "fh_receipt_data.receiptIdentifier"
+ "fh_receipt_data.subtitle"
+ "fh_receipt_data.title"
+ "histogramKeysForCardPurchaseTransaction:transactionAmount:transactionType:amountFromDatabase:receiptIdentifier:"
+ "insert into fh_receipt_data(receiptIdentifier, line_item_index, title, subtitle, quantity, amount, currencyCode, adamIdentifier) values (%!@(MISSING), %!@(MISSING), %!@(MISSING), %!@(MISSING), %!d(MISSING), %!d(MISSING), %!@(MISSING), %!d(MISSING))"
+ "insertReceiptData:identifier:title:subtitle:quantity:amount:currencyCode:adamIdentifier:"
+ "select * from fh_receipts_data"
+ "setAssociatedReceiptUniqueID:"
+ "update transactions set t_service_identifier = %!@(MISSING), t_finance_transaction_id = %!@(MISSING), t_payment_hash = %!@(MISSING), t_source_identifier = %!@(MISSING), t_amount = %!d(MISSING), t_currencycode = %!@(MISSING), t_timezone = %!@(MISSING), t_date = %!d(MISSING), t_status = %!d(MISSING), t_status_changed_date = %!d(MISSING), t_source = %!d(MISSING), t_card_type = %!d(MISSING), t_type = %!d(MISSING), a_type = %!d(MISSING), t_altDSID = %!@(MISSING), t_receipt_identifier = %!@(MISSING), t_associated_receipt_unique_id = %!@(MISSING), t_fh_internal_state = %!d(MISSING), m_merchant_identifier = %!@(MISSING), m_industrycode = %!d(MISSING), m_name = %!@(MISSING), m_raw_name = %!@(MISSING), m_category = %!d(MISSING), m_detailed_category = %!@(MISSING), m_displayname = %!@(MISSING), m_street = %!@(MISSING), m_city = %!@(MISSING), m_state = %!@(MISSING), m_zip = %!@(MISSING), m_country_code = %!@(MISSING), m_country = %!@(MISSING), m_maps_merchant_id = %!@(MISSING), m_maps_merchant_result_id = %!d(MISSING), m_maps_merchant_brand_id = %!@(MISSING), m_maps_merchant_brand_result_id = %!d(MISSING), lat = %!f(MISSING), long = %!f(MISSING), v_accuracy = %!f(MISSING), h_accuracy = %!f(MISSING), dispute_type = %!d(MISSING), dispute_status = %!d(MISSING), peer_pay_counterpart = %!@(MISSING), peer_pay_type = %!d(MISSING), t_description = %!@(MISSING), peer_pay_is_recurring = %!d(MISSING), dispute_open_date = %!d(MISSING), dispute_last_updated_date = %!d(MISSING) where t_identifier == %!@(MISSING)"
- "(t_tid integer primary key autoincrement, t_identifier text, t_service_identifier text, t_finance_transaction_id text, t_payment_hash text, t_source_identifier text, t_amount integer, t_currencycode text, t_timezone integer, t_date integer, t_status integer, t_status_changed_date integer, t_source integer, t_card_type integer, t_type integer, a_type integer, t_altDSID text, t_receipt_identifier text, t_fh_internal_state integer, m_merchant_identifier text, m_industrycode integer, m_name text, m_raw_name text, m_category integer, m_detailed_category text, m_displayname text, m_street text, m_city text, m_state text, m_zip text, m_country_code text, m_country text, m_maps_merchant_id text, m_maps_merchant_result_id integer, m_maps_merchant_brand_id text, m_maps_merchant_brand_result_id integer, lat real, long real, v_accuracy real, h_accuracy real, dispute_type integer, dispute_status integer, peer_pay_counterpart text, peer_pay_type integer, t_description text, peer_pay_is_recurring integer, dispute_open_date integer, dispute_last_updated_date integer)"
- ")T\"\x19\x11#\x11\x11"
- "10.71"
- "histogramKeysForCardPurchaseTransaction:transactionAmount:transactionType:amountFromDatabase:"
- "update transactions set t_service_identifier = %!@(MISSING), t_finance_transaction_id = %!@(MISSING), t_payment_hash = %!@(MISSING), t_source_identifier = %!@(MISSING), t_amount = %!d(MISSING), t_currencycode = %!@(MISSING), t_timezone = %!@(MISSING), t_date = %!d(MISSING), t_status = %!d(MISSING), t_status_changed_date = %!d(MISSING), t_source = %!d(MISSING), t_card_type = %!d(MISSING), t_type = %!d(MISSING), a_type = %!d(MISSING), t_altDSID = %!@(MISSING), t_receipt_identifier = %!@(MISSING), t_fh_internal_state = %!d(MISSING), m_merchant_identifier = %!@(MISSING), m_industrycode = %!d(MISSING), m_name = %!@(MISSING), m_raw_name = %!@(MISSING), m_category = %!d(MISSING), m_detailed_category = %!@(MISSING), m_displayname = %!@(MISSING), m_street = %!@(MISSING), m_city = %!@(MISSING), m_state = %!@(MISSING), m_zip = %!@(MISSING), m_country_code = %!@(MISSING), m_country = %!@(MISSING), m_maps_merchant_id = %!@(MISSING), m_maps_merchant_result_id = %!d(MISSING), m_maps_merchant_brand_id = %!@(MISSING), m_maps_merchant_brand_result_id = %!d(MISSING), lat = %!f(MISSING), long = %!f(MISSING), v_accuracy = %!f(MISSING), h_accuracy = %!f(MISSING), dispute_type = %!d(MISSING), dispute_status = %!d(MISSING), peer_pay_counterpart = %!@(MISSING), peer_pay_type = %!d(MISSING), t_description = %!@(MISSING), peer_pay_is_recurring = %!d(MISSING), dispute_open_date = %!d(MISSING), dispute_last_updated_date = %!d(MISSING) where t_identifier == %!@(MISSING)"

```
