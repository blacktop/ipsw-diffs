## SpotlightUIServices

> `/System/Library/PrivateFrameworks/SpotlightUIServices.framework/SpotlightUIServices`

```diff

-181.1.4.0.0
-  __TEXT.__text: 0x43280
+181.1.10.0.0
+  __TEXT.__text: 0x4374c
   __TEXT.__auth_stubs: 0xfe0
-  __TEXT.__objc_methlist: 0x4850
-  __TEXT.__const: 0x694
-  __TEXT.__cstring: 0x24a3
-  __TEXT.__oslogstring: 0x64b
+  __TEXT.__objc_methlist: 0x4880
+  __TEXT.__const: 0x684
+  __TEXT.__cstring: 0x2503
   __TEXT.__ustring: 0x38
+  __TEXT.__oslogstring: 0x64b
   __TEXT.__gcc_except_tab: 0x148
-  __TEXT.__constg_swiftt: 0x418
   __TEXT.__swift5_typeref: 0x282
-  __TEXT.__swift5_fieldmd: 0x134
-  __TEXT.__swift5_types: 0x3c
-  __TEXT.__swift5_reflstr: 0xcb
+  __TEXT.__swift5_reflstr: 0xbd
   __TEXT.__swift5_assocty: 0x78
+  __TEXT.__constg_swiftt: 0x418
+  __TEXT.__swift5_fieldmd: 0x134
   __TEXT.__swift5_proto: 0x2c
+  __TEXT.__swift5_types: 0x3c
   __TEXT.__swift5_capture: 0x94
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0xf98
+  __TEXT.__unwind_info: 0xfa0
   __TEXT.__eh_frame: 0x70
-  __TEXT.__objc_classname: 0x8fe
-  __TEXT.__objc_methname: 0xa899
-  __TEXT.__objc_methtype: 0x4f2
-  __TEXT.__objc_stubs: 0x9e20
-  __DATA_CONST.__got: 0x13d8
+  __TEXT.__objc_classname: 0x8ea
+  __TEXT.__objc_methname: 0xa966
+  __TEXT.__objc_methtype: 0x4f5
+  __TEXT.__objc_stubs: 0x9ea0
+  __DATA_CONST.__got: 0x13d0
   __DATA_CONST.__const: 0x4d0
-  __DATA_CONST.__objc_classlist: 0x2c8
+  __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2bf0
+  __DATA_CONST.__objc_selrefs: 0x2c18
   __DATA_CONST.__objc_superrefs: 0x240
-  __DATA_CONST.__objc_arraydata: 0x80
+  __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x800
-  __AUTH_CONST.__const: 0xa90
-  __AUTH_CONST.__cfstring: 0x2780
-  __AUTH_CONST.__objc_const: 0x6b08
+  __AUTH_CONST.__const: 0xab0
+  __AUTH_CONST.__cfstring: 0x2800
+  __AUTH_CONST.__objc_const: 0x6ab8
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x1f98
+  __AUTH.__objc_data: 0x1f48
   __AUTH.__data: 0x1d8
-  __DATA.__objc_ivar: 0x48c
+  __DATA.__objc_ivar: 0x490
   __DATA.__data: 0x160
-  __DATA.__bss: 0x830
+  __DATA.__bss: 0x850
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D8342784-BC1C-3D5F-B337-7E6A48DD1854
-  Functions: 1801
-  Symbols:   6134
-  CStrings:  2814
+  UUID: E00DFEB8-15A0-39AC-A64E-03AE3D4359D1
+  Functions: 1808
+  Symbols:   6149
+  CStrings:  2829
 
Symbols:
+ +[SPUISAppBrowseSectionBuilder _bundleIdToOnenessBundleId]
+ +[SPUISAppBrowseSectionBuilder _resultForAppIdentity:bundleIdToOnenessBundleIdMapping:]
+ +[SPUISAppBrowseSectionBuilder updateBundleIdToOnenessBundleIdMapping:]
+ +[SPUISAppBrowseSectionBuilder updateBundleIdToOnenessBundleIdMapping:].cold.1
+ +[SPUISBrowseSectionBuilder _sectionResultForResults:style:sectionTitle:sectionIdentifier:]
+ -[SPUISApplicationResultBuilder hasOnenessCounterpart]
+ -[SPUISContactResultBuilder highlightedMatchedText]
+ -[SPUISMailResultBuilder bundleIdentifierForAppIconBadgeImage]
+ -[SPUISResultBuilder lastUsedDate]
+ -[SPUISResultBuilder setLastUsedDate:]
+ -[SPUISToolResultBuilder buildBadgingImageWithThumbnail:]
+ -[SPUISToolResultBuilder buildSecondaryCommand]
+ -[SPUISToolResultBuilder setToolIconData:]
+ -[SPUISToolResultBuilder toolIconData]
+ _OBJC_IVAR_$_SPUISResultBuilder._lastUsedDate
+ _OBJC_IVAR_$_SPUISToolResultBuilder._toolIconData
+ ___71+[SPUISAppBrowseSectionBuilder updateBundleIdToOnenessBundleIdMapping:]_block_invoke
+ ___block_literal_global.446
+ ___block_literal_global.447
+ ___block_literal_global.509
+ ___block_literal_global.528
+ ___block_literal_global.531
+ ___block_literal_global.536
+ ___block_literal_global.538
+ ___block_literal_global.541
+ ___block_literal_global.555
+ ___block_literal_global.591
+ ___block_literal_global.594
+ ___block_literal_global.598
+ __spuisBundleIdToOnenessBundleId
+ __spuisOnenessBundleIdMappingLock
+ _objc_msgSend$_bundleIdToOnenessBundleId
+ _objc_msgSend$_resultForAppIdentity:bundleIdToOnenessBundleIdMapping:
+ _objc_msgSend$_sectionResultForResults:style:sectionTitle:sectionIdentifier:
+ _objc_msgSend$highlightedMatchedText
+ _objc_msgSend$setImageData:
+ _objc_msgSend$setToolIconData:
+ _objc_msgSend$toolIconData
+ _updateBundleIdToOnenessBundleIdMapping:.onceToken
- +[SPUISAppBrowseSectionBuilder _appInfoForBundleID:]
- +[SPUISAppBrowseSectionBuilder _resultForAppIdentity:]
- +[SPUISAppBrowseSectionBuilder sectionBundleIdentifier]
- +[SPUISBrowseSectionBuilder _sectionResultForResults:style:withSectionTitle:]
- +[SPUISBrowseSectionBuilder sectionBundleIdentifier]
- +[SPUISFilesBrowseSectionBuilder sectionBundleIdentifier]
- -[SPUISFileResultBuilder lastUsedDate]
- -[SPUISFileResultBuilder setLastUsedDate:]
- _OBJC_CLASS_$_ATXAppIdentity
- _OBJC_CLASS_$_NSConstantDictionary
- _OBJC_CLASS_$_SFCommand
- _OBJC_CLASS_$_SPUISQuickLookCommand
- _OBJC_IVAR_$_SPUISFileResultBuilder._lastUsedDate
- _OBJC_METACLASS_$_SFCommand
- _OBJC_METACLASS_$_SPUISQuickLookCommand
- __OBJC_CLASS_RO_$_SPUISQuickLookCommand
- __OBJC_METACLASS_RO_$_SPUISQuickLookCommand
- ___block_literal_global.425
- ___block_literal_global.426
- ___block_literal_global.488
- ___block_literal_global.507
- ___block_literal_global.510
- ___block_literal_global.513
- ___block_literal_global.515
- ___block_literal_global.517
- ___block_literal_global.520
- ___block_literal_global.569
- ___block_literal_global.572
- ___block_literal_global.577
- _objc_msgSend$_resultForAppIdentity:
- _objc_msgSend$_sectionResultForResults:style:withSectionTitle:
- _objc_msgSend$initWithBundleIdentifier:appType:
CStrings:
+ "@44@0:8@16i24@28@36"
+ "T@\"NSData\",&,V_toolIconData"
+ "T@\"NSDate\",&,N"
+ "_bundleIdToOnenessBundleId"
+ "_resultForAppIdentity:bundleIdToOnenessBundleIdMapping:"
+ "_sectionResultForResults:style:sectionTitle:sectionIdentifier:"
+ "_toolIconData"
+ "com.apple.spotlight.zkw.apps"
+ "com_apple_shortcuts_spotlight_tool_icon"
+ "hasOnenessCounterpart"
+ "highlightedMatchedText"
+ "setImageData:"
+ "setToolIconData:"
+ "skipExecution"
+ "toolIconData"
+ "updateBundleIdToOnenessBundleIdMapping:"
+ "visited %@"
- "@36@0:8@16i24@28"
- "SPUISQuickLookCommand"
- "_appInfoForBundleID:"
- "_resultForAppIdentity:"
- "_sectionResultForResults:style:withSectionTitle:"
- "initWithBundleIdentifier:appType:"

```
