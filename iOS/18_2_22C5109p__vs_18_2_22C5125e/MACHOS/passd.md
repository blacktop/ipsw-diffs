## passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

-1591.3.6.2.1
-  __TEXT.__text: 0x50d6b8
-  __TEXT.__auth_stubs: 0x4fd0
-  __TEXT.__objc_stubs: 0x6a280
-  __TEXT.__objc_methlist: 0x2bcc4
+1591.3.8.0.0
+  __TEXT.__text: 0x50f130
+  __TEXT.__auth_stubs: 0x4fc0
+  __TEXT.__objc_stubs: 0x6a400
+  __TEXT.__objc_methlist: 0x2bd1c
   __TEXT.__const: 0x191a
-  __TEXT.__cstring: 0x594bb
-  __TEXT.__objc_classname: 0x693e
-  __TEXT.__objc_methtype: 0x12370
-  __TEXT.__gcc_except_tab: 0x9544
-  __TEXT.__objc_methname: 0x9528e
-  __TEXT.__oslogstring: 0x4c19d
+  __TEXT.__cstring: 0x5968b
+  __TEXT.__objc_classname: 0x693f
+  __TEXT.__objc_methtype: 0x12395
+  __TEXT.__gcc_except_tab: 0x9594
+  __TEXT.__objc_methname: 0x95565
+  __TEXT.__oslogstring: 0x4c34d
   __TEXT.__ustring: 0x14
   __TEXT.__swift5_typeref: 0x102a
   __TEXT.__constg_swiftt: 0xb7c

   __TEXT.__swift5_types: 0xa0
   __TEXT.__swift5_capture: 0xa94
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x11628
+  __TEXT.__unwind_info: 0x11478
   __TEXT.__eh_frame: 0xe1c
-  __DATA_CONST.__auth_got: 0x27f8
-  __DATA_CONST.__got: 0x3268
+  __DATA_CONST.__auth_got: 0x27f0
+  __DATA_CONST.__got: 0x32e0
   __DATA_CONST.__auth_ptr: 0x2e0
-  __DATA_CONST.__const: 0x2b210
-  __DATA_CONST.__cfstring: 0x2e960
+  __DATA_CONST.__const: 0x2b358
+  __DATA_CONST.__cfstring: 0x2eae0
   __DATA_CONST.__objc_classlist: 0x16f0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x568

   __DATA_CONST.__objc_arrayobj: 0x4f8
   __DATA_CONST.__objc_dictobj: 0x280
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x456c0
-  __DATA.__objc_selrefs: 0x1ceb8
-  __DATA.__objc_ivar: 0x25bc
+  __DATA.__objc_const: 0x457a0
+  __DATA.__objc_selrefs: 0x1cf28
+  __DATA.__objc_ivar: 0x25cc
   __DATA.__objc_data: 0xeff0
   __DATA.__data: 0x4b20
   __DATA.__bss: 0x1390

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 24257
-  Symbols:   2997
-  CStrings:  32526
+  Functions: 24274
+  Symbols:   3011
+  CStrings:  32570
 
