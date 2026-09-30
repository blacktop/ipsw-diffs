## BiomeFoundation

> `/System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation`

```diff

-200.6.0.0.0
-  __TEXT.__text: 0x35718
-  __TEXT.__auth_stubs: 0xdc0
-  __TEXT.__objc_methlist: 0x29bc
+209.12.1.0.0
+  __TEXT.__text: 0x370c4
+  __TEXT.__auth_stubs: 0xd90
+  __TEXT.__objc_methlist: 0x2a1c
   __TEXT.__const: 0x22a
-  __TEXT.__cstring: 0x4f56
-  __TEXT.__oslogstring: 0x3209
-  __TEXT.__gcc_except_tab: 0xdb8
+  __TEXT.__cstring: 0x4f8d
+  __TEXT.__oslogstring: 0x3305
+  __TEXT.__gcc_except_tab: 0xdcc
   __TEXT.__dlopen_cstrs: 0x2d4
   __TEXT.__constg_swiftt: 0x64
   __TEXT.__swift5_typeref: 0x21
   __TEXT.__swift5_reflstr: 0x2f
   __TEXT.__swift5_fieldmd: 0x44
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0xe30
-  __TEXT.__objc_classname: 0x669
-  __TEXT.__objc_methname: 0x59eb
-  __TEXT.__objc_methtype: 0x10d9
-  __TEXT.__objc_stubs: 0x48a0
+  __TEXT.__unwind_info: 0xe90
+  __TEXT.__objc_classname: 0x6b8
+  __TEXT.__objc_methname: 0x5b99
+  __TEXT.__objc_methtype: 0x10da
+  __TEXT.__objc_stubs: 0x49a0
   __DATA_CONST.__got: 0x380
-  __DATA_CONST.__const: 0xc88
+  __DATA_CONST.__const: 0xcb0
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x78
+  __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1818
-  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_selrefs: 0x1858
+  __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x1328
-  __AUTH_CONST.__auth_got: 0x6f0
+  __AUTH_CONST.__auth_got: 0x6d8
   __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x5720
-  __AUTH_CONST.__objc_const: 0x68a0
+  __AUTH_CONST.__cfstring: 0x5820
+  __AUTH_CONST.__objc_const: 0x6c38
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x230
-  __AUTH.__objc_data: 0x480
+  __AUTH.__objc_data: 0x520
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x290
-  __DATA.__data: 0x5b8
-  __DATA.__bss: 0x130
+  __DATA.__data: 0x618
+  __DATA.__bss: 0x120
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0xdc0
+  __DATA_DIRTY.__objc_data: 0xd20
   __DATA_DIRTY.__data: 0x198
-  __DATA_DIRTY.__bss: 0x180
+  __DATA_DIRTY.__bss: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 4F58002C-8FB9-39BB-93F4-FB050CD0493D
-  Functions: 1205
-  Symbols:   4486
-  CStrings:  3016
+  UUID: 588E01EF-BD00-3089-AC38-B56DB421CC0D
+  Functions: 1231
+  Symbols:   4615
+  CStrings:  3045
 
Symbols:
+ +[BMResourceDescriptor descriptorWithKey:fromDescriptors:]
+ -[BMAccessControlPolicy allowsConnectionToEntitledAccessServiceWithDomain:]
+ -[BMAccessControlPolicy allowsConnectionToEntitledAccessServiceWithDomain:].cold.1
+ -[BMAccessControlPolicy allowsConnectionToEntitledAccessServiceWithDomain:].cold.2
+ -[BMAccessControlPolicy identityMatchWithSourceIdentifier:appIdentifier:]
+ -[BMAccessControlPolicy isSpotlightInlineDonationSetIdentifier:]
+ -[BMAccessControlPolicy onBehalfOfPolicy]
+ -[BMAccessControlPolicy processIdentityMatchesSourceIdentifierForResource:]
+ -[BMAccessControlPolicy processIdentityMatchesSourceIdentifierForResource:].cold.1
+ -[BMAccessControlPolicy(BMUnentitledAccessService) allowsConnectionToUnentitledAccessServiceWithDomain:]
+ -[BMAccessServiceListener _acceptConnection:withInterface:]
+ -[BMAccessServiceListener _acceptUnentitledConnection:]
+ -[BMAccessServiceListener _acceptUnentitledConnection:].cold.1
+ -[BMAccessServiceListener connection:handleInvocation:isReply:].cold.2
+ -[BMAccessServiceListener listener:shouldAcceptNewConnection:].cold.7
+ -[BMProcess _canTrustUnrestrictedEntitlementsAndSigningIdentifier]
+ -[BMProcess codeSigningIdentity]
+ GCC_except_table17
+ GCC_except_table41
+ GCC_except_table49
+ GCC_except_table52
+ GCC_except_table64
+ _BMResourceDescriptorKeySourceIdentifier
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __OBJC_$_CLASS_METHODS_BMAccessControlPolicy(LegacyViewEntitlement|SyncableSets|SetStoreUpdateService|WriteService|DaemonToAgent|UseCase|BMUnentitledAccessService)
+ __OBJC_$_INSTANCE_METHODS_BMAccessControlPolicy(LegacyViewEntitlement|SyncableSets|SetStoreUpdateService|WriteService|DaemonToAgent|UseCase|BMUnentitledAccessService)
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BMAccessUnentitledService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BMAccessUnentitledService
+ __OBJC_$_PROTOCOL_REFS_BMAccessUnentitledService
+ __OBJC_LABEL_PROTOCOL_$_BMAccessUnentitledService
+ __OBJC_PROTOCOL_$_BMAccessUnentitledService
+ __OBJC_PROTOCOL_REFERENCE_$_BMAccessUnentitledService
+ ___54-[BMXPCConnectionFactory _requestConnectionFromCaller]_block_invoke.95
+ ___54-[BMXPCConnectionFactory _requestConnectionFromCaller]_block_invoke.95.cold.1
+ ___55-[BMAccessServiceListener _acceptUnentitledConnection:]_block_invoke
+ ___57-[BMXPCConnectionFactory _proxyConnectionThroughCoreDuet]_block_invoke.91
+ ___57-[BMXPCConnectionFactory _proxyConnectionThroughCoreDuet]_block_invoke.91.cold.1
+ ___BMResourcesAndAccessModesListedUnderEntitlement_block_invoke.353
+ ___BMResourcesAndAccessModesListedUnderEntitlement_block_invoke_2.354
+ ___BMResourcesAndAccessModesListedUnderEntitlement_block_invoke_3.355
+ ___block_literal_global.209
+ ___block_literal_global.211
+ ___block_literal_global.231
+ ___block_literal_global.287
+ ___block_literal_global.299
+ ___block_literal_global.90
+ ___block_literal_global.94
+ ___block_literal_global.97
+ __acceptUnentitledConnection:.UnentitledInterface
+ __acceptUnentitledConnection:.onceToken
+ __os_feature_enabled_impl
+ _objc_msgSend$_acceptConnection:withInterface:
+ _objc_msgSend$_canTrustUnrestrictedEntitlementsAndSigningIdentifier
+ _objc_msgSend$allowsConnectionToEntitledAccessServiceWithDomain:
+ _objc_msgSend$allowsConnectionToUnentitledAccessServiceWithDomain:
+ _objc_msgSend$codeSigningIdentity
+ _objc_msgSend$descriptorWithKey:fromDescriptors:
+ _objc_msgSend$effectiveBoolValueForSetting:
+ _objc_msgSend$identityMatchWithSourceIdentifier:appIdentifier:
+ _objc_msgSend$init
+ _objc_msgSend$isSpotlightInlineDonationSetIdentifier:
+ _objc_msgSend$processIdentityMatchesSourceIdentifierForResource:
+ _objc_msgSend$protocol
+ _objc_msgSend$sharedConnection
+ _objc_retain_x27
+ _objc_retain_x28
+ _xpc_copy_code_signing_identity_for_token
- -[BMAccessControlPolicy allowsConnectionToAccessServiceWithDomain:]
- -[BMAccessControlPolicy allowsConnectionToAccessServiceWithDomain:].cold.1
- -[BMAccessControlPolicy allowsConnectionToAccessServiceWithDomain:].cold.2
- -[BMAccessControlPolicy(SetStoreUpdateService) allowsAccessToSetStoreUpdateServiceForSet:]
- -[BMAccessServiceListener _acceptConnection:]
- -[BMAccessServiceListener _acceptConnection:].cold.1
- -[BMProcess _canTrustApplicationIdentifierEntitlement]
- GCC_except_table14
- GCC_except_table40
- GCC_except_table47
- GCC_except_table60
- __OBJC_$_CLASS_METHODS_BMAccessControlPolicy(LegacyViewEntitlement|SyncableSets|SetStoreUpdateService|WriteService|DaemonToAgent|UseCase)
- __OBJC_$_INSTANCE_METHODS_BMAccessControlPolicy(LegacyViewEntitlement|SyncableSets|SetStoreUpdateService|WriteService|DaemonToAgent|UseCase)
- ___45-[BMAccessServiceListener _acceptConnection:]_block_invoke
- ___54-[BMXPCConnectionFactory _requestConnectionFromCaller]_block_invoke.94
- ___54-[BMXPCConnectionFactory _requestConnectionFromCaller]_block_invoke.94.cold.1
- ___57-[BMXPCConnectionFactory _proxyConnectionThroughCoreDuet]_block_invoke.90
- ___57-[BMXPCConnectionFactory _proxyConnectionThroughCoreDuet]_block_invoke.90.cold.1
- ___BMResourcesAndAccessModesListedUnderEntitlement_block_invoke.322
- ___BMResourcesAndAccessModesListedUnderEntitlement_block_invoke_2.323
- ___BMResourcesAndAccessModesListedUnderEntitlement_block_invoke_3.324
- ___block_literal_global.205
- ___block_literal_global.207
- ___block_literal_global.227
- ___block_literal_global.256
- ___block_literal_global.268
- ___block_literal_global.89
- ___block_literal_global.93
- ___block_literal_global.96
- __acceptConnection:.interface
- __acceptConnection:.onceToken
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_acceptConnection:
- _objc_msgSend$_canTrustApplicationIdentifierEntitlement
- _objc_msgSend$allowsConnectionToAccessServiceWithDomain:
- _objc_msgSend$allowsConnectionToSetStoreUpdateService
- _objc_msgSend$allowsConnectionToWriteService
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
CStrings:
+ "App.Intents.IndexedEntity"
+ "BMAccessUnentitledService"
+ "BMUnentitledAccessService"
+ "Cache missing onBehalfOf process for listener: %@ (policy: %@)"
+ "Cascade"
+ "Cascade.CachedDocument"
+ "Method not allowed for Unentitled clients"
+ "NOT "
+ "Refusing connection from %{public}@(%d) via %{public}@, no suitable interface"
+ "Refusing connection from %{public}@(%d), no suitable interface"
+ "T@\"BMAccessControlPolicy\",R,N"
+ "Unentitled client: blocking method %@ from %@"
+ "_acceptConnection:withInterface:"
+ "_acceptUnentitledConnection:"
+ "_canTrustUnrestrictedEntitlementsAndSigningIdentifier"
+ "allowsConnectionToEntitledAccessServiceWithDomain:"
+ "allowsConnectionToUnentitledAccessServiceWithDomain:"
+ "codeSigningIdentity"
+ "com.apple."
+ "descriptorWithKey:fromDescriptors:"
+ "identityMatchWithSourceIdentifier:appIdentifier:"
+ "isSpotlightInlineDonationSetIdentifier:"
+ "no-create"
+ "onBehalfOfPolicy"
+ "processIdentityMatchesSourceIdentifierForResource:"
+ "protocol"
+ "read-write-no-create"
+ "sourceIdentifier"
+ "sourceIdentifier for requested resource: %@ does %@match identity of client process: %@"
+ "sourceIdentifier is missing for requested resource: %@ from client: %@"
+ "spotlightInlineTextContent"
- "Refusing connection from %{public}@(%d) via %{public}@, process not properly entitled"
- "Refusing connection from %{public}@(%d), process not properly entitled"
- "_acceptConnection:"
- "_canTrustApplicationIdentifierEntitlement"
- "allowsAccessToSetStoreUpdateServiceForSet:"
- "allowsConnectionToAccessServiceWithDomain:"

```
