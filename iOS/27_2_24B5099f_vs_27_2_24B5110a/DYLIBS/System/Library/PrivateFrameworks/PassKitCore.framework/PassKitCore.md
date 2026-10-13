## PassKitCore

> `/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore`

```diff

-1696.2.8.1.0
-  __TEXT.__text: 0x8f23bc
-  __TEXT.__objc_methlist: 0x72a98
+1696.2.9.0.0
+  __TEXT.__text: 0x8f19f8
+  __TEXT.__objc_methlist: 0x72a68
   __TEXT.__const: 0x2d760
   __TEXT.__swift5_typeref: 0x8da0
-  __TEXT.__cstring: 0x741ce
+  __TEXT.__cstring: 0x741b8
   __TEXT.__constg_swiftt: 0x7588
   __TEXT.__swift5_reflstr: 0x664d
   __TEXT.__swift5_fieldmd: 0x7de0

   __TEXT.__swift5_types2: 0x4
   __TEXT.__gcc_except_tab: 0x6ae8
   __TEXT.__ustring: 0x1e6c
-  __TEXT.__unwind_info: 0x27268
+  __TEXT.__unwind_info: 0x27250
   __TEXT.__eh_frame: 0x8978
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x238c8
+  __DATA_CONST.__const: 0x23898
   __DATA_CONST.__objc_classlist: 0x3e48
   __DATA_CONST.__objc_catlist: 0x110
   __DATA_CONST.__objc_protolist: 0x5d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x25420
+  __DATA_CONST.__objc_selrefs: 0x25408
   __DATA_CONST.__objc_protorefs: 0x260
   __DATA_CONST.__objc_superrefs: 0x3158
   __DATA_CONST.__objc_arraydata: 0x2810
   __DATA_CONST.__got: 0x53a0
   __AUTH_CONST.__const: 0x27208
-  __AUTH_CONST.__cfstring: 0x7a620
-  __AUTH_CONST.__objc_const: 0xd07b0
+  __AUTH_CONST.__cfstring: 0x7a540
+  __AUTH_CONST.__objc_const: 0xd07c0
   __AUTH_CONST.__objc_arrayobj: 0xd20
   __AUTH_CONST.__objc_intobj: 0x11d0
   __AUTH_CONST.__objc_dictobj: 0x15b8

   __AUTH.__data: 0x59a8
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0x734c
+  __DATA.__objc_ivar: 0x7348
   __DATA.__data: 0xa2b0
   __DATA.__common: 0xc49
-  __DATA_DIRTY.__objc_ivar: 0x1f50
+  __DATA_DIRTY.__objc_ivar: 0x1f58
   __DATA_DIRTY.__objc_data: 0x7940
   __DATA_DIRTY.__data: 0x188
-  __DATA_DIRTY.__bss: 0x1358
+  __DATA_DIRTY.__bss: 0x1348
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 55942
-  Symbols:   79224
-  CStrings:  21824
+  Functions: 55937
+  Symbols:   79209
+  CStrings:  21817
 
Symbols:
+ +[PKAnalyticsReporter(Attribution) reportCampaignIdentifier:eventType:referralSource:deepLinkType:productType:]
+ +[PKPaymentAuthorizationErrorStateParam paramWithError:requiresExtendedDisplayDuration:]
+ -[PKPaymentAuthorizationErrorStateParam requiresExtendedDisplayDuration]
+ -[PKPaymentAuthorizationErrorStateParam setRequiresExtendedDisplayDuration:]
+ -[PKPaymentProvisioningController allowsUserGeneratedPass]
+ -[PKPaymentProvisioningController includePrecursorPasses]
+ -[PKPaymentProvisioningController setAllowsUserGeneratedPass:]
+ -[PKPaymentProvisioningController setIncludePrecursorPasses:]
+ _OBJC_IVAR_$_PKPaymentAuthorizationErrorStateParam._requiresExtendedDisplayDuration
+ _OBJC_IVAR_$_PKPaymentProvisioningController._allowsUserGeneratedPass
+ _OBJC_IVAR_$_PKPaymentProvisioningController._includePrecursorPasses
+ _PKRemoteNetworkPaymentHostAllowGuestCodeScan
+ _PKRemoteNetworkPaymentHostAllowGuestCodeScanKey
+ _PKRemoteNetworkPaymentHostAllowPersonaCodeScan
+ _PKRemoteNetworkPaymentHostAllowPersonaCodeScanKey
+ _PKRemoteNetworkPaymentHostAllowPersonaDisabledPersonalContentCodeScan
+ _PKRemoteNetworkPaymentHostAllowPersonaDisabledPersonalContentCodeScanKey
- +[PKAnalyticsReporter(Attribution) isNewToWalletUser]
- +[PKAnalyticsReporter(Attribution) reportCampaignIdentifier:eventType:referralSource:deepLinkType:productType:newToWalletUser:newToProductUser:]
- -[PKPaymentProvisioningController allowUserGeneratedPassInUnsupportedRegion]
- -[PKPaymentProvisioningController setAllowUserGeneratedPassInUnsupportedRegion:]
- -[PKProvisioningAnalyticsSession reportNCCCheck]
- -[PKProvisioningAnalyticsSessionCampaignAttributionSubjectHandle reportNCCCheckWithState:]
- -[PKProvisioningAnalyticsState campaignAttributionNewToProductUser]
- -[PKProvisioningAnalyticsState campaignAttributionNewToWalletUser]
- -[PKProvisioningAnalyticsState campaignAttributionReferralSource]
- -[PKProvisioningAnalyticsState setCampaignAttributionNewToProductUser:]
- -[PKProvisioningAnalyticsState setCampaignAttributionNewToWalletUser:]
- _OBJC_IVAR_$_PKPaymentProvisioningController._allowUserGeneratedPassInUnsupportedRegion
- _OBJC_IVAR_$_PKProvisioningAnalyticsSession._didReportNCCCheck
- _OBJC_IVAR_$_PKProvisioningAnalyticsState._campaignAttributionNewToProductUser
- _OBJC_IVAR_$_PKProvisioningAnalyticsState._campaignAttributionNewToWalletUser
- _PKAnalyticsReportNewToCreditUserKey
- _PKAnalyticsReportNewToDebitUserKey
- _PKAnalyticsReportNewToTransitUserKey
- _PKAnalyticsReportNewToWalletUserKey
- _PKCurrentSecureElementPasses
- _PKISO23220_1_PhotoID_FamilyNameUnicode
- _PKISO23220_1_PhotoID_GivenNameUnicode
- _PKISO23220_1_PhotoID_IssuingAuthorityUnicode
- _PKPendingCampaignAttributionCampaignIdentifierKey
- _PKPendingCampaignAttributionForPassUniqueIdentifier
- _PKPendingCampaignAttributionNewToProductUserKey
- _PKPendingCampaignAttributionNewToWalletUserKey
- _PKPendingCampaignAttributionProductTypeKey
- _PKPendingCampaignAttributionReferralSourceKey
- _PKRemovePendingCampaignAttributionForPassUniqueIdentifier
- _PKSetLocalSecureElementPassesProvider
- _PKSetPendingCampaignAttributionForPassUniqueIdentifier
CStrings:
+ "PKRemoteNetworkPaymentHostAllowGuestCodeScan"
+ "PKRemoteNetworkPaymentHostAllowPersonaCodeScan"
+ "PKRemoteNetworkPaymentHostAllowPersonaDisabledPersonalContentCodeScan"
+ "requiresExtendedDisplayDuration: '%@'; "
- "PKPendingCampaignAttributionKey"
- "appleAccount"
- "campaignAttributionNewToProductUser"
- "campaignAttributionNewToWalletUser"
- "cardReadyToUse"
- "nccCheck"
- "newToCreditUser"
- "newToDebitUser"
- "newToProductUser"
- "newToTransitUser"
- "newToWalletUser"
```
