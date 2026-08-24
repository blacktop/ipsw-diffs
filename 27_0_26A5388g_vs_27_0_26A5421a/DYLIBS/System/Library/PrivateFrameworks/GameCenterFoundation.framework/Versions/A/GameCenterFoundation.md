## GameCenterFoundation

> `/System/Library/PrivateFrameworks/GameCenterFoundation.framework/Versions/A/GameCenterFoundation`

```diff

-821.0.20.0.0
-  __TEXT.__text: 0x1806b4
-  __TEXT.__objc_methlist: 0x1217c
+821.0.25.0.0
+  __TEXT.__text: 0x180dac
+  __TEXT.__objc_methlist: 0x1219c
   __TEXT.__cstring: 0x194d0
   __TEXT.__const: 0x65f8
   __TEXT.__gcc_except_tab: 0x12e0
-  __TEXT.__oslogstring: 0xdaab
+  __TEXT.__oslogstring: 0xdb4b
   __TEXT.__ustring: 0x18
   __TEXT.__dlopen_cstrs: 0x58
   __TEXT.__swift5_typeref: 0x2056

   __TEXT.__swift_as_ret: 0x1dc
   __TEXT.__swift_as_cont: 0x3f4
   __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__unwind_info: 0x6800
+  __TEXT.__unwind_info: 0x6818
   __TEXT.__eh_frame: 0x59c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x84a0
+  __DATA_CONST.__objc_selrefs: 0x84b8
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x4e8
   __DATA_CONST.__objc_arraydata: 0x2a8
-  __DATA_CONST.__got: 0x1048
-  __AUTH_CONST.__const: 0xa9e8
+  __DATA_CONST.__got: 0x1058
+  __AUTH_CONST.__const: 0xaa08
   __AUTH_CONST.__cfstring: 0x11840
   __AUTH_CONST.__objc_const: 0x244c8
   __AUTH_CONST.__objc_arrayobj: 0x150

   __AUTH.__data: 0x1088
   __DATA.__objc_ivar: 0xfb8
   __DATA.__data: 0x3a30
-  __DATA.__bss: 0x82b0
+  __DATA.__bss: 0x82c0
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x2c40
   __DATA_DIRTY.__data: 0x748

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11301
-  Symbols:   15158
-  CStrings:  4200
+  Functions: 11307
+  Symbols:   15171
+  CStrings:  4202
 
Symbols:
+ +[GKLocalPlayer _gkPromotedLocalPlayerInternalFromInternal:]
+ -[GKLocalPlayer setInternal:]
+ GCC_except_table116
+ GCC_except_table43
+ GCC_except_table47
+ GCC_except_table74
+ GCC_except_table82
+ GKCanonicalImageCacheRoot.once
+ GKCanonicalImageCacheRoot.sCanonicalRoot
+ GKPathInsideImageCache
+ _GKPathInsideImageCache
+ _NSURLCanonicalPathKey
+ _NSURLIsSymbolicLinkKey
+ __GKCanonicalImageCacheRoot_block_invoke
+ ___GKCanonicalImageCacheRoot_block_invoke
+ _objc_msgSend$_gkPromotedLocalPlayerInternalFromInternal:
+ _objc_msgSend$getResourceValue:forKey:error:
+ _objc_msgSend$hasSuffix:
- GCC_except_table114
- GCC_except_table45
- GCC_except_table63
- GCC_except_table72
- GCC_except_table80
CStrings:
+ "GKLocalPlayer.setInternal: promoting %@ to GKLocalPlayerInternal. Stack trace:%@"
+ "Image cache root %@ is not under home %@; cannot validate cache paths"
+ "Refusing out-of-cache image path for subdirectory: %@, filename: %@"
- "Illegal file cache path for subdirectory: %@, filename: %@"
```
