## devicecheckd

> `/System/Library/PrivateFrameworks/DeviceCheckInternal.framework/devicecheckd`

```diff

-88.3.0.0.0
-  __TEXT.__text: 0x31f4
-  __TEXT.__auth_stubs: 0x340
-  __TEXT.__objc_stubs: 0x800
-  __TEXT.__objc_methlist: 0x2cc
+108.2.0.0.0
+  __TEXT.__text: 0x43c8
+  __TEXT.__auth_stubs: 0x440
+  __TEXT.__objc_stubs: 0x5c0
+  __TEXT.__objc_methlist: 0x45c
+  __TEXT.__objc_classname: 0x97
+  __TEXT.__objc_methname: 0x9e2
+  __TEXT.__objc_methtype: 0x4c5
+  __TEXT.__cstring: 0x48d
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x235
-  __TEXT.__objc_classname: 0xb0
-  __TEXT.__oslogstring: 0x5c9
-  __TEXT.__objc_methname: 0x97d
-  __TEXT.__objc_methtype: 0x33e
-  __TEXT.__gcc_except_tab: 0x30
-  __TEXT.__unwind_info: 0x120
-  __DATA_CONST.__auth_got: 0x1b0
-  __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x198
-  __DATA_CONST.__cfstring: 0x1a0
-  __DATA_CONST.__objc_classlist: 0x30
+  __TEXT.__gcc_except_tab: 0xc0
+  __TEXT.__oslogstring: 0x62e
+  __TEXT.__unwind_info: 0x150
+  __DATA_CONST.__auth_got: 0x230
+  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__const: 0x1b8
+  __DATA_CONST.__cfstring: 0x240
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0xa70
-  __DATA.__objc_selrefs: 0x270
-  __DATA.__objc_ivar: 0x24
-  __DATA.__objc_data: 0x1e0
+  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA.__objc_const: 0x628
+  __DATA.__objc_selrefs: 0x2c8
+  __DATA.__objc_ivar: 0x18
+  __DATA.__objc_data: 0x140
   __DATA.__data: 0x120
-  __DATA.__bss: 0x40
+  __DATA.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security

   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/Versions/A/RemoteServiceDiscovery
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9AFEE9D8-3CF4-321D-BE78-866E4DFC67B5
-  Functions: 95
-  Symbols:   80
-  CStrings:  247
+  UUID: 8AB2A317-8511-327F-BB06-4812E3349EEC
+  Functions: 86
+  Symbols:   109
+  CStrings:  237
 
Symbols:
+ _AppAttest_AppAttestation_AssertWithTeamIdentifier
+ _AppAttest_AppAttestation_AttestKeyWithTeamIdentifier
+ _AppAttest_AppAttestation_CreateKeyWithTeamIdentifier
+ _AppAttest_AppAttestation_IsEligibleApplicationPriv
+ _AppAttest_AppAttestation_Sign
+ _AppAttest_DeviceAttestation_AttestKeyWithAuditToken
+ _AppAttest_DeviceAttestation_IsSupportedWithAuditToken
+ _AppAttest_WebAuthentication_AttestKey
+ _AppAttest_WebAuthentication_IsSupported
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSDictionary
+ _SecCertificateCopyData
+ _SecItemAdd
+ _SecItemCopyMatching
+ _SecItemDelete
+ ___kCFBooleanTrue
+ _createAppAttestError
+ _kSecAttrAccessGroup
+ _kSecAttrAccessible
+ _kSecAttrAccessibleAlwaysThisDeviceOnlyPrivate
+ _kSecAttrAccount
+ _kSecAttrGeneric
+ _kSecAttrLabel
+ _kSecAttrService
+ _kSecClass
+ _kSecClassGenericPassword
+ _kSecClassKey
+ _kSecReturnRef
+ _kSecUseDataProtectionKeychain
+ _kSecUseSystemKeychainAlways
+ _kSecValueData
+ _objc_enumerationMutation
+ _objc_retainAutorelease
+ _objc_retainBlock
+ _objc_terminate
- _ASAttributeContentVersion
- _OBJC_CLASS_$_MAAsset
- _OBJC_CLASS_$_MAAssetQuery
- _kBGSRefreshTaskID
- _objc_autorelease
- _objc_setProperty_nonatomic_copy
CStrings:
+ "%25s:%-5d App attestation service is not supported. { isSupportedHardware=%d, isEligibleApplication=%d, privService=%d }"
+ "%25s:%-5d App attestation service is supported. { isSupportedHardware=%d, isEligibleApplication=%d, privService=%d }"
+ "%25s:%-5d DeviceCheck is not supported."
+ "%25s:%-5d DeviceCheck is supported."
+ "%25s:%-5d Failed to fetch AppID."
+ "%25s:%-5d Failed to fetch appID for client connection from entitlement, using codesign identifier. { appID=%@ }"
+ "%25s:%-5d Failed to fetch key from keychain. { error=%@, err=%d }"
+ "%25s:%-5d Failed to register AA BGST task. { taskID=%@ }"
+ "%25s:%-5d Failed to register DC BGST task. { taskID=%@ }"
+ "%25s:%-5d Failed to save cert data to keychain. { error=%@ }"
+ "%25s:%-5d Fetched appID for client connection from entitlement. { appID=%@ }"
+ "%25s:%-5d Handling device look up request."
+ "%25s:%-5d Handling sign data with BAA certificate."
+ "%25s:%-5d Invalidated connection. { connection=%@ }"
+ "%25s:%-5d New incoming connection to devicecheckd. { newConnection=%@ }"
+ "%25s:%-5d SIGTERM requested, devicecheckd is being terminated."
+ "%25s:%-5d Saved cert data to keychain. { label=%@ }"
+ "%25s:%-5d Setting up SIGTERM observer."
+ "%25s:%-5d devicecheckd starting."
+ "%@:%@:%d"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/devicecheckd/Source/Core/DCClientHandler.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/devicecheckd/Source/Core/DCXPCListener.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/devicecheckd/Source/main.m"
+ "Failed to add %@ to keychain: %d"
+ "Failed to copy keychain item %@: %d"
+ "Failed to delete existing keychain item."
+ "Failed to remove existing keychain item %@: %d"
+ "Invalid input(s)."
+ "Invalid input."
+ "T@\"NSXPCConnection\",&,N,V_connection"
+ "aai"
+ "appAttestationAssertWithTeamIdentifier:appUUID:keyId:clientDataHash:completion:"
+ "appAttestationAttestKeyWithTeamIdentifier:appUUID:keyId:clientDataHash:completion:"
+ "appAttestationCreateKeyWithTeamIdentifier:appUUID:completion:"
+ "appAttestationDeviceAttestKey:useSystemKeychain:clientDataHash:options:completion:"
+ "appAttestationDeviceIsSupportedWithCompletion:"
+ "appAttestationPrivIsSupportedWithCompletion:"
+ "appAttestationSign:appUUID:keyId:completion:"
+ "appAttestationWebAttestKey:clientDataHash:authData:completion:"
+ "appAttestationWebIsSupportedWithCompletion:"
+ "appattest-device"
+ "appattest-webauthn"
+ "cert"
+ "connection"
+ "copy_keychain_item_for_system_keychain"
+ "countByEnumeratingWithState:objects:count:"
+ "dcd"
+ "delete_keychain_data"
+ "dictionaryWithObjects:forKeys:count:"
+ "generateAppIDFromCurrentConnection"
+ "isSupported"
+ "isSupportedForPrivService:completion:"
+ "localizedDescription"
+ "mutableCopy"
+ "objectAtIndexedSubscript:"
+ "setConnection:"
+ "setObject:forKeyedSubscript:"
+ "store_keychain_data"
+ "taskID"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v28@0:8B16@?20"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSString\"@\"NSString\"@\"NSError\">32"
+ "v40@0:8@16@24@?32"
+ "v48@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSData\"@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSData\"24@\"NSData\"32@?<v@?i@\"NSError\">40"
+ "v52@0:8@\"NSString\"16B24@\"NSData\"28@\"NSDictionary\"36@?<v@?i@\"NSError\">44"
+ "v52@0:8@16B24@28@36@?44"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40@?<v@?@\"NSData\"@\"NSError\">48"
+ "v56@0:8@16@24@32@40@?48"
- "  Using codesign identifier: %@"
- "!"
- "<%@: %p - version: %lu, refreshInterval: %f>"
- "@\"NSData\""
- "@32@0:8@16^@24"
- "AppAttest_AppAttestation_IsEligibleApplication - (%s)\n"
- "AppAttest_AppAttestation_IsSupported - (%s)\n"
- "AppAttest_AppAttestation_IsSupportedHardware - (%s)\n"
- "Attempting to download catalog, waiting for result..."
- "Attempting to validate asset: <%@ - %ld> - %@"
- "Catalog downloaded with result %ld..."
- "Catalog refetch not allowed, failing..."
- "Client App ID: %@"
- "Client has entitlement"
- "Connection invalidated... %@"
- "DC starting..."
- "DCAsset"
- "DCAssetFetcher"
- "DeviceCheck_IsSupported - (%s)\n"
- "FAILED"
- "Failed to parse asset, required fields are missing!"
- "Handling device look up request"
- "Handling sign data with baa certificate..."
- "Incoming connections.. %@"
- "Initiated an out of band catalog download completed with result: %ld"
- "Initiating an out of band catalog download"
- "Q"
- "Query success, results count: %lu"
- "Query sync result indicated missing asset catalog"
- "Querying..."
- "Returning parsed asset: %@"
- "SIGTERM requested, devicecheckd is being terminated."
- "SUCCESS"
- "Setting up SIGTERM observer."
- "Starting to fetch asset with context: %@"
- "T@\"NSData\",C,N,V_publicKey"
- "TQ,N,V_version"
- "Td,N,V_publicKeyRefreshInterval"
- "Unable to fetch AppID..."
- "Unexpected query result: %ld"
- "Unexpected result count detected!!!"
- "_assetQuery"
- "_fetchAssetWithContext:completionHandler:"
- "_generateAppIDFromCurrentConnection"
- "_handleMissingMetadataWithContext:completion:"
- "_handleSuccessForQuery:completion:"
- "_isSupported"
- "_publicKey"
- "_publicKeyRefreshInterval"
- "_queryMetadataWithContext:completion:"
- "_validateAsset:error:"
- "_version"
- "assetProperty:"
- "assetWithMobileAsset:"
- "attestation"
- "attributes"
- "com.apple.MobileAsset.DeviceCheck"
- "com.apple.devicecheck.pubvalue"
- "com.apple.devicecheck.refreshtimer"
- "com.apple.twobit.fetcherror"
- "core"
- "d"
- "d16@0:8"
- "doubleValue"
- "fetchPublicKeyAssetWithCompletion:"
- "firstObject"
- "initWithType:"
- "initiateMetadataFetchIgnoringCachesWithCompletion:"
- "publicKey"
- "publicKeyRefreshInterval"
- "queryMetaDataSync"
- "results"
- "setPublicKey:"
- "setPublicKeyRefreshInterval:"
- "setVersion:"
- "sharedFetcher"
- "startCatalogDownload:then:"
- "state"
- "unsignedIntegerValue"
- "updateTaskWithIdentifier:withRefreshInterval:"
- "v16@?0q8"
- "v24@0:8Q16"
- "v24@0:8d16"
- "version"

```
