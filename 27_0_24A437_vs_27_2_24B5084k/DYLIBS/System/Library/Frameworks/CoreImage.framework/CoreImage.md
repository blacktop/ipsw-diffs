## CoreImage

> `/System/Library/Frameworks/CoreImage.framework/CoreImage`

### Sections with Same Size but Changed Content

- `__TEXT.__dlopen_cstrs`

```diff

-1667.22.1.0.0
-  __TEXT.__text: 0x341f7c
-  __TEXT.__objc_methlist: 0x159b0
+1667.40.3.0.0
+  __TEXT.__text: 0x342700
+  __TEXT.__objc_methlist: 0x159d0
   __TEXT.__const: 0xe198
-  __TEXT.__gcc_except_tab: 0xa868
-  __TEXT.__cstring: 0x1049a8
-  __TEXT.__oslogstring: 0xb283
+  __TEXT.__gcc_except_tab: 0xa87c
+  __TEXT.__cstring: 0x104a1a
+  __TEXT.__oslogstring: 0xb275
   __TEXT.__dlopen_cstrs: 0x3fd
   __TEXT.__runtimeheader: 0x15aa4
   __TEXT.__cikl2metal_pre: 0x54b
   __TEXT.__grain: 0x105040
-  __TEXT.__unwind_info: 0xc7e0
+  __TEXT.__unwind_info: 0xc800
   __TEXT.__eh_frame: 0x350
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x64d8
+  __DATA_CONST.__const: 0x6528
   __DATA_CONST.__objc_classlist: 0x1078
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8e50
+  __DATA_CONST.__objc_selrefs: 0x8e68
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x1488
-  __DATA_CONST.__got: 0xaf8
+  __DATA_CONST.__got: 0xb20
   __AUTH_CONST.__const: 0xde40
   __AUTH_CONST.__cfstring: 0x1dba0
-  __AUTH_CONST.__objc_const: 0x2b4c0
+  __AUTH_CONST.__objc_const: 0x2b4e0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0xdc8
   __AUTH_CONST.__objc_dictobj: 0x410
   __AUTH_CONST.__objc_doubleobj: 0x2a40
   __AUTH_CONST.__objc_floatobj: 0x2e0
   __AUTH_CONST.__objc_arrayobj: 0x198
-  __AUTH_CONST.__auth_got: 0x1858
+  __AUTH_CONST.__auth_got: 0x1898
   __AUTH.__objc_data: 0x9dd0
   __AUTH.__data: 0x278a0
   __DATA.__objc_ivar: 0x1fc0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 15163
-  Symbols:   28584
-  CStrings:  8881
+  Functions: 15173
+  Symbols:   28608
+  CStrings:  8883
 
Symbols:
+ +[CIContextCache currentEntryCount]
+ +[CIContextCache peakEntryCount]
+ +[CIRAWFilter downloadAllResourcesWithTimeout:completionHandler:]
+ GCC_except_table280
+ GCC_except_table285
+ _CGColorSpaceContainsISO5Metadata
+ _CGColorSpaceCopyColorSyncProfile
+ _CGColorSpaceGetISO5Headroom
+ _ColorSyncProfileCopyData
+ _ColorSyncProfileCreate
+ _ColorSyncProfileCreateCopyWithISO5Metadata
+ _ColorSyncProfileGetCICPInfo
+ _ColorSyncProfileGetISO5AverageLightLevel
+ _GetSurfaceCacheEntryCount
+ _GetSurfaceCachePeakEntryCount
+ __ZL19CreateNewMTLTexturePU19objcproto9MTLDevice11objc_objectP11__IOSurfacej
+ __ZL21CCPortraitLibraryCorePPc
+ __ZN2CI44ColorSpaceCreateCopyWithISO5HeadroomMetadataEP12CGColorSpaceff
+ __ZN2CIL27pqOrExtendedRangeLightlevelEP12CGColorSpace
+ __ZNK2CI18TagColorSpaceImage10lightlevelEv
+ ___65+[CIRAWFilter downloadAllResourcesWithTimeout:completionHandler:]_block_invoke
+ ___GetSurfaceCacheEntryCount_block_invoke
+ ___GetSurfaceCachePeakEntryCount_block_invoke
+ _kColorSyncAverageLightLevel
+ _kColorSyncCLLInfo
+ _kColorSyncMaxLightLevel
+ _kColorSyncPrimaries
+ _kColorSyncReferenceWhite
- GCC_except_table144
- GCC_except_table279
- __ZNSt3__15dequeIPN2CI17SurfaceCacheEntryENS_9allocatorIS3_EEE26__maybe_remove_front_spareB9fqn220106Eb
- __ZNSt3__15dequeIPN2CI17SurfaceCacheEntryENS_9allocatorIS3_EEE9pop_frontEv
CStrings:
+ "1667.40.3"
+ "CGImage base address (%p) is not aligned to its pixel size (%lu bytes)!\n"
+ "Cannot get the provider from a CGImage.\n"
+ "Failed to load CoreImage.metallib from %{public}@: %{public}@\n"
+ "Failed to serialize CoreImage.metallib from %{public}@ to %{public}@: %{public}@\n"
+ "softlink:o:path:/System/Library/VideoProcessors/CCPortrait.bundle/CCPortrait"
- "%{public}s a CIImageProcessorInput with a empty region cannot be accessed via its base address."
- "1667.22.1"
- "Failed loading CoreImage.metallib from %{public}@: %{public}@\n"
- "softlink:r:path:/System/Library/VideoProcessors/CCPortrait.bundle/CCPortrait"
```
