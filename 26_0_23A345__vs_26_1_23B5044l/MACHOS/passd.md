## passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

-1632.1.4.0.0
-  __TEXT.__text: 0x5c8450
-  __TEXT.__auth_stubs: 0x69a0
-  __TEXT.__objc_stubs: 0x71240
-  __TEXT.__objc_methlist: 0x34dac
+1640.2.0.0.0
+  __TEXT.__text: 0x5cccf4
+  __TEXT.__auth_stubs: 0x69e0
+  __TEXT.__objc_stubs: 0x71620
+  __TEXT.__objc_methlist: 0x34a5c
   __TEXT.__const: 0x47a8
-  __TEXT.__cstring: 0x6336d
-  __TEXT.__objc_classname: 0x70bb
-  __TEXT.__objc_methtype: 0x137e2
-  __TEXT.__gcc_except_tab: 0xa0ec
-  __TEXT.__objc_methname: 0xa0556
-  __TEXT.__oslogstring: 0x556ab
+  __TEXT.__cstring: 0x63a3d
+  __TEXT.__objc_classname: 0x7120
+  __TEXT.__objc_methtype: 0x1334a
+  __TEXT.__gcc_except_tab: 0xa2b0
+  __TEXT.__objc_methname: 0xa0532
+  __TEXT.__oslogstring: 0x557fb
   __TEXT.__ustring: 0x10
-  __TEXT.__swift5_typeref: 0x353e
+  __TEXT.__swift5_typeref: 0x3534
   __TEXT.__constg_swiftt: 0x1bbc
   __TEXT.__swift5_reflstr: 0x1335
   __TEXT.__swift5_fieldmd: 0x12e8

   __TEXT.__swift5_assocty: 0x318
   __TEXT.__swift5_proto: 0x1cc
   __TEXT.__swift5_types: 0x1a0
-  __TEXT.__swift5_capture: 0x1570
+  __TEXT.__swift5_capture: 0x1558
   __TEXT.__swift_as_entry: 0x88
   __TEXT.__swift_as_ret: 0xc8
   __TEXT.__swift5_protos: 0x34
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x133b8
-  __TEXT.__eh_frame: 0x2ff0
-  __DATA_CONST.__auth_got: 0x34e0
-  __DATA_CONST.__got: 0x3da8
+  __TEXT.__unwind_info: 0x13498
+  __TEXT.__eh_frame: 0x3038
+  __DATA_CONST.__auth_got: 0x3500
+  __DATA_CONST.__got: 0x3db8
   __DATA_CONST.__auth_ptr: 0x8b0
-  __DATA_CONST.__const: 0x2fc98
-  __DATA_CONST.__cfstring: 0x32f60
-  __DATA_CONST.__objc_classlist: 0x1900
+  __DATA_CONST.__const: 0x2fed0
+  __DATA_CONST.__cfstring: 0x333a0
+  __DATA_CONST.__objc_classlist: 0x1918
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x620
+  __DATA_CONST.__objc_protolist: 0x618
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xe0
-  __DATA_CONST.__objc_superrefs: 0xf08
-  __DATA_CONST.__objc_intobj: 0x1350
-  __DATA_CONST.__objc_arraydata: 0x5a0
+  __DATA_CONST.__objc_superrefs: 0xf18
+  __DATA_CONST.__objc_intobj: 0x13c8
+  __DATA_CONST.__objc_arraydata: 0x5d0
   __DATA_CONST.__objc_dictobj: 0x280
-  __DATA_CONST.__objc_arrayobj: 0x648
+  __DATA_CONST.__objc_arrayobj: 0x678
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x41620
-  __DATA.__objc_selrefs: 0x1f778
-  __DATA.__objc_ivar: 0x2964
-  __DATA.__objc_data: 0x10d00
-  __DATA.__data: 0x6cd0
-  __DATA.__bss: 0x3a50
+  __DATA.__objc_const: 0x41448
+  __DATA.__objc_selrefs: 0x1f758
+  __DATA.__objc_ivar: 0x2980
+  __DATA.__objc_data: 0x10df0
+  __DATA.__data: 0x6c60
+  __DATA.__bss: 0x3a70
   __DATA.__common: 0xb0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 881BDBFE-B83E-3384-B646-56E2365D611C
