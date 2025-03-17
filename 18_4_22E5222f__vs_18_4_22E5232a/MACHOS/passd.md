## passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

-1591.5.16.5.0
-  __TEXT.__text: 0x53fc38
+1591.5.17.5.1
+  __TEXT.__text: 0x541060
   __TEXT.__auth_stubs: 0x59b0
-  __TEXT.__objc_stubs: 0x6c3e0
-  __TEXT.__objc_methlist: 0x323a4
+  __TEXT.__objc_stubs: 0x6c620
+  __TEXT.__objc_methlist: 0x32454
   __TEXT.__const: 0x299a
-  __TEXT.__cstring: 0x5e14b
+  __TEXT.__cstring: 0x5ecdb
   __TEXT.__objc_classname: 0x6ca9
   __TEXT.__objc_methtype: 0x126f4
-  __TEXT.__gcc_except_tab: 0x96bc
-  __TEXT.__objc_methname: 0x99599
-  __TEXT.__oslogstring: 0x4fd0d
+  __TEXT.__gcc_except_tab: 0x9718
+  __TEXT.__objc_methname: 0x997e7
+  __TEXT.__oslogstring: 0x5008d
   __TEXT.__ustring: 0x14
   __TEXT.__swift5_typeref: 0x1776
   __TEXT.__constg_swiftt: 0xeb0

   __TEXT.__swift_as_ret: 0x30
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x11b48
+  __TEXT.__unwind_info: 0x11b78
   __TEXT.__eh_frame: 0x1390
   __DATA_CONST.__auth_got: 0x2ce8
   __DATA_CONST.__got: 0x3598
-  __DATA_CONST.__auth_ptr: 0x4c0
-  __DATA_CONST.__const: 0x2ca08
-  __DATA_CONST.__cfstring: 0x301c0
+  __DATA_CONST.__auth_ptr: 0x490
+  __DATA_CONST.__const: 0x2ca48
+  __DATA_CONST.__cfstring: 0x30640
   __DATA_CONST.__objc_classlist: 0x17a8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x598

   __DATA_CONST.__objc_dictobj: 0x280
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0x3d6b8
-  __DATA.__objc_selrefs: 0x1dfe8
+  __DATA.__objc_selrefs: 0x1e078
   __DATA.__objc_ivar: 0x2730
   __DATA.__objc_data: 0xf828
   __DATA.__data: 0x5340

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 25475
+  Functions: 25490
   Symbols:   3305
-  CStrings:  33506
+  CStrings:  33576
 
