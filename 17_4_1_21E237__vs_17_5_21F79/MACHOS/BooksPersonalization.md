## BooksPersonalization

> `/private/var/staged_system_apps/Books.app/Frameworks/BooksPersonalization.framework/BooksPersonalization`

```diff

-6040.0.0.0.0
-  __TEXT.__text: 0x103cc0
-  __TEXT.__auth_stubs: 0x1fa0
+6070.12.1.0.0
+  __TEXT.__text: 0x16e02c
+  __TEXT.__auth_stubs: 0x2030
   __TEXT.__objc_methlist: 0xb4
-  __TEXT.__const: 0xd830
-  __TEXT.__cstring: 0x38e3
-  __TEXT.__constg_swiftt: 0x307c
-  __TEXT.__swift5_typeref: 0x3d22
-  __TEXT.__swift5_reflstr: 0x2fb1
-  __TEXT.__swift5_fieldmd: 0x3e10
-  __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_proto: 0xd88
-  __TEXT.__swift5_types: 0x4a0
-  __TEXT.__swift5_assocty: 0x840
-  __TEXT.__swift5_protos: 0xb8
-  __TEXT.__objc_methname: 0x4c4
-  __TEXT.__swift5_capture: 0x26c
-  __TEXT.__swift5_mpenum: 0x88
-  __TEXT.__unwind_info: 0x5958
-  __TEXT.__eh_frame: 0x8a60
-  __DATA_CONST.__auth_got: 0xfd0
-  __DATA_CONST.__got: 0x3f0
-  __DATA_CONST.__auth_ptr: 0x170
-  __DATA_CONST.__const: 0x9e80
-  __DATA_CONST.__objc_classlist: 0x170
+  __TEXT.__const: 0xfbe0
+  __TEXT.__cstring: 0x4333
+  __TEXT.__constg_swiftt: 0x37ec
+  __TEXT.__swift5_typeref: 0x48c2
+  __TEXT.__swift5_reflstr: 0x3a26
+  __TEXT.__swift5_fieldmd: 0x48dc
+  __TEXT.__swift5_builtin: 0x104
+  __TEXT.__swift5_proto: 0xfb4
+  __TEXT.__swift5_types: 0x544
+  __TEXT.__swift5_assocty: 0x930
+  __TEXT.__swift5_protos: 0xc8
+  __TEXT.__objc_methname: 0x51d
+  __TEXT.__swift5_capture: 0x3cc
+  __TEXT.__swift5_mpenum: 0x2b4
+  __TEXT.__unwind_info: 0x6dc4
+  __TEXT.__eh_frame: 0xadb8
+  __DATA_CONST.__auth_got: 0x1018
+  __DATA_CONST.__got: 0x420
+  __DATA_CONST.__auth_ptr: 0x188
+  __DATA_CONST.__const: 0xb4f8
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0xa8
-  __DATA.__objc_const: 0x2360
-  __DATA.__objc_selrefs: 0x208
-  __DATA.__objc_data: 0x3c8
-  __DATA.__data: 0x8a90
-  __DATA.__bss: 0x1a000
+  __DATA_CONST.__objc_classrefs: 0xb0
+  __DATA.__objc_const: 0x2a30
+  __DATA.__objc_selrefs: 0x238
+  __DATA.__objc_data: 0x418
+  __DATA.__data: 0xa300
+  __DATA.__bss: 0x1e380
   __DATA.__common: 0xa8
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation
-  - /System/Library/PrivateFrameworks/TeaSettings.framework/TeaSettings
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7385
-  Symbols:   184
-  CStrings:  486
+  Functions: 8823
+  Symbols:   189
+  CStrings:  559
 
Symbols:
+ _OBJC_CLASS_$_NSUserDefaults
+ _dispatch_semaphore_create
+ _swift_defaultActor_deallocate
+ _swift_defaultActor_destroy
+ _swift_defaultActor_initialize
CStrings:
+ " integrating results of request "
+ " launching known type request "
+ " launching unknown type request "
+ " secondsSinceExplicitDecline="
+ " to borrowing request "
+ "$defaultActor"
+ "6449246700 about to calculate finishedIntervalSinceReferenceDate"
+ "6449246700 finishedDate=%s"
+ "AllCollectionTypesFillingClusteringService clustering %ld books books=%ld audiobooks=%ld seriesBooks=%ld"
+ "BKDebugODPClusteringEnabled"
+ "BooksClusteringService"
+ "Clustered: %s"
+ "Clustering %ld books diversified=%ld allowSingleBooks=%{bool}d allowSeriesBooks=%{bool}d maxHighScoringSingleBookCollectionCount=%ld thresholdRatio=%f books=%ld audiobooks=%ld seriesBooks=%ld"
+ "Common schema library for both Books Personalization Server and AMP Reco Service"
+ "Error fetching legacy MAPI collection: %s"
+ "Filtering recommendations because earlier selections already used the series or mapped series ID: %s"
+ "Overall request "
+ "Remedial request for "
+ "Similar titles within suggestions, removed later candidates: %s"
+ "_TtC20BooksPersonalization31CollectionRecommendationsScorer"
+ "_TtC20BooksPersonalization34CollectionRecommendationsGenerator"
+ "_TtC20BooksPersonalization35SeedBasedMoreFromYourAuthorsService"
+ "_TtC20BooksPersonalization42AllCollectionTypesFillingClusteringService"
+ "_TtCV20BooksPersonalizationP33_70376CE8EC2D09E5A49FA5EEA60ED9CA16RequestListActor9ActorType"
+ "acquiredExternallyUnknownFinishedInterval"
+ "authorAndMediaType"
+ "authorIDs"
+ "bisacCodes"
+ "book"
+ "bookAuthors"
+ "bookHistoryAuthorFetchMaxCount"
+ "bookIdToMetadataEntries"
+ "bookIds"
+ "booksBasedOnSeed"
+ "booksByAuthor"
+ "booksByAuthorsService"
+ "booksBySuggestedAuthors"
+ "booksBySuggestedAuthorsServicesBySource"
+ "booksInGenre"
+ "booksInGenrePermittedGenres"
+ "boolForKey:"
+ "cacheMetadata(_:moc:)"
+ "candidateSingleBooks"
+ "collectionRecommendationTypeToUtility"
+ "collectionRecommendations"
+ "descendingOrderByScore"
+ "genreAndMediaType"
+ "indefiniteAuthorIDs"
+ "level"
+ "logger"
+ "mangaYouMightLike"
+ "mangaYouMightLikeServicesBySource"
+ "mappedSeriesID"
+ "maxBooksForCollection"
+ "minBooksForCollection"
+ "mixed"
+ "ndcgDiscountRate"
+ "orphanScoredBooks"
+ "profileGenreDenylistForBooks"
+ "rankBoostByCollectionRecommendationType"
+ "requestsInFlight"
+ "score"
+ "secondsSinceExplicitDecline"
+ "seedBookAcrossMediaTypes"
+ "selectedBookIDs"
+ "selectedSingleBookIds"
+ "series"
+ "seriesID"
+ "setMappedSeriesID:"
+ "setSeriesID:"
+ "sortedBooksByMediaType"
+ "standardUserDefaults"
+ "storeBookUnknownFinishedIntervalSincePurchase"
+ "thresholdRatio"
+ "ulyssesEmbedding"
+ "v20240223.sqlite"
- "Client and Books service API"
- "http://localhost:18060"
- "identifiersQueuedForCache"
- "identifiersQueuedForNetwork"
- "v20230927.sqlite"

```
