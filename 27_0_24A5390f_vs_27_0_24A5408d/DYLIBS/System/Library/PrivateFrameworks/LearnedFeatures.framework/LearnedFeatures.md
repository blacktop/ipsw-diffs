## LearnedFeatures

> `/System/Library/PrivateFrameworks/LearnedFeatures.framework/LearnedFeatures`

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
- `__DATA_DIRTY.__objc_data`

```diff

-9.26.6.16.5
-  __TEXT.__text: 0x232cbc
-  __TEXT.__gcc_except_tab: 0x167a0
-  __TEXT.__cstring: 0xcf0b
-  __TEXT.__const: 0x192e0
+9.26.7.9.0
+  __TEXT.__text: 0x23d790
+  __TEXT.__gcc_except_tab: 0x17044
+  __TEXT.__cstring: 0xd2d6
+  __TEXT.__const: 0x19f30
   __TEXT.__oslogstring: 0x87
-  __TEXT.__unwind_info: 0x8110
+  __TEXT.__unwind_info: 0x83f0
   __TEXT.__eh_frame: 0x438
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __DATA_CONST.__const: 0x1138
-  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x28
   __DATA_CONST.__objc_selrefs: 0x28
   __DATA_CONST.__got: 0x330
-  __AUTH_CONST.__const: 0x10610
+  __AUTH_CONST.__const: 0x10e18
   __AUTH_CONST.__cfstring: 0x260
-  __AUTH_CONST.__objc_const: 0x630
+  __AUTH_CONST.__objc_const: 0x6c0
   __AUTH_CONST.__weak_auth_got: 0x40
   __AUTH_CONST.__auth_got: 0xa88
+  __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x10
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x10
   __DATA.__data: 0x880
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x848
-  __DATA.__common: 0x150
+  __DATA.__bss: 0x8c8
+  __DATA.__common: 0x100
   __DATA_DIRTY.__objc_data: 0x370
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5634
+  Functions: 5752
   Symbols:   580
-  CStrings:  1039
+  CStrings:  1049
 
CStrings:
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/EndToEndExtraction/include_private/LearnedFeatures/EndToEndExtraction/Globaldensefeat2.h"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCV3D_LearnedFeatures/library/LearnedFeatures/EndToEndExtraction/src/Globaldensefeat2.cpp"
+ "DetectKeypoints is not implemented for GlobalDenseFeat2Model"
+ "ExtractDescriptors is not implemented for GlobalDenseFeat2Model"
+ "ExtractLocalGlobalDescriptors is not implemented for GlobalDenseFeat2Model"
+ "Failed to access model resource path"
+ "Failed to create GlobalDenseFeat2 model"
+ "Models/GlobalDenseFeat/"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Two16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::iosimg::IOSurfaceImageBuffer<img::Format::Two16u>]"
```
