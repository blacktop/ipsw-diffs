## passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

-1642.3.3.0.0
-  __TEXT.__text: 0x5de258
+1642.3.5.0.0
+  __TEXT.__text: 0x5deae8
   __TEXT.__auth_stubs: 0x6e80
-  __TEXT.__objc_stubs: 0x71f00
-  __TEXT.__objc_methlist: 0x34e0c
+  __TEXT.__objc_stubs: 0x72000
+  __TEXT.__objc_methlist: 0x34e64
   __TEXT.__const: 0x53b8
-  __TEXT.__cstring: 0x6470d
+  __TEXT.__cstring: 0x64a4d
   __TEXT.__objc_classname: 0x713c
   __TEXT.__objc_methtype: 0x134bf
   __TEXT.__gcc_except_tab: 0xa384
-  __TEXT.__objc_methname: 0xa1393
-  __TEXT.__oslogstring: 0x5639b
+  __TEXT.__objc_methname: 0xa14a5
+  __TEXT.__oslogstring: 0x5653b
   __TEXT.__ustring: 0x10
   __TEXT.__swift5_typeref: 0x3676
   __TEXT.__constg_swiftt: 0x1cd0

   __TEXT.__unwind_info: 0x136a0
   __TEXT.__eh_frame: 0x3050
   __DATA_CONST.__auth_got: 0x3750
-  __DATA_CONST.__got: 0x3e40
+  __DATA_CONST.__got: 0x3e48
   __DATA_CONST.__auth_ptr: 0x940
-  __DATA_CONST.__const: 0x30238
-  __DATA_CONST.__cfstring: 0x337e0
+  __DATA_CONST.__const: 0x30230
+  __DATA_CONST.__cfstring: 0x33920
   __DATA_CONST.__objc_classlist: 0x1940
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x618

   __DATA_CONST.__objc_arrayobj: 0x6c0
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0x41d58
-  __DATA.__objc_selrefs: 0x1f9a0
+  __DATA.__objc_selrefs: 0x1f9e8
   __DATA.__objc_ivar: 0x29a8
   __DATA.__objc_data: 0x10f60
   __DATA.__data: 0x6ff0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 384D2740-E2A4-3093-AC71-92BF2BD9976B
-  Functions: 27975
-  Symbols:   3979
-  CStrings:  42177
+  UUID: 83AF055B-FBDB-3107-8563-9FF43C4BC06D
+  Functions: 27984
+  Symbols:   3980
+  CStrings:  42213
 
