## CoreCDP

> `/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP`

```diff

-359.4.6.0.0
-  __TEXT.__text: 0x30bec
+359.13.0.0.0
+  __TEXT.__text: 0x312f8
   __TEXT.__auth_stubs: 0x9a0
-  __TEXT.__objc_methlist: 0x279c
+  __TEXT.__objc_methlist: 0x27d4
   __TEXT.__const: 0xe0
   __TEXT.__gcc_except_tab: 0xe28
-  __TEXT.__oslogstring: 0x7237
-  __TEXT.__cstring: 0x27c4
+  __TEXT.__oslogstring: 0x745a
+  __TEXT.__cstring: 0x2860
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0xd9c
+  __TEXT.__ustring: 0x28
+  __TEXT.__unwind_info: 0xda8
   __TEXT.__objc_classname: 0x6b4
-  __TEXT.__objc_methname: 0x7515
+  __TEXT.__objc_methname: 0x7601
   __TEXT.__objc_methtype: 0x184d
-  __TEXT.__objc_stubs: 0x42e0
+  __TEXT.__objc_stubs: 0x43a0
   __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0x12a0
+  __DATA_CONST.__const: 0x12b0
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x7648
-  __DATA_CONST.__objc_selrefs: 0x1b08
+  __DATA_CONST.__objc_const: 0x7678
+  __DATA_CONST.__objc_selrefs: 0x1b38
+  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_classrefs: 0x288
+  __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__objc_const: 0x14f0
-  __AUTH_CONST.__cfstring: 0x2a20
-  __AUTH_CONST.__const: 0x3a0
+  __AUTH_CONST.__cfstring: 0x2aa0
+  __AUTH_CONST.__const: 0x3c0
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x4e0
   __AUTH.__objc_data: 0x780
   __AUTH.__data: 0x8
-  __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x288
-  __DATA.__objc_superrefs: 0xd8
   __DATA.__objc_ivar: 0x278
-  __DATA.__data: 0x790
-  __DATA.__bss: 0x90
+  __DATA.__data: 0x7a0
+  __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0x820
   __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A42BC6F2-99D4-3B27-82C5-896E4E62F72B
-  Functions: 1434
-  Symbols:   4797
-  CStrings:  2705
+  UUID: A5EB7B90-8ACD-39BC-AF5E-5B7C135CD807
+  Functions: 1443
+  Symbols:   4823
+  CStrings:  2727
 
Symbols:
+ +[CDPUtilities isSilentBurnInMiniBuddyEnabled]
+ +[CDPUtilities useCDPContextSecretInsteadOfSBDSecretFeatureEnabled]
+ -[CDPAccountRepresentation isSilentBurnCDPRepairEnabled]
+ -[CDPAccountRepresentation isSilentBurnCDPRepairEnabled].cold.1
+ -[CDPContext _isLocalSecretCachedAcknowledgingInMemoryValue]
+ -[CDPContext _isLocalSecretCachedAcknowledgingInMemoryValue].cold.1
+ -[CDPContext isLocalSecretCached]
+ GCC_except_table22
+ __CDPLogSystemAnalytics
+ __CDPLogSystemAnalytics.log
+ __CDPLogSystemAnalytics.onceToken
+ ___62-[CDPAccountRepresentation isICDPEnabledByCheckingWithServer:]_block_invoke.45
+ ____CDPLogSystemAnalytics_block_invoke
+ ___block_literal_global.10
+ ___block_literal_global.124
+ ___block_literal_global.16
+ ___block_literal_global.46
+ ___block_literal_global.64
+ ___block_literal_global.97
+ _objc_msgSend$_isLocalSecretCachedAcknowledgingInMemoryValue
+ _objc_msgSend$_useSecureBackupCachedPassphrase
+ _objc_msgSend$cachedLocalSecret
+ _objc_msgSend$cachedPassphraseMissing
+ _objc_msgSend$isSilentBurnCDPRepairEnabledForAccount:
+ _objc_msgSend$useCDPContextSecretInsteadOfSBDSecretFeatureEnabled
- ___62-[CDPAccountRepresentation isICDPEnabledByCheckingWithServer:]_block_invoke.43
- ___block_literal_global.123
- ___block_literal_global.14
- ___block_literal_global.40
- ___block_literal_global.63
- ___block_literal_global.96
CStrings:
+ "\"%@: Assuming silent burn in mini-buddy is disabled\""
+ "\"%@: Calling to fetch user info for altDSID (%{mask.hash}@) for 'silentEscrowRecordRepairEnabled' value\""
+ "\"%@: Checking iCDP status for account with DSID (%{mask.hash}@), will check with server (%{BOOL}d)\""
+ "\"%@: Failed to check if iCDP is enabled for account with DSID (%{mask.hash}@) with error (%@)\""
+ "\"%@: Generated context (%@) for account with DSID (%{mask.hash}@)\""
+ "\"%@: Returning %@ for 'isSilentBurnCDPRepairEnabled'\""
+ "\"%@: Unable to check 'isSilentBurnCDPRepairEnabled' because AKAccountManager (%@) doesn't respond to selector\""
+ "\"%@: iCDP status for account with DSID (%{mask.hash}@) is %@\""
+ "\"%s: Found a cached secret that was just an empty string.\""
+ "\"CDPCircleProxyImpl: appleID:%{mask.hash}@, dsid: %{mask.hash}@, type: %ld\""
+ "\"CDPCircleProxyImpl: fetching OT Status for altDSID: %{mask.hash}@\""
+ "\"CDPFollowUpContext: set altDSID to %{mask.hash}@\""
+ "\"CDPSOSCircleProxyImpl: appleID:%{mask.hash}@, dsid: %{mask.hash}@, type: %ld\""
+ "\"Checking iCDP status for DSID %{mask.hash}@ (checkWithServer=%{BOOL}d)\""
+ "\"Failed to fetch user info for altDSID (%{mask.hash}@) with error (%@)\""
+ "\"Failed to find account for altDSID: %{mask.hash}@\""
+ "\"Failed to find account for dsid: %{mask.hash}@\""
+ "\"OT CRK uuid %@ is %@ to AA custodianID %@\""
+ "\"Returning server fetched 'silentEscrowRecordRepairEnabled' value (%@) for altDSID (%{mask.hash}@)\""
+ "\"XPC Error while checking if iCDP is enabled for DSID %{mask.hash}@: %@\""
+ "\"_registerCredentialsOnlyIfNeeded: appleID:%{mask.hash}@, dsid: %{mask.hash}@, type: %ld\""
+ "\"iCDP status for DSID %{mask.hash}@ is %@\""
+ "-[CDPContext _isLocalSecretCachedAcknowledgingInMemoryValue]"
+ "Circle Missing"
+ "MiniBuddy"
+ "SilentBurnInMiniBuddy"
+ "T@\"NSString\",?,R,C"
+ "UseCDPContextSecretInsteadOfSBDSecret"
+ "_isLocalSecretCachedAcknowledgingInMemoryValue"
+ "analytics"
+ "e"
+ "isLocalSecretCached"
+ "isSilentBurnCDPRepairEnabled"
+ "isSilentBurnCDPRepairEnabledForAccount:"
+ "isSilentBurnInMiniBuddyEnabled"
+ "n"
+ "useCDPContextSecretInsteadOfSBDSecretFeatureEnabled"
- "\"%@: Calling to fetch user info for altDSID (%@) for 'silentEscrowRecordRepairEnabled' value\""
- "\"%@: Checking iCDP status for account with DSID (%@), will check with server (%{BOOL}d)\""
- "\"%@: Failed to check if iCDP is enabled for account with DSID (%@) with error (%@)\""
- "\"%@: Generated context (%@) for account with DSID (%@)\""
- "\"%@: iCDP status for account with DSID (%@) is %@\""
- "\"CDPCircleProxyImpl: appleID:%@, dsid: %@, type: %ld\""
- "\"CDPCircleProxyImpl: fetching OT Status for altDSID: %@\""
- "\"CDPFollowUpContext: set altDSID to %@\""
- "\"CDPSOSCircleProxyImpl: appleID:%@, dsid: %@, type: %ld\""
- "\"Checking iCDP status for DSID %@ (checkWithServer=%i)\""
- "\"Failed to fetch user info for altDSID (%@) with error (%@)\""
- "\"Failed to find account for altDSID: %@\""
- "\"Failed to find account for dsid: %@\""
- "\"Returning server fetched 'silentEscrowRecordRepairEnabled' value (%@) for altDSID (%@)\""
- "\"XPC Error while checking if iCDP is enabled for DSID %@: %@\""
- "\"_registerCredentialsOnlyIfNeeded: appleID:%@, dsid: %@, type: %ld\""
- "\"iCDP status for DSID %@ is %@\""

```
