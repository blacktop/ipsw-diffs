## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3826.300.86.2.3
-  __TEXT.__text: 0x23dd2c
-  __TEXT.__auth_stubs: 0x23e0
-  __TEXT.__objc_methlist: 0x12e64
-  __TEXT.__gcc_except_tab: 0x490e0
+3826.300.87.2.11
+  __TEXT.__text: 0x2422b8
+  __TEXT.__auth_stubs: 0x2400
+  __TEXT.__objc_methlist: 0x12f54
+  __TEXT.__gcc_except_tab: 0x49b6c
   __TEXT.__const: 0x1d08
-  __TEXT.__cstring: 0x201d7
-  __TEXT.__oslogstring: 0x17456
+  __TEXT.__cstring: 0x201e7
+  __TEXT.__oslogstring: 0x17bc6
   __TEXT.__ustring: 0x2c
   __TEXT.__dlopen_cstrs: 0x57
   __TEXT.__swift5_typeref: 0x715

   __TEXT.__swift5_types: 0xbc
   __TEXT.__swift5_capture: 0x128
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xfd48
+  __TEXT.__unwind_info: 0xfe88
   __TEXT.__eh_frame: 0x860
   __TEXT.__objc_classname: 0x2d18
-  __TEXT.__objc_methname: 0x37e71
-  __TEXT.__objc_methtype: 0x7ebb
-  __TEXT.__objc_stubs: 0x245e0
+  __TEXT.__objc_methname: 0x382e3
+  __TEXT.__objc_methtype: 0x7f05
+  __TEXT.__objc_stubs: 0x24860
   __DATA_CONST.__got: 0x1a90
-  __DATA_CONST.__const: 0x8bf8
+  __DATA_CONST.__const: 0x8d60
   __DATA_CONST.__objc_classlist: 0x950
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x3b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb440
+  __DATA_CONST.__objc_selrefs: 0xb4f0
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x670
   __DATA_CONST.__objc_arraydata: 0x680
-  __AUTH_CONST.__auth_got: 0x1200
+  __AUTH_CONST.__auth_got: 0x1210
   __AUTH_CONST.__auth_ptr: 0x340
-  __AUTH_CONST.__const: 0x3ce8
-  __AUTH_CONST.__cfstring: 0x107c0
-  __AUTH_CONST.__objc_const: 0x26bc0
+  __AUTH_CONST.__const: 0x3ca8
+  __AUTH_CONST.__cfstring: 0x10860
+  __AUTH_CONST.__objc_const: 0x26c38
   __AUTH_CONST.__objc_intobj: 0x8e8
   __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH.__objc_data: 0x230
   __AUTH.__data: 0x20
-  __DATA.__objc_ivar: 0x1624
+  __DATA.__objc_ivar: 0x162c
   __DATA.__data: 0x2f80
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x22f0

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10329
-  Symbols:   11177
-  CStrings:  14051
+  Functions: 10368
+  Symbols:   11218
+  CStrings:  14107
 