Symbols:
+ _OBJC_CLASS_$_PKBadgeCountItem
+ _PKPassKeyAccessibilityURL
+ _PKPassKeyAddOnURL
+ _PKPassKeyBagPolicyURL
+ _PKPassKeyContactVenueEmail
+ _PKPassKeyContactVenuePhoneNumber
+ _PKPassKeyContactVenueWebsite
+ _PKPassKeyDirectionsInformationURL
+ _PKPassKeyMerchandiseURL
+ _PKPassKeyOrderFoodURL
+ _PKPassKeyParkingInformationURL
+ _PKPassKeyPurchaseParkingURL
+ _PKPassKeySellURL
+ _PKPassKeyTransferURL
+ _PKPassKeyTransitInformationURL
- _PKPayWithRewardsEnabled
CStrings:
+ "\x01\x19"
+ "\t\x12\x11"
+ "\t%!@(MISSING)"
+ "\x14\x1b\x14\x16"
+ "@\"PKPaymentOfferInstallmentCriteria\""
+ "Anonymous peer payment pass (pending payment)"
+ "Badge count for savings account"
+ "Badge count items changed:"
+ "Badged application message registrations count"
+ "CREATE TABLE IF NOT EXISTS cow (pid INTEGER, c_pid INTEGER, a TEXT, b INTEGER, c INTEGER, d TEXT, e TEXT, h TEXT, j TEXT, k INTEGER, l INTEGER, m TEXT, r TEXT, s TEXT, t TEXT, u TEXT, v TEXT, w INTEGER, x TEXT, y BOOL, z TEXT, aa TEXT, ab TEXT, localized_pay_in_full_subtitle_override TEXT, has_preconfigured_offers TEXT, PRIMARY KEY (pid));"
+ "CREATE TABLE IF NOT EXISTS honey (pid INTEGER, a INTEGER, b TEXT, c BLOB, d TEXT, document_type TEXT NOT NULL, e TEXT, f TEXT, PRIMARY KEY(pid));"
+ "Device assessment education visible"
+ "Discovery items"
+ "Migrating database from user_version 17067 to 17068"
+ "Migrating database from user_version 17068 to 17069"
+ "Migrating database from user_version 17069 to 17070"
+ "New account user invitations"
+ "PDAppletSubcredentialManager.credential.register"
+ "PDAppletSubcredentialManager.pass.download"
+ "PDPeerPaymentWebServiceCoordinator.pass.download"
+ "PDRemoteInterfacePresenter: invalidated boost assertion %!p(MISSING)."
+ "PDRemoteInterfacePresenter: unexpectedly invalidated boost assertion %!p(MISSING) - %!@(MISSING)."
+ "Pass requiring verification"
+ "Past due broadway account"
+ "Pay Later Account financing plan dispute (%!@(MISSING))"
+ "Pay Later Account fraud suspected"
+ "Pay Later installments with status"
+ "T@\"PKPaymentOfferInstallmentCriteria\",&,N,V_installmentCriteria"
+ "T@\"PKPaymentOfferInstallmentCriteria\",R,N,V_installmentCriteria"
+ "Transaction not a maps reprocessing or CloudKit update, skip clearing merchant"
+ "Transaction not a maps reprocessing update or CloudKit update, skip clearing brand"
+ "Unanswered question on the broadway pass"
+ "_badgeCountItemsForPayLaterWithAccount:"
+ "_installmentCriteria"
+ "_lastLoggedBadgeCountItems"
+ "_migrateFrom17067To17068:context:"
+ "_migrateFrom17068To17069:context:"
+ "_migrateFrom17069To17070:context:"
+ "_passbookUIServiceBoostGraceTimeout"
+ "_sendMessage:toEndpoint:completion:"
+ "badgeCountItems"
+ "badgeCountItemsAccess"
+ "badgeCountItemsWithCompletion:"
+ "criteriaWithType:passUniqueID:"
+ "hasPreconfiguredOffers"
+ "has_preconfigured_offers"
+ "has_preconfigured_offers TEXT"
+ "initWithPaymentTransaction:forPassUniqueIdentifier:paymentApplication:familyMember:accountUser:installmentCriteria:"
+ "initWithPaymentTransaction:forPassUniqueIdentifier:paymentApplication:familyMember:balance:accountUser:installmentCriteria:"
+ "initWithTitle:subtitle:count:"
+ "installmentCriteria"
+ "primaryIdentifier"
+ "q24@?0@\"PKBadgeCountItem\"8@\"PKBadgeCountItem\"16"
+ "setHasPreconfiguredOffers:"
+ "setInstallmentCriteria:"
+ "updateIngestedDate:forPassWithUniqueID:"
- "\x01\x18"
- "\t\x12"
- "\x14\x1b\x13\x16"
- "CREATE TABLE IF NOT EXISTS cow (pid INTEGER, c_pid INTEGER, a TEXT, b INTEGER, c INTEGER, d TEXT, e TEXT, h TEXT, j TEXT, k INTEGER, l INTEGER, m TEXT, r TEXT, s TEXT, t TEXT, u TEXT, v TEXT, w INTEGER, x TEXT, y BOOL, z TEXT, aa TEXT, ab TEXT, localized_pay_in_full_subtitle_override TEXT, PRIMARY KEY (pid));"
- "CREATE TABLE IF NOT EXISTS honey (pid INTEGER, a INTEGER, b TEXT, c BLOB, d TEXT, document_type TEXT NOT NULL, PRIMARY KEY(pid));"
- "Cannot fetch rewards balance since the feature is not enabled"
- "Cannot fetch rewards redemptions since the feature is not enabled"
- "Cannot get payment rewards redemptions from the database since the feature is not enabled"
- "PDPeerPaymentWebServiceCoordinator.write_peer_payment_pass"
- "PDRemoteInterfacePresenter: invalidated boost assertion %!p(MISSING)..."
- "_badgeCount"
- "_badgeCountForPayLaterWithAccount:"
- "_badgeCountForSavingsWithAccount:"
- "initWithPaymentTransaction:forPassUniqueIdentifier:paymentApplication:familyMember:balance:accountUser:"
- "v24@?0@\"NSURL\"8@?<v@?@\"PKPaymentPass\"@\"NSError\">16"

```
