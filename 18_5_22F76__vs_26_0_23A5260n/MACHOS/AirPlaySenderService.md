## AirPlaySenderService

> `/System/Library/PrivateFrameworks/AirPlaySenderKit.framework/XPCServices/AirPlaySenderService.xpc/AirPlaySenderService`

```diff

-860.7.1.0.0
-  __TEXT.__text: 0x85d8
-  __TEXT.__auth_stubs: 0xad0
+890.61.4.11.2
+  __TEXT.__text: 0x8658
+  __TEXT.__auth_stubs: 0xb00
   __TEXT.__objc_stubs: 0x240
   __TEXT.__objc_methlist: 0xb0
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x1d73
+  __TEXT.__cstring: 0x1ef6
   __TEXT.__gcc_except_tab: 0x7c
   __TEXT.__objc_methname: 0x1ef
   __TEXT.__objc_classname: 0x15
   __TEXT.__objc_methtype: 0xa1
-  __TEXT.__unwind_info: 0x230
-  __DATA_CONST.__auth_got: 0x578
+  __TEXT.__unwind_info: 0x238
+  __DATA_CONST.__auth_got: 0x590
   __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__const: 0x6f0
-  __DATA_CONST.__cfstring: 0xc0
+  __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3A36139B-3FBD-3595-A1BB-B783475241E5
-  Functions: 244
-  Symbols:   237
-  CStrings:  237
+  UUID: F2C8758B-9BFE-368F-B47B-31E2D1557ACB
+  Functions: 245
+  Symbols:   240
+  CStrings:  240
 
Symbols:
+ _CVBufferCopyAttachment
+ _CVBufferSetAttachment
+ _LogControl
Functions:
~ sub_100001534 : 1024 -> 1088
~ _main : 36 -> 40
+ sub_100006600
CStrings:
+ "?AirPlayClientCore:level=info,AirPlayEndpointCore:level=info,APAudioEngine:level=info,APBrowser:level=info,APBrowserBTLEManager:level=info,APBonjourBrowser:level=info,APBrowserController:level=info,APEndpoint:level=info,APEndpointManager:level=info,APEndpointStreamAudio:level=info,APEndpointStreamScreen:level=info,APSenderSessionAirPlay:level=info,AirPlayPairing:level=info"
+ "FVDFrameUserData"
+ "void serviceSetupSandbox(void)"
- "void serviceSetupTempDirectory(void)"

```
