## NanoPassbookBridgeSettings

> `/System/Library/NanoPreferenceBundles/Applications/NanoPassbookBridgeSettings.bundle/NanoPassbookBridgeSettings`

```diff

-1289.24.0.0.0
-  __TEXT.__text: 0x16bac
-  __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_stubs: 0x3ec0
-  __TEXT.__objc_methlist: 0x1da4
+1329.0.0.0.0
+  __TEXT.__text: 0x14a28
+  __TEXT.__auth_stubs: 0x730
+  __TEXT.__objc_stubs: 0x3f20
+  __TEXT.__objc_methlist: 0x1e54
   __TEXT.__const: 0xa0
-  __TEXT.__objc_methname: 0x6ce0
-  __TEXT.__cstring: 0xec5
-  __TEXT.__objc_classname: 0x3e8
-  __TEXT.__objc_methtype: 0x21b6
-  __TEXT.__gcc_except_tab: 0x680
+  __TEXT.__objc_methname: 0x70e4
+  __TEXT.__cstring: 0xedb
+  __TEXT.__objc_classname: 0x3d1
+  __TEXT.__objc_methtype: 0x24f0
+  __TEXT.__gcc_except_tab: 0x4b8
   __TEXT.__oslogstring: 0x2658
   __TEXT.__ustring: 0x28
   __TEXT.__dlopen_cstrs: 0xbc
-  __TEXT.__unwind_info: 0x6c8
-  __DATA_CONST.__auth_got: 0x378
-  __DATA_CONST.__got: 0x2e8
+  __TEXT.__unwind_info: 0x610
   __DATA_CONST.__const: 0xc10
   __DATA_CONST.__cfstring: 0xae0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA.__objc_const: 0x2b90
-  __DATA.__objc_selrefs: 0x16d8
+  __DATA_CONST.__auth_got: 0x3a8
+  __DATA_CONST.__got: 0x2e8
+  __DATA.__objc_const: 0x2c20
+  __DATA.__objc_selrefs: 0x1760
   __DATA.__objc_ivar: 0xd4
   __DATA.__objc_data: 0x320
   __DATA.__data: 0x6c0

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A9CB67DA-421C-35B0-BAAD-07C73C72307A
+  UUID: 56E5E1DA-FB24-3395-B8DB-13DD3C8C66C3
   Functions: 493
-  Symbols:   235
-  CStrings:  1449
+  Symbols:   241
+  CStrings:  1482
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x2
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x26
+ _objc_retain_x4
+ _objc_retain_x5
- _objc_autorelease
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "@\"NSArray\"24@0:8@\"NSString\"16"
+ "@\"PKPaymentOfferCatalog\"16@0:8"
+ "@\"PKSelectedPaymentOffer\"32@0:8@\"PKSelectedPaymentOffer\"16@\"NSString\"24"
+ "TB,?,N,GisIdentityDocumentWebVerificationEnabled"
+ "allSelectedPaymentOffersForPassUniqueID:"
+ "attemptToDownloadPeerPaymentPassAtURL:withWebService:device:completion:"
+ "identityDocumentWebVerificationEnabled"
+ "insertOrUpdatePaymentOfferConfirmationRecord:completion:"
+ "insertOrUpdatePaymentTransaction:forTransactionSourceIdentifier:completion:"
+ "isBeingPresented"
+ "isIdentityDocumentWebVerificationEnabled"
+ "isMovingFromParentViewController"
+ "isMovingToParentViewController"
+ "isViewLoaded"
+ "paymentOffersCatalog"
+ "paymentOffersForCriteriaIdentifier:selectedPassDetails:sessionIdentifier:sessionDetails:updateReason:fraudAssessment:completion:"
+ "paymentOffersMerchandisingForSessionDetails:merchandisingIdentifiers:needsProvisioningMerchandisingIdentifiers:completion:"
+ "paymentRewardsBalancesWithPassUniqueIdentifier:"
+ "removeSelectedPaymentOffer:associatedWithPassUniqueID:"
+ "sendPaymentOfferPaymentStatusForCriteriaIdentifier:sessionIdentifier:status:"
+ "setIdentityDocumentWebVerificationEnabled:"
+ "updatePaymentOfferConfirmationRecordProcessEvents:forPaymentHash:successfully:completion:"
+ "updatePaymentOffersCatalogWithReason:completion:"
+ "updatePaymentRewardsBalancesWithPassUniqueIdentifier:completion:"
+ "updateSelectedPaymentOffer:forPassUniqueID:"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"PKPaymentOfferConfirmationRecord\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"PKSelectedPaymentOffer\"16@\"NSString\"24"
+ "v32@0:8Q16@?24"
+ "v32@0:8Q16@?<v@?@\"PKPaymentOfferCatalog\"@\"NSError\">24"
+ "v40@0:8@\"NSString\"16@\"NSString\"24Q32"
+ "v40@0:8@\"PKPaymentTransaction\"16@\"NSString\"24@?<v@?@\"PKPaymentTransaction\">32"
+ "v40@0:8@16@24Q32"
+ "v44@0:8Q16@\"NSString\"24B32@?<v@?@\"PKPaymentOfferConfirmationRecord\">36"
+ "v44@0:8Q16@24B32@?36"
+ "v48@0:8@\"PKPaymentOffersSessionDetails\"16@\"NSSet\"24@\"NSSet\"32@?<v@?@\"PKPaymentOfferMerchandisingOfferDetails\"@\"NSError\">40"
+ "v72@0:8@\"NSString\"16@\"PKSelectedPaymentOfferPaymentPassDetails\"24@\"NSString\"32@\"PKPaymentOffersSessionDetails\"40Q48@\"NSString\"56@?<v@?@\"PKPaymentOfferAssessmentCollection\"@\"NSError\">64"
+ "v72@0:8@16@24@32@40Q48@56@?64"
- "attemptToDownloadPeerPaymentPassAtURL:withWebService:completion:"
- "childViewControllers"
- "settingsController:requestsPresentAutofillInformationWithSpecifier:cardDescriptors:authentication:"
- "v48@0:8@\"PKPassbookSettingsController\"16@\"PSSpecifier\"24@\"NSArray\"32@\"NSData\"40"
- "v48@0:8@16@24@32@40"

```
