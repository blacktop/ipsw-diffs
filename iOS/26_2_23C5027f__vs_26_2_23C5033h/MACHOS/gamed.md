## gamed

> `/usr/libexec/gamed`

```diff

-820.2.6.0.0
-  __TEXT.__text: 0x2a3c10
-  __TEXT.__auth_stubs: 0x4560
-  __TEXT.__objc_stubs: 0x1a3e0
-  __TEXT.__objc_methlist: 0xdca4
-  __TEXT.__const: 0x17060
+820.2.8.2.1
+  __TEXT.__text: 0x2a5f38
+  __TEXT.__auth_stubs: 0x4570
+  __TEXT.__objc_stubs: 0x1a480
+  __TEXT.__objc_methlist: 0xdd44
+  __TEXT.__const: 0x170e0
   __TEXT.__objc_classname: 0x1d5a
-  __TEXT.__oslogstring: 0x18639
-  __TEXT.__cstring: 0x1b864
-  __TEXT.__objc_methname: 0x22681
-  __TEXT.__objc_methtype: 0x5e68
-  __TEXT.__gcc_except_tab: 0x3558
-  __TEXT.__swift5_typeref: 0x33b4
-  __TEXT.__constg_swiftt: 0x2258
-  __TEXT.__swift5_reflstr: 0x15f9
-  __TEXT.__swift5_fieldmd: 0x1e58
+  __TEXT.__oslogstring: 0x186e9
+  __TEXT.__cstring: 0x1ba44
+  __TEXT.__objc_methname: 0x22801
+  __TEXT.__objc_methtype: 0x5ea7
+  __TEXT.__gcc_except_tab: 0x356c
+  __TEXT.__swift5_typeref: 0x33b8
+  __TEXT.__constg_swiftt: 0x21a8
+  __TEXT.__swift5_reflstr: 0x1659
+  __TEXT.__swift5_fieldmd: 0x1e7c
   __TEXT.__swift5_builtin: 0x12c
   __TEXT.__swift5_assocty: 0x258
   __TEXT.__swift5_proto: 0x3d8
   __TEXT.__swift5_types: 0x26c
-  __TEXT.__swift5_capture: 0xfdc
-  __TEXT.__swift_as_entry: 0x574
-  __TEXT.__swift_as_ret: 0x644
+  __TEXT.__swift5_capture: 0x1028
+  __TEXT.__swift_as_entry: 0x588
+  __TEXT.__swift_as_ret: 0x650
   __TEXT.__swift5_protos: 0x34
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x9278
-  __TEXT.__eh_frame: 0xc698
-  __DATA_CONST.__auth_got: 0x22c8
-  __DATA_CONST.__got: 0x1f60
-  __DATA_CONST.__auth_ptr: 0xe90
-  __DATA_CONST.__const: 0x141c0
+  __TEXT.__unwind_info: 0x9318
+  __TEXT.__eh_frame: 0xc7f0
+  __DATA_CONST.__auth_got: 0x22d0
+  __DATA_CONST.__got: 0x1f78
+  __DATA_CONST.__auth_ptr: 0xeb0
+  __DATA_CONST.__const: 0x142e0
   __DATA_CONST.__cfstring: 0xc3c0
   __DATA_CONST.__objc_classlist: 0x960
   __DATA_CONST.__objc_catlist: 0x158

   __DATA_CONST.__objc_arraydata: 0x3e8
   __DATA_CONST.__objc_dictobj: 0x2d0
   __DATA_CONST.__objc_arrayobj: 0x168
-  __DATA.__objc_const: 0x20da8
-  __DATA.__objc_selrefs: 0x8190
-  __DATA.__objc_ivar: 0x718
-  __DATA.__objc_data: 0x7068
-  __DATA.__data: 0x51c8
+  __DATA.__objc_const: 0x21548
+  __DATA.__objc_selrefs: 0x81d0
+  __DATA.__objc_ivar: 0x71c
+  __DATA.__objc_data: 0x70c0
+  __DATA.__data: 0x5108
   __DATA.__bss: 0x7a98
   __DATA.__common: 0xaf0
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 13B0E0D9-BB4A-37DA-A92A-22FC6370CDB1
-  Functions: 12382
-  Symbols:   2511
-  CStrings:  12412
+  UUID: 2CFC37EF-511D-3CC5-8C2B-0735AE6EDC44
+  Functions: 12431
+  Symbols:   2516
+  CStrings:  12435
 
Symbols:
+ _$s10Foundation17URLResourceValuesV8fileSizeSiSgvg
+ _$s16GameServicesCore23InstallMetadataProtocolP19sizeOnDeviceInBytesSo8NSNumberCSgvgTq
+ _$sSiSEsWP
+ _$sSiSesWP
+ _NSURLFileSizeKey
CStrings:
+ "\v"
+ "-[GKGameServicePrivate clearInstallMetadataCacheWithCompletion:]"
+ "@\"GKLibraryBagObserver\""
+ "Attempting to fetch install metadata without a bag observer."
+ "Attempting to fetch library metadata without a bag observer."
+ "Failed to refresh install metadata: %@"
+ "GKLibraryBagObserver"
+ "GameDaemonCore.LibraryBagObserver"
+ "T@\"GKLibraryBagObserver\",&,V_libraryBagObserver"
+ "Vv32@0:8@\"NSString\"16@\"BSAuditToken\"24"
+ "_libraryBagObserver"
+ "_sizeOnDeviceInBytes"
+ "applicationsDidUpdateMetadata:"
+ "backgroundAssetsInfo"
+ "backgroundAssetsInfoWithOptional"
+ "clearInstallMetadataCacheWithCompletion:"
+ "createWithCodeSigning:fileManager:bagObserver:cache:completionHandler:"
+ "fetchWithRequest:bagObserver:refreshExpiredCompletion:completionHandler:"
+ "fileSizeByDevice"
+ "flag.2.crossed.fill"
+ "getInstallMetadataForBundleIDs:deleteNonmatchingCachedEntries:withCompletion - self was deallocated"
+ "getLibraryBagObserverWithCompletion:"
+ "initWithAmsbag:"
+ "initWithBundleID:adamID:bundleShortVersion:name:shortName:estimatedInstallDate:supportsGameController:isArcade:platform:isHidden:metadataEligibility:applicationType:isBeta:sizeOnDeviceInBytes:persistentRecordID:"
+ "initWithInteger:"
+ "launchOverlayForGameBundleId: %@, pid: %@"
+ "launchOverlayForGameBundleId:auditToken:"
+ "libraryBagObserver"
+ "maxEssentialInstallSizeInBytes"
+ "maxInstallSizeInBytes"
+ "productTypes"
+ "setLibraryBagObserver:"
+ "showDashboardWithGame:deepLink:launchContext:auditToken:"
+ "thinnedAppVariantId"
+ "v16@?0@\"GKInstallMetadataFetcher\"8"
+ "v16@?0@\"GKLibraryBagObserver\"8"
+ "v48@0:8@\"GKAppMetadataFetcherRequest\"16@\"GKLibraryBagObserver\"24@?<v@?@\"NSDictionary\">32@?<v@?@\"NSDictionary\"@\"NSError\">40"
+ "v56@0:8@\"<GKCodeSigning>\"16@\"NSFileManager\"24@\"GKLibraryBagObserver\"32@\"GKInstallMetadataCache\"40@?<v@?@\"GKInstallMetadataFetcher\">48"
- "Attempting to fetch library metadata without a bag."
- "Failed to refresh install metadat: %@"
- "_TtC14GameDaemonCore18LibraryBagObserver"
- "bagObserver"
- "fetchWithRequest:bag:refreshExpiredCompletion:completionHandler:"
- "flag.filled.and.flag.crossed"
- "initWithBundleID:adamID:bundleShortVersion:name:shortName:estimatedInstallDate:supportsGameController:isArcade:platform:isHidden:metadataEligibility:applicationType:isBeta:persistentRecordID:"
- "initWithCodeSigning:cache:"
- "installSizeByDeviceInBytes"
- "launchOverlayForGameBundleId: %@"
- "productType"
- "showDashboardWithGame:deepLink:launchContext:"
- "v48@0:8@\"GKAppMetadataFetcherRequest\"16@\"AMSBag\"24@?<v@?@\"NSDictionary\">32@?<v@?@\"NSDictionary\"@\"NSError\">40"

```
