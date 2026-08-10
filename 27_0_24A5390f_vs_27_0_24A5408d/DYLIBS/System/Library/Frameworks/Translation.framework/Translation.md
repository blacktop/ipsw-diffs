## Translation

> `/System/Library/Frameworks/Translation.framework/Translation`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-385.0.0.0.0
-  __TEXT.__text: 0x5c160
-  __TEXT.__objc_methlist: 0x5cb0
+388.0.0.0.0
+  __TEXT.__text: 0x5cb08
+  __TEXT.__objc_methlist: 0x5e10
   __TEXT.__const: 0xf68
-  __TEXT.__cstring: 0x33b4
-  __TEXT.__oslogstring: 0x5176
-  __TEXT.__gcc_except_tab: 0xb3c
+  __TEXT.__cstring: 0x3414
+  __TEXT.__oslogstring: 0x5306
+  __TEXT.__gcc_except_tab: 0xb44
   __TEXT.__ustring: 0x90
   __TEXT.__swift5_typeref: 0x607
   __TEXT.__constg_swiftt: 0x3e4

   __TEXT.__swift_as_entry: 0x4c
   __TEXT.__swift_as_ret: 0x50
   __TEXT.__swift_as_cont: 0x84
-  __TEXT.__unwind_info: 0x1c50
+  __TEXT.__unwind_info: 0x1c78
   __TEXT.__eh_frame: 0x8e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1ea0
-  __DATA_CONST.__objc_classlist: 0x328
+  __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2850
+  __DATA_CONST.__objc_selrefs: 0x2898
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x2a8
-  __DATA_CONST.__objc_arraydata: 0x178
-  __DATA_CONST.__got: 0x598
-  __AUTH_CONST.__const: 0x1010
-  __AUTH_CONST.__cfstring: 0x3c80
-  __AUTH_CONST.__objc_const: 0xbde0
-  __AUTH_CONST.__objc_arrayobj: 0xd8
+  __DATA_CONST.__objc_superrefs: 0x2b0
+  __DATA_CONST.__objc_arraydata: 0x1a0
+  __DATA_CONST.__got: 0x5a0
+  __AUTH_CONST.__const: 0x1050
+  __AUTH_CONST.__cfstring: 0x3d60
+  __AUTH_CONST.__objc_const: 0xc0f8
+  __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0xa60
-  __AUTH.__objc_data: 0xe8
+  __AUTH.__objc_data: 0x138
   __AUTH.__data: 0x338
-  __DATA.__objc_ivar: 0x8b0
+  __DATA.__objc_ivar: 0x8e0
   __DATA.__data: 0xb70
-  __DATA.__bss: 0x1070
+  __DATA.__bss: 0x1090
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x1e28
   __DATA_DIRTY.__data: 0x3a8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2861
-  Symbols:   5254
-  CStrings:  931
+  Functions: 2896
+  Symbols:   5324
+  CStrings:  944
 
