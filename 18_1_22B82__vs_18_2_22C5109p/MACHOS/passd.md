## passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

-1591.2.8.2.1
-  __TEXT.__text: 0x50bd9c
-  __TEXT.__auth_stubs: 0x4ff0
-  __TEXT.__objc_stubs: 0x69e60
-  __TEXT.__objc_methlist: 0x2bb5c
+1591.3.6.2.1
+  __TEXT.__text: 0x50d6b8
+  __TEXT.__auth_stubs: 0x4fd0
+  __TEXT.__objc_stubs: 0x6a280
+  __TEXT.__objc_methlist: 0x2bcc4
   __TEXT.__const: 0x191a
-  __TEXT.__cstring: 0x5936b
-  __TEXT.__objc_classname: 0x6911
-  __TEXT.__objc_methtype: 0x12352
-  __TEXT.__gcc_except_tab: 0x94d0
-  __TEXT.__objc_methname: 0x94d64
-  __TEXT.__oslogstring: 0x4c07d
+  __TEXT.__cstring: 0x594bb
+  __TEXT.__objc_classname: 0x693e
+  __TEXT.__objc_methtype: 0x12370
+  __TEXT.__gcc_except_tab: 0x9544
+  __TEXT.__objc_methname: 0x9528e
+  __TEXT.__oslogstring: 0x4c19d
   __TEXT.__ustring: 0x14
   __TEXT.__swift5_typeref: 0x102a
   __TEXT.__constg_swiftt: 0xb7c

   __TEXT.__swift5_types: 0xa0
   __TEXT.__swift5_capture: 0xa94
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x115b8
+  __TEXT.__unwind_info: 0x11628
   __TEXT.__eh_frame: 0xe1c
-  __DATA_CONST.__auth_got: 0x2808
-  __DATA_CONST.__got: 0x3258
-  __DATA_CONST.__auth_ptr: 0x2d8
-  __DATA_CONST.__const: 0x2b0a8
-  __DATA_CONST.__cfstring: 0x2e880
-  __DATA_CONST.__objc_classlist: 0x16e0
+  __DATA_CONST.__auth_got: 0x27f8
+  __DATA_CONST.__got: 0x3268
+  __DATA_CONST.__auth_ptr: 0x2e0
+  __DATA_CONST.__const: 0x2b210
+  __DATA_CONST.__cfstring: 0x2e960
+  __DATA_CONST.__objc_classlist: 0x16f0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x568
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x80
-  __DATA_CONST.__objc_superrefs: 0xe28
+  __DATA_CONST.__objc_superrefs: 0xe30
   __DATA_CONST.__objc_intobj: 0x1308
   __DATA_CONST.__objc_arraydata: 0x588
   __DATA_CONST.__objc_arrayobj: 0x4f8
   __DATA_CONST.__objc_dictobj: 0x280
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x45510
-  __DATA.__objc_selrefs: 0x1cda8
-  __DATA.__objc_ivar: 0x25ac
-  __DATA.__objc_data: 0xef50
+  __DATA.__objc_const: 0x456c0
+  __DATA.__objc_selrefs: 0x1ceb8
+  __DATA.__objc_ivar: 0x25bc
+  __DATA.__objc_data: 0xeff0
   __DATA.__data: 0x4b20
   __DATA.__bss: 0x1390
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 24214
+  Functions: 24257
   Symbols:   2997
-  CStrings:  32469
+  CStrings:  32526
 
