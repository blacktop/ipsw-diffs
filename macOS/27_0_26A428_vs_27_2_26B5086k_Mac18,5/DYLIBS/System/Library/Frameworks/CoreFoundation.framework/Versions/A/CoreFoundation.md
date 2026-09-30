## CoreFoundation

> `/System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation`

```diff

-5027.0.69.0.0
-  __TEXT.__text: 0x200a28
+5027.1.2.0.0
+  __TEXT.__text: 0x202cfc
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x8434
+  __TEXT.__objc_methlist: 0x846c
   __TEXT.__const: 0x1a8114
-  __TEXT.__oslogstring: 0xb3a5
-  __TEXT.__cstring: 0xbbbb1
-  __TEXT.__gcc_except_tab: 0x6850
+  __TEXT.__oslogstring: 0xb46d
+  __TEXT.__cstring: 0xbbcab
+  __TEXT.__gcc_except_tab: 0x68c8
   __TEXT.__ustring: 0x1446
   __TEXT.__dlopen_cstrs: 0xcc
   __TEXT.__dof_NSAppNap: 0x4cf
   __TEXT.__dof_CFRunLoop: 0x964
   __TEXT.__dof_Cocoa_Aut: 0x486
-  __TEXT.__unwind_info: 0x8b30
+  __TEXT.__unwind_info: 0x8ba8
   __TEXT.__eh_frame: 0x450
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3ac748
+  __DATA_CONST.__const: 0x3ac768
   __DATA_CONST.__objc_classlist: 0x4c0
   __DATA_CONST.__objc_nlclslist: 0x58
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3150
+  __DATA_CONST.__objc_selrefs: 0x3168
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x328
   __DATA_CONST.__objc_arraydata: 0x1760
   __DATA_CONST.__got: 0x540
-  __AUTH_CONST.__const: 0x93c0
-  __AUTH_CONST.__cfstring: 0xd55e0
+  __AUTH_CONST.__const: 0x93e8
+  __AUTH_CONST.__cfstring: 0xd5600
   __AUTH_CONST.__objc_const: 0xb208
   __AUTH_CONST.__const_cfobj2: 0x40
   __AUTH_CONST.__objc_dictobj: 0x848

   __AUTH.__objc_data: 0xcd0
   __AUTH.__data: 0x120
   __DATA.__objc_ivar: 0x670
-  __DATA.__data: 0x94d
+  __DATA.__data: 0x955
   __DATA.__cf_except_bt: 0x2000
   __DATA.__cf_except_pack: 0x410
   __DATA.__crash_info: 0x148
   __DATA.__common: 0xc0
   __DATA_DIRTY.__objc_data: 0x22b0
   __DATA_DIRTY.__data: 0x198
-  __DATA_DIRTY.__bss: 0xce8
+  __DATA_DIRTY.__bss: 0xce0
   __DATA_DIRTY.__common: 0x3e8
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/CoreServicesInternal.framework/Versions/A/CoreServicesInternal

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/liboah.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9437
-  Symbols:   14854
-  CStrings:  31436
+  Functions: 9469
+  Symbols:   14886
+  CStrings:  31444
 
Symbols:
+ -[CFPDSource needsToCleanUpAfterAcceptingMessage:]
+ -[_CFGeneralPasteboardStore _onqueue_isGenerationLocalOnly:]
+ -[_CFPasteboardStore _onqueue_isGenerationLocalOnly:]
+ -[_CFPasteboardStore handleGetGenerationIsLocalOnly:]
+ -[_CFXPreferences withSourceForIdentifier:user:byHost:container:cloud:createSource:suppressError:perform:]
+ CFPasteboardGetIsGenerationLocalOnly
+ GCC_except_table102
+ GCC_except_table104
+ GCC_except_table109
+ GCC_except_table126
+ GCC_except_table133
+ GCC_except_table143
+ GCC_except_table146
+ GCC_except_table167
+ GCC_except_table175
+ GCC_except_table190
+ GCC_except_table191
+ GCC_except_table201
+ GCC_except_table210
+ GCC_except_table228
+ GCC_except_table234
+ GCC_except_table253
+ GCC_except_table294
+ GCC_except_table295
+ GCC_except_table323
+ GCC_except_table324
+ GCC_except_table335
+ _CFPasteboardGetIsGenerationLocalOnly
+ __123-[_CFXPreferences(SourceAdditions) withSourceForIdentifier:user:byHost:container:cloud:createSource:suppressError:perform:]_block_invoke
+ __53-[_CFPasteboardStore handleGetGenerationIsLocalOnly:]_block_invoke
+ __53-[_CFPasteboardStore handleGetIsExcludedFromHistory:]_block_invoke_2
+ __CFBundleCopyLanguageSearchListWithRootDirectory
+ __CFBundleGetResolvedStringTableCache
+ __CFBundleGetResolvedTableCacheForLocalizations
+ __CFBundleGetStringTableCache
+ __CFBundleIngestResultsIntoExistingCachedResult
+ __CFBundleReleaseStringsSource
+ __CFPreferencesPathErrorsAreFatal
+ __CFPreferencesSetPathErrorsAreFatal
+ ___123-[_CFXPreferences(SourceAdditions) withSourceForIdentifier:user:byHost:container:cloud:createSource:suppressError:perform:]_block_invoke
+ ___123-[_CFXPreferences(SourceAdditions) withSourceForIdentifier:user:byHost:container:cloud:createSource:suppressError:perform:]_block_invoke_2
+ ___123-[_CFXPreferences(SourceAdditions) withSourceForIdentifier:user:byHost:container:cloud:createSource:suppressError:perform:]_block_invoke_3
+ ___123-[_CFXPreferences(SourceAdditions) withSourceForIdentifier:user:byHost:container:cloud:createSource:suppressError:perform:]_block_invoke_4
+ ___53-[_CFPasteboardStore handleGetGenerationIsLocalOnly:]_block_invoke
+ ___53-[_CFPasteboardStore handleGetIsExcludedFromHistory:]_block_invoke_3
+ ___CFBundleSearchForLocalizedString_block_invoke
+ ___CFBundleTestCacheContents
+ ___CFPasteboardGetIsGenerationLocalOnly_block_invoke
+ ___CFPreferencesPathErrorsAreFatal
+ ____copyIngestedCacheResult_block_invoke_3
+ ____copyIngestedCacheResult_block_invoke_4
+ ___block_descriptor_40_e23_v16?0"CFPrefsSource"8l
+ ___block_descriptor_83_e8_32o40r_e25_v16?0^{__CFDictionary=}8l
+ ___block_descriptor_90_e8_32r40r48r_e13_v24?0r^v8*16l
+ ___stringTableFromCacheSatisfyingRequest_block_invoke
+ __postProcessStringsDict
+ __releaseResolvedStringTableCache
+ __releaseStringTableCache
+ __stringTableFromCacheSatisfyingRequest
+ _copyStringTable
+ _handle_get_generation_is_local_only
+ _objc_msgSend$_onqueue_isGenerationLocalOnly:
+ _objc_msgSend$handleGetGenerationIsLocalOnly:
+ _objc_msgSend$needsToCleanUpAfterAcceptingMessage:
+ _stringTableFromCacheSatisfyingRequest
+ withSourceForIdentifier:user:byHost:container:cloud:createSource:suppressError:perform:.registerOnce
- GCC_except_table110
- GCC_except_table124
- GCC_except_table129
- GCC_except_table141
- GCC_except_table150
- GCC_except_table166
- GCC_except_table171
- GCC_except_table173
- GCC_except_table181
- GCC_except_table186
- GCC_except_table188
- GCC_except_table189
- GCC_except_table193
- GCC_except_table208
- GCC_except_table222
- GCC_except_table229
- GCC_except_table248
- GCC_except_table291
- GCC_except_table292
- GCC_except_table321
- GCC_except_table322
- GCC_except_table333
- _CFBundleIngestResultForBundleCache
- __53-[_CFPasteboardStore handleGetIsExcludedFromHistory:]_block_invoke
- __96-[_CFXPreferences(SourceAdditions) withSourceForIdentifier:user:byHost:container:cloud:perform:]_block_invoke
- __CFBundleReleaseStringsSources
- __CFBundleRetainStringsSources
- ___96-[_CFXPreferences(SourceAdditions) withSourceForIdentifier:user:byHost:container:cloud:perform:]_block_invoke
- ___96-[_CFXPreferences(SourceAdditions) withSourceForIdentifier:user:byHost:container:cloud:perform:]_block_invoke_2
- ___96-[_CFXPreferences(SourceAdditions) withSourceForIdentifier:user:byHost:container:cloud:perform:]_block_invoke_3
- ___block_descriptor_64_e8_32r_e18_v32?0r^v8r^v16*24l
- ___block_descriptor_82_e8_32o40r_e25_v16?0^{__CFDictionary=}8l
- __releaseStringsSource
- withSourceForIdentifier:user:byHost:container:cloud:perform:.registerOnce
CStrings:
+ "!addToTables"
+ "!localizationNames || bundle->_cacheAllLocalizedStrings"
+ "!localizations || bundle->_cacheAllLocalizedStrings"
+ "'%@' is an absolute path that is not valid on this operating system."
+ "-[_CFXPreferences(SourceAdditions) withSourceForIdentifier:user:byHost:container:cloud:createSource:suppressError:perform:]"
+ "CFDictionaryGetCount(lookedUpStringsTable) == 0 && CFDictionaryGetCount(lookedUpStringsDictTable) == 0"
+ "CFPasteboardGetIsGenerationLocalOnly('%{public}@' (%{public}@) gen: %ld)"
+ "Unable to specify current generation for CFPasteboardGetIsGenerationLocalOnly - result: %d"
+ "_copyIngestedCacheResult"
+ "_stringTableFromCacheSatisfyingRequest"
+ "addFallbacks"
+ "com.apple.pboard.get-generation-is-local-only"
+ "com.apple.pboard.isLocalOnly"
+ "result: %d gen: %ld isLocalOnly: %d"
- "!existingCachedResult->stringsData"
- "!existingCachedResult->stringsDictData"
- "!existingCachedResult->stringsDictTableURL"
- "!existingCachedResult->stringsTableURL"
- "-[_CFXPreferences(SourceAdditions) withSourceForIdentifier:user:byHost:container:cloud:perform:]"
- "_CFBundleIngestDefaultLocalizationResultsIntoExistingCachedResult"
```
