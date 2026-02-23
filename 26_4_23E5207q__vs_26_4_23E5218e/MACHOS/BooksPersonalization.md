## BooksPersonalization

> `/private/var/staged_system_apps/Books.app/Frameworks/BooksPersonalization.framework/BooksPersonalization`

```diff

-6556.0.0.0.0
-  __TEXT.__text: 0x1ac7e8
-  __TEXT.__auth_stubs: 0x2660
+6562.0.0.0.0
+  __TEXT.__text: 0x1b6a10
+  __TEXT.__auth_stubs: 0x2680
   __TEXT.__objc_stubs: 0xc20
   __TEXT.__objc_methlist: 0x140
-  __TEXT.__const: 0x1e100
+  __TEXT.__const: 0x1e3c0
   __TEXT.__objc_classname: 0x11c2
   __TEXT.__objc_methname: 0x11a5
   __TEXT.__objc_methtype: 0x38
-  __TEXT.__constg_swiftt: 0x5094
-  __TEXT.__swift5_typeref: 0x69c2
-  __TEXT.__swift5_reflstr: 0x5029
-  __TEXT.__swift5_fieldmd: 0x6e28
-  __TEXT.__swift5_builtin: 0x17c
-  __TEXT.__swift5_assocty: 0xce8
-  __TEXT.__swift5_proto: 0x195c
-  __TEXT.__swift5_types: 0x804
-  __TEXT.__swift_as_entry: 0x270
-  __TEXT.__swift_as_ret: 0x334
-  __TEXT.__cstring: 0x39b2
-  __TEXT.__swift5_protos: 0xf0
-  __TEXT.__swift5_capture: 0x640
-  __TEXT.__swift5_mpenum: 0x2ec
-  __TEXT.__oslogstring: 0xd4b
-  __TEXT.__unwind_info: 0x6bb0
-  __TEXT.__eh_frame: 0xe594
-  __DATA_CONST.__auth_got: 0x1338
-  __DATA_CONST.__got: 0x5d0
-  __DATA_CONST.__auth_ptr: 0xe80
-  __DATA_CONST.__const: 0x13f20
+  __TEXT.__constg_swiftt: 0x5128
+  __TEXT.__swift5_typeref: 0x6b32
+  __TEXT.__swift5_reflstr: 0x5179
+  __TEXT.__swift5_fieldmd: 0x6f04
+  __TEXT.__swift5_builtin: 0x190
+  __TEXT.__swift5_assocty: 0xd18
+  __TEXT.__swift5_proto: 0x198c
+  __TEXT.__swift5_types: 0x810
+  __TEXT.__swift_as_entry: 0x278
+  __TEXT.__swift_as_ret: 0x34c
+  __TEXT.__cstring: 0x3ac2
+  __TEXT.__swift5_protos: 0xf4
+  __TEXT.__swift5_capture: 0x630
+  __TEXT.__swift5_mpenum: 0x2f4
+  __TEXT.__oslogstring: 0x104b
+  __TEXT.__unwind_info: 0x6d00
+  __TEXT.__eh_frame: 0xea8c
+  __DATA_CONST.__auth_got: 0x1348
+  __DATA_CONST.__got: 0x5d8
+  __DATA_CONST.__auth_ptr: 0xea8
+  __DATA_CONST.__const: 0x14158
   __DATA_CONST.__objc_classlist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x36b8
   __DATA.__objc_selrefs: 0x330
   __DATA.__objc_data: 0x8a0
-  __DATA.__data: 0x7ee0
-  __DATA.__bss: 0x30aa0
+  __DATA.__data: 0x8040
+  __DATA.__bss: 0x30fa0
   __DATA.__common: 0xc0
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 64E90147-B062-385A-86EC-AD8E07BCEA46
-  Functions: 8706
+  UUID: 8185B9D8-59C3-3E0C-A0A3-6D7FA2DFBD26
+  Functions: 8804
   Symbols:   220
-  CStrings:  777
+  CStrings:  790
 
CStrings:
+ "BooksPersonalization.BookHistory"
+ "BooksPersonalization.CollectionRecommendationFilter"
+ "BooksPersonalization.RecommendationPenalty"
+ "BooksPersonalization.SeriesHistory"
+ "[BookDecline] Book %llu: DECLINED (explicit Less Like This)"
+ "[BookDecline] Book %llu: NOT eligible for decline (implied by engagement)"
+ "[BookDecline] Book %llu: declined=%{bool}d daysRecommendedCount=%ld, daysRecommendationPassedOverCount=%ld, declinedByRecommendations=%{bool}d, declinedByPassovers=%{bool}d"
+ "[Filter] Series %llu declined - filtering candidate book %llu"
+ "[PeriodicPenalty] storeID:%s: earnedPenalty=%ld, consecutiveDaysNotRecommended=%ld, shouldApply=%{bool}d"
+ "[SeriesDecline] Series %llu: NOT declined (candidate book %llu has engagement)"
+ "[SeriesDecline] Series %llu: declined=%{bool}d daysRecommendedCount=%ld, daysRecommendationPassedOverCount=%ld, declinedByRecommendations=%{bool}d, declinedByPassovers=%{bool}d"
+ "seriesID timestamp "
+ "seriesImpression"

```
