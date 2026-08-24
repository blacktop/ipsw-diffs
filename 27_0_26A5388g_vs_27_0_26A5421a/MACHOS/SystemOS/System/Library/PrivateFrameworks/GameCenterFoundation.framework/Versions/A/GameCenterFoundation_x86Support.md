## GameCenterFoundation_x86Support

> `/System/Library/PrivateFrameworks/GameCenterFoundation.framework/Versions/A/GameCenterFoundation_x86Support`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__auth_got`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-821.0.20.0.0
-  __TEXT.__text: 0x114268
-  __TEXT.__objc_methlist: 0x11acc
+821.0.25.0.0
+  __TEXT.__text: 0x114960
+  __TEXT.__objc_methlist: 0x11aec
   __TEXT.__cstring: 0x178f0
   __TEXT.__const: 0x24b8
   __TEXT.__gcc_except_tab: 0x1304
-  __TEXT.__oslogstring: 0xb9cb
+  __TEXT.__oslogstring: 0xba6b
   __TEXT.__ustring: 0x18
   __TEXT.__dlopen_cstrs: 0x58
   __TEXT.__constg_swiftt: 0xa88

   __TEXT.__swift_as_ret: 0x40
   __TEXT.__swift_as_cont: 0x70
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4c00
+  __TEXT.__unwind_info: 0x4c10
   __TEXT.__eh_frame: 0xcd0
-  __TEXT.__objc_stubs: 0x14da0
+  __TEXT.__objc_stubs: 0x14e00
   __TEXT.__auth_stubs: 0x1b30
   __TEXT.__objc_classname: 0x211d
-  __TEXT.__objc_methname: 0x261c5
+  __TEXT.__objc_methname: 0x26215
   __TEXT.__objc_methtype: 0x6301
   __DATA_CONST.__const: 0x2ac8
   __DATA_CONST.__objc_classlist: 0x798
   __DATA_CONST.__objc_catlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8160
+  __DATA_CONST.__objc_selrefs: 0x8178
   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x4c8
   __DATA_CONST.__objc_arraydata: 0x2a8
-  __DATA_CONST.__got: 0xd30
-  __AUTH_CONST.__const: 0x7550
+  __DATA_CONST.__got: 0xd40
+  __AUTH_CONST.__const: 0x7570
   __AUTH_CONST.__cfstring: 0x111e0
   __AUTH_CONST.__objc_const: 0x220d0
   __AUTH_CONST.__objc_arrayobj: 0x150

   __AUTH.__data: 0x5e8
   __DATA.__objc_ivar: 0xf44
   __DATA.__data: 0x2ad8
-  __DATA.__bss: 0x24e0
+  __DATA.__bss: 0x24f0
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x28c8
   __DATA_DIRTY.__data: 0x550

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8610
-  Symbols:   14161
-  CStrings:  10194
+  Functions: 8616
+  Symbols:   14174
+  CStrings:  10199
 
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
+ "_gkPromotedLocalPlayerInternalFromInternal:"
+ "getResourceValue:forKey:error:"
+ "hasSuffix:"
- "Illegal file cache path for subdirectory: %@, filename: %@"
```
