## PosterBoardServices

> `/System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices`

```diff

-304.3.8.100.0
-  __TEXT.__text: 0x4c664
-  __TEXT.__auth_stubs: 0xae0
-  __TEXT.__objc_methlist: 0x3c94
+304.4.11.0.0
+  __TEXT.__text: 0x4cdf8
+  __TEXT.__auth_stubs: 0xa70
+  __TEXT.__objc_methlist: 0x3d5c
   __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x4a2e
-  __TEXT.__gcc_except_tab: 0x958
+  __TEXT.__cstring: 0x4bbc
+  __TEXT.__gcc_except_tab: 0x80c
   __TEXT.__oslogstring: 0x2759
   __TEXT.__dlopen_cstrs: 0x2a6
-  __TEXT.__unwind_info: 0x10c0
+  __TEXT.__unwind_info: 0x1188
   __TEXT.__objc_classname: 0x89a
-  __TEXT.__objc_methname: 0xa970
-  __TEXT.__objc_methtype: 0x1c38
-  __TEXT.__objc_stubs: 0x6220
+  __TEXT.__objc_methname: 0xab3c
+  __TEXT.__objc_methtype: 0x1c8b
+  __TEXT.__objc_stubs: 0x63c0
   __DATA_CONST.__got: 0x480
-  __DATA_CONST.__const: 0x1230
+  __DATA_CONST.__const: 0x1280
   __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f70
+  __DATA_CONST.__objc_selrefs: 0x1fd8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1f8
-  __AUTH_CONST.__auth_got: 0x580
+  __AUTH_CONST.__auth_got: 0x548
   __AUTH_CONST.__const: 0x4c0
-  __AUTH_CONST.__cfstring: 0x37a0
-  __AUTH_CONST.__objc_const: 0xc2e8
+  __AUTH_CONST.__cfstring: 0x37e0
+  __AUTH_CONST.__objc_const: 0xc3e8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0xb40
-  __DATA.__objc_ivar: 0x430
+  __AUTH.__objc_data: 0xa50
+  __DATA.__objc_ivar: 0x438
   __DATA.__data: 0x5c0
   __DATA.__bss: 0xb0
-  __DATA_DIRTY.__objc_data: 0xa00
+  __DATA_DIRTY.__objc_data: 0xaf0
   __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 926AE020-45AE-3D50-BC64-5A95D94ACADD
-  Functions: 1744
-  Symbols:   6177
-  CStrings:  2968
+  UUID: C93F53E2-CB2A-3600-82D1-C673DAAF64C1
+  Functions: 1813
+  Symbols:   6407
+  CStrings:  2996
 
Symbols:
+ -[PRSPosterArchiver abortWithMessage:]
+ -[PRSPosterArchiver initWithPFPosterArchiver:]
+ -[PRSPosterArchiver processDisallowsAppleArchive]
+ -[PRSPosterGalleryItemOptions initWithModularComplications:modularLandscapeComplications:inlineComplication:allowsSystemSuggestedComplications:allowsSystemSuggestedComplicationsInLandscape:featuredConfidenceLevel:displayNameLocalizationKey:spokenNameLocalizationKey:descriptiveTextLocalizationKey:hero:shouldShowAsShuffleStack:photoSubtype:focus:onlyEligibleForMadeForFocusSection:isOffloaded:]
+ -[PRSPosterGalleryItemOptions isOffloaded]
+ -[PRSPosterGalleryItemOptions optionsBySettingIsOffloaded:]
+ -[PRSPosterIconConfiguration initWithPoster:type:variant:accentColor:size:]
+ -[PRSPosterIconConfiguration size]
+ -[PRSServer ensurePosterExtensionAvailable:completion:]
+ -[PRSServer fetchDownloadablePosterAppsWithCompletion:]
+ -[PRSServer installAllPosterAppsWithCompletion:]
+ -[PRSServer uninstallAllPosterAppsWithCompletion:]
+ -[PRSService ensurePosterExtensionAvailable:completion:]
+ -[PRSService ensurePosterExtensionAvailable:completion:].cold.1
+ -[PRSService ensurePosterExtensionAvailable:completion:].cold.2
+ -[PRSService fetchDownloadablePosterAppsWithCompletion:]
+ -[PRSService fetchDownloadablePosterAppsWithCompletion:].cold.1
+ -[PRSService installAllPosterAppsWithCompletion:]
+ -[PRSService installAllPosterAppsWithCompletion:].cold.1
+ -[PRSService uninstallAllPosterAppsWithCompletion:]
+ -[PRSService uninstallAllPosterAppsWithCompletion:].cold.1
+ _OBJC_IVAR_$_PRSPosterGalleryItemOptions._isOffloaded
+ _OBJC_IVAR_$_PRSPosterIconConfiguration._size
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ ___103-[PRSServer createPosterConfigurationForProviderIdentifier:posterDescriptorIdentifier:role:completion:]_block_invoke.21
+ ___39-[PRSPosterGalleryItemOptions isEqual:]_block_invoke_15
+ ___48-[PRSServer installAllPosterAppsWithCompletion:]_block_invoke
+ ___49-[PRSService installAllPosterAppsWithCompletion:]_block_invoke
+ ___49-[PRSService installAllPosterAppsWithCompletion:]_block_invoke.cold.1
+ ___50-[PRSServer uninstallAllPosterAppsWithCompletion:]_block_invoke
+ ___51-[PRSService uninstallAllPosterAppsWithCompletion:]_block_invoke
+ ___51-[PRSService uninstallAllPosterAppsWithCompletion:]_block_invoke.cold.1
+ ___55-[PRSServer fetchDownloadablePosterAppsWithCompletion:]_block_invoke
+ ___56-[PRSService ensurePosterExtensionAvailable:completion:]_block_invoke
+ ___56-[PRSService ensurePosterExtensionAvailable:completion:]_block_invoke.cold.1
+ ___56-[PRSService fetchDownloadablePosterAppsWithCompletion:]_block_invoke
+ ___56-[PRSService fetchDownloadablePosterAppsWithCompletion:]_block_invoke.cold.1
+ ___64-[PRSService _selectConfigurationAndRefreshSnapshot:completion:]_block_invoke.156
+ ___64-[PRSService _selectConfigurationAndRefreshSnapshot:completion:]_block_invoke.156.cold.1
+ ___73-[PRSServer refreshPosterDescriptorsForExtension:sessionInfo:completion:]_block_invoke.17
+ ___75-[PRSServer refreshPosterConfigurationMatchingUUID:sessionInfo:completion:]_block_invoke.26
+ ___77-[PRSService createAndSelectLegacyPosterConfigurationIfNeededWithCompletion:]_block_invoke.152
+ ___77-[PRSService createAndSelectLegacyPosterConfigurationIfNeededWithCompletion:]_block_invoke.154
+ ___block_descriptor_40_e8_32bs_e41_v32?0"NSArray"8"NSArray"16"NSError"24ls32l8
+ ___block_descriptor_56_e8_32s40bs_e69_v32?0"NSArray<__NSString__>"8"NSArray<__NSString__>"16"NSError"24ls32l8s40l8
+ ___block_literal_global.23
+ ___block_literal_global.28
+ ___block_literal_global.56
+ _objc_msgSend$abortWithMessage:
+ _objc_msgSend$ensurePosterExtensionAvailable:completion:
+ _objc_msgSend$fetchDownloadablePosterAppsWithCompletion:
+ _objc_msgSend$initWithFileManager:unarchivingContainerURL:
+ _objc_msgSend$initWithModularComplications:modularLandscapeComplications:inlineComplication:allowsSystemSuggestedComplications:allowsSystemSuggestedComplicationsInLandscape:featuredConfidenceLevel:displayNameLocalizationKey:spokenNameLocalizationKey:descriptiveTextLocalizationKey:hero:shouldShowAsShuffleStack:photoSubtype:focus:onlyEligibleForMadeForFocusSection:isOffloaded:
+ _objc_msgSend$initWithPoster:type:variant:accentColor:size:
+ _objc_msgSend$installAllPosterAppsWithCompletion:
+ _objc_msgSend$isOffloaded
+ _objc_msgSend$processDisallowsAppleArchive
+ _objc_msgSend$server:ensurePosterExtensionAvailable:completion:
+ _objc_msgSend$server:fetchDownloadablePosterAppsWithCompletion:
+ _objc_msgSend$server:installAllPosterAppsWithCompletion:
+ _objc_msgSend$server:uninstallAllPosterAppsWithCompletion:
+ _objc_msgSend$setIsOffloaded:
+ _objc_msgSend$size
+ _objc_msgSend$uninstallAllPosterAppsWithCompletion:
- -[PRSPosterArchiver initWithFileManager:processHandle:]
- -[PRSPosterArchiver initWithFileManager:processHandle:unarchivingContainerURL:]
- -[PRSPosterGalleryItemOptions initWithModularComplications:modularLandscapeComplications:inlineComplication:allowsSystemSuggestedComplications:allowsSystemSuggestedComplicationsInLandscape:featuredConfidenceLevel:displayNameLocalizationKey:spokenNameLocalizationKey:descriptiveTextLocalizationKey:hero:shouldShowAsShuffleStack:photoSubtype:focus:onlyEligibleForMadeForFocusSection:]
- -[PRSPosterIconConfiguration initWithPoster:type:variant:accentColor:]
- ___103-[PRSServer createPosterConfigurationForProviderIdentifier:posterDescriptorIdentifier:role:completion:]_block_invoke.19
- ___64-[PRSService _selectConfigurationAndRefreshSnapshot:completion:]_block_invoke.141
- ___64-[PRSService _selectConfigurationAndRefreshSnapshot:completion:]_block_invoke.141.cold.1
- ___73-[PRSServer refreshPosterDescriptorsForExtension:sessionInfo:completion:]_block_invoke.15
- ___75-[PRSServer refreshPosterConfigurationMatchingUUID:sessionInfo:completion:]_block_invoke.24
- ___77-[PRSService createAndSelectLegacyPosterConfigurationIfNeededWithCompletion:]_block_invoke.137
- ___77-[PRSService createAndSelectLegacyPosterConfigurationIfNeededWithCompletion:]_block_invoke.139
- ___block_literal_global.26
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$initWithFileManager:processHandle:unarchivingContainerURL:
- _objc_msgSend$initWithModularComplications:modularLandscapeComplications:inlineComplication:allowsSystemSuggestedComplications:allowsSystemSuggestedComplicationsInLandscape:featuredConfidenceLevel:displayNameLocalizationKey:spokenNameLocalizationKey:descriptiveTextLocalizationKey:hero:shouldShowAsShuffleStack:photoSubtype:focus:onlyEligibleForMadeForFocusSection:
- _objc_msgSend$initWithPoster:type:variant:accentColor:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
CStrings:
+ "-[PRSServer ensurePosterExtensionAvailable:completion:]"
+ "-[PRSServer fetchDownloadablePosterAppsWithCompletion:]"
+ "-[PRSServer installAllPosterAppsWithCompletion:]"
+ "-[PRSServer uninstallAllPosterAppsWithCompletion:]"
+ "/Library/Caches/com.apple.xbs/20592CB2-CE93-4791-B073-22FA0B8D3066/TemporaryDirectory.YcoMN6/Sources/Wallpaper_NonUI/PosterBoardServices/Server/PRSServer.m"
+ "@112@0:8@16@24@32B40B44q48@56@64@72B80B84q88q96B104B108"
+ "@56@0:8@16Q24Q32@40Q48"
+ "TB,R,N,V_isOffloaded"
+ "TQ,R,N,V_size"
+ "Vv24@0:8@?<v@?@\"NSArray<__NSString__>\"@\"NSArray<__NSString__>\"@\"NSError\">16"
+ "_isOffloaded"
+ "_size"
+ "abortWithMessage:"
+ "ensurePosterExtensionAvailable:completion:"
+ "fetchDownloadablePosterAppsWithCompletion:"
+ "initWithModularComplications:modularLandscapeComplications:inlineComplication:allowsSystemSuggestedComplications:allowsSystemSuggestedComplicationsInLandscape:featuredConfidenceLevel:displayNameLocalizationKey:spokenNameLocalizationKey:descriptiveTextLocalizationKey:hero:shouldShowAsShuffleStack:photoSubtype:focus:onlyEligibleForMadeForFocusSection:isOffloaded:"
+ "initWithPFPosterArchiver:"
+ "initWithPoster:type:variant:accentColor:size:"
+ "installAllPosterAppsWithCompletion:"
+ "isOffloaded"
+ "optionsBySettingIsOffloaded:"
+ "processDisallowsAppleArchive"
+ "server:ensurePosterExtensionAvailable:completion:"
+ "server:fetchDownloadablePosterAppsWithCompletion:"
+ "server:installAllPosterAppsWithCompletion:"
+ "server:uninstallAllPosterAppsWithCompletion:"
+ "setIsOffloaded:"
+ "size"
+ "uninstallAllPosterAppsWithCompletion:"
+ "v32@?0@\"NSArray\"8@\"NSArray\"16@\"NSError\"24"
+ "v32@?0@\"NSArray<__NSString__>\"8@\"NSArray<__NSString__>\"16@\"NSError\"24"
- "/Library/Caches/com.apple.xbs/Sources/Wallpaper_NonUI/PosterBoardServices/Server/PRSServer.m"
- "@108@0:8@16@24@32B40B44q48@56@64@72B80B84q88q96B104"
- "@48@0:8@16Q24Q32@40"
- "initWithFileManager:processHandle:"
- "initWithFileManager:processHandle:unarchivingContainerURL:"
- "initWithModularComplications:modularLandscapeComplications:inlineComplication:allowsSystemSuggestedComplications:allowsSystemSuggestedComplicationsInLandscape:featuredConfidenceLevel:displayNameLocalizationKey:spokenNameLocalizationKey:descriptiveTextLocalizationKey:hero:shouldShowAsShuffleStack:photoSubtype:focus:onlyEligibleForMadeForFocusSection:"
- "initWithPoster:type:variant:accentColor:"

```
