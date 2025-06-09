## gamecontrollerd

> `/usr/libexec/gamecontrollerd`

```diff

-12.5.2.0.0
-  __TEXT.__text: 0x20d0
+13.0.28.0.0
+  __TEXT.__text: 0x222c
   __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_stubs: 0x640
-  __TEXT.__objc_methlist: 0x434
-  __TEXT.__objc_classname: 0xa8
-  __TEXT.__objc_methname: 0xa9d
-  __TEXT.__objc_methtype: 0x5c7
+  __TEXT.__objc_stubs: 0x6a0
+  __TEXT.__objc_methlist: 0x47c
+  __TEXT.__objc_classname: 0xc4
+  __TEXT.__objc_methname: 0xbd7
+  __TEXT.__objc_methtype: 0x632
   __TEXT.__const: 0x20
-  __TEXT.__cstring: 0x2ca
+  __TEXT.__cstring: 0x322
   __TEXT.__oslogstring: 0x1b8
   __TEXT.__gcc_except_tab: 0xfc
   __TEXT.__unwind_info: 0x148
   __DATA_CONST.__auth_got: 0x1d8
-  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__got: 0xd0
   __DATA_CONST.__const: 0x200
-  __DATA_CONST.__cfstring: 0x180
+  __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0xab0
-  __DATA.__objc_selrefs: 0x370
-  __DATA.__objc_ivar: 0x38
+  __DATA.__objc_const: 0xb70
+  __DATA.__objc_selrefs: 0x3b0
+  __DATA.__objc_ivar: 0x44
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x1e8
+  __DATA.__data: 0x248
   __DATA.__bss: 0xc8
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/GameControllerSettings.framework/GameControllerSettings
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E15C5A6D-9056-31A8-A95D-380949136BB8
+  UUID: 625D4E04-A49B-3AB5-A07B-9DF794D21A02
   Functions: 79
-  Symbols:   91
-  CStrings:  271
+  Symbols:   94
+  CStrings:  292
 
Symbols:
+ _OBJC_CLASS_$_GCGameIntentManager
+ _OBJC_CLASS_$_GCSystemButtonServer
+ _OBJC_CLASS_$_IOGCFastPathProxyServer
Functions:
~ sub_10000170c : 504 -> 532
~ sub_100001a18 -> sub_100001a34 : 600 -> 716
~ sub_100001cdc -> sub_100001d6c : 92 -> 108
~ sub_100001da8 -> sub_100001e48 : 232 -> 292
~ sub_100002230 -> sub_10000230c : 388 -> 456
~ sub_1000027fc -> sub_10000291c : 244 -> 304
CStrings:
+ "\r"
+ "@\"<GCSTouchControlsGameConfigs>\"16@0:8"
+ "@\"GCGameIntentManager\""
+ "@\"GCSystemButtonServer\""
+ "GCGameIntentLauncherService"
+ "T@\"<GCSTouchControlsGameConfigs>\",R,N"
+ "_gameIntentManager"
+ "_systemButtonServer"
+ "_systemButtonServiceListener"
+ "acceptConnection:fromProcess:"
+ "activate"
+ "com.apple.GameController.gamecontrollerd"
+ "com.apple.GameController.system-button-service"
+ "hasPairedSpatialController"
+ "initWithServerName:"
+ "launchApplicationWithBundleIdentifier:"
+ "setHasPairedSpatialController:"
+ "togglePlatformGamesLibrary"
+ "touchControlsGameConfigs"
+ "v24@0:8@\"NSString\"16"
- "\n"

```
