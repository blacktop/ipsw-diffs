## gamecontrollerd

> `/usr/libexec/gamecontrollerd`

```diff

-13.5.1.0.0
-  __TEXT.__text: 0x2110
-  __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_stubs: 0x6a0
-  __TEXT.__objc_methlist: 0x46c
-  __TEXT.__objc_classname: 0xc4
-  __TEXT.__objc_methname: 0xb98
-  __TEXT.__objc_methtype: 0x60b
-  __TEXT.__cstring: 0x309
+14.0.14.0.0
+  __TEXT.__text: 0x1fc8
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__objc_stubs: 0x6e0
+  __TEXT.__objc_methlist: 0x494
+  __TEXT.__objc_classname: 0xc0
+  __TEXT.__objc_methname: 0xc4e
+  __TEXT.__objc_methtype: 0x655
+  __TEXT.__cstring: 0x315
   __TEXT.__oslogstring: 0x19e
-  __TEXT.__gcc_except_tab: 0xf4
+  __TEXT.__gcc_except_tab: 0xb0
   __TEXT.__const: 0x18
-  __TEXT.__unwind_info: 0x178
-  __DATA_CONST.__auth_got: 0x1b8
-  __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0x1c0
-  __DATA_CONST.__cfstring: 0x1c0
+  __TEXT.__unwind_info: 0x118
+  __DATA_CONST.__const: 0x1a0
+  __DATA_CONST.__cfstring: 0x1e0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0xb58
-  __DATA.__objc_selrefs: 0x3a8
-  __DATA.__objc_ivar: 0x44
+  __DATA_CONST.__auth_got: 0x1d0
+  __DATA_CONST.__got: 0xc8
+  __DATA.__objc_const: 0xbb8
+  __DATA.__objc_selrefs: 0x3c8
+  __DATA.__objc_ivar: 0x4c
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x248
-  __DATA.__bss: 0xa8
+  __DATA.__bss: 0x98
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/GameController.framework/GameController
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/GameControllerFoundation.framework/GameControllerFoundation
+  - /System/Library/PrivateFrameworks/GameControllerServer.framework/GameControllerServer
   - /System/Library/PrivateFrameworks/GameControllerSettings.framework/GameControllerSettings
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6D71F679-DC06-36E4-A5F1-7D51E0CC64D1
-  Functions: 75
-  Symbols:   89
-  CStrings:  286
+  UUID: 9F2EBA4A-83F4-3762-8319-EEA056048B85
+  Functions: 72
+  Symbols:   92
+  CStrings:  296
 
Symbols:
+ _OBJC_CLASS_$_GCSettingsServer
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retain
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "@\"<GCSDevices>\"16@0:8"
+ "@\"GCSDevice\"24@0:8@\"NSString\"16"
+ "@\"GCSettingsServer\""
+ "T@\"<GCSDevices>\",R,N"
+ "_settingsServer"
+ "_settingsServiceListener"
+ "acceptNewConnection:forSettingsClient:"
+ "acceptNewConnection:fromClient:"
+ "com.apple.GameController.gamecontrollerd"
+ "deviceForPersistentControllerIdentifier:"
+ "devices"
- "\r"
- "com.apple.GameController.Haptics"

```
