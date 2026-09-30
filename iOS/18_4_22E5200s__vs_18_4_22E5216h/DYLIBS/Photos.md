## Photos

> `/System/Library/Frameworks/Photos.framework/Photos`

```diff

-750.5.104.0.0
-  __TEXT.__text: 0x26b2f8
-  __TEXT.__auth_stubs: 0x2930
-  __TEXT.__objc_methlist: 0x224d4
-  __TEXT.__const: 0xfa8
+750.11.101.0.0
+  __TEXT.__text: 0x26b6dc
+  __TEXT.__auth_stubs: 0x2920
+  __TEXT.__objc_methlist: 0x224fc
+  __TEXT.__const: 0xfb0
   __TEXT.__dlopen_cstrs: 0x47
   __TEXT.__constg_swiftt: 0x1dc
   __TEXT.__swift5_typeref: 0x290

   __TEXT.__swift5_assocty: 0x80
   __TEXT.__swift5_proto: 0x2c
   __TEXT.__swift5_types: 0x18
-  __TEXT.__cstring: 0x29437
+  __TEXT.__cstring: 0x294e0
   __TEXT.__swift5_capture: 0x6c
-  __TEXT.__gcc_except_tab: 0x9388
-  __TEXT.__oslogstring: 0x1b40b
+  __TEXT.__gcc_except_tab: 0x93d8
+  __TEXT.__oslogstring: 0x1b4c8
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x7fc0
-  __TEXT.__eh_frame: 0x228
+  __TEXT.__unwind_info: 0x7fa0
+  __TEXT.__eh_frame: 0x1a0
   __TEXT.__objc_classname: 0x3487
-  __TEXT.__objc_methname: 0x65f09
+  __TEXT.__objc_methname: 0x65fdf
   __TEXT.__objc_methtype: 0x69d2
-  __TEXT.__objc_stubs: 0x37180
-  __DATA_CONST.__got: 0x2548
-  __DATA_CONST.__const: 0x78c0
+  __TEXT.__objc_stubs: 0x371e0
+  __DATA_CONST.__got: 0x2550
+  __DATA_CONST.__const: 0x7898
   __DATA_CONST.__objc_classlist: 0xd18
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x2e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12128
+  __DATA_CONST.__objc_selrefs: 0x12140
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0xac0
   __DATA_CONST.__objc_arraydata: 0x948
-  __AUTH_CONST.__auth_got: 0x14a8
+  __AUTH_CONST.__auth_got: 0x14a0
   __AUTH_CONST.__auth_ptr: 0x1e0
-  __AUTH_CONST.__const: 0x37d8
+  __AUTH_CONST.__const: 0x3810
   __AUTH_CONST.__cfstring: 0x26a40
   __AUTH_CONST.__objc_const: 0x3a3d8
   __AUTH_CONST.__objc_intobj: 0x1f68

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 12775
+  Functions: 12767
   Symbols:   15584
-  CStrings:  22892
+  CStrings:  22903
 
Symbols:
+ _PLCreateShortLivedSystemPhotoLibrary
+ _PLMobileSlideshowBundleId
+ _RepresentationMarkerLocation
- _PLCreateShortLivedPhotoLibraryWithPhotoLibraryURL
- _PLCreateShortLivedWellKnownPhotoLibrary
CStrings:
+ "%s no curated assets in momentShare %p"
+ "%s with nil identifiers"
+ "%s with no mdIDs"
+ "+[PHQuery queryForAssetsInAssetCollection:options:]"
+ "+[PHQuery queryForCuratedAssetsInMomentShare:options:]"
+ "+[PHQuery queryForPersonsWithLocalIdentifiers:options:]"
+ "+[PHQuery queryForPersonsWithMdIDs:options:]"
+ "Unable to find photo library with identifier %@"
+ "[RM]: %{public}@ video chooser overriding streaming with download (didDisableNetworkAccess=%d) for asset %{public}@ / resource %{public}@ because ADP is enabled and fingerprint scheme %@ does not allow streaming"
+ "_updateFetchOptionsForProcessedAssets:"
+ "fetchExclusiveSocialGroupAssetsForPersons:minimumNumberOfSharedAssets:options:error:"
+ "newPhotoLibraryWithName:loadedFromURL:options:error:"
+ "nil assetCollection passed to %s"
+ "runAssetContainmentWithMinimumNumberOfSharedAssets:error:"
- "This resource set requires a full size video complement render resource to be provided"
- "[RM]: %{public}@ video chooser overriding streaming with download for asset %{public}@ / resource %{public}@ because ADP+%@ are enabled"
- "runAssetContainment:"

```
