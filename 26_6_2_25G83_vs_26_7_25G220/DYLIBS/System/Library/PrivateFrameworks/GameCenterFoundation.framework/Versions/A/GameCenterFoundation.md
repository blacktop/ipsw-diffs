## GameCenterFoundation

> `/System/Library/PrivateFrameworks/GameCenterFoundation.framework/Versions/A/GameCenterFoundation`

```diff

-820.6.10.1.1
-  __TEXT.__text: 0x18ecb8
+820.6.10.1.2
+  __TEXT.__text: 0x18f2d4
   __TEXT.__auth_stubs: 0x2670
   __TEXT.__objc_methlist: 0x1244c
   __TEXT.__cstring: 0x194f0
   __TEXT.__const: 0x65c8
   __TEXT.__gcc_except_tab: 0x14c8
-  __TEXT.__oslogstring: 0xdaab
+  __TEXT.__oslogstring: 0xdafb
   __TEXT.__ustring: 0x18
   __TEXT.__dlopen_cstrs: 0x58
   __TEXT.__swift5_typeref: 0x1f7c

   __TEXT.__swift_as_entry: 0x190
   __TEXT.__swift_as_ret: 0x1dc
   __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__unwind_info: 0x7368
+  __TEXT.__unwind_info: 0x7370
   __TEXT.__eh_frame: 0x5a88
   __TEXT.__objc_classname: 0x259d
-  __TEXT.__objc_methname: 0x288e5
+  __TEXT.__objc_methname: 0x28915
   __TEXT.__objc_methtype: 0x6c32
-  __TEXT.__objc_stubs: 0x155c0
-  __DATA_CONST.__got: 0x1090
+  __TEXT.__objc_stubs: 0x15600
+  __DATA_CONST.__got: 0x10a0
   __DATA_CONST.__const: 0x2b00
   __DATA_CONST.__objc_classlist: 0x820
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8598
+  __DATA_CONST.__objc_selrefs: 0x85a8
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x500
   __DATA_CONST.__objc_arraydata: 0x2a8
   __AUTH_CONST.__auth_got: 0x1348
-  __AUTH_CONST.__const: 0x9790
+  __AUTH_CONST.__const: 0x97b0
   __AUTH_CONST.__cfstring: 0x11b20
   __AUTH_CONST.__objc_const: 0x24f40
   __AUTH_CONST.__objc_arrayobj: 0x150

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11149
-  Symbols:   15260
-  CStrings:  10845
+  Functions: 11153
+  Symbols:   15270
+  CStrings:  10848
 
Symbols:
+ GKCanonicalImageCacheRoot.once
+ GKCanonicalImageCacheRoot.sCanonicalRoot
+ GKPathInsideImageCache
+ _GKPathInsideImageCache
+ _NSURLCanonicalPathKey
+ _NSURLIsSymbolicLinkKey
+ __GKCanonicalImageCacheRoot_block_invoke
+ ___GKCanonicalImageCacheRoot_block_invoke
+ _objc_msgSend$getResourceValue:forKey:error:
+ _objc_msgSend$hasSuffix:
Functions:
+ _GKPathInsideImageCache
+ ___GKCanonicalImageCacheRoot_block_invoke
~ +[NSData(GKAdditions) _gkLoadRemoteImageDataForUrl:session:subdirectory:filename:queue:imageQueue:handler:] : 1616 -> 1628
+ GKSupportDataRoot.cold.1
+ __GKCanonicalImageCacheRoot_block_invoke.cold.1
CStrings:
+ "Image cache root %@ is not under home %@; cannot validate cache paths"
+ "Refusing out-of-cache image path for subdirectory: %@, filename: %@"
+ "getResourceValue:forKey:error:"
+ "hasSuffix:"
- "Illegal file cache path for subdirectory: %@, filename: %@"
```
