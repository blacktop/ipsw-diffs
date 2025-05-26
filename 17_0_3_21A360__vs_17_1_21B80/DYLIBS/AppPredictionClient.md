## AppPredictionClient

> `/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient`

```diff

-541.0.5.0.0
-  __TEXT.__text: 0x1681d8
+541.5.2.0.1
+  __TEXT.__text: 0x1684c8
   __TEXT.__auth_stubs: 0xe40
-  __TEXT.__objc_methlist: 0x14778
+  __TEXT.__objc_methlist: 0x14788
   __TEXT.__const: 0x568
-  __TEXT.__cstring: 0x18bef
-  __TEXT.__oslogstring: 0x1565d
+  __TEXT.__cstring: 0x18bdf
+  __TEXT.__oslogstring: 0x1564d
   __TEXT.__gcc_except_tab: 0x1af4
   __TEXT.__dlopen_cstrs: 0x438
   __TEXT.__ustring: 0x18a
-  __TEXT.__unwind_info: 0x5c7c
+  __TEXT.__unwind_info: 0x5ca0
   __TEXT.__objc_classname: 0x33aa
-  __TEXT.__objc_methname: 0x2d3bb
+  __TEXT.__objc_methname: 0x2d39b
   __TEXT.__objc_methtype: 0x5e9c
-  __TEXT.__objc_stubs: 0x196e0
+  __TEXT.__objc_stubs: 0x19720
   __DATA_CONST.__got: 0x2d8
-  __DATA_CONST.__const: 0x5848
+  __DATA_CONST.__const: 0x5898
   __DATA_CONST.__objc_classlist: 0xc28
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x34748
+  __DATA_CONST.__objc_const: 0x347b8
   __DATA_CONST.__objc_selrefs: 0x8a98
   __DATA_CONST.__objc_arraydata: 0xaf0
   __AUTH_CONST.__cfstring: 0x12fa0
-  __AUTH_CONST.__objc_const: 0xa640
+  __AUTH_CONST.__objc_const: 0xa5f8
   __AUTH_CONST.__const: 0x24c0
   __AUTH_CONST.__objc_intobj: 0x9d8
   __AUTH_CONST.__objc_arrayobj: 0x6c0

   __AUTH.__objc_data: 0x3318
   __DATA.__objc_protorefs: 0x98
   __DATA.__objc_classrefs: 0x1258
-  __DATA.__objc_superrefs: 0xa80
-  __DATA.__objc_ivar: 0x18d4
+  __DATA.__objc_superrefs: 0xa88
+  __DATA.__objc_ivar: 0x18d8
   __DATA.__data: 0x18e8
   __DATA.__bss: 0x280
   __DATA_DIRTY.__objc_data: 0x4678

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 9797
-  Symbols:   31025
-  CStrings:  11847
+  Functions: 9796
+  Symbols:   31028
+  CStrings:  11846
 
Symbols:
+ -[ATXFamilyCircleCache .cxx_destruct]
+ -[ATXFamilyCircleCache _cache]
+ -[ATXFamilyCircleCache _fetchFamilyCircleFromCache]
+ -[ATXFamilyCircleCache initWithCachePath:]
+ -[ATXFamilyCircleCache init]
+ _OBJC_IVAR_$_ATXFamilyCircleCache._path
+ __OBJC_$_INSTANCE_VARIABLES_ATXFamilyCircleCache
+ ___71-[ATXFaceSuggestionClient fetchFaceGalleryConfigurationWithCompletion:]_block_invoke.26
+ ___71-[ATXFaceSuggestionClient fetchFaceGalleryConfigurationWithCompletion:]_block_invoke.27
+ ___71-[ATXFaceSuggestionClient fetchFaceSuggestionsForFocusMode:completion:]_block_invoke.30
+ ___71-[ATXFaceSuggestionClient fetchFaceSuggestionsForFocusMode:completion:]_block_invoke.31
+ ___76-[ATXFaceSuggestionClient regenerateFaceGalleryConfigurationWithCompletion:]_block_invoke.22
+ ___76-[ATXFaceSuggestionClient regenerateFaceGalleryConfigurationWithCompletion:]_block_invoke.24
+ ___block_descriptor_48_e8_32bs40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32bs40bs_e49_v24?0"ATXFaceGalleryConfiguration"8"NSError"16ls32l8s40l8
+ _objc_msgSend$_cache
+ _objc_msgSend$_fetchFamilyCircleFromCache
+ _objc_msgSend$initWithCachePath:
- +[ATXFamilyCircleCache cachedDefaultsKey]
- +[ATXFamilyCircleCache lastFetchDateDefaultsKey]
- -[ATXFamilyCircleCache _fetchFamilyCircleWithUserDefaults:]
- -[ATXFamilyCircleCache _fetchFamilyCircleWithUserDefaults:].cold.1
- -[ATXFamilyCircleCache _fetchFamilyCircleWithUserDefaults:].cold.2
- -[ATXSpotlightHidingUIController _hidingPreviewButtonItemsWithBundleIdentifier:context:].cold.2
- -[ATXSpotlightHidingUIController _nameWithNearbySuggestionIdentifier:].cold.1
- __OBJC_$_CLASS_METHODS_ATXFamilyCircleCache
- ___71-[ATXFaceSuggestionClient fetchFaceSuggestionsForFocusMode:completion:]_block_invoke.25
- ___71-[ATXFaceSuggestionClient fetchFaceSuggestionsForFocusMode:completion:]_block_invoke.26
- _objc_msgSend$_fetchFamilyCircleWithUserDefaults:
CStrings:
+ "FetchLockScreenGalleryConfiguration"
+ "RegenerateLockScreenGalleryConfiguration"
+ "_fetchFamilyCircleFromCache"
+ "cached family circle"
+ "familyCircleCache"
+ "initWithCachePath:"
+ "v24@?0@\"ATXFaceGalleryConfiguration\"8@\"NSError\"16"
- "%s: Could not archive new family circle: %@"
- "%s: Could not unarchive cached family circle: %@"
- "-[ATXFamilyCircleCache _fetchFamilyCircleWithUserDefaults:]"
- "_fetchFamilyCircleWithUserDefaults:"
- "cachedDefaultsKey"
- "cachedFamilyCircle"
- "lastFamilyCircleFetchDate"
- "lastFetchDateDefaultsKey"

```
