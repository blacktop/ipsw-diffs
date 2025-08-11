## ScreenTimeCore

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore`

```diff

-601.0.0.0.0
-  __TEXT.__text: 0xb61d0
-  __TEXT.__auth_stubs: 0x1570
-  __TEXT.__objc_methlist: 0x8858
-  __TEXT.__const: 0x1df0
-  __TEXT.__cstring: 0xa318
-  __TEXT.__oslogstring: 0x9bac
+604.2.0.0.0
+  __TEXT.__text: 0xbea10
+  __TEXT.__auth_stubs: 0x1660
+  __TEXT.__objc_methlist: 0x8ba0
+  __TEXT.__const: 0x2028
+  __TEXT.__cstring: 0xa748
+  __TEXT.__oslogstring: 0xa19f
   __TEXT.__gcc_except_tab: 0x1d00
-  __TEXT.__constg_swiftt: 0x844
-  __TEXT.__swift5_typeref: 0xa52
+  __TEXT.__constg_swiftt: 0x8b4
+  __TEXT.__swift5_typeref: 0xba4
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0x50f
-  __TEXT.__swift5_fieldmd: 0x6e8
+  __TEXT.__swift5_reflstr: 0x556
+  __TEXT.__swift5_fieldmd: 0x720
   __TEXT.__swift5_assocty: 0xf0
-  __TEXT.__swift5_proto: 0x1a0
-  __TEXT.__swift5_types: 0x94
-  __TEXT.__swift5_capture: 0x160
-  __TEXT.__swift_as_entry: 0x14
-  __TEXT.__swift_as_ret: 0x18
+  __TEXT.__swift5_proto: 0x1ac
+  __TEXT.__swift5_types: 0x9c
+  __TEXT.__swift5_capture: 0x33c
+  __TEXT.__swift_as_entry: 0x54
+  __TEXT.__swift_as_ret: 0x64
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x2bb8
-  __TEXT.__eh_frame: 0xcf8
-  __TEXT.__objc_classname: 0x1835
-  __TEXT.__objc_methname: 0x164f3
-  __TEXT.__objc_methtype: 0x23ff
-  __TEXT.__objc_stubs: 0xd580
-  __DATA_CONST.__got: 0xb50
-  __DATA_CONST.__const: 0x1a50
-  __DATA_CONST.__objc_classlist: 0x5e0
+  __TEXT.__unwind_info: 0x2ea8
+  __TEXT.__eh_frame: 0x1628
+  __TEXT.__objc_classname: 0x18c6
+  __TEXT.__objc_methname: 0x16dab
+  __TEXT.__objc_methtype: 0x251c
+  __TEXT.__objc_stubs: 0xd920
+  __DATA_CONST.__got: 0xb90
+  __DATA_CONST.__const: 0x1af0
+  __DATA_CONST.__objc_classlist: 0x608
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x1d0
+  __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4978
-  __DATA_CONST.__objc_protorefs: 0x108
-  __DATA_CONST.__objc_superrefs: 0x458
+  __DATA_CONST.__objc_selrefs: 0x4b40
+  __DATA_CONST.__objc_protorefs: 0x118
+  __DATA_CONST.__objc_superrefs: 0x470
   __DATA_CONST.__objc_arraydata: 0x250
-  __AUTH_CONST.__auth_got: 0xac8
-  __AUTH_CONST.__const: 0x1770
-  __AUTH_CONST.__cfstring: 0x8940
-  __AUTH_CONST.__objc_const: 0x10070
-  __AUTH_CONST.__objc_intobj: 0x138
+  __AUTH_CONST.__auth_got: 0xb40
+  __AUTH_CONST.__const: 0x1d60
+  __AUTH_CONST.__cfstring: 0x8cc0
+  __AUTH_CONST.__objc_const: 0x10588
+  __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0x2f68
-  __AUTH.__data: 0x260
-  __DATA.__objc_ivar: 0x600
-  __DATA.__data: 0x1aa8
-  __DATA.__bss: 0x33b0
+  __AUTH.__objc_data: 0x30c8
+  __AUTH.__data: 0x340
+  __DATA.__objc_ivar: 0x620
+  __DATA.__data: 0x1bf8
+  __DATA.__bss: 0x3550
   __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x13c8
   __DATA_DIRTY.__data: 0x48

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0F2723D8-91A3-3533-8280-7942AEF185D0
-  Functions: 4419
-  Symbols:   11703
-  CStrings:  6849
+  UUID: 7A29442C-216F-3369-A8BE-2B093CED2DF5
+  Functions: 4626
+  Symbols:   12008
+  CStrings:  7021
 
