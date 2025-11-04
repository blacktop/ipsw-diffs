## passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

-1642.2.9.6.0
-  __TEXT.__text: 0x5dce90
-  __TEXT.__auth_stubs: 0x6e90
-  __TEXT.__objc_stubs: 0x71e00
-  __TEXT.__objc_methlist: 0x34d6c
+1642.3.2.0.0
+  __TEXT.__text: 0x5dd8d4
+  __TEXT.__auth_stubs: 0x6e80
+  __TEXT.__objc_stubs: 0x71ec0
+  __TEXT.__objc_methlist: 0x34dbc
   __TEXT.__const: 0x53b8
-  __TEXT.__cstring: 0x6456d
+  __TEXT.__cstring: 0x6470d
   __TEXT.__objc_classname: 0x713c
   __TEXT.__objc_methtype: 0x13424
-  __TEXT.__gcc_except_tab: 0xa378
-  __TEXT.__objc_methname: 0xa10e9
-  __TEXT.__oslogstring: 0x561fb
+  __TEXT.__gcc_except_tab: 0xa384
+  __TEXT.__objc_methname: 0xa11aa
+  __TEXT.__oslogstring: 0x5631b
   __TEXT.__ustring: 0x10
   __TEXT.__swift5_typeref: 0x3676
   __TEXT.__constg_swiftt: 0x1cd0

   __TEXT.__swift_as_ret: 0xc8
   __TEXT.__swift5_protos: 0x34
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x13680
+  __TEXT.__unwind_info: 0x13690
   __TEXT.__eh_frame: 0x3050
-  __DATA_CONST.__auth_got: 0x3758
+  __DATA_CONST.__auth_got: 0x3750
   __DATA_CONST.__got: 0x3e40
   __DATA_CONST.__auth_ptr: 0x940
-  __DATA_CONST.__const: 0x30218
-  __DATA_CONST.__cfstring: 0x33720
+  __DATA_CONST.__const: 0x30238
+  __DATA_CONST.__cfstring: 0x337e0
   __DATA_CONST.__objc_classlist: 0x1940
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x618

   __DATA_CONST.__objc_arrayobj: 0x6c0
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0x41d40
-  __DATA.__objc_selrefs: 0x1f948
+  __DATA.__objc_selrefs: 0x1f978
   __DATA.__objc_ivar: 0x29a8
   __DATA.__objc_data: 0x10f60
   __DATA.__data: 0x6ff0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A99694D6-643C-3849-8BB5-3076EE9678AD
-  Functions: 27961
-  Symbols:   3980
-  CStrings:  42145
+  UUID: 3D3175AC-7A34-3876-9E0E-B520A8728E4E
+  Functions: 27969
+  Symbols:   3979
+  CStrings:  42167
 
