## com.apple.podcasts.SpotlightIndexExtension

> `/private/var/staged_system_apps/Podcasts.app/PlugIns/com.apple.podcasts.SpotlightIndexExtension.appex/com.apple.podcasts.SpotlightIndexExtension`

```diff

-4025.110.62.2.0
-  __TEXT.__text: 0x8f94
+4025.100.80.0.0
+  __TEXT.__text: 0x9280
   __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_stubs: 0x2480
-  __TEXT.__objc_methlist: 0x96c
-  __TEXT.__const: 0x132
-  __TEXT.__gcc_except_tab: 0xc4
-  __TEXT.__objc_methname: 0x251d
-  __TEXT.__cstring: 0x4b3
-  __TEXT.__oslogstring: 0x588
-  __TEXT.__objc_classname: 0x12a
-  __TEXT.__objc_methtype: 0x4b9
+  __TEXT.__objc_stubs: 0x2560
+  __TEXT.__objc_methlist: 0x9cc
+  __TEXT.__const: 0x142
+  __TEXT.__gcc_except_tab: 0xb0
+  __TEXT.__objc_methname: 0x26a0
+  __TEXT.__cstring: 0x4c3
+  __TEXT.__oslogstring: 0x5bf
+  __TEXT.__objc_classname: 0x127
+  __TEXT.__objc_methtype: 0x4dd
   __TEXT.__swift5_typeref: 0x66
   __TEXT.__swift5_fieldmd: 0x20
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x2d8
+  __TEXT.__unwind_info: 0x2e0
   __DATA_CONST.__auth_got: 0x2a0
-  __DATA_CONST.__got: 0x238
+  __DATA_CONST.__got: 0x240
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x828
-  __DATA_CONST.__cfstring: 0x3c0
+  __DATA_CONST.__const: 0x818
+  __DATA_CONST.__cfstring: 0x3e0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA.__objc_const: 0xff8
-  __DATA.__objc_selrefs: 0xbc0
-  __DATA.__objc_ivar: 0x74
+  __DATA.__objc_const: 0x1088
+  __DATA.__objc_selrefs: 0xc18
+  __DATA.__objc_ivar: 0x80
   __DATA.__objc_data: 0x2f0
   __DATA.__data: 0x1d8
   __DATA.__bss: 0x20

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   - @rpath/PodcastsActions.framework/PodcastsActions
-  UUID: D355492B-2B3D-3881-A55F-BE83B2FE165D
-  Functions: 229
-  Symbols:   201
-  CStrings:  617
+  UUID: 9DD0F57B-C434-34EB-94ED-C49803F94676
+  Functions: 236
+  Symbols:   199
+  CStrings:  640
 
Symbols:
+ _OBJC_CLASS_$_MTCoreSpotlightGlobalReindexer
+ _OBJC_CLASS_$_PFClientUtil
+ _OBJC_METACLASS_$_MTCoreSpotlightGlobalReindexer
+ _kMTCoreSpotlightGlobalReindexBatchSize
- _OBJC_CLASS_$_MTCoreSpotlightIndexBatchGenerator
- _OBJC_METACLASS_$_MTCoreSpotlightIndexBatchGenerator
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "@\"MTCoreSpotlightGlobalReindexer\""
+ "@\"NSArray\""
+ "@24@0:8Q16"
+ "@32@0:8Q16@24"
+ "@40@0:8Q16Q24Q32"
+ "Indexing found a MOID with no backing object with error: %@"
+ "MTCoreSpotlightGlobalReindex_BatchNumber"
+ "MTCoreSpotlightGlobalReindex_IndexInBatch"
+ "MTCoreSpotlightGlobalReindexer"
+ "Q"
+ "Q24@0:8@16"
+ "T@\"MTCoreSpotlightGlobalReindexer\",&,V_indexAllBatchGenerator"
+ "T@\"NSArray\",&,N,V_currentObjectIDList"
+ "TB,R,N,V_cancelled"
+ "TQ,N,V_indexInCurrentBatch"
+ "[Indexing] *** batch processing - #%@ in batch %@ with %@ entities [%@]"
+ "_cancelled"
+ "_currentObjectIDList"
+ "_indexInCurrentBatch"
+ "batchForIndexPath:"
+ "cancelled"
+ "currentObjectIDList"
+ "indexAtPosition:"
+ "indexInBatchForIndexPath:"
+ "indexInCurrentBatch"
+ "indexPathForObjectType:batch:indexInBatch:"
+ "initWithIndexes:length:"
+ "isPodcastsApp"
+ "kMTCoreSpotlightGlobalReindex_ObjectType"
+ "nextBatch"
+ "objectAtIndex:"
+ "objectTypeForIndexPath:"
+ "refreshObject:mergeChanges:"
+ "setCurrentObjectIDList:"
+ "setIndexInCurrentBatch:"
+ "setResultType:"
+ "unsignedIntegerValue"
+ "v24@0:8Q16"
+ "v24@?0@\"NSManagedObject\"8@\"NSIndexPath\"16"
+ "{MTIndexPath=\"object\"Q\"batch\"q}"
- "@\"MTCoreSpotlightIndexBatchGenerator\""
- "@16@?0@\"NSManagedObject\"8"
- "@20@0:8i16"
- "@24@0:8@?16"
- "@28@0:8i16@20"
- "MTCoreSpotlightIndexBatchGenerator"
- "MTCoreSpotlightPartialIndexBatchNumber"
- "MTCoreSpotlightPartialIndexObjectNumber"
- "T@\"MTCoreSpotlightIndexBatchGenerator\",&,V_indexAllBatchGenerator"
- "[Indexing] *** batch processing - continuing batch #%@ with %@ entities [%@]"
- "indexPathForRow:inSection:"
- "integerValue"
- "nextBatchWithTransformationBlock:"
- "nextIndexPath"
- "row"
- "section"
- "v24@?0@\"NSManagedObjectContext\"8@\"NSArray\"16"
- "{MTIndexPath=\"batch\"q\"object\"i}"

```
