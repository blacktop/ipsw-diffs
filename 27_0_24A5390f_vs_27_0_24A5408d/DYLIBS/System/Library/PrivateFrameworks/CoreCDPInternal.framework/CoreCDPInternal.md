## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-445.0.0.0.0
-  __TEXT.__text: 0x8dbdc
+447.0.0.0.0
+  __TEXT.__text: 0x8dda4
   __TEXT.__objc_methlist: 0x568c
   __TEXT.__const: 0x888
-  __TEXT.__oslogstring: 0x14a5e
-  __TEXT.__cstring: 0xe055
-  __TEXT.__gcc_except_tab: 0xb94
+  __TEXT.__oslogstring: 0x14a9e
+  __TEXT.__cstring: 0xe0c5
+  __TEXT.__gcc_except_tab: 0xb68
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0x3b7
   __TEXT.__swift5_fieldmd: 0x80

   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift_as_cont: 0x68
-  __TEXT.__unwind_info: 0x1df8
+  __TEXT.__unwind_info: 0x1e10
   __TEXT.__eh_frame: 0x8f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x220
-  __DATA_CONST.__got: 0x10b8
+  __DATA_CONST.__got: 0x10f0
   __AUTH_CONST.__const: 0xad0
-  __AUTH_CONST.__cfstring: 0x94c0
+  __AUTH_CONST.__cfstring: 0x9520
   __AUTH_CONST.__objc_const: 0x100b0
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0xc0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3158
-  Symbols:   5791
-  CStrings:  2806
+  Functions: 3159
+  Symbols:   5798
+  CStrings:  2809
 
Symbols:
+ _kAAAnalyticsEventRCOwnerCustodianCountMatch
+ _kAAAnalyticsEventRCOwnerEscapeOfferTapped
+ _kAAAnalyticsEventRCOwnerFlowOutcome
+ _kAAAnalyticsEventRCOwnerGetCodeLanding
+ _kAAAnalyticsEventRCOwnerPrivateChannelCreated
+ _kAAAnalyticsEventRCOwnerRecoveryLanding
+ _kSecureBackupDBRKey
Functions:
~ _OUTLINED_FUNCTION_4 : 12 -> 20
~ _OUTLINED_FUNCTION_4 : 28 -> 12
+ _OUTLINED_FUNCTION_4
~ ___46+[CDPDAnalyticsTransport getAllowedDIDCEvents]_block_invoke : 488 -> 520
~ +[CDPDAnalyticsTransport approvedRecoveryContactEventsForDIDCAndDNU] : 1824 -> 1996
~ -[CDPInternalWalrusStateController _fetchiCDPAccountInfoDictionaryWithContext:error:] : 436 -> 500
~ -[CDPWalrusDaemonService combinedWalrusStatusWithContext:completion:].cold.2 : 136 -> 124
~ ___77-[CDPWalrusDaemonService updateWalrusStatus:authenticatedContext:completion:]_block_invoke.cold.1 : 52 -> 120
~ -[CDPWalrusDaemonService _checkWalrusBeforeFetchingPCSKeysForServices:pcsController:completion:].cold.2 : 52 -> 64
~ ___71-[CDPWalrusDaemonService _pcsKeysForServices:pcsController:completion:]_block_invoke.cold.2 : 52 -> 64
~ ___87-[CDPInternalWalrusStateController _retryWalrusStateUpdate:context:account:completion:]_block_invoke.cold.1 : 52 -> 140
CStrings:
+ "Failed to update walrus status with error: domain=%{public}@ code=%{public}ld"
+ "Silent re-authentication prior to Walrus re-try failed with error: domain=%{public}@ code=%{public}ld"
+ "com.apple.authkit.pac.signature"
+ "com.apple.authkit.pac.subscriptionInfo"
+ "com.apple.authkit.pac.subscriptionSource"
- "Failed to update walrus status with error: %@"
- "Silent re-authentication prior to Walrus re-try failed with error: %@"
```
