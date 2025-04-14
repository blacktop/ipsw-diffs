## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3826.600.15.2.1
-  __TEXT.__text: 0x255d18
+3826.600.32.0.0
+  __TEXT.__text: 0x2575a8
   __TEXT.__auth_stubs: 0x2760
-  __TEXT.__objc_methlist: 0x15a8c
+  __TEXT.__objc_methlist: 0x15cdc
   __TEXT.__const: 0x1eec
-  __TEXT.__gcc_except_tab: 0x4c0b0
-  __TEXT.__cstring: 0x220c7
-  __TEXT.__oslogstring: 0x191c6
+  __TEXT.__gcc_except_tab: 0x4c3ac
+  __TEXT.__cstring: 0x22137
+  __TEXT.__oslogstring: 0x193b6
   __TEXT.__ustring: 0x2c
   __TEXT.__dlopen_cstrs: 0x57
   __TEXT.__swift5_typeref: 0x951

   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x105a0
+  __TEXT.__unwind_info: 0x106b0
   __TEXT.__eh_frame: 0xd60
-  __TEXT.__objc_classname: 0x2e91
-  __TEXT.__objc_methname: 0x3996c
-  __TEXT.__objc_methtype: 0x852f
-  __TEXT.__objc_stubs: 0x25000
-  __DATA_CONST.__got: 0x1b58
-  __DATA_CONST.__const: 0x9220
-  __DATA_CONST.__objc_classlist: 0x998
+  __TEXT.__objc_classname: 0x2efa
+  __TEXT.__objc_methname: 0x39cb9
+  __TEXT.__objc_methtype: 0x85b3
+  __TEXT.__objc_stubs: 0x252a0
+  __DATA_CONST.__got: 0x1b80
+  __DATA_CONST.__const: 0x9270
+  __DATA_CONST.__objc_classlist: 0x9b0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x400
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb9a0
-  __DATA_CONST.__objc_protorefs: 0xd0
-  __DATA_CONST.__objc_superrefs: 0x698
+  __DATA_CONST.__objc_selrefs: 0xba50
+  __DATA_CONST.__objc_protorefs: 0xd8
+  __DATA_CONST.__objc_superrefs: 0x6b0
   __DATA_CONST.__objc_arraydata: 0x688
   __AUTH_CONST.__auth_got: 0x13c0
   __AUTH_CONST.__auth_ptr: 0x2e8
-  __AUTH_CONST.__const: 0x40f8
-  __AUTH_CONST.__cfstring: 0x11460
-  __AUTH_CONST.__objc_const: 0x24a68
+  __AUTH_CONST.__const: 0x4118
+  __AUTH_CONST.__cfstring: 0x114c0
+  __AUTH_CONST.__objc_const: 0x24f10
   __AUTH_CONST.__objc_intobj: 0x930
   __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x60
-  __AUTH.__objc_data: 0x4d0
+  __AUTH.__objc_data: 0x5c0
   __AUTH.__data: 0x170
-  __DATA.__objc_ivar: 0x16cc
+  __DATA.__objc_ivar: 0x16f0
   __DATA.__data: 0x3390
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x2480
   __DATA_DIRTY.__objc_data: 0x5db8
   __DATA_DIRTY.__data: 0xe98
-  __DATA_DIRTY.__bss: 0x14e8
+  __DATA_DIRTY.__bss: 0x1508
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10692
-  Symbols:   11660
-  CStrings:  14574
+  Functions: 10744
+  Symbols:   11721
+  CStrings:  14621
 
