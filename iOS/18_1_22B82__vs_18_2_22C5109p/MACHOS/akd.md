## akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

-493.100.9.2.0
-  __TEXT.__text: 0x18776c
+493.225.2.0.0
+  __TEXT.__text: 0x18be94
   __TEXT.__auth_stubs: 0x1d20
-  __TEXT.__objc_stubs: 0x17840
-  __TEXT.__objc_methlist: 0x8af4
-  __TEXT.__const: 0x2be0
-  __TEXT.__cstring: 0xaf53
-  __TEXT.__objc_classname: 0x182f
-  __TEXT.__objc_methname: 0x21184
-  __TEXT.__objc_methtype: 0x59cb
-  __TEXT.__gcc_except_tab: 0x22a4
-  __TEXT.__oslogstring: 0x1f7c8
+  __TEXT.__objc_stubs: 0x17f60
+  __TEXT.__objc_methlist: 0x8f44
+  __TEXT.__const: 0x2bf0
+  __TEXT.__cstring: 0xb123
+  __TEXT.__objc_classname: 0x18a3
+  __TEXT.__objc_methname: 0x21cac
+  __TEXT.__objc_methtype: 0x5a7d
+  __TEXT.__gcc_except_tab: 0x22bc
+  __TEXT.__oslogstring: 0x1ffe8
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__swift5_typeref: 0x1580
   __TEXT.__swift5_fieldmd: 0xb6c
-  __TEXT.__constg_swiftt: 0x1188
+  __TEXT.__constg_swiftt: 0x1190
   __TEXT.__swift5_reflstr: 0xae0
   __TEXT.__swift5_assocty: 0x150
   __TEXT.__swift5_capture: 0xff8

   __TEXT.__swift5_proto: 0x118
   __TEXT.__swift5_types: 0xec
   __TEXT.__swift5_protos: 0x34
-  __TEXT.__unwind_info: 0x5190
+  __TEXT.__unwind_info: 0x56a0
   __TEXT.__eh_frame: 0x76f0
   __DATA_CONST.__auth_got: 0xea0
-  __DATA_CONST.__got: 0x1628
-  __DATA_CONST.__auth_ptr: 0x4f0
-  __DATA_CONST.__const: 0xc440
-  __DATA_CONST.__cfstring: 0x6d80
-  __DATA_CONST.__objc_classlist: 0x6d8
+  __DATA_CONST.__got: 0x1640
+  __DATA_CONST.__auth_ptr: 0x510
+  __DATA_CONST.__const: 0xc4d0
+  __DATA_CONST.__cfstring: 0x6f20
+  __DATA_CONST.__objc_classlist: 0x708
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x2b0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xf8
-  __DATA_CONST.__objc_superrefs: 0x3b8
+  __DATA_CONST.__objc_superrefs: 0x3e8
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_intobj: 0x2d0
   __DATA_CONST.__objc_arraydata: 0x2c0
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__linkguard: 0x3e
   __DATA_CONST.__objc_dictobj: 0x118
-  __DATA.__objc_const: 0x24db0
-  __DATA.__objc_selrefs: 0x6eb8
-  __DATA.__objc_ivar: 0x9c4
-  __DATA.__objc_data: 0x5380
-  __DATA.__data: 0x3c28
-  __DATA.__bss: 0x2190
+  __DATA.__objc_const: 0x25480
+  __DATA.__objc_selrefs: 0x70e0
+  __DATA.__objc_ivar: 0xa04
+  __DATA.__objc_data: 0x5568
+  __DATA.__data: 0x3c18
+  __DATA.__bss: 0x21a0
   __DATA.__common: 0x111
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 6771
-  Symbols:   1316
-  CStrings:  9377
+  Functions: 6898
+  Symbols:   1319
+  CStrings:  9530
 
