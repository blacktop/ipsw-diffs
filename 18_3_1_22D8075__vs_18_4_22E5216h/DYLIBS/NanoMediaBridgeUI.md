## NanoMediaBridgeUI

> `/System/Library/PrivateFrameworks/NanoMediaBridgeUI.framework/NanoMediaBridgeUI`

```diff

-2022.300.3.0.0
-  __TEXT.__text: 0xc564
+2022.500.7.0.0
+  __TEXT.__text: 0xb384
   __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_methlist: 0xbbc
+  __TEXT.__objc_methlist: 0xc04
   __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x1a2e
-  __TEXT.__gcc_except_tab: 0xc0
-  __TEXT.__oslogstring: 0x4aa
+  __TEXT.__cstring: 0x19d6
+  __TEXT.__oslogstring: 0x338
   __TEXT.__ustring: 0x1ea0
-  __TEXT.__unwind_info: 0x330
+  __TEXT.__gcc_except_tab: 0x74
+  __TEXT.__unwind_info: 0x2c8
   __TEXT.__objc_classname: 0x27d
-  __TEXT.__objc_methname: 0x2f0b
-  __TEXT.__objc_methtype: 0x662
-  __TEXT.__objc_stubs: 0x29a0
-  __DATA_CONST.__got: 0x308
-  __DATA_CONST.__const: 0x670
+  __TEXT.__objc_methname: 0x2ae8
+  __TEXT.__objc_methtype: 0x61a
+  __TEXT.__objc_stubs: 0x25e0
+  __DATA_CONST.__got: 0x2a8
+  __DATA_CONST.__const: 0x5d8
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcc0
+  __DATA_CONST.__objc_selrefs: 0xc38
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x2c8
-  __AUTH_CONST.__const: 0xc0
+  __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x26c0
-  __AUTH_CONST.__objc_const: 0x1c28
+  __AUTH_CONST.__objc_const: 0x1960
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x640
-  __DATA.__objc_ivar: 0x11c
+  __DATA.__objc_ivar: 0x110
   __DATA.__data: 0xc0
   __DATA.__bss: 0xb0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/NanoSystemSettings.framework/NanoSystemSettings
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
+  - /System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 270
-  Symbols:   508
-  CStrings:  965
+  Functions: 243
+  Symbols:   475
+  CStrings:  906
 
Symbols:
+ _ICActiveUserIdentityDidChangeNotification
+ _ICUserIdentityStoreDidChangeNotification
+ _OBJC_CLASS_$_ICMonitoredAccountStore
+ _dispatch_assert_queue$V2
+ _objc_retain_x25
- _ACAccountTypeIdentifierIDMS
- _ACAccountTypeIdentifieriTunesStore
- _ACDAccountStoreDidChangeNotification
- _ACErrorDomain
- _OBJC_CLASS_$_ACAccountStore
- _OBJC_CLASS_$_AKAccountManager
- _OBJC_CLASS_$_AKDevice
- _OBJC_CLASS_$_NSSManager
- _kAASaveOptionCompanionDeviceClientInfoKey
- _kAASaveOptionCompanionDeviceUDIDKey
- _kNSSAccountAltDSIDKey
- _kNSSAccountDSIDKey
- _kNSSAccountIsAuthenticatedKey
- _kNSSAccountUsernameKey
- _kNSSAccountsKey
- _objc_retain_x24
- _objc_retain_x26
CStrings:
+ "[Account Util] Failed to fetch active store account with error: %@."
+ "[Account Util] Received active user identity did change notification."
+ "[Account Util] Received user identity store did change notification."
+ "_account"
+ "_handleActiveUserIdentityDidChangeNotification:"
+ "_handleUserIdentityStoreDidChangeNotification:"
+ "_updateActiveAccount"
+ "account"
+ "activeStoreAccountWithError:"
+ "sharedAccountStore"
- "@\"ACAccountStore\""
- "@\"NSSManager\""
- "B32@0:8@16@24"
- "B64@0:8@16@24@32@40@48@56"
- "DSIDForAccount:"
- "T@\"ACAccount\",&,N,V_idmsAccount"
- "T@\"ACAccount\",&,N,V_itunesAccount"
- "T@\"ACAccountStore\",&,N,V_accountStore"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_workQueue"
- "T@\"NSSManager\",&,N,V_nssManager"
- "[Accounts Sync] Error fetching gizmo accounts info <%@>"
- "[Accounts Sync] Gizmo already has matching iTunes account"
- "[Accounts Sync] IDMS account already present on gizmo. Attempting sign in."
- "[Accounts Sync] IDMS account has no credentials - %@"
- "[Accounts Sync] Pushing IDMS account FAILED with error %@"
- "[Accounts Sync] Pushing IDMS account SUCCEEDED. Attempting sign in."
- "[Accounts Sync] Sign in FAILED with error %@"
- "[Accounts Sync] Sign in SUCCEEDED"
- "[Accounts Sync] There is no IDMS account available on companion"
- "[Accounts Sync] There is no iTunes account available on companion"
- "_accountStore"
- "_attemptSignIn"
- "_doesAccount:matchAccount:"
- "_doesAccount:matchAccountDict:"
- "_doesAccountWithAltDSID:DSID:username:matchAccountWithAltDSID:DSID:username:"
- "_handleAccountStoreDidChangeNotification:"
- "_idmsAccount"
- "_idmsAccountForCurrentAccount"
- "_itunesAccount"
- "_itunesAccountNoAuth"
- "_nssManager"
- "_sendITunesAccountToGizmoIfNecessary"
- "_signGizmoIntoITunesAccount"
- "_signInOptions"
- "_workQueue"
- "accountStore"
- "accountTypeWithAccountTypeIdentifier:"
- "accountsWithAccountType:"
- "altDSIDForAccount:"
- "credentialWithError:"
- "currentDevice"
- "dictionary"
- "getAccountsInfoForAccountType:completionHandler:"
- "ic_activeStoreAccount"
- "ic_activeStoreAccountWithCompletion:"
- "ic_sharedAccountStore"
- "idmsAccount"
- "initWithQueue:"
- "isEqualToNumber:"
- "itunesAccount"
- "nssManager"
- "removeObserver:"
- "saveAccount:toPairedDeviceWithOptions:completion:"
- "sendITunesAccountToGizmoIfNecessary"
- "serverFriendlyDescription"
- "setAccountStore:"
- "setAuthenticated:"
- "setCredential:"
- "setIdmsAccount:"
- "setItunesAccount:"
- "setNssManager:"
- "setObject:forKeyedSubscript:"
- "setWorkQueue:"
- "uniqueDeviceIdentifier"
- "username"
- "v20@?0B8@\"NSError\"12"
- "v24@?0@\"ACAccount\"8@\"NSError\"16"
- "v24@?0@\"NSDictionary\"8@\"NSError\"16"
- "workQueue"

```
