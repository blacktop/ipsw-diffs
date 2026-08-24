## Translation

> `/System/Library/Frameworks/Translation.framework/Versions/A/Translation`

```diff

-385.0.0.0.0
-  __TEXT.__text: 0x61e14
-  __TEXT.__objc_methlist: 0x5cb0
+389.0.0.0.0
+  __TEXT.__text: 0x62a24
+  __TEXT.__objc_methlist: 0x5e10
   __TEXT.__const: 0xfa0
-  __TEXT.__cstring: 0x33b4
-  __TEXT.__oslogstring: 0x5176
-  __TEXT.__gcc_except_tab: 0xb44
+  __TEXT.__cstring: 0x3464
+  __TEXT.__oslogstring: 0x5336
+  __TEXT.__gcc_except_tab: 0xb4c
   __TEXT.__ustring: 0x90
   __TEXT.__swift5_typeref: 0x639
   __TEXT.__constg_swiftt: 0x3e4

   __TEXT.__swift_as_entry: 0x4c
   __TEXT.__swift_as_ret: 0x50
   __TEXT.__swift_as_cont: 0x84
-  __TEXT.__unwind_info: 0x1c58
+  __TEXT.__unwind_info: 0x1c80
   __TEXT.__eh_frame: 0x8c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x698
-  __DATA_CONST.__objc_classlist: 0x328
+  __DATA_CONST.__const: 0x6c8
+  __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2850
+  __DATA_CONST.__objc_selrefs: 0x2898
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x2a8
-  __DATA_CONST.__objc_arraydata: 0x178
-  __DATA_CONST.__got: 0x5c0
-  __AUTH_CONST.__const: 0x2c00
-  __AUTH_CONST.__cfstring: 0x3c80
-  __AUTH_CONST.__objc_const: 0xbde0
-  __AUTH_CONST.__objc_arrayobj: 0xd8
+  __DATA_CONST.__objc_superrefs: 0x2b0
+  __DATA_CONST.__objc_arraydata: 0x1a0
+  __DATA_CONST.__got: 0x5c8
+  __AUTH_CONST.__const: 0x2c40
+  __AUTH_CONST.__cfstring: 0x3e40
+  __AUTH_CONST.__objc_const: 0xc0f8
+  __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x920
-  __AUTH.__objc_data: 0x48
+  __AUTH.__objc_data: 0x98
   __AUTH.__data: 0x338
-  __DATA.__objc_ivar: 0x8b0
+  __DATA.__objc_ivar: 0x8e0
   __DATA.__data: 0xba0
-  __DATA.__bss: 0x1060
+  __DATA.__bss: 0x1080
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x1ec8
   __DATA_DIRTY.__data: 0x3a8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2920
-  Symbols:   5364
-  CStrings:  931
+  Functions: 2956
+  Symbols:   5433
+  CStrings:  952
 
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
+ GCC_except_table142
+ GCC_except_table40
+ GCC_except_table41
+ GCC_except_table60
+ GCC_except_table71
+ GCC_except_table72
+ GCC_except_table81
+ GCC_except_table86
+ OBJC_IVAR_$__LTCombinedTranslationResult._engineInfo
+ OBJC_IVAR_$__LTTextResult._engineInfo
+ OBJC_IVAR_$__LTTextSession._configuration
+ OBJC_IVAR_$__LTTextSession._originatingProcessIdentifier
+ OBJC_IVAR_$__LTTextSessionConfiguration._isHeadless
+ OBJC_IVAR_$__LTTextSessionConfiguration._originatingProcessIdentifier
+ OBJC_IVAR_$__LTTextSessionConfiguration._preferredStrategy
+ OBJC_IVAR_$__LTTextSessionConfiguration._sourceLocale
+ OBJC_IVAR_$__LTTextSessionConfiguration._targetLocale
+ OBJC_IVAR_$__LTTranslationContext._originatingProcessIdentifier
+ OBJC_IVAR_$__LTTranslationRequest._originatingProcessIdentifier
+ OBJC_IVAR_$__LTTranslationResult._engineInfo
+ _LTOSLogVariantFiltering
+ _LTOSLogVariantFiltering.log
+ _LTOSLogVariantFiltering.onceToken
+ _LTSupportedLocaleDefaultLIDLanguageMapping
+ _LTSupportedLocaleDefaultLIDLanguageMapping.mapping
+ _LTSupportedLocaleDefaultLIDLanguageMapping.onceToken
+ _OBJC_CLASS_$__LTTextSessionConfiguration
+ _OBJC_METACLASS_$__LTTextSessionConfiguration
+ __LTEngineInfoDescription
+ __LTOSLogVariantFiltering
+ __LTSupportedLocaleDefaultLIDLanguageMapping
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
- GCC_except_table140
- GCC_except_table24
- GCC_except_table28
- GCC_except_table63
- GCC_except_table70
- GCC_except_table74
- GCC_except_table79
- _objc_msgSend$initWithLocalePair:sourceAttributedText:targetAttributedText:clientIdentifier:
- _objc_msgSend$initWithLocalePair:sourceText:targetText:clientIdentifier:
CStrings:
+ "Debug setting to prevent language variant filtering enabled. Will show all supported variants in UI"
+ "Filtered %zu supported languages into %zu to display"
+ "NSLocale.currentLocale.regionCode: %{public}@"
+ "NSLocale.preferredLanguages: %{public}@"
+ "Not creating _LTCombinedTranslationResult instance because a translation result has engineInfo %zd, which is mismatched from other results with engineInfo %zd"
+ "Translation completed using engine: %{public}@"
+ "VariantFiltering"
+ "ai-afm-lora"
+ "ai-ifp-lora"
+ "ai-mt-expert"
+ "ar"
+ "ar_AE"
+ "de_AT"
+ "engineInfo"
+ "nl"
+ "nl_NL"
+ "none"
+ "originatingProcessIdentifier"
+ "traditional"
+ "traditional-server"
+ "unknown(%ld)"
+ "\xc2"
- "\xa2"
```
