## Diagnostic-6004

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Diagnostic-6004`

```diff

-1066.0.19.502.1
-  __TEXT.__text: 0x12648
-  __TEXT.__auth_stubs: 0xc60
-  __TEXT.__objc_stubs: 0x2a0
-  __TEXT.__objc_methlist: 0x4bc
-  __TEXT.__cstring: 0xff9
-  __TEXT.__objc_methname: 0xc92
+1066.0.41.0.0
+  __TEXT.__text: 0x12a20
+  __TEXT.__auth_stubs: 0xcb0
+  __TEXT.__objc_stubs: 0x2e0
+  __TEXT.__objc_methlist: 0x4cc
+  __TEXT.__cstring: 0x1089
+  __TEXT.__objc_methname: 0xcc2
   __TEXT.__objc_classname: 0x118
   __TEXT.__objc_methtype: 0x368
+  __TEXT.__oslogstring: 0xfe
   __TEXT.__const: 0x9d8
   __TEXT.__swift5_typeref: 0x1464
   __TEXT.__constg_swiftt: 0x6dc

   __TEXT.__swift5_fieldmd: 0x3dc
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_capture: 0x264
-  __TEXT.__oslogstring: 0x9e
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x34
-  __TEXT.__unwind_info: 0x470
+  __TEXT.__unwind_info: 0x478
   __TEXT.__eh_frame: 0xd8
-  __DATA_CONST.__auth_got: 0x638
-  __DATA_CONST.__got: 0x298
+  __DATA_CONST.__auth_got: 0x660
+  __DATA_CONST.__got: 0x2a0
   __DATA_CONST.__auth_ptr: 0x2d0
   __DATA_CONST.__const: 0xdd8
-  __DATA_CONST.__cfstring: 0x1e0
+  __DATA_CONST.__cfstring: 0x380
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0xce8
-  __DATA.__objc_selrefs: 0x488
+  __DATA.__objc_selrefs: 0x498
   __DATA.__objc_data: 0x7a0
   __DATA.__data: 0xf00
   __DATA.__bss: 0x400

   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
+  - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
+  - /System/Library/PrivateFrameworks/EXDisplayPipe.framework/EXDisplayPipe
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4D33403B-12B5-3533-9DB6-C9D693693CC1
-  Functions: 456
-  Symbols:   166
-  CStrings:  355
+  UUID: F33E06A0-6F40-3A63-8147-AF2DD18304A8
+  Functions: 459
+  Symbols:   172
+  CStrings:  385
 
Symbols:
+ _DiagnosticLogHandleForCategory
+ _EXDisplayPipeClose
+ _EXDisplayPipeGetStats
+ _EXDisplayPipeOpen
+ _OBJC_CLASS_$_NSNumber
+ __os_log_error_impl
CStrings:
+ "Failed to get ExDisplayPipe status!"
+ "Failed to open ExDisplayPipe client for status!"
+ "_exDisplayPipeStats"
+ "brightness"
+ "dcpTransportHealth"
+ "displayPipeStats"
+ "globalHealth"
+ "link"
+ "numberWithUnsignedLongLong:"
+ "pipe"
+ "scaAlgorithm"
+ "scaDriver"
+ "sclDriver"
+ "sclHealth"
+ "tconCRC"
+ "tconHPD"
+ "tconHealth"

```
