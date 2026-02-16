## ScreenSharingServer

> `/System/Library/CoreServices/ScreenSharingServer.app/ScreenSharingServer`

```diff

-138.1.0.0.0
-  __TEXT.__text: 0x42438
-  __TEXT.__auth_stubs: 0xe50
+144.1.0.0.0
+  __TEXT.__text: 0x44308
+  __TEXT.__auth_stubs: 0xe00
   __TEXT.__objc_stubs: 0x45e0
   __TEXT.__objc_methlist: 0x1cfc
-  __TEXT.__const: 0xe2
+  __TEXT.__const: 0xf2
   __TEXT.__objc_methname: 0x5f28
-  __TEXT.__cstring: 0xb11e
+  __TEXT.__cstring: 0xb64e
   __TEXT.__oslogstring: 0x7495
   __TEXT.__objc_classname: 0x2c8
   __TEXT.__objc_methtype: 0x3183
   __TEXT.__gcc_except_tab: 0x3e0
-  __TEXT.__unwind_info: 0x558
-  __DATA_CONST.__auth_got: 0x738
+  __TEXT.__unwind_info: 0x5a8
+  __DATA_CONST.__auth_got: 0x710
   __DATA_CONST.__got: 0x3f0
-  __DATA_CONST.__const: 0x688
+  __DATA_CONST.__const: 0x678
   __DATA_CONST.__cfstring: 0x1d80
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
   - /usr/lib/swift/libswiftCore.dylib
-  - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
-  - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 97972374-67BE-34D1-BE90-6EFA5D99A191
-  Functions: 614
-  Symbols:   372
+  UUID: AEF7B215-2840-3A9D-A760-9358FB161477
+  Functions: 616
+  Symbols:   365
   CStrings:  3569
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- __swift_FORCE_LOAD_$_swiftDispatch
- __swift_FORCE_LOAD_$_swiftXPC
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
CStrings:
+ "/Library/Caches/com.apple.xbs/5260A680-BEF9-4D7A-813C-CBBCFCE74F9B/TemporaryDirectory.WPEUIF/Sources/EmbeddedScreenSharingServer/Pause.c"
+ "/Library/Caches/com.apple.xbs/5260A680-BEF9-4D7A-813C-CBBCFCE74F9B/TemporaryDirectory.WPEUIF/Sources/EmbeddedScreenSharingServer/RFBCommon/AuthRandom.c"
+ "/Library/Caches/com.apple.xbs/5260A680-BEF9-4D7A-813C-CBBCFCE74F9B/TemporaryDirectory.WPEUIF/Sources/EmbeddedScreenSharingServer/RFBCommon/NWConnectionManager.m"
+ "/Library/Caches/com.apple.xbs/5260A680-BEF9-4D7A-813C-CBBCFCE74F9B/TemporaryDirectory.WPEUIF/Sources/EmbeddedScreenSharingServer/RFBCommon/NetBuffer.c"
+ "/Library/Caches/com.apple.xbs/5260A680-BEF9-4D7A-813C-CBBCFCE74F9B/TemporaryDirectory.WPEUIF/Sources/EmbeddedScreenSharingServer/RFBCommon/UDPUtils.c"
+ "/Library/Caches/com.apple.xbs/5260A680-BEF9-4D7A-813C-CBBCFCE74F9B/TemporaryDirectory.WPEUIF/Sources/EmbeddedScreenSharingServer/common/Log.m"
+ "/Library/Caches/com.apple.xbs/5260A680-BEF9-4D7A-813C-CBBCFCE74F9B/TemporaryDirectory.WPEUIF/Sources/EmbeddedScreenSharingServer/common/RDSemaphore.c"
+ "/Library/Caches/com.apple.xbs/5260A680-BEF9-4D7A-813C-CBBCFCE74F9B/TemporaryDirectory.WPEUIF/Sources/EmbeddedScreenSharingServer/common/RDThread.c"
+ "/Library/Caches/com.apple.xbs/5260A680-BEF9-4D7A-813C-CBBCFCE74F9B/TemporaryDirectory.WPEUIF/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/IDSServiceEmbeddedController.m"
+ "/Library/Caches/com.apple.xbs/5260A680-BEF9-4D7A-813C-CBBCFCE74F9B/TemporaryDirectory.WPEUIF/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/IDSSessionEmbeddedControllerAppleCare.m"
+ "/Library/Caches/com.apple.xbs/5260A680-BEF9-4D7A-813C-CBBCFCE74F9B/TemporaryDirectory.WPEUIF/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/IDSSessionEmbeddedControllerBase.m"
+ "/Library/Caches/com.apple.xbs/5260A680-BEF9-4D7A-813C-CBBCFCE74F9B/TemporaryDirectory.WPEUIF/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/IDSSessionEmbeddedControllerShareSettings.m"
+ "/Library/Caches/com.apple.xbs/5260A680-BEF9-4D7A-813C-CBBCFCE74F9B/TemporaryDirectory.WPEUIF/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/SSAVCMediaStreamController.m"
+ "/Library/Caches/com.apple.xbs/5260A680-BEF9-4D7A-813C-CBBCFCE74F9B/TemporaryDirectory.WPEUIF/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/SSAnnotationRenderer.m"
+ "/Library/Caches/com.apple.xbs/5260A680-BEF9-4D7A-813C-CBBCFCE74F9B/TemporaryDirectory.WPEUIF/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/SSAssistanceHelper.m"
+ "/Library/Caches/com.apple.xbs/5260A680-BEF9-4D7A-813C-CBBCFCE74F9B/TemporaryDirectory.WPEUIF/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/ShareSettingsInfo.m"
+ "/Library/Caches/com.apple.xbs/5260A680-BEF9-4D7A-813C-CBBCFCE74F9B/TemporaryDirectory.WPEUIF/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/TouchEventMonitor.m"
+ "/Library/Caches/com.apple.xbs/5260A680-BEF9-4D7A-813C-CBBCFCE74F9B/TemporaryDirectory.WPEUIF/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/UDPReceiver.c"
+ "/Library/Caches/com.apple.xbs/5260A680-BEF9-4D7A-813C-CBBCFCE74F9B/TemporaryDirectory.WPEUIF/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/UDPSend.c"
+ "/Library/Caches/com.apple.xbs/5260A680-BEF9-4D7A-813C-CBBCFCE74F9B/TemporaryDirectory.WPEUIF/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/VNCServer.m"
+ "/Library/Caches/com.apple.xbs/5260A680-BEF9-4D7A-813C-CBBCFCE74F9B/TemporaryDirectory.WPEUIF/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/ViewerMessages.c"
- "/Library/Caches/com.apple.xbs/Sources/EmbeddedScreenSharingServer/Pause.c"
- "/Library/Caches/com.apple.xbs/Sources/EmbeddedScreenSharingServer/RFBCommon/AuthRandom.c"
- "/Library/Caches/com.apple.xbs/Sources/EmbeddedScreenSharingServer/RFBCommon/NWConnectionManager.m"
- "/Library/Caches/com.apple.xbs/Sources/EmbeddedScreenSharingServer/RFBCommon/NetBuffer.c"
- "/Library/Caches/com.apple.xbs/Sources/EmbeddedScreenSharingServer/RFBCommon/UDPUtils.c"
- "/Library/Caches/com.apple.xbs/Sources/EmbeddedScreenSharingServer/common/Log.m"
- "/Library/Caches/com.apple.xbs/Sources/EmbeddedScreenSharingServer/common/RDSemaphore.c"
- "/Library/Caches/com.apple.xbs/Sources/EmbeddedScreenSharingServer/common/RDThread.c"
- "/Library/Caches/com.apple.xbs/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/IDSServiceEmbeddedController.m"
- "/Library/Caches/com.apple.xbs/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/IDSSessionEmbeddedControllerAppleCare.m"
- "/Library/Caches/com.apple.xbs/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/IDSSessionEmbeddedControllerBase.m"
- "/Library/Caches/com.apple.xbs/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/IDSSessionEmbeddedControllerShareSettings.m"
- "/Library/Caches/com.apple.xbs/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/SSAVCMediaStreamController.m"
- "/Library/Caches/com.apple.xbs/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/SSAnnotationRenderer.m"
- "/Library/Caches/com.apple.xbs/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/SSAssistanceHelper.m"
- "/Library/Caches/com.apple.xbs/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/ShareSettingsInfo.m"
- "/Library/Caches/com.apple.xbs/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/TouchEventMonitor.m"
- "/Library/Caches/com.apple.xbs/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/UDPReceiver.c"
- "/Library/Caches/com.apple.xbs/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/UDPSend.c"
- "/Library/Caches/com.apple.xbs/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/VNCServer.m"
- "/Library/Caches/com.apple.xbs/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/ViewerMessages.c"

```
