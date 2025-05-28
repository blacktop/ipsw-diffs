## SpotlightServices

> `/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices`

```diff

-2274.13.3.0.0
-  __TEXT.__text: 0xe5ad8
-  __TEXT.__auth_stubs: 0x1380
-  __TEXT.__objc_methlist: 0x9554
-  __TEXT.__const: 0x21f0
-  __TEXT.__cstring: 0x2b87d
+2274.23.0.3.0
+  __TEXT.__text: 0xe6894
+  __TEXT.__auth_stubs: 0x1400
+  __TEXT.__objc_methlist: 0x9604
+  __TEXT.__const: 0x2252
+  __TEXT.__cstring: 0x2b93c
   __TEXT.__oslogstring: 0x2deb
   __TEXT.__gcc_except_tab: 0x2b04
   __TEXT.__ustring: 0x3e
-  __TEXT.__unwind_info: 0x2274
+  __TEXT.__constg_swiftt: 0x50
+  __TEXT.__swift5_typeref: 0x14
+  __TEXT.__swift5_fieldmd: 0x10
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__unwind_info: 0x22ac
   __TEXT.__objc_classname: 0xe06
-  __TEXT.__objc_methname: 0x1ccca
-  __TEXT.__objc_methtype: 0x26ce
-  __TEXT.__objc_stubs: 0x15000
-  __DATA_CONST.__got: 0xb60
-  __DATA_CONST.__const: 0xf3b8
-  __DATA_CONST.__objc_classlist: 0x420
+  __TEXT.__objc_methname: 0x1cf52
+  __TEXT.__objc_methtype: 0x26e2
+  __TEXT.__objc_stubs: 0x15220
+  __DATA_CONST.__got: 0xb78
+  __DATA_CONST.__const: 0xf438
+  __DATA_CONST.__objc_classlist: 0x428
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xbaa0
-  __DATA_CONST.__objc_selrefs: 0x64b8
+  __DATA_CONST.__objc_const: 0xbb00
+  __DATA_CONST.__objc_selrefs: 0x6548
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0xa70
+  __DATA_CONST.__objc_superrefs: 0x350
   __DATA_CONST.__objc_arraydata: 0xb78
-  __AUTH_CONST.__cfstring: 0x246a0
-  __AUTH_CONST.__objc_const: 0x4138
+  __AUTH_CONST.__cfstring: 0x24700
+  __AUTH_CONST.__objc_const: 0x4180
   __AUTH_CONST.__const: 0x1ad0
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__objc_intobj: 0x2118
+  __AUTH_CONST.__objc_intobj: 0x2130
   __AUTH_CONST.__objc_doubleobj: 0x1c0
   __AUTH_CONST.__objc_arrayobj: 0x498
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__auth_ptr: 0x30
-  __AUTH_CONST.__auth_got: 0x9d0
-  __AUTH.__objc_data: 0x5a0
-  __AUTH.__data: 0x28
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0xa60
-  __DATA.__objc_superrefs: 0x350
-  __DATA.__objc_ivar: 0xd98
+  __AUTH_CONST.__auth_got: 0xa10
+  __AUTH.__objc_data: 0x610
+  __AUTH.__data: 0x50
+  __DATA.__objc_ivar: 0xda0
   __DATA.__data: 0xd78
   __DATA.__thread_ptrs: 0x8
-  __DATA.__bss: 0x3e0
+  __DATA.__bss: 0x370
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x23a0
+  __DATA_DIRTY.__objc_data: 0x23f0
   __DATA_DIRTY.__data: 0x2a8
-  __DATA_DIRTY.__bss: 0x4c50
+  __DATA_DIRTY.__bss: 0x4cf0
   __DATA_DIRTY.__common: 0x28
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
+  - /System/Library/PrivateFrameworks/AppDistribution.framework/AppDistribution
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4042
-  Symbols:   14738
-  CStrings:  10440
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  Functions: 4068
+  Symbols:   14829
+  CStrings:  10470
 
Symbols:
+ +[SSRankingManager fillRankingPosition:]
+ +[SSSearchInAppResultBuilder buildResultWithAppName:appBundleId:searchString:searchInAppType:]
+ +[SSSearchInAppSectionBuilder cachedPreferredStoreBundleIdentifier]
+ +[SSSearchInAppSectionBuilder updateCachedPreferredStoreBundleID]
+ -[SSSearchInAppResultBuilder initWithAppName:appBundleId:searchString:searchInAppType:]
+ -[SSSearchInAppResultBuilder searchInAppType]
+ -[SSSearchInAppResultBuilder setSearchInAppType:]
+ -[SSShortcutResultBuilder buildCompactThumbnail]
+ -[SSShortcutResultBuilder buildStandardThumbnail]
+ -[SSShortcutResultBuilder lnPropertyIdentifier]
+ -[SSShortcutResultBuilder setLnPropertyIdentifier:]
+ -[SSSuggestionResultBuilder buildHighlightedTextForSuggestion]
+ -[SSSuggestionResultBuilder buildPhotoTextAndGlyphForSuggestion:]
+ _CFPreferencesCopyValue
+ _MDItemRunnableShortcutsLNPropertyIdentifier
+ _OBJC_CLASS_$_SFShortcutsImage
+ _OBJC_CLASS_$__TtC17SpotlightServices26SSAppDistributionUtilities
+ _OBJC_IVAR_$_SSSearchInAppResultBuilder._searchInAppType
+ _OBJC_IVAR_$_SSShortcutResultBuilder._lnPropertyIdentifier
+ _OBJC_METACLASS_$__TtC17SpotlightServices26SSAppDistributionUtilities
+ _PREFERENCE_QUERY_LENGTH_CUTOFF_THRESHOLD
+ _SSGetDisabledBundleSet
+ __DATA__TtC17SpotlightServices26SSAppDistributionUtilities
+ __METACLASS_DATA__TtC17SpotlightServices26SSAppDistributionUtilities
+ __OBJC_$_CLASS_METHODS__TtC17SpotlightServices26SSAppDistributionUtilities
+ __OBJC_$_INSTANCE_METHODS__TtC17SpotlightServices26SSAppDistributionUtilities
+ ___65+[SSSearchInAppSectionBuilder updateCachedPreferredStoreBundleID]_block_invoke
+ ___65+[SSSearchInAppSectionBuilder updateCachedPreferredStoreBundleID]_block_invoke_2
+ ___65+[SSSearchInAppSectionBuilder updateCachedPreferredStoreBundleID]_block_invoke_3
+ ___block_descriptor_40_e24_v16?0"NSNotification"8l
+ ___block_literal_global.331
+ ___block_literal_global.336
+ ___block_literal_global.344
+ ___block_literal_global.75
+ ___block_literal_global.907
+ ___block_literal_global.909
+ ___block_literal_global.911
+ ___swift_reflection_version
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_SpotlightServices
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_SpotlightServices
+ __swift_FORCE_LOAD_$_swiftCoreGraphics
+ __swift_FORCE_LOAD_$_swiftCoreGraphics_$_SpotlightServices
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_SpotlightServices
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_SpotlightServices
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_SpotlightServices
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_SpotlightServices
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_SpotlightServices
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_SpotlightServices
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_SpotlightServices
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_SpotlightServices
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_SpotlightServices
+ __unnamed_array_storage.349
+ __unnamed_array_storage.364
+ __unnamed_array_storage.376
+ __unnamed_array_storage.385
+ __unnamed_array_storage.398
+ __unnamed_array_storage.404
+ _kCFPreferencesAnyHost
+ _kCFPreferencesCurrentUser
+ _objc_allocWithZone
+ _objc_msgSend$addObserverForName:object:queue:usingBlock:
+ _objc_msgSend$buildCompactThumbnail
+ _objc_msgSend$buildHighlightedTextForSuggestion
+ _objc_msgSend$buildPhotoTextAndGlyphForSuggestion:
+ _objc_msgSend$buildResultWithAppName:appBundleId:searchString:searchInAppType:
+ _objc_msgSend$buildStandardThumbnail
+ _objc_msgSend$cachedPreferredStoreBundleIdentifier
+ _objc_msgSend$distributorPriorityList
+ _objc_msgSend$distributorPriorityListChangedNotifationName
+ _objc_msgSend$indexOfResultInSectionWhenRanked
+ _objc_msgSend$indexOfSectionWhenRanked
+ _objc_msgSend$initWithAppName:appBundleId:searchString:searchInAppType:
+ _objc_msgSend$lnPropertyIdentifier
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$searchInAppType
+ _objc_msgSend$setIndexOfResultInSectionWhenRanked:
+ _objc_msgSend$setIndexOfSectionWhenRanked:
+ _objc_msgSend$setLnPropertyIdentifier:
+ _objc_msgSend$setSearchInAppType:
+ _objc_msgSend$updateCachedPreferredStoreBundleID
+ _s_cachedPreferredStoreBundleID
+ _swift_bridgeObjectRelease
+ _swift_lookUpClassMethod
+ _symbolic So8NSObjectC
+ _symbolic _____ 17SpotlightServices26SSAppDistributionUtilitiesC
+ _updateCachedPreferredStoreBundleID.onceToken
+ _updateCachedPreferredStoreBundleID.queue
- +[SSSearchInAppResultBuilder buildResultWithAppName:appBundleId:searchString:]
- -[SSSearchInAppResultBuilder initWithAppName:appBundleId:searchString:]
- -[SSSuggestionResultBuilder buildHighlightedTextForSuggestionAppendingTextPieces:]
- _NSFileProtectionNone
- ___block_literal_global.328
- ___block_literal_global.333
- ___block_literal_global.74
- ___block_literal_global.906
- ___block_literal_global.908
- ___block_literal_global.910
- __unnamed_array_storage.346
- __unnamed_array_storage.352
- __unnamed_array_storage.370
- __unnamed_array_storage.382
- __unnamed_array_storage.395
- __unnamed_array_storage.401
- _objc_msgSend$buildHighlightedTextForSuggestionAppendingTextPieces:
- _objc_msgSend$buildResultWithAppName:appBundleId:searchString:
- _objc_msgSend$initWithAppName:appBundleId:searchString:
CStrings:
+ "\x16\x13"
+ "<photo-icon>"
+ "<query>"
+ "@44@0:8@16@24@32i40"
+ "EXPOSURE_NOTIFICATION"
+ "SBSearchDisabledBundles"
+ "SSAppDistributionUtilities fetching queue"
+ "T@\"NSString\",&,N,V_lnPropertyIdentifier"
+ "T@\"NSString\",?,R,C"
+ "TEMPLATE_PHOTOS_LOCATION_SEARCH"
+ "Ti,N,V_searchInAppType"
+ "_TtC17SpotlightServices26SSAppDistributionUtilities"
+ "_lnPropertyIdentifier"
+ "_searchInAppType"
+ "addObserverForName:object:queue:usingBlock:"
+ "buildCompactThumbnail"
+ "buildHighlightedTextForSuggestion"
+ "buildPhotoTextAndGlyphForSuggestion:"
+ "buildResultWithAppName:appBundleId:searchString:searchInAppType:"
+ "buildStandardThumbnail"
+ "cachedPreferredStoreBundleIdentifier"
+ "distributorPriorityList"
+ "distributorPriorityListChangedNotifationName"
+ "fillRankingPosition:"
+ "indexOfResultInSectionWhenRanked"
+ "indexOfSectionWhenRanked"
+ "initWithAppName:appBundleId:searchString:searchInAppType:"
+ "lnPropertyIdentifier"
+ "numberWithUnsignedInt:"
+ "searchInAppType"
+ "setIndexOfResultInSectionWhenRanked:"
+ "setIndexOfSectionWhenRanked:"
+ "setLnPropertyIdentifier:"
+ "setSearchInAppType:"
+ "updateCachedPreferredStoreBundleID"
- "\x16\x12"
- "App Store"
- "PHOTOS_KEY"
- "buildHighlightedTextForSuggestionAppendingTextPieces:"
- "buildResultWithAppName:appBundleId:searchString:"
- "initWithAppName:appBundleId:searchString:"

```
