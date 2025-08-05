## AXSoundDetectionUI

> `/System/Library/PrivateFrameworks/AXSoundDetectionUI.framework/AXSoundDetectionUI`

```diff

-406.1.3.0.0
-  __TEXT.__text: 0x2380c
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0x1a10
+406.1.12.0.0
+  __TEXT.__text: 0x23a28
+  __TEXT.__auth_stubs: 0x680
+  __TEXT.__objc_methlist: 0x1a3c
   __TEXT.__const: 0xa0
   __TEXT.__gcc_except_tab: 0x268
-  __TEXT.__oslogstring: 0x4136
-  __TEXT.__cstring: 0xffd
+  __TEXT.__oslogstring: 0x41db
+  __TEXT.__cstring: 0x105d
   __TEXT.__dlopen_cstrs: 0xd4
-  __TEXT.__unwind_info: 0x980
+  __TEXT.__unwind_info: 0x988
   __TEXT.__objc_classname: 0x440
-  __TEXT.__objc_methname: 0x4b12
+  __TEXT.__objc_methname: 0x4b3e
   __TEXT.__objc_methtype: 0xd4c
-  __TEXT.__objc_stubs: 0x44a0
+  __TEXT.__objc_stubs: 0x44c0
   __DATA_CONST.__got: 0x1b0
   __DATA_CONST.__const: 0x6f8
   __DATA_CONST.__objc_classlist: 0xb8

   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x5408
-  __DATA_CONST.__objc_selrefs: 0x1428
+  __DATA_CONST.__objc_selrefs: 0x1438
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__objc_const: 0xaa0
   __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x1320
+  __AUTH_CONST.__cfstring: 0x1380
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x338
+  __AUTH_CONST.__auth_got: 0x350
   __AUTH.__objc_data: 0x730
   __AUTH.__data: 0x10
   __DATA.__objc_classrefs: 0x290

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 604BDDF3-3166-3534-8E52-67F037880159
-  Functions: 951
-  Symbols:   3279
-  CStrings:  1667
+  UUID: 9252DF28-AA0F-3D63-9538-5B8C4C8A41B3
+  Functions: 956
+  Symbols:   3293
+  CStrings:  1677
 
Symbols:
+ -[AXSDCustomDetectionController containsCustomDetector:]
+ -[AXSDDetectorQueueManager containsListenType:]
+ -[AXSDListenEngine audioEngineInputNode].cold.2
+ -[AXSDSoundDetectionController containsListenType:]
+ _AXDeviceIsPad
+ _AXDeviceIsPhone
+ _MGGetBoolAnswer
+ ___38-[AXSDListenEngine addListenDelegate:]_block_invoke.17
+ ___38-[AXSDListenEngine addListenDelegate:]_block_invoke.18
+ ___41-[AXSDListenEngine removeListenDelegate:]_block_invoke.21
+ ___49-[AXSDListenEngine _carPlayIsConnectedDidChange:]_block_invoke.94
+ _objc_msgSend$containsListenType:
- ___38-[AXSDListenEngine addListenDelegate:]_block_invoke.10
- ___38-[AXSDListenEngine addListenDelegate:]_block_invoke.11
- ___41-[AXSDListenEngine removeListenDelegate:]_block_invoke.14
- ___49-[AXSDListenEngine _carPlayIsConnectedDidChange:]_block_invoke.85
CStrings:
+ "AXSDListenEngine state is currently in an interrupt state, so can't handle configuration change"
+ "DeviceSupportsUSBTypeC"
+ "KeyboardMutePreservesRegionalShutterClickBehavior"
+ "Trying to access audioEngineInputNode on a non-existant audio engine"
+ "YiUtBQygkHRhLcdO3LFB4A"
+ "containsCustomDetector:"
+ "containsListenType:"

```
