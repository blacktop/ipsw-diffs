## passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_dictobj`

```diff

-1696.2.9.0.0
-  __TEXT.__text: 0x605f7c
-  __TEXT.__auth_stubs: 0x7c70
-  __TEXT.__objc_stubs: 0x78920
-  __TEXT.__objc_methlist: 0x373bc
-  __TEXT.__const: 0x6518
-  __TEXT.__cstring: 0x69ad4
-  __TEXT.__objc_classname: 0x82d8
-  __TEXT.__objc_methtype: 0x14f92
-  __TEXT.__gcc_except_tab: 0x91b8
-  __TEXT.__objc_methname: 0xa96bc
-  __TEXT.__oslogstring: 0x5d7bb
+1696.3.2.0.0
+  __TEXT.__text: 0x60a93c
+  __TEXT.__auth_stubs: 0x7ca0
+  __TEXT.__objc_stubs: 0x78ce0
+  __TEXT.__objc_methlist: 0x3756c
+  __TEXT.__const: 0x6538
+  __TEXT.__cstring: 0x6ace4
+  __TEXT.__objc_classname: 0x8318
+  __TEXT.__objc_methtype: 0x14ff2
+  __TEXT.__gcc_except_tab: 0x9208
+  __TEXT.__objc_methname: 0xa9adc
+  __TEXT.__oslogstring: 0x5dd1b
   __TEXT.__ustring: 0x10
-  __TEXT.__swift5_typeref: 0x4490
-  __TEXT.__constg_swiftt: 0x27cc
-  __TEXT.__swift5_reflstr: 0x1af5
-  __TEXT.__swift5_fieldmd: 0x1bf0
+  __TEXT.__swift5_typeref: 0x4496
+  __TEXT.__constg_swiftt: 0x2808
+  __TEXT.__swift5_reflstr: 0x1b05
+  __TEXT.__swift5_fieldmd: 0x1c0c
   __TEXT.__swift5_builtin: 0x280
   __TEXT.__swift5_assocty: 0x438
   __TEXT.__swift5_capture: 0x1cb4
   __TEXT.__swift5_proto: 0x24c
-  __TEXT.__swift5_types: 0x244
+  __TEXT.__swift5_types: 0x248
   __TEXT.__swift_as_entry: 0xdc
   __TEXT.__swift_as_ret: 0x138
   __TEXT.__swift_as_cont: 0x1dc
   __TEXT.__swift5_protos: 0x38
   __TEXT.__swift5_mpenum: 0x40
-  __TEXT.__unwind_info: 0x1abf0
+  __TEXT.__unwind_info: 0x1ace0
   __TEXT.__eh_frame: 0x39a0
-  __DATA_CONST.__const: 0x33390
-  __DATA_CONST.__cfstring: 0x35920
-  __DATA_CONST.__objc_classlist: 0x1ad0
+  __DATA_CONST.__const: 0x334f8
+  __DATA_CONST.__cfstring: 0x35fc0
+  __DATA_CONST.__objc_classlist: 0x1ae0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x668
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x118
   __DATA_CONST.__objc_superrefs: 0xfc8
-  __DATA_CONST.__objc_intobj: 0x16f8
-  __DATA_CONST.__objc_arraydata: 0x728
+  __DATA_CONST.__objc_intobj: 0x1710
+  __DATA_CONST.__objc_arraydata: 0x730
   __DATA_CONST.__objc_dictobj: 0x2a8
-  __DATA_CONST.__objc_arrayobj: 0x6a8
+  __DATA_CONST.__objc_arrayobj: 0x6c0
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x3e48
-  __DATA_CONST.__got: 0x4a60
-  __DATA_CONST.__auth_ptr: 0xae0
-  __DATA.__objc_const: 0x45ab0
-  __DATA.__objc_selrefs: 0x21040
-  __DATA.__objc_ivar: 0x2b7c
-  __DATA.__objc_data: 0x12778
-  __DATA.__data: 0x81d0
+  __DATA_CONST.__auth_got: 0x3e60
+  __DATA_CONST.__got: 0x4a88
+  __DATA_CONST.__auth_ptr: 0xae8
+  __DATA.__objc_const: 0x45c60
+  __DATA.__objc_selrefs: 0x21130
+  __DATA.__objc_ivar: 0x2b8c
+  __DATA.__objc_data: 0x12888
+  __DATA.__data: 0x8200
   __DATA.__common: 0xc0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 29997
-  Symbols:   4444
-  CStrings:  36611
+  Functions: 30061
+  Symbols:   4451
+  CStrings:  36723
 
Symbols:
+ _OBJC_CLASS_$_DIIdentityProvisioningSession
+ _OBJC_CLASS_$_PKPassDateField
+ _PKDateForStringIgnoringTimeZone
+ _PKTransitCommutePlanGenericTimedPlanExpiryDateKey
+ _PKTransitCommutePlanGenericTimedPlanStartDateKey
+ __Z25PKLocalizedIdentityStringP8NSStringS0_z
+ _dispatch_walltime
CStrings:
+ "-[PDPaymentService generateIdentityPrearmTrustKeyMaterialForDeviceID:completion:]"
+ "@16@?0@\"PKTicket\"8"
+ "B16@?0@\"PKPaymentCommutePlanDetail\"8"
+ "B16@?0@\"PKTicket\"8"
+ "CREATE TABLE IF NOT EXISTS account_fetch_periods (pid INTEGER, blocked_endpoints TEXT, account_pid INTEGER, account_fetch_period INTEGER, extended_account_fetch_period INTEGER, a INTEGER, b INTEGER, c INTEGER, funding_sources_fetch_period INTEGER, recovery_payment_plans_fetch_period INTEGER, physical_cards_fetch_period INTEGER, migration_fetch_period INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS account_migration (pid INTEGER, account_pid INTEGER, messaging_pid INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS account_migration_action (pid INTEGER, message_pid INTEGER, title TEXT, action TEXT, url TEXT, order_index INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS account_migration_feature_unavailability (pid INTEGER, account_migration_pid INTEGER, identifier TEXT, start_date INTEGER, end_date INTEGER, alert_body TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS account_migration_message (pid INTEGER, title TEXT, body TEXT, dismissable BOOL, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS account_migration_messaging (pid INTEGER, phase TEXT, scheduled_date TEXT, expiration_date INTEGER, user_notification_pid INTEGER, application_message_pid INTEGER, dashboard_message_pid INTEGER, sheet_pid INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS account_payment_due_date (pid INTEGER, payment_due_date_info_pid INTEGER, type INTEGER, payment_due_day INTEGER, payment_due_date INTEGER, statement_open_date INTEGER, statement_close_date INTEGER, variable_amount_autopay_status INTEGER, variable_amount_autopay_restricted_days TEXT, fixed_amount_autopay_restricted_days TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS account_payment_due_date_info (pid INTEGER, account_identifier TEXT, eligible INTEGER, reason_code INTEGER, next_eligible_date INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS carambola (pid INTEGER, a INTEGER NOT NULL, b TEXT, c TEXT, d TEXT, e INTEGER, f INTEGER, g INTEGER, h INTEGER, i TEXT, activate_on_first_use INTEGER, is_activated INTEGER, pre_activation_message TEXT, active_ticket_end_date INTEGER, plan_type INTEGER, status INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS chrysalis (pid INTEGER, a TEXT NOT NULL, b TEXT NOT NULL, c INTEGER NOT NULL, d INTEGER NOT NULL, e INTEGER, f BLOB NOT NULL, g INTEGER NOT NULL, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS credit_account_interest_summary (pid INTEGER, credit_account_summary_pid INTEGER, block_finance_charges INTEGER, projected_unposted_interest INTEGER, projected_unposted_interest_timestamp INTEGER, interest_on_purchases INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS credit_account_interest_summary_balance (pid INTEGER, credit_account_interest_summary_pid INTEGER, sequence_id INTEGER, balance_amount INTEGER, apr INTEGER, projected_unposted_interest INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS feature_application_stored_field (pid INTEGER, application_pid INTEGER, field_identifier TEXT, submission_string TEXT, submission_key TEXT, submission_destination TEXT, odi_attribute TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS ice_cream_banana (pid INTEGER, a INTEGER, b TEXT, c TEXT, d TEXT, e INTEGER, f INTEGER, g INTEGER, h INTEGER, i TEXT, j TEXT, ticket_identifier TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS oranges (pid INTEGER, a INTEGER, b INTEGER, c INTEGER, d INTEGER, e INTEGER, f INTEGER, g INTEGER, h INTEGER, i INTEGER, j INTEGER, k INTEGER, l INTEGER, m INTEGER, n INTEGER, o INTEGER, p INTEGER, q INTEGER, r INTEGER, s INTEGER, t INTEGER, u INTEGER, recovery_payment_plans_supported INTEGER, remaining_statement_balance_for_interest_calculation INTEGER, projected_in_grace INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS payment_transaction (pid INTEGER, source_pid INTEGER, archive_pid INTEGER, identifier TEXT, service_identifier TEXT, payment_hash TEXT, payment_hash_component_1 TEXT, payment_hash_component_2 TEXT, currency_code TEXT, amount INTEGER, subtotal_amount INTEGER, locality TEXT, administrative_area TEXT, transaction_date INTEGER  NOT NULL, transaction_status_changed_date INTEGER, transaction_cleared_date INTEGER, location_date INTEGER, location_latitude REAL, location_longitude REAL, location_altitude REAL, location_horizontal_accuracy REAL, location_vertical_accuracy REAL, start_station_code BLOB, start_station TEXT, start_station_latitude REAL, start_station_longitude REAL, end_station_code BLOB, end_station TEXT, end_station_latitude REAL, end_station_longitude REAL, transaction_status INTEGER, transaction_type INTEGER, transit_type INTEGER, transit_modifiers INTEGER, en_route INTEGER, station_code_provider TEXT, city_code INTEGER, technology_type INTEGER, transaction_source INTEGER, requires_location INTEGER, has_notification_service_data INTEGER, processed_for_location INTEGER, processed_for_merchant_cleanup INTEGER, requires_merchant_reprocessing INTEGER, last_merchant_reprocessing_date INTEGER, processed_for_stations INTEGER, merchant_name TEXT, merchant_raw_name TEXT, merchant_industry_category TEXT, merchant_industry_code INTEGER, peer_payment_type INTEGER,peer_payment_counterpart_handle TEXT,peer_payment_memo TEXT,peer_payment_message_received_date INTEGER,account_type INTEGER,foreign_exchange_information_destination_currency_code TEXT,foreign_exchange_information_destination_amount INTEGER,foreign_exchange_information_exchange_rate TEXT,primary_funding_source_amount INTEGER,primary_funding_source_currency_code TEXT,secondary_funding_source_amount INTEGER,secondary_funding_source_currency_code TEXT,secondary_funding_source_network INTEGER,secondary_funding_source_dpan_suffix TEXT,secondary_funding_source_fpan_identifier TEXT,secondary_funding_source_description TEXT,secondary_funding_source_type INTEGER,request_device_score_identifier TEXT,send_device_score_identifier TEXT,device_score_identifiers_required INTEGER,device_score_identifiers_submitted INTEGER,merchant_provided_description TEXT,merchant_provided_title TEXT,metadata TEXT,expiration_date INTEGER,adjustment_type INTEGER,transaction_declined_reason INTEGER, a INTEGER, account_identifier TEXT, c INTEGER, d TEXT, e TEXT, f TEXT, g TEXT, h TEXT, i TEXT, j TEXT, k TEXT, l TEXT, m INTEGER, n INTEGER, o TEXT, should_suppress_date INTEGER, p TEXT, q INTEGER, r TEXT, s TEXT, t TEXT, maps_merchant_pid INTEGER, u INTEGER, v TEXT, w INTEGER, x INTEGER, y TEXT, ab TEXT, ac INTEGER, ad INTEGER, ae TEXT, af TEXT, ag TEXT, ah TEXT, use_raw_merchant_data INTEGER, issue_report_identifier TEXT, suppress_notifications INTEGER, fuzzy_matched INTEGER, receipt_provider_identifier TEXT, receipt_provider_url TEXT, receipt_identifier TEXT, barcode_identifier TEXT, payment_pin_format INTEGER, nonce BLOB, signing_key_material BLOB, partial_signature BLOB, requested_auth_mechanisms INTEGER, primary_funding_source_description TEXT, nominal_amount INTEGER, has_additional_offers BOOL, dpan_identifier TEXT, zm TEXT, eligible_eligible_rewards_percent_aggregate INTEGER, eligible_rewards_cash_aggregate INTEGER, is_coarse_location INTEGER, amount_added_to_auth INTEGER, afi INTEGER, is_merchant_token_transaction INTEGER, recurring BOOL, merchant_fallback_logo_image_url TEXT, interest_reassessment BOOL, associated_statement_identifiers TEXT, payment_network_identifier INTEGER, update_sequence_number INTEGER NOT NULL, needs_sync_to_finance INTEGER NOT NULL, ca INTEGER, iit INTEGER, iimu TEXT, cb TEXT, peer_payment_flow_type INTEGER, top_up_type INTEGER, preferred_category INTEGER, merchant_business_connect_brand_identifier TEXT, request_token TEXT, last_force_merchant_reprocessing_request_date INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS payment_transaction_amount (pid INTEGER, payment_transaction_pid INTEGER, label TEXT, currency TEXT, exponent INTEGER, amount INTEGER, preformatted_string TEXT, pending INTEGER DEFAULT 0, unit_identifier TEXT, unit_type INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS pineapples (pid INTEGER, a INTEGER, b TEXT, c INTEGER, d INTEGER, e INTEGER, f TEXT, g INTEGER, h INTEGER, i INTEGER, j INTEGER, k INTEGER, l INTEGER, m INTEGER, n INTEGER, o INTEGER, p INTEGER, q INTEGER, r INTEGER, s INTEGER, t TEXT, u INTEGER, v INTEGER, total_balance INTEGER, in_grace INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS plum (pid INTEGER, a INTEGER, b TEXT, c TEXT, d TEXT, e TEXT, f TEXT, g TEXT, pu TEXT, physical_cards TEXT, servicing_token TEXT, funding_sources TEXT, virtual_cards TEXT, recovery_payment_plans TEXT, migration TEXT, payment_due_dates TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS strawberries (pid INTEGER, a INTEGER, b TEXT, c INTEGER, d INTEGER, e TEXT, f TEXT, g INTEGER, h INTEGER, i INTEGER, j INTEGER, k TEXT, l TEXT, m TEXT, n INTEGER, o INTEGER, os_version_requirement_range BLOB, p INTEGER, q INTEGER, r TEXT, s INTEGER, savings_interest_rate INTEGER, savings_current_minimum_os_versions_pid INTEGER, savings_future_minimum_os_versions_pid INTEGER, minimum_date INTEGER, migration_type INTEGER, start_date INTEGER, effective_date INTEGER, old_issuer_closure_date INTEGER, old_issuer_identifier TEXT, new_issuer_identifier TEXT, learn_more_url TEXT, due_date_terms_identifier TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS ticket_state (pid INTEGER, pass_pid INTEGER NOT NULL, ticket_identifier TEXT NOT NULL, cns_snapshot BLOB, count_remaining INTEGER, count_reached_zero_date INTEGER, retired_date INTEGER, received_date INTEGER, local_state BLOB, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS water (pid INTEGER, a INTEGER, b TEXT, c TEXT, d INTEGER, e INTEGER, f INTEGER, PRIMARY KEY(pid));"
+ "CREATE TABLE IF NOT EXISTS whitney_rtc (pid INTEGER, a INTEGER, b INTEGER, c INTEGER, PRIMARY KEY (pid));"
+ "CREATE UNIQUE INDEX IF NOT EXISTS pending_pass_upgrade_index ON chrysalis (a, b);"
+ "CREATE UNIQUE INDEX IF NOT EXISTS ticket_state_index ON ticket_state (pass_pid, ticket_identifier);"
+ "CREATE UNIQUE INDEX IF NOT EXISTS whitney_rtc_index ON whitney_rtc (a, b);"
+ "Deleting ISO18013 credential with identifier: %@ deletionReason: %{public}@"
+ "Discarding the update for ticket %{private}@: its lastUpdatedDate %@ is older than the stored %@"
+ "Discarding the update for ticket %{private}@: pass %{private}@ has no ticket with that identifier"
+ "Failed to generate prearm trust for deviceID %@ with error: %@"
+ "Failed to generate prearm trust for deviceID %@. No target device."
+ "Migrating database from user_version 26070 to 26071"
+ "Migrating database from user_version 26071 to 26072"
+ "Migrating database from user_version 26072 to 26073"
+ "Migrating database from user_version 26073 to 26074"
+ "Migrating database from user_version 26074 to 26075"
+ "Migrating database from user_version 26075 to 26076"
+ "Migrating database from user_version 26076 to 26077"
+ "Migrating database from user_version 26077 to 26078"
+ "Migrating database from user_version 26078 to 26079"
+ "Migrating database from user_version 26079 to 26080"
+ "Missing prearm trust attestation data for secure element identifier %@"
+ "NOTIFICATION_ID_CARD_DYNAMIC_ID_INFO_CHANGE"
+ "NOTIFICATION_ID_CARD_DYNAMIC_INFO_CHANGE"
+ "NOTIFICATION_ID_CARD_DYNAMIC_PERSONAL_INFO_CHANGE"
+ "No prearm trust attestations (%@) found to match any secure element identifiers (%@) for the paired Watch with deviceID %@"
+ "Not creating pass %@ from download while provisioning is in progress."
+ "Not recreating pass %@ from download because provisioning removed it."
+ "PDARRCompanionPreArmTrustProvider: %s called on unsupported OS"
+ "PKFieldUnitTypeNone, PKFieldUnitTypeDefault, PKFieldUnitTypeRides, PKFieldUnitTypeTickets, PKFieldUnitTypeLoyaltyPoints, PKFieldUnitTypeCrossings, PKFieldUnitTypeJourneys, PKFieldUnitTypeExcursions"
+ "T@\"NSArray\",C,N,V_tickets"
+ "TicketState"
+ "UPDATE water SET f = 1 WHERE d = 1 AND e > 0"
+ "Unable to access DIPrearmTrustAttestation.casdCertificate for secure element identifier %@"
+ "Warning: generated prearm trust successfully for deviceID %@ but also received error: %@"
+ "_TtC5passd33PDARRCompanionPreArmTrustProvider"
+ "_migrateFrom26070To26071:context:"
+ "_migrateFrom26071To26072:context:"
+ "_migrateFrom26072To26073:context:"
+ "_migrateFrom26073To26074:context:"
+ "_migrateFrom26074To26075:context:"
+ "_migrateFrom26075To26076:context:"
+ "_migrateFrom26076To26077:context:"
+ "_migrateFrom26077To26078:context:"
+ "_migrateFrom26078To26079:context:"
+ "_migrateFrom26079To26080:context:"
+ "_noteRemovedDuringProvisioning:"
+ "_planUpdateDates"
+ "_removedDuringProvisioningLock"
+ "_schedulePlanUpdateForPassUniqueIdentifier:atNextBoundaryOfPlans:"
+ "_ticketStateForTicketIdentifier:pass:"
+ "_tickets"
+ "_uniqueIDsRemovedDuringProvisioning"
+ "_wasRemovedDuringProvisioning:"
+ "`"
+ "activate_on_first_use INTEGER"
+ "bundle-diff-cleanup"
+ "cns_snapshot"
+ "countRemaining"
+ "count_reached_zero_date"
+ "count_remaining"
+ "deleteCredentialsForCredentialIds:deletionReason:completion:"
+ "deleteSubCredentialIdentifiers:cardType:deletionReason:completion:"
+ "displayedPlans:forPassUniqueIdentifier:"
+ "due_date_terms_identifier TEXT"
+ "generateIdentityPrearmTrustKeyMaterialForDeviceID:completion:"
+ "generateKeyMaterial(for:context:completion:)"
+ "generatePrearmTrustWithDeviceID:completion:"
+ "getPassLocalizedStringsForKeys:uniqueID:handler:"
+ "in_grace INTEGER"
+ "isActivatedValue"
+ "isRegistered(for:context:completion:)"
+ "is_activated"
+ "is_activated INTEGER"
+ "migration TEXT"
+ "migration_fetch_period INTEGER"
+ "nextBoundaryDateForPlans:"
+ "pass-remove-generic"
+ "passLocalizedStringsForKeys:completion:"
+ "passWillBeRemoved:diagnosticReason:"
+ "passd.PDARRCompanionPreArmTrustProvider"
+ "payment_due_dates TEXT"
+ "plan_type INTEGER"
+ "pre_activation_message"
+ "pre_activation_message TEXT"
+ "projected_in_grace INTEGER"
+ "regionBySettingLastUpdatedTag:"
+ "requiresAppletSourceOfTruth"
+ "server-consistency-check"
+ "setIsActivatedValue:"
+ "setRetirementDate:"
+ "setTicketState:"
+ "setTickets:"
+ "status INTEGER"
+ "ticketIdentifier"
+ "ticket_identifier"
+ "ticket_identifier TEXT"
+ "ticket_state"
+ "tickets"
+ "transaction_cleared_date INTEGER"
+ "unit_type INTEGER"
+ "updateTicketStateWithEntry:forPassUniqueIdentifier:"
+ "v32@0:8@\"NSString\"16@?<v@?@\"PKAuxiliaryCapabilityRequirementKeyMaterial\"@\"NSError\">24"
+ "wallet-key-material-removal"
+ "\xf0\xf3"
- "CREATE TABLE IF NOT EXISTS account_fetch_periods (pid INTEGER, blocked_endpoints TEXT, account_pid INTEGER, account_fetch_period INTEGER, extended_account_fetch_period INTEGER, a INTEGER, b INTEGER, c INTEGER, funding_sources_fetch_period INTEGER, recovery_payment_plans_fetch_period INTEGER, physical_cards_fetch_period INTEGER, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS carambola (pid INTEGER, a INTEGER NOT NULL, b TEXT, c TEXT, d TEXT, e INTEGER, f INTEGER, g INTEGER, h INTEGER, i TEXT, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS ice_cream_banana (pid INTEGER, a INTEGER, b TEXT, c TEXT, d TEXT, e INTEGER, f INTEGER, g INTEGER, h INTEGER, i TEXT, j TEXT, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS oranges (pid INTEGER, a INTEGER, b INTEGER, c INTEGER, d INTEGER, e INTEGER, f INTEGER, g INTEGER, h INTEGER, i INTEGER, j INTEGER, k INTEGER, l INTEGER, m INTEGER, n INTEGER, o INTEGER, p INTEGER, q INTEGER, r INTEGER, s INTEGER, t INTEGER, u INTEGER, recovery_payment_plans_supported INTEGER, remaining_statement_balance_for_interest_calculation INTEGER, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS payment_transaction (pid INTEGER, source_pid INTEGER, archive_pid INTEGER, identifier TEXT, service_identifier TEXT, payment_hash TEXT, payment_hash_component_1 TEXT, payment_hash_component_2 TEXT, currency_code TEXT, amount INTEGER, subtotal_amount INTEGER, locality TEXT, administrative_area TEXT, transaction_date INTEGER  NOT NULL, transaction_status_changed_date INTEGER, location_date INTEGER, location_latitude REAL, location_longitude REAL, location_altitude REAL, location_horizontal_accuracy REAL, location_vertical_accuracy REAL, start_station_code BLOB, start_station TEXT, start_station_latitude REAL, start_station_longitude REAL, end_station_code BLOB, end_station TEXT, end_station_latitude REAL, end_station_longitude REAL, transaction_status INTEGER, transaction_type INTEGER, transit_type INTEGER, transit_modifiers INTEGER, en_route INTEGER, station_code_provider TEXT, city_code INTEGER, technology_type INTEGER, transaction_source INTEGER, requires_location INTEGER, has_notification_service_data INTEGER, processed_for_location INTEGER, processed_for_merchant_cleanup INTEGER, requires_merchant_reprocessing INTEGER, last_merchant_reprocessing_date INTEGER, processed_for_stations INTEGER, merchant_name TEXT, merchant_raw_name TEXT, merchant_industry_category TEXT, merchant_industry_code INTEGER, peer_payment_type INTEGER,peer_payment_counterpart_handle TEXT,peer_payment_memo TEXT,peer_payment_message_received_date INTEGER,account_type INTEGER,foreign_exchange_information_destination_currency_code TEXT,foreign_exchange_information_destination_amount INTEGER,foreign_exchange_information_exchange_rate TEXT,primary_funding_source_amount INTEGER,primary_funding_source_currency_code TEXT,secondary_funding_source_amount INTEGER,secondary_funding_source_currency_code TEXT,secondary_funding_source_network INTEGER,secondary_funding_source_dpan_suffix TEXT,secondary_funding_source_fpan_identifier TEXT,secondary_funding_source_description TEXT,secondary_funding_source_type INTEGER,request_device_score_identifier TEXT,send_device_score_identifier TEXT,device_score_identifiers_required INTEGER,device_score_identifiers_submitted INTEGER,merchant_provided_description TEXT,merchant_provided_title TEXT,metadata TEXT,expiration_date INTEGER,adjustment_type INTEGER,transaction_declined_reason INTEGER, a INTEGER, account_identifier TEXT, c INTEGER, d TEXT, e TEXT, f TEXT, g TEXT, h TEXT, i TEXT, j TEXT, k TEXT, l TEXT, m INTEGER, n INTEGER, o TEXT, should_suppress_date INTEGER, p TEXT, q INTEGER, r TEXT, s TEXT, t TEXT, maps_merchant_pid INTEGER, u INTEGER, v TEXT, w INTEGER, x INTEGER, y TEXT, ab TEXT, ac INTEGER, ad INTEGER, ae TEXT, af TEXT, ag TEXT, ah TEXT, use_raw_merchant_data INTEGER, issue_report_identifier TEXT, suppress_notifications INTEGER, fuzzy_matched INTEGER, receipt_provider_identifier TEXT, receipt_provider_url TEXT, receipt_identifier TEXT, barcode_identifier TEXT, payment_pin_format INTEGER, nonce BLOB, signing_key_material BLOB, partial_signature BLOB, requested_auth_mechanisms INTEGER, primary_funding_source_description TEXT, nominal_amount INTEGER, has_additional_offers BOOL, dpan_identifier TEXT, zm TEXT, eligible_eligible_rewards_percent_aggregate INTEGER, eligible_rewards_cash_aggregate INTEGER, is_coarse_location INTEGER, amount_added_to_auth INTEGER, afi INTEGER, is_merchant_token_transaction INTEGER, recurring BOOL, merchant_fallback_logo_image_url TEXT, interest_reassessment BOOL, associated_statement_identifiers TEXT, payment_network_identifier INTEGER, update_sequence_number INTEGER NOT NULL, needs_sync_to_finance INTEGER NOT NULL, ca INTEGER, iit INTEGER, iimu TEXT, cb TEXT, peer_payment_flow_type INTEGER, top_up_type INTEGER, preferred_category INTEGER, merchant_business_connect_brand_identifier TEXT, request_token TEXT, last_force_merchant_reprocessing_request_date INTEGER, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS payment_transaction_amount (pid INTEGER, payment_transaction_pid INTEGER, label TEXT, currency TEXT, exponent INTEGER, amount INTEGER, preformatted_string TEXT, pending INTEGER DEFAULT 0, unit_identifier TEXT, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS pineapples (pid INTEGER, a INTEGER, b TEXT, c INTEGER, d INTEGER, e INTEGER, f TEXT, g INTEGER, h INTEGER, i INTEGER, j INTEGER, k INTEGER, l INTEGER, m INTEGER, n INTEGER, o INTEGER, p INTEGER, q INTEGER, r INTEGER, s INTEGER, t TEXT, u INTEGER, v INTEGER, total_balance INTEGER, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS plum (pid INTEGER, a INTEGER, b TEXT, c TEXT, d TEXT, e TEXT, f TEXT, g TEXT, pu TEXT, physical_cards TEXT, servicing_token TEXT, funding_sources TEXT, virtual_cards TEXT, recovery_payment_plans TEXT, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS strawberries (pid INTEGER, a INTEGER, b TEXT, c INTEGER, d INTEGER, e TEXT, f TEXT, g INTEGER, h INTEGER, i INTEGER, j INTEGER, k TEXT, l TEXT, m TEXT, n INTEGER, o INTEGER, os_version_requirement_range BLOB, p INTEGER, q INTEGER, r TEXT, s INTEGER, savings_interest_rate INTEGER, savings_current_minimum_os_versions_pid INTEGER, savings_future_minimum_os_versions_pid INTEGER, minimum_date INTEGER, migration_type INTEGER, start_date INTEGER, effective_date INTEGER, old_issuer_closure_date INTEGER, old_issuer_identifier TEXT, new_issuer_identifier TEXT, learn_more_url TEXT, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS water (pid INTEGER, a INTEGER, b TEXT, c TEXT, d INTEGER, e INTEGER, PRIMARY KEY(pid));"
- "Deleting ISO18013 credential with identifier: %@"
- "PKFieldUnitTypeNone, PKFieldUnitTypeDefault, PKFieldUnitTypeRides, PKFieldUnitTypeTickets, PKFieldUnitTypeLoyaltyPoints"
- "Provisioning is in progress, deferring pass fetch for push topic %@."
- "deleteCredential:completion:"
- "deleteCredentialsForCredentialIds:completion:"
- "deleteSubCredentialIdentifiers:cardType:completion:"
- "\xf0\xd3"
```