Symbols:
+ _OBJC_CLASS_$_PKApplyFooterContent
+ _OBJC_CLASS_$_PKApplyFooterContentLink
+ _PKServiceNotificationsBundleIdentifier
- _PKMagmaEnabled
- _TCCAccessReset
- _kTCCServiceFinancialData
CStrings:
+ "\a2"
+ "-[PDPaymentService transactionsWithFullPaymentHashes:transactionSourceIdentifiers:completion:]_block_invoke"
+ "@48@0:8@16Q24q32@40"
+ "ApplyFooterContent"
+ "ApplyFooterContentLink"
+ "B16@?0@\"PDUserNotification\"8"
+ "CREATE TABLE IF NOT EXISTS footer_content (pid INTEGER, type INTEGER, footer_text TEXT, installment_criteria_pid INTEGER, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS footer_content_link (pid INTEGER, footer_content_pid INTEGER, link_text TEXT, link_url TEXT, terms_identifier TEXT, analytics_identifier TEXT, PRIMARY KEY (pid));"
+ "Cannot insert Service Notification: %!@(MISSING) in Notification Center: %!@(MISSING) as connecting has not completed yet."
+ "J"
+ "Migrating database from user_version 17066 to 17067"
+ "PDUserNotificationCenter: Service Notification Authorization status: %!@(MISSING)"
+ "Service Notification Authorization status granted: %!@(MISSING) error: %!@(MISSING)"
+ "TB,N,V_isServiceNotification"
+ "_internalServiceNotificationCenter"
+ "_isServiceNotification"
+ "_linksWithQuery:"
+ "_migrateFrom17066To17067:context:"
+ "_predicateForFooterContentPID:"
+ "_predicateForType:installmentCriteriaPID:"
+ "_processServiceConnectionOperations"
+ "_propertySettersForFooterContent"
+ "_propertySettersForFooterContentLink"
+ "_propertyValuesForFooterContent:type:"
+ "_propertyValuesForFooterContentLink:"
+ "_registeredServiceCategories"
+ "_serviceCenterConnected"
+ "_serviceNotificationCategories"
+ "_userCenterConnected"
+ "analyticsIdentifier"
+ "analytics_identifier"
+ "deleteAllFooterContentLinksWithFooterContentPID:inDatabase:"
+ "deleteFooterContentWithInstallmentCriteriaPID:inDatabase:"
+ "deleteFooterContentWithType:installmentCriteriaPID:inDatabase:"
+ "disclosureFooter"
+ "footerContent"
+ "footerContentForType:installmentCriteriaPID:inDatabase:"
+ "footerText"
+ "footer_content"
+ "footer_content_link"
+ "footer_content_pid"
+ "footer_text"
+ "initWithFooterContent:type:installmentCriteriaPID:inDatabase:"
+ "initWithFooterContentLink:footerContentPID:inDatabase:"
+ "insertFooterContentLinks:withFooterContentPID:inDatabase:"
+ "insertOrUpdateWithFooterContent:type:installmentCriteriaPID:inDatabase:"
+ "installment_criteria_pid"
+ "isServiceNotification"
+ "linkText"
+ "linkURL"
+ "link_text"
+ "link_url"
+ "links"
+ "linksForFooterContentPID:inDatabase:"
+ "paymentTransactionsInDatabase:withFullPaymentHashes:transactionSourceIdentifiers:"
+ "paymentTransactionsWithFullPaymentHashes:transactionSourceIdentifiers:"
+ "setAnalyticsIdentifier:"
+ "setDisclosureFooter:"
+ "setFooterText:"
+ "setIsServiceNotification:"
+ "setLinkText:"
+ "setLinkURL:"
+ "setLinks:"
+ "transactionsWithFullPaymentHashes:transactionSourceIdentifiers:completion:"
+ "v24@?0@\"PKApplyFooterContent\"8@16"
+ "v24@?0@\"PKApplyFooterContentLink\"8@16"
+ "v40@0:8@\"NSSet\"16@\"NSSet\"24@?<v@?@\"NSArray\">32"
- "-[PDPaymentService transactionsWithFullPaymentHashes:completion:]_block_invoke"
- "Cannot delete issuer installment transactions from the database since the feature is not enabled"
- "Cannot fetch payment offers since the feature is not enabled"
- "Cannot get issuer installment transactions from the database since the feature is not enabled"
- "_connected"
- "paymentTransactionsInDatabase:withFullPaymentHashes:"
- "paymentTransactionsWithFullPaymentHashes:"
- "transactionsWithFullPaymentHashes:completion:"
- "v32@0:8@\"NSSet\"16@?<v@?@\"NSArray\">24"

```