Symbols:
+ +[_LTLanguageVariantFilter _hiRequestedLanguageIdentifiers]
+ -[_LTCombinedTranslationResult engineInfo]
+ -[_LTLanguageVariantFilter deviceRegionForFilter:]
+ -[_LTTextResult engineInfo]
+ -[_LTTextResult initWithLocalePair:sourceAttributedText:targetAttributedText:clientIdentifier:engineInfo:]
+ -[_LTTextResult initWithLocalePair:sourceText:targetText:clientIdentifier:engineInfo:]
+ -[_LTTextSession _initWithConfiguration:]
+ -[_LTTextSession configuration]
+ -[_LTTextSession initWithConfiguration:]
+ -[_LTTextSession originatingProcessIdentifier]
+ -[_LTTextSessionConfiguration .cxx_destruct]
+ -[_LTTextSessionConfiguration copyWithZone:]
+ -[_LTTextSessionConfiguration init]
+ -[_LTTextSessionConfiguration isHeadless]
+ -[_LTTextSessionConfiguration originatingProcessIdentifier]
+ -[_LTTextSessionConfiguration preferredStrategy]
+ -[_LTTextSessionConfiguration setIsHeadless:]
+ -[_LTTextSessionConfiguration setOriginatingProcessIdentifier:]
+ -[_LTTextSessionConfiguration setPreferredStrategy:]
+ -[_LTTextSessionConfiguration setSourceLocale:]
+ -[_LTTextSessionConfiguration setTargetLocale:]
+ -[_LTTextSessionConfiguration sourceLocale]
+ -[_LTTextSessionConfiguration targetLocale]
+ -[_LTTranslationContext originatingProcessIdentifier]
+ -[_LTTranslationContext setOriginatingProcessIdentifier:]
+ -[_LTTranslationRequest originatingProcessIdentifier]
+ -[_LTTranslationRequest setOriginatingProcessIdentifier:]
+ -[_LTTranslationResult engineInfo]
+ -[_LTTranslationResult setEngineInfo:]
+ GCC_except_table131
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table47
+ GCC_except_table55
+ GCC_except_table56
+ GCC_except_table65
+ GCC_except_table68
+ GCC_except_table72
+ GCC_except_table75
+ _OBJC_CLASS_$__LTTextSessionConfiguration
+ _OBJC_IVAR_$__LTCombinedTranslationResult._engineInfo
+ _OBJC_IVAR_$__LTTextResult._engineInfo
+ _OBJC_IVAR_$__LTTextSession._configuration
+ _OBJC_IVAR_$__LTTextSession._originatingProcessIdentifier
+ _OBJC_IVAR_$__LTTextSessionConfiguration._isHeadless
+ _OBJC_IVAR_$__LTTextSessionConfiguration._originatingProcessIdentifier
+ _OBJC_IVAR_$__LTTextSessionConfiguration._preferredStrategy
+ _OBJC_IVAR_$__LTTextSessionConfiguration._sourceLocale
+ _OBJC_IVAR_$__LTTextSessionConfiguration._targetLocale
+ _OBJC_IVAR_$__LTTranslationContext._originatingProcessIdentifier
+ _OBJC_IVAR_$__LTTranslationRequest._originatingProcessIdentifier
+ _OBJC_IVAR_$__LTTranslationResult._engineInfo
+ _OBJC_METACLASS_$__LTTextSessionConfiguration
+ __LTOSLogVariantFiltering
+ __LTOSLogVariantFiltering.log
+ __LTOSLogVariantFiltering.onceToken
+ __LTSupportedLocaleDefaultLIDLanguageMapping
+ __LTSupportedLocaleDefaultLIDLanguageMapping.mapping
+ __LTSupportedLocaleDefaultLIDLanguageMapping.onceToken
+ __OBJC_$_CLASS_METHODS__LTLanguageVariantFilter
+ __OBJC_$_CLASS_PROP_LIST__LTLanguageVariantFilter
+ __OBJC_$_INSTANCE_METHODS__LTTextSessionConfiguration
+ __OBJC_$_INSTANCE_VARIABLES__LTTextSessionConfiguration
+ __OBJC_$_PROP_LIST__LTTextSessionConfiguration
+ __OBJC_CLASS_PROTOCOLS_$__LTTextSessionConfiguration
+ __OBJC_CLASS_RO_$__LTTextSessionConfiguration
+ __OBJC_METACLASS_RO_$__LTTextSessionConfiguration
+ ____LTOSLogVariantFiltering_block_invoke
+ ____LTSupportedLocaleDefaultLIDLanguageMapping_block_invoke
+ _objc_msgSend$_hiRequestedLanguageIdentifiers
+ _objc_msgSend$_initWithConfiguration:
+ _objc_msgSend$deviceRegionForFilter:
+ _objc_msgSend$engineInfo
+ _objc_msgSend$initWithLocalePair:sourceAttributedText:targetAttributedText:clientIdentifier:engineInfo:
+ _objc_msgSend$initWithLocalePair:sourceText:targetText:clientIdentifier:engineInfo:
+ _objc_msgSend$originatingProcessIdentifier
+ _objc_msgSend$setOriginatingProcessIdentifier:
+ _objc_msgSend$setSourceLocale:
+ _objc_msgSend$setTargetLocale:
- -[_LTTextResult initWithLocalePair:sourceAttributedText:targetAttributedText:clientIdentifier:]
- -[_LTTextResult initWithLocalePair:sourceText:targetText:clientIdentifier:]
- GCC_except_table129
- GCC_except_table63
- GCC_except_table66
- GCC_except_table70
- GCC_except_table73
- _objc_msgSend$initWithLocalePair:sourceAttributedText:targetAttributedText:clientIdentifier:
- _objc_msgSend$initWithLocalePair:sourceText:targetText:clientIdentifier:
CStrings:
+ "Debug setting to prevent language variant filtering enabled. Will show all supported variants in UI"
+ "Filtered %zu supported languages into %zu to display"
+ "NSLocale.currentLocale.regionCode: %{public}@"
+ "NSLocale.preferredLanguages: %{public}@"
+ "Not creating _LTCombinedTranslationResult instance because a translation result has engineInfo %zd, which is mismatched from other results with engineInfo %zd"
+ "VariantFiltering"
+ "ar"
+ "ar_AE"
+ "de_AT"
+ "engineInfo"
+ "nl"
+ "nl_NL"
+ "originatingProcessIdentifier"
+ "\xc2"
- "\xa2"
```
