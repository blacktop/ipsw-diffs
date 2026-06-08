## CoreIDCred

> `/System/Library/PrivateFrameworks/CoreIDCred.framework/CoreIDCred`

```diff

-8.504.0.0.0
-  __TEXT.__text: 0x3e9b4
-  __TEXT.__auth_stubs: 0xbf0
-  __TEXT.__objc_methlist: 0x21c4
-  __TEXT.__const: 0x3650
-  __TEXT.__cstring: 0x1a4b
-  __TEXT.__oslogstring: 0x3e6c
+9.31.0.0.0
+  __TEXT.__text: 0x3f750
+  __TEXT.__objc_methlist: 0x20ac
+  __TEXT.__const: 0x3680
+  __TEXT.__cstring: 0x229b
+  __TEXT.__oslogstring: 0x2ccc
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__constg_swiftt: 0x7d0
-  __TEXT.__swift5_typeref: 0xc87
+  __TEXT.__swift5_typeref: 0xcf3
+  __TEXT.__constg_swiftt: 0x800
   __TEXT.__swift5_builtin: 0x1b8
   __TEXT.__swift5_reflstr: 0x334
-  __TEXT.__swift5_fieldmd: 0x65c
-  __TEXT.__swift5_assocty: 0x60
-  __TEXT.__swift5_proto: 0x2b4
-  __TEXT.__swift5_types: 0xe4
+  __TEXT.__swift5_fieldmd: 0x668
+  __TEXT.__swift5_assocty: 0x78
+  __TEXT.__swift5_proto: 0x2cc
+  __TEXT.__swift5_types: 0xe8
   __TEXT.__swift5_mpenum: 0x28
   __TEXT.__swift5_capture: 0x2f4
   __TEXT.__swift_as_entry: 0x6c
-  __TEXT.__swift_as_ret: 0x84
-  __TEXT.__unwind_info: 0x1548
-  __TEXT.__eh_frame: 0x1678
-  __TEXT.__objc_classname: 0x3e2
-  __TEXT.__objc_methname: 0x4974
-  __TEXT.__objc_methtype: 0x12da
-  __TEXT.__objc_stubs: 0x1d60
-  __DATA_CONST.__got: 0x270
-  __DATA_CONST.__const: 0x9e8
-  __DATA_CONST.__objc_classlist: 0xe8
+  __TEXT.__swift_as_ret: 0x6c
+  __TEXT.__swift_as_cont: 0x12c
+  __TEXT.__unwind_info: 0x1568
+  __TEXT.__eh_frame: 0x1528
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xa10
+  __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xca0
+  __DATA_CONST.__objc_selrefs: 0xc88
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0xc0
-  __AUTH_CONST.__auth_got: 0x608
-  __AUTH_CONST.__const: 0x1b50
-  __AUTH_CONST.__cfstring: 0x17c0
-  __AUTH_CONST.__objc_const: 0x3960
-  __AUTH.__objc_data: 0x2f8
+  __DATA_CONST.__objc_superrefs: 0xa0
+  __DATA_CONST.__got: 0x318
+  __AUTH_CONST.__const: 0x1b80
+  __AUTH_CONST.__cfstring: 0x1560
+  __AUTH_CONST.__objc_const: 0x3740
+  __AUTH_CONST.__auth_got: 0x7e0
+  __AUTH.__objc_data: 0x3d0
   __AUTH.__data: 0xe8
-  __DATA.__objc_ivar: 0x264
-  __DATA.__data: 0xc10
-  __DATA.__bss: 0x5700
-  __DATA_DIRTY.__objc_data: 0x708
-  __DATA_DIRTY.__data: 0x88
+  __DATA.__objc_ivar: 0x210
+  __DATA.__data: 0xd40
+  __DATA.__bss: 0x5990
+  __DATA_DIRTY.__objc_data: 0x640
+  __DATA_DIRTY.__data: 0x118
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 81E973A0-46C0-3310-9DE3-11D7AF197E55
-  Functions: 2144
-  Symbols:   3399
-  CStrings:  1490
+  UUID: A2CA69D9-CCF8-3D81-9024-9DD8BD847DAC
+  Functions: 2135
+  Symbols:   3278
+  CStrings:  599
 
Symbols:
+ -[DCBiometricStore _remoteObjectProxyWithErrorHandler:]
+ -[DCBiometricStore connection]
+ -[DCBiometricStore dealloc]
+ -[DCBiometricStore globalPayloadAuthACLWithCompletion:]
+ -[DCBiometricStore setConnection:]
+ -[DCCredentialOptions requiresFirstPartyInAppPresentment]
+ -[DCCredentialOptions setRequiresFirstPartyInAppPresentment:]
+ -[DCCredentialProperties elementIdentifiersByNamespace]
+ -[DCCredentialProperties setElementIdentifiersByNamespace:]
+ -[DCCredentialStore deletePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:credentialIdentifier:completion:]
+ -[DCCredentialStore deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:keystoreType:completion:]
+ -[DCCredentialStore retrieveAllItemsFromSyncableKeyStoreForItemService:completion:]
+ -[DCCredentialStore retrievePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:completion:]
+ -[DCCredentialStore retrievePIITokenFromSyncableKeyStoreForIdentifier:keystoreType:credentialIdentifier:completion:]
+ -[DCCredentialStore storePIIDataInSyncableKeyStoreForIdentifier:data:keystoreType:piiDataType:credentialIdentifier:completion:]
+ -[DCCredentialStore storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:keystoreType:completion:]
+ -[DCCredentialStore updatePIIDataInSyncableKeyStoreForIdentifier:attributesToUpdate:keystoreType:piiDataType:credentialIdentifier:completion:]
+ -[DCCredentialStore updatePIITokenInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:keystoreType:completion:]
+ -[DCCredentialStoreClient deletePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:credentialIdentifier:completion:]
+ -[DCCredentialStoreClient deletePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:credentialIdentifier:completion:].cold.1
+ -[DCCredentialStoreClient retrieveAllItemsFromSyncableKeyStoreForItemService:completion:]
+ -[DCCredentialStoreClient retrieveAllItemsFromSyncableKeyStoreForItemService:completion:].cold.1
+ -[DCCredentialStoreClient retrievePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:completion:]
+ -[DCCredentialStoreClient retrievePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:completion:].cold.1
+ -[DCCredentialStoreClient storePIIDataInSyncableKeyStoreForIdentifier:data:keystoreType:piiDataType:credentialIdentifier:completion:]
+ -[DCCredentialStoreClient storePIIDataInSyncableKeyStoreForIdentifier:data:keystoreType:piiDataType:credentialIdentifier:completion:].cold.1
+ -[DCCredentialStoreClient updatePIIDataInSyncableKeyStoreForIdentifier:attributesToUpdate:keystoreType:piiDataType:credentialIdentifier:completion:]
+ -[DCCredentialStoreClient updatePIIDataInSyncableKeyStoreForIdentifier:attributesToUpdate:keystoreType:piiDataType:credentialIdentifier:completion:].cold.1
+ _DCCredentialPIIDataTypeToString
+ _NSUnderlyingErrorKey
+ _OBJC_IVAR_$_DCBiometricStore._connection
+ _OBJC_IVAR_$_DCCredentialOptions._requiresFirstPartyInAppPresentment
+ _OBJC_IVAR_$_DCCredentialProperties._elementIdentifiersByNamespace
+ __CLASS_METHODS_DCCredentialAuthACL
+ __CLASS_METHODS_DCCredentialCryptoKeyInfo
+ __CLASS_METHODS_DCCredentialElement
+ __CLASS_PROPERTIES_DCCredentialAuthACL
+ __CLASS_PROPERTIES_DCCredentialCryptoKeyInfo
+ __CLASS_PROPERTIES_DCCredentialElement
+ __DATA_DCCredentialAuthACL
+ __DATA_DCCredentialCryptoKeyInfo
+ __DATA_DCCredentialElement
+ __INSTANCE_METHODS_DCCredentialAuthACL
+ __INSTANCE_METHODS_DCCredentialCryptoKeyInfo
+ __INSTANCE_METHODS_DCCredentialElement
+ __IVARS_DCCredentialAuthACL
+ __IVARS_DCCredentialCryptoKeyInfo
+ __IVARS_DCCredentialElement
+ __METACLASS_DATA_DCCredentialAuthACL
+ __METACLASS_DATA_DCCredentialCryptoKeyInfo
+ __METACLASS_DATA_DCCredentialElement
+ __PROPERTIES_DCCredentialAuthACL
+ __PROPERTIES_DCCredentialCryptoKeyInfo
+ __PROPERTIES_DCCredentialElement
+ __PROTOCOLS_DCCredentialAuthACL
+ __PROTOCOLS_DCCredentialAuthACL.2
+ __PROTOCOLS_DCCredentialCryptoKeyInfo
+ __PROTOCOLS_DCCredentialCryptoKeyInfo.2
+ __PROTOCOLS_DCCredentialElement
+ __PROTOCOLS_DCCredentialElement.2
+ __PROTOCOLS_DCPresentmentRequest.10
+ __PROTOCOLS_DCPresentmentRequestedElement.6
+ ___100-[DCBiometricStore refreshProgenitorKeyDesignationsWithSessionHandoffToken:onlyIfNeeded:completion:]_block_invoke
+ ___100-[DCBiometricStore refreshProgenitorKeyDesignationsWithSessionHandoffToken:onlyIfNeeded:completion:]_block_invoke_2
+ ___100-[DCBiometricStore refreshProgenitorKeyDesignationsWithSessionHandoffToken:onlyIfNeeded:completion:]_block_invoke_2.cold.1
+ ___100-[DCBiometricStore refreshProgenitorKeyDesignationsWithSessionHandoffToken:onlyIfNeeded:completion:]_block_invoke_2.cold.2
+ ___101-[DCCredentialStore deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:completion:]_block_invoke.31
+ ___106-[DCCredentialStore retrievePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:completion:]_block_invoke
+ ___106-[DCCredentialStore retrievePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:completion:]_block_invoke.41
+ ___106-[DCCredentialStore retrievePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:completion:]_block_invoke.cold.1
+ ___112-[DCCredentialStoreClient retrievePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:completion:]_block_invoke
+ ___112-[DCCredentialStoreClient retrievePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:completion:]_block_invoke_2
+ ___112-[DCCredentialStoreClient retrievePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:completion:]_block_invoke_2.cold.1
+ ___112-[DCCredentialStoreClient retrievePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:completion:]_block_invoke_2.cold.2
+ ___114-[DCCredentialStore deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:keystoreType:completion:]_block_invoke
+ ___114-[DCCredentialStore deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:keystoreType:completion:]_block_invoke.35
+ ___114-[DCCredentialStore deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:keystoreType:completion:]_block_invoke.cold.1
+ ___116-[DCCredentialStore retrievePIITokenFromSyncableKeyStoreForIdentifier:keystoreType:credentialIdentifier:completion:]_block_invoke
+ ___116-[DCCredentialStore retrievePIITokenFromSyncableKeyStoreForIdentifier:keystoreType:credentialIdentifier:completion:]_block_invoke.34
+ ___116-[DCCredentialStore retrievePIITokenFromSyncableKeyStoreForIdentifier:keystoreType:credentialIdentifier:completion:]_block_invoke.cold.1
+ ___116-[DCCredentialStore storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:keystoreType:completion:]_block_invoke
+ ___116-[DCCredentialStore storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:keystoreType:completion:]_block_invoke.33
+ ___116-[DCCredentialStore storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:keystoreType:completion:]_block_invoke.cold.1
+ ___118-[DCCredentialStore updatePIITokenInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:]_block_invoke.32
+ ___125-[DCCredentialStore deletePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:credentialIdentifier:completion:]_block_invoke
+ ___125-[DCCredentialStore deletePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:credentialIdentifier:completion:]_block_invoke.42
+ ___125-[DCCredentialStore deletePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:credentialIdentifier:completion:]_block_invoke.cold.1
+ ___127-[DCCredentialStore storePIIDataInSyncableKeyStoreForIdentifier:data:keystoreType:piiDataType:credentialIdentifier:completion:]_block_invoke
+ ___127-[DCCredentialStore storePIIDataInSyncableKeyStoreForIdentifier:data:keystoreType:piiDataType:credentialIdentifier:completion:]_block_invoke.40
+ ___127-[DCCredentialStore storePIIDataInSyncableKeyStoreForIdentifier:data:keystoreType:piiDataType:credentialIdentifier:completion:]_block_invoke.cold.1
+ ___131-[DCCredentialStore updatePIITokenInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:keystoreType:completion:]_block_invoke
+ ___131-[DCCredentialStore updatePIITokenInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:keystoreType:completion:]_block_invoke.36
+ ___131-[DCCredentialStore updatePIITokenInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:keystoreType:completion:]_block_invoke.cold.1
+ ___131-[DCCredentialStoreClient deletePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:credentialIdentifier:completion:]_block_invoke
+ ___131-[DCCredentialStoreClient deletePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:credentialIdentifier:completion:]_block_invoke_2
+ ___131-[DCCredentialStoreClient deletePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:credentialIdentifier:completion:]_block_invoke_2.cold.1
+ ___131-[DCCredentialStoreClient deletePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:credentialIdentifier:completion:]_block_invoke_2.cold.2
+ ___133-[DCCredentialStoreClient storePIIDataInSyncableKeyStoreForIdentifier:data:keystoreType:piiDataType:credentialIdentifier:completion:]_block_invoke
+ ___133-[DCCredentialStoreClient storePIIDataInSyncableKeyStoreForIdentifier:data:keystoreType:piiDataType:credentialIdentifier:completion:]_block_invoke_2
+ ___133-[DCCredentialStoreClient storePIIDataInSyncableKeyStoreForIdentifier:data:keystoreType:piiDataType:credentialIdentifier:completion:]_block_invoke_2.cold.1
+ ___133-[DCCredentialStoreClient storePIIDataInSyncableKeyStoreForIdentifier:data:keystoreType:piiDataType:credentialIdentifier:completion:]_block_invoke_2.cold.2
+ ___142-[DCCredentialStore updatePIIDataInSyncableKeyStoreForIdentifier:attributesToUpdate:keystoreType:piiDataType:credentialIdentifier:completion:]_block_invoke
+ ___142-[DCCredentialStore updatePIIDataInSyncableKeyStoreForIdentifier:attributesToUpdate:keystoreType:piiDataType:credentialIdentifier:completion:]_block_invoke.43
+ ___142-[DCCredentialStore updatePIIDataInSyncableKeyStoreForIdentifier:attributesToUpdate:keystoreType:piiDataType:credentialIdentifier:completion:]_block_invoke.cold.1
+ ___148-[DCCredentialStoreClient updatePIIDataInSyncableKeyStoreForIdentifier:attributesToUpdate:keystoreType:piiDataType:credentialIdentifier:completion:]_block_invoke
+ ___148-[DCCredentialStoreClient updatePIIDataInSyncableKeyStoreForIdentifier:attributesToUpdate:keystoreType:piiDataType:credentialIdentifier:completion:]_block_invoke_2
+ ___148-[DCCredentialStoreClient updatePIIDataInSyncableKeyStoreForIdentifier:attributesToUpdate:keystoreType:piiDataType:credentialIdentifier:completion:]_block_invoke_2.cold.1
+ ___148-[DCCredentialStoreClient updatePIIDataInSyncableKeyStoreForIdentifier:attributesToUpdate:keystoreType:piiDataType:credentialIdentifier:completion:]_block_invoke_2.cold.2
+ ___39-[DCBiometricStore getCASDCertificate:]_block_invoke
+ ___39-[DCBiometricStore getCASDCertificate:]_block_invoke_2
+ ___39-[DCBiometricStore getCASDCertificate:]_block_invoke_2.cold.1
+ ___39-[DCBiometricStore getCASDCertificate:]_block_invoke_2.cold.2
+ ___41-[DCBiometricStore bioBindingUnboundACL:]_block_invoke
+ ___41-[DCBiometricStore bioBindingUnboundACL:]_block_invoke_2
+ ___41-[DCBiometricStore bioBindingUnboundACL:]_block_invoke_2.cold.1
+ ___41-[DCBiometricStore bioBindingUnboundACL:]_block_invoke_2.cold.2
+ ___41-[DCBiometricStore bioBindingUnboundACL:]_block_invoke_2.cold.3
+ ___46-[DCBiometricStore boundAppletPresentmentACL:]_block_invoke
+ ___46-[DCBiometricStore boundAppletPresentmentACL:]_block_invoke_2
+ ___46-[DCBiometricStore boundAppletPresentmentACL:]_block_invoke_2.cold.1
+ ___46-[DCBiometricStore boundAppletPresentmentACL:]_block_invoke_2.cold.2
+ ___46-[DCBiometricStore passcodeBindingUnboundACL:]_block_invoke
+ ___46-[DCBiometricStore passcodeBindingUnboundACL:]_block_invoke_2
+ ___46-[DCBiometricStore passcodeBindingUnboundACL:]_block_invoke_2.cold.1
+ ___46-[DCBiometricStore passcodeBindingUnboundACL:]_block_invoke_2.cold.2
+ ___46-[DCBiometricStore passcodeBindingUnboundACL:]_block_invoke_2.cold.3
+ ___48-[DCBiometricStore globalAuthACLWithCompletion:]_block_invoke
+ ___48-[DCBiometricStore globalAuthACLWithCompletion:]_block_invoke_2
+ ___48-[DCBiometricStore globalAuthACLWithCompletion:]_block_invoke_2.cold.1
+ ___48-[DCBiometricStore globalAuthACLWithCompletion:]_block_invoke_2.cold.2
+ ___48-[DCBiometricStore globalAuthACLWithCompletion:]_block_invoke_2.cold.3
+ ___54-[DCBiometricStore establishPrearmTrustV2:completion:]_block_invoke
+ ___54-[DCBiometricStore establishPrearmTrustV2:completion:]_block_invoke_2
+ ___54-[DCBiometricStore establishPrearmTrustV2:completion:]_block_invoke_2.cold.1
+ ___54-[DCBiometricStore establishPrearmTrustV2:completion:]_block_invoke_2.cold.2
+ ___54-[DCBiometricStore establishPrearmTrustV2:completion:]_block_invoke_2.cold.3
+ ___54-[DCBiometricStore getGlobalProgenitorKeyAttestation:]_block_invoke
+ ___54-[DCBiometricStore getGlobalProgenitorKeyAttestation:]_block_invoke_2
+ ___54-[DCBiometricStore getGlobalProgenitorKeyAttestation:]_block_invoke_2.cold.1
+ ___54-[DCBiometricStore getGlobalProgenitorKeyAttestation:]_block_invoke_2.cold.2
+ ___54-[DCBiometricStore migratePrearmTrustBlob:completion:]_block_invoke
+ ___54-[DCBiometricStore migratePrearmTrustBlob:completion:]_block_invoke_2
+ ___54-[DCBiometricStore migratePrearmTrustBlob:completion:]_block_invoke_2.cold.1
+ ___54-[DCBiometricStore migratePrearmTrustBlob:completion:]_block_invoke_2.cold.2
+ ___55-[DCBiometricStore _remoteObjectProxyWithErrorHandler:]_block_invoke
+ ___55-[DCBiometricStore _remoteObjectProxyWithErrorHandler:]_block_invoke.cold.1
+ ___55-[DCBiometricStore globalPayloadAuthACLWithCompletion:]_block_invoke
+ ___55-[DCBiometricStore globalPayloadAuthACLWithCompletion:]_block_invoke_2
+ ___55-[DCBiometricStore globalPayloadAuthACLWithCompletion:]_block_invoke_2.cold.1
+ ___55-[DCBiometricStore globalPayloadAuthACLWithCompletion:]_block_invoke_2.cold.2
+ ___55-[DCBiometricStore globalPayloadAuthACLWithCompletion:]_block_invoke_2.cold.3
+ ___55-[DCBiometricStore revokeCredentialAuthorizationToken:]_block_invoke
+ ___55-[DCBiometricStore revokeCredentialAuthorizationToken:]_block_invoke.cold.1
+ ___55-[DCBiometricStore revokeCredentialAuthorizationToken:]_block_invoke.cold.2
+ ___55-[DCBiometricStore revokeCredentialAuthorizationToken:]_block_invoke.cold.3
+ ___55-[DCBiometricStore setGlobalAuthACL:ofType:completion:]_block_invoke
+ ___55-[DCBiometricStore setGlobalAuthACL:ofType:completion:]_block_invoke.cold.1
+ ___55-[DCBiometricStore setGlobalAuthACL:ofType:completion:]_block_invoke.cold.2
+ ___55-[DCBiometricStore setGlobalAuthACL:ofType:completion:]_block_invoke.cold.3
+ ___56-[DCBiometricStore credentialAuthenticationTokenStatus:]_block_invoke
+ ___56-[DCBiometricStore credentialAuthenticationTokenStatus:]_block_invoke_2
+ ___56-[DCBiometricStore credentialAuthenticationTokenStatus:]_block_invoke_2.cold.1
+ ___56-[DCBiometricStore credentialAuthenticationTokenStatus:]_block_invoke_2.cold.2
+ ___59-[DCCredentialProperties setElementIdentifiersByNamespace:]_block_invoke
+ ___61-[DCBiometricStore deleteGlobalAuthACLWithOutcomeCompletion:]_block_invoke
+ ___61-[DCBiometricStore deleteGlobalAuthACLWithOutcomeCompletion:]_block_invoke_2
+ ___61-[DCBiometricStore deleteGlobalAuthACLWithOutcomeCompletion:]_block_invoke_2.cold.1
+ ___61-[DCBiometricStore deleteGlobalAuthACLWithOutcomeCompletion:]_block_invoke_2.cold.2
+ ___61-[DCBiometricStore deleteGlobalAuthACLWithOutcomeCompletion:]_block_invoke_2.cold.3
+ ___61-[DCBiometricStore nonceForAuthorizationTokenWithCompletion:]_block_invoke
+ ___61-[DCBiometricStore nonceForAuthorizationTokenWithCompletion:]_block_invoke_2
+ ___61-[DCBiometricStore nonceForAuthorizationTokenWithCompletion:]_block_invoke_2.cold.1
+ ___61-[DCBiometricStore nonceForAuthorizationTokenWithCompletion:]_block_invoke_2.cold.2
+ ___61-[DCBiometricStore nonceForAuthorizationTokenWithCompletion:]_block_invoke_2.cold.3
+ ___64-[DCBiometricStore getGlobalThirdPartyProgenitorKeyAttestation:]_block_invoke
+ ___64-[DCBiometricStore getGlobalThirdPartyProgenitorKeyAttestation:]_block_invoke_2
+ ___64-[DCBiometricStore getGlobalThirdPartyProgenitorKeyAttestation:]_block_invoke_2.cold.1
+ ___64-[DCBiometricStore getGlobalThirdPartyProgenitorKeyAttestation:]_block_invoke_2.cold.2
+ ___64-[DCCredentialStore(DebugAPIs) eraseLegacySEKeySlot:completion:]_block_invoke.282
+ ___64-[DCCredentialStore(DebugAPIs) keyInfoForCredential:completion:]_block_invoke.284
+ ___64-[DCCredentialStore(DebugAPIs) payloadsOfCredential:completion:]_block_invoke.279
+ ___65-[DCBiometricStore clearProgenitorKeyDesignationsWithCompletion:]_block_invoke
+ ___65-[DCBiometricStore clearProgenitorKeyDesignationsWithCompletion:]_block_invoke_2
+ ___65-[DCBiometricStore clearProgenitorKeyDesignationsWithCompletion:]_block_invoke_2.cold.1
+ ___65-[DCBiometricStore clearProgenitorKeyDesignationsWithCompletion:]_block_invoke_2.cold.2
+ ___65-[DCCredentialStore isPIITokenAvailableForIdentifier:completion:]_block_invoke.44
+ ___70-[DCBiometricStore prearmCredentialWithAuthorizationToken:completion:]_block_invoke
+ ___70-[DCBiometricStore prearmCredentialWithAuthorizationToken:completion:]_block_invoke.cold.1
+ ___70-[DCBiometricStore prearmCredentialWithAuthorizationToken:completion:]_block_invoke.cold.2
+ ___70-[DCBiometricStore prearmCredentialWithAuthorizationToken:completion:]_block_invoke.cold.3
+ ___71-[DCCredentialStore(DebugAPIs) occupiedLegacySEKeySlotsWithCompletion:]_block_invoke.281
+ ___76-[DCCredentialStore(DebugAPIs) allElementsOfCredential:authData:completion:]_block_invoke.280
+ ___77-[DCBiometricStore generatePhoneTokenWithNonce:keyBlob:pairingID:completion:]_block_invoke
+ ___77-[DCBiometricStore generatePhoneTokenWithNonce:keyBlob:pairingID:completion:]_block_invoke_2
+ ___77-[DCBiometricStore generatePhoneTokenWithNonce:keyBlob:pairingID:completion:]_block_invoke_2.cold.1
+ ___77-[DCBiometricStore generatePhoneTokenWithNonce:keyBlob:pairingID:completion:]_block_invoke_2.cold.2
+ ___77-[DCBiometricStore generatePhoneTokenWithNonce:keyBlob:pairingID:completion:]_block_invoke_2.cold.3
+ ___78-[DCBiometricStore setModifiedGlobalAuthACL:externalizedLAContext:completion:]_block_invoke
+ ___78-[DCBiometricStore setModifiedGlobalAuthACL:externalizedLAContext:completion:]_block_invoke_2
+ ___78-[DCBiometricStore setModifiedGlobalAuthACL:externalizedLAContext:completion:]_block_invoke_2.cold.1
+ ___78-[DCBiometricStore setModifiedGlobalAuthACL:externalizedLAContext:completion:]_block_invoke_2.cold.2
+ ___78-[DCBiometricStore setModifiedGlobalAuthACL:externalizedLAContext:completion:]_block_invoke_2.cold.3
+ ___79-[DCBiometricStore globalAuthACLTemplateUUIDsAndCredentialCountWithCompletion:]_block_invoke
+ ___79-[DCBiometricStore globalAuthACLTemplateUUIDsAndCredentialCountWithCompletion:]_block_invoke_2
+ ___79-[DCBiometricStore globalAuthACLTemplateUUIDsAndCredentialCountWithCompletion:]_block_invoke_2.cold.1
+ ___79-[DCBiometricStore globalAuthACLTemplateUUIDsAndCredentialCountWithCompletion:]_block_invoke_2.cold.2
+ ___79-[DCBiometricStore globalAuthACLTemplateUUIDsAndCredentialCountWithCompletion:]_block_invoke_2.cold.3
+ ___81-[DCBiometricStore generatePrearmTrustCertificateWithNonce:pairingID:completion:]_block_invoke
+ ___81-[DCBiometricStore generatePrearmTrustCertificateWithNonce:pairingID:completion:]_block_invoke_2
+ ___81-[DCBiometricStore generatePrearmTrustCertificateWithNonce:pairingID:completion:]_block_invoke_2.cold.1
+ ___81-[DCBiometricStore generatePrearmTrustCertificateWithNonce:pairingID:completion:]_block_invoke_2.cold.2
+ ___81-[DCCredentialStore(DebugAPIs) clearPresentmentKeyUsageForCredential:completion:]_block_invoke.283
+ ___83-[DCCredentialStore retrieveAllItemsFromSyncableKeyStoreForItemService:completion:]_block_invoke
+ ___83-[DCCredentialStore retrieveAllItemsFromSyncableKeyStoreForItemService:completion:]_block_invoke.45
+ ___83-[DCCredentialStore retrieveAllItemsFromSyncableKeyStoreForItemService:completion:]_block_invoke.cold.1
+ ___89-[DCBiometricStore generatePrearmTrustCertificateFromKeyBlob:nonce:pairingID:completion:]_block_invoke
+ ___89-[DCBiometricStore generatePrearmTrustCertificateFromKeyBlob:nonce:pairingID:completion:]_block_invoke_2
+ ___89-[DCBiometricStore generatePrearmTrustCertificateFromKeyBlob:nonce:pairingID:completion:]_block_invoke_2.cold.1
+ ___89-[DCBiometricStore generatePrearmTrustCertificateFromKeyBlob:nonce:pairingID:completion:]_block_invoke_2.cold.2
+ ___89-[DCCredentialStoreClient retrieveAllItemsFromSyncableKeyStoreForItemService:completion:]_block_invoke
+ ___89-[DCCredentialStoreClient retrieveAllItemsFromSyncableKeyStoreForItemService:completion:]_block_invoke_2
+ ___89-[DCCredentialStoreClient retrieveAllItemsFromSyncableKeyStoreForItemService:completion:]_block_invoke_2.cold.1
+ ___89-[DCCredentialStoreClient retrieveAllItemsFromSyncableKeyStoreForItemService:completion:]_block_invoke_2.cold.2
+ ___92-[DCCredentialStore deletePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]_block_invoke.39
+ ___94-[DCCredentialStore retrievePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]_block_invoke.38
+ ___94-[DCCredentialStore storePIIHashInSyncableKeyStoreForIdentifier:data:keystoreType:completion:]_block_invoke.37
+ ___block_descriptor_72_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.230
+ ___swift__destructor
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.10
+ ___swift_closure_destructor.106
+ ___swift_closure_destructor.10Tm
+ ___swift_closure_destructor.110
+ ___swift_closure_destructor.115
+ ___swift_closure_destructor.120
+ ___swift_closure_destructor.126
+ ___swift_closure_destructor.132
+ ___swift_closure_destructor.14
+ ___swift_closure_destructor.144
+ ___swift_closure_destructor.148
+ ___swift_closure_destructor.153
+ ___swift_closure_destructor.158
+ ___swift_closure_destructor.167
+ ___swift_closure_destructor.171
+ ___swift_closure_destructor.176
+ ___swift_closure_destructor.18
+ ___swift_closure_destructor.181
+ ___swift_closure_destructor.190
+ ___swift_closure_destructor.194
+ ___swift_closure_destructor.199
+ ___swift_closure_destructor.204
+ ___swift_closure_destructor.216
+ ___swift_closure_destructor.22
+ ___swift_closure_destructor.222
+ ___swift_closure_destructor.30
+ ___swift_closure_destructor.30Tm
+ ___swift_closure_destructor.36
+ ___swift_closure_destructor.42
+ ___swift_closure_destructor.42Tm
+ ___swift_closure_destructor.47
+ ___swift_closure_destructor.6
+ ___swift_closure_destructor.60
+ ___swift_closure_destructor.64
+ ___swift_closure_destructor.69
+ ___swift_closure_destructor.6Tm
+ ___swift_closure_destructor.74
+ ___swift_closure_destructor.83
+ ___swift_closure_destructor.83Tm
+ ___swift_closure_destructor.87
+ ___swift_closure_destructor.92
+ ___swift_closure_destructor.97
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_CoreIDCred
+ __swift_stdlib_malloc_size
+ _associated conformance So19SecAccessControlRefa14CoreFoundation9_CFObjectSCSH
+ _associated conformance So19SecAccessControlRefaSHSCSQ
+ _associated conformance So23DCCredentialAuthACLTypeVSHSCSQ
+ _block_copy_helper.139
+ _block_copy_helper.162
+ _block_copy_helper.185
+ _block_copy_helper.208
+ _block_copy_helper.229
+ _block_descriptor.141
+ _block_descriptor.164
+ _block_descriptor.187
+ _block_descriptor.210
+ _block_descriptor.231
+ _block_destroy_helper.140
+ _block_destroy_helper.163
+ _block_destroy_helper.186
+ _block_destroy_helper.209
+ _block_destroy_helper.230
+ _kRequiresFirstPartyInAppPresentment
+ _malloc_size
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_remoteObjectProxyWithErrorHandler:
+ _objc_msgSend$_underlyingCodableValue
+ _objc_msgSend$accessControl
+ _objc_msgSend$aclType
+ _objc_msgSend$connection
+ _objc_msgSend$deletePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:credentialIdentifier:completion:
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$globalAuthACLTemplateUUIDsAndCredentialCountWithCompletion:
+ _objc_msgSend$globalPayloadAuthACLWithCompletion:
+ _objc_msgSend$initWithAccessControl:type:
+ _objc_msgSend$initWithElementIdentifier:
+ _objc_msgSend$initWithIdentifier:credentialIdentifier:publicKey:publicKeyIdentifier:keyType:keyUsage:createdAt:updatedAt:presentmentKeyTimesUsed:acl:
+ _objc_msgSend$retrieveAllItemsFromSyncableKeyStoreForItemService:completion:
+ _objc_msgSend$retrievePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:completion:
+ _objc_msgSend$retrievePIITokenFromSyncableKeyStoreForIdentifier:keystoreType:credentialIdentifier:completion:
+ _objc_msgSend$setConnection:
+ _objc_msgSend$setRequiresFirstPartyInAppPresentment:
+ _objc_msgSend$storePIIDataInSyncableKeyStoreForIdentifier:data:keystoreType:piiDataType:credentialIdentifier:completion:
+ _objc_msgSend$storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:keystoreType:completion:
+ _objc_msgSend$updatePIIDataInSyncableKeyStoreForIdentifier:attributesToUpdate:keystoreType:piiDataType:credentialIdentifier:completion:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x7
+ _swift_arrayInitWithCopy
+ _swift_endAccess
+ _swift_getObjCClassFromObject
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x27
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x27
+ _swift_retain_x8
+ _swift_task_future_wait_throwing
+ _symbolic SS18merchantIdentifier_Sb12isFirstPartyt
+ _symbolic _____Sg 10Foundation14DateComponentsV
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic _____Sg 13CoreIDVShared10AnyCodableO
+ _symbolic _____Sg 13CoreIDVShared8ISO23220O9BirthDateV
+ _symbolic _____m 13CoreIDVShared10AnyCodableO
+ _symbolic _____y______pG s23_ContiguousArrayStorageC s7CVarArgP
+ _symbolic _____y_____ypG s18_DictionaryStorageC s11AnyHashableV
+ _symbolic yp
- +[DCCredentialAuthACL supportsSecureCoding]
- +[DCCredentialCryptoKeyInfo supportsSecureCoding]
- +[DCCredentialElement supportsSecureCoding]
- -[DCBiometricStore client]
- -[DCBiometricStoreClient .cxx_destruct]
- -[DCBiometricStoreClient bioBindingUnboundACL:]
- -[DCBiometricStoreClient bioBindingUnboundACL:].cold.1
- -[DCBiometricStoreClient boundAppletPresentmentACL:]
- -[DCBiometricStoreClient boundAppletPresentmentACL:].cold.1
- -[DCBiometricStoreClient clearProgenitorKeyDesignationsWithCompletion:]
- -[DCBiometricStoreClient clearProgenitorKeyDesignationsWithCompletion:].cold.1
- -[DCBiometricStoreClient createDaemonDisconnectedError]
- -[DCBiometricStoreClient credentialAuthenticationTokenStatus:]
- -[DCBiometricStoreClient credentialAuthenticationTokenStatus:].cold.1
- -[DCBiometricStoreClient dealloc]
- -[DCBiometricStoreClient dealloc].cold.1
- -[DCBiometricStoreClient deleteGlobalAuthACLWithCompletion:]
- -[DCBiometricStoreClient deleteGlobalAuthACLWithCompletion:].cold.1
- -[DCBiometricStoreClient establishPrearmTrustV2:completion:]
- -[DCBiometricStoreClient establishPrearmTrustV2:completion:].cold.1
- -[DCBiometricStoreClient generatePhoneTokenWithNonce:keyBlob:pairingID:completion:]
- -[DCBiometricStoreClient generatePhoneTokenWithNonce:keyBlob:pairingID:completion:].cold.1
- -[DCBiometricStoreClient generatePrearmTrustCertificateFromKeyBlob:nonce:pairingID:completion:]
- -[DCBiometricStoreClient generatePrearmTrustCertificateFromKeyBlob:nonce:pairingID:completion:].cold.1
- -[DCBiometricStoreClient generatePrearmTrustCertificateWithNonce:pairingID:completion:]
- -[DCBiometricStoreClient generatePrearmTrustCertificateWithNonce:pairingID:completion:].cold.1
- -[DCBiometricStoreClient getCASDCertificate:]
- -[DCBiometricStoreClient getCASDCertificate:].cold.1
- -[DCBiometricStoreClient getGlobalProgenitorKeyAttestation:]
- -[DCBiometricStoreClient getGlobalProgenitorKeyAttestation:].cold.1
- -[DCBiometricStoreClient getGlobalThirdPartyProgenitorKeyAttestation:]
- -[DCBiometricStoreClient getGlobalThirdPartyProgenitorKeyAttestation:].cold.1
- -[DCBiometricStoreClient globalAuthACLTemplateUUIDsWithCompletion:]
- -[DCBiometricStoreClient globalAuthACLTemplateUUIDsWithCompletion:].cold.1
- -[DCBiometricStoreClient globalAuthACLWithCompletion:]
- -[DCBiometricStoreClient globalAuthACLWithCompletion:].cold.1
- -[DCBiometricStoreClient init]
- -[DCBiometricStoreClient init].cold.1
- -[DCBiometricStoreClient init].cold.2
- -[DCBiometricStoreClient invalidate]
- -[DCBiometricStoreClient invalidate].cold.1
- -[DCBiometricStoreClient migratePrearmTrustBlob:completion:]
- -[DCBiometricStoreClient migratePrearmTrustBlob:completion:].cold.1
- -[DCBiometricStoreClient nonceForAuthorizationTokenWithCompletion:]
- -[DCBiometricStoreClient nonceForAuthorizationTokenWithCompletion:].cold.1
- -[DCBiometricStoreClient passcodeBindingUnboundACL:]
- -[DCBiometricStoreClient passcodeBindingUnboundACL:].cold.1
- -[DCBiometricStoreClient prearmCredentialWithAuthorizationToken:completion:]
- -[DCBiometricStoreClient prearmCredentialWithAuthorizationToken:completion:].cold.1
- -[DCBiometricStoreClient refreshProgenitorKeyDesignationsWithSessionHandoffToken:onlyIfNeeded:completion:]
- -[DCBiometricStoreClient refreshProgenitorKeyDesignationsWithSessionHandoffToken:onlyIfNeeded:completion:].cold.1
- -[DCBiometricStoreClient remoteObjectProxyWithErrorHandler:]
- -[DCBiometricStoreClient revokeCredentialAuthorizationToken:]
- -[DCBiometricStoreClient revokeCredentialAuthorizationToken:].cold.1
- -[DCBiometricStoreClient serverConnection]
- -[DCBiometricStoreClient setGlobalAuthACL:ofType:completion:]
- -[DCBiometricStoreClient setGlobalAuthACL:ofType:completion:].cold.1
- -[DCBiometricStoreClient setModifiedGlobalAuthACL:externalizedLAContext:completion:]
- -[DCBiometricStoreClient setModifiedGlobalAuthACL:externalizedLAContext:completion:].cold.1
- -[DCBiometricStoreClient setServerConnection:]
- -[DCCredentialAuthACL .cxx_destruct]
- -[DCCredentialAuthACL aclData]
- -[DCCredentialAuthACL aclType]
- -[DCCredentialAuthACL encodeWithCoder:]
- -[DCCredentialAuthACL initWithCoder:]
- -[DCCredentialAuthACL initWithData:type:]
- -[DCCredentialAuthACL setAclData:]
- -[DCCredentialAuthACL setAclType:]
- -[DCCredentialCryptoKeyInfo .cxx_destruct]
- -[DCCredentialCryptoKeyInfo acl]
- -[DCCredentialCryptoKeyInfo createdAt]
- -[DCCredentialCryptoKeyInfo credentialIdentifier]
- -[DCCredentialCryptoKeyInfo encodeWithCoder:]
- -[DCCredentialCryptoKeyInfo identifier]
- -[DCCredentialCryptoKeyInfo initWithCoder:]
- -[DCCredentialCryptoKeyInfo initWithIdentifier:credentialIdentifier:publicKey:publicKeyIdentifier:keyType:keyUsage:createdAt:updatedAt:presentmentKeyTimesUsed:acl:]
- -[DCCredentialCryptoKeyInfo keyType]
- -[DCCredentialCryptoKeyInfo keyUsage]
- -[DCCredentialCryptoKeyInfo presentmentKeyTimesUsed]
- -[DCCredentialCryptoKeyInfo publicKeyIdentifier]
- -[DCCredentialCryptoKeyInfo publicKey]
- -[DCCredentialCryptoKeyInfo updatedAt]
- -[DCCredentialElement .cxx_destruct]
- -[DCCredentialElement arrayValue]
- -[DCCredentialElement birthDateValue]
- -[DCCredentialElement dataValue]
- -[DCCredentialElement dateValue]
- -[DCCredentialElement description]
- -[DCCredentialElement dictionaryValue]
- -[DCCredentialElement elementIdentifier]
- -[DCCredentialElement encodeWithCoder:]
- -[DCCredentialElement initWithCoder:]
- -[DCCredentialElement initWithElementIdentifier:]
- -[DCCredentialElement initWithElementIdentifier:arrayValue:]
- -[DCCredentialElement initWithElementIdentifier:birthDateValue:]
- -[DCCredentialElement initWithElementIdentifier:boolValue:]
- -[DCCredentialElement initWithElementIdentifier:dataValue:]
- -[DCCredentialElement initWithElementIdentifier:dateValue:]
- -[DCCredentialElement initWithElementIdentifier:dictionaryValue:]
- -[DCCredentialElement initWithElementIdentifier:doubleValue:]
- -[DCCredentialElement initWithElementIdentifier:intValue:]
- -[DCCredentialElement initWithElementIdentifier:stringValue:]
- -[DCCredentialElement initWithElementIdentifier:stringValue:dataValue:dateValue:birthDateValue:numberValue:arrayValue:dictionaryValue:numericTypeHint:]
- -[DCCredentialElement numberValue]
- -[DCCredentialElement numericTypeHint]
- -[DCCredentialElement stringValue]
- -[DCCredentialStore deleteDataFromSyncableKeyStoreForIdentifier:completion:]
- -[DCCredentialStore retrieveDataFromSyncableKeyStoreForIdentifier:completion:]
- -[DCCredentialStore storeDataInSyncableKeyStoreForIdentifier:data:completion:]
- -[DCCredentialStore storeDataInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:]
- -[DCCredentialStore updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:]
- -[DCCredentialStoreClient deletePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]
- -[DCCredentialStoreClient deletePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:].cold.1
- -[DCCredentialStoreClient deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:completion:]
- -[DCCredentialStoreClient deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:completion:].cold.1
- -[DCCredentialStoreClient retrievePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]
- -[DCCredentialStoreClient retrievePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:].cold.1
- -[DCCredentialStoreClient retrievePIITokenFromSyncableKeyStoreForIdentifier:completion:]
- -[DCCredentialStoreClient retrievePIITokenFromSyncableKeyStoreForIdentifier:completion:].cold.1
- -[DCCredentialStoreClient storePIIHashInSyncableKeyStoreForIdentifier:data:keystoreType:completion:]
- -[DCCredentialStoreClient storePIIHashInSyncableKeyStoreForIdentifier:data:keystoreType:completion:].cold.1
- -[DCCredentialStoreClient storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:]
- -[DCCredentialStoreClient storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:].cold.1
- -[DCCredentialStoreClient updatePIITokenInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:]
- -[DCCredentialStoreClient updatePIITokenInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:].cold.1
- _OBJC_CLASS_$_DCBiometricStoreClient
- _OBJC_CLASS_$_NSDateComponents
- _OBJC_IVAR_$_DCBiometricStore._client
- _OBJC_IVAR_$_DCBiometricStoreClient._serverConnection
- _OBJC_IVAR_$_DCCredentialAuthACL._aclData
- _OBJC_IVAR_$_DCCredentialAuthACL._aclType
- _OBJC_IVAR_$_DCCredentialAuthACL._lock
- _OBJC_IVAR_$_DCCredentialCryptoKeyInfo._acl
- _OBJC_IVAR_$_DCCredentialCryptoKeyInfo._createdAt
- _OBJC_IVAR_$_DCCredentialCryptoKeyInfo._credentialIdentifier
- _OBJC_IVAR_$_DCCredentialCryptoKeyInfo._identifier
- _OBJC_IVAR_$_DCCredentialCryptoKeyInfo._keyType
- _OBJC_IVAR_$_DCCredentialCryptoKeyInfo._keyUsage
- _OBJC_IVAR_$_DCCredentialCryptoKeyInfo._presentmentKeyTimesUsed
- _OBJC_IVAR_$_DCCredentialCryptoKeyInfo._publicKey
- _OBJC_IVAR_$_DCCredentialCryptoKeyInfo._publicKeyIdentifier
- _OBJC_IVAR_$_DCCredentialCryptoKeyInfo._updatedAt
- _OBJC_IVAR_$_DCCredentialElement._arrayValue
- _OBJC_IVAR_$_DCCredentialElement._birthDateValue
- _OBJC_IVAR_$_DCCredentialElement._dataValue
- _OBJC_IVAR_$_DCCredentialElement._dateValue
- _OBJC_IVAR_$_DCCredentialElement._dictionaryValue
- _OBJC_IVAR_$_DCCredentialElement._elementIdentifier
- _OBJC_IVAR_$_DCCredentialElement._numberValue
- _OBJC_IVAR_$_DCCredentialElement._numericTypeHint
- _OBJC_IVAR_$_DCCredentialElement._stringValue
- _OBJC_METACLASS_$_DCBiometricStoreClient
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- __OBJC_$_CLASS_METHODS_DCCredentialAuthACL
- __OBJC_$_CLASS_METHODS_DCCredentialCryptoKeyInfo
- __OBJC_$_CLASS_METHODS_DCCredentialElement
- __OBJC_$_CLASS_PROP_LIST_DCCredentialAuthACL
- __OBJC_$_CLASS_PROP_LIST_DCCredentialCryptoKeyInfo
- __OBJC_$_CLASS_PROP_LIST_DCCredentialElement
- __OBJC_$_INSTANCE_METHODS_DCBiometricStoreClient
- __OBJC_$_INSTANCE_METHODS_DCCredentialAuthACL
- __OBJC_$_INSTANCE_METHODS_DCCredentialCryptoKeyInfo
- __OBJC_$_INSTANCE_METHODS_DCCredentialElement
- __OBJC_$_INSTANCE_VARIABLES_DCBiometricStoreClient
- __OBJC_$_INSTANCE_VARIABLES_DCCredentialAuthACL
- __OBJC_$_INSTANCE_VARIABLES_DCCredentialCryptoKeyInfo
- __OBJC_$_INSTANCE_VARIABLES_DCCredentialElement
- __OBJC_$_PROP_LIST_DCBiometricStoreClient
- __OBJC_$_PROP_LIST_DCCredentialAuthACL
- __OBJC_$_PROP_LIST_DCCredentialCryptoKeyInfo
- __OBJC_$_PROP_LIST_DCCredentialElement
- __OBJC_CLASS_PROTOCOLS_$_DCBiometricStoreClient
- __OBJC_CLASS_PROTOCOLS_$_DCCredentialAuthACL
- __OBJC_CLASS_PROTOCOLS_$_DCCredentialCryptoKeyInfo
- __OBJC_CLASS_PROTOCOLS_$_DCCredentialElement
- __OBJC_CLASS_RO_$_DCBiometricStoreClient
- __OBJC_CLASS_RO_$_DCCredentialAuthACL
- __OBJC_CLASS_RO_$_DCCredentialCryptoKeyInfo
- __OBJC_CLASS_RO_$_DCCredentialElement
- __OBJC_METACLASS_RO_$_DCBiometricStoreClient
- __OBJC_METACLASS_RO_$_DCCredentialAuthACL
- __OBJC_METACLASS_RO_$_DCCredentialCryptoKeyInfo
- __OBJC_METACLASS_RO_$_DCCredentialElement
- __PROTOCOLS_DCPresentmentRequest.31
- __PROTOCOLS_DCPresentmentRequestedElement.19
- ___100-[DCCredentialStoreClient retrievePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]_block_invoke
- ___100-[DCCredentialStoreClient retrievePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]_block_invoke_2
- ___100-[DCCredentialStoreClient retrievePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]_block_invoke_2.cold.1
- ___100-[DCCredentialStoreClient retrievePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]_block_invoke_2.cold.2
- ___100-[DCCredentialStoreClient storePIIHashInSyncableKeyStoreForIdentifier:data:keystoreType:completion:]_block_invoke
- ___100-[DCCredentialStoreClient storePIIHashInSyncableKeyStoreForIdentifier:data:keystoreType:completion:]_block_invoke_2
- ___100-[DCCredentialStoreClient storePIIHashInSyncableKeyStoreForIdentifier:data:keystoreType:completion:]_block_invoke_2.cold.1
- ___100-[DCCredentialStoreClient storePIIHashInSyncableKeyStoreForIdentifier:data:keystoreType:completion:]_block_invoke_2.cold.2
- ___101-[DCCredentialStore deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:completion:]_block_invoke.43
- ___103-[DCCredentialStore storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:]_block_invoke
- ___103-[DCCredentialStore storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:]_block_invoke.41
- ___103-[DCCredentialStore storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:]_block_invoke.cold.1
- ___106-[DCBiometricStoreClient refreshProgenitorKeyDesignationsWithSessionHandoffToken:onlyIfNeeded:completion:]_block_invoke
- ___106-[DCBiometricStoreClient refreshProgenitorKeyDesignationsWithSessionHandoffToken:onlyIfNeeded:completion:]_block_invoke_2
- ___106-[DCBiometricStoreClient refreshProgenitorKeyDesignationsWithSessionHandoffToken:onlyIfNeeded:completion:]_block_invoke_2.cold.1
- ___106-[DCBiometricStoreClient refreshProgenitorKeyDesignationsWithSessionHandoffToken:onlyIfNeeded:completion:]_block_invoke_2.cold.2
- ___107-[DCCredentialStoreClient deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:completion:]_block_invoke
- ___107-[DCCredentialStoreClient deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:completion:]_block_invoke_2
- ___107-[DCCredentialStoreClient deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:completion:]_block_invoke_2.cold.1
- ___107-[DCCredentialStoreClient deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:completion:]_block_invoke_2.cold.2
- ___109-[DCCredentialStoreClient storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:]_block_invoke
- ___109-[DCCredentialStoreClient storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:]_block_invoke_2
- ___109-[DCCredentialStoreClient storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:]_block_invoke_2.cold.1
- ___109-[DCCredentialStoreClient storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:]_block_invoke_2.cold.2
- ___114-[DCCredentialStore updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:]_block_invoke
- ___114-[DCCredentialStore updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:]_block_invoke.40
- ___114-[DCCredentialStore updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:]_block_invoke.cold.1
- ___118-[DCCredentialStore updatePIITokenInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:]_block_invoke.44
- ___124-[DCCredentialStoreClient updatePIITokenInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:]_block_invoke
- ___124-[DCCredentialStoreClient updatePIITokenInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:]_block_invoke_2
- ___124-[DCCredentialStoreClient updatePIITokenInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:]_block_invoke_2.cold.1
- ___124-[DCCredentialStoreClient updatePIITokenInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:]_block_invoke_2.cold.2
- ___45-[DCBiometricStoreClient getCASDCertificate:]_block_invoke
- ___45-[DCBiometricStoreClient getCASDCertificate:]_block_invoke_2
- ___45-[DCBiometricStoreClient getCASDCertificate:]_block_invoke_2.cold.1
- ___45-[DCBiometricStoreClient getCASDCertificate:]_block_invoke_2.cold.2
- ___47-[DCBiometricStoreClient bioBindingUnboundACL:]_block_invoke
- ___47-[DCBiometricStoreClient bioBindingUnboundACL:]_block_invoke_2
- ___47-[DCBiometricStoreClient bioBindingUnboundACL:]_block_invoke_2.cold.1
- ___47-[DCBiometricStoreClient bioBindingUnboundACL:]_block_invoke_2.cold.2
- ___47-[DCBiometricStoreClient bioBindingUnboundACL:]_block_invoke_2.cold.3
- ___52-[DCBiometricStoreClient boundAppletPresentmentACL:]_block_invoke
- ___52-[DCBiometricStoreClient boundAppletPresentmentACL:]_block_invoke_2
- ___52-[DCBiometricStoreClient boundAppletPresentmentACL:]_block_invoke_2.cold.1
- ___52-[DCBiometricStoreClient boundAppletPresentmentACL:]_block_invoke_2.cold.2
- ___52-[DCBiometricStoreClient passcodeBindingUnboundACL:]_block_invoke
- ___52-[DCBiometricStoreClient passcodeBindingUnboundACL:]_block_invoke_2
- ___52-[DCBiometricStoreClient passcodeBindingUnboundACL:]_block_invoke_2.cold.1
- ___52-[DCBiometricStoreClient passcodeBindingUnboundACL:]_block_invoke_2.cold.2
- ___52-[DCBiometricStoreClient passcodeBindingUnboundACL:]_block_invoke_2.cold.3
- ___54-[DCBiometricStoreClient globalAuthACLWithCompletion:]_block_invoke
- ___54-[DCBiometricStoreClient globalAuthACLWithCompletion:]_block_invoke_2
- ___54-[DCBiometricStoreClient globalAuthACLWithCompletion:]_block_invoke_2.cold.1
- ___54-[DCBiometricStoreClient globalAuthACLWithCompletion:]_block_invoke_2.cold.2
- ___54-[DCBiometricStoreClient globalAuthACLWithCompletion:]_block_invoke_2.cold.3
- ___60-[DCBiometricStoreClient deleteGlobalAuthACLWithCompletion:]_block_invoke
- ___60-[DCBiometricStoreClient deleteGlobalAuthACLWithCompletion:]_block_invoke_2
- ___60-[DCBiometricStoreClient deleteGlobalAuthACLWithCompletion:]_block_invoke_2.cold.1
- ___60-[DCBiometricStoreClient deleteGlobalAuthACLWithCompletion:]_block_invoke_2.cold.2
- ___60-[DCBiometricStoreClient deleteGlobalAuthACLWithCompletion:]_block_invoke_2.cold.3
- ___60-[DCBiometricStoreClient establishPrearmTrustV2:completion:]_block_invoke
- ___60-[DCBiometricStoreClient establishPrearmTrustV2:completion:]_block_invoke_2
- ___60-[DCBiometricStoreClient establishPrearmTrustV2:completion:]_block_invoke_2.cold.1
- ___60-[DCBiometricStoreClient establishPrearmTrustV2:completion:]_block_invoke_2.cold.2
- ___60-[DCBiometricStoreClient establishPrearmTrustV2:completion:]_block_invoke_2.cold.3
- ___60-[DCBiometricStoreClient getGlobalProgenitorKeyAttestation:]_block_invoke
- ___60-[DCBiometricStoreClient getGlobalProgenitorKeyAttestation:]_block_invoke_2
- ___60-[DCBiometricStoreClient getGlobalProgenitorKeyAttestation:]_block_invoke_2.cold.1
- ___60-[DCBiometricStoreClient getGlobalProgenitorKeyAttestation:]_block_invoke_2.cold.2
- ___60-[DCBiometricStoreClient migratePrearmTrustBlob:completion:]_block_invoke
- ___60-[DCBiometricStoreClient migratePrearmTrustBlob:completion:]_block_invoke_2
- ___60-[DCBiometricStoreClient migratePrearmTrustBlob:completion:]_block_invoke_2.cold.1
- ___60-[DCBiometricStoreClient migratePrearmTrustBlob:completion:]_block_invoke_2.cold.2
- ___60-[DCBiometricStoreClient remoteObjectProxyWithErrorHandler:]_block_invoke
- ___60-[DCBiometricStoreClient remoteObjectProxyWithErrorHandler:]_block_invoke.cold.1
- ___61-[DCBiometricStoreClient revokeCredentialAuthorizationToken:]_block_invoke
- ___61-[DCBiometricStoreClient revokeCredentialAuthorizationToken:]_block_invoke.cold.1
- ___61-[DCBiometricStoreClient revokeCredentialAuthorizationToken:]_block_invoke.cold.2
- ___61-[DCBiometricStoreClient revokeCredentialAuthorizationToken:]_block_invoke.cold.3
- ___61-[DCBiometricStoreClient setGlobalAuthACL:ofType:completion:]_block_invoke
- ___61-[DCBiometricStoreClient setGlobalAuthACL:ofType:completion:]_block_invoke.cold.1
- ___61-[DCBiometricStoreClient setGlobalAuthACL:ofType:completion:]_block_invoke.cold.2
- ___61-[DCBiometricStoreClient setGlobalAuthACL:ofType:completion:]_block_invoke.cold.3
- ___62-[DCBiometricStoreClient credentialAuthenticationTokenStatus:]_block_invoke
- ___62-[DCBiometricStoreClient credentialAuthenticationTokenStatus:]_block_invoke_2
- ___62-[DCBiometricStoreClient credentialAuthenticationTokenStatus:]_block_invoke_2.cold.1
- ___62-[DCBiometricStoreClient credentialAuthenticationTokenStatus:]_block_invoke_2.cold.2
- ___64-[DCCredentialStore(DebugAPIs) eraseLegacySEKeySlot:completion:]_block_invoke.277
- ___64-[DCCredentialStore(DebugAPIs) keyInfoForCredential:completion:]_block_invoke.279
- ___64-[DCCredentialStore(DebugAPIs) payloadsOfCredential:completion:]_block_invoke.274
- ___65-[DCCredentialStore isPIITokenAvailableForIdentifier:completion:]_block_invoke.48
- ___67-[DCBiometricStoreClient globalAuthACLTemplateUUIDsWithCompletion:]_block_invoke
- ___67-[DCBiometricStoreClient globalAuthACLTemplateUUIDsWithCompletion:]_block_invoke_2
- ___67-[DCBiometricStoreClient globalAuthACLTemplateUUIDsWithCompletion:]_block_invoke_2.cold.1
- ___67-[DCBiometricStoreClient globalAuthACLTemplateUUIDsWithCompletion:]_block_invoke_2.cold.2
- ___67-[DCBiometricStoreClient globalAuthACLTemplateUUIDsWithCompletion:]_block_invoke_2.cold.3
- ___67-[DCBiometricStoreClient nonceForAuthorizationTokenWithCompletion:]_block_invoke
- ___67-[DCBiometricStoreClient nonceForAuthorizationTokenWithCompletion:]_block_invoke_2
- ___67-[DCBiometricStoreClient nonceForAuthorizationTokenWithCompletion:]_block_invoke_2.cold.1
- ___67-[DCBiometricStoreClient nonceForAuthorizationTokenWithCompletion:]_block_invoke_2.cold.2
- ___67-[DCBiometricStoreClient nonceForAuthorizationTokenWithCompletion:]_block_invoke_2.cold.3
- ___70-[DCBiometricStoreClient getGlobalThirdPartyProgenitorKeyAttestation:]_block_invoke
- ___70-[DCBiometricStoreClient getGlobalThirdPartyProgenitorKeyAttestation:]_block_invoke_2
- ___70-[DCBiometricStoreClient getGlobalThirdPartyProgenitorKeyAttestation:]_block_invoke_2.cold.1
- ___70-[DCBiometricStoreClient getGlobalThirdPartyProgenitorKeyAttestation:]_block_invoke_2.cold.2
- ___71-[DCBiometricStoreClient clearProgenitorKeyDesignationsWithCompletion:]_block_invoke
- ___71-[DCBiometricStoreClient clearProgenitorKeyDesignationsWithCompletion:]_block_invoke_2
- ___71-[DCBiometricStoreClient clearProgenitorKeyDesignationsWithCompletion:]_block_invoke_2.cold.1
- ___71-[DCBiometricStoreClient clearProgenitorKeyDesignationsWithCompletion:]_block_invoke_2.cold.2
- ___71-[DCCredentialStore(DebugAPIs) occupiedLegacySEKeySlotsWithCompletion:]_block_invoke.276
- ___76-[DCBiometricStoreClient prearmCredentialWithAuthorizationToken:completion:]_block_invoke
- ___76-[DCBiometricStoreClient prearmCredentialWithAuthorizationToken:completion:]_block_invoke.cold.1
- ___76-[DCBiometricStoreClient prearmCredentialWithAuthorizationToken:completion:]_block_invoke.cold.2
- ___76-[DCBiometricStoreClient prearmCredentialWithAuthorizationToken:completion:]_block_invoke.cold.3
- ___76-[DCCredentialStore deleteDataFromSyncableKeyStoreForIdentifier:completion:]_block_invoke
- ___76-[DCCredentialStore deleteDataFromSyncableKeyStoreForIdentifier:completion:]_block_invoke.39
- ___76-[DCCredentialStore deleteDataFromSyncableKeyStoreForIdentifier:completion:]_block_invoke.cold.1
- ___76-[DCCredentialStore(DebugAPIs) allElementsOfCredential:authData:completion:]_block_invoke.275
- ___78-[DCCredentialStore retrieveDataFromSyncableKeyStoreForIdentifier:completion:]_block_invoke
- ___78-[DCCredentialStore retrieveDataFromSyncableKeyStoreForIdentifier:completion:]_block_invoke.38
- ___78-[DCCredentialStore retrieveDataFromSyncableKeyStoreForIdentifier:completion:]_block_invoke.cold.1
- ___81-[DCCredentialStore(DebugAPIs) clearPresentmentKeyUsageForCredential:completion:]_block_invoke.278
- ___82-[DCCredentialStore retrievePIITokenFromSyncableKeyStoreForIdentifier:completion:]_block_invoke
- ___82-[DCCredentialStore retrievePIITokenFromSyncableKeyStoreForIdentifier:completion:]_block_invoke.42
- ___82-[DCCredentialStore retrievePIITokenFromSyncableKeyStoreForIdentifier:completion:]_block_invoke.cold.1
- ___83-[DCBiometricStoreClient generatePhoneTokenWithNonce:keyBlob:pairingID:completion:]_block_invoke
- ___83-[DCBiometricStoreClient generatePhoneTokenWithNonce:keyBlob:pairingID:completion:]_block_invoke_2
- ___83-[DCBiometricStoreClient generatePhoneTokenWithNonce:keyBlob:pairingID:completion:]_block_invoke_2.cold.1
- ___83-[DCBiometricStoreClient generatePhoneTokenWithNonce:keyBlob:pairingID:completion:]_block_invoke_2.cold.2
- ___83-[DCBiometricStoreClient generatePhoneTokenWithNonce:keyBlob:pairingID:completion:]_block_invoke_2.cold.3
- ___84-[DCBiometricStoreClient setModifiedGlobalAuthACL:externalizedLAContext:completion:]_block_invoke
- ___84-[DCBiometricStoreClient setModifiedGlobalAuthACL:externalizedLAContext:completion:]_block_invoke_2
- ___84-[DCBiometricStoreClient setModifiedGlobalAuthACL:externalizedLAContext:completion:]_block_invoke_2.cold.1
- ___84-[DCBiometricStoreClient setModifiedGlobalAuthACL:externalizedLAContext:completion:]_block_invoke_2.cold.2
- ___84-[DCBiometricStoreClient setModifiedGlobalAuthACL:externalizedLAContext:completion:]_block_invoke_2.cold.3
- ___87-[DCBiometricStoreClient generatePrearmTrustCertificateWithNonce:pairingID:completion:]_block_invoke
- ___87-[DCBiometricStoreClient generatePrearmTrustCertificateWithNonce:pairingID:completion:]_block_invoke_2
- ___87-[DCBiometricStoreClient generatePrearmTrustCertificateWithNonce:pairingID:completion:]_block_invoke_2.cold.1
- ___87-[DCBiometricStoreClient generatePrearmTrustCertificateWithNonce:pairingID:completion:]_block_invoke_2.cold.2
- ___88-[DCCredentialStoreClient retrievePIITokenFromSyncableKeyStoreForIdentifier:completion:]_block_invoke
- ___88-[DCCredentialStoreClient retrievePIITokenFromSyncableKeyStoreForIdentifier:completion:]_block_invoke_2
- ___88-[DCCredentialStoreClient retrievePIITokenFromSyncableKeyStoreForIdentifier:completion:]_block_invoke_2.cold.1
- ___88-[DCCredentialStoreClient retrievePIITokenFromSyncableKeyStoreForIdentifier:completion:]_block_invoke_2.cold.2
- ___92-[DCCredentialStore deletePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]_block_invoke.47
- ___94-[DCCredentialStore retrievePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]_block_invoke.46
- ___94-[DCCredentialStore storePIIHashInSyncableKeyStoreForIdentifier:data:keystoreType:completion:]_block_invoke.45
- ___95-[DCBiometricStoreClient generatePrearmTrustCertificateFromKeyBlob:nonce:pairingID:completion:]_block_invoke
- ___95-[DCBiometricStoreClient generatePrearmTrustCertificateFromKeyBlob:nonce:pairingID:completion:]_block_invoke_2
- ___95-[DCBiometricStoreClient generatePrearmTrustCertificateFromKeyBlob:nonce:pairingID:completion:]_block_invoke_2.cold.1
- ___95-[DCBiometricStoreClient generatePrearmTrustCertificateFromKeyBlob:nonce:pairingID:completion:]_block_invoke_2.cold.2
- ___98-[DCCredentialStoreClient deletePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]_block_invoke
- ___98-[DCCredentialStoreClient deletePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]_block_invoke_2
- ___98-[DCCredentialStoreClient deletePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]_block_invoke_2.cold.1
- ___98-[DCCredentialStoreClient deletePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]_block_invoke_2.cold.2
- ___99-[DCCredentialStore storeDataInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:]_block_invoke
- ___99-[DCCredentialStore storeDataInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:]_block_invoke.37
- ___99-[DCCredentialStore storeDataInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:]_block_invoke.cold.1
- ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s64l8s56l8
- ___block_literal_global.204
- _block_copy_helper.142
- _block_copy_helper.165
- _block_copy_helper.188
- _block_copy_helper.211
- _block_copy_helper.236
- _block_descriptor.144
- _block_descriptor.167
- _block_descriptor.190
- _block_descriptor.213
- _block_descriptor.238
- _block_destroy_helper.143
- _block_destroy_helper.166
- _block_destroy_helper.189
- _block_destroy_helper.212
- _block_destroy_helper.237
- _kACLData
- _kACLType
- _kArrayValue
- _kBirthDateValue
- _kCreatedAt
- _kDataValue
- _kDateValue
- _kDictionaryValue
- _kElementIdentifier
- _kNumberValue
- _kNumericTypeHint
- _kPresentmentKeyTimesUsed
- _kStringValue
- _kUpdatedAt
- _objc_msgSend$arrayValue
- _objc_msgSend$birthDateValue
- _objc_msgSend$dataValue
- _objc_msgSend$dateValue
- _objc_msgSend$decodeIntForKey:
- _objc_msgSend$deletePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:
- _objc_msgSend$deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:completion:
- _objc_msgSend$dictionaryValue
- _objc_msgSend$initWithElementIdentifier:stringValue:dataValue:dateValue:birthDateValue:numberValue:arrayValue:dictionaryValue:numericTypeHint:
- _objc_msgSend$localizedCaseInsensitiveContainsString:
- _objc_msgSend$numberValue
- _objc_msgSend$numberWithBool:
- _objc_msgSend$numberWithDouble:
- _objc_msgSend$numberWithInteger:
- _objc_msgSend$numericTypeHint
- _objc_msgSend$retrievePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:
- _objc_msgSend$retrievePIITokenFromSyncableKeyStoreForIdentifier:completion:
- _objc_msgSend$storeDataInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:
- _objc_msgSend$storePIIHashInSyncableKeyStoreForIdentifier:data:keystoreType:completion:
- _objc_msgSend$storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:
- _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
- _objc_msgSend$stringValue
- _objc_msgSend$updatePIITokenInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:
- _objectdestroy.10Tm
- _objectdestroy.30Tm
- _objectdestroy.42Tm
- _objectdestroy.6Tm
- _objectdestroy.83Tm
- _swift_getAtKeyPath
- _swift_getKeyPath
- _swift_release_n
- _symbolic SS18merchantIdentifier_t
- _symbolic SS_ypt
CStrings:
+ "%s returned successfully"
+ "%s returned with error %{public}@"
+ "%s: %{public}@"
+ "-[DCBiometricStore _remoteObjectProxyWithErrorHandler:]_block_invoke"
+ "-[DCBiometricStore bioBindingUnboundACL:]_block_invoke"
+ "-[DCBiometricStore bioBindingUnboundACL:]_block_invoke_2"
+ "-[DCBiometricStore boundAppletPresentmentACL:]_block_invoke"
+ "-[DCBiometricStore boundAppletPresentmentACL:]_block_invoke_2"
+ "-[DCBiometricStore clearProgenitorKeyDesignationsWithCompletion:]_block_invoke"
+ "-[DCBiometricStore clearProgenitorKeyDesignationsWithCompletion:]_block_invoke_2"
+ "-[DCBiometricStore credentialAuthenticationTokenStatus:]_block_invoke"
+ "-[DCBiometricStore credentialAuthenticationTokenStatus:]_block_invoke_2"
+ "-[DCBiometricStore deleteGlobalAuthACLWithOutcomeCompletion:]_block_invoke"
+ "-[DCBiometricStore deleteGlobalAuthACLWithOutcomeCompletion:]_block_invoke_2"
+ "-[DCBiometricStore establishPrearmTrustV2:completion:]_block_invoke"
+ "-[DCBiometricStore establishPrearmTrustV2:completion:]_block_invoke_2"
+ "-[DCBiometricStore generatePhoneTokenWithNonce:keyBlob:pairingID:completion:]_block_invoke"
+ "-[DCBiometricStore generatePhoneTokenWithNonce:keyBlob:pairingID:completion:]_block_invoke_2"
+ "-[DCBiometricStore generatePrearmTrustCertificateFromKeyBlob:nonce:pairingID:completion:]_block_invoke"
+ "-[DCBiometricStore generatePrearmTrustCertificateFromKeyBlob:nonce:pairingID:completion:]_block_invoke_2"
+ "-[DCBiometricStore generatePrearmTrustCertificateWithNonce:pairingID:completion:]_block_invoke"
+ "-[DCBiometricStore generatePrearmTrustCertificateWithNonce:pairingID:completion:]_block_invoke_2"
+ "-[DCBiometricStore getCASDCertificate:]_block_invoke"
+ "-[DCBiometricStore getCASDCertificate:]_block_invoke_2"
+ "-[DCBiometricStore getGlobalProgenitorKeyAttestation:]_block_invoke"
+ "-[DCBiometricStore getGlobalProgenitorKeyAttestation:]_block_invoke_2"
+ "-[DCBiometricStore getGlobalThirdPartyProgenitorKeyAttestation:]_block_invoke"
+ "-[DCBiometricStore getGlobalThirdPartyProgenitorKeyAttestation:]_block_invoke_2"
+ "-[DCBiometricStore globalAuthACLTemplateUUIDsAndCredentialCountWithCompletion:]_block_invoke"
+ "-[DCBiometricStore globalAuthACLTemplateUUIDsAndCredentialCountWithCompletion:]_block_invoke_2"
+ "-[DCBiometricStore globalAuthACLWithCompletion:]_block_invoke"
+ "-[DCBiometricStore globalAuthACLWithCompletion:]_block_invoke_2"
+ "-[DCBiometricStore globalPayloadAuthACLWithCompletion:]_block_invoke"
+ "-[DCBiometricStore globalPayloadAuthACLWithCompletion:]_block_invoke_2"
+ "-[DCBiometricStore migratePrearmTrustBlob:completion:]_block_invoke"
+ "-[DCBiometricStore migratePrearmTrustBlob:completion:]_block_invoke_2"
+ "-[DCBiometricStore nonceForAuthorizationTokenWithCompletion:]_block_invoke"
+ "-[DCBiometricStore nonceForAuthorizationTokenWithCompletion:]_block_invoke_2"
+ "-[DCBiometricStore passcodeBindingUnboundACL:]_block_invoke"
+ "-[DCBiometricStore passcodeBindingUnboundACL:]_block_invoke_2"
+ "-[DCBiometricStore prearmCredentialWithAuthorizationToken:completion:]_block_invoke"
+ "-[DCBiometricStore refreshProgenitorKeyDesignationsWithSessionHandoffToken:onlyIfNeeded:completion:]_block_invoke"
+ "-[DCBiometricStore refreshProgenitorKeyDesignationsWithSessionHandoffToken:onlyIfNeeded:completion:]_block_invoke_2"
+ "-[DCBiometricStore revokeCredentialAuthorizationToken:]_block_invoke"
+ "-[DCBiometricStore setGlobalAuthACL:ofType:completion:]_block_invoke"
+ "-[DCBiometricStore setModifiedGlobalAuthACL:externalizedLAContext:completion:]_block_invoke"
+ "-[DCBiometricStore setModifiedGlobalAuthACL:externalizedLAContext:completion:]_block_invoke_2"
+ "7c87f2ef"
+ "; codableValue = "
+ "; elementIdentifier = "
+ "CoreIDCred.DCCredentialAuthACL"
+ "CoreIDCred.DCCredentialElement"
+ "CoreIDCred_Private.DCCredentialCryptoKeyInfo"
+ "DCCredentialOptions deleteInactiveKeysAfterDays=%ld deleteIncompleteCredentialAfterDays=%ld readerAuthenticationPolicy=%ld presentmentAuthPolicy=%ld payloadProtectionPolicy=%ld requiresFirstPartyInAppPresentment=%d"
+ "DCCredentialStore deletePIIDataFromSyncableKeyStoreForIdentifier"
+ "DCCredentialStore retrieveAllItemsFromSyncableKeyStoreForItemService"
+ "DCCredentialStore retrievePIIDataFromSyncableKeyStoreForIdentifier"
+ "DCCredentialStore storePIIDataInSyncableKeyStoreForIdentifier"
+ "DCCredentialStore updatePIIDataInSyncableKeyStoreForIdentifier"
+ "DCCredentialStoreClient deletePIIDataFromSyncableKeyStoreForIdentifier"
+ "DCCredentialStoreClient deletePIIDataFromSyncableKeyStoreForIdentifier returned successfully"
+ "DCCredentialStoreClient deletePIIDataFromSyncableKeyStoreForIdentifier returned with error %{public}@"
+ "DCCredentialStoreClient retrieveAllItemsFromSyncableKeyStoreForItemService"
+ "DCCredentialStoreClient retrieveAllItemsFromSyncableKeyStoreForItemService returned successfully"
+ "DCCredentialStoreClient retrieveAllItemsFromSyncableKeyStoreForItemService returned with error %{public}@"
+ "DCCredentialStoreClient retrievePIIDataFromSyncableKeyStoreForIdentifier"
+ "DCCredentialStoreClient retrievePIIDataFromSyncableKeyStoreForIdentifier returned successfully"
+ "DCCredentialStoreClient retrievePIIDataFromSyncableKeyStoreForIdentifier returned with error %{public}@"
+ "DCCredentialStoreClient storePIIDataInSyncableKeyStoreForIdentifier"
+ "DCCredentialStoreClient storePIIDataInSyncableKeyStoreForIdentifier returned successfully"
+ "DCCredentialStoreClient storePIIDataInSyncableKeyStoreForIdentifier returned with error %{public}@"
+ "DCCredentialStoreClient updatePIIDataInSyncableKeyStoreForIdentifier"
+ "DCCredentialStoreClient updatePIIDataInSyncableKeyStoreForIdentifier returned successfully"
+ "DCCredentialStoreClient updatePIIDataInSyncableKeyStoreForIdentifier returned with error %{public}@"
+ "PII Hash"
+ "PII Token"
+ "globalPayloadAuthACLWithCompletion - OK"
+ "requiresFirstPartyInAppPresentment"
- "#16@0:8"
- "%s %s"
- "%s %s returned successfully"
- "%s %s returned with error %{public}@"
- "-[DCBiometricStoreClient boundAppletPresentmentACL:]"
- "-[DCBiometricStoreClient boundAppletPresentmentACL:]_block_invoke"
- "-[DCBiometricStoreClient boundAppletPresentmentACL:]_block_invoke_2"
- "-[DCBiometricStoreClient getCASDCertificate:]"
- "-[DCBiometricStoreClient getCASDCertificate:]_block_invoke"
- "-[DCBiometricStoreClient getCASDCertificate:]_block_invoke_2"
- "-[DCBiometricStoreClient getGlobalProgenitorKeyAttestation:]"
- "-[DCBiometricStoreClient getGlobalProgenitorKeyAttestation:]_block_invoke"
- "-[DCBiometricStoreClient getGlobalProgenitorKeyAttestation:]_block_invoke_2"
- "-[DCBiometricStoreClient getGlobalThirdPartyProgenitorKeyAttestation:]"
- "-[DCBiometricStoreClient getGlobalThirdPartyProgenitorKeyAttestation:]_block_invoke"
- "-[DCBiometricStoreClient getGlobalThirdPartyProgenitorKeyAttestation:]_block_invoke_2"
- "-cross-check"
- ".cxx_destruct"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreIDV_framework/CoreIDCred/Biometric Storage/DCBiometricStoreClient.m"
- "@\"DCBiometricStoreClient\""
- "@\"DCCredentialOptions\""
- "@\"DCCredentialRevocationInfo\""
- "@\"DCCredentialStoreClient\""
- "@\"DCPresentmentProposalReaderAnalytics\""
- "@\"DCPresentmentProposalReaderMetadata\""
- "@\"DCPresentmentResponseEncryptionParameters\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSDateComponents\""
- "@\"NSDictionary\""
- "@\"NSNumber\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSXPCConnection\""
- "@\"NSXPCListenerEndpoint\""
- "@128@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120"
- "@136@0:8Q16Q24@32@40@48@56@64@72@80@88@96@104@112@120@128"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8Q16"
- "@24@0:8^v16"
- "@24@0:8^{_NSZone=}16"
- "@28@0:8@16B24"
- "@28@0:8q16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@32@0:8@16d24"
- "@32@0:8@16q24"
- "@32@0:8Q16Q24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16Q24@32"
- "@40@0:8@16Q24q32"
- "@44@0:8@16@24@32B40"
- "@48@0:8@16@24@32@40"
- "@52@0:8B16@20@28@36@44"
- "@52@0:8q16B24@28@36@44"
- "@56@0:8@16@24@32@40@48"
- "@72@0:8@16@24@32@40Q48Q56@64"
- "@88@0:8@16@24@32@40@48@56@64@72Q80"
- "@88@0:8@16@24@32@40Q48Q56@64@72@80"
- "@96@0:8@16@24@32@40@48@56@64@72q80@88"
- "@96@0:8@16@24@32@40@48@56Q64@72@80@88"
- "@96@0:8@16@24@32@40Q48Q56@64@72@80@88"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "DCBioBindingProtocol"
- "DCBiometricStoreClient"
- "DCBiometricStoreClient bioBindingUnboundACL"
- "DCBiometricStoreClient bioBindingUnboundACL returned successfully"
- "DCBiometricStoreClient bioBindingUnboundACL returned with error %{public}@"
- "DCBiometricStoreClient clearProgenitorKeyDesignations"
- "DCBiometricStoreClient clearProgenitorKeyDesignations returned successfully"
- "DCBiometricStoreClient clearProgenitorKeyDesignations returned with error %{public}@"
- "DCBiometricStoreClient credentialAuthenticationTokenStatus"
- "DCBiometricStoreClient credentialAuthenticationTokenStatus returned successfully"
- "DCBiometricStoreClient credentialAuthenticationTokenStatus returned with error %{public}@"
- "DCBiometricStoreClient dealloc called"
- "DCBiometricStoreClient deleteGlobalAuthACLWithCompletion"
- "DCBiometricStoreClient deleteGlobalAuthACLWithCompletion returned successfully"
- "DCBiometricStoreClient deleteGlobalAuthACLWithCompletion returned with error %{public}@"
- "DCBiometricStoreClient establishPrearmTrustV2"
- "DCBiometricStoreClient establishPrearmTrustV2 returned successfully"
- "DCBiometricStoreClient establishPrearmTrustV2 returned with error %{public}@"
- "DCBiometricStoreClient generatePhoneTokenWithNonce"
- "DCBiometricStoreClient generatePhoneTokenWithNonce returned successfully"
- "DCBiometricStoreClient generatePhoneTokenWithNonce returned with error %{public}@"
- "DCBiometricStoreClient generatePrearmTrustCertificateForWatchWithNonce"
- "DCBiometricStoreClient generatePrearmTrustCertificateForWatchWithNonce returned successfully"
- "DCBiometricStoreClient generatePrearmTrustCertificateForWatchWithNonce returned with error %{public}@"
- "DCBiometricStoreClient generatePrearmTrustCertificateFromKeyBlob"
- "DCBiometricStoreClient generatePrearmTrustCertificateFromKeyBlob returned successfully"
- "DCBiometricStoreClient generatePrearmTrustCertificateFromKeyBlob returned with error %{public}@"
- "DCBiometricStoreClient globalAuthACLTemplateUUIDsWithCompletion"
- "DCBiometricStoreClient globalAuthACLTemplateUUIDsWithCompletion returned successfully"
- "DCBiometricStoreClient globalAuthACLTemplateUUIDsWithCompletion returned with error %{public}@"
- "DCBiometricStoreClient globalAuthACLWithCompletion"
- "DCBiometricStoreClient globalAuthACLWithCompletion returned successfully"
- "DCBiometricStoreClient globalAuthACLWithCompletion returned with error %{public}@"
- "DCBiometricStoreClient init called"
- "DCBiometricStoreClient invalidate"
- "DCBiometricStoreClient migratePrearmTrustBlob"
- "DCBiometricStoreClient migratePrearmTrustBlob returned successfully"
- "DCBiometricStoreClient migratePrearmTrustBlob returned with error %{public}@"
- "DCBiometricStoreClient nonceForAuthorizationTokenWithCompletion"
- "DCBiometricStoreClient nonceForAuthorizationTokenWithCompletion returned successfully"
- "DCBiometricStoreClient nonceForAuthorizationTokenWithCompletion returned with error %{public}@"
- "DCBiometricStoreClient passcodeBindingUnboundACL"
- "DCBiometricStoreClient passcodeBindingUnboundACL returned successfully"
- "DCBiometricStoreClient passcodeBindingUnboundACL returned with error %{public}@"
- "DCBiometricStoreClient prearmCredentialWithAuthorizationToken"
- "DCBiometricStoreClient prearmCredentialWithAuthorizationToken returned successfully"
- "DCBiometricStoreClient prearmCredentialWithAuthorizationToken returned with error %{public}@"
- "DCBiometricStoreClient refreshProgenitorKeyDesignations"
- "DCBiometricStoreClient refreshProgenitorKeyDesignations returned successfully"
- "DCBiometricStoreClient refreshProgenitorKeyDesignations returned with error %{public}@"
- "DCBiometricStoreClient remote object proxy error: %{public}@"
- "DCBiometricStoreClient revokeCredentialAuthorizationToken"
- "DCBiometricStoreClient revokeCredentialAuthorizationToken returned successfully"
- "DCBiometricStoreClient revokeCredentialAuthorizationToken returned with error %{public}@"
- "DCBiometricStoreClient setGlobalAuthACL"
- "DCBiometricStoreClient setGlobalAuthACL returned successfully"
- "DCBiometricStoreClient setGlobalAuthACL returned with error %{public}@"
- "DCBiometricStoreClient setModifiedGlobalAuthACL"
- "DCBiometricStoreClient setModifiedGlobalAuthACL returned successfully"
- "DCBiometricStoreClient setModifiedGlobalAuthACL returned with error %{public}@"
- "DCBiometricStoreXPCProtocol"
- "DCCredentialAttestation"
- "DCCredentialAuthACL"
- "DCCredentialAuthorizationToken"
- "DCCredentialCryptoKey"
- "DCCredentialCryptoKeyInfo"
- "DCCredentialElement"
- "DCCredentialElement identifier = %@; array value = %@"
- "DCCredentialElement identifier = %@; birthDate value = %@"
- "DCCredentialElement identifier = %@; data value = %@"
- "DCCredentialElement identifier = %@; date value = %@"
- "DCCredentialElement identifier = %@; dictionary value = %@"
- "DCCredentialElement identifier = %@; no value"
- "DCCredentialElement identifier = %@; number value = %@, type hint = %@"
- "DCCredentialElement identifier = %@; string value = %@"
- "DCCredentialNonce"
- "DCCredentialOptions"
- "DCCredentialOptions deleteInactiveKeysAfterDays=%ld deleteIncompleteCredentialAfterDays=%ld readerAuthenticationPolicy=%ld presentmentAuthPolicy=%ld payloadProtectionPolicy=%ld"
- "DCCredentialPayload"
- "DCCredentialResponse"
- "DCCredentialRevocationInfo"
- "DCCredentialStore deleteDataFromSyncableKeyStoreForIdentifier"
- "DCCredentialStore retrieveDataFromSyncableKeyStoreForIdentifier"
- "DCCredentialStore storeDataInSyncableKeyStoreForIdentifier"
- "DCCredentialStore updateDataInSyncableKeyStoreForIdentifier"
- "DCCredentialStoreClient"
- "DCCredentialStoreClient deletePIIHashFromSyncableKeyStoreForIdentifier"
- "DCCredentialStoreClient deletePIIHashFromSyncableKeyStoreForIdentifier returned successfully"
- "DCCredentialStoreClient deletePIIHashFromSyncableKeyStoreForIdentifier returned with error %{public}@"
- "DCCredentialStoreClient deletePIITokenFromSyncableKeyStoreForIdentifier"
- "DCCredentialStoreClient deletePIITokenFromSyncableKeyStoreForIdentifier returned successfully"
- "DCCredentialStoreClient deletePIITokenFromSyncableKeyStoreForIdentifier returned with error %{public}@"
- "DCCredentialStoreClient retrievePIIHashFromSyncableKeyStoreForIdentifier"
- "DCCredentialStoreClient retrievePIIHashFromSyncableKeyStoreForIdentifier returned successfully"
- "DCCredentialStoreClient retrievePIIHashFromSyncableKeyStoreForIdentifier returned with error %{public}@"
- "DCCredentialStoreClient retrievePIITokenFromSyncableKeyStoreForIdentifier"
- "DCCredentialStoreClient retrievePIITokenFromSyncableKeyStoreForIdentifier returned successfully"
- "DCCredentialStoreClient retrievePIITokenFromSyncableKeyStoreForIdentifier returned with error %{public}@"
- "DCCredentialStoreClient storePIIHashInSyncableKeyStoreForIdentifier"
- "DCCredentialStoreClient storePIIHashInSyncableKeyStoreForIdentifier returned successfully"
- "DCCredentialStoreClient storePIIHashInSyncableKeyStoreForIdentifier returned with error %{public}@"
- "DCCredentialStoreClient storePIITokenInSyncableKeyStoreForIdentifier"
- "DCCredentialStoreClient storePIITokenInSyncableKeyStoreForIdentifier returned successfully"
- "DCCredentialStoreClient storePIITokenInSyncableKeyStoreForIdentifier returned with error %{public}@"
- "DCCredentialStoreClient updatePIITokenInSyncableKeyStoreForIdentifier"
- "DCCredentialStoreClient updatePIITokenInSyncableKeyStoreForIdentifier returned successfully"
- "DCCredentialStoreClient updatePIITokenInSyncableKeyStoreForIdentifier returned with error %{public}@"
- "DCCredentialStoreXPCProtocol"
- "DCCredentialTrust"
- "DCLegacySESlotInfo"
- "DCPresentmentProposal"
- "DCPresentmentProposalReaderAnalytics"
- "DCPresentmentProposalReaderMetadata"
- "DCPresentmentRequest"
- "DCPresentmentRequestedElement"
- "DCPresentmentResponseEncryptionParameters"
- "DCPresentmentSelection"
- "DCPresentmentSession"
- "DCPresentmentSessionOptions"
- "DebugAPIs"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"DCBiometricStoreClient\",R,N,V_client"
- "T@\"DCCredentialOptions\",&,N,V_options"
- "T@\"DCCredentialRevocationInfo\",&,N,V_credentialRevocationInfo"
- "T@\"DCCredentialRevocationInfo\",R,N"
- "T@\"DCCredentialRevocationInfo\",R,N,V_credentialRevocationInfo"
- "T@\"DCCredentialStoreClient\",R,N,V_client"
- "T@\"DCPresentmentProposalReaderAnalytics\",R,N,V_readerAnalytics"
- "T@\"DCPresentmentProposalReaderMetadata\",R,N,V_readerMetadata"
- "T@\"DCPresentmentResponseEncryptionParameters\",C,N"
- "T@\"DCPresentmentResponseEncryptionParameters\",N,R"
- "T@\"NSArray\",&,N"
- "T@\"NSArray\",&,N,V_issuerCertificateChain"
- "T@\"NSArray\",&,N,V_payloadProtectionKeys"
- "T@\"NSArray\",&,N,V_payloads"
- "T@\"NSArray\",&,N,V_provisioningFailureReasons"
- "T@\"NSArray\",R,N,V_arrayValue"
- "T@\"NSArray\",R,N,V_issuerCertificateChain"
- "T@\"NSArray\",R,N,V_partitions"
- "T@\"NSData\",&"
- "T@\"NSData\",&,N"
- "T@\"NSData\",&,N,V_encryptedCredentialPII"
- "T@\"NSData\",&,N,V_ingestionHash"
- "T@\"NSData\",&,N,V_responseData"
- "T@\"NSData\",N,C"
- "T@\"NSData\",R,N"
- "T@\"NSData\",R,N,V_acl"
- "T@\"NSData\",R,N,V_authACL"
- "T@\"NSData\",R,N,V_certificate"
- "T@\"NSData\",R,N,V_credentialAuthorizationToken"
- "T@\"NSData\",R,N,V_credentialBAACertificate"
- "T@\"NSData\",R,N,V_credentialKeyBlob"
- "T@\"NSData\",R,N,V_credentialNonce"
- "T@\"NSData\",R,N,V_dataValue"
- "T@\"NSData\",R,N,V_iconData"
- "T@\"NSData\",R,N,V_iconDigest"
- "T@\"NSData\",R,N,V_identifier"
- "T@\"NSData\",R,N,V_issuerSignerCertificateData"
- "T@\"NSData\",R,N,V_payloadData"
- "T@\"NSData\",R,N,V_presentmentPublicKey"
- "T@\"NSData\",R,N,V_publicKey"
- "T@\"NSData\",R,N,V_publicKeyIdentifier"
- "T@\"NSData\",R,N,V_readerAuthCertificateData"
- "T@\"NSDate\",&,N,V_createdAt"
- "T@\"NSDate\",&,N,V_signedAt"
- "T@\"NSDate\",&,N,V_updatedAt"
- "T@\"NSDate\",&,N,V_validFrom"
- "T@\"NSDate\",&,N,V_validUntil"
- "T@\"NSDate\",R,N"
- "T@\"NSDate\",R,N,V_createdAt"
- "T@\"NSDate\",R,N,V_dateValue"
- "T@\"NSDate\",R,N,V_signedAt"
- "T@\"NSDate\",R,N,V_updatedAt"
- "T@\"NSDate\",R,N,V_validFrom"
- "T@\"NSDate\",R,N,V_validUntil"
- "T@\"NSDateComponents\",R,N,V_birthDateValue"
- "T@\"NSDictionary\",&,N"
- "T@\"NSDictionary\",&,N,V_deviceEncryptionKeys"
- "T@\"NSDictionary\",&,N,V_elementsByNamespace"
- "T@\"NSDictionary\",&,N,V_keySigningKeys"
- "T@\"NSDictionary\",&,N,V_presentmentKeys"
- "T@\"NSDictionary\",R,N"
- "T@\"NSDictionary\",R,N,V_dictionaryValue"
- "T@\"NSDictionary\",R,N,V_elementIdentifiersByNamespace"
- "T@\"NSDictionary\",R,N,V_elements"
- "T@\"NSNumber\",R,N,V_merchantCategoryCode"
- "T@\"NSNumber\",R,N,V_numberValue"
- "T@\"NSString\",&,N"
- "T@\"NSString\",&,N,V_credentialIdentifier"
- "T@\"NSString\",&,N,V_documentType"
- "T@\"NSString\",&,N,V_issuingAuthority"
- "T@\"NSString\",&,N,V_issuingJurisdiction"
- "T@\"NSString\",&,N,V_partition"
- "T@\"NSString\",&,N,V_presentmentKeyIdentifier"
- "T@\"NSString\",&,N,V_region"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",N,R"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_credentialIdentifier"
- "T@\"NSString\",R,N,V_credentialPairingID"
- "T@\"NSString\",R,N,V_docType"
- "T@\"NSString\",R,N,V_elementIdentifier"
- "T@\"NSString\",R,N,V_iconMediaType"
- "T@\"NSString\",R,N,V_identifier"
- "T@\"NSString\",R,N,V_issuingAuthority"
- "T@\"NSString\",R,N,V_issuingJurisdiction"
- "T@\"NSString\",R,N,V_keyType"
- "T@\"NSString\",R,N,V_keyUsage"
- "T@\"NSString\",R,N,V_organization"
- "T@\"NSString\",R,N,V_organizationalUnit"
- "T@\"NSString\",R,N,V_partition"
- "T@\"NSString\",R,N,V_presentmentKeyIdentifier"
- "T@\"NSString\",R,N,V_region"
- "T@\"NSString\",R,N,V_stringValue"
- "T@\"NSString\",R,N,V_untrustedIdentifier"
- "T@\"NSString\",R,N,V_untrustedIssuerIdentifier"
- "T@\"NSString\",R,N,V_untrustedIssuerOrganization"
- "T@\"NSString\",R,N,V_untrustedOrganization"
- "T@\"NSURL\",R,N,V_URL"
- "T@\"NSURL\",R,N,V_iconURL"
- "T@\"NSURL\",R,N,V_privacyPolicyURL"
- "T@\"NSXPCConnection\",&,N,V_serverConnection"
- "T@\"NSXPCListenerEndpoint\",&,N"
- "T@?,C"
- "TB,N,R"
- "TB,N,V_hasUsablePresentmentAuthPolicy"
- "TB,N,V_isMissing"
- "TB,N,V_needsPresentmentKeyRefresh"
- "TB,R"
- "TB,R,N,GisTrusted,V_trusted"
- "TB,R,N,V_credentialAccessibilityEnabled"
- "TQ"
- "TQ,N"
- "TQ,N,R"
- "TQ,N,V_credentialState"
- "TQ,R"
- "TQ,R,N,V_format"
- "TQ,R,N,V_iconDigestAlgorithm"
- "TQ,R,N,V_numericTypeHint"
- "TQ,R,N,V_protectionType"
- "Tq,N"
- "Tq,N,R"
- "Tq,N,V_seSlot"
- "Tq,R,N,V_presentmentKeyTimesUsed"
- "T{os_unfair_lock_s=I},N,V_lock"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_TtC10CoreIDCred31XPCCredentialPresentmentRequest"
- "_TtP10CoreIDCred24DCPresentmentXPCProtocol_"
- "_URL"
- "_acl"
- "_aclData"
- "_aclType"
- "_arrayValue"
- "_attestation"
- "_attestationData"
- "_attestationType"
- "_authACL"
- "_authData"
- "_birthDateValue"
- "_casdAttestation"
- "_casdSignature"
- "_certificate"
- "_client"
- "_createdAt"
- "_credentialAccessibilityEnabled"
- "_credentialAuthorizationToken"
- "_credentialBAACertificate"
- "_credentialIdentifier"
- "_credentialKeyBlob"
- "_credentialNonce"
- "_credentialPairingID"
- "_credentialRevocationInfo"
- "_credentialState"
- "_dataValue"
- "_dateValue"
- "_deleteInactiveKeysAfterDays"
- "_deleteIncompleteCredentialAfterDays"
- "_deviceEncryptionKeys"
- "_deviceNamespaces"
- "_dictionaryValue"
- "_docType"
- "_documentType"
- "_elementFallbackModes"
- "_elementIdentifier"
- "_elementIdentifiersByNamespace"
- "_elements"
- "_elementsByNamespace"
- "_elementsToPresent"
- "_encryptedCredentialPII"
- "_format"
- "_hasBeenConfigured"
- "_hasUsablePresentmentAuthPolicy"
- "_iconData"
- "_iconDigest"
- "_iconDigestAlgorithm"
- "_iconMediaType"
- "_iconURL"
- "_identifier"
- "_ingestionHash"
- "_isMissing"
- "_issuerCertificateChain"
- "_issuerSignerCertificateData"
- "_issuingAuthority"
- "_issuingJurisdiction"
- "_keyAuthorization"
- "_keySigningKeys"
- "_keyType"
- "_keyUsage"
- "_kskAttestation"
- "_lock"
- "_merchantCategoryCode"
- "_messageEncodingFormat"
- "_needsPresentmentKeyRefresh"
- "_numberValue"
- "_numericTypeHint"
- "_options"
- "_organization"
- "_organizationalUnit"
- "_partition"
- "_partitions"
- "_payloadData"
- "_payloadProtectionKeys"
- "_payloadProtectionPolicy"
- "_payloads"
- "_presentmentAuthPolicy"
- "_presentmentKeyIdentifier"
- "_presentmentKeyTimesUsed"
- "_presentmentKeys"
- "_presentmentPublicKey"
- "_privacyPolicyURL"
- "_progenitorKeyAttestation"
- "_protectionType"
- "_provisioningFailureReasons"
- "_publicKey"
- "_publicKeyCOSEKey"
- "_publicKeyIdentifier"
- "_readerAnalytics"
- "_readerAuthCertificateData"
- "_readerAuthenticationPolicy"
- "_readerMetadata"
- "_region"
- "_responseData"
- "_responseEncryptionParameters"
- "_seAccessEndpoint"
- "_seSlot"
- "_serverConnection"
- "_sessionEncryptionMode"
- "_signedAt"
- "_stringValue"
- "_trusted"
- "_untrustedIdentifier"
- "_untrustedIssuerIdentifier"
- "_untrustedIssuerOrganization"
- "_untrustedOrganization"
- "_updatedAt"
- "_validFrom"
- "_validUntil"
- "acl"
- "aclData"
- "aclType"
- "activate"
- "activeRegionsInPartitions:docTypes:completion:"
- "allElementsOfCredential:authData:completion:"
- "allElementsOfCredential:completion:"
- "allKeys"
- "allocWithZone:"
- "appendFormat:"
- "appendString:"
- "appleHPKEWithSessionTranscript:certificateChain:"
- "arrayValue"
- "arrayWithObjects:count:"
- "associateExternalPresentmentKeyWithCredential:publicKeyIdentifier:completion:"
- "authorizeDeviceKeySigningKeyOfCredential:accountKeyIdentifier:completion:"
- "authorizeRemoteKeySigningKeyWithCredential:remoteKey:completion:"
- "autorelease"
- "bioBindingUnboundACL:"
- "birthDateValue"
- "boundAppletPresentmentACL:"
- "buildCredentialResponseFor:completionHandler:"
- "buildCredentialResponseForSelection:completion:"
- "buildErrorResponseWith:completionHandler:"
- "buildErrorResponseWithStatus:completion:"
- "buildGenericDataResponse:completion:"
- "buildGenericDataResponse:completionHandler:"
- "buildResponseFor:completionHandler:"
- "buildResponseForSelection:completion:"
- "checkCompletenessOfCredential:completion:"
- "class"
- "clearPresentmentKeyUsageForCredential:completion:"
- "clearProgenitorKeyDesignationsWithCompletion:"
- "client"
- "code"
- "compare:"
- "configureIfNeededWithContinuation:errorHandler:"
- "configureWithPartitions:completion:"
- "configureWithPartitions:presentmentType:options:completionHandler:"
- "conformsToProtocol:"
- "connection"
- "connectionConfigurationStatus"
- "copy"
- "copyWithElementsToPresent:"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createAccountKeySigningKeyForAccountKeyIdentifier:completion:"
- "createCredentialInPartition:options:completion:"
- "createDaemonDisconnectedError"
- "createdAt"
- "credentialAuthenticationTokenStatus:"
- "credentialIdentifierForPublicKeyIdentifier:completion:"
- "credentialIdentifiers:"
- "credentialIdentifiersForPublicKeyIdentifier:completion:"
- "credentialIdentifiersInPartitions:completion:"
- "credentialIdentifiersInPartitions:docType:completion:"
- "credentialState"
- "cross-check"
- "dataValue"
- "dateValue"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeIntForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "deleteAccountKeySigningKeyForAccountKeyIdentifier:completion:"
- "deleteCharactersInRange:"
- "deleteCredential:completion:"
- "deleteDataFromSyncableKeyStoreForIdentifier:completion:"
- "deleteGlobalAuthACLWithCompletion:"
- "deleteGlobalAuthACLWithOutcomeCompletion:"
- "deletePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:"
- "deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:completion:"
- "description"
- "deviceEncryptionKeys"
- "dictionaryRepresentation"
- "dictionaryValue"
- "dictionaryWithValuesForKeys:"
- "documentType"
- "elementIdentifiersByNamespace"
- "elementsByNamespace"
- "elementsOfCredential:elementIdentifiers:authData:completion:"
- "elementsOfCredential:elementIdentifiers:completion:"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "encodedData"
- "encryptedCredentialPII"
- "enumerateKeysAndObjectsUsingBlock:"
- "eraseLegacySEKeySlot:completion:"
- "errorWithDomain:code:userInfo:"
- "establishPrearmTrustV2:completion:"
- "failWithError:"
- "finishConfiguration"
- "finishDecoding"
- "finishEncoding"
- "firstObject"
- "format"
- "generateAccountKeyAuthorizationForCredential:accountKeyIdentifier:completion:"
- "generateDeviceEncryptionKeyForCredential:completion:"
- "generateDeviceEncryptionKeyForCredential:keyType:completion:"
- "generateKeySigningKeyForCredential:completion:"
- "generatePhoneTokenWithNonce:keyBlob:pairingID:completion:"
- "generatePrearmTrustCertificateFromKeyBlob:nonce:pairingID:completion:"
- "generatePrearmTrustCertificateWithNonce:pairingID:completion:"
- "generatePresentmentKeyForCredential:completion:"
- "generatePresentmentKeysForCredential:numKeys:completion:"
- "generateTransportKeyFor:completionHandler:"
- "generateTransportKeyForSpecification:completion:"
- "getCASDCertificate:"
- "getGlobalProgenitorKeyAttestation:"
- "getGlobalThirdPartyProgenitorKeyAttestation:"
- "globalAuthACLTemplateUUIDsAndCredentialCountWithCompletion:"
- "globalAuthACLTemplateUUIDsWithCompletion:"
- "globalAuthACLWithCompletion:"
- "hasBeenConfigured"
- "hasUsablePresentmentAuthPolicy"
- "hash"
- "ingestionHash"
- "init"
- "initForReadingFromData:error:"
- "initRequiringSecureCoding:"
- "initWithArray:"
- "initWithArray:copyItems:"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithCredentialAuthorizationToken:pairingID:"
- "initWithCredentialIdentifier:elementsToPresent:authData:seAccessEndpoint:"
- "initWithCredentialIdentifier:elementsToPresent:authData:seAccessEndpoint:deviceNamespaces:"
- "initWithCredentialIdentifier:presentmentKeyIdentifier:presentmentPublicKey:partition:docType:elements:authACL:readerAuthCertificateData:issuerSignerCertificateData:readerMetadata:readerAnalytics:region:issuingJurisdiction:credentialRevocationInfo:"
- "initWithCredentialKeyBlob:baaCertificate:pairingID:isAccessibilityEnabled:"
- "initWithCredentialNonce:"
- "initWithData:type:"
- "initWithDictionary:copyItems:"
- "initWithElementIdentifier:"
- "initWithElementIdentifier:arrayValue:"
- "initWithElementIdentifier:birthDateValue:"
- "initWithElementIdentifier:boolValue:"
- "initWithElementIdentifier:dataValue:"
- "initWithElementIdentifier:dateValue:"
- "initWithElementIdentifier:dictionaryValue:"
- "initWithElementIdentifier:doubleValue:"
- "initWithElementIdentifier:intValue:"
- "initWithElementIdentifier:intentToRetain:retentionPeriod:"
- "initWithElementIdentifier:stringValue:"
- "initWithElementIdentifier:stringValue:dataValue:dateValue:birthDateValue:numberValue:arrayValue:dictionaryValue:numericTypeHint:"
- "initWithFormat:protectionType:docType:createdAt:updatedAt:validFrom:validUntil:signedAt:elementIdentifiersByNamespace:issuerCertificateChain:region:issuingJurisdiction:issuingAuthority:credentialRevocationInfo:payloadData:"
- "initWithIdentifier:certificate:URL:"
- "initWithIdentifier:credentialIdentifier:publicKey:publicKeyIdentifier:keyType:keyUsage:createdAt:updatedAt:presentmentKeyTimesUsed:acl:"
- "initWithIdentifier:organization:organizationalUnit:iconData:iconURL:iconDigest:iconDigestAlgorithm:iconMediaType:privacyPolicyURL:merchantCategoryCode:"
- "initWithIdentifier:publicKey:publicKeyIdentifier:publicKeyCOSEKey:keyType:keyUsage:attestation:"
- "initWithIdentifier:publicKey:publicKeyIdentifier:publicKeyCOSEKey:keyType:keyUsage:attestation:keyAuthorization:kskAttestation:"
- "initWithIdentifier:publicKey:publicKeyIdentifier:publicKeyCOSEKey:keyType:keyUsage:casdAttestation:keyAuthorization:kskAttestation:"
- "initWithIdentifier:publicKey:publicKeyIdentifier:publicKeyCOSEKey:keyType:keyUsage:casdSignature:casdAttestation:keyAuthorization:kskAttestation:"
- "initWithIdentifier:publicKey:publicKeyIdentifier:publicKeyCOSEKey:keyType:keyUsage:progenitorKeyAttestation:casdAttestation:keyAuthorization:kskAttestation:"
- "initWithMachServiceName:options:"
- "initWithPartitions:"
- "initWithPartitions:presentmentType:"
- "initWithPartitions:presentmentType:options:"
- "initWithResponseData:elementsByNamespace:"
- "initWithSESlot:isMissing:"
- "initWithSESlot:isMissing:partition:credentialIdentifier:presentmentKeyIdentifier:"
- "initWithSessionEncryptionMode:"
- "initWithSessionEncryptionMode:readerAuthenticationPolicy:"
- "initWithSessionEstablishment:sessionTranscript:"
- "initWithTrusted:untrustedIdentifier:untrustedOrganization:untrustedIssuerIdentifier:untrustedIssuerOrganization:"
- "intentToRetain"
- "interfaceWithProtocol:"
- "interpretCredentialRequest:completionHandler:"
- "interpretGenericDataRequest:completion:"
- "interpretGenericDataRequest:completionHandler:"
- "interpretRequest:completion:"
- "interpretRequest:completionHandler:"
- "interruptionHandler"
- "invalidate"
- "isAccountKeySigningKeyAvailableForAccountKeyIdentifier:completion:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPIITokenAvailableForIdentifier:completion:"
- "isProxy"
- "isTrusted"
- "issuerCertificateChain"
- "issuingAuthority"
- "keyInfoForCredential:completion:"
- "keySigningKeys"
- "length"
- "localizedCaseInsensitiveContainsString:"
- "lock"
- "migratePrearmTrustBlob:completion:"
- "needsPresentmentKeyRefresh"
- "nonceForAuthorizationTokenWithCompletion:"
- "null"
- "numberValue"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInteger:"
- "numericTypeHint"
- "objectForKeyedSubscript:"
- "occupiedLegacySEKeySlotsWithCompletion:"
- "options"
- "partitions"
- "passcodeBindingUnboundACL:"
- "payloadAuthACLForCredential:completion:"
- "payloadData"
- "payloadIngestionHash"
- "payloadProtectionKeys"
- "payloadSignedAt"
- "payloadValidFrom"
- "payloadValidUntil"
- "payloads"
- "payloadsOfCredential:completion:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "prearmCredentialWithAuthorizationToken:completion:"
- "presentmentAuthPolicy"
- "presentmentKeyTimesUsed"
- "presentmentKeys"
- "presentmentType"
- "propertiesOfCredential:completion:"
- "protectionType"
- "provisioningFailureReasons"
- "publicKeyCOSEKey"
- "q"
- "q16@0:8"
- "refreshProgenitorKeyDesignationsWithSessionHandoffToken:onlyIfNeeded:completion:"
- "release"
- "remoteObjectInterface"
- "remoteObjectProxyWithErrorHandler:"
- "replacePayloadOfCredential:withPayload:format:completion:"
- "respondsToSelector:"
- "responseData"
- "retain"
- "retainCount"
- "retentionPeriod"
- "retrieveAccountKeySigningKeyForAccountKeyIdentifier:completion:"
- "retrieveDataFromSyncableKeyStoreForIdentifier:completion:"
- "retrievePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:"
- "retrievePIITokenFromSyncableKeyStoreForIdentifier:completion:"
- "revokeCredentialAuthorizationToken:"
- "self"
- "serverConnection"
- "setAclData:"
- "setAclType:"
- "setAttestation:"
- "setAttestationData:"
- "setAttestationType:"
- "setAuthData:"
- "setCasdAttestation:"
- "setCasdSignature:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setCreatedAt:"
- "setCredentialIdentifier:"
- "setCredentialRevocationInfo:"
- "setCredentialState:"
- "setDeleteInactiveKeysAfterDays:"
- "setDeleteIncompleteCredentialAfterDays:"
- "setDeviceEncryptionKeys:"
- "setDeviceNamespaces:"
- "setDocumentType:"
- "setElementFallbackModes:"
- "setElementsByNamespace:"
- "setElementsToPresent:"
- "setEncryptedCredentialPII:"
- "setGlobalAuthACL:ofType:completion:"
- "setHasBeenConfigured:"
- "setHasUsablePresentmentAuthPolicy:"
- "setIdentifier:"
- "setIngestionHash:"
- "setInterruptionHandler:"
- "setIsMissing:"
- "setIssuerCertificateChain:"
- "setIssuingAuthority:"
- "setIssuingJurisdiction:"
- "setKeyAuthorization:"
- "setKeySigningKeys:"
- "setKeyType:"
- "setKeyUsage:"
- "setKskAttestation:"
- "setLock:"
- "setMessageEncodingFormat:"
- "setModifiedGlobalAuthACL:externalizedLAContext:completion:"
- "setNeedsPresentmentKeyRefresh:"
- "setObject:forKeyedSubscript:"
- "setOptions:"
- "setPartition:"
- "setPayloadProtectionKeys:"
- "setPayloadProtectionPolicy:"
- "setPayloads:"
- "setPresentmentAuthPolicy:"
- "setPresentmentKeyIdentifier:"
- "setPresentmentKeys:"
- "setProgenitorKeyAttestation:"
- "setProvisioningFailureReasons:"
- "setPublicKey:"
- "setPublicKeyCOSEKey:"
- "setPublicKeyIdentifier:"
- "setReaderAuthenticationPolicy:"
- "setRegion:"
- "setRemoteObjectInterface:"
- "setRequiredPublicKeyIdentifier:"
- "setResponseData:"
- "setResponseEncryptionParameters:"
- "setSeAccessEndpoint:"
- "setSeSlot:"
- "setServerConnection:"
- "setSessionEncryptionIntermediateKeyMaterial:"
- "setSessionEncryptionMode:"
- "setSessionEstablishment:"
- "setSessionTranscript:"
- "setSignedAt:"
- "setStateOfCredential:to:completion:"
- "setUpdatedAt:"
- "setValidFrom:"
- "setValidUntil:"
- "setWithArray:"
- "setWithObjects:"
- "signedAt"
- "sortedArrayUsingSelector:"
- "state"
- "storage"
- "storeDataInSyncableKeyStoreForIdentifier:data:completion:"
- "storeDataInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:"
- "storePIIHashInSyncableKeyStoreForIdentifier:data:keystoreType:completion:"
- "storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:"
- "string"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringValue"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:"
- "updatePIITokenInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:"
- "updatedAt"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8{os_unfair_lock_s=I}16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"DCCredentialAttestation\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"DCCredentialAuthACL\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"DCCredentialNonce\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSArray\"qq@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSData\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8@?<v@?Q@\"NSError\">16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v24@?0@\"DCCredentialResponse\"8@\"NSError\"16"
- "v32@0:8@\"DCCredentialAuthorizationToken\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"DCCredentialTrust\"16@?<v@?@\"DCCredentialAttestation\"@\"NSError\">24"
- "v32@0:8@\"DCPresentmentRequest\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"DCPresentmentSelection\"16@?<v@?@\"DCCredentialResponse\"@\"NSError\">24"
- "v32@0:8@\"DCPresentmentSelection\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"DCCredentialCryptoKey\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"DCCredentialProperties\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?Q@\"NSError\">24"
- "v32@0:8@\"_TtC10CoreIDCred31XPCCredentialPresentmentRequest\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "v32@0:8@?16@?24"
- "v32@0:8Q16@?24"
- "v32@0:8Q16@?<v@?@\"NSData\"@\"NSError\">24"
- "v32@0:8q16@?24"
- "v32@0:8q16@?<v@?@\"NSError\">24"
- "v36@0:8@\"NSData\"16B24@?<v@?@\"NSError\">28"
- "v36@0:8@16B24@?28"
- "v40@0:8@\"NSArray\"16@\"NSSet\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@\"NSArray\"16@\"NSString\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@\"NSData\"16@\"NSData\"24@?<v@?@\"NSArray\"@\"NSError\">32"
- "v40@0:8@\"NSData\"16@\"NSString\"24@?<v@?@\"DCCredentialTrust\"@\"NSError\">32"
- "v40@0:8@\"NSData\"16Q24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"DCCredentialOptions\"24@?<v@?@\"NSString\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSData\"24@?<v@?@\"NSData\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSData\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSData\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSData\"@\"NSData\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSData\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSString\"16Q24@?<v@?@\"DCCredentialCryptoKey\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16Q24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSString\"16Q24@?<v@?@\"NSString\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16q24@?<v@?@\"NSArray\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16Q24@?32"
- "v40@0:8@16q24@?32"
- "v48@0:8@\"DCCredentialNonce\"16@\"NSData\"24@\"NSString\"32@?<v@?@\"DCCredentialAuthorizationToken\"@\"NSError\">40"
- "v48@0:8@\"NSArray\"16Q24@\"DCPresentmentSessionOptions\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"NSData\"16@\"NSData\"24@\"NSString\"32@?<v@?@\"DCCredentialTrust\"@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"NSData\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"NSData\"24Q32@?<v@?@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSData\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24Q32@?40"
- "v48@0:8@16Q24@32@?40"
- "validFrom"
- "validUntil"
- "value"
- "webProposalHPKEWithSessionTranscript:rawEncryptionKey:"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "{os_unfair_lock_s=I}16@0:8"

```
