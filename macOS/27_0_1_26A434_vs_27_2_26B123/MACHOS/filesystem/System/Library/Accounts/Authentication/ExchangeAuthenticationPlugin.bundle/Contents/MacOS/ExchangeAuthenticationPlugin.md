## ExchangeAuthenticationPlugin

> `/System/Library/Accounts/Authentication/ExchangeAuthenticationPlugin.bundle/Contents/MacOS/ExchangeAuthenticationPlugin`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_protolist`
- `__DATA.__data`

```diff

-844.0.0.0.0
-  __TEXT.__text: 0x80f8
-  __TEXT.__auth_stubs: 0x250
-  __TEXT.__objc_stubs: 0x1400
-  __TEXT.__objc_methlist: 0x48c
-  __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x4b5
-  __TEXT.__oslogstring: 0x1006
-  __TEXT.__objc_classname: 0xd8
-  __TEXT.__objc_methname: 0x14c2
-  __TEXT.__objc_methtype: 0x673
-  __TEXT.__gcc_except_tab: 0xec
-  __TEXT.__unwind_info: 0x2c0
-  __DATA_CONST.__const: 0x390
-  __DATA_CONST.__cfstring: 0x2c0
-  __DATA_CONST.__objc_classlist: 0x20
+846.200.71.0.0
+  __TEXT.__text: 0xdbc4
+  __TEXT.__auth_stubs: 0x340
+  __TEXT.__objc_stubs: 0x1f40
+  __TEXT.__objc_methlist: 0x71c
+  __TEXT.__const: 0xf0
+  __TEXT.__cstring: 0x596
+  __TEXT.__oslogstring: 0x1633
+  __TEXT.__objc_classname: 0x15c
+  __TEXT.__objc_methname: 0x2518
+  __TEXT.__objc_methtype: 0x7ba
+  __TEXT.__gcc_except_tab: 0x224
+  __TEXT.__unwind_info: 0x490
+  __DATA_CONST.__const: 0x698
+  __DATA_CONST.__cfstring: 0x3a0
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__auth_got: 0x138
-  __DATA_CONST.__got: 0x298
-  __DATA.__objc_const: 0xd10
-  __DATA.__objc_selrefs: 0x620
-  __DATA.__objc_ivar: 0x30
-  __DATA.__objc_data: 0x140
+  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__objc_arraydata: 0x8
+  __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__auth_got: 0x1b0
+  __DATA_CONST.__got: 0x368
+  __DATA.__objc_const: 0x1170
+  __DATA.__objc_selrefs: 0x8f0
+  __DATA.__objc_ivar: 0x68
+  __DATA.__objc_data: 0x280
   __DATA.__data: 0x180
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/PrivateFrameworks/ExchangeWebServices.framework/Versions/A/ExchangeWebServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 176
-  Symbols:   138
-  CStrings:  380
+  Functions: 288
+  Symbols:   195
+  CStrings:  535
 
