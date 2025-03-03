## VisualLocalization

> `/System/Library/PrivateFrameworks/VisualLocalization.framework/VisualLocalization`

```diff

-54.33.11.14.1
-  __TEXT.__text: 0x9c0c8
-  __TEXT.__auth_stubs: 0x1140
-  __TEXT.__objc_methlist: 0x7fc
-  __TEXT.__cstring: 0x7615
-  __TEXT.__oslogstring: 0x1281
-  __TEXT.__const: 0x2da0
-  __TEXT.__gcc_except_tab: 0xb20
+54.34.9.12.8
+  __TEXT.__text: 0xacd34
+  __TEXT.__auth_stubs: 0x1d80
+  __TEXT.__objc_methlist: 0x1474
   __TEXT.__dlopen_cstrs: 0xe1
-  __TEXT.__unwind_info: 0x910
-  __TEXT.__objc_classname: 0x16d
-  __TEXT.__objc_methname: 0x286b
-  __TEXT.__objc_methtype: 0x3d7e
-  __TEXT.__objc_stubs: 0x2100
-  __DATA_CONST.__got: 0x208
-  __DATA_CONST.__const: 0x620
-  __DATA_CONST.__objc_classlist: 0x48
+  __TEXT.__cstring: 0x7773
+  __TEXT.__const: 0x3db0
+  __TEXT.__constg_swiftt: 0x51c
+  __TEXT.__swift5_typeref: 0x5b4
+  __TEXT.__swift5_fieldmd: 0x5a0
+  __TEXT.__swift5_types: 0x94
+  __TEXT.__oslogstring: 0x15fb
+  __TEXT.__swift5_capture: 0xd8
+  __TEXT.__swift5_reflstr: 0x303
+  __TEXT.__swift5_assocty: 0x48
+  __TEXT.__swift5_builtin: 0x64
+  __TEXT.__swift5_proto: 0xc0
+  __TEXT.__swift_as_entry: 0x18
+  __TEXT.__swift_as_ret: 0x14
+  __TEXT.__swift5_protos: 0x8
+  __TEXT.__gcc_except_tab: 0xb1c
+  __TEXT.__unwind_info: 0xd38
+  __TEXT.__eh_frame: 0x6f0
+  __TEXT.__objc_classname: 0x178
+  __TEXT.__objc_methname: 0x5fa1
+  __TEXT.__objc_methtype: 0x4532
+  __TEXT.__objc_stubs: 0x2160
+  __DATA_CONST.__got: 0x358
+  __DATA_CONST.__const: 0x6d8
+  __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9e0
+  __DATA_CONST.__objc_selrefs: 0x1228
+  __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x8b8
-  __AUTH_CONST.__auth_ptr: 0x90
-  __AUTH_CONST.__const: 0x280
+  __AUTH_CONST.__auth_got: 0xed8
+  __AUTH_CONST.__auth_ptr: 0x2f0
+  __AUTH_CONST.__const: 0x1430
   __AUTH_CONST.__cfstring: 0x1060
-  __AUTH_CONST.__objc_const: 0x19e0
+  __AUTH_CONST.__objc_const: 0x2c80
   __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH.__data: 0x128
   __DATA.__objc_ivar: 0x128
-  __DATA.__data: 0x2d4
-  __DATA.__common: 0x190
+  __DATA.__data: 0x5c4
+  __DATA.__bss: 0x1240
+  __DATA.__common: 0x1a8
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0xe8

   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/Metal.framework/Metal
+  - /System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/Espresso.framework/Espresso
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
+  - /System/Library/PrivateFrameworks/PhoneNumbers.framework/PhoneNumbers
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 680
-  Symbols:   1096
-  CStrings:  1893
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 1097
+  Symbols:   1227
+  CStrings:  2597
 
Symbols:
+ _CFPhoneNumberCreate
+ _CFPhoneNumberCreateString
+ _GEOBearingFromCoordinateToCoordinate
+ _GEOMapRectContainsRect
+ _GEOMapRectMakeWithRadialDistance
+ _OBJC_CLASS_$_GEOCountryConfiguration
+ _OBJC_CLASS_$_GEOLocation
+ _OBJC_CLASS_$_GEOMapItemIdentifier
+ _OBJC_CLASS_$_GEOMapService
+ _OBJC_CLASS_$_GEOPOICategoryFilter
+ _OBJC_CLASS_$_GEOSpatialPlaceLookupParameters
+ _OBJC_CLASS_$_GEOVisualIntelligenceCameraConfiguration
+ _OBJC_CLASS_$_NLTokenizer
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __Block_copy
+ __Block_release
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _malloc_size
+ _objc_allocWithZone
+ _objc_opt_self
+ _objc_retainAutoreleasedReturnValue
+ _swift_allocBox
+ _swift_allocError
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_checkMetadataState
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocObject
+ _swift_defaultActor_deallocate
+ _swift_defaultActor_destroy
+ _swift_defaultActor_initialize
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getAssociatedConformanceWitness
+ _swift_getAssociatedTypeWitness
+ _swift_getForeignTypeMetadata
+ _swift_getGenericMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_initStackObject
+ _swift_isClassType
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_lookUpClassMethod
+ _swift_once
+ _swift_release
+ _swift_release_n
+ _swift_retain
+ _swift_retain_n
+ _swift_setDeallocating
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_isCurrentExecutor
+ _swift_task_reportUnexpectedExecutor
+ _swift_task_switch
+ _swift_unexpectedError
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRelease_n
+ _swift_unknownObjectRetain
+ _swift_unknownObjectRetain_n
+ _swift_willThrow
- ___exp10
- _cosh
CStrings:
+ "  \"%s\" / \"%s\" → %s"
+ "  - %s produced score %f"
+ "\"\r\n\\"
+ "$defaultActor"
+ "@\"<GEOAnnotatedItemList>\"16@0:8"
+ "@\"<GEOEncyclopedicInfo>\"16@0:8"
+ "@\"<GEOMapItem>\"16@0:8"
+ "@\"<GEOMapItem>\"20@0:8B16"
+ "@\"<GEOMapItemTransitInfo>\"16@0:8"
+ "@\"<GEOMapItemVenueInfo>\"16@0:8"
+ "@\"<GEOTransitAttribution>\"16@0:8"
+ "@\"<GEOTransitVehiclePosition>\"16@0:8"
+ "@\"GEOAddress\"16@0:8"
+ "@\"GEOAddressObject\"16@0:8"
+ "@\"GEOAppleRating\"16@0:8"
+ "@\"GEOAssociatedApp\"16@0:8"
+ "@\"GEOBusinessAssets\"16@0:8"
+ "@\"GEOEVCharger\"16@0:8"
+ "@\"GEOEnclosingPlace\"16@0:8"
+ "@\"GEOEnhancedPlacement\"16@0:8"
+ "@\"GEOEnrichmentData\"16@0:8"
+ "@\"GEOEnrichmentInfo\"16@0:8"
+ "@\"GEOExploreGuides\"16@0:8"
+ "@\"GEOFeatureStyleAttributes\"16@0:8"
+ "@\"GEOHikeSummary\"16@0:8"
+ "@\"GEOInlineRapEnablement\"16@0:8"
+ "@\"GEOLabelGeometry\"16@0:8"
+ "@\"GEOLocalizedString\"16@0:8"
+ "@\"GEOMapItemAdditionalPlaceInfo\"16@0:8"
+ "@\"GEOMapItemClientAttributes\"16@0:8"
+ "@\"GEOMapItemContainedPlace\"16@0:8"
+ "@\"GEOMapItemDetourInfo\"16@0:8"
+ "@\"GEOMapItemIdentifier\"16@0:8"
+ "@\"GEOMapItemPhotosAttribution\"16@0:8"
+ "@\"GEOMapItemPlaceAttribution\"16@0:8"
+ "@\"GEOMapItemReviewsAttribution\"16@0:8"
+ "@\"GEOMapRegion\"16@0:8"
+ "@\"GEOMapRegion\"20@0:8i16"
+ "@\"GEOMessageLink\"16@0:8"
+ "@\"GEOMiniBrowseCategories\"16@0:8"
+ "@\"GEOMuninViewState\"16@0:8"
+ "@\"GEOPDFlyover\"16@0:8"
+ "@\"GEOPDHikeAssociatedInfo\"16@0:8"
+ "@\"GEOPDHikeGeometry\"16@0:8"
+ "@\"GEOPDPlace\"16@0:8"
+ "@\"GEOPDURLData\"16@0:8"
+ "@\"GEOPOIClaim\"16@0:8"
+ "@\"GEOPlace\"16@0:8"
+ "@\"GEOPlaceQuestionnaire\"16@0:8"
+ "@\"GEOPlaceResult\"16@0:8"
+ "@\"GEOPlacecardLayoutData\"16@0:8"
+ "@\"GEOPriceDescription\"16@0:8"
+ "@\"GEORelatedPlaceList\"20@0:8i16"
+ "@\"GEORestaurantFeaturesLink\"16@0:8"
+ "@\"GEOStorefrontInfo\"16@0:8"
+ "@\"GEOStorefrontPresentationInfo\"16@0:8"
+ "@\"GEOStyleAttributes\"16@0:8"
+ "@\"GEOTooltip\"16@0:8"
+ "@\"GEOTrailHead\"16@0:8"
+ "@\"GEOViewportFrame\"16@0:8"
+ "@\"NSArray\"16@0:8"
+ "@\"NSArray\"20@0:8I16"
+ "@\"NSData\"16@0:8"
+ "@\"NSDate\"16@0:8"
+ "@\"NSDictionary\"16@0:8"
+ "@\"NSNumber\"16@0:8"
+ "@\"NSSet\"16@0:8"
+ "@\"NSString\"24@0:8@\"NSString\"16"
+ "@\"NSTimeZone\"16@0:8"
+ "@\"NSURL\"16@0:8"
+ "@\"NSURL\"36@0:8{CGSize=dd}16B32"
+ "@20@0:8B16"
+ "@20@0:8I16"
+ "@20@0:8i16"
+ "@36@0:8{CGSize=dd}16B32"
+ "Assertion failed: self != ((void*)0)"
+ "Assertion failed: stats != ((void*)0)"
+ "B20@0:8I16"
+ "B24@0:8@\"<GEOMapItem>\"16"
+ "B24@?0{_NSRange=QQ}8"
+ "Brand '%s' / %s → %f"
+ "Canceling existing request"
+ "Canceling in-flight request"
+ "Clearing cached candidate results"
+ "Duplicate values for key: '"
+ "Exceeded max candidate limit. Reducing valid radius for cached response"
+ "Existing cached results are still valid for new location: %s with radius %f meters"
+ "Failed to parse URL: %s"
+ "Fatal error"
+ "Found address match: %s"
+ "Found exact phone number match: %s"
+ "Found exact webURL match: %s"
+ "Found host-only webURL match: %s -> %s"
+ "GEOMapItem"
+ "Generating matches for %s with radius %f meters"
+ "I16@0:8"
+ "In-flight request will be valid for new location"
+ "Issuing new request for nearby map items"
+ "LCS is sufficiently-long. Clamping score to at least %f"
+ "RAPFlowType"
+ "Results for this location have not yet been fetched"
+ "Scoring \"%s\" with recipe \"%s\""
+ "Swift/Dictionary.swift"
+ "Swift/NativeDictionary.swift"
+ "T@\"<GEOAnnotatedItemList>\",R,N,G_annotatedItemList"
+ "T@\"<GEOEncyclopedicInfo>\",R,N,G_encyclopedicInfo"
+ "T@\"<GEOMapItemTransitInfo>\",R,N,G_transitInfo"
+ "T@\"<GEOMapItemVenueInfo>\",R,N,G_venueInfo"
+ "T@\"<GEOTransitAttribution>\",R,N,G_transitAttribution"
+ "T@\"<GEOTransitVehiclePosition>\",R,N,G_transitVehiclePosition"
+ "T@\"GEOAddress\",R,N"
+ "T@\"GEOAppleRating\",R,N,G_overallAppleRating"
+ "T@\"GEOAssociatedApp\",R,N,G_associatedApp"
+ "T@\"GEOBusinessAssets\",R,N"
+ "T@\"GEOEVCharger\",R,N,G_evCharger"
+ "T@\"GEOEnclosingPlace\",R,N,G_enclosingPlace"
+ "T@\"GEOEnhancedPlacement\",R,N,G_enhancedPlacement"
+ "T@\"GEOEnrichmentData\",R,N,G_enrichmentData"
+ "T@\"GEOEnrichmentInfo\",R,N,G_enrichmentInfo"
+ "T@\"GEOExploreGuides\",R,N,G_exploreGuides"
+ "T@\"GEOFeatureStyleAttributes\",R,N,G_styleAttributes"
+ "T@\"GEOHikeSummary\",R,N,G_hikeSummary"
+ "T@\"GEOInlineRapEnablement\",R,N,G_inlineRapEnablement"
+ "T@\"GEOLabelGeometry\",R,N,G_labelGeometry"
+ "T@\"GEOLocalizedString\",R,N"
+ "T@\"GEOMapItemClientAttributes\",R,N,G_clientAttributes"
+ "T@\"GEOMapItemContainedPlace\",R,N,G_containedPlace"
+ "T@\"GEOMapItemDetourInfo\",R,N"
+ "T@\"GEOMapItemIdentifier\",R,N"
+ "T@\"GEOMapItemIdentifier\",R,N,G_identifier"
+ "T@\"GEOMapItemPhotosAttribution\",R,N,G_photosAttribution"
+ "T@\"GEOMapItemPlaceAttribution\",R,N,G_attribution"
+ "T@\"GEOMapItemReviewsAttribution\",R,N,G_reviewsAttribution"
+ "T@\"GEOMapRegion\",R,N"
+ "T@\"GEOMessageLink\",R,N,G_messageLink"
+ "T@\"GEOMiniBrowseCategories\",R,N,G_miniBrowseCategories"
+ "T@\"GEOMuninViewState\",R,N,G_muninViewState"
+ "T@\"GEOPDFlyover\",R,N,G_flyover"
+ "T@\"GEOPDHikeAssociatedInfo\",R,N,G_hikeAssociatedInfo"
+ "T@\"GEOPDHikeGeometry\",R,N,G_hikeGeometry"
+ "T@\"GEOPDPlace\",R,N,G_placeData"
+ "T@\"GEOPDURLData\",R,N"
+ "T@\"GEOPOIClaim\",R,N,G_poiClaim"
+ "T@\"GEOPlace\",R,N,G_place"
+ "T@\"GEOPlaceQuestionnaire\",R,N,G_placeQuestionnaire"
+ "T@\"GEOPlaceResult\",R,N,G_placeResult"
+ "T@\"GEOPlacecardLayoutData\",R,N,G_placecardLayoutData"
+ "T@\"GEOPriceDescription\",R,N,G_priceDescription"
+ "T@\"GEORestaurantFeaturesLink\",R,N,G_featureLink"
+ "T@\"GEOStorefrontInfo\",R,N,G_storefrontInfo"
+ "T@\"GEOStorefrontPresentationInfo\",R,N,G_storefrontPresentationInfo"
+ "T@\"GEOStyleAttributes\",R,N,G_walletCategoryStyling"
+ "T@\"GEOStyleAttributes\",R,N,G_walletPlaceStyling"
+ "T@\"GEOTooltip\",R,N,G_tooltip"
+ "T@\"GEOTrailHead\",R,N,G_trailHead"
+ "T@\"GEOViewportFrame\",R,N,G_viewportFrame"
+ "T@\"NSArray\",R,N"
+ "T@\"NSArray\",R,N,G_accolades"
+ "T@\"NSArray\",R,N,G_additionalPlaceInfos"
+ "T@\"NSArray\",R,N,G_allPhotoAttributions"
+ "T@\"NSArray\",R,N,G_alternateMapsCategoryIDs"
+ "T@\"NSArray\",R,N,G_alternateMapsCategoryMUIDs"
+ "T@\"NSArray\",R,N,G_alternateSearchableNames"
+ "T@\"NSArray\",R,N,G_amenities"
+ "T@\"NSArray\",R,N,G_appleRatings"
+ "T@\"NSArray\",R,N,G_browseCategories"
+ "T@\"NSArray\",R,N,G_businessHours"
+ "T@\"NSArray\",R,N,G_captionedPhotoAlbums"
+ "T@\"NSArray\",R,N,G_childItems"
+ "T@\"NSArray\",R,N,G_externalActionLinks"
+ "T@\"NSArray\",R,N,G_identifierHistory"
+ "T@\"NSArray\",R,N,G_linkedServices"
+ "T@\"NSArray\",R,N,G_photos"
+ "T@\"NSArray\",R,N,G_placeCollectionPullQuotes"
+ "T@\"NSArray\",R,N,G_placeCollections"
+ "T@\"NSArray\",R,N,G_placeCollectionsIds"
+ "T@\"NSArray\",R,N,G_quickLinks"
+ "T@\"NSArray\",R,N,G_relatedPlaceLists"
+ "T@\"NSArray\",R,N,G_reviews"
+ "T@\"NSArray\",R,N,G_roadAccessPoints"
+ "T@\"NSArray\",R,N,G_searchResultPhotoCarousel"
+ "T@\"NSArray\",R,N,G_secondaryQuickLinks"
+ "T@\"NSArray\",R,N,G_tips"
+ "T@\"NSData\",R,N"
+ "T@\"NSData\",R,N,G_placeDataAsData"
+ "T@\"NSDate\",R,N"
+ "T@\"NSDictionary\",R,N"
+ "T@\"NSNumber\",R,N,G_mapsCategoryMUID"
+ "T@\"NSSet\",R,N,G_alternateIdentifiers"
+ "T@\"NSString\",R,C,N,G_vendorID"
+ "T@\"NSString\",R,N"
+ "T@\"NSString\",R,N,G_bestAvailableCountryCode"
+ "T@\"NSString\",R,N,G_businessURL"
+ "T@\"NSString\",R,N,G_disambiguationName"
+ "T@\"NSString\",R,N,G_flyoverAnnouncementMessage"
+ "T@\"NSString\",R,N,G_iso3166CountryCode"
+ "T@\"NSString\",R,N,G_iso3166SubdivisionCode"
+ "T@\"NSString\",R,N,G_mapsCategoryId"
+ "T@\"NSString\",R,N,G_placeDescription"
+ "T@\"NSString\",R,N,G_poiCategory"
+ "T@\"NSString\",R,N,G_poiPinpointURLString"
+ "T@\"NSString\",R,N,G_poiSurveyURLString"
+ "T@\"NSString\",R,N,G_resultSnippetLocationString"
+ "T@\"NSString\",R,N,G_telephone"
+ "T@\"NSString\",R,N,G_walletCategoryIdentifier"
+ "T@\"NSString\",R,N,G_walletCategoryLocalizedString"
+ "T@\"NSString\",R,N,G_walletCategoryLocalizedStringLocale"
+ "T@\"NSString\",R,N,G_walletMapsCategoryIdentifier"
+ "T@\"NSString\",R,N,G_walletPlaceLocalizedString"
+ "T@\"NSString\",R,N,G_walletPlaceLocalizedStringLocale"
+ "T@\"NSTimeZone\",R,N"
+ "T@\"NSURL\",R,C,N,G_providerURL"
+ "T@\"NSURL\",R,C,N,G_webURL"
+ "TB,R,N"
+ "TB,R,N,G_canDownloadMorePhotos"
+ "TB,R,N,G_enableRAPLightweightFeedback"
+ "TB,R,N,G_hasAnyAccolades"
+ "TB,R,N,G_hasAnyAmenities"
+ "TB,R,N,G_hasAppleRatings"
+ "TB,R,N,G_hasAreaHighlightId"
+ "TB,R,N,G_hasAreaInMeters"
+ "TB,R,N,G_hasBrandMUID"
+ "TB,R,N,G_hasBusinessHours"
+ "TB,R,N,G_hasCaptionedPhotoAlbum"
+ "TB,R,N,G_hasCurrentOperatingHours"
+ "TB,R,N,G_hasEVCharger"
+ "TB,R,N,G_hasEnclosingPlace"
+ "TB,R,N,G_hasEncyclopedicInfo"
+ "TB,R,N,G_hasFeatureLink"
+ "TB,R,N,G_hasFlyover"
+ "TB,R,N,G_hasGroundViewLocationId"
+ "TB,R,N,G_hasLinkedServices"
+ "TB,R,N,G_hasMUID"
+ "TB,R,N,G_hasOperatingHours"
+ "TB,R,N,G_hasPOIClaim"
+ "TB,R,N,G_hasPlaceCollectionPullQuotes"
+ "TB,R,N,G_hasPlaceDescription"
+ "TB,R,N,G_hasPlaceQuestionnaire"
+ "TB,R,N,G_hasPriceRange"
+ "TB,R,N,G_hasResolvablePartialInformation"
+ "TB,R,N,G_hasResultProviderID"
+ "TB,R,N,G_hasTelephone"
+ "TB,R,N,G_hasTransit"
+ "TB,R,N,G_hasUserRatingScore"
+ "TB,R,N,G_hasVenueFeatureType"
+ "TB,R,N,G_hasWifiFingerprintConfidence"
+ "TB,R,N,G_hasWifiFingerprintLabelStatusCode"
+ "TB,R,N,G_hasWifiFingerprintLabelType"
+ "TB,R,N,G_isInLinkedPlaceRelationship"
+ "TB,R,N,G_isPartiallyClientized"
+ "TB,R,N,G_isStandaloneBrand"
+ "TB,R,N,G_isTransitDisplayFeature"
+ "TB,R,N,G_needsAttribution"
+ "TB,R,N,G_optsOutOfTelephoneAds"
+ "TB,R,N,G_responseStatusIsIncomplete"
+ "TB,R,N,G_showSuggestAnEditButton"
+ "TB,R,N,GisDisputed"
+ "TB,R,N,GisValid"
+ "TI,R,N,G_maxScoreForPriceRange"
+ "TI,R,N,G_priceRange"
+ "TI,R,N,G_resultSnippetDistanceDisplayThreshold"
+ "TI,R,N,G_sampleSizeForUserRatingScore"
+ "TI,R,N,G_wifiFingerprintConfidence"
+ "TQ,R,N,G_areaHighlightId"
+ "TQ,R,N,G_brandMUID"
+ "TQ,R,N,G_customIconID"
+ "TQ,R,N,G_groundViewLocationId"
+ "TQ,R,N,G_muid"
+ "TQ,R,N,G_openingHoursOptions"
+ "TQ,R,N,G_totalPhotoCount"
+ "Td,R,N,G_areaInMeters"
+ "Tf,R,N"
+ "Tf,R,N,G_normalizedUserRatingScore"
+ "Tf,R,N,G_photosMemoryScore"
+ "Ti,R,N"
+ "Ti,R,N,G_RAPFlowType"
+ "Ti,R,N,G_addressGeocodeAccuracy"
+ "Ti,R,N,G_hikeGeometryElevationModel"
+ "Ti,R,N,G_parsecSectionType"
+ "Ti,R,N,G_placeCategoryType"
+ "Ti,R,N,G_placeDisplayStyle"
+ "Ti,R,N,G_placeDisplayType"
+ "Ti,R,N,G_placeType"
+ "Ti,R,N,G_resultProviderID"
+ "Ti,R,N,G_venueFeatureType"
+ "Ti,R,N,G_wifiFingerprintLabelStatusCode"
+ "Ti,R,N,G_wifiFingerprintLabelType"
+ "Tq,R,N"
+ "T{?=dd},R,N"
+ "VisualLocalization/VLPointOfInterestMatcher.swift"
+ "_RAPFlowType"
+ "_TtC18VisualLocalization24VLPointOfInterestMatcher"
+ "_accolades"
+ "_additionalPlaceInfos"
+ "_addressGeocodeAccuracy"
+ "_allPhotoAttributions"
+ "_alternateIdentifiers"
+ "_alternateMapsCategoryIDs"
+ "_alternateMapsCategoryMUIDs"
+ "_alternateSearchableNames"
+ "_amenities"
+ "_annotatedItemList"
+ "_appleRatings"
+ "_areaHighlightId"
+ "_areaInMeters"
+ "_arrivalMapRegionForTransportType:"
+ "_asPlaceInfo"
+ "_associatedApp"
+ "_attribution"
+ "_bestAvailableCountryCode"
+ "_bestAvatarBrandIconURLForSize:allowSmaller:"
+ "_bestHeroBrandIconURLForSize:allowSmaller:"
+ "_bestNavbarBrandIconURLForSize:allowSmaller:"
+ "_brandMUID"
+ "_browseCategories"
+ "_businessHours"
+ "_businessURL"
+ "_canDownloadMorePhotos"
+ "_captionedPhotoAlbums"
+ "_childItems"
+ "_clientAttributes"
+ "_containedPlace"
+ "_customIconID"
+ "_disambiguationName"
+ "_enableRAPLightweightFeedback"
+ "_enclosingPlace"
+ "_encyclopedicInfo"
+ "_enhancedPlacement"
+ "_enrichmentData"
+ "_enrichmentInfo"
+ "_evCharger"
+ "_exploreGuides"
+ "_externalActionLinks"
+ "_featureLink"
+ "_firstRelatedPlaceListForType:"
+ "_flyover"
+ "_flyoverAnnouncementMessage"
+ "_groundViewLocationId"
+ "_hasAnyAccolades"
+ "_hasAnyAmenities"
+ "_hasAppleRatings"
+ "_hasAreaHighlightId"
+ "_hasAreaInMeters"
+ "_hasBrandMUID"
+ "_hasBusinessHours"
+ "_hasCaptionedPhotoAlbum"
+ "_hasCurrentOperatingHours"
+ "_hasEVCharger"
+ "_hasEnclosingPlace"
+ "_hasEncyclopedicInfo"
+ "_hasFeatureLink"
+ "_hasFlyover"
+ "_hasGroundViewLocationId"
+ "_hasLinkedServices"
+ "_hasLocalizedCategoryNamesForType:"
+ "_hasMUID"
+ "_hasOperatingHours"
+ "_hasPOIClaim"
+ "_hasPlaceCollectionPullQuotes"
+ "_hasPlaceDescription"
+ "_hasPlaceQuestionnaire"
+ "_hasPriceRange"
+ "_hasResolvablePartialInformation"
+ "_hasResultProviderID"
+ "_hasTelephone"
+ "_hasTransit"
+ "_hasUserRatingScore"
+ "_hasVenueFeatureType"
+ "_hasWifiFingerprintConfidence"
+ "_hasWifiFingerprintLabelStatusCode"
+ "_hasWifiFingerprintLabelType"
+ "_hikeAssociatedInfo"
+ "_hikeGeometry"
+ "_hikeGeometryElevationModel"
+ "_hikeSummary"
+ "_identifierHistory"
+ "_inlineRapEnablement"
+ "_isInLinkedPlaceRelationship"
+ "_isPartiallyClientized"
+ "_isStandaloneBrand"
+ "_isTransitDisplayFeature"
+ "_iso3166CountryCode"
+ "_iso3166SubdivisionCode"
+ "_labelGeometry"
+ "_linkedServices"
+ "_localizedCategoryNamesForType:"
+ "_mapItemBySettingIsTransitDisplayFeature:"
+ "_mapItemByStrippingOptionalData"
+ "_mapsCategoryId"
+ "_mapsCategoryMUID"
+ "_maxScoreForPriceRange"
+ "_messageLink"
+ "_miniBrowseCategories"
+ "_muid"
+ "_muninViewState"
+ "_needsAttribution"
+ "_normalizedUserRatingScore"
+ "_openingHoursOptions"
+ "_optsOutOfTelephoneAds"
+ "_overallAppleRating"
+ "_parsecSectionType"
+ "_photos"
+ "_photosAttribution"
+ "_photosMemoryScore"
+ "_place"
+ "_placeCategoryType"
+ "_placeCollectionPullQuotes"
+ "_placeCollections"
+ "_placeCollectionsIds"
+ "_placeData"
+ "_placeDataAsData"
+ "_placeDescription"
+ "_placeDisplayStyle"
+ "_placeDisplayType"
+ "_placeQuestionnaire"
+ "_placeResult"
+ "_placeType"
+ "_placecardLayoutData"
+ "_poiCategory"
+ "_poiClaim"
+ "_poiPinpointURLString"
+ "_poiSurveyURLString"
+ "_priceDescription"
+ "_priceRange"
+ "_providerURL"
+ "_quickLinks"
+ "_relatedPlaceListForComponentIdentifier:"
+ "_relatedPlaceLists"
+ "_responseStatusIsIncomplete"
+ "_resultProviderID"
+ "_resultSnippetDistanceDisplayThreshold"
+ "_resultSnippetLocationString"
+ "_reviews"
+ "_reviewsAttribution"
+ "_roadAccessPoints"
+ "_sampleSizeForUserRatingScore"
+ "_searchResultPhotoCarousel"
+ "_secondaryQuickLinks"
+ "_showSuggestAnEditButton"
+ "_spokenAddressForLocale:"
+ "_storefrontInfo"
+ "_storefrontPresentationInfo"
+ "_styleAttributes"
+ "_telephone"
+ "_tips"
+ "_tooltip"
+ "_totalPhotoCount"
+ "_trailHead"
+ "_transitAttribution"
+ "_transitInfo"
+ "_transitVehiclePosition"
+ "_vendorID"
+ "_venueFeatureType"
+ "_venueInfo"
+ "_viewportFrame"
+ "_walletCategoryIdentifier"
+ "_walletCategoryLocalizedString"
+ "_walletCategoryLocalizedStringLocale"
+ "_walletCategoryStyling"
+ "_walletMapsCategoryIdentifier"
+ "_walletPlaceLocalizedString"
+ "_walletPlaceLocalizedStringLocale"
+ "_walletPlaceStyling"
+ "_webURL"
+ "_wifiFingerprintConfidence"
+ "_wifiFingerprintLabelStatusCode"
+ "_wifiFingerprintLabelType"
+ "accolades"
+ "additionalPlaceInfos"
+ "address"
+ "addressDictionary"
+ "addressGeocodeAccuracy"
+ "addressObject"
+ "allPhotoAttributions"
+ "alternateIdentifiers"
+ "alternateMapsCategoryIDs"
+ "alternateMapsCategoryMUIDs"
+ "alternateSearchableNames"
+ "amenities"
+ "annotatedItemList"
+ "appleRatings"
+ "areaHighlightId"
+ "areaInMeters"
+ "areasOfInterest"
+ "associatedApp"
+ "attribution"
+ "bestAvailableCountryCode"
+ "brandMUID"
+ "browseCategories"
+ "businessAssets"
+ "businessHours"
+ "businessURL"
+ "cachedResponse"
+ "cachingRadiusMeters"
+ "canDownloadMorePhotos"
+ "captionedPhotoAlbums"
+ "centerCoordinate"
+ "childItems"
+ "clientAttributes"
+ "contactAddressType"
+ "contactIsMe"
+ "contactName"
+ "contactSpokenName"
+ "containedPlace"
+ "countryCode"
+ "currentCountrySupportsFeature:"
+ "customIconID"
+ "detourInfo"
+ "disambiguationName"
+ "disclaimerText"
+ "displayMapRegion"
+ "displayMapRegionOrNil"
+ "displayMaxZoom"
+ "displayMinZoom"
+ "disputed"
+ "enableRAPLightweightFeedback"
+ "enclosingPlace"
+ "encodedData"
+ "encyclopedicInfo"
+ "enhancedPlacement"
+ "enrichmentData"
+ "enrichmentInfo"
+ "enumerateTokensInRange:usingBlock:"
+ "evCharger"
+ "eventDate"
+ "eventName"
+ "exploreGuides"
+ "externalActionLinks"
+ "externalTransitStationCode"
+ "featureLink"
+ "flyover"
+ "flyoverAnnouncementMessage"
+ "geoAddress"
+ "geoFenceMapRegion"
+ "geoFenceMapRegionOrNil"
+ "groundViewLocationId"
+ "hasAnyAccolades"
+ "hasAnyAmenities"
+ "hasAppleRatings"
+ "hasAreaHighlightId"
+ "hasAreaInMeters"
+ "hasBrandMUID"
+ "hasBusinessHours"
+ "hasCaptionedPhotoAlbum"
+ "hasCurrentOperatingHours"
+ "hasDisplayMaxZoom"
+ "hasDisplayMinZoom"
+ "hasEVCharger"
+ "hasEnclosingPlace"
+ "hasEncyclopedicInfo"
+ "hasExpiredComponents"
+ "hasFeatureLink"
+ "hasFlyover"
+ "hasGroundViewLocationId"
+ "hasLinkedServices"
+ "hasMUID"
+ "hasOperatingHours"
+ "hasPOIClaim"
+ "hasPlaceCollectionPullQuotes"
+ "hasPlaceDescription"
+ "hasPlaceQuestionnaire"
+ "hasPriceRange"
+ "hasResolvablePartialInformation"
+ "hasResultProviderID"
+ "hasTelephone"
+ "hasTransit"
+ "hasUserRatingScore"
+ "hasVenueCapacity"
+ "hasVenueFeatureType"
+ "hasWifiFingerprintConfidence"
+ "hasWifiFingerprintLabelStatusCode"
+ "hasWifiFingerprintLabelType"
+ "hikeAssociatedInfo"
+ "hikeGeometry"
+ "hikeGeometryElevationModel"
+ "hikeSummary"
+ "identifierHistory"
+ "inFlightRequest"
+ "inLinkedPlaceRelationship"
+ "initWithCategoriesToInclude:categoriesToExclude:"
+ "initWithCoordinate:radius:poiCategoryFilter:maxResultCount:source:"
+ "initWithUnit:"
+ "inlineRapEnablement"
+ "isDisputed"
+ "isEqualToMapItem:"
+ "isEventAllDay"
+ "isPartiallyClientized"
+ "isStandAloneBrand"
+ "isTransitDisplayFeature"
+ "isValid"
+ "iso3166CountryCode"
+ "iso3166SubdivisionCode"
+ "iterateGroundViewsWithBlock:"
+ "labelCoordinate"
+ "labelGeometry"
+ "linkedServices"
+ "mapDisplayType"
+ "mapItemsForSpatialLookupParameters:"
+ "mapsCategoryId"
+ "mapsCategoryMUID"
+ "matchingPolicyForMapItem:"
+ "maxResultCount"
+ "maxScoreForPriceRange"
+ "messageLink"
+ "miniBrowseCategories"
+ "muid"
+ "muninViewState"
+ "needsAttribution"
+ "normalizedUserRatingScore"
+ "offlineDownloadRegion"
+ "openingHoursOptions"
+ "optsOutOfTelephoneAds"
+ "overallRating"
+ "parsecSectionType"
+ "photoCarousel"
+ "photos"
+ "photosAttribution"
+ "photosMemoryScore"
+ "place"
+ "placeCategoryType"
+ "placeCollectionPullQuotes"
+ "placeCollections"
+ "placeCollectionsIds"
+ "placeData"
+ "placeDataAsData"
+ "placeDescription"
+ "placeDisplayStyle"
+ "placeDisplayType"
+ "placeQuestionnaire"
+ "placeResult"
+ "placeType"
+ "placecardLayoutData"
+ "poiCategory"
+ "poiClaim"
+ "poiPinpointURLString"
+ "poiSurveyURLString"
+ "poiType"
+ "priceDescription"
+ "priceRange"
+ "providerURL"
+ "q16@0:8"
+ "quickLinks"
+ "referenceFrame"
+ "relatedPlaceLists"
+ "responseStatusIncomplete"
+ "resultProviderID"
+ "resultSnippetDistanceDisplayThreshold"
+ "resultSnippetLocationString"
+ "reviews"
+ "reviewsAttribution"
+ "roadAccessPoints"
+ "sampleSizeForUserRatingScore"
+ "secondaryName"
+ "secondaryQuickLinks"
+ "secondarySpokenName"
+ "setString:"
+ "sharedConfiguration"
+ "sharedService"
+ "shortAddress"
+ "showSuggestAnEditButton"
+ "spatialMappedCategories"
+ "spatialMappedPlaceCategories"
+ "spokenNameForLocale:"
+ "storefrontInfo"
+ "storefrontPresentationInfo"
+ "structuredAddress"
+ "styleAttributes"
+ "subThoroughfare"
+ "submitWithHandler:queue:"
+ "supportedTransitPaymentMethods"
+ "supportsOfflineMaps"
+ "telephone"
+ "ticketForSpatialPlaceLookupParameters:traits:"
+ "timezone"
+ "tips"
+ "tooltip"
+ "totalPhotoCount"
+ "trailHead"
+ "traits"
+ "transitAttribution"
+ "transitInfo"
+ "transitPaymentMethodSuggestions"
+ "transitStationIdentifier"
+ "transitVehiclePosition"
+ "unsupportedPOICategories"
+ "update(location:)"
+ "urlData"
+ "v24@0:8@?<v@?dd@\"NSString\"@\"NSString\"@\"NSString\">16"
+ "v24@?0@\"GEOSpatialPlaceLookupResult\"8@\"NSError\"16"
+ "v40@?0{_NSRange=QQ}8Q24^B32"
+ "valid"
+ "vendorID"
+ "venueCapacity"
+ "venueFeatureType"
+ "venueInfo"
+ "viewportFrame"
+ "walletCategoryIdentifier"
+ "walletCategoryLocalizedString"
+ "walletCategoryLocalizedStringLocale"
+ "walletCategoryStyling"
+ "walletMapsCategoryIdentifier"
+ "walletPlaceLocalizedString"
+ "walletPlaceLocalizedStringLocale"
+ "walletPlaceStyling"
+ "weatherDisplayName"
+ "webURL"
+ "wifiFingerprintConfidence"
+ "wifiFingerprintLabelStatusCode"
+ "wifiFingerprintLabelType"
+ "→ Final score: %f"
- "/t/"
- "0 && \"Not a spline based camera model.\""
- "Assertion failed: self != ((void *)0)"
- "Assertion failed: stats != ((void *)0)"
- "Invalid VL status: %d"
- "Unsupported map status: %d"
- "g_proj_bspline_cnt"

```
