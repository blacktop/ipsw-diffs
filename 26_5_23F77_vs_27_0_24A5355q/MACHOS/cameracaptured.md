## cameracaptured

> `/usr/libexec/cameracaptured`

```diff

-665.120.8.0.0
-  __TEXT.__text: 0x530
-  __TEXT.__auth_stubs: 0x280
-  __TEXT.__objc_stubs: 0x20
-  __TEXT.__const: 0x24
-  __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__oslogstring: 0x106
-  __TEXT.__cstring: 0x71
-  __TEXT.__objc_methname: 0x21
-  __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0x150
-  __DATA_CONST.__got: 0x38
-  __DATA_CONST.__auth_ptr: 0x8
+748.0.0.122.2
+  __TEXT.__text: 0x704
+  __TEXT.__auth_stubs: 0x2d0
+  __TEXT.__objc_stubs: 0xa0
+  __TEXT.__const: 0x34
+  __TEXT.__gcc_except_tab: 0x74
+  __TEXT.__oslogstring: 0x254
+  __TEXT.__cstring: 0x76
+  __TEXT.__objc_methname: 0x7d
+  __TEXT.__unwind_info: 0x80
   __DATA_CONST.__const: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x8
+  __DATA_CONST.__auth_got: 0x178
+  __DATA_CONST.__got: 0x50
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__objc_selrefs: 0x28
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/MediaSafetyNet.framework/MediaSafetyNet
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DC91CAE2-B6F0-393D-8D7E-D05DC1CE7F4D
-  Functions: 4
-  Symbols:   51
-  CStrings:  13
+  UUID: A5EEF862-1E3B-34A1-9452-47F4EA5FDA29
+  Functions: 6
+  Symbols:   59
+  CStrings:  20
 
Symbols:
+ _FigCapturePrewarmEncoderRegistry
+ _FigVirtualCaptureCardServerStartNew
+ _NSTemporaryDirectory
+ _NSURLFileProtectionCompleteUntilFirstUserAuthentication
+ _NSURLFileProtectionKey
+ _OBJC_CLASS_$_NSURL
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _FigVirtualCaptureCardServerStart
CStrings:
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/CMCapture/Sources/cameracaptured/Resources-Embedded/cameracaptured.m %s: cannot listen for language changed notification (%d)"
+ "Error setting NSURLFileProtectionCompleteUntilFirstUserAuthentication for %{public}@: %s"
+ "UTF8String"
+ "cameracaptured servers are starting"
+ "fileURLWithPath:isDirectory:"
+ "localizedDescription"
+ "main"
+ "setResourceValue:forKey:error:"
- "cameracaptured servers starting"

```
