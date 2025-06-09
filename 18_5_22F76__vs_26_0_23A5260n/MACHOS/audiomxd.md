## audiomxd

> `/usr/libexec/audiomxd`

```diff

-1456.607.0.0.0
-  __TEXT.__text: 0x3e80
-  __TEXT.__auth_stubs: 0x8a0
+1534.2.30.1.0
+  __TEXT.__text: 0x3dd4
+  __TEXT.__auth_stubs: 0x890
   __TEXT.__objc_stubs: 0xc0
-  __TEXT.__const: 0xb2
+  __TEXT.__const: 0xa4
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__gcc_except_tab: 0x374
-  __TEXT.__cstring: 0x402
-  __TEXT.__oslogstring: 0x3d5
+  __TEXT.__gcc_except_tab: 0x358
+  __TEXT.__cstring: 0x452
+  __TEXT.__oslogstring: 0x31c
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x7f
-  __TEXT.__unwind_info: 0x178
-  __DATA_CONST.__auth_got: 0x460
+  __TEXT.__unwind_info: 0x170
+  __DATA_CONST.__auth_got: 0x458
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x3c8
+  __DATA_CONST.__const: 0x360
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x30
-  __DATA.__bss: 0x40
+  __DATA.__bss: 0x38
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /System/Library/PrivateFrameworks/WatchdogClient.framework/WatchdogClient
+  - /System/Library/PrivateFrameworks/caulk.framework/caulk
   - /usr/lib/libAudioToolboxUtility.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 12FB737A-E61B-3349-9AEB-870300081DF7
-  Functions: 62
-  Symbols:   177
-  CStrings:  92
+  UUID: 708AF334-DE81-3F40-8601-D39376BE56D0
+  Functions: 57
+  Symbols:   175
+  CStrings:  91
 
Symbols:
+ _CAAssertRtn
+ _CAVerboseAbort
+ __ZN5caulk5build6detail8get_kindEv
+ _objc_release_x20
- __ZN21PlatformUtilities_iOS15IsInternalBuildEv
- __ZNSt9exceptionD2Ev
- __ZTVN10__cxxabiv121__vmi_class_type_infoE
- __Znwm
- _audiomxd_enabled
- _objc_release_x22
CStrings:
+ "CAD_SubServer::~CAD_SubServer: still running at destruction"
+ "audiomxdStartTime"
+ "audiomxdSubServerCreationTime"
+ "audiomxd_iOS.mm"
+ "com.apple.audiomxd.up"
+ "com.apple.coreaudio.audiomxd"
+ "com.apple.coreaudio.audiomxd.cleanup"
+ "mIsServer"
+ "nbufs >= 1 && nbufs <= 64"
- "%25s:%-5d  CAD_SubServer::~CAD_SubServer: still running at destruction"
- "%25s:%-5d  STACK_ABL: invalid number of buffers"
- "%25s:%-5d ASSERTION FAILURE [(mIsServer) != 0 is false]: "
- "CAD_SubServer.cpp"
- "CAException"
- "com.apple.coreaudio.mediaserverd"
- "com.apple.coreaudio.mediaserverd.cleanup"
- "mediaserverd.mm"
- "mediaserverdStartTime"
- "mediaserverdSubServerCreationTime"

```
