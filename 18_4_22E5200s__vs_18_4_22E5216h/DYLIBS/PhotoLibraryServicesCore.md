## PhotoLibraryServicesCore

> `/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore`

```diff

-750.5.104.0.0
-  __TEXT.__text: 0xc2e4c
-  __TEXT.__auth_stubs: 0x1ca0
-  __TEXT.__objc_methlist: 0x7d1c
-  __TEXT.__const: 0x2484
-  __TEXT.__cstring: 0x13d9a
+750.11.101.0.0
+  __TEXT.__text: 0xc2dc4
+  __TEXT.__auth_stubs: 0x1c90
+  __TEXT.__objc_methlist: 0x7cd4
+  __TEXT.__const: 0x249c
+  __TEXT.__cstring: 0x14013
   __TEXT.__dlopen_cstrs: 0x19c
-  __TEXT.__gcc_except_tab: 0x7044
-  __TEXT.__oslogstring: 0x9ddb
-  __TEXT.__unwind_info: 0x3000
-  __TEXT.__objc_classname: 0x107e
-  __TEXT.__objc_methname: 0x15303
-  __TEXT.__objc_methtype: 0x4c08
-  __TEXT.__objc_stubs: 0xba00
-  __DATA_CONST.__got: 0xaa8
-  __DATA_CONST.__const: 0x38e8
+  __TEXT.__gcc_except_tab: 0x7080
+  __TEXT.__oslogstring: 0x9e02
+  __TEXT.__unwind_info: 0x2ff8
+  __TEXT.__objc_classname: 0x107a
+  __TEXT.__objc_methname: 0x1524d
+  __TEXT.__objc_methtype: 0x4bed
+  __TEXT.__objc_stubs: 0xb9e0
+  __DATA_CONST.__got: 0xa98
+  __DATA_CONST.__const: 0x39b0
   __DATA_CONST.__objc_classlist: 0x400
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4998
+  __DATA_CONST.__objc_selrefs: 0x4978
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x260
-  __DATA_CONST.__objc_arraydata: 0x418
-  __AUTH_CONST.__auth_got: 0xe60
+  __DATA_CONST.__objc_arraydata: 0x408
+  __AUTH_CONST.__auth_got: 0xe58
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x32f0
-  __AUTH_CONST.__cfstring: 0x10a20
-  __AUTH_CONST.__objc_const: 0xa640
+  __AUTH_CONST.__const: 0x3310
+  __AUTH_CONST.__cfstring: 0x10cc0
+  __AUTH_CONST.__objc_const: 0xa5d0
   __AUTH_CONST.__objc_intobj: 0x960
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_arrayobj: 0x258
+  __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x64c
+  __DATA.__objc_ivar: 0x640
   __DATA.__data: 0x1020
-  __DATA.__bss: 0xb98
+  __DATA.__bss: 0xba8
   __DATA_DIRTY.__objc_data: 0x2580
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x548

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3695
-  Symbols:   5548
-  CStrings:  7125
+  Functions: 3690
+  Symbols:   5565
+  CStrings:  7135
 
Symbols:
+ _PLCameraBundleId
+ _PLCameraLockScreenBundleId
+ _PLCameraMessagesBundleId
+ _PLCaptureBundleId
+ _PLCarPlayAppBundleId
+ _PLFileProviderLocalStorageBundleID
+ _PLFilesPlaceholderBundleID
+ _PLImagePlaygroundAppBundleIdentifier
+ _PLIsImagePlaygroundApp
+ _PLLibraryServicesOperationNameCheckForAutoCreateWellKnownLibrary
+ _PLMessagesBundleID
+ _PLMigrationKitBundleId
+ _PLMobileDocumentsFileProviderBundleID
+ _PLMobileSlideshowBundleId
+ _PLNotesBundleID
+ _PLPhotosBundleId
+ _PLPhotosPickerBundleId
+ _PLQuickLookPreviewBundleId
+ _PLScreenshotsBundleId
+ _PLShareAddToPhotoBundleId
+ _PLSharingDaemonBundleId
+ _PLSpotlightBundleId
+ _PLSpringBoardBundleId
+ _PLStickersBundleID
+ _PLSurfBoardBundleId
+ _PLiCloudDriveFileProviderBundleID
+ _PLiCloudDriveFileProviderManagedBundleID
- _NSKeyValueChangeNewKey
- _NSKeyValueChangeOldKey
- _PLMacPlatformLibraryServicesOperationNameCheckForAutoCreateSPL
- _sprintf
CStrings:
+ "@56@0:8@16@24q32@40@?48"
+ "Check for auto-create well-known library"
+ "LSM is nil, not executing operation %@"
+ "com.apple.Capture"
+ "com.apple.CarPlayApp"
+ "com.apple.CloudDocs.MobileDocumentsFileProvider"
+ "com.apple.CloudDocs.iCloudDriveFileProvider"
+ "com.apple.CloudDocs.iCloudDriveFileProviderManaged"
+ "com.apple.FileProvider.LocalStorage"
+ "com.apple.GenerativePlaygroundApp"
+ "com.apple.MigrationKit"
+ "com.apple.MobileSMS"
+ "com.apple.ScreenshotServicesService"
+ "com.apple.Spotlight"
+ "com.apple.Stickers"
+ "com.apple.SurfBoard"
+ "com.apple.camera.CameraMessagesApp"
+ "com.apple.mobilenotes"
+ "com.apple.mobileslideshow.photospicker"
+ "com.apple.photos.filesPlaceholder"
+ "com.apple.quicklook.extension.previewUI"
+ "com.apple.share.System.add-to-iphoto"
+ "com.apple.sharingd"
+ "com.apple.springboard"
+ "operationWithName:libraryServicesManager:requiredState:parentProgress:executionBlock:"
+ "unknown(%ld)"
- "\x01!\x11"
- "@48@0:8@16q24@32@?40"
- "@?16@0:8"
- "Check for auto-create SPL"
- "T@?,C,N,V_cancellationBlock"
- "_cancellationBlock"
- "_cancellationBlockCalled"
- "_cancellationLock"
- "_safeRemoveCancellationObserver"
- "cancel changed context"
- "cancellationBlock"
- "cancelled"
- "observeValueForKeyPath:ofObject:change:context:"
- "operationWithName:requiredState:parentProgress:execution:"
- "setCancellationBlock:"
- "v48@0:8@16@24@32^v40"

```
