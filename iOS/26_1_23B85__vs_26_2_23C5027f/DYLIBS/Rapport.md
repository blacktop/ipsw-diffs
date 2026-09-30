## Rapport

> `/System/Library/PrivateFrameworks/Rapport.framework/Rapport`

```diff

-716.201.11.0.0
-  __TEXT.__text: 0x9ba50
-  __TEXT.__auth_stubs: 0x1cd0
-  __TEXT.__objc_methlist: 0x8eb4
-  __TEXT.__const: 0x3978
-  __TEXT.__cstring: 0x150f4
+716.300.51.0.0
+  __TEXT.__text: 0x9f4c0
+  __TEXT.__auth_stubs: 0x1e00
+  __TEXT.__objc_methlist: 0x8fb4
+  __TEXT.__const: 0x39d8
+  __TEXT.__cstring: 0x15684
   __TEXT.__gcc_except_tab: 0x171c
-  __TEXT.__oslogstring: 0x6cd
-  __TEXT.__swift5_typeref: 0x739
+  __TEXT.__oslogstring: 0x6fd
+  __TEXT.__swift5_typeref: 0x7cb
+  __TEXT.__swift5_capture: 0xe0
   __TEXT.__swift5_fieldmd: 0x7f4
   __TEXT.__constg_swiftt: 0x6f0
   __TEXT.__swift5_reflstr: 0x35c
-  __TEXT.__swift5_capture: 0xa4
   __TEXT.__swift5_proto: 0x128
   __TEXT.__swift5_types: 0x98
-  __TEXT.__swift_as_entry: 0x4
-  __TEXT.__swift_as_ret: 0x4
+  __TEXT.__swift_as_entry: 0xc
+  __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift5_assocty: 0x40
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2570
-  __TEXT.__eh_frame: 0x7b0
-  __TEXT.__objc_classname: 0xa7c
-  __TEXT.__objc_methname: 0x10d59
-  __TEXT.__objc_methtype: 0x2bff
-  __TEXT.__objc_stubs: 0x8f60
-  __DATA_CONST.__got: 0x3e8
-  __DATA_CONST.__const: 0x26d0
-  __DATA_CONST.__objc_classlist: 0x298
+  __TEXT.__unwind_info: 0x2640
+  __TEXT.__eh_frame: 0x838
+  __TEXT.__objc_classname: 0xaae
+  __TEXT.__objc_methname: 0x11068
+  __TEXT.__objc_methtype: 0x2c19
+  __TEXT.__objc_stubs: 0x9100
+  __DATA_CONST.__got: 0x410
+  __DATA_CONST.__const: 0x2720
+  __DATA_CONST.__objc_classlist: 0x2a8
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x128
+  __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a80
-  __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__objc_superrefs: 0x1d8
+  __DATA_CONST.__objc_selrefs: 0x3b40
+  __DATA_CONST.__objc_protorefs: 0xd8
+  __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__auth_got: 0xe78
-  __AUTH_CONST.__const: 0x11e0
-  __AUTH_CONST.__cfstring: 0x51a0
-  __AUTH_CONST.__objc_const: 0x107a8
+  __AUTH_CONST.__auth_got: 0xf10
+  __AUTH_CONST.__const: 0x1318
+  __AUTH_CONST.__cfstring: 0x51e0
+  __AUTH_CONST.__objc_const: 0x10a40
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH.__objc_data: 0x7a0
-  __AUTH.__data: 0x8c0
-  __DATA.__objc_ivar: 0x1128
-  __DATA.__data: 0x1d48
-  __DATA.__bss: 0x2ab0
+  __AUTH.__objc_data: 0x840
+  __AUTH.__data: 0x8f0
+  __DATA.__objc_ivar: 0x1144
+  __DATA.__data: 0x1e60
+  __DATA.__bss: 0x2b60
   __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x14a0
   __DATA_DIRTY.__data: 0x1a0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 060FCDB5-0AE9-3EEE-968A-F62DF0A269C9
-  Functions: 4475
-  Symbols:   12099
-  CStrings:  7060
+  UUID: 8BDFF83E-D8B6-3192-8F2F-E3F2ADFBBFEE
+  Functions: 4566
+  Symbols:   12318
+  CStrings:  7137
 
Symbols:
+ +[RPContactsWrapper createContactStore]
+ +[RPContactsWrapper donateContactToSharing:]
+ +[RPContactsWrapper donateContactToSharing:].cold.1
+ +[RPContactsWrapper donateContactToSharing:].cold.2
+ +[RPContactsWrapper donateContactToSharing:].cold.3
+ +[RPContactsWrapper getKeysToFetchForMeCard]
+ +[RPContactsWrapper getMeCard:]
+ +[RPContactsWrapper getMeCard:].cold.1
+ +[RPContactsWrapper getMeCard:].cold.2
+ +[RPContactsWrapper getMeCard:].cold.3
+ +[RPContactsWrapper getMeCard:].cold.4
+ +[RPContactsWrapper getMeCard:].cold.5
+ +[RPContactsWrapper getMeCard:].cold.6
+ +[RPContactsWrapper getMeCard:].cold.7
+ -[RPContactInfo .cxx_destruct]
+ -[RPContactInfo deviceName]
+ -[RPContactInfo expiryDate]
+ -[RPContactInfo familyName]
+ -[RPContactInfo givenName]
+ -[RPContactInfo identifier]
+ -[RPContactInfo imageData]
+ -[RPContactInfo initIdentifier:imageData:deviceName:givenName:familyName:expiryDate:]
+ -[RPContactInfo setDeviceName:]
+ -[RPContactInfo setExpiryDate:]
+ -[RPContactInfo setFamilyName:]
+ -[RPContactInfo setGivenName:]
+ -[RPContactInfo setIdentifier:]
+ -[RPContactInfo setImageData:]
+ -[RPIdentity dateExpires]
+ -[RPIdentity setDateExpires:]
+ _CNContactFamilyNameKeyFunction
+ _CNContactGivenNameKeyFunction
+ _CNContactImageDataKeyFunction
+ _CNContactStoreFunction
+ _ContactsLibrary.sLib
+ _ContactsLibrary.sOnce
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_RPContactInfo
+ _OBJC_CLASS_$_RPContactsWrapper
+ _OBJC_IVAR_$_RPContactInfo._deviceName
+ _OBJC_IVAR_$_RPContactInfo._expiryDate
+ _OBJC_IVAR_$_RPContactInfo._familyName
+ _OBJC_IVAR_$_RPContactInfo._givenName
+ _OBJC_IVAR_$_RPContactInfo._identifier
+ _OBJC_IVAR_$_RPContactInfo._imageData
+ _OBJC_IVAR_$_RPIdentity._dateExpires
+ _OBJC_METACLASS_$_RPContactInfo
+ _OBJC_METACLASS_$_RPContactsWrapper
+ __OBJC_$_CLASS_METHODS_RPContactsWrapper
+ __OBJC_$_INSTANCE_METHODS_RPContactInfo
+ __OBJC_$_INSTANCE_VARIABLES_RPContactInfo
+ __OBJC_$_PROP_LIST_RPContactInfo
+ __OBJC_$_PROTOCOL_REFS_OS_sec_identity
+ __OBJC_CLASS_RO_$_RPContactInfo
+ __OBJC_CLASS_RO_$_RPContactsWrapper
+ __OBJC_LABEL_PROTOCOL_$_OS_sec_identity
+ __OBJC_METACLASS_RO_$_RPContactInfo
+ __OBJC_METACLASS_RO_$_RPContactsWrapper
+ __OBJC_PROTOCOL_$_OS_sec_identity
+ ___31+[RPContactsWrapper getMeCard:]_block_invoke
+ ___31+[RPContactsWrapper getMeCard:]_block_invoke.cold.1
+ ___31+[RPContactsWrapper getMeCard:]_block_invoke.cold.2
+ ___31+[RPContactsWrapper getMeCard:]_block_invoke.cold.3
+ ___44+[RPContactsWrapper donateContactToSharing:]_block_invoke
+ ___44+[RPContactsWrapper donateContactToSharing:]_block_invoke_2
+ ___44+[RPContactsWrapper donateContactToSharing:]_block_invoke_2.cold.1
+ ___ContactsLibrary_block_invoke
+ ___block_descriptor_40_e8_32s_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e18_v16?0"NSString"8ls32l8s40l8s48l8
+ ___block_literal_global.211
+ ___block_literal_global.79
+ ___block_literal_global.83
+ ___block_literal_global.87
+ ___block_literal_global.90
+ ___block_literal_global.93
+ ___initValCNContactFamilyNameKey_block_invoke
+ ___initValCNContactFamilyNameKey_block_invoke.cold.1
+ ___initValCNContactGivenNameKey_block_invoke
+ ___initValCNContactGivenNameKey_block_invoke.cold.1
+ ___initValCNContactImageDataKey_block_invoke
+ ___initValCNContactImageDataKey_block_invoke.cold.1
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ __swiftImmortalRefCount
+ __swift_stdlib_malloc_size
+ _block_copy_helper.49
+ _block_descriptor.51
+ _block_destroy_helper.10
+ _block_destroy_helper.50
+ _classCNContactStore
+ _constantValCNContactFamilyNameKey
+ _constantValCNContactGivenNameKey
+ _constantValCNContactImageDataKey
+ _donateContactToSharing:.managerClass
+ _donateContactToSharing:.onceToken
+ _flat unique So15OS_sec_identity_p
+ _gLogCategory_RPContactsWrapper
+ _getCNContactFamilyNameKey
+ _getCNContactGivenNameKey
+ _getCNContactImageDataKey
+ _getCNContactStoreClass
+ _initCNContactStore
+ _initCNContactStore.cold.1
+ _initSFCreateAskToAirDropReceiverController
+ _initSFCreateAskToAirDropReceiverController.cold.1
+ _initSFCreatePairedContactManager
+ _initSFCreatePairedContactManager.cold.1
+ _initValCNContactFamilyNameKey
+ _initValCNContactFamilyNameKey.cold.1
+ _initValCNContactGivenNameKey
+ _initValCNContactGivenNameKey.cold.1
+ _initValCNContactImageDataKey
+ _initValCNContactImageDataKey.cold.1
+ _malloc_size
+ _memmove
+ _objc_msgSend$_crossPlatformUnifiedMeContactWithKeysToFetch:error:
+ _objc_msgSend$createContactStore
+ _objc_msgSend$dateExpires
+ _objc_msgSend$donateContactWithIdentifier:imageData:deviceName:givenName:familyName:expiryDate:completion:
+ _objc_msgSend$expiryDate
+ _objc_msgSend$familyName
+ _objc_msgSend$fetchSharingNameWithCompletion:
+ _objc_msgSend$getKeysToFetchForMeCard
+ _objc_msgSend$givenName
+ _objc_msgSend$imageData
+ _objc_msgSend$initIdentifier:imageData:deviceName:givenName:familyName:expiryDate:
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$substringToIndex:
+ _softLinkOnceCNContactFamilyNameKey
+ _softLinkOnceCNContactGivenNameKey
+ _softLinkOnceCNContactImageDataKey
+ _softLinkSFCreateAskToAirDropReceiverController
+ _softLinkSFCreatePairedContactManager
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_bridgeObjectRetain_n
+ _swift_getObjCClassFromMetadata
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_task_alloc
+ _swift_task_dealloc
+ _swift_unknownObjectRetain
+ _symbolic Say_____GIego_ 7Rapport23SPAKE2PlusConfigurationV
+ _symbolic ScCySo13RPContactInfoCSg_____G s5NeverO
+ _symbolic So13RPContactInfoCSg
+ _symbolic _____XMT 7Network12NWParametersC
+ _symbolic ______pSgIeyBy_ So15OS_sec_identityP
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 7Rapport26RPPairingTemporaryIdentityV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
- ___block_literal_global.204
CStrings:
+ "+[RPContactsWrapper donateContactToSharing:]"
+ "+[RPContactsWrapper donateContactToSharing:]_block_invoke_2"
+ "+[RPContactsWrapper getMeCard:]"
+ "+[RPContactsWrapper getMeCard:]_block_invoke"
+ ", Expires %@"
+ "/Library/Caches/com.apple.xbs/Sources/Rapport/Rapport/Pairing/RPPairingHelpers.swift"
+ "/System/Library/Frameworks/Contacts.framework/Contacts"
+ "@64@0:8@16@24@32@40@48@56"
+ "CNContactFamilyNameKey"
+ "CNContactGivenNameKey"
+ "CNContactImageDataKey"
+ "CNContactStore"
+ "Cannot donate contact - identifier unavailable"
+ "Failed to create paired contact manager"
+ "Failed to donate contact to Sharing: %@, error: %@"
+ "Failed to get me card"
+ "OS_sec_identity"
+ "RPContactInfo"
+ "RPContactsWrapper"
+ "RPIdentityExpiryDateOverride"
+ "SFCreateAskToAirDropReceiverController"
+ "SFCreatePairedContactManager"
+ "Successfully donated contact to Sharing: %@"
+ "T@\"NSData\",C,N,V_imageData"
+ "T@\"NSDate\",C,N,V_dateExpires"
+ "T@\"NSDate\",C,N,V_expiryDate"
+ "T@\"NSString\",C,N,V_familyName"
+ "T@\"NSString\",C,N,V_givenName"
+ "Using RPIdentityExpiryDateOverride: %s"
+ "_appSvcPrePair._tcp"
+ "_crossPlatformUnifiedMeContactWithKeysToFetch:error:"
+ "_dateExpires"
+ "_expiryDate"
+ "_familyName"
+ "_givenName"
+ "_imageData"
+ "client_identity"
+ "com.apple.rapport.asktoairdropcontroller"
+ "createContactStore"
+ "dateExpires"
+ "donateContactToSharing:"
+ "donateContactWithIdentifier:imageData:deviceName:givenName:familyName:expiryDate:completion:"
+ "dtExp"
+ "expiryDate"
+ "fetchSharingNameWithCompletion:"
+ "getKeysToFetchForMeCard"
+ "getMeCard:"
+ "getMeCard: both names missing, attempting to fetch from Sharing framework"
+ "getMeCard: called"
+ "getMeCard: failed to create SFAskToAirDropReceiverController, returning fallback"
+ "getMeCard: failed to create contact store"
+ "getMeCard: fetched meCard (givenName: %@, familyName: %@, deviceName: %@)"
+ "getMeCard: no me card present, falling back to sharing name"
+ "getMeCard: received sharing name: %@"
+ "getMeCard: returning contact info from sharing name"
+ "getMeCard: returning meCard with names"
+ "getMeCard: split into givenName: %@, familyName: %@"
+ "getMeCard: using as givenName only: %@"
+ "imageData"
+ "initIdentifier:imageData:deviceName:givenName:familyName:expiryDate:"
+ "initWithSuiteName:"
+ "persistentDomainForName:"
+ "server_identity"
+ "setDateExpires:"
+ "setExpiryDate:"
+ "setFamilyName:"
+ "setGivenName:"
+ "setImageData:"
+ "standardUserDefaults"
+ "stringForKey:"
+ "substringFromIndex:"
+ "substringToIndex:"
+ "v16@?0@\"RPContactInfo\"8"
+ "v20@?0B8@\"NSError\"12"
- "_applicationServicePrePairing._tcp"

```
