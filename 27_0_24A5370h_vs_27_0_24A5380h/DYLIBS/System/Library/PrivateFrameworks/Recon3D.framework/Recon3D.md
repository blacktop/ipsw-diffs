## Recon3D

> `/System/Library/PrivateFrameworks/Recon3D.framework/Recon3D`

```diff

-  __TEXT.__text: 0x171ef90
-  __TEXT.__const: 0x1135f0
-  __TEXT.__cstring: 0x4d48f
-  __TEXT.__gcc_except_tab: 0xed98c
+  __TEXT.__text: 0x17059b4
+  __TEXT.__const: 0x112110
+  __TEXT.__cstring: 0x4d400
+  __TEXT.__gcc_except_tab: 0xebcf8
   __TEXT.__oslogstring: 0x88da
-  __TEXT.__unwind_info: 0x37220
-  __TEXT.__eh_frame: 0xb34
+  __TEXT.__unwind_info: 0x36f90
+  __TEXT.__eh_frame: 0xbfc
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0

   __DATA_CONST.__weak_got: 0x28
   __DATA_CONST.__objc_selrefs: 0x438
   __DATA_CONST.__got: 0x4f0
-  __AUTH_CONST.__const: 0x60aa8
+  __AUTH_CONST.__const: 0x609d0
   __AUTH_CONST.__cfstring: 0x4a0
   __AUTH_CONST.__weak_auth_got: 0x58
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x1638
-  __AUTH.__data: 0x10
+  __AUTH_CONST.__auth_got: 0x1630
+  __AUTH.__data: 0x20
   __AUTH.__thread_vars: 0x48
   __AUTH.__thread_bss: 0x38
   __DATA.__data: 0x57c0
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x68
-  __DATA.__common: 0x7a8
-  __DATA_DIRTY.__data: 0x68
-  __DATA_DIRTY.__bss: 0x3f60
+  __DATA.__common: 0x848
+  __DATA_DIRTY.__data: 0x58
+  __DATA_DIRTY.__bss: 0x3ec0
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 38096
-  Symbols:   1892
-  CStrings:  7413
+  Functions: 38035
+  Symbols:   1894
+  CStrings:  7414
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__thread_vars : content changed
Symbols:
+ __ZNKSt3__119bad_expected_accessIvE4whatEv
+ __ZTINSt3__119bad_expected_accessIvEE
CStrings:
+ "%d [%t] %p %c: %m%n"
+ "(null)"
+ "another file exporter already exists at the same location"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::concurrency::ChannelOutput<std::expected<cv3d::recon::frame::KeyframeData, cv3d::esn::Error>>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::concurrency::ChannelOutput<std::expected<std::shared_ptr<const cv3d::recon::kfplanes::PlaneDetectionResult>, cv3d::esn::Error>>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::concurrency::ChannelOutput<std::expected<std::shared_ptr<cv3d::recon::kf::KeyframeEngineResult>, cv3d::esn::Error>>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::concurrency::OptionalReturn<cv3d::recon::sng::MeshingNodeMeshUpdateResult> (const std::expected<std::shared_ptr<const cv3d::recon::kfplanes::PlaneDetectionResult>, cv3d::esn::Error> &)]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::concurrency::OptionalReturn<cv3d::recon::sng::MeshingNodeMeshUpdateResult> (cv3d::kit::concurrency::ChannelLimitedInput<std::expected<std::shared_ptr<cv3d::recon::kf::KeyframeEngineResult>, cv3d::esn::Error>, 1>)]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = std::expected<cv3d::recon::frame::KeyframeData, cv3d::esn::Error> (const cv3d::esn::random::UUID &)]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = std::expected<cv3d::recon::frame::KeyframeData, cv3d::esn::Error>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = std::expected<std::shared_ptr<const cv3d::recon::kfplanes::PlaneDetectionResult>, cv3d::esn::Error> (const std::expected<std::shared_ptr<cv3d::recon::kf::KeyframeEngineResult>, cv3d::esn::Error> &)]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = std::expected<std::shared_ptr<const cv3d::recon::kfplanes::PlaneDetectionResult>, cv3d::esn::Error> (const std::expected<std::shared_ptr<cv3d::recon::sng::KeyframeEngineResultSync>, cv3d::esn::Error> &)]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = std::expected<std::shared_ptr<const cv3d::recon::kfplanes::PlaneDetectionResult>, cv3d::esn::Error>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = std::expected<std::shared_ptr<cv3d::recon::kf::KeyframeEngineResult>, cv3d::esn::Error> (const cv3d::recon::frame::FrameBundle &)]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = std::expected<std::shared_ptr<cv3d::recon::kf::KeyframeEngineResult>, cv3d::esn::Error> (const cv3d::recon::sng::FrameBundleSync &)]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = std::expected<std::shared_ptr<cv3d::recon::kf::KeyframeEngineResult>, cv3d::esn::Error>]"
- " : %.*s"
- "%s: %s:%d"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::concurrency::ChannelOutput<std::experimental::expected<cv3d::recon::frame::KeyframeData, cv3d::esn::Error>>]"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::concurrency::ChannelOutput<std::experimental::expected<std::shared_ptr<const cv3d::recon::kfplanes::PlaneDetectionResult>, cv3d::esn::Error>>]"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::concurrency::ChannelOutput<std::experimental::expected<std::shared_ptr<cv3d::recon::kf::KeyframeEngineResult>, cv3d::esn::Error>>]"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::concurrency::OptionalReturn<cv3d::recon::sng::MeshingNodeMeshUpdateResult> (const std::experimental::expected<std::shared_ptr<const cv3d::recon::kfplanes::PlaneDetectionResult>, cv3d::esn::Error> &)]"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::concurrency::OptionalReturn<cv3d::recon::sng::MeshingNodeMeshUpdateResult> (cv3d::kit::concurrency::ChannelLimitedInput<std::experimental::expected<std::shared_ptr<cv3d::recon::kf::KeyframeEngineResult>, cv3d::esn::Error>, 1>)]"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = std::experimental::expected<cv3d::recon::frame::KeyframeData, cv3d::esn::Error> (const cv3d::esn::random::UUID &)]"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = std::experimental::expected<cv3d::recon::frame::KeyframeData, cv3d::esn::Error>]"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = std::experimental::expected<std::shared_ptr<const cv3d::recon::kfplanes::PlaneDetectionResult>, cv3d::esn::Error> (const std::experimental::expected<std::shared_ptr<cv3d::recon::kf::KeyframeEngineResult>, cv3d::esn::Error> &)]"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = std::experimental::expected<std::shared_ptr<const cv3d::recon::kfplanes::PlaneDetectionResult>, cv3d::esn::Error> (const std::experimental::expected<std::shared_ptr<cv3d::recon::sng::KeyframeEngineResultSync>, cv3d::esn::Error> &)]"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = std::experimental::expected<std::shared_ptr<const cv3d::recon::kfplanes::PlaneDetectionResult>, cv3d::esn::Error>]"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = std::experimental::expected<std::shared_ptr<cv3d::recon::kf::KeyframeEngineResult>, cv3d::esn::Error> (const cv3d::recon::frame::FrameBundle &)]"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = std::experimental::expected<std::shared_ptr<cv3d::recon::kf::KeyframeEngineResult>, cv3d::esn::Error> (const cv3d::recon::sng::FrameBundleSync &)]"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = std::experimental::expected<std::shared_ptr<cv3d::recon::kf::KeyframeEngineResult>, cv3d::esn::Error>]"

```
