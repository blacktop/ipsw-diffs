## Diagnostic-8389

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8389.appex/Diagnostic-8389`

```diff

-1066.0.19.502.1
-  __TEXT.__text: 0x1f478
-  __TEXT.__auth_stubs: 0xd70
-  __TEXT.__objc_stubs: 0x180
-  __TEXT.__objc_methlist: 0x534
-  __TEXT.__cstring: 0x158d
+1066.0.41.0.0
+  __TEXT.__text: 0x1f850
+  __TEXT.__auth_stubs: 0xdd0
+  __TEXT.__objc_stubs: 0x1c0
+  __TEXT.__objc_methlist: 0x544
+  __TEXT.__cstring: 0x161d
+  __TEXT.__oslogstring: 0x54
   __TEXT.__objc_classname: 0x12e
-  __TEXT.__objc_methname: 0xe23
+  __TEXT.__objc_methname: 0xe53
   __TEXT.__objc_methtype: 0x6bb
   __TEXT.__const: 0x3418
   __TEXT.__constg_swiftt: 0xda0

   __TEXT.__swift5_capture: 0xe4
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x8e8
+  __TEXT.__unwind_info: 0x8f0
   __TEXT.__eh_frame: 0x900
-  __DATA_CONST.__auth_got: 0x6c0
+  __DATA_CONST.__auth_got: 0x6f0
   __DATA_CONST.__got: 0x228
   __DATA_CONST.__auth_ptr: 0x198
   __DATA_CONST.__const: 0x20f8
-  __DATA_CONST.__cfstring: 0x1c0
+  __DATA_CONST.__cfstring: 0x360
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0xab8
-  __DATA.__objc_selrefs: 0x480
+  __DATA.__objc_selrefs: 0x490
   __DATA.__objc_data: 0x798
   __DATA.__data: 0x11d0
   __DATA.__bss: 0x6780

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
+  - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
+  - /System/Library/PrivateFrameworks/EXDisplayPipe.framework/EXDisplayPipe
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FD01702E-741B-3094-8B3F-9A60D969188D
-  Functions: 852
-  Symbols:   160
-  CStrings:  413
+  UUID: C57A27BB-216D-31D7-97F2-1EC3C0CCF899
+  Functions: 855
+  Symbols:   166
+  CStrings:  443
 
Symbols:
+ _DiagnosticLogHandleForCategory
+ _EXDisplayPipeClose
+ _EXDisplayPipeGetStats
+ _EXDisplayPipeOpen
+ __os_log_error_impl
+ _os_log_type_enabled
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