Symbols:
+ _AKPersonalInformationErrorDomain
+ _AKUserCanAttestAgeKey
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_CLASS_$_NSDateFormatter
- _OBJC_CLASS_$_AKTokenManager
CStrings:
+ "\x01E)/\x0f\x1f\x0f\x03"
+ "%!@(MISSING)-%!@(MISSING)-%!@(MISSING)"
+ "%!@(MISSING).%!@(MISSING)"
+ "@\"ACAccountCredential\""
+ "@\"AKTokenCache\""
+ "@\"AKTokenKeychain\""
+ "@\"AKUserInfoController\""
+ "@48@0:8@16@24@32^@40"
+ "@52@0:8@16@24@32B40^@44"
+ "AKBirthDayKeychain"
+ "AKServerResponseAccountUpdater"
+ "AKTokenCache"
+ "AKTokenKeychain"
+ "AKTokenManager"
+ "AKTokenManager attempting to fetch token."
+ "AKTokenManager attempting to update token."
+ "AKTokenManager fetching tokens for tokenIdentifier:%!@(MISSING) altDSID:%!@(MISSING)"
+ "AKTokenManager keychainDescriptorService:%!@(MISSING)"
+ "AKTokenManager missing required inputs (altDSID). Skipping."
+ "AKTokenManager missing required inputs (tokenIdentifier). Skipping."
+ "AKTokenManager: Synchronizing Credential"
+ "AKTokenManager: Token creation time not enabled. Defaulting to choose token from account credential"
+ "AKTokenManager: attempting to delete token from keychain"
+ "AKTokenManager: didn't find token in keychain."
+ "AKTokenManager: error deleting token: %!@(MISSING)"
+ "AKTokenManager: error fetching from keychain: %!@(MISSING)"
+ "AKTokenManager: found token from account credential."
+ "AKTokenManager: found token in cache."
+ "AKTokenManager: found token in keychain."
+ "AKTokenManager: missing required inputs."
+ "AKTokenManager: shouldUpdateCache:%!d(MISSING), shouldUpdateKeychain:%!d(MISSING), shouldUpdateAccountCredential:%!d(MISSING)"
+ "AKTokenManager: token from Accounts has newer creation date. Picking this one."
+ "AKTokenManager: token from keychain has newer creation date. Picking this one."
+ "AKTokenManager: we received an Account, deleting from there as well."
+ "AKTokenRequestContext"
+ "ALTER TABLE authorized_primary_applications ADD COLUMN adam_id TEXT;"
+ "B56@0:8@16@24@32@40^@48"
+ "B64@0:8@16@24@32@40@48^@56"
+ "Begin reporting PAC event %!@(MISSING) with error: %!@(MISSING)"
+ "Birthday keychain delete failed with error: %!@(MISSING)"
+ "Birthday keychain fetch failed - unable to unarchive token data with error: %!@(MISSING)"
+ "Birthday keychain update failed - unable to generate archived data from token with error: %!@(MISSING)"
+ "Birthday keychain update failed with error: %!@(MISSING)."
+ "Client is not allow listed to access birthday!"
+ "Failed to fetch accounts, unable to update birthday: %!@(MISSING)."
+ "Finish reporting PAC event %!@(MISSING)."
+ "INSERT OR REPLACE INTO authorized_primary_applications (client_id, app_name, app_developer_name, adam_id) VALUES (?, ?, ?, ?)"
+ "MM-dd-yyyy"
+ "Missing required inputs. Skipping."
+ "SELECT client_id, app_name, app_developer_name, adam_id FROM authorized_primary_applications"
+ "SELECT client_id, app_name, app_developer_name, adam_id FROM authorized_primary_applications WHERE client_id = ?"
+ "T@\"AAFKeychainManager\",&,N,V_keychainManager"
+ "T@\"ACAccount\",&,N,V_account"
+ "T@\"ACAccountCredential\",&,N,V_credential"
+ "T@\"AKToken\",&,N,V_token"
+ "T@\"AKTokenCache\",&,N,V_tokenCache"
+ "T@\"AKTokenKeychain\",&,N,V_tokenKeychain"
+ "T@\"AKTokenManager\",&,N,V_tokenManager"
+ "T@\"AKUserInfoController\",&,N,V_userInfoController"
+ "T@\"NSMutableDictionary\",&,N,V_tokenCache"
+ "T@\"NSNumber\",R,N,V_canAttestAge"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_tokenManagerQueue"
+ "T@\"NSString\",R,N,V_tokenIdentifier"
+ "Token is nil. Let's delete the token."
+ "Token keychain delete failed with error: %!@(MISSING)"
+ "Token keychain failed to clear all tokens with error: %!@(MISSING)"
+ "Token keychain fetch failed - unable to unarchive token data with error: %!@(MISSING)"
+ "Token keychain update failed - unable to generate archived data from token with error: %!@(MISSING)"
+ "Token keychain update failed with error: %!@(MISSING)."
+ "Unable to delete birthday from keychain due to error: %!@(MISSING)."
+ "Upgrading database to schema version: 8"
+ "_birthDayKeychainDescriptorForAltDSID:"
+ "_canAttestAge"
+ "_clearBirthDayForAltDSID:"
+ "_credential"
+ "_deleteTokenWithIdentifer:altDSID:account:credential:error:"
+ "_fetchIDSCertificateWithContext:completionHandler:"
+ "_postUserInfoChangedNotificationWithPayload:"
+ "_reportPacTelemetryForEvent:context:error:"
+ "_saveAccount:userInfoDictionary:error:"
+ "_tokenCache"
+ "_tokenIdentifier"
+ "_tokenKeychain"
+ "_tokenKeychainDescriptorForContext:"
+ "_tokenKeychainDescriptorWithIdentifier:altDSID:"
+ "_tokenManagerQueue"
+ "_tokenWithName:forAccount:error:"
+ "_updateAccountInUseForAccount:withContext:"
+ "_updateAccountInfoPropertiesForAccount:withServerResponse:userInfoDictionary:"
+ "_updateAppleAccountSecurityPropertiesForAccount:withServerResponse:userInfoDictionary:"
+ "_updateBeneficiaryPropertiesForAccount:withServerResponse:"
+ "_updateChildPasscodePropertiesForAccount:withServerResponse:"
+ "_updateCustodianPropertiesForAccount:withServerResponse:"
+ "_updateMaidPropertiesForAccount:withServerResponse:"
+ "_updatePasskeyPropertiesForAccount:withServerResponse:"
+ "_updateRemainingPropertiesForAccount:withServerResponse:"
+ "_updateSecurityLevelForAccount:withServerResponse:userInfoDictionary:"
+ "_updateTelemetryDeviceSessionIDForAccount:withContext:"
+ "_updateTokensForAccount:withServerResponse:context:"
+ "_updateUserInfoPropertiesForAccount:withServerResponse:"
+ "_upgradeToSchemaVersion8"
+ "_userInfoController"
+ "ak_livenessErrorWithCode:"
+ "allAuthKitAccountsWithError:"
+ "authKitAccountTypeWithError:"
+ "canAttestAge"
+ "canAttestAgeForAccount:"
+ "clearAllTokensForAltDSID:"
+ "clearAllTokensForAltDSID:error:"
+ "com.apple.WatchFacesWallpaperSupport.SnoopyPoster"
+ "com.apple.appleaccountd"
+ "com.apple.authkit.AKTokenManagerQueue"
+ "com.apple.authkit.birthDay"
+ "com.apple.authkit.pac.signature"
+ "com.apple.authkit.pac.subscriptionInfo"
+ "com.apple.authkit.pac.subscriptionSource"
+ "com.apple.authkit.tdl.cache.allowedMIDHashMismatch"
+ "com.apple.authkit.tdl.cache.deletedMIDHashMismatch"
+ "com.apple.authkit.tokenManager"
+ "components:fromDate:"
+ "currentCalendar"
+ "dateFromString:"
+ "day"
+ "deleteBirthdayForAltDSID:error:"
+ "deleteWithContext:"
+ "deleteWithContext:error:"
+ "fetchBirthDayForAltDSID:error:"
+ "fetchDeviceListFromCache(with:accountManager:)"
+ "fetchWithContext:"
+ "fetchWithContext:error:"
+ "initWithIdentifier:altDSID:"
+ "isPermittedToAccessBirthday"
+ "isTokenCreationTimeEnabled"
+ "keychainManager"
+ "month"
+ "setAdamID:"
+ "setCanAttestAge:forAccount:"
+ "setDateFormat:"
+ "setKeychainManager:"
+ "setTokenCache:"
+ "setTokenKeychain:"
+ "setTokenManager:"
+ "setTokenManagerQueue:"
+ "setUserAgeRange:forAccount:"
+ "setUserInfoController:"
+ "synchronizedCredentialForAccount:"
+ "tokenCache"
+ "tokenCreationDateWithIdentifier:forAccount:error:"
+ "tokenIdentifier"
+ "tokenKeychain"
+ "tokenManager"
+ "tokenManagerQueue"
+ "tokenWithIdentifier:altDSID:forAccount:shouldSync:error:"
+ "updateAuthKitAccount:withServerResponse:context:error:"
+ "updateBirthdayForAltDSID:userInformation:"
+ "updateBirthdayForAltDSID:userInformation:error:"
+ "updateWithContext:"
+ "updateWithContext:error:"
+ "userAgeRange"
+ "userAgeRangeForAccount:"
+ "userInfoController"
- "\x01E)/\x0e\x1f\x0f\x03"
- "INSERT OR REPLACE INTO authorized_primary_applications (client_id, app_name, app_developer_name) VALUES (?, ?, ?)"
- "SELECT client_id, app_name, app_developer_name FROM authorized_primary_applications"
- "SELECT client_id, app_name, app_developer_name FROM authorized_primary_applications WHERE client_id = ?"
- "_fetchIDSCertificateWithCompletionHandler:"
- "authKitAccountType"
- "authKitAccountWithAppleID:"
- "fetchDeviceListFromCache(with:cdpFactory:serviceController:accountManager:)"

```
