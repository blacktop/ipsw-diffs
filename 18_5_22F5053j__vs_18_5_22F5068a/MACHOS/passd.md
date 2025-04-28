## passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

-1591.6.3.0.0
-  __TEXT.__text: 0x5429ec
+1591.6.7.0.0
+  __TEXT.__text: 0x543510
   __TEXT.__auth_stubs: 0x59b0
-  __TEXT.__objc_stubs: 0x6c940
-  __TEXT.__objc_methlist: 0x32534
+  __TEXT.__objc_stubs: 0x6cb80
+  __TEXT.__objc_methlist: 0x325dc
   __TEXT.__const: 0x299a
-  __TEXT.__cstring: 0x5f3cb
+  __TEXT.__cstring: 0x5f6bb
   __TEXT.__objc_classname: 0x6cb9
-  __TEXT.__objc_methtype: 0x126f4
+  __TEXT.__objc_methtype: 0x12702
   __TEXT.__gcc_except_tab: 0x974c
-  __TEXT.__objc_methname: 0x99aba
-  __TEXT.__oslogstring: 0x5025d
+  __TEXT.__objc_methname: 0x99d3f
+  __TEXT.__oslogstring: 0x504cd
   __TEXT.__ustring: 0x14
   __TEXT.__swift5_typeref: 0x1776
   __TEXT.__constg_swiftt: 0xeb0

   __TEXT.__swift_as_ret: 0x30
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x11bc8
+  __TEXT.__unwind_info: 0x11bf0
   __TEXT.__eh_frame: 0x1390
   __DATA_CONST.__auth_got: 0x2ce8
   __DATA_CONST.__got: 0x35a0
   __DATA_CONST.__auth_ptr: 0x4c0
-  __DATA_CONST.__const: 0x2cac8
-  __DATA_CONST.__cfstring: 0x309e0
+  __DATA_CONST.__const: 0x2cae8
+  __DATA_CONST.__cfstring: 0x30b60
   __DATA_CONST.__objc_classlist: 0x17b0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x598

   __DATA_CONST.__objc_arrayobj: 0x540
   __DATA_CONST.__objc_dictobj: 0x280
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x3d748
-  __DATA.__objc_selrefs: 0x1e138
-  __DATA.__objc_ivar: 0x2730
+  __DATA.__objc_const: 0x3d768
+  __DATA.__objc_selrefs: 0x1e1c8
+  __DATA.__objc_ivar: 0x2734
   __DATA.__objc_data: 0xf878
   __DATA.__data: 0x5340
   __DATA.__bss: 0x25a0

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 25517
+  Functions: 25533
   Symbols:   3306
-  CStrings:  33640
+  CStrings:  33684
 
