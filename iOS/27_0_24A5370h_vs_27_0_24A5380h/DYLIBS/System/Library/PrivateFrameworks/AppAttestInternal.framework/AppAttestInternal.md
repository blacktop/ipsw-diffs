## AppAttestInternal

> `/System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal`

```diff

-  __TEXT.__text: 0x6a460
+  __TEXT.__text: 0x69b10
   __TEXT.__objc_methlist: 0x6c4
   __TEXT.__const: 0x4550
   __TEXT.__cstring: 0x64ee

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0xe8
-  __DATA_CONST.__got: 0x4c0
+  __DATA_CONST.__got: 0x4e8
   __AUTH_CONST.__const: 0x3128
   __AUTH_CONST.__cfstring: 0x1aa0
   __AUTH_CONST.__objc_const: 0x1938

   __DATA.__objc_ivar: 0x40
   __DATA.__data: 0x498
   __DATA.__bss: 0x38d0
-  __DATA.__common: 0x38
+  __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x838
-  __DATA_DIRTY.__data: 0xbf8
-  __DATA_DIRTY.__bss: 0x13a0
-  __DATA_DIRTY.__common: 0x150
+  __DATA_DIRTY.__data: 0xc08
+  __DATA_DIRTY.__bss: 0x13b0
+  __DATA_DIRTY.__common: 0x151
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Functions:
~ ___45+[FeatureFlagsManager isModernizationEnabled]_block_invoke : 240 -> 228
~ ___35+[FeatureFlagsManager isMacEnabled]_block_invoke : 240 -> 228
~ ___52+[FeatureFlagsManager isExtensionAttestationEnabled]_block_invoke : 240 -> 228
~ ___46+[AppAttestTaskCreator createForDefaultAttest]_block_invoke : 272 -> 260
~ ___54+[AppAttestTaskCreator createForWebAuthAttestKeychain]_block_invoke : 576 -> 552
~ ___53+[AppAttestTaskCreator createForDeviceAttestKeychain]_block_invoke : 576 -> 552
~ -[PinnedUrlDelegate URLSession:didReceiveChallenge:completionHandler:] : 888 -> 864
~ ___sendServerRequestWithError_block_invoke : 872 -> 860
~ _AppAttest_WebAuthentication_AttestKey : 1092 -> 1080
~ ___AppAttest_WebAuthentication_AttestKey_block_invoke : 1424 -> 1400
~ _resolveAppUUIDKeychain : 5428 -> 5188
~ _saveAppUUIDKeychain : 852 -> 828
~ _encodeKeyToCOSE : 1400 -> 1364
~ _fetchPublicKey : 1220 -> 1172
~ _generateCOSEForKeySize : 1032 -> 1008
~ _generateEnvironmentByAppSigning : 1888 -> 1804
~ _resolveAppAttestApplicationIdentifiersForApplicationRecord : 948 -> 928
~ _extractApplicationIdentifiers : 2164 -> 2140
~ _generateAttestationObject : 1352 -> 1316
~ _generateAssertionObject : 768 -> 756
~ _saveCredentialKeychain : 680 -> 656
~ _loadCredentialKeychain : 732 -> 708
~ _deleteCredentialKeychainWithLabel : 548 -> 524
~ _getAllCredentialKeychainLabelsWithShouldExit : 544 -> 532
~ _saveAssertionCounterKeychain : 776 -> 752
~ _loadAssertionCounterKeychain : 812 -> 788
~ _deleteAssertionCounterKeychainWithLabel : 548 -> 524
~ _getAllAssertionCounterKeychainLabelsWithShouldExit : 544 -> 532
~ _getApplicationIdentifierHashFromKeychainLabel : 368 -> 356
~ _getAllAppUUIDKeychainLabelsWithShouldExit : 1876 -> 1836
~ _removeAllKeychainItemsForMissingAppsWithShouldExit : 1116 -> 1080
~ _listOfInstalledAppHashesWithShouldExit : 952 -> 920
~ _listOfAllowlistedDaemonHashesWithShouldExit : 1048 -> 1012
~ _listOfInstalledExtensionHashesWithShouldExit : 916 -> 900
~ ___removeAllKeychainItemsForMissingAppsWithShouldExit_block_invoke : 2048 -> 1964
~ ___removeAllKeychainItemsForMissingAppsWithShouldExit_block_invoke.130 : 840 -> 812
~ ___removeAllKeychainItemsForMissingAppsWithShouldExit_block_invoke.133 : 840 -> 812
~ -[AppAttestEligibilityManager isEligibleClientFor:] : 864 -> 816
~ -[AppAttestEligibilityManager isEligibleApplicationFor:] : 536 -> 512
~ -[AppAttestEligibilityManager isEligibleApplicationExtensionFor:] : 2580 -> 2484
~ -[AppAttestEligibilityManager isEligibleDaemonFor:] : 1416 -> 1344
~ -[AppAttestEligibilityManager isEligibleForPrivService:] : 696 -> 660
~ -[AppAttestEligibilityManager containsValidEntitlements] : 1368 -> 1320
~ -[AppAttestEligibilityManager fetchEntitlementForAuditToken:withKey:] : 1056 -> 1032
~ -[AppAttestEligibilityManager meetsSecurityControlsForAuditToken:] : 1752 -> 1668
~ -[AppAttestEligibilityManager fetchBundleRecordFor:] : 756 -> 732
~ _AppAttest_DeviceAttestation_AttestKey : 3852 -> 3756
~ ___AppAttest_DeviceAttestation_AttestKey_block_invoke : 2052 -> 1992
~ _fetchAlwaysAccessibleKeysEntitlement : 692 -> 680
~ _fetchOptInEntitlements : 1020 -> 984
~ _fetchCdHash : 444 -> 432
~ _AppAttest_AppAttestation_IsEligibleApplication : 332 -> 320
~ _AppAttest_AppAttestation_IsSupportedAndEligibleApplication : 484 -> 460
~ _CreateKey : 2144 -> 2084
~ _AttestKey : 3932 -> 3812
~ _AppAttest_AppAttestation_Assert : 780 -> 768
~ _Assert : 2600 -> 2552
~ _Sign : 2756 -> 2672
~ _GetKey : 1952 -> 1892
~ ___AttestKey_block_invoke : 3032 -> 2936

```
