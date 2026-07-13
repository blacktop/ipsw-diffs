## BackgroundAssets

> `/System/Library/Frameworks/BackgroundAssets.framework/BackgroundAssets`

```diff

-  __TEXT.__text: 0x63e64
-  __TEXT.__auth_stubs: 0x18c0
+  __TEXT.__text: 0x69744
+  __TEXT.__auth_stubs: 0x19a0
   __TEXT.__objc_methlist: 0x12f0
-  __TEXT.__const: 0x22c0
+  __TEXT.__const: 0x2350
   __TEXT.__gcc_except_tab: 0x360
-  __TEXT.__cstring: 0x3e53
-  __TEXT.__oslogstring: 0x35e3
-  __TEXT.__swift5_typeref: 0xb8e
-  __TEXT.__swift5_fieldmd: 0x660
-  __TEXT.__constg_swiftt: 0x9c8
+  __TEXT.__cstring: 0x3ea3
+  __TEXT.__oslogstring: 0x3ce3
+  __TEXT.__swift5_typeref: 0xbea
+  __TEXT.__swift5_fieldmd: 0x678
+  __TEXT.__constg_swiftt: 0x9f8
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0x5f1
+  __TEXT.__swift5_reflstr: 0x631
   __TEXT.__swift5_assocty: 0x1c8
-  __TEXT.__swift5_capture: 0x478
+  __TEXT.__swift5_capture: 0x4d4
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_proto: 0x14c
   __TEXT.__swift5_types: 0x8c
-  __TEXT.__swift_as_entry: 0xe4
-  __TEXT.__swift_as_ret: 0x104
+  __TEXT.__swift_as_entry: 0xf8
+  __TEXT.__swift_as_ret: 0x114
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1468
-  __TEXT.__eh_frame: 0x2f60
+  __TEXT.__unwind_info: 0x1528
+  __TEXT.__eh_frame: 0x3268
   __TEXT.__objc_classname: 0x677
-  __TEXT.__objc_methname: 0x2da2
+  __TEXT.__objc_methname: 0x2e3c
   __TEXT.__objc_methtype: 0xe21
-  __TEXT.__objc_stubs: 0x1d40
-  __DATA_CONST.__got: 0x4f8
-  __DATA_CONST.__const: 0x540
+  __TEXT.__objc_stubs: 0x1d60
+  __DATA_CONST.__got: 0x568
+  __DATA_CONST.__const: 0x558
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa08
+  __DATA_CONST.__objc_selrefs: 0xa10
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x88
-  __AUTH_CONST.__auth_got: 0xc70
-  __AUTH_CONST.__const: 0x1480
-  __AUTH_CONST.__cfstring: 0x10a0
-  __AUTH_CONST.__objc_const: 0x2708
-  __AUTH.__objc_data: 0x7e8
-  __AUTH.__data: 0x870
-  __DATA.__objc_ivar: 0x11c
-  __DATA.__data: 0x1020
+  __AUTH_CONST.__auth_got: 0xce0
+  __AUTH_CONST.__const: 0x1520
+  __AUTH_CONST.__cfstring: 0x10c0
+  __AUTH_CONST.__objc_const: 0x2768
+  __AUTH.__objc_data: 0x7f0
+  __AUTH.__data: 0x8b0
+  __DATA.__objc_ivar: 0x120
+  __DATA.__data: 0x1080
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x29d0
   __DATA.__common: 0x30

   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/ManagedBackgroundAssets.framework/ManagedBackgroundAssets
   - /System/Library/PrivateFrameworks/ManagedBackgroundAssetsHelper.framework/ManagedBackgroundAssetsHelper
   - /usr/lib/libBASupport.dylib

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftExtensionFoundation.dylib

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftSystem.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1522
-  Symbols:   2260
-  CStrings:  1277
+  Functions: 1555
+  Symbols:   2283
+  CStrings:  1304
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[BADownload wasForegroundDownload]
+ GCC_except_table11
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_CLASS_$_UIApplication
+ _OBJC_IVAR_$_BADownload._wasForegroundDownload
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_BackgroundAssets
+ __swift_FORCE_LOAD_$_swiftSpatial
+ __swift_FORCE_LOAD_$_swiftSpatial_$_BackgroundAssets
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swift_FORCE_LOAD_$_swiftUIKit_$_BackgroundAssets
+ _get_type_metadata 15Synchronization5MutexVySo20NSNotificationCenterC10FoundationE16ObservationTokenVSgG noncopyable
+ _objc_msgSend$defaultCenter
+ _objectdestroy.103Tm
+ _objectdestroy.51Tm
+ _objectdestroy.82Tm
+ _objectdestroy.88Tm
+ _objectdestroy.92Tm
+ _swift_deletedAsyncMethodErrorTu
+ _swift_task_isCurrentExecutor
+ _swift_task_reportUnexpectedExecutor
+ _symbolic SDySSypG
+ _symbolic ShySSG
+ _symbolic _____Sg So20NSNotificationCenterC10FoundationE16ObservationTokenV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 29ManagedBackgroundAssetsHelper26DeferredStatusUpdateRecordC20StaticRepresentationV
+ _symbolic _____y_____SgG 15Synchronization5MutexVAARi_zrlE So20NSNotificationCenterC10FoundationE16ObservationTokenV
+ _symbolic _____y_____SgG 15Synchronization5_CellVAARi_zrlE So20NSNotificationCenterC10FoundationE16ObservationTokenV
+ _symbolic _____y______G So20NSNotificationCenterC10FoundationE21BaseMessageIdentifierV So13UIApplicationC5UIKitE015DidBecomeActiveE0V
- GCC_except_table21
- GCC_except_table9
- _objectdestroy.100Tm
- _objectdestroy.44Tm
- _objectdestroy.79Tm
- _objectdestroy.85Tm
- _objectdestroy.89Tm
CStrings:
+ "%ld deferred status update%{public}s %{public}s drained."
+ "A status update about the failed download with the unique ID “%{public}s” of the asset pack with the ID “%{public}s” couldn’t be deferred: %{public}@"
+ "A status update about the finished download with the unique ID “%{public}s” of the asset pack with the ID “%{public}s” couldn’t be deferred: %{public}@"
+ "App did become active: %{public}s"
+ "Cancellation handler for: %{public}@"
+ "Defer status update about failed download with unique ID: %{public}s error: %{public}@ of asset pack with ID: %{public}s"
+ "Defer status update about finished download with unique ID: %{public}s of asset pack with ID: %{public}s"
+ "Deferred status updates couldn’t be drained: %{public}@"
+ "Deferring a status update about the failed download with the unique ID “%s” of the asset pack with the ID “%{public}s”…"
+ "Deferring a status update about the finished download with the unique ID “%{public}s” of the asset pack with the ID “%{public}s”…"
+ "Drain deferred status updates"
+ "Draining deferred status updates…"
+ "EXAppExtensionAttributes"
+ "EXExtensionPointIdentifier"
+ "Is running in downloader extension"
+ "Report failed download of asset pack with ID: %{public}s version: %lu error: %{public}@"
+ "Report finished download of asset pack with ID: %{public}s version: %lu"
+ "The app became active."
+ "The deferred-status-update kind “%{public}s” is unknown."
+ "The download with the ID “%{public}s” is essential and is already in the foreground; awaiting status updates…"
+ "The essential download with the ID “%{public}s” couldn’t be rescheduled as an optional download: %{public}@"
+ "The fact that version %lu of the asset pack with the ID “%{public}s” failed to be downloaded couldn’t be reported: %{public}@"
+ "The kind of the deferred status update with the record “%{public}s” couldn’t be determined: %{public}@"
+ "Verify download be for known asset pack: %{public}@"
+ "_wasForegroundDownload"
+ "defaultCenter"
+ "foregroundDownloadIDs"
+ "observationToken"
+ "wasForegroundDownload"
- "The asset pack with the ID “%{public}s” was scheduled to be updated."
- "The download with the ID “%{public}s” is essential and is already foreground; awaiting status updates…"
- "The download with the ID “%{public}s” was promoted to the foreground."

```
