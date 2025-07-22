## Diagnostic-4153

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4153.appex/Diagnostic-4153`

```diff

-1066.0.19.502.1
-  __TEXT.__text: 0x7c70
-  __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_stubs: 0x2340
-  __TEXT.__objc_methlist: 0xb90
-  __TEXT.__cstring: 0x332
+1066.0.41.0.0
+  __TEXT.__text: 0x8048
+  __TEXT.__auth_stubs: 0x3a0
+  __TEXT.__objc_stubs: 0x2380
+  __TEXT.__objc_methlist: 0xba0
+  __TEXT.__cstring: 0x3b3
+  __TEXT.__oslogstring: 0x282
   __TEXT.__objc_classname: 0x13e
   __TEXT.__objc_methtype: 0xbd4
-  __TEXT.__objc_methname: 0x2b83
+  __TEXT.__objc_methname: 0x2bb3
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x7c
-  __TEXT.__oslogstring: 0x22e
-  __TEXT.__unwind_info: 0x1a8
-  __DATA_CONST.__auth_got: 0x1c8
+  __TEXT.__unwind_info: 0x1b0
+  __DATA_CONST.__auth_got: 0x1e0
   __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__const: 0x1b8
-  __DATA_CONST.__cfstring: 0x740
+  __DATA_CONST.__cfstring: 0x8c0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA.__objc_const: 0x1118
-  __DATA.__objc_selrefs: 0xbe0
+  __DATA.__objc_selrefs: 0xbf0
   __DATA.__objc_ivar: 0xd0
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x2a0

   - /System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
+  - /System/Library/PrivateFrameworks/EXDisplayPipe.framework/EXDisplayPipe
   - /System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9CD5349F-F276-39A2-94F3-5790BEDC5863
-  Functions: 189
-  Symbols:   160
-  CStrings:  738
+  UUID: A13C57FC-E061-38AB-B2B2-8E94012C9929
+  Functions: 192
+  Symbols:   163
+  CStrings:  766
 
Symbols:
+ _EXDisplayPipeClose
+ _EXDisplayPipeGetStats
+ _EXDisplayPipeOpen
CStrings:
+ "Failed to get ExDisplayPipe status!"
+ "Failed to open ExDisplayPipe client for status!"
+ "_exDisplayPipeStats"
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
