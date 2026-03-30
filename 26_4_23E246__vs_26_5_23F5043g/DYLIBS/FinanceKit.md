## FinanceKit

> `/System/Library/Frameworks/FinanceKit.framework/FinanceKit`

```diff

-310.4.18.0.0
-  __TEXT.__text: 0x6700f8
+310.5.1.0.0
+  __TEXT.__text: 0x670384
   __TEXT.__auth_stubs: 0x5350
-  __TEXT.__objc_methlist: 0x4388
-  __TEXT.__const: 0x6c328
-  __TEXT.__cstring: 0x12703
+  __TEXT.__objc_methlist: 0x4390
+  __TEXT.__const: 0x6c368
+  __TEXT.__cstring: 0x12723
   __TEXT.__oslogstring: 0x83c8
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__swift5_typeref: 0x1599a
   __TEXT.__constg_swiftt: 0x1448c
-  __TEXT.__swift5_reflstr: 0xf683
-  __TEXT.__swift5_fieldmd: 0x188f4
+  __TEXT.__swift5_reflstr: 0xf6c3
+  __TEXT.__swift5_fieldmd: 0x18924
   __TEXT.__swift5_builtin: 0x528
   __TEXT.__swift5_assocty: 0x2cb0
   __TEXT.__swift5_proto: 0x5dbc

   __TEXT.__swift_as_entry: 0x8c0
   __TEXT.__swift_as_ret: 0xa20
   __TEXT.__swift5_mpenum: 0x1d0
-  __TEXT.__unwind_info: 0x1c518
+  __TEXT.__unwind_info: 0x1c530
   __TEXT.__eh_frame: 0x2ed44
   __TEXT.__objc_classname: 0x468b
-  __TEXT.__objc_methname: 0x14ca5
+  __TEXT.__objc_methname: 0x14d25
   __TEXT.__objc_methtype: 0x1bb3
-  __TEXT.__objc_stubs: 0x10260
+  __TEXT.__objc_stubs: 0x102a0
   __DATA_CONST.__got: 0x1508
-  __DATA_CONST.__const: 0x4938
+  __DATA_CONST.__const: 0x4948
   __DATA_CONST.__objc_classlist: 0xac8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4668
+  __DATA_CONST.__objc_selrefs: 0x4678
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x1c0
   __AUTH_CONST.__auth_got: 0x29b8
   __AUTH_CONST.__const: 0x38488
   __AUTH_CONST.__cfstring: 0x480
-  __AUTH_CONST.__objc_const: 0x14d68
+  __AUTH_CONST.__objc_const: 0x14da8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x5dd8
   __AUTH.__data: 0xac90
-  __DATA.__objc_ivar: 0x3fc
+  __DATA.__objc_ivar: 0x400
   __DATA.__data: 0xfe30
   __DATA.__bss: 0xa8a20
   __DATA.__common: 0x210
   __DATA_DIRTY.__objc_data: 0x3800
-  __DATA_DIRTY.__data: 0x8270
+  __DATA_DIRTY.__data: 0x8280
   __DATA_DIRTY.__bss: 0xb980
   __DATA_DIRTY.__common: 0xb8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BF887F8E-D223-3A60-BCB2-CF223A5BE6E9
-  Functions: 40083
-  Symbols:   16746
-  CStrings:  6170
+  UUID: 838B41F1-DCCF-3555-8543-80B3F9853382
+  Functions: 40091
+  Symbols:   16753
+  CStrings:  6175
 
Symbols:
+ -[FKInstitution acceptsNewConsents]
+ -[FKInstitution initWithInstitutionIdentifier:name:reconsentType:supportedAuthTypes:firstTransactionsRequestWindow:maxAgeTransactionsFirstRequest:maxAgeTransactionsRefreshRequest:extensionsBundleIdentifiers:maximumNumberOfBackgroundRefreshes:numberOfRemainingBackgroundRefreshes:backgroundRefreshRetryAfterDate:lastBackgroundRefreshDate:backgroundRefreshConfirmationWindow:backgroundRefreshConfirmationExpiryWindow:multipleConsentsEnabled:termsAndConditions:problemReportingEnabled:financialLabEnabled:consentSyncingEnabled:balanceWidgetEnabled:personalizedInsightsEnabled:supportsTransactions:consentSyncingOutdatedTokenWaitTimeout:timestampSuitableForUserDisplay:piiRedactionConfigurationCountryCodes:privacyLabels:accountMatchType:accountsLimitedToCurrency:acceptsNewConsents:]
+ _OBJC_IVAR_$_FKInstitution._acceptsNewConsents
+ _keypath_get_selector_acceptsNewConsents
+ _objc_msgSend$acceptsNewConsents
+ _objc_msgSend$initWithInstitutionIdentifier:name:reconsentType:supportedAuthTypes:firstTransactionsRequestWindow:maxAgeTransactionsFirstRequest:maxAgeTransactionsRefreshRequest:extensionsBundleIdentifiers:maximumNumberOfBackgroundRefreshes:numberOfRemainingBackgroundRefreshes:backgroundRefreshRetryAfterDate:lastBackgroundRefreshDate:backgroundRefreshConfirmationWindow:backgroundRefreshConfirmationExpiryWindow:multipleConsentsEnabled:termsAndConditions:problemReportingEnabled:financialLabEnabled:consentSyncingEnabled:balanceWidgetEnabled:personalizedInsightsEnabled:supportsTransactions:consentSyncingOutdatedTokenWaitTimeout:timestampSuitableForUserDisplay:piiRedactionConfigurationCountryCodes:privacyLabels:accountMatchType:accountsLimitedToCurrency:acceptsNewConsents:
+ _objc_msgSend$setAcceptsNewConsents:
- -[FKInstitution initWithInstitutionIdentifier:name:reconsentType:supportedAuthTypes:firstTransactionsRequestWindow:maxAgeTransactionsFirstRequest:maxAgeTransactionsRefreshRequest:extensionsBundleIdentifiers:maximumNumberOfBackgroundRefreshes:numberOfRemainingBackgroundRefreshes:backgroundRefreshRetryAfterDate:lastBackgroundRefreshDate:backgroundRefreshConfirmationWindow:backgroundRefreshConfirmationExpiryWindow:multipleConsentsEnabled:termsAndConditions:problemReportingEnabled:financialLabEnabled:consentSyncingEnabled:balanceWidgetEnabled:personalizedInsightsEnabled:supportsTransactions:consentSyncingOutdatedTokenWaitTimeout:timestampSuitableForUserDisplay:piiRedactionConfigurationCountryCodes:privacyLabels:accountMatchType:accountsLimitedToCurrency:]
- _objc_msgSend$initWithInstitutionIdentifier:name:reconsentType:supportedAuthTypes:firstTransactionsRequestWindow:maxAgeTransactionsFirstRequest:maxAgeTransactionsRefreshRequest:extensionsBundleIdentifiers:maximumNumberOfBackgroundRefreshes:numberOfRemainingBackgroundRefreshes:backgroundRefreshRetryAfterDate:lastBackgroundRefreshDate:backgroundRefreshConfirmationWindow:backgroundRefreshConfirmationExpiryWindow:multipleConsentsEnabled:termsAndConditions:problemReportingEnabled:financialLabEnabled:consentSyncingEnabled:balanceWidgetEnabled:personalizedInsightsEnabled:supportsTransactions:consentSyncingOutdatedTokenWaitTimeout:timestampSuitableForUserDisplay:piiRedactionConfigurationCountryCodes:privacyLabels:accountMatchType:accountsLimitedToCurrency:
CStrings:
+ "@204@0:8@16@24Q32s40@44d52d60@68q76q84@92@100@108@116B124@128B136B140B144B148B152B156@160B168@172s180@184@192B200"
+ "TB,R,N,V_acceptsNewConsents"
+ "_acceptsNewConsents"
+ "acceptsNewConsents"
+ "initWithInstitutionIdentifier:name:reconsentType:supportedAuthTypes:firstTransactionsRequestWindow:maxAgeTransactionsFirstRequest:maxAgeTransactionsRefreshRequest:extensionsBundleIdentifiers:maximumNumberOfBackgroundRefreshes:numberOfRemainingBackgroundRefreshes:backgroundRefreshRetryAfterDate:lastBackgroundRefreshDate:backgroundRefreshConfirmationWindow:backgroundRefreshConfirmationExpiryWindow:multipleConsentsEnabled:termsAndConditions:problemReportingEnabled:financialLabEnabled:consentSyncingEnabled:balanceWidgetEnabled:personalizedInsightsEnabled:supportsTransactions:consentSyncingOutdatedTokenWaitTimeout:timestampSuitableForUserDisplay:piiRedactionConfigurationCountryCodes:privacyLabels:accountMatchType:accountsLimitedToCurrency:acceptsNewConsents:"
+ "setAcceptsNewConsents:"
- "@200@0:8@16@24Q32s40@44d52d60@68q76q84@92@100@108@116B124@128B136B140B144B148B152B156@160B168@172s180@184@192"
- "initWithInstitutionIdentifier:name:reconsentType:supportedAuthTypes:firstTransactionsRequestWindow:maxAgeTransactionsFirstRequest:maxAgeTransactionsRefreshRequest:extensionsBundleIdentifiers:maximumNumberOfBackgroundRefreshes:numberOfRemainingBackgroundRefreshes:backgroundRefreshRetryAfterDate:lastBackgroundRefreshDate:backgroundRefreshConfirmationWindow:backgroundRefreshConfirmationExpiryWindow:multipleConsentsEnabled:termsAndConditions:problemReportingEnabled:financialLabEnabled:consentSyncingEnabled:balanceWidgetEnabled:personalizedInsightsEnabled:supportsTransactions:consentSyncingOutdatedTokenWaitTimeout:timestampSuitableForUserDisplay:piiRedactionConfigurationCountryCodes:privacyLabels:accountMatchType:accountsLimitedToCurrency:"

```
