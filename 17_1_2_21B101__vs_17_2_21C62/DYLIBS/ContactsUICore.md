## ContactsUICore

> `/System/Library/PrivateFrameworks/ContactsUICore.framework/ContactsUICore`

```diff

-3501.0.0.0.0
-  __TEXT.__text: 0x5c634
-  __TEXT.__auth_stubs: 0xbb0
-  __TEXT.__objc_methlist: 0x5ab8
-  __TEXT.__const: 0x210
-  __TEXT.__oslogstring: 0x27d0
-  __TEXT.__cstring: 0x3338
+3506.0.0.0.0
+  __TEXT.__text: 0x63d5c
+  __TEXT.__auth_stubs: 0x1010
+  __TEXT.__objc_methlist: 0x5bf8
+  __TEXT.__const: 0x276
+  __TEXT.__oslogstring: 0x293f
+  __TEXT.__cstring: 0x387e
   __TEXT.__gcc_except_tab: 0x594
   __TEXT.__dlopen_cstrs: 0x51
-  __TEXT.__unwind_info: 0x1afc
-  __TEXT.__objc_classname: 0x196f
-  __TEXT.__objc_methname: 0x11063
-  __TEXT.__objc_methtype: 0x2c40
-  __TEXT.__objc_stubs: 0xc1a0
-  __DATA_CONST.__got: 0x338
-  __DATA_CONST.__const: 0x2598
-  __DATA_CONST.__objc_classlist: 0x530
+  __TEXT.__swift5_typeref: 0x90
+  __TEXT.__swift5_capture: 0x10
+  __TEXT.__constg_swiftt: 0x7c
+  __TEXT.__swift5_fieldmd: 0x20
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__unwind_info: 0x1c38
+  __TEXT.__eh_frame: 0x50
+  __TEXT.__objc_classname: 0x1982
+  __TEXT.__objc_methname: 0x11542
+  __TEXT.__objc_methtype: 0x2c5b
+  __TEXT.__objc_stubs: 0xc3c0
+  __DATA_CONST.__got: 0x410
+  __DATA_CONST.__const: 0x25e8
+  __DATA_CONST.__objc_classlist: 0x548
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x1d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xad18
-  __DATA_CONST.__objc_selrefs: 0x3878
+  __DATA_CONST.__objc_const: 0xaf18
+  __DATA_CONST.__objc_selrefs: 0x3a70
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__const: 0x18a0
+  __AUTH_CONST.__const: 0x1928
   __AUTH_CONST.__cfstring: 0x2400
-  __AUTH_CONST.__objc_const: 0x3c78
+  __AUTH_CONST.__objc_const: 0x3d08
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x50
-  __AUTH_CONST.__auth_got: 0x5e8
-  __AUTH.__objc_data: 0x1860
-  __AUTH.__data: 0x90
+  __AUTH_CONST.__auth_got: 0x818
+  __AUTH.__objc_data: 0x1960
+  __AUTH.__data: 0x150
   __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x7e8
-  __DATA.__objc_superrefs: 0x350
-  __DATA.__objc_ivar: 0x540
-  __DATA.__data: 0x1640
+  __DATA.__objc_classrefs: 0x830
+  __DATA.__objc_superrefs: 0x358
+  __DATA.__objc_ivar: 0x550
+  __DATA.__data: 0x1760
   __DATA.__bss: 0x3f0
-  __DATA.__common: 0x8
+  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1b80
   __DATA_DIRTY.__data: 0x68
   __DATA_DIRTY.__bss: 0x2d0

   - /System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle
   - /System/Library/PrivateFrameworks/PersonaKit.framework/PersonaKit
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/Transparency.framework/Transparency
+  - /System/Library/PrivateFrameworks/vCard.framework/vCard
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 63D92C29-07E2-31BD-AC3D-009964B6CBEF
-  Functions: 2726
-  Symbols:   10003
-  CStrings:  3967
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 3A77EF2C-244A-3F50-A1AA-26D7D64C3483
+  Functions: 2816
+  Symbols:   10226
+  CStrings:  4080
 
Symbols:
+ +[CNUIMeContactMonitor log]
+ +[CNUIStaticIdentity addStaticKeyWithPublicIDString:contact:]
+ +[CNUIStaticIdentity addStaticKeyWithPublicIDString:contact:].cold.1
+ +[CNUIStaticIdentity findStoreEntryByContact:]
+ +[CNUIStaticIdentity findStoreEntryByContact:].cold.1
+ +[CNUIStaticIdentity isHandleInStore:]
+ +[CNUIStaticIdentity isHandleInStore:].cold.1
+ +[CNUIStaticIdentity isHandleInStore:].cold.2
+ +[CNUIStaticIdentity isValidStaticKeyString:]
+ +[CNUIStaticIdentity ktStore]
+ +[CNUIStaticIdentity makeKTPublicIDWithString:]
+ +[CNUIStaticIdentity makeKTPublicIDWithString:].cold.1
+ +[CNUIStaticIdentity removeAccountKeyFromContact:]
+ +[CNUIStaticIdentity removeAccountKeyFromContact:].cold.1
+ -[CNUICoreMainWhitelistedContactsController hasDowntimeWhitelistContainer]
+ -[CNUIPRLikenessLookup futureResultForPhotoImageDataForMeContact:error:]
+ -[CNUIPRLikenessLookup lookupOptions]
+ -[CNUIPRLikenessLookup setLookupOptions:]
+ -[CNUIPRLikenessLookup shouldFetchSharedPhotoForContact:]
+ -[CNUIPRLikenessResolver lookupOptions]
+ -[CNUIPRLikenessResolver setLookupOptions:]
+ -[CNUIStaticIdentity .cxx_destruct]
+ -[CNUIStaticIdentity contact]
+ -[CNUIStaticIdentity initWithContact:]
+ -[CNUIStaticIdentity isHandleInStore:]
+ -[CNUIStaticIdentity isHandleInStore:].cold.1
+ -[CNUIStaticIdentity storeEntry]
+ -[CNUIStaticIdentity verificationCode]
+ -[_CNUICachingLikenessRenderer lookupOptions]
+ -[_CNUICachingLikenessRenderer setLookupOptions:]
+ -[_CNUILikenessRenderer lookupOptions]
+ -[_CNUILikenessRenderer setLookupOptions:]
+ GCC_except_table14
+ GCC_except_table17
+ _CNContactAddressingGrammarKey
+ _CNContactBirthdayKey
+ _CNContactDatesKey
+ _CNContactDepartmentNameKey
+ _CNContactJobTitleKey
+ _CNContactMiddleNameKey
+ _CNContactNamePrefixKey
+ _CNContactNameSuffixKey
+ _CNContactNonGregorianBirthdayKey
+ _CNContactOrganizationNameKey
+ _CNContactPhoneticFamilyNameKey
+ _CNContactPhoneticGivenNameKey
+ _CNContactPhoneticMiddleNameKey
+ _CNContactPhoneticOrganizationNameKey
+ _CNContactPreviousFamilyNameKey
+ _CNContactUrlAddressesKey
+ _CNContactWallpaperKey
+ _CNContactWatchWallpaperImageDataKey
+ _CNIsChineseJapaneseKoreanString
+ _CNVCardLabelHome
+ _CNVCardLabelWork
+ _OBJC_CLASS_$_CNContactVCardSerialization
+ _OBJC_CLASS_$_CNUIStaticIdentity
+ _OBJC_CLASS_$_CNVCardWritingOptions
+ _OBJC_CLASS_$_KTAccountPublicID
+ _OBJC_CLASS_$_KTIDStaticKeyStore
+ _OBJC_CLASS_$_NSDateComponents
+ _OBJC_CLASS_$_NSTermOfAddress
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$__TtC14ContactsUICore12CNUINameDrop
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_CNUIPRLikenessLookup._lookupOptions
+ _OBJC_IVAR_$_CNUIPRLikenessResolver._lookupOptions
+ _OBJC_IVAR_$_CNUIStaticIdentity._contact
+ _OBJC_IVAR_$_CNUIStaticIdentity._storeEntry
+ _OBJC_IVAR_$__CNUICachingLikenessRenderer._lookupOptions
+ _OBJC_IVAR_$__CNUILikenessRenderer._lookupOptions
+ _OBJC_METACLASS_$_CNUIStaticIdentity
+ _OBJC_METACLASS_$__TtC14ContactsUICore12CNUINameDrop
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __DATA__TtC14ContactsUICore12CNUINameDrop
+ __DATA__TtC14ContactsUICoreP33_7042A531D25A04CDF663229957ABD9CE19ResourceBundleClass
+ __METACLASS_DATA__TtC14ContactsUICore12CNUINameDrop
+ __METACLASS_DATA__TtC14ContactsUICoreP33_7042A531D25A04CDF663229957ABD9CE19ResourceBundleClass
+ __OBJC_$_CLASS_METHODS_CNUIStaticIdentity
+ __OBJC_$_INSTANCE_METHODS_CNUIStaticIdentity
+ __OBJC_$_INSTANCE_METHODS__TtC14ContactsUICore12CNUINameDrop
+ __OBJC_$_INSTANCE_VARIABLES_CNUIStaticIdentity
+ __OBJC_$_PROP_LIST_CNUILikenessRendering
+ __OBJC_$_PROP_LIST_CNUIStaticIdentity
+ __OBJC_CLASS_RO_$_CNUIStaticIdentity
+ __OBJC_METACLASS_RO_$_CNUIStaticIdentity
+ ___27+[CNUIMeContactMonitor log]_block_invoke
+ ___29+[CNUIStaticIdentity ktStore]_block_invoke
+ ___72-[CNUIPRLikenessLookup futureResultForPhotoImageDataForMeContact:error:]_block_invoke
+ ___block_literal_global.135
+ ___block_literal_global.149
+ ___block_literal_global.153
+ ___block_literal_global.174
+ ___block_literal_global.189
+ ___swift_allocate_value_buffer
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_instantiateConcreteTypeFromMangledNameAbstract
+ ___swift_project_value_buffer
+ ___swift_reflection_version
+ __swiftEmptyArrayStorage
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_ContactsUICore
+ __swift_FORCE_LOAD_$_swiftCoreGraphics
+ __swift_FORCE_LOAD_$_swiftCoreGraphics_$_ContactsUICore
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_ContactsUICore
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_ContactsUICore
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_ContactsUICore
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_ContactsUICore
+ __swift_FORCE_LOAD_$_swiftIntents
+ __swift_FORCE_LOAD_$_swiftIntents_$_ContactsUICore
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_ContactsUICore
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_ContactsUICore
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_ContactsUICore
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_malloc_size
+ _ktStore.ktStore
+ _ktStore.onceToken
+ _malloc_size
+ _meContactMonitor.cn_once_object_2
+ _meContactMonitor.cn_once_token_2
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_msgSend$findByContact:error:
+ _objc_msgSend$findKeyByHandle:error:
+ _objc_msgSend$findStoreEntryByContact:
+ _objc_msgSend$futureResultForPhotoImageDataForMeContact:error:
+ _objc_msgSend$handles
+ _objc_msgSend$ktAccountPublicIDWithString:error:
+ _objc_msgSend$ktStore
+ _objc_msgSend$lookupOptions
+ _objc_msgSend$makeKTPublicIDWithString:
+ _objc_msgSend$publicAccountIdentity
+ _objc_msgSend$publicKeyID
+ _objc_msgSend$removeEntryByKDID:error:
+ _objc_msgSend$setLookupOptions:
+ _objc_msgSend$shouldFetchSharedPhotoForContact:
+ _objc_msgSend$static_identity_os_log
+ _objc_msgSend$storeEntry
+ _objc_msgSend$updateStaticKeyEntry:contact:error:
+ _objc_msgSend$valid
+ _objc_retainAutoreleasedReturnValue
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_deallocClassInstance
+ _swift_deallocObject
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_willThrow
+ _symbolic SaySSG
+ _symbolic So14CNLabeledValueC
+ _symbolic So8NSObjectC
+ _symbolic So8NSObjectCSg
+ _symbolic _____ 14ContactsUICore12CNUINameDropC
+ _symbolic _____ 14ContactsUICore19ResourceBundleClass33_7042A531D25A04CDF663229957ABD9CELLC
+ _symbolic _____Sg 10Foundation14DateComponentsV
+ _symbolic ______p s7CVarArgP
+ _symbolic _____ySSG s23_ContiguousArrayStorageC
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____y______pG s23_ContiguousArrayStorageC s7CVarArgP
+ _symbolic _____yyXlG s23_ContiguousArrayStorageC
+ _symbolic ypSg
+ _unifiedMeContactMonitor.cn_once_object_3
+ _unifiedMeContactMonitor.cn_once_token_3
- -[CNUIPRLikenessLookup setSkipContactLookup:]
- -[CNUIPRLikenessResolver setSkipContactLookup:]
- -[CNUIPRLikenessResolver skipContactLookup]
- GCC_except_table12
- _OBJC_IVAR_$_CNUIPRLikenessLookup._skipContactLookup
- _OBJC_IVAR_$_CNUIPRLikenessResolver._skipContactLookup
- ___62-[CNUIPRLikenessLookup photoFutureForContactFuture:scheduler:]_block_invoke_4
- ___block_literal_global.147
- ___block_literal_global.173
- ___block_literal_global.186
- _meContactMonitor.cn_once_object_1
- _meContactMonitor.cn_once_token_1
- _objc_msgSend$setSkipContactLookup:
- _unifiedMeContactMonitor.cn_once_object_2
- _unifiedMeContactMonitor.cn_once_token_2
CStrings:
+ "*** WARNING *** contact is not unified %@"
+ "@\"KTIDStaticKeyStoreEntry\""
+ "CNUIStaticIdentity"
+ "Could not decode vCard from pref: %@"
+ "Could not encode vCard: %@"
+ "Could not turn preference %s into CNContact"
+ "Error creating public id with verification code %@: %@"
+ "Error removing verification code from contact %@: %@"
+ "Error saving static id: %@"
+ "Failed to save NameDrop field pref: %@"
+ "NAMEDROP_ADDRESS"
+ "NAMEDROP_ADDRESSES"
+ "NAMEDROP_BIRTHDAY"
+ "NAMEDROP_EMAIL_ADDRESSES"
+ "NAMEDROP_ICLOUD_EMAIL"
+ "NAMEDROP_INSTANT_MESSAGE"
+ "NAMEDROP_INSTANT_MESSAGES"
+ "NAMEDROP_PHONE_NUMBERS"
+ "NAMEDROP_PRONOUNS"
+ "NAMEDROP_RELATED_NAME"
+ "NAMEDROP_RELATED_NAMES"
+ "NAMEDROP_REVIEW_INFO"
+ "NAMEDROP_SOCIAL_PROFILE"
+ "NAMEDROP_SOCIAL_PROFILES"
+ "NAMEDROP_TERM_SEPARATOR"
+ "Saved NameDrop field pref"
+ "T@\"KTIDStaticKeyStoreEntry\",R,N,V_storeEntry"
+ "TQ,N,V_lookupOptions"
+ "Unable to find store entry for contact %@: %@"
+ "Unable to find store entry for handle %@: %@"
+ "Unable to find store handle for handle %@"
+ "Unable to find store handle for handle in contact %@: %@"
+ "Using NameDrop field pref"
+ "Using NameDrop pronoun pref"
+ "Using legacy NameDrop handle pref"
+ "_TtC14ContactsUICore12CNUINameDrop"
+ "_TtC14ContactsUICoreP33_7042A531D25A04CDF663229957ABD9CE19ResourceBundleClass"
+ "_lookupOptions"
+ "_storeEntry"
+ "addStaticKeyWithPublicIDString:contact:"
+ "addressingGrammars"
+ "birthday"
+ "boolForKey:"
+ "bubble.left.fill"
+ "com.apple.Sharing"
+ "com.apple.contacts.namedrop"
+ "contactRelations"
+ "contactsWithData:error:"
+ "dataForKey:"
+ "dataWithContacts:options:error:"
+ "dates"
+ "day"
+ "didSharePronouns"
+ "era"
+ "findByContact:error:"
+ "findKeyByHandle:error:"
+ "findStoreEntryByContact:"
+ "futureResultForPhotoImageDataForMeContact:error:"
+ "hasDowntimeWhitelistContainer"
+ "hasSuffix:"
+ "initWithLabel:value:"
+ "initWithStringValue:"
+ "initWithSuiteName:"
+ "isHandleInStore:"
+ "isValidDate"
+ "isValidStaticKeyString:"
+ "ktAccountPublicIDWithString:error:"
+ "ktStore"
+ "lastSharedFields"
+ "lastSharedHandle"
+ "lookupOptions"
+ "makeKTPublicIDWithString:"
+ "me-contact-monitor"
+ "month"
+ "phoneticFamilyName"
+ "phoneticGivenName"
+ "phoneticMiddleName"
+ "pin.point.of.interest.fill"
+ "publicAccountIdentity"
+ "publicKeyID"
+ "removeAccountKeyFromContact:"
+ "removeEntryByKDID:error:"
+ "setAddressingGrammars:"
+ "setBool:forKey:"
+ "setContactType:"
+ "setIncludeNotes:"
+ "setIncludePhotos:"
+ "setIncludePronouns:"
+ "setIncludeWallpaper:"
+ "setLookupOptions:"
+ "setNilValueForKey:"
+ "setPhoneticFamilyName:"
+ "setPhoneticGivenName:"
+ "setPhoneticMiddleName:"
+ "setSharedPhotoDisplayPreference:"
+ "setUseUnencryptedPronouns:"
+ "setValue:forKey:"
+ "setWallpaper:"
+ "setWatchWallpaperImageData:"
+ "shouldFetchSharedPhotoForContact:"
+ "storeEntry"
+ "stringForKey:"
+ "termsOfAddress"
+ "unable to find date pref in me card: %@"
+ "unable to find pref in me card: %@"
+ "unable to find string pref in me card: %@"
+ "updateStaticKeyEntry:contact:error:"
+ "urlAddresses"
+ "valid"
+ "verificationCode"
+ "wallpaper"
+ "watchWallpaperImageData"
+ "year"
- "\x16"
- "TB,N,V_skipContactLookup"
- "_skipContactLookup"
- "setSkipContactLookup:"

```
