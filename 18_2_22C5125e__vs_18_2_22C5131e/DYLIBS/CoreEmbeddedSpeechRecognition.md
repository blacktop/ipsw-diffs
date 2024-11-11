## CoreEmbeddedSpeechRecognition

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition`

```diff

-3402.71.2.0.0
-  __TEXT.__text: 0x141c3c
-  __TEXT.__auth_stubs: 0x2b00
-  __TEXT.__objc_methlist: 0x36f8
+3402.74.1.0.0
+  __TEXT.__text: 0x142be8
+  __TEXT.__auth_stubs: 0x2b20
+  __TEXT.__objc_methlist: 0x3778
   __TEXT.__const: 0x10a8
   __TEXT.__swift5_typeref: 0x1960
-  __TEXT.__cstring: 0x98c2
+  __TEXT.__cstring: 0x9af9
   __TEXT.__swift5_capture: 0x2eac
-  __TEXT.__oslogstring: 0x5ead
+  __TEXT.__oslogstring: 0x60ed
   __TEXT.__constg_swiftt: 0xbbc
   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_reflstr: 0x703

   __TEXT.__swift5_protos: 0x4
   __TEXT.__gcc_except_tab: 0x988
   __TEXT.__ustring: 0x112
-  __TEXT.__unwind_info: 0x1fe0
+  __TEXT.__unwind_info: 0x2008
   __TEXT.__eh_frame: 0x208c
   __TEXT.__objc_classname: 0x8f5
-  __TEXT.__objc_methname: 0xce51
-  __TEXT.__objc_methtype: 0x292d
-  __TEXT.__objc_stubs: 0x7640
-  __DATA_CONST.__got: 0x1000
-  __DATA_CONST.__const: 0x1420
+  __TEXT.__objc_methname: 0xcf87
+  __TEXT.__objc_methtype: 0x2965
+  __TEXT.__objc_stubs: 0x7700
+  __DATA_CONST.__got: 0x1018
+  __DATA_CONST.__const: 0x1448
   __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b68
+  __DATA_CONST.__objc_selrefs: 0x2bb0
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x198
+  __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x240
-  __AUTH_CONST.__auth_got: 0x1598
+  __AUTH_CONST.__auth_got: 0x15a8
   __AUTH_CONST.__auth_ptr: 0x4b0
-  __AUTH_CONST.__const: 0x80d0
-  __AUTH_CONST.__cfstring: 0x5fa0
-  __AUTH_CONST.__objc_const: 0x7b48
-  __AUTH_CONST.__objc_intobj: 0x5a0
+  __AUTH_CONST.__const: 0x80f0
+  __AUTH_CONST.__cfstring: 0x6040
+  __AUTH_CONST.__objc_const: 0x7bb0
+  __AUTH_CONST.__objc_intobj: 0x5b8
   __AUTH_CONST.__objc_arrayobj: 0x300
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x434
+  __DATA.__objc_ivar: 0x438
   __DATA.__data: 0x1438
-  __DATA.__bss: 0x598
+  __DATA.__bss: 0x5b0
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x1440
   __DATA_DIRTY.__data: 0x1770

   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
+  - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets
   - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet
   - /System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3845
-  Symbols:   2133
-  CStrings:  3825
+  Functions: 3859
+  Symbols:   2152
+  CStrings:  3860
 
Symbols:
+ _CacheDeletePurgeSpaceWithInfo
+ _EARErrorDomain
+ _NSFileSystemFreeSize
+ _NSOpenStepRootDirectory
+ _OBJC_CLASS_$_NSByteCountFormatter
CStrings:
+ "%!s(MISSING) CacheDelete failed to return any results."
+ "%!s(MISSING) CacheDelete purged %!@(MISSING) (requested %!@(MISSING))."
+ "%!s(MISSING) CacheDelete reported an error: %!@(MISSING)"
+ "%!s(MISSING) Error requesting model compilation for the primary %!@(MISSING) asset: %!@(MISSING)"
+ "%!s(MISSING) Failed to evaluate the free space on volume: %!@(MISSING)"
+ "%!s(MISSING) Failed to retrieve file system attributes, error: %!@(MISSING)"
+ "%!s(MISSING) File system attributes did not contain a value for NSFileSystemFreeSize."
+ "%!s(MISSING) Free space (%!@(MISSING)) already meets or exceeds the requested space: %!@(MISSING)"
+ "%!s(MISSING) Requested CacheDelete to purge %!@(MISSING) from volume: %!@(MISSING)"
+ "%!s(MISSING) The volume and/or amount to purge was not specified: %!@(MISSING)"
+ "%!s(MISSING) path cannot be nil."
+ "+[CESRUtilities _cacheDeletePurgeSpaceWithInfo:completion:]"
+ "+[CESRUtilities _cacheDeletePurgeSpaceWithInfo:completion:]_block_invoke"
+ "+[CESRUtilities _freeSpaceInBytesForPath:]"
+ "+[CESRUtilities purgeSpaceForModelCompilationAsNeeded:completion:]"
+ "+[CoreEmbeddedSpeechRecognizer compilePrimaryAssistantAssetWithCompletion:]"
+ "+[CoreEmbeddedSpeechRecognizer compilePrimaryAssistantAssetWithCompletion:]_block_invoke"
+ "-[CESRGeoLMRegionIDCache lastUsedGeoLMRegionIdForLanguage:]"
+ "-[CESRGeoLMRegionIDCache purgeUnusedGeoLMRegionIdFromCacheForLanguage:]"
+ "-[CESRGeoLMRegionIDCache purgeUserDefaultsGeoLMAssetsInfoDictForLanguages:]"
+ "@\"NSUserDefaults\""
+ "CACHE_DELETE_AMOUNT"
+ "CACHE_DELETE_ERROR"
+ "CACHE_DELETE_URGENCY"
+ "CACHE_DELETE_VOLUME"
+ "_cacheDeletePurgeSpaceWithInfo:completion:"
+ "_freeSpaceInBytesForPath:"
+ "_userDefaults"
+ "attributesOfFileSystemForPath:error:"
+ "com.apple.siri.embeddedspeech.compilation.%!@(MISSING).primary"
+ "compilePrimaryAssistantAssetWithCompletion:"
+ "initWithUserDefaults:"
+ "isEARError:"
+ "isInsufficientDiskSpaceError:"
+ "purgeSpaceForModelCompilationAsNeeded:completion:"
+ "stringFromByteCount:countStyle:"
+ "v16@?0^{__CFDictionary=}8"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "v32@0:8Q16@?<v@?B@\"NSError\">24"
- "+[CESRGeoLMRegionIDCache lastUsedGeoLMRegionIdForLanguage:]"
- "+[CESRGeoLMRegionIDCache purgeUnusedGeoLMRegionIdFromCacheForLanguage:]"
- "+[CESRGeoLMRegionIDCache purgeUserDefaultsGeoLMAssetsInfoDictForLanguages:]"
- "v32@0:8Q16@?<v@?B>24"

```