CStrings:
+ "@\"NSCalendar\""
+ "CREATE TABLE IF NOT EXISTS cow (pid INTEGER, c_pid INTEGER, a TEXT, b INTEGER, c INTEGER, d TEXT, e TEXT, h TEXT, j TEXT, k INTEGER, l INTEGER, m TEXT, r TEXT, s TEXT, t TEXT, u TEXT, v TEXT, w INTEGER, x TEXT, y BOOL, z TEXT, aa TEXT, ab TEXT, localized_pay_in_full_subtitle_override TEXT, has_preconfigured_offers TEXT, has_default_plan BOOL, instore_capabilities TEXT, is_handoff BOOL, requires_in_store_plan_selection BOOL, merchandising_identifier TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS cowboy (pid INTEGER, c_pid INTEGER, a TEXT, b INTEGER, c INTEGER, d TEXT, e TEXT, f TEXT, h TEXT, i TEXT, ma BOOL, mb BOOL, instore_capabilities TEXT, selected_offer_sticky_duration INTEGER, selected_offer_active_duration INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS payment_offer_installment_assessment_offer (pid INTEGER, assessment_pid INTEGER, identifier TEXT, service_provider_url TEXT, due_date INTEGER, expiration_date INTEGER, total_cost_amount INTEGER, total_cost_currency TEXT, installment_count INTEGER, installment_period INTEGER, installment_interval INTEGER, installment_amount_amount INTEGER, installment_amount_currency TEXT, total_interest_and_fees_amount_amount INTEGER, total_interest_and_fees_amount_currency TEXT, service_provider_data TEXT, preferred_language TEXT, order_index INTEGER, type INTEGER, follow_up_type INTEGER, sticky_duration INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS payment_transaction (pid INTEGER, source_pid INTEGER, archive_pid INTEGER, identifier TEXT, service_identifier TEXT, payment_hash TEXT, payment_hash_component_1 TEXT, payment_hash_component_2 TEXT, currency_code TEXT, amount INTEGER, subtotal_amount INTEGER, locality TEXT, administrative_area TEXT, transaction_date INTEGER  NOT NULL, transaction_status_changed_date INTEGER, location_date INTEGER, location_latitude REAL, location_longitude REAL, location_altitude REAL, location_horizontal_accuracy REAL, location_vertical_accuracy REAL, start_station_code BLOB, start_station TEXT, start_station_latitude REAL, start_station_longitude REAL, end_station_code BLOB, end_station TEXT, end_station_latitude REAL, end_station_longitude REAL, transaction_status INTEGER, transaction_type INTEGER, transit_type INTEGER, transit_modifiers INTEGER, en_route INTEGER, station_code_provider TEXT, city_code INTEGER, technology_type INTEGER, transaction_source INTEGER, requires_location INTEGER, has_notification_service_data INTEGER, processed_for_location INTEGER, processed_for_merchant_cleanup INTEGER, requires_merchant_reprocessing INTEGER, last_merchant_reprocessing_date INTEGER, processed_for_stations INTEGER, merchant_name TEXT, merchant_raw_name TEXT, merchant_industry_category TEXT, merchant_industry_code INTEGER, peer_payment_type INTEGER,peer_payment_counterpart_handle TEXT,peer_payment_memo TEXT,peer_payment_message_received_date INTEGER,account_type INTEGER,foreign_exchange_information_destination_currency_code TEXT,foreign_exchange_information_destination_amount INTEGER,foreign_exchange_information_exchange_rate TEXT,primary_funding_source_amount INTEGER,primary_funding_source_currency_code TEXT,secondary_funding_source_amount INTEGER,secondary_funding_source_currency_code TEXT,secondary_funding_source_network INTEGER,secondary_funding_source_dpan_suffix TEXT,secondary_funding_source_fpan_identifier TEXT,secondary_funding_source_description TEXT,secondary_funding_source_type INTEGER,request_device_score_identifier TEXT,send_device_score_identifier TEXT,device_score_identifiers_required INTEGER,device_score_identifiers_submitted INTEGER,merchant_provided_description TEXT,merchant_provided_title TEXT,metadata TEXT,expiration_date INTEGER,adjustment_type INTEGER,transaction_declined_reason INTEGER, a INTEGER, account_identifier TEXT, c INTEGER, d TEXT, e TEXT, f TEXT, g TEXT, h TEXT, i TEXT, j TEXT, k TEXT, l TEXT, m INTEGER, n INTEGER, o TEXT, should_suppress_date INTEGER, p TEXT, q INTEGER, r TEXT, s TEXT, t TEXT, maps_merchant_pid INTEGER, u INTEGER, v TEXT, w INTEGER, x INTEGER, y TEXT, ab TEXT, ac INTEGER, ad INTEGER, ae TEXT, af TEXT, ag TEXT, ah TEXT, use_raw_merchant_data INTEGER, issue_report_identifier TEXT, suppress_notifications INTEGER, fuzzy_matched INTEGER, receipt_provider_identifier TEXT, receipt_provider_url TEXT, receipt_identifier TEXT, barcode_identifier TEXT, payment_pin_format INTEGER, nonce BLOB, signing_key_material BLOB, partial_signature BLOB, requested_auth_mechanisms INTEGER, primary_funding_source_description TEXT, nominal_amount INTEGER, has_additional_offers BOOL, dpan_identifier TEXT, zm TEXT, eligible_eligible_rewards_percent_aggregate INTEGER, eligible_rewards_cash_aggregate INTEGER, is_coarse_location INTEGER, amount_added_to_auth INTEGER, afi INTEGER, is_merchant_token_transaction INTEGER, recurring BOOL, merchant_fallback_logo_image_url TEXT, interest_reassessment BOOL, associated_statement_identifiers TEXT, payment_network_identifier INTEGER, update_sequence_number INTEGER NOT NULL, needs_sync_to_finance INTEGER NOT NULL, ca INTEGER, iit INTEGER, iimu TEXT, cb TEXT, top_up_type INTEGER, preferred_category INTEGER, merchant_business_connect_brand_identifier TEXT, request_token TEXT, last_force_merchant_reprocessing_request_date INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS selected_payment_offer (pid INTEGER, type INTEGER, pass_pid INTEGER, confirmation_record_pid INTEGER, selected_offer_pid INTEGER, storage_type INTEGER, user_selection_date INTEGER, created_date INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS selected_payment_offer_rewards (pid INTEGER, type INTEGER, pass_pid INTEGER, pass_unique_id TEXT, dpan_identifier TEXT, pass_type_identifier TEXT, pass_serial_number TEXT, primary_account_identifier TEXT, selected_offer_identifier TEXT, criteria_identifier TEXT, session_identifier TEXT, service_provider_data TEXT, sticky_duration INTEGER, active_duration INTEGER, PRIMARY KEY (pid));"
+ "Migrating database from user_version 18039 to 18040"
+ "Migrating database from user_version 18040 to 18041"
+ "Migrating database from user_version 18041 to 18042"
+ "Migrating database from user_version 18042 to 18043"
+ "Migrating database from user_version 18043 to 18044"
+ "Migrating database from user_version 18044 to 18045"
+ "Migrating database from user_version 18045 to 18046"
+ "Migrating database from user_version 18046 to 18047"
+ "Migrating database from user_version 18047 to 18048"
+ "Migrating database from user_version 18048 to 18049"
+ "Migrating database from user_version 18049 to 18050"
+ "Migrating database from user_version 18050 to 18051"
+ "SELECT source_pid, transaction_type, merchant_industry_code FROM payment_transaction JOIN transaction_source ON payment_transaction.source_pid = transaction_source.pid WHERE payment_transaction.transaction_date >= ? AND payment_transaction.transaction_date <= ?"
+ "UPDATE whitney SET q = l WHERE q = 0"
+ "_createIntervalFromPreviousSunday:"
+ "_migrateFrom18039To18040:context:"
+ "_migrateFrom18040To18041:context:"
+ "_migrateFrom18041To18042:context:"
+ "_migrateFrom18042To18043:context:"
+ "_migrateFrom18043To18044:context:"
+ "_migrateFrom18044To18045:context:"
+ "_migrateFrom18045To18046:context:"
+ "_migrateFrom18046To18047:context:"
+ "_migrateFrom18047To18048:context:"
+ "_migrateFrom18048To18049:context:"
+ "_migrateFrom18049To18050:context:"
+ "_migrateFrom18050To18051:context:"
+ "_utcCalendar"
+ "active_duration INTEGER"
+ "anyInDatabase:potentialUnattributedMapsMatchForTransaction:"
+ "currentCollectionDateInterval"
+ "has_default_plan BOOL"
+ "lastForceMerchantReprocessingRequestDate"
+ "last_force_merchant_reprocessing_request_date"
+ "last_force_merchant_reprocessing_request_date INTEGER"
+ "payment_offer_contactless_selection_type"
+ "payment_offer_contactless_selection_type INTEGER"
+ "selected_offer_active_duration INTEGER"
+ "selected_offer_sticky_duration INTEGER"
+ "setIsPotentialUnattributedMapsMatch:"
+ "setLastForceMerchantReprocessingRequestDate:"
+ "shouldIgnoreMapsMatches"
+ "sticky_duration INTEGER"
+ "storage_type INTEGER"
+ "user_selection_date INTEGER"
- "CREATE TABLE IF NOT EXISTS cow (pid INTEGER, c_pid INTEGER, a TEXT, b INTEGER, c INTEGER, d TEXT, e TEXT, h TEXT, j TEXT, k INTEGER, l INTEGER, m TEXT, r TEXT, s TEXT, t TEXT, u TEXT, v TEXT, w INTEGER, x TEXT, y BOOL, z TEXT, aa TEXT, ab TEXT, localized_pay_in_full_subtitle_override TEXT, has_preconfigured_offers TEXT, instore_capabilities TEXT, is_handoff BOOL, requires_in_store_plan_selection BOOL, merchandising_identifier TEXT, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS cowboy (pid INTEGER, c_pid INTEGER, a TEXT, b INTEGER, c INTEGER, d TEXT, e TEXT, f TEXT, h TEXT, i TEXT, ma BOOL, mb BOOL, instore_capabilities TEXT, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS payment_offer_installment_assessment_offer (pid INTEGER, assessment_pid INTEGER, identifier TEXT, service_provider_url TEXT, due_date INTEGER, expiration_date INTEGER, total_cost_amount INTEGER, total_cost_currency TEXT, installment_count INTEGER, installment_period INTEGER, installment_interval INTEGER, installment_amount_amount INTEGER, installment_amount_currency TEXT, total_interest_and_fees_amount_amount INTEGER, total_interest_and_fees_amount_currency TEXT, service_provider_data TEXT, preferred_language TEXT, order_index INTEGER, type INTEGER, follow_up_type INTEGER, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS payment_transaction (pid INTEGER, source_pid INTEGER, archive_pid INTEGER, identifier TEXT, service_identifier TEXT, payment_hash TEXT, payment_hash_component_1 TEXT, payment_hash_component_2 TEXT, currency_code TEXT, amount INTEGER, subtotal_amount INTEGER, locality TEXT, administrative_area TEXT, transaction_date INTEGER  NOT NULL, transaction_status_changed_date INTEGER, location_date INTEGER, location_latitude REAL, location_longitude REAL, location_altitude REAL, location_horizontal_accuracy REAL, location_vertical_accuracy REAL, start_station_code BLOB, start_station TEXT, start_station_latitude REAL, start_station_longitude REAL, end_station_code BLOB, end_station TEXT, end_station_latitude REAL, end_station_longitude REAL, transaction_status INTEGER, transaction_type INTEGER, transit_type INTEGER, transit_modifiers INTEGER, en_route INTEGER, station_code_provider TEXT, city_code INTEGER, technology_type INTEGER, transaction_source INTEGER, requires_location INTEGER, has_notification_service_data INTEGER, processed_for_location INTEGER, processed_for_merchant_cleanup INTEGER, requires_merchant_reprocessing INTEGER, last_merchant_reprocessing_date INTEGER, processed_for_stations INTEGER, merchant_name TEXT, merchant_raw_name TEXT, merchant_industry_category TEXT, merchant_industry_code INTEGER, peer_payment_type INTEGER,peer_payment_counterpart_handle TEXT,peer_payment_memo TEXT,peer_payment_message_received_date INTEGER,account_type INTEGER,foreign_exchange_information_destination_currency_code TEXT,foreign_exchange_information_destination_amount INTEGER,foreign_exchange_information_exchange_rate TEXT,primary_funding_source_amount INTEGER,primary_funding_source_currency_code TEXT,secondary_funding_source_amount INTEGER,secondary_funding_source_currency_code TEXT,secondary_funding_source_network INTEGER,secondary_funding_source_dpan_suffix TEXT,secondary_funding_source_fpan_identifier TEXT,secondary_funding_source_description TEXT,secondary_funding_source_type INTEGER,request_device_score_identifier TEXT,send_device_score_identifier TEXT,device_score_identifiers_required INTEGER,device_score_identifiers_submitted INTEGER,merchant_provided_description TEXT,merchant_provided_title TEXT,metadata TEXT,expiration_date INTEGER,adjustment_type INTEGER,transaction_declined_reason INTEGER, a INTEGER, account_identifier TEXT, c INTEGER, d TEXT, e TEXT, f TEXT, g TEXT, h TEXT, i TEXT, j TEXT, k TEXT, l TEXT, m INTEGER, n INTEGER, o TEXT, should_suppress_date INTEGER, p TEXT, q INTEGER, r TEXT, s TEXT, t TEXT, maps_merchant_pid INTEGER, u INTEGER, v TEXT, w INTEGER, x INTEGER, y TEXT, ab TEXT, ac INTEGER, ad INTEGER, ae TEXT, af TEXT, ag TEXT, ah TEXT, use_raw_merchant_data INTEGER, issue_report_identifier TEXT, suppress_notifications INTEGER, fuzzy_matched INTEGER, receipt_provider_identifier TEXT, receipt_provider_url TEXT, receipt_identifier TEXT, barcode_identifier TEXT, payment_pin_format INTEGER, nonce BLOB, signing_key_material BLOB, partial_signature BLOB, requested_auth_mechanisms INTEGER, primary_funding_source_description TEXT, nominal_amount INTEGER, has_additional_offers BOOL, dpan_identifier TEXT, zm TEXT, eligible_eligible_rewards_percent_aggregate INTEGER, eligible_rewards_cash_aggregate INTEGER, is_coarse_location INTEGER, amount_added_to_auth INTEGER, afi INTEGER, is_merchant_token_transaction INTEGER, recurring BOOL, merchant_fallback_logo_image_url TEXT, interest_reassessment BOOL, associated_statement_identifiers TEXT, payment_network_identifier INTEGER, update_sequence_number INTEGER NOT NULL, needs_sync_to_finance INTEGER NOT NULL, ca INTEGER, iit INTEGER, iimu TEXT, cb TEXT, top_up_type INTEGER, preferred_category INTEGER, merchant_business_connect_brand_identifier TEXT, request_token TEXT, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS selected_payment_offer (pid INTEGER, type INTEGER, pass_pid INTEGER, confirmation_record_pid INTEGER, selected_offer_pid INTEGER, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS selected_payment_offer_rewards (pid INTEGER, type INTEGER, pass_pid INTEGER, pass_unique_id TEXT, dpan_identifier TEXT, pass_type_identifier TEXT, pass_serial_number TEXT, primary_account_identifier TEXT, selected_offer_identifier TEXT, criteria_identifier TEXT, session_identifier TEXT, service_provider_data TEXT, PRIMARY KEY (pid));"
- "SELECT source_pid, transaction_type FROM payment_transaction JOIN transaction_source ON payment_transaction.source_pid = transaction_source.pid WHERE payment_transaction.transaction_date >= ? AND payment_transaction.transaction_date <= ?"
- "_createIntervalFromPreviousSunday:withCalendar:"

```
