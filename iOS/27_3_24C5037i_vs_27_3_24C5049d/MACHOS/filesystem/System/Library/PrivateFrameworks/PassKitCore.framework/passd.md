## passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-1696.3.2.0.0
-  __TEXT.__text: 0x60a93c
-  __TEXT.__auth_stubs: 0x7ca0
-  __TEXT.__objc_stubs: 0x78ce0
-  __TEXT.__objc_methlist: 0x3756c
-  __TEXT.__const: 0x6538
-  __TEXT.__cstring: 0x6ace4
-  __TEXT.__objc_classname: 0x8318
+1696.3.5.4.0
+  __TEXT.__text: 0x60e7fc
+  __TEXT.__auth_stubs: 0x7d40
+  __TEXT.__objc_stubs: 0x790c0
+  __TEXT.__objc_methlist: 0x3770c
+  __TEXT.__const: 0x6548
+  __TEXT.__cstring: 0x6b7c4
+  __TEXT.__objc_classname: 0x8338
   __TEXT.__objc_methtype: 0x14ff2
-  __TEXT.__gcc_except_tab: 0x9208
-  __TEXT.__objc_methname: 0xa9adc
-  __TEXT.__oslogstring: 0x5dd1b
+  __TEXT.__gcc_except_tab: 0x9654
+  __TEXT.__objc_methname: 0xaa18c
+  __TEXT.__oslogstring: 0x5e11b
   __TEXT.__ustring: 0x10
   __TEXT.__swift5_typeref: 0x4496
   __TEXT.__constg_swiftt: 0x2808

   __TEXT.__swift_as_cont: 0x1dc
   __TEXT.__swift5_protos: 0x38
   __TEXT.__swift5_mpenum: 0x40
-  __TEXT.__unwind_info: 0x1ace0
+  __TEXT.__unwind_info: 0x1adc8
   __TEXT.__eh_frame: 0x39a0
-  __DATA_CONST.__const: 0x334f8
-  __DATA_CONST.__cfstring: 0x35fc0
-  __DATA_CONST.__objc_classlist: 0x1ae0
+  __DATA_CONST.__const: 0x33c80
+  __DATA_CONST.__cfstring: 0x364a0
+  __DATA_CONST.__objc_classlist: 0x1ae8
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x668
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x118
-  __DATA_CONST.__objc_superrefs: 0xfc8
-  __DATA_CONST.__objc_intobj: 0x1710
-  __DATA_CONST.__objc_arraydata: 0x730
+  __DATA_CONST.__objc_superrefs: 0xfd0
+  __DATA_CONST.__objc_intobj: 0x1728
+  __DATA_CONST.__objc_arraydata: 0x7d0
   __DATA_CONST.__objc_dictobj: 0x2a8
-  __DATA_CONST.__objc_arrayobj: 0x6c0
+  __DATA_CONST.__objc_arrayobj: 0x750
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x3e60
-  __DATA_CONST.__got: 0x4a88
+  __DATA_CONST.__auth_got: 0x3eb0
+  __DATA_CONST.__got: 0x4ad0
   __DATA_CONST.__auth_ptr: 0xae8
-  __DATA.__objc_const: 0x45c60
-  __DATA.__objc_selrefs: 0x21130
-  __DATA.__objc_ivar: 0x2b8c
-  __DATA.__objc_data: 0x12888
+  __DATA.__objc_const: 0x45de0
+  __DATA.__objc_selrefs: 0x21240
+  __DATA.__objc_ivar: 0x2b9c
+  __DATA.__objc_data: 0x128d8
   __DATA.__data: 0x8200
   __DATA.__common: 0xc0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 30061
-  Symbols:   4451
-  CStrings:  36723
+  Functions: 30123
+  Symbols:   4469
+  CStrings:  36821
 
