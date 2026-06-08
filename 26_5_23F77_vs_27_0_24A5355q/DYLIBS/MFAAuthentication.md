## MFAAuthentication

> `/System/Library/PrivateFrameworks/MFAAuthentication.framework/MFAAuthentication`

```diff

-1147.120.2.0.0
-  __TEXT.__text: 0x3b47c
-  __TEXT.__auth_stubs: 0xed0
-  __TEXT.__objc_methlist: 0x444
-  __TEXT.__const: 0x62bb8
-  __TEXT.__cstring: 0x193f
-  __TEXT.__gcc_except_tab: 0x294
-  __TEXT.__oslogstring: 0x4a88
+1176.0.26.502.1
+  __TEXT.__text: 0x424d4
+  __TEXT.__objc_methlist: 0x494
+  __TEXT.__const: 0x69773
+  __TEXT.__cstring: 0x1a90
+  __TEXT.__gcc_except_tab: 0x22c
+  __TEXT.__oslogstring: 0x4d7c
   __TEXT.__ustring: 0xa
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x7c0
-  __TEXT.__eh_frame: 0x4c
-  __TEXT.__objc_classname: 0x6e
-  __TEXT.__objc_methname: 0x105f
-  __TEXT.__objc_methtype: 0x3dc
-  __TEXT.__objc_stubs: 0xfe0
-  __DATA_CONST.__got: 0x210
-  __DATA_CONST.__const: 0x4f20
+  __TEXT.__unwind_info: 0x7d8
+  __TEXT.__eh_frame: 0x48
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x5268
   __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4a0
+  __DATA_CONST.__objc_selrefs: 0x4d0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x778
-  __AUTH_CONST.__const: 0x16b0
-  __AUTH_CONST.__cfstring: 0x1aa0
-  __AUTH_CONST.__objc_const: 0x608
+  __DATA_CONST.__got: 0x210
+  __AUTH_CONST.__const: 0x1c30
+  __AUTH_CONST.__cfstring: 0x1b20
+  __AUTH_CONST.__objc_const: 0x648
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__auth_got: 0x7c8
   __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0xb8
+  __AUTH.__data: 0x208
   __DATA.__objc_ivar: 0x10
-  __DATA.__data: 0xa0
-  __DATA.__bss: 0x110
+  __DATA.__data: 0x60
+  __DATA.__bss: 0xc0
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x88
-  __DATA_DIRTY.__bss: 0x1b0
+  __DATA_DIRTY.__data: 0xc8
+  __DATA_DIRTY.__bss: 0x230
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EA63F8C5-118D-3AE9-9CC2-D13B0ED076BE
-  Functions: 817
-  Symbols:   3138
-  CStrings:  1098
+  UUID: 1E02D46C-57B5-311A-B019-44522998E61D
+  Functions: 849
+  Symbols:   3312
+  CStrings:  932
 
Symbols:
+ +[MFAACertificateManager _anchorCertificatesDataForTypes:].cold.4
+ +[MFAACertificateManager _anchorCertificatesDataForTypes:].cold.5
+ +[MFAACertificateManager _anchorCertificatesDataForTypes:].cold.6
+ +[MFAACertificateManager isMFi4AnyPolicy:]
+ +[MFAACertificateManager isMFi4AnyPolicy:].cold.1
+ +[MFAACertificateManager isMFi4AnyPolicy:].cold.2
+ +[MFAACertificateManager isMFi4CertInfo:]
+ -[MFAACertificateManager copyEvaluatedCertificateChainInfo:forSpecificType:].cold.13
+ -[MFAACertificateManager copyEvaluatedCertificateChainInfo:forSpecificType:].cold.14
+ -[MFAACertificateManager copyEvaluatedCertificateChainInfo:forSpecificType:].cold.15
+ -[MFAACertificateManager copyEvaluatedCertificateChainInfo:forSpecificType:].cold.16
+ -[MFAACertificateManager verifyModuleCertificate:forModule:forAuthFlags:]
+ -[MFAACertificateManager verifyModuleCertificate:forModule:forAuthFlags:].cold.1
+ -[MFAACertificateManager verifyModuleCertificate:forModule:forAuthFlags:].cold.10
+ -[MFAACertificateManager verifyModuleCertificate:forModule:forAuthFlags:].cold.2
+ -[MFAACertificateManager verifyModuleCertificate:forModule:forAuthFlags:].cold.3
+ -[MFAACertificateManager verifyModuleCertificate:forModule:forAuthFlags:].cold.4
+ -[MFAACertificateManager verifyModuleCertificate:forModule:forAuthFlags:].cold.5
+ -[MFAACertificateManager verifyModuleCertificate:forModule:forAuthFlags:].cold.6
+ -[MFAACertificateManager verifyModuleCertificate:forModule:forAuthFlags:].cold.7
+ -[MFAACertificateManager verifyModuleCertificate:forModule:forAuthFlags:].cold.8
+ -[MFAACertificateManager verifyModuleCertificate:forModule:forAuthFlags:].cold.9
+ -[NSData(Hash) SHA1]
+ -[NSData(Hash) SHA256]
+ -[NSData(Hash) SHA256_16]
+ GCC_except_table34
+ GCC_except_table39
+ _ApplePlatformCodeSigningMLDSA_RSARootCAG1
+ _ApplePlatformCodeSigningMLDSA_RSARootCAG1PublicKey
+ _ApplePlatformCodeSigningMLDSA_RSARootCAG1SKID
+ _ApplePlatformCodeSigningMLDSA_RSARootCAG1SPKI
+ _ApplePlatformCodeSigningMLDSA_RSARootCAG1_public_key
+ _ApplePlatformCodeSigningMLDSA_RSARootCAG1_skid
+ _ApplePlatformCodeSigningMLDSA_RSARootCAG1_spki
+ _CC_SHA1
+ _CC_SHA256
+ _CFNumberGetType
+ _CTEvaluateKeyTransparency
+ _CTEvaluateVLTileSigning
+ _CTGetAKIDFromCertificate
+ _CTGetSKIDFromCertificate
+ _CTOidAppleAAICA
+ _CTOidAppleKeyTransparencyLeaf
+ _CTOidAppleVLTilesSigning
+ _DeleteAllSynchronizableFeatureKeysForFeature.cold.1
+ _DeleteAllSynchronizableFeatureKeysForFeature.cold.2
+ _DeleteAllSynchronizableFeatureKeysForFeature.cold.3
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_47
+ _OUTLINED_FUNCTION_48
+ _OUTLINED_FUNCTION_49
+ _OUTLINED_FUNCTION_50
+ _OUTLINED_FUNCTION_51
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1PublicKey
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1SKID
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1SPKI
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_HW
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_HWPublicKey
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_HWSKID
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_HWSPKI
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_HW_public_key
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_HW_skid
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_HW_spki
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_draft13
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_draft13PublicKey
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_draft13SKID
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_draft13SPKI
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_draft13_public_key
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_draft13_skid
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_draft13_spki
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_public_key
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_skid
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_spki
+ _X509ExtensionParseKeyTransparencyLeaf
+ _X509PolicyVLTile
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSData_$_Hash
+ __OBJC_$_CATEGORY_NSData_$_Hash
+ ___50+[MFAATokenManager isTokenValidForFeatures:token:]_block_invoke.39
+ ___62-[MFAACertificateManager _getCachedCertStatus:issuerSeq:ppid:]_block_invoke.147
+ ___78-[MFAACertificateManager _validateCertificateWithServer:issuerSeq:ppid:error:]_block_invoke.142
+ _____initMFAADeviceIdentity_block_invoke.10
+ ____anchorCertsForMFi4_block_invoke
+ ___block_descriptor_tmp.20
+ ___block_descriptor_tmp.36
+ ___block_descriptor_tmp.8
+ ___block_literal_global.13
+ ___block_literal_global.226
+ ___block_literal_global.228
+ ___block_literal_global.230
+ ___block_literal_global.232
+ ___block_literal_global.234
+ ___block_literal_global.236
+ ___block_literal_global.238
+ ___block_literal_global.240
+ ___block_literal_global.242
+ ___block_literal_global.38
+ ___logObjectForModule_block_invoke
+ ___logObjectForModule_block_invoke.cold.1
+ _algorithmIsPQCComposite
+ _cchybridsig_import_pubkey
+ _cchybridsig_lamps13_mldsa87_rsa3072_pub_ctx_init
+ _cchybridsig_mldsa87_rsa3072_pub_ctx_init
+ _cchybridsig_verify_prehashed_with_context
+ _cpGetComponentIndex
+ _cpSetCertificate
+ _kCertDER_ComponentAuth_ComponentRoot_Area51
+ _kCertDER_ComponentAuth_ComponentRoot_Area51_Length
+ _logObjectForModule.onceToken
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$isComponentCertInfo:
+ _objc_msgSend$isEqualToData:
+ _objc_msgSend$isMFi4AnyPolicy:
+ _objc_msgSend$isMFi4CertInfo:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
+ _pqcCompositeAlgs
+ _sha512WithMLDSA87_RSA3072_draft13
+ _sha512WithMLDSA87_RSA3072_draft7
+ _validateSignaturePQCComposite
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.1
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.10
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.11
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.12
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.13
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.14
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.15
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.16
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.17
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.18
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.19
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.2
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.20
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.21
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.22
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.23
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.24
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.25
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.26
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.27
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.3
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.4
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.5
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.6
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.7
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.8
- -[MFAACertificateManager validateCertificateChain:type:realtime:error:].cold.9
- GCC_except_table33
- GCC_except_table38
- _SecItemUpdate
- _X509ExtensionParseMFIAuthv3Leaf
- __DeleteAllSynchronizableKeysForMFi4
- __DeleteAllSynchronizableKeysForMFi4.cold.1
- __DeleteAllSynchronizableKeysForMFi4.cold.2
- __DeleteAllSynchronizableKeysForMFi4.cold.3
- __UpdateMFi4FeatureKeyAttributes
- __UpdateMFi4FeatureKeyAttributes.cold.1
- __UpdateMFi4FeatureKeyAttributes.cold.2
- __UpdateMFi4FeatureKeyAttributes.cold.3
- __UpdateMFi4FeatureKeyAttributes.cold.4
- __UpdateMFi4FeatureKeyAttributes.cold.5
- __UpdateMFi4FeatureKeyAttributes.cold.6
- ___50+[MFAATokenManager isTokenValidForFeatures:token:]_block_invoke.40
- ___62-[MFAACertificateManager _getCachedCertStatus:issuerSeq:ppid:]_block_invoke.133
- ___78-[MFAACertificateManager _validateCertificateWithServer:issuerSeq:ppid:error:]_block_invoke.128
- _____initMFAADeviceIdentity_block_invoke.14
- ___block_descriptor_tmp.12
- ___block_descriptor_tmp.15
- ___block_descriptor_tmp.32
- ___block_literal_global.17
- ___block_literal_global.209
- ___block_literal_global.211
- ___block_literal_global.213
- ___block_literal_global.215
- ___block_literal_global.217
- ___block_literal_global.219
- ___block_literal_global.221
- ___findAuthCP
- ___findAuthCP.cold.1
- ___findAuthCP.cold.2
- ___findAuthCP.cold.3
- __anchorCertsForDEVN.anchorCerts
- __anchorCertsForDEVN.onceToken
- __anchorCertsForMFi2.anchorCerts
- __anchorCertsForMFi2.onceToken
- __anchorCertsForMFi3.anchorCerts
- __anchorCertsForMFi3.onceToken
- __anchorCertsForProvenance.anchorCerts
- __anchorCertsForProvenance.onceToken
- __anchorCertsForWPC.anchorCerts
- __anchorCertsForWPC.onceToken
- __findValidIndex
- __findValidIndex.cold.1
- __readStateFromDisk
- __storeIndexToDisk
- __storeStateToDisk
- _gCertificateUseTimestamp
- _malloc
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
- _objc_retain_x27
CStrings:
+ "%lu anchor cert(s) returned for MFi4"
+ "(moduleType=%d) Auth flags indicate Veridian...do not compare Roswell auth flags"
+ "(moduleType=%d) Error: Could not create caps from certificate"
+ "(moduleType=%d) Error: Could not evaluate certificate"
+ "(moduleType=%d) Failure: cannot find component type"
+ "(moduleType=%d) Failure: cannot find touchTypeData"
+ "(moduleType=%d) Failure: componentType:%@"
+ "(moduleType=%d) Failure: validated cert caps, but auth flags and certificate do not match"
+ "(moduleType=%d) Success: validated cert caps"
+ "(moduleType=%d) mfi2_3:%d, mfi4:%d"
+ "+[MFAACertificateManager isMFi4AnyPolicy:]"
+ "Add ComponentAuth_ComponentRoot for types: 0x%02X"
+ "Add ComponentAuth_ComponentRoot_Area51 for types: 0x%02X"
+ "Add VeridianAuth_SoftCA for types: 0x%02X"
+ "ComponentIndex"
+ "Mac"
+ "Mac Display"
+ "Mac LAS"
+ "PearlIDCapability"
+ "Phone Display"
+ "Repair UCRT"
+ "copyEvaluatedCertificateChainInfo: policy %llu"
+ "cpGetComponentIndex: Component index not CFNumber"
+ "cpGetComponentIndex: Component index not SInt32"
+ "cpGetComponentIndex: Failed to find ComponentIndex property"
+ "cpGetComponentIndex: Got component index : %x\n"
+ "iPad"
+ "iPad Display"
+ "iPhone"
+ "validateCertificateChain: CFArrayCreateMutable failed for type %d"
+ "validateCertificateChain: Cannot parse intermediateCert for type %d"
+ "validateCertificateChain: Cannot parse leafCert for type %d"
+ "validateCertificateChain: MFi4 status = %d"
- ".cxx_destruct"
- "8olRm6C1xqr7AJGpLRnpSw"
- "@\"NSUserDefaults\""
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@28@0:8@16i24"
- "@32@0:8@16@24"
- "@32@0:8@16q24"
- "@40@0:8@16q24@32"
- "ACCUserDefaults"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B28@0:8@16i24"
- "B32@0:8Q16@24"
- "B40@0:8@16@24@32"
- "JSONObjectWithData:options:error:"
- "MFAACertificateManager"
- "MFAAError"
- "MFAANetworkProtocol"
- "MFAAPairingManager"
- "MFAATokenManager"
- "MFAA_errorWithDomain:code:"
- "MFAA_errorWithDomain:code:description:"
- "MFAA_errorWithDomain:code:failureReason:"
- "SHA256"
- "T@\"NSUserDefaults\",&,N,V_userDefaults"
- "T@\"NSXPCConnection\",&,N,V_xpcConnection"
- "UTF8String"
- "UUID"
- "Unable to fetch key for featureTag %@, unable to update"
- "Unable to update attributes, status=%d"
- "Updated attributes for key"
- "_anchorCertificatesDataForTypes:"
- "_anchorType2CertType:"
- "_getAnchorCertsForPolicy:"
- "_getCachedCertStatus:issuerSeq:ppid:"
- "_init"
- "_userDefaults"
- "_validateBAACertificateChain:error:"
- "_validateCertificateChain:realtime:error:"
- "_validateCertificateWithServer:issuerSeq:ppid:error:"
- "_validateX509CertificateChain:anchorCerts:error:"
- "_xpcConnection"
- "addObject:"
- "addObjectsFromArray:"
- "addPairingWithToken:completionHandler:"
- "addPairingWithToken:withReply:"
- "anchorCertificatesForTypes:"
- "appendData:"
- "appendFormat:"
- "array"
- "arrayForKey:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "authVersionFromCertificateChainInfo:"
- "base64EncodedStringWithOptions:"
- "boolForKey:"
- "bytes"
- "characterSetWithCharactersInString:"
- "componentsJoinedByString:"
- "componentsSeparatedByCharactersInSet:"
- "confirmActivationForAuthToken:withUUID:completionHandler:"
- "confirmActivationForToken:withUUID:completionHandler:"
- "confirmActivationForToken:withUUID:withReply:"
- "copy"
- "copyCertificateSerialNumber:authVer:"
- "copyEvaluatedCertificateChainInfo:"
- "copyEvaluatedCertificateChainInfo:forSpecificType:"
- "copyLeafCertificateSerialNumber:"
- "copyParsedCertificateChainInfo:"
- "copyParsedCertificateChainInfo:assumeType:"
- "copyParsedCertificateChainInfoFromCerts:assumeType:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createVeridianNonce:withChallenge:"
- "dataUsingEncoding:"
- "dataWithBytes:length:"
- "dataWithContentsOfFile:"
- "dataWithData:"
- "dataWithJSONObject:options:error:"
- "date"
- "dateWithTimeIntervalSinceReferenceDate:"
- "description"
- "determineCertificateType:"
- "dictionaryForKey:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "doubleForKey:"
- "errorWithDomain:code:userInfo:"
- "found private valid key for featureTag %@, update to support new attributes"
- "generatePairingTokenWithCompletionHandler:"
- "getBytes:range:"
- "getCachedStatusForCertSerial:issuerSeq:ppid:withReply:"
- "getUUIDBytes:"
- "hexadecimalCharacterSet"
- "i20@0:8i16"
- "i24@0:8@16"
- "i32@0:8@16^@24"
- "i36@0:8@16B24^@28"
- "i40@0:8@16@24@32"
- "i40@0:8@16@24^@32"
- "i40@0:8@16i24B28^@32"
- "i48@0:8@16@24@32^@40"
- "increaseLengthBy:"
- "init"
- "initWithBase64EncodedString:options:"
- "initWithBytes:length:"
- "initWithServiceName:"
- "initWithSuiteName:"
- "instancesRespondToSelector:"
- "intValue"
- "integerForKey:"
- "interfaceWithProtocol:"
- "invertedSet"
- "isBAAUserCertInfo:"
- "isBAAUserPolicy:"
- "isCertificateValidForFeatures:certificate:"
- "isComponentCertInfo:"
- "isComponentPolicy:"
- "isEqual:"
- "isEqualToString:"
- "isMFi2_3CertInfo:"
- "isMFi2_3Policy:"
- "isTokenValidForFeatures:token:"
- "isValidJSONObject:"
- "length"
- "localeIdentifier"
- "mutableCopy"
- "new attribute dictionary %@"
- "null"
- "numberWithUnsignedInt:"
- "numberWithUnsignedLongLong:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "raise:format:"
- "remoteObjectProxyWithErrorHandler:"
- "removeObjectForKey:"
- "removePairingWithToken:completionHandler:"
- "removePairingWithToken:withReply:"
- "requestActivationForAuthToken:withUUID:completionHandler:"
- "requestActivationForToken:withUUID:completionHandler:"
- "requestActivationForToken:withUUID:withReply:"
- "requestMetadataForAuthToken:withUUID:requestedLocale:requestInfo:completionHandler:"
- "requestMetadataForCertSerial:issuerSeq:ppid:requestedLocale:requestInfo:withReply:"
- "requestMetadataForCertificate:requestedLocale:requestInfo:completionHandler:"
- "requestMetadataForToken:withUUID:requestedLocale:requestInfo:completionHandler:"
- "requestMetadataForToken:withUUID:requestedLocale:requestInfo:withReply:"
- "resume"
- "set"
- "setDouble:forKey:"
- "setInteger:forKey:"
- "setObject:forKey:"
- "setRemoteObjectInterface:"
- "setUserDefaults:"
- "setValue:forKey:"
- "setWithSet:"
- "setXpcConnection:"
- "sharedDefaults"
- "sharedDefaultsIapd"
- "sharedDefaultsLogging"
- "sharedManager"
- "stringByTrimmingCharactersInSet:"
- "stringForKey:"
- "stringWithString:"
- "timeIntervalSince1970"
- "timeIntervalSinceDate:"
- "unsignedLongLongValue"
- "userDefaults"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSData\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@16@?24"
- "v36@0:8@16B24@?28"
- "v40@0:8@\"NSData\"16@\"NSString\"24@?<v@?@\"NSData\"@\"NSError\">32"
- "v40@0:8@\"NSData\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"NSData\"16@\"NSData\"24@\"NSString\"32@?<v@?i@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v56@0:8@\"NSData\"16@\"NSString\"24@\"NSLocale\"32@\"NSDictionary\"40@?<v@?@\"NSString\"@\"NSLocale\"@\"NSDictionary\"@\"NSError\">48"
- "v56@0:8@16@24@32@40@?48"
- "v64@0:8@\"NSData\"16@\"NSData\"24@\"NSString\"32@\"NSLocale\"40@\"NSDictionary\"48@?<v@?@\"NSString\"@\"NSLocale\"@\"NSDictionary\"@\"NSError\">56"
- "v64@0:8@16@24@32@40@48@?56"
- "validateCertSerial:issuerSeq:ppid:withReply:"
- "validateCertificate:realtime:completionHandler:"
- "validateCertificate:realtime:error:"
- "validateCertificateChain:realtime:error:"
- "validateCertificateChain:type:realtime:error:"
- "valueForKey:"
- "verifyCertificateChainInfoSerialNumber:"
- "verifyCertificateSerialNumber:authVer:"
- "verifyCertificateSerialNumberBySerialNumber:authVer:"
- "verifyNonceSignature:nonce:signature:"
- "verifyPairingWithToken:completionHandler:"
- "verifyPairingWithToken:withReply:"
- "writeToFile:atomically:"
- "xpcConnection"

```
