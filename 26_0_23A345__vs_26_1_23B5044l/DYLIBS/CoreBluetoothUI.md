## CoreBluetoothUI

> `/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/CoreBluetoothUI`

```diff

-190.51.1.6.0
-  __TEXT.__text: 0x1bd8
-  __TEXT.__auth_stubs: 0x2d0
+191.5.1.1.0
+  __TEXT.__text: 0x1d5c
+  __TEXT.__auth_stubs: 0x2f0
   __TEXT.__objc_methlist: 0x2a8
   __TEXT.__const: 0x50
   __TEXT.__cstring: 0x243
   __TEXT.__gcc_except_tab: 0x1c
-  __TEXT.__oslogstring: 0xfd
+  __TEXT.__oslogstring: 0x13a
   __TEXT.__unwind_info: 0x100
   __TEXT.__objc_classname: 0x83
-  __TEXT.__objc_methname: 0xa10
+  __TEXT.__objc_methname: 0xa24
   __TEXT.__objc_methtype: 0x1e7
   __TEXT.__objc_stubs: 0x980
   __DATA_CONST.__got: 0x98

   __DATA_CONST.__objc_selrefs: 0x2f0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x178
+  __AUTH_CONST.__auth_got: 0x188
   __AUTH_CONST.__cfstring: 0x300
   __AUTH_CONST.__objc_const: 0x4d8
   __AUTH.__objc_data: 0x140

   - /System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 86B4D2B4-3DC8-3FD6-AE92-0506E5A3859C
-  Functions: 50
-  Symbols:   313
-  CStrings:  198
+  UUID: DB6E17CF-8666-3FD5-8C5B-F9FC7C74969A
+  Functions: 52
+  Symbols:   321
+  CStrings:  199
 
Symbols:
+ -[BTDevicePicker createAlertWindowForRootViewController:].cold.1
+ -[BTDevicePicker createAlertWindowForRootViewController:].cold.2
+ _OBJC_CLASS_$_UIWindowScene
+ _OUTLINED_FUNCTION_1
+ __os_log_error_impl
+ _objc_msgSend$activationState
+ _objc_msgSend$connectedScenes
+ _objc_msgSend$initWithWindowScene:
+ _objc_retain_x23
- _OBJC_CLASS_$_UIScreen
- _objc_msgSend$bounds
- _objc_msgSend$initWithFrame:
- _objc_msgSend$mainScreen
Functions:
~ -[BTDevicePicker createAlertWindowForRootViewController:] : 388 -> 700
+ _OUTLINED_FUNCTION_1
~ -[BTDevicePicker dealloc].cold.2 : 52 -> 36
CStrings:
+ "Failed to find an active scene to present the BTDevicePicker"
+ "activationState"
+ "connectedScenes"
+ "initWithWindowScene:"
- "bounds"
- "initWithFrame:"
- "mainScreen"

```
