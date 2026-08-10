## akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

### Sections with Same Size but Changed Content

- `__TEXT.__dlopen_cstrs`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-555.0.0.0.0
-  __TEXT.__text: 0x31f164
-  __TEXT.__auth_stubs: 0x27d0
-  __TEXT.__objc_stubs: 0x1d6c0
-  __TEXT.__objc_methlist: 0xd02c
-  __TEXT.__const: 0x82d0
-  __TEXT.__objc_methname: 0x292a5
-  __TEXT.__cstring: 0xbe54
-  __TEXT.__objc_classname: 0x3062
-  __TEXT.__objc_methtype: 0x8381
-  __TEXT.__oslogstring: 0x28930
-  __TEXT.__gcc_except_tab: 0x28a8
+559.0.0.0.0
+  __TEXT.__text: 0x326520
+  __TEXT.__auth_stubs: 0x27a0
+  __TEXT.__objc_stubs: 0x1d740
+  __TEXT.__objc_methlist: 0xd074
+  __TEXT.__const: 0x82e0
+  __TEXT.__objc_methname: 0x293d5
+  __TEXT.__cstring: 0xbdc4
+  __TEXT.__objc_classname: 0x3092
+  __TEXT.__objc_methtype: 0x8321
+  __TEXT.__oslogstring: 0x29920
+  __TEXT.__gcc_except_tab: 0x28b4
   __TEXT.__dlopen_cstrs: 0x1cf
-  __TEXT.__constg_swiftt: 0x2e08
-  __TEXT.__swift5_typeref: 0x3cf8
-  __TEXT.__swift5_reflstr: 0x1868
-  __TEXT.__swift5_fieldmd: 0x1d3c
+  __TEXT.__constg_swiftt: 0x2de8
+  __TEXT.__swift5_typeref: 0x3cd8
+  __TEXT.__swift5_reflstr: 0x1898
+  __TEXT.__swift5_fieldmd: 0x1d44
   __TEXT.__swift5_builtin: 0x168
   __TEXT.__swift5_assocty: 0x318
   __TEXT.__swift5_proto: 0x378

   __TEXT.__swift_as_cont: 0xf00
   __TEXT.__swift5_capture: 0x2784
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x8b20
-  __TEXT.__eh_frame: 0x12f10
-  __DATA_CONST.__const: 0x14f20
-  __DATA_CONST.__cfstring: 0x8660
-  __DATA_CONST.__objc_classlist: 0x920
+  __TEXT.__unwind_info: 0x8b90
+  __TEXT.__eh_frame: 0x12f68
+  __DATA_CONST.__const: 0x14fd0
+  __DATA_CONST.__cfstring: 0x85c0
+  __DATA_CONST.__objc_classlist: 0x928
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x470
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x218
+  __DATA_CONST.__objc_protorefs: 0x210
   __DATA_CONST.__objc_superrefs: 0x460
   __DATA_CONST.__objc_intobj: 0x378
   __DATA_CONST.__objc_arraydata: 0x370

   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__linkguard: 0x3e
-  __DATA_CONST.__auth_got: 0x13f8
-  __DATA_CONST.__got: 0x1c20
+  __DATA_CONST.__auth_got: 0x13e0
+  __DATA_CONST.__got: 0x1c18
   __DATA_CONST.__auth_ptr: 0x810
-  __DATA.__objc_const: 0x30d38
-  __DATA.__objc_selrefs: 0x8918
-  __DATA.__objc_ivar: 0xbbc
-  __DATA.__objc_data: 0x7570
-  __DATA.__data: 0x5d20
+  __DATA.__objc_const: 0x310f0
+  __DATA.__objc_selrefs: 0x8940
+  __DATA.__objc_ivar: 0xbb8
+  __DATA.__objc_data: 0x75b0
+  __DATA.__data: 0x5d80
   __DATA.__bss: 0x6390
   __DATA.__common: 0x1b0
   - /System/Library/Frameworks/Accessibility.framework/Accessibility

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10526
-  Symbols:   1706
-  CStrings:  11442
+  Functions: 10546
+  Symbols:   1703
+  CStrings:  11534
 
