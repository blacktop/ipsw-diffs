## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/Versions/A/CoreCDPInternal`

```diff

-445.0.0.0.0
-  __TEXT.__text: 0x93acc
+447.0.0.0.0
+  __TEXT.__text: 0x93cdc
   __TEXT.__objc_methlist: 0x555c
   __TEXT.__const: 0x890
-  __TEXT.__oslogstring: 0x145fa
-  __TEXT.__cstring: 0xdae6
-  __TEXT.__gcc_except_tab: 0xb48
+  __TEXT.__oslogstring: 0x1463a
+  __TEXT.__cstring: 0xdb56
+  __TEXT.__gcc_except_tab: 0xb1c
   __TEXT.__dlopen_cstrs: 0xbc
   __TEXT.__constg_swiftt: 0x1e4
   __TEXT.__swift5_typeref: 0x3b8

   __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift_as_cont: 0x68
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1e00
+  __TEXT.__unwind_info: 0x1e18
   __TEXT.__eh_frame: 0x8f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x220
-  __DATA_CONST.__got: 0x1088
+  __DATA_CONST.__got: 0x10c0
   __AUTH_CONST.__const: 0x2d90
-  __AUTH_CONST.__cfstring: 0x90e0
+  __AUTH_CONST.__cfstring: 0x9140
   __AUTH_CONST.__objc_const: 0xfb08
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0xc0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3170
-  Symbols:   5871
-  CStrings:  2753
+  Functions: 3172
+  Symbols:   5878
+  CStrings:  2756
 
Symbols:
+ _kAAAnalyticsEventRCOwnerCustodianCountMatch
+ _kAAAnalyticsEventRCOwnerEscapeOfferTapped
+ _kAAAnalyticsEventRCOwnerFlowOutcome
+ _kAAAnalyticsEventRCOwnerGetCodeLanding
+ _kAAAnalyticsEventRCOwnerPrivateChannelCreated
+ _kAAAnalyticsEventRCOwnerRecoveryLanding
+ _kSecureBackupDBRKey
Functions:
~ ___46+[CDPDAnalyticsTransport getAllowedDIDCEvents]_block_invoke : 520 -> 552
~ +[CDPDAnalyticsTransport approvedRecoveryContactEventsForDIDCAndDNU] : 1876 -> 2056
~ -[CDPDPDPRecoveryController setupPDPStateWithCompletion:] : 740 -> 736
+ _OUTLINED_FUNCTION_4
~ -[CDPInternalWalrusStateController _fetchiCDPAccountInfoDictionaryWithContext:error:] : 472 -> 544
~ -[CDPWalrusDaemonService combinedWalrusStatusWithContext:completion:].cold.2 : 140 -> 128
~ __77-[CDPWalrusDaemonService updateWalrusStatus:authenticatedContext:completion:]_block_invoke.cold.1 : 52 -> 124
~ -[CDPWalrusDaemonService _checkWalrusBeforeFetchingPCSKeysForServices:pcsController:completion:].cold.2 : 52 -> 64
~ __71-[CDPWalrusDaemonService _pcsKeysForServices:pcsController:completion:]_block_invoke.cold.2 : 52 -> 64
+ -[CDPDSecureBackupController supportsWalrusRecoveryKeyWithError:].cold.1
~ __87-[CDPInternalWalrusStateController _retryWalrusStateUpdate:context:account:completion:]_block_invoke.cold.1 : 52 -> 144
CStrings:
+ "Failed to update walrus status with error: domain=%{public}@ code=%{public}ld"
+ "Silent re-authentication prior to Walrus re-try failed with error: domain=%{public}@ code=%{public}ld"
+ "com.apple.authkit.pac.signature"
+ "com.apple.authkit.pac.subscriptionInfo"
+ "com.apple.authkit.pac.subscriptionSource"
- "Failed to update walrus status with error: %@"
- "Silent re-authentication prior to Walrus re-try failed with error: %@"
```
