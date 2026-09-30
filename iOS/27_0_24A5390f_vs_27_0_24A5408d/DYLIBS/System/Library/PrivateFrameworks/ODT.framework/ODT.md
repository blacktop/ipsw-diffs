## ODT

> `/System/Library/PrivateFrameworks/ODT.framework/ODT`

```diff

-26.5.0.0.0
-  __TEXT.__text: 0x4e988c
-  __TEXT.__const: 0x2c328
-  __TEXT.__gcc_except_tab: 0x23524
-  __TEXT.__cstring: 0x11cb3
-  __TEXT.__oslogstring: 0x98c
-  __TEXT.__unwind_info: 0xd050
+30.3.0.0.0
+  __TEXT.__text: 0x4f2558
+  __TEXT.__const: 0x2ccf8
+  __TEXT.__gcc_except_tab: 0x23ce8
+  __TEXT.__cstring: 0x11e2d
+  __TEXT.__oslogstring: 0xa00
+  __TEXT.__unwind_info: 0xd2e8
   __TEXT.__eh_frame: 0xc20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__weak_got: 0x28
   __DATA_CONST.__objc_selrefs: 0x30
   __DATA_CONST.__got: 0x368
-  __AUTH_CONST.__const: 0x19b50
+  __AUTH_CONST.__const: 0x1a110
   __AUTH_CONST.__cfstring: 0x2a0
   __AUTH_CONST.__weak_auth_got: 0x40
-  __AUTH_CONST.__auth_got: 0xff0
+  __AUTH_CONST.__auth_got: 0x1018
   __AUTH.__data: 0x20
   __AUTH.__thread_vars: 0x48
   __AUTH.__thread_bss: 0x18
-  __DATA.__data: 0x280
+  __DATA.__data: 0x308
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xde8
-  __DATA.__common: 0x120
+  __DATA.__bss: 0xe28
+  __DATA.__common: 0x170
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 10544
-  Symbols:   743
-  CStrings:  1650
+  Functions: 10638
+  Symbols:   748
+  CStrings:  1655
 
Symbols:
+ __os_log_send_and_compose_impl
+ __os_signpost_emit_unreliably_with_name_impl
+ _os_signpost_enabled
+ _pthread_threadid_np
+ _timespec_get
CStrings:
+ "ODTHeatmapPose: ncand=%zu,ncams=%zu,preemptive=%u,gp3p=%u,quorum=%u,n_filtered=%zu,n_factors=%zu,required=%zu"
+ "Trace"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cv::CVImageBuffer<img::Format::Two16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::iosimg::IOSurfaceImageBuffer<img::Format::Two16u>]"
+ "tracing"
```
