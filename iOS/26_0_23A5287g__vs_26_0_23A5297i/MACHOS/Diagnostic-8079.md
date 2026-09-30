## Diagnostic-8079

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8079.appex/Diagnostic-8079`

```diff

-1066.0.19.502.1
-  __TEXT.__text: 0x81e0
-  __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_stubs: 0x2240
-  __TEXT.__objc_methlist: 0xad4
-  __TEXT.__cstring: 0x632
-  __TEXT.__objc_methname: 0x26e8
+1066.0.41.0.0
+  __TEXT.__text: 0x85b8
+  __TEXT.__auth_stubs: 0x4b0
+  __TEXT.__objc_stubs: 0x2280
+  __TEXT.__objc_methlist: 0xae4
+  __TEXT.__cstring: 0x6be
+  __TEXT.__objc_methname: 0x2718
   __TEXT.__objc_classname: 0x181
   __TEXT.__objc_methtype: 0x2f3
   __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0x118
-  __TEXT.__oslogstring: 0xa46
+  __TEXT.__oslogstring: 0xa9a
   __TEXT.__unwind_info: 0x1f8
-  __DATA_CONST.__auth_got: 0x250
+  __DATA_CONST.__auth_got: 0x268
   __DATA_CONST.__got: 0x160
   __DATA_CONST.__const: 0x238
-  __DATA_CONST.__cfstring: 0xac0
+  __DATA_CONST.__cfstring: 0xc60
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x1798
-  __DATA.__objc_selrefs: 0x9c0
+  __DATA.__objc_selrefs: 0x9d0
   __DATA.__objc_ivar: 0x100
   __DATA.__objc_data: 0x500
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/AXSoundDetection.framework/AXSoundDetection
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
+  - /System/Library/PrivateFrameworks/EXDisplayPipe.framework/EXDisplayPipe
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 763D478C-E816-3CF4-A860-E47F1B49BC56
-  Functions: 221
-  Symbols:   169
-  CStrings:  752
+  UUID: 18203FA1-4764-328F-AA67-858B25CBC472
+  Functions: 224
+  Symbols:   172
+  CStrings:  782
 
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
