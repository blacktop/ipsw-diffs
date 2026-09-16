## AssetExplorer

> `/System/Library/PrivateFrameworks/AssetExplorer.framework/AssetExplorer`

```diff

-912.0.235.0.0
-  __TEXT.__text: 0x206a8
+916.40.110.0.0
+  __TEXT.__text: 0x207f0
   __TEXT.__objc_methlist: 0x2aac
   __TEXT.__const: 0x338
   __TEXT.__constg_swiftt: 0x1c8

   __TEXT.__swift5_capture: 0x10
   __TEXT.__swift5_types: 0xc
   __TEXT.__gcc_except_tab: 0x384
-  __TEXT.__oslogstring: 0x1e63
+  __TEXT.__oslogstring: 0x1f80
   __TEXT.__unwind_info: 0xad0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2078
+  __DATA_CONST.__objc_selrefs: 0x2080
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__got: 0x5a0
   __AUTH_CONST.__const: 0x288
   __AUTH_CONST.__cfstring: 0xee0
   __AUTH_CONST.__objc_const: 0x4628
   __AUTH_CONST.__objc_intobj: 0xd8
-  __AUTH_CONST.__auth_got: 0x628
+  __AUTH_CONST.__auth_got: 0x630
   __AUTH.__objc_data: 0x8d8
   __AUTH.__data: 0xe8
   __DATA.__objc_ivar: 0x198

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 774
-  Symbols:   2652
-  CStrings:  251
+  Symbols:   2654
+  CStrings:  255
 
Symbols:
+ _PXPhotosFileProviderRegisterConfigurationSetShouldIncludeRating
+ _objc_msgSend$shouldIncludeRating
Functions:
~ -[AEPackageTransport expectedPackageIdentifiers] : 84 -> 80
~ -[AEAssetPackage(CKBrowserItemPayload) browserItemPayload] : 2040 -> 2172
~ -[AEPhotosAssetPackageGenerator _generatePackageFromAsset:] : 804 -> 884
~ -[AEPhotosAssetPackageGenerator _generatePackageFromAssetUsingDVPSharing:] : 1364 -> 1484
CStrings:
+ "Failed to generate sandbox token for fileProviderURL: %@"
+ "Failed to generate sandbox token for thumbnailFilePathURL: %@"
+ "[AEPhotosAssetPackageGenerator] Failed to create file provider register for DVP sharing"
+ "[AEPhotosAssetPackageGenerator] No file representations found for DVP sharing"
```
