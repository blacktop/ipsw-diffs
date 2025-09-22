## Diagnostic-6002

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6002.appex/Diagnostic-6002`

```diff

-56.0.0.0.0
-  __TEXT.__text: 0x1bbf4
-  __TEXT.__auth_stubs: 0xb30
-  __TEXT.__objc_stubs: 0x1d00
+57.0.0.0.0
+  __TEXT.__text: 0x1c034
+  __TEXT.__auth_stubs: 0xb60
+  __TEXT.__objc_stubs: 0x1d60
   __TEXT.__objc_methlist: 0x8e4
-  __TEXT.__gcc_except_tab: 0x2f50
+  __TEXT.__gcc_except_tab: 0x3074
   __TEXT.__const: 0x128
-  __TEXT.__objc_methname: 0x2381
-  __TEXT.__cstring: 0x4485
+  __TEXT.__objc_methname: 0x23bf
+  __TEXT.__cstring: 0x4554
   __TEXT.__objc_classname: 0xc0
   __TEXT.__objc_methtype: 0xa6d
   __TEXT.__oslogstring: 0x26
-  __TEXT.__unwind_info: 0x7e8
-  __DATA_CONST.__auth_got: 0x5b0
+  __TEXT.__unwind_info: 0x7f8
+  __DATA_CONST.__auth_got: 0x5c8
   __DATA_CONST.__got: 0x428
   __DATA_CONST.__const: 0x5e8
-  __DATA_CONST.__cfstring: 0x33c0
+  __DATA_CONST.__cfstring: 0x3580
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x12b8
-  __DATA.__objc_selrefs: 0xa18
+  __DATA.__objc_selrefs: 0xa30
   __DATA.__objc_ivar: 0x160
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
-  UUID: 3A545E91-457D-39D4-9CDC-98D104AA6C78
-  Functions: 350
-  Symbols:   463
-  CStrings:  1497
+  UUID: E594730F-4109-36DB-AED0-BFD344E4D758
+  Functions: 351
+  Symbols:   467
+  CStrings:  1528
 
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
