## Transparency

> `/System/Library/PrivateFrameworks/Transparency.framework/Transparency`

```diff

-948.0.0.0.1
-  __TEXT.__text: 0x2746c
-  __TEXT.__auth_stubs: 0x590
-  __TEXT.__objc_methlist: 0x2284
-  __TEXT.__cstring: 0x1748
-  __TEXT.__oslogstring: 0x1278
-  __TEXT.__const: 0x118
-  __TEXT.__gcc_except_tab: 0x2ec
-  __TEXT.__unwind_info: 0xcd4
-  __TEXT.__objc_classname: 0x488
-  __TEXT.__objc_methname: 0x4d62
-  __TEXT.__objc_methtype: 0x11b7
-  __TEXT.__objc_stubs: 0x3c00
-  __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0xdd0
-  __DATA_CONST.__objc_classlist: 0x138
+1033.62.3.0.0
+  __TEXT.__text: 0x33b5c
+  __TEXT.__auth_stubs: 0x650
+  __TEXT.__objc_methlist: 0x2b3c
+  __TEXT.__cstring: 0x1d8b
+  __TEXT.__const: 0x160
+  __TEXT.__gcc_except_tab: 0x4a0
+  __TEXT.__oslogstring: 0x16a0
+  __TEXT.__dlopen_cstrs: 0x47
+  __TEXT.__unwind_info: 0x10b8
+  __TEXT.__objc_classname: 0x59a
+  __TEXT.__objc_methname: 0x60ce
+  __TEXT.__objc_methtype: 0x1928
+  __TEXT.__objc_stubs: 0x4900
+  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__const: 0x11b0
+  __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3770
-  __DATA_CONST.__objc_selrefs: 0x1338
-  __AUTH_CONST.__cfstring: 0x2820
-  __AUTH_CONST.__objc_const: 0x1a8
-  __AUTH_CONST.__const: 0x840
+  __DATA_CONST.__objc_const: 0x4fc8
+  __DATA_CONST.__objc_selrefs: 0x1810
+  __AUTH_CONST.__cfstring: 0x2f00
+  __AUTH_CONST.__objc_const: 0x670
+  __AUTH_CONST.__const: 0xce0
   __AUTH_CONST.__objc_intobj: 0x150
-  __AUTH_CONST.__auth_got: 0x2d8
-  __AUTH.__objc_data: 0x50
+  __AUTH_CONST.__auth_got: 0x338
+  __AUTH.__objc_data: 0x370
   __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x200
-  __DATA.__objc_superrefs: 0xd8
-  __DATA.__objc_ivar: 0x214
-  __DATA.__data: 0x3f8
+  __DATA.__objc_classrefs: 0x238
+  __DATA.__objc_superrefs: 0x108
+  __DATA.__objc_ivar: 0x2ac
+  __DATA.__data: 0x590
   __DATA.__bss: 0x20
-  __DATA_DIRTY.__const: 0xe80
+  __DATA.__common: 0x8
+  __DATA_DIRTY.__const: 0x1080
   __DATA_DIRTY.__objc_const: 0x1238
   __DATA_DIRTY.__objc_data: 0xbe0
-  __DATA_DIRTY.__bss: 0x168
+  __DATA_DIRTY.__bss: 0x198
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0A272775-84A1-3053-B7C7-DFBC761108BB
-  Functions: 1099
-  Symbols:   3832
-  CStrings:  1830
+  UUID: BA760187-73BB-3B85-B23C-FFA9EA196CC7
+  Functions: 1417
+  Symbols:   4873
+  CStrings:  2266
 
Symbols:
+ +[KTIDSSession supportsSecureCoding]
+ +[KTIDStaticKeyStoreEntry supportsSecureCoding]
+ +[KTIDStaticKeyStoreHandle supportsSecureCoding]
+ +[KTLoggableData combineLoggableDatasForUI:byAdding:]
+ +[KTPeerOverride supportsSecureCoding]
+ +[KTPeerOverrides clearPeerOverride:application:]
+ +[KTPeerOverrides listPeerOverrides]
+ +[KTPeerOverrides setPeerOverride:application:state:]
+ +[KTStaticKeyPeer stripIMPrefix:]
+ +[KTStaticKeyPeer supportsSecureCoding]
+ +[KTVaudenaySAS randomValueOfLength:]
+ +[KTVaudenaySASConfiguration sha256Transparency]
+ +[TransparencyApplication idsServiceForIdentifier:]
+ +[TransparencySettings backgroundFollowupDelayPeriod]
+ +[TransparencySettings backgroundFollowupFailureCount]
+ +[TransparencySettings defaultSelfFollowupTicketLifetime]
+ +[TransparencySettings enableSelfValidationXPCActivity]
+ +[TransparencySettings queryJustMadeTimeout]
+ +[TransparencyXPCConnection invokeIDSSupportWithBlock:errorHandler:]
+ +[TransparencyXPCConnection invokeIDSXPCWithBlock:errorHandler:]
+ +[TransparencyXPCConnection retryable:counter:]
+ -[KTIDSSession .cxx_destruct]
+ -[KTIDSSession contactIdentifier]
+ -[KTIDSSession description]
+ -[KTIDSSession encodeWithCoder:]
+ -[KTIDSSession expectedPeerHandles]
+ -[KTIDSSession initWithCoder:]
+ -[KTIDSSession init]
+ -[KTIDSSession jsonObject]
+ -[KTIDSSession markAsVerified:]
+ -[KTIDSSession markContactAsVerified:error:]
+ -[KTIDSSession peerAccountIdentity]
+ -[KTIDSSession peerDisconnected]
+ -[KTIDSSession peerHandle]
+ -[KTIDSSession sasCode]
+ -[KTIDSSession sessionExpire]
+ -[KTIDSSession sessionID]
+ -[KTIDSSession setContactIdentifier:]
+ -[KTIDSSession setExpectedPeerHandles:]
+ -[KTIDSSession setPeerAccountIdentity:]
+ -[KTIDSSession setPeerDisconnected:]
+ -[KTIDSSession setPeerHandle:]
+ -[KTIDSSession setSasCode:]
+ -[KTIDSSession setSessionExpire:]
+ -[KTIDSSession setSessionID:]
+ -[KTIDSSession setState:]
+ -[KTIDSSession state]
+ -[KTIDStaticKeyStore addMapping:forKTId:error:]
+ -[KTIDStaticKeyStore addStaticKeyEntry:contactServerPath:contactIdentifier:error:]
+ -[KTIDStaticKeyStore findByContact:error:]
+ -[KTIDStaticKeyStore findByContactIdentifier:error:]
+ -[KTIDStaticKeyStore findByIdentifier:error:]
+ -[KTIDStaticKeyStore findKeyByContactsServerPath:contactIdentifier:error:]
+ -[KTIDStaticKeyStore findKeyByHandle:error:]
+ -[KTIDStaticKeyStore listKTID:]
+ -[KTIDStaticKeyStore mappings:error:]
+ -[KTIDStaticKeyStore removeEntryByContact:error:]
+ -[KTIDStaticKeyStore removeEntryByContactIdentifier:error:]
+ -[KTIDStaticKeyStore removeEntryByKDID:error:]
+ -[KTIDStaticKeyStore removeMapping:forKTId:error:]
+ -[KTIDStaticKeyStore resetCloudKit:]
+ -[KTIDStaticKeyStore setContactServerPath:forKTId:error:]
+ -[KTIDStaticKeyStore setErrorCode:forMapping:error:]
+ -[KTIDStaticKeyStore setupCloudSchema:error:]
+ -[KTIDStaticKeyStore triggerSync:]
+ -[KTIDStaticKeyStore updateStaticKeyEntry:contact:error:]
+ -[KTIDStaticKeyStore updateStaticKeyEntry:contactServerPath:contactIdentifier:mappings:error:]
+ -[KTIDStaticKeyStore validateByContact:error:]
+ -[KTIDStaticKeyStore validateByContactIdentifier:error:]
+ -[KTIDStaticKeyStore validateByIdentifier:error:]
+ -[KTIDStaticKeyStoreEntry .cxx_destruct]
+ -[KTIDStaticKeyStoreEntry contactExternalURI]
+ -[KTIDStaticKeyStoreEntry contactIdentifier]
+ -[KTIDStaticKeyStoreEntry contactServerPath]
+ -[KTIDStaticKeyStoreEntry copyWithZone:]
+ -[KTIDStaticKeyStoreEntry encodeWithCoder:]
+ -[KTIDStaticKeyStoreEntry handles]
+ -[KTIDStaticKeyStoreEntry initWithCoder:]
+ -[KTIDStaticKeyStoreEntry init]
+ -[KTIDStaticKeyStoreEntry mappings]
+ -[KTIDStaticKeyStoreEntry publicKeyID]
+ -[KTIDStaticKeyStoreEntry setContactExternalURI:]
+ -[KTIDStaticKeyStoreEntry setContactIdentifier:]
+ -[KTIDStaticKeyStoreEntry setContactServerPath:]
+ -[KTIDStaticKeyStoreEntry setHandles:]
+ -[KTIDStaticKeyStoreEntry setMappings:]
+ -[KTIDStaticKeyStoreEntry setPublicKeyID:]
+ -[KTIDStaticKeyStoreEntry valid]
+ -[KTIDStaticKeyStoreHandle .cxx_destruct]
+ -[KTIDStaticKeyStoreHandle copyWithZone:]
+ -[KTIDStaticKeyStoreHandle encodeWithCoder:]
+ -[KTIDStaticKeyStoreHandle errorCode]
+ -[KTIDStaticKeyStoreHandle handle]
+ -[KTIDStaticKeyStoreHandle initWithCoder:]
+ -[KTIDStaticKeyStoreHandle setErrorCode:]
+ -[KTIDStaticKeyStoreHandle setHandle:]
+ -[KTIDStaticKeyStoreHandle setValid:]
+ -[KTIDStaticKeyStoreHandle setValidationDate:]
+ -[KTIDStaticKeyStoreHandle valid]
+ -[KTIDStaticKeyStoreHandle validationDate]
+ -[KTOptInState everOptIn]
+ -[KTOptInState setEverOptIn:]
+ -[KTPeerOverride description]
+ -[KTPeerOverride encodeWithCoder:]
+ -[KTPeerOverride initWithCoder:]
+ -[KTPeerOverride setUiStatus:]
+ -[KTPeerOverride uiStatus]
+ -[KTSelfStatusResult everOptIn]
+ -[KTSelfStatusResult setEverOptIn:]
+ -[KTStaticKeyPeer .cxx_destruct]
+ -[KTStaticKeyPeer encodeWithCoder:]
+ -[KTStaticKeyPeer initWithCoder:]
+ -[KTStaticKeyPeer initWithPeer:]
+ -[KTStaticKeyPeer lastUsedAddressOfMe]
+ -[KTStaticKeyPeer otherNamesForPeer]
+ -[KTStaticKeyPeer peer]
+ -[KTStaticKeyPeer setLastUsedAddressOfMe:]
+ -[KTStaticKeyPeer setOtherNamesForPeer:]
+ -[KTStaticKeyPeer setPeer:]
+ -[KTStatus status:]
+ -[KTVaudenaySAS .cxx_destruct]
+ -[KTVaudenaySAS acceptorInfo]
+ -[KTVaudenaySAS acceptorRandom]
+ -[KTVaudenaySAS config]
+ -[KTVaudenaySAS initAcceptorWithPublic:configuration:]
+ -[KTVaudenaySAS initInitiatorWithPublic:configuration:]
+ -[KTVaudenaySAS init]
+ -[KTVaudenaySAS initiatorInfo]
+ -[KTVaudenaySAS initiatorRandom]
+ -[KTVaudenaySAS initiator]
+ -[KTVaudenaySAS selfRandom]
+ -[KTVaudenaySAS sentUndisclosedRandom]
+ -[KTVaudenaySAS setAcceptorInfo:]
+ -[KTVaudenaySAS setAcceptorRandom:]
+ -[KTVaudenaySAS setConfig:]
+ -[KTVaudenaySAS setInitiator:]
+ -[KTVaudenaySAS setInitiatorInfo:]
+ -[KTVaudenaySAS setInitiatorRandom:]
+ -[KTVaudenaySAS setInitiatorUndisclosedRandom:]
+ -[KTVaudenaySAS setPeerPublic:]
+ -[KTVaudenaySAS setPeerRandom:]
+ -[KTVaudenaySAS setSentUndisclosedRandom:]
+ -[KTVaudenaySAS shortAuthenticationString]
+ -[KTVaudenaySAS undisclosedInitiatorRandom]
+ -[KTVaudenaySAS undisclosedInitiatorValue:]
+ -[KTVaudenaySASConfiguration .cxx_destruct]
+ -[KTVaudenaySASConfiguration di]
+ -[KTVaudenaySASConfiguration digestPrefix]
+ -[KTVaudenaySASConfiguration initWithName:digestPrefix:shortCodeLength:digest:]
+ -[KTVaudenaySASConfiguration name]
+ -[KTVaudenaySASConfiguration setDi:]
+ -[KTVaudenaySASConfiguration setDigestPrefix:]
+ -[KTVaudenaySASConfiguration setName:]
+ -[KTVaudenaySASConfiguration setShortCodeLength:]
+ -[KTVaudenaySASConfiguration setShortCodeMod10:]
+ -[KTVaudenaySASConfiguration shortCodeLength]
+ -[KTVaudenaySASConfiguration shortCodeMod10]
+ -[KTVerificationInfo optedIn]
+ -[KTVerificationInfo setOptedIn:]
+ -[KTVerifierResult setStaticAccountKeyStatus:]
+ -[KTVerifierResult staticAccountKeyStatus]
+ -[KTVerifierResult updateWithStaticKeyEnforced:isFailureIgnoredForDate:]
+ -[TransparencyDaemon transparencyIDMSDeviceList:]
+ -[TransparencySettings systemFailureFeatureEnabled]
+ -[TransparencyStaticKey .cxx_destruct]
+ -[TransparencyStaticKey accountIdentity]
+ -[TransparencyStaticKey deleteKTSession:complete:]
+ -[TransparencyStaticKey getKTSessionByHandle:complete:]
+ -[TransparencyStaticKey getKTSessionByID:complete:]
+ -[TransparencyStaticKey listKTSessions:]
+ -[TransparencyStaticKey setAccountIdentity:]
+ -[TransparencyStaticKey setupKTSession:complete:]
+ -[TransparencyStaticKey updateStaticKeyDatabaseForContact:peerPublicAccountIdentity:complete:]
+ GCC_except_table102
+ GCC_except_table107
+ GCC_except_table112
+ GCC_except_table116
+ GCC_except_table117
+ GCC_except_table122
+ GCC_except_table138
+ GCC_except_table23
+ GCC_except_table35
+ GCC_except_table4
+ GCC_except_table45
+ GCC_except_table46
+ GCC_except_table48
+ GCC_except_table54
+ GCC_except_table59
+ GCC_except_table6
+ GCC_except_table60
+ GCC_except_table67
+ GCC_except_table70
+ GCC_except_table79
+ GCC_except_table85
+ GCC_except_table90
+ GCC_except_table96
+ _ContactsLibraryCore.frameworkLibrary
+ _KTIDStaticKeyStoreEntryChanged
+ _KTIDStaticKeyStoreEntryIdentifier
+ _KTStaticKeyPeerValidateResultGetString
+ _NSCocoaErrorDomain
+ _OBJC_CLASS_$_KTIDSSession
+ _OBJC_CLASS_$_KTIDStaticKeyStore
+ _OBJC_CLASS_$_KTIDStaticKeyStoreEntry
+ _OBJC_CLASS_$_KTIDStaticKeyStoreHandle
+ _OBJC_CLASS_$_KTPeerOverride
+ _OBJC_CLASS_$_KTPeerOverrides
+ _OBJC_CLASS_$_KTStaticKeyPeer
+ _OBJC_CLASS_$_KTVaudenaySAS
+ _OBJC_CLASS_$_KTVaudenaySASConfiguration
+ _OBJC_CLASS_$_TransparencyStaticKey
+ _OBJC_IVAR_$_KTIDSSession._contactIdentifier
+ _OBJC_IVAR_$_KTIDSSession._expectedPeerHandles
+ _OBJC_IVAR_$_KTIDSSession._peerAccountIdentity
+ _OBJC_IVAR_$_KTIDSSession._peerDisconnected
+ _OBJC_IVAR_$_KTIDSSession.peerHandle
+ _OBJC_IVAR_$_KTIDSSession.sasCode
+ _OBJC_IVAR_$_KTIDSSession.sessionExpire
+ _OBJC_IVAR_$_KTIDSSession.sessionID
+ _OBJC_IVAR_$_KTIDSSession.state
+ _OBJC_IVAR_$_KTIDStaticKeyStoreEntry.contactExternalURI
+ _OBJC_IVAR_$_KTIDStaticKeyStoreEntry.contactIdentifier
+ _OBJC_IVAR_$_KTIDStaticKeyStoreEntry.handles
+ _OBJC_IVAR_$_KTIDStaticKeyStoreEntry.publicKeyID
+ _OBJC_IVAR_$_KTIDStaticKeyStoreHandle._errorCode
+ _OBJC_IVAR_$_KTIDStaticKeyStoreHandle._handle
+ _OBJC_IVAR_$_KTIDStaticKeyStoreHandle._valid
+ _OBJC_IVAR_$_KTIDStaticKeyStoreHandle._validationDate
+ _OBJC_IVAR_$_KTOptInState._everOptIn
+ _OBJC_IVAR_$_KTPeerOverride._uiStatus
+ _OBJC_IVAR_$_KTSelfStatusResult._everOptIn
+ _OBJC_IVAR_$_KTStaticKeyPeer._lastUsedAddressOfMe
+ _OBJC_IVAR_$_KTStaticKeyPeer._otherNames
+ _OBJC_IVAR_$_KTStaticKeyPeer._peer
+ _OBJC_IVAR_$_KTVaudenaySAS._acceptorInfo
+ _OBJC_IVAR_$_KTVaudenaySAS._acceptorRandom
+ _OBJC_IVAR_$_KTVaudenaySAS._config
+ _OBJC_IVAR_$_KTVaudenaySAS._initiator
+ _OBJC_IVAR_$_KTVaudenaySAS._initiatorInfo
+ _OBJC_IVAR_$_KTVaudenaySAS._initiatorRandom
+ _OBJC_IVAR_$_KTVaudenaySAS._sentUndisclosedRandom
+ _OBJC_IVAR_$_KTVaudenaySASConfiguration._di
+ _OBJC_IVAR_$_KTVaudenaySASConfiguration._digestPrefix
+ _OBJC_IVAR_$_KTVaudenaySASConfiguration._name
+ _OBJC_IVAR_$_KTVaudenaySASConfiguration._shortCodeLength
+ _OBJC_IVAR_$_KTVaudenaySASConfiguration._shortCodeMod10
+ _OBJC_IVAR_$_KTVerificationInfo._optedIn
+ _OBJC_IVAR_$_KTVerifierResult._staticAccountKeyStatus
+ _OBJC_IVAR_$_TransparencyStaticKey._accountIdentity
+ _OBJC_METACLASS_$_KTIDSSession
+ _OBJC_METACLASS_$_KTIDStaticKeyStore
+ _OBJC_METACLASS_$_KTIDStaticKeyStoreEntry
+ _OBJC_METACLASS_$_KTIDStaticKeyStoreHandle
+ _OBJC_METACLASS_$_KTPeerOverride
+ _OBJC_METACLASS_$_KTPeerOverrides
+ _OBJC_METACLASS_$_KTStaticKeyPeer
+ _OBJC_METACLASS_$_KTVaudenaySAS
+ _OBJC_METACLASS_$_KTVaudenaySASConfiguration
+ _OBJC_METACLASS_$_TransparencyStaticKey
+ __OBJC_$_CLASS_METHODS_KTIDSSession
+ __OBJC_$_CLASS_METHODS_KTIDStaticKeyStoreEntry
+ __OBJC_$_CLASS_METHODS_KTIDStaticKeyStoreHandle
+ __OBJC_$_CLASS_METHODS_KTPeerOverride
+ __OBJC_$_CLASS_METHODS_KTPeerOverrides
+ __OBJC_$_CLASS_METHODS_KTStaticKeyPeer
+ __OBJC_$_CLASS_METHODS_KTVaudenaySAS
+ __OBJC_$_CLASS_METHODS_KTVaudenaySASConfiguration
+ __OBJC_$_CLASS_PROP_LIST_KTIDSSession
+ __OBJC_$_CLASS_PROP_LIST_KTIDStaticKeyStoreEntry
+ __OBJC_$_CLASS_PROP_LIST_KTIDStaticKeyStoreHandle
+ __OBJC_$_CLASS_PROP_LIST_KTPeerOverride
+ __OBJC_$_CLASS_PROP_LIST_KTStaticKeyPeer
+ __OBJC_$_INSTANCE_METHODS_KTIDSSession
+ __OBJC_$_INSTANCE_METHODS_KTIDStaticKeyStore
+ __OBJC_$_INSTANCE_METHODS_KTIDStaticKeyStoreEntry
+ __OBJC_$_INSTANCE_METHODS_KTIDStaticKeyStoreHandle
+ __OBJC_$_INSTANCE_METHODS_KTPeerOverride
+ __OBJC_$_INSTANCE_METHODS_KTStaticKeyPeer
+ __OBJC_$_INSTANCE_METHODS_KTVaudenaySAS
+ __OBJC_$_INSTANCE_METHODS_KTVaudenaySASConfiguration
+ __OBJC_$_INSTANCE_METHODS_TransparencyStaticKey
+ __OBJC_$_INSTANCE_VARIABLES_KTIDSSession
+ __OBJC_$_INSTANCE_VARIABLES_KTIDStaticKeyStoreEntry
+ __OBJC_$_INSTANCE_VARIABLES_KTIDStaticKeyStoreHandle
+ __OBJC_$_INSTANCE_VARIABLES_KTPeerOverride
+ __OBJC_$_INSTANCE_VARIABLES_KTStaticKeyPeer
+ __OBJC_$_INSTANCE_VARIABLES_KTVaudenaySAS
+ __OBJC_$_INSTANCE_VARIABLES_KTVaudenaySASConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_TransparencyStaticKey
+ __OBJC_$_PROP_LIST_KTIDSSession
+ __OBJC_$_PROP_LIST_KTIDStaticKeyStore
+ __OBJC_$_PROP_LIST_KTIDStaticKeyStoreEntry
+ __OBJC_$_PROP_LIST_KTIDStaticKeyStoreHandle
+ __OBJC_$_PROP_LIST_KTPeerOverride
+ __OBJC_$_PROP_LIST_KTStaticKeyPeer
+ __OBJC_$_PROP_LIST_KTVaudenaySAS
+ __OBJC_$_PROP_LIST_KTVaudenaySASConfiguration
+ __OBJC_$_PROP_LIST_TransparencyDaemon
+ __OBJC_$_PROP_LIST_TransparencyStaticKey
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_KTIDStaticKeyStoreProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_KTStatusProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TransparencyIDMSDeviceProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TransparencydIDSProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_KTIDStaticKeyStoreProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_KTStatusProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TransparencyIDMSDeviceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TransparencydIDSProtocol
+ __OBJC_$_PROTOCOL_REFS_KTIDStaticKeyStoreProtocol
+ __OBJC_$_PROTOCOL_REFS_TransparencyIDMSDeviceProtocol
+ __OBJC_CLASS_PROTOCOLS_$_KTIDSSession
+ __OBJC_CLASS_PROTOCOLS_$_KTIDStaticKeyStore
+ __OBJC_CLASS_PROTOCOLS_$_KTIDStaticKeyStoreEntry
+ __OBJC_CLASS_PROTOCOLS_$_KTIDStaticKeyStoreHandle
+ __OBJC_CLASS_PROTOCOLS_$_KTPeerOverride
+ __OBJC_CLASS_PROTOCOLS_$_KTStaticKeyPeer
+ __OBJC_CLASS_PROTOCOLS_$_KTStatus
+ __OBJC_CLASS_PROTOCOLS_$_TransparencyDaemon
+ __OBJC_CLASS_RO_$_KTIDSSession
+ __OBJC_CLASS_RO_$_KTIDStaticKeyStore
+ __OBJC_CLASS_RO_$_KTIDStaticKeyStoreEntry
+ __OBJC_CLASS_RO_$_KTIDStaticKeyStoreHandle
+ __OBJC_CLASS_RO_$_KTPeerOverride
+ __OBJC_CLASS_RO_$_KTPeerOverrides
+ __OBJC_CLASS_RO_$_KTStaticKeyPeer
+ __OBJC_CLASS_RO_$_KTVaudenaySAS
+ __OBJC_CLASS_RO_$_KTVaudenaySASConfiguration
+ __OBJC_CLASS_RO_$_TransparencyStaticKey
+ __OBJC_LABEL_PROTOCOL_$_KTIDStaticKeyStoreProtocol
+ __OBJC_LABEL_PROTOCOL_$_KTStatusProtocol
+ __OBJC_LABEL_PROTOCOL_$_TransparencyIDMSDeviceProtocol
+ __OBJC_METACLASS_RO_$_KTIDSSession
+ __OBJC_METACLASS_RO_$_KTIDStaticKeyStore
+ __OBJC_METACLASS_RO_$_KTIDStaticKeyStoreEntry
+ __OBJC_METACLASS_RO_$_KTIDStaticKeyStoreHandle
+ __OBJC_METACLASS_RO_$_KTPeerOverride
+ __OBJC_METACLASS_RO_$_KTPeerOverrides
+ __OBJC_METACLASS_RO_$_KTStaticKeyPeer
+ __OBJC_METACLASS_RO_$_KTVaudenaySAS
+ __OBJC_METACLASS_RO_$_KTVaudenaySASConfiguration
+ __OBJC_METACLASS_RO_$_TransparencyStaticKey
+ __OBJC_PROTOCOL_$_KTIDStaticKeyStoreProtocol
+ __OBJC_PROTOCOL_$_KTStatusProtocol
+ __OBJC_PROTOCOL_$_TransparencyIDMSDeviceProtocol
+ ___125-[TransparencyDaemon replaySelfValidate:application:pcsAccountKey:queryRequest:queryResponse:responseTime:completionHandler:]_block_invoke.318
+ ___19-[KTStatus status:]_block_invoke
+ ___19-[KTStatus status:]_block_invoke_2
+ ___19-[KTStatus status:]_block_invoke_3
+ ___19-[KTStatus status:]_block_invoke_4
+ ___22-[KTStatus getStatus:]_block_invoke.241
+ ___22-[KTStatus getStatus:]_block_invoke.244
+ ___22-[KTStatus getStatus:]_block_invoke_2.245
+ ___26-[KTStatus getSelfStatus:]_block_invoke.250
+ ___26-[KTStatus getSelfStatus:]_block_invoke.253
+ ___26-[KTStatus getSelfStatus:]_block_invoke_2.254
+ ___31-[KTIDStaticKeyStore listKTID:]_block_invoke
+ ___31-[KTIDStaticKeyStore listKTID:]_block_invoke_2
+ ___31-[KTIDStaticKeyStore listKTID:]_block_invoke_3
+ ___31-[KTIDStaticKeyStore listKTID:]_block_invoke_4
+ ___31-[KTOptInManager getOptInState]_block_invoke.218
+ ___31-[KTOptInManager getOptInState]_block_invoke.222
+ ___31-[KTOptInManager getOptInState]_block_invoke.227
+ ___31-[KTOptInManager getOptInState]_block_invoke_2.223
+ ___31-[KTOptInManager getOptInState]_block_invoke_2.230
+ ___34-[KTIDStaticKeyStore triggerSync:]_block_invoke
+ ___34-[KTIDStaticKeyStore triggerSync:]_block_invoke_2
+ ___34-[KTIDStaticKeyStore triggerSync:]_block_invoke_3
+ ___34-[KTIDStaticKeyStore triggerSync:]_block_invoke_4
+ ___36+[KTPeerOverrides listPeerOverrides]_block_invoke
+ ___36+[KTPeerOverrides listPeerOverrides]_block_invoke_2
+ ___36+[KTPeerOverrides listPeerOverrides]_block_invoke_3
+ ___36+[KTPeerOverrides listPeerOverrides]_block_invoke_4
+ ___36-[KTIDStaticKeyStore resetCloudKit:]_block_invoke
+ ___36-[KTIDStaticKeyStore resetCloudKit:]_block_invoke_2
+ ___36-[KTIDStaticKeyStore resetCloudKit:]_block_invoke_3
+ ___36-[KTIDStaticKeyStore resetCloudKit:]_block_invoke_4
+ ___40-[TransparencyDaemon getAllOptInStates:]_block_invoke.379
+ ___40-[TransparencyStaticKey listKTSessions:]_block_invoke
+ ___40-[TransparencyStaticKey listKTSessions:]_block_invoke.319
+ ___40-[TransparencyStaticKey listKTSessions:]_block_invoke_2
+ ___40-[TransparencyStaticKey listKTSessions:]_block_invoke_2.321
+ ___40-[TransparencyStaticKey listKTSessions:]_block_invoke_3
+ ___42-[KTIDStaticKeyStore findByContact:error:]_block_invoke
+ ___42-[KTIDStaticKeyStore findByContact:error:]_block_invoke.154
+ ___42-[KTIDStaticKeyStore findByContact:error:]_block_invoke_2
+ ___42-[KTIDStaticKeyStore findByContact:error:]_block_invoke_2.155
+ ___42-[KTIDStaticKeyStore findByContact:error:]_block_invoke_3
+ ___43+[KTOptInManager getOptInState:completion:]_block_invoke.207
+ ___43+[KTOptInManager getOptInState:completion:]_block_invoke_2.208
+ ___44-[KTIDStaticKeyStore findKeyByHandle:error:]_block_invoke
+ ___44-[KTIDStaticKeyStore findKeyByHandle:error:]_block_invoke.142
+ ___44-[KTIDStaticKeyStore findKeyByHandle:error:]_block_invoke_2
+ ___44-[KTIDStaticKeyStore findKeyByHandle:error:]_block_invoke_2.143
+ ___44-[KTIDStaticKeyStore findKeyByHandle:error:]_block_invoke_3
+ ___45-[KTIDStaticKeyStore findByIdentifier:error:]_block_invoke
+ ___45-[KTIDStaticKeyStore findByIdentifier:error:]_block_invoke_2
+ ___45-[KTIDStaticKeyStore findByIdentifier:error:]_block_invoke_3
+ ___45-[KTIDStaticKeyStore findByIdentifier:error:]_block_invoke_4
+ ___45-[KTIDStaticKeyStore setupCloudSchema:error:]_block_invoke
+ ___45-[KTIDStaticKeyStore setupCloudSchema:error:]_block_invoke_2
+ ___45-[KTIDStaticKeyStore setupCloudSchema:error:]_block_invoke_3
+ ___45-[KTIDStaticKeyStore setupCloudSchema:error:]_block_invoke_4
+ ___45-[TransparencyDaemon getOptInState:complete:]_block_invoke.370
+ ___46+[TransparencySettings jsonDictFromPlistDict:]_block_invoke.127
+ ___46-[KTIDStaticKeyStore removeEntryByKDID:error:]_block_invoke
+ ___46-[KTIDStaticKeyStore removeEntryByKDID:error:]_block_invoke.123
+ ___46-[KTIDStaticKeyStore removeEntryByKDID:error:]_block_invoke_2
+ ___46-[KTIDStaticKeyStore removeEntryByKDID:error:]_block_invoke_2.125
+ ___46-[KTIDStaticKeyStore removeEntryByKDID:error:]_block_invoke_3
+ ___46-[KTStatus ignoreFailedEvent:completionBlock:]_block_invoke.278
+ ___46-[KTStatus ignoreFailedEvent:completionBlock:]_block_invoke.281
+ ___46-[KTStatus ignoreFailedEvent:completionBlock:]_block_invoke_2.282
+ ___47-[KTStatus ignoreFailedEvents:completionBlock:]_block_invoke.287
+ ___47-[KTStatus ignoreFailedEvents:completionBlock:]_block_invoke.290
+ ___47-[KTStatus ignoreFailedEvents:completionBlock:]_block_invoke_2.291
+ ___47-[TransparencyDaemon transparencyCloudDevices:]_block_invoke.353
+ ___48-[KTOptInManager getOptInState:completionBlock:]_block_invoke.235
+ ___48-[KTOptInManager getOptInState:completionBlock:]_block_invoke.238
+ ___48-[KTOptInManager getOptInState:completionBlock:]_block_invoke_2.239
+ ___48-[KTStatus errorForFailedEvent:completionBlock:]_block_invoke.259
+ ___48-[KTStatus errorForFailedEvent:completionBlock:]_block_invoke.262
+ ___48-[KTStatus errorForFailedEvent:completionBlock:]_block_invoke_2.264
+ ___49+[KTPeerOverrides clearPeerOverride:application:]_block_invoke
+ ___49+[KTPeerOverrides clearPeerOverride:application:]_block_invoke_2
+ ___49+[KTPeerOverrides clearPeerOverride:application:]_block_invoke_3
+ ___49-[KTIDStaticKeyStore removeEntryByContact:error:]_block_invoke
+ ___49-[KTIDStaticKeyStore removeEntryByContact:error:]_block_invoke.136
+ ___49-[KTIDStaticKeyStore removeEntryByContact:error:]_block_invoke_2
+ ___49-[KTIDStaticKeyStore removeEntryByContact:error:]_block_invoke_2.137
+ ___49-[KTIDStaticKeyStore removeEntryByContact:error:]_block_invoke_3
+ ___49-[KTIDStaticKeyStore validateByIdentifier:error:]_block_invoke
+ ___49-[KTIDStaticKeyStore validateByIdentifier:error:]_block_invoke_2
+ ___49-[KTIDStaticKeyStore validateByIdentifier:error:]_block_invoke_3
+ ___49-[KTIDStaticKeyStore validateByIdentifier:error:]_block_invoke_4
+ ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke.333
+ ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke_2.335
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke.309
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.311
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_3
+ ___49-[TransparencyStaticKey setupKTSession:complete:]_block_invoke
+ ___49-[TransparencyStaticKey setupKTSession:complete:]_block_invoke.303
+ ___49-[TransparencyStaticKey setupKTSession:complete:]_block_invoke_2
+ ___49-[TransparencyStaticKey setupKTSession:complete:]_block_invoke_2.306
+ ___49-[TransparencyStaticKey setupKTSession:complete:]_block_invoke_3
+ ___50-[KTStatus errorsForFailedEvents:completionBlock:]_block_invoke.269
+ ___50-[KTStatus errorsForFailedEvents:completionBlock:]_block_invoke.272
+ ___50-[KTStatus errorsForFailedEvents:completionBlock:]_block_invoke_2.273
+ ___50-[TransparencyDaemon transparencyFetchPublicKeys:]_block_invoke.321
+ ___50-[TransparencyDaemon transparencyIDSRegistration:]_block_invoke.338
+ ___50-[TransparencyStaticKey deleteKTSession:complete:]_block_invoke
+ ___50-[TransparencyStaticKey deleteKTSession:complete:]_block_invoke.312
+ ___50-[TransparencyStaticKey deleteKTSession:complete:]_block_invoke_2
+ ___50-[TransparencyStaticKey deleteKTSession:complete:]_block_invoke_2.314
+ ___50-[TransparencyStaticKey deleteKTSession:complete:]_block_invoke_3
+ ___51-[TransparencyStaticKey getKTSessionByID:complete:]_block_invoke
+ ___51-[TransparencyStaticKey getKTSessionByID:complete:]_block_invoke.332
+ ___51-[TransparencyStaticKey getKTSessionByID:complete:]_block_invoke_2
+ ___51-[TransparencyStaticKey getKTSessionByID:complete:]_block_invoke_2.334
+ ___51-[TransparencyStaticKey getKTSessionByID:complete:]_block_invoke_3
+ ___52-[KTIDStaticKeyStore findByContactIdentifier:error:]_block_invoke
+ ___52-[KTIDStaticKeyStore findByContactIdentifier:error:]_block_invoke.148
+ ___52-[KTIDStaticKeyStore findByContactIdentifier:error:]_block_invoke_2
+ ___52-[KTIDStaticKeyStore findByContactIdentifier:error:]_block_invoke_2.149
+ ___52-[KTIDStaticKeyStore findByContactIdentifier:error:]_block_invoke_3
+ ___52-[KTIDStaticKeyStore setErrorCode:forMapping:error:]_block_invoke
+ ___52-[KTIDStaticKeyStore setErrorCode:forMapping:error:]_block_invoke_2
+ ___52-[KTIDStaticKeyStore setErrorCode:forMapping:error:]_block_invoke_3
+ ___52-[KTIDStaticKeyStore setErrorCode:forMapping:error:]_block_invoke_4
+ ___53+[KTPeerOverrides setPeerOverride:application:state:]_block_invoke
+ ___53+[KTPeerOverrides setPeerOverride:application:state:]_block_invoke_2
+ ___53+[KTPeerOverrides setPeerOverride:application:state:]_block_invoke_3
+ ___55-[TransparencyStaticKey getKTSessionByHandle:complete:]_block_invoke
+ ___55-[TransparencyStaticKey getKTSessionByHandle:complete:]_block_invoke.326
+ ___55-[TransparencyStaticKey getKTSessionByHandle:complete:]_block_invoke_2
+ ___55-[TransparencyStaticKey getKTSessionByHandle:complete:]_block_invoke_2.327
+ ___55-[TransparencyStaticKey getKTSessionByHandle:complete:]_block_invoke_3
+ ___56-[KTIDStaticKeyStore validateByContactIdentifier:error:]_block_invoke
+ ___56-[KTIDStaticKeyStore validateByContactIdentifier:error:]_block_invoke_2
+ ___56-[KTIDStaticKeyStore validateByContactIdentifier:error:]_block_invoke_3
+ ___56-[KTIDStaticKeyStore validateByContactIdentifier:error:]_block_invoke_4
+ ___56-[KTOptInManager setOptInState:detailedCompletionBlock:]_block_invoke.243
+ ___56-[KTOptInManager setOptInState:detailedCompletionBlock:]_block_invoke.246
+ ___56-[KTOptInManager setOptInState:detailedCompletionBlock:]_block_invoke_2.247
+ ___56-[KTOptInManager setOptInState:detailedCompletionBlock:]_block_invoke_3
+ ___57-[KTIDStaticKeyStore updateStaticKeyEntry:contact:error:]_block_invoke
+ ___57-[KTIDStaticKeyStore updateStaticKeyEntry:contact:error:]_block_invoke_2
+ ___57-[KTIDStaticKeyStore updateStaticKeyEntry:contact:error:]_block_invoke_3
+ ___57-[KTIDStaticKeyStore updateStaticKeyEntry:contact:error:]_block_invoke_4
+ ___57-[TransparencyDaemon transparencyDumpKTRegistrationData:]_block_invoke.344
+ ___57-[TransparencyDaemon transparencyTriggerIDSRegistration:]_block_invoke.324
+ ___58-[TransparencyDaemon getOptInForURI:application:complete:]_block_invoke.373
+ ___58-[TransparencyDaemon transparencyClearKTRegistrationData:]_block_invoke.350
+ ___59-[KTIDStaticKeyStore removeEntryByContactIdentifier:error:]_block_invoke
+ ___59-[KTIDStaticKeyStore removeEntryByContactIdentifier:error:]_block_invoke.130
+ ___59-[KTIDStaticKeyStore removeEntryByContactIdentifier:error:]_block_invoke_2
+ ___59-[KTIDStaticKeyStore removeEntryByContactIdentifier:error:]_block_invoke_2.131
+ ___59-[KTIDStaticKeyStore removeEntryByContactIdentifier:error:]_block_invoke_3
+ ___59-[KTOptInManager changeOptInState:detailedCompletionBlock:]_block_invoke.252
+ ___59-[KTOptInManager changeOptInState:detailedCompletionBlock:]_block_invoke.255
+ ___59-[KTOptInManager changeOptInState:detailedCompletionBlock:]_block_invoke_2.256
+ ___59-[KTOptInManager changeOptInState:detailedCompletionBlock:]_block_invoke_3
+ ___59-[TransparencyDaemon getOptInStateForApplication:complete:]_block_invoke.382
+ ___59-[TransparencyDaemon transparencyGetKTSignatures:complete:]_block_invoke.347
+ ___60-[TransparencyDaemon changeOptInState:application:complete:]_block_invoke.367
+ ___60-[TransparencyDaemon transparencyTriggerOperation:complete:]_block_invoke.364
+ ___61-[TransparencyDaemon transparencyCheckKTAccountKey:complete:]_block_invoke.327
+ ___63-[TransparencyDaemon transparencyPerformRegistrationSignature:]_block_invoke.341
+ ___64+[TransparencyXPCConnection invokeIDSXPCWithBlock:errorHandler:]_block_invoke
+ ___64+[TransparencyXPCConnection invokeIDSXPCWithBlock:errorHandler:]_block_invoke.50
+ ___64+[TransparencyXPCConnection invokeIDSXPCWithBlock:errorHandler:]_block_invoke.53
+ ___64+[TransparencyXPCConnection invokeIDSXPCWithBlock:errorHandler:]_block_invoke_2
+ ___65-[TransparencyDaemon clearOptInStateForURI:application:complete:]_block_invoke.385
+ ___68+[TransparencyXPCConnection invokeIDSSupportWithBlock:errorHandler:]_block_invoke
+ ___68+[TransparencyXPCConnection invokeIDSSupportWithBlock:errorHandler:]_block_invoke.58
+ ___68+[TransparencyXPCConnection invokeIDSSupportWithBlock:errorHandler:]_block_invoke.61
+ ___68+[TransparencyXPCConnection invokeIDSSupportWithBlock:errorHandler:]_block_invoke_2
+ ___69-[TransparencyDaemon transparencyCloudDeviceAdd:clientData:complete:]_block_invoke.388
+ ___72-[KTVerifierResult updateWithStaticKeyEnforced:isFailureIgnoredForDate:]_block_invoke
+ ___72-[TransparencyDaemon transparencyCloudDeviceRemove:clientData:complete:]_block_invoke.391
+ ___73+[TransparencyXPCConnection invokeAccountsSupportWithBlock:errorHandler:]_block_invoke.66
+ ___76+[TransparencyXPCConnection invokeXPCSynchronousCallWithBlock:errorHandler:]_block_invoke
+ ___76+[TransparencyXPCConnection invokeXPCSynchronousCallWithBlock:errorHandler:]_block_invoke_2
+ ___77-[TransparencyDaemon setOptInForURI:application:state:smtTimestamp:complete:]_block_invoke.376
+ ___94-[KTIDStaticKeyStore updateStaticKeyEntry:contactServerPath:contactIdentifier:mappings:error:]_block_invoke
+ ___94-[KTIDStaticKeyStore updateStaticKeyEntry:contactServerPath:contactIdentifier:mappings:error:]_block_invoke_2
+ ___94-[KTIDStaticKeyStore updateStaticKeyEntry:contactServerPath:contactIdentifier:mappings:error:]_block_invoke_3
+ ___94-[KTIDStaticKeyStore updateStaticKeyEntry:contactServerPath:contactIdentifier:mappings:error:]_block_invoke_4
+ ___94-[TransparencyStaticKey updateStaticKeyDatabaseForContact:peerPublicAccountIdentity:complete:]_block_invoke
+ ___94-[TransparencyStaticKey updateStaticKeyDatabaseForContact:peerPublicAccountIdentity:complete:]_block_invoke.339
+ ___94-[TransparencyStaticKey updateStaticKeyDatabaseForContact:peerPublicAccountIdentity:complete:]_block_invoke.345
+ ___94-[TransparencyStaticKey updateStaticKeyDatabaseForContact:peerPublicAccountIdentity:complete:]_block_invoke_2
+ ___94-[TransparencyStaticKey updateStaticKeyDatabaseForContact:peerPublicAccountIdentity:complete:]_block_invoke_2.340
+ ___94-[TransparencyStaticKey updateStaticKeyDatabaseForContact:peerPublicAccountIdentity:complete:]_block_invoke_2.346
+ ___ContactsLibraryCore_block_invoke
+ ___NSArray0__struct
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSArray"8ls32l8
+ ___block_descriptor_40_e8_32bs_e22_v16?0"KTIDSSession"8ls32l8
+ ___block_descriptor_40_e8_32bs_e34_v24?0"KTIDSSession"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e45_v24?0"KTIDStaticKeyStoreEntry"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e48_v24?0"<TransparencydIDSProtocol>"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
+ ___block_descriptor_40_e8_32r_e46_v24?0"<transparencyd_protocol>"8"NSError"16lr32l8
+ ___block_descriptor_48_e8_32r40r_e20_v20?0B8"NSError"12lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e29_v24?0"NSArray"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e36_v24?0"KTStatusResult"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e45_v24?0"KTIDStaticKeyStoreEntry"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e48_v24?0"<TransparencydIDSProtocol>"8"NSError"16ls40l8s32l8
+ ___block_descriptor_49_e8_32r40r_e46_v24?0"<transparencyd_protocol>"8"NSError"16lr32l8r40l8
+ ___block_descriptor_49_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e46_v24?0"<transparencyd_protocol>"8"NSError"16lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40s48s_e46_v24?0"<transparencyd_protocol>"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_60_e8_32s40r48r_e46_v24?0"<transparencyd_protocol>"8"NSError"16lr40l8s32l8r48l8
+ ___block_descriptor_64_e8_32bs40r48r_e17_v16?0"NSError"8lr40l8r48l8s32l8
+ ___block_descriptor_64_e8_32s40s48r56r_e46_v24?0"<transparencyd_protocol>"8"NSError"16lr48l8s32l8s40l8r56l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e46_v24?0"<transparencyd_protocol>"8"NSError"16lr64l8s32l8s40l8s48l8s56l8r72l8
+ ___block_literal_global.101
+ ___block_literal_global.120
+ ___block_literal_global.122
+ ___block_literal_global.126
+ ___block_literal_global.127
+ ___block_literal_global.129
+ ___block_literal_global.141
+ ___block_literal_global.145
+ ___block_literal_global.147
+ ___block_literal_global.151
+ ___block_literal_global.153
+ ___block_literal_global.157
+ ___block_literal_global.159
+ ___block_literal_global.161
+ ___block_literal_global.163
+ ___block_literal_global.166
+ ___block_literal_global.168
+ ___block_literal_global.172
+ ___block_literal_global.174
+ ___block_literal_global.210
+ ___block_literal_global.214
+ ___block_literal_global.220
+ ___block_literal_global.225
+ ___block_literal_global.233
+ ___block_literal_global.240
+ ___block_literal_global.242
+ ___block_literal_global.245
+ ___block_literal_global.247
+ ___block_literal_global.249
+ ___block_literal_global.252
+ ___block_literal_global.256
+ ___block_literal_global.261
+ ___block_literal_global.268
+ ___block_literal_global.271
+ ___block_literal_global.275
+ ___block_literal_global.277
+ ___block_literal_global.280
+ ___block_literal_global.284
+ ___block_literal_global.293
+ ___block_literal_global.30
+ ___block_literal_global.302
+ ___block_literal_global.313
+ ___block_literal_global.315
+ ___block_literal_global.316
+ ___block_literal_global.318
+ ___block_literal_global.320
+ ___block_literal_global.325
+ ___block_literal_global.326
+ ___block_literal_global.329
+ ___block_literal_global.332
+ ___block_literal_global.336
+ ___block_literal_global.338
+ ___block_literal_global.34
+ ___block_literal_global.342
+ ___block_literal_global.348
+ ___block_literal_global.349
+ ___block_literal_global.352
+ ___block_literal_global.355
+ ___block_literal_global.384
+ ___block_literal_global.387
+ ___block_literal_global.390
+ ___block_literal_global.41
+ ___block_literal_global.57
+ ___block_literal_global.60
+ ___block_literal_global.63
+ ___block_literal_global.65
+ ___block_literal_global.68
+ ___chkstk_darwin
+ ___getCNContactClass_block_invoke
+ ___getCNContactClass_block_invoke.cold.1
+ __os_feature_enabled_impl
+ __sl_dlopen
+ _abort
+ _abort_report_np
+ _audit_stringContacts
+ _bzero
+ _cc_clear
+ _cchmac_final
+ _cchmac_init
+ _cchmac_update
+ _dispatch_async
+ _dispatch_get_global_queue
+ _getCNContactClass
+ _getCNContactClass.softClass
+ _kApplicationIDSServiceMap
+ _kKTBackgroundFollowupDelayPeriod
+ _kKTBackgroundFollowupFailureCount
+ _kKTStatusAccountKey
+ _kKTStatusEverOptInState
+ _kTransparencyFlagSelfValidationXPCActivity
+ _kTransparencyOverrideBackgroundFollowupDelayPeriod
+ _kTransparencyOverrideBackgroundFollowupFailureCount
+ _kTransparencyOverrideQueryJustMadeTimeout
+ _kTransparencyQueryJustMadeTimeout
+ _kTransparencyStaticKeyNotification
+ _kTransparencyStaticKeySessionID
+ _kTransparencyStaticKeyState
+ _kTransparencyStaticKeyStateCodeAvailable
+ _kTransparencyStaticKeyStateCodeError
+ _kTransparencyStaticKeyStateDeleted
+ _kTransparencyStaticKeyStateInit
+ _kTransparencyStaticKeyStateNegotiating
+ _kTransparencyStaticKeyStoreContactIdentifier
+ _kTransparencyStaticKeyStoreNotification
+ _kTransparencyStaticKeyStorePublicIdentifydentifier
+ _kTransparencyTriggerOperationEnrollmentValidation
+ _objc_getClass
+ _objc_msgSend$acceptorInfo
+ _objc_msgSend$acceptorRandom
+ _objc_msgSend$clearPeerOverride:application:
+ _objc_msgSend$config
+ _objc_msgSend$contactExternalURI
+ _objc_msgSend$contactIdentifier
+ _objc_msgSend$dataWithData:
+ _objc_msgSend$deleteKTSession:complete:
+ _objc_msgSend$di
+ _objc_msgSend$digestPrefix
+ _objc_msgSend$errorCode
+ _objc_msgSend$everOptIn
+ _objc_msgSend$findByIdentifier:error:
+ _objc_msgSend$findStaticKeyStoreMappingByContact:complete:
+ _objc_msgSend$findStaticKeyStoreMappingByContactIdentifer:complete:
+ _objc_msgSend$findStaticKeyStoreMappingByIDSURI:complete:
+ _objc_msgSend$findStaticKeyStoreMappingByKey:complete:
+ _objc_msgSend$getKTSessionByHandle:complete:
+ _objc_msgSend$getKTSessionByID:complete:
+ _objc_msgSend$handle
+ _objc_msgSend$handles
+ _objc_msgSend$identifier
+ _objc_msgSend$idmsDevices:
+ _objc_msgSend$idsInstance
+ _objc_msgSend$initWithLength:
+ _objc_msgSend$initWithName:digestPrefix:shortCodeLength:digest:
+ _objc_msgSend$initiator
+ _objc_msgSend$initiatorInfo
+ _objc_msgSend$initiatorRandom
+ _objc_msgSend$invokeIDSXPCWithBlock:errorHandler:
+ _objc_msgSend$ktAccountPublicIDWithString:error:
+ _objc_msgSend$lastUsedAddressOfMe
+ _objc_msgSend$listKTSession:
+ _objc_msgSend$listPeerOverrides:
+ _objc_msgSend$listStaticKey:
+ _objc_msgSend$mappings
+ _objc_msgSend$markContactAsVerified:error:
+ _objc_msgSend$mutableBytes
+ _objc_msgSend$otherNamesForPeer
+ _objc_msgSend$peer
+ _objc_msgSend$peerAccountIdentity
+ _objc_msgSend$peerDisconnected
+ _objc_msgSend$peerHandle
+ _objc_msgSend$publicKeyID
+ _objc_msgSend$randomValueOfLength:
+ _objc_msgSend$removeEntryByContactIdentifier:complete:
+ _objc_msgSend$removeEntryByKDID:complete:
+ _objc_msgSend$removeObject:
+ _objc_msgSend$resetCloudZone:
+ _objc_msgSend$retryable:counter:
+ _objc_msgSend$sasCode
+ _objc_msgSend$sentUndisclosedRandom
+ _objc_msgSend$sessionExpire
+ _objc_msgSend$sessionID
+ _objc_msgSend$set
+ _objc_msgSend$setAcceptorInfo:
+ _objc_msgSend$setAcceptorRandom:
+ _objc_msgSend$setConfig:
+ _objc_msgSend$setContactExternalURI:
+ _objc_msgSend$setContactIdentifier:
+ _objc_msgSend$setDi:
+ _objc_msgSend$setDigestPrefix:
+ _objc_msgSend$setErrorCode:
+ _objc_msgSend$setErrorCode:forMapping:complete:
+ _objc_msgSend$setEverOptIn:
+ _objc_msgSend$setHandle:
+ _objc_msgSend$setHandles:
+ _objc_msgSend$setInitiator:
+ _objc_msgSend$setInitiatorInfo:
+ _objc_msgSend$setInitiatorRandom:
+ _objc_msgSend$setLastUsedAddressOfMe:
+ _objc_msgSend$setOtherNamesForPeer:
+ _objc_msgSend$setPeer:
+ _objc_msgSend$setPeerAccountIdentity:
+ _objc_msgSend$setPeerDisconnected:
+ _objc_msgSend$setPeerHandle:
+ _objc_msgSend$setPeerOverride:application:state:
+ _objc_msgSend$setPublicKeyID:
+ _objc_msgSend$setSasCode:
+ _objc_msgSend$setSentUndisclosedRandom:
+ _objc_msgSend$setSessionExpire:
+ _objc_msgSend$setSessionID:
+ _objc_msgSend$setShortCodeLength:
+ _objc_msgSend$setShortCodeMod10:
+ _objc_msgSend$setStaticAccountKeyStatus:
+ _objc_msgSend$setValid:
+ _objc_msgSend$setValidationDate:
+ _objc_msgSend$setupCloudSchema:complete:
+ _objc_msgSend$setupKTSession:complete:
+ _objc_msgSend$shortCodeLength
+ _objc_msgSend$shortCodeMod10
+ _objc_msgSend$staticAccountKeyStatus
+ _objc_msgSend$staticKeyTriggerSync:
+ _objc_msgSend$stripIMPrefix:
+ _objc_msgSend$transparencySupportInstance
+ _objc_msgSend$undisclosedInitiatorValue:
+ _objc_msgSend$updateStaticKeyEntry:contact:complete:
+ _objc_msgSend$updateStaticKeyEntry:contactIdentifier:contactExternalIdentifier:mappings:error:
+ _objc_msgSend$updateStaticKeyEntry:contactServerPath:contactIdentifier:mappings:error:
+ _objc_msgSend$valid
+ _objc_msgSend$validateByContactIdentifier:error:
+ _objc_msgSend$validateStaticKeyStoreMappingByContactIdentifer:complete:
+ _objc_msgSend$validateStaticKeyStoreMappingByKey:complete:
+ _objc_msgSend$validationDate
+ _sha256Transparency.prefixString
- +[TransparencySettings defaultFollowupTicketLifetime]
- -[KTVerifierResult debugDescription]
- GCC_except_table13
- GCC_except_table132
- GCC_except_table41
- GCC_except_table5
- GCC_except_table68
- ___125-[TransparencyDaemon replaySelfValidate:application:pcsAccountKey:queryRequest:queryResponse:responseTime:completionHandler:]_block_invoke.309
- ___22-[KTStatus getStatus:]_block_invoke.219
- ___22-[KTStatus getStatus:]_block_invoke.223
- ___22-[KTStatus getStatus:]_block_invoke_2.224
- ___26-[KTStatus getSelfStatus:]_block_invoke.230
- ___26-[KTStatus getSelfStatus:]_block_invoke.233
- ___26-[KTStatus getSelfStatus:]_block_invoke_2.234
- ___31-[KTOptInManager getOptInState]_block_invoke.210
- ___31-[KTOptInManager getOptInState]_block_invoke.214
- ___31-[KTOptInManager getOptInState]_block_invoke.219
- ___31-[KTOptInManager getOptInState]_block_invoke_2.215
- ___31-[KTOptInManager getOptInState]_block_invoke_2.222
- ___40-[TransparencyDaemon getAllOptInStates:]_block_invoke.370
- ___43+[KTOptInManager getOptInState:completion:]_block_invoke.199
- ___43+[KTOptInManager getOptInState:completion:]_block_invoke_2.200
- ___45-[TransparencyDaemon getOptInState:complete:]_block_invoke.361
- ___46+[TransparencySettings jsonDictFromPlistDict:]_block_invoke.113
- ___46-[KTStatus ignoreFailedEvent:completionBlock:]_block_invoke.258
- ___46-[KTStatus ignoreFailedEvent:completionBlock:]_block_invoke.261
- ___46-[KTStatus ignoreFailedEvent:completionBlock:]_block_invoke_2.262
- ___47-[KTStatus ignoreFailedEvents:completionBlock:]_block_invoke.267
- ___47-[KTStatus ignoreFailedEvents:completionBlock:]_block_invoke.270
- ___47-[KTStatus ignoreFailedEvents:completionBlock:]_block_invoke_2.271
- ___47-[TransparencyDaemon transparencyCloudDevices:]_block_invoke.344
- ___48-[KTOptInManager getOptInState:completionBlock:]_block_invoke.227
- ___48-[KTOptInManager getOptInState:completionBlock:]_block_invoke.230
- ___48-[KTOptInManager getOptInState:completionBlock:]_block_invoke_2.231
- ___48-[KTStatus errorForFailedEvent:completionBlock:]_block_invoke.239
- ___48-[KTStatus errorForFailedEvent:completionBlock:]_block_invoke.242
- ___48-[KTStatus errorForFailedEvent:completionBlock:]_block_invoke_2.244
- ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke.324
- ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke_2.326
- ___50-[KTStatus errorsForFailedEvents:completionBlock:]_block_invoke.249
- ___50-[KTStatus errorsForFailedEvents:completionBlock:]_block_invoke.252
- ___50-[KTStatus errorsForFailedEvents:completionBlock:]_block_invoke_2.253
- ___50-[TransparencyDaemon transparencyFetchPublicKeys:]_block_invoke.312
- ___50-[TransparencyDaemon transparencyIDSRegistration:]_block_invoke.329
- ___56-[KTOptInManager setOptInState:detailedCompletionBlock:]_block_invoke.235
- ___56-[KTOptInManager setOptInState:detailedCompletionBlock:]_block_invoke.238
- ___56-[KTOptInManager setOptInState:detailedCompletionBlock:]_block_invoke_2.239
- ___57-[TransparencyDaemon transparencyDumpKTRegistrationData:]_block_invoke.335
- ___57-[TransparencyDaemon transparencyTriggerIDSRegistration:]_block_invoke.315
- ___58-[TransparencyDaemon getOptInForURI:application:complete:]_block_invoke.364
- ___58-[TransparencyDaemon transparencyClearKTRegistrationData:]_block_invoke.341
- ___59-[KTOptInManager changeOptInState:detailedCompletionBlock:]_block_invoke.244
- ___59-[KTOptInManager changeOptInState:detailedCompletionBlock:]_block_invoke.247
- ___59-[KTOptInManager changeOptInState:detailedCompletionBlock:]_block_invoke_2.248
- ___59-[TransparencyDaemon getOptInStateForApplication:complete:]_block_invoke.373
- ___59-[TransparencyDaemon transparencyGetKTSignatures:complete:]_block_invoke.338
- ___60-[TransparencyDaemon changeOptInState:application:complete:]_block_invoke.358
- ___60-[TransparencyDaemon transparencyTriggerOperation:complete:]_block_invoke.355
- ___61-[TransparencyDaemon transparencyCheckKTAccountKey:complete:]_block_invoke.318
- ___63-[TransparencyDaemon transparencyPerformRegistrationSignature:]_block_invoke.332
- ___65-[TransparencyDaemon clearOptInStateForURI:application:complete:]_block_invoke.376
- ___69-[TransparencyDaemon transparencyCloudDeviceAdd:clientData:complete:]_block_invoke.379
- ___72-[TransparencyDaemon transparencyCloudDeviceRemove:clientData:complete:]_block_invoke.382
- ___73+[TransparencyXPCConnection invokeAccountsSupportWithBlock:errorHandler:]_block_invoke.48
- ___77-[TransparencyDaemon setOptInForURI:application:state:smtTimestamp:complete:]_block_invoke.367
- ___block_literal_global.107
- ___block_literal_global.202
- ___block_literal_global.206
- ___block_literal_global.209
- ___block_literal_global.212
- ___block_literal_global.218
- ___block_literal_global.221
- ___block_literal_global.224
- ___block_literal_global.226
- ___block_literal_global.236
- ___block_literal_global.238
- ___block_literal_global.241
- ___block_literal_global.246
- ___block_literal_global.248
- ___block_literal_global.255
- ___block_literal_global.257
- ___block_literal_global.260
- ___block_literal_global.269
- ___block_literal_global.273
- ___block_literal_global.314
- ___block_literal_global.328
- ___block_literal_global.334
- ___block_literal_global.354
- ___block_literal_global.357
- ___block_literal_global.360
- ___block_literal_global.50
- ___block_literal_global.81
- _kTransparencyTriggerOperationGarbageCollectDB
CStrings:
+ "\x11\x11"
+ "\x12#"
+ "\x16"
+ "\x18"
+ " failure: %@"
+ " loggableDatas:%@"
+ " optIn: %d, everOptedIn: %d"
+ " staticKeyEnforced: %d, staticKeyStatus: %@, accountKey:%@ "
+ "%"
+ "%0.*llu"
+ "%s"
+ "<KTIDSSession: state: %@ handle: %@ peerIdentity: %@ sasCode: %@ %@>"
+ "<KTPeerOverride: (uiStatus: %lu)>"
+ "@\"KTIDStaticKeyStoreEntry\"32@0:8@\"CNContact\"16^@24"
+ "@\"KTIDStaticKeyStoreEntry\"32@0:8@\"KTAccountPublicID\"16^@24"
+ "@\"KTIDStaticKeyStoreEntry\"32@0:8@\"NSString\"16^@24"
+ "@\"KTIDStaticKeyStoreEntry\"40@0:8@\"NSString\"16@\"NSString\"24^@32"
+ "@\"KTStatusResult\"24@0:8^@16"
+ "@\"KTVaudenaySASConfiguration\""
+ "@\"NSArray\"24@0:8^@16"
+ "@\"NSArray\"32@0:8@\"KTAccountPublicID\"16^@24"
+ "@\"NSSet\""
+ "@40@0:8@16@24^@32"
+ "@44@0:8@16@24i32r^{ccdigest_info=QQQQ*^v^?^?i}36"
+ "B24@0:8^@16"
+ "B28@0:8@16i24"
+ "B28@0:8B16^@20"
+ "B32@0:8@\"CNContact\"16^@24"
+ "B32@0:8@\"KTAccountPublicID\"16^@24"
+ "B32@0:8@\"NSString\"16^@24"
+ "B36@0:8i16@\"NSString\"20^@28"
+ "B36@0:8i16@20^@28"
+ "B40@0:8@\"KTAccountPublicID\"16@\"CNContact\"24^@32"
+ "B40@0:8@\"NSString\"16@\"KTAccountPublicID\"24^@32"
+ "B48@0:8@\"KTAccountPublicID\"16@\"NSString\"24@\"NSString\"32^@40"
+ "B48@0:8@16@24@32^@40"
+ "B56@0:8@\"KTAccountPublicID\"16@\"NSString\"24@\"NSString\"32@\"NSArray\"40^@48"
+ "B56@0:8@16@24@32@40^@48"
+ "CNContact"
+ "Connection findKeyByHandle error: %@"
+ "Connection removeEntryByContactIdentifier error: %@"
+ "Connection removeEntryByKDID error: %@"
+ "EnrollmentValidation"
+ "ErrorValidating"
+ "KTIDSSession"
+ "KTIDStaticKeyStore"
+ "KTIDStaticKeyStoreEntry"
+ "KTIDStaticKeyStoreEntryIdentifier"
+ "KTIDStaticKeyStoreHandle"
+ "KTIDStaticKeyStoreProtocol"
+ "KTPeerOverride"
+ "KTPeerOverrides"
+ "KTStaticKeyPeer"
+ "KTStatus: optIn = %@, everOptIn = %d, serverOptIn = %@, accountStatus = %@, systemStatus = %@, selfStatus = %@, pendingChanges: %@\n"
+ "KTStatusProtocol"
+ "KTSystemFailureUI"
+ "KTVaudenaySAS"
+ "KTVaudenaySASConfiguration"
+ "NoConfig"
+ "Sending deviceStatus"
+ "Sending synchronous opt-in state set for %{public}@"
+ "Sending synchronous opt-in state set for %{public}@: %d"
+ "SignatureFailed"
+ "Static key exchange not complete, can't mark as verified"
+ "Static key have not contact identifier, can't mark as verified"
+ "Success"
+ "T@\"KTAccountPublicID\",&,V_peerAccountIdentity"
+ "T@\"KTAccountPublicID\",C,V_accountIdentity"
+ "T@\"KTAccountPublicID\",C,VpublicKeyID"
+ "T@\"KTVaudenaySASConfiguration\",&,V_config"
+ "T@\"NSArray\",C"
+ "T@\"NSData\",&,V_acceptorInfo"
+ "T@\"NSData\",&,V_acceptorRandom"
+ "T@\"NSData\",&,V_digestPrefix"
+ "T@\"NSData\",&,V_initiatorInfo"
+ "T@\"NSData\",&,V_initiatorRandom"
+ "T@\"NSData\",&,V_sentUndisclosedRandom"
+ "T@\"NSData\",R,&"
+ "T@\"NSDate\",&,VsessionExpire"
+ "T@\"NSDate\",C,V_validationDate"
+ "T@\"NSMutableDictionary\",&,Vhandles"
+ "T@\"NSSet\",&"
+ "T@\"NSSet\",&,V_expectedPeerHandles"
+ "T@\"NSString\",&,V_contactIdentifier"
+ "T@\"NSString\",&,V_lastUsedAddressOfMe"
+ "T@\"NSString\",&,V_peer"
+ "T@\"NSString\",&,VpeerHandle"
+ "T@\"NSString\",&,VsasCode"
+ "T@\"NSString\",&,VsessionID"
+ "T@\"NSString\",&,Vstate"
+ "T@\"NSString\",C"
+ "T@\"NSString\",C,V_handle"
+ "T@\"NSString\",C,VcontactExternalURI"
+ "T@\"NSString\",C,VcontactIdentifier"
+ "TB,V_everOptIn"
+ "TB,V_initiator"
+ "TB,V_peerDisconnected"
+ "TB,V_valid"
+ "TQ,V_optedIn"
+ "TQ,V_shortCodeMod10"
+ "TQ,V_staticAccountKeyStatus"
+ "Ti,V_errorCode"
+ "Ti,V_shortCodeLength"
+ "Tr^{ccdigest_info=QQQQ*^v^?^?i},V_di"
+ "TransparancyKTIDStaticKeyStoreEntry"
+ "Transparency"
+ "TransparencyIDMSDeviceProtocol"
+ "TransparencyStaticKey"
+ "Unable to find class %s"
+ "Unknown deleteKTSession error: %@"
+ "Unknown findByContactIdentifier error: %@"
+ "Unknown findByIdentifier error: %@"
+ "Unknown getKTSessionByHandle error: %@"
+ "Unknown getKTSessionByID error: %@"
+ "Unknown listKTID error: %@"
+ "Unknown listKTSessions error: %@"
+ "Unknown removeEntryByContactIdentifier error: %@"
+ "Unknown removeEntryByKDID error: %@"
+ "Unknown resetCloudKit error: %@"
+ "Unknown setErrorCode error: %@"
+ "Unknown setupCloudSchema error: %@"
+ "Unknown setupKTSession error: %@"
+ "Unknown triggerSync error: %@"
+ "Unknown updateStaticKeyEntry error: %@"
+ "Unknown validateByContactIdentifier error: %@"
+ "Unknown validateByIdentifier error: %@"
+ "_acceptorInfo"
+ "_acceptorRandom"
+ "_accountIdentity"
+ "_config"
+ "_contactIdentifier"
+ "_di"
+ "_digestPrefix"
+ "_errorCode"
+ "_everOptIn"
+ "_expectedPeerHandles"
+ "_handle"
+ "_initiator"
+ "_initiatorInfo"
+ "_initiatorRandom"
+ "_lastUsedAddressOfMe"
+ "_otherNames"
+ "_peer"
+ "_peerAccountIdentity"
+ "_peerDisconnected"
+ "_sentUndisclosedRandom"
+ "_shortCodeLength"
+ "_shortCodeMod10"
+ "_staticAccountKeyStatus"
+ "_valid"
+ "_validationDate"
+ "acceptorInfo"
+ "acceptorRandom"
+ "accountIdentity"
+ "addMapping:forKTId:error:"
+ "addStaticKeyEntry:contactServerPath:contactIdentifier:error:"
+ "backgroundFollowupDelayPeriod"
+ "backgroundFollowupFailureCount"
+ "clearPeerOverride error: %@"
+ "clearPeerOverride:application:"
+ "code-available"
+ "com.apple.madrid"
+ "com.apple.private.alloy.facetime.multi"
+ "com.apple.private.alloy.multiplex1"
+ "combineLoggableDatasForUI:byAdding:"
+ "config"
+ "connected"
+ "contactExternalURI"
+ "contactIdentifier"
+ "contactServerPath"
+ "dataWithData:"
+ "defaultSelfFollowupTicketLifetime"
+ "deleteKTSession:complete:"
+ "deleted"
+ "deviceStatus failed with: %@"
+ "di"
+ "digestPrefix"
+ "disconnected"
+ "enableSelfValidationXPCActivity"
+ "errorCode"
+ "everOptIn"
+ "everOptInState"
+ "expectedPeerHandles"
+ "expire"
+ "findByContact:error:"
+ "findByContactIdentifier:error:"
+ "findByIdentifier:error:"
+ "findKeyByContactsServerPath:contactIdentifier:error:"
+ "findKeyByHandle:error:"
+ "findStaticKeyStoreMappingByContact:complete:"
+ "findStaticKeyStoreMappingByContactIdentifer:complete:"
+ "findStaticKeyStoreMappingByIDSURI:complete:"
+ "findStaticKeyStoreMappingByKey:complete:"
+ "getKTSessionByHandle:complete:"
+ "getKTSessionByID:complete:"
+ "handle"
+ "handles"
+ "i16@0:8"
+ "identifier"
+ "idmsDevices:"
+ "idsServiceForIdentifier:"
+ "im://"
+ "initAcceptorWithPublic:configuration:"
+ "initInitiatorWithPublic:configuration:"
+ "initWithLength:"
+ "initWithName:digestPrefix:shortCodeLength:digest:"
+ "initWithPeer:"
+ "initiator"
+ "initiatorInfo"
+ "initiatorRandom"
+ "invokeIDSSupportWithBlock:errorHandler:"
+ "invokeIDSXPCWithBlock:errorHandler:"
+ "jsonObject"
+ "kTransparencyStaticKeyNotification"
+ "kTransparencyStaticKeySessionID"
+ "kTransparencyStaticKeyState"
+ "kTransparencyStaticKeyStoreContactIdentifier"
+ "kTransparencyStaticKeyStoreNotification"
+ "kTransparencyStaticKeyStorePublicIdentifydentifier"
+ "kt(%@) ui(%@) %@[%@]"
+ "lastUsed"
+ "lastUsedAddressOfMe"
+ "listKTID:"
+ "listKTSession:"
+ "listKTSessions:"
+ "listPeerOverrides"
+ "listPeerOverrides error: %@"
+ "listPeerOverrides:"
+ "listStaticKey:"
+ "mappings"
+ "mappings:error:"
+ "markAsVerified:"
+ "markContactAsVerified:error:"
+ "mutableBytes"
+ "negotiating"
+ "opted in=%lu\n"
+ "otherNames"
+ "otherNamesForPeer"
+ "overrideBackgroundFollowupDelayPeriod"
+ "overrideBackgroundFollowupFailureCount"
+ "overrideQueryJustMadeTimeout"
+ "peerAccountIdentity"
+ "peerDisconnected"
+ "peerHandle"
+ "publicKeyID"
+ "queryJustMadeTimeout"
+ "r^{ccdigest_info=QQQQ*^v^?^?i}"
+ "r^{ccdigest_info=QQQQ*^v^?^?i}16@0:8"
+ "randomValueOfLength:"
+ "removeEntryByContact:error:"
+ "removeEntryByContactIdentifier:complete:"
+ "removeEntryByContactIdentifier:error:"
+ "removeEntryByKDID:complete:"
+ "removeEntryByKDID:error:"
+ "removeMapping:forKTId:error:"
+ "removeObject:"
+ "resetCloudKit:"
+ "resetCloudZone:"
+ "retryable:counter:"
+ "retrying invokeXPCSynchronousCallWithBlock: %@"
+ "sasCode"
+ "selfRandom"
+ "sentUndisclosedRandom"
+ "sessionExpire"
+ "sessionID"
+ "set"
+ "setAcceptorInfo:"
+ "setAcceptorRandom:"
+ "setAccountIdentity:"
+ "setConfig:"
+ "setContactExternalURI:"
+ "setContactIdentifier:"
+ "setContactServerPath:"
+ "setContactServerPath:forKTId:error:"
+ "setDi:"
+ "setDigestPrefix:"
+ "setErrorCode:"
+ "setErrorCode:forMapping:complete:"
+ "setErrorCode:forMapping:error:"
+ "setEverOptIn:"
+ "setExpectedPeerHandles:"
+ "setHandle:"
+ "setHandles:"
+ "setInitiator:"
+ "setInitiatorInfo:"
+ "setInitiatorRandom:"
+ "setInitiatorUndisclosedRandom:"
+ "setLastUsedAddressOfMe:"
+ "setMappings:"
+ "setOtherNamesForPeer:"
+ "setPeer:"
+ "setPeerAccountIdentity:"
+ "setPeerDisconnected:"
+ "setPeerHandle:"
+ "setPeerOverride error: %@"
+ "setPeerOverride:application:state:"
+ "setPeerPublic:"
+ "setPeerRandom:"
+ "setPublicKeyID:"
+ "setSasCode:"
+ "setSentUndisclosedRandom:"
+ "setSessionExpire:"
+ "setSessionID:"
+ "setShortCodeLength:"
+ "setShortCodeMod10:"
+ "setStaticAccountKeyStatus:"
+ "setValid:"
+ "setValidationDate:"
+ "setupCloudSchema:complete:"
+ "setupCloudSchema:error:"
+ "setupKTSession:complete:"
+ "sha256Transparency"
+ "shortAuthenticationString"
+ "shortCodeLength"
+ "shortCodeMod10"
+ "softlink:r:path:/System/Library/Frameworks/Contacts.framework/Contacts"
+ "staticAccountKeyStatus"
+ "staticKeyStatus"
+ "staticKeyTriggerSync:"
+ "status failed without status and no error"
+ "status:"
+ "stripIMPrefix:"
+ "systemFailureFeatureEnabled"
+ "transparencyIDMSDeviceList:"
+ "triggerSync:"
+ "undisclosedInitiatorRandom"
+ "undisclosedInitiatorValue:"
+ "updateStaticKeyDatabaseForContact error: %@"
+ "updateStaticKeyDatabaseForContact:peerPublicAccountIdentity:complete:"
+ "updateStaticKeyEntry:contact:complete:"
+ "updateStaticKeyEntry:contact:error:"
+ "updateStaticKeyEntry:contactIdentifier:contactExternalIdentifier:mappings:error:"
+ "updateStaticKeyEntry:contactServerPath:contactIdentifier:mappings:error:"
+ "updateWithStaticKeyEnforced updating UIStatus to %{public}@ for uri %{mask.hash}@"
+ "updateWithStaticKeyEnforced:isFailureIgnoredForDate:"
+ "v12@?0B8"
+ "v16@?0@\"KTIDSSession\"8"
+ "v16@?0@\"NSArray\"8"
+ "v20@0:8i16"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8@?<v@?@\"NSArray\">16"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "v24@0:8r^{ccdigest_info=QQQQ*^v^?^?i}16"
+ "v24@?0@\"<TransparencydIDSProtocol>\"8@\"NSError\"16"
+ "v24@?0@\"KTIDSSession\"8@\"NSError\"16"
+ "v24@?0@\"KTIDStaticKeyStoreEntry\"8@\"NSError\"16"
+ "v28@0:8B16@?<v@?B@\"NSError\">20"
+ "v28@0:8Q16B24"
+ "v32@0:8@\"CNContact\"16@?<v@?@\"KTIDStaticKeyStoreEntry\"@\"NSError\">24"
+ "v32@0:8@\"KTAccountPublicID\"16@?<v@?@\"KTIDStaticKeyStoreEntry\"@\"NSError\">24"
+ "v32@0:8@\"KTAccountPublicID\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"KTStaticKeyPeer\"16@?<v@?@\"KTIDSSession\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"KTIDSSession\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"KTIDStaticKeyStoreEntry\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\">24"
+ "v32@0:8@\"NSString\"16@?<v@?B>24"
+ "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
+ "v36@0:8i16@\"NSString\"20@?<v@?B@\"NSError\">28"
+ "v36@0:8i16@20@?28"
+ "v40@0:8@\"KTAccountPublicID\"16@\"CNContact\"24@?<v@?@\"KTIDStaticKeyStoreEntry\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@\"KTPeerOverride\"32"
+ "v40@0:8@16@24@32"
+ "v56@0:8@\"KTAccountPublicID\"16@\"NSString\"24@\"NSString\"32@\"NSArray\"40@?<v@?@\"KTIDStaticKeyStoreEntry\"@\"NSError\">48"
+ "valid"
+ "validateByContact:error:"
+ "validateByContactIdentifier:error:"
+ "validateByIdentifier:error:"
+ "validateStaticKeyStoreMappingByContactExternalURI:complete:"
+ "validateStaticKeyStoreMappingByContactIdentifer:complete:"
+ "validateStaticKeyStoreMappingByKey:complete:"
+ "validationDate"
+ "xpc ids error: %@"
- "\tfailure:%@\n"
- "\tloggableDatas:%@\n"
- "\toptIn: %d, everOptedIn: %d\n"
- "\x12\x13"
- "\x15"
- "GarbageCollectDB"
- "Sending asynchronous opt-in state set for %{public}@"
- "Sending asynchronous opt-in state set for %{public}@: %d"
- "defaultFollowupTicketLifetime"
- "kt result of %@, ui state of %@ for application: %@ uri: %@\n"

```