Symbols:
+ _EDCoreAnalyticAccountMapperFile
+ _OBJC_CLASS_$_EDCoreAnalyticAccountMapper
+ _OBJC_CLASS_$_EDCoreAnalyticAccountMapperService
+ _OBJC_CLASS_$_EDCoreAnalyticsBiomeInteractionEventLog
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_METACLASS_$_EDCoreAnalyticAccountMapper
+ _OBJC_METACLASS_$_EDCoreAnalyticAccountMapperService
+ _OBJC_METACLASS_$_EDCoreAnalyticsBiomeInteractionEventLog
+ _kEMPayloadKeyCategorizationEnabled
CStrings:
+ "\f"
+ "-[EDPersistenceDatabaseConnection _fetchTransactionWriteGenerationWithSQLConnection:newGeneration:error:]"
+ "-[EDPersistenceDatabaseConnection _storeTransactionWriteGenerationWithSQLConnection:newGeneration:error:]"
+ "/[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}/"
+ "@\"EDCoreAnalyticAccountMapper\""
+ "@\"EDCoreAnalyticAccountMapperService\""
+ "@\"EDCoreAnalyticsBiomeInteractionEventLog\""
+ "Address string for address %{mask:mailaddr}@ is invalid. Treating as commerce"
+ "B48@0:8@16@24@32@40"
+ "CAAccountMapper.plist"
+ "Cannot verify business display name for address with addressID %lld, due to empty address display name"
+ "Cannot verify business for address with addressID %lld, due to nil address"
+ "EDCoreAnalyticAccountMapper"
+ "EDCoreAnalyticAccountMapperService"
+ "EDCoreAnalyticsBiomeInteractionEventLog"
+ "Failed to categorize message with error %{public}@ sender %{mask:mailaddr}@ isVIP: %{BOOL}d isContact: %{BOOL}d unsubPresent: %{BOOL}d isPrimarySender: %{BOOL}d"
+ "Failed to get redacted address for addressID %lld"
+ "Found addressID %lld is mapped to businessID %lld but display names do not match: businessName: %{public}@, messageName: %{public}@ (%{public}@)"
+ "Recipient %{mask:mailaddr}@ isNotPersonal: %s"
+ "Sender %{mask:mailaddr}@ isVIP: %s isContact: %s unsubPresent: %s isPrimarySender: %s"
+ "T@\"EDCoreAnalyticAccountMapper\",&,V_accountMapper"
+ "T@\"EDCoreAnalyticAccountMapperService\",&,N,V_accountMapperService"
+ "T@\"EDCoreAnalyticsBiomeInteractionEventLog\",R,N,V_coreAnalyticsBiomeEventLog"
+ "T@\"NSDate\",N,V_date"
+ "T@\"NSLock\",&,N,V_lock"
+ "WITH receive_row_num AS (    SELECT accountId,           messageId,           senderId,           receivingAccountDomain,           metadataPrimaryKey,           predictedCategory,           currCategoryView,           reasonCodes,           isAllInboxesCategoriesEnabled AS isAllInboxesBlackPearlEnabled,           isMailAccountPersonalAccount,           isMailAccountCategoriesEnabled AS isMailAccountBlackPearlEnabled,           CASE WHEN receiveTimestamp >= %llu                     THEN TRUE                ELSE FALSE                END AS isL1,           ROW_NUMBER() OVER (PARTITION BY accountId, messageId ORDER BY eventTimestamp DESC) AS rn    FROM \"Mail.CategorizationAnalytics.Receive\"    WHERE receiveTimestamp >= %llu          AND receiveTimestamp < %llu          AND accountId IN (%@) ),receive AS (    SELECT accountId,           messageId,           senderId,           receivingAccountDomain,           metadataPrimaryKey,           predictedCategory,           currCategoryView,           reasonCodes,           isAllInboxesBlackPearlEnabled,           isMailAccountPersonalAccount,           isMailAccountBlackPearlEnabled,           isL1    FROM receive_row_num    WHERE rn = 1),read_row_num AS (    SELECT accountId,           messageId,           readTimestamp,           readWithCategoriesEnabled,           ROW_NUMBER() OVER (PARTITION BY accountId, messageId ORDER BY readTimestamp ASC) AS rn    FROM \"Mail.CategorizationAnalytics.Read\"),read AS (    SELECT accountId,           messageId,           readTimestamp AS firstReadTimestamp,           readWithCategoriesEnabled AS hadFirstReadWithBlackPearlEnabled    FROM read_row_num    WHERE rn = 1),recategorize_row_num AS (    SELECT accountId,           messageId,           currCategoryView,           recategorizationBy,           recategorizeTimestamp,           ROW_NUMBER() OVER (PARTITION BY accountId, messageId ORDER BY recategorizeTimestamp DESC) AS rn    FROM \"Mail.CategorizationAnalytics.Recategorize\"),recategorize AS (    SELECT accountId,           messageId,           currCategoryView,           recategorizationBy,           recategorizeTimestamp AS lastRecategorizeTimestamp    FROM recategorize_row_num    WHERE rn = 1),flattened AS (    SELECT receive.accountId,           receive.messageId,           receive.senderId,           receive.receivingAccountDomain,           receive.metadataPrimaryKey,           receive.isAllInboxesBlackPearlEnabled,           receive.isMailAccountPersonalAccount,           receive.isMailAccountBlackPearlEnabled,           receive.predictedCategory,           COALESCE(recategorize.currCategoryView, receive.currCategoryView) AS currCategoryView,           read.hadFirstReadWithBlackPearlEnabled,           CASE                 WHEN read.firstReadTimestamp IS NOT NULL                         AND recategorize.lastRecategorizeTimestamp IS NULL                     THEN TRUE                WHEN read.firstReadTimestamp IS NULL                         AND recategorize.lastRecategorizeTimestamp IS NOT NULL                     THEN FALSE                WHEN read.firstReadTimestamp IS NOT NULL                         AND recategorize.lastRecategorizeTimestamp IS NOT NULL                         AND read.firstReadTimestamp < recategorize.lastRecategorizeTimestamp                     THEN TRUE                WHEN read.firstReadTimestamp IS NOT NULL                         AND recategorize.lastRecategorizeTimestamp IS NOT NULL                         AND read.firstReadTimestamp >= recategorize.lastRecategorizeTimestamp                     THEN FALSE                WHEN read.firstReadTimestamp IS NULL                         AND recategorize.lastRecategorizeTimestamp IS NULL                     THEN False                ELSE NULL                END AS hadReadBeforeRecat,           receive.reasonCodes,           recategorize.recategorizationBy,           receive.isL1,           ROW_NUMBER() OVER (ORDER BY RANDOM()) AS rn    FROM receive         LEFT JOIN read                 ON receive.accountId = read.accountId                    AND receive.messageId = read.messageId         LEFT JOIN recategorize                 ON receive.accountId = recategorize.accountId                    AND receive.messageId = recategorize.messageId), sampled_msg_cnt AS (    SELECT MIN(500, (ABS(RANDOM()) %% (COUNT(*) - FLOOR(0.9 * COUNT(*)) + 1)) + FLOOR(0.9 * COUNT(*))) AS max_rn    FROM flattened) SELECT accountId,       messageId,       senderId,       receivingAccountDomain,       metadataPrimaryKey,       isAllInboxesBlackPearlEnabled,       isMailAccountPersonalAccount,       isMailAccountBlackPearlEnabled,       predictedCategory,       currCategoryView,       hadFirstReadWithBlackPearlEnabled,       hadReadBeforeRecat,       reasonCodes,       recategorizationBy,       isL1 FROM flattened      JOIN sampled_msg_cnt           ON 1=1 WHERE rn <= max_rn;"
+ "[BlackPearl] [ETL-To-CA] Account Extraction for path %@ error %@"
+ "[BlackPearl][AccountMapper] Failed to remove temporary read URL [%@] error [%@]"
+ "[BlackPearl][AccountMapper] list of Active accounts in order : %@ mailAccounts total count %lu"
+ "_accountMapper"
+ "_accountMapperService"
+ "_allActiveMailAccounts"
+ "_convertMailAccountToAccountMapper"
+ "_coreAnalyticsBiomeEventLog"
+ "_extractAccountIdentifier:"
+ "_findAccountMapping:"
+ "_retrieveBlackPearlConfig"
+ "_retrieveFromDisk"
+ "accountKey: %@, mailAccountInboxesEnabled: %ui"
+ "accountMapper"
+ "accountMapperService"
+ "coreAnalyticsBiomeEventLog"
+ "findAccountId:"
+ "getFileNameURL"
+ "indexOfAccountId:"
+ "initWithAccountProvider:"
+ "initWithReadBiomeCollector:"
+ "isDate:inSameDayAsDate:"
+ "isMailAccountBlackPearlEnabled:accountIdentifier:bbConfig:accountIdentifierTobbConfig:"
+ "logReadEventForMessageID:accountId:readTimestamp:categorizationEnabled:"
+ "q24@?0@\"NSString\"8@\"NSString\"16"
+ "rangeOfFirstMatchInString:options:range:"
+ "regularExpressionWithPattern:options:error:"
+ "saveToDisk"
+ "setAccountMapper:"
+ "setAccountMapperService:"
+ "setLock:"
+ "validate"
- "-[EDPersistenceDatabaseConnection _fetchTransactionWriteGenerationWithSQLConnection:newGeneration:]"
- "-[EDPersistenceDatabaseConnection _storeTransactionWriteGenerationWithSQLConnection:newGeneration:]"
- "Address string for address %{public}@ is invalid. Treating as commerce"
- "Failed to categorize message with error %{public}@ sender %{public}@ isVIP: %{BOOL}d isContact: %{BOOL}d unsubPresent: %{BOOL}d isPrimarySender: %{BOOL}d"
- "Found addressID %@ is mapped to businessID %lld but display names do not match: businessName: %{public}@, messageName: %{public}@ (%{public}@)"
- "Recipient %{public}@ isNotPersonal: %s"
- "Sender %{public}@ isVIP: %s isContact: %s unsubPresent: %s isPrimarySender: %s"
- "T@\"EMCategory\",R,N"
- "WITH receive_row_num AS (    SELECT accountId,           messageId,           senderId,           receivingAccountDomain,           metadataPrimaryKey,           predictedCategory,           currCategoryView,           reasonCodes,           isAllInboxesCategoriesEnabled AS isAllInboxesBlackPearlEnabled,           isMailAccountPersonalAccount,           isMailAccountCategoriesEnabled AS isMailAccountBlackPearlEnabled,           CASE WHEN receiveTimestamp >= %llu                     THEN TRUE                ELSE FALSE                END AS isL1,           ROW_NUMBER() OVER (PARTITION BY accountId, messageId ORDER BY eventTimestamp DESC) AS rn    FROM \"Mail.CategorizationAnalytics.Receive\"    WHERE receiveTimestamp >= %llu          AND receiveTimestamp < %llu          AND accountId IN (%@) ),receive AS (    SELECT accountId,           messageId,           senderId,           receivingAccountDomain,           metadataPrimaryKey,           predictedCategory,           currCategoryView,           reasonCodes,           isAllInboxesBlackPearlEnabled,           isMailAccountPersonalAccount,           isMailAccountBlackPearlEnabled,           isL1    FROM receive_row_num    WHERE rn = 1),read_row_num AS (    SELECT accountId,           messageId,           readTimestamp,           readWithCategoriesEnabled,           ROW_NUMBER() OVER (PARTITION BY accountId, messageId ORDER BY readTimestamp ASC) AS rn    FROM \"Mail.CategorizationAnalytics.Read\"),read AS (    SELECT accountId,           messageId,           readTimestamp AS firstReadTimestamp,           readWithCategoriesEnabled AS hadFirstReadWithBlackPearlEnabled    FROM read_row_num    WHERE rn = 1),recategorize_row_num AS (    SELECT accountId,           messageId,           currCategoryView,           recategorizationBy,           recategorizeTimestamp,           ROW_NUMBER() OVER (PARTITION BY accountId, messageId ORDER BY recategorizeTimestamp DESC) AS rn    FROM \"Mail.CategorizationAnalytics.Recategorize\"),recategorize AS (    SELECT accountId,           messageId,           currCategoryView,           recategorizationBy,           recategorizeTimestamp AS lastRecategorizeTimestamp    FROM recategorize_row_num    WHERE rn = 1),flattened AS (    SELECT receive.accountId,           receive.messageId,           receive.senderId,           receive.receivingAccountDomain,           receive.metadataPrimaryKey,           receive.isAllInboxesBlackPearlEnabled,           receive.isMailAccountPersonalAccount,           receive.isMailAccountBlackPearlEnabled,           receive.predictedCategory,           COALESCE(recategorize.currCategoryView, receive.currCategoryView) AS currCategoryView,           read.hadFirstReadWithBlackPearlEnabled,           CASE                 WHEN read.firstReadTimestamp IS NOT NULL                         AND recategorize.lastRecategorizeTimestamp IS NULL                     THEN TRUE                WHEN read.firstReadTimestamp IS NULL                         AND recategorize.lastRecategorizeTimestamp IS NOT NULL                     THEN FALSE                WHEN read.firstReadTimestamp IS NOT NULL                         AND recategorize.lastRecategorizeTimestamp IS NOT NULL                         AND read.firstReadTimestamp < recategorize.lastRecategorizeTimestamp                     THEN TRUE                WHEN read.firstReadTimestamp IS NOT NULL                         AND recategorize.lastRecategorizeTimestamp IS NOT NULL                         AND read.firstReadTimestamp >= recategorize.lastRecategorizeTimestamp                     THEN FALSE                WHEN read.firstReadTimestamp IS NULL                         AND recategorize.lastRecategorizeTimestamp IS NULL                     THEN False                ELSE NULL                END AS hadReadBeforeRecat,           receive.reasonCodes,           recategorize.recategorizationBy,           receive.isL1,           ROW_NUMBER() OVER (ORDER BY RANDOM()) AS rn    FROM receive         LEFT JOIN read                 ON receive.accountId = read.accountId                    AND receive.messageId = read.messageId         LEFT JOIN recategorize                 ON receive.accountId = recategorize.accountId                    AND receive.messageId = recategorize.messageId), sampled_msg_cnt AS (    SELECT MIN(500, (ABS(RANDOM()) %% (COUNT(*) - FLOOR(0.9 * COUNT(*)) + 1)) + FLOOR(0.9 * COUNT(*))) AS max_rn    FROM flattened) SELECT NULL AS accountId,       messageId,       senderId,       receivingAccountDomain,       metadataPrimaryKey,       isAllInboxesBlackPearlEnabled,       isMailAccountPersonalAccount,       isMailAccountBlackPearlEnabled,       predictedCategory,       currCategoryView,       NULL AS hadFirstReadWithBlackPearlEnabled,       NULL AS hadReadBeforeRecat,       reasonCodes,       recategorizationBy,       isL1 FROM flattened      JOIN sampled_msg_cnt           ON 1=1 WHERE rn <= max_rn;"
- "accountKey: %@, mailAccountInboxesEnabled: %@"
- "logReadEventForMessageID:messageDictionary:"
- "logReadEventForMessages:categoryPersistence:"

```
