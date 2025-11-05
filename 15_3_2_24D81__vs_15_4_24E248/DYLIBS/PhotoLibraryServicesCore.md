## PhotoLibraryServicesCore

> `/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/Versions/A/PhotoLibraryServicesCore`

```diff

-741.0.130.0.0
-  __TEXT.__text: 0xcdee4
+751.0.104.0.0
+  __TEXT.__text: 0xd12d8
   __TEXT.__auth_stubs: 0x1a40
-  __TEXT.__objc_methlist: 0x66b8
-  __TEXT.__const: 0x22f4
-  __TEXT.__gcc_except_tab: 0x6f78
-  __TEXT.__cstring: 0x132d3
-  __TEXT.__oslogstring: 0xa0a6
+  __TEXT.__objc_methlist: 0x7f9c
+  __TEXT.__const: 0x22fc
+  __TEXT.__cstring: 0x13883
   __TEXT.__dlopen_cstrs: 0xe1
-  __TEXT.__unwind_info: 0x2e90
-  __TEXT.__objc_classname: 0x105d
-  __TEXT.__objc_methname: 0x15e23
-  __TEXT.__objc_methtype: 0x4b6a
-  __TEXT.__objc_stubs: 0xbf60
-  __DATA_CONST.__got: 0xa38
-  __DATA_CONST.__const: 0x1f88
-  __DATA_CONST.__objc_classlist: 0x3e8
+  __TEXT.__gcc_except_tab: 0x7128
+  __TEXT.__oslogstring: 0xa221
+  __TEXT.__unwind_info: 0x2f18
+  __TEXT.__objc_classname: 0x110e
+  __TEXT.__objc_methname: 0x160c4
+  __TEXT.__objc_methtype: 0x4c6d
+  __TEXT.__objc_stubs: 0xc300
+  __DATA_CONST.__got: 0xa50
+  __DATA_CONST.__const: 0x2078
+  __DATA_CONST.__objc_classlist: 0x410
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x150
+  __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b80
+  __DATA_CONST.__objc_selrefs: 0x4d48
   __DATA_CONST.__objc_protorefs: 0xc0
-  __DATA_CONST.__objc_superrefs: 0x248
+  __DATA_CONST.__objc_superrefs: 0x268
   __DATA_CONST.__objc_arraydata: 0x408
   __AUTH_CONST.__auth_got: 0xd30
-  __AUTH_CONST.__const: 0x4d90
-  __AUTH_CONST.__cfstring: 0x10240
-  __AUTH_CONST.__objc_const: 0xcfe8
+  __AUTH_CONST.__const: 0x4ea0
+  __AUTH_CONST.__cfstring: 0x10660
+  __AUTH_CONST.__objc_const: 0xac48
   __AUTH_CONST.__objc_intobj: 0x948
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x240
-  __AUTH.__objc_data: 0x2710
-  __DATA.__objc_ivar: 0x644
-  __DATA.__data: 0x1028
-  __DATA.__bss: 0xfe8
+  __AUTH.__objc_data: 0x28a0
+  __DATA.__objc_ivar: 0x690
+  __DATA.__data: 0x1088
+  __DATA.__bss: 0x1028
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: C01F91DA-FFC8-3F94-A047-368FAFE1302F
-  Functions: 3757
-  Symbols:   9543
-  CStrings:  9265
+  UUID: 33715765-5439-328E-8B64-B81F4B9C96BF
+  Functions: 3810
+  Symbols:   9765
+  CStrings:  9375
 
Symbols:
+ +[PLLibraryServicesOperation operationWithName:libraryServicesManager:requiredState:parentProgress:executionBlock:]
+ +[PLPhotoLibraryPathManager photosLibrariesDataVaultPath]
+ +[PLPhotoLibraryPathManager photosLibraryTombstoneExtension]
+ +[PLPhotoLibraryPathManagerCore photosLibraryTombstoneExtension]
+ +[PLXPCLibraryToken clientOptions]
+ +[PLXPCLibraryToken clientToServiceSandboxExtensionForURL:]
+ +[PLXPCLibraryToken supportsSecureCoding]
+ -[PLAssetsdBaseClient clientState]
+ -[PLAssetsdBaseClient initWithQueue:proxyCreating:proxyGetter:clientState:]
+ -[PLAssetsdClient _isSecondXPCConnectionDisabled]
+ -[PLAssetsdClient _primitiveClientForCurrentQoS]
+ -[PLAssetsdClient nonBindingPhotoKitAddClient]
+ -[PLAssetsdClient nonBindingPhotoKitClient]
+ -[PLAssetsdClientState .cxx_destruct]
+ -[PLAssetsdClientState consumeSandboxExtensions:]
+ -[PLAssetsdClientState init]
+ -[PLAssetsdClientState isOpen]
+ -[PLAssetsdCloudClient computeStableHashesOfAsset:synchronously:completionHandler:]
+ -[PLAssetsdDebugClient requestSearchDebugInformationForAssetUUID:redacted:error:]
+ -[PLAssetsdLibraryClient isOpen]
+ -[PLAssetsdLibraryInternalClient signalAvailabilityWithChanges:error:]
+ -[PLAssetsdResourceClient initWithQueue:proxyCreating:proxyGetter:clientState:]
+ -[PLNonBindingAssetsdPhotoKitAddClient .cxx_destruct]
+ -[PLNonBindingAssetsdPhotoKitAddClient clientName]
+ -[PLNonBindingAssetsdPhotoKitAddClient initWithQueue:proxyCreating:libraryURL:]
+ -[PLNonBindingAssetsdPhotoKitAddClient sendChangesRequest:error:]
+ -[PLNonBindingAssetsdPhotoKitAddClient sendChangesRequest:reply:]
+ -[PLNonBindingAssetsdPhotoKitClient .cxx_destruct]
+ -[PLNonBindingAssetsdPhotoKitClient clientName]
+ -[PLNonBindingAssetsdPhotoKitClient initWithQueue:proxyCreating:libraryURL:]
+ -[PLNonBindingAssetsdPhotoKitClient sendChangesRequest:error:]
+ -[PLNonBindingAssetsdPhotoKitClient sendChangesRequest:reply:]
+ -[PLPrimitiveAssetsdClient .cxx_destruct]
+ -[PLPrimitiveAssetsdClient _setupClientClass:proxyGetter:options:]
+ -[PLPrimitiveAssetsdClient _updateLibraryStateConnectionInterrupted:]
+ -[PLPrimitiveAssetsdClient addPhotoLibraryUnavailabilityHandler:]
+ -[PLPrimitiveAssetsdClient cloudClient]
+ -[PLPrimitiveAssetsdClient cloudInternalClient]
+ -[PLPrimitiveAssetsdClient dealloc]
+ -[PLPrimitiveAssetsdClient debugClient]
+ -[PLPrimitiveAssetsdClient demoClient]
+ -[PLPrimitiveAssetsdClient diagnosticsClient]
+ -[PLPrimitiveAssetsdClient initWithPhotoLibraryURL:clientState:]
+ -[PLPrimitiveAssetsdClient init]
+ -[PLPrimitiveAssetsdClient libraryClient]
+ -[PLPrimitiveAssetsdClient libraryInternalClient]
+ -[PLPrimitiveAssetsdClient libraryManagementClient]
+ -[PLPrimitiveAssetsdClient migrationClient]
+ -[PLPrimitiveAssetsdClient nonBindingDebugClient]
+ -[PLPrimitiveAssetsdClient nonBindingPhotoKitAddClient]
+ -[PLPrimitiveAssetsdClient nonBindingPhotoKitClient]
+ -[PLPrimitiveAssetsdClient notificationClient]
+ -[PLPrimitiveAssetsdClient photoKitAddClient]
+ -[PLPrimitiveAssetsdClient photoKitClient]
+ -[PLPrimitiveAssetsdClient privacySupportClient]
+ -[PLPrimitiveAssetsdClient resourceAvailabilityClient]
+ -[PLPrimitiveAssetsdClient resourceClient]
+ -[PLPrimitiveAssetsdClient resourceInternalClient]
+ -[PLPrimitiveAssetsdClient resourceWriteOnlyClient]
+ -[PLPrimitiveAssetsdClient sendDaemonJob:shouldRunSerially:replyHandler:]
+ -[PLPrimitiveAssetsdClient syncClient]
+ -[PLPrimitiveAssetsdClient systemLibraryURLReadOnlyClient]
+ -[PLPrimitiveAssetsdClient waitUntilConnectionSendsAllMessages]
+ -[PLXPCLibraryToken .cxx_destruct]
+ -[PLXPCLibraryToken clientOptions]
+ -[PLXPCLibraryToken encodeWithCoder:]
+ -[PLXPCLibraryToken initWithCoder:]
+ -[PLXPCLibraryToken initWithURL:]
+ -[PLXPCLibraryToken initWithURL:sandboxExtension:clientOptions:]
+ -[PLXPCLibraryToken sandboxExtension]
+ -[PLXPCLibraryToken url]
+ GCC_except_table1000
+ GCC_except_table1008
+ GCC_except_table1011
+ GCC_except_table1014
+ GCC_except_table1017
+ GCC_except_table1020
+ GCC_except_table1023
+ GCC_except_table1027
+ GCC_except_table1031
+ GCC_except_table1034
+ GCC_except_table1037
+ GCC_except_table1040
+ GCC_except_table1046
+ GCC_except_table1050
+ GCC_except_table1053
+ GCC_except_table1083
+ GCC_except_table1085
+ GCC_except_table1131
+ GCC_except_table1454
+ GCC_except_table1611
+ GCC_except_table1618
+ GCC_except_table1653
+ GCC_except_table1664
+ GCC_except_table1684
+ GCC_except_table1700
+ GCC_except_table1729
+ GCC_except_table1732
+ GCC_except_table1735
+ GCC_except_table1738
+ GCC_except_table1740
+ GCC_except_table1748
+ GCC_except_table1751
+ GCC_except_table1754
+ GCC_except_table1757
+ GCC_except_table1771
+ GCC_except_table1774
+ GCC_except_table1777
+ GCC_except_table1780
+ GCC_except_table1784
+ GCC_except_table1791
+ GCC_except_table1794
+ GCC_except_table1797
+ GCC_except_table1800
+ GCC_except_table1808
+ GCC_except_table1811
+ GCC_except_table1814
+ GCC_except_table1817
+ GCC_except_table1825
+ GCC_except_table1833
+ GCC_except_table1941
+ GCC_except_table1960
+ GCC_except_table2151
+ GCC_except_table2156
+ GCC_except_table2157
+ GCC_except_table2159
+ GCC_except_table2162
+ GCC_except_table2289
+ GCC_except_table229
+ GCC_except_table2359
+ GCC_except_table238
+ GCC_except_table2399
+ GCC_except_table241
+ GCC_except_table243
+ GCC_except_table2431
+ GCC_except_table2447
+ GCC_except_table245
+ GCC_except_table2450
+ GCC_except_table2453
+ GCC_except_table2456
+ GCC_except_table2459
+ GCC_except_table2462
+ GCC_except_table2465
+ GCC_except_table2468
+ GCC_except_table2492
+ GCC_except_table250
+ GCC_except_table2528
+ GCC_except_table2531
+ GCC_except_table2533
+ GCC_except_table2544
+ GCC_except_table256
+ GCC_except_table2562
+ GCC_except_table2564
+ GCC_except_table2568
+ GCC_except_table2572
+ GCC_except_table2576
+ GCC_except_table2580
+ GCC_except_table2584
+ GCC_except_table2588
+ GCC_except_table259
+ GCC_except_table2592
+ GCC_except_table2596
+ GCC_except_table2600
+ GCC_except_table2603
+ GCC_except_table2607
+ GCC_except_table2615
+ GCC_except_table2623
+ GCC_except_table2630
+ GCC_except_table2637
+ GCC_except_table264
+ GCC_except_table2640
+ GCC_except_table2643
+ GCC_except_table2645
+ GCC_except_table2648
+ GCC_except_table267
+ GCC_except_table2671
+ GCC_except_table2674
+ GCC_except_table2677
+ GCC_except_table2680
+ GCC_except_table2683
+ GCC_except_table2686
+ GCC_except_table2689
+ GCC_except_table2691
+ GCC_except_table272
+ GCC_except_table275
+ GCC_except_table278
+ GCC_except_table2808
+ GCC_except_table287
+ GCC_except_table2878
+ GCC_except_table290
+ GCC_except_table2932
+ GCC_except_table2944
+ GCC_except_table2946
+ GCC_except_table2950
+ GCC_except_table2952
+ GCC_except_table2970
+ GCC_except_table2979
+ GCC_except_table298
+ GCC_except_table2983
+ GCC_except_table306
+ GCC_except_table309
+ GCC_except_table312
+ GCC_except_table3132
+ GCC_except_table3137
+ GCC_except_table3142
+ GCC_except_table3147
+ GCC_except_table3150
+ GCC_except_table3153
+ GCC_except_table317
+ GCC_except_table3185
+ GCC_except_table3190
+ GCC_except_table320
+ GCC_except_table3250
+ GCC_except_table3253
+ GCC_except_table3264
+ GCC_except_table3428
+ GCC_except_table3438
+ GCC_except_table3443
+ GCC_except_table3447
+ GCC_except_table3454
+ GCC_except_table3508
+ GCC_except_table3511
+ GCC_except_table3518
+ GCC_except_table3524
+ GCC_except_table3528
+ GCC_except_table3536
+ GCC_except_table3540
+ GCC_except_table3563
+ GCC_except_table3568
+ GCC_except_table3577
+ GCC_except_table3590
+ GCC_except_table3608
+ GCC_except_table3618
+ GCC_except_table3623
+ GCC_except_table3627
+ GCC_except_table3633
+ GCC_except_table3638
+ GCC_except_table3641
+ GCC_except_table3644
+ GCC_except_table3648
+ GCC_except_table3651
+ GCC_except_table3657
+ GCC_except_table3662
+ GCC_except_table3665
+ GCC_except_table3669
+ GCC_except_table3672
+ GCC_except_table3675
+ GCC_except_table3678
+ GCC_except_table3681
+ GCC_except_table3685
+ GCC_except_table3689
+ GCC_except_table3705
+ GCC_except_table3750
+ GCC_except_table376
+ GCC_except_table377
+ GCC_except_table3776
+ GCC_except_table3777
+ GCC_except_table3778
+ GCC_except_table3780
+ GCC_except_table3782
+ GCC_except_table3784
+ GCC_except_table3785
+ GCC_except_table3788
+ GCC_except_table3795
+ GCC_except_table398
+ GCC_except_table404
+ GCC_except_table411
+ GCC_except_table424
+ GCC_except_table473
+ GCC_except_table478
+ GCC_except_table481
+ GCC_except_table484
+ GCC_except_table487
+ GCC_except_table492
+ GCC_except_table499
+ GCC_except_table502
+ GCC_except_table506
+ GCC_except_table510
+ GCC_except_table516
+ GCC_except_table519
+ GCC_except_table525
+ GCC_except_table529
+ GCC_except_table540
+ GCC_except_table598
+ GCC_except_table657
+ GCC_except_table696
+ GCC_except_table699
+ GCC_except_table702
+ GCC_except_table708
+ GCC_except_table712
+ GCC_except_table715
+ GCC_except_table718
+ GCC_except_table721
+ GCC_except_table722
+ GCC_except_table884
+ GCC_except_table887
+ GCC_except_table890
+ GCC_except_table893
+ GCC_except_table899
+ GCC_except_table902
+ GCC_except_table905
+ GCC_except_table908
+ GCC_except_table911
+ GCC_except_table929
+ GCC_except_table932
+ GCC_except_table935
+ GCC_except_table938
+ GCC_except_table942
+ GCC_except_table946
+ GCC_except_table949
+ GCC_except_table952
+ GCC_except_table955
+ GCC_except_table958
+ GCC_except_table961
+ GCC_except_table964
+ GCC_except_table967
+ GCC_except_table970
+ GCC_except_table973
+ GCC_except_table976
+ GCC_except_table987
+ GCC_except_table991
+ GCC_except_table994
+ GCC_except_table997
+ OBJC_IVAR_$_PLAssetsdBaseClient._clientState
+ OBJC_IVAR_$_PLAssetsdClient._clientState
+ OBJC_IVAR_$_PLAssetsdClient._highPriorityClient
+ OBJC_IVAR_$_PLAssetsdClient._lowPriorityClient
+ OBJC_IVAR_$_PLAssetsdClientSandboxExtensions._lock
+ OBJC_IVAR_$_PLAssetsdClientSandboxExtensions._lock_securityScopedURLs
+ OBJC_IVAR_$_PLAssetsdClientState._isOpen
+ OBJC_IVAR_$_PLAssetsdClientState._sandboxExtensions
+ OBJC_IVAR_$_PLDelayedActionTimer._lock
+ OBJC_IVAR_$_PLNonBindingAssetsdClient._clientState
+ OBJC_IVAR_$_PLNonBindingAssetsdPhotoKitAddClient._libraryToken
+ OBJC_IVAR_$_PLNonBindingAssetsdPhotoKitAddClient._libraryURL
+ OBJC_IVAR_$_PLNonBindingAssetsdPhotoKitAddClient._proxyFactory
+ OBJC_IVAR_$_PLNonBindingAssetsdPhotoKitAddClient._queue
+ OBJC_IVAR_$_PLNonBindingAssetsdPhotoKitClient._libraryToken
+ OBJC_IVAR_$_PLNonBindingAssetsdPhotoKitClient._libraryURL
+ OBJC_IVAR_$_PLNonBindingAssetsdPhotoKitClient._proxyFactory
+ OBJC_IVAR_$_PLNonBindingAssetsdPhotoKitClient._queue
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._autoBindingProxyFactory
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._clientState
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._cloudClient
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._cloudInternalClient
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._connection
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._debugClient
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._demoClient
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._diagnosticsClient
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._isolationQueue
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._libraryClient
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._libraryInternalClient
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._libraryManagementClient
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._libraryURL
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._migrationClient
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._nonBindingDebugClient
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._nonBindingPhotoKitAddClient
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._nonBindingPhotoKitClient
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._notificationClient
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._photoKitAddClient
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._photoKitClient
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._privacySupportClient
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._resourceAvailabilityClient
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._resourceClient
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._resourceInternalClient
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._resourceWriteOnlyClient
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._sandboxExtensions
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._syncClient
+ OBJC_IVAR_$_PLPrimitiveAssetsdClient._systemLibraryURLReadOnlyClient
+ OBJC_IVAR_$_PLXPCLibraryToken._clientOptions
+ OBJC_IVAR_$_PLXPCLibraryToken._sandboxExtension
+ OBJC_IVAR_$_PLXPCLibraryToken._url
+ PLIsImagePlaygroundApp.didCheck
+ PLIsImagePlaygroundApp.isImagePlayground
+ PLIsMacPhotosApp.didCheck
+ PLIsMacPhotosApp.isPhotosApp
+ PLSearchBackendFeedbackDiagnosticsGetLog.log
+ PLSearchBackendFeedbackDiagnosticsGetLog.predicate
+ PLSearchBackendIndexEntityResultGetLog.log
+ PLSearchBackendIndexEntityResultGetLog.predicate
+ PL_gKTXFileIdentifier.11607
+ _OBJC_$_PROP_LIST_PLPhotoLibraryPathManagerCore.636
+ _OBJC_CLASS_$_PLAssetsdClientState
+ _OBJC_CLASS_$_PLNonBindingAssetsdPhotoKitAddClient
+ _OBJC_CLASS_$_PLNonBindingAssetsdPhotoKitClient
+ _OBJC_CLASS_$_PLPrimitiveAssetsdClient
+ _OBJC_CLASS_$_PLXPCLibraryToken
+ _OBJC_METACLASS_$_PLAssetsdClientState
+ _OBJC_METACLASS_$_PLNonBindingAssetsdPhotoKitAddClient
+ _OBJC_METACLASS_$_PLNonBindingAssetsdPhotoKitClient
+ _OBJC_METACLASS_$_PLPrimitiveAssetsdClient
+ _OBJC_METACLASS_$_PLXPCLibraryToken
+ _PLCameraBundleId
+ _PLCameraLockScreenBundleId
+ _PLCameraMessagesBundleId
+ _PLCaptureBundleId
+ _PLCarPlayAppBundleId
+ _PLDisableSecondXPCConnectionUserDefaultsKey
+ _PLFileProviderLocalStorageBundleID
+ _PLFilesPlaceholderBundleID
+ _PLImagePlaygroundAppBundleIdentifier
+ _PLIsImagePlaygroundApp
+ _PLIsMacPhotosApp
+ _PLLibraryServicesOperationNameCheckForAutoCreateWellKnownLibrary
+ _PLLibraryServicesOperationNameCrashRecoveryProcessAssetAlbumAssociativity
+ _PLMessagesBundleID
+ _PLMigrationKitBundleId
+ _PLMobileDocumentsFileProviderBundleID
+ _PLMobileSlideshowBundleId
+ _PLNotesBundleID
+ _PLPhotosBundleId
+ _PLPhotosPickerBundleId
+ _PLQuickLookPreviewBundleId
+ _PLScreenshotsBundleId
+ _PLSearchBackendFeedbackDiagnosticsGetLog
+ _PLSearchBackendIndexEntityResultGetLog
+ _PLShareAddToPhotoBundleId
+ _PLSharingDaemonBundleId
+ _PLSpotlightBundleId
+ _PLSpringBoardBundleId
+ _PLStickersBundleID
+ _PLSurfBoardBundleId
+ _PLVoidResultFromResultAndError
+ _PLiCloudDriveFileProviderBundleID
+ _PLiCloudDriveFileProviderManagedBundleID
+ __48-[PLDelayedActionTimer afterDelay:performBlock:]_block_invoke.19
+ __48-[PLDelayedActionTimer afterDelay:performBlock:]_block_invoke.24
+ __48-[PLDelayedActionTimer afterDelay:performBlock:]_block_invoke_2.25
+ __52-[PLAutoBindingProxyFactory _connectionInterrupted:]_block_invoke.18
+ __55-[PLAutoBindingProxyFactory _attemptBindToPhotoLibrary]_block_invoke.16
+ __62-[PLNonBindingAssetsdPhotoKitClient sendChangesRequest:error:]_block_invoke.10
+ __62-[PLNonBindingAssetsdPhotoKitClient sendChangesRequest:reply:]_block_invoke.4
+ __65-[PLNonBindingAssetsdPhotoKitAddClient sendChangesRequest:error:]_block_invoke.10
+ __65-[PLNonBindingAssetsdPhotoKitAddClient sendChangesRequest:reply:]_block_invoke.4
+ __70-[PLAssetsdLibraryInternalClient signalAvailabilityWithChanges:error:]_block_invoke.109
+ __73-[PLPrimitiveAssetsdClient sendDaemonJob:shouldRunSerially:replyHandler:]_block_invoke.90
+ __81-[PLAssetsdDebugClient requestSearchDebugInformationForAssetUUID:redacted:error:]_block_invoke.60
+ __83-[PLAssetsdCloudClient computeStableHashesOfAsset:synchronously:completionHandler:]_block_invoke.45
+ __83-[PLAssetsdCloudClient computeStableHashesOfAsset:synchronously:completionHandler:]_block_invoke.49
+ __83-[PLAssetsdCloudClient computeStableHashesOfAsset:synchronously:completionHandler:]_block_invoke.50
+ __83-[PLAssetsdCloudClient computeStableHashesOfAsset:synchronously:completionHandler:]_block_invoke.51
+ __Block_byref_object_copy_.11101
+ __Block_byref_object_copy_.11674
+ __Block_byref_object_copy_.11833
+ __Block_byref_object_copy_.11889
+ __Block_byref_object_copy_.11936
+ __Block_byref_object_copy_.11987
+ __Block_byref_object_copy_.12225
+ __Block_byref_object_copy_.1475
+ __Block_byref_object_copy_.1591
+ __Block_byref_object_copy_.2151
+ __Block_byref_object_copy_.3164
+ __Block_byref_object_copy_.3345
+ __Block_byref_object_copy_.3418
+ __Block_byref_object_copy_.3527
+ __Block_byref_object_copy_.4799
+ __Block_byref_object_copy_.5383
+ __Block_byref_object_copy_.5626
+ __Block_byref_object_copy_.5949
+ __Block_byref_object_copy_.6274
+ __Block_byref_object_copy_.6455
+ __Block_byref_object_copy_.7086
+ __Block_byref_object_copy_.7933
+ __Block_byref_object_copy_.8920
+ __Block_byref_object_copy_.8962
+ __Block_byref_object_copy_.9476
+ __Block_byref_object_copy_.960
+ __Block_byref_object_dispose_.11102
+ __Block_byref_object_dispose_.11675
+ __Block_byref_object_dispose_.11834
+ __Block_byref_object_dispose_.11890
+ __Block_byref_object_dispose_.11937
+ __Block_byref_object_dispose_.11988
+ __Block_byref_object_dispose_.12226
+ __Block_byref_object_dispose_.1476
+ __Block_byref_object_dispose_.1592
+ __Block_byref_object_dispose_.2152
+ __Block_byref_object_dispose_.3165
+ __Block_byref_object_dispose_.3346
+ __Block_byref_object_dispose_.3419
+ __Block_byref_object_dispose_.3528
+ __Block_byref_object_dispose_.4800
+ __Block_byref_object_dispose_.5384
+ __Block_byref_object_dispose_.5627
+ __Block_byref_object_dispose_.5950
+ __Block_byref_object_dispose_.6275
+ __Block_byref_object_dispose_.6456
+ __Block_byref_object_dispose_.7087
+ __Block_byref_object_dispose_.7934
+ __Block_byref_object_dispose_.8921
+ __Block_byref_object_dispose_.8963
+ __Block_byref_object_dispose_.9477
+ __Block_byref_object_dispose_.961
+ __OBJC_$_CLASS_METHODS_PLXPCLibraryToken
+ __OBJC_$_CLASS_PROP_LIST_PLXPCLibraryToken
+ __OBJC_$_INSTANCE_METHODS_PLAssetsdClientState
+ __OBJC_$_INSTANCE_METHODS_PLNonBindingAssetsdPhotoKitAddClient
+ __OBJC_$_INSTANCE_METHODS_PLNonBindingAssetsdPhotoKitClient
+ __OBJC_$_INSTANCE_METHODS_PLPrimitiveAssetsdClient
+ __OBJC_$_INSTANCE_METHODS_PLXPCLibraryToken
+ __OBJC_$_INSTANCE_VARIABLES_PLAssetsdClientState
+ __OBJC_$_INSTANCE_VARIABLES_PLNonBindingAssetsdPhotoKitAddClient
+ __OBJC_$_INSTANCE_VARIABLES_PLNonBindingAssetsdPhotoKitClient
+ __OBJC_$_INSTANCE_VARIABLES_PLPrimitiveAssetsdClient
+ __OBJC_$_INSTANCE_VARIABLES_PLXPCLibraryToken
+ __OBJC_$_PROP_LIST_PLXPCLibraryToken
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PLAssetsdNonBindingPhotoKitServiceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PLAssetsdNonBindingPhotoKitServiceProtocol
+ __OBJC_$_PROTOCOL_REFS_PLAssetsdNonBindingPhotoKitServiceProtocol
+ __OBJC_CLASS_PROTOCOLS_$_PLNonBindingAssetsdPhotoKitAddClient
+ __OBJC_CLASS_PROTOCOLS_$_PLNonBindingAssetsdPhotoKitClient
+ __OBJC_CLASS_PROTOCOLS_$_PLXPCLibraryToken
+ __OBJC_CLASS_RO_$_PLAssetsdClientState
+ __OBJC_CLASS_RO_$_PLNonBindingAssetsdPhotoKitAddClient
+ __OBJC_CLASS_RO_$_PLNonBindingAssetsdPhotoKitClient
+ __OBJC_CLASS_RO_$_PLPrimitiveAssetsdClient
+ __OBJC_CLASS_RO_$_PLXPCLibraryToken
+ __OBJC_LABEL_PROTOCOL_$_PLAssetsdNonBindingPhotoKitServiceProtocol
+ __OBJC_METACLASS_RO_$_PLAssetsdClientState
+ __OBJC_METACLASS_RO_$_PLNonBindingAssetsdPhotoKitAddClient
+ __OBJC_METACLASS_RO_$_PLNonBindingAssetsdPhotoKitClient
+ __OBJC_METACLASS_RO_$_PLPrimitiveAssetsdClient
+ __OBJC_METACLASS_RO_$_PLXPCLibraryToken
+ __OBJC_PROTOCOL_$_PLAssetsdNonBindingPhotoKitServiceProtocol
+ ___115+[PLLibraryServicesOperation operationWithName:libraryServicesManager:requiredState:parentProgress:executionBlock:]_block_invoke
+ ___30-[PLDelayedActionTimer cancel]_block_invoke
+ ___33-[PLDelayedActionTimer isRunning]_block_invoke
+ ___35-[PLDelayedActionTimer description]_block_invoke
+ ___37-[PLDelayedActionTimer timeRemaining]_block_invoke
+ ___38-[PLPrimitiveAssetsdClient demoClient]_block_invoke
+ ___38-[PLPrimitiveAssetsdClient syncClient]_block_invoke
+ ___39-[PLPrimitiveAssetsdClient cloudClient]_block_invoke
+ ___39-[PLPrimitiveAssetsdClient debugClient]_block_invoke
+ ___41-[PLPrimitiveAssetsdClient libraryClient]_block_invoke
+ ___42-[PLPrimitiveAssetsdClient photoKitClient]_block_invoke
+ ___42-[PLPrimitiveAssetsdClient resourceClient]_block_invoke
+ ___43-[PLPrimitiveAssetsdClient migrationClient]_block_invoke
+ ___45-[PLPrimitiveAssetsdClient diagnosticsClient]_block_invoke
+ ___45-[PLPrimitiveAssetsdClient photoKitAddClient]_block_invoke
+ ___46-[PLPrimitiveAssetsdClient notificationClient]_block_invoke
+ ___47-[PLPrimitiveAssetsdClient cloudInternalClient]_block_invoke
+ ___48-[PLDelayedActionTimer afterDelay:performBlock:]_block_invoke_2
+ ___48-[PLPrimitiveAssetsdClient privacySupportClient]_block_invoke
+ ___49-[PLAssetsdClient _isSecondXPCConnectionDisabled]_block_invoke
+ ___49-[PLPrimitiveAssetsdClient libraryInternalClient]_block_invoke
+ ___49-[PLPrimitiveAssetsdClient nonBindingDebugClient]_block_invoke
+ ___50-[PLPrimitiveAssetsdClient resourceInternalClient]_block_invoke
+ ___51-[PLPrimitiveAssetsdClient libraryManagementClient]_block_invoke
+ ___51-[PLPrimitiveAssetsdClient resourceWriteOnlyClient]_block_invoke
+ ___52-[PLPrimitiveAssetsdClient nonBindingPhotoKitClient]_block_invoke
+ ___54-[PLPrimitiveAssetsdClient resourceAvailabilityClient]_block_invoke
+ ___55-[PLPrimitiveAssetsdClient nonBindingPhotoKitAddClient]_block_invoke
+ ___58-[PLPrimitiveAssetsdClient systemLibraryURLReadOnlyClient]_block_invoke
+ ___61-[PLAssetsdClientSandboxExtensions consumeSandboxExtensions:]_block_invoke_2
+ ___62-[PLNonBindingAssetsdPhotoKitClient sendChangesRequest:error:]_block_invoke
+ ___62-[PLNonBindingAssetsdPhotoKitClient sendChangesRequest:reply:]_block_invoke
+ ___63-[PLPrimitiveAssetsdClient waitUntilConnectionSendsAllMessages]_block_invoke
+ ___64-[PLAssetsdClientSandboxExtensions _stopUsingSecurityScopedURLs]_block_invoke
+ ___65-[PLNonBindingAssetsdPhotoKitAddClient sendChangesRequest:error:]_block_invoke
+ ___65-[PLNonBindingAssetsdPhotoKitAddClient sendChangesRequest:reply:]_block_invoke
+ ___69-[PLPrimitiveAssetsdClient _updateLibraryStateConnectionInterrupted:]_block_invoke
+ ___70-[PLAssetsdLibraryInternalClient signalAvailabilityWithChanges:error:]_block_invoke
+ ___73-[PLPrimitiveAssetsdClient sendDaemonJob:shouldRunSerially:replyHandler:]_block_invoke
+ ___73-[PLPrimitiveAssetsdClient sendDaemonJob:shouldRunSerially:replyHandler:]_block_invoke_2
+ ___81-[PLAssetsdDebugClient requestSearchDebugInformationForAssetUUID:redacted:error:]_block_invoke
+ ___83-[PLAssetsdCloudClient computeStableHashesOfAsset:synchronously:completionHandler:]_block_invoke
+ ___PLIsImagePlaygroundApp_block_invoke
+ ___PLIsMacPhotosApp_block_invoke
+ ___PLSearchBackendFeedbackDiagnosticsGetLog_block_invoke
+ ___PLSearchBackendIndexEntityResultGetLog_block_invoke
+ ___block_descriptor_40_e8_32s_e15_"NSString"8?0l
+ ___block_descriptor_40_e8_32s_e5_B8?0l
+ ___block_descriptor_48_e8_32s40w_e5_v8?0l
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0l
+ ___copy_helper_block_e8_32s40b48w
+ ___destroy_helper_block_e8_32s40s48w
+ __block_literal_global.1051
+ __block_literal_global.1067
+ __block_literal_global.10808
+ __block_literal_global.11107
+ __block_literal_global.11352
+ __block_literal_global.11454
+ __block_literal_global.11567
+ __block_literal_global.11989
+ __block_literal_global.120.2570
+ __block_literal_global.1220
+ __block_literal_global.12204
+ __block_literal_global.123.2573
+ __block_literal_global.1235
+ __block_literal_global.12592
+ __block_literal_global.127
+ __block_literal_global.12713
+ __block_literal_global.129.2577
+ __block_literal_global.129.3903
+ __block_literal_global.134.3911
+ __block_literal_global.1365
+ __block_literal_global.144.5974
+ __block_literal_global.148
+ __block_literal_global.153.3928
+ __block_literal_global.158
+ __block_literal_global.162.2592
+ __block_literal_global.1642
+ __block_literal_global.166.5952
+ __block_literal_global.168.3937
+ __block_literal_global.173
+ __block_literal_global.177.5944
+ __block_literal_global.178
+ __block_literal_global.183.3942
+ __block_literal_global.189.6352
+ __block_literal_global.191.3947
+ __block_literal_global.192.12057
+ __block_literal_global.193
+ __block_literal_global.195.6353
+ __block_literal_global.196.3952
+ __block_literal_global.2.6141
+ __block_literal_global.201.3954
+ __block_literal_global.202.6345
+ __block_literal_global.206.4815
+ __block_literal_global.211
+ __block_literal_global.216.3959
+ __block_literal_global.221
+ __block_literal_global.223
+ __block_literal_global.2237
+ __block_literal_global.2249
+ __block_literal_global.228.3964
+ __block_literal_global.234.3966
+ __block_literal_global.24.2220
+ __block_literal_global.24.2525
+ __block_literal_global.2509
+ __block_literal_global.251
+ __block_literal_global.256
+ __block_literal_global.259
+ __block_literal_global.26.2214
+ __block_literal_global.267.3975
+ __block_literal_global.269
+ __block_literal_global.27.6106
+ __block_literal_global.270.2630
+ __block_literal_global.280
+ __block_literal_global.282.3990
+ __block_literal_global.286
+ __block_literal_global.3.2512
+ __block_literal_global.30.2531
+ __block_literal_global.301
+ __block_literal_global.309
+ __block_literal_global.318.4013
+ __block_literal_global.3186
+ __block_literal_global.3292
+ __block_literal_global.33.6100
+ __block_literal_global.3361
+ __block_literal_global.3428
+ __block_literal_global.36.6094
+ __block_literal_global.3635
+ __block_literal_global.366.4973
+ __block_literal_global.3896
+ __block_literal_global.39.2536
+ __block_literal_global.39.3618
+ __block_literal_global.39.6088
+ __block_literal_global.396
+ __block_literal_global.399
+ __block_literal_global.4120
+ __block_literal_global.46.641
+ __block_literal_global.48.6080
+ __block_literal_global.4968
+ __block_literal_global.507
+ __block_literal_global.51.2542
+ __block_literal_global.54.3597
+ __block_literal_global.5571
+ __block_literal_global.56.6070
+ __block_literal_global.56.7697
+ __block_literal_global.5618
+ __block_literal_global.6.1039
+ __block_literal_global.6.2515
+ __block_literal_global.6.6513
+ __block_literal_global.6152
+ __block_literal_global.6269
+ __block_literal_global.638
+ __block_literal_global.6385
+ __block_literal_global.65.12590
+ __block_literal_global.651
+ __block_literal_global.6523
+ __block_literal_global.6696
+ __block_literal_global.7093
+ __block_literal_global.72.2549
+ __block_literal_global.725
+ __block_literal_global.7735
+ __block_literal_global.78.2552
+ __block_literal_global.7950
+ __block_literal_global.81.2555
+ __block_literal_global.8567
+ __block_literal_global.8886
+ __block_literal_global.9.6514
+ __block_literal_global.90.3561
+ __block_literal_global.92.3557
+ __block_literal_global.94.6251
+ __block_literal_global.9652
+ _dispatch_source_set_cancel_handler
+ _isSecondXPCConnectionDisabled.sIsSecondConnectionDisabled
+ _isSecondXPCConnectionDisabled.sOnceToken
+ _objc_msgSend$PhotoKitAddService_applyChangesRequest:libraryToken:reply:
+ _objc_msgSend$PhotoKitService_applyChangesRequest:libraryToken:reply:
+ _objc_msgSend$_isSecondXPCConnectionDisabled
+ _objc_msgSend$_primitiveClientForCurrentQoS
+ _objc_msgSend$clientOptions
+ _objc_msgSend$clientState
+ _objc_msgSend$cloudClient
+ _objc_msgSend$computeStableHashesOfAsset:synchronously:completionHandler:
+ _objc_msgSend$computeStableHashesOfAssetWithObjectURI:synchronously:reply:
+ _objc_msgSend$debugClient
+ _objc_msgSend$decodeObjectOfClasses:forKey:
+ _objc_msgSend$demoClient
+ _objc_msgSend$diagnosticsClient
+ _objc_msgSend$initWithPhotoLibraryURL:clientState:
+ _objc_msgSend$initWithQueue:proxyCreating:libraryURL:
+ _objc_msgSend$initWithQueue:proxyCreating:proxyGetter:clientState:
+ _objc_msgSend$initWithURL:sandboxExtension:clientOptions:
+ _objc_msgSend$isOpen
+ _objc_msgSend$migrationClient
+ _objc_msgSend$nonBindingDebugClient
+ _objc_msgSend$nonBindingPhotoKitAddClient
+ _objc_msgSend$nonBindingPhotoKitClient
+ _objc_msgSend$notificationClient
+ _objc_msgSend$photoKitAddClient
+ _objc_msgSend$photoKitClient
+ _objc_msgSend$photosLibraryTombstoneExtension
+ _objc_msgSend$resourceAvailabilityClient
+ _objc_msgSend$resourceInternalClient
+ _objc_msgSend$resourceWriteOnlyClient
+ _objc_msgSend$searchAttributesForAssetWithUUID:redacted:reply:
+ _objc_msgSend$sendDaemonJob:shouldRunSerially:replyHandler:
+ _objc_msgSend$signalAvailabilityWithChanges:reply:
+ _objc_msgSend$syncClient
+ _objc_msgSend$waitUntilConnectionSendsAllMessages
+ _sClientOptionsKey
+ _sSandboxExtensionKey
+ _sUrlKey
+ sharedInstance.onceToken.8885
- +[PLAutoBindingProxyFactory clientToServiceSandboxExtensionForURL:]
- +[PLLibraryServicesOperation operationWithName:requiredState:parentProgress:execution:]
- -[PLAssetsdBaseClient initWithQueue:proxyCreating:proxyGetter:]
- -[PLAssetsdClient _setupClientClass:proxyGetter:options:]
- -[PLAssetsdClient _updateLibraryStateConnectionInterrupted:]
- -[PLAssetsdClient dealloc]
- -[PLAssetsdDebugClient requestSearchDebugInformationForAssetUUID:error:]
- -[PLAssetsdLibraryClient .cxx_destruct]
- -[PLAssetsdLibraryClient initWithQueue:proxyCreating:proxyGetter:sandboxExtensions:]
- -[PLAssetsdLibraryClient isOpened]
- -[PLAssetsdResourceClient initWithQueue:proxyCreating:proxyGetter:]
- -[PLDelayedActionTimer targetQueue]
- -[PLLibraryServicesOperation _safeRemoveCancellationObserver]
- -[PLLibraryServicesOperation cancellationBlock]
- -[PLLibraryServicesOperation dealloc]
- -[PLLibraryServicesOperation init]
- -[PLLibraryServicesOperation observeValueForKeyPath:ofObject:change:context:]
- -[PLLibraryServicesOperation setCancellationBlock:]
- GCC_except_table1001
- GCC_except_table1009
- GCC_except_table1012
- GCC_except_table1015
- GCC_except_table1018
- GCC_except_table1022
- GCC_except_table1026
- GCC_except_table1029
- GCC_except_table1032
- GCC_except_table1035
- GCC_except_table1038
- GCC_except_table1041
- GCC_except_table1045
- GCC_except_table1078
- GCC_except_table1080
- GCC_except_table1126
- GCC_except_table1445
- GCC_except_table1602
- GCC_except_table1609
- GCC_except_table1644
- GCC_except_table1655
- GCC_except_table1675
- GCC_except_table1691
- GCC_except_table1696
- GCC_except_table1699
- GCC_except_table1702
- GCC_except_table1728
- GCC_except_table1730
- GCC_except_table1733
- GCC_except_table1736
- GCC_except_table1739
- GCC_except_table1747
- GCC_except_table1750
- GCC_except_table1753
- GCC_except_table1756
- GCC_except_table1772
- GCC_except_table1776
- GCC_except_table1779
- GCC_except_table1782
- GCC_except_table1785
- GCC_except_table1790
- GCC_except_table1793
- GCC_except_table1796
- GCC_except_table1799
- GCC_except_table1813
- GCC_except_table1821
- GCC_except_table1945
- GCC_except_table2024
- GCC_except_table2137
- GCC_except_table2142
- GCC_except_table2143
- GCC_except_table2145
- GCC_except_table2148
- GCC_except_table2275
- GCC_except_table230
- GCC_except_table2345
- GCC_except_table2383
- GCC_except_table2384
- GCC_except_table239
- GCC_except_table2414
- GCC_except_table2419
- GCC_except_table242
- GCC_except_table2422
- GCC_except_table2425
- GCC_except_table2430
- GCC_except_table2433
- GCC_except_table244
- GCC_except_table2445
- GCC_except_table2448
- GCC_except_table2451
- GCC_except_table246
- GCC_except_table2475
- GCC_except_table2507
- GCC_except_table251
- GCC_except_table2510
- GCC_except_table2512
- GCC_except_table2517
- GCC_except_table2520
- GCC_except_table2523
- GCC_except_table2526
- GCC_except_table2530
- GCC_except_table2534
- GCC_except_table2543
- GCC_except_table2563
- GCC_except_table2567
- GCC_except_table257
- GCC_except_table2571
- GCC_except_table2575
- GCC_except_table2579
- GCC_except_table2582
- GCC_except_table2586
- GCC_except_table2590
- GCC_except_table2594
- GCC_except_table2598
- GCC_except_table260
- GCC_except_table2602
- GCC_except_table2606
- GCC_except_table2609
- GCC_except_table2614
- GCC_except_table2616
- GCC_except_table2617
- GCC_except_table2622
- GCC_except_table2624
- GCC_except_table2629
- GCC_except_table2641
- GCC_except_table2644
- GCC_except_table2647
- GCC_except_table265
- GCC_except_table2670
- GCC_except_table268
- GCC_except_table273
- GCC_except_table2752
- GCC_except_table2755
- GCC_except_table276
- GCC_except_table279
- GCC_except_table2865
- GCC_except_table2877
- GCC_except_table2879
- GCC_except_table288
- GCC_except_table2883
- GCC_except_table2885
- GCC_except_table2903
- GCC_except_table291
- GCC_except_table2912
- GCC_except_table2916
- GCC_except_table299
- GCC_except_table3062
- GCC_except_table3067
- GCC_except_table307
- GCC_except_table3070
- GCC_except_table3073
- GCC_except_table310
- GCC_except_table313
- GCC_except_table3157
- GCC_except_table3165
- GCC_except_table318
- GCC_except_table3180
- GCC_except_table321
- GCC_except_table3342
- GCC_except_table3352
- GCC_except_table3357
- GCC_except_table3361
- GCC_except_table3368
- GCC_except_table3422
- GCC_except_table3425
- GCC_except_table3431
- GCC_except_table3437
- GCC_except_table3441
- GCC_except_table3445
- GCC_except_table3449
- GCC_except_table3453
- GCC_except_table3476
- GCC_except_table3481
- GCC_except_table3490
- GCC_except_table3503
- GCC_except_table3522
- GCC_except_table3530
- GCC_except_table3537
- GCC_except_table3541
- GCC_except_table3547
- GCC_except_table3552
- GCC_except_table3555
- GCC_except_table3558
- GCC_except_table3562
- GCC_except_table3565
- GCC_except_table3571
- GCC_except_table3576
- GCC_except_table3579
- GCC_except_table3583
- GCC_except_table3586
- GCC_except_table3589
- GCC_except_table3592
- GCC_except_table3595
- GCC_except_table3599
- GCC_except_table3603
- GCC_except_table3619
- GCC_except_table3664
- GCC_except_table3690
- GCC_except_table3691
- GCC_except_table3692
- GCC_except_table3694
- GCC_except_table3696
- GCC_except_table3698
- GCC_except_table3699
- GCC_except_table3709
- GCC_except_table378
- GCC_except_table379
- GCC_except_table400
- GCC_except_table406
- GCC_except_table413
- GCC_except_table426
- GCC_except_table475
- GCC_except_table480
- GCC_except_table483
- GCC_except_table486
- GCC_except_table489
- GCC_except_table494
- GCC_except_table501
- GCC_except_table504
- GCC_except_table508
- GCC_except_table512
- GCC_except_table518
- GCC_except_table521
- GCC_except_table527
- GCC_except_table531
- GCC_except_table593
- GCC_except_table652
- GCC_except_table686
- GCC_except_table694
- GCC_except_table697
- GCC_except_table703
- GCC_except_table707
- GCC_except_table710
- GCC_except_table713
- GCC_except_table716
- GCC_except_table717
- GCC_except_table874
- GCC_except_table882
- GCC_except_table885
- GCC_except_table888
- GCC_except_table894
- GCC_except_table897
- GCC_except_table900
- GCC_except_table903
- GCC_except_table906
- GCC_except_table909
- GCC_except_table912
- GCC_except_table930
- GCC_except_table933
- GCC_except_table937
- GCC_except_table941
- GCC_except_table944
- GCC_except_table947
- GCC_except_table950
- GCC_except_table953
- GCC_except_table956
- GCC_except_table959
- GCC_except_table962
- GCC_except_table965
- GCC_except_table968
- GCC_except_table971
- GCC_except_table974
- GCC_except_table982
- GCC_except_table986
- GCC_except_table992
- GCC_except_table995
- GCC_except_table998
- OBJC_IVAR_$_PLAssetsdClient._autoBindingProxyFactory
- OBJC_IVAR_$_PLAssetsdClient._cloudClient
- OBJC_IVAR_$_PLAssetsdClient._cloudInternalClient
- OBJC_IVAR_$_PLAssetsdClient._connection
- OBJC_IVAR_$_PLAssetsdClient._debugClient
- OBJC_IVAR_$_PLAssetsdClient._demoClient
- OBJC_IVAR_$_PLAssetsdClient._diagnosticsClient
- OBJC_IVAR_$_PLAssetsdClient._isolationQueue
- OBJC_IVAR_$_PLAssetsdClient._libraryClient
- OBJC_IVAR_$_PLAssetsdClient._libraryInternalClient
- OBJC_IVAR_$_PLAssetsdClient._libraryManagementClient
- OBJC_IVAR_$_PLAssetsdClient._migrationClient
- OBJC_IVAR_$_PLAssetsdClient._nonBindingDebugClient
- OBJC_IVAR_$_PLAssetsdClient._notificationClient
- OBJC_IVAR_$_PLAssetsdClient._photoKitAddClient
- OBJC_IVAR_$_PLAssetsdClient._photoKitClient
- OBJC_IVAR_$_PLAssetsdClient._privacySupportClient
- OBJC_IVAR_$_PLAssetsdClient._resourceAvailabilityClient
- OBJC_IVAR_$_PLAssetsdClient._resourceClient
- OBJC_IVAR_$_PLAssetsdClient._resourceInternalClient
- OBJC_IVAR_$_PLAssetsdClient._resourceWriteOnlyClient
- OBJC_IVAR_$_PLAssetsdClient._sandboxExtensions
- OBJC_IVAR_$_PLAssetsdClient._syncClient
- OBJC_IVAR_$_PLAssetsdClient._systemLibraryURLReadOnlyClient
- OBJC_IVAR_$_PLAssetsdClientSandboxExtensions._securityScopedURLs
- OBJC_IVAR_$_PLAssetsdLibraryClient._isOpen
- OBJC_IVAR_$_PLAssetsdLibraryClient._sandboxExtensions
- OBJC_IVAR_$_PLLibraryServicesOperation._cancellationBlock
- OBJC_IVAR_$_PLLibraryServicesOperation._cancellationBlockCalled
- OBJC_IVAR_$_PLLibraryServicesOperation._cancellationLock
- PLIsPhotosApp.didCheck
- PLIsPhotosApp.isPhotosApp
- PL_gKTXFileIdentifier.11442
- _NSKeyValueChangeNewKey
- _NSKeyValueChangeOldKey
- _OBJC_$_PROP_LIST_PLPhotoLibraryPathManagerCore.633
- _PLIsPhotosApp
- _PLMacPlatformLibraryServicesOperationNameCheckForAutoCreateSPL
- __52-[PLAutoBindingProxyFactory _connectionInterrupted:]_block_invoke.23
- __55-[PLAutoBindingProxyFactory _attemptBindToPhotoLibrary]_block_invoke.21
- __64-[PLAssetsdClient sendDaemonJob:shouldRunSerially:replyHandler:]_block_invoke.93
- __72-[PLAssetsdDebugClient requestSearchDebugInformationForAssetUUID:error:]_block_invoke.60
- __83-[PLAssetsdCloudClient computeFingerPrintsOfAsset:synchronously:completionHandler:]_block_invoke.45
- __83-[PLAssetsdCloudClient computeFingerPrintsOfAsset:synchronously:completionHandler:]_block_invoke.49
- __83-[PLAssetsdCloudClient computeFingerPrintsOfAsset:synchronously:completionHandler:]_block_invoke.50
- __83-[PLAssetsdCloudClient computeFingerPrintsOfAsset:synchronously:completionHandler:]_block_invoke.51
- __Block_byref_object_copy_.10937
- __Block_byref_object_copy_.11508
- __Block_byref_object_copy_.11681
- __Block_byref_object_copy_.11737
- __Block_byref_object_copy_.11784
- __Block_byref_object_copy_.11838
- __Block_byref_object_copy_.12077
- __Block_byref_object_copy_.1479
- __Block_byref_object_copy_.1595
- __Block_byref_object_copy_.2156
- __Block_byref_object_copy_.3170
- __Block_byref_object_copy_.3352
- __Block_byref_object_copy_.3424
- __Block_byref_object_copy_.3529
- __Block_byref_object_copy_.4929
- __Block_byref_object_copy_.5516
- __Block_byref_object_copy_.5758
- __Block_byref_object_copy_.6060
- __Block_byref_object_copy_.6376
- __Block_byref_object_copy_.6541
- __Block_byref_object_copy_.7082
- __Block_byref_object_copy_.7873
- __Block_byref_object_copy_.8854
- __Block_byref_object_copy_.975
- __Block_byref_object_dispose_.10938
- __Block_byref_object_dispose_.11509
- __Block_byref_object_dispose_.11682
- __Block_byref_object_dispose_.11738
- __Block_byref_object_dispose_.11785
- __Block_byref_object_dispose_.11839
- __Block_byref_object_dispose_.12078
- __Block_byref_object_dispose_.1480
- __Block_byref_object_dispose_.1596
- __Block_byref_object_dispose_.2157
- __Block_byref_object_dispose_.3171
- __Block_byref_object_dispose_.3353
- __Block_byref_object_dispose_.3425
- __Block_byref_object_dispose_.3530
- __Block_byref_object_dispose_.4930
- __Block_byref_object_dispose_.5517
- __Block_byref_object_dispose_.5759
- __Block_byref_object_dispose_.6061
- __Block_byref_object_dispose_.6377
- __Block_byref_object_dispose_.6542
- __Block_byref_object_dispose_.7083
- __Block_byref_object_dispose_.7874
- __Block_byref_object_dispose_.8855
- __Block_byref_object_dispose_.976
- __OBJC_$_INSTANCE_VARIABLES_PLAssetsdLibraryClient
- ___29-[PLAssetsdClient demoClient]_block_invoke
- ___29-[PLAssetsdClient syncClient]_block_invoke
- ___30-[PLAssetsdClient cloudClient]_block_invoke
- ___30-[PLAssetsdClient debugClient]_block_invoke
- ___32-[PLAssetsdClient libraryClient]_block_invoke
- ___33-[PLAssetsdClient photoKitClient]_block_invoke
- ___33-[PLAssetsdClient resourceClient]_block_invoke
- ___34-[PLAssetsdClient migrationClient]_block_invoke
- ___36-[PLAssetsdClient diagnosticsClient]_block_invoke
- ___36-[PLAssetsdClient photoKitAddClient]_block_invoke
- ___37-[PLAssetsdClient notificationClient]_block_invoke
- ___38-[PLAssetsdClient cloudInternalClient]_block_invoke
- ___39-[PLAssetsdClient privacySupportClient]_block_invoke
- ___40-[PLAssetsdClient libraryInternalClient]_block_invoke
- ___40-[PLAssetsdClient nonBindingDebugClient]_block_invoke
- ___41-[PLAssetsdClient resourceInternalClient]_block_invoke
- ___42-[PLAssetsdClient libraryManagementClient]_block_invoke
- ___42-[PLAssetsdClient resourceWriteOnlyClient]_block_invoke
- ___45-[PLAssetsdClient resourceAvailabilityClient]_block_invoke
- ___49-[PLAssetsdClient systemLibraryURLReadOnlyClient]_block_invoke
- ___51-[PLLibraryServicesOperation setCancellationBlock:]_block_invoke
- ___54-[PLAssetsdClient waitUntilConnectionSendsAllMessages]_block_invoke
- ___60-[PLAssetsdClient _updateLibraryStateConnectionInterrupted:]_block_invoke
- ___64-[PLAssetsdClient sendDaemonJob:shouldRunSerially:replyHandler:]_block_invoke
- ___64-[PLAssetsdClient sendDaemonJob:shouldRunSerially:replyHandler:]_block_invoke_2
- ___72-[PLAssetsdDebugClient requestSearchDebugInformationForAssetUUID:error:]_block_invoke
- ___77-[PLLibraryServicesOperation observeValueForKeyPath:ofObject:change:context:]_block_invoke
- ___83-[PLAssetsdCloudClient computeFingerPrintsOfAsset:synchronously:completionHandler:]_block_invoke
- ___PLIsPhotosApp_block_invoke
- ___block_descriptor_64_e8_32s40s48bs56w_e5_v8?0l
- ___copy_helper_block_e8_32s40s48b56w
- ___destroy_helper_block_e8_32s40s48s56w
- __block_literal_global.103
- __block_literal_global.10652
- __block_literal_global.1066
- __block_literal_global.108.3883
- __block_literal_global.1082
- __block_literal_global.10943
- __block_literal_global.11189
- __block_literal_global.11290
- __block_literal_global.11402
- __block_literal_global.116
- __block_literal_global.11840
- __block_literal_global.120.2577
- __block_literal_global.12056
- __block_literal_global.121
- __block_literal_global.1223
- __block_literal_global.123.2580
- __block_literal_global.1238
- __block_literal_global.12445
- __block_literal_global.12565
- __block_literal_global.126.3894
- __block_literal_global.129.2584
- __block_literal_global.131
- __block_literal_global.136
- __block_literal_global.1368
- __block_literal_global.141.3899
- __block_literal_global.144.6083
- __block_literal_global.146.3901
- __block_literal_global.151.3906
- __block_literal_global.157.3911
- __block_literal_global.162.2599
- __block_literal_global.1646
- __block_literal_global.174.3930
- __block_literal_global.177.6055
- __block_literal_global.179
- __block_literal_global.182.3934
- __block_literal_global.190
- __block_literal_global.192.11908
- __block_literal_global.192.3944
- __block_literal_global.2.6249
- __block_literal_global.203
- __block_literal_global.205.3951
- __block_literal_global.224
- __block_literal_global.2244
- __block_literal_global.2256
- __block_literal_global.232
- __block_literal_global.24.2227
- __block_literal_global.24.2532
- __block_literal_global.241
- __block_literal_global.2516
- __block_literal_global.26.2221
- __block_literal_global.27.6214
- __block_literal_global.270.2637
- __block_literal_global.287
- __block_literal_global.3.2519
- __block_literal_global.30.2538
- __block_literal_global.3192
- __block_literal_global.3297
- __block_literal_global.33.6208
- __block_literal_global.3368
- __block_literal_global.3434
- __block_literal_global.36.6202
- __block_literal_global.3636
- __block_literal_global.366.5110
- __block_literal_global.3833
- __block_literal_global.39.2543
- __block_literal_global.39.3619
- __block_literal_global.39.6196
- __block_literal_global.4.6606
- __block_literal_global.4253
- __block_literal_global.430
- __block_literal_global.46.658
- __block_literal_global.48.6188
- __block_literal_global.51.2549
- __block_literal_global.5105
- __block_literal_global.52
- __block_literal_global.54.3598
- __block_literal_global.54.3843
- __block_literal_global.56.6178
- __block_literal_global.56.7641
- __block_literal_global.561
- __block_literal_global.5703
- __block_literal_global.5750
- __block_literal_global.59.3854
- __block_literal_global.6.1054
- __block_literal_global.6.2522
- __block_literal_global.6.6440
- __block_literal_global.6.6595
- __block_literal_global.6260
- __block_literal_global.6439
- __block_literal_global.6475
- __block_literal_global.65.12443
- __block_literal_global.6605
- __block_literal_global.668
- __block_literal_global.6693
- __block_literal_global.7089
- __block_literal_global.72.2556
- __block_literal_global.73
- __block_literal_global.742
- __block_literal_global.7674
- __block_literal_global.78.2559
- __block_literal_global.78.3866
- __block_literal_global.7890
- __block_literal_global.81.2562
- __block_literal_global.83.3871
- __block_literal_global.8513
- __block_literal_global.8826
- __block_literal_global.9.6596
- __block_literal_global.90.3562
- __block_literal_global.91
- __block_literal_global.92.3558
- __block_literal_global.93.3875
- __block_literal_global.9488
- __block_literal_global.95.6371
- __block_literal_global.98
- __block_literal_global.99.6354
- _objc_msgSend$_safeRemoveCancellationObserver
- _objc_msgSend$computeFingerPrintsOfAssetWithObjectURI:synchronously:reply:
- _objc_msgSend$initWithDictionary:
- _objc_msgSend$initWithQueue:proxyCreating:proxyGetter:sandboxExtensions:
- _objc_msgSend$searchAttributesForAssetWithUUID:reply:
- _sprintf
- sharedInstance.onceToken.8825
CStrings:
+ "-[PLAssetsdCloudClient computeStableHashesOfAsset:synchronously:completionHandler:]_block_invoke"
+ "-[PLAssetsdDebugClient requestSearchDebugInformationForAssetUUID:redacted:error:]_block_invoke"
+ "-[PLAssetsdLibraryInternalClient signalAvailabilityWithChanges:error:]_block_invoke"
+ "-[PLNonBindingAssetsdPhotoKitAddClient sendChangesRequest:reply:]_block_invoke"
+ "-[PLNonBindingAssetsdPhotoKitClient sendChangesRequest:reply:]_block_invoke"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/Projects/PhotoLibraryServicesCore/Sources/PLTaggedPointer.m"
+ "@\"NSString\"8@?0"
+ "@\"PLAssetsdClientState\""
+ "@\"PLNonBindingAssetsdPhotoKitAddClient\""
+ "@\"PLNonBindingAssetsdPhotoKitClient\""
+ "@\"PLPrimitiveAssetsdClient\""
+ "@\"PLXPCLibraryToken\""
+ "@56@0:8@16@24q32@40@?48"
+ "B8@?0"
+ "Check for auto-create well-known library"
+ "CrashRecovery: Process asset album associativity"
+ "Failed to bind to photo library %@, %@"
+ "LSM is nil, not executing operation %@"
+ "NSString * _Nonnull PLStringFromPLPhotoLibraryCacheSubPathType(PLPhotoLibraryCacheSubPathType)"
+ "NSString * _Nonnull PLStringFromPLPhotoLibraryExternalPathType(PLPhotoLibraryExternalPathType)"
+ "NSString * _Nonnull PLStringFromPLPhotoLibraryInternalPathType(PLPhotoLibraryInternalPathType)"
+ "NSString * _Nonnull PLStringFromPLPhotoLibrarySubPathLeafType(PLPhotoLibrarySubPathLeafType)"
+ "NSString * _Nonnull PLStringFromPLPhotoLibrarySubPathType(PLPhotoLibrarySubPathType)"
+ "PLAssetsdClientState"
+ "PLAssetsdNonBindingPhotoKitServiceProtocol"
+ "PLNonBindingAssetsdPhotoKitAddClient"
+ "PLNonBindingAssetsdPhotoKitClient"
+ "PLPhotosErrorLocaleChanged"
+ "PLPrimitiveAssetsdClient"
+ "PLVoidResult * _Nonnull PLVoidResultFromResultAndError(BOOL, NSError * _Nullable __strong)"
+ "PLXPC Client: computeStableHashesOfAsset:synchronously:completionHandler:"
+ "PLXPC Client: sendChangesRequest:error:"
+ "PLXPC Client: sendChangesRequest:reply:"
+ "PLXPC Client: signalAvailabilityWithChanges:error:"
+ "PLXPCLibraryToken"
+ "PLXPCLibraryToken.m"
+ "PLXPCLibraryToken.url cannot be nil"
+ "PhotoKitAddService_applyChangesRequest:libraryToken:reply:"
+ "PhotoKitService_applyChangesRequest:libraryToken:reply:"
+ "SearchBackendFeedbackDiagnostics"
+ "SearchBackendIndexEntityResult"
+ "Second assetsd XPC connection is disabled due to user default"
+ "Successfully bound to photo library: %@, %@"
+ "T@\"NSData\",R,C,V_sandboxExtension"
+ "T@\"NSDictionary\",R,C,V_clientOptions"
+ "T@\"NSURL\",R,C,V_url"
+ "T@\"PLAssetsdClientState\",R,V_clientState"
+ "T@\"PLNonBindingAssetsdPhotoKitAddClient\",R"
+ "T@\"PLNonBindingAssetsdPhotoKitClient\",R"
+ "Unable to get asset stableHashes because XPC service returned an error. (%@)"
+ "Using high priority assetsd XPC client: %@"
+ "Using low priority assetsd XPC client: %@"
+ "_clientOptions"
+ "_clientState"
+ "_highPriorityClient"
+ "_isSecondXPCConnectionDisabled"
+ "_libraryToken"
+ "_lock_securityScopedURLs"
+ "_lowPriorityClient"
+ "_nonBindingPhotoKitAddClient"
+ "_nonBindingPhotoKitClient"
+ "_primitiveClientForCurrentQoS"
+ "_sandboxExtension"
+ "clientOptions"
+ "clientState"
+ "com.apple.Capture"
+ "com.apple.CarPlayApp"
+ "com.apple.CloudDocs.MobileDocumentsFileProvider"
+ "com.apple.CloudDocs.iCloudDriveFileProvider"
+ "com.apple.CloudDocs.iCloudDriveFileProviderManaged"
+ "com.apple.FileProvider.LocalStorage"
+ "com.apple.GenerativePlaygroundApp"
+ "com.apple.MigrationKit"
+ "com.apple.MobileSMS"
+ "com.apple.Notes"
+ "com.apple.ScreenshotServicesService"
+ "com.apple.Spotlight"
+ "com.apple.Stickers"
+ "com.apple.SurfBoard"
+ "com.apple.camera"
+ "com.apple.camera.CameraMessagesApp"
+ "com.apple.camera.lockscreen"
+ "com.apple.mobileslideshow"
+ "com.apple.mobileslideshow.photospicker"
+ "com.apple.photos.backend.disableSecondXPCConnection"
+ "com.apple.photos.filesPlaceholder"
+ "com.apple.quicklook.extension.previewUI"
+ "com.apple.share.System.add-to-iphoto"
+ "com.apple.sharingd"
+ "com.apple.springboard"
+ "computeStableHashesOfAsset:synchronously:completionHandler:"
+ "computeStableHashesOfAssetWithObjectURI:synchronously:reply:"
+ "decodeObjectOfClasses:forKey:"
+ "error == nil"
+ "ignoring request to cancel inactive PLDelayedActionTimer"
+ "initWithPhotoLibraryURL:clientState:"
+ "initWithQueue:proxyCreating:libraryURL:"
+ "initWithQueue:proxyCreating:proxyGetter:clientState:"
+ "initWithURL:sandboxExtension:clientOptions:"
+ "isOpen"
+ "non-binding PhotoKit client"
+ "non-binding PhotoKitAdd client"
+ "nonBindingPhotoKitAddClient"
+ "nonBindingPhotoKitClient"
+ "operationWithName:libraryServicesManager:requiredState:parentProgress:executionBlock:"
+ "photosLibraryTombstoneExtension"
+ "requestSearchDebugInformationForAssetUUID:redacted:error:"
+ "sandboxExtension"
+ "searchAttributesForAssetWithUUID:redacted:reply:"
+ "signalAvailabilityWithChanges:error:"
+ "signalAvailabilityWithChanges:reply:"
+ "tombstone"
+ "unknown(%ld)"
+ "v32@0:8@\"PLFeatureAvailabilitySignalledChanges\"16@?<v@?B@\"NSError\">24"
+ "v36@0:8@\"NSString\"16B24@?<v@?@\"NSDictionary\">28"
+ "v40@0:8@\"PLXPCObject\"16@\"PLXPCLibraryToken\"24@?<v@?B@\"NSError\">32"
- "-[PLAssetsdCloudClient computeFingerPrintsOfAsset:synchronously:completionHandler:]_block_invoke"
- "-[PLAssetsdDebugClient requestSearchDebugInformationForAssetUUID:error:]_block_invoke"
- ".."
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/Projects/PhotoLibraryServicesCore/Sources/PLTaggedPointer.m"
- "@48@0:8@16q24@32@?40"
- "@?16@0:8"
- "Check for auto-create SPL"
- "Failed to open photo library %@, %@"
- "NSString *PLStringFromPLPhotoLibraryCacheSubPathType(PLPhotoLibraryCacheSubPathType)"
- "NSString *PLStringFromPLPhotoLibraryExternalPathType(PLPhotoLibraryExternalPathType)"
- "NSString *PLStringFromPLPhotoLibraryInternalPathType(PLPhotoLibraryInternalPathType)"
- "NSString *PLStringFromPLPhotoLibrarySubPathLeafType(PLPhotoLibrarySubPathLeafType)"
- "NSString *PLStringFromPLPhotoLibrarySubPathType(PLPhotoLibrarySubPathType)"
- "PLXPC Client: computeFingerPrintsOfAsset:synchronously:completionHandler:"
- "T@\"NSObject<OS_dispatch_queue>\",R,N"
- "T@?,C,N,V_cancellationBlock"
- "Unable to get asset fingerprints because XPC service returned an error. (%@)"
- "_cancellationBlock"
- "_cancellationBlockCalled"
- "_cancellationLock"
- "_safeRemoveCancellationObserver"
- "_securityScopedURLs"
- "add"
- "bindToPhotoLibraryURL:sandboxExtension:withReply:"
- "cancel changed context"
- "cancellationBlock"
- "cancelled"
- "computeFingerPrintsOfAssetWithObjectURI:synchronously:reply:"
- "ignoring request to cancel inactive timer"
- "initWithDictionary:"
- "initWithQueue:proxyCreating:proxyGetter:sandboxExtensions:"
- "isOpened"
- "modify"
- "observeValueForKeyPath:ofObject:change:context:"
- "operationWithName:requiredState:parentProgress:execution:"
- "requestSearchDebugInformationForAssetUUID:error:"
- "searchAttributesForAssetWithUUID:reply:"
- "setCancellationBlock:"
- "targetQueue"
- "v40@0:8@\"NSURL\"16@\"NSData\"24@?<v@?@\"NSError\">32"
- "v48@0:8@16@24@32^v40"

```
