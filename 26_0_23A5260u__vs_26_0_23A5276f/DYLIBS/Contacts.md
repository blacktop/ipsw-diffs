## Contacts

> `/System/Library/Frameworks/Contacts.framework/Contacts`

```diff

-3793.100.1.0.0
-  __TEXT.__text: 0x1a9ea4
-  __TEXT.__auth_stubs: 0x3130
-  __TEXT.__objc_methlist: 0x1ac28
+3796.100.1.0.0
+  __TEXT.__text: 0x1a96fc
+  __TEXT.__auth_stubs: 0x3140
+  __TEXT.__objc_methlist: 0x1ac40
   __TEXT.__const: 0x1e50
-  __TEXT.__gcc_except_tab: 0x3ac8
-  __TEXT.__cstring: 0xc912
+  __TEXT.__gcc_except_tab: 0x3ac4
+  __TEXT.__cstring: 0xc8b2
   __TEXT.__dlopen_cstrs: 0x8de
-  __TEXT.__oslogstring: 0xaa0a
+  __TEXT.__oslogstring: 0xa8da
   __TEXT.__ustring: 0x12
   __TEXT.__constg_swiftt: 0xd58
   __TEXT.__swift5_typeref: 0xca7

   __TEXT.__swift5_capture: 0x51c
   __TEXT.__swift_as_entry: 0x68
   __TEXT.__swift_as_ret: 0x5c
-  __TEXT.__unwind_info: 0x7d28
+  __TEXT.__unwind_info: 0x7d00
   __TEXT.__eh_frame: 0x2210
-  __TEXT.__objc_classname: 0x43a3
-  __TEXT.__objc_methname: 0x2af56
-  __TEXT.__objc_methtype: 0x538d
-  __TEXT.__objc_stubs: 0x1e580
+  __TEXT.__objc_classname: 0x43cd
+  __TEXT.__objc_methname: 0x2aef8
+  __TEXT.__objc_methtype: 0x53b1
+  __TEXT.__objc_stubs: 0x1e440
   __DATA_CONST.__got: 0x1b18
-  __DATA_CONST.__const: 0x6278
-  __DATA_CONST.__objc_classlist: 0x10d8
+  __DATA_CONST.__const: 0x6228
+  __DATA_CONST.__objc_classlist: 0x10e0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x308
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9578
+  __DATA_CONST.__objc_selrefs: 0x9568
   __DATA_CONST.__objc_protorefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x9a8
   __DATA_CONST.__objc_arraydata: 0x268
-  __AUTH_CONST.__auth_got: 0x18a8
-  __AUTH_CONST.__const: 0x6560
-  __AUTH_CONST.__cfstring: 0xd980
-  __AUTH_CONST.__objc_const: 0x2b820
+  __AUTH_CONST.__auth_got: 0x18b0
+  __AUTH_CONST.__const: 0x64e0
+  __AUTH_CONST.__cfstring: 0xd960
+  __AUTH_CONST.__objc_const: 0x2b998
   __AUTH_CONST.__objc_intobj: 0x5d0
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x5660
+  __AUTH.__objc_data: 0x56b0
   __AUTH.__data: 0x530
-  __DATA.__objc_ivar: 0x1238
+  __DATA.__objc_ivar: 0x1244
   __DATA.__data: 0x2c10
-  __DATA.__bss: 0x21a0
+  __DATA.__bss: 0x2190
   __DATA.__common: 0x80
   __DATA_DIRTY.__objc_data: 0x5d48
   __DATA_DIRTY.__data: 0x38

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C8A3EF40-E1C7-3AF1-8DD4-CA8E87775086
-  Functions: 12291
-  Symbols:   36308
-  CStrings:  12647
+  UUID: 2005B5C7-EB9E-32B6-9A27-889345E797AD
+  Functions: 12284
+  Symbols:   36273
+  CStrings:  12641
 
Symbols:
+ +[CNContactPosterDataStore warnAboutLackOfPosterAPIAccess].cold.2
+ -[CNContactPosterDataInitiallyUnknownAccess .cxx_destruct]
+ -[CNContactPosterDataInitiallyUnknownAccess countForFetchRequest:error:]
+ -[CNContactPosterDataInitiallyUnknownAccess currentImpl]
+ -[CNContactPosterDataInitiallyUnknownAccess executeCreateRequest:error:]
+ -[CNContactPosterDataInitiallyUnknownAccess executeDeleteRequest:error:]
+ -[CNContactPosterDataInitiallyUnknownAccess executeFetchRequest:error:]
+ -[CNContactPosterDataInitiallyUnknownAccess executeUpdateRequest:error:]
+ -[CNContactPosterDataInitiallyUnknownAccess failImpl]
+ -[CNContactPosterDataInitiallyUnknownAccess remoteImpl]
+ -[CNXPCContactsSupport reindexSearchableItemsWithIdentifiers:error:]
+ -[CNXPCContactsSupport verifyIndexWithError:]
+ -[CNiOSAddressBook preparingCount]
+ _OBJC_CLASS_$_CNContactPosterDataInitiallyUnknownAccess
+ _OBJC_IVAR_$_CNContactPosterDataInitiallyUnknownAccess._failImpl
+ _OBJC_IVAR_$_CNContactPosterDataInitiallyUnknownAccess._remoteImpl
+ _OBJC_IVAR_$_CNiOSAddressBook._preparingCount
+ _OBJC_METACLASS_$_CNContactPosterDataInitiallyUnknownAccess
+ __OBJC_$_CLASS_METHODS_CNContactStore(FamilyCircle|UnitTesting|iOSAB|iOSABUnitTesting|iOSABLegacyCompatibility|iOSPublicABCompatibilityCN|ElaborateSearches|_iOSPublicABCompatibility|CNFavoritesLegacyStore|Suggestions)
+ __OBJC_$_INSTANCE_METHODS_CNAggregateContactStore(iOSAB|CNFavoritesLegacyStore|Suggestions)
+ __OBJC_$_INSTANCE_METHODS_CNContactPosterDataInitiallyUnknownAccess
+ __OBJC_$_INSTANCE_METHODS_CNContactStore(FamilyCircle|UnitTesting|iOSAB|iOSABUnitTesting|iOSABLegacyCompatibility|iOSPublicABCompatibilityCN|ElaborateSearches|_iOSPublicABCompatibility|CNFavoritesLegacyStore|Suggestions)
+ __OBJC_$_INSTANCE_VARIABLES_CNContactPosterDataInitiallyUnknownAccess
+ __OBJC_$_PROP_LIST_CNContactPosterDataInitiallyUnknownAccess
+ __OBJC_CLASS_PROTOCOLS_$_CNContactPosterDataInitiallyUnknownAccess
+ __OBJC_CLASS_RO_$_CNContactPosterDataInitiallyUnknownAccess
+ __OBJC_METACLASS_RO_$_CNContactPosterDataInitiallyUnknownAccess
+ ___29-[CNiOSAddressBook flushPool]_block_invoke_2
+ ___40-[CNContactsEnvironment posterDataStore]_block_invoke
+ ___40-[CNiOSAddressBook preparedAddressBook:]_block_invoke
+ ___40-[CNiOSAddressBook preparedAddressBook:]_block_invoke_2
+ ___53-[CNContactPosterDataInitiallyUnknownAccess failImpl]_block_invoke
+ ___55-[CNContactPosterDataInitiallyUnknownAccess remoteImpl]_block_invoke
+ ___block_literal_global.495
+ ___block_literal_global.499
+ _backgroundColorRelatedKeys.cn_once_object_2
+ _backgroundColorRelatedKeys.cn_once_token_2
+ _objc_msgSend$currentImpl
+ _usleep
- +[CNCalculatesContactDiff clearWallpaperURIInUpdates:forContact:]
- +[CNContactStore(Spotlight) IsSpotlightIndexingSupported]
- +[CNContactStore(Spotlight) isXPCDataMapperStoreForSpotlight:]
- +[CNContactStore(Spotlight) logSpotlight]
- +[CNContactStore(Spotlight) logSpotlight].cold.1
- -[CNAggregateContactStore(Spotlight) contactStoresSupportingSpotlightIndexing]
- -[CNAggregateContactStore(Spotlight) firstContactStoreSupportingSpotlightIndexing]
- -[CNAggregateContactStore(Spotlight) isSpotlightIndexingSupported]
- -[CNAggregateContactStore(Spotlight) reindexSearchableItemsWithIdentifiers:]
- -[CNAggregateContactStore(Spotlight) reindexSearchableItemsWithIdentifiers:].cold.1
- -[CNAggregateContactStore(Spotlight) verifyIndexWithError:]
- -[CNContactStore(Spotlight) isSpotlightIndexingSupported]
- -[CNContactStore(Spotlight) reindexSearchableItemsWithIdentifiers:]
- -[CNContactStore(Spotlight) reindexSearchableItemsWithIdentifiers:].cold.1
- -[CNContactStore(Spotlight) verifyIndexWithError:]
- _CNContactsSupportContactProviderServiceName
- __OBJC_$_CLASS_METHODS_CNContactStore(FamilyCircle|UnitTesting|Spotlight|iOSAB|iOSABUnitTesting|iOSABLegacyCompatibility|iOSPublicABCompatibilityCN|ElaborateSearches|_iOSPublicABCompatibility|CNFavoritesLegacyStore|Suggestions)
- __OBJC_$_INSTANCE_METHODS_CNAggregateContactStore(Spotlight|iOSAB|CNFavoritesLegacyStore|Suggestions)
- __OBJC_$_INSTANCE_METHODS_CNContactStore(FamilyCircle|UnitTesting|Spotlight|iOSAB|iOSABUnitTesting|iOSABLegacyCompatibility|iOSPublicABCompatibilityCN|ElaborateSearches|_iOSPublicABCompatibility|CNFavoritesLegacyStore|Suggestions)
- ___41+[CNContactStore(Spotlight) logSpotlight]_block_invoke
- ___50-[CNContactStore(Spotlight) verifyIndexWithError:]_block_invoke
- ___50-[CNContactStore(Spotlight) verifyIndexWithError:]_block_invoke.17
- ___50-[CNContactStore(Spotlight) verifyIndexWithError:]_block_invoke.cold.1
- ___57+[CNContactStore(Spotlight) IsSpotlightIndexingSupported]_block_invoke
- ___65+[CNCalculatesContactDiff clearWallpaperURIInUpdates:forContact:]_block_invoke
- ___65+[CNCalculatesContactDiff clearWallpaperURIInUpdates:forContact:]_block_invoke_2
- ___67-[CNContactStore(Spotlight) reindexSearchableItemsWithIdentifiers:]_block_invoke
- ___67-[CNContactStore(Spotlight) reindexSearchableItemsWithIdentifiers:]_block_invoke.15
- ___67-[CNContactStore(Spotlight) reindexSearchableItemsWithIdentifiers:]_block_invoke.cold.1
- ___block_descriptor_48_e8_32r40r_e30_v24?0"NSString"8"NSError"16lr32l8r40l8
- ___block_literal_global.500
- ___block_literal_global.504
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_Contacts
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_Contacts
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_Contacts
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_Contacts
- _backgroundColorRelatedKeys.cn_once_object_3
- _backgroundColorRelatedKeys.cn_once_token_3
- _logSpotlight.cn_once_object_1
- _logSpotlight.cn_once_token_1
- _objc_msgSend$IsSpotlightIndexingSupported
- _objc_msgSend$clearWallpaperURIInUpdates:forContact:
- _objc_msgSend$contactStoresSupportingSpotlightIndexing
- _objc_msgSend$firstContactStoreSupportingSpotlightIndexing
- _objc_msgSend$isSpotlightIndexingSupported
- _objc_msgSend$isXPCDataMapperStoreForSpotlight:
- _objc_msgSend$logSpotlight
- _objc_msgSend$reindexSearchableItemsWithIdentifiers:
- _objc_msgSend$reindexSearchableItemsWithIdentifiers:withReply:
- _objc_msgSend$verifyIndexWithError:
- _objc_msgSend$verifyIndexWithReply:
CStrings:
+ "@\"CNContactPosterDataFailAccess\""
+ "@\"CNContactPosterDataXPCAccess\""
+ "CNContactPosterDataInitiallyUnknownAccess"
+ "Process lacks sandbox access to poster API, but that's expected because TCC status is unknown"
+ "T@\"<CNContactPosterDataStore>\",&,N"
+ "TQ,R,N,V_preparingCount"
+ "_failImpl"
+ "_preparingCount"
+ "_remoteImpl"
+ "currentImpl"
+ "failImpl"
+ "preparingCount"
+ "reindexSearchableItemsWithIdentifiers:error:"
+ "remoteImpl"
- "Cleared wallpaper URI for contact identifier %{public}@"
- "Could not obtain contacts service proxy for Spotlight query, error = %@"
- "Did reindex searchable items (%{public}@)"
- "Error reindexing searchable items: no supported stores"
- "IsSpotlightIndexingSupported"
- "T@\"<CNContactPosterDataStore>\",&,N,V_posterDataStore"
- "Unable to fulfill request to reindex searchable items: this store does not support spotlight indexing"
- "Will reindex all searchable items"
- "Will reindex searchable items: %{public}@"
- "clearWallpaperURIInUpdates:forContact:"
- "com.apple.contactsd.support.contact-provider"
- "contactStoresSupportingSpotlightIndexing"
- "firstContactStoreSupportingSpotlightIndexing"
- "isSpotlightIndexingSupported"
- "isXPCDataMapperStoreForSpotlight:"
- "logSpotlight"
- "spotlight"
- "v24@?0@\"NSString\"8@\"NSError\"16"
- "v32@0:8@\"NSArray\"16@?<v@?>24"

```