Symbols:
- _PKSecureElementAccessPassTypeToString
CStrings:
+ "Access activity signals event sent to RTC for collection interval: %@"
+ "CREATE TABLE IF NOT EXISTS account_minimum_os_versions (pid INTEGER, versions_pid INTEGER, is_device_eligible_for_upgrade BOOL, effective_date INTEGER, should_display_effective_date BOOL, ineligible_learn_more_url TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS pass (pid INTEGER, unique_id TEXT NOT NULL, pass_type_pid INTEGER NOT NULL, serial_number TEXT NOT NULL, sequence_counter INTEGER, organization_name TEXT, provisioning_credential_hash TEXT, relevant_date INTEGER, expiration_date INTEGER, signing_date INTEGER, voided INTEGER, user_info BLOB, template INTEGER, background_color TEXT, secondary_background_color TEXT, foreground_color TEXT, label_color TEXT, strip_color TEXT, tall_code INTEGER, has_background_image INTEGER, has_strip_image INTEGER, manifest_hash BLOB, web_service_pid INTEGER, push_registration_status INTEGER, push_registration_date INTEGER, authentication_token TEXT, last_modified_tag TEXT, ingested_date INTEGER, modified_date INTEGER, modified_source INTEGER, grouping_id TEXT, group_pid INTEGER, revoked INTEGER, share_count INTEGER, pass_transaction_service_pid INTEGER, pass_message_service_pid INTEGER, pass_flavor INTEGER, card_type INTEGER, identity_pass_type INTEGER, access_pass_type INTEGER, access_reporting_type TEXT, primary_account_identifier TEXT, primary_account_suffix TEXT, sanitized_pan TEXT, sharing_method INTEGER, sharing_url TEXT, sharing_text TEXT, supports_dpan_notifications INTEGER, supports_fpan_notifications INTEGER, supports_default_card_selection INTEGER, is_shell_pass INTEGER, supports_serial_number_based_provisioning INTEGER, requires_transfer_serial_number_based_provisioning INTEGER, has_stored_value INTEGER, contactless_activation_grouping_type INTEGER, pass_default_payment_application_pid INTEGER, cobranded INTEGER, low_balance_reminder_amount INTEGER, low_balance_reminder_currency TEXT, commute_plan_renewal_reminder_time_interval INTEGER, issuer_country_code TEXT, has_associated_peer_payment_account INTEGER, is_cloud_kit_archived INTEGER,cloud_kit_metadata BLOB,is_cloud_kit_securely_archived INTEGER,cloud_kit_secure_metadata BLOB,a TEXT,b INTEGER, c TEXT, transaction_source_pid INTEGER, d TEXT, e TEXT, mute_ready_for_use_notification INTEGER DEFAULT 0, live_render_background_type TEXT, f TEXT, g TEXT, shipping_address_seed TEXT, supports_issuer_binding INTEGER DEFAULT 0, original_provisioning_date INTEGER, live_rendering_requires_enablement INTEGER, transfer_url TEXT, sell_url TEXT, h TEXT, bag_policy_url TEXT, order_food_url TEXT, transit_information_url TEXT, parking_information_url TEXT, directions_information_url TEXT, merchandise_url TEXT, accessibility_url TEXT, purchase_parking_url TEXT, add_on_url TEXT, i TEXT, j TEXT, k TEXT, m TEXT, n TEXT, contact_venue_phone_number TEXT, contact_venue_email TEXT, contact_venue_website TEXT, p TEXT, q TEXT, r TEXT, supports_automatic_foreground_vibrancy INTEGER, supports_automatic_label_vibrancy INTEGER, footer_background_color TEXT, suppress_header_darkening INTEGER, s TEXT, t TEXT, u TEXT, v TEXT, w TEXT, PRIMARY KEY (pid));"
+ "Migrating database from user_version 26008 to 26009"
+ "Migrating database from user_version 26009 to 26010"
+ "Migrating database from user_version 26010 to 26011"
+ "Migrating database from user_version 26011 to 26012"
+ "PDCardFileManager: the user signed out of their iCloud, deleting all cards"
+ "T@\"NSString\",C,N,V_subtypeDescription"
+ "The next user activity signals for access was scheduled for: %@ "
+ "_migrateFrom26008To26009:context:"
+ "_migrateFrom26009To26010:context:"
+ "_migrateFrom26010To26011:context:"
+ "_migrateFrom26011To26012:context:"
+ "_nextMonthCollectionDateInterval"
+ "_nextMonthCollectionDateIntervalWithRandomOffset"
+ "access_reporting_type"
+ "access_reporting_type TEXT"
+ "account_minimum_os_versions"
+ "account_minimum_os_versions_configuration"
+ "deleteAllCardsDueToSignout"
+ "ineligible_learn_more_url TEXT"
+ "setAccessReportingType:"
- "Access activity signals event sent to RTC"
- "Access activity signals event sent to RTC, next collection interval: %@"
- "CREATE TABLE IF NOT EXISTS pass (pid INTEGER, unique_id TEXT NOT NULL, pass_type_pid INTEGER NOT NULL, serial_number TEXT NOT NULL, sequence_counter INTEGER, organization_name TEXT, provisioning_credential_hash TEXT, relevant_date INTEGER, expiration_date INTEGER, signing_date INTEGER, voided INTEGER, user_info BLOB, template INTEGER, background_color TEXT, secondary_background_color TEXT, foreground_color TEXT, label_color TEXT, strip_color TEXT, tall_code INTEGER, has_background_image INTEGER, has_strip_image INTEGER, manifest_hash BLOB, web_service_pid INTEGER, push_registration_status INTEGER, push_registration_date INTEGER, authentication_token TEXT, last_modified_tag TEXT, ingested_date INTEGER, modified_date INTEGER, modified_source INTEGER, grouping_id TEXT, group_pid INTEGER, revoked INTEGER, share_count INTEGER, pass_transaction_service_pid INTEGER, pass_message_service_pid INTEGER, pass_flavor INTEGER, card_type INTEGER, identity_pass_type INTEGER, access_pass_type INTEGER, primary_account_identifier TEXT, primary_account_suffix TEXT, sanitized_pan TEXT, sharing_method INTEGER, sharing_url TEXT, sharing_text TEXT, supports_dpan_notifications INTEGER, supports_fpan_notifications INTEGER, supports_default_card_selection INTEGER, is_shell_pass INTEGER, supports_serial_number_based_provisioning INTEGER, requires_transfer_serial_number_based_provisioning INTEGER, has_stored_value INTEGER, contactless_activation_grouping_type INTEGER, pass_default_payment_application_pid INTEGER, cobranded INTEGER, low_balance_reminder_amount INTEGER, low_balance_reminder_currency TEXT, commute_plan_renewal_reminder_time_interval INTEGER, issuer_country_code TEXT, has_associated_peer_payment_account INTEGER, is_cloud_kit_archived INTEGER,cloud_kit_metadata BLOB,is_cloud_kit_securely_archived INTEGER,cloud_kit_secure_metadata BLOB,a TEXT,b INTEGER, c TEXT, transaction_source_pid INTEGER, d TEXT, e TEXT, mute_ready_for_use_notification INTEGER DEFAULT 0, live_render_background_type TEXT, f TEXT, g TEXT, shipping_address_seed TEXT, supports_issuer_binding INTEGER DEFAULT 0, original_provisioning_date INTEGER, live_rendering_requires_enablement INTEGER, transfer_url TEXT, sell_url TEXT, h TEXT, bag_policy_url TEXT, order_food_url TEXT, transit_information_url TEXT, parking_information_url TEXT, directions_information_url TEXT, merchandise_url TEXT, accessibility_url TEXT, purchase_parking_url TEXT, add_on_url TEXT, i TEXT, j TEXT, k TEXT, m TEXT, n TEXT, contact_venue_phone_number TEXT, contact_venue_email TEXT, contact_venue_website TEXT, p TEXT, q TEXT, r TEXT, supports_automatic_foreground_vibrancy INTEGER, supports_automatic_label_vibrancy INTEGER, footer_background_color TEXT, suppress_header_darkening INTEGER, s TEXT, t TEXT, u TEXT, v TEXT, w TEXT, PRIMARY KEY (pid));"
- "Deleting all cards"
- "T@\"NSString\",N,V_subtypeDescription"
- "_collectionDateIntervalWithRandomOffsetMonthly"
- "deleteAllWithDiagnosticReason:"

```
