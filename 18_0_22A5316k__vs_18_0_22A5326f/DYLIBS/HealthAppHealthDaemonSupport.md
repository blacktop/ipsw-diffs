## HealthAppHealthDaemonSupport

> `/System/Library/PrivateFrameworks/HealthAppHealthDaemonSupport.framework/HealthAppHealthDaemonSupport`

```diff

-5132.0.0.0.0
-  __TEXT.__text: 0x10768
+5138.0.1.1.0
+  __TEXT.__text: 0x10754
   __TEXT.__auth_stubs: 0xbb0
   __TEXT.__objc_methlist: 0xfc
   __TEXT.__const: 0x87c

   __TEXT.__objc_methname: 0x556
   __TEXT.__objc_methtype: 0x278
   __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0xd0
+  __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60

   __AUTH_CONST.__objc_const: 0x7d8
   __AUTH.__objc_data: 0xd8
   __DATA.__data: 0x328
-  __DATA.__bss: 0x790
+  __DATA.__bss: 0x710
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x298
-  __DATA_DIRTY.__data: 0x210
+  __DATA_DIRTY.__data: 0x208
   __DATA_DIRTY.__common: 0x30
-  __DATA_DIRTY.__bss: 0x500
-  - /System/Library/Frameworks/Combine.framework/Combine
+  __DATA_DIRTY.__bss: 0x580
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
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
   Functions: 580
-  Symbols:   213
-  CStrings:  0
+  Symbols:   221
+  CStrings:  65
 
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
+ "_$s18PodcastsFoundation0A12MediaLibraryC5ErrorO19unrecognizedResultsyA2EmFWC"
+ "_$s18PodcastsFoundation0A12MediaLibraryC5ErrorO37unableToCreateRequestFromQueueContextyA2EmFWC"
+ "_$s18PodcastsFoundation0A12MediaLibraryC5ErrorO9noResultsyA2EmFWC"
+ "_$s18PodcastsFoundation11CacheDomainV10DiskCachesVMn"
+ "_$s18PodcastsFoundation11CacheDomainVMn"
+ "_$s18PodcastsFoundation11EpisodeTypeOSeAAMc"
+ "_$s18PodcastsFoundation12MediaRequestC11ContentTypeO14podcastChannelyA2EmFWC"
+ "_$s18PodcastsFoundation12MediaRequestC11ContentTypeO14podcastEpisodeyA2EmFWC"
+ "_$s18PodcastsFoundation12MediaRequestC11ContentTypeO7podcastyA2EmFWC"
+ "_$s18PodcastsFoundation12MediaRequestC18IncludeExtendTypesO9inLibraryyA2EmFWC"
+ "_$s18PodcastsFoundation12MetricsTopicVMn"
+ "_$s18PodcastsFoundation12StorageSpaceVSEAAMc"
+ "_$s18PodcastsFoundation12StorageSpaceVSQAAMc"
+ "_$s18PodcastsFoundation12StorageSpaceVSeAAMc"
+ "_$s18PodcastsFoundation13AssetLifetimeO13opportunisticyA2CmFWC"
+ "_$s18PodcastsFoundation13AssetLifetimeO9ephemeralyA2CmFWC"
+ "_$s18PodcastsFoundation14ArtworkContentOMn"
+ "_$s18PodcastsFoundation14PlaybackIntentV15ValidationErrorO13externalMediayAE0B03URLVcAEmFWC"
+ "_$s18PodcastsFoundation14PlaybackIntentV15ValidationErrorOs0F0AAMc"
+ "_$s18PodcastsFoundation14PlaybackIntentV6OptionOSHAAMc"
+ "_$s18PodcastsFoundation14PlaybackIntentV6OptionOSQAAMc"
+ "_$s18PodcastsFoundation14PlaybackIntentVSeAAMc"
+ "_$s18PodcastsFoundation14UniquePipelineVyxGAA19AssetProcessingStepAAMc"
+ "_$s18PodcastsFoundation15AssetSourceStepVyxq_GAA0c10ProcessingE0AAMc"
+ "_$s18PodcastsFoundation15MediaIdentifierO10mediaQueryyACSays6UInt64VG_AFSgtcACmFWC"
+ "_$s18PodcastsFoundation15MediaIdentifierO12localPodcastyACSS_tcACmFWC"
+ "_$s18PodcastsFoundation15MediaIdentifierO13localEpisodesyACSaySSG_tcACmFWC"
+ "_$s18PodcastsFoundation15MediaIdentifierO27universalEpisodeIdentifiersyACSayAA09UniversalfD0VG_tcACmFWC"
+ "_$s18PodcastsFoundation15MediaIdentifierO7libraryyA2CmFWC"
+ "_$s18PodcastsFoundation15MediaIdentifierO7podcastyAcA6AdamIDV_tcACmFWC"
+ "_$s18PodcastsFoundation15MediaIdentifierO7stationyACSS_SSSgtcACmFWC"
+ "_$s18PodcastsFoundation15MediaIdentifierO8episodesyACSayAA6AdamIDVG_tcACmFWC"
+ "_$s18PodcastsFoundation15MediaIdentifierO8snapshotyACSayAA0aC7LibraryC0C12ItemSnapshotVGcACmFWC"
+ "_$s18PodcastsFoundation16EpisodePlayStateOAA0cE0AAMc"
+ "_$s18PodcastsFoundation17ArtworkTextColorsVSeAAMc"
+ "_$s18PodcastsFoundation17SubscriptionOfferC7AppTypeO4newsyA2EmFWC"
+ "_$s18PodcastsFoundation17SubscriptionOfferC7AppTypeO5musicyA2EmFWC"
+ "_$s18PodcastsFoundation18InMemoryAssetCacheCyxq_GAA0eF0AAMc"
+ "_$s18PodcastsFoundation18URLTaskAssetSourceVyxGAA0dE0AAMc"
+ "_$s18PodcastsFoundation19DownloadConsistencyC5IssueO12unownedAssetyAE0B04UUIDV_AG3URLVtcAEmFWC"
+ "_$s18PodcastsFoundation19EpisodeListSettingsVSQAAMc"
+ "_$s18PodcastsFoundation20DatabaseEntityChangeVMn"
+ "_$s18PodcastsFoundation20MediaSpaceCalculatorC0cD12DistributionVSEAAMc"
+ "_$s18PodcastsFoundation20MediaSpaceCalculatorC0cD12DistributionVSeAAMc"
+ "_$s18PodcastsFoundation20MediaSpaceCalculatorCSciAAMc"
+ "_$s18PodcastsFoundation22AssetBackgroundSessionVyxGAA0C18URLSessionProtocolAAMc"
+ "_$s18PodcastsFoundation22SubscriptionControllerCMn"
+ "_$s18PodcastsFoundation23ForegroundSessionSourceVyxGAA05AssetE0AAMc"
+ "_$s18PodcastsFoundation24EpisodeTimelineAlignmentV0E0VMn"
+ "_$s18PodcastsFoundation24RepublishingValueSubjectCMn"
+ "_$s18PodcastsFoundation25DatabasePropertyPublisherVMn"
+ "_$s18PodcastsFoundation30SubscribeOnAssetProcessingStepVyxGAA0efG0AAMc"
+ "_$s18PodcastsFoundation37PodcastPlaybackPositionDataAttributesCSeAAMc"
+ "_$s18PodcastsFoundation9PriceTypeO4plusyA2CmFWC"
+ "_$s18PodcastsFoundation9PriceTypeO4psubyA2CmFWC"
+ "_$s18PodcastsFoundation9PriceTypeO4stdqyA2CmFWC"
+ "_$sSo14NSUserDefaultsC18PodcastsFoundationE4NameO6sharedyA2EmFWC"
+ "_$sSo14NSUserDefaultsC18PodcastsFoundationE4NameO8settingsyA2EmFWC"
+ "_$sSo14NSUserDefaultsC18PodcastsFoundationE4NameO8standardyA2EmFWC"
+ "_$sSo14NSUserDefaultsC18PodcastsFoundationE4NameOSHACMc"
+ "_$sSo14NSUserDefaultsC18PodcastsFoundationE4NameOSQACMc"
+ "leToFetchAllItemsyA2EmFWC"
+ "tEpisodeAttributesC9MediaKindOSQAAMc"
+ "tchEpisodeStateyA2EmFWC"
+ "tion24PodcastEpisodeAttributesC9MediaKindO5videoyA2EmFWC"

```
