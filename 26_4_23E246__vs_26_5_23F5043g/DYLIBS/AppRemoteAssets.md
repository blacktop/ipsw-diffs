## AppRemoteAssets

> `/System/Library/PrivateFrameworks/AppRemoteAssets.framework/AppRemoteAssets`

```diff

-17.0.0.0.0
-  __TEXT.__text: 0x15a0b0
-  __TEXT.__auth_stubs: 0x2790
+20.0.0.0.0
+  __TEXT.__text: 0x1643c4
+  __TEXT.__auth_stubs: 0x27c0
   __TEXT.__objc_methlist: 0x25c
-  __TEXT.__const: 0x11f3c
-  __TEXT.__swift5_typeref: 0x4c74
-  __TEXT.__swift5_reflstr: 0x31bb
+  __TEXT.__const: 0x121bc
+  __TEXT.__swift5_typeref: 0x4d70
+  __TEXT.__swift5_reflstr: 0x326b
   __TEXT.__swift5_assocty: 0xc88
-  __TEXT.__constg_swiftt: 0x50e0
-  __TEXT.__swift5_fieldmd: 0x4fe0
+  __TEXT.__constg_swiftt: 0x51c8
+  __TEXT.__swift5_fieldmd: 0x50b0
   __TEXT.__swift5_builtin: 0x104
-  __TEXT.__swift5_proto: 0xfa0
-  __TEXT.__swift5_types: 0x5f8
-  __TEXT.__swift_as_entry: 0x380
-  __TEXT.__swift_as_ret: 0x468
-  __TEXT.__swift5_capture: 0xdb0
-  __TEXT.__oslogstring: 0x3152
+  __TEXT.__swift5_proto: 0xfa8
+  __TEXT.__swift5_types: 0x604
+  __TEXT.__swift_as_entry: 0x39c
+  __TEXT.__swift_as_ret: 0x484
+  __TEXT.__swift5_capture: 0xef8
+  __TEXT.__oslogstring: 0x34c2
   __TEXT.__cstring: 0x2031
-  __TEXT.__swift5_protos: 0x100
+  __TEXT.__swift5_protos: 0x104
   __TEXT.__swift5_mpenum: 0x60
-  __TEXT.__unwind_info: 0x5178
-  __TEXT.__eh_frame: 0xd2e4
-  __TEXT.__objc_classname: 0xf40
-  __TEXT.__objc_methname: 0x19a6
+  __TEXT.__unwind_info: 0x5360
+  __TEXT.__eh_frame: 0xd92c
+  __TEXT.__objc_classname: 0xf80
+  __TEXT.__objc_methname: 0x19f6
   __TEXT.__objc_methtype: 0x5b6
   __TEXT.__objc_stubs: 0x8a0
-  __DATA_CONST.__got: 0x6f0
+  __DATA_CONST.__got: 0x708
   __DATA_CONST.__const: 0xe8
-  __DATA_CONST.__objc_classlist: 0x218
+  __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x370
   __DATA_CONST.__objc_protorefs: 0x18
-  __AUTH_CONST.__auth_got: 0x13d0
-  __AUTH_CONST.__const: 0xbf60
-  __AUTH_CONST.__objc_const: 0x4878
+  __AUTH_CONST.__auth_got: 0x13e8
+  __AUTH_CONST.__const: 0xc1e0
+  __AUTH_CONST.__objc_const: 0x49b0
   __AUTH.__objc_data: 0x1f0
-  __AUTH.__data: 0x5240
-  __DATA.__data: 0x4200
-  __DATA.__bss: 0x17178
+  __AUTH.__data: 0x53c0
+  __DATA.__data: 0x4280
+  __DATA.__bss: 0x171f8
   __DATA.__common: 0x148
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftSystem.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A06FE69E-D1A5-3EF2-8631-C3F309B4F554
-  Functions: 5918
-  Symbols:   231
-  CStrings:  804
+  UUID: 64C61E51-2A40-3F9E-A2D2-FE7CBAC472F9
+  Functions: 6045
+  Symbols:   232
+  CStrings:  818
 
Symbols:
+ _swift_runtimeSupportsNoncopyableTypes
CStrings:
+ "Background download of newer Asset Pack version failed, identifier=%s, version=%s, error=%@"
+ "Background download of newer Asset Pack version succeeded, identifier=%s, version=%s"
+ "Deleted old asset pack version, identifier=%s, version=%s"
+ "Disk version is up to date - serving existing download, identifier=%s, version=%s"
+ "Download for Asset Pack version deduplicated, identifier=%s, version=%s"
+ "Eager update strategy - downloading and serving new version, identifier=%s, version=%s"
+ "Failed to delete old asset pack version, identifier=%s, version=%s, error=%@"
+ "Lazy update strategy - serving existing version and downloading update in background, identifier=%s, servedVersion=%s, backgroundVersion=%s"
+ "Newer Asset Pack version available in manifest, identifier=%s, diskVersion=%s, manifestVersion=%s"
+ "No existing download found - downloading Asset Pack, identifier=%s, version=%s"
+ "Serving session-pinned Asset Pack version, identifier=%s, version=%s"
+ "Session-pinned Asset Pack version was deleted externally - resetting session pin, identifier=%s, version=%s"
+ "_TtC15AppRemoteAssets34AssetPackDownloadStatusCoordinator"
+ "listeners"
+ "servedVersions"
+ "statusCoordinator"
+ "versionDownloadDeduper"
- "Download succeeded for Asset Pack, identifier=%s, version=%s, containerURL=%s"
- "Found existing download for Asset Pack - serving it, containerURL=%s"
- "Found matching Asset Pack variant in manifest - downloading it, version=%s, variantFilePath=%s"

```
