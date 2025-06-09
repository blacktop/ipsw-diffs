## DACalDAV

> `/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACalDAV.framework/DACalDAV`

```diff

-2673.6.1.0.0
-  __TEXT.__text: 0x35e5c
-  __TEXT.__auth_stubs: 0x1ea0
-  __TEXT.__objc_methlist: 0x3d2c
+2690.0.0.0.0
+  __TEXT.__text: 0x376d8
+  __TEXT.__auth_stubs: 0x1e90
+  __TEXT.__objc_methlist: 0x45e4
   __TEXT.__const: 0x108
-  __TEXT.__gcc_except_tab: 0x570
-  __TEXT.__cstring: 0x1630
-  __TEXT.__oslogstring: 0x5097
+  __TEXT.__cstring: 0x1641
+  __TEXT.__oslogstring: 0x506c
+  __TEXT.__gcc_except_tab: 0x5e4
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__unwind_info: 0x9a8
-  __TEXT.__objc_classname: 0x45e
-  __TEXT.__objc_methname: 0x9a94
-  __TEXT.__objc_methtype: 0x1be2
-  __TEXT.__objc_stubs: 0x7dc0
-  __DATA_CONST.__got: 0x7f0
-  __DATA_CONST.__const: 0x9c8
-  __DATA_CONST.__objc_classlist: 0xa8
-  __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x98
+  __TEXT.__unwind_info: 0xa30
+  __TEXT.__objc_classname: 0x504
+  __TEXT.__objc_methname: 0x9e34
+  __TEXT.__objc_methtype: 0x1f9f
+  __TEXT.__objc_stubs: 0x7f80
+  __DATA_CONST.__got: 0x7e0
+  __DATA_CONST.__const: 0x9f8
+  __DATA_CONST.__objc_classlist: 0xb0
+  __DATA_CONST.__objc_catlist: 0x18
+  __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x27a0
-  __DATA_CONST.__objc_superrefs: 0x88
-  __AUTH_CONST.__auth_got: 0xf60
+  __DATA_CONST.__objc_selrefs: 0x2808
+  __DATA_CONST.__objc_superrefs: 0x90
+  __AUTH_CONST.__auth_got: 0xf58
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x23a0
-  __AUTH_CONST.__objc_const: 0x7188
+  __AUTH_CONST.__objc_const: 0x8490
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0x32c
-  __DATA.__data: 0x748
+  __DATA.__objc_ivar: 0x340
+  __DATA.__data: 0x928
   __DATA.__bss: 0x70
-  __DATA_DIRTY.__objc_data: 0xa0
+  __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: FF9831AB-2B28-3B97-AA2E-DDFF8DBFFE52
-  Functions: 1011
-  Symbols:   4510
-  CStrings:  2839
+  UUID: 29F2DE91-54E5-3A77-A044-F57C5FC5AB0D
+  Functions: 1087
+  Symbols:   4732
+  CStrings:  2906
 
Symbols:
+ +[MobileCalDAVAccount _defaultAlarmOffsetFromICSString:]
+ +[MobileCalDAVDAAccount mobileCalDAVAccountClass]
+ -[ACAccount(MobileCalDAVAccountInfo) cal_isPrimaryAppleAccount]
+ -[DACalDAViCalItem initWithURL:eTag:dataPayload:inContainerWithURL:withAccountInfoProvider:].cold.1
+ -[DACalDAViCalItem initWithURL:eTag:dataPayload:inContainerWithURL:withAccountInfoProvider:].cold.2
+ -[MobileCalDAVAccount _checkExistingStoreAndSetChangeReason]
+ -[MobileCalDAVAccount _externalInfoDictionary]
+ -[MobileCalDAVAccount _reallyCancelPendingSearchQuery:]
+ -[MobileCalDAVAccount _releasePowerAssertion]
+ -[MobileCalDAVAccount _retainPowerAssertion]
+ -[MobileCalDAVAccount accountID]
+ -[MobileCalDAVAccount addUsernameToURL:]
+ -[MobileCalDAVAccount backingAccount]
+ -[MobileCalDAVAccount changeTrackingID]
+ -[MobileCalDAVAccount contextDictionary]
+ -[MobileCalDAVAccount dbHelper]
+ -[MobileCalDAVAccount didSetAccountDescription]
+ -[MobileCalDAVAccount initWithBackingAccount:]
+ -[MobileCalDAVAccount objectForKeyedSubscript:]
+ -[MobileCalDAVAccount password]
+ -[MobileCalDAVAccount port]
+ -[MobileCalDAVAccount principalURL]
+ -[MobileCalDAVAccount principalsDict]
+ -[MobileCalDAVAccount publicDescription]
+ -[MobileCalDAVAccount refreshWithContext:completion:]
+ -[MobileCalDAVAccount setAccountProperty:forKey:]
+ -[MobileCalDAVAccount setEnabled:forDADataclass:]
+ -[MobileCalDAVAccount setHost:]
+ -[MobileCalDAVAccount setObject:forKeyedSubscript:]
+ -[MobileCalDAVAccount setPassword:]
+ -[MobileCalDAVAccount setPort:]
+ -[MobileCalDAVAccount setShouldDoInitialAutodiscovery:]
+ -[MobileCalDAVAccount setUseSSL:]
+ -[MobileCalDAVAccount setUsername:]
+ -[MobileCalDAVAccount shouldDoInitialAutodiscovery]
+ -[MobileCalDAVAccount shouldFailAllTasks]
+ -[MobileCalDAVAccount uid]
+ -[MobileCalDAVAccount updateCalendarStoreWithAlreadyOpenDBShouldCreate:syncingThisAccount:]
+ -[MobileCalDAVAccount updateDelegatesWithUserInfo:]
+ -[MobileCalDAVAccount useSSL]
+ -[MobileCalDAVAccount(CompatibilityShims) backingAccountInfo]
+ -[MobileCalDAVAccountRefreshActor cancelCompletionBlock]
+ -[MobileCalDAVAccountRefreshActor delegateRefreshForPrincipal:completedWithDelegateUserInfo:error:]
+ -[MobileCalDAVAccountRefreshActor refreshWithCompletion:]
+ -[MobileCalDAVAccountRefreshActor refreshWithCompletion:].cold.1
+ -[MobileCalDAVAccountRefreshActor setCancelCompletionBlock:]
+ -[MobileCalDAVDAAccount .cxx_destruct]
+ -[MobileCalDAVDAAccount _discoverInitialPropertiesWithConsumer:]
+ -[MobileCalDAVDAAccount _reallyCancelAllSearchQueries]
+ -[MobileCalDAVDAAccount _reallyCancelPendingSearchQuery:]
+ -[MobileCalDAVDAAccount _reallyCancelSearchQuery:]
+ -[MobileCalDAVDAAccount _reallyPerformSearchQuery:]
+ -[MobileCalDAVDAAccount _reallySearchQueriesRunning]
+ -[MobileCalDAVDAAccount accountDescription]
+ -[MobileCalDAVDAAccount accountHasSignificantPropertyChangesWithChangeInfo:]
+ -[MobileCalDAVDAAccount accountIdentifier]
+ -[MobileCalDAVDAAccount accountInfo]
+ -[MobileCalDAVDAAccount addToCoreDAVLoggingDelegates]
+ -[MobileCalDAVDAAccount additionalHeaderValues]
+ -[MobileCalDAVDAAccount backingAccountShouldDoInitialAutodiscovery]
+ -[MobileCalDAVDAAccount beginDownloadingAttachmentWithUUID:consumer:]
+ -[MobileCalDAVDAAccount calendarsDataclassModified]
+ -[MobileCalDAVDAAccount checkValidityTaskGroup]
+ -[MobileCalDAVDAAccount childAccountWithIdentifier:]
+ -[MobileCalDAVDAAccount childAccountsWithAccountTypeIdentifier:]
+ -[MobileCalDAVDAAccount coreDAVLogTransmittedDataPartial:]
+ -[MobileCalDAVDAAccount coreDAVLogger]
+ -[MobileCalDAVDAAccount coreDAVTransmittedDataFinished]
+ -[MobileCalDAVDAAccount createChildAccountWithAccountTypeIdentifier:]
+ -[MobileCalDAVDAAccount customConnectionProperties]
+ -[MobileCalDAVDAAccount daAccount]
+ -[MobileCalDAVDAAccount dbHelper]
+ -[MobileCalDAVDAAccount dealloc]
+ -[MobileCalDAVDAAccount discoverInitialPropertiesWithConsumer:]
+ -[MobileCalDAVDAAccount discoveryTask:gotAccountInfo:error:]
+ -[MobileCalDAVDAAccount dropAssertionsAndRenewCredentialsInQueue:withHandler:]
+ -[MobileCalDAVDAAccount emailAddresses]
+ -[MobileCalDAVDAAccount host]
+ -[MobileCalDAVDAAccount httpPorts]
+ -[MobileCalDAVDAAccount httpsPorts]
+ -[MobileCalDAVDAAccount ingestBackingAccountInfoProperties]
+ -[MobileCalDAVDAAccount initWithBackingAccountInfo:]
+ -[MobileCalDAVDAAccount initWithBackingAccountInfo:].cold.1
+ -[MobileCalDAVDAAccount isCalDAVAccount]
+ -[MobileCalDAVDAAccount isDelegateAccount]
+ -[MobileCalDAVDAAccount isEqualToAccount:]
+ -[MobileCalDAVDAAccount isICloudAccount]
+ -[MobileCalDAVDAAccount localizedIdenticalAccountFailureMessage]
+ -[MobileCalDAVDAAccount localizedInvalidPasswordMessage]
+ -[MobileCalDAVDAAccount logHandle]
+ -[MobileCalDAVDAAccount mainPrincipal]
+ -[MobileCalDAVDAAccount mobileCalDAVAccount]
+ -[MobileCalDAVDAAccount needsToVerifyTerms]
+ -[MobileCalDAVDAAccount noteHomeSetOnDifferentHost:]
+ -[MobileCalDAVDAAccount oauth2Token]
+ -[MobileCalDAVDAAccount onBehalfOfBundleIdentifier]
+ -[MobileCalDAVDAAccount parentAccountIdentifier]
+ -[MobileCalDAVDAAccount performDiscoveryWithHostname:username:consumer:]
+ -[MobileCalDAVDAAccount portListByInsertingUserEnteredPort:]
+ -[MobileCalDAVDAAccount preferredAddress]
+ -[MobileCalDAVDAAccount principalPath]
+ -[MobileCalDAVDAAccount pushDisabled]
+ -[MobileCalDAVDAAccount refreshInterval]
+ -[MobileCalDAVDAAccount removeAccount:]
+ -[MobileCalDAVDAAccount removeFromCoreDAVLoggingDelegates]
+ -[MobileCalDAVDAAccount retryDiscoveryTask:]
+ -[MobileCalDAVDAAccount saveModifiedPropertiesOnBackingAccount]
+ -[MobileCalDAVDAAccount setAccountDescription:]
+ -[MobileCalDAVDAAccount setBackingAccountShouldDoInitialAutodiscovery:]
+ -[MobileCalDAVDAAccount setCheckValidityTaskGroup:]
+ -[MobileCalDAVDAAccount setCoreDAVLogger:]
+ -[MobileCalDAVDAAccount setPrincipalPath:]
+ -[MobileCalDAVDAAccount setPushDisabled:]
+ -[MobileCalDAVDAAccount setRefreshInterval:]
+ -[MobileCalDAVDAAccount setShouldDoInitialAutodiscovery:]
+ -[MobileCalDAVDAAccount setSubscribedCalendars:]
+ -[MobileCalDAVDAAccount shouldDoInitialAutodiscovery]
+ -[MobileCalDAVDAAccount shouldLogTransmittedData]
+ -[MobileCalDAVDAAccount spinnerIdentifiers]
+ -[MobileCalDAVDAAccount subscribedCalendars]
+ -[MobileCalDAVDAAccount taskManager]
+ -[MobileCalDAVDAAccount topLevelAccountTypeIdentifier]
+ -[MobileCalDAVDAAccount upgradeAccount]
+ -[MobileCalDAVDAAccount username]
+ -[MobileCalDAVDAAccount webLoginRequestedAtURL:reasonString:inQueue:completionBlock:]
+ -[MobileCalDAVDAAccount wellKnownPaths]
+ -[MobileCalDAVPrincipal contextDictionary]
+ GCC_except_table101
+ GCC_except_table104
+ GCC_except_table118
+ GCC_except_table120
+ GCC_except_table21
+ GCC_except_table24
+ GCC_except_table27
+ GCC_except_table38
+ GCC_except_table41
+ GCC_except_table47
+ GCC_except_table51
+ GCC_except_table52
+ GCC_except_table61
+ GCC_except_table70
+ GCC_except_table83
+ GCC_except_table97
+ _CalCalendarIsAlwaysReadOnly
+ _CalCalendarIsEffectivelyReadOnly
+ _CalCalendarSetAlwaysReadOnly
+ _OBJC_CLASS_$_MobileCalDAVDAAccount
+ _OBJC_IVAR_$_DACalDAViCalItem._dbHelperForLoadLocalItemWithAccount
+ _OBJC_IVAR_$_MobileCalDAVAccount._backingAccount
+ _OBJC_IVAR_$_MobileCalDAVAccount._principalsDict
+ _OBJC_IVAR_$_MobileCalDAVAccount._wellKnownPaths
+ _OBJC_IVAR_$_MobileCalDAVAccountRefreshActor._cancelCompletionBlock
+ _OBJC_IVAR_$_MobileCalDAVAccountRefreshActor._transaction
+ _OBJC_IVAR_$_MobileCalDAVCalendar._mustCalendarBeReadOnly
+ _OBJC_IVAR_$_MobileCalDAVDAAccount._checkValidityTaskGroup
+ _OBJC_IVAR_$_MobileCalDAVDAAccount._coreDAVLogger
+ _OBJC_IVAR_$_MobileCalDAVDAAccount._hostForDiscovery
+ _OBJC_IVAR_$_MobileCalDAVDAAccount._mobileCalDAVAccount
+ _OBJC_IVAR_$_MobileCalDAVDAAccount._usernameForDiscovery
+ _OBJC_METACLASS_$_MobileCalDAVDAAccount
+ __OBJC_$_CATEGORY_ACAccount_$_MobileCalDAVAccountInfo
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_ACAccount_$_MobileCalDAVAccountInfo
+ __OBJC_$_CLASS_METHODS_MobileCalDAVDAAccount
+ __OBJC_$_INSTANCE_METHODS_MobileCalDAVAccount(CompatibilityShims|CompatibilityShims|CompatibilityShims|CompatibilityShims|CompatibilityShims)
+ __OBJC_$_INSTANCE_METHODS_MobileCalDAVDAAccount
+ __OBJC_$_INSTANCE_VARIABLES_MobileCalDAVDAAccount
+ __OBJC_$_PROP_LIST_ACAccount_$_MobileCalDAVAccountInfo
+ __OBJC_$_PROP_LIST_CalDAVAccount
+ __OBJC_$_PROP_LIST_CoreDAVAccountInfoProvider
+ __OBJC_$_PROP_LIST_MobileCalDAVAccountInfo
+ __OBJC_$_PROP_LIST_MobileCalDAVDAAccount
+ __OBJC_$_PROP_LIST_MobileCalDAVDABackingAccount
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CalDAVAccount
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CoreDAVDiscoveryTaskGroupDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CoreDAVLogDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MobileCalDAVAccountInfo
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MobileCalDAVDABackingAccount
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CoreDAVLogDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CalDAVAccount
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CoreDAVDiscoveryTaskGroupDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CoreDAVLogDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MobileCalDAVAccountInfo
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MobileCalDAVDABackingAccount
+ __OBJC_$_PROTOCOL_REFS_CalDAVAccount
+ __OBJC_$_PROTOCOL_REFS_CoreDAVDiscoveryTaskGroupDelegate
+ __OBJC_$_PROTOCOL_REFS_CoreDAVLogDelegate
+ __OBJC_$_PROTOCOL_REFS_MobileCalDAVAccountInfo
+ __OBJC_$_PROTOCOL_REFS_MobileCalDAVDABackingAccount
+ __OBJC_CATEGORY_PROTOCOLS_$_ACAccount_$_MobileCalDAVAccountInfo
+ __OBJC_CLASS_PROTOCOLS_$_MobileCalDAVDAAccount
+ __OBJC_CLASS_RO_$_MobileCalDAVDAAccount
+ __OBJC_LABEL_PROTOCOL_$_CalDAVAccount
+ __OBJC_LABEL_PROTOCOL_$_CoreDAVDiscoveryTaskGroupDelegate
+ __OBJC_LABEL_PROTOCOL_$_CoreDAVLogDelegate
+ __OBJC_LABEL_PROTOCOL_$_MobileCalDAVAccountInfo
+ __OBJC_LABEL_PROTOCOL_$_MobileCalDAVDABackingAccount
+ __OBJC_METACLASS_RO_$_MobileCalDAVDAAccount
+ __OBJC_PROTOCOL_$_CalDAVAccount
+ __OBJC_PROTOCOL_$_CoreDAVDiscoveryTaskGroupDelegate
+ __OBJC_PROTOCOL_$_CoreDAVLogDelegate
+ __OBJC_PROTOCOL_$_MobileCalDAVAccountInfo
+ __OBJC_PROTOCOL_$_MobileCalDAVDABackingAccount
+ ___51-[MobileCalDAVAccount updateDelegatesWithUserInfo:]_block_invoke
+ ___52-[MobileCalDAVDAAccount initWithBackingAccountInfo:]_block_invoke
+ ___53-[MobileCalDAVAccount refreshWithContext:completion:]_block_invoke
+ ___block_descriptor_56_e8_32s40bs48w_e17_v16?0"NSError"8lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e55_v32?0"NSString"8"MobileCalDAVDelegateUserInfo"16^B24ls32l8s40l8s48l8r56l8r64l8
+ ___block_literal_global.110
+ __os_log_fault_impl
+ _kDACalDAVContextDictionaryKey_DBHelper
+ _objc_msgSend$_checkExistingStoreAndSetChangeReason
+ _objc_msgSend$_defaultAlarmOffsetFromICSString:
+ _objc_msgSend$_discoverInitialPropertiesWithConsumer:
+ _objc_msgSend$_externalInfoDictionary
+ _objc_msgSend$_reallyCancelAllSearchQueries
+ _objc_msgSend$_reallyCancelPendingSearchQuery:
+ _objc_msgSend$_reallyCancelSearchQuery:
+ _objc_msgSend$_reallyPerformSearchQuery:
+ _objc_msgSend$_reallySearchQueriesRunning
+ _objc_msgSend$_releasePowerAssertion
+ _objc_msgSend$_retainPowerAssertion
+ _objc_msgSend$aa_needsToVerifyTerms
+ _objc_msgSend$accountIdentifier
+ _objc_msgSend$accountInfo
+ _objc_msgSend$backingAccount
+ _objc_msgSend$backingAccountShouldDoInitialAutodiscovery
+ _objc_msgSend$cal_isPrimaryAppleAccount
+ _objc_msgSend$calendarsDataclassModified
+ _objc_msgSend$cancelCompletionBlock
+ _objc_msgSend$contextDictionary
+ _objc_msgSend$createChildAccountWithAccountTypeIdentifier:
+ _objc_msgSend$da_stringByAddingPercentEscapesForUsername
+ _objc_msgSend$dbHelper
+ _objc_msgSend$delegateRefreshForPrincipal:completedWithDelegateUserInfo:error:
+ _objc_msgSend$didSetAccountDescription
+ _objc_msgSend$discoverInitialPropertiesWithConsumer:
+ _objc_msgSend$discoveryTask:gotAccountInfo:error:
+ _objc_msgSend$ingestBackingAccountInfoProperties
+ _objc_msgSend$initWithBackingAccount:
+ _objc_msgSend$isICloudAccount
+ _objc_msgSend$mobileCalDAVAccount
+ _objc_msgSend$mobileCalDAVAccountClass
+ _objc_msgSend$parentAccountIdentifier
+ _objc_msgSend$pushDisabled
+ _objc_msgSend$refreshWithCompletion:
+ _objc_msgSend$removeAccount:
+ _objc_msgSend$setAccountDescription:
+ _objc_msgSend$setAccountProperty:forKey:
+ _objc_msgSend$setBackingAccountShouldDoInitialAutodiscovery:
+ _objc_msgSend$setCancelCompletionBlock:
+ _objc_msgSend$setEnabled:forDADataclass:
+ _objc_msgSend$setPassword:
+ _objc_msgSend$setPushDisabled:
+ _objc_msgSend$spinnerIdentifiers
+ _objc_msgSend$topLevelAccountTypeIdentifier
+ _objc_msgSend$updateCalendarStoreWithAlreadyOpenDBShouldCreate:syncingThisAccount:
+ _objc_msgSend$updateDelegatesWithUserInfo:
- +[MobileCalDAVAccount defaultAlarmOffsetFromICSString:]
- -[DACalDAViCalItem _addOrModifyTask:inICSCalendar:withContainer:shouldMergeProperties:outMergeDidChooseLocalProperties:inMobileCalendar:]
- -[MobileCalDAVAccount _setParentAccount:]
- -[MobileCalDAVAccount _setSpinning:]
- -[MobileCalDAVAccount _updateCalendarStoreWithAlreadyOpenDBShouldCreate:syncingThisAccount:]
- -[MobileCalDAVAccount accountHasSignificantPropertyChangesWithChangeInfo:]
- -[MobileCalDAVAccount addToCoreDAVLoggingDelegates]
- -[MobileCalDAVAccount checkExistingStoreAndSetChangeReason]
- -[MobileCalDAVAccount checkValidityTaskGroup]
- -[MobileCalDAVAccount childAccountWithIdentifier:]
- -[MobileCalDAVAccount coreDAVLogTransmittedDataPartial:]
- -[MobileCalDAVAccount coreDAVLogger]
- -[MobileCalDAVAccount coreDAVTransmittedDataFinished]
- -[MobileCalDAVAccount delegateUserInfos]
- -[MobileCalDAVAccount dropPowerAssertions]
- -[MobileCalDAVAccount externalInfoDictionary]
- -[MobileCalDAVAccount httpPorts]
- -[MobileCalDAVAccount httpsPorts]
- -[MobileCalDAVAccount initWithBackingAccountInfo:]
- -[MobileCalDAVAccount initWithBackingAccountInfo:].cold.1
- -[MobileCalDAVAccount isCalDAVAccount]
- -[MobileCalDAVAccount isEqualToAccount:]
- -[MobileCalDAVAccount isSpinning]
- -[MobileCalDAVAccount localizedIdenticalAccountFailureMessage]
- -[MobileCalDAVAccount localizedInvalidPasswordMessage]
- -[MobileCalDAVAccount logHandle]
- -[MobileCalDAVAccount onBehalfOfBundleIdentifier]
- -[MobileCalDAVAccount overriddenPort]
- -[MobileCalDAVAccount overriddenScheme]
- -[MobileCalDAVAccount overriddenServer]
- -[MobileCalDAVAccount performDiscoveryWithHostname:username:consumer:]
- -[MobileCalDAVAccount portListByInsertingUserEnteredPort:]
- -[MobileCalDAVAccount reattainPowerAssertions]
- -[MobileCalDAVAccount refreshWithContext:]
- -[MobileCalDAVAccount releasePowerAssertion]
- -[MobileCalDAVAccount removeFromCoreDAVLoggingDelegates]
- -[MobileCalDAVAccount retainPowerAssertion]
- -[MobileCalDAVAccount retryDiscoveryTask:]
- -[MobileCalDAVAccount serverBaseURL]
- -[MobileCalDAVAccount setCheckValidityTaskGroup:]
- -[MobileCalDAVAccount setCoreDAVLogger:]
- -[MobileCalDAVAccount setDelegateUserInfos:]
- -[MobileCalDAVAccount setIsSpinning:]
- -[MobileCalDAVAccount setOverriddenPort:]
- -[MobileCalDAVAccount setOverriddenScheme:]
- -[MobileCalDAVAccount setOverriddenServer:]
- -[MobileCalDAVAccount setUseKerberos:]
- -[MobileCalDAVAccount shouldLogTransmittedData]
- -[MobileCalDAVAccount updateDelegates]
- -[MobileCalDAVAccount upgradeAccount]
- -[MobileCalDAVAccount useKerberos]
- -[MobileCalDAVAccount viewedTimeZone]
- -[MobileCalDAVAccountRefreshActor delegateRefreshForPrincipal:completedWithError:]
- -[MobileCalDAVAccountRefreshActor refresh]
- -[MobileCalDAVAccountRefreshActor refresh].cold.1
- -[MobileCalDAVCalendar daPrincipal]
- -[MobileCalDAVPrincipal daAccount]
- GCC_except_table122
- GCC_except_table133
- GCC_except_table20
- GCC_except_table23
- GCC_except_table26
- GCC_except_table37
- GCC_except_table40
- GCC_except_table44
- GCC_except_table45
- GCC_except_table60
- GCC_except_table69
- GCC_except_table73
- GCC_except_table88
- GCC_except_table95
- OBJC_IVAR_$_MobileCalDAVAccountRefreshActor._transaction
- _CalAccountPropertyCalDAVUseKerberos
- _CalCalendarIsReadOnly
- _CalCalendarSetReadOnly
- _CalCopyDefaultTimeZone
- _CalDatabaseCopyUpdatedCalTaskFromICSTodoWithOptions
- _OBJC_IVAR_$_MobileCalDAVAccount._checkValidityTaskGroup
- _OBJC_IVAR_$_MobileCalDAVAccount._coreDAVLogger
- _OBJC_IVAR_$_MobileCalDAVAccount._delegateUserInfos
- _OBJC_IVAR_$_MobileCalDAVAccount._hostForDiscovery
- _OBJC_IVAR_$_MobileCalDAVAccount._isSpinning
- _OBJC_IVAR_$_MobileCalDAVAccount._usernameForDiscovery
- __OBJC_$_INSTANCE_METHODS_MobileCalDAVAccount
- __OBJC_$_PROP_LIST_MobileCalDAVAccount
- ___38-[MobileCalDAVAccount updateDelegates]_block_invoke
- ___38-[MobileCalDAVAccount updateDelegates]_block_invoke.158
- ___50-[MobileCalDAVAccount initWithBackingAccountInfo:]_block_invoke
- ___block_descriptor_40_e8_32s_e20_v20?0B8"NSError"12ls32l8
- ___block_descriptor_80_e8_32s40s48s56s64r72r_e55_v32?0"NSString"8"MobileCalDAVDelegateUserInfo"16^B24ls32l8s40l8s48l8s56l8r64l8r72l8
- ___block_literal_global.107
- _kAccountAuthenticationTypeParent
- _objc_msgSend$_setParentAccount:
- _objc_msgSend$_setSpinning:
- _objc_msgSend$_updateCalendarStoreWithAlreadyOpenDBShouldCreate:syncingThisAccount:
- _objc_msgSend$accountTypeWithAccountTypeIdentifier:
- _objc_msgSend$calTopLevelAccount
- _objc_msgSend$checkExistingStoreAndSetChangeReason
- _objc_msgSend$daAccount
- _objc_msgSend$daPrincipal
- _objc_msgSend$defaultAlarmOffsetFromICSString:
- _objc_msgSend$delegateRefreshForPrincipal:completedWithError:
- _objc_msgSend$delegateUserInfos
- _objc_msgSend$dictionaryWithDictionary:
- _objc_msgSend$dropPowerAssertionsForGroupIdentifier:
- _objc_msgSend$externalInfoDictionary
- _objc_msgSend$initWithAccountType:
- _objc_msgSend$initWithBackingAccountInfo:
- _objc_msgSend$isSpinning
- _objc_msgSend$mustCalendarBeReadOnly
- _objc_msgSend$overriddenPort
- _objc_msgSend$overriddenScheme
- _objc_msgSend$overriddenServer
- _objc_msgSend$principals
- _objc_msgSend$reattainPowerAssertionsForGroupIdentifier:
- _objc_msgSend$refresh
- _objc_msgSend$releasePowerAssertion
- _objc_msgSend$removeAccount:withDeleteSync:completion:
- _objc_msgSend$retainPowerAssertion
- _objc_msgSend$setActive:
- _objc_msgSend$setAuthenticationType:
- _objc_msgSend$setDelegateUserInfos:
- _objc_msgSend$setIsSpinning:
- _objc_msgSend$setParentAccount:
- _objc_msgSend$updateDelegates
- _sharedDAAccountStore
CStrings:
+ "#"
+ "@\"<MobileCalDAVAccountInfo>\"16@0:8"
+ "@\"<MobileCalDAVDABackingAccount>\""
+ "@\"<MobileCalDAVDABackingAccount>\"24@0:8@\"NSString\"16"
+ "@\"CalDAVPrincipalSearchPropertySet\"16@0:8"
+ "@\"CalDAVServerVersion\"16@0:8"
+ "@\"DAAccount\"16@0:8"
+ "@\"DACoreDAVTaskManager\"16@0:8"
+ "@\"DALocalDBHelper\""
+ "@\"DALocalDBHelper\"16@0:8"
+ "@\"DAStatusReport\"16@0:8"
+ "@\"DATrustHandler\"16@0:8"
+ "@\"MobileCalDAVAccount\"16@0:8"
+ "@\"MobileCalDAVAccount<CalDAVAccount>\""
+ "@\"NSArray\"24@0:8@\"NSString\"16"
+ "@\"NSObject<OS_os_log>\"16@0:8"
+ "@24@0:8@\"NSString\"16"
+ "@32@0:8@\"NSString\"16@\"<DAEventsAttachmentDownloadConsumer>\"24"
+ "@32@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16@24"
+ "@48@0:8i16i20@24i32i36@40"
+ "B24@0:8^@16"
+ "B36@0:8i16@20^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}28"
+ "B40@0:8@16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24@32"
+ "CalDAVAccount"
+ "CompatibilityShims"
+ "CoreDAVDiscoveryTaskGroupDelegate"
+ "CoreDAVLogDelegate"
+ "Dispatching cancel completion callback on the main queue..."
+ "Failed to find DBHelper in account info provider context dictionary. Falling back on the shared instance."
+ "MobileCalDAVAccountInfo"
+ "MobileCalDAVDAAccount"
+ "MobileCalDAVDABackingAccount"
+ "T@\"<MobileCalDAVAccountInfo>\",R,N"
+ "T@\"<MobileCalDAVDABackingAccount>\",R,W,N,V_backingAccount"
+ "T@\"ACAccount\",R,N"
+ "T@\"CalDAVPrincipalSearchPropertySet\",&,N"
+ "T@\"CalDAVServerVersion\",&,N"
+ "T@\"DAAccount\",R,N"
+ "T@\"DALocalDBHelper\",R,N"
+ "T@\"DAStatusReport\",R,N"
+ "T@\"DATrustHandler\",R,N"
+ "T@\"MobileCalDAVAccount\",R,N,V_mobileCalDAVAccount"
+ "T@\"MobileCalDAVAccount<CalDAVAccount>\",W,N,V_account"
+ "T@\"MobileCalDAVPrincipal<CalDAVPrincipal>\",W,N,V_principal"
+ "T@\"NSArray\",R,N,V_wellKnownPaths"
+ "T@\"NSData\",R,C,N"
+ "T@\"NSDictionary\",?,R,N"
+ "T@\"NSDictionary\",R,N,V_principalsDict"
+ "T@\"NSString\",R,C,N"
+ "T@?,C,N,V_cancelCompletionBlock"
+ "TB,N,GisAuthenticated"
+ "TB,R,N,V_mustCalendarBeReadOnly"
+ "Ti,N,V_objectType"
+ "Unexpected type for DBHelper in account info provider context dictionary. Falling back on the shared instance."
+ "^v32@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16^v24"
+ "^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}"
+ "_backingAccount"
+ "_cancelCompletionBlock"
+ "_checkExistingStoreAndSetChangeReason"
+ "_dbHelperForLoadLocalItemWithAccount"
+ "_defaultAlarmOffsetFromICSString:"
+ "_discoverInitialPropertiesWithConsumer:"
+ "_externalInfoDictionary"
+ "_mobileCalDAVAccount"
+ "_mustCalendarBeReadOnly"
+ "_principalsDict"
+ "_reallyCancelPendingSearchQuery:"
+ "_releasePowerAssertion"
+ "_retainPowerAssertion"
+ "_wellKnownPaths"
+ "aa_needsToVerifyTerms"
+ "accountIdentifier"
+ "accountInfo"
+ "authenticated"
+ "backingAccount"
+ "backingAccountShouldDoInitialAutodiscovery"
+ "cal_isPrimaryAppleAccount"
+ "cancelCompletionBlock"
+ "contextDictionary"
+ "coreDAVLogDiagnosticMessage:atLevel:"
+ "coreDAVLogLevel"
+ "coreDAVLogRequestBody:"
+ "coreDAVLogResponseBody:"
+ "coreDAVOutputLevel"
+ "createChildAccountWithAccountTypeIdentifier:"
+ "da_stringByAddingPercentEscapesForUsername"
+ "dbHelper"
+ "delegateRefreshForPrincipal:completedWithDelegateUserInfo:error:"
+ "didSetAccountDescription"
+ "hostWithoutPath"
+ "initWithBackingAccount:"
+ "isAuthenticated"
+ "isICloudAccount"
+ "kDACalDAVContextDictionaryKey_DBHelper"
+ "mobileCalDAVAccount"
+ "mobileCalDAVAccountClass"
+ "needsToVerifyTerms"
+ "parentAccountIdentifier"
+ "principalsDict"
+ "refreshWithCompletion:"
+ "refreshWithContext:completion:"
+ "removeAccount:"
+ "setAccountProperty:forKey:"
+ "setAuthenticated:"
+ "setBackingAccountShouldDoInitialAutodiscovery:"
+ "setCancelCompletionBlock:"
+ "setEnabled:forDADataclass:"
+ "setIsValidating:"
+ "setPassword:"
+ "setUser:"
+ "setWasUserInitiated:"
+ "supportsAuthentication"
+ "topLevelAccountTypeIdentifier"
+ "trustHandler"
+ "updateCalendarStoreWithAlreadyOpenDBShouldCreate:syncingThisAccount:"
+ "updateDelegatesWithUserInfo:"
+ "updateExistingAccountProperties"
+ "v16@?0@\"NSError\"8"
+ "v24@0:8@\"<DAValidityCheckConsumer>\"16"
+ "v24@0:8@\"<MobileCalDAVAccountInfo>\"16"
+ "v24@0:8@\"CalDAVPrincipalSearchPropertySet\"16"
+ "v24@0:8@\"CalDAVServerVersion\"16"
+ "v24@0:8@\"NSData\"16"
+ "v24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16"
+ "v28@0:8B16q20"
+ "v32@0:8@\"NSObject<OS_dispatch_queue>\"16@?<v@?q@\"NSError\">24"
+ "v32@0:8@\"NSString\"16q24"
+ "v32@0:8@16@\"<NSCopying>\"24"
+ "v32@0:8@16@\"NSString\"24"
+ "v32@0:8@16@?24"
+ "v32@0:8@16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24"
+ "v32@0:8@16q24"
+ "v40@0:8@\"<CalDAVPrincipal>\"16@\"NSDictionary\"24@\"NSError\"32"
+ "v40@0:8@\"CoreDAVDiscoveryTaskGroup\"16@\"<CoreDAVAccountInfoProvider>\"24@\"NSError\"32"
+ "wasUserInitiated"
+ "\x81"
+ "\xb1"
- "%@://%@:%ld"
- "@\"<CalDAVAccount>\""
- "@\"MobileCalDAVPrincipal\""
- "@32@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}16@24"
- "@52@0:8i16i20@24i32q36@44"
- "Adding or modifying todo with guid %@\n"
- "B36@0:8i16@20^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}28"
- "B40@0:8@16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}24@32"
- "Could not create CalTask for %@."
- "Could not find local CalDAV calendar %@ for the account \"%@\" (%{public}@). Refusing to add todo."
- "Delegate with account ID %@ failed to be removed"
- "Delegate with account ID %@ was successfully removed"
- "Dispatching result callback on the main queue..."
- "T@\"<CalDAVAccount>\",W,N,V_account"
- "T@\"<CalDAVPrincipal>\",&,N"
- "T@\"<CalDAVPrincipal>\",W,N"
- "T@\"MobileCalDAVPrincipal\",R,N"
- "T@\"NSDictionary\",&,N,V_delegateUserInfos"
- "T@\"NSTimeZone\",R,N"
- "TB,N,V_isSpinning"
- "Tq,N,V_objectType"
- "^v32@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}16^v24"
- "^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}"
- "_addOrModifyTask:inICSCalendar:withContainer:shouldMergeProperties:outMergeDidChooseLocalProperties:inMobileCalendar:"
- "_delegateUserInfos"
- "_isSpinning"
- "_setParentAccount:"
- "_setSpinning:"
- "_updateCalendarStoreWithAlreadyOpenDBShouldCreate:syncingThisAccount:"
- "accountTypeWithAccountTypeIdentifier:"
- "calTopLevelAccount"
- "checkExistingStoreAndSetChangeReason"
- "daPrincipal"
- "defaultAlarmOffsetFromICSString:"
- "delegateRefreshForPrincipal:completedWithError:"
- "delegateUserInfos"
- "dictionaryWithDictionary:"
- "dropPowerAssertions"
- "dropPowerAssertionsForGroupIdentifier:"
- "externalInfoDictionary"
- "initWithAccountType:"
- "isSpinning"
- "overriddenPort"
- "overriddenScheme"
- "overriddenServer"
- "reattainPowerAssertions"
- "reattainPowerAssertionsForGroupIdentifier:"
- "refresh"
- "refreshWithContext:"
- "releasePowerAssertion"
- "removeAccount:withDeleteSync:completion:"
- "retainPowerAssertion"
- "serverBaseURL"
- "setActive:"
- "setAuthenticationType:"
- "setDelegateUserInfos:"
- "setIsSpinning:"
- "setOverriddenPort:"
- "setOverriddenScheme:"
- "setOverriddenServer:"
- "setParentAccount:"
- "setUseKerberos:"
- "updateDelegates"
- "useKerberos"
- "v20@?0B8@\"NSError\"12"
- "v24@0:8@\"<CalDAVPrincipal>\"16"
- "v24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}16"
- "v32@0:8@16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}24"
- "viewedTimeZone"

```
