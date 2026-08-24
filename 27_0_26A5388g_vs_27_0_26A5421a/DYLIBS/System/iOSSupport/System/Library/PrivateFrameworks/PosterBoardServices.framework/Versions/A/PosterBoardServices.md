## PosterBoardServices

> `/System/iOSSupport/System/Library/PrivateFrameworks/PosterBoardServices.framework/Versions/A/PosterBoardServices`

```diff

-350.1.0.0.0
-  __TEXT.__text: 0x7b630
-  __TEXT.__objc_methlist: 0x5038
-  __TEXT.__const: 0xb18
-  __TEXT.__cstring: 0x698b
-  __TEXT.__gcc_except_tab: 0x1000
-  __TEXT.__oslogstring: 0x39ee
+355.0.0.0.0
+  __TEXT.__text: 0x7a850
+  __TEXT.__objc_methlist: 0x5078
+  __TEXT.__const: 0xb28
+  __TEXT.__cstring: 0x6a2b
+  __TEXT.__gcc_except_tab: 0xfbc
+  __TEXT.__oslogstring: 0x37de
   __TEXT.__dlopen_cstrs: 0x2f6
   __TEXT.__swift5_typeref: 0x466
   __TEXT.__constg_swiftt: 0x1b0

   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_capture: 0x30
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1ab0
+  __TEXT.__unwind_info: 0x1a88
   __TEXT.__eh_frame: 0x590
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1bd8
+  __DATA_CONST.__const: 0x1ac0
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a38
+  __DATA_CONST.__objc_selrefs: 0x2a48
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x230
   __DATA_CONST.__got: 0x6e8
-  __AUTH_CONST.__const: 0x728
-  __AUTH_CONST.__cfstring: 0x4bc0
-  __AUTH_CONST.__objc_const: 0x10658
+  __AUTH_CONST.__const: 0x748
+  __AUTH_CONST.__cfstring: 0x4ca0
+  __AUTH_CONST.__objc_const: 0x106d8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0xc48
+  __AUTH_CONST.__auth_got: 0xc28
   __AUTH.__objc_data: 0xdf0
   __AUTH.__data: 0x118
-  __DATA.__objc_ivar: 0x5c4
+  __DATA.__objc_ivar: 0x5cc
   __DATA.__data: 0xc20
-  __DATA.__bss: 0xc50
+  __DATA.__bss: 0xc60
   __DATA.__common: 0x58
   __DATA_DIRTY.__objc_data: 0xf00
   __DATA_DIRTY.__data: 0x58

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2622
-  Symbols:   4944
-  CStrings:  1097
+  Functions: 2616
+  Symbols:   4935
+  CStrings:  1082
 
Symbols:
+ +[PRSPosterUpdater _sharedNotificationService]
+ -[PRSLockScreenColorConfigurationCache invalidateCacheWithReason:]
+ -[PRSMigrationDescriptor configurationMigrationTimeoutInterval]
+ -[PRSMigrationDescriptor setConfigurationMigrationTimeoutInterval:]
+ -[PRSPosterIconConfiguration configVersion]
+ -[PRSPosterIconConfiguration initWithPoster:type:variant:accentColor:size:configVersion:]
+ -[PRSPosterUpdate canBeServicedWithoutExtension]
+ -[PRSServer migrateLockScreenToPhotosWallpaperWithImageData:homeScreenImageData:completion:]
+ -[PRSService migrateLockScreenToPhotosWallpaperWithImageData:homeScreenImageData:completion:]
+ OBJC_IVAR_$_PRSMigrationDescriptor._configurationMigrationTimeoutInterval
+ OBJC_IVAR_$_PRSPosterIconConfiguration._configVersion
+ __93-[PRSService migrateLockScreenToPhotosWallpaperWithImageData:homeScreenImageData:completion:]_block_invoke
+ ___46+[PRSPosterUpdater _sharedNotificationService]_block_invoke
+ ___92-[PRSServer migrateLockScreenToPhotosWallpaperWithImageData:homeScreenImageData:completion:]_block_invoke
+ ___93-[PRSService migrateLockScreenToPhotosWallpaperWithImageData:homeScreenImageData:completion:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e28_v24?0"NSUUID"8"NSError"16ls32l8
+ _objc_msgSend$_sharedNotificationService
+ _objc_msgSend$configurationMigrationTimeoutInterval
+ _objc_msgSend$domain
+ _objc_msgSend$initWithPoster:type:variant:accentColor:size:configVersion:
+ _objc_msgSend$invalidateCacheWithReason:
+ _objc_msgSend$migrateLockScreenToPhotosWallpaperWithImageData:homeScreenImageData:completion:
+ _objc_msgSend$server:migrateLockScreenToPhotosWallpaperWithImageData:homeScreenImageData:completion:
+ _objc_msgSend$setConfigurationMigrationTimeoutInterval:
+ _sharedNotificationService.onceToken
+ _sharedNotificationService.service
- -[PRSExternalSystemService createLockScreenPhotosPosterWithImageAtURL:selectedLockScreenPoster:]
- -[PRSPosterIconConfiguration initWithPoster:type:variant:accentColor:size:]
- -[PRSPosterUpdater synchronouslyApplyUpdates:error:]
- -[PRSServer forceUpdatePosterPath:updates:completion:]
- -[PRSService forceUpdatePosterPath:updates:error:]
- GCC_except_table1
- GCC_except_table18
- _OUTLINED_FUNCTION_20
- __50-[PRSService forceUpdatePosterPath:updates:error:]_block_invoke
- __96-[PRSExternalSystemService createLockScreenPhotosPosterWithImageAtURL:selectedLockScreenPoster:]_block_invoke
- ___50-[PRSService forceUpdatePosterPath:updates:error:]_block_invoke
- ___96-[PRSExternalSystemService createLockScreenPhotosPosterWithImageAtURL:selectedLockScreenPoster:]_block_invoke
- ___block_descriptor_40_e8_32bs_e32_v16?0"PRSPosterConfiguration"8ls32l8
- ___block_descriptor_40_e8_32s_e44_v24?0"PRSPosterConfiguration"8"NSError"16ls32l8
- ___block_descriptor_48_e8_32s40bs_e45_"<PFTFuture>"16?0"PRSPosterConfiguration"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8ls32l8r40l8
- ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e43_"PFTFuture"16?0"PRSPosterConfiguration"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e70_v32?0"PRSPosterConfiguration"8"PRSPosterUpdateResult"16"NSError"24ls32l8s40l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e29_v24?0"NSArray"8"NSError"16ls64l8s32l8s40l8s48l8s56l8
- ___getPRPosterPathModelObjectCacheClass_block_invoke
- __getPRPosterPathModelObjectCacheClass_block_invoke
- _dispatch_group_create
- _dispatch_group_enter
- _dispatch_group_leave
- _dispatch_group_notify
- _objc_msgSend$createLockScreenPhotosPosterWithImageAtURL:selectLockScreenPoster:completion:
- _objc_msgSend$createLockScreenPhotosPosterWithImageAtURL:selectedLockScreenPoster:
- _objc_msgSend$finishWithResult:
- _objc_msgSend$forceUpdatePosterPath:updates:completion:
- _objc_msgSend$forceUpdatePosterPath:updates:error:
- _objc_msgSend$initWithPoster:type:variant:accentColor:size:
- _objc_msgSend$invalidateModelObjectCacheForPath:
- _objc_msgSend$server:forceUpdatePosterPath:updates:completion:
- getPRPosterPathModelObjectCacheClass.softClass
CStrings:
+ "-[PRSServer migrateLockScreenToPhotosWallpaperWithImageData:homeScreenImageData:completion:]"
+ "Active poster provider is %@, not PhotosPosterProvider; will not return data"
+ "Cache file unavailable (errno %d)"
+ "Could not render the poster snapshot (the render may have timed out)"
+ "Failed to read homeScreenWallpaperURL: %{public}@"
+ "Failed to read lockScreenImageURL: %{public}@"
+ "No poster snapshot was produced (the render may have timed out or returned nothing)"
+ "PRSLockScreenColorConfigurationCache: cache open failed: %{darwin.errno}d"
+ "PRSLockScreenColorConfigurationCache: invalidate (%{public}@) delete failed: %{public}@"
+ "PRSLockScreenColorConfigurationCache: invalidated (deleted) cache: %{public}@"
+ "PRSLockScreenColorConfigurationCache: unarchive failed / unexpected root type: %{public}@"
+ "PRSLockScreenColorConfigurationCache: unarchive threw: %{public}@"
+ "Reset complete; new active poster UUID=%{public}@"
+ "Snapshot contained no %@ configuration; the poster render did not complete"
+ "Snapshot has no %{public}@ configuration path; render did not complete"
+ "_configVersion"
+ "_configurationMigrationTimeoutInterval"
+ "com.apple.migrationd"
+ "configurationMigrationTimeoutInterval"
+ "file unavailable"
+ "home-screen"
+ "hostConfiguredPropertiesDidChange"
+ "lock-screen"
+ "lockScreenImageData"
+ "migrateLockScreenToPhotosWallpaper failed: %{public}@"
+ "migrateLockScreenToPhotosWallpaper: allowing com.apple.migrationd via temporary signing-identity bypass (pending deleteDescriptors adoption, rdar://TODO-ADOPTION)"
- "-[PRSServer forceUpdatePosterPath:updates:completion:]"
- "@\"<PFTFuture>\"16@?0@\"PRSPosterConfiguration\"8"
- "@\"PFTFuture\"16@?0@\"PRSPosterConfiguration\"8"
- "Cache file missing"
- "Checking if lockScreenImageURL is reachable: %{public}@"
- "Class getPRPosterPathModelObjectCacheClass(void)_block_invoke"
- "Cleanup completed successfully"
- "Creating lock screen photos poster and starting reset operation"
- "Deleting configuration: %{public}@"
- "Error deleting configuration %{public}@: %{public}@"
- "Error fetching configurations for cleanup: %{public}@"
- "Error updating home screen wallpaper (not aborting operation): %{public}@"
- "Found %ld configurations to process for cleanup"
- "Future-based poster creation failed: %{public}@"
- "Future-based poster creation succeeded"
- "Initiated deletion of %ld configurations"
- "Lock screen poster created successfully: %{public}@"
- "New configuration UUID to preserve: %{public}@"
- "No home screen wallpaper to update"
- "No snapshots available"
- "PRPosterPathModelObjectCache"
- "Provider is not PhotosPosterProvider; will not return data"
- "Reset lock screen wallpapers operation completed successfully"
- "Reset lock screen wallpapers operation failed: %{public}@"
- "Skipping deletion of new configuration: %{public}@"
- "Starting cleanup of existing poster configurations"
- "Starting createLockScreenPhotosPosterWithImageAtURL (future variant): %{public}@, selectPoster: %{public}@"
- "Successfully deleted configuration: %{public}@"
- "Successfully updated home screen wallpaper"
- "Updating home screen wallpaper"
- "file missing"
- "force RPC failed on %{public}@: %{public}@"
- "force RPC reply received on %{public}@"
- "forceUpdatePosterPath: nil path"
- "homeScreenWallpaperURL is not reachable"
- "homeScreenWallpaperURL is not reachable: %{public}@"
- "homeScreenWallpaperURL is reachable"
- "lockScreenImageURL is not reachable"
- "lockScreenImageURL is not reachable: %{public}@"
- "lockScreenImageURL is reachable"
- "v16@?0@\"PRSPosterConfiguration\"8"
```
