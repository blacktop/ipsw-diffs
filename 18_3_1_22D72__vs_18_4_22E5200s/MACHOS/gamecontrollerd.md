## gamecontrollerd

> `/usr/libexec/gamecontrollerd`

```diff

-12.3.1.0.0
-  __TEXT.__text: 0x557c
-  __TEXT.__auth_stubs: 0x430
-  __TEXT.__objc_stubs: 0xd60
-  __TEXT.__objc_methlist: 0x290
-  __TEXT.__objc_classname: 0xe7
-  __TEXT.__objc_methname: 0x1081
-  __TEXT.__objc_methtype: 0x6e3
-  __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x373
-  __TEXT.__oslogstring: 0x382
-  __TEXT.__gcc_except_tab: 0x4e4
-  __TEXT.__unwind_info: 0x1e0
-  __DATA_CONST.__auth_got: 0x228
-  __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__const: 0x348
-  __DATA_CONST.__cfstring: 0x1a0
-  __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x38
+12.4.10.0.0
+  __TEXT.__text: 0x20d0
+  __TEXT.__auth_stubs: 0x390
+  __TEXT.__objc_stubs: 0x640
+  __TEXT.__objc_methlist: 0x434
+  __TEXT.__objc_classname: 0xa8
+  __TEXT.__objc_methname: 0xa9d
+  __TEXT.__objc_methtype: 0x5c7
+  __TEXT.__const: 0x20
+  __TEXT.__cstring: 0x2ca
+  __TEXT.__oslogstring: 0x1b8
+  __TEXT.__gcc_except_tab: 0xfc
+  __TEXT.__unwind_info: 0x148
+  __DATA_CONST.__auth_got: 0x1d8
+  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__const: 0x200
+  __DATA_CONST.__cfstring: 0x180
+  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x18
-  __DATA.__objc_const: 0x16c0
-  __DATA.__objc_selrefs: 0x428
-  __DATA.__objc_ivar: 0x44
-  __DATA.__objc_data: 0x140
-  __DATA.__data: 0x2a8
-  __DATA.__bss: 0xd8
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA.__objc_const: 0xab0
+  __DATA.__objc_selrefs: 0x370
+  __DATA.__objc_ivar: 0x38
+  __DATA.__objc_data: 0xf0
+  __DATA.__data: 0x1e8
+  __DATA.__bss: 0xc8
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/GameControllerSettings.framework/GameControllerSettings
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 113
-  Symbols:   104
-  CStrings:  368
+  Functions: 79
+  Symbols:   91
+  CStrings:  260
 
Symbols:
- _GCBundleWithPID
- _OBJC_CLASS_$_NSMutableArray
- _OBJC_CLASS_$_NSXPCInterface
- __NSConcreteStackBlock
- _objc_copyWeak
- _objc_destroyWeak
- _objc_enumerationMutation
- _objc_initWeak
- _objc_loadWeakRetained
- _objc_release_x24
- _objc_release_x25
- _objc_retainBlock
- _objc_retain_x24
CStrings:
- "\x03"
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
- "countByEnumeratingWithState:objects:count:"
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
- "processIdentifier"
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
