## Diagnostic-4009

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4009.appex/Diagnostic-4009`

```diff

-1066.0.19.502.1
-  __TEXT.__text: 0x6f6c
-  __TEXT.__auth_stubs: 0x660
-  __TEXT.__objc_stubs: 0x16c0
-  __TEXT.__objc_methlist: 0xccc
-  __TEXT.__cstring: 0xa3d
+1066.0.41.0.0
+  __TEXT.__text: 0x7344
+  __TEXT.__auth_stubs: 0x690
+  __TEXT.__objc_stubs: 0x1700
+  __TEXT.__objc_methlist: 0xcdc
+  __TEXT.__cstring: 0xac9
   __TEXT.__const: 0x40
   __TEXT.__gcc_except_tab: 0x188
   __TEXT.__objc_classname: 0x14b
-  __TEXT.__objc_methname: 0x18de
+  __TEXT.__objc_methname: 0x190e
   __TEXT.__objc_methtype: 0x70c
-  __TEXT.__oslogstring: 0x2dd
-  __TEXT.__unwind_info: 0x278
-  __DATA_CONST.__auth_got: 0x340
+  __TEXT.__oslogstring: 0x331
+  __TEXT.__unwind_info: 0x280
+  __DATA_CONST.__auth_got: 0x358
   __DATA_CONST.__got: 0x1b0
   __DATA_CONST.__const: 0x210
-  __DATA_CONST.__cfstring: 0x820
+  __DATA_CONST.__cfstring: 0x9c0
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x1f8
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA.__objc_const: 0x1280
-  __DATA.__objc_selrefs: 0x6f8
+  __DATA.__objc_selrefs: 0x708
   __DATA.__objc_ivar: 0xa8
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x308

   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
+  - /System/Library/PrivateFrameworks/EXDisplayPipe.framework/EXDisplayPipe
   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9EA9E214-1580-3C52-9EDF-44D497632EA1
-  Functions: 229
-  Symbols:   200
-  CStrings:  603
+  UUID: 9D4E4378-D3BD-3945-9A84-DECA82A0C7CE
+  Functions: 232
+  Symbols:   203
+  CStrings:  633
 
Symbols:
+ _EXDisplayPipeClose
+ _EXDisplayPipeGetStats
+ _EXDisplayPipeOpen
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
