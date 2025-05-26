## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount`

```diff

-973.1.1.3.0
-  __TEXT.__text: 0xb9dc8
-  __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_methlist: 0x8c7c
+981.1.1.0.0
+  __TEXT.__text: 0xb8858
+  __TEXT.__auth_stubs: 0xab0
+  __TEXT.__objc_methlist: 0x8bc4
   __TEXT.__const: 0x1100
-  __TEXT.__cstring: 0xb030
-  __TEXT.__oslogstring: 0xcf53
-  __TEXT.__gcc_except_tab: 0x1694
+  __TEXT.__cstring: 0xb234
+  __TEXT.__oslogstring: 0xca6c
+  __TEXT.__gcc_except_tab: 0x1624
   __TEXT.__dlopen_cstrs: 0x241
-  __TEXT.__unwind_info: 0x2434
-  __TEXT.__objc_classname: 0x1bc5
-  __TEXT.__objc_methname: 0x12f8f
-  __TEXT.__objc_methtype: 0x29e4
-  __TEXT.__objc_stubs: 0xabc0
+  __TEXT.__unwind_info: 0x23d4
+  __TEXT.__objc_classname: 0x1b53
+  __TEXT.__objc_methname: 0x12da7
+  __TEXT.__objc_methtype: 0x293c
+  __TEXT.__objc_stubs: 0xa9c0
   __DATA_CONST.__got: 0x508
-  __DATA_CONST.__const: 0x2ed8
-  __DATA_CONST.__objc_classlist: 0x720
+  __DATA_CONST.__const: 0x2eb8
+  __DATA_CONST.__objc_classlist: 0x710
   __DATA_CONST.__objc_catlist: 0x98
-  __DATA_CONST.__objc_protolist: 0x150
+  __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1b400
-  __DATA_CONST.__objc_selrefs: 0x4358
+  __DATA_CONST.__objc_const: 0x1ab30
+  __DATA_CONST.__objc_selrefs: 0x42e8
   __DATA_CONST.__objc_arraydata: 0xc0
-  __AUTH_CONST.__cfstring: 0xa8a0
+  __AUTH_CONST.__cfstring: 0xaa60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_const: 0xd0
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH_CONST.__const: 0x4e00
+  __AUTH_CONST.__const: 0x4e60
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__auth_got: 0x570
+  __AUTH_CONST.__auth_got: 0x568
   __AUTH.__objc_data: 0x50
   __DATA.__objc_protorefs: 0x38
-  __DATA.__objc_classrefs: 0x730
-  __DATA.__objc_superrefs: 0x518
-  __DATA.__objc_ivar: 0xacc
-  __DATA.__data: 0x12b8
+  __DATA.__objc_classrefs: 0x710
+  __DATA.__objc_superrefs: 0x508
+  __DATA.__objc_ivar: 0xab8
+  __DATA.__data: 0x1200
   __DATA.__bss: 0x300
   __DATA.__common: 0x64
-  __DATA_DIRTY.__const: 0x7a0
-  __DATA_DIRTY.__objc_const: 0x5c40
-  __DATA_DIRTY.__objc_data: 0x46f0
+  __DATA_DIRTY.__const: 0x740
+  __DATA_DIRTY.__objc_const: 0x5bb0
+  __DATA_DIRTY.__objc_data: 0x4650
   __DATA_DIRTY.__data: 0x60
   __DATA_DIRTY.__bss: 0x1e8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libcompression.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3851
-  Symbols:   13632
-  CStrings:  6295
+  Functions: 3816
+  Symbols:   13506
+  CStrings:  6260
 
Symbols:
+ +[AAPreferences customAppleIDAvailabilityHealthCheckIntervalMinutes]
+ +[AAPreferences getCustodianInfo]
+ +[AAPreferences isCustomAppleIDAvailabilityHealthCheckIntervalEnabled]
+ +[AAPreferences setCustodianInfo:]
+ +[AAPreferences setCustomAppleIDAvailabilityHealthCheckIntervalEnabled:]
+ +[AAPreferences setCustomAppleIDAvailabilityHealthCheckIntervalMinutes:]
+ +[AAPreferences simulate2FAFA]
+ -[AADataclassManager allowListedDataclassesForAppleAccountClassBasic]
+ -[AADataclassManager allowListedDataclassesForAppleAccountClassFull]
+ -[AADataclassManager denyListedMacOSDataclasses]
+ -[AAFollowUpController _adpUserMissingHealthyCustodianNotification]
+ -[AAFollowUpController _followUpItemForADPUserMissingHealthyCustodian:]
+ -[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]
+ -[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:].cold.1
+ -[AALocalContactInfo preflightStatus]
+ -[AALocalContactInfo setPreflightStatus:]
+ -[AATrustedContact initWithID:status:handle:firstName:lastName:displayName:isAcceptedAndShared:isIdMSConfirmed:preflightStatus:]
+ -[AATrustedContact preflightStatus]
+ GCC_except_table61
+ _AAFollowUpIdentifierADPUserMissingHealthyCustodian
+ _OBJC_IVAR_$_AALocalContactInfo._preflightStatus
+ _OBJC_IVAR_$_AATrustedContact._preflightStatus
+ ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke
+ ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.361
+ ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.361.cold.1
+ ___65-[AAFollowUpController dismissFollowUpWithIdentifier:completion:]_block_invoke.311
+ ___65-[AAFollowUpController dismissFollowUpWithIdentifier:completion:]_block_invoke.311.cold.1
+ ___65-[AAFollowUpController pendingFollowUpWithIdentifier:completion:]_block_invoke.308
+ ___71-[AAFollowUpController postFollowUpWithIdentifier:userInfo:completion:]_block_invoke.304
+ ___71-[AAFollowUpController postFollowUpWithIdentifier:userInfo:completion:]_block_invoke.304.cold.1
+ ___75-[AAFollowUpController(Convenience) pendingFollowUpsForAccount:completion:]_block_invoke.362
+ ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.366
+ ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.366.cold.1
+ ___87-[AAFollowUpController(Convenience) dismissFollowUpsForAccount:identifiers:completion:]_block_invoke.360
+ ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.358
+ ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.358.cold.1
+ ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.358.cold.2
+ ___93-[AADataclassManager enableDataclassesWithoutLocalDataDataclassActionsForAccount:completion:]_block_invoke.115
+ ___93-[AADataclassManager enableDataclassesWithoutLocalDataDataclassActionsForAccount:completion:]_block_invoke.115.cold.1
+ ____AAFollowUpControllerHandleSetupAssistantExited_block_invoke.397
+ ___block_descriptor_56_e8_32s40s48bs_e87_v32?0^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}8"NSArray"16"NSError"24ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs56bs_e87_v32?0^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}8"NSArray"16"NSError"24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s56l8s48l8
+ ___block_literal_global.108
+ ___block_literal_global.93
+ ___block_literal_global.96
+ _kAAAnalyticsAdvancedDataProtectionState
+ _kAAAnalyticsCdpStatus
+ _kAAAnalyticsCircleSyncingStatus
+ _kAAAnalyticsCliqueStatus
+ _kAAAnalyticsSecurityLevel
+ _kAAProtocolPrefCustomAppleIDAvailabilityHealthCheckIntervalMinutes
+ _kAAProtocolPrefCustomAppleIDAvailabilityIntervalEnabled
+ _kAAProtocolPrefSimulate2FAFAKey
+ _kAppleIDHealthCheckEventName
+ _objc_msgSend$_adpUserMissingHealthyCustodianNotification
+ _objc_msgSend$_followUpItemForADPUserMissingHealthyCustodian:
+ _objc_msgSend$allowListedDataclassesForAppleAccountClassBasic
+ _objc_msgSend$allowListedDataclassesForAppleAccountClassFull
+ _objc_msgSend$preflightStatus
+ _objc_msgSend$setPreflightStatus:
- +[AAPreferences isCustodianPreflightDisabled]
- +[AAPreferences isCustodianPreflightTTREnabled]
- +[AAPreferences setCustodianPreflightDisabled:]
- +[AAPreferences setCustodianPreflightTTREnabled:]
- -[AADaemonController handleMarkedForSignOutForAccount:completion:]
- -[AADataclassManager blackListedMacOSDataclasses]
- -[AADataclassManager whitelistedDataclassesForAppleAccountClassBasic]
- -[AADataclassManager whitelistedDataclassesForAppleAccountClassFull]
- -[AASignOutManager .cxx_destruct]
- -[AASignOutManager _accountForService:matchingAltDSID:DSID:]
- -[AASignOutManager _signOutOfAppleAccount:iTunesAccount:withServiceContext:completion:]
- -[AASignOutManager _signOutOfAppleAccount:iTunesAccount:withServiceContext:completion:].cold.1
- -[AASignOutManager _signOutSecondaryAccountsWithAltDSID:DSID:context:completion:]
- -[AASignOutManager _signOutSecondaryAccountsWithAltDSID:DSID:context:completion:].cold.1
- -[AASignOutManager accountStore]
- -[AASignOutManager accountsForAccountManager:]
- -[AASignOutManager altDSIDToSignOut]
- -[AASignOutManager initWithAccount:]
- -[AASignOutManager serviceOwnersManager]
- -[AASignOutManager setAccountStore:]
- -[AASignOutManager setAltDSIDToSignOut:]
- -[AASignOutManager setServiceOwnersManager:]
- -[AASignOutManager signOutOfAccount:completion:]
- -[AASignOutManager signOutOfAccount:completion:].cold.1
- -[AASignOutManager signOutOfAccount:completion:].cold.2
- -[AASignOutManager signOutOfAccount:completion:].cold.3
- -[AASignOutManager signOutOfAccount:completion:].cold.4
- -[AASilentSignOutFlowControllerDelegate .cxx_destruct]
- -[AASilentSignOutFlowControllerDelegate accountManager]
- -[AASilentSignOutFlowControllerDelegate init]
- -[AASilentSignOutFlowControllerDelegate setAccountManager:]
- -[AASilentSignOutFlowControllerDelegate signOutFlowController:disableFindMyDeviceForAccount:completion:]
- -[AASilentSignOutFlowControllerDelegate signOutFlowController:performWalrusValidationForAccount:completion:]
- -[AASilentSignOutFlowControllerDelegate signOutFlowController:showAlertWithTitle:message:completion:]
- -[AASilentSignOutFlowControllerDelegate signOutFlowController:signOutAccount:completion:]
- -[AATrustedContact initWithID:status:handle:firstName:lastName:displayName:isAcceptedAndShared:isIdMSConfirmed:]
- GCC_except_table23
- GCC_except_table29
- GCC_except_table38
- GCC_except_table56
- GCC_except_table59
- _OBJC_CLASS_$_AASignOutManager
- _OBJC_CLASS_$_AASilentSignOutFlowControllerDelegate
- _OBJC_CLASS_$_AIDAAccountManager
- _OBJC_CLASS_$_AIDAMutableServiceContext
- _OBJC_CLASS_$_AIDAServiceOwnersManager
- _OBJC_IVAR_$_AASignOutManager._accountStore
- _OBJC_IVAR_$_AASignOutManager._altDSIDToSignOut
- _OBJC_IVAR_$_AASignOutManager._serviceOwnersManager
- _OBJC_IVAR_$_AASignOutManager._signOutQueue
- _OBJC_IVAR_$_AASilentSignOutFlowControllerDelegate._accountManager
- _OBJC_IVAR_$_AASilentSignOutFlowControllerDelegate._accountStore
- _OBJC_IVAR_$_AASilentSignOutFlowControllerDelegate._pendingSignOutCompletion
- _OBJC_METACLASS_$_AASignOutManager
- _OBJC_METACLASS_$_AASilentSignOutFlowControllerDelegate
- __OBJC_$_INSTANCE_METHODS_AASignOutManager
- __OBJC_$_INSTANCE_METHODS_AASilentSignOutFlowControllerDelegate
- __OBJC_$_INSTANCE_VARIABLES_AASignOutManager
- __OBJC_$_INSTANCE_VARIABLES_AASilentSignOutFlowControllerDelegate
- __OBJC_$_PROP_LIST_AASignOutManager
- __OBJC_$_PROP_LIST_AASilentSignOutFlowControllerDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AIDAAccountManagerDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AASignOutFlowControllerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_AASignOutFlowControllerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_AIDAAccountManagerDelegate
- __OBJC_$_PROTOCOL_REFS_AASignOutFlowControllerDelegate
- __OBJC_$_PROTOCOL_REFS_AIDAAccountManagerDelegate
- __OBJC_CLASS_PROTOCOLS_$_AASignOutManager
- __OBJC_CLASS_PROTOCOLS_$_AASilentSignOutFlowControllerDelegate
- __OBJC_CLASS_RO_$_AASignOutManager
- __OBJC_CLASS_RO_$_AASilentSignOutFlowControllerDelegate
- __OBJC_LABEL_PROTOCOL_$_AASignOutFlowControllerDelegate
- __OBJC_LABEL_PROTOCOL_$_AIDAAccountManagerDelegate
- __OBJC_METACLASS_RO_$_AASignOutManager
- __OBJC_METACLASS_RO_$_AASilentSignOutFlowControllerDelegate
- __OBJC_PROTOCOL_$_AASignOutFlowControllerDelegate
- __OBJC_PROTOCOL_$_AIDAAccountManagerDelegate
- ___65-[AAFollowUpController dismissFollowUpWithIdentifier:completion:]_block_invoke.296
- ___65-[AAFollowUpController dismissFollowUpWithIdentifier:completion:]_block_invoke.296.cold.1
- ___65-[AAFollowUpController pendingFollowUpWithIdentifier:completion:]_block_invoke.293
- ___66-[AADaemonController handleMarkedForSignOutForAccount:completion:]_block_invoke
- ___66-[AADaemonController handleMarkedForSignOutForAccount:completion:]_block_invoke_2
- ___66-[AADaemonController handleMarkedForSignOutForAccount:completion:]_block_invoke_2.cold.1
- ___71-[AAFollowUpController postFollowUpWithIdentifier:userInfo:completion:]_block_invoke.289
- ___71-[AAFollowUpController postFollowUpWithIdentifier:userInfo:completion:]_block_invoke.289.cold.1
- ___75-[AAFollowUpController(Convenience) pendingFollowUpsForAccount:completion:]_block_invoke.344
- ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.348
- ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.348.cold.1
- ___81-[AASignOutManager _signOutSecondaryAccountsWithAltDSID:DSID:context:completion:]_block_invoke
- ___87-[AAFollowUpController(Convenience) dismissFollowUpsForAccount:identifiers:completion:]_block_invoke.343
- ___87-[AASignOutManager _signOutOfAppleAccount:iTunesAccount:withServiceContext:completion:]_block_invoke
- ___87-[AASignOutManager _signOutOfAppleAccount:iTunesAccount:withServiceContext:completion:]_block_invoke.32
- ___87-[AASignOutManager _signOutOfAppleAccount:iTunesAccount:withServiceContext:completion:]_block_invoke.34
- ___87-[AASignOutManager _signOutOfAppleAccount:iTunesAccount:withServiceContext:completion:]_block_invoke.35
- ___87-[AASignOutManager _signOutOfAppleAccount:iTunesAccount:withServiceContext:completion:]_block_invoke.35.cold.1
- ___87-[AASignOutManager _signOutOfAppleAccount:iTunesAccount:withServiceContext:completion:]_block_invoke.36
- ___87-[AASignOutManager _signOutOfAppleAccount:iTunesAccount:withServiceContext:completion:]_block_invoke.cold.1
- ___87-[AASignOutManager _signOutOfAppleAccount:iTunesAccount:withServiceContext:completion:]_block_invoke.cold.2
- ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.341
- ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.341.cold.1
- ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.341.cold.2
- ___89-[AASilentSignOutFlowControllerDelegate signOutFlowController:signOutAccount:completion:]_block_invoke
- ___93-[AADataclassManager enableDataclassesWithoutLocalDataDataclassActionsForAccount:completion:]_block_invoke.113
- ___93-[AADataclassManager enableDataclassesWithoutLocalDataDataclassActionsForAccount:completion:]_block_invoke.113.cold.1
- ____AAFollowUpControllerHandleSetupAssistantExited_block_invoke.378
- ___block_descriptor_48_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
- ___block_descriptor_56_e8_32bs40r48r_e5_v8?0ls32l8r40l8r48l8
- ___block_descriptor_56_e8_32s40r48r_e20_v20?0B8"NSError"12lr40l8r48l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e43_v32?0^{__SecKey=}8"NSArray"16"NSError"24ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48bs56bs_e43_v32?0^{__SecKey=}8"NSArray"16"NSError"24ls32l8s40l8s48l8s56l8
- ___block_literal_global.106
- ___block_literal_global.91
- ___block_literal_global.94
- _kAAProtocolPrefDisableCustodianPreflightKey
- _kAAProtocolPrefEnableCustodianPreflightTTRKey
- _markedForSignOutAccountKey
- _objc_msgSend$DSIDForAccount:service:
- _objc_msgSend$_accountForService:matchingAltDSID:DSID:
- _objc_msgSend$_signOutOfAppleAccount:iTunesAccount:withServiceContext:completion:
- _objc_msgSend$_signOutSecondaryAccountsWithAltDSID:DSID:context:completion:
- _objc_msgSend$accountForService:
- _objc_msgSend$altDSIDForAccount:
- _objc_msgSend$altDSIDForAccount:service:
- _objc_msgSend$altDSIDToSignOut
- _objc_msgSend$handleMarkedForSignOutForAccount:completion:
- _objc_msgSend$initWithAccountStore:
- _objc_msgSend$isPrimaryiCloudAccount:
- _objc_msgSend$removeAccount:withDataclassActions:completion:
- _objc_msgSend$serviceOwnersManager
- _objc_msgSend$setAccountManager:
- _objc_msgSend$setAccountStore:
- _objc_msgSend$setAltDSIDToSignOut:
- _objc_msgSend$setServiceOwnersManager:
- _objc_msgSend$setSignOutContexts:
- _objc_msgSend$signOutService:withContext:completion:
- _objc_msgSend$supportedServices
- _objc_msgSend$whitelistedDataclassesForAppleAccountClassBasic
- _objc_msgSend$whitelistedDataclassesForAppleAccountClassFull
- _objc_retain_x5
CStrings:
+ "\x17\x11!"
+ "@40@0:8@16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24^@32"
+ "@80@0:8@16q24@32@40@48@56B64B68q72"
+ "AACustodianInfo"
+ "AACustomAppleIDAvailabilityIntervalMinutes"
+ "AACustomAppleIDAvailabilitykIntervalEnabled"
+ "AASimulate2FAFA"
+ "Attempting to teardown followups starting with identifier %@ for account: %@"
+ "FOLLOWUP_HEALTHY_RECOVERY_CONTACT_MISSING_BUTTON_DISMISS"
+ "FOLLOWUP_HEALTHY_RECOVERY_CONTACT_MISSING_BUTTON_PRIMARY"
+ "FOLLOWUP_HEALTHY_RECOVERY_CONTACT_MISSING_MESSAGE"
+ "FOLLOWUP_HEALTHY_RECOVERY_CONTACT_MISSING_NOTIFICATION_MESSAGE"
+ "FOLLOWUP_HEALTHY_RECOVERY_CONTACT_MISSING_NOTIFICATION_TITLE_IOS"
+ "Messages"
+ "Tq,N,V_preflightStatus"
+ "Tq,R,N,V_preflightStatus"
+ "_adpUserMissingHealthyCustodianNotification"
+ "_followUpItemForADPUserMissingHealthyCustodian:"
+ "_preflightStatus"
+ "advancedDataProtectionState"
+ "allowListedDataclassesForAppleAccountClassBasic"
+ "allowListedDataclassesForAppleAccountClassFull"
+ "cdpStatus"
+ "circleSyncingStatus"
+ "cliqueStatus"
+ "com.apple.AAFollowUpIdentifier.adpUserMissingHealthyCustodian"
+ "com.apple.appleid.accountHealthEvent"
+ "customAppleIDAvailabilityHealthCheckIntervalMinutes"
+ "denyListedMacOSDataclasses"
+ "dismissFollowUpsStartingWithIdentifierPrefix:account:completion:"
+ "getCustodianInfo"
+ "initWithID:status:handle:firstName:lastName:displayName:isAcceptedAndShared:isIdMSConfirmed:preflightStatus:"
+ "isCustomAppleIDAvailabilityHealthCheckIntervalEnabled"
+ "mic2_ui"
+ "preflightStatus"
+ "securityLevel"
+ "setCustodianInfo:"
+ "setCustomAppleIDAvailabilityHealthCheckIntervalEnabled:"
+ "setCustomAppleIDAvailabilityHealthCheckIntervalMinutes:"
+ "setPreflightStatus:"
+ "simulate2FAFA"
+ "v32@?0^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}8@\"NSArray\"16@\"NSError\"24"
- "\x17\x11\x11"
- "-[AADaemonController handleMarkedForSignOutForAccount:completion:]_block_invoke_2"
- "@\"AIDAServiceOwnersManager\""
- "@\"NSDictionary\"24@0:8@\"AIDAAccountManager\"16"
- "@40@0:8@16^{__SecKey=}24^@32"
- "@72@0:8@16q24@32@40@48@56B64B68"
- "AADisableCustodianPreflight"
- "AAEnableCustodianPreflightTTR"
- "AASignOutFlowControllerDelegate"
- "AASignOutManager"
- "AASilentSignOutFlowControllerDelegate"
- "AIDAAccountManagerDelegate"
- "Attempting to sign out account %@ with dataclass actions (not used)."
- "DSIDForAccount:service:"
- "Failed to Sign out with error %@"
- "Failed to Sign out with no error"
- "Has Apple account %@:, Has iTunes store account %@:"
- "No primary account found for %@, no sign out necessary."
- "Primary account for %@ has DSID (%@) that does not match, bailing!"
- "Primary account for %@ has altDSID (%@) that does not match, checking DSID..."
- "Primary account for %@ has matching DSID..."
- "Primary account for %@ has matching altDSID..."
- "Removal of account completed with success: %@, error: %@"
- "Secondary account sign out complete!"
- "Sign out for service %@ completed with success: %@, error: %@"
- "Sign out of apple account completed with success: %@"
- "Sign out of store account completed with success: %@, error: %@"
- "Signing out of service %@ with account %@..."
- "Signing out secondary accounts with altDSID: %@"
- "Signing out store account %@ now..."
- "Silent force sign out does not check for disableFindMyDevice for %@"
- "Silent force sign out does not check for walrus validation"
- "Silent force sign out showAlertWithTitle was called"
- "Starting the sign out flow, setting up service context, and checking for associated apple and store associated accounts"
- "T@\"ACAccountStore\",&,N,V_accountStore"
- "T@\"AIDAAccountManager\",&,N,V_accountManager"
- "T@\"AIDAServiceOwnersManager\",&,N,V_serviceOwnersManager"
- "T@\"NSString\",&,N,V_altDSIDToSignOut"
- "This account is not primary, doing nothing."
- "This account is primary, continue to silently sign out."
- "_accountForService:matchingAltDSID:DSID:"
- "_altDSIDToSignOut"
- "_pendingSignOutCompletion"
- "_serviceOwnersManager"
- "_signOutOfAppleAccount:iTunesAccount:withServiceContext:completion:"
- "_signOutQueue"
- "_signOutSecondaryAccountsWithAltDSID:DSID:context:completion:"
- "accountForService:"
- "accountManager"
- "accountsForAccountManager:"
- "altDSIDForAccount:"
- "altDSIDForAccount:service:"
- "altDSIDToSignOut"
- "blackListedMacOSDataclasses"
- "daemon-appleaccount/handle-MarkedForSignOut-SignOut"
- "handleMarkedForSignOutForAccount:completion:"
- "initWithID:status:handle:firstName:lastName:displayName:isAcceptedAndShared:isIdMSConfirmed:"
- "isCustodianPreflightDisabled"
- "isCustodianPreflightTTREnabled"
- "isPrimaryiCloudAccount:"
- "markedForSignOut"
- "removeAccount:withDataclassActions:completion:"
- "serviceOwnersManager"
- "setAccountManager:"
- "setAccountStore:"
- "setAltDSIDToSignOut:"
- "setCustodianPreflightDisabled:"
- "setCustodianPreflightTTREnabled:"
- "setServiceOwnersManager:"
- "setSignOutContexts:"
- "signOutOfAccount:completion:"
- "signOutService:withContext:completion:"
- "supportedServices"
- "v32@?0^{__SecKey=}8@\"NSArray\"16@\"NSError\"24"
- "v40@0:8@\"AASignOutFlowController\"16@\"ACAccount\"24@?<v@?B@\"NSError\">32"
- "v48@0:8@\"AASignOutFlowController\"16@\"NSString\"24@\"NSString\"32@?<v@?B>40"
- "whitelistedDataclassesForAppleAccountClassBasic"
- "whitelistedDataclassesForAppleAccountClassFull"

```
