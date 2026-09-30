## PosterBoardServices

> `/System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices`

```diff

-289.103.0.0.0
-  __TEXT.__text: 0x45704
+290.105.0.0.0
+  __TEXT.__text: 0x48280
   __TEXT.__auth_stubs: 0xa50
-  __TEXT.__objc_methlist: 0x393c
-  __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x44c2
-  __TEXT.__gcc_except_tab: 0x764
-  __TEXT.__oslogstring: 0x159b
+  __TEXT.__objc_methlist: 0x3944
+  __TEXT.__const: 0x150
+  __TEXT.__cstring: 0x4588
+  __TEXT.__gcc_except_tab: 0x788
+  __TEXT.__oslogstring: 0x282b
   __TEXT.__dlopen_cstrs: 0x203
-  __TEXT.__unwind_info: 0xf48
+  __TEXT.__unwind_info: 0xf98
   __TEXT.__objc_classname: 0x860
-  __TEXT.__objc_methname: 0x9e64
-  __TEXT.__objc_methtype: 0x1a0b
-  __TEXT.__objc_stubs: 0x5d60
+  __TEXT.__objc_methname: 0x9e8e
+  __TEXT.__objc_methtype: 0x1a1a
+  __TEXT.__objc_stubs: 0x5da0
   __DATA_CONST.__got: 0x450
   __DATA_CONST.__const: 0x1118
   __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1de0
+  __DATA_CONST.__objc_selrefs: 0x1de8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1e0
   __AUTH_CONST.__auth_got: 0x538
-  __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x3320
+  __AUTH_CONST.__const: 0x4c0
+  __AUTH_CONST.__cfstring: 0x33c0
   __AUTH_CONST.__objc_const: 0xb778
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xa50
   __DATA.__objc_ivar: 0x3ec
   __DATA.__data: 0x5c0
-  __DATA.__bss: 0x68
+  __DATA.__bss: 0x78
   __DATA_DIRTY.__objc_data: 0xa00
   __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F0BF4FA5-CD2C-384D-A31D-1433B752F7F5
-  Functions: 1616
-  Symbols:   5772
-  CStrings:  2691
+  UUID: 6FDDBDFB-D224-35EC-8F5C-C2459962FC9B
+  Functions: 1648
+  Symbols:   5844
+  CStrings:  2799
 
Symbols:
+ +[NSError(PRSAdditions) prs_entitlementFailureErrorWithFile:line:]
+ -[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:].cold.2
+ -[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:].cold.3
+ _PRSLogExternalSystemService
+ _PRSLogExternalSystemService.__logObj
+ _PRSLogExternalSystemService.cold.1
+ _PRSLogExternalSystemService.onceToken
+ ___103-[PRSServer createPosterConfigurationForProviderIdentifier:posterDescriptorIdentifier:role:completion:]_block_invoke.19
+ ___105-[PRSExternalSystemService createLockScreenPhotosPosterWithImageAtURL:selectLockScreenPoster:completion:]_block_invoke.43
+ ___105-[PRSExternalSystemService createLockScreenPhotosPosterWithImageAtURL:selectLockScreenPoster:completion:]_block_invoke.43.cold.1
+ ___105-[PRSExternalSystemService createLockScreenPhotosPosterWithImageAtURL:selectLockScreenPoster:completion:]_block_invoke.44
+ ___105-[PRSExternalSystemService createLockScreenPhotosPosterWithImageAtURL:selectLockScreenPoster:completion:]_block_invoke.44.cold.1
+ ___105-[PRSExternalSystemService createLockScreenPhotosPosterWithImageAtURL:selectLockScreenPoster:completion:]_block_invoke.46
+ ___105-[PRSExternalSystemService createLockScreenPhotosPosterWithImageAtURL:selectLockScreenPoster:completion:]_block_invoke.46.cold.1
+ ___105-[PRSExternalSystemService createLockScreenPhotosPosterWithImageAtURL:selectLockScreenPoster:completion:]_block_invoke.cold.1
+ ___106-[PRSExternalSystemService updateLockScreenPhotosPoster:withImageAtURL:selectLockScreenPoster:completion:]_block_invoke.61
+ ___106-[PRSExternalSystemService updateLockScreenPhotosPoster:withImageAtURL:selectLockScreenPoster:completion:]_block_invoke.61.cold.1
+ ___106-[PRSExternalSystemService updateLockScreenPhotosPoster:withImageAtURL:selectLockScreenPoster:completion:]_block_invoke.62
+ ___106-[PRSExternalSystemService updateLockScreenPhotosPoster:withImageAtURL:selectLockScreenPoster:completion:]_block_invoke.62.cold.1
+ ___106-[PRSExternalSystemService updateLockScreenPhotosPoster:withImageAtURL:selectLockScreenPoster:completion:]_block_invoke.cold.1
+ ___106-[PRSExternalSystemService updateLockScreenPhotosPoster:withImageAtURL:selectLockScreenPoster:completion:]_block_invoke.cold.2
+ ___112-[PRSExternalSystemService updateHomeScreenImageForLockScreenPoster:withImageAtURL:selectLockPoster:completion:]_block_invoke.64
+ ___112-[PRSExternalSystemService updateHomeScreenImageForLockScreenPoster:withImageAtURL:selectLockPoster:completion:]_block_invoke.64.cold.1
+ ___112-[PRSExternalSystemService updateHomeScreenImageForLockScreenPoster:withImageAtURL:selectLockPoster:completion:]_block_invoke.cold.1
+ ___70-[PRSExternalSystemService fetchEligibleConfigurationsWithCompletion:]_block_invoke.cold.1
+ ___70-[PRSExternalSystemService fetchEligibleConfigurationsWithCompletion:]_block_invoke.cold.2
+ ___73-[PRSServer refreshPosterDescriptorsForExtension:sessionInfo:completion:]_block_invoke.15
+ ___75-[PRSServer refreshPosterConfigurationMatchingUUID:sessionInfo:completion:]_block_invoke.24
+ ___82-[PRSExternalSystemService updatePosterMatchingUUID:withConfiguration:completion:]_block_invoke.cold.1
+ ___82-[PRSExternalSystemService updatePosterMatchingUUID:withConfiguration:completion:]_block_invoke.cold.2
+ ___96-[PRSExternalSystemService createLockScreenPhotosPosterWithImageAtURL:selectedLockScreenPoster:]_block_invoke.cold.1
+ ___96-[PRSExternalSystemService fetchLockScreenWallpaperForRequest:checkLockScreenPoster:completion:]_block_invoke.cold.1
+ ___96-[PRSExternalSystemService fetchLockScreenWallpaperForRequest:checkLockScreenPoster:completion:]_block_invoke.cold.2
+ ___96-[PRSExternalSystemService fetchLockScreenWallpaperForRequest:checkLockScreenPoster:completion:]_block_invoke.cold.3
+ ___96-[PRSExternalSystemService fetchLockScreenWallpaperForRequest:checkLockScreenPoster:completion:]_block_invoke.cold.4
+ ___96-[PRSExternalSystemService fetchLockScreenWallpaperForRequest:checkLockScreenPoster:completion:]_block_invoke.cold.5
+ ___96-[PRSExternalSystemService fetchLockScreenWallpaperForRequest:checkLockScreenPoster:completion:]_block_invoke.cold.6
+ ___97-[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]_block_invoke.101
+ ___97-[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]_block_invoke.102
+ ___97-[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]_block_invoke.102.cold.1
+ ___97-[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]_block_invoke.103
+ ___97-[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]_block_invoke.103.cold.1
+ ___97-[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]_block_invoke.104
+ ___97-[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]_block_invoke.107
+ ___97-[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]_block_invoke.109
+ ___97-[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]_block_invoke.109.cold.1
+ ___97-[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]_block_invoke.98
+ ___97-[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]_block_invoke.98.cold.1
+ ___PRSLogExternalSystemService_block_invoke
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_literal_global.13
+ ___block_literal_global.26
+ _objc_msgSend$prs_entitlementFailureErrorWithFile:line:
+ _objc_msgSend$prs_errorWithCode:userInfo:
- ___103-[PRSServer createPosterConfigurationForProviderIdentifier:posterDescriptorIdentifier:role:completion:]_block_invoke.18
- ___105-[PRSExternalSystemService createLockScreenPhotosPosterWithImageAtURL:selectLockScreenPoster:completion:]_block_invoke_2
- ___105-[PRSExternalSystemService createLockScreenPhotosPosterWithImageAtURL:selectLockScreenPoster:completion:]_block_invoke_3
- ___105-[PRSExternalSystemService createLockScreenPhotosPosterWithImageAtURL:selectLockScreenPoster:completion:]_block_invoke_4
- ___106-[PRSExternalSystemService updateLockScreenPhotosPoster:withImageAtURL:selectLockScreenPoster:completion:]_block_invoke_2
- ___106-[PRSExternalSystemService updateLockScreenPhotosPoster:withImageAtURL:selectLockScreenPoster:completion:]_block_invoke_3
- ___112-[PRSExternalSystemService updateHomeScreenImageForLockScreenPoster:withImageAtURL:selectLockPoster:completion:]_block_invoke_2
- ___73-[PRSServer refreshPosterDescriptorsForExtension:sessionInfo:completion:]_block_invoke.14
- ___75-[PRSServer refreshPosterConfigurationMatchingUUID:sessionInfo:completion:]_block_invoke.23
- ___97-[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]_block_invoke_2
- ___97-[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]_block_invoke_3
- ___97-[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]_block_invoke_4
- ___97-[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]_block_invoke_5
- ___97-[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]_block_invoke_6
- ___97-[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]_block_invoke_7
- ___97-[PRSExternalSystemService resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:]_block_invoke_8
- ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
- ___block_literal_global.20
- ___block_literal_global.25
CStrings:
+ "%s:%u"
+ "/Library/Caches/com.apple.xbs/Sources/Wallpaper_NonUI/PosterBoardServices/Server/PRSServer.m"
+ "@28@0:8r*16i24"
+ "Accessing service instance"
+ "Adding eligible configuration UUID: %{public}@"
+ "Checking configuration with bundle identifier: %{public}@"
+ "Checking if lockScreenImageURL is reachable: %{public}@"
+ "Checking if poster UUID %{public}@ is in eligible set of %ld configurations"
+ "Cleanup completed successfully"
+ "Configuration type is not photo: %ld"
+ "Created %ld poster updates for wallpaper configuration"
+ "Created snapshot request with definition identifier: OSMigration"
+ "Creating lock screen photos poster and starting reset operation"
+ "Creating new PRSService instance"
+ "Deleting configuration: %{public}@"
+ "Error cleaning up failed poster configuration: %{public}@"
+ "Error creating poster configuration: %{public}@"
+ "Error deleting configuration %{public}@: %{public}@"
+ "Error fetching configurations for cleanup: %{public}@"
+ "Error fetching eligible configurations: %{public}@"
+ "Error fetching poster configurations: %{public}@"
+ "Error fetching poster snapshots: %{public}@"
+ "Error loading PFPosterConfiguration: %{public}@"
+ "Error mapping data from PNG file: %{public}@"
+ "Error removing temporary directory: %{public}@"
+ "Error selecting lock screen poster: %{public}@"
+ "Error selecting poster: %{public}@"
+ "Error selecting updated poster: %{public}@"
+ "Error updating home screen image: %{public}@"
+ "Error updating home screen wallpaper (not aborting operation): %{public}@"
+ "Error updating lock screen poster: %{public}@"
+ "Error updating poster configuration with image: %{public}@"
+ "Error updating poster configuration: %{public}@"
+ "Error writing PNG to temporary URL: %{public}@"
+ "ExternalSystemService"
+ "Failed to load PFPosterConfiguration (nil result)"
+ "Found %ld configurations to process for cleanup"
+ "Found %ld eligible configurations"
+ "Future-based poster creation failed: %{public}@"
+ "Future-based poster creation succeeded"
+ "Home screen image updated successfully without lock poster selection"
+ "Initiated deletion of %ld configurations"
+ "Loading PFPosterConfiguration from URL: %{public}@"
+ "Lock screen poster created successfully: %{public}@"
+ "NO"
+ "New configuration UUID to preserve: %{public}@"
+ "No home screen wallpaper to update"
+ "No snapshots available"
+ "No snapshots returned in response"
+ "Poster UUID %{public}@ is not eligible for update"
+ "Poster created successfully without selection"
+ "Poster is eligible, proceeding with update"
+ "Poster updated successfully without selection"
+ "Provider is not PhotosPosterProvider: %{public}@"
+ "Received %ld update results"
+ "Reset lock screen wallpapers operation completed successfully"
+ "Reset lock screen wallpapers operation failed: %{public}@"
+ "Retrieved %ld poster configurations"
+ "Selecting lock screen poster as active"
+ "Selecting newly created poster as active"
+ "Selecting updated poster as active"
+ "Skipping deletion of new configuration: %{public}@"
+ "Skipping non-Photos configuration: %{public}@"
+ "Snapshot provider: %{public}@"
+ "Starting cleanup of existing poster configurations"
+ "Starting createLockScreenPhotosPosterWithImageAtURL (future variant): %{public}@, selectPoster: %{public}@"
+ "Starting createLockScreenPhotosPosterWithImageAtURL: %{public}@, selectPoster: %{public}@"
+ "Starting fetchEligibleConfigurationsWithCompletion"
+ "Starting fetchHomeScreenWallpaperForOrientation: %ld"
+ "Starting fetchHomeScreenWallpaperWithCompletion (portrait orientation)"
+ "Starting fetchLockScreenWallpaperForOrientation: %ld"
+ "Starting fetchLockScreenWallpaperForRequest, checkLockScreenPoster: %{public}@"
+ "Starting fetchLockScreenWallpaperForType: %ld, variant: %ld, options: %ld, orientation: %ld"
+ "Starting fetchLockScreenWallpaperWithCompletion (portrait orientation)"
+ "Starting resetLockScreenWallpapersToImageAtURL: %{public}@"
+ "Starting resetLockScreenWallpapersToImageAtURL: %{public}@, homeScreenWallpaper: %{public}@"
+ "Starting updateHomeScreenImageForLockScreenPoster: %{public}@, imageURL: %{public}@, selectLockPoster: %{public}@"
+ "Starting updateLockScreenPhotosPoster: %{public}@, imageURL: %{public}@, selectPoster: %{public}@"
+ "Starting updatePosterMatchingUUID: %{public}@"
+ "Successfully cleaned up failed poster configuration"
+ "Successfully created poster configuration: %{public}@"
+ "Successfully deleted configuration: %{public}@"
+ "Successfully fetched wallpaper data (%ld bytes)"
+ "Successfully removed temporary directory"
+ "Successfully selected lock screen poster"
+ "Successfully selected poster"
+ "Successfully selected updated poster"
+ "Successfully updated home screen image"
+ "Successfully updated home screen wallpaper"
+ "Successfully updated lock screen poster"
+ "Successfully updated poster configuration"
+ "Successfully updated poster configuration with image"
+ "Successfully wrote PNG, now mapping data"
+ "Update result contains error: %{public}@"
+ "Updating home screen wallpaper"
+ "Writing snapshot to temporary URL: %{public}@"
+ "YES"
+ "an entitlement was not found which was needed."
+ "homeScreenWallpaperURL is not reachable: %{public}@"
+ "homeScreenWallpaperURL is reachable"
+ "lockScreenImageURL is not reachable: %{public}@"
+ "lockScreenImageURL is reachable"
+ "prs_entitlementFailureErrorWithFile:line:"

```