Symbols:
+ _AKDeviceCategoryListChangedNotification
+ _kSecAttrApplicationTag
+ _kSecAttrSynchronizableAny
- _AKTrustedDeviceIdKey
- _CFRetain
- _OBJC_CLASS_$_AKTrustedDeviceId
- _SecAccessControlCreateWithFlags
- _SecKeyCreateRandomKey
- _kSecAttrAccessibleAlwaysThisDeviceOnlyPrivate
CStrings:
+ " (retry)"
+ "%s: Failed to fetch auth mode with error: %{public}@"
+ "@\"<AKDeviceIdentityProtocol>\""
+ "@\"<SettingsRedirectPromptProtocol>\""
+ "AKDeviceIdentityBridge"
+ "AKDeviceListValidator"
+ "AKSettingsRedirectPromptController"
+ "Activate proximity session completed with response: %@"
+ "BEGIN [%lld]: ClientUIActivateProximitySession  enableTelemetry=YES "
+ "BEGIN [%lld]: ClientUIDismissBasicLogin  enableTelemetry=YES "
+ "BEGIN [%lld]: ClientUIDismissKeepUsing  enableTelemetry=YES "
+ "BEGIN [%lld]: ClientUIDismissNativeRecovery  enableTelemetry=YES "
+ "BEGIN [%lld]: ClientUIDismissProximityPairing  enableTelemetry=YES "
+ "BEGIN [%lld]: ClientUIDismissSecondFactor  enableTelemetry=YES "
+ "BEGIN [%lld]: ClientUIDismissServerProvided  enableTelemetry=YES "
+ "BEGIN [%lld]: ClientUIPresentBasicLogin  enableTelemetry=YES "
+ "BEGIN [%lld]: ClientUIPresentFidoAuth  enableTelemetry=YES "
+ "BEGIN [%lld]: ClientUIPresentKeepUsing  enableTelemetry=YES "
+ "BEGIN [%lld]: ClientUIPresentLocalAuth  enableTelemetry=YES "
+ "BEGIN [%lld]: ClientUIPresentLoginAlert  enableTelemetry=YES "
+ "BEGIN [%lld]: ClientUIPresentNativeRecovery  enableTelemetry=YES "
+ "BEGIN [%lld]: ClientUIPresentProximityBroadcast  enableTelemetry=YES "
+ "BEGIN [%lld]: ClientUIPresentProximityPairing  enableTelemetry=YES "
+ "BEGIN [%lld]: ClientUIPresentProximityPinCode  enableTelemetry=YES "
+ "BEGIN [%lld]: ClientUIPresentSecondFactor  enableTelemetry=YES "
+ "BEGIN [%lld]: ClientUIPresentSecondFactorAlert  enableTelemetry=YES "
+ "BEGIN [%lld]: ClientUIPresentServerProvided  enableTelemetry=YES "
+ "BEGIN [%lld]: ClientUIShowProximityError  enableTelemetry=YES "
+ "Basic server request failed: %{public}@"
+ "Basic server request failed: missing internal access entitlement"
+ "Basic server request rejected: failed to construct auth context"
+ "Basic server request rejected: urlBagKey '%s' is not in the allowed set"
+ "Basic server request succeeded with HTTP status %ld"
+ "Begin activate proximity session."
+ "Begin dismiss basic login UI."
+ "Begin dismiss keep using UI."
+ "Begin dismiss native recovery UI."
+ "Begin dismiss proximity pairing UI."
+ "Begin dismiss second factor UI."
+ "Begin dismiss server UI."
+ "Begin present FIDO auth."
+ "Begin present basic login UI."
+ "Begin present biometric or passcode validation via LocalAuthentication."
+ "Begin present keep using UI."
+ "Begin present login alert."
+ "Begin present native recovery UI."
+ "Begin present proximity broadcast UI."
+ "Begin present proximity pairing UI."
+ "Begin present proximity pin code UI."
+ "Begin present second factor UI."
+ "Begin present second factor alert."
+ "Begin present server UI."
+ "Begin show proximity error."
+ "Calling DeviceIdentity to issue certs%s."
+ "Cannot create OS bound RefKey without an altDSID"
+ "Cannot retrieve OS bound RefKey without an altDSID"
+ "ClientUIActivateProximitySession"
+ "ClientUIDismissBasicLogin"
+ "ClientUIDismissKeepUsing"
+ "ClientUIDismissNativeRecovery"
+ "ClientUIDismissProximityPairing"
+ "ClientUIDismissSecondFactor"
+ "ClientUIDismissServerProvided"
+ "ClientUIPresentBasicLogin"
+ "ClientUIPresentFidoAuth"
+ "ClientUIPresentKeepUsing"
+ "ClientUIPresentLocalAuth"
+ "ClientUIPresentLoginAlert"
+ "ClientUIPresentNativeRecovery"
+ "ClientUIPresentProximityBroadcast"
+ "ClientUIPresentProximityPairing"
+ "ClientUIPresentProximityPinCode"
+ "ClientUIPresentSecondFactor"
+ "ClientUIPresentSecondFactorAlert"
+ "ClientUIPresentServerProvided"
+ "ClientUIShowProximityError"
+ "CryptoTokenKit"
+ "DeletedDeviceListProvider - Skipping deleted device with missing date(s); reason=%ld"
+ "DeviceListProvider - Skipping trusted device with missing lastUpdatedDate"
+ "DeviceListValidator - Ambiguous match: %ld devices share the same stableId"
+ "DeviceListValidator - Local stableId is nil, cannot mark thisDevice"
+ "DeviceListValidator - No device in list of %ld matched localStableId"
+ "Dismiss basic login UI completed with response: %@"
+ "Dismiss keep using UI completed with response: %@"
+ "Dismiss native recovery UI completed with response: %@"
+ "Dismiss proximity pairing UI completed with response: %@"
+ "Dismiss second factor UI completed with response: %@"
+ "Dismiss server UI completed with response: %@"
+ "END [%lld] %fs:ClientUIActivateProximitySession "
+ "END [%lld] %fs:ClientUIDismissBasicLogin "
+ "END [%lld] %fs:ClientUIDismissKeepUsing "
+ "END [%lld] %fs:ClientUIDismissNativeRecovery "
+ "END [%lld] %fs:ClientUIDismissProximityPairing "
+ "END [%lld] %fs:ClientUIDismissSecondFactor "
+ "END [%lld] %fs:ClientUIDismissServerProvided "
+ "END [%lld] %fs:ClientUIPresentBasicLogin "
+ "END [%lld] %fs:ClientUIPresentFidoAuth "
+ "END [%lld] %fs:ClientUIPresentKeepUsing "
+ "END [%lld] %fs:ClientUIPresentLocalAuth "
+ "END [%lld] %fs:ClientUIPresentLoginAlert "
+ "END [%lld] %fs:ClientUIPresentNativeRecovery "
+ "END [%lld] %fs:ClientUIPresentProximityBroadcast "
+ "END [%lld] %fs:ClientUIPresentProximityPairing "
+ "END [%lld] %fs:ClientUIPresentProximityPinCode "
+ "END [%lld] %fs:ClientUIPresentSecondFactor "
+ "END [%lld] %fs:ClientUIPresentSecondFactorAlert "
+ "END [%lld] %fs:ClientUIPresentServerProvided "
+ "END [%lld] %fs:ClientUIShowProximityError "
+ "Error %d deleting existing OS bound RefKey before storing replacement"
+ "Error %d deleting legacy OS bound RefKey"
+ "Error %d saving OS bound RefKey to keychain; aborting OS attestation"
+ "Error fetching AuthKit account %{public}@. Skipping auth mode save."
+ "Error saving AuthKit account after updating auth mode: %{public}@."
+ "Fetch auth mode entitlement check failed — Internal/Private access required"
+ "Fetch auth mode failed: %{public}@"
+ "Fetch auth mode returned an unexpected error: %{public}@"
+ "Fetch auth mode returned apple managed account fetchError: %{public}@"
+ "Fetch auth mode starting for %@"
+ "Fetch auth mode succeeded"
+ "Fetched auth mode %lu for %@"
+ "Fetching primary iCloud account for keep using flow."
+ "Found primary iCloud account %@ for keep using flow."
+ "Handling device-category push cmd:%lu."
+ "Invalid host certificates(%lu)."
+ "New BAA cert detected."
+ "No CK token available for primary iCloud account. Skipping keep using flow."
+ "No primary iCloud account found. Skipping keep using flow."
+ "Present FIDO auth completed with response: %@"
+ "Present basic login UI completed with response: %@"
+ "Present biometric or passcode validation completed with response: %@"
+ "Present keep using UI completed with response: %@"
+ "Present login alert completed with response: %@"
+ "Present native recovery UI completed with recoveredInfo: %{mask.hash}@"
+ "Present native recovery UI completed with response: %@"
+ "Present proximity broadcast UI completed with response: %@"
+ "Present proximity pairing UI completed with response: %@"
+ "Present proximity pin code UI completed with response: %@"
+ "Present second factor UI completed with response: %@"
+ "Present second factor alert completed with response: %@"
+ "Present server UI completed with response: %@"
+ "Presenting login alert for error: %@"
+ "Retryable DeviceIdentity error, retrying: %@"
+ "SettingsRedirectPromptProtocol"
+ "Show proximity error completed with response: %@"
+ "Silent reauth failed: %{public}@"
+ "T@\"<AKDeviceIdentityProtocol>\",&,N,V_deviceIdentity"
+ "T@\"<SettingsRedirectPromptProtocol>\",&,N,V_settingsRedirectPrompter"
+ "Trying to delete OSVersionAttestationRefKey for altDSID: %{mask.hash}@"
+ "Trying to get OSVersionAttestationRefKey for altDSID: %{mask.hash}@"
+ "Trying to store OSVersionAttestationRefKey for altDSID: %{mask.hash}@"
+ "Unable to call back to client! XPC Error: %@"
+ "Unable to fetch accounts for legacy OS bound RefKey cleanup: %@"
+ "_deviceIdentity"
+ "_isRetryableCryptoTokenKitError:"
+ "_isRetryableDeviceIdentityError:"
+ "_issueSigningMaterialForDataFields:isRetry:completion:"
+ "_sendDeviceCategoryListChangeNotification"
+ "_settingsRedirectPrompter"
+ "_showPromptWithContext:client:needFullUI:completion:"
+ "_storeOSVersionAttestationRefKey:forAltDSID:"
+ "akd.DeviceListValidator"
+ "contextFromAuthenticationServerResponse:accountManager:"
+ "createHostSignatureForData:options:completion:"
+ "createOSVersionAttestationRefKeyWithContext:error:"
+ "deleteLegacyOSVersionAttestationRefKeys"
+ "deviceIdentity"
+ "httpResponse"
+ "initWithAccountManager:tokenManager:userInfoController:profileManager:"
+ "initWithCurrentDevice:requestContext:accountManager:analyticsReporter:"
+ "initWithDeviceIdentity:"
+ "markThisDeviceForDeviceList:"
+ "requestContext"
+ "secAccessControlCreateWithProtection:flags:error:"
+ "secKeyCreateRandomKeyWithParameters:error:"
+ "setDeviceIdentity:"
+ "setIsThisDevice:"
+ "setSettingsRedirectPrompter:"
+ "settingsRedirectPrompter"
+ "v32@?0^{__SecKey=}8@\"NSArray\"16@\"NSError\"24"
+ "v40@0:8@\"NSData\"16@\"NSDictionary\"24@?<v@?@\"NSData\"@\"NSArray\"@\"NSError\">32"
- "@\"<AKAccountTDIDValidating>\""
- "AKAccountTDIDValidating"
- "AKAccountTDIDValidator"
- "AKDeviceIdentityShim"
- "Asking client to dismiss any presented server UI..."
- "Attempting to show login error: %@"
- "B24@?0@\"AKRemoteDevice\"8Q16"
- "B40@0:8@\"NSString\"16@\"NSString\"24@\"ACAccount\"32"
- "B40@0:8@16@24@32"
- "BasicServerRequest rejected: failed to construct AKAppleIDAuthenticationContext for altDSID %s"
- "BasicServerRequest rejected: urlBagKey '%s' is not in the allowed set"
- "Calling DeviceIdentity to issue certs."
- "Client decision to keep using: %@. Error: %@"
- "Could not dismiss UI! Error: %@"
- "DeviceListStoreManager - Unable to create trusted device version mismatch event for altDSID - %s."
- "Error %d deleteing OS bound key from keychain for altDSID %@"
- "Error %d retrieving OS bound key from keychain for altDSID %@"
- "Error %d storing OS bound key to keychain for altDSID %@"
- "Error fetching AuthKit account %@. Skipping auth mode save."
- "Error fetching AuthKitAccount %@"
- "Error fetching account for processing TDL response: %@"
- "Error saving AuthKit account after updating auth mode: %@."
- "Error saving account with trusted device ID: %@"
- "Failed to create analytics event for eventId - %s"
- "Failed to dismiss second factor UI %@"
- "Failed to refresh BAA device token after detecting new BAA cert %@."
- "Fetch user info returned an unexpected error: %@"
- "Fetch user info returned apple managed account fetchError: %@"
- "Fetched authMode for %@"
- "Internal access entitlement required but missing for performBasicServerRequest"
- "Invalid host signature(%lu) or certificates(%lu)."
- "Looking for primary iCloud account to suggest using..."
- "Native recovery failed! Error: %@"
- "Native recovery flow completed"
- "Native recovery flow: recoveredInfo %@"
- "New BAA cert detected, refreshing BAA device token."
- "Nothing found."
- "PCS web session TTL: authKitAccount=%@, isPDPEligible=%d -> %@"
- "Reported analytics event for eventId - %s"
- "Request to show server UI came back with error: %@"
- "Silent reauth failed: %@"
- "Skipping TDID presence non-HSA2 account"
- "Skipping non-prod analytics event for eventId - %s"
- "Successfully obtained trustedDeviceId from secondary auth response."
- "T@\"<AKAccountTDIDValidating>\",&,N,V_tdidValidator"
- "T@\"NSString\",R,N,V_trustedDeviceId"
- "TDID does not match the current device. Reporting mismatch."
- "TDID is different than what is persisted. Reporting rotated TDID."
- "TDID is not present when it shuld have been. Reporting missing TDID."
- "Telling client to ask the user about using Apple ID: %@"
- "Trying to delete OSVersionAttestationRefKey for altDSID: %@"
- "Trying to get OSVersionAttestationRefKey for altDSID: %@"
- "Trying to store OSVersionAttestationRefKey for altDSID: %@"
- "Unable to dismiss UI on client side even though auth is complete! Error: %@"
- "Unable to dismiss UI on client side! Error: %@"
- "Unable to dismiss client-side second-factor UI. Error: %@"
- "Unable to tear down native recovery UI! Error: %@"
- "Unable to tear down server UI! Error: %@"
- "X-Apple-I-Trusted-Device-Id"
- "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}40@0:8@16^{__SecAccessControl=}24^@32"
- "_tdidValidator"
- "_trustedDeviceId"
- "_updateAccountWithDeviceListResponse:"
- "_verifyPostUpdateAccountStateForAccount:"
- "akd.AccountTDIDValidator"
- "com.apple.authkit.StableIDAvailability"
- "com.apple.authkit.TDIDAvailability.signin"
- "com.apple.authkit.TDIDAvailability.upgrade"
- "createOSVersionAttestationRefKeyWithContext:accessControl:error:"
- "dismissNativeRecoveryUIForContext did succeed."
- "initWithAccountManager:currentDevice:"
- "initWithAccountManager:tokenManager:tdidValidator:userInfoController:profileManager:"
- "initWithClient:tdidValidator:passwordResetPresenter:"
- "initWithRawString:"
- "isTrustedDeviceIdEnabled"
- "presentNativeRecoveryUIForContext did succeed. Recovered info: %@ and error: %@"
- "rawValue"
- "serverTTL"
- "setTdidValidator:"
- "setTrustedDeviceId:forAccount:"
- "setTrustedDeviceId:telemetryEventId:forAccount:"
- "shorterTTL"
- "storeOSVersionAttestationRefKey:forAltDSID:"
- "tdidValidator"
- "trustedDeviceId"
- "trustedDeviceIdentifierForAccount:"
- "v24@0:8@\"ACAccount\"16"
- "validateTrustedDeviceIdOnUpgradeForAccount:"
```
