## VisualLogger

> `/System/Library/PrivateFrameworks/VisualLogger.framework/VisualLogger`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__data`

```diff

-9.26.6.16.5
-  __TEXT.__text: 0x700b3c
-  __TEXT.__const: 0x671f0
-  __TEXT.__gcc_except_tab: 0x648b8
-  __TEXT.__cstring: 0x1674e
+9.26.7.9.0
+  __TEXT.__text: 0x70d98c
+  __TEXT.__const: 0x68980
+  __TEXT.__gcc_except_tab: 0x653e0
+  __TEXT.__cstring: 0x16804
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x1c060
+  __TEXT.__unwind_info: 0x1c418
   __TEXT.__eh_frame: 0x98
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__weak_got: 0x28
   __DATA_CONST.__objc_selrefs: 0x18
   __DATA_CONST.__got: 0x310
-  __AUTH_CONST.__const: 0x32640
+  __AUTH_CONST.__const: 0x330e0
   __AUTH_CONST.__cfstring: 0x2a0
   __AUTH_CONST.__weak_auth_got: 0x40
-  __AUTH_CONST.__auth_got: 0xdf8
+  __AUTH_CONST.__auth_got: 0xde8
   __AUTH.__data: 0x18
   __DATA.__data: 0x21f8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x2740
-  __DATA.__common: 0x338
+  __DATA.__bss: 0x27c0
+  __DATA.__common: 0x2e8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 16895
-  Symbols:   1149
-  CStrings:  2205
+  Functions: 17047
+  Symbols:   1147
+  CStrings:  2204
 
Symbols:
- _CFBundleCopyBundleURL
- _CFURLGetString
CStrings:
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Two16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::iosimg::IOSurfaceImageBuffer<img::Format::Two16u>]"
- "Failed to convert bundle URL to string"
- "bundle_url"
- "file://"
```