Symbols:
+ _PKPassSemanticDateKeyCurrentDepartureDate
CStrings:
+ "CREATE TABLE IF NOT EXISTS clementines (pid INTEGER, a INTEGER, b INTEGER, c TEXT, d TEXT, f INTEGER, g TEXT, h TEXT, i TEXT, j TEXT, k TEXT, l INTEGER, m TEXT, n INTEGER, o INTEGER, p INTEGER, business_chat_identifier TEXT, contact_number TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS cow (pid INTEGER, c_pid INTEGER, a TEXT, b INTEGER, c INTEGER, d TEXT, e TEXT, h TEXT, j TEXT, k INTEGER, l INTEGER, m TEXT, r TEXT, s TEXT, t TEXT, u TEXT, v TEXT, w INTEGER, x TEXT, y BOOL, z TEXT, aa TEXT, ab TEXT, localized_pay_in_full_subtitle_override TEXT, has_preconfigured_offers TEXT, has_default_plan BOOL, instore_capabilities TEXT, is_handoff BOOL, requires_in_store_plan_selection BOOL, merchandising_identifier TEXT, setup_after_purchase_sticky_duration INTEGER, setup_after_purchase_active_duration INTEGER, supports_payment_status BOOL, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS cowboy (pid INTEGER, c_pid INTEGER, a TEXT, b INTEGER, c INTEGER, d TEXT, e TEXT, f TEXT, h TEXT, i TEXT, ma BOOL, mb BOOL, instore_capabilities TEXT, selected_offer_sticky_duration INTEGER, selected_offer_active_duration INTEGER, supported_merchant_country_codes TEXT, supports_payment_status BOOL, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS pass (pid INTEGER, unique_id TEXT NOT NULL, pass_type_pid INTEGER NOT NULL, serial_number TEXT NOT NULL, sequence_counter INTEGER, organization_name TEXT, provisioning_credential_hash TEXT, relevant_date INTEGER, expiration_date INTEGER, signing_date INTEGER, voided INTEGER, user_info BLOB, template INTEGER, background_color TEXT, secondary_background_color TEXT, foreground_color TEXT, label_color TEXT, strip_color TEXT, tall_code INTEGER, has_background_image INTEGER, has_strip_image INTEGER, manifest_hash BLOB, web_service_pid INTEGER, push_registration_status INTEGER, push_registration_date INTEGER, authentication_token TEXT, last_modified_tag TEXT, ingested_date INTEGER, modified_date INTEGER, modified_source INTEGER, grouping_id TEXT, group_pid INTEGER, revoked INTEGER, share_count INTEGER, pass_transaction_service_pid INTEGER, pass_message_service_pid INTEGER, pass_flavor INTEGER, card_type INTEGER, identity_pass_type INTEGER, access_pass_type INTEGER, access_reporting_type TEXT, primary_account_identifier TEXT, primary_account_suffix TEXT, sanitized_pan TEXT, sharing_method INTEGER, sharing_url TEXT, sharing_text TEXT, supports_dpan_notifications INTEGER, supports_fpan_notifications INTEGER, supports_default_card_selection INTEGER, is_shell_pass INTEGER, supports_serial_number_based_provisioning INTEGER, requires_transfer_serial_number_based_provisioning INTEGER, has_stored_value INTEGER, contactless_activation_grouping_type INTEGER, pass_default_payment_application_pid INTEGER, cobranded INTEGER, low_balance_reminder_amount INTEGER, low_balance_reminder_currency TEXT, commute_plan_renewal_reminder_time_interval INTEGER, issuer_country_code TEXT, has_associated_peer_payment_account INTEGER, is_cloud_kit_archived INTEGER,cloud_kit_metadata BLOB,is_cloud_kit_securely_archived INTEGER,cloud_kit_secure_metadata BLOB,a TEXT,b INTEGER, c TEXT, transaction_source_pid INTEGER, d TEXT, e TEXT, mute_ready_for_use_notification INTEGER DEFAULT 0, live_render_background_type TEXT, f TEXT, g TEXT, shipping_address_seed TEXT, supports_issuer_binding INTEGER DEFAULT 0, original_provisioning_date INTEGER, live_rendering_requires_enablement INTEGER, transfer_url TEXT, sell_url TEXT, h TEXT, bag_policy_url TEXT, order_food_url TEXT, transit_information_url TEXT, parking_information_url TEXT, directions_information_url TEXT, merchandise_url TEXT, accessibility_url TEXT, purchase_parking_url TEXT, add_on_url TEXT, i TEXT, j TEXT, k TEXT, l TEXT, m TEXT, n TEXT, contact_venue_phone_number TEXT, contact_venue_email TEXT, contact_venue_website TEXT, p TEXT, q TEXT, r TEXT, supports_automatic_foreground_vibrancy INTEGER, supports_automatic_label_vibrancy INTEGER, footer_background_color TEXT, suppress_header_darkening INTEGER, s TEXT, t TEXT, u TEXT, v TEXT, w TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS payment_offer_capability (pid INTEGER, catalog_pid INTEGER, fpan_identifier TEXT, pass_serial_number TEXT, pass_type_identifier TEXT, features TEXT, merchandising_identifier TEXT, balance_institution_identifier TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS payment_transaction_question (pid INTEGER, payment_transaction_pid INTEGER, type INTEGER, expiration_date INTEGER, answered INTEGER, answered_on_device INTEGER, answer TEXT, message_dismissed INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS strawberries (pid INTEGER, a INTEGER, b TEXT, c INTEGER, d INTEGER, e TEXT, f TEXT, g INTEGER, h INTEGER, i INTEGER, j INTEGER, k TEXT, l TEXT, m TEXT, n INTEGER, o INTEGER, os_version_requirement_range BLOB, p INTEGER, q INTEGER, r TEXT, s INTEGER, savings_interest_rate INTEGER, savings_current_minimum_os_versions_pid INTEGER, savings_future_minimum_os_versions_pid INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS user_notification_receipt (pid INTEGER, notification_identifier TEXT, account_identifier TEXT, message_title TEXT, message_subtitle TEXT, message_body TEXT, date_scheduled INTEGER, scheduled_time_zone TEXT, date_delivered INTEGER, delivered_time_zone TEXT, PRIMARY KEY(pid));"
+ "Migrating database from user_version 26012 to 26013"
+ "Migrating database from user_version 26013 to 26014"
+ "Migrating database from user_version 26014 to 26015"
+ "Migrating database from user_version 26015 to 26016"
+ "Migrating database from user_version 26016 to 26017"
+ "Migrating database from user_version 26017 to 26018"
+ "Migrating database from user_version 26018 to 26019"
+ "Migrating database from user_version 26019 to 26020"
+ "_migrateFrom26012To26013:context:"
+ "_migrateFrom26013To26014:context:"
+ "_migrateFrom26014To26015:context:"
+ "_migrateFrom26015To26016:context:"
+ "_migrateFrom26016To26017:context:"
+ "_migrateFrom26017To26018:context:"
+ "_migrateFrom26018To26019:context:"
+ "_migrateFrom26019To26020:context:"
+ "_relevantDateForBoardingPass:"
+ "balance_institution_identifier TEXT"
+ "business_chat_identifier TEXT"
+ "contact_number TEXT"
+ "delivered_time_zone TEXT"
+ "message_dismissed INTEGER"
+ "savings_current_minimum_os_versions_pid INTEGER"
+ "savings_future_minimum_os_versions_pid INTEGER"
+ "scheduled_time_zone TEXT"
+ "setStandbyListURL:"
+ "supports_payment_status BOOL"
- "B32@?0@\"PKFlight\"8Q16^B24"
- "CREATE TABLE IF NOT EXISTS clementines (pid INTEGER, a INTEGER, b INTEGER, c TEXT, d TEXT, f INTEGER, g TEXT, h TEXT, i TEXT, j TEXT, k TEXT, l INTEGER, m TEXT, n INTEGER, o INTEGER, p INTEGER, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS cow (pid INTEGER, c_pid INTEGER, a TEXT, b INTEGER, c INTEGER, d TEXT, e TEXT, h TEXT, j TEXT, k INTEGER, l INTEGER, m TEXT, r TEXT, s TEXT, t TEXT, u TEXT, v TEXT, w INTEGER, x TEXT, y BOOL, z TEXT, aa TEXT, ab TEXT, localized_pay_in_full_subtitle_override TEXT, has_preconfigured_offers TEXT, has_default_plan BOOL, instore_capabilities TEXT, is_handoff BOOL, requires_in_store_plan_selection BOOL, merchandising_identifier TEXT, setup_after_purchase_sticky_duration INTEGER, setup_after_purchase_active_duration INTEGER, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS cowboy (pid INTEGER, c_pid INTEGER, a TEXT, b INTEGER, c INTEGER, d TEXT, e TEXT, f TEXT, h TEXT, i TEXT, ma BOOL, mb BOOL, instore_capabilities TEXT, selected_offer_sticky_duration INTEGER, selected_offer_active_duration INTEGER, supported_merchant_country_codes TEXT, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS pass (pid INTEGER, unique_id TEXT NOT NULL, pass_type_pid INTEGER NOT NULL, serial_number TEXT NOT NULL, sequence_counter INTEGER, organization_name TEXT, provisioning_credential_hash TEXT, relevant_date INTEGER, expiration_date INTEGER, signing_date INTEGER, voided INTEGER, user_info BLOB, template INTEGER, background_color TEXT, secondary_background_color TEXT, foreground_color TEXT, label_color TEXT, strip_color TEXT, tall_code INTEGER, has_background_image INTEGER, has_strip_image INTEGER, manifest_hash BLOB, web_service_pid INTEGER, push_registration_status INTEGER, push_registration_date INTEGER, authentication_token TEXT, last_modified_tag TEXT, ingested_date INTEGER, modified_date INTEGER, modified_source INTEGER, grouping_id TEXT, group_pid INTEGER, revoked INTEGER, share_count INTEGER, pass_transaction_service_pid INTEGER, pass_message_service_pid INTEGER, pass_flavor INTEGER, card_type INTEGER, identity_pass_type INTEGER, access_pass_type INTEGER, access_reporting_type TEXT, primary_account_identifier TEXT, primary_account_suffix TEXT, sanitized_pan TEXT, sharing_method INTEGER, sharing_url TEXT, sharing_text TEXT, supports_dpan_notifications INTEGER, supports_fpan_notifications INTEGER, supports_default_card_selection INTEGER, is_shell_pass INTEGER, supports_serial_number_based_provisioning INTEGER, requires_transfer_serial_number_based_provisioning INTEGER, has_stored_value INTEGER, contactless_activation_grouping_type INTEGER, pass_default_payment_application_pid INTEGER, cobranded INTEGER, low_balance_reminder_amount INTEGER, low_balance_reminder_currency TEXT, commute_plan_renewal_reminder_time_interval INTEGER, issuer_country_code TEXT, has_associated_peer_payment_account INTEGER, is_cloud_kit_archived INTEGER,cloud_kit_metadata BLOB,is_cloud_kit_securely_archived INTEGER,cloud_kit_secure_metadata BLOB,a TEXT,b INTEGER, c TEXT, transaction_source_pid INTEGER, d TEXT, e TEXT, mute_ready_for_use_notification INTEGER DEFAULT 0, live_render_background_type TEXT, f TEXT, g TEXT, shipping_address_seed TEXT, supports_issuer_binding INTEGER DEFAULT 0, original_provisioning_date INTEGER, live_rendering_requires_enablement INTEGER, transfer_url TEXT, sell_url TEXT, h TEXT, bag_policy_url TEXT, order_food_url TEXT, transit_information_url TEXT, parking_information_url TEXT, directions_information_url TEXT, merchandise_url TEXT, accessibility_url TEXT, purchase_parking_url TEXT, add_on_url TEXT, i TEXT, j TEXT, k TEXT, m TEXT, n TEXT, contact_venue_phone_number TEXT, contact_venue_email TEXT, contact_venue_website TEXT, p TEXT, q TEXT, r TEXT, supports_automatic_foreground_vibrancy INTEGER, supports_automatic_label_vibrancy INTEGER, footer_background_color TEXT, suppress_header_darkening INTEGER, s TEXT, t TEXT, u TEXT, v TEXT, w TEXT, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS payment_transaction_question (pid INTEGER, payment_transaction_pid INTEGER, type INTEGER, expiration_date INTEGER, answered INTEGER, answered_on_device INTEGER, answer TEXT, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS strawberries (pid INTEGER, a INTEGER, b TEXT, c INTEGER, d INTEGER, e TEXT, f TEXT, g INTEGER, h INTEGER, i INTEGER, j INTEGER, k TEXT, l TEXT, m TEXT, n INTEGER, o INTEGER, os_version_requirement_range BLOB, p INTEGER, q INTEGER, r TEXT, s INTEGER, savings_interest_rate INTEGER, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS user_notification_receipt (pid INTEGER, notification_identifier TEXT, account_identifier TEXT, message_title TEXT, message_subtitle TEXT, message_body TEXT, date_scheduled INTEGER, date_delivered INTEGER, PRIMARY KEY(pid));"
- "relevantSharedFlights"
- "startActivitiesForSharedFlightsIfNeeded"

```
