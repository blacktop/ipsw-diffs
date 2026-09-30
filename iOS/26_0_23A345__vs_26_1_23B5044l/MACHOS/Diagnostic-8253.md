## Diagnostic-8253

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8253.appex/Diagnostic-8253`

```diff

-56.0.0.0.0
-  __TEXT.__text: 0x128a0
-  __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_stubs: 0x780
-  __TEXT.__objc_methlist: 0xe0
-  __TEXT.__gcc_except_tab: 0x2098
+57.0.0.0.0
+  __TEXT.__text: 0x12f88
+  __TEXT.__auth_stubs: 0x700
+  __TEXT.__objc_stubs: 0x820
+  __TEXT.__objc_methlist: 0xf8
+  __TEXT.__gcc_except_tab: 0x2220
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x3a72
+  __TEXT.__cstring: 0x3baf
   __TEXT.__objc_classname: 0x20
-  __TEXT.__objc_methname: 0x5a1
+  __TEXT.__objc_methname: 0x60a
   __TEXT.__objc_methtype: 0x7bd
-  __TEXT.__unwind_info: 0x5a8
-  __DATA_CONST.__auth_got: 0x378
+  __TEXT.__unwind_info: 0x5c8
+  __DATA_CONST.__auth_got: 0x390
   __DATA_CONST.__got: 0x320
   __DATA_CONST.__const: 0x4f8
-  __DATA_CONST.__cfstring: 0x2fa0
+  __DATA_CONST.__cfstring: 0x3220
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x120
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x258
-  __DATA.__objc_selrefs: 0x208
-  __DATA.__objc_ivar: 0x38
+  __DATA.__objc_const: 0x278
+  __DATA.__objc_selrefs: 0x230
+  __DATA.__objc_ivar: 0x3c
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/AppleDepthCore.framework/AppleDepthCore
   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
+  - /System/Library/PrivateFrameworks/EXDisplayPipe.framework/EXDisplayPipe
   - /System/Library/PrivateFrameworks/H10ISPServices.framework/H10ISPServices
   - /System/Library/PrivateFrameworks/PeridotDepth.framework/PeridotDepth
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 56C294AB-6E7E-3EFB-A17E-305A035FC02B
-  Functions: 204
-  Symbols:   351
-  CStrings:  921
+  UUID: 41356E9D-A9B9-36CC-BEC6-F2DC539576E8
+  Functions: 207
+  Symbols:   355
+  CStrings:  967
 
Symbols:
+ _EXDisplayPipeClose
+ _EXDisplayPipeGetStats
+ _EXDisplayPipeOpen
+ __Z13ecStatusCheckv
+ __Z18ecDisplayPipeStatsv
- __Z18ecPearlStatusCheckv
CStrings:
+ "Exclave"
+ "Exclave Display Pipes Stats"
+ "Exclave returne code"
+ "ExclavesStatus: %@"
+ "Failed to get ExDisplayPipe status!"
+ "Failed to open ExDisplayPipe client for status!"
+ "N/A"
+ "brightness"
+ "copy"
+ "dcpTransportHealth"
+ "detecting exclave value %@ %d"
+ "getEcPipeStats"
+ "getEcStatus"
+ "globalHealth"
+ "link"
+ "m_exclaveStatus"
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
+ "\xb1qq"
- "\xb1qa"

```
