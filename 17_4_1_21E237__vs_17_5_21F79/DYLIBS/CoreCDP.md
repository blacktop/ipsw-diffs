## CoreCDP

> `/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP`

```diff

-359.13.0.0.0
-  __TEXT.__text: 0x312f8
+359.21.0.0.0
+  __TEXT.__text: 0x316f0
   __TEXT.__auth_stubs: 0x9a0
-  __TEXT.__objc_methlist: 0x27d4
+  __TEXT.__objc_methlist: 0x2814
   __TEXT.__const: 0xe0
   __TEXT.__gcc_except_tab: 0xe28
-  __TEXT.__oslogstring: 0x745a
-  __TEXT.__cstring: 0x2860
+  __TEXT.__oslogstring: 0x7506
+  __TEXT.__cstring: 0x29dd
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0xda8
-  __TEXT.__objc_classname: 0x6b4
-  __TEXT.__objc_methname: 0x7601
-  __TEXT.__objc_methtype: 0x184d
-  __TEXT.__objc_stubs: 0x43a0
+  __TEXT.__unwind_info: 0xddc
+  __TEXT.__objc_classname: 0x6b6
+  __TEXT.__objc_methname: 0x76f9
+  __TEXT.__objc_methtype: 0x1861
+  __TEXT.__objc_stubs: 0x4420
   __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0x12b0
+  __DATA_CONST.__const: 0x1308
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x7678
-  __DATA_CONST.__objc_selrefs: 0x1b38
+  __DATA_CONST.__objc_const: 0x76d8
+  __DATA_CONST.__objc_selrefs: 0x1b68
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_classrefs: 0x288
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__objc_const: 0x14f0
-  __AUTH_CONST.__cfstring: 0x2aa0
+  __AUTH_CONST.__cfstring: 0x2c40
   __AUTH_CONST.__const: 0x3c0
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28

   __AUTH_CONST.__auth_got: 0x4e0
   __AUTH.__objc_data: 0x780
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x278
-  __DATA.__data: 0x7a0
-  __DATA.__bss: 0x98
+  __DATA.__objc_ivar: 0x280
+  __DATA.__data: 0x7f8
+  __DATA.__bss: 0x40
   __DATA_DIRTY.__objc_data: 0x820
   __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1443
-  Symbols:   4823
-  CStrings:  2386
+  Functions: 1451
+  Symbols:   4856
+  CStrings:  2414
 
Symbols:
+ +[CDPFollowUpContext contextForADPUpsell]
+ +[CDPFollowUpContext contextForADPUpsell].cold.1
+ -[CDPContext adpCohort]
+ -[CDPContext adpCohort].cold.1
+ -[CDPContext setAdpCohort:]
+ -[CDPCustodianRecoveryInfo initWithWrappedRKC:wrappingKey:custodianUUID:recordBuildVersion:]
+ -[CDPCustodianRecoveryInfo recordBuildVersion]
+ GCC_except_table31
+ _CDPFollowUpUIExtensionIdentifier
+ _CDP_FOLLOWUP_ADP_UPSELL
+ _OBJC_IVAR_$_CDPContext._adpCohort
+ _OBJC_IVAR_$_CDPCustodianRecoveryInfo._recordBuildVersion
+ ___36-[CDPAccount isOTEnabledForContext:]_block_invoke.35
+ ___51+[CDPAccount isICDPEnabledForDSID:checkWithServer:]_block_invoke.23
+ ___62-[CDPAccountRepresentation isICDPEnabledByCheckingWithServer:]_block_invoke.51
+ ___73-[CDPStateUIProviderProxy cdpContext:promptForLocalSecretWithCompletion:]_block_invoke.31
+ ___block_literal_global.31
+ ___block_literal_global.34
+ _kADPUpsellCFURefreshed
+ _kADPUpsellCFURejected
+ _kADPUpsellCFUTriggered
+ _kADPUpsellLandingPageSetUpLaterIniCloudSettingsEscapeOffer
+ _kADPUpsellLandingPageTurnOnEscapeOffer
+ _kADPUpsellLandingPageViewed
+ _kCDPAnalyticsADPCohortType
+ _kCDPAnalyticsRecordBuildVersion
+ _kCDP_AKADPCohortKey
+ _objc_msgSend$adpCohort
+ _objc_msgSend$adpCohortForAccount:
+ _objc_msgSend$initWithWrappedRKC:wrappingKey:custodianUUID:recordBuildVersion:
+ _objc_msgSend$recordBuildVersion
- GCC_except_table27
- ___36-[CDPAccount isOTEnabledForContext:]_block_invoke.29
- ___51+[CDPAccount isICDPEnabledForDSID:checkWithServer:]_block_invoke.17
- ___62-[CDPAccountRepresentation isICDPEnabledByCheckingWithServer:]_block_invoke.45
- ___73-[CDPStateUIProviderProxy cdpContext:promptForLocalSecretWithCompletion:]_block_invoke.25
- ___block_literal_global.25
- ___block_literal_global.28
CStrings:
+ "\x02e\x11\x15u$"
+ "\x04"
+ "\"%@: ADP Cohort type is %@\""
+ "\"%@: Unable to obtain the adpCohortForAccount because AKAccountManager (%@) doesn't respond to selector.\""
+ "\"Creating context for ADP Upsell CFU\""
+ "<%@: %p> for UUID: %@ recordBuildVersion: %@"
+ "@48@0:8@16@24@32@40"
+ "T@\"NSNumber\",C,N,V_adpCohort"
+ "T@\"NSString\",R,C,N,V_recordBuildVersion"
+ "_adpCohort"
+ "_recordBuildVersion"
+ "adpCh"
+ "adpCohort"
+ "adpCohortForAccount:"
+ "com.apple.CoreCDPUI.CDPFollowUpExtension"
+ "com.apple.corecdp.adpUpsellCFURejected"
+ "com.apple.corecdp.adpUpsellCFUTriggered"
+ "com.apple.corecdp.adpUpsellLandingPageView"
+ "com.apple.corecdp.cfuRefreshed"
+ "com.apple.dataaccess.adpupsell.setuplater"
+ "com.apple.dataaccess.adpupsell.turnon"
+ "contextForADPUpsell"
+ "initWithWrappedRKC:wrappingKey:custodianUUID:recordBuildVersion:"
+ "kADPUpsell"
+ "recordBuildVersion"
+ "setAdpCohort:"
+ "telemetryVersion"
- "\x02e\x11\x15u#"
- "<%@: %p> for UUID: %@"

```
