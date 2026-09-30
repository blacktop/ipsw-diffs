## AppAttestInternal

> `/System/Library/PrivateFrameworks/AppAttestInternal.framework/Versions/A/AppAttestInternal`

```diff

-  __TEXT.__text: 0x6c3a0
+  __TEXT.__text: 0x6bb28
   __TEXT.__objc_methlist: 0x6c4
   __TEXT.__const: 0x4490
   __TEXT.__cstring: 0x69be

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0xe8
-  __DATA_CONST.__got: 0x4b0
+  __DATA_CONST.__got: 0x4d8
   __AUTH_CONST.__const: 0x3198
   __AUTH_CONST.__cfstring: 0x1a20
   __AUTH_CONST.__objc_const: 0x1938

   __DATA.__objc_ivar: 0x40
   __DATA.__data: 0x4a8
   __DATA.__bss: 0x3750
-  __DATA.__common: 0x38
+  __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x838
-  __DATA_DIRTY.__data: 0xc00
+  __DATA_DIRTY.__data: 0xc10
   __DATA_DIRTY.__bss: 0x1370
-  __DATA_DIRTY.__common: 0x150
+  __DATA_DIRTY.__common: 0x158
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
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
~ ___46+[AppAttestTaskCreator createForDefaultAttest]_block_invoke : 284 -> 272
~ ___54+[AppAttestTaskCreator createForWebAuthAttestKeychain]_block_invoke : 600 -> 576
~ ___53+[AppAttestTaskCreator createForDeviceAttestKeychain]_block_invoke : 600 -> 576
~ -[PinnedUrlDelegate URLSession:didReceiveChallenge:completionHandler:] : 940 -> 916
~ ___sendServerRequestWithError_block_invoke : 936 -> 924
~ _AppAttest_WebAuthentication_AttestKey : 1136 -> 1124
~ ___AppAttest_WebAuthentication_AttestKey_block_invoke : 1504 -> 1480
~ _resolveAppUUIDKeychain : 5340 -> 5136
~ _saveAppUUIDKeychain : 916 -> 892
~ _encodeKeyToCOSE : 1432 -> 1396
~ _fetchPublicKey : 1244 -> 1196
~ _generateCOSEForKeySize : 1104 -> 1080
~ _generateEnvironmentByAppSigning : 1712 -> 1640
~ _extractApplicationIdentifiers : 1604 -> 1592
~ _generateAttestationObject : 1432 -> 1396
~ _generateAssertionObject : 832 -> 820
~ _saveCredentialKeychain : 720 -> 696
~ _loadCredentialKeychain : 772 -> 748
~ _deleteCredentialKeychainWithLabel : 564 -> 540
~ _getAllCredentialKeychainLabelsWithShouldExit : 560 -> 548
~ _saveAssertionCounterKeychain : 832 -> 808
~ _loadAssertionCounterKeychain : 860 -> 836
~ _deleteAssertionCounterKeychainWithLabel : 564 -> 540
~ _getAllAssertionCounterKeychainLabelsWithShouldExit : 560 -> 548
~ _getApplicationIdentifierHashFromKeychainLabel : 380 -> 368
~ _getAllAppUUIDKeychainLabelsWithShouldExit : 1920 -> 1880
~ _removeAllKeychainItemsForMissingAppsWithShouldExit : 1160 -> 1124
~ _listOfInstalledAppHashesWithShouldExit : 980 -> 948
~ _listOfAllowlistedDaemonHashesWithShouldExit : 1076 -> 1044
~ _listOfInstalledExtensionHashesWithShouldExit : 948 -> 932
~ ___removeAllKeychainItemsForMissingAppsWithShouldExit_block_invoke : 2124 -> 2040
~ __removeAllKeychainItemsForMissingAppsWithShouldExit_block_invoke.116 : 852 -> 824
~ __removeAllKeychainItemsForMissingAppsWithShouldExit_block_invoke.119 : 852 -> 824
~ -[AppAttestEligibilityManager isEligibleClientFor:] : 864 -> 816
~ -[AppAttestEligibilityManager isEligibleApplicationExtensionFor:] : 1300 -> 1264
~ -[AppAttestEligibilityManager isEligibleDaemonFor:] : 1432 -> 1360
~ -[AppAttestEligibilityManager isEligibleForPrivService:] : 700 -> 664
~ -[AppAttestEligibilityManager containsValidEntitlements] : 1388 -> 1340
~ -[AppAttestEligibilityManager fetchEntitlementForAuditToken:withKey:] : 1088 -> 1064
~ -[AppAttestEligibilityManager meetsSecurityControlsForAuditToken:] : 1764 -> 1680
~ -[AppAttestEligibilityManager fetchBundleRecordFor:] : 780 -> 756
~ _AppAttest_DeviceAttestation_AttestKey : 3992 -> 3896
~ ___AppAttest_DeviceAttestation_AttestKey_block_invoke : 2140 -> 2080
~ _fetchAlwaysAccessibleKeysEntitlement : 704 -> 692
~ _fetchOptInEntitlements : 1036 -> 1000
~ _fetchCdHash : 448 -> 436
~ _AppAttest_AppAttestation_IsEligibleApplication : 336 -> 324
~ _AppAttest_AppAttestation_IsSupportedAndEligibleApplication : 292 -> 280
~ _CreateKey : 2248 -> 2224
~ _AttestKey : 4096 -> 3976
~ _AppAttest_AppAttestation_Assert : 820 -> 808
~ _Assert : 2672 -> 2624
~ _Sign : 2856 -> 2772
~ _GetKey : 2020 -> 1960
~ ___AttestKey_block_invoke : 3160 -> 3064
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/AppAttestInternal/Source/Core/AppAttestEligibilityManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/AppAttestInternal/Source/Core/AppAttestHandler.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/AppAttestInternal/Source/Core/Controllers/BundleRecordController.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/AppAttestInternal/Source/Core/Controllers/KeychainController.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/AppAttestInternal/Source/Core/Controllers/SecurityController+Extensions.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/AppAttestInternal/Source/Core/Controllers/SecurityController.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/AppAttestInternal/Source/Core/DeviceAttestHandler.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AppUUIDDataManager.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AssertionCBORManager.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AssertionDataManager.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AttestationCBORManager.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AttestationManager.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AuthenticationManager.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/EligibilityManager.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/IdentityManager.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/KeyDataManager.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/AppAttestInternal/Source/Core/Utility/KeyUtility.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/AppAttestInternal/Source/Core/Utility/SecKey+AppAttestInternal.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/AppAttestInternal/Source/Core/support/AnonymousAttestation.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/AppAttestInternal/Source/Core/support/AppAttestation.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestAppAttestation.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestDeviceAttestation.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestTaskCreator.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestUtils.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestWebAuthentication.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/FeatureFlags/DeviceCheck.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VVt6At/Sources/TwoBit/FeatureFlags/FeatureFlagsManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/AppAttestInternal/Source/Core/AppAttestEligibilityManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/AppAttestInternal/Source/Core/AppAttestHandler.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/AppAttestInternal/Source/Core/Controllers/BundleRecordController.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/AppAttestInternal/Source/Core/Controllers/KeychainController.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/AppAttestInternal/Source/Core/Controllers/SecurityController+Extensions.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/AppAttestInternal/Source/Core/Controllers/SecurityController.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/AppAttestInternal/Source/Core/DeviceAttestHandler.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AppUUIDDataManager.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AssertionCBORManager.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AssertionDataManager.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AttestationCBORManager.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AttestationManager.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AuthenticationManager.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/EligibilityManager.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/IdentityManager.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/KeyDataManager.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/AppAttestInternal/Source/Core/Utility/KeyUtility.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/AppAttestInternal/Source/Core/Utility/SecKey+AppAttestInternal.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/AppAttestInternal/Source/Core/support/AnonymousAttestation.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/AppAttestInternal/Source/Core/support/AppAttestation.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestAppAttestation.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestDeviceAttestation.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestTaskCreator.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestUtils.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestWebAuthentication.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/FeatureFlags/DeviceCheck.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QCEAAc/Sources/TwoBit/FeatureFlags/FeatureFlagsManager.m"

```
