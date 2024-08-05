## SessionAlert

> `/System/Library/PrivateFrameworks/SessionAlert.framework/SessionAlert`

```diff

-198.100.0.0.0
-  __TEXT.__text: 0x19bd4
+200.0.0.0.0
+  __TEXT.__text: 0x19aa0
   __TEXT.__auth_stubs: 0xac0
   __TEXT.__const: 0x15fe
   __TEXT.__cstring: 0x552

   __TEXT.__unwind_info: 0x648
   __TEXT.__eh_frame: 0x468
   __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0x68
+  __DATA_CONST.__const: 0xa8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __AUTH_CONST.__auth_got: 0x560

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 572
-  Symbols:   122
-  CStrings:  129
+  Symbols:   130
+  CStrings:  0
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
- "MIPGenre"
- "MIPLibraryIdentifier"
- "MIPPlaybackInfo"
- "MIPPlaylist"
- "MIPPodcast"
- "MIPSeries"
- "MIPSong"
- "MIPTVShow"
- "ML3AccountStore"
- "ML3ActiveTransaction"
- "ML3AggregateQuery"
- "ML3Album"
- "ML3AlbumArtist"
- "ML3AlbumArtistTable"
- "ML3AllCompoundPredicate"
- "ML3AnyCompoundPredicate"
- "ML3Artist"
- "ML3ArtworkConfiguration"
- "ML3ArtworkTokenSet"
- "ML3BaseLocation"
- "ML3BitMaskPredicate"
- "ML3ChapterTOC"
- "ML3ChapterTable"
- "ML3ClientImportItem"
- "ML3ClientImportServiceSession"
- "ML3Collection"
- "ML3ComparisonPredicate"
- "ML3Composer"
- "ML3ComposerTable"
- "ML3CompoundPredicate"
- "ML3ConditionalPredicate"
- "ML3Container"
- "ML3ContainerItemDiffMetadata"
- "ML3ContainerItemDiffOperation"
- "ML3ContainerItemPerson"
- "ML3ContainerQuery"
- "ML3ContainerTable"
- "ML3ContainmentPredicate"
- "ML3ContainsPredicate"
- "ML3DAAPImportOperation"
- "ML3DaemonClient"
- "ML3DatabaseColumn"
- "ML3DatabaseForeignKeyConstraint"
- "ML3DatabaseFunction"
- "ML3DatabaseFunctionBlock"
- "ML3DatabaseFunctionPointer"
- "ML3DatabaseImportManager"
- "ML3DatabasePrivacyContext"
- "ML3DatabaseStatementCache"
- "ML3DatabaseTable"
- "ML3DatabaseValidation"
- "ML3Entity"
- "ML3ExportItem"
- "ML3Genre"
- "ML3GenreTable"
- "ML3HomeSharingImportOperation"
- "ML3ItemExtraTable"
- "ML3ItemStatsTable"
- "ML3MigrationDirectives"
- "ML3MusicLibrary"
- "ML3MusicLibraryResourcesManagerContext"
- "ML3MusicLibrary_SortMapEntry"
- "ML3MutableDatabaseTable"
- "ML3NegationPredicate"
- "ML3PersistentIDsPredicate"
- "ML3PersonTable"
- "ML3Predicate"
- "ML3ProcessClient"
- "ML3ProcessDownloadedAssetsOperation"
- "ML3PropertyPredicate"
- "ML3ProtoSyncImportOperation"
- "ML3PurchaseHistoryImportOperation"
- "ML3Query"
- "ML3QuerySection"
- "ML3RemoveCloudSourcesOperation"
- "ML3SearchStringPredicate"
- "ML3ServiceDatabaseImport"
- "ML3SortMap"
- "ML3SortMapFaultingEntryArray"
- "ML3SortMapFaultingNameOrderDictionary"
- "ML3StatementCacheList"
- "ML3StatementCacheNode"
- "ML3StoreItemAlbumData"
- "ML3TerminationCoordinator"
- "ML3Track"
- "ML3TruthPredicate"
- "ML3UnaryPredicate"
- "ML3UpdateArtworkInterestDataOperation"
- "MLEQPreset"
- "MLMediaLibraryResourcesServiceClient"
- "MLTrackImportChapter"
- "ManagerAssembly"
- "SCUpdateUserIDCommand"
- "_ML3ArtworkConfigurationMediaArtworkTypeKey"
- "_ML3MultiUserAccountChangeOperation"
- "_ML3SortMapFaultingNameOrderDictionaryEnumerator"
- "_TtC10StocksCore15NewsRegionCheck"
- "_TtC10StocksCore16NewsCoreAssembly"
- "_TtC10StocksCore16SDSMetadataCache"
- "_TtC10StocksCore16SparklineManager"
- "_TtC10StocksCore16StubQuoteService"
- "_TtC10StocksCore17YahooQuoteService"
- "_TtC10StocksCore19FeatureAvailability"
- "_TtC10StocksCore19SDSAuthTokenManager"
- "_TtC10StocksCore19SDSStockFeedService"
- "_TtC10StocksCore20LegacyStocksAssembly"
- "_TtC10StocksCore20StubStockFeedService"
- "_TtC10StocksCore20TestStockFeedService"
- "_TtC10StocksCore21AppConfigurationStore"
- "_TtC10StocksCore21SDSAuthTokenRefresher"
- "_TtC10StocksCore21TestTopStoriesService"
- "_TtC10StocksCore21YahooChartModelEngine"
- "_TtC10StocksCore21YahooStockFeedService"
- "_TtC10StocksCore22HeadlineViewingHistory"
- "_TtC10StocksCore22StockFeedLookupService"
- "_TtC10StocksCore22StubQuoteDetailService"
- "_TtC10StocksCore22UnnecessaryWordRemover"
- "_TtC10StocksCore23AppConfigurationManager"
- "_TtC10StocksCore23WatchlistSortingService"
- "_TtC10StocksCore23YahooQuoteDetailService"
- "_TtC10StocksCore24NewsStockMetadataService"
- "_TtC10StocksCore24YahooAttributionProvider"
- "_TtC10StocksCore29StaticAppConfigurationManager"
- "_TtC10StocksCore30FeedPersonalizerHeadlineScorer"
- "_TtC10StocksCore34StockPriceDataManagerObserverProxy"
- "_TtC10StocksCoreP33_6F15235305946077A82EB95D8E9A724719NewsUserProfileShim"
- "_TtC10StocksCoreP33_8188EFB552A1879D25D8FDAD94CCB0E125PrivateDataActionProvider"
- "_TtC8StoreKitP33_1FB6740A85F65241A77B22F13F1E5BBF19ResourceBundleClass"
- "nager25SubscriptionGroupObserver"

```
