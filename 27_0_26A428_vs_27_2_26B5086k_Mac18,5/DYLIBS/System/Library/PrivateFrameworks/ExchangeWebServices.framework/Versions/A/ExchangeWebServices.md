## ExchangeWebServices

> `/System/Library/PrivateFrameworks/ExchangeWebServices.framework/Versions/A/ExchangeWebServices`

```diff

-844.0.0.0.0
-  __TEXT.__text: 0x37dd4
-  __TEXT.__objc_methlist: 0xa600
-  __TEXT.__const: 0x108
-  __TEXT.__cstring: 0xa103
-  __TEXT.__oslogstring: 0xd8f
-  __TEXT.__gcc_except_tab: 0x56c
-  __TEXT.__unwind_info: 0x1440
+846.200.41.1.1
+  __TEXT.__text: 0x40ca4
+  __TEXT.__objc_methlist: 0xb110
+  __TEXT.__const: 0x188
+  __TEXT.__cstring: 0xaa34
+  __TEXT.__oslogstring: 0xf6c
+  __TEXT.__gcc_except_tab: 0x5f0
+  __TEXT.__unwind_info: 0x1788
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x24f0
-  __DATA_CONST.__objc_classlist: 0xf08
+  __DATA_CONST.__const: 0x25d0
+  __DATA_CONST.__objc_classlist: 0xfa0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3898
+  __DATA_CONST.__objc_selrefs: 0x3f38
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x400
-  __DATA_CONST.__objc_arraydata: 0x78
-  __DATA_CONST.__got: 0x1000
-  __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0xfe80
-  __AUTH_CONST.__objc_const: 0x49070
+  __DATA_CONST.__objc_superrefs: 0x458
+  __DATA_CONST.__objc_arraydata: 0xf0
+  __DATA_CONST.__got: 0x10f0
+  __AUTH_CONST.__const: 0x720
+  __AUTH_CONST.__cfstring: 0x107c0
+  __AUTH_CONST.__objc_const: 0x49e28
+  __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__auth_got: 0x290
-  __AUTH.__objc_data: 0x9650
-  __DATA.__objc_ivar: 0xf50
-  __DATA.__data: 0x548
+  __AUTH_CONST.__auth_got: 0x338
+  __AUTH.__objc_data: 0x9c40
+  __DATA.__objc_ivar: 0x1010
+  __DATA.__data: 0x550
   __DATA.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/OpenDirectory.framework/Versions/A/OpenDirectory
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/AccountsDaemon.framework/Versions/A/AccountsDaemon
+  - /System/Library/PrivateFrameworks/DeviceConfiguration.framework/Versions/A/DeviceConfiguration
   - /System/Library/PrivateFrameworks/KerberosHelper.framework/Versions/A/KerberosHelper
   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3007
-  Symbols:   8415
-  CStrings:  2141
+  Functions: 3263
+  Symbols:   9106
+  CStrings:  2236
 
Symbols:
+ +[EWSExchangeServiceBinding _denialReportRepeatTimeForTests]
+ +[EWSExchangeServiceBinding _setDenialReportRepeatTimeForTests:]
+ +[EWSMailboxDenialPolicy denialQualifiesWithCount:countThreshold:]
+ +[EWSMailboxDenialPolicy denialReasonForOptionsPayload:]
+ +[EWSMailboxDenialPolicy denialReasonForStatusCode:isAccessDeniedFault:faultMessage:]
+ +[EWSMailboxDenialPolicy denialReasonForToken:]
+ +[EWSMailboxDenialPolicy optionsPayloadForDenialReason:]
+ +[EWSMailboxDenialPolicy shouldPublishReportingEnabled:currentValue:accountInStore:retrying:]
+ +[EWSMailboxDenialPolicy shouldRecordDenialGivenIntervalSinceLastDenial:spacingInterval:]
+ +[EWSMailboxDenialPolicy statusCodeIsAccessDeniedRefusal:isAccessDeniedFault:]
+ +[EWSMailboxDenialPolicy statusCodeIsMailboxSuccess:faultReceived:]
+ +[EWSMailboxLocationPolicy durableLocationForProbedLocation:statusCode:]
+ +[EWSMailboxLocationPolicy mailboxLocationForProbeData:error:]
+ +[EWSMailboxLocationPolicy probeURLForEmailAddress:]
+ +[EWSMailboxLocationProbe _responseInvalidError]
+ +[EWSMailboxLocationProbe sendServerLocationRequestForEmailAddress:session:completion:]
+ +[EWSMailboxLocationStore locationForToken:]
+ +[EWSManagementRestrictionPolicy accountIsManagedWithManagingOwnerIdentifier:]
+ +[EWSManagementRestrictionPolicy alertsSuppressedForManagedAccount:permission:]
+ +[EWSManagementRestrictionPolicy permissionForAllowAlertsValue:]
+ +[EWSManagementRestrictionPolicy permissionForToken:]
+ +[EWSManagementRestrictionReader effectivePermission]
+ +[EWSManagementRestrictionReader log]
+ +[EWSManagementRestrictionReader permissionForConfiguration:]
+ +[EWSOAuthTenantPolicy tenantInURIString:]
+ +[EWSOAuthTenantPolicy uriString:withTenant:]
+ +[EWSRetirementAlertConfiguration _disabledConfiguration]
+ +[EWSRetirementAlertCoordinator log]
+ +[EWSRetirementAlertCoordinator sharedCoordinator]
+ +[EWSRetirementAlertPolicy dueAlertKindForAffectedAccounts:coveredAccounts:intervalSinceLastShown:shownGeneration:alertKind:configuration:]
+ +[EWSRetirementAlertPolicy intervalSinceDate:]
+ +[EWSRetirementAlertPolicy shouldClassifyMailboxLocation:intervalSinceLastAttempt:retryInterval:]
+ +[EWSRetirementAlertPolicy shouldRecordClassificationAttemptForStatusCode:]
+ +[EWSRetirementAlertPresenter _postAlertWithParameters:learnMoreURL:posted:acknowledged:transaction:]
+ +[EWSRetirementAlertPresenter accountListDescriptionForNames:]
+ +[EWSRetirementAlertPresenter presentAlertOfKind:accountNames:learnMoreURL:posted:acknowledged:]
+ +[EWSRetirementAlertPresenter responseForError:flags:]
+ +[EWSRetirementAlertStore sharedStore]
+ +[EWSServerConfigurationFetcher configurationFromData:response:error:]
+ +[EWSServerConfigurationStore sharedStore]
+ +[ExchangeOAuthClient graphTestTenantEnabled]
+ -[EWSAutodiscoverV2Binding boundsProbeLifetime]
+ -[EWSAutodiscoverV2Binding setBoundsProbeLifetime:]
+ -[EWSAutodiscoverV2Operation initWithEmailAddress:binding:boundsProbeLifetime:]
+ -[EWSExchangeServiceBinding _accountEligibleForMailboxReporting]
+ -[EWSExchangeServiceBinding _mailboxDenialReportingAllowedForAccount:]
+ -[EWSExchangeServiceBinding _reportMailboxAccessRestoredWithTask:bindingTask:]
+ -[EWSExchangeServiceBinding _reportMailboxDenialWithTask:bindingTask:]
+ -[EWSExchangeServiceBinding _sendMailboxReportForAccount:optionKey:value:]
+ -[EWSExchangeServiceBinding _shouldReportAccessRestoredForAccountIdentifier:]
+ -[EWSExchangeServiceBinding _shouldReportDenialForAccountIdentifier:]
+ -[EWSExchangeServiceBinding reportsMailboxDenials]
+ -[EWSExchangeServiceBinding setReportsMailboxDenials:]
+ -[EWSExchangeServiceBindingTask _captureFault:]
+ -[EWSExchangeServiceBindingTask faultIsAccessDenied]
+ -[EWSExchangeServiceBindingTask faultMessage]
+ -[EWSExchangeServiceBindingTask faultReceived]
+ -[EWSExchangeServiceBindingTask setFaultIsAccessDenied:]
+ -[EWSExchangeServiceBindingTask setFaultMessage:]
+ -[EWSExchangeServiceBindingTask setFaultReceived:]
+ -[EWSMailboxDenialRecord .cxx_destruct]
+ -[EWSMailboxDenialRecord count]
+ -[EWSMailboxDenialRecord initWithReason:count:lastDenialDate:]
+ -[EWSMailboxDenialRecord init]
+ -[EWSMailboxDenialRecord lastDenialDate]
+ -[EWSMailboxDenialRecord reason]
+ -[EWSMailboxDenialStore _countForAccountIdentifier:]
+ -[EWSMailboxDenialStore _keySuffixes]
+ -[EWSMailboxDenialStore _lastDenialDateForAccountIdentifier:]
+ -[EWSMailboxDenialStore _reasonForAccountIdentifier:]
+ -[EWSMailboxDenialStore _recordForAccountIdentifier:]
+ -[EWSMailboxDenialStore clearDenialForAccountIdentifier:]
+ -[EWSMailboxDenialStore denialRecordForAccountIdentifier:]
+ -[EWSMailboxDenialStore initWithPreferencesDomain:]
+ -[EWSMailboxDenialStore invalidateCachedValues]
+ -[EWSMailboxDenialStore pruneAccountsNotIn:]
+ -[EWSMailboxDenialStore recordDenialWithReason:date:spacingInterval:forAccountIdentifier:]
+ -[EWSMailboxLocationStore _attemptKeyForAccountIdentifier:]
+ -[EWSMailboxLocationStore _keySuffixes]
+ -[EWSMailboxLocationStore _locationKeyForAccountIdentifier:]
+ -[EWSMailboxLocationStore initWithPreferencesDomain:]
+ -[EWSMailboxLocationStore invalidateCachedValues]
+ -[EWSMailboxLocationStore lastAttemptDateForAccountIdentifier:]
+ -[EWSMailboxLocationStore locationForAccountIdentifier:]
+ -[EWSMailboxLocationStore pruneAccountsNotIn:]
+ -[EWSMailboxLocationStore recordLocation:attemptDate:forAccountIdentifier:]
+ -[EWSPreferenceStore .cxx_destruct]
+ -[EWSPreferenceStore _accountIdentifierForKey:]
+ -[EWSPreferenceStore _keyForAccountIdentifier:suffix:]
+ -[EWSPreferenceStore _keyList]
+ -[EWSPreferenceStore _keySuffixes]
+ -[EWSPreferenceStore _setValue:forKey:]
+ -[EWSPreferenceStore _staleKeysForAccountIdentifiers:]
+ -[EWSPreferenceStore _synchronize]
+ -[EWSPreferenceStore _valueForKey:]
+ -[EWSPreferenceStore domain]
+ -[EWSPreferenceStore initWithPreferencesDomain:]
+ -[EWSPreferenceStore init]
+ -[EWSRetirementAlertAccountSnapshot .cxx_destruct]
+ -[EWSRetirementAlertAccountSnapshot displayName]
+ -[EWSRetirementAlertAccountSnapshot emailAddress]
+ -[EWSRetirementAlertAccountSnapshot identifier]
+ -[EWSRetirementAlertAccountSnapshot initWithIdentifier:emailAddress:displayName:inAccountStore:managed:]
+ -[EWSRetirementAlertAccountSnapshot init]
+ -[EWSRetirementAlertAccountSnapshot isInAccountStore]
+ -[EWSRetirementAlertAccountSnapshot isManaged]
+ -[EWSRetirementAlertConfiguration .cxx_destruct]
+ -[EWSRetirementAlertConfiguration classificationRetryInterval]
+ -[EWSRetirementAlertConfiguration configurationForAlertKind:]
+ -[EWSRetirementAlertConfiguration denialCountThreshold]
+ -[EWSRetirementAlertConfiguration denialSpacingInterval]
+ -[EWSRetirementAlertConfiguration initWithEnabled:classificationRetryInterval:denialCountThreshold:denialSpacingInterval:proactiveConfiguration:reactiveConfiguration:]
+ -[EWSRetirementAlertConfiguration init]
+ -[EWSRetirementAlertConfiguration isEnabled]
+ -[EWSRetirementAlertConfiguration proactiveConfiguration]
+ -[EWSRetirementAlertConfiguration reactiveConfiguration]
+ -[EWSRetirementAlertCoordinator .cxx_destruct]
+ -[EWSRetirementAlertCoordinator _accountsByIdentifierForAccounts:]
+ -[EWSRetirementAlertCoordinator _adoptSharedServerConfiguration]
+ -[EWSRetirementAlertCoordinator _anyAlertEnabledForConfiguration:]
+ -[EWSRetirementAlertCoordinator _beginCycle]
+ -[EWSRetirementAlertCoordinator _denialReasonForAccountIdentifier:configuration:simulatedReason:]
+ -[EWSRetirementAlertCoordinator _displayNameForAccount:]
+ -[EWSRetirementAlertCoordinator _endCycleWithToken:completion:]
+ -[EWSRetirementAlertCoordinator _evaluateAlertForAccounts:overriddenLocation:excludedIdentifiers:]
+ -[EWSRetirementAlertCoordinator _finishCycleWithAccounts:excludedIdentifiers:overriddenLocation:token:completion:]
+ -[EWSRetirementAlertCoordinator _isCurrentCycleToken:]
+ -[EWSRetirementAlertCoordinator _learnMoreURLForConfiguration:]
+ -[EWSRetirementAlertCoordinator _presentAlertOfKind:affectedAccounts:accounts:configuration:recordsHistory:]
+ -[EWSRetirementAlertCoordinator _reactiveAlertEnabledForConfiguration:]
+ -[EWSRetirementAlertCoordinator _runCycleWithAccounts:excludedIdentifiers:token:completion:]
+ -[EWSRetirementAlertCoordinator _shouldClassifyAccountWithIdentifier:configuration:]
+ -[EWSRetirementAlertCoordinator _treatsAccountAsManaged:identifier:simulatedManaged:]
+ -[EWSRetirementAlertCoordinator alertStore]
+ -[EWSRetirementAlertCoordinator alertsSuppressedForAccountIdentifier:managed:]
+ -[EWSRetirementAlertCoordinator clearDenialForAccountIdentifier:]
+ -[EWSRetirementAlertCoordinator considerAlertsForAccounts:excludingAccountIdentifier:]
+ -[EWSRetirementAlertCoordinator considerAlertsForAccounts:excludingAccountIdentifiers:completion:]
+ -[EWSRetirementAlertCoordinator cycleAgeBound]
+ -[EWSRetirementAlertCoordinator denialReportingEnabledForAccountIdentifier:managed:]
+ -[EWSRetirementAlertCoordinator denialReportingEnabled]
+ -[EWSRetirementAlertCoordinator denialStore]
+ -[EWSRetirementAlertCoordinator initWithLocationStore:alertStore:denialStore:managementPermissionProvider:presentationHandler:]
+ -[EWSRetirementAlertCoordinator locationStore]
+ -[EWSRetirementAlertCoordinator managementPermissionProvider]
+ -[EWSRetirementAlertCoordinator managementPermission]
+ -[EWSRetirementAlertCoordinator presentationHandler]
+ -[EWSRetirementAlertCoordinator recordDenialWithReason:forAccountIdentifier:managed:]
+ -[EWSRetirementAlertCoordinator serverConfigurationFetcher]
+ -[EWSRetirementAlertCoordinator session]
+ -[EWSRetirementAlertCoordinator setCycleAgeBound:]
+ -[EWSRetirementAlertCoordinator setServerConfigurationFetcher:]
+ -[EWSRetirementAlertKindConfiguration .cxx_destruct]
+ -[EWSRetirementAlertKindConfiguration generation]
+ -[EWSRetirementAlertKindConfiguration initWithEnabled:repeatInterval:generation:learnMoreURL:]
+ -[EWSRetirementAlertKindConfiguration init]
+ -[EWSRetirementAlertKindConfiguration isEnabled]
+ -[EWSRetirementAlertKindConfiguration learnMoreURL]
+ -[EWSRetirementAlertKindConfiguration repeatInterval]
+ -[EWSRetirementAlertStore .cxx_destruct]
+ -[EWSRetirementAlertStore _URLForKey:fallback:]
+ -[EWSRetirementAlertStore _boolForKey:fallback:]
+ -[EWSRetirementAlertStore _configurationStringForKey:]
+ -[EWSRetirementAlertStore _configurationValueForKey:]
+ -[EWSRetirementAlertStore _coveredAccountsForKey:]
+ -[EWSRetirementAlertStore _coveredAccountsKeyForAlertKind:]
+ -[EWSRetirementAlertStore _integerForKey:fallback:]
+ -[EWSRetirementAlertStore _intervalForKey:fallback:]
+ -[EWSRetirementAlertStore _intervalForKey:fallback:serverMinimum:]
+ -[EWSRetirementAlertStore _intervalFromValue:fallback:]
+ -[EWSRetirementAlertStore _isUsableInterval:]
+ -[EWSRetirementAlertStore _lastShownKeyForAlertKind:]
+ -[EWSRetirementAlertStore _numberFromValue:]
+ -[EWSRetirementAlertStore _shownGenerationKeyForAlertKind:]
+ -[EWSRetirementAlertStore _stringFromValue:]
+ -[EWSRetirementAlertStore coveredAccountsForAlertKind:]
+ -[EWSRetirementAlertStore currentConfiguration]
+ -[EWSRetirementAlertStore initWithPreferencesDomain:]
+ -[EWSRetirementAlertStore invalidateCachedValues]
+ -[EWSRetirementAlertStore lastShownDateForAlertKind:]
+ -[EWSRetirementAlertStore overriddenMailboxLocation]
+ -[EWSRetirementAlertStore overriddenManagementPermission]
+ -[EWSRetirementAlertStore pruneCoveredAccountsForAlertKind:toPresentAccounts:]
+ -[EWSRetirementAlertStore recordAlertAcknowledged:coveringAccounts:generation:]
+ -[EWSRetirementAlertStore recordAlertPosted:date:]
+ -[EWSRetirementAlertStore removeCoveredAccount:forAlertKind:]
+ -[EWSRetirementAlertStore serverConfigurationStore]
+ -[EWSRetirementAlertStore setServerConfigurationStore:]
+ -[EWSRetirementAlertStore shownGenerationForAlertKind:]
+ -[EWSRetirementAlertStore simulatedDenialReason]
+ -[EWSRetirementAlertStore simulatedManagedAccountIdentifiers]
+ -[EWSServerConfigurationFetcher .cxx_destruct]
+ -[EWSServerConfigurationFetcher _consumeData:response:error:]
+ -[EWSServerConfigurationFetcher fetchInFlight]
+ -[EWSServerConfigurationFetcher fetchTransaction]
+ -[EWSServerConfigurationFetcher initWithStore:]
+ -[EWSServerConfigurationFetcher init]
+ -[EWSServerConfigurationFetcher refreshIfStaleWithValidityInterval:]
+ -[EWSServerConfigurationFetcher setFetchInFlight:]
+ -[EWSServerConfigurationFetcher setFetchTransaction:]
+ -[EWSServerConfigurationFetcher setTransportForTests:]
+ -[EWSServerConfigurationFetcher store]
+ -[EWSServerConfigurationFetcher transportForTests]
+ -[EWSServerConfigurationStore _payload]
+ -[EWSServerConfigurationStore _repairedDateForKey:]
+ -[EWSServerConfigurationStore clearConfiguration]
+ -[EWSServerConfigurationStore configurationURL]
+ -[EWSServerConfigurationStore configurationValueForKey:]
+ -[EWSServerConfigurationStore initWithPreferencesDomain:]
+ -[EWSServerConfigurationStore invalidateCachedValues]
+ -[EWSServerConfigurationStore lastAttemptDate]
+ -[EWSServerConfigurationStore lastFetchDate]
+ -[EWSServerConfigurationStore needsRefreshWithValidityInterval:]
+ -[EWSServerConfigurationStore recordFetchFailureAtDate:]
+ -[EWSServerConfigurationStore storeConfiguration:fetchDate:]
+ -[ExchangeAutodiscovererV2 boundsProbeLifetime]
+ -[ExchangeAutodiscovererV2 setBoundsProbeLifetime:]
+ EWSMailboxReportStateInitialize.onceToken
+ EWSServerConfigurationKnownKeys
+ EWSServerConfigurationKnownKeys.keys
+ EWSServerConfigurationKnownKeys.onceToken
+ GCC_except_table33
+ GCC_except_table35
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table4
+ GCC_except_table48
+ GCC_except_table49
+ GCC_except_table54
+ GCC_except_table60
+ GCC_except_table61
+ GCC_except_table62
+ OBJC_IVAR_$_EWSAutodiscoverV2Binding._boundsProbeLifetime
+ OBJC_IVAR_$_EWSExchangeServiceBinding._reportsMailboxDenials
+ OBJC_IVAR_$_EWSExchangeServiceBindingTask._faultIsAccessDenied
+ OBJC_IVAR_$_EWSExchangeServiceBindingTask._faultMessage
+ OBJC_IVAR_$_EWSExchangeServiceBindingTask._faultReceived
+ OBJC_IVAR_$_EWSMailboxDenialRecord._count
+ OBJC_IVAR_$_EWSMailboxDenialRecord._lastDenialDate
+ OBJC_IVAR_$_EWSMailboxDenialRecord._reason
+ OBJC_IVAR_$_EWSMailboxDenialStore._writeLock
+ OBJC_IVAR_$_EWSMailboxLocationStore._writeLock
+ OBJC_IVAR_$_EWSPreferenceStore._domain
+ OBJC_IVAR_$_EWSRetirementAlertAccountSnapshot._displayName
+ OBJC_IVAR_$_EWSRetirementAlertAccountSnapshot._emailAddress
+ OBJC_IVAR_$_EWSRetirementAlertAccountSnapshot._identifier
+ OBJC_IVAR_$_EWSRetirementAlertAccountSnapshot._inAccountStore
+ OBJC_IVAR_$_EWSRetirementAlertAccountSnapshot._managed
+ OBJC_IVAR_$_EWSRetirementAlertConfiguration._classificationRetryInterval
+ OBJC_IVAR_$_EWSRetirementAlertConfiguration._denialCountThreshold
+ OBJC_IVAR_$_EWSRetirementAlertConfiguration._denialSpacingInterval
+ OBJC_IVAR_$_EWSRetirementAlertConfiguration._enabled
+ OBJC_IVAR_$_EWSRetirementAlertConfiguration._proactiveConfiguration
+ OBJC_IVAR_$_EWSRetirementAlertConfiguration._reactiveConfiguration
+ OBJC_IVAR_$_EWSRetirementAlertCoordinator._alertStore
+ OBJC_IVAR_$_EWSRetirementAlertCoordinator._cycleAgeBound
+ OBJC_IVAR_$_EWSRetirementAlertCoordinator._cycleInFlight
+ OBJC_IVAR_$_EWSRetirementAlertCoordinator._cycleLock
+ OBJC_IVAR_$_EWSRetirementAlertCoordinator._cycleStartedAt
+ OBJC_IVAR_$_EWSRetirementAlertCoordinator._cycleToken
+ OBJC_IVAR_$_EWSRetirementAlertCoordinator._cycleTransaction
+ OBJC_IVAR_$_EWSRetirementAlertCoordinator._denialStore
+ OBJC_IVAR_$_EWSRetirementAlertCoordinator._locationStore
+ OBJC_IVAR_$_EWSRetirementAlertCoordinator._managementPermissionProvider
+ OBJC_IVAR_$_EWSRetirementAlertCoordinator._presentationHandler
+ OBJC_IVAR_$_EWSRetirementAlertCoordinator._serverConfigurationFetcher
+ OBJC_IVAR_$_EWSRetirementAlertCoordinator._session
+ OBJC_IVAR_$_EWSRetirementAlertKindConfiguration._enabled
+ OBJC_IVAR_$_EWSRetirementAlertKindConfiguration._generation
+ OBJC_IVAR_$_EWSRetirementAlertKindConfiguration._learnMoreURL
+ OBJC_IVAR_$_EWSRetirementAlertKindConfiguration._repeatInterval
+ OBJC_IVAR_$_EWSRetirementAlertStore._serverConfigurationStore
+ OBJC_IVAR_$_EWSRetirementAlertStore._stateLock
+ OBJC_IVAR_$_EWSServerConfigurationFetcher._fetchInFlight
+ OBJC_IVAR_$_EWSServerConfigurationFetcher._fetchTransaction
+ OBJC_IVAR_$_EWSServerConfigurationFetcher._inFlightLock
+ OBJC_IVAR_$_EWSServerConfigurationFetcher._store
+ OBJC_IVAR_$_EWSServerConfigurationFetcher._transportForTests
+ OBJC_IVAR_$_EWSServerConfigurationStore._writeLock
+ OBJC_IVAR_$_ExchangeAutodiscovererV2._boundsProbeLifetime
+ _ACAccountPropertyExchangeGraphAPIEndpointURI
+ _CFPreferencesCopyKeyList
+ _CFPreferencesCopyValue
+ _CFPreferencesSetValue
+ _CFPreferencesSynchronize
+ _CFUserNotificationCancel
+ _CFUserNotificationCreate
+ _CFUserNotificationReceiveResponse
+ _DenialReportRepeatTime
+ _EWSMailboxDenialFaultMessageContains
+ _EWSServerConfigurationKnownKeys
+ _LSOpenCFURLRef
+ _OBJC_CLASS_$_DCUserConsumer
+ _OBJC_CLASS_$_EWSMailboxDenialPolicy
+ _OBJC_CLASS_$_EWSMailboxDenialRecord
+ _OBJC_CLASS_$_EWSMailboxDenialStore
+ _OBJC_CLASS_$_EWSMailboxLocationPolicy
+ _OBJC_CLASS_$_EWSMailboxLocationProbe
+ _OBJC_CLASS_$_EWSMailboxLocationStore
+ _OBJC_CLASS_$_EWSManagementRestrictionPolicy
+ _OBJC_CLASS_$_EWSManagementRestrictionReader
+ _OBJC_CLASS_$_EWSOAuthTenantPolicy
+ _OBJC_CLASS_$_EWSPreferenceStore
+ _OBJC_CLASS_$_EWSRetirementAlertAccountSnapshot
+ _OBJC_CLASS_$_EWSRetirementAlertConfiguration
+ _OBJC_CLASS_$_EWSRetirementAlertCoordinator
+ _OBJC_CLASS_$_EWSRetirementAlertKindConfiguration
+ _OBJC_CLASS_$_EWSRetirementAlertPolicy
+ _OBJC_CLASS_$_EWSRetirementAlertPresenter
+ _OBJC_CLASS_$_EWSRetirementAlertStore
+ _OBJC_CLASS_$_EWSServerConfigurationFetcher
+ _OBJC_CLASS_$_EWSServerConfigurationStore
+ _OBJC_CLASS_$_NSListFormatter
+ _OBJC_CLASS_$_NSSet
+ _OBJC_METACLASS_$_EWSMailboxDenialPolicy
+ _OBJC_METACLASS_$_EWSMailboxDenialRecord
+ _OBJC_METACLASS_$_EWSMailboxDenialStore
+ _OBJC_METACLASS_$_EWSMailboxLocationPolicy
+ _OBJC_METACLASS_$_EWSMailboxLocationProbe
+ _OBJC_METACLASS_$_EWSMailboxLocationStore
+ _OBJC_METACLASS_$_EWSManagementRestrictionPolicy
+ _OBJC_METACLASS_$_EWSManagementRestrictionReader
+ _OBJC_METACLASS_$_EWSOAuthTenantPolicy
+ _OBJC_METACLASS_$_EWSPreferenceStore
+ _OBJC_METACLASS_$_EWSRetirementAlertAccountSnapshot
+ _OBJC_METACLASS_$_EWSRetirementAlertConfiguration
+ _OBJC_METACLASS_$_EWSRetirementAlertCoordinator
+ _OBJC_METACLASS_$_EWSRetirementAlertKindConfiguration
+ _OBJC_METACLASS_$_EWSRetirementAlertPolicy
+ _OBJC_METACLASS_$_EWSRetirementAlertPresenter
+ _OBJC_METACLASS_$_EWSRetirementAlertStore
+ _OBJC_METACLASS_$_EWSServerConfigurationFetcher
+ _OBJC_METACLASS_$_EWSServerConfigurationStore
+ __108-[EWSRetirementAlertCoordinator _presentAlertOfKind:affectedAccounts:accounts:configuration:recordsHistory:]_block_invoke
+ __68-[EWSServerConfigurationFetcher refreshIfStaleWithValidityInterval:]_block_invoke
+ __92-[EWSRetirementAlertCoordinator _runCycleWithAccounts:excludedIdentifiers:token:completion:]_block_invoke
+ __OBJC_$_CLASS_METHODS_EWSMailboxDenialPolicy
+ __OBJC_$_CLASS_METHODS_EWSMailboxLocationPolicy
+ __OBJC_$_CLASS_METHODS_EWSMailboxLocationProbe
+ __OBJC_$_CLASS_METHODS_EWSMailboxLocationStore
+ __OBJC_$_CLASS_METHODS_EWSManagementRestrictionPolicy
+ __OBJC_$_CLASS_METHODS_EWSManagementRestrictionReader
+ __OBJC_$_CLASS_METHODS_EWSOAuthTenantPolicy
+ __OBJC_$_CLASS_METHODS_EWSRetirementAlertConfiguration
+ __OBJC_$_CLASS_METHODS_EWSRetirementAlertCoordinator
+ __OBJC_$_CLASS_METHODS_EWSRetirementAlertPolicy
+ __OBJC_$_CLASS_METHODS_EWSRetirementAlertPresenter
+ __OBJC_$_CLASS_METHODS_EWSRetirementAlertStore
+ __OBJC_$_CLASS_METHODS_EWSServerConfigurationFetcher
+ __OBJC_$_CLASS_METHODS_EWSServerConfigurationStore
+ __OBJC_$_INSTANCE_METHODS_EWSMailboxDenialRecord
+ __OBJC_$_INSTANCE_METHODS_EWSMailboxDenialStore
+ __OBJC_$_INSTANCE_METHODS_EWSMailboxLocationStore
+ __OBJC_$_INSTANCE_METHODS_EWSPreferenceStore
+ __OBJC_$_INSTANCE_METHODS_EWSRetirementAlertAccountSnapshot
+ __OBJC_$_INSTANCE_METHODS_EWSRetirementAlertConfiguration
+ __OBJC_$_INSTANCE_METHODS_EWSRetirementAlertCoordinator
+ __OBJC_$_INSTANCE_METHODS_EWSRetirementAlertKindConfiguration
+ __OBJC_$_INSTANCE_METHODS_EWSRetirementAlertStore
+ __OBJC_$_INSTANCE_METHODS_EWSServerConfigurationFetcher
+ __OBJC_$_INSTANCE_METHODS_EWSServerConfigurationStore
+ __OBJC_$_INSTANCE_VARIABLES_EWSMailboxDenialRecord
+ __OBJC_$_INSTANCE_VARIABLES_EWSMailboxDenialStore
+ __OBJC_$_INSTANCE_VARIABLES_EWSMailboxLocationStore
+ __OBJC_$_INSTANCE_VARIABLES_EWSPreferenceStore
+ __OBJC_$_INSTANCE_VARIABLES_EWSRetirementAlertAccountSnapshot
+ __OBJC_$_INSTANCE_VARIABLES_EWSRetirementAlertConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_EWSRetirementAlertCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_EWSRetirementAlertKindConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_EWSRetirementAlertStore
+ __OBJC_$_INSTANCE_VARIABLES_EWSServerConfigurationFetcher
+ __OBJC_$_INSTANCE_VARIABLES_EWSServerConfigurationStore
+ __OBJC_$_PROP_LIST_EWSMailboxDenialRecord
+ __OBJC_$_PROP_LIST_EWSPreferenceStore
+ __OBJC_$_PROP_LIST_EWSRetirementAlertAccountSnapshot
+ __OBJC_$_PROP_LIST_EWSRetirementAlertConfiguration
+ __OBJC_$_PROP_LIST_EWSRetirementAlertCoordinator
+ __OBJC_$_PROP_LIST_EWSRetirementAlertKindConfiguration
+ __OBJC_$_PROP_LIST_EWSRetirementAlertStore
+ __OBJC_$_PROP_LIST_EWSServerConfigurationFetcher
+ __OBJC_CLASS_RO_$_EWSMailboxDenialPolicy
+ __OBJC_CLASS_RO_$_EWSMailboxDenialRecord
+ __OBJC_CLASS_RO_$_EWSMailboxDenialStore
+ __OBJC_CLASS_RO_$_EWSMailboxLocationPolicy
+ __OBJC_CLASS_RO_$_EWSMailboxLocationProbe
+ __OBJC_CLASS_RO_$_EWSMailboxLocationStore
+ __OBJC_CLASS_RO_$_EWSManagementRestrictionPolicy
+ __OBJC_CLASS_RO_$_EWSManagementRestrictionReader
+ __OBJC_CLASS_RO_$_EWSOAuthTenantPolicy
+ __OBJC_CLASS_RO_$_EWSPreferenceStore
+ __OBJC_CLASS_RO_$_EWSRetirementAlertAccountSnapshot
+ __OBJC_CLASS_RO_$_EWSRetirementAlertConfiguration
+ __OBJC_CLASS_RO_$_EWSRetirementAlertCoordinator
+ __OBJC_CLASS_RO_$_EWSRetirementAlertKindConfiguration
+ __OBJC_CLASS_RO_$_EWSRetirementAlertPolicy
+ __OBJC_CLASS_RO_$_EWSRetirementAlertPresenter
+ __OBJC_CLASS_RO_$_EWSRetirementAlertStore
+ __OBJC_CLASS_RO_$_EWSServerConfigurationFetcher
+ __OBJC_CLASS_RO_$_EWSServerConfigurationStore
+ __OBJC_METACLASS_RO_$_EWSMailboxDenialPolicy
+ __OBJC_METACLASS_RO_$_EWSMailboxDenialRecord
+ __OBJC_METACLASS_RO_$_EWSMailboxDenialStore
+ __OBJC_METACLASS_RO_$_EWSMailboxLocationPolicy
+ __OBJC_METACLASS_RO_$_EWSMailboxLocationProbe
+ __OBJC_METACLASS_RO_$_EWSMailboxLocationStore
+ __OBJC_METACLASS_RO_$_EWSManagementRestrictionPolicy
+ __OBJC_METACLASS_RO_$_EWSManagementRestrictionReader
+ __OBJC_METACLASS_RO_$_EWSOAuthTenantPolicy
+ __OBJC_METACLASS_RO_$_EWSPreferenceStore
+ __OBJC_METACLASS_RO_$_EWSRetirementAlertAccountSnapshot
+ __OBJC_METACLASS_RO_$_EWSRetirementAlertConfiguration
+ __OBJC_METACLASS_RO_$_EWSRetirementAlertCoordinator
+ __OBJC_METACLASS_RO_$_EWSRetirementAlertKindConfiguration
+ __OBJC_METACLASS_RO_$_EWSRetirementAlertPolicy
+ __OBJC_METACLASS_RO_$_EWSRetirementAlertPresenter
+ __OBJC_METACLASS_RO_$_EWSRetirementAlertStore
+ __OBJC_METACLASS_RO_$_EWSServerConfigurationFetcher
+ __OBJC_METACLASS_RO_$_EWSServerConfigurationStore
+ ___108-[EWSRetirementAlertCoordinator _presentAlertOfKind:affectedAccounts:accounts:configuration:recordsHistory:]_block_invoke
+ ___36+[EWSRetirementAlertCoordinator log]_block_invoke
+ ___37+[EWSManagementRestrictionReader log]_block_invoke
+ ___38+[EWSRetirementAlertStore sharedStore]_block_invoke
+ ___42+[EWSServerConfigurationStore sharedStore]_block_invoke
+ ___50+[EWSRetirementAlertCoordinator sharedCoordinator]_block_invoke
+ ___50+[EWSRetirementAlertCoordinator sharedCoordinator]_block_invoke_2
+ ___50+[EWSRetirementAlertCoordinator sharedCoordinator]_block_invoke_3
+ ___57+[EWSRetirementAlertConfiguration _disabledConfiguration]_block_invoke
+ ___68-[EWSServerConfigurationFetcher refreshIfStaleWithValidityInterval:]_block_invoke
+ ___74-[EWSExchangeServiceBinding _sendMailboxReportForAccount:optionKey:value:]_block_invoke
+ ___87+[EWSMailboxLocationProbe sendServerLocationRequestForEmailAddress:session:completion:]_block_invoke
+ ___92-[EWSRetirementAlertCoordinator _runCycleWithAccounts:excludedIdentifiers:token:completion:]_block_invoke
+ ___96+[EWSRetirementAlertPresenter presentAlertOfKind:accountNames:learnMoreURL:posted:acknowledged:]_block_invoke
+ ___EWSMailboxReportStateInitialize_block_invoke
+ ___EWSServerConfigurationKnownKeys_block_invoke
+ ___NSArray0__struct
+ ___block_descriptor_32_e31_v24?0"ACAccount"8"NSError"16l
+ ___block_descriptor_32_e49_v48?0q8"NSArray"16"NSURL"24?<v?B>32?<v?>40l
+ ___block_descriptor_32_e5_q8?0l
+ ___block_descriptor_40_e8_32s_e23_v32?0q8q16"NSError"24l
+ ___block_descriptor_48_e8_32bs_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24l
+ ___block_descriptor_48_e8_32s40w_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24l
+ ___block_descriptor_49_e8_32s_e8_v12?0B8l
+ ___block_descriptor_56_e8_32s40s48s_e23_v32?0q8q16"NSError"24l
+ ___block_descriptor_65_e8_32s40s48s_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0l
+ ___block_descriptor_80_e8_32s40s48s56bs64bs_e5_v8?0l
+ ___copy_helper_block_e8_32b
+ ___copy_helper_block_e8_32s40s48s
+ ___copy_helper_block_e8_32s40s48s56b
+ ___copy_helper_block_e8_32s40s48s56b64b
+ ___copy_helper_block_e8_32s40w
+ ___destroy_helper_block_e8_32s40s48s
+ ___destroy_helper_block_e8_32s40s48s56s
+ ___destroy_helper_block_e8_32s40s48s56s64s
+ ___destroy_helper_block_e8_32s40w
+ ___kCFBooleanFalse
+ _disabledConfiguration.disabledConfiguration
+ _disabledConfiguration.onceToken
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_notify
+ _kACDShouldNotUseParentAccount
+ _kACDiscoverPropertiesShouldSaveKey
+ _kCFPreferencesAnyHost
+ _kCFPreferencesCurrentUser
+ _kCFUserNotificationAlertHeaderKey
+ _kCFUserNotificationAlertMessageKey
+ _kCFUserNotificationAlternateButtonTitleKey
+ _kCFUserNotificationDefaultButtonTitleKey
+ _kEWSMailboxAccessRestoredOptionKey
+ _kEWSMailboxDenialPreferencesDomain
+ _kEWSMailboxDenialReportOptionKey
+ _kEWSMailboxDenialReportingEnabledKey
+ _kEWSMailboxDenialTokenBlockedByPolicy
+ _kEWSMailboxDenialTokenTurnedOff
+ _kEWSMailboxLocationPreferencesDomain
+ _kEWSMailboxLocationTokenExchangeOnline
+ _kEWSMailboxLocationTokenNotExchangeOnline
+ _kEWSManagementAllowAlertsItemName
+ _kEWSManagementConfigurationID
+ _kEWSManagementTokenAllowed
+ _kEWSManagementTokenSuppressed
+ _kEWSServerConfigurationMaximumPayloadSize
+ _kEWSServerConfigurationPreferencesDomain
+ _kEWSServerConfigurationRetryInterval
+ _kEWSServerConfigurationURLString
+ _kEWSServerConfigurationValidityInterval
+ _kGraphTestTenantDefaultsKey
+ _objc_begin_catch
+ _objc_copyWeak
+ _objc_end_catch
+ _objc_exception_rethrow
+ _objc_initWeak
+ _objc_msgSend$URLPathAllowedCharacterSet
+ _objc_msgSend$_URLForKey:fallback:
+ _objc_msgSend$_accountEligibleForMailboxReporting
+ _objc_msgSend$_accountIdentifierForKey:
+ _objc_msgSend$_accountsByIdentifierForAccounts:
+ _objc_msgSend$_adoptSharedServerConfiguration
+ _objc_msgSend$_anyAlertEnabledForConfiguration:
+ _objc_msgSend$_attemptKeyForAccountIdentifier:
+ _objc_msgSend$_beginCycle
+ _objc_msgSend$_boolForKey:fallback:
+ _objc_msgSend$_captureFault:
+ _objc_msgSend$_configurationStringForKey:
+ _objc_msgSend$_configurationValueForKey:
+ _objc_msgSend$_consumeData:response:error:
+ _objc_msgSend$_countForAccountIdentifier:
+ _objc_msgSend$_coveredAccountsForKey:
+ _objc_msgSend$_coveredAccountsKeyForAlertKind:
+ _objc_msgSend$_denialReasonForAccountIdentifier:configuration:simulatedReason:
+ _objc_msgSend$_disabledConfiguration
+ _objc_msgSend$_displayNameForAccount:
+ _objc_msgSend$_endCycleWithToken:completion:
+ _objc_msgSend$_evaluateAlertForAccounts:overriddenLocation:excludedIdentifiers:
+ _objc_msgSend$_finishCycleWithAccounts:excludedIdentifiers:overriddenLocation:token:completion:
+ _objc_msgSend$_integerForKey:fallback:
+ _objc_msgSend$_intervalForKey:fallback:
+ _objc_msgSend$_intervalForKey:fallback:serverMinimum:
+ _objc_msgSend$_intervalFromValue:fallback:
+ _objc_msgSend$_isCurrentCycleToken:
+ _objc_msgSend$_isUsableInterval:
+ _objc_msgSend$_keyForAccountIdentifier:suffix:
+ _objc_msgSend$_keyList
+ _objc_msgSend$_keySuffixes
+ _objc_msgSend$_lastDenialDateForAccountIdentifier:
+ _objc_msgSend$_lastShownKeyForAlertKind:
+ _objc_msgSend$_learnMoreURLForConfiguration:
+ _objc_msgSend$_locationKeyForAccountIdentifier:
+ _objc_msgSend$_mailboxDenialReportingAllowedForAccount:
+ _objc_msgSend$_numberFromValue:
+ _objc_msgSend$_payload
+ _objc_msgSend$_postAlertWithParameters:learnMoreURL:posted:acknowledged:transaction:
+ _objc_msgSend$_presentAlertOfKind:affectedAccounts:accounts:configuration:recordsHistory:
+ _objc_msgSend$_reactiveAlertEnabledForConfiguration:
+ _objc_msgSend$_reasonForAccountIdentifier:
+ _objc_msgSend$_recordForAccountIdentifier:
+ _objc_msgSend$_repairedDateForKey:
+ _objc_msgSend$_reportMailboxAccessRestoredWithTask:bindingTask:
+ _objc_msgSend$_reportMailboxDenialWithTask:bindingTask:
+ _objc_msgSend$_responseInvalidError
+ _objc_msgSend$_runCycleWithAccounts:excludedIdentifiers:token:completion:
+ _objc_msgSend$_sendMailboxReportForAccount:optionKey:value:
+ _objc_msgSend$_setValue:forKey:
+ _objc_msgSend$_shouldClassifyAccountWithIdentifier:configuration:
+ _objc_msgSend$_shouldReportAccessRestoredForAccountIdentifier:
+ _objc_msgSend$_shouldReportDenialForAccountIdentifier:
+ _objc_msgSend$_shownGenerationKeyForAlertKind:
+ _objc_msgSend$_staleKeysForAccountIdentifiers:
+ _objc_msgSend$_stringFromValue:
+ _objc_msgSend$_synchronize
+ _objc_msgSend$_treatsAccountAsManaged:identifier:simulatedManaged:
+ _objc_msgSend$_valueForKey:
+ _objc_msgSend$accountListDescriptionForNames:
+ _objc_msgSend$alertStore
+ _objc_msgSend$alertsSuppressedForAccountIdentifier:managed:
+ _objc_msgSend$alertsSuppressedForManagedAccount:permission:
+ _objc_msgSend$allKeys
+ _objc_msgSend$array
+ _objc_msgSend$arrayByAddingObject:
+ _objc_msgSend$boundsProbeLifetime
+ _objc_msgSend$classificationRetryInterval
+ _objc_msgSend$clearDenialForAccountIdentifier:
+ _objc_msgSend$componentsWithString:
+ _objc_msgSend$configurationForAlertKind:
+ _objc_msgSend$configurationFromData:response:error:
+ _objc_msgSend$configurationURL
+ _objc_msgSend$configurationValueForKey:
+ _objc_msgSend$considerAlertsForAccounts:excludingAccountIdentifiers:completion:
+ _objc_msgSend$coveredAccountsForAlertKind:
+ _objc_msgSend$currentConfiguration
+ _objc_msgSend$dataTaskWithURL:completionHandler:
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$denialCountThreshold
+ _objc_msgSend$denialQualifiesWithCount:countThreshold:
+ _objc_msgSend$denialReasonForStatusCode:isAccessDeniedFault:faultMessage:
+ _objc_msgSend$denialReasonForToken:
+ _objc_msgSend$denialRecordForAccountIdentifier:
+ _objc_msgSend$denialReportingEnabled
+ _objc_msgSend$denialSpacingInterval
+ _objc_msgSend$denialStore
+ _objc_msgSend$discoverPropertiesForAccount:options:completion:
+ _objc_msgSend$dueAlertKindForAffectedAccounts:coveredAccounts:intervalSinceLastShown:shownGeneration:alertKind:configuration:
+ _objc_msgSend$durableLocationForProbedLocation:statusCode:
+ _objc_msgSend$effectivePermission
+ _objc_msgSend$faultIsAccessDenied
+ _objc_msgSend$faultMessage
+ _objc_msgSend$faultReceived
+ _objc_msgSend$fetchInFlight
+ _objc_msgSend$generation
+ _objc_msgSend$getConfigurationSyncFor:error:
+ _objc_msgSend$graphTestTenantEnabled
+ _objc_msgSend$initWithEmailAddress:binding:boundsProbeLifetime:
+ _objc_msgSend$initWithEnabled:classificationRetryInterval:denialCountThreshold:denialSpacingInterval:proactiveConfiguration:reactiveConfiguration:
+ _objc_msgSend$initWithEnabled:repeatInterval:generation:learnMoreURL:
+ _objc_msgSend$initWithLocationStore:alertStore:denialStore:managementPermissionProvider:presentationHandler:
+ _objc_msgSend$initWithPreferencesDomain:
+ _objc_msgSend$initWithReason:count:lastDenialDate:
+ _objc_msgSend$initWithStore:
+ _objc_msgSend$intersectSet:
+ _objc_msgSend$intervalSinceDate:
+ _objc_msgSend$invalidateCachedValues
+ _objc_msgSend$isEnabled
+ _objc_msgSend$isEqualToSet:
+ _objc_msgSend$isInAccountStore
+ _objc_msgSend$isManaged
+ _objc_msgSend$isSubsetOfSet:
+ _objc_msgSend$lastAttemptDate
+ _objc_msgSend$lastAttemptDateForAccountIdentifier:
+ _objc_msgSend$lastDenialDate
+ _objc_msgSend$lastFetchDate
+ _objc_msgSend$lastShownDateForAlertKind:
+ _objc_msgSend$learnMoreURL
+ _objc_msgSend$localizedStringByJoiningStrings:
+ _objc_msgSend$locationForAccountIdentifier:
+ _objc_msgSend$locationForToken:
+ _objc_msgSend$locationStore
+ _objc_msgSend$mailboxLocationForProbeData:error:
+ _objc_msgSend$managementPermission
+ _objc_msgSend$managementPermissionProvider
+ _objc_msgSend$minusSet:
+ _objc_msgSend$needsRefreshWithValidityInterval:
+ _objc_msgSend$optionsPayloadForDenialReason:
+ _objc_msgSend$overriddenMailboxLocation
+ _objc_msgSend$overriddenManagementPermission
+ _objc_msgSend$pathComponents
+ _objc_msgSend$pathWithComponents:
+ _objc_msgSend$permissionForAllowAlertsValue:
+ _objc_msgSend$permissionForConfiguration:
+ _objc_msgSend$permissionForToken:
+ _objc_msgSend$presentAlertOfKind:accountNames:learnMoreURL:posted:acknowledged:
+ _objc_msgSend$presentationHandler
+ _objc_msgSend$proactiveConfiguration
+ _objc_msgSend$probeURLForEmailAddress:
+ _objc_msgSend$pruneAccountsNotIn:
+ _objc_msgSend$pruneCoveredAccountsForAlertKind:toPresentAccounts:
+ _objc_msgSend$rangeOfString:options:
+ _objc_msgSend$reactiveConfiguration
+ _objc_msgSend$reason
+ _objc_msgSend$recordAlertAcknowledged:coveringAccounts:generation:
+ _objc_msgSend$recordAlertPosted:date:
+ _objc_msgSend$recordDenialWithReason:date:spacingInterval:forAccountIdentifier:
+ _objc_msgSend$recordFetchFailureAtDate:
+ _objc_msgSend$recordLocation:attemptDate:forAccountIdentifier:
+ _objc_msgSend$refreshIfStaleWithValidityInterval:
+ _objc_msgSend$removeCoveredAccount:forAlertKind:
+ _objc_msgSend$repeatInterval
+ _objc_msgSend$reportsMailboxDenials
+ _objc_msgSend$responseForError:flags:
+ _objc_msgSend$scannerWithString:
+ _objc_msgSend$sendServerLocationRequestForEmailAddress:session:completion:
+ _objc_msgSend$serverConfigurationFetcher
+ _objc_msgSend$serverConfigurationStore
+ _objc_msgSend$sessionWithConfiguration:
+ _objc_msgSend$set
+ _objc_msgSend$setAllowsConstrainedNetworkAccess:
+ _objc_msgSend$setAllowsExpensiveNetworkAccess:
+ _objc_msgSend$setBoundsProbeLifetime:
+ _objc_msgSend$setFaultIsAccessDenied:
+ _objc_msgSend$setFaultMessage:
+ _objc_msgSend$setFaultReceived:
+ _objc_msgSend$setFetchInFlight:
+ _objc_msgSend$setFetchTransaction:
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$setServerConfigurationFetcher:
+ _objc_msgSend$setServerConfigurationStore:
+ _objc_msgSend$setTimeoutIntervalForRequest:
+ _objc_msgSend$setTimeoutIntervalForResource:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$setWithObject:
+ _objc_msgSend$sharedStore
+ _objc_msgSend$shouldClassifyMailboxLocation:intervalSinceLastAttempt:retryInterval:
+ _objc_msgSend$shouldRecordClassificationAttemptForStatusCode:
+ _objc_msgSend$shouldRecordDenialGivenIntervalSinceLastDenial:spacingInterval:
+ _objc_msgSend$shownGenerationForAlertKind:
+ _objc_msgSend$simulatedDenialReason
+ _objc_msgSend$simulatedManagedAccountIdentifiers
+ _objc_msgSend$sortUsingSelector:
+ _objc_msgSend$sortedArrayUsingSelector:
+ _objc_msgSend$statusCodeIsAccessDeniedRefusal:isAccessDeniedFault:
+ _objc_msgSend$statusCodeIsMailboxSuccess:faultReceived:
+ _objc_msgSend$store
+ _objc_msgSend$storeConfiguration:fetchDate:
+ _objc_msgSend$subarrayWithRange:
+ _objc_msgSend$tenantInURIString:
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$transportForTests
+ _objc_msgSend$unionSet:
+ _objc_msgSend$uriString:withTenant:
+ _objc_terminate
+ _os_transaction_create
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _sDenialReportDates
+ _sMailboxReportStateLock
+ _sPostInFlight
+ _sRecoveryReportedAccounts
+ sharedCoordinator.onceToken
+ sharedCoordinator.sharedCoordinator
+ sharedStore.onceToken
+ sharedStore.sharedStore
- -[EWSAutodiscoverV2Operation dealloc]
- -[EWSAutodiscoverV2Operation initWithEmailAddress:binding:]
- GCC_except_table29
- GCC_except_table30
- GCC_except_table38
- GCC_except_table39
- GCC_except_table40
- GCC_except_table41
- GCC_except_table44
- __OBJC_CLASS_PROTOCOLS_$_EWSAutodiscoverV2Operation
- _objc_msgSend$initWithEmailAddress:binding:
CStrings:
+ "\"'"
+ "%@ (%@)"
+ "%lu others"
+ "%{public}@ mailbox refused with access denied but no known shutoff wording, status %ld, fault %{private}@."
+ ", "
+ ".DenialCount"
+ ".DenialReason"
+ ".LastAttempt"
+ ".LastDenial"
+ ".Location"
+ "/%@/v2.0/.well-known/openid-configuration"
+ "1 other"
+ "Account %{public}@ reached its mailbox again; discarded refusals %{public}s, alert history %{public}s."
+ "Account %{public}@ was refused; report %{public}s."
+ "Administrator restriction read for %{public}@: %{public}@."
+ "Administrator restriction unreadable for %{public}@: %{public}@."
+ "Administrator restriction unreadable: DeviceConfiguration is not available in this process."
+ "B"
+ "Calendars.ReadWrite.Shared"
+ "ClassificationRetryInterval"
+ "Configuration"
+ "Contacts.ReadWrite"
+ "DenialCountThreshold"
+ "DenialSpacingInterval"
+ "EWS is blocked by policy for this user or tenant"
+ "EWS is disabled for this user or tenant"
+ "EWSMailboxAccessRestored"
+ "EWSMailboxDenialReport"
+ "EWSMailboxDenialReportingEnabled"
+ "EWSMailboxDenialStore.m"
+ "EWSMailboxLocationProbe.m"
+ "EWSManagementRestriction"
+ "EWSPreferenceStore.m"
+ "EWSRetirementAlert"
+ "EWSRetirementAlertConfiguration.m"
+ "EWSRetirementAlertCoordinator.m"
+ "EWSServerConfigurationFetcher.m"
+ "GraphTestTenant"
+ "Invalid parameter not satisfying: %@"
+ "LastAttempt"
+ "LastFetch"
+ "Learn More"
+ "MailboxSettings.ReadWrite"
+ "Microsoft is ending support for the protocol these accounts use: %@. Update macOS to keep them syncing."
+ "NO"
+ "OverrideMailboxLocation"
+ "OverrideURLForTesting"
+ "PinnedForTesting"
+ "ProactiveAlertCoveredAccounts"
+ "ProactiveAlertGeneration"
+ "ProactiveAlertLastShown"
+ "ProactiveAlertShownGeneration"
+ "ProactiveEnabled"
+ "ProactiveLearnMoreURL"
+ "ProactiveRepeatInterval"
+ "ReactiveAlertCoveredAccounts"
+ "ReactiveAlertGeneration"
+ "ReactiveAlertLastShown"
+ "ReactiveAlertShownGeneration"
+ "ReactiveEnabled"
+ "ReactiveLearnMoreURL"
+ "ReactiveRepeatInterval"
+ "SimulateAccessDenied"
+ "SimulateManagedAccounts"
+ "SimulateManagementRestriction"
+ "The server is refusing to sync these accounts: %@. This can happen when support for the protocol they use ends, or when an administrator turns it off. Contact the administrator of your account."
+ "Your Exchange account has stopped syncing"
+ "Your Exchange account will stop syncing"
+ "allowEWSRetirementAlerts"
+ "allowed"
+ "blockedByPolicy"
+ "com.apple.ExchangeAccounts"
+ "com.apple.exchangewebservices.ewsdenial"
+ "com.apple.exchangewebservices.mailboxlocation"
+ "com.apple.exchangewebservices.retirementalert"
+ "com.apple.exchangewebservices.retirementalert.alert"
+ "com.apple.exchangewebservices.retirementalert.cycle"
+ "com.apple.exchangewebservices.serverconfig"
+ "com.apple.exchangewebservices.serverconfig.fetch"
+ "common"
+ "completion != nil"
+ "dropped, too soon after the last one"
+ "exchangeOnline"
+ "https://configuration.apple.com/configurations/internetservices/exchangesync/ews-retirement-alert.plist"
+ "no"
+ "notExchangeOnline"
+ "q8@?0"
+ "recorded"
+ "session != nil"
+ "suppressed"
+ "turnedOff"
+ "v12@?0B8"
+ "v24@?0@\"ACAccount\"8@\"NSError\"16"
+ "v32@?0q8q16@\"NSError\"24"
+ "v48@?0q8@\"NSArray\"16@\"NSURL\"24@?<v@?B>32@?<v@?>40"
+ "yes"
- "/common/v2.0/.well-known/openid-configuration"
```
