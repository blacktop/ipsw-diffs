## CoreImage

> `/System/Library/Frameworks/CoreImage.framework/Versions/A/CoreImage`

### Sections with Same Size but Changed Content

- `__TEXT.__dlopen_cstrs`

```diff

-1667.21.2.0.0
-  __TEXT.__text: 0x34aec4
-  __TEXT.__objc_methlist: 0x16078
+1667.40.3.0.0
+  __TEXT.__text: 0x34b684
+  __TEXT.__objc_methlist: 0x16098
   __TEXT.__const: 0xe268
-  __TEXT.__gcc_except_tab: 0xaa58
-  __TEXT.__cstring: 0x105a08
-  __TEXT.__oslogstring: 0xb95c
+  __TEXT.__gcc_except_tab: 0xaa6c
+  __TEXT.__cstring: 0x105a7a
+  __TEXT.__oslogstring: 0xb94e
   __TEXT.__dlopen_cstrs: 0x3fd
   __TEXT.__runtimeheader: 0x15aa4
   __TEXT.__cikl2metal_pre: 0x54b
   __TEXT.__grain: 0x105040
   __TEXT.__cruft: 0x36d1
-  __TEXT.__unwind_info: 0xcb20
+  __TEXT.__unwind_info: 0xcb48
   __TEXT.__eh_frame: 0x350
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9098
+  __DATA_CONST.__objc_selrefs: 0x90b0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x3a0
   __DATA_CONST.__objc_arraydata: 0x1478
-  __DATA_CONST.__got: 0xb38
-  __AUTH_CONST.__const: 0x10440
+  __DATA_CONST.__got: 0xb60
+  __AUTH_CONST.__const: 0x104a0
   __AUTH_CONST.__cfstring: 0x1de40
-  __AUTH_CONST.__objc_const: 0x2bdf0
+  __AUTH_CONST.__objc_const: 0x2be10
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0xde0
   __AUTH_CONST.__objc_dictobj: 0x3e8
   __AUTH_CONST.__objc_doubleobj: 0x2a50
   __AUTH_CONST.__objc_floatobj: 0x2e0
   __AUTH_CONST.__objc_arrayobj: 0x198
-  __AUTH_CONST.__auth_got: 0x1808
+  __AUTH_CONST.__auth_got: 0x1848
   __AUTH.__objc_data: 0x9880
   __AUTH.__data: 0x277f0
   __DATA.__objc_ivar: 0x200c

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 15312
-  Symbols:   29336
-  CStrings:  9009
+  Functions: 15324
+  Symbols:   29365
+  CStrings:  9011
 
Symbols:
+ +[CIContextCache currentEntryCount]
+ +[CIContextCache peakEntryCount]
+ +[CIRAWFilter downloadAllResourcesWithTimeout:completionHandler:]
+ GCC_except_table160
+ GCC_except_table286
+ GetSurfaceCacheEntryCount
+ GetSurfaceCachePeakEntryCount
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
- GCC_except_table159
CStrings:
+ "1667.40.3"
+ "CGImage base address (%p) is not aligned to its pixel size (%lu bytes)!\n"
+ "Cannot get the provider from a CGImage.\n"
+ "Failed to load CoreImage.metallib from %{public}@: %{public}@\n"
+ "Failed to serialize CoreImage.metallib from %{public}@ to %{public}@: %{public}@\n"
+ "softlink:o:path:/System/Library/VideoProcessors/CCPortrait.bundle/CCPortrait"
- "%{public}s a CIImageProcessorInput with a empty region cannot be accessed via its base address."
- "1667.21.2"
- "Failed loading CoreImage.metallib from %{public}@: %{public}@\n"
- "softlink:r:path:/System/Library/VideoProcessors/CCPortrait.bundle/CCPortrait"
```
