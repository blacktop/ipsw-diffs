## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-493.100.9.2.0
-  __TEXT.__text: 0xce844
+493.225.2.0.0
+  __TEXT.__text: 0xcc4b0
   __TEXT.__auth_stubs: 0xd80
-  __TEXT.__objc_methlist: 0xb380
+  __TEXT.__objc_methlist: 0xb2c8
   __TEXT.__const: 0x2121
-  __TEXT.__cstring: 0xd7c0
-  __TEXT.__oslogstring: 0x10590
-  __TEXT.__gcc_except_tab: 0x5360
+  __TEXT.__cstring: 0xd8bf
+  __TEXT.__oslogstring: 0xff20
+  __TEXT.__gcc_except_tab: 0x53c4
   __TEXT.__ustring: 0x1b8
   __TEXT.__dlopen_cstrs: 0x10e
-  __TEXT.__unwind_info: 0x3ac0
-  __TEXT.__objc_classname: 0x1943
-  __TEXT.__objc_methname: 0x1f507
-  __TEXT.__objc_methtype: 0x4283
-  __TEXT.__objc_stubs: 0xdd40
-  __DATA_CONST.__got: 0x990
-  __DATA_CONST.__const: 0x52b8
-  __DATA_CONST.__objc_classlist: 0x578
+  __TEXT.__unwind_info: 0x3aa0
+  __TEXT.__objc_classname: 0x1934
+  __TEXT.__objc_methname: 0x1f14c
+  __TEXT.__objc_methtype: 0x41d5
+  __TEXT.__objc_stubs: 0xd9e0
+  __DATA_CONST.__got: 0x968
+  __DATA_CONST.__const: 0x5298
+  __DATA_CONST.__objc_classlist: 0x570
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x1d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6550
+  __DATA_CONST.__objc_selrefs: 0x64a8
   __DATA_CONST.__objc_protorefs: 0xd8
-  __DATA_CONST.__objc_superrefs: 0x360
+  __DATA_CONST.__objc_superrefs: 0x358
   __DATA_CONST.__objc_arraydata: 0x148
   __AUTH_CONST.__auth_got: 0x6d0
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0x10b0
-  __AUTH_CONST.__cfstring: 0xe2c0
-  __AUTH_CONST.__objc_const: 0x24420
+  __AUTH_CONST.__cfstring: 0xe380
+  __AUTH_CONST.__objc_const: 0x24300
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH.__objc_data: 0x1ab8
-  __DATA.__objc_ivar: 0xeb0
+  __DATA.__objc_ivar: 0xea4
   __DATA.__data: 0x1660
-  __DATA.__bss: 0x628
-  __DATA_DIRTY.__objc_data: 0x1bf8
-  __DATA_DIRTY.__bss: 0x240
+  __DATA.__bss: 0x630
+  __DATA_DIRTY.__objc_data: 0x1ba8
+  __DATA_DIRTY.__bss: 0x230
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5697
-  Symbols:   7760
-  CStrings:  8951
+  Functions: 5649
+  Symbols:   7710
+  CStrings:  8892
 