Symbols:
+ +[STAppRatingChangedUserNotificationContext new]
+ +[STAppRatingChangedUserNotificationContext supportsSecureCoding]
+ +[STLog regionRating]
+ +[STRegionRatings loadRegionRatingsWithOptions:completionHandler:]
+ +[STRegionRatings loadRegionRatingsWithOptions:storefrontClient:managementState:completionHandler:]
+ +[STRegionRatings sharedRatings]
+ +[STRegionRatings sharedRatings].cold.1
+ -[STAppRatingChangedUserNotificationContext .cxx_destruct]
+ -[STAppRatingChangedUserNotificationContext bundleIdentifiers]
+ -[STAppRatingChangedUserNotificationContext customizeNotificationContent:withCompletionBlock:]
+ -[STAppRatingChangedUserNotificationContext encodeWithCoder:]
+ -[STAppRatingChangedUserNotificationContext initWithCoder:]
+ -[STAppRatingChangedUserNotificationContext initWithIdentifier:]
+ -[STAppRatingChangedUserNotificationContext initWithRatingLimit:bundleIdentifiers:]
+ -[STAppRatingChangedUserNotificationContext init]
+ -[STAppRatingChangedUserNotificationContext notificationBundleIdentifier]
+ -[STAppRatingChangedUserNotificationContext regionRatingLimit]
+ -[STRegionRatings .cxx_destruct]
+ -[STRegionRatings _loadRegionRatingsDataForStorefront:includeUnrated:managementState:completionHandler:]
+ -[STRegionRatings _loadRegionRatingsDataWithOptions:managementState:completionHandler:]
+ -[STRegionRatings _localizedLabelForRegion:rating:]
+ -[STRegionRatings _localizedRatingsForRegion:type:includeAllContentKey:]
+ -[STRegionRatings _overrideValueForString:]
+ -[STRegionRatings getClosestRestrictionMatch:within:forPayloadKey:]
+ -[STRegionRatings getRatingSystemTypeFrom:]
+ -[STRegionRatings getRatingSystemTypeFrom:].cold.1
+ -[STRegionRatings initWithStorefrontClient:]
+ -[STRegionRatings localizedAppRatingsForRegion:]
+ -[STRegionRatings localizedMovieRatingsForRegion:]
+ -[STRegionRatings localizedStringForAppRatingLabel:]
+ -[STRegionRatings localizedTVRatingsForRegion:]
+ -[STRegionRatings preferredRegion]
+ -[STRegionRatings preferredRegion].cold.1
+ -[STRegionRatings ratingValuesByRatingSystemType]
+ -[STRegionRatings regionRatingsData]
+ -[STRegionRatings setRegionRatingsData:]
+ -[STRegionRatings setStorefront:]
+ -[STRegionRatings setStorefrontClient:]
+ -[STRegionRatings storefrontClient]
+ -[STRegionRatings storefront]
+ -[STRegionRatingsRequestOptions .cxx_destruct]
+ -[STRegionRatingsRequestOptions initWithUnrated:userDSID:]
+ -[STRegionRatingsRequestOptions initWithUnrated:userDSID:localDeviceLocale:]
+ -[STRegionRatingsRequestOptions localDeviceLocale]
+ -[STRegionRatingsRequestOptions setLocalDeviceLocale:]
+ -[STRegionRatingsRequestOptions setUnrated:]
+ -[STRegionRatingsRequestOptions setUserDSID:]
+ -[STRegionRatingsRequestOptions unrated]
+ -[STRegionRatingsRequestOptions userDSID]
+ _AMSAccountMediaTypeProduction
+ _OBJC_CLASS_$_AMSChildAccountStorefrontTask
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_CLASS_$_STAppRatingChangedUserNotificationContext
+ _OBJC_CLASS_$_STRegionRatings
+ _OBJC_CLASS_$_STRegionRatingsRequestOptions
+ _OBJC_CLASS_$_STStorefrontClient
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_STAppRatingChangedUserNotificationContext._bundleIdentifiers
+ _OBJC_IVAR_$_STAppRatingChangedUserNotificationContext._regionRatingLimit
+ _OBJC_IVAR_$_STRegionRatings._regionRatingsData
+ _OBJC_IVAR_$_STRegionRatings._storefront
+ _OBJC_IVAR_$_STRegionRatings._storefrontClient
+ _OBJC_IVAR_$_STRegionRatingsRequestOptions._localDeviceLocale
+ _OBJC_IVAR_$_STRegionRatingsRequestOptions._unrated
+ _OBJC_IVAR_$_STRegionRatingsRequestOptions._userDSID
+ _OBJC_METACLASS_$_STAppRatingChangedUserNotificationContext
+ _OBJC_METACLASS_$_STRegionRatings
+ _OBJC_METACLASS_$_STRegionRatingsRequestOptions
+ _OBJC_METACLASS_$_STStorefrontClient
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ _STRegionRatingsDontAllowValue
+ _STRegionRatingsLeastRestrictiveValue
+ __DATA_STStorefrontClient
+ __DATA__TtC14ScreenTimeCore21STAMSStorefrontClient
+ __INSTANCE_METHODS_STStorefrontClient
+ __INSTANCE_METHODS__TtC14ScreenTimeCore21STAMSStorefrontClient
+ __IVARS_STStorefrontClient
+ __METACLASS_DATA_STStorefrontClient
+ __METACLASS_DATA__TtC14ScreenTimeCore21STAMSStorefrontClient
+ __OBJC_$_CLASS_METHODS_STAppRatingChangedUserNotificationContext
+ __OBJC_$_CLASS_METHODS_STRegionRatings
+ __OBJC_$_CLASS_PROP_LIST_STRegionRatings
+ __OBJC_$_INSTANCE_METHODS_STAppRatingChangedUserNotificationContext
+ __OBJC_$_INSTANCE_METHODS_STRegionRatings
+ __OBJC_$_INSTANCE_METHODS_STRegionRatingsRequestOptions
+ __OBJC_$_INSTANCE_VARIABLES_STAppRatingChangedUserNotificationContext
+ __OBJC_$_INSTANCE_VARIABLES_STRegionRatings
+ __OBJC_$_INSTANCE_VARIABLES_STRegionRatingsRequestOptions
+ __OBJC_$_PROP_LIST_STAppRatingChangedUserNotificationContext
+ __OBJC_$_PROP_LIST_STRegionRatings
+ __OBJC_$_PROP_LIST_STRegionRatingsRequestOptions
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_STAMSStorefrontClientProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_STStorefrontClientProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_STAMSStorefrontClientProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_STStorefrontClientProtocol
+ __OBJC_$_PROTOCOL_REFS_STStorefrontClientProtocol
+ __OBJC_CLASS_RO_$_STAppRatingChangedUserNotificationContext
+ __OBJC_CLASS_RO_$_STRegionRatings
+ __OBJC_CLASS_RO_$_STRegionRatingsRequestOptions
+ __OBJC_LABEL_PROTOCOL_$_STAMSStorefrontClientProtocol
+ __OBJC_LABEL_PROTOCOL_$_STStorefrontClientProtocol
+ __OBJC_METACLASS_RO_$_STAppRatingChangedUserNotificationContext
+ __OBJC_METACLASS_RO_$_STRegionRatings
+ __OBJC_METACLASS_RO_$_STRegionRatingsRequestOptions
+ __OBJC_PROTOCOL_$_STAMSStorefrontClientProtocol
+ __OBJC_PROTOCOL_$_STStorefrontClientProtocol
+ __PROTOCOLS_STStorefrontClient
+ __PROTOCOLS_STStorefrontClient.3
+ __PROTOCOLS__TtC14ScreenTimeCore21STAMSStorefrontClient
+ __PROTOCOLS__TtC14ScreenTimeCore21STAMSStorefrontClient.2
+ ___104-[STRegionRatings _loadRegionRatingsDataForStorefront:includeUnrated:managementState:completionHandler:]_block_invoke
+ ___104-[STRegionRatings _loadRegionRatingsDataForStorefront:includeUnrated:managementState:completionHandler:]_block_invoke_2
+ ___104-[STRegionRatings _loadRegionRatingsDataForStorefront:includeUnrated:managementState:completionHandler:]_block_invoke_2.cold.1
+ ___32+[STRegionRatings sharedRatings]_block_invoke
+ ___43-[STRegionRatings getRatingSystemTypeFrom:]_block_invoke
+ ___67-[STRegionRatings getClosestRestrictionMatch:within:forPayloadKey:]_block_invoke
+ ___67-[STRegionRatings getClosestRestrictionMatch:within:forPayloadKey:]_block_invoke_2
+ ___87-[STRegionRatings _loadRegionRatingsDataWithOptions:managementState:completionHandler:]_block_invoke
+ ___87-[STRegionRatings _loadRegionRatingsDataWithOptions:managementState:completionHandler:]_block_invoke.cold.1
+ ___87-[STRegionRatings _loadRegionRatingsDataWithOptions:managementState:completionHandler:]_block_invoke_2
+ ___94-[STAppRatingChangedUserNotificationContext customizeNotificationContent:withCompletionBlock:]_block_invoke
+ ___99+[STRegionRatings loadRegionRatingsWithOptions:storefrontClient:managementState:completionHandler:]_block_invoke
+ ___assert_rtn
+ ___block_descriptor_32_e11_q24?0816l
+ ___block_descriptor_40_e25_B32?0"NSNumber"8Q16^B24l
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_literal_global.61
+ ___block_literal_global.89
+ ___swift_project_boxed_opaque_existential_0
+ _associated conformance 14ScreenTimeCore23STStorefrontClientErrorOSHAASQ
+ _block_copy_helper.30
+ _block_copy_helper.46
+ _block_copy_helper.49
+ _block_copy_helper.68
+ _block_copy_helper.71
+ _block_copy_helper.75
+ _block_copy_helper.78
+ _block_descriptor.32
+ _block_descriptor.48
+ _block_descriptor.51
+ _block_descriptor.70
+ _block_descriptor.73
+ _block_descriptor.77
+ _block_descriptor.80
+ _block_destroy_helper.31
+ _block_destroy_helper.47
+ _block_destroy_helper.50
+ _block_destroy_helper.69
+ _block_destroy_helper.72
+ _block_destroy_helper.76
+ _block_destroy_helper.79
+ _getRatingSystemTypeFrom:.onceToken
+ _getRatingSystemTypeFrom:.typeValues
+ _objc_msgSend$_loadRegionRatingsDataForStorefront:includeUnrated:managementState:completionHandler:
+ _objc_msgSend$_loadRegionRatingsDataWithOptions:managementState:completionHandler:
+ _objc_msgSend$_localizedLabelForRegion:rating:
+ _objc_msgSend$_localizedRatingsForRegion:type:includeAllContentKey:
+ _objc_msgSend$_overrideValueForString:
+ _objc_msgSend$bytes
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$fetchStorefrontWithOptions:completionHandler:
+ _objc_msgSend$firstMatchInString:options:range:
+ _objc_msgSend$initWithStorefrontClient:
+ _objc_msgSend$initWithUnrated:userDSID:localDeviceLocale:
+ _objc_msgSend$loadRegionRatingsWithOptions:storefrontClient:managementState:completionHandler:
+ _objc_msgSend$localizedStringWithValidatedFormat:validFormatSpecifiers:error:
+ _objc_msgSend$mutableBytes
+ _objc_msgSend$preferredRegion
+ _objc_msgSend$range
+ _objc_msgSend$ratingValuesByRatingSystemType
+ _objc_msgSend$regionRating
+ _objc_msgSend$regionRatingLimit
+ _objc_msgSend$regionRatingsData
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$setLocalDeviceLocale:
+ _objc_msgSend$setRegionRatingsData:
+ _objc_msgSend$setStorefront:
+ _objc_msgSend$setUnrated:
+ _objc_msgSend$setUserDSID:
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$storefrontClient
+ _objc_msgSend$unrated
+ _objectdestroy.10Tm
+ _objectdestroy.16Tm
+ _objectdestroy.54Tm
+ _objectdestroy.7Tm
+ _sharedRatings.onceToken
+ _sharedRatings.sharedRatings
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _swift_deletedAsyncMethodErrorTu
+ _symbolic IeAgH_
+ _symbolic IeghH_
+ _symbolic SccySS______pG s5ErrorP
+ _symbolic SccySo8NSStringC______pG s5ErrorP
+ _symbolic SccySo9ACAccountC______pG s5ErrorP
+ _symbolic So18STStorefrontClientC
+ _symbolic So29STRegionRatingsRequestOptionsC
+ _symbolic So8NSStringCSgSo7NSErrorCSgIeyBhyy_Sg
+ _symbolic So8NSStringCSgSo7NSErrorCSgIeyByy_
+ _symbolic So8NSStringCSgSo7NSErrorCSgIeyByy_Sg
+ _symbolic So9ACAccountC
+ _symbolic So9ACAccountCSgSo7NSErrorCSgIeyBhyy_Sg
+ _symbolic _____ 14ScreenTimeCore21STAMSStorefrontClientC
+ _symbolic _____ 14ScreenTimeCore23STStorefrontClientErrorO
+ _symbolic _____Sg 10Foundation6LocaleV6RegionV
+ _sysctlbyname
CStrings:
+ "%@&path=CONTENT_PRIVACY/CONTENT_RESTRICTIONS/APP_RATING"
+ "%ld"
+ "(\\d+)"
+ "+[STAppRatingChangedUserNotificationContext new]"
+ "-[STAppRatingChangedUserNotificationContext initWithIdentifier:]"
+ "-[STAppRatingChangedUserNotificationContext init]"
+ "@\"<STStorefrontClientProtocol>\""
+ "AllowAll"
+ "AppRatingChangedNotificationBodyIpad"
+ "AppRatingChangedNotificationBodyIphone"
+ "AppRatingChangedNotificationTitleFormat"
+ "B32@?0@\"NSNumber\"8Q16^B24"
+ "DontAllow"
+ "No matching restriction value was found, so conservatively returning Don't Allow"
+ "RatingProviders"
+ "STAMSStorefrontClientProtocol"
+ "STAppRatingChangedUserNotificationContext"
+ "STAppRatingChangedUserNotificationContext.m"
+ "STRegionRatings"
+ "STRegionRatings found no country code for device locale; falling back to 'us'"
+ "STRegionRatings loadRegionRatingsDataWithCompletionHandler received error: %@"
+ "STRegionRatings loadRegionRatingsDataWithCompletionHandler received ratings data: %@"
+ "STRegionRatingsRequestOptions"
+ "STStorefrontClient"
+ "STStorefrontClient failed to fetch storefront from AMS: %{public}@; falling back to storefront from locale %{public}s"
+ "STStorefrontClient fetching active iTunes account..."
+ "STStorefrontClient fetching storefront for local user from AMS bag..."
+ "STStorefrontClient fetching storefront for remote child with DSID %{public}@, parent account %@..."
+ "STStorefrontClient found active iTunes account matching DSID %{public}@"
+ "STStorefrontClient found local non-iCloud user"
+ "STStorefrontClient found local signed-in iTunes account with DSID %{public}@ different from user DSID %{public}@; assuming user is remote child"
+ "STStorefrontClient got options with iCloud user DSID %{public}@, but active iTunes account has nil DSID"
+ "STStorefrontClient got storefront: %{public}s from device locale"
+ "STStorefrontClient successfully fetched active iTunes account: %@"
+ "STStorefrontClient successfully fetched storefront: %{public}s for local user from AMS bag"
+ "STStorefrontClient successfully fetched storefront: %{public}s for remote child with DSID %{public}@"
+ "STStorefrontClientProtocol"
+ "T@\"<STStorefrontClientProtocol>\",&,N,V_storefrontClient"
+ "T@\"NSArray\",R,V_bundleIdentifiers"
+ "T@\"NSDictionary\",&,N,V_regionRatingsData"
+ "T@\"NSLocale\",&,N,V_localDeviceLocale"
+ "T@\"NSNumber\",&,N,V_userDSID"
+ "T@\"NSString\",C,N,V_storefront"
+ "T@\"NSString\",R,V_regionRatingLimit"
+ "T@\"STRegionRatings\",R"
+ "TB,N,V_unrated"
+ "When loading region ratings, failed to fetch storefront: %{public}@"
+ "_TtC14ScreenTimeCore21STAMSStorefrontClient"
+ "_bundleIdentifiers"
+ "_loadRegionRatingsDataForStorefront:includeUnrated:managementState:completionHandler:"
+ "_loadRegionRatingsDataWithOptions:managementState:completionHandler:"
+ "_localDeviceLocale"
+ "_localizedLabelForRegion:rating:"
+ "_localizedRatingsForRegion:type:includeAllContentKey:"
+ "_overrideValueForString:"
+ "_regionRatingLimit"
+ "_regionRatingsData"
+ "_storefront"
+ "_storefrontClient"
+ "_unrated"
+ "activeiTunesAccountWithCompletionHandler:"
+ "amsStorefrontClient"
+ "ams_DSID"
+ "ams_activeiTunesAccountForMediaType:"
+ "app-bundles"
+ "app-rating-changed"
+ "bagCountryCodeWithCompletionHandler:"
+ "bundleIdentifiers"
+ "bytes"
+ "dataWithLength:"
+ "fetchStorefrontFromAMSForChildWithDSID:parentAccount:completionHandler:"
+ "fetchStorefrontFromAMSForLocalUserWithCompletionHandler:"
+ "fetchStorefrontFromAMSWith:completionHandler:"
+ "fetchStorefrontFromLocale:error:"
+ "fetchStorefrontWithOptions:completionHandler:"
+ "firstMatchInString:options:range:"
+ "getClosestRestrictionMatch:within:forPayloadKey:"
+ "getRatingSystemTypeFrom:"
+ "hw.machine"
+ "iPad"
+ "in-apps"
+ "initWithAmsStorefrontClient:"
+ "initWithParentAccount:childDSID:bag:"
+ "initWithRatingLimit:bundleIdentifiers:"
+ "initWithStorefrontClient:"
+ "initWithUnrated:userDSID:"
+ "initWithUnrated:userDSID:localDeviceLocale:"
+ "loadRegionRatingsWithOptions:completionHandler:"
+ "loadRegionRatingsWithOptions:storefrontClient:managementState:completionHandler:"
+ "localDeviceLocale"
+ "localizedAppRatingsForRegion:"
+ "localizedMovieRatingsForRegion:"
+ "localizedStringForAppRatingLabel:"
+ "localizedStringWithValidatedFormat:validFormatSpecifiers:error:"
+ "localizedTVRatingsForRegion:"
+ "movie-bundles"
+ "movies"
+ "mutableBytes"
+ "notifyUserOfAppRatingChange:completionHandler:"
+ "preferredRegion"
+ "q24@?0@8@16"
+ "range"
+ "rank"
+ "rating"
+ "ratingApps"
+ "ratingMovies"
+ "ratingTVShows"
+ "ratingValuesByRatingSystemType"
+ "regionRating"
+ "regionRatingLimit"
+ "regionRatingsData"
+ "regularExpressionWithPattern:options:error:"
+ "resultWithCompletion:"
+ "setLocalDeviceLocale:"
+ "setRegionRatingsData:"
+ "setStorefront:"
+ "setStorefrontClient:"
+ "setUnrated:"
+ "setUserDSID:"
+ "sharedRatings"
+ "sortedArrayUsingComparator:"
+ "storefront"
+ "storefrontClient"
+ "storefrontForChildWithDSID:parentAccount:withCompletionHandler:"
+ "tv-episodes"
+ "tv-seasons"
+ "unrated"
+ "us"
+ "v24@0:8@?<v@?@\"ACAccount\"@\"NSError\">16"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"STRegionRatingsRequestOptions\"16@?<v@?@\"NSString\"@\"NSError\">24"
+ "v40@0:8@\"NSNumber\"16@\"ACAccount\"24@?<v@?@\"NSString\"@\"NSError\">32"
+ "v44@0:8@16B24@28@?36"
+ "valuePromise"
+ "xx"

```
