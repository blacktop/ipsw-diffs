## Passbook

> `/private/var/staged_system_apps/Passbook.app/Passbook`

```diff

-1591.6.7.0.0
-  __TEXT.__text: 0xd994
-  __TEXT.__auth_stubs: 0x5c0
-  __TEXT.__objc_stubs: 0x26a0
+1619.6.3.0.0
+  __TEXT.__text: 0xde74
+  __TEXT.__auth_stubs: 0x5e0
+  __TEXT.__objc_stubs: 0x28a0
   __TEXT.__objc_methlist: 0x7c4
   __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0x64
-  __TEXT.__objc_methname: 0x3a25
-  __TEXT.__cstring: 0x609
+  __TEXT.__gcc_except_tab: 0x78
+  __TEXT.__objc_methname: 0x3cc2
+  __TEXT.__cstring: 0x5e9
   __TEXT.__oslogstring: 0x52a
   __TEXT.__objc_classname: 0x138
-  __TEXT.__objc_methtype: 0xc40
-  __TEXT.__unwind_info: 0x268
-  __DATA_CONST.__auth_got: 0x2f0
-  __DATA_CONST.__got: 0x880
-  __DATA_CONST.__const: 0x770
+  __TEXT.__objc_methtype: 0xc68
+  __TEXT.__unwind_info: 0x248
+  __DATA_CONST.__auth_got: 0x300
+  __DATA_CONST.__got: 0x8b0
+  __DATA_CONST.__const: 0x738
   __DATA_CONST.__cfstring: 0x340
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA.__objc_const: 0x8c0
-  __DATA.__objc_selrefs: 0xcf8
+  __DATA.__objc_selrefs: 0xd78
   __DATA.__objc_ivar: 0x58
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x368

   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
-  - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
   - /System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI
   - /System/Library/PrivateFrameworks/PassKitUIFoundation.framework/PassKitUIFoundation
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 35FD8D52-7F70-3C3C-80DD-EE60B2D9F8A3
-  Functions: 153
-  Symbols:   375
-  CStrings:  667
+  UUID: 28FD73A2-3D43-316A-87FF-12CB4C0743FB
+  Functions: 152
+  Symbols:   383
+  CStrings:  683
 
Symbols:
+ _OBJC_CLASS_$_PKPassGroupsViewNavigationController
+ _OBJC_CLASS_$_PKWalletAppShortcutProviderWrapper
+ _PKAnalyticsSubjectAttribution
+ _PKApplePayUserEducationDemoSourceFromString
+ _PKURLActionApplePayUserEducationDemo
+ _PKURLActionHowToUseWallet
+ _PKURLActionPaymentOffers
+ _PKURLActionPaymentOffersCriteriaIdentifier
+ _PKURLActionPaymentOffersProductIdentifier
+ _PKURLActionPaymentSetupSelectSection
+ _PKURLActionRouteAccount
+ _PKURLActionRoutePeerPaymentAddMoney
+ _PKURLApplePayUserEducationDemoSourceKey
+ _PKUserNotificationActionQueryItemConfirmPaymentOfferPlan
+ _PKUserNotificationActionRouteFPANCardConsent
+ __UISolariumFeatureFlagEnabled
- _OBJC_CLASS_$_PKNavigationDashboardPassViewController
- _PKURLActionRoutePayLaterFPSPaymentPass
- _PKURLActionRoutePayLaterPaymentPass
- _PKURLActionRoutePayLaterPaymentPassDetailsAction
- _PKURLActionRoutePayLaterPaymentPassLoan
- _PKUserNotificationActionQueryItemFinancingPlanIdentifier
- _PKUserNotificationActionRouteImportSafariCardConsent
- _PKUserNotificationActionRoutePayLaterViewFinancingPlan
CStrings:
+ "@\"PKPassGroupsViewNavigationController\""
+ "_backgroundQueue"
+ "_navigationController"
+ "accountIdentifierFromSpotlightIdentifier:"
+ "accountWithIdentifier:completion:"
+ "boolValue"
+ "clearFPANCardImportNotificationsWithCompletion:"
+ "dashboardPassGroupViewController"
+ "feature"
+ "forceModalPresentationFromButton:"
+ "indexOfObject:"
+ "initWithPassGroupsViewController:"
+ "paymentSetupProductIdentifierFromSpotlightIdentifier:"
+ "presentAddFPANCardAnimated:preflight:selectedCredentials:referralSource:completion:"
+ "presentApplePayUserEducationDemoFromSource:"
+ "presentHowToUseWalletWithCardLotIdentifier:"
+ "presentImportFPANCardConsentAnimated:referralSource:completion:"
+ "presentPaymentOfferCriteriaIdentifier:productIdentifier:"
+ "presentPaymentSetupInMode:referrerIdentifier:paymentNetwork:transitNetworkIdentifier:allowedFeatureIdentifiers:productIdentifiers:sectionIdentifier:"
+ "presentPeerPaymentPassAnimated:referrerIdentifier:completion:"
+ "presentTransactionDetailsForTransactionWithIdentifier:confirmPaymentOfferPlan:"
+ "presentTransactionDetailsForTransactionWithServiceIdentifier:transactionSourceIdentifier:confirmPaymentOfferPlan:"
+ "reportCampaignIdentifier:eventType:referralSource:deepLinkType:productType:"
+ "setPrefersExternalPresentation:"
+ "setWithObject:"
+ "updateAppShortcutParametersWithCompletion:"
+ "visibleDashboardPassGroupViewController"
- "_discoveryItemsBackgroundQueue"
- "_foregroundActiveResourcesBackgroundQueue"
- "clearSafariCardImportNotificationsWithCompletion:"
- "com.apple.passkit.di.background"
- "forcePaymentPresentationFromButton:"
- "presentImportSafariCardConsentAnimated:referralSource:completion:"
- "presentPayLaterFinancingPlanWithIdentifier:"
- "presentPayLaterPassAnimated:completion:"
- "presentPaymentSetupInMode:referrerIdentifier:paymentNetwork:transitNetworkIdentifier:allowedFeatureIdentifiers:productIdentifiers:"
- "presentTransactionDetailsForTransactionWithIdentifier:"
- "presentTransactionDetailsForTransactionWithServiceIdentifier:transactionSourceIdentifier:"

```