Symbols:
+ _OBJC_CLASS_$_CSDonationProgress
+ _OBJC_CLASS_$_PKCampaignAttributionSessionManager
+ _PKAnalyticsReporterAttributionAddLocalPendingCardReadyToUse
+ _PKAnalyticsReporterAttributionFetchNewToStatuses
+ _PKAnalyticsReporterAttributionSetLocalNewToStatusProvider
+ _PKAnalyticsReporterAttributionSetLocalPendingCardReadyToUseAddedHandler
+ _PKPassUniqueIdentifiersWithPendingCampaignAttribution
+ _PKPendingCampaignAttributionCampaignIdentifierKey
+ _PKPendingCampaignAttributionForPassUniqueIdentifier
+ _PKPendingCampaignAttributionNewToProductUserKey
+ _PKPendingCampaignAttributionNewToWalletUserKey
+ _PKPendingCampaignAttributionProductTypeKey
+ _PKPendingCampaignAttributionQueue
+ _PKPendingCampaignAttributionReferralSourceKey
+ _PKPendingCampaignAttributionSessionIDKey
+ _PKRemoveExpiredPendingCampaignAttributions
+ _PKRemovePendingCampaignAttributionForPassUniqueIdentifier
+ _PKTouchIDIsAvailable
+ _os_unfair_recursive_lock_lock
- _os_unfair_recursive_lock_lock_with_options
CStrings:
+ "B32@?0@\"NSString\"8@\"PDUserNotification\"16^B24"
+ "CREATE INDEX IF NOT EXISTS dragonfruit_b_c_index ON dragonfruit (b, c);"
+ "CREATE INDEX IF NOT EXISTS pass_brands_index ON pass_brands (pass_pid);"
+ "CREATE INDEX IF NOT EXISTS tangerine_b_index ON tangerine (b);"
+ "CREATE TABLE IF NOT EXISTS account_migration (pid INTEGER, account_pid INTEGER, messaging_pid INTEGER, migration_effective_date INTEGER, learn_more_url TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS account_migration_feature_unavailability (pid INTEGER, account_migration_pid INTEGER, identifier TEXT, start_date INTEGER, end_date INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS account_migration_messaging (pid INTEGER, phase TEXT, scheduled_date TEXT, expiration_date INTEGER, user_notification_pid INTEGER, application_message_pid INTEGER, dashboard_message_pid INTEGER, sheet_pid INTEGER, notification_scheduled_date TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS account_payment_due_date (pid INTEGER, payment_due_date_info_pid INTEGER, type INTEGER, payment_due_day INTEGER, payment_due_date INTEGER, statement_open_date INTEGER, statement_close_date INTEGER, autopay_status INTEGER, variable_amount_autopay_restricted_days TEXT, fixed_amount_autopay_restricted_days TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS blueberry (pid INTEGER, a INTEGER NOT NULL, b TEXT NOT NULL, c INTEGER, d TEXT, e TEXT, f TEXT, g TEXT, h TEXT, i INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS clementines (pid INTEGER, a INTEGER, b INTEGER, c TEXT, d TEXT, f INTEGER, g TEXT, h TEXT, i TEXT, j TEXT, k TEXT, l INTEGER, m TEXT, n INTEGER, o INTEGER, p INTEGER, business_chat_identifier TEXT, contact_number TEXT, privacy_policy_url TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS dragonfruit (pid INTEGER, a TEXT NOT NULL, b INTEGER NOT NULL, c TEXT NOT NULL, d INTEGER NOT NULL, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS issuer_messaging_flag (pid INTEGER, identifier TEXT, name TEXT, context_type INTEGER, context_identifier TEXT, context_feature INTEGER, expiration_date INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS leek (pid INTEGER, base_pid INTEGER, a TEXT, b TEXT, c TEXT, d INTEGER, e TEXT, f TEXT, g TEXT, h TEXT, k TEXT, l INTEGER, m INTEGER, n TEXT, o TEXT, p TEXT, q INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS pass_brands (pid INTEGER, pass_pid INTEGER, brand_identifier INTEGER NOT NULL, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS pears (pid INTEGER, a TEXT, b INTEGER, c INTEGER, d INTEGER, e INTEGER, f INTEGER, g INTEGER, h TEXT, i INTEGER, j INTEGER, cloud_store_zone_names TEXT, k TEXT, l INTEGER, m TEXT, n TEXT, o TEXT, p INTEGER, transaction_source_pid INTEGER, block_all_account_access INTEGER, current_minimum_os_versions_pid INTEGER, future_minimum_os_versions_pid INTEGER, issuer_identifier TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS rhubarb (pid INTEGER, a INTEGER, b TEXT, c INTEGER, d INTEGER, e TEXT, f TEXT, g INTEGER, h INTEGER, i INTEGER, j TEXT, k TEXT, l TEXT, m INTEGER, n BOOL, q BOOL, r BOOL, s BOOL, t BOOL, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS strawberries (pid INTEGER, a INTEGER, b TEXT, c INTEGER, d INTEGER, e TEXT, f TEXT, g INTEGER, h INTEGER, i INTEGER, j INTEGER, k TEXT, l TEXT, m TEXT, n INTEGER, o INTEGER, os_version_requirement_range BLOB, p INTEGER, q INTEGER, r TEXT, s INTEGER, savings_interest_rate INTEGER, savings_current_minimum_os_versions_pid INTEGER, savings_future_minimum_os_versions_pid INTEGER, minimum_date INTEGER, due_date_terms_identifier TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS tangerine (a INTEGER NOT NULL REFERENCES dragonfruit(pid) ON DELETE CASCADE, b INTEGER NOT NULL REFERENCES blueberry(pid) ON DELETE CASCADE, PRIMARY KEY (a, b));"
+ "CREATE TABLE IF NOT EXISTS user_notification_receipt (pid INTEGER, notification_identifier TEXT, notification_type TEXT, account_identifier TEXT, account_base_url TEXT, message_title TEXT, message_subtitle TEXT, message_body TEXT, date_scheduled INTEGER, scheduled_time_zone TEXT, date_delivered INTEGER, delivered_time_zone TEXT, date_reported INTEGER, requires_reporting INTEGER, PRIMARY KEY(pid));"
+ "CREATE UNIQUE INDEX IF NOT EXISTS blueberry_a_b_index ON blueberry (a, b);"
+ "CREATE UNIQUE INDEX IF NOT EXISTS dragonfruit_a_index ON dragonfruit (a);"
+ "Convenience"
+ "Could not report donation progress with error %@"
+ "DROP TABLE IF EXISTS account_service_unavailable_period;"
+ "Ignoring expired issuer messaging flag %@ - expired %@"
+ "Indexing %lu items (%lu transactions/ %lu passes / %lu accounts / %lu payment setup products / %lu FinanceKit Transactions/ %lu FinanceKit Accounts), donation progress: %lu known / %lu needing donation / %lu donated, partial: %@"
+ "Migrating database from user_version 26080 to 26081"
+ "Migrating database from user_version 26081 to 26082"
+ "Migrating database from user_version 26082 to 26083"
+ "Migrating database from user_version 26083 to 26084"
+ "Migrating database from user_version 26084 to 26085"
+ "Migrating database from user_version 26085 to 26086"
+ "Migrating database from user_version 26086 to 26087"
+ "Migrating database from user_version 26087 to 26088"
+ "Migrating database from user_version 26088 to 26089"
+ "Notification for this type is inflight, so delivery is not allowed. delivered notification: %@ suppressed notification: %@"
+ "Notification for this type was delivered on the same calendar day, so delivery is not allowed. delivered receipt: %@ suppressed notification: %@"
+ "Reporting donation progress: %lu known / %lu needing donation / %lu donated, partial: %@"
+ "SpotlightIndexerItemDonationCounts"
+ "T@\"NSDate\",R,N,V_newestUndonatedItemDate"
+ "TQ,R,N,V_donatedCount"
+ "TQ,R,N,V_needingDonationCount"
+ "UPDATE user_notification_receipt SET notification_type = 'PDUserNotificationTypeAccountPaymentPastDue' WHERE notification_identifier LIKE 'accountPaymentPastDue-%'"
+ "UPDATE user_notification_receipt SET notification_type = 'PDUserNotificationTypePassAccountState' WHERE notification_identifier LIKE 'accountStateChange-%'"
+ "UPDATE user_notification_receipt SET requires_reporting = 1"
+ "[Test Receipt] Past Due Body"
+ "[Test Receipt] Past Due Subtitle"
+ "[Test Receipt] Past Due Title"
+ "_donatedCount"
+ "_hasCampaignAttributionAccess"
+ "_migrateFrom26080To26081:context:"
+ "_migrateFrom26081To26082:context:"
+ "_migrateFrom26082To26083:context:"
+ "_migrateFrom26083To26084:context:"
+ "_migrateFrom26084To26085:context:"
+ "_migrateFrom26085To26086:context:"
+ "_migrateFrom26086To26087:context:"
+ "_migrateFrom26087To26088:context:"
+ "_migrateFrom26088To26089:context:"
+ "_needingDonationCount"
+ "_newestUndonatedItemDate"
+ "_notificationDeliveryAllowed:"
+ "_pendingCampaignAttributionQueue"
+ "_predicateForPurgeableBeforeDate:"
+ "_queue_donationProgressAdjustingForIndexedCount:"
+ "_queue_isDiscoveringItemsToIndex"
+ "_reportDonationProgress"
+ "account_migration"
+ "account_migration_feature_unavailability"
+ "account_migration_messaging"
+ "account_payment_due_date"
+ "addPendingCampaignAttribution:forPassUniqueIdentifier:"
+ "alert_body"
+ "allKnownItems"
+ "allKnownItemsIsPartial"
+ "autopay_status"
+ "campaignAttributionNewToStatuses"
+ "campaignAttributionNewToStatusesWithHandler:"
+ "deletePurgeableReceiptsBeforeDate:"
+ "deletePurgeableReceiptsBeforeDate:inDatabase:"
+ "donatedCount"
+ "donatedItems"
+ "donationCountsOfTypes:newestUndonatedDateStatuses:inDatabase:"
+ "indexSearchableItems:updatingDonationProgress:completionHandler:"
+ "indexerItemDonationCountsOfTypes:newestUndonatedDateStatuses:"
+ "initWithAllKnownItems:itemsNeedingDonation:donatedItems:partiallyDonatedItems:itemsNeedingDonationForRedonationRequests:dateOfNewestUndonatedItem:allKnownItemsIsPartial:"
+ "initWithNeedingDonationCount:donatedCount:newestUndonatedItemDate:"
+ "initWithNotificationIdentifier:notificationType:accountIdentifier:accountBaseURL:requiresReporting:"
+ "insertUserNotificationReceiptForAccountIdentifier:deliveredDate:"
+ "itemsNeedingDonation"
+ "learn_more_url"
+ "migration_effective_date INTEGER"
+ "migration_type"
+ "needingDonationCount"
+ "new_issuer_identifier"
+ "newestUndonatedItemDate"
+ "notification_scheduled_date TEXT"
+ "notification_type TEXT"
+ "old_issuer_closure_date"
+ "old_issuer_identifier"
+ "preventMultipleSameDayDelivery"
+ "privacy_policy_url TEXT"
+ "reportCampaignIdentifier:eventType:referralSource:deepLinkType:productType:newToWalletUser:newToProductUser:sessionIdentifier:"
+ "reportDonationProgress:completionHandler:"
+ "requiresReporting"
+ "requires_reporting"
+ "requires_reporting INTEGER"
+ "setRequiresFullscreenPresentationWhenTargetAppIsResizable:"
+ "setRequiresReporting:"
+ "userNotificationReceiptsForNotificationType:"
+ "v32@0:8@\"NSDictionary\"16@\"NSString\"24"
+ "v32@?0@\"NSString\"8#16^B24"
+ "variable_amount_autopay_status"
+ "{os_unfair_recursive_lock_s=\"_os_unfair_recursive_lock_opaque\"[2I]}"
+ "\xf0\xf0\x81"
- "CREATE TABLE IF NOT EXISTS account_service_unavailable_period (pid INTEGER, reason INTEGER, start_date INTEGER, unavailable_feature_identifiers TEXT, learn_more_url TEXT, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS clementines (pid INTEGER, a INTEGER, b INTEGER, c TEXT, d TEXT, f INTEGER, g TEXT, h TEXT, i TEXT, j TEXT, k TEXT, l INTEGER, m TEXT, n INTEGER, o INTEGER, p INTEGER, business_chat_identifier TEXT, contact_number TEXT, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS leek (pid INTEGER, base_pid INTEGER, a TEXT, b TEXT, c TEXT, d INTEGER, e TEXT, f TEXT, g TEXT, h TEXT, k TEXT, l INTEGER, m INTEGER, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS pears (pid INTEGER, a TEXT, b INTEGER, c INTEGER, d INTEGER, e INTEGER, f INTEGER, g INTEGER, h TEXT, i INTEGER, j INTEGER, cloud_store_zone_names TEXT, k TEXT, l INTEGER, m TEXT, n TEXT, o TEXT, p INTEGER, transaction_source_pid INTEGER, block_all_account_access INTEGER, current_minimum_os_versions_pid INTEGER, future_minimum_os_versions_pid INTEGER, service_unavailable_period_pid INTEGER, issuer_identifier TEXT, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS rhubarb (pid INTEGER, a INTEGER, b TEXT, c INTEGER, d INTEGER, e TEXT, f TEXT, g INTEGER, h INTEGER, i INTEGER, j TEXT, k TEXT, l TEXT, m INTEGER, n BOOL, q BOOL, r BOOL, s BOOL, t BOOL, migration_type INTEGER, start_date INTEGER, effective_date INTEGER, old_issuer_closure_date INTEGER, old_issuer_identifier TEXT, new_issuer_identifier TEXT, learn_more_url TEXT, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS strawberries (pid INTEGER, a INTEGER, b TEXT, c INTEGER, d INTEGER, e TEXT, f TEXT, g INTEGER, h INTEGER, i INTEGER, j INTEGER, k TEXT, l TEXT, m TEXT, n INTEGER, o INTEGER, os_version_requirement_range BLOB, p INTEGER, q INTEGER, r TEXT, s INTEGER, savings_interest_rate INTEGER, savings_current_minimum_os_versions_pid INTEGER, savings_future_minimum_os_versions_pid INTEGER, minimum_date INTEGER, migration_type INTEGER, start_date INTEGER, effective_date INTEGER, old_issuer_closure_date INTEGER, old_issuer_identifier TEXT, new_issuer_identifier TEXT, learn_more_url TEXT, due_date_terms_identifier TEXT, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS user_notification_receipt (pid INTEGER, notification_identifier TEXT, account_identifier TEXT, account_base_url TEXT, message_title TEXT, message_subtitle TEXT, message_body TEXT, date_scheduled INTEGER, scheduled_time_zone TEXT, date_delivered INTEGER, delivered_time_zone TEXT, date_reported INTEGER, PRIMARY KEY(pid));"
- "Indexing %lu items (%lu transactions/ %lu passes / %lu accounts / %lu payment setup products / %lu FinanceKit Transactions/ %lu FinanceKit Accounts)"
- "_predicateForReportedBeforeDate:"
- "deleteReportedUserNotificationReceiptsBeforeDate:"
- "deleteReportedUserNotificationReceiptsBeforeDate:inDatabase:"
- "indexSearchableItems:completionHandler:"
- "initWithNotificationIdentifier:accountIdentifier:accountBaseURL:"
- "reportCampaignIdentifier:eventType:referralSource:deepLinkType:productType:"
- "setRequiresFullscreenPresentation:"
- "{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}"
- "\xf0\xf0q"
```
