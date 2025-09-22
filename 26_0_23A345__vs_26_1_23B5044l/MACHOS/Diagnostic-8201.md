## Diagnostic-8201

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8201.appex/Diagnostic-8201`

```diff

-56.0.0.0.0
-  __TEXT.__text: 0x26094
-  __TEXT.__auth_stubs: 0x800
-  __TEXT.__objc_stubs: 0xa00
+57.0.0.0.0
+  __TEXT.__text: 0x26530
+  __TEXT.__auth_stubs: 0x830
+  __TEXT.__objc_stubs: 0xa60
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x31c
-  __TEXT.__gcc_except_tab: 0x2598
+  __TEXT.__objc_methlist: 0x324
+  __TEXT.__gcc_except_tab: 0x26c4
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x5869
+  __TEXT.__cstring: 0x5954
   __TEXT.__objc_classname: 0x55
-  __TEXT.__objc_methname: 0xb71
+  __TEXT.__objc_methname: 0xba1
   __TEXT.__objc_methtype: 0x657
   __TEXT.__oslogstring: 0x99e
-  __TEXT.__unwind_info: 0x738
-  __DATA_CONST.__auth_got: 0x410
+  __TEXT.__unwind_info: 0x750
+  __DATA_CONST.__auth_got: 0x428
   __DATA_CONST.__got: 0x350
   __DATA_CONST.__const: 0x558
-  __DATA_CONST.__cfstring: 0x3b40
+  __DATA_CONST.__cfstring: 0x3d20
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x638
-  __DATA.__objc_selrefs: 0x390
+  __DATA.__objc_selrefs: 0x3a8
   __DATA.__objc_ivar: 0x68
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
+  - /System/Library/PrivateFrameworks/EXDisplayPipe.framework/EXDisplayPipe
   - /System/Library/PrivateFrameworks/H10ISPServices.framework/H10ISPServices
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libFDR.dylib

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ABDF7AC7-584E-3BBC-8EA4-D70E8B195B5A
-  Functions: 462
-  Symbols:   411
-  CStrings:  1432
+  UUID: 5BB64073-DA0F-3783-9DDC-D2A541B2AED8
+  Functions: 464
+  Symbols:   415
+  CStrings:  1465
 
Symbols:
+ _EXDisplayPipeClose
+ _EXDisplayPipeGetStats
+ _EXDisplayPipeOpen
+ __Z13ecStatusCheckv
+ __Z18ecDisplayPipeStatsv
- __Z18ecPearlStatusCheckv
CStrings:
+ "Exclave Display Pipes Stats"
+ "Failed to get ExDisplayPipe status!"
+ "Failed to open ExDisplayPipe client for status!"
+ "brightness"
+ "copy"
+ "dcpTransportHealth"
+ "getEcPipeStats"
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
