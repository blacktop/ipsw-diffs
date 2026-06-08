## AppAttestInternal

> `/System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal`

```diff

-132.2.0.0.0
-  __TEXT.__text: 0x69178
-  __TEXT.__auth_stubs: 0x1620
+151.0.0.0.0
+  __TEXT.__text: 0x69a70
   __TEXT.__objc_methlist: 0x6c4
-  __TEXT.__const: 0x3700
-  __TEXT.__cstring: 0x5dbe
-  __TEXT.__oslogstring: 0x38da
-  __TEXT.__gcc_except_tab: 0x91c
-  __TEXT.__swift5_typeref: 0xa70
-  __TEXT.__swift5_reflstr: 0xf9c
-  __TEXT.__swift5_assocty: 0x1f8
-  __TEXT.__constg_swiftt: 0xe48
-  __TEXT.__swift5_fieldmd: 0x1010
+  __TEXT.__const: 0x4550
+  __TEXT.__cstring: 0x64ee
+  __TEXT.__oslogstring: 0x389a
+  __TEXT.__gcc_except_tab: 0x724
+  __TEXT.__swift5_typeref: 0xb06
+  __TEXT.__swift5_reflstr: 0x127d
+  __TEXT.__swift5_assocty: 0x270
+  __TEXT.__constg_swiftt: 0x1058
+  __TEXT.__swift5_fieldmd: 0x1424
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__swift5_proto: 0x238
-  __TEXT.__swift5_types: 0x188
-  __TEXT.__swift_as_entry: 0x10
-  __TEXT.__swift_as_ret: 0x10
+  __TEXT.__swift5_proto: 0x280
+  __TEXT.__swift5_types: 0x1d8
+  __TEXT.__swift_as_entry: 0x14
+  __TEXT.__swift_as_ret: 0x14
+  __TEXT.__swift_as_cont: 0x34
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__swift5_capture: 0x218
-  __TEXT.__unwind_info: 0xfa0
-  __TEXT.__eh_frame: 0xea0
-  __TEXT.__objc_classname: 0x3f0
-  __TEXT.__objc_methname: 0x1791
-  __TEXT.__objc_methtype: 0x399
-  __TEXT.__objc_stubs: 0x1660
-  __DATA_CONST.__got: 0x4b8
-  __DATA_CONST.__const: 0x308
+  __TEXT.__swift5_capture: 0x250
+  __TEXT.__unwind_info: 0x1080
+  __TEXT.__eh_frame: 0x1008
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x310
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b8
+  __DATA_CONST.__objc_selrefs: 0x6b0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x48
-  __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__auth_got: 0xb20
-  __AUTH_CONST.__const: 0x2718
-  __AUTH_CONST.__cfstring: 0x1b20
+  __DATA_CONST.__objc_arraydata: 0xe8
+  __DATA_CONST.__got: 0x4c0
+  __AUTH_CONST.__const: 0x3128
+  __AUTH_CONST.__cfstring: 0x1aa0
   __AUTH_CONST.__objc_const: 0x1938
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x90
+  __AUTH_CONST.__auth_got: 0xbe8
   __AUTH.__objc_data: 0x3b8
-  __AUTH.__data: 0x1d0
+  __AUTH.__data: 0x2e0
   __DATA.__objc_ivar: 0x40
-  __DATA.__data: 0x570
-  __DATA.__bss: 0x3030
+  __DATA.__data: 0x498
+  __DATA.__bss: 0x38d0
   __DATA.__common: 0x38
   __DATA_DIRTY.__objc_data: 0x838
-  __DATA_DIRTY.__data: 0xaf0
-  __DATA_DIRTY.__bss: 0x1320
+  __DATA_DIRTY.__data: 0xbf8
+  __DATA_DIRTY.__bss: 0x13a0
   __DATA_DIRTY.__common: 0x150
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B28AD92F-34E0-3FBD-84D4-9CC8F8B7BCC5
-  Functions: 1371
-  Symbols:   2011
-  CStrings:  1357
+  UUID: 65A722F9-0566-30D6-9BFC-B851702CF866
+  Functions: 1488
+  Symbols:   2110
+  CStrings:  1039
 
Symbols:
+ _SecCodeCopySigningInformation
+ _SecCopyErrorMessageString
+ _SecStaticCodeCreateWithPath
+ __PROTOCOLS__TtCC17AppAttestInternal18AttestationManagerP33_6A9676F167D55AEBDBB586D6DBA1125411URLDelegate.18
+ ___block_descriptor_108_e8_32s40s48s56s64s72s80s88s96bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s96l8s88l8
+ ___fetchPublicKey_block_invoke.140
+ ___removeAllKeychainItemsForMissingAppsWithShouldExit_block_invoke.130
+ ___removeAllKeychainItemsForMissingAppsWithShouldExit_block_invoke.130.cold.1
+ ___removeAllKeychainItemsForMissingAppsWithShouldExit_block_invoke.130.cold.2
+ ___removeAllKeychainItemsForMissingAppsWithShouldExit_block_invoke.130.cold.3
+ ___removeAllKeychainItemsForMissingAppsWithShouldExit_block_invoke.133
+ ___removeAllKeychainItemsForMissingAppsWithShouldExit_block_invoke.133.cold.1
+ ___removeAllKeychainItemsForMissingAppsWithShouldExit_block_invoke.133.cold.2
+ ___removeAllKeychainItemsForMissingAppsWithShouldExit_block_invoke.133.cold.3
+ ___swift__destructor
+ ___swift__destructorTm
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.10
+ ___swift_closure_destructor.14
+ ___swift_closure_destructor.27
+ ___swift_closure_destructor.33
+ ___swift_closure_destructor.38
+ ___swift_closure_destructorTm
+ ___swift_exist.box.addr_destructor
+ ___swift_exist.box.addr_destructor.28
+ ___swift_exist.box.addr_destructor.4
+ ___swift_exist.box.addr_destructor.9
+ ___swift_memcpy112_8
+ ___swift_memcpy136_8
+ ___swift_memcpy184_8
+ ___swift_memcpy24_8
+ ___swift_memcpy56_8
+ ___swift_memcpy96_8
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_AppAttestInternal
+ _associated conformance 17AppAttestInternal18SecurityControllerC06DeviceD5StateOSHAASQ
+ _associated conformance 17AppAttestInternal18SecurityControllerC10BootPolicyOSHAASQ
+ _associated conformance 17AppAttestInternal18SecurityControllerC13SigningStatusOSHAASQ
+ _associated conformance 17AppAttestInternal18SecurityControllerC18NotaryTicketStatusOSHAASQ
+ _associated conformance 17AppAttestInternal18SecurityControllerC18ValidationCategoryOSHAASQ
+ _associated conformance 17AppAttestInternal18SecurityControllerC9SIPStatusOSHAASQ
+ _dyld_version_token_at_least
+ _kSecCodeInfoPList
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$attestKeyWith:credential:clientDataHash:clientSDKVersionToken:completion:
+ _objc_msgSend$generateAssertionWith:credential:clientDataHash:clientSDKVersionToken:completion:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _proc_pidpath_audittoken
+ _swift_errorRetain
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x8
+ _symbolic Say_____G 17AppAttestInternal22AttestationCBORManagerC0D11CertificateV
+ _symbolic So7NSErrorCSg
+ _symbolic _____ 10Foundation4DateV
+ _symbolic _____ 17AppAttestInternal0A22AttestationCBORContextV
+ _symbolic _____ 17AppAttestInternal18SecurityControllerC06DeviceD5StateO
+ _symbolic _____ 17AppAttestInternal18SecurityControllerC10BootPolicyO
+ _symbolic _____ 17AppAttestInternal18SecurityControllerC10ExtensionsV
+ _symbolic _____ 17AppAttestInternal18SecurityControllerC13SigningStatusO
+ _symbolic _____ 17AppAttestInternal18SecurityControllerC18NotaryTicketStatusO
+ _symbolic _____ 17AppAttestInternal18SecurityControllerC18ValidationCategoryO
+ _symbolic _____ 17AppAttestInternal18SecurityControllerC9SIPStatusO
+ _symbolic _____ 17AppAttestInternal21AuthenticationManagerC7StringsO
+ _symbolic _____ 17AppAttestInternal22AttestationCBORManagerC0D0V
+ _symbolic _____ 17AppAttestInternal22AttestationCBORManagerC0D11CertificateV
+ _symbolic _____ 17AppAttestInternal22AttestationCBORManagerC0D26StatementValidationContextV
+ _symbolic _____ 17AppAttestInternal22AttestationCBORManagerC0D28CertificateValidationContextV
+ _symbolic _____ 17AppAttestInternal22AttestationCBORManagerC0D9StatementV
+ _symbolic _____ 17AppAttestInternal22AttestationCBORManagerC17AuthenticatorDataV
+ _symbolic _____ 17AppAttestInternal22AttestationCBORManagerC17ValidationContextV
+ _symbolic _____ 17AppAttestInternal22AttestationCBORManagerC23AuthenticatorDataLayoutO
+ _symbolic _____ 17AppAttestInternal22AttestationCBORManagerC34AuthenticatorDataValidationContextV
+ _symbolic _____ s6UInt16V
+ _symbolic _____ s6UInt32V
+ _symbolic _____ s6UInt64V
+ _symbolic ______p s5ErrorP
+ _symbolic ytIeAgHr_
+ _type_layout_string 17AppAttestInternal0A22AttestationCBORContextV
+ _type_layout_string 17AppAttestInternal18SecurityControllerC10ExtensionsV
+ _type_layout_string 17AppAttestInternal22AttestationCBORManagerC0D0V
+ _type_layout_string 17AppAttestInternal22AttestationCBORManagerC0D26StatementValidationContextV
+ _type_layout_string 17AppAttestInternal22AttestationCBORManagerC0D9StatementV
+ _type_layout_string 17AppAttestInternal22AttestationCBORManagerC17AuthenticatorDataV
+ _type_layout_string 17AppAttestInternal22AttestationCBORManagerC17ValidationContextV
+ _type_layout_string 17AppAttestInternal22AttestationCBORManagerC34AuthenticatorDataValidationContextV
- __PROTOCOLS__TtCC17AppAttestInternal18AttestationManagerP33_6A9676F167D55AEBDBB586D6DBA1125411URLDelegate.16
- ___block_descriptor_140_e8_32s40s48s56s64s72s80s88s96bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s96l8s88l8
- ___fetchPublicKey_block_invoke.149
- ___removeAllKeychainItemsForMissingAppsWithShouldExit_block_invoke.139
- ___removeAllKeychainItemsForMissingAppsWithShouldExit_block_invoke.139.cold.1
- ___removeAllKeychainItemsForMissingAppsWithShouldExit_block_invoke.139.cold.2
- ___removeAllKeychainItemsForMissingAppsWithShouldExit_block_invoke.139.cold.3
- ___removeAllKeychainItemsForMissingAppsWithShouldExit_block_invoke.142
- ___removeAllKeychainItemsForMissingAppsWithShouldExit_block_invoke.142.cold.1
- ___removeAllKeychainItemsForMissingAppsWithShouldExit_block_invoke.142.cold.2
- ___removeAllKeychainItemsForMissingAppsWithShouldExit_block_invoke.142.cold.3
- ___swift_destroy_boxed_opaque_existential_1Tm
- ___swift_memcpy72_8
- ___swift_memcpy80_8
- _generateAttestationObject.cold.4
- _get_enum_tag_for_layout_string 17AppAttestInternal18SecurityControllerC6CDHashVSg
- _objc_msgSend$attestKeyWith:credential:clientDataHash:completion:
- _objc_msgSend$cdHash
- _objc_msgSend$dictionary
- _objc_msgSend$generateAssertionWith:credential:clientDataHash:completion:
- _objc_msgSend$type
- _objectdestroy.2Tm
- _objectdestroy.8Tm
- _objectdestroyTm
- _symbolic _____Sg 17AppAttestInternal18SecurityControllerC6CDHashV
- _symbolic ______A19At s5UInt8V
- _symbolic ______ypt So38UIApplicationOpenExternalURLOptionsKeya
- _symbolic _____y_____Sg_____G s6ResultOsRi_zRi0_zrlE 17AppAttestInternal0B24AttestationObjectContextV AC0E7ManagerC0E4FailO
- _symbolic _____y______p_____GSg s6ResultOsRi_zRi0_zrlE 17AppAttestInternal18AttestationRequestP AC4FailO
CStrings:
+ " }, clientSDKVersionToken="
+ ", clientSDKVersionToken="
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/TwoBit/AppAttestInternal/Source/Core/Controllers/SecurityController+Extensions.swift"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/TwoBit/AppAttestInternal/Source/Core/Utility/SecKey+AppAttestInternal.swift"
+ "AppAttest (%@-151) - %@"
+ "Appended extensions CBOR data."
+ "Client with AAC entitled default is attempting attestation."
+ "Client with AAC entitlement is attempting attestation. { aacEntitlement="
+ "Created key. { keyId="
+ "Extensions not appended."
+ "Failed to access key for assertion generation. { error="
+ "Failed to access key for attestation generation."
+ "Failed to convert extensions CBOR to Data representation."
+ "Failed to create static code representation of client binary. { error="
+ "Failed to determine application launch environment validation category."
+ "Failed to determine application launch environment validation category. { err="
+ "Failed to fetch SecKey public key hash. { error="
+ "Failed to fetch bundle version for extensions. { error="
+ "Failed to fetch bundle version."
+ "Failed to fetch client binary Info.plist file."
+ "Failed to fetch client binary path."
+ "Failed to fetch signing information of client binary. { error="
+ "Failed to generate assertion object."
+ "Failed to generate assertion object. { credential="
+ "Failed to generate attestation."
+ "InDiagnosticsMode"
+ "appStore"
+ "apple"
+ "apple_bundle_version_01"
+ "apple_cd_hash_hash_01"
+ "apple_cd_hash_type_01"
+ "apple_validation_category_01"
+ "com.apple.app-attest.aac-entitled"
+ "com.apple.assistivetouchd"
+ "com.apple.developer.automatic-assessment-configuration"
+ "com.apple.financed"
+ "developer"
+ "medium"
+ "none"
+ "objectContext={ "
+ "permissive"
+ "reduced"
+ "revoked"
+ "testFlight"
+ "unknown"
+ "valid"
- "#16@0:8"
- "$__lazy_storage_$_allowlistedDaemons"
- "$__lazy_storage_$_allowlistedExtensions"
- "$__lazy_storage_$_allowlistedThirdPartyAppExtensionTypes"
- "$__lazy_storage_$_appUUIDDataManager"
- "$__lazy_storage_$_assertionCborManager"
- "$__lazy_storage_$_assertionDataManager"
- "$__lazy_storage_$_attestationCborManager"
- "$__lazy_storage_$_attestationManager"
- "$__lazy_storage_$_authenticationManager"
- "$__lazy_storage_$_bundleRecordController"
- "$__lazy_storage_$_eligibilityManager"
- "$__lazy_storage_$_identityManager"
- "$__lazy_storage_$_isSupportedHardware"
- "$__lazy_storage_$_isSupportedSPIClient"
- "$__lazy_storage_$_keyDataManager"
- "$__lazy_storage_$_keychainController"
- "$__lazy_storage_$_recordCache"
- "$__lazy_storage_$_secTask"
- "$__lazy_storage_$_securityController"
- "$__lazy_storage_$_selfSecTask"
- "%25s:%-5d Adding CD Hash data to attestation object CBOR."
- ".cxx_destruct"
- "3kmXfug8VcxLI5yEmsqQKw"
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSMapTable\""
- "@\"NSMutableArray\""
- "@\"NSNumber\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8q16"
- "@28@0:8@16C24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@48@0:8{?=[8I]}16"
- "@56@0:8{?=[8I]}16@48"
- "@?"
- "@?16@0:8"
- "AppAttest (%@-132.2) - %@"
- "AppAttestCDHash"
- "AppAttestEligibilityManager"
- "AppAttestTaskCreator"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B48@0:8{?=[8I]}16"
- "C"
- "C16@0:8"
- "CBORArray"
- "CBORData"
- "CBORMap"
- "CBORNegative"
- "CBORString"
- "CBORUnsigned"
- "CBORValue"
- "CDhash"
- "DCBGSTask"
- "Failed to access attestation CBOR object."
- "Failed to create assertion object."
- "Failed to create assertion object. { uuid="
- "FeatureFlagsManager"
- "JSONObjectWithData:options:error:"
- "NSObject"
- "NSURLSessionDelegate"
- "PinnedUrlDelegate"
- "Q"
- "Q16@0:8"
- "Q24@0:8Q16"
- "T#,R"
- "T@\"NSArray\",&,N,V_allowlistedDaemons"
- "T@\"NSArray\",&,N,V_allowlistedFirstPartyExtensions"
- "T@\"NSArray\",&,N,V_allowlistedThirdPartyExtensions"
- "T@\"NSData\",&,N,V_cdHash"
- "T@\"NSNumber\",&,N,V_refreshInterval"
- "T@\"NSString\",&,N,V_observerID"
- "T@\"NSString\",&,N,V_taskID"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@?,C,N,V_taskHandler"
- "TC,N,V_type"
- "TC,R,N"
- "TQ,R"
- "Ti,R,N"
- "URL"
- "URLSession:didBecomeInvalidWithError:"
- "URLSession:didReceiveChallenge:completionHandler:"
- "URLSessionDidFinishEventsForBackgroundURLSession:"
- "URLWithString:"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_TtC17AppAttestInternal14KeyDataManager"
- "_TtC17AppAttestInternal15IdentityManager"
- "_TtC17AppAttestInternal16AppAttestHandler"
- "_TtC17AppAttestInternal18AppUUIDDataManager"
- "_TtC17AppAttestInternal18AttestationManager"
- "_TtC17AppAttestInternal18EligibilityManager"
- "_TtC17AppAttestInternal18KeychainController"
- "_TtC17AppAttestInternal18SecurityController"
- "_TtC17AppAttestInternal19DeviceAttestHandler"
- "_TtC17AppAttestInternal20AssertionCBORManager"
- "_TtC17AppAttestInternal20AssertionDataManager"
- "_TtC17AppAttestInternal21AuthenticationManager"
- "_TtC17AppAttestInternal22AttestationCBORManager"
- "_TtC17AppAttestInternal22BundleRecordController"
- "_TtCC17AppAttestInternal18AttestationManagerP33_6A9676F167D55AEBDBB586D6DBA1125411URLDelegate"
- "__swift_objectForKeyedSubscript:"
- "_allowlistedDaemons"
- "_allowlistedFirstPartyExtensions"
- "_allowlistedThirdPartyExtensions"
- "_cdHash"
- "_observerID"
- "_refreshInterval"
- "_taskHandler"
- "_taskID"
- "_type"
- "aaGuidLength"
- "accessGroup"
- "addCdHash"
- "addObject:"
- "allowlistedDaemons"
- "allowlistedFirstPartyExtensions"
- "allowlistedThirdPartyExtensions"
- "appClipMetadata"
- "appendBytes:length:"
- "appendData:"
- "applicationIdentifier"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "arrayByAddingObject:"
- "arrayByAddingObjectsFromArray:"
- "arrayWithArray:"
- "arrayWithObjects:count:"
- "attestKeyWith:credential:clientDataHash:completion:"
- "attestKeyWith:options:completion:"
- "auditToken"
- "authenticationMethod"
- "autorelease"
- "base64EncodedStringWithOptions:"
- "boolForKey:"
- "boolValue"
- "bundleIdentifier"
- "bundleRecordForAuditToken:error:"
- "bundleRecordWithBundleIdentifier:allowPlaceholder:error:"
- "bundleVersion"
- "bytes"
- "caseInsensitiveCompare:"
- "cborWithArray:"
- "cborWithData:"
- "cborWithDictionary:"
- "cborWithUTF8String:"
- "cdHash"
- "class"
- "code"
- "compare:"
- "componentsSeparatedByString:"
- "configuration"
- "conformsToProtocol:"
- "connectionProxyDictionary"
- "containsObject:"
- "containsValidEntitlements"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "create"
- "createForDefaultAttest"
- "createForDeviceAttestKeychain"
- "createForWebAuthAttestKeychain"
- "createKeyWith:completion:"
- "credentialForTrust:"
- "currentConnection"
- "dataTaskWithRequest:completionHandler:"
- "dataUsingEncoding:"
- "dataWithBytes:length:"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "dataWithData:"
- "dataWithJSONObject:options:error:"
- "dataWithPropertyList:format:options:error:"
- "dealloc"
- "debugDescription"
- "defaultSessionConfiguration"
- "description"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "domain"
- "doubleValue"
- "encodeStartItems:output:"
- "enumeratorWithOptions:"
- "errorWithDomain:code:userInfo:"
- "extensionPointRecord"
- "fetchBundleRecordFor:"
- "fetchEntitlementForAuditToken:withKey:"
- "fieldType"
- "fieldValue"
- "finishTasksAndInvalidate"
- "generateAssertionWith:credential:clientDataHash:completion:"
- "getBytes:range:"
- "getKeyFor:credential:completion:"
- "getLabel"
- "getNumUintBytes:"
- "getSortedKeys"
- "hasPrefix:"
- "hash"
- "host"
- "i16@0:8"
- "init"
- "initWith:"
- "initWithArray:"
- "initWithBase64EncodedData:options:"
- "initWithData:"
- "initWithData:encoding:"
- "initWithDomain:code:userInfo:"
- "initWithFormat:"
- "initWithFormat:arguments:"
- "initWithHash:andType:"
- "initWithHost:"
- "initWithKeyOptions:valueOptions:capacity:"
- "initWithPattern:options:error:"
- "initWithString:"
- "initWithSuiteName:"
- "initWithTaskIdentifier:observerIdentifier:"
- "initWithTrust:"
- "initWithUUIDString:"
- "initWithUnsignedInt:"
- "intValue"
- "integerValue"
- "invalidateAndCancel"
- "isBeta"
- "isEligibleApplicationExtensionFor:"
- "isEligibleApplicationFor:"
- "isEligibleClientFor:"
- "isEligibleDaemonFor:"
- "isEligibleForPrivService:"
- "isEqual:"
- "isEqualToString:"
- "isExtensionAttestationEnabled"
- "isKindOfClass:"
- "isMacEnabled"
- "isMemberOfClass:"
- "isModernizationEnabled"
- "isProfileValidated"
- "isProxy"
- "isSupported"
- "isSupportedHardware"
- "isUPPValidated"
- "keychainController"
- "length"
- "localizedDescription"
- "localizedStringForStatusCode:"
- "logger"
- "longLongValue"
- "m_data"
- "m_host"
- "matchesInString:options:range:"
- "meetsSecurityControlsForAuditToken:"
- "mutableCopy"
- "name"
- "nextObject"
- "numberOfRanges"
- "numberWithInt:"
- "objectAtIndexedSubscript:"
- "objectEnumerator"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observerID"
- "openURL:options:completionHandler:"
- "parentApplicationIdentifiers"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "persistentDomainForName:"
- "processIdentifier"
- "processInfo"
- "processName"
- "protectionSpace"
- "q"
- "q24@0:8@16"
- "rangeAtIndex:"
- "refreshInterval"
- "release"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "serverTrust"
- "sessionWithConfiguration:delegate:delegateQueue:"
- "setAdditionalInformation:item2:output:"
- "setAllowlistedDaemons:"
- "setAllowlistedFirstPartyExtensions:"
- "setAllowlistedThirdPartyExtensions:"
- "setCachePolicy:"
- "setCdHash:"
- "setDateFormat:"
- "setDoesRelativeDateFormatting:"
- "setHTTPBody:"
- "setHTTPMethod:"
- "setKey:value:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setObserverID:"
- "setRefreshInterval:"
- "setTaskCompleted"
- "setTaskHandler:"
- "setTaskID:"
- "setTimeoutInterval:"
- "setTimeoutIntervalForResource:"
- "setType:"
- "setURL:"
- "setUint:item2:output:"
- "setValue:forHTTPHeaderField:"
- "sharedApplication"
- "signWithClientUUID:blob:credential:completion:"
- "sortedArrayUsingComparator:"
- "statusCode"
- "stringFromDate:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "supported"
- "taskHandler"
- "taskID"
- "teamIdentifier"
- "type"
- "unarchivedObjectOfClass:fromData:error:"
- "unsignedIntValue"
- "unsignedLongValue"
- "v12@?0B8"
- "v16@0:8"
- "v20@0:8C16"
- "v24@0:8@\"NSURLSession\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8@\"NSURLSession\"16@\"NSError\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8C16C20@24"
- "v32@0:8Q16@24"
- "v36@0:8C16Q20@28"
- "v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
- "v40@0:8@16@24@?32"
- "v40@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16@24@?32"
- "v48@0:8@16@24@32@?40"
- "valueForHTTPHeaderField:"
- "valueForKey:"
- "write:"
- "zone"

```