Symbols:
+ _EFNumbersAreEqual
+ _EMCategoryFromSubtype
CStrings:
+ "\x01C1\x16"
+ "%lu addresses need an updated brand ID."
+ "%p: %{public}@ - rescheduling changes for keyPaths:%{public}@ removed=%lu added=%lu changed=%lu after %.3f due to generation %lld not being higher than generation window of the change %lld"
+ "-[EDBusinessPersistence businessAddressMapWithCategoryOverride]"
+ "-[EDBusinessPersistence categoryTypeForBusinessID:]"
+ "-[EDBusinessPersistence fetchBusinessMetadataForAddresses:completionHandler:]"
+ "<%@ %p> Unable to fetch messages for %{public}@, as the protected database is unavailable. Skipping updating cached messages"
+ "Business Connect took longer than 5 seconds to return the results for addresses: %{public}@"
+ "Checking for BCS update for existing businessID %lld for address %lld: %{public}@"
+ "Completed call to fetchBusinessMetadataForEmails with %lld addresses"
+ "Couldn't convert a Business Connect Identifier for address %{public}@: %{public}@"
+ "DROP TEMP VIEW"
+ "Failed to create messages for threadObjectID: %{public}@"
+ "Failed to create temp_thread_scope_message temp view"
+ "Failed to drop temp_persisted_messages temp view"
+ "Failed to drop temp_thread_scope_message temp view"
+ "Failed to find or create businessID for address %lld: %{public}@"
+ "Failed to insert business with brandID %{public}@ (as int64) and brand names %{public}@, due to error %{public}@"
+ "Fetched Business Connect metadata (brandID %{public}@) for addressID: %@ (%{public}@)"
+ "Finding or creating businessID for address %lld (brandID %{public}@): %{public}@"
+ "Finding or creating businessID for address %lld: %{public}@"
+ "Finished writing + fetching metadata for %lld addresses"
+ "First 3 characters do not match"
+ "Found a business with an invalid display name: %{public}lld, businessName: %{public}@, messageName: %{public}@ (%{public}@)"
+ "Found existing businessID %lld for address %lld: %{public}@"
+ "Found existing businessID %lld for externalID %{public}@, businessIDs to combine: %{public}@"
+ "Missing category for addressID %lld. Adding a placeholder category"
+ "New businessID %lld for brandID %{public}@ with brand names: %{public}@"
+ "New businessID %lld with display name %{public}@ for external ID %{public}@"
+ "New businessID %lld with display name %{public}@ for external ID %{public}@ by combining businesIDs: %{public}@"
+ "No addresses needing an update, exiting."
+ "Skipping update for address %lld, new brand ID matches existing one."
+ "Skipping updating category for business %{public}@, no corresponding businessID on this device"
+ "Successfully inserted business with ID %lld, brandID %{public}@ (as int64), and brand names %{public}@"
+ "Try to update business ID for address %@"
+ "Unable to create empty temp_persisted_messages"
+ "Unable to create temp_persisted_messages"
+ "Unable to get category type for businessID %lld, due to error: %{public}@"
+ "Updating brand names to %{public}@"
+ "_dropTemporaryView"
+ "_hasCategoryChanged:from:"
+ "_hasCommonDomain:"
+ "_logRecategorizeAnalyticsWithPersistedMessages:isRestoreModelCategory:categoryChangeAction:"
+ "_loggedDisplayNameErrorCount"
+ "_performBlockAfterGenerationCheck:generation:keyPaths:removedMessages:changedMessages:addedMessages:"
+ "_persistedBusinessDisplayName"
+ "_removeCategoryCloudStorageForBusiness:lastModifiedDate:"
+ "_reportChangesForCurrentlyMatchingMessages:previouslyMatchingMessages:keyPaths:generation:"
+ "_reportChangesForPersistedMessages:withPendingChangesKey:keyPaths:generation:"
+ "_senderDisplayName"
+ "_shouldUseGroupingSimpleAddressForEmailAddress:grouping:"
+ "_updateCategoryOverrideForBusinessExternalID:"
+ "_updateCategoryOverrideForBusinessID:withBusinessExternalID:"
+ "aol"
+ "businessAddressMapWithCategoryOverride"
+ "categoryTypeForBusinessID:"
+ "createMessagesWithThreadObjectID:wrappedMessages:threadMessages:"
+ "displayNamesMatch"
+ "domainStrippingTopLevelDomain"
+ "gmail"
+ "googlemail"
+ "highLevelDomainStrippingTopLevelDomain"
+ "hotmail"
+ "i24@0:8Q16"
+ "icloud"
+ "initWithBusinessPersistence:categoryPersistence:messagePersistence:hookRegistry:"
+ "live"
+ "logFedStatRecategorizationEventForMessages:categoryChangeAction:categoryPersistence:"
+ "logRecategorizationEventForMessages:categoryType:categoryPersistence:isHighImpactFlagChange:"
+ "mac"
+ "me"
+ "msn"
+ "outlook"
+ "persisted display name has more tokens"
+ "persisted display name is longer"
+ "persistedBusinessLogoID"
+ "persistenceIsCreatingBusinessID:withExternalBusinessID:"
+ "recipientDatabaseIDsAndDatesForRecipientType:recipients:"
+ "senderDatabaseIDsAndDates:"
+ "token %ld desn't match"
+ "updatedCategoryForAddressID:fromCategorizationResult:"
+ "v16@?0@\"NSString\"8"
+ "v24@?0Q8Q16"
+ "v32@0:8q16@\"EMBusinessExternalID\"24"
+ "v32@?0@\"EFPair\"8Q16^B24"
+ "v32@?0@\"NSNumber\"8@\"<ECEmailAddressConvertible>\"16@\"NSError\"24"
+ "v64@0:8@?16@24@32@40@48@56"
+ "yahoo"
- "\x0131\x16"
- "-[_EDThreadPersistence_PersistedThread _ensureTempMessagesView]"
- "-[_EDThreadPersistence_PersistedThread _ensureTempMessagesView]_block_invoke"
- "-[_EDThreadPersistence_PersistedThread dropTemporaryView]_block_invoke"
- "-[_EDThreadPersistence_ThreadScope _ensureTempScopeView]"
- "-[_EDThreadPersistence_ThreadScope dropTemporaryView]"
- "Couldn't convert a Business Connect Identifier for address: %@ with address ID: %@"
- "Failed to drop temp_persisted_messages temp view: %{public}@"
- "Failed to drop temp_thread_scope_message temp view: %{public}@"
- "Failed to find or create businessID for address %{public}@"
- "Failed to insert business with brandID %lld (as int64) and brand names %{public}@, due to error %{public}@"
- "Fetched Business Connect metadata for addressID: %@ (%{public}@)"
- "Successfully inserted business with ID %lld, brandID %lld (as int64), and brand names %{public}@"
- "Unable to create empty temp_persisted_messages: %{public}@"
- "_reportChangesForCurrentlyMatchingMessages:previouslyMatchingMessages:keyPaths:"
- "_reportChangesForPersistedMessages:withPendingChangesKey:keyPaths:"
- "aol.com"
- "createMessagesWithThreadObjectID:wrappedMessages:"
- "dropTemporaryView"
- "gmail.com"
- "googlemail.com"
- "hotmail.com"
- "icloud.com"
- "live.com"
- "mac.com"
- "me.com"
- "msn.com"
- "outlook.com"
- "recipientDatabaseIDsAndDatesForRecipientType:"
- "senderDatabaseIDsAndDates"
- "v32@?0@\"<ECEmailAddressConvertible>\"8@\"NSNumber\"16@\"NSError\"24"
- "yahoo.com"

```