CStrings:
+ "CREATE TABLE IF NOT EXISTS cow (pid INTEGER, c_pid INTEGER, a TEXT, b INTEGER, c INTEGER, d TEXT, e TEXT, h TEXT, j TEXT, k INTEGER, l INTEGER, m TEXT, r TEXT, s TEXT, t TEXT, u TEXT, v TEXT, w INTEGER, x TEXT, y BOOL, z TEXT, aa TEXT, ab TEXT, localized_pay_in_full_subtitle_override TEXT, has_preconfigured_offers TEXT, instore_capabilities TEXT, is_handoff BOOL, requires_in_store_plan_selection BOOL, merchandising_identifier TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS cowboy (pid INTEGER, c_pid INTEGER, a TEXT, b INTEGER, c INTEGER, d TEXT, e TEXT, f TEXT, h TEXT, i TEXT, ma BOOL, mb BOOL, instore_capabilities TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS flights (pid INTEGER, pass_pid INTEGER, airline_code TEXT, airline_name TEXT, flight_number INTEGER, departure_airport_code TEXT, departure_airport_name TEXT, departure_airport_latitude REAL, departure_airport_longitude REAL, departure_airport_time_zone_name TEXT, departure_terminal TEXT, departure_gate TEXT, departure_status INTEGER, original_departure_date INTEGER, current_departure_date INTEGER, arrival_airport_code TEXT, arrival_airport_name TEXT, arrival_airport_latitude REAL, arrival_airport_longitude REAL, arrival_airport_time_zone_name TEXT, arrival_terminal TEXT, arrival_gate TEXT, arrival_baggage_claim TEXT, arrival_status INTEGER, original_arrival_date INTEGER, current_arrival_date INTEGER, state INTEGER, data_source INTEGER, last_updated_date INTEGER, departure_airport_city TEXT, arrival_airport_city TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS giraffe (pid INTEGER, i_pid INTEGER, table_pid INTEGER, default_variant INTEGER, light_variant INTEGER, dark_variant INTEGER, type INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS issuer_messaging_flag (pid INTEGER, identifier TEXT, name TEXT, context_type INTEGER, context_identifier TEXT, context_feature INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS payment_offer_capability (pid INTEGER, catalog_pid INTEGER, fpan_identifier TEXT, pass_serial_number TEXT, pass_type_identifier TEXT, features TEXT, merchandising_identifier TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS payment_offer_installment_assessment_offer (pid INTEGER, assessment_pid INTEGER, identifier TEXT, service_provider_url TEXT, due_date INTEGER, expiration_date INTEGER, total_cost_amount INTEGER, total_cost_currency TEXT, installment_count INTEGER, installment_period INTEGER, installment_interval INTEGER, installment_amount_amount INTEGER, installment_amount_currency TEXT, total_interest_and_fees_amount_amount INTEGER, total_interest_and_fees_amount_currency TEXT, service_provider_data TEXT, preferred_language TEXT, order_index INTEGER, type INTEGER, follow_up_type INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS payment_offer_installment_merchant_details (pid INTEGER, installment_assessment_offer_pid INTEGER, merchant_name TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS payment_transaction (pid INTEGER, source_pid INTEGER, archive_pid INTEGER, identifier TEXT, service_identifier TEXT, payment_hash TEXT, payment_hash_component_1 TEXT, payment_hash_component_2 TEXT, currency_code TEXT, amount INTEGER, subtotal_amount INTEGER, locality TEXT, administrative_area TEXT, transaction_date INTEGER  NOT NULL, transaction_status_changed_date INTEGER, location_date INTEGER, location_latitude REAL, location_longitude REAL, location_altitude REAL, location_horizontal_accuracy REAL, location_vertical_accuracy REAL, start_station_code BLOB, start_station TEXT, start_station_latitude REAL, start_station_longitude REAL, end_station_code BLOB, end_station TEXT, end_station_latitude REAL, end_station_longitude REAL, transaction_status INTEGER, transaction_type INTEGER, transit_type INTEGER, transit_modifiers INTEGER, en_route INTEGER, station_code_provider TEXT, city_code INTEGER, technology_type INTEGER, transaction_source INTEGER, requires_location INTEGER, has_notification_service_data INTEGER, processed_for_location INTEGER, processed_for_merchant_cleanup INTEGER, requires_merchant_reprocessing INTEGER, last_merchant_reprocessing_date INTEGER, processed_for_stations INTEGER, merchant_name TEXT, merchant_raw_name TEXT, merchant_industry_category TEXT, merchant_industry_code INTEGER, peer_payment_type INTEGER,peer_payment_counterpart_handle TEXT,peer_payment_memo TEXT,peer_payment_message_received_date INTEGER,account_type INTEGER,foreign_exchange_information_destination_currency_code TEXT,foreign_exchange_information_destination_amount INTEGER,foreign_exchange_information_exchange_rate TEXT,primary_funding_source_amount INTEGER,primary_funding_source_currency_code TEXT,secondary_funding_source_amount INTEGER,secondary_funding_source_currency_code TEXT,secondary_funding_source_network INTEGER,secondary_funding_source_dpan_suffix TEXT,secondary_funding_source_fpan_identifier TEXT,secondary_funding_source_description TEXT,secondary_funding_source_type INTEGER,request_device_score_identifier TEXT,send_device_score_identifier TEXT,device_score_identifiers_required INTEGER,device_score_identifiers_submitted INTEGER,merchant_provided_description TEXT,merchant_provided_title TEXT,metadata TEXT,expiration_date INTEGER,adjustment_type INTEGER,transaction_declined_reason INTEGER, a INTEGER, account_identifier TEXT, c INTEGER, d TEXT, e TEXT, f TEXT, g TEXT, h TEXT, i TEXT, j TEXT, k TEXT, l TEXT, m INTEGER, n INTEGER, o TEXT, should_suppress_date INTEGER, p TEXT, q INTEGER, r TEXT, s TEXT, t TEXT, maps_merchant_pid INTEGER, u INTEGER, v TEXT, w INTEGER, x INTEGER, y TEXT, ab TEXT, ac INTEGER, ad INTEGER, ae TEXT, af TEXT, ag TEXT, ah TEXT, use_raw_merchant_data INTEGER, issue_report_identifier TEXT, suppress_notifications INTEGER, fuzzy_matched INTEGER, receipt_provider_identifier TEXT, receipt_provider_url TEXT, receipt_identifier TEXT, barcode_identifier TEXT, payment_pin_format INTEGER, nonce BLOB, signing_key_material BLOB, partial_signature BLOB, requested_auth_mechanisms INTEGER, primary_funding_source_description TEXT, nominal_amount INTEGER, has_additional_offers BOOL, dpan_identifier TEXT, zm TEXT, eligible_eligible_rewards_percent_aggregate INTEGER, eligible_rewards_cash_aggregate INTEGER, is_coarse_location INTEGER, amount_added_to_auth INTEGER, afi INTEGER, is_merchant_token_transaction INTEGER, recurring BOOL, merchant_fallback_logo_image_url TEXT, interest_reassessment BOOL, associated_statement_identifiers TEXT, payment_network_identifier INTEGER, update_sequence_number INTEGER NOT NULL, needs_sync_to_finance INTEGER NOT NULL, ca INTEGER, iit INTEGER, iimu TEXT, cb TEXT, top_up_type INTEGER, preferred_category INTEGER, merchant_business_connect_brand_identifier TEXT, request_token TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS payment_transaction_archive (pid INTEGER, payment_transaction_pid INTEGER, bokchoy_pid INTEGER, cumin_pid INTEGER, peer_payment_requests_pid INTEGER, PRIMARY KEY(pid));"
+ "CREATE TABLE IF NOT EXISTS peer_payment_requests (pid INTEGER, request_token TEXT, peer_payment_account_pid INTEGER, requester_address TEXT, requestee_address TEXT, amount INTEGER, currency TEXT, memo TEXT, session_id TEXT, expiry_date INTEGER, actions TEXT, request_date INTEGER, last_dismissed_date INTEGER, status TEXT, message_guid TEXT, context INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS pending_provisioning_remote_credential (pid INTEGER, base_pid INTEGER, a TEXT, b INTEGER, c TEXT, d INTEGER, e TEXT, f TEXT, g TEXT, i TEXT, l TEXT, m TEXT, n BLOB, j BOOL, k BOOL, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS selected_payment_offer_installment (pid INTEGER, type INTEGER, pass_pid INTEGER, pass_unique_id TEXT, dpan_identifier TEXT, pass_type_identifier TEXT, pass_serial_number TEXT, primary_account_identifier TEXT, selected_offer_identifier TEXT, criteria_identifier TEXT, session_identifier TEXT, selection_type INTEGER, is_preconfigured_offer BOOL, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS selected_payment_offer_rewards (pid INTEGER, type INTEGER, pass_pid INTEGER, pass_unique_id TEXT, dpan_identifier TEXT, pass_type_identifier TEXT, pass_serial_number TEXT, primary_account_identifier TEXT, selected_offer_identifier TEXT, criteria_identifier TEXT, session_identifier TEXT, service_provider_data TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS whitney (pid INTEGER, a INTEGER, b TEXT, c INTEGER, d INTEGER, e TEXT,f TEXT,g TEXT,h INTEGER,i BLOB,j TEXT,k INTEGER, l INTEGER, m TEXT, n INTEGER, o TEXT, p TEXT, q INTEGER, r TEXT, s TEXT, t TEXT, u TEXT, v BLOB, w INTEGER, x TEXT, y BOOL, PRIMARY KEY (pid));"
+ "Identifying %lu stale credentials for pass: '%@'..."
+ "MERCHANT_TOKEN_UPCOMING_PAYMENTS_NOTIFICATION_SINGLE_PAYMENT_BODY_WITH_AMOUNT"
+ "MERCHANT_TOKEN_UPCOMING_PAYMENTS_NOTIFICATION_SINGLE_PAYMENT_BODY_WITH_AMOUNT_AND_CARD_NAME"
+ "Migrating database from user_version 18015 to 18016"
+ "Migrating database from user_version 18016 to 18017"
+ "Migrating database from user_version 18017 to 18018"
+ "Migrating database from user_version 18018 to 18019"
+ "Migrating database from user_version 18019 to 18020"
+ "Migrating database from user_version 18020 to 18021"
+ "Migrating database from user_version 18021 to 18022"
+ "Migrating database from user_version 18022 to 18023"
+ "Migrating database from user_version 18023 to 18024"
+ "Migrating database from user_version 18024 to 18025"
+ "Migrating database from user_version 18025 to 18026"
+ "Migrating database from user_version 18026 to 18027"
+ "Migrating database from user_version 18027 to 18028"
+ "Migrating database from user_version 18028 to 18029"
+ "Migrating database from user_version 18029 to 18030"
+ "PDMerchantTokenMetadataCache: failed to create private key. merchantTokenId=%@, createRandomKeyError=%@"
+ "PDMerchantTokenMetadataCache: failed to modify application tag of private key. merchantTokenId=%@, privateKeyApplicationLabel=%@, updateError=%@"
+ "PDMerchantTokenMetadataCache: failed to retrieve external representation of private key. merchantTokenId=%@, publicKeyHash=%@, copyExternalRepresentationError=%@"
+ "PDMerchantTokenMetadataCache: failed to retrieve external representation of public key. merchantTokenId=%@, privateKeyApplicationLabel=%@, copyExternalRepresentationError=%@"
+ "PDMerchantTokenMetadataCache: failed to retrieve private key. merchantTokenId=%@, publicKeyHash=%@, copyMatchingError=%@"
+ "PDMerchantTokenMetadataCache: failed to retrieve public key associated with private key. merchantTokenId=%@, privateKeyApplicationLabel=%@"
+ "SELECT pid, i_pid, dynamic_content_page_pid FROM giraffe"
+ "SELECT pid, supports_instore FROM cow"
+ "SELECT pid, supports_instore FROM cowboy"
+ "UPDATE cow SET instore_capabilities = %@ WHERE pid = %ld"
+ "UPDATE cowboy SET instore_capabilities = %@ WHERE pid = %ld"
+ "UPDATE giraffe SET table_pid = %ld WHERE pid = %ld"
+ "UPDATE payment_transaction SET needs_sync_to_finance = 1;"
+ "UPDATE whitney SET y = CASE WHEN pa.pni <> 133 THEN 1 ELSE 0 END FROM (SELECT pid, payment_network_identifier AS pni FROM payment_application) AS pa WHERE pa.pid = whitney.a"
+ "_migrateFrom18015To18016:context:"
+ "_migrateFrom18016To18017:context:"
+ "_migrateFrom18017To18018:context:"
+ "_migrateFrom18018To18019:context:"
+ "_migrateFrom18019To18020:context:"
+ "_migrateFrom18020To18021:context:"
+ "_migrateFrom18021To18022:context:"
+ "_migrateFrom18022To18023:context:"
+ "_migrateFrom18023To18024:context:"
+ "_migrateFrom18024To18025:context:"
+ "_migrateFrom18025To18026:context:"
+ "_migrateFrom18026To18027:context:"
+ "_migrateFrom18027To18028:context:"
+ "_migrateFrom18028To18029:context:"
+ "_migrateFrom18029To18030:context:"
+ "arrival_airport_city TEXT"
+ "context INTEGER"
+ "departure_airport_city TEXT"
+ "dynamic_content_page_pid"
+ "flights"
+ "follow_up_type INTEGER"
+ "instore_capabilities TEXT"
+ "isManagedByTSM"
+ "is_preconfigured_offer BOOL"
+ "j BOOL"
+ "k BOOL"
+ "merchandising_identifier TEXT"
+ "merchant_business_connect_brand_identifier TEXT"
+ "message_guid TEXT"
+ "pass_serial_number TEXT"
+ "pass_type_identifier TEXT"
+ "peer_payment_requests_pid INTEGER"
+ "postPurchase"
+ "prePurchase"
+ "request_token TEXT"
+ "selection_type INTEGER"
+ "setDeleteInactiveKeysAfterDays:"
+ "setDeleteIncompleteCredentialAfterDays:"
+ "setIsManagedByTSM:"
+ "supports_instore"
+ "supports_merchandising"
+ "table_pid INTEGER"
+ "v28@?0@\"NSArray\"8B16@\"NSError\"20"
- "CREATE TABLE IF NOT EXISTS cow (pid INTEGER, c_pid INTEGER, a TEXT, b INTEGER, c INTEGER, d TEXT, e TEXT, h TEXT, j TEXT, k INTEGER, l INTEGER, m TEXT, r TEXT, s TEXT, t TEXT, u TEXT, v TEXT, w INTEGER, x TEXT, y BOOL, z TEXT, aa TEXT, ab TEXT, localized_pay_in_full_subtitle_override TEXT, has_preconfigured_offers TEXT, supports_merchandising BOOL, supports_instore BOOL, is_handoff BOOL, requires_in_store_plan_selection BOOL, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS cowboy (pid INTEGER, c_pid INTEGER, a TEXT, b INTEGER, c INTEGER, d TEXT, e TEXT, f TEXT, h TEXT, i TEXT, ma BOOL, mb BOOL, supports_merchandising BOOL, supports_instore BOOL, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS giraffe (pid INTEGER, i_pid INTEGER, dynamic_content_page_pid INTEGER,default_variant INTEGER, light_variant INTEGER, dark_variant INTEGER, type INTEGER, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS payment_offer_installment_assessment_offer (pid INTEGER, assessment_pid INTEGER, identifier TEXT, service_provider_url TEXT, due_date INTEGER, total_cost_amount INTEGER, total_cost_currency TEXT, installment_count INTEGER, installment_period INTEGER, installment_interval INTEGER, installment_amount_amount INTEGER, installment_amount_currency TEXT, total_interest_and_fees_amount_amount INTEGER, total_interest_and_fees_amount_currency TEXT, service_provider_data TEXT, preferred_language TEXT, order_index INTEGER, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS payment_transaction (pid INTEGER, source_pid INTEGER, archive_pid INTEGER, identifier TEXT, service_identifier TEXT, payment_hash TEXT, payment_hash_component_1 TEXT, payment_hash_component_2 TEXT, currency_code TEXT, amount INTEGER, subtotal_amount INTEGER, locality TEXT, administrative_area TEXT, transaction_date INTEGER  NOT NULL, transaction_status_changed_date INTEGER, location_date INTEGER, location_latitude REAL, location_longitude REAL, location_altitude REAL, location_horizontal_accuracy REAL, location_vertical_accuracy REAL, start_station_code BLOB, start_station TEXT, start_station_latitude REAL, start_station_longitude REAL, end_station_code BLOB, end_station TEXT, end_station_latitude REAL, end_station_longitude REAL, transaction_status INTEGER, transaction_type INTEGER, transit_type INTEGER, transit_modifiers INTEGER, en_route INTEGER, station_code_provider TEXT, city_code INTEGER, technology_type INTEGER, transaction_source INTEGER, requires_location INTEGER, has_notification_service_data INTEGER, processed_for_location INTEGER, processed_for_merchant_cleanup INTEGER, requires_merchant_reprocessing INTEGER, last_merchant_reprocessing_date INTEGER, processed_for_stations INTEGER, merchant_name TEXT, merchant_raw_name TEXT, merchant_industry_category TEXT, merchant_industry_code INTEGER, peer_payment_type INTEGER,peer_payment_counterpart_handle TEXT,peer_payment_memo TEXT,peer_payment_message_received_date INTEGER,account_type INTEGER,foreign_exchange_information_destination_currency_code TEXT,foreign_exchange_information_destination_amount INTEGER,foreign_exchange_information_exchange_rate TEXT,primary_funding_source_amount INTEGER,primary_funding_source_currency_code TEXT,secondary_funding_source_amount INTEGER,secondary_funding_source_currency_code TEXT,secondary_funding_source_network INTEGER,secondary_funding_source_dpan_suffix TEXT,secondary_funding_source_fpan_identifier TEXT,secondary_funding_source_description TEXT,secondary_funding_source_type INTEGER,request_device_score_identifier TEXT,send_device_score_identifier TEXT,device_score_identifiers_required INTEGER,device_score_identifiers_submitted INTEGER,merchant_provided_description TEXT,merchant_provided_title TEXT,metadata TEXT,expiration_date INTEGER,adjustment_type INTEGER,transaction_declined_reason INTEGER, a INTEGER, account_identifier TEXT, c INTEGER, d TEXT, e TEXT, f TEXT, g TEXT, h TEXT, i TEXT, j TEXT, k TEXT, l TEXT, m INTEGER, n INTEGER, o TEXT, should_suppress_date INTEGER, p TEXT, q INTEGER, r TEXT, s TEXT, t TEXT, maps_merchant_pid INTEGER, u INTEGER, v TEXT, w INTEGER, x INTEGER, y TEXT, ab TEXT, ac INTEGER, ad INTEGER, ae TEXT, af TEXT, ag TEXT, ah TEXT, use_raw_merchant_data INTEGER, issue_report_identifier TEXT, suppress_notifications INTEGER, fuzzy_matched INTEGER, receipt_provider_identifier TEXT, receipt_provider_url TEXT, receipt_identifier TEXT, barcode_identifier TEXT, payment_pin_format INTEGER, nonce BLOB, signing_key_material BLOB, partial_signature BLOB, requested_auth_mechanisms INTEGER, primary_funding_source_description TEXT, nominal_amount INTEGER, has_additional_offers BOOL, dpan_identifier TEXT, zm TEXT, eligible_eligible_rewards_percent_aggregate INTEGER, eligible_rewards_cash_aggregate INTEGER, is_coarse_location INTEGER, amount_added_to_auth INTEGER, afi INTEGER, is_merchant_token_transaction INTEGER, recurring BOOL, merchant_fallback_logo_image_url TEXT, interest_reassessment BOOL, associated_statement_identifiers TEXT, payment_network_identifier INTEGER, update_sequence_number INTEGER NOT NULL, needs_sync_to_finance INTEGER NOT NULL, ca INTEGER, iit INTEGER, iimu TEXT, cb TEXT, top_up_type INTEGER, preferred_category INTEGER, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS payment_transaction_archive (pid INTEGER, payment_transaction_pid INTEGER, bokchoy_pid INTEGER, cumin_pid INTEGER, PRIMARY KEY(pid));"
- "CREATE TABLE IF NOT EXISTS peer_payment_requests (pid INTEGER, request_token TEXT, peer_payment_account_pid INTEGER, requester_address TEXT, requestee_address TEXT, amount INTEGER, currency TEXT, memo TEXT, session_id TEXT, expiry_date INTEGER, actions TEXT, request_date INTEGER, last_dismissed_date INTEGER, status TEXT, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS pending_provisioning_remote_credential (pid INTEGER, base_pid INTEGER, a TEXT, b INTEGER, c TEXT, d INTEGER, e TEXT, f TEXT, g TEXT, i TEXT, l TEXT, m TEXT, n BLOB, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS selected_payment_offer_installment (pid INTEGER, type INTEGER, pass_pid INTEGER, pass_unique_id TEXT, dpan_identifier TEXT, primary_account_identifier TEXT, selected_offer_identifier TEXT, criteria_identifier TEXT, session_identifier TEXT, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS selected_payment_offer_rewards (pid INTEGER, type INTEGER, pass_pid INTEGER, pass_unique_id TEXT, dpan_identifier TEXT, primary_account_identifier TEXT, selected_offer_identifier TEXT, criteria_identifier TEXT, session_identifier TEXT, service_provider_data TEXT, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS whitney (pid INTEGER, a INTEGER, b TEXT, c INTEGER, d INTEGER, e TEXT,f TEXT,g TEXT,h INTEGER,i BLOB,j TEXT,k INTEGER, l INTEGER, m TEXT, n INTEGER, o TEXT, p TEXT, q INTEGER, r TEXT, s TEXT, t TEXT, u TEXT, v BLOB, w INTEGER, x TEXT, PRIMARY KEY (pid));"
- "Identifying stale credentials for pass: '%@'..."
- "MERCHANT_TOKEN_UPCOMING_PAYMENTS_NOTIFICATION_SINGLE_PAYMENT_SUBTITLE_WITH_AMOUNT"
- "PDMerchantTokenMetadataCache: failed to create private key. createRandomKeyError=%@"
- "PDMerchantTokenMetadataCache: failed to modify application tag of private key. privateKeyApplicationLabel=%@, updateError=%@"
- "PDMerchantTokenMetadataCache: failed to retrieve external representation of private key. privateKeyApplicationTag=%@, copyExternalRepresentationError=%@"
- "PDMerchantTokenMetadataCache: failed to retrieve external representation of public key. privateKeyApplicationLabel=%@, copyExternalRepresentationError=%@"
- "PDMerchantTokenMetadataCache: failed to retrieve private key. publicKeyHash=%@, copyMatchingError=%@"
- "PDMerchantTokenMetadataCache: failed to retrieve public key associated with private key. privateKeyApplicationLabel=%@"
- "addAppletTypesToSnapshot:"

```
