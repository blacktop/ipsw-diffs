## gamecontrollerd

> `/usr/libexec/gamecontrollerd`

```diff

-12.3.1.0.0
-  __TEXT.__text: 0x6ea4
-  __TEXT.__auth_stubs: 0x3e0
-  __TEXT.__objc_stubs: 0xfc0
-  __TEXT.__objc_methlist: 0x2d8
-  __TEXT.__objc_classname: 0xe7
-  __TEXT.__objc_methname: 0x126b
-  __TEXT.__objc_methtype: 0x720
-  __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x42f
-  __TEXT.__oslogstring: 0x739
-  __TEXT.__gcc_except_tab: 0x63c
-  __TEXT.__unwind_info: 0x230
-  __DATA_CONST.__auth_got: 0x200
-  __DATA_CONST.__got: 0x110
-  __DATA_CONST.__const: 0x3d0
-  __DATA_CONST.__cfstring: 0x200
-  __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x38
+12.4.12.0.0
+  __TEXT.__text: 0x3580
+  __TEXT.__auth_stubs: 0x3d0
+  __TEXT.__objc_stubs: 0x8e0
+  __TEXT.__objc_methlist: 0x47c
+  __TEXT.__objc_classname: 0xa8
+  __TEXT.__objc_methname: 0xcc4
+  __TEXT.__objc_methtype: 0x604
+  __TEXT.__const: 0x30
+  __TEXT.__cstring: 0x386
+  __TEXT.__oslogstring: 0x56f
+  __TEXT.__gcc_except_tab: 0x258
+  __TEXT.__unwind_info: 0x1a8
+  __DATA_CONST.__auth_got: 0x1f8
+  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__const: 0x260
+  __DATA_CONST.__cfstring: 0x1e0
+  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x18
-  __DATA.__objc_const: 0x1700
-  __DATA.__objc_selrefs: 0x4b0
-  __DATA.__objc_ivar: 0x4c
-  __DATA.__objc_data: 0x140
-  __DATA.__data: 0x2a8
-  __DATA.__bss: 0xd8
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA.__objc_const: 0xaf0
+  __DATA.__objc_selrefs: 0x400
+  __DATA.__objc_ivar: 0x40
+  __DATA.__objc_data: 0xf0
+  __DATA.__data: 0x1e8
+  __DATA.__bss: 0xc8
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/GameControllerSettings.framework/Versions/A/GameControllerSettings
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 857A916A-ADD6-3D50-BA8C-9987A5071BB2
-  Functions: 139
-  Symbols:   107
-  CStrings:  425
+  UUID: 0F3E684E-5F27-3D16-8BAA-5FEB7381C690
+  Functions: 98
+  Symbols:   104
+  CStrings:  319
 
Symbols:
- _GCBundleWithPID
- _OBJC_CLASS_$_NSMutableArray
- _OBJC_CLASS_$_NSXPCInterface
CStrings:
- "/System/Library/PrivateFrameworks/MediaRemote.framework/Support"
- "@\"NSMutableArray\""
- "@\"NSXPCConnection\""
- "GCDGameControllerDaemonDelegate"
- "GameControllerClientProtocol"
- "New connection '%@' for listener '%@' from %@"
- "Stopping..."
- "UDID:%ld, digitizerXY:%.1f,%.1f, touchDown:%d"
- "_appConnections"
- "_foregroundAppConnections"
- "_mediaremoted"
- "acceptNewConnectionFromGCEnabledApp: %@"
- "acceptNewConnectionFromMediaRemote:"
- "acceptNewConnectionFromMediaRemote: %@"
- "addController:"
- "addController:%@ for hash:%lu"
- "addController:forward:"
- "addControllerForAppStoreRemote:"
- "appDidEnterBackground"
- "appDidEnterBackgroundWithPID:"
- "appDidEnterBackgroundWithPID:%d"
- "appWillEnterForeground"
- "appWillEnterForegroundWithPID:"
- "appWillEnterForegroundWithPID:%d"
- "attitude"
- "buttonA"
- "buttonB"
- "buttonHome"
- "buttonMenu"
- "buttonOptions"
- "buttonX"
- "buttonY"
- "containsObject:"
- "containsString:"
- "controllerDidConnect:"
- "controllerDidDisconnect:"
- "controllerWithUDID:setArrayValue:forElement:forward:"
- "controllerWithUDID:setData:"
- "controllerWithUDID:setValue0:setValue1:setValue2:setValue3:forElement:"
- "controllerWithUDID:setValue:forElement:"
- "controllerWithUDID:setValue:forElement:forward:"
- "deviceHash"
- "down"
- "dpad"
- "extendedGamepad"
- "gamepad"
- "gravity"
- "interfaceWithProtocol:"
- "isATVRemote"
- "left"
- "leftShoulder"
- "leftThumbstick"
- "leftThumbstickButton"
- "leftTrigger"
- "microControllerWithDigitizerX called unexpectedly. NO-OP"
- "microControllerWithDigitizerX:withY:withTimeStamp:touchDown:"
- "microControllerWithUDID:setDigitizerX:digitizerY:withTimeStamp:touchDown:"
- "motion"
- "object"
- "ping"
- "processMicroControllerWithUDID:setDigitizerX:withY:withTimeStamp:touchDown:"
- "remoteObjectProxy"
- "remoteObjectProxyWithErrorHandler:"
- "removeController:"
- "removeController:%@ for hash: %lu"
- "removeController:forward:"
- "resourcePath"
- "right"
- "rightShoulder"
- "rightThumbstick"
- "rightThumbstickButton"
- "rightTrigger"
- "rotationRate"
- "setControllerPausedHandler:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setRemoteObjectInterface:"
- "setValueChangedHandler:"
- "shouldKeepRunning"
- "udid:%ld, value:%f, element:%d"
- "up"
- "userAcceleration"
- "v16@?0@\"GCController\"8"
- "v16@?0@\"GCMotion\"8"
- "v16@?0@\"NSError\"8"
- "v20@0:8i16"
- "v24@0:8@\"GCController\"16"
- "v24@?0@\"GCControllerButtonInput\"8f16B20"
- "v28@0:8@\"GCController\"16B24"
- "v28@0:8@16B24"
- "v32@0:8Q16@\"NSData\"24"
- "v32@0:8Q16@24"
- "v32@0:8Q16f24i28"
- "v36@0:8Q16f24i28B32"
- "v36@0:8f16f20Q24B32"
- "v44@0:8Q16f24f28Q32B40"
- "v44@0:8Q16f24f28f32f36i40"
- "v48@0:8Q16{?=[4f]}24i40B44"

```