Symbols:
+ OBJC_IVAR_$_ExchangeAuthenticationPlugin._discoveryInFlightAccountIDs
+ OBJC_IVAR_$_ExchangeAuthenticationPlugin._discoveryInFlightLock
+ OBJC_IVAR_$_ExchangeAuthenticationPlugin._graphCapabilityFullyStampedAccountIDs
+ OBJC_IVAR_$_ExchangeAuthenticationPlugin._graphCapabilityFullyStampedLock
+ OBJC_IVAR_$_ExchangeAuthenticationPlugin._graphCapabilityInFlightTracker
+ OBJC_IVAR_$_ExchangeAuthenticationPlugin._graphCapabilityRecentlyCheckedEntries
+ OBJC_IVAR_$_ExchangeAuthenticationPlugin._graphCapabilityRecentlyCheckedLock
+ OBJC_IVAR_$_ExchangeAuthenticationPlugin._graphCapabilitySession
+ _ACAccountPropertyManagingOwnerIdentifier
+ _EWSMailboxRefusalLearnMoreURLKey
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_EWSGraphCapabilityInFlightTracker
+ _OBJC_CLASS_$_EWSGraphCapabilityPolicy
+ _OBJC_CLASS_$_EWSGraphCapabilityRecentlyCheckedEntry
+ _OBJC_CLASS_$_EWSMailboxDenialPolicy
+ _OBJC_CLASS_$_EWSMailboxLocationPolicy
+ _OBJC_CLASS_$_EWSMailboxLocationProbe
+ _OBJC_CLASS_$_EWSManagementRestrictionPolicy
+ _OBJC_CLASS_$_EWSRetirementAlertAccountSnapshot
+ _OBJC_CLASS_$_EWSRetirementAlertCoordinator
+ _OBJC_CLASS_$_EWSRetirementAlertPolicy
+ _OBJC_CLASS_$_EWSRetirementAlertPresenter
+ _OBJC_CLASS_$_ExchangeAutodiscoverRoutingPolicy
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_METACLASS_$_EWSGraphCapabilityInFlightTracker
+ _OBJC_METACLASS_$_EWSGraphCapabilityPolicy
+ _OBJC_METACLASS_$_EWSGraphCapabilityRecentlyCheckedEntry
+ _OBJC_METACLASS_$_ExchangeAutodiscoverRoutingPolicy
+ __NSConcreteGlobalBlock
+ ___NSArray0__struct
+ __os_log_impl
+ _arc4random_uniform
+ _dispatch_after
+ _dispatch_block_cancel
+ _dispatch_block_create
+ _dispatch_once
+ _kAutodiscoverProtocolGraph
+ _kEWSMailboxAccessRestoredOptionKey
+ _kEWSMailboxDenialReportOptionKey
+ _kEWSMailboxDenialReportingEnabledKey
+ _kEWSMailboxEndpointGoneReportingEnabledKey
+ _kExchangeAutodiscoverADFSIssuer
+ _kExchangeGraphCapabilityKey
+ _kExchangeGraphMigrationContactsKey
+ _kExchangeGraphMigrationExchangeSyncKey
+ _kExchangeGraphMigrationMailKey
+ _objc_alloc_init
+ _objc_autorelease
+ _objc_autoreleaseReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_sync_enter
+ _objc_sync_exit
+ _os_transaction_create
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
CStrings:
+ ""
+ "@\"EWSGraphCapabilityInFlightTracker\""
+ "@\"NSDate\""
+ "@\"NSMutableSet\""
+ "@\"NSURLSession\""
+ "@40@0:8@16d24d32"
+ "ADFS"
+ "Account %{public}@ has lost access to its mailbox, so not asking for a password. A new one could not help."
+ "Autodiscover did not yield an Exchange Online authorize URL for a provisioned Graph account; not reclassifying (hasURI=%d isEXO=%d issuer=%{public}@)"
+ "B32@0:8@16@24"
+ "B60@0:8@16B24@28@36@44@52"
+ "B8@?0"
+ "Could not mark %{public}@ authenticated after its mailbox access was restored: %{public}@"
+ "Could not mark %{public}@ unauthenticated after its mailbox access was lost: %{public}@"
+ "EWSGraphCapabilityInFlightTracker"
+ "EWSGraphCapabilityPolicy"
+ "EWSGraphCapabilityRecentlyCheckedEntry"
+ "ExchangeAutodiscoverRoutingPolicy"
+ "Failed to save Graph migration properties for account %{public}@: %{private}@"
+ "Graph capability check deferred for account %{public}@: no email or username to probe with"
+ "Graph capability check running for account %{public}@ (usingGraph=%{public}d)"
+ "Graph capability verdict for account %{public}@: location=%{public}ld capable=%{public}d fullyResolved=%{public}d locationValueChanged=%{public}d missingMigrationKeys=%{public}lu probeFailedDueToConnectivity=%{public}d"
+ "Graph migration capability"
+ "Graph-protocol autodiscover did not yield a Graph endpoint (hasHost=%d error=%{public}@); falling back to EWS endpoint"
+ "GraphCapability"
+ "Neither Graph nor EWS host available for Exchange Online account; cannot persist an endpoint"
+ "No EWS host available for Exchange Online account; cannot persist an endpoint"
+ "OAuth account already has the necessary information"
+ "Saved Graph migration properties for account %{public}@ (fullyResolved=%{public}d)"
+ "Saved account (%{public}@); calling completion with account %{public}@"
+ "Saving account (%{public}@) returned error %{public}@"
+ "Sign-in URL discovery failed for OAuth account: %{public}@"
+ "T@\"NSDate\",R,N,V_checkedAt"
+ "TB,V_mailboxAccessWasRestored"
+ "Td,R,N,V_connectivityFailureBase"
+ "Td,R,N,V_retryInterval"
+ "UUID"
+ "V2 classification did not confirm modern-auth Exchange Online (hasURI=%d isEXO=%d issuer=%{public}@ error=%{public}@); falling back to legacy V1 autodiscover"
+ "V2 classifier probe exceeded %d s deadline; falling back to legacy V1 autodiscover"
+ "V2-classified Exchange Online"
+ "_accountEligibleForMailboxRefusalTracking:"
+ "_accountForMailboxAccessStateChange:"
+ "_actOnGraphMigrationCapabilityLocation:probeFailedDueToConnectivity:accountIdentifier:accountStore:invocationToken:releaseClaim:"
+ "_allGraphMigrationKeys"
+ "_checkGraphMigrationCapabilityForAccountIdentifier:emailAddress:usingGraph:hasEverBeenEWSAccount:accountStore:"
+ "_checkedAt"
+ "_clearMailboxRefusalFromTask:"
+ "_completeWithMailboxRefusedError:"
+ "_connectivityFailureBase"
+ "_currentExchangeAccountIdentifiersInStore:"
+ "_discoverAndPersistOAuthV2URLsForAccount:accountStore:completion:"
+ "_discoveryInFlightAccountIDs"
+ "_discoveryInFlightLock"
+ "_freshExchangeAccountWithIdentifier:accountStore:"
+ "_graphCapabilityFullyStampedAccountIDs"
+ "_graphCapabilityFullyStampedLock"
+ "_graphCapabilityInFlightTracker"
+ "_graphCapabilityRecentlyCheckedEntries"
+ "_graphCapabilityRecentlyCheckedLock"
+ "_graphCapabilitySession"
+ "_hasAllGraphMigrationKeysOnAccount:"
+ "_hasEverBeenEWSAccount:"
+ "_isGraphCapabilityFullyStampedForAccountIdentifier:"
+ "_isGraphCapabilityRecentlyCheckedForAccountIdentifier:"
+ "_lock"
+ "_mailboxAccessWasRestored"
+ "_markAccountAuthenticatedAfterMailboxAccessRestored:store:"
+ "_markAccountUnauthenticatedAfterMailboxAccessLost:store:"
+ "_presentGraphMigrationKeysForAccount:allKeys:"
+ "_previousGraphCapabilityConnectivityFailureBaseForAccountIdentifier:"
+ "_pruneGraphCapabilityFullyStampedAccountIDsNotIn:"
+ "_pruneGraphCapabilityRecentlyCheckedEntriesNotIn:"
+ "_reconcileDenialReportingFlagForAccount:accountStore:"
+ "_recordGraphCapabilityOutcomeForAccountIdentifier:permanentlyResolved:retryInterval:connectivityFailureBase:"
+ "_recordMailboxAccessRestoredForAccount:accountStore:completion:"
+ "_recordMailboxDenialWithReason:forAccount:accountStore:completion:"
+ "_recordMailboxRefusalFromTask:"
+ "_rememberGraphCapabilityFullyStampedForAccountIdentifier:"
+ "_rememberGraphCapabilityRecentlyCheckedForAccountIdentifier:retryInterval:connectivityFailureBase:"
+ "_retryInterval"
+ "_saveAccount:store:context:completion:"
+ "_shouldDispatchGraphCapabilityCheckForAccount:accountIdentifier:"
+ "_shouldSkipInvalidCredentialPromptForAccountIdentifier:account:"
+ "_tokensByAccountID"
+ "accountDescription"
+ "accountIsManagedWithManagingOwnerIdentifier:"
+ "accountsWithAccountTypeIdentifier:"
+ "array"
+ "authenticationType"
+ "autodiscover v2 properties"
+ "checkedAt"
+ "claimAccountIdentifier:"
+ "clearDenialForAccountIdentifier:"
+ "com.apple.exchangewebservices.graphcapabilitycheck"
+ "connectivityFailureBase"
+ "considerAlertsForAccounts:excludingAccountIdentifier:"
+ "d"
+ "d16@0:8"
+ "d24@0:8@16"
+ "d40@0:8d16d24d32"
+ "denialReasonForOptionsPayload:"
+ "dictionary"
+ "durableLocationForProbedLocation:statusCode:"
+ "hasEverBeenEWSAccountWithExternalURLPresent:internalURLPresent:"
+ "initWithCheckedAt:retryInterval:connectivityFailureBase:"
+ "initWithIdentifier:emailAddress:displayName:inAccountStore:managed:graphCapable:"
+ "intersectSet:"
+ "intervalSinceDate:"
+ "invalidateCachedValues"
+ "isAccountIdentifierClaimed:"
+ "isAuthenticated"
+ "isGraphCapableForDurableMailboxLocation:"
+ "isToken:stillOwnerOfAccountIdentifier:"
+ "lastAttemptDateForAccountIdentifier:consumer:"
+ "locationForAccountIdentifier:"
+ "locationStore"
+ "mailboxAccessLostForAccountIdentifier:"
+ "mailboxAccessWasRestored"
+ "mailboxDenialReason"
+ "mailboxDenialReasonIsActionableForAddAccount:"
+ "mailboxReportingFlags"
+ "mailboxRequestSucceeded"
+ "messageForKind:accountNames:"
+ "missingKeysFromKeys:presentKeys:"
+ "nextConnectivityFailureBaseInterval:capInterval:baseInterval:"
+ "numberWithBool:"
+ "oauthTokenRefreshRequestForTokenRequestURI:clientID:hostURL:isOnPrem:usingGraph:refreshToken:"
+ "parent"
+ "parentAccount"
+ "pruneAccountsNotIn:"
+ "reactiveLearnMoreURLIfActionable"
+ "recordDenialWithReason:forAccountIdentifier:"
+ "recordLocation:attemptDate:forAccountIdentifier:consumer:"
+ "releaseAccountIdentifier:ifStillOwnedByToken:"
+ "removeObject:"
+ "removeObjectForKey:"
+ "removeObjectsForKeys:"
+ "retryInterval"
+ "retryIsDueAfterInterval:retryInterval:"
+ "sendServerLocationRequestForEmailAddress:session:completion:"
+ "set"
+ "setAuthenticated:"
+ "setBoundsProbeLifetime:"
+ "setByAddingObject:"
+ "setMailboxAccessWasRestored:"
+ "setReportsMailboxDenials:"
+ "sharedCoordinator"
+ "shouldClearRecordedDenialsWhenPublishingReporting:reportingEnabled:"
+ "shouldPublishReportingEnabled:currentValue:valueWhenAbsent:accountInStore:retrying:"
+ "shouldRecordClassificationAttemptForStatusCode:"
+ "shouldRouteToModernAuthForAutodiscoverV2Error:isExchangeOnline:authorizationURI:authV2URI:host:issuer:"
+ "v24@?0B8@\"ExchangeOAuthTokenRefreshResponse\"12B20"
+ "v24@?0q8@\"NSError\"16"
+ "v32@?0q8q16@\"NSError\"24"
+ "v40@0:8@16d24d32"
+ "v44@0:8@16B24d28d36"
+ "v48@0:8@16@24B32B36@40"
+ "v48@0:8q16@24@32@?40"
+ "v60@0:8q16B24@28@36@44@?52"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "Calling auto discover v2 properties completion with account %{public}@"
- "OAuth account already has necessary necessary information"
- "Saving account returned error %{public}@"
- "oauthTokenRefreshRequestForTokenRequestURI:clientID:scope:refreshToken:"
- "v20@?0B8@\"ExchangeOAuthTokenRefreshResponse\"12"
```
