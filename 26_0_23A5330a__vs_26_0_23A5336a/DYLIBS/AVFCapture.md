## AVFCapture

> `/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`

```diff

-664.2.8.0.1
-  __TEXT.__text: 0x103fa8
+664.2.10.0.0
+  __TEXT.__text: 0x10455c
   __TEXT.__auth_stubs: 0x1b30
-  __TEXT.__objc_methlist: 0xdedc
+  __TEXT.__objc_methlist: 0xdee4
   __TEXT.__const: 0x918
   __TEXT.__gcc_except_tab: 0x24e0
-  __TEXT.__cstring: 0x1d01f
-  __TEXT.__oslogstring: 0x6a96
+  __TEXT.__cstring: 0x1d07b
+  __TEXT.__oslogstring: 0x6c0b
   __TEXT.__dlopen_cstrs: 0x178
   __TEXT.__ustring: 0x54
-  __TEXT.__unwind_info: 0x45f8
+  __TEXT.__unwind_info: 0x4608
   __TEXT.__objc_classname: 0x17d3
-  __TEXT.__objc_methname: 0x26d39
+  __TEXT.__objc_methname: 0x26d58
   __TEXT.__objc_methtype: 0x3c78
   __TEXT.__objc_stubs: 0x16a40
-  __DATA_CONST.__got: 0x27a0
+  __DATA_CONST.__got: 0x27a8
   __DATA_CONST.__const: 0x6fc8
   __DATA_CONST.__objc_classlist: 0x580
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x71a8
+  __DATA_CONST.__objc_selrefs: 0x71b0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x4c0
   __DATA_CONST.__objc_arraydata: 0x428
   __AUTH_CONST.__auth_got: 0xda8
   __AUTH_CONST.__const: 0xa20
-  __AUTH_CONST.__cfstring: 0x13220
+  __AUTH_CONST.__cfstring: 0x13280
   __AUTH_CONST.__objc_const: 0x16850
   __AUTH_CONST.__objc_intobj: 0x9f0
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 11656BA5-C193-356C-AEF3-6CAC07BD1815
-  Functions: 5848
-  Symbols:   20753
-  CStrings:  11627
+  UUID: 7D57F4D4-C18F-309B-877B-2C9255171757
+  Functions: 5851
+  Symbols:   20760
+  CStrings:  11638
 
Symbols:
+ -[AVCaptureFigAudioDevice audioServicesWereResetHandler:]
+ _AVAudioSessionMediaServicesWereResetNotification
+ ___57-[AVCaptureFigAudioDevice audioServicesWereResetHandler:]_block_invoke
+ _fad_isRunningOnDeviceClass
CStrings:
+ "-[AVCaptureFigAudioDevice audioServicesWereResetHandler:]_block_invoke"
+ "<<<< AVCaptureFigAudioDevice >>>> %s: [Routing] %p After audiomxd crash, no available input devices reported by AVIDDS"
+ "<<<< AVCaptureFigAudioDevice >>>> %s: [Routing] %p After audiomxd crash, no built-in mic detected, so setting current mic to %@"
+ "<<<< AVCaptureFigAudioDevice >>>> %s: [Routing] %p Input device changed to nil, DS available inputs count is 0, so we're *forgetting* last committed"
+ "<<<< AVCaptureFigAudioDevice >>>> %s: [Routing] %p Input device changed to nil, and last committed wasn't found in discovery session available inputs, so we're forgetting it"
+ "<<<< AVCaptureFigAudioDevice >>>> %s: [Routing] %p audiomxd recovered from a crash, reasserting PlayAndRecord category"
+ "DeviceClass"
+ "audioServicesWereResetHandler:"
+ "description=CameraCapture_AVF-664.2.10"
+ "iPad"
+ "iPhone"
- "<<<< AVCaptureFigAudioDevice >>>> %s: [Routing] %p Input device changed to nil, DS available inputs count is 0, but carrying on with last committed"
- "<<<< AVCaptureFigAudioDevice >>>> %s: [Routing] %p Input device changed to nil, but last committed wasn't found in discovery session available inputs, so forgetting it"
- "description=CameraCapture_AVF-664.2.8.0.1"

```
