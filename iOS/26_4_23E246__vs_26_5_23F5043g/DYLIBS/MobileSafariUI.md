## MobileSafariUI

> `/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI`

```diff

-624.1.16.10.6
-  __TEXT.__text: 0x27c4e4
-  __TEXT.__auth_stubs: 0x3f60
-  __TEXT.__objc_methlist: 0x230ac
-  __TEXT.__const: 0x23e8
-  __TEXT.__gcc_except_tab: 0x1d338
-  __TEXT.__cstring: 0xed00
+624.2.1.10.1
+  __TEXT.__text: 0x27df60
+  __TEXT.__auth_stubs: 0x3f80
+  __TEXT.__objc_methlist: 0x2311c
+  __TEXT.__const: 0x2418
+  __TEXT.__gcc_except_tab: 0x1d59c
+  __TEXT.__cstring: 0xed40
   __TEXT.__dlopen_cstrs: 0x83a
-  __TEXT.__oslogstring: 0x9af8
+  __TEXT.__oslogstring: 0x9e28
   __TEXT.__ustring: 0x113a
   __TEXT.__swift5_typeref: 0x23ca
   __TEXT.__constg_swiftt: 0xfb8

   __TEXT.__swift_as_entry: 0x6c
   __TEXT.__swift_as_ret: 0x88
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0xe330
+  __TEXT.__unwind_info: 0xe378
   __TEXT.__eh_frame: 0x1768
   __TEXT.__objc_classname: 0x496d
-  __TEXT.__objc_methname: 0x6fd00
+  __TEXT.__objc_methname: 0x6ff40
   __TEXT.__objc_methtype: 0x15ac7
-  __TEXT.__objc_stubs: 0x491a0
-  __DATA_CONST.__got: 0x2f08
-  __DATA_CONST.__const: 0x8c08
+  __TEXT.__objc_stubs: 0x49320
+  __DATA_CONST.__got: 0x2f18
+  __DATA_CONST.__const: 0x8c58
   __DATA_CONST.__objc_classlist: 0x980
   __DATA_CONST.__objc_catlist: 0xb0
   __DATA_CONST.__objc_protolist: 0xb00
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16e98
+  __DATA_CONST.__objc_selrefs: 0x16f08
   __DATA_CONST.__objc_protorefs: 0x178
   __DATA_CONST.__objc_superrefs: 0x6a0
   __DATA_CONST.__objc_arraydata: 0x370
-  __AUTH_CONST.__auth_got: 0x1fc8
-  __AUTH_CONST.__const: 0x6388
-  __AUTH_CONST.__cfstring: 0xd120
-  __AUTH_CONST.__objc_const: 0x31160
+  __AUTH_CONST.__auth_got: 0x1fd8
+  __AUTH_CONST.__const: 0x63a8
+  __AUTH_CONST.__cfstring: 0xd160
+  __AUTH_CONST.__objc_const: 0x311c0
   __AUTH_CONST.__objc_intobj: 0x498
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x2a0
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH.__objc_data: 0x29c8
   __AUTH.__data: 0x538
-  __DATA.__objc_ivar: 0x2100
+  __DATA.__objc_ivar: 0x2108
   __DATA.__data: 0x8530
   __DATA.__bss: 0x1cf0
   __DATA.__common: 0x41

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 211BCBEF-5219-3F37-B0A8-27629AEBF4B6
-  Functions: 13937
-  Symbols:   45079
-  CStrings:  22336
+  UUID: 5A9C5407-4FC4-31FC-8D94-4E87A9F837A6
+  Functions: 13951
+  Symbols:   45134
+  CStrings:  22367
 
Symbols:
+ -[CompletionList _requestSearchSuggestionImages]
+ -[CompletionList _searchSuggestionsRequiringImage]
+ -[CompletionListTableViewCell .cxx_destruct]
+ -[CompletionListTableViewCell _updateIconForCurrentAppearance]
+ -[CompletionListTableViewCell completionIconSystemImageName]
+ -[CompletionListTableViewCell initWithStyle:reuseIdentifier:]
+ -[CompletionListTableViewCell prepareForReuse]
+ -[CompletionListTableViewCell setCompletionIconSystemImageName:]
+ -[SearchSuggestionTableViewCell _applyCornerRadiusIfNecessary]
+ -[TabDocument webView:didFailProvisionalNavigation:withError:].cold.1
+ GCC_except_table1166
+ GCC_except_table965
+ _OBJC_CLASS_$_WBSCompletionIconProvider
+ _OBJC_CLASS_$_WBSRichSearchSuggestionImageProvider
+ _OBJC_IVAR_$_CompletionList._urlStringsForInProgressSearchSuggestionImageLoads
+ _OBJC_IVAR_$_CompletionListTableViewCell._completionIconSystemImageName
+ _WBSOSLogNavigation
+ _WBSOSLogWebKit2Callbacks
+ __OBJC_$_INSTANCE_VARIABLES_CompletionListTableViewCell
+ __OBJC_$_PROP_LIST_CompletionListTableViewCell
+ ___40-[Application _historyItemsWereRemoved:]_block_invoke.378
+ ___48-[CompletionList _requestSearchSuggestionImages]_block_invoke
+ ___50-[CompletionList _searchSuggestionsRequiringImage]_block_invoke
+ ___55-[Application pdfDataForTabWithUUID:completionHandler:]_block_invoke.421
+ ___55-[Application pdfDataForTabWithUUID:completionHandler:]_block_invoke.421.cold.1
+ ___56-[Application prewarmAndRemoveOrphanedProfileDataStores]_block_invoke.273
+ ___56-[Application prewarmAndRemoveOrphanedProfileDataStores]_block_invoke.273.cold.1
+ ___63-[TabDocument sfScribbleControllerDidUpdateHiddenElementCount:]_block_invoke
+ ___68-[Application _updateCloudFeatureAvailabilityWithCompletionHandler:]_block_invoke.370
+ ___68-[Application _updateCloudFeatureAvailabilityWithCompletionHandler:]_block_invoke_2.372
+ ___68-[Application _updateCloudFeatureAvailabilityWithCompletionHandler:]_block_invoke_2.372.cold.1
+ ___97-[CatalogViewController dismissCompletionDetailWindowAndResumeEditingIfNeeded:completionHandler:]_block_invoke.130
+ ___block_descriptor_32_e26_B16?0"SearchSuggestion"8l
+ ___block_descriptor_56_e8_32s40s48w_e17_v16?0"UIImage"8lw48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40r48w_e33_v16?0"WBSSiteMetadataResponse"8lw48l8s32l8r40l8
+ ___block_literal_global.1131
+ ___block_literal_global.1137
+ ___block_literal_global.1139
+ ___block_literal_global.1141
+ ___block_literal_global.1143
+ ___block_literal_global.1145
+ ___block_literal_global.167
+ ___block_literal_global.179
+ ___block_literal_global.185
+ ___block_literal_global.368
+ ___block_literal_global.381
+ ___block_literal_global.385
+ ___block_literal_global.388
+ ___block_literal_global.393
+ ___block_literal_global.401
+ ___block_literal_global.408
+ ___block_literal_global.411
+ ___block_literal_global.415
+ ___block_literal_global.419
+ ___block_literal_global.426
+ ___block_literal_global.428
+ ___block_literal_global.441
+ ___block_literal_global.444
+ ___block_literal_global.448
+ _completionListFaviconSizeLarge
+ _objc_msgSend$_applyCornerRadiusIfNecessary
+ _objc_msgSend$_requestSearchSuggestionImages
+ _objc_msgSend$_searchSuggestionsRequiringImage
+ _objc_msgSend$cachedImageForURLString:
+ _objc_msgSend$clearSearchSuggestionImageCacheNow
+ _objc_msgSend$fetchImageForURLString:completionHandler:
+ _objc_msgSend$iconForSystemImageName:isDarkMode:
+ _objc_msgSend$imageURLString
+ _objc_msgSend$isGraphicIconsInCompletionListEnabled
+ _objc_msgSend$isSearchSuggestionImagesEnabled
+ _objc_msgSend$populateCompletionListIcons
+ _objc_msgSend$setCompletionIconSystemImageName:
- GCC_except_table966
- ___40-[Application _historyItemsWereRemoved:]_block_invoke.377
- ___55-[Application pdfDataForTabWithUUID:completionHandler:]_block_invoke.420
- ___55-[Application pdfDataForTabWithUUID:completionHandler:]_block_invoke.420.cold.1
- ___56-[Application prewarmAndRemoveOrphanedProfileDataStores]_block_invoke.272
- ___56-[Application prewarmAndRemoveOrphanedProfileDataStores]_block_invoke.272.cold.1
- ___68-[Application _updateCloudFeatureAvailabilityWithCompletionHandler:]_block_invoke.369
- ___68-[Application _updateCloudFeatureAvailabilityWithCompletionHandler:]_block_invoke_2.371
- ___68-[Application _updateCloudFeatureAvailabilityWithCompletionHandler:]_block_invoke_2.371.cold.1
- ___97-[CatalogViewController dismissCompletionDetailWindowAndResumeEditingIfNeeded:completionHandler:]_block_invoke.129
- ___block_descriptor_56_e8_32s40r48w_e33_v16?0"WBSSiteMetadataResponse"8lw48l8s32l8r40l8
- ___block_literal_global.1130
- ___block_literal_global.1136
- ___block_literal_global.1138
- ___block_literal_global.1140
- ___block_literal_global.1142
- ___block_literal_global.1144
- ___block_literal_global.166
- ___block_literal_global.174
- ___block_literal_global.303
- ___block_literal_global.329
- ___block_literal_global.338
- ___block_literal_global.361
- ___block_literal_global.363
- ___block_literal_global.367
- ___block_literal_global.380
- ___block_literal_global.384
- ___block_literal_global.387
- ___block_literal_global.392
- ___block_literal_global.407
- ___block_literal_global.410
- ___block_literal_global.414
- ___block_literal_global.418
- ___block_literal_global.425
- ___block_literal_global.427
- ___block_literal_global.440
- ___block_literal_global.443
- ___block_literal_global.447
CStrings:
+ "Rich Suggestion With Image"
+ "Rich Suggestion With Image and Subtitle"
+ "T@\"NSString\",&,N,V_completionIconSystemImageName"
+ "Unified field is becoming first responder; allows reflected Top Hits: YES"
+ "Unified field is resigning first responder; allows reflected Top Hits: YES"
+ "Web view (pid: %d) asked us to decide policy for navigation action"
+ "Web view (pid: %d) did commit navigation for <%{sensitive}@>"
+ "Web view (pid: %d) did decide policy for navigation response for MIME type \"%{private}@\" and url <%{sensitive}@> on page <%{sensitive}@>, isForMainFrame <%{public}@>"
+ "Web view (pid: %d) did fail navigation for <%{sensitive}@> with error %{public}@"
+ "Web view (pid: %d) did fail provisional navigation (%{public}@)"
+ "Web view (pid: %d) did finish navigation for <%{sensitive}@>"
+ "Web view (pid: %d) did receive authentication challenge for <%{sensitive}@>"
+ "Web view (pid: %d) did receive server redirect for provisional navigation for <%{sensitive}@>"
+ "Web view (pid: %d) did start provisional navigation for <%{sensitive}@>"
+ "Web view (pid: %d) is loading a web search"
+ "_applyCornerRadiusIfNecessary"
+ "_completionIconSystemImageName"
+ "_requestSearchSuggestionImages"
+ "_searchSuggestionsRequiringImage"
+ "_updateIconForCurrentAppearance"
+ "_urlStringsForInProgressSearchSuggestionImageLoads"
+ "cachedImageForURLString:"
+ "clearSearchSuggestionImageCacheNow"
+ "completionIconSystemImageName"
+ "fetchImageForURLString:completionHandler:"
+ "iconForSystemImageName:isDarkMode:"
+ "imageURLString"
+ "isGraphicIconsInCompletionListEnabled"
+ "isSearchSuggestionImagesEnabled"
+ "populateCompletionListIcons"
+ "setCompletionIconSystemImageName:"
- "Becoming first responder; allows reflected Top Hits: YES"
- "Resigning first responder; allows reflected Top Hits: YES"

```
