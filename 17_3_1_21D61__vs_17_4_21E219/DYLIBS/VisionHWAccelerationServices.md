## VisionHWAccelerationServices

> `/System/Library/PrivateFrameworks/VisionHWAccelerationServices.framework/VisionHWAccelerationServices`

```diff

-2.17.0.0.0
-  __TEXT.__text: 0x1a074
-  __TEXT.__auth_stubs: 0xad0
+3.2.6.0.0
+  __TEXT.__text: 0x1c068
+  __TEXT.__auth_stubs: 0xc20
   __TEXT.__objc_methlist: 0x74
-  __TEXT.__const: 0xb8e
-  __TEXT.__oslogstring: 0xea8
-  __TEXT.__gcc_except_tab: 0x10f8
-  __TEXT.__cstring: 0xf45
-  __TEXT.__unwind_info: 0x8b8
+  __TEXT.__const: 0xbee
+  __TEXT.__oslogstring: 0x100e
+  __TEXT.__gcc_except_tab: 0x1278
+  __TEXT.__cstring: 0x1076
+  __TEXT.__unwind_info: 0x94c
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x34
-  __TEXT.__objc_methname: 0x3bb
+  __TEXT.__objc_methname: 0x3cb
   __TEXT.__objc_methtype: 0x1bf
   __TEXT.__objc_stubs: 0x2e0
-  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__got: 0x178
   __DATA_CONST.__const: 0x1c8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x550
   __DATA_CONST.__objc_selrefs: 0xe8
-  __AUTH_CONST.__const: 0xa48
+  __DATA_CONST.__objc_classrefs: 0x40
+  __DATA_CONST.__objc_superrefs: 0x8
+  __AUTH_CONST.__const: 0xa98
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0x48
-  __AUTH_CONST.__auth_got: 0x578
+  __AUTH_CONST.__auth_got: 0x620
   __AUTH.__objc_data: 0x50
   __DATA.__got_weak: 0x8
-  __DATA.__objc_classrefs: 0x40
-  __DATA.__objc_superrefs: 0x8
   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0x100
-  __DATA.__bss: 0x1f8
+  __DATA.__crash_info: 0x40
+  __DATA.__bss: 0x208
   __DATA.__common: 0x4
-  __DATA_DIRTY.__data: 0x160
+  __DATA_DIRTY.__data: 0x1c0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
-  - /System/Library/Frameworks/MediaToolbox.framework/MediaToolbox
+  - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/Metal.framework/Metal
+  - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
+  - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine
   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
-  - /System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libncurses.5.4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B4596A40-C0A0-37F5-BC60-ECFB52567311
-  Functions: 473
-  Symbols:   241
-  CStrings:  331
+  UUID: 85767685-F23C-3F9E-94F2-0CC8E0526AC0
+  Functions: 501
+  Symbols:   268
+  CStrings:  347
 
Symbols:
+ _VisionHWServerStart
+ __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
+ __ZNKSt3__16locale9use_facetERNS0_2idE
+ __ZNKSt3__18ios_base6getlocEv
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryD1Ev
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEi
+ __ZNSt3__114basic_iostreamIcNS_11char_traitsIcEEED2Ev
+ __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
+ __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
+ __ZNSt3__15ctypeIcE2idE
+ __ZNSt3__16localeD1Ev
+ __ZNSt3__18ios_base33__set_badbit_and_consider_rethrowEv
+ __ZNSt3__18ios_base4initEPv
+ __ZNSt3__18ios_base5clearEj
+ __ZNSt3__19basic_iosIcNS_11char_traitsIcEEED2Ev
+ __ZTTNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZTVNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZTVNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ ___cxa_end_catch
+ ___stderrp
+ __os_feature_enabled_impl
+ _fputs
+ _memset
+ _os_log_create
+ _os_release
+ _os_transaction_create
+ _strncpy
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
CStrings:
+ " : "
+ "%s"
+ "(transaction == nullptr) && \"stale os_transaction pointer\""
+ "**************** VisionHWAServer has been disabled in mediaserverd"
+ "**************** VisionHWAServer has been disabled in visionserverd"
+ "/Library/Caches/com.apple.xbs/Sources/VisionHWAccelerationServices/product/VisionHWAccelerationServices/VisionHWAccelerationServices/src/VisionHWAServices.cpp"
+ ":"
+ "AppleCVHWA"
+ "Application PID=%d terminated with status %d"
+ "Assert: "
+ "T@\"NSString\",?,R,C"
+ "VisionHWAServer: received release command but numClients is already zero!!"
+ "VisionHWAServer: unable to create and prepare an ISP Processing Session"
+ "VisionHWAccelerationServices framework launched via mediaserverd"
+ "VisionHWAccelerationServices framework launched via visionhwserverd"
+ "XPC_ERROR_CONNECTION_INVALID w/ client_connection = %p"
+ "com.apple.visionhwserverd.active"
+ "cv3d"
+ "enable_visionhwserverd"
- "VisionHWAServer: VisionHWAProgramLoader: detected COLL platform."
- "VisionHWAServer: VisionHWAProgramLoader: detected CRETE platform."
- "XPC_ERROR_CONNECTION_INVALID"

```
