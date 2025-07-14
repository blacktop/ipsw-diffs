## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount`

```diff

-981.1.1.0.0
-  __TEXT.__text: 0xb8858
+981.5.1.0.0
+  __TEXT.__text: 0xb8ba8
   __TEXT.__auth_stubs: 0xab0
-  __TEXT.__objc_methlist: 0x8bc4
+  __TEXT.__objc_methlist: 0x8bbc
   __TEXT.__const: 0x1100
-  __TEXT.__cstring: 0xb234
-  __TEXT.__oslogstring: 0xca6c
+  __TEXT.__cstring: 0xb2d6
+  __TEXT.__oslogstring: 0xca5d
   __TEXT.__gcc_except_tab: 0x1624
   __TEXT.__dlopen_cstrs: 0x241
-  __TEXT.__unwind_info: 0x23d4
-  __TEXT.__objc_classname: 0x1b53
-  __TEXT.__objc_methname: 0x12da7
-  __TEXT.__objc_methtype: 0x293c
-  __TEXT.__objc_stubs: 0xa9c0
+  __TEXT.__unwind_info: 0x23c8
+  __TEXT.__objc_classname: 0x1b6a
+  __TEXT.__objc_methname: 0x12d69
+  __TEXT.__objc_methtype: 0x2951
+  __TEXT.__objc_stubs: 0xaa00
   __DATA_CONST.__got: 0x508
   __DATA_CONST.__const: 0x2eb8
-  __DATA_CONST.__objc_classlist: 0x710
+  __DATA_CONST.__objc_classlist: 0x718
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1ab30
+  __DATA_CONST.__objc_const: 0x1ab78
   __DATA_CONST.__objc_selrefs: 0x42e8
   __DATA_CONST.__objc_arraydata: 0xc0
-  __AUTH_CONST.__cfstring: 0xaa60
+  __AUTH_CONST.__cfstring: 0xab00
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_const: 0xd0
+  __AUTH_CONST.__objc_const: 0x118
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__const: 0x4e60
   __AUTH_CONST.__auth_got: 0x568
-  __AUTH.__objc_data: 0x50
+  __AUTH.__objc_data: 0xa0
   __DATA.__objc_protorefs: 0x38
   __DATA.__objc_classrefs: 0x710
   __DATA.__objc_superrefs: 0x508
   __DATA.__objc_ivar: 0xab8
-  __DATA.__data: 0x1200
+  __DATA.__data: 0x1210
   __DATA.__bss: 0x300
   __DATA.__common: 0x64
   __DATA_DIRTY.__const: 0x740

   - /usr/lib/libcompression.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C6F8F2AE-4794-34AA-983B-2D5B1EF9E085
-  Functions: 3816
-  Symbols:   13506
-  CStrings:  7623
+  UUID: 5A2BB667-1AAA-3AF5-B3DC-D5720DBC3594
+  Functions: 3814
+  Symbols:   13511
+  CStrings:  7635
 
Symbols:
+ +[AATermsStringsProvider neediCloudTermsAcceptanceDeviceSpecificMessage]
+ +[AATermsStringsProvider neediCloudTermsAcceptanceTitle]
+ -[AAFollowUpController _adpUserMissingHealthyCustodianNotification:]
+ -[AASignInFlowController _onqueue_saveAccount:withAuthResults:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:]
+ -[AASignInFlowController _onqueue_saveAccount:withAuthResults:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:].cold.1
+ -[AASignInFlowController _saveAccount:withAuthResults:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:]
+ -[NSString(AppleAccount) unredactedSuffixOfLength:]
+ _AAFollowUpOpenPrefPaneActionPresentAccountRecovery
+ _AAFollowUpUserInfoHasMultipleRecoveryContacts
+ _OBJC_CLASS_$_AATermsStringsProvider
+ _OBJC_METACLASS_$_AATermsStringsProvider
+ __OBJC_$_CLASS_METHODS_AATermsStringsProvider
+ __OBJC_CLASS_RO_$_AATermsStringsProvider
+ __OBJC_METACLASS_RO_$_AATermsStringsProvider
+ ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.367
+ ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.367.cold.1
+ ___123-[AASignInFlowController _saveAccount:withAuthResults:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:]_block_invoke
+ ___131-[AASignInFlowController _onqueue_saveAccount:withAuthResults:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:]_block_invoke
+ ___131-[AASignInFlowController _onqueue_saveAccount:withAuthResults:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:]_block_invoke.105
+ ___65-[AAFollowUpController dismissFollowUpWithIdentifier:completion:]_block_invoke.317
+ ___65-[AAFollowUpController dismissFollowUpWithIdentifier:completion:]_block_invoke.317.cold.1
+ ___65-[AAFollowUpController pendingFollowUpWithIdentifier:completion:]_block_invoke.314
+ ___71-[AAFollowUpController postFollowUpWithIdentifier:userInfo:completion:]_block_invoke.310
+ ___71-[AAFollowUpController postFollowUpWithIdentifier:userInfo:completion:]_block_invoke.310.cold.1
+ ___75-[AAFollowUpController(Convenience) pendingFollowUpsForAccount:completion:]_block_invoke.368
+ ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.372
+ ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.372.cold.1
+ ___87-[AAFollowUpController(Convenience) dismissFollowUpsForAccount:identifiers:completion:]_block_invoke.366
+ ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.364
+ ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.364.cold.1
+ ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.364.cold.2
+ ____AAFollowUpControllerHandleSetupAssistantExited_block_invoke.403
+ ___block_descriptor_64_e8_32s40s48bs56w_e20_v20?0B8"NSError"12ls32l8w56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s_e34_v28?0B8"ACAccount"12"NSError"20ls32l8s40l8
+ ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ _kAAAnalyticsEventiCloudAccountAdd
+ _kAAAnalyticsTotalViableEscrowRecords
+ _objc_msgSend$_adpUserMissingHealthyCustodianNotification:
+ _objc_msgSend$_onqueue_saveAccount:withAuthResults:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:
+ _objc_msgSend$_saveAccount:withAuthResults:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$unredactedSuffixOfLength:
- +[AAPreferences customAppleIDAvailabilityHealthCheckIntervalMinutes]
- +[AAPreferences isCustomAppleIDAvailabilityHealthCheckIntervalEnabled]
- +[AAPreferences isMomentsDataclassEnabled].cold.1
- +[AAPreferences setCustomAppleIDAvailabilityHealthCheckIntervalEnabled:]
- +[AAPreferences setCustomAppleIDAvailabilityHealthCheckIntervalMinutes:]
- -[AAFollowUpController _adpUserMissingHealthyCustodianNotification]
- -[AASignInFlowController _onqueue_saveAccount:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:]
- -[AASignInFlowController _onqueue_saveAccount:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:].cold.1
- -[AASignInFlowController _saveAccount:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:]
- ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.361
- ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.361.cold.1
- ___107-[AASignInFlowController _saveAccount:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:]_block_invoke
- ___115-[AASignInFlowController _onqueue_saveAccount:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:]_block_invoke
- ___115-[AASignInFlowController _onqueue_saveAccount:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:]_block_invoke.105
- ___65-[AAFollowUpController dismissFollowUpWithIdentifier:completion:]_block_invoke.311
- ___65-[AAFollowUpController dismissFollowUpWithIdentifier:completion:]_block_invoke.311.cold.1
- ___65-[AAFollowUpController pendingFollowUpWithIdentifier:completion:]_block_invoke.308
- ___71-[AAFollowUpController postFollowUpWithIdentifier:userInfo:completion:]_block_invoke.304
- ___71-[AAFollowUpController postFollowUpWithIdentifier:userInfo:completion:]_block_invoke.304.cold.1
- ___75-[AAFollowUpController(Convenience) pendingFollowUpsForAccount:completion:]_block_invoke.362
- ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.366
- ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.366.cold.1
- ___87-[AAFollowUpController(Convenience) dismissFollowUpsForAccount:identifiers:completion:]_block_invoke.360
- ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.358
- ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.358.cold.1
- ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.358.cold.2
- ____AAFollowUpControllerHandleSetupAssistantExited_block_invoke.397
- ___block_descriptor_56_e8_32s40bs48w_e20_v20?0B8"NSError"12ls32l8w48l8s40l8
- ___block_descriptor_56_e8_32s_e34_v28?0B8"ACAccount"12"NSError"20ls32l8
- ___block_descriptor_64_e8_32s40bs_e34_v28?0B8"ACAccount"12"NSError"20ls32l8s40l8
- _kAAProtocolPrefCustomAppleIDAvailabilityHealthCheckIntervalMinutes
- _kAAProtocolPrefCustomAppleIDAvailabilityIntervalEnabled
- _objc_msgSend$_adpUserMissingHealthyCustodianNotification
- _objc_msgSend$_onqueue_saveAccount:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:
- _objc_msgSend$_saveAccount:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:
CStrings:
+ "...%@"
+ "AATermsStringsProvider"
+ "FOLLOWUP_HEALTHY_RECOVERY_CONTACTS_MISSING_NOTIFICATION_MESSAGE"
+ "FOLLOWUP_HEALTHY_RECOVERY_CONTACT_MISSING_ADD_RECOVERY_CONTACT"
+ "Using PET: %@"
+ "_adpUserMissingHealthyCustodianNotification:"
+ "_onqueue_saveAccount:withAuthResults:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:"
+ "_saveAccount:withAuthResults:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:"
+ "com.apple.appleaccount.iCloudAccountAdd"
+ "hasMultipleRecoveryContacts"
+ "neediCloudTermsAcceptanceDeviceSpecificMessage"
+ "neediCloudTermsAcceptanceTitle"
+ "presentAccountRecovery"
+ "substringFromIndex:"
+ "totalViableEscrowRecords"
+ "unredactedSuffixOfLength:"
+ "v44@0:8@16@24B32@?36"
- "AACustomAppleIDAvailabilityIntervalMinutes"
- "AACustomAppleIDAvailabilitykIntervalEnabled"
- "Moments dataclass enabled %d"
- "_adpUserMissingHealthyCustodianNotification"
- "_onqueue_saveAccount:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:"
- "_saveAccount:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:"
- "customAppleIDAvailabilityHealthCheckIntervalMinutes"
- "isCustomAppleIDAvailabilityHealthCheckIntervalEnabled"
- "setCustomAppleIDAvailabilityHealthCheckIntervalEnabled:"
- "setCustomAppleIDAvailabilityHealthCheckIntervalMinutes:"

```
