## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount`

```diff

-1027.0.0.0.0
-  __TEXT.__text: 0xdfaac
+1030.0.0.0.0
+  __TEXT.__text: 0xddaec
   __TEXT.__auth_stubs: 0x1180
-  __TEXT.__objc_methlist: 0xabcc
-  __TEXT.__const: 0x2240
-  __TEXT.__cstring: 0xed47
-  __TEXT.__oslogstring: 0xf9b9
-  __TEXT.__gcc_except_tab: 0x23f0
-  __TEXT.__dlopen_cstrs: 0x2d9
+  __TEXT.__objc_methlist: 0xac04
+  __TEXT.__const: 0x2250
+  __TEXT.__cstring: 0xed77
+  __TEXT.__oslogstring: 0xfa19
+  __TEXT.__gcc_except_tab: 0x240c
+  __TEXT.__dlopen_cstrs: 0x325
   __TEXT.__constg_swiftt: 0x2d8
   __TEXT.__swift5_typeref: 0x2ed
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_reflstr: 0xc9
+  __TEXT.__swift5_reflstr: 0xc4
   __TEXT.__swift5_fieldmd: 0x1cc
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_proto: 0x64
   __TEXT.__swift5_types: 0x34
-  __TEXT.__swift5_capture: 0x80
+  __TEXT.__swift5_capture: 0x90
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
-  __TEXT.__unwind_info: 0x2e68
-  __TEXT.__eh_frame: 0x3c0
+  __TEXT.__unwind_info: 0x2ea0
+  __TEXT.__eh_frame: 0x3e8
   __TEXT.__objc_classname: 0x1f36
-  __TEXT.__objc_methname: 0x15581
-  __TEXT.__objc_methtype: 0x2f2e
-  __TEXT.__objc_stubs: 0xc040
-  __DATA_CONST.__got: 0xd68
-  __DATA_CONST.__const: 0x3a20
+  __TEXT.__objc_methname: 0x1565d
+  __TEXT.__objc_methtype: 0x2f4a
+  __TEXT.__objc_stubs: 0xc060
+  __DATA_CONST.__got: 0xd70
+  __DATA_CONST.__const: 0x3a30
   __DATA_CONST.__objc_classlist: 0x7d8
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4d60
+  __DATA_CONST.__objc_selrefs: 0x4d80
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x560
   __DATA_CONST.__objc_arraydata: 0xe0
   __AUTH_CONST.__auth_got: 0x8d0
-  __AUTH_CONST.__const: 0x5c90
-  __AUTH_CONST.__cfstring: 0xcb80
-  __AUTH_CONST.__objc_const: 0x23410
+  __AUTH_CONST.__const: 0x5fc0
+  __AUTH_CONST.__cfstring: 0xcc00
+  __AUTH_CONST.__objc_const: 0x23460
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_intobj: 0x108
+  __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH.__objc_data: 0xb88
-  __AUTH.__data: 0x1e8
-  __DATA.__objc_ivar: 0xb7c
-  __DATA.__data: 0x19c8
-  __DATA.__bss: 0x1070
-  __DATA.__common: 0x94
+  __AUTH.__data: 0x1d8
+  __DATA.__objc_ivar: 0xb84
+  __DATA.__data: 0x1a18
+  __DATA.__bss: 0x1080
+  __DATA.__common: 0x44
   __DATA_DIRTY.__objc_data: 0x4510
   __DATA_DIRTY.__data: 0x90
   __DATA_DIRTY.__bss: 0x1f0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 642B241B-64D4-3938-AC7F-453F34E7DAB8
-  Functions: 4830
-  Symbols:   16003
-  CStrings:  8833
+  UUID: 3560C881-CBC6-3C26-A137-93145599D7BE
+  Functions: 4843
+  Symbols:   16031
+  CStrings:  8852
 
Symbols:
+ -[AADeviceInfo qualifiedBuildVersion]
+ -[AAFollowUpController(Convenience) reportPostCFUEvent:]
+ -[AAFollowUpController(Convenience) reportPostCFUEvent:].cold.1
+ -[AASignInFlowController setSignInOperationHelper:]
+ -[AASignInFlowController signInOperationHelper]
+ -[AASignInOperationHelper initWithAccountStore:]
+ -[AASignInOperationHelper signInAccount:enablingDataclasses:completion:].cold.1
+ -[AASignInOperationHelper signInAccount:withDataclassActions:completion:]
+ -[AASignInOperationHelper signInAccount:withDataclassActions:completion:].cold.1
+ _OBJC_IVAR_$_AASignInFlowController._signInOperationHelper
+ _OBJC_IVAR_$_AASignInOperationHelper._dataclassManager
+ ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.385
+ ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.385.cold.1
+ ___53-[AACustodianController repairCustodians:completion:]_block_invoke.106
+ ___53-[AACustodianController repairCustodians:completion:]_block_invoke.106.cold.1
+ ___53-[AACustodianController repairCustodians:completion:]_block_invoke.107
+ ___53-[AACustodianController repairCustodians:completion:]_block_invoke.107.cold.1
+ ___56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.83
+ ___56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.83.cold.1
+ ___56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.84
+ ___56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.84.cold.1
+ ___61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.85
+ ___61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.85.cold.1
+ ___61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.86
+ ___61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.86.cold.1
+ ___62-[AACustodianController fetchCustodianshipInfoWithCompletion:]_block_invoke.50
+ ___62-[AACustodianController fetchCustodianshipInfoWithCompletion:]_block_invoke.50.cold.1
+ ___62-[AACustodianController fetchCustodianshipInfoWithCompletion:]_block_invoke.51
+ ___62-[AACustodianController fetchCustodianshipInfoWithCompletion:]_block_invoke.51.cold.1
+ ___63-[AACustodianController removeCustodianWithContext:completion:]_block_invoke.42
+ ___63-[AACustodianController removeCustodianWithContext:completion:]_block_invoke.42.cold.1
+ ___63-[AACustodianController removeCustodianWithContext:completion:]_block_invoke.43
+ ___63-[AACustodianController removeCustodianWithContext:completion:]_block_invoke.43.cold.1
+ ___64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.104
+ ___64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.104.cold.1
+ ___64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.105
+ ___64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.105.cold.1
+ ___64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.91
+ ___64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.91.cold.1
+ ___64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.92
+ ___64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.92.cold.1
+ ___64-[AACustodianController fetchSuggestedCustodiansWithCompletion:]_block_invoke.55
+ ___64-[AACustodianController fetchSuggestedCustodiansWithCompletion:]_block_invoke.55.cold.1
+ ___64-[AACustodianController fetchSuggestedCustodiansWithCompletion:]_block_invoke.56
+ ___64-[AACustodianController fetchSuggestedCustodiansWithCompletion:]_block_invoke.56.cold.1
+ ___66-[AACustodianController fetchCustodianHealthStatusWithCompletion:]_block_invoke.59
+ ___66-[AACustodianController fetchCustodianHealthStatusWithCompletion:]_block_invoke.59.cold.1
+ ___66-[AACustodianController fetchCustodianHealthStatusWithCompletion:]_block_invoke.60
+ ___66-[AACustodianController fetchCustodianHealthStatusWithCompletion:]_block_invoke.60.cold.1
+ ___66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.108
+ ___66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.108.cold.1
+ ___66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.109
+ ___66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.109.cold.1
+ ___66-[AACustodianController setupCustodianshipWithContext:completion:]_block_invoke.35
+ ___66-[AACustodianController setupCustodianshipWithContext:completion:]_block_invoke.35.cold.1
+ ___66-[AACustodianController setupCustodianshipWithContext:completion:]_block_invoke.37
+ ___66-[AACustodianController setupCustodianshipWithContext:completion:]_block_invoke.37.cold.1
+ ___66-[AACustodianController stopBeingCustodianWithContext:completion:]_block_invoke.44
+ ___66-[AACustodianController stopBeingCustodianWithContext:completion:]_block_invoke.44.cold.1
+ ___66-[AACustodianController stopBeingCustodianWithContext:completion:]_block_invoke.45
+ ___66-[AACustodianController stopBeingCustodianWithContext:completion:]_block_invoke.45.cold.1
+ ___67-[AACustodianController fetchCustodianshipInfoWithUUID:completion:]_block_invoke.53
+ ___67-[AACustodianController fetchCustodianshipInfoWithUUID:completion:]_block_invoke.53.cold.1
+ ___67-[AACustodianController fetchCustodianshipInfoWithUUID:completion:]_block_invoke.54
+ ___67-[AACustodianController fetchCustodianshipInfoWithUUID:completion:]_block_invoke.54.cold.1
+ ___68-[AACustodianController fetchTrustedContactsWithRequest:completion:]_block_invoke.48
+ ___68-[AACustodianController fetchTrustedContactsWithRequest:completion:]_block_invoke.48.cold.1
+ ___68-[AACustodianController fetchTrustedContactsWithRequest:completion:]_block_invoke.49
+ ___68-[AACustodianController fetchTrustedContactsWithRequest:completion:]_block_invoke.49.cold.1
+ ___70-[AACustodianController startCustodianRecoveryWithContext:completion:]_block_invoke.62
+ ___70-[AACustodianController startCustodianRecoveryWithContext:completion:]_block_invoke.62.cold.1
+ ___71-[AACustodianController cancelCustodianRecoveryWithContext:completion:]_block_invoke.79
+ ___71-[AACustodianController cancelCustodianRecoveryWithContext:completion:]_block_invoke.79.cold.1
+ ___71-[AACustodianController cancelCustodianRecoveryWithContext:completion:]_block_invoke.80
+ ___71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.89
+ ___71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.89.cold.1
+ ___71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.90
+ ___71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.90.cold.1
+ ___71-[AACustodianController pullTrustedContactsFromCloudKitWithCompletion:]_block_invoke.87
+ ___71-[AACustodianController pullTrustedContactsFromCloudKitWithCompletion:]_block_invoke.87.cold.1
+ ___71-[AACustodianController pullTrustedContactsFromCloudKitWithCompletion:]_block_invoke.88
+ ___73-[AACustodianController fetchSuggestedCustodiansForUpsellWithCompletion:]_block_invoke.57
+ ___73-[AACustodianController fetchSuggestedCustodiansForUpsellWithCompletion:]_block_invoke.57.cold.1
+ ___73-[AACustodianController fetchSuggestedCustodiansForUpsellWithCompletion:]_block_invoke.58
+ ___73-[AACustodianController fetchSuggestedCustodiansForUpsellWithCompletion:]_block_invoke.58.cold.1
+ ___74-[AACustodianController fetchCustodianRecoveryKeysWithContext:completion:]_block_invoke.78
+ ___74-[AACustodianController fetchCustodianRecoveryKeysWithContext:completion:]_block_invoke.78.cold.1
+ ___74-[AACustodianController respondToCustodianRequestWithResponse:completion:]_block_invoke.38
+ ___74-[AACustodianController respondToCustodianRequestWithResponse:completion:]_block_invoke.38.cold.1
+ ___74-[AACustodianController respondToCustodianRequestWithResponse:completion:]_block_invoke.39
+ ___74-[AACustodianController respondToCustodianRequestWithResponse:completion:]_block_invoke.39.cold.1
+ ___75-[AACustodianController fetchCustodianRecoveryConfigurationWithCompletion:]_block_invoke.64
+ ___75-[AACustodianController fetchCustodianRecoveryConfigurationWithCompletion:]_block_invoke.64.cold.1
+ ___75-[AAFollowUpController(Convenience) pendingFollowUpsForAccount:completion:]_block_invoke.386
+ ___77-[AACustodianController generateCustodianRecoveryCodeWithContext:completion:]_block_invoke.65
+ ___77-[AACustodianController generateCustodianRecoveryCodeWithContext:completion:]_block_invoke.68
+ ___77-[AACustodianController validateCustodianRecoveryCodeWithContext:completion:]_block_invoke.73
+ ___77-[AACustodianController validateCustodianRecoveryCodeWithContext:completion:]_block_invoke.74
+ ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.390
+ ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.390.cold.1
+ ___86-[AACustodianController _retryingGenerateCustodianRecoveryCodeWithContext:completion:]_block_invoke.71
+ ___86-[AACustodianController _retryingValidateCustodianRecoveryCodeWithContext:completion:]_block_invoke.76
+ ___87-[AAFollowUpController(Convenience) dismissFollowUpsForAccount:identifiers:completion:]_block_invoke.384
+ ___88-[AACustodianController fetchCustodianPasswordResetInformationWithSessionID:completion:]_block_invoke.82
+ ___88-[AACustodianController fetchCustodianPasswordResetInformationWithSessionID:completion:]_block_invoke.82.cold.1
+ ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.382
+ ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.382.cold.1
+ ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.382.cold.2
+ ___91-[AAFollowUpController(Convenience) pendingFollowUpItemUserInfosWithIdentifier:completion:]_block_invoke.394
+ ___95-[AAFollowUpController(Convenience) postFollowUpWithIdentifier:forAccount:userInfo:completion:]_block_invoke.cold.1
+ ____AAFollowUpControllerHandleSetupAssistantExited_block_invoke.435
+ ___block_literal_global.140
+ ___block_literal_global.397
+ ___block_literal_global.437
+ _kAAAnalyticsIdmsWalrusStatus
+ _kAAFPostFollowupEvent
+ _objc_msgSend$analyticsEventWithName:eventCategory:followupAnalyticsData:altDSID:
+ _objc_msgSend$reportPostCFUEvent:
+ _objc_msgSend$signInAccount:withDataclassActions:completion:
- -[AAFollowUpController(Convenience) reportPostCFUEvent]
- -[AAFollowUpController(Convenience) reportPostCFUEvent].cold.1
- -[AASignInOperationHelper signInAccount:enablingDataclasses:dataclassActions:completion:]
- ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.382
- ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.382.cold.1
- ___53-[AACustodianController repairCustodians:completion:]_block_invoke.102
- ___53-[AACustodianController repairCustodians:completion:]_block_invoke.102.cold.1
- ___53-[AACustodianController repairCustodians:completion:]_block_invoke.103
- ___53-[AACustodianController repairCustodians:completion:]_block_invoke.103.cold.1
- ___56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.79
- ___56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.79.cold.1
- ___56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.80
- ___56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.80.cold.1
- ___61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.81
- ___61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.81.cold.1
- ___61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.82
- ___61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.82.cold.1
- ___62-[AACustodianController fetchCustodianshipInfoWithCompletion:]_block_invoke.46
- ___62-[AACustodianController fetchCustodianshipInfoWithCompletion:]_block_invoke.46.cold.1
- ___62-[AACustodianController fetchCustodianshipInfoWithCompletion:]_block_invoke.47
- ___62-[AACustodianController fetchCustodianshipInfoWithCompletion:]_block_invoke.47.cold.1
- ___63-[AACustodianController removeCustodianWithContext:completion:]_block_invoke.38
- ___63-[AACustodianController removeCustodianWithContext:completion:]_block_invoke.38.cold.1
- ___63-[AACustodianController removeCustodianWithContext:completion:]_block_invoke.39
- ___63-[AACustodianController removeCustodianWithContext:completion:]_block_invoke.39.cold.1
- ___64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.100
- ___64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.100.cold.1
- ___64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.101
- ___64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.101.cold.1
- ___64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.87
- ___64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.87.cold.1
- ___64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.88
- ___64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.88.cold.1
- ___64-[AACustodianController fetchSuggestedCustodiansWithCompletion:]_block_invoke.51
- ___64-[AACustodianController fetchSuggestedCustodiansWithCompletion:]_block_invoke.51.cold.1
- ___64-[AACustodianController fetchSuggestedCustodiansWithCompletion:]_block_invoke.52
- ___64-[AACustodianController fetchSuggestedCustodiansWithCompletion:]_block_invoke.52.cold.1
- ___66-[AACustodianController fetchCustodianHealthStatusWithCompletion:]_block_invoke.55
- ___66-[AACustodianController fetchCustodianHealthStatusWithCompletion:]_block_invoke.55.cold.1
- ___66-[AACustodianController fetchCustodianHealthStatusWithCompletion:]_block_invoke.56
- ___66-[AACustodianController fetchCustodianHealthStatusWithCompletion:]_block_invoke.56.cold.1
- ___66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.104
- ___66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.104.cold.1
- ___66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.105
- ___66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.105.cold.1
- ___66-[AACustodianController setupCustodianshipWithContext:completion:]_block_invoke.31
- ___66-[AACustodianController setupCustodianshipWithContext:completion:]_block_invoke.31.cold.1
- ___66-[AACustodianController setupCustodianshipWithContext:completion:]_block_invoke.33
- ___66-[AACustodianController setupCustodianshipWithContext:completion:]_block_invoke.33.cold.1
- ___66-[AACustodianController stopBeingCustodianWithContext:completion:]_block_invoke.40
- ___66-[AACustodianController stopBeingCustodianWithContext:completion:]_block_invoke.40.cold.1
- ___66-[AACustodianController stopBeingCustodianWithContext:completion:]_block_invoke.41
- ___66-[AACustodianController stopBeingCustodianWithContext:completion:]_block_invoke.41.cold.1
- ___67-[AACustodianController fetchCustodianshipInfoWithUUID:completion:]_block_invoke.49
- ___67-[AACustodianController fetchCustodianshipInfoWithUUID:completion:]_block_invoke.49.cold.1
- ___67-[AACustodianController fetchCustodianshipInfoWithUUID:completion:]_block_invoke.50
- ___67-[AACustodianController fetchCustodianshipInfoWithUUID:completion:]_block_invoke.50.cold.1
- ___68-[AACustodianController fetchTrustedContactsWithRequest:completion:]_block_invoke.44
- ___68-[AACustodianController fetchTrustedContactsWithRequest:completion:]_block_invoke.44.cold.1
- ___68-[AACustodianController fetchTrustedContactsWithRequest:completion:]_block_invoke.45
- ___68-[AACustodianController fetchTrustedContactsWithRequest:completion:]_block_invoke.45.cold.1
- ___70-[AACustodianController startCustodianRecoveryWithContext:completion:]_block_invoke.58
- ___70-[AACustodianController startCustodianRecoveryWithContext:completion:]_block_invoke.58.cold.1
- ___71-[AACustodianController cancelCustodianRecoveryWithContext:completion:]_block_invoke.75
- ___71-[AACustodianController cancelCustodianRecoveryWithContext:completion:]_block_invoke.75.cold.1
- ___71-[AACustodianController cancelCustodianRecoveryWithContext:completion:]_block_invoke.76
- ___71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.85
- ___71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.85.cold.1
- ___71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.86
- ___71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.86.cold.1
- ___71-[AACustodianController pullTrustedContactsFromCloudKitWithCompletion:]_block_invoke.83
- ___71-[AACustodianController pullTrustedContactsFromCloudKitWithCompletion:]_block_invoke.83.cold.1
- ___71-[AACustodianController pullTrustedContactsFromCloudKitWithCompletion:]_block_invoke.84
- ___73-[AACustodianController fetchSuggestedCustodiansForUpsellWithCompletion:]_block_invoke.53
- ___73-[AACustodianController fetchSuggestedCustodiansForUpsellWithCompletion:]_block_invoke.53.cold.1
- ___73-[AACustodianController fetchSuggestedCustodiansForUpsellWithCompletion:]_block_invoke.54
- ___73-[AACustodianController fetchSuggestedCustodiansForUpsellWithCompletion:]_block_invoke.54.cold.1
- ___74-[AACustodianController fetchCustodianRecoveryKeysWithContext:completion:]_block_invoke.74
- ___74-[AACustodianController fetchCustodianRecoveryKeysWithContext:completion:]_block_invoke.74.cold.1
- ___74-[AACustodianController respondToCustodianRequestWithResponse:completion:]_block_invoke.34
- ___74-[AACustodianController respondToCustodianRequestWithResponse:completion:]_block_invoke.34.cold.1
- ___74-[AACustodianController respondToCustodianRequestWithResponse:completion:]_block_invoke.35
- ___74-[AACustodianController respondToCustodianRequestWithResponse:completion:]_block_invoke.35.cold.1
- ___75-[AACustodianController fetchCustodianRecoveryConfigurationWithCompletion:]_block_invoke.60
- ___75-[AACustodianController fetchCustodianRecoveryConfigurationWithCompletion:]_block_invoke.60.cold.1
- ___75-[AAFollowUpController(Convenience) pendingFollowUpsForAccount:completion:]_block_invoke.383
- ___77-[AACustodianController generateCustodianRecoveryCodeWithContext:completion:]_block_invoke.61
- ___77-[AACustodianController generateCustodianRecoveryCodeWithContext:completion:]_block_invoke.64
- ___77-[AACustodianController validateCustodianRecoveryCodeWithContext:completion:]_block_invoke.69
- ___77-[AACustodianController validateCustodianRecoveryCodeWithContext:completion:]_block_invoke.70
- ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.387
- ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.387.cold.1
- ___86-[AACustodianController _retryingGenerateCustodianRecoveryCodeWithContext:completion:]_block_invoke.67
- ___86-[AACustodianController _retryingValidateCustodianRecoveryCodeWithContext:completion:]_block_invoke.72
- ___87-[AAFollowUpController(Convenience) dismissFollowUpsForAccount:identifiers:completion:]_block_invoke.381
- ___88-[AACustodianController fetchCustodianPasswordResetInformationWithSessionID:completion:]_block_invoke.78
- ___88-[AACustodianController fetchCustodianPasswordResetInformationWithSessionID:completion:]_block_invoke.78.cold.1
- ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.379
- ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.379.cold.1
- ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.379.cold.2
- ___91-[AAFollowUpController(Convenience) pendingFollowUpItemUserInfosWithIdentifier:completion:]_block_invoke.390
- ____AAFollowUpControllerHandleSetupAssistantExited_block_invoke.431
- ___block_literal_global.131
- ___block_literal_global.134
- ___block_literal_global.393
- ___block_literal_global.433
- _objc_msgSend$reportPostCFUEvent
- _objc_msgSend$signInAccount:enablingDataclasses:dataclassActions:completion:
- _objc_release_x2
CStrings:
+ "%@ (%@)"
+ "@\"AADataclassManager\""
+ "@\"AASignInOperationHelper\""
+ "Enabling dataclasses without local data and saving account."
+ "Saving account with dataclass actions."
+ "T@\"AASignInOperationHelper\",&,N,V_signInOperationHelper"
+ "UNKNOWN OS"
+ "_dataclassManager"
+ "_signInOperationHelper"
+ "analyticsEventWithName:eventCategory:followupAnalyticsData:altDSID:"
+ "contextType"
+ "idmsWalrusStatus"
+ "qualifiedBuildVersion"
+ "reportPostCFUEvent:"
+ "setSignInOperationHelper:"
+ "signInAccount:withDataclassActions:completion:"
+ "signInOperationHelper"
- "reportPostCFUEvent"
- "signInAccount:enablingDataclasses:dataclassActions:completion:"
- "v44@0:8@16B24@28@?36"

```
