## BKLibrary

> `/private/var/staged_system_apps/Books.app/Frameworks/BKLibrary.framework/BKLibrary`

```diff

-6454.0.0.0.0
-  __TEXT.__text: 0x8de2c
-  __TEXT.__auth_stubs: 0x14c0
-  __TEXT.__objc_stubs: 0xbe40
+6460.0.0.0.0
+  __TEXT.__text: 0x8ec98
+  __TEXT.__auth_stubs: 0x1500
+  __TEXT.__objc_stubs: 0xbdc0
   __TEXT.__objc_methlist: 0x6390
-  __TEXT.__const: 0xdac
+  __TEXT.__const: 0xdcc
   __TEXT.__gcc_except_tab: 0x1214
-  __TEXT.__oslogstring: 0x6faf
-  __TEXT.__cstring: 0x714f
-  __TEXT.__objc_methname: 0x1283e
-  __TEXT.__objc_classname: 0x7ff
+  __TEXT.__oslogstring: 0x7036
+  __TEXT.__cstring: 0x721f
+  __TEXT.__objc_methname: 0x127f4
+  __TEXT.__objc_classname: 0x819
   __TEXT.__objc_methtype: 0x2775
   __TEXT.__ustring: 0x40
   __TEXT.__dlopen_cstrs: 0x66
   __TEXT.__constg_swiftt: 0x4e8
-  __TEXT.__swift5_typeref: 0x7f0
+  __TEXT.__swift5_typeref: 0x830
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_reflstr: 0x2aa
   __TEXT.__swift5_fieldmd: 0x32c
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_proto: 0x54
   __TEXT.__swift5_types: 0x40
-  __TEXT.__swift5_capture: 0x228
+  __TEXT.__swift5_capture: 0x238
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift_as_entry: 0xbc
   __TEXT.__swift_as_ret: 0xdc
-  __TEXT.__unwind_info: 0x2048
-  __TEXT.__eh_frame: 0x1498
-  __DATA_CONST.__auth_got: 0xa70
-  __DATA_CONST.__got: 0x6b0
-  __DATA_CONST.__auth_ptr: 0x228
-  __DATA_CONST.__const: 0x2e48
-  __DATA_CONST.__cfstring: 0x54e0
-  __DATA_CONST.__objc_classlist: 0x190
+  __TEXT.__unwind_info: 0x2070
+  __TEXT.__eh_frame: 0x1518
+  __DATA_CONST.__auth_got: 0xa90
+  __DATA_CONST.__got: 0x6c0
+  __DATA_CONST.__auth_ptr: 0x230
+  __DATA_CONST.__const: 0x2ec8
+  __DATA_CONST.__cfstring: 0x54c0
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0xf0
-  __DATA_CONST.__objc_arraydata: 0x368
+  __DATA_CONST.__objc_arraydata: 0x350
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_intobj: 0x240
-  __DATA_CONST.__objc_arrayobj: 0x150
+  __DATA_CONST.__objc_arrayobj: 0x138
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x8b18
-  __DATA.__objc_selrefs: 0x40b8
+  __DATA.__objc_const: 0x8ba8
+  __DATA.__objc_selrefs: 0x40b0
   __DATA.__objc_ivar: 0x4c4
-  __DATA.__objc_data: 0x1468
-  __DATA.__data: 0x1610
+  __DATA.__objc_data: 0x14b8
+  __DATA.__data: 0x1680
   __DATA.__bss: 0xb40
   __DATA.__common: 0x30
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftMetalKit.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - @rpath/BookAnalytics.framework/BookAnalytics
   - @rpath/BookCore.framework/BookCore
-  UUID: 6D622696-AE87-3F7C-B345-B825B1A33CD5
-  Functions: 2944
-  Symbols:   654
-  CStrings:  5141
+  UUID: FEB81B22-AAB9-3E83-A72B-55891B2DA716
+  Functions: 2958
+  Symbols:   658
+  CStrings:  5144
 
Symbols:
+ _OBJC_CLASS_$_BKLibrarySpotlightHelpers
+ _OBJC_METACLASS_$_BKLibrarySpotlightHelpers
+ __swift_FORCE_LOAD_$_swiftIntents
+ _swift_bridgeObjectRetain_n
CStrings:
+ "(isFinished == NULL OR isFinished == NO) AND ((bookHighWaterMarkProgress == NULL OR bookHighWaterMarkProgress < %@) OR notFinished == YES) AND (dateFinished == NULL)"
+ "AppIntents.LibraryAssetProvider"
+ "BKLibrarySpotlightHelpers"
+ "Requested for an asset using contentTypes:%s, term:%s"
+ "appIntentsLibraryAssetsForSearchPredicate: spotlight search query: %s"
+ "appIntentsLibraryAssetsForSearchTerm: executeFetchRequest failed. error: %@"
+ "predicateToExcludeAllFinishedLibraryAssets"
+ "spotlightAssetsWithContentTypes:searchQueryString:inManagedObjectContext:"
+ "spotlightQueryStringForSearchString:attributes:"
- "_fetchLibraryAssetsWithTypes:searchTerm:inManagedObjectContext:"
- "_spotlightAssetsWithContentTypes:searchTerm:inManagedObjectContext:"
- "appIntentsLibraryAssetsWithTypes:searchTerm:inManagedObjectContext:"
- "libraryAssetsForAppIntentsSearchTerm: executeFetchRequest failed. error: %@"
- "queryStringForSearchString:attributes:"

```
