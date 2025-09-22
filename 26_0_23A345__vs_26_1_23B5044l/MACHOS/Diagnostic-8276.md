## Diagnostic-8276

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8276.appex/Diagnostic-8276`

```diff

-56.0.0.0.0
-  __TEXT.__text: 0x1adf0
-  __TEXT.__auth_stubs: 0xb20
-  __TEXT.__objc_stubs: 0x1b60
+57.0.0.0.0
+  __TEXT.__text: 0x1b230
+  __TEXT.__auth_stubs: 0xb50
+  __TEXT.__objc_stubs: 0x1bc0
   __TEXT.__objc_methlist: 0x8a4
-  __TEXT.__gcc_except_tab: 0x2c5c
+  __TEXT.__gcc_except_tab: 0x2d80
   __TEXT.__const: 0x128
-  __TEXT.__objc_methname: 0x221f
-  __TEXT.__cstring: 0x420b
+  __TEXT.__objc_methname: 0x225d
+  __TEXT.__cstring: 0x42da
   __TEXT.__objc_classname: 0xca
   __TEXT.__objc_methtype: 0x9fe
   __TEXT.__oslogstring: 0x11d
-  __TEXT.__unwind_info: 0x7c0
-  __DATA_CONST.__auth_got: 0x5a8
+  __TEXT.__unwind_info: 0x7d0
+  __DATA_CONST.__auth_got: 0x5c0
   __DATA_CONST.__got: 0x418
   __DATA_CONST.__const: 0x5e8
-  __DATA_CONST.__cfstring: 0x3240
+  __DATA_CONST.__cfstring: 0x3400
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x1288
-  __DATA.__objc_selrefs: 0x9b0
+  __DATA.__objc_selrefs: 0x9c8
   __DATA.__objc_ivar: 0x15c
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
   - /System/Library/PrivateFrameworks/CoreUI.framework/CoreUI
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
+  - /System/Library/PrivateFrameworks/EXDisplayPipe.framework/EXDisplayPipe
   - /System/Library/PrivateFrameworks/JasperDepth.framework/JasperDepth
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/PeridotDepth.framework/PeridotDepth
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D62114D0-0044-3AA3-8EB0-8BA3C7942A0A
-  Functions: 345
-  Symbols:   460
-  CStrings:  1458
+  UUID: FE0DCB7A-743D-3337-BCC1-B8658C785667
+  Functions: 346
+  Symbols:   464
+  CStrings:  1489
 
Symbols:
+ _EXDisplayPipeClose
+ _EXDisplayPipeGetStats
+ _EXDisplayPipeOpen
+ __Z13ecStatusCheckv
+ __Z18ecDisplayPipeStatsv
- __Z18ecPearlStatusCheckv
Functions:
+ __Z18ecDisplayPipeStatsv
CStrings:
+ "Failed to get ExDisplayPipe status!"
+ "Failed to open ExDisplayPipe client for status!"
+ "brightness"
+ "copy"
+ "dcpTransportHealth"
+ "globalHealth"
+ "link"
+ "numberWithUnsignedLongLong:"
+ "pipe"
+ "scaAlgorithm"
+ "scaDriver"
+ "sclDriver"
+ "sclHealth"
+ "setObject:forKeyedSubscript:"
+ "tconCRC"
+ "tconHPD"
+ "tconHealth"

```