-  Functions: 27717
-  Symbols:   3873
-  CStrings:  41886
+  UUID: CA9D4171-313E-3040-AEBE-CABEE0C8C4D4
+  Functions: 27790
+  Symbols:   3879
+  CStrings:  41946
 
Symbols:
+ _CFDictionaryApplyFunction
+ _CFDictionaryContainsKey
+ _CFDictionaryRemoveValue
+ _NSSelectorFromString
+ _OBJC_CLASS_$_PKCreditAccountUserInfo
+ _OBJC_CLASS_$_PKPassTransactionActivitySummary
+ _PKCloudStoreOperationGroupSuffixViewedTransactionsRecoveringFromFullFetchError
+ _PKCloudStoreOperationGroupSuffixViewedTransactionsRecoveringFromProactiveFetchError
+ _PKDateIsBetweenDates
+ _PKLiveActivityAttributesTypeFromString
+ _PKPassRelevancySystemPresentmentStateFromString
- _OBJC_CLASS_$_PKExpressPassController
- _PKCloudStoreOperationGroupSuffixViewedTransactionsRecoveringFromPreviousError
- _PKSetHandoffPaymentsDisabled
- _PKSetOrderManagementDisabled
- _PKSetOrderManagementNotificationsDisabled
CStrings:
+ "%@.effective_category"
+ "%s called with passUniqueIdentifier: %@, paymentApplicationIdentifier: %@"
+ "-[PDPaymentService cashbackByPeriodForTransactionSourceIdentifiers:withStartDate:endDate:calendar:calendarUnit:type:usingSynchronousProxy:completion:]"
+ "-[PDPaymentService earliestDailyBucketForTransactionSourceIdentifiers:calendar:type:limit:completion:]"
+ "-[PDPaymentService recordPassTransactionActivitySummaryForPassUniqueIdentifier:paymentApplicationIdentifier:presentmentType:]"
+ "-[PDPaymentService spendingCategoryTransactionGroupsForRequest:byCalendarUnit:completion:]"
+ "-[PDPaymentService transactionCountForRequest:usingSynchronousProxy:completion:]"
+ "-[PDPaymentService transactionSourceIdentifiersForPassUniqueIdentifiers:completion:]_block_invoke"
+ "-[PDPaymentService transactionsForRequest:usingSynchronousProxy:completion:]"
+ "@\"PDUserActivityAccessPresentmentInformation\""
+ "@\"PKPeerPaymentAddress\""
+ "B16@?0@\"PKPaymentTransactionGroup\"8"
+ "COALESCE(NULLIF(preferred_category, 0), NULLIF(maps_merchant.c, 0), NULLIF(plantains.g, 0), NULLIF(x, 0)) as effective_category"
+ "CREATE INDEX IF NOT EXISTS account_event_date_index ON grapes (d);"
+ "CREATE INDEX IF NOT EXISTS cloud_store_record_combined_index ON cloud_store_record (record_name, zone_pid);"
+ "CREATE INDEX IF NOT EXISTS payment_transaction_date_index ON payment_transaction (transaction_date);"
+ "CREATE INDEX IF NOT EXISTS payment_transaction_request_token_index on payment_transaction (request_token);"
+ "CREATE INDEX cloud_store_record_combined_index ON cloud_store_record (record_name, zone_pid);"
+ "CREATE TABLE IF NOT EXISTS live_activity_section_state (pid INTEGER, identifier TEXT, attributes_type TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS live_activity_state (pid INTEGER, live_activity_section_state_pid INTEGER, identifier TEXT, activity_id TEXT, state TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS pass_transaction_activity_summary (pid INTEGER, pass_unique_identifier TEXT, payment_application_identifier TEXT, subcredential_identifier TEXT, last_used INTEGER, presentment_type INTEGER,PRIMARY KEY (pid));"
+ "Creating new invalid billing address notification"
+ "DROP INDEX IF EXISTS account_rewards_redemption_success;"
+ "DROP INDEX IF EXISTS payment_transaction_merchant_name_index;"
+ "DROP INDEX IF EXISTS payment_transaction_merchant_raw_canl_index;"
+ "DROP INDEX IF EXISTS payment_transaction_merchant_raw_name_index;"
+ "DROP INDEX IF EXISTS payment_transaction_use_raw_merchant_data_index;"
+ "Failed to fetch updated peer payment recurring payments with error: %@."
+ "INVALID_BILLING_ADDRESS_NOTIFICATION_MESSAGE"
+ "INVALID_BILLING_ADDRESS_NOTIFICATION_MESSAGE_DEFAULT"
+ "INVALID_BILLING_ADDRESS_NOTIFICATION_TITLE"
+ "INVALID_BILLING_ADDRESS_RESTRICTED_NOTIFICATION_MESSAGE"
+ "INVALID_BILLING_ADDRESS_RESTRICTED_NOTIFICATION_TITLE"
+ "Migrating database from user_version 18084 to 18085"
+ "Migrating database from user_version 18085 to 18086"
+ "Migrating database from user_version 18086 to 18087"
+ "Migrating database from user_version 18087 to 18088"
+ "No cleanup of PII because subcredential %@ lacks an identifier for pass %@"
+ "No cleanup of PII token for pass id %@ because credentialStore does not support new SPI yet"
+ "No cleanup of PII token for pass id %@ because credentialStore is nil"
+ "Not creating an invalid billing address notification since one already exists %@"
+ "PDPeerPaymentInvalidBillingAddressUserNotification"
+ "PDUserActivityAccessPresentmentInformation"
+ "PassTransactionActivitySummary"
+ "Requesting cleanup of the assiciated PII token as the deleted pass %@ relies on one"
+ "SELECT %@ FROM (%@) AS %@ GROUP BY %@"
+ "SELECT %@, MAX(%@) as total FROM %@ JOIN peer_payment_account on (%@.%@ = %ld AND peer_payment_account.associated_account_pid is NULL) WHERE %@ IS NOT NULL AND %@ != '' AND %@ != %ld AND %@ = %ld "
+ "STRFTIME('%%s', DATETIME(%@.transaction_date + %ld, 'unixepoch', 'localtime', 'start of %@', 'utc')) AS %@"
+ "SUM(%@.%@)"
+ "Skipping peer payment recurring payments update because account is not eligible."
+ "Successfully cleaned up PII token with identifier %@ and credentialIdentifier %@ for pass id %@"
+ "T@\"PDUserActivityAccessPresentmentInformation\",R,N,V_accessInformation"
+ "T@\"PDUserActivitySignalsManager\",&,N,V_userActivitySignalsManager"
+ "T@\"PKPeerPaymentAddress\",R,C,N,V_billingAddress"
+ "TQ,N,V_presentmentType"
+ "Tq,R,N,V_productSubtype"
+ "Unable to clean up identity PII token with identifier %@ and credentialIdentifier %@ for pass id %@ due to error %@"
+ "[BoardingPassLiveActivityDescriptor] Failed to fetch destination weather for flight: %s with error: '%@'"
+ "[BoardingPassLiveActivityDescriptor] Failed to update flight live activity: content not found for pass: %@"
+ "[BoardingPassLiveActivityDescriptor] Failed to update live activity with destination weather for flight: %s"
+ "[BoardingPassLiveActivityDescriptor] Failed to update live activity: Flight not found in pass: %@"
+ "[BoardingPassLiveActivityDescriptor] Successfully fetched destination weather for flight: %s"
+ "[LiveActivitySupplier] Discarding invalid sections: %s"
+ "_accessInformation"
+ "_billingAddress"
+ "_creditUserInfoForAccount:forceFetch:completion:"
+ "_fetchCreditUserInfoForAccount:completion:"
+ "_getSubcredentialIdentifierWithPaymentApplicationIdentifier:paymentApplications:"
+ "_insertOrRemoveUserInfoNotificationIfNeededWithAccount:"
+ "_migrateFrom18084To18085:context:"
+ "_migrateFrom18085To18086:context:"
+ "_migrateFrom18086To18087:context:"
+ "_migrateFrom18087To18088:context:"
+ "_passTransactionActivitySummariesWithQuery:inDatabase:"
+ "_predicateForIncompleteGroupRequest"
+ "_predicateForNotGroupRequest"
+ "_predicateForPassUniqueIdentifier:paymentApplicationIdentifier:subcredentialIdentifier:"
+ "_presentmentType"
+ "_productSubtype"
+ "_savingsUserInfoForAccount:completion:"
+ "_stringTagForAccessProductSubType:"
+ "_stringTagForPaymentProductSubType:"
+ "_transactionSourceUpdatesRequested"
+ "_userActivitySignalsManager"
+ "accessInformation"
+ "accountUsersForAccountWithIdentifier:usingSynchronousProxy:completion:"
+ "allPassTransactionActivitySummariesInDatabase:"
+ "associatedPassUniqueIDInDatabase:"
+ "attributes_type TEXT"
+ "carAccess"
+ "cashbackByPeriodForTransactionSourceIdentifiers:withStartDate:endDate:calendar:calendarUnit:type:usingSynchronousProxy:completion:"
+ "corporateAccess"
+ "creditAccountUserInfoWithRequest:completion:"
+ "currencyAmountByAddingCurrencyAmount:"
+ "dbAccountUser"
+ "dbTransactionWithServiceIdentifier:transactionSourceIdentifier:"
+ "defaultAccountForFeature:"
+ "defaultAccountForFeature:usingSynchronousProxy:completion:"
+ "deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:completion:"
+ "deletePassTransactionActivitySummariesForPassUniqueIdentifier:inDatabase:"
+ "enumerateTransactionAmountAndCategory:request:block:"
+ "findFidoKeyForRelyingParty:relyingPartyAccountHash:challenge:completion:"
+ "generalAccess"
+ "handlePassTransactionActivitySummaryWithPassUniqueIdentifier:paymentApplicationIdentifier:lastUsed:presentmentType:"
+ "handlePassTransactionActivitySummaryWithPassUniqueIdentifier:paymentApplicationIdentifier:pass:state:"
+ "homeAccess"
+ "hospitalityAccess"
+ "initWithAccessInformation:"
+ "initWithPassUniqueIdentifier:paymentApplicationIdentifier:subcredentialIdentifier:lastUsed:presentmentType:"
+ "initWithPassUniqueIdentifier:paymentApplicationIdentifier:subcredentialIdentifier:pass:state:"
+ "initWithPeerPaymentBillingAddress:state:passUniqueIdentifier:"
+ "initWithSubtype:"
+ "insertOrUpdatePassTransactionActivitySummary:inDatabase:"
+ "insertPassTransactionActivitySummary:"
+ "isEligibleForRecurringPaymentUpdates"
+ "methodForSelector:"
+ "multiFamilyAccess"
+ "passTransactionActivitySummariesForPassUniqueIdentifier:inDatabase:"
+ "passTransactionActivitySummary"
+ "pass_transaction_activity_summary"
+ "peerPaymentInvalidBillingAddress"
+ "period_group"
+ "presentment_type"
+ "productSubtype"
+ "recordPassTransactionActivitySummaryForPassUniqueIdentifier:paymentApplicationIdentifier:presentmentType:"
+ "retrievePIITokenFromSyncableKeyStoreForIdentifier:completion:"
+ "setCreditUserInfo:"
+ "setGroups:"
+ "setHasIssuerInstallmentsHandoffViewOpenAssertion:"
+ "setPresentmentType:"
+ "setPrimaryUser:"
+ "setTotalRewardsAmount:"
+ "setUserActivitySignalsManager:"
+ "spendingCategoryTransactionGroupsForRequest:byCalendarUnit:"
+ "spendingCategoryTransactionGroupsForRequest:byCalendarUnit:completion:"
+ "spendingCategoryTransactionGroupsInDatabase:request:byCalendarUnit:"
+ "state TEXT"
+ "subcredential_identifier"
+ "totalRewardsAmount"
+ "transactionCountForRequest:usingSynchronousProxy:completion:"
+ "transactionSourceIdentifiersForPassUniqueIdentifiers:completion:"
+ "transactionsForRequest:usingSynchronousProxy:completion:"
+ "updateWithPassTransactionActivitySummary:"
+ "urbanMobilityAccess"
+ "userActivitySignalsManager"
+ "v16@?0@\"PDPeerPaymentInvalidBillingAddressUserNotification\"8"
+ "v16@?0@\"PKPaymentTransactionGroup\"8"
+ "v24@?0@\"PKCreditAccountUserInfo\"8@\"NSError\"16"
+ "v24@?0@\"PKCreditAccountWebServiceAccountUserInfoResponse\"8@\"NSError\"16"
+ "v24@?0@\"PKPassTransactionActivitySummary\"8@16"
+ "v32@0:8@\"NSSet\"16@?<v@?@\"NSDictionary\">24"
+ "v32@?0q8q16^B24"
+ "v36@0:8@\"NSString\"16B24@?<v@?@\"NSSet\">28"
+ "v36@0:8@\"PKPaymentTransactionRequest\"16B24@?<v@?@\"NSArray\">28"
+ "v36@0:8@\"PKPaymentTransactionRequest\"16B24@?<v@?@\"NSNumber\">28"
+ "v36@0:8Q16B24@?<v@?@\"PKAccount\"@\"NSError\">28"
+ "v40@0:8@\"NSString\"16@\"NSString\"24Q32"
+ "v40@0:8@\"PKPaymentTransactionRequest\"16Q24@?<v@?@\"NSArray\">32"
+ "v48@0:8@16@24@32Q40"
+ "v76@0:8@\"NSSet\"16@\"NSDate\"24@\"NSDate\"32@\"NSCalendar\"40Q48Q56B64@?<v@?@\"NSArray\">68"
+ "v76@0:8@16@24@32@40Q48Q56B64@?68"
- "-[PDPaymentService cashbackByPeriodForTransactionSourceIdentifiers:withStartDate:endDate:calendar:calendarUnit:type:completion:]_block_invoke"
- "-[PDPaymentService earliestDailyBucketForTransactionSourceIdentifiers:calendar:type:limit:completion:]_block_invoke"
- "-[PDPaymentService spendingCategoryTransactionGroupsForRequest:completion:]_block_invoke"
- "-[PDPaymentService transactionCountForRequest:completion:]_block_invoke"
- "-[PDPaymentService transactionsForRequest:completion:]_block_invoke"
- "@\"<PKPaymentDataProviderDelegate>\""
- "@\"<PKPaymentDataProviderDelegate>\"16@0:8"
- "@\"NSArray\"24@0:8@\"PKPaymentTransactionRequest\"16"
- "@\"NSArray\"64@0:8@\"NSSet\"16@\"NSDate\"24@\"NSDate\"32@\"NSCalendar\"40Q48Q56"
- "@\"NSDate\"48@0:8@\"NSSet\"16@\"NSCalendar\"24Q32q40"
- "@\"PKOSVersionRequirement\"16@0:8"
- "@\"PKPaymentRewardsBalance\"24@0:8@\"NSString\"16"
- "@\"PKPaymentWebService\"16@0:8"
- "Attempting to delete PII -- will check if any paired device has Digital ID"
- "B24@0:8@\"PKPass\"16"
- "CREATE INDEX IF NOT EXISTS account_rewards_redemption_success ON avocados (f);"
- "CREATE TABLE IF NOT EXISTS live_activity_section_state (pid INTEGER, identifier TEXT, attributes_type INTEGER, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS live_activity_state (pid INTEGER, live_activity_section_state_pid INTEGER, identifier TEXT, activity_id TEXT, state INTEGER, PRIMARY KEY (pid));"
- "Error: Failed to fetch updated peer payment recurring payments with error: %@."
- "Error: could not find the pass unique identifier for the card or peer payment transaction with service identifier %{public}@"
- "Failed to fetch current weather with error: '%@'"
- "LEFT JOIN payment_transaction AS payment_transaction_left on (payment_transaction_left.pid =  (SELECT pt.pid FROM payment_transaction pt  WHERE ( (pt.merchant_raw_name = payment_transaction.merchant_raw_name OR pt.merchant_name = payment_transaction.merchant_name OR pt.f = payment_transaction.f)  AND pt.last_force_merchant_reprocessing_request_date > 0 ) LIMIT 1))"
- "No cleanup of PII because credentialStore is nil"
- "No cleanup of PII because devicePrimaryPaymentApplication is nil"
- "No cleanup of PII because no subcredentials are found in the primary payment application"
- "No cleanup of PII because pass is nil"
- "No cleanup of PII because the subCrential identifier is missing"
- "No cleanup of PII because there is no subcredential in the subcredentials set"
- "PII cleanup NOT needed because this is NOT a Digital ID"
- "PII cleanup needed because this is a Digital ID"
- "PKPaymentDataProvider"
- "SELECT %@, MAX(%@) as total FROM %@ JOIN peer_payment_account on (%@.%@ = %ld AND peer_payment_account.associated_account_pid is NULL) WHERE %@ IS NOT NULL AND %@ != '' AND %@ != %ld AND %@ = %ld"
- "SELECT COALESCE(NULLIF(%@, 0), NULLIF(%@, 0), NULLIF(%@, 0), NULLIF(%@, 0)) as effective_category, SUM(amount), COUNT(*) FROM payment_transaction %@ WHERE %@ GROUP BY effective_category"
- "Successfully cleaned up PII token with identifier %@ for pass id %@"
- "T@\"<PKPaymentDataProviderDelegate>\",W,N"
- "T@\"<PKPaymentDataProviderDelegate>\",W,N,V_delegate"
- "T@\"NSString\",&,N"
- "T@\"PKOSVersionRequirement\",R,N"
- "T@\"PKPaymentWebService\",R,N"
- "Unable to clean up identity PII token with error %@"
- "Will cleanup PII token - no Digital ID on paired device"
- "Will not cleanup PII token, there is a Digital ID on a paired device"
- "[PassRelevancySystemPresentmentsCoordinator.BoardingPassLiveActivity] Failed to update flight live activity: content not found for pass: %@"
- "[PassRelevancySystemPresentmentsCoordinator.BoardingPassLiveActivity] Failed to update live activity: Flight not found in pass: %@"
- "_creditUserInfoForAccountIdentifier:forceFetch:completion:"
- "_fetchCreditUserInfoForAccountIdentifier:completion:"
- "_needsIdentityCleanupBeforePassDeletion:"
- "_savingsUserInfoForAccountIdentifier:completion:"
- "_stringTagForProductSubType:"
- "_userActivitySignalManager"
- "accountUserInfoWithRequest:completion:"
- "apiVersion"
- "balanceReminderThresholdForBalance:pass:withCompletion:"
- "balancesForPaymentPassWithUniqueIdentifier:completion:"
- "broadwayOrSurfPassUniqueIdentifierForAmbiguousServiceIdentifier:"
- "cancelAutoTopUpForPassWithUniqueIdentifier:balanceIdentifiers:completion:"
- "cashbackByPeriodForTransactionSourceIdentifiers:withStartDate:endDate:calendar:calendarUnit:type:completion:"
- "commutePlanReminderForCommutePlan:pass:withCompletion:"
- "defaultAccountForFeature:forAccounts:"
- "deleteDataFromSyncableKeyStoreForIdentifier:completion:"
- "expressModeUpgradeRequestForPass:"
- "expressPassesInformation"
- "felicaStateWithPassUniqueIdentifier:paymentApplication:completion:"
- "hideCardBenefitMerchandisingOffers"
- "hideCardBenefitPayLater"
- "hideCardBenefitRewards"
- "hidePayLaterOptions"
- "initWithPaymentDataProvider:passLibraryDataProvider:isForWatch:"
- "insertUserLegalAgreement:"
- "messagesAppLaunchTokenForPassWithUniqueIdentifier:"
- "messagesForPaymentPassWithUniqueIdentifier:completion:"
- "passUpgradeWithRequest:pass:visibleViewController:completion:"
- "payment_transaction_left.last_force_merchant_reprocessing_request_date"
- "plansForPaymentPassWithUniqueIdentifier:completion:"
- "recurringPaymentsWithPreventingServerFetch:completion:"
- "removeExpressPassWithUniqueIdentifier:visibleViewController:completion:"
- "removeExpressPassesWithUniqueIdentifiers:visibleViewController:completion:"
- "setBalanceReminder:forBalance:pass:completion:"
- "setCommutePlanReminder:forCommutePlan:pass:completion:"
- "setCreditPrimaryUser:"
- "setDefaultPaymentApplication:forPassUniqueIdentifier:completion:"
- "setExpressWithPassConfiguration:visibleViewController:completion:"
- "setExpressWithPassConfiguration:visibleViewController:requiresAuth:completion:"
- "setExpressWithPassInformation:visibleViewController:completion:"
- "setExpressWithPassInformation:visibleViewController:requiresAuth:completion:"
- "setHideCardBenefitMerchandisingOffers:"
- "setHideCardBenefitPayLater:"
- "setHideCardBenefitRewards:"
- "setHidePayLaterOptions:"
- "setOrderManagementDisabled:"
- "setOrderManagementNotificationsDisabled:"
- "setPaymentHandoffDisabled:"
- "sharingCapabilitiesForPassIdentifier:outHasShares:outHasShareableEntitlements:"
- "spendingCategoryTransactionGroupsForRequest:"
- "spendingCategoryTransactionGroupsForRequest:completion:"
- "spendingCategoryTransactionGroupsInDatabase:request:"
- "startServiceModeForPassWithUniqueIdentifier:visibleViewController:"
- "supportsAddingPaymentPasses"
- "supportsInAppPaymentsForPass:"
- "supportsLowPowerExpressMode"
- "supportsMessagesForPass:"
- "supportsNotificationsForPass:"
- "supportsTransactionsForPass:"
- "tilesForPassWithUniqueIdentifier:context:completion:"
- "transactionCountByPeriodForRequest:calendar:calendarUnit:includePurchaseTotal:completion:"
- "transactionCountForRequest:completion:"
- "transactionWithServiceIdentifier:completion:"
- "transactionsAppLaunchTokenForPassWithUniqueIdentifier:"
- "transactionsForPaymentPassWithUniqueIdentifier:withTransactionSource:withNotificationServiceData:limit:completion:"
- "transactionsForRequest:completion:"
- "transitStateWithPassUniqueIdentifier:paymentApplication:completion:"
- "v24@0:8@\"<PKPaymentDataProviderDelegate>\"16"
- "v24@0:8@\"PKUserLegalAgreementConsent\"16"
- "v24@?0@\"CNContact\"8@\"NSError\"16"
- "v24@?0@\"PKAccountWebServiceAccountUserInfoResponse\"8@\"NSError\"16"
- "v32@0:8@\"NSString\"16@24"
- "v32@0:8@\"PKPaymentTransactionRequest\"16@?<v@?@\"NSArray\">24"
- "v32@0:8@\"PKPaymentTransactionRequest\"16@?<v@?@\"NSNumber\">24"
- "v32@0:8Q16@?<v@?@\"PKAccount\"@\"NSError\">24"
- "v40@0:8@\"NSArray\"16@24@?<v@?B@\"NSSet\">32"
- "v40@0:8@\"NSString\"16@\"PKPaymentApplication\"24@?<v@?@\"PKFelicaTransitAppletState\">32"
- "v40@0:8@\"NSString\"16@24@?<v@?B@\"NSSet\">32"
- "v40@0:8@\"NSString\"16^B24^B32"
- "v40@0:8@\"PKExpressPassConfiguration\"16@24@?<v@?B@\"PKExpressPassConfiguration\">32"
- "v40@0:8@\"PKExpressPassInformation\"16@24@?<v@?B@\"PKExpressPassInformation\">32"
- "v40@0:8@\"PKPaymentBalance\"16@\"PKPaymentPass\"24@?<v@?@\"PKPaymentBalanceReminder\">32"
- "v40@0:8@\"PKTransitCommutePlan\"16@\"PKPaymentPass\"24@?<v@?@\"PKPaymentCommutePlanReminder\">32"
- "v40@0:8@16^B24^B32"
- "v44@0:8@\"PKExpressPassConfiguration\"16@24B32@?<v@?B@\"NSSet\">36"
- "v44@0:8@\"PKExpressPassInformation\"16@24B32@?<v@?B@\"NSSet\">36"
- "v48@0:8@\"PKPassUpgradeRequest\"16@\"PKPaymentPass\"24@32@?<v@?@\"NSError\"@\"PKPaymentPass\">40"
- "v48@0:8@\"PKPaymentBalanceReminder\"16@\"PKPaymentBalance\"24@\"PKPaymentPass\"32@?<v@?B>40"
- "v48@0:8@\"PKPaymentCommutePlanReminder\"16@\"PKTransitCommutePlan\"24@\"PKPaymentPass\"32@?<v@?B>40"
- "v56@0:8@\"NSString\"16Q24Q32q40@?<v@?@\"NSSet\">48"
- "v72@0:8@\"NSSet\"16@\"NSDate\"24@\"NSDate\"32@\"NSCalendar\"40Q48Q56@?<v@?@\"NSArray\">64"
- "v72@0:8@16@24@32@40Q48Q56@?64"
- "\xf0\xf1"

```
