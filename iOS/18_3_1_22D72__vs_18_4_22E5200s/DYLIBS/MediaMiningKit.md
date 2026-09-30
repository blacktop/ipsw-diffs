## MediaMiningKit

> `/System/Library/PrivateFrameworks/MediaMiningKit.framework/MediaMiningKit`

```diff

-742.0.141.0.0
-  __TEXT.__text: 0x6ae84
-  __TEXT.__auth_stubs: 0xca0
-  __TEXT.__objc_methlist: 0x6adc
-  __TEXT.__const: 0x600
+750.5.104.0.0
+  __TEXT.__text: 0x6b5cc
+  __TEXT.__auth_stubs: 0xc90
+  __TEXT.__objc_methlist: 0x7108
+  __TEXT.__const: 0x5f8
   __TEXT.__swift5_typeref: 0x2a
-  __TEXT.__oslogstring: 0x2528
-  __TEXT.__cstring: 0x3fc2
+  __TEXT.__oslogstring: 0x294a
+  __TEXT.__cstring: 0x3fd7
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_reflstr: 0xa
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x2cf0
-  __TEXT.__unwind_info: 0x1d48
+  __TEXT.__gcc_except_tab: 0x2d30
+  __TEXT.__unwind_info: 0x1d60
   __TEXT.__eh_frame: 0x78
   __TEXT.__objc_classname: 0xf3d
-  __TEXT.__objc_methname: 0x1299e
+  __TEXT.__objc_methname: 0x12a9e
   __TEXT.__objc_methtype: 0x19d9
-  __TEXT.__objc_stubs: 0xc840
+  __TEXT.__objc_stubs: 0xc8e0
   __DATA_CONST.__got: 0x928
-  __DATA_CONST.__const: 0x20c0
+  __DATA_CONST.__const: 0x20e0
   __DATA_CONST.__objc_classlist: 0x450
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4160
+  __DATA_CONST.__objc_selrefs: 0x4208
   __DATA_CONST.__objc_superrefs: 0x310
   __DATA_CONST.__objc_arraydata: 0x1e0
-  __AUTH_CONST.__auth_got: 0x660
+  __AUTH_CONST.__auth_got: 0x658
   __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__const: 0x520
+  __AUTH_CONST.__const: 0x540
   __AUTH_CONST.__cfstring: 0x5260
-  __AUTH_CONST.__objc_const: 0xe440
+  __AUTH_CONST.__objc_const: 0xd938
   __AUTH_CONST.__objc_intobj: 0x3f0
   __AUTH_CONST.__objc_arrayobj: 0x1b0
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x8b8
+  __AUTH.__objc_data: 0x778
   __DATA.__objc_ivar: 0x93c
   __DATA.__data: 0x5d0
-  __DATA.__bss: 0x100
-  __DATA_DIRTY.__objc_data: 0x22e0
+  __DATA.__bss: 0xe0
+  __DATA_DIRTY.__objc_data: 0x2420
   __DATA_DIRTY.__data: 0x40
-  __DATA_DIRTY.__bss: 0x108
+  __DATA_DIRTY.__bss: 0x128
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2437
-  Symbols:   3341
-  CStrings:  4519
+  Functions: 2439
+  Symbols:   3348
+  CStrings:  4536
 
Symbols:
+ _kCLSLocationIngestionDistanceThreshold
+ _kCLSLocationOfInterestVisitHighConfidenceThreshold
- __swift_FORCE_LOAD_$_swiftFileProvider
- _kCLSDisambiguationRadiusHomeWork
CStrings:
+ "Low confidence visit ingested after passing dwell time and relaxed distance threshold. LOI-ID: %@{private}@ | MUID:%{private}llu"
+ "Returning visits after merging high and low confidence visits. High Confidence visit count:%lu | Low Confidence visit count:%lu | Merged Count:%lu"
+ "Visit ingested after exact match with location coordinates. LOI-ID: %@{private}@ | MUID:%{private}llu"
+ "Visit ingested after exact match with placemark location distance. LOI-ID: %@{private}@ | MUID:%{private}llu"
+ "Visit ingested after passing dwell time and relaxed distance threshold. LOI-ID: %@{private}@ | MUID:%{private}llu"
+ "[RoutineLocationIngest] Core Routine is not available"
+ "[RoutineLocationIngest] Error fetching finer granularity map item, error:%@"
+ "[RoutineLocationIngest] Fetched valid finer granularity map item with MUID:%{private}lu"
+ "[RoutineLocationIngest] Finer Granularity Map Item is invalid. Returning unknown MUID"
+ "[RoutineLocationIngest] Map Item not available on inferred map item."
+ "[RoutineLocationIngest] Timeout getting Finer granularity map item from CoreRoutine"
+ "_fetchFinerGranularityMapItemForVisitIdentifier:routineManager:"
+ "fetchFinerGranularityBusinessItemNumberForVisitIdentifier:"
+ "fetchFinerGranularityInferredMapItemWithVisitIdentifier:handler:"
+ "isHighConfidence"
+ "mergeHighConfidenceVisits:withLowConfidenceVisits:"
+ "v24@?0@8@\"NSError\"16"

```
