## ExchangeAuthenticationPlugin

> `/System/Library/Accounts/Authentication/ExchangeAuthenticationPlugin.bundle/Contents/MacOS/ExchangeAuthenticationPlugin`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_intobj`
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
+846.200.41.1.1
+  __TEXT.__text: 0xa6c4
+  __TEXT.__auth_stubs: 0x2c0
+  __TEXT.__objc_stubs: 0x16e0
+  __TEXT.__objc_methlist: 0x4fc
+  __TEXT.__const: 0xd8
+  __TEXT.__cstring: 0x510
+  __TEXT.__oslogstring: 0x12f1
+  __TEXT.__objc_classname: 0xfa
+  __TEXT.__objc_methname: 0x18b5
+  __TEXT.__objc_methtype: 0x6df
+  __TEXT.__gcc_except_tab: 0x214
+  __TEXT.__unwind_info: 0x388
+  __DATA_CONST.__const: 0x558
+  __DATA_CONST.__cfstring: 0x320
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__auth_got: 0x138
-  __DATA_CONST.__got: 0x298
-  __DATA.__objc_const: 0xd10
-  __DATA.__objc_selrefs: 0x620
-  __DATA.__objc_ivar: 0x30
-  __DATA.__objc_data: 0x140
+  __DATA_CONST.__auth_got: 0x170
+  __DATA_CONST.__got: 0x2f0
+  __DATA.__objc_const: 0xde8
+  __DATA.__objc_selrefs: 0x6d8
+  __DATA.__objc_ivar: 0x38
+  __DATA.__objc_data: 0x190
   __DATA.__data: 0x180
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/ExchangeWebServices.framework/Versions/A/ExchangeWebServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 176
-  Symbols:   138
-  CStrings:  380
+  Functions: 217
+  Symbols:   161
+  CStrings:  422
 
Symbols:
+ OBJC_IVAR_$_ExchangeAuthenticationPlugin._discoveryInFlightAccountIDs
+ OBJC_IVAR_$_ExchangeAuthenticationPlugin._discoveryInFlightLock
+ _ACAccountPropertyManagingOwnerIdentifier
+ _OBJC_CLASS_$_EWSMailboxDenialPolicy
+ _OBJC_CLASS_$_EWSManagementRestrictionPolicy
+ _OBJC_CLASS_$_EWSRetirementAlertAccountSnapshot
+ _OBJC_CLASS_$_EWSRetirementAlertCoordinator
+ _OBJC_CLASS_$_ExchangeAutodiscoverRoutingPolicy
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_METACLASS_$_ExchangeAutodiscoverRoutingPolicy
+ __NSConcreteGlobalBlock
+ _dispatch_after
+ _dispatch_once
+ _kAutodiscoverProtocolGraph
+ _kEWSMailboxAccessRestoredOptionKey
+ _kEWSMailboxDenialReportOptionKey
+ _kEWSMailboxDenialReportingEnabledKey
+ _kExchangeAutodiscoverADFSIssuer
+ _objc_autoreleaseReturnValue
+ _objc_sync_enter
+ _objc_sync_exit
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
CStrings:
+ "@\"NSMutableSet\""
+ "ADFS"
+ "Autodiscover did not yield an Exchange Online authorize URL for a provisioned Graph account; not reclassifying (hasURI=%d isEXO=%d issuer=%{public}@)"
+ "B60@0:8@16B24@28@36@44@52"
+ "B8@?0"
+ "ExchangeAutodiscoverRoutingPolicy"
+ "Graph-protocol autodiscover did not yield a Graph endpoint (hasHost=%d error=%{public}@); falling back to EWS endpoint"
+ "Neither Graph nor EWS host available for Exchange Online account; cannot persist an endpoint"
+ "No EWS host available for Exchange Online account; cannot persist an endpoint"
+ "OAuth account already has the necessary information"
+ "Saved account (%{public}@); calling completion with account %{public}@"
+ "Saving account (%{public}@) returned error %{public}@"
+ "Sign-in URL discovery failed for OAuth account: %{public}@"
+ "V2 classification did not confirm modern-auth Exchange Online (hasURI=%d isEXO=%d issuer=%{public}@ error=%{public}@); falling back to legacy V1 autodiscover"
+ "V2 classifier probe exceeded %d s deadline; falling back to legacy V1 autodiscover"
+ "V2-classified Exchange Online"
+ "_discoverAndPersistOAuthV2URLsForAccount:accountStore:completion:"
+ "_discoveryInFlightAccountIDs"
+ "_discoveryInFlightLock"
+ "_reconcileDenialReportingFlagForAccount:accountStore:"
+ "_recordMailboxAccessRestoredForAccount:accountStore:completion:"
+ "_recordMailboxDenialWithReason:forAccount:accountStore:completion:"
+ "_saveAccount:store:context:completion:"
+ "accountDescription"
+ "accountIsManagedWithManagingOwnerIdentifier:"
+ "accountsWithAccountTypeIdentifier:"
+ "array"
+ "autodiscover v2 properties"
+ "clearDenialForAccountIdentifier:"
+ "considerAlertsForAccounts:excludingAccountIdentifier:"
+ "denialReasonForOptionsPayload:"
+ "denialReportingEnabledForAccountIdentifier:managed:"
+ "initWithIdentifier:emailAddress:displayName:inAccountStore:managed:"
+ "numberWithBool:"
+ "recordDenialWithReason:forAccountIdentifier:managed:"
+ "removeObject:"
+ "set"
+ "setBoundsProbeLifetime:"
+ "setReportsMailboxDenials:"
+ "sharedCoordinator"
+ "shouldPublishReportingEnabled:currentValue:accountInStore:retrying:"
+ "shouldRouteToModernAuthForAutodiscoverV2Error:isExchangeOnline:authorizationURI:authV2URI:host:issuer:"
+ "v24@?0q8@\"NSError\"16"
+ "v48@0:8q16@24@32@?40"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "Calling auto discover v2 properties completion with account %{public}@"
- "OAuth account already has necessary necessary information"
- "Saving account returned error %{public}@"
```