Symbols:
+ _AKPersonalInformationErrorDomain
+ _AKUserCanAttestAgeKey
+ _kAKAnalyticsEventCachedAllowedMIDHashMismatch
+ _kAKAnalyticsEventCachedDeletedMIDHashMismatch
+ _kAKAnalyticsEventPACSignature
+ _kAKAnalyticsEventPACSubscriptionInfo
+ _kAKAnalyticsEventPACSubscriptionSource
- _NSOSStatusErrorDomain
- _OBJC_CLASS_$_AAFKeychainItem
- _OBJC_CLASS_$_AAFKeychainItemDescriptor
- _OBJC_CLASS_$_AAFKeychainManager
- _OBJC_CLASS_$_AKTokenManager
- _OBJC_METACLASS_$_AKTokenManager
CStrings:
+ "\x04\x11\x11\x11\x11"
+ "\x0f\x01\x16!\x1f\x0f\x0f\x02"
+ "<%!@(MISSING): %!p(MISSING) {\n\tgivenName: %!@(MISSING),\n\tfamilyName: %!@(MISSING),\n\tforwardingEmail: %!@(MISSING),\n\tprimaryEmailAddress: %!@(MISSING),\n\taccountName: %!@(MISSING),\n\taccountAliases: %!@(MISSING),\n\treachableEmails: %!@(MISSING),\n\tauthorizedApplicationsListVersion: %!@(MISSING),\n\tmasterKeyID: %!@(MISSING),\n\tvettedPrimaryEmail: %!@(MISSING),\n\tphoneAsAppleID: %!@(MISSING),\n\tisUnderage: %!@(MISSING),\n\tparentalAgeConsent: %!@(MISSING),\n\tisSiwaForChildEnabled: %!@(MISSING),\n\tuserAgeRange: %!l(MISSING)u,\n\tisSenior: %!@(MISSING),\n\tageOfMajority: %!@(MISSING),\n\tisLegacyStudent: %!@(MISSING),\n\tappleIDCountryCode: %!@(MISSING),\n\thasUsedAuthorization: %!@(MISSING), \n\tprivateAttestationEnabled: %!@(MISSING), \n\tappleIDSecurityLevel: %!l(MISSING)u,\n\tauthMode: %!l(MISSING)u,\n\tisMdmInfoRequired: %!@(MISSING),\n\trepairState: %!l(MISSING)u,\n\tselectedEmail: %!@(MISSING),\n\tcanBeCustodian: %!@(MISSING),\n\tcanHaveCustodian: %!@(MISSING),\n\tcustodianEnabled: %!@(MISSING),\n\tcanBeBeneficiary: %!@(MISSING),\n\tcanHaveBeneficiary: %!@(MISSING),\n\thasMDM: %!@(MISSING),\n\tmanagedOrganizationType: %!@(MISSING),\n\tmanagedOrganizationName: %!@(MISSING),\n\tisNotificationEmailAvailable: %!@(MISSING),\n\tnotificationEmail: %!@(MISSING),\n\tadditionalInfo: %!@(MISSING),\n\ttrustedPhoneNumbers: %!@(MISSING),\n\tsecurityKeys: %!@(MISSING),\n\tloginHandles: %!@(MISSING),\n\tprivateEmailListVersion: %!@(MISSING),\n\tisProximityAuthEligible: %!@(MISSING),\n\twebAccessEnabled: %!@(MISSING),\n\tserverExperimentalFeatures: %!@(MISSING),\n\tcustodianInfos: %!@(MISSING),\n\tbeneficiaryInfo: %!@(MISSING),\n\tpasskeyEligible: %!@(MISSING),\n\tpasskeyPresent: %!@(MISSING),\n\tgroupKitEligibility: %!@(MISSING),\n\tpasscodeAuthEnabled: %!@(MISSING),\n\taskToBuy: %!@(MISSING),\n\thasSOSActiveDevice: %!@(MISSING),\n\tSOSNeeded: %!@(MISSING),\n\tdeviceListVersion: %!@(MISSING),\n\tconfigDataVersion: %!@(MISSING),\n\tbirthYear: %!@(MISSING),\n\tcriticalAccountEditsAllowed: %!@(MISSING),\n\thasModernRecoveryKey: %!@(MISSING),\n\tadpCohort: %!@(MISSING),\n\tthirdPartyRegulatoryOverride: %!@(MISSING),\n\tedpState: %!@(MISSING),\n\tpasswordVersion: %!@(MISSING),\n\tsrpProtocol: %!@(MISSING),\n\tidmsEDPTTokenId: %!@(MISSING),\n\tpiggybackingApprovalEligible: %!@(MISSING),\n}>"
+ "@16@?0@\"AKRemoteDevice\"8"
+ "AKPersonalInformationErrorDomain"
+ "Calling out to remote auth service to fetch birthday"
+ "Exception caught when setting userAgeRange property: %!@(MISSING)"
+ "T@\"NSNumber\",C,N,V_canAttestAge"
+ "_canAttestAge"
+ "_computeHashForDevices:"
+ "ak_livenessErrorWithCode:"
+ "canAttestAge"
+ "canAttestAgeForAccount:"
+ "com.apple.authkit.pac.signature"
+ "com.apple.authkit.pac.subscriptionInfo"
+ "com.apple.authkit.pac.subscriptionSource"
+ "com.apple.authkit.tdl.cache.allowedMIDHashMismatch"
+ "com.apple.authkit.tdl.cache.deletedMIDHashMismatch"
+ "deletedDevicesClientHash"
+ "parentalAgeConsent"
+ "setCanAttestAge:"
+ "setCanAttestAge:forAccount:"
+ "setUserAgeRange:forAccount:"
+ "sortedArrayUsingSelector:"
+ "trustedDevicesClientHash"
+ "userAgeRangeForAccount:"
- "\x05\x11\x11\x11\x11"
- "\x0f\x01\x16!\x1f\x0f\x0f\x01"
- "%!@(MISSING).%!@(MISSING)"
- "%!@(MISSING): Token not found in keychain (%!@(MISSING))"
- "<%!@(MISSING): %!p(MISSING) {\n\tgivenName: %!@(MISSING),\n\tfamilyName: %!@(MISSING),\n\tforwardingEmail: %!@(MISSING),\n\tprimaryEmailAddress: %!@(MISSING),\n\taccountName: %!@(MISSING),\n\taccountAliases: %!@(MISSING),\n\treachableEmails: %!@(MISSING),\n\tauthorizedApplicationsListVersion: %!@(MISSING),\n\tmasterKeyID: %!@(MISSING),\n\tvettedPrimaryEmail: %!@(MISSING),\n\tphoneAsAppleID: %!@(MISSING),\n\tisUnderage: %!@(MISSING),\n\tisSiwaForChildEnabled: %!@(MISSING),\n\tuserAgeRange: %!l(MISSING)u,\n\tisSenior: %!@(MISSING),\n\tageOfMajority: %!@(MISSING),\n\tisLegacyStudent: %!@(MISSING),\n\tappleIDCountryCode: %!@(MISSING),\n\thasUsedAuthorization: %!@(MISSING), \n\tprivateAttestationEnabled: %!@(MISSING), \n\tappleIDSecurityLevel: %!l(MISSING)u,\n\tauthMode: %!l(MISSING)u,\n\tisMdmInfoRequired: %!@(MISSING),\n\trepairState: %!l(MISSING)u,\n\tselectedEmail: %!@(MISSING),\n\tcanBeCustodian: %!@(MISSING),\n\tcanHaveCustodian: %!@(MISSING),\n\tcustodianEnabled: %!@(MISSING),\n\tcanBeBeneficiary: %!@(MISSING),\n\tcanHaveBeneficiary: %!@(MISSING),\n\thasMDM: %!@(MISSING),\n\tmanagedOrganizationType: %!@(MISSING),\n\tmanagedOrganizationName: %!@(MISSING),\n\tisNotificationEmailAvailable: %!@(MISSING),\n\tnotificationEmail: %!@(MISSING),\n\tadditionalInfo: %!@(MISSING),\n\ttrustedPhoneNumbers: %!@(MISSING),\n\tsecurityKeys: %!@(MISSING),\n\tloginHandles: %!@(MISSING),\n\tprivateEmailListVersion: %!@(MISSING),\n\tisProximityAuthEligible: %!@(MISSING),\n\twebAccessEnabled: %!@(MISSING),\n\tserverExperimentalFeatures: %!@(MISSING),\n\tcustodianInfos: %!@(MISSING),\n\tbeneficiaryInfo: %!@(MISSING),\n\tpasskeyEligible: %!@(MISSING),\n\tpasskeyPresent: %!@(MISSING),\n\tgroupKitEligibility: %!@(MISSING),\n\tpasscodeAuthEnabled: %!@(MISSING),\n\taskToBuy: %!@(MISSING),\n\thasSOSActiveDevice: %!@(MISSING),\n\tSOSNeeded: %!@(MISSING),\n\tdeviceListVersion: %!@(MISSING),\n\tconfigDataVersion: %!@(MISSING),\n\tbirthYear: %!@(MISSING),\n\tcriticalAccountEditsAllowed: %!@(MISSING),\n\thasModernRecoveryKey: %!@(MISSING),\n\tadpCohort: %!@(MISSING),\n\tthirdPartyRegulatoryOverride: %!@(MISSING),\n\tedpState: %!@(MISSING),\n\tpasswordVersion: %!@(MISSING),\n\tsrpProtocol: %!@(MISSING),\n\tidmsEDPTTokenId: %!@(MISSING),\n\tpiggybackingApprovalEligible: %!@(MISSING),\n}>"
- "@\"AAFKeychainManager\""
- "@\"AKTokenManager\""
- "@48@0:8@16@24@32^@40"
- "@52@0:8@16@24@32B40^@44"
- "AKTokenManager"
- "AKTokenManager attempting to fetch token."
- "AKTokenManager attempting to save token to keychain"
- "AKTokenManager attempting to update token."
- "AKTokenManager fetching tokens for tokenIdentifier:%!@(MISSING) altDSID:%!@(MISSING)"
- "AKTokenManager keychainDescriptorService:%!@(MISSING)"
- "AKTokenManager missing required inputs (altDSID). Skipping."
- "AKTokenManager missing required inputs (tokenIdentifier). Skipping."
- "AKTokenManager sync hit an error: %!@(MISSING)."
- "AKTokenManager: Synchronizing Credential"
- "AKTokenManager: Token creation time not enabled. Defaulting to choose token from account credential"
- "AKTokenManager: attempting to delete token from keychain"
- "AKTokenManager: didn't find token in keychain."
- "AKTokenManager: error deleting in keychain: %!@(MISSING)"
- "AKTokenManager: error deleting token: %!@(MISSING)"
- "AKTokenManager: error fetching from keychain: %!@(MISSING)"
- "AKTokenManager: found token from account credential."
- "AKTokenManager: found token in cache."
- "AKTokenManager: found token in keychain."
- "AKTokenManager: missing required inputs."
- "AKTokenManager: no tokens for this altDSID in cache"
- "AKTokenManager: shouldUpdateCache:%!d(MISSING), shouldUpdateKeychain:%!d(MISSING), shouldUpdateAccountCredential:%!d(MISSING)"
- "AKTokenManager: token from Accounts has newer creation date. Picking this one."
- "AKTokenManager: token from cache is %!@(MISSING)"
- "AKTokenManager: token from keychain has newer creation date. Picking this one."
- "AKTokenManager: tokenIdentifier is nil, so we'll clear all tokens for this adsid from cache."
- "AKTokenManager: tokenIdentifier is nil, so we'll clear all tokens for this adsid from keychain."
- "AKTokenManager: update in keychain hit an error: %!@(MISSING)."
- "AKTokenManager: we received an Account, deleting from there as well."
- "B40@0:8@16@24@32"
- "B48@0:8@16@24@32^@40"
- "B56@0:8@16@24@32@40^@48"
- "B64@0:8@16@24@32@40@48^@56"
- "Missing required inputs. Skipping."
- "T@\"AAFKeychainManager\",&,N,V_keychainManager"
- "T@\"NSMutableDictionary\",&,N,V_tokenCache"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_tokenManagerQueue"
- "Token is nil. Let's delete the token."
- "Unable to archive token"
- "_deleteTokenFromCacheWithIdentifer:altDSID:"
- "_deleteTokenFromKeychainWithIdentifer:altDSID:error:"
- "_deleteTokenWithIdentifer:altDSID:account:credential:error:"
- "_fetchTokenFromCacheWithIdentifier:altDSID:"
- "_fetchTokenFromKeychainWithIdentifier:altDSID:error:"
- "_keychainManager"
- "_tokenCache"
- "_tokenKeychainDescriptorForIdentifier:altDSID:"
- "_tokenManager"
- "_tokenManagerQueue"
- "_updateCacheWithToken:identifier:altDSID:"
- "_updateKeychainWithToken:identifier:altDSID:error:"
- "addOrUpdateKeychainItem:error:"
- "com.apple.authkit.AKTokenManagerQueue"
- "com.apple.authkit.tokenManager"
- "deleteKeychainItemsForDescriptor:error:"
- "deleteTokenFromCacheWithIdentifer:altDSID:error:"
- "initWithDescriptor:value:"
- "keychainItemForDescriptor:error:"
- "keychainManager"
- "setAccount:"
- "setInvisible:"
- "setItemAccessible:"
- "setItemClass:"
- "setKeychainManager:"
- "setService:"
- "setSynchronizable:"
- "setTokenCache:"
- "setTokenManagerQueue:"
- "setUseDataProtection:"
- "synchronizeTokensForAllAccounts:"
- "synchronizeTokensForAltDSID:account:error:"
- "synchronizedCredentialForAccount:"
- "tokenCache"
- "tokenManagerQueue"
- "tokenWithIdentifier:altDSID:forAccount:error:"
- "tokenWithIdentifier:altDSID:forAccount:shouldSync:error:"
- "updateToken:identifier:altDSID:account:credential:error:"

```
