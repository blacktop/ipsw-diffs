## SpotlightServices

> `/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices`

```diff

-2393.100.0.0.0
-  __TEXT.__text: 0x156780
+2400.8.1.0.0
+  __TEXT.__text: 0x156c50
   __TEXT.__auth_stubs: 0x1ce0
-  __TEXT.__objc_methlist: 0xf048
-  __TEXT.__const: 0x2a10
-  __TEXT.__cstring: 0x3100f
+  __TEXT.__objc_methlist: 0xf0a8
+  __TEXT.__const: 0x2a20
+  __TEXT.__cstring: 0x3105f
   __TEXT.__gcc_except_tab: 0x4d04
   __TEXT.__oslogstring: 0x9c7b
-  __TEXT.__ustring: 0x8d6
+  __TEXT.__ustring: 0x8c2
   __TEXT.__dlopen_cstrs: 0xd1
   __TEXT.__swift5_typeref: 0x1e6
   __TEXT.__swift5_reflstr: 0x99

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_capture: 0x94
-  __TEXT.__unwind_info: 0x33b8
-  __TEXT.__objc_classname: 0x14eb
-  __TEXT.__objc_methname: 0x2ba24
-  __TEXT.__objc_methtype: 0x312b
-  __TEXT.__objc_stubs: 0x1ce40
-  __DATA_CONST.__got: 0x2098
-  __DATA_CONST.__const: 0xfcf8
-  __DATA_CONST.__objc_classlist: 0x6b0
+  __TEXT.__unwind_info: 0x33d8
+  __TEXT.__objc_classname: 0x1520
+  __TEXT.__objc_methname: 0x2ba57
+  __TEXT.__objc_methtype: 0x3111
+  __TEXT.__objc_stubs: 0x1cf00
+  __DATA_CONST.__got: 0x20a0
+  __DATA_CONST.__const: 0xfce8
+  __DATA_CONST.__objc_classlist: 0x6c8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8ef0
+  __DATA_CONST.__objc_selrefs: 0x8f18
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x558
+  __DATA_CONST.__objc_superrefs: 0x560
   __DATA_CONST.__objc_arraydata: 0x1248
   __AUTH_CONST.__auth_got: 0xe80
-  __AUTH_CONST.__const: 0x2890
-  __AUTH_CONST.__cfstring: 0x2b3e0
-  __AUTH_CONST.__objc_const: 0x185a8
+  __AUTH_CONST.__const: 0x28b0
+  __AUTH_CONST.__cfstring: 0x2b440
+  __AUTH_CONST.__objc_const: 0x187d8
   __AUTH_CONST.__objc_intobj: 0x32b8
   __AUTH_CONST.__objc_doubleobj: 0x2a0
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x828
   __AUTH_CONST.__objc_dictobj: 0x258
-  __AUTH.__objc_data: 0x2138
+  __AUTH.__objc_data: 0x2228
   __AUTH.__data: 0x118
-  __DATA.__objc_ivar: 0x153c
+  __DATA.__objc_ivar: 0x1544
   __DATA.__data: 0x1238
-  __DATA.__bss: 0xc58
+  __DATA.__bss: 0xc68
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x23f0
   __DATA_DIRTY.__data: 0x298

   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/MarketplaceKit.framework/MarketplaceKit
   - /System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage
-  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/AeroML.framework/AeroML
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
-  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2DC7CBCC-3146-376E-8D5C-FAD7A1B8FD19
-  Functions: 6412
-  Symbols:   22183
-  CStrings:  19537
+  UUID: 37FCFD65-7689-3EB3-A851-0E8CBF701FF2
+  Functions: 6419
+  Symbols:   22225
+  CStrings:  19554
 
Symbols:
+ +[SSAppBrowseSectionBuilder _bundleIdToOnenessBundleId]
+ +[SSAppBrowseSectionBuilder _resultForAppIdentity:bundleIdToOnenessBundleIdMapping:]
+ +[SSAppBrowseSectionBuilder updateBundleIdToOnenessBundleIdMapping:]
+ +[SSAppBrowseSectionBuilder updateBundleIdToOnenessBundleIdMapping:].cold.1
+ +[SSAppBrowseSectionBuilder useWiderBrowseView]
+ +[SSBrowseSectionBuilder _resultCardSectionForResult:]
+ +[SSBrowseSectionBuilder _sectionResultForResults:style:withSectionTitle:]
+ +[SSBrowseSectionBuilder useWiderBrowseView]
+ +[SSFilesBrowseSectionBuilder useWiderBrowseView]
+ +[SSJournalResultBuilder bundleId]
+ +[SSJournalResultBuilder isCoreSpotlightResult]
+ +[SSPunchout punchoutFromSFPunchout:]
+ -[SSApplicationResultBuilder hasOnenessCounterpart]
+ -[SSJournalResultBuilder .cxx_destruct]
+ -[SSJournalResultBuilder buildFootnote]
+ -[SSJournalResultBuilder dateCreated]
+ -[SSJournalResultBuilder initWithResult:]
+ -[SSJournalResultBuilder setDateCreated:]
+ -[SSPunchout .cxx_destruct]
+ -[SSPunchout counterpartBundleIdentifier]
+ -[SSPunchout setCounterpartBundleIdentifier:]
+ _OBJC_CLASS_$_SSJournalResultBuilder
+ _OBJC_CLASS_$_SSPunchout
+ _OBJC_CLASS_$_SSQuickLookCommand
+ _OBJC_IVAR_$_SSJournalResultBuilder._dateCreated
+ _OBJC_IVAR_$_SSPunchout._counterpartBundleIdentifier
+ _OBJC_METACLASS_$_SFPunchout
+ _OBJC_METACLASS_$_SSJournalResultBuilder
+ _OBJC_METACLASS_$_SSPunchout
+ _OBJC_METACLASS_$_SSQuickLookCommand
+ __OBJC_$_CATEGORY_NSArray_$_QueryUtils
+ __OBJC_$_CATEGORY_NSString_$_QueryParser
+ __OBJC_$_CLASS_METHODS_SSJournalResultBuilder
+ __OBJC_$_CLASS_METHODS_SSPunchout
+ __OBJC_$_INSTANCE_METHODS_NSArray(QueryUtils|Tokenize|PRSRankingItemAdditions)
+ __OBJC_$_INSTANCE_METHODS_NSString(QueryParser|MatchScore|SSQueryUtils|TokenMatch|ParsecExtras)
+ __OBJC_$_INSTANCE_METHODS_SSJournalResultBuilder
+ __OBJC_$_INSTANCE_METHODS_SSPunchout
+ __OBJC_$_INSTANCE_VARIABLES_SSJournalResultBuilder
+ __OBJC_$_INSTANCE_VARIABLES_SSPunchout
+ __OBJC_$_PROP_LIST_SSJournalResultBuilder
+ __OBJC_$_PROP_LIST_SSPunchout
+ __OBJC_CLASS_RO_$_SSJournalResultBuilder
+ __OBJC_CLASS_RO_$_SSPunchout
+ __OBJC_CLASS_RO_$_SSQuickLookCommand
+ __OBJC_METACLASS_RO_$_SSJournalResultBuilder
+ __OBJC_METACLASS_RO_$_SSPunchout
+ __OBJC_METACLASS_RO_$_SSQuickLookCommand
+ ___68+[SSAppBrowseSectionBuilder updateBundleIdToOnenessBundleIdMapping:]_block_invoke
+ ___block_literal_global.168
+ __ssBundleIdToOnenessBundleId
+ __ssOnenessBundleIdMappingLock
+ _objc_msgSend$_bundleIdToOnenessBundleId
+ _objc_msgSend$_resultCardSectionForResult:
+ _objc_msgSend$_resultForAppIdentity:bundleIdToOnenessBundleIdMapping:
+ _objc_msgSend$_sectionResultForResults:style:withSectionTitle:
+ _objc_msgSend$actionTarget
+ _objc_msgSend$appSectionWithTitle:identifier:style:results:
+ _objc_msgSend$forceOpenInBrowser
+ _objc_msgSend$hasClip
+ _objc_msgSend$isRunnableInBackground
+ _objc_msgSend$sectionWithTitle:identifier:style:results:
+ _objc_msgSend$setActionTarget:
+ _objc_msgSend$setForceOpenInBrowser:
+ _objc_msgSend$setHasClip:
+ _objc_msgSend$useWiderBrowseView
+ _updateBundleIdToOnenessBundleIdMapping:.onceToken
- +[SSAppBrowseSectionBuilder _appIconImageForAppInfo:size:]
- +[SSAppBrowseSectionBuilder _appInfoForBundleID:]
- +[SSAppBrowseSectionBuilder _resultForAppIdentity:]
- +[SSAppBrowseSectionBuilder appSectionWithTitle:identifier:style:highDensity:appIdentities:]
- +[SSAppBrowseSectionBuilder appSectionWithTitle:identifier:style:highDensity:results:]
- +[SSAppBrowseSectionBuilder commandForResult:resultBuilder:]
- +[SSAppBrowseSectionBuilder imageForResult:resultBuilder:size:]
- +[SSAppBrowseSectionBuilder useResultBuilderForThumbnailAndCommand]
- +[SSBrowseSectionBuilder _resultCardSectionForResult:highDensity:]
- +[SSBrowseSectionBuilder _sectionResultForResults:style:highDensity:withSectionTitle:]
- +[SSBrowseSectionBuilder commandForResult:resultBuilder:]
- +[SSBrowseSectionBuilder imageForResult:resultBuilder:size:]
- +[SSBrowseSectionBuilder sectionWithTitle:identifier:style:highDensity:results:]
- +[SSBrowseSectionBuilder useResultBuilderForThumbnailAndCommand]
- +[SSFilesBrowseSectionBuilder useResultBuilderForThumbnailAndCommand]
- _OBJC_CLASS_$_ATXAppIdentity
- __OBJC_$_CATEGORY_NSArray_$_Tokenize
- __OBJC_$_CATEGORY_NSString_$_TokenMatch
- __OBJC_$_INSTANCE_METHODS_NSArray(Tokenize|QueryUtils|PRSRankingItemAdditions)
- __OBJC_$_INSTANCE_METHODS_NSString(TokenMatch|QueryParser|MatchScore|SSQueryUtils|ParsecExtras)
- ___block_literal_global.167
- ___block_literal_global.169
- __swift_FORCE_LOAD_$_swiftSpatial
- __swift_FORCE_LOAD_$_swiftSpatial_$_SpotlightServices
- __swift_FORCE_LOAD_$_swiftUIKit
- __swift_FORCE_LOAD_$_swiftUIKit_$_SpotlightServices
- _objc_msgSend$_appIconImageForAppInfo:size:
- _objc_msgSend$_resultCardSectionForResult:highDensity:
- _objc_msgSend$_resultForAppIdentity:
- _objc_msgSend$_sectionResultForResults:style:highDensity:withSectionTitle:
- _objc_msgSend$appSectionWithTitle:identifier:style:highDensity:appIdentities:
- _objc_msgSend$appSectionWithTitle:identifier:style:highDensity:results:
- _objc_msgSend$initWithBundleIdentifier:appType:
- _objc_msgSend$sectionWithTitle:identifier:style:highDensity:results:
CStrings:
+ "@36@0:8@16i24@28"
+ "Entry"
+ "Go to Settings"
+ "Remove"
+ "SSJournalResultBuilder"
+ "SSPunchout"
+ "SSQuickLookCommand"
+ "SUIWiderFilesBrowseViewEnabled"
+ "T@\"NSDate\",&,V_dateCreated"
+ "T@\"NSString\",C,N,V_counterpartBundleIdentifier"
+ "_bundleIdToOnenessBundleId"
+ "_counterpartBundleIdentifier"
+ "_resultCardSectionForResult:"
+ "_resultForAppIdentity:bundleIdToOnenessBundleIdMapping:"
+ "_sectionResultForResults:style:withSectionTitle:"
+ "actionTarget"
+ "com.apple.spotlight.prototype"
+ "counterpartBundleIdentifier"
+ "document.on.clipboard"
+ "forceOpenInBrowser"
+ "hasClip"
+ "hasOnenessCounterpart"
+ "isRunnableInBackground"
+ "minus.circle"
+ "public.voice-audio"
+ "punchoutFromSFPunchout:"
+ "setActionTarget:"
+ "setCounterpartBundleIdentifier:"
+ "setForceOpenInBrowser:"
+ "setHasClip:"
+ "updateBundleIdToOnenessBundleIdMapping:"
+ "useWiderBrowseView"
- "@40@0:8@16i24B28@32"
- "@48@0:8@16@24i32B36@40"
- "Delete Item"
- "_appIconImageForAppInfo:size:"
- "_appInfoForBundleID:"
- "_resultCardSectionForResult:highDensity:"
- "_resultForAppIdentity:"
- "_sectionResultForResults:style:highDensity:withSectionTitle:"
- "appSectionWithTitle:identifier:style:highDensity:appIdentities:"
- "appSectionWithTitle:identifier:style:highDensity:results:"
- "arrow.turn.up.right"
- "commandForResult:resultBuilder:"
- "imageForResult:resultBuilder:size:"
- "initWithBundleIdentifier:appType:"
- "kSpotlightItemTypeVoicemail"
- "sectionWithTitle:identifier:style:highDensity:results:"
- "trash"
- "useResultBuilderForThumbnailAndCommand"

```
