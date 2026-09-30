## ODT

> `/System/Library/PrivateFrameworks/ODT.framework/ODT`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__data`
- `__AUTH.__thread_vars`

```diff

-25.2.0.0.0
-  __TEXT.__text: 0x4ef2d0
-  __TEXT.__const: 0x2db68
-  __TEXT.__gcc_except_tab: 0x239ec
-  __TEXT.__cstring: 0x11cdb
-  __TEXT.__oslogstring: 0x954
-  __TEXT.__unwind_info: 0xd240
+26.5.0.0.0
+  __TEXT.__text: 0x4e988c
+  __TEXT.__const: 0x2c328
+  __TEXT.__gcc_except_tab: 0x23524
+  __TEXT.__cstring: 0x11cb3
+  __TEXT.__oslogstring: 0x98c
+  __TEXT.__unwind_info: 0xd050
   __TEXT.__eh_frame: 0xc20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__weak_got: 0x28
   __DATA_CONST.__objc_selrefs: 0x30
   __DATA_CONST.__got: 0x368
-  __AUTH_CONST.__const: 0x1a408
+  __AUTH_CONST.__const: 0x19b50
   __AUTH_CONST.__cfstring: 0x2a0
   __AUTH_CONST.__weak_auth_got: 0x40
   __AUTH_CONST.__auth_got: 0xff0

   __AUTH.__thread_bss: 0x18
   __DATA.__data: 0x280
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xe28
+  __DATA.__bss: 0xde8
   __DATA.__common: 0x120
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 10674
+  Functions: 10544
   Symbols:   743
-  CStrings:  1645
+  CStrings:  1650
 
CStrings:
+ " OTA asset missing metadata.json"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/ODT/library/ODT/Util/include/ODT/Util/PoseFilter.h"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/ODT/product/ODT/ODT/src/ODT3DContext.mm"
+ "ApplyModelCatalogAssets: %s missing metadata.json at %s"
+ "Detector"
+ "ResetTo not implemented for this filter"
+ "Unhandled BlendAlphaMapping"
+ "iPhone tracker"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::concurrency::ChannelOutput<cv3d::odt::api::odt3d::ModelCatalogAssetsReleaseOutput>]"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::odt::api::odt3d::ModelCatalogAssetsReleaseOutput (const cv3d::odt::api::odt3d::ModelCatalogAssetsReleaseInput &)]"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::odt::api::odt3d::ModelCatalogAssetsReleaseOutput]"
```
