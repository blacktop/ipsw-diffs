## PhotoLibraryServicesCore

> `/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore`

```diff

-742.0.141.0.0
-  __TEXT.__text: 0xc19cc
-  __TEXT.__auth_stubs: 0x1c80
-  __TEXT.__objc_methlist: 0x6578
+750.5.104.0.0
+  __TEXT.__text: 0xc2e4c
+  __TEXT.__auth_stubs: 0x1ca0
+  __TEXT.__objc_methlist: 0x7d1c
   __TEXT.__const: 0x2484
-  __TEXT.__gcc_except_tab: 0x6fdc
-  __TEXT.__cstring: 0x13c2c
-  __TEXT.__oslogstring: 0x9c8e
+  __TEXT.__cstring: 0x13d9a
   __TEXT.__dlopen_cstrs: 0x19c
-  __TEXT.__unwind_info: 0x2ff8
-  __TEXT.__objc_classname: 0x104f
-  __TEXT.__objc_methname: 0x151d3
-  __TEXT.__objc_methtype: 0x4b5e
-  __TEXT.__objc_stubs: 0xb740
-  __DATA_CONST.__got: 0xa98
-  __DATA_CONST.__const: 0x3860
-  __DATA_CONST.__objc_classlist: 0x3f0
+  __TEXT.__gcc_except_tab: 0x7044
+  __TEXT.__oslogstring: 0x9ddb
+  __TEXT.__unwind_info: 0x3000
+  __TEXT.__objc_classname: 0x107e
+  __TEXT.__objc_methname: 0x15303
+  __TEXT.__objc_methtype: 0x4c08
+  __TEXT.__objc_stubs: 0xba00
+  __DATA_CONST.__got: 0xaa8
+  __DATA_CONST.__const: 0x38e8
+  __DATA_CONST.__objc_classlist: 0x400
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4870
+  __DATA_CONST.__objc_selrefs: 0x4998
   __DATA_CONST.__objc_protorefs: 0xc0
-  __DATA_CONST.__objc_superrefs: 0x258
+  __DATA_CONST.__objc_superrefs: 0x260
   __DATA_CONST.__objc_arraydata: 0x418
-  __AUTH_CONST.__auth_got: 0xe50
+  __AUTH_CONST.__auth_got: 0xe60
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x32b0
+  __AUTH_CONST.__const: 0x32f0
   __AUTH_CONST.__cfstring: 0x10a20
-  __AUTH_CONST.__objc_const: 0xce10
+  __AUTH_CONST.__objc_const: 0xa640
   __AUTH_CONST.__objc_intobj: 0x960
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x62c
+  __DATA.__objc_ivar: 0x64c
   __DATA.__data: 0x1020
-  __DATA.__bss: 0xb90
-  __DATA_DIRTY.__objc_data: 0x24e0
+  __DATA.__bss: 0xb98
+  __DATA_DIRTY.__objc_data: 0x2580
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x530
+  __DATA_DIRTY.__bss: 0x548
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3686
-  Symbols:   5490
-  CStrings:  7100
+  Functions: 3695
+  Symbols:   5548
+  CStrings:  7125
 
Symbols:
+ _CFPreferencesGetAppIntegerValue
+ _OBJC_CLASS_$_PLAssetsdClientState
+ _OBJC_CLASS_$_PLPrimitiveAssetsdClient
+ _OBJC_METACLASS_$_PLAssetsdClientState
+ _OBJC_METACLASS_$_PLPrimitiveAssetsdClient
+ _PLDisableSecondXPCConnectionUserDefaultsKey
+ _PLIsMacPhotosApp
+ _PLLibraryServicesOperationNameCrashRecoveryProcessAssetAlbumAssociativity
+ _PLSearchBackendFeedbackDiagnosticsGetLog
+ _PLSearchBackendIndexEntityResultGetLog
+ _PLSetSharedLibraryNoSuggestionsDismissCount
+ _PLSharedLibraryNoSuggestionsDismissCount
+ _dispatch_source_set_cancel_handler
- _PLIsPhotosApp
CStrings:
+ "\x01\x11"
+ "\x0f\n"
+ "%@%@.%@"
+ "%@%s.%s"
+ "%@.%s"
+ "%@.JPG"
+ "%@.data"
+ "%@.full.JPG"
+ "%@.large.JPG"
+ "%@.media.dat"
+ "%@.medium.JPG"
+ "%@_sRGB.JPG"
+ "%s/%@/%@/%@/"
+ "-[PLAssetsdCloudClient computeStableHashesOfAsset:synchronously:completionHandler:]_block_invoke"
+ "-[PLAssetsdDebugClient requestSearchDebugInformationForAssetUUID:redacted:error:]_block_invoke"
+ "-[PLAssetsdLibraryInternalClient signalAvailabilityWithChanges:error:]_block_invoke"
+ "@\"NSString\"8@?0"
+ "@\"PLAssetsdClientState\""
+ "@\"PLPrimitiveAssetsdClient\""
+ "B8@?0"
+ "CrashRecovery: Process asset album associativity"
+ "Failed to bind to photo library %@, %@"
+ "NSString * _Nonnull PLStringFromPLPhotoLibraryCacheSubPathType(PLPhotoLibraryCacheSubPathType)"
+ "NSString * _Nonnull PLStringFromPLPhotoLibraryExternalPathType(PLPhotoLibraryExternalPathType)"
+ "NSString * _Nonnull PLStringFromPLPhotoLibraryInternalPathType(PLPhotoLibraryInternalPathType)"
+ "NSString * _Nonnull PLStringFromPLPhotoLibrarySubPathLeafType(PLPhotoLibrarySubPathLeafType)"
+ "NSString * _Nonnull PLStringFromPLPhotoLibrarySubPathType(PLPhotoLibrarySubPathType)"
+ "PLAssetsdClientState"
+ "PLPhotosErrorLocaleChanged"
+ "PLPrimitiveAssetsdClient"
+ "PLXPC Client: computeStableHashesOfAsset:synchronously:completionHandler:"
+ "PLXPC Client: signalAvailabilityWithChanges:error:"
+ "SearchBackendFeedbackDiagnostics"
+ "SearchBackendIndexEntityResult"
+ "Second assetsd XPC connection is disabled due to user default"
+ "Shared Library suggestions default not set in domain %@. Defaulting to 0"
+ "SharedLibraryNOSuggestionsDismissCount"
+ "Successfully bound to photo library: %@, %@"
+ "T@\"PLAssetsdClientState\",R,V_clientState"
+ "Unable to get asset stableHashes because XPC service returned an error. (%@)"
+ "Using high priority assetsd XPC client: %@"
+ "Using low priority assetsd XPC client: %@"
+ "_clientState"
+ "_highPriorityClient"
+ "_isSecondXPCConnectionDisabled"
+ "_lock_securityScopedURLs"
+ "_lowPriorityClient"
+ "_primitiveClientForCurrentQoS"
+ "clientState"
+ "com.apple.photos.backend.disableSecondXPCConnection"
+ "computeStableHashesOfAsset:synchronously:completionHandler:"
+ "computeStableHashesOfAssetWithObjectURI:synchronously:reply:"
+ "ignoring request to cancel inactive PLDelayedActionTimer"
+ "initWithPhotoLibraryURL:clientState:"
+ "initWithQueue:proxyCreating:proxyGetter:clientState:"
+ "isOpen"
+ "requestSearchDebugInformationForAssetUUID:redacted:error:"
+ "searchAttributesForAssetWithUUID:redacted:reply:"
+ "signalAvailabilityWithChanges:error:"
+ "signalAvailabilityWithChanges:reply:"
+ "v32@0:8@\"PLFeatureAvailabilitySignalledChanges\"16@?<v@?B@\"NSError\">24"
+ "v36@0:8@\"NSString\"16B24@?<v@?@\"NSDictionary\">28"
- "\a"
- "\x0f\t"
- "%s%@.%@"
- "%s%s.%s"
- "%s.%@"
- "%s.%s"
- "%s.JPG"
- "%s.data"
- "%s.full.JPG"
- "%s.large.JPG"
- "%s.media.dat"
- "%s.medium.JPG"
- "%s/%@/%s/"
- "%s/%@/%s/%@/"
- "%s_sRGB.JPG"
- "-[PLAssetsdCloudClient computeFingerPrintsOfAsset:synchronously:completionHandler:]_block_invoke"
- "-[PLAssetsdDebugClient requestSearchDebugInformationForAssetUUID:error:]_block_invoke"
- ".."
- "Failed to open photo library %@, %@"
- "NSString *PLStringFromPLPhotoLibraryCacheSubPathType(PLPhotoLibraryCacheSubPathType)"
- "NSString *PLStringFromPLPhotoLibraryExternalPathType(PLPhotoLibraryExternalPathType)"
- "NSString *PLStringFromPLPhotoLibraryInternalPathType(PLPhotoLibraryInternalPathType)"
- "NSString *PLStringFromPLPhotoLibrarySubPathLeafType(PLPhotoLibrarySubPathLeafType)"
- "NSString *PLStringFromPLPhotoLibrarySubPathType(PLPhotoLibrarySubPathType)"
- "PLXPC Client: computeFingerPrintsOfAsset:synchronously:completionHandler:"
- "T@\"NSObject<OS_dispatch_queue>\",R,N"
- "Unable to get asset fingerprints because XPC service returned an error. (%@)"
- "_securityScopedURLs"
- "add"
- "computeFingerPrintsOfAssetWithObjectURI:synchronously:reply:"
- "ignoring request to cancel inactive timer"
- "initWithQueue:proxyCreating:proxyGetter:sandboxExtensions:"
- "isOpened"
- "modify"
- "requestSearchDebugInformationForAssetUUID:error:"
- "searchAttributesForAssetWithUUID:reply:"
- "targetQueue"

```
