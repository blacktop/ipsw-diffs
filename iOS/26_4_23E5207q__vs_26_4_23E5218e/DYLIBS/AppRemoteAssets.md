## AppRemoteAssets

> `/System/Library/PrivateFrameworks/AppRemoteAssets.framework/AppRemoteAssets`

```diff

-15.0.0.0.0
-  __TEXT.__text: 0x13ac6c
-  __TEXT.__auth_stubs: 0x25d0
+16.0.0.0.0
+  __TEXT.__text: 0x15a210
+  __TEXT.__auth_stubs: 0x2790
   __TEXT.__objc_methlist: 0x25c
-  __TEXT.__const: 0x1025c
-  __TEXT.__swift5_typeref: 0x4660
-  __TEXT.__swift5_reflstr: 0x2c4b
-  __TEXT.__swift5_assocty: 0xbe0
-  __TEXT.__constg_swiftt: 0x4b68
-  __TEXT.__swift5_fieldmd: 0x48d8
-  __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__swift5_proto: 0xdf8
-  __TEXT.__swift5_types: 0x560
-  __TEXT.__swift_as_entry: 0x328
-  __TEXT.__swift_as_ret: 0x410
-  __TEXT.__swift5_capture: 0xcc8
-  __TEXT.__oslogstring: 0x2592
-  __TEXT.__cstring: 0x1e41
-  __TEXT.__swift5_protos: 0xfc
-  __TEXT.__swift5_mpenum: 0x50
-  __TEXT.__unwind_info: 0x49d0
-  __TEXT.__eh_frame: 0xbf4c
-  __TEXT.__objc_classname: 0xe20
-  __TEXT.__objc_methname: 0x18e6
+  __TEXT.__const: 0x11f3c
+  __TEXT.__swift5_typeref: 0x4c74
+  __TEXT.__swift5_reflstr: 0x31bb
+  __TEXT.__swift5_assocty: 0xc88
+  __TEXT.__constg_swiftt: 0x50e0
+  __TEXT.__swift5_fieldmd: 0x4fe0
+  __TEXT.__swift5_builtin: 0x104
+  __TEXT.__swift5_proto: 0xfa0
+  __TEXT.__swift5_types: 0x5f8
+  __TEXT.__swift_as_entry: 0x380
+  __TEXT.__swift_as_ret: 0x468
+  __TEXT.__swift5_capture: 0xdb0
+  __TEXT.__oslogstring: 0x3152
+  __TEXT.__cstring: 0x2031
+  __TEXT.__swift5_protos: 0x100
+  __TEXT.__swift5_mpenum: 0x60
+  __TEXT.__unwind_info: 0x5188
+  __TEXT.__eh_frame: 0xd30c
+  __TEXT.__objc_classname: 0xf40
+  __TEXT.__objc_methname: 0x19a6
   __TEXT.__objc_methtype: 0x5b6
-  __TEXT.__objc_stubs: 0x860
-  __DATA_CONST.__got: 0x6a0
-  __DATA_CONST.__const: 0xd8
-  __DATA_CONST.__objc_classlist: 0x1f0
+  __TEXT.__objc_stubs: 0x8a0
+  __DATA_CONST.__got: 0x6f0
+  __DATA_CONST.__const: 0xe8
+  __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x360
+  __DATA_CONST.__objc_selrefs: 0x370
   __DATA_CONST.__objc_protorefs: 0x18
-  __AUTH_CONST.__auth_got: 0x12f0
-  __AUTH_CONST.__const: 0xafb0
-  __AUTH_CONST.__objc_const: 0x4448
-  __AUTH.__objc_data: 0x240
-  __AUTH.__data: 0x4bd0
-  __DATA.__data: 0x3d10
-  __DATA.__bss: 0x13f08
-  __DATA.__common: 0x128
+  __AUTH_CONST.__auth_got: 0x13d0
+  __AUTH_CONST.__const: 0xbf60
+  __AUTH_CONST.__objc_const: 0x4878
+  __AUTH.__objc_data: 0x1f0
+  __AUTH.__data: 0x5240
+  __DATA.__data: 0x4210
+  __DATA.__bss: 0x17178
+  __DATA.__common: 0x1a8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
+  - /usr/lib/swift/libswiftSystem.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9FE014A4-9868-3F16-9548-19BDDDE1BB08
-  Functions: 5362
-  Symbols:   229
-  CStrings:  744
+  UUID: AA41FFB4-A610-3B1D-B9DE-F36F00BBC410
+  Functions: 5920
+  Symbols:   231
+  CStrings:  804
 
Symbols:
+ _NSURLIsDirectoryKey
+ _sysctlbyname
CStrings:
+ ".requirements.json"
+ "App launched - checking for pre-downloadable assets, assetType=%s"
+ "AppRemoteAssets/ContainerDefinitions.swift"
+ "Asset Pack not found in manifest while finding compatible variant, identifier=%s"
+ "Asset pack filter context did not provide a required value, filterValue=%s"
+ "Asset pack filters did not contain a value matching context, contextValue=%s, filterValue=%s"
+ "AssetPackSpecifier"
+ "Attempting to pre-download asset pack because it's marked as downloadable on launch, name=%s"
+ "CFBundleShortVersionString"
+ "Download for Asset Pack deduplicated, identifier=%s"
+ "Download requested for Asset Pack - deduping if necessary, identifier=%s"
+ "Download succeeded - writing requirements to disk"
+ "Download succeeded for Asset Pack, identifier=%s, version=%s, containerURL=%s"
+ "Downloaded Asset Pack archive - decompressing it to its container directory, archiveFileURL=%s, containerDirectoryURL=%s"
+ "Downloading and decompressing asset pack to temporary container directory, artifactReference=%s, containerURL=%s"
+ "Failed to convert destination directory URL to file path while decompressing Asset Pack archive"
+ "Failed to create decode stream while decompressing Asset Pack archive"
+ "Failed to create decompression stream while decompressing Asset Pack archive"
+ "Failed to create extract stream while decompressing Asset Pack archive"
+ "Failed to create read file stream while decompressing Asset Pack archive"
+ "Failed to find matching Asset Pack variant in manifest, identifier=%s"
+ "Failed to initialize Version from string literal, stringLiteral=%s, error=%@"
+ "Failed to load environment from asset pack manifest - falling back to production, error=%@"
+ "Failed to parse archive URL as local file path, archiveURL=%s"
+ "Failed to parse version from app version string - asset packs with app version requirements will fail to download, appVersionString=%s, error=%@"
+ "Failed to pre-download AssetPack, name=%s, error=%@"
+ "Failed to read asset pack requirements from file - assuming it's incompatible, error=%@"
+ "Found existing download for Asset Pack - serving it, containerURL=%s"
+ "Found matching Asset Pack variant in manifest - downloading it, version=%s, variantFilePath=%s"
+ "Invalid number of keys found, expected one."
+ "Invalid version range: "
+ "No matching variant found for Asset Pack version, identifier=%s, version=%s"
+ "Skipping asset pack because it's not marked as downloadable on launch, name=%s, downloadTrigger=%s"
+ "Successfully pre-downloaded Asset Pack, assetPackName=%s, containerURL=%s"
+ "Unable to determine device type from device model - asset packs with device type filters will fail to download, deviceModel=%s"
+ "Unable to read app version from bundle info dictionary - asset packs with app version requirements will fail to download"
+ "Unable to read contents of asset pack versions directory - assuming no versions have been downloaded, error=%@"
+ "Unable to resolve asset pack manifest while determining base URL for download - falling back to base URL from ARA config, error=%@"
+ "Unexpectedly found no AssetPackManifestProvider in dependency context. \nMake sure to register a Task-local value using Container.shared.assetPackManifestProvider.withValue(_:operation:)."
+ "_TtC15AppRemoteAssets12Decompressor"
+ "_TtC15AppRemoteAssets19AssetPackDownloader"
+ "_TtC15AppRemoteAssets32AssetPackManifestBaseURLProvider"
+ "_TtC15AppRemoteAssets36AssetPackManifestEnvironmentProvider"
+ "_TtC15AppRemoteAssets36DeviceAssetPackFilterContextProvider"
+ "artifactDownloader"
+ "assetPackFilterContextProvider"
+ "decompressor"
+ "downloadDeduper"
+ "fetchManifest"
+ "hw.model"
+ "iOS"
+ "infoDictionary"
+ "mac"
+ "macOS"
+ "operatingSystemVersion"
+ "operatingSystemVersions"
+ "pad"
+ "phone"
+ "supportedAssetPacks"
+ "vision"
+ "visionOS"
- "cachesDirectory"

```
