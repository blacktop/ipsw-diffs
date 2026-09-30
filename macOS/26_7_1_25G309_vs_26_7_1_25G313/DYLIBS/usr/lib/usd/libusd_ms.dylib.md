## libusd_ms.dylib

> `/usr/lib/usd/libusd_ms.dylib`

```diff

-23.5.4.0.0
-  __TEXT.__text: 0x15349d8
+23.5.6.0.0
+  __TEXT.__text: 0x1536434
   __TEXT.__auth_stubs: 0xc1c0
-  __TEXT.__gcc_except_tab: 0x172404
-  __TEXT.__const: 0x360be0
-  __TEXT.__cstring: 0x2900dc
+  __TEXT.__gcc_except_tab: 0x172424
+  __TEXT.__const: 0x360bf0
+  __TEXT.__cstring: 0x29079c
   __TEXT.__oslogstring: 0x1fc
   __TEXT.__constg_swiftt: 0x5d3c
   __TEXT.__swift5_typeref: 0x38ce

   __TEXT.__swift5_builtin: 0x3160
   __TEXT.__swift5_proto: 0x177c
   __TEXT.__swift5_protos: 0x78
-  __TEXT.__unwind_info: 0x98568
+  __TEXT.__unwind_info: 0x98588
   __TEXT.__eh_frame: 0x26040
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x1bca

   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__data: 0x1db8
   __AUTH.pxrctor: 0x40
-  __AUTH.__tf_func: 0x35a0
+  __AUTH.__tf_func: 0x35b8
   __AUTH.__mtlx_registry: 0x2c8
   __AUTH.__thread_vars: 0x288
   __AUTH.__thread_bss: 0x44148
-  __DATA.__data: 0x49210
-  __DATA.__common: 0x5eb8
-  __DATA_DIRTY.__tf_func: 0x0
+  __DATA.__data: 0x49230
+  __DATA.__common: 0x5ec0
   __DATA_DIRTY.__mtlx_registry: 0x0
+  __DATA_DIRTY.__tf_func: 0x0
   - /System/Library/Frameworks/ColorSync.framework/Versions/A/ColorSync
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_errno.dylib
-  Functions: 109122
-  Symbols:   40692
-  CStrings:  30229
+  Functions: 109125
+  Symbols:   40694
+  CStrings:  30248
 
Symbols:
+ __ZN32pxrInternal__aapl__pxrReserved__38SDF_TEXT_FILE_FORMAT_MAX_NESTING_DEPTHE
+ __ZN32pxrInternal__aapl__pxrReserved__44SDF_TEXT_FILE_FORMAT_MAX_NESTING_DEPTH_valueE
CStrings:
+ "21:45:42)"
+ "Failed to allocate destination images (%d x %d) for specular-glossiness to metallic-roughness conversion; aborting conversion"
+ "Image::allocate: image dimensions (%d x %d x %d) are invalid or too large; refusing to allocate to avoid integer overflow"
+ "Image::read: decoded image dimensions (%d x %d x %d) are invalid or too large; refusing to allocate to avoid integer overflow"
+ "Maximum nesting depth for container values (lists, tuples, and dictionaries) in the USDA text file format. Input nested more deeply than this is rejected as a parse error to prevent a thread-stack overflow. Values less than 1 are treated as 1."
+ "Ptex face resolution log2 (%d x %d) exceeds the maximum packable size (%d); rejecting face by treating it as 1x1."
+ "SDF_TEXT_FILE_FORMAT_MAX_NESTING_DEPTH"
+ "Value nesting too deep (exceeds maximum depth of %zu). Increase SDF_TEXT_FILE_FORMAT_MAX_NESTING_DEPTH if this input is trusted."
+ "allocate"
+ "bool adobe::usd::Image::allocate(int, int, int)"
+ "bool adobe::usd::Image::read(const ImageAsset &, int)"
+ "bool adobe::usd::processAnisotropyPixels(const Image &, const tinygltf::Image *, float, bool, const AnisotropyData &, Image &, Image &)"
+ "bool adobe::usd::processAnisotropyPixelsFromRoughness(const AnisotropyData &, const tinygltf::Image *, bool, Image &)"
+ "nanoexr error: invalid or too-large image dimensions\n"
+ "processAnisotropyPixels"
+ "processAnisotropyPixels: failed to allocate %d x %d anisotropy level/angle images; skipping anisotropy conversion"
+ "processAnisotropyPixelsFromRoughness"
+ "processAnisotropyPixelsFromRoughness: failed to allocate %d x %d anisotropy level image; skipping anisotropy conversion"
+ "read"
+ "void pxrInternal__aapl__pxrReserved__::HdStPtexMipmapTextureLoader::Block::SetSize(unsigned char, unsigned char, bool)"
- "04:22:27)"
```
