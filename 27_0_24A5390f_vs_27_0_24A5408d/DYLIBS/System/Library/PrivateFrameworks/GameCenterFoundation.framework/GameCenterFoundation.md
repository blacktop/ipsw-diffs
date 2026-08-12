## GameCenterFoundation

> `/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation`

```diff

-821.0.20.0.0
-  __TEXT.__text: 0x172850
-  __TEXT.__objc_methlist: 0x121dc
+821.0.25.0.0
+  __TEXT.__text: 0x172ee8
+  __TEXT.__objc_methlist: 0x121fc
   __TEXT.__cstring: 0x18ff0
   __TEXT.__const: 0x6608
   __TEXT.__gcc_except_tab: 0x12a0
-  __TEXT.__oslogstring: 0xde1b
+  __TEXT.__oslogstring: 0xdebb
   __TEXT.__ustring: 0x18
   __TEXT.__dlopen_cstrs: 0xba
   __TEXT.__swift5_typeref: 0x2062

   __TEXT.__swift_as_ret: 0x1dc
   __TEXT.__swift_as_cont: 0x3f4
   __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__unwind_info: 0x67c8
+  __TEXT.__unwind_info: 0x67d8
   __TEXT.__eh_frame: 0x5968
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8560
+  __DATA_CONST.__objc_selrefs: 0x8578
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x4f0
   __DATA_CONST.__objc_arraydata: 0x280
-  __DATA_CONST.__got: 0x10f8
-  __AUTH_CONST.__const: 0x6ce8
+  __DATA_CONST.__got: 0x1108
+  __AUTH_CONST.__const: 0x6d08
   __AUTH_CONST.__cfstring: 0x11640
   __AUTH_CONST.__objc_const: 0x245c8
   __AUTH_CONST.__objc_arrayobj: 0x150

   __AUTH.__data: 0x1088
   __DATA.__objc_ivar: 0xfb0
   __DATA.__data: 0x3a60
-  __DATA.__bss: 0x82d0
+  __DATA.__bss: 0x82e0
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x2c40
   __DATA_DIRTY.__data: 0x748

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11219
-  Symbols:   15067
-  CStrings:  4202
+  Functions: 11225
+  Symbols:   15077
+  CStrings:  4204
 
Symbols:
+ +[GKLocalPlayer _gkPromotedLocalPlayerInternalFromInternal:]
+ -[GKLocalPlayer setInternal:]
+ GCC_except_table38
+ GCC_except_table53
+ GCC_except_table67
+ _GKCanonicalImageCacheRoot.once
+ _GKCanonicalImageCacheRoot.sCanonicalRoot
+ _GKPathInsideImageCache
+ _NSURLCanonicalPathKey
+ _NSURLIsSymbolicLinkKey
+ ___GKCanonicalImageCacheRoot_block_invoke
+ _objc_msgSend$_gkPromotedLocalPlayerInternalFromInternal:
+ _objc_msgSend$getResourceValue:forKey:error:
+ _objc_msgSend$hasSuffix:
- GCC_except_table51
- GCC_except_table65
- GCC_except_table88
- GCC_except_table97
CStrings:
+ "GKLocalPlayer.setInternal: promoting %@ to GKLocalPlayerInternal. Stack trace:%@"
+ "Image cache root %@ is not under home %@; cannot validate cache paths"
+ "Refusing out-of-cache image path for subdirectory: %@, filename: %@"
- "Illegal file cache path for subdirectory: %@, filename: %@"
```
