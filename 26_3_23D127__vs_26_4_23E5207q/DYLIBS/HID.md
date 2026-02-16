## HID

> `/System/Library/PrivateFrameworks/HID.framework/HID`

```diff

-2222.80.22.0.0
-  __TEXT.__text: 0x8fcc
-  __TEXT.__auth_stubs: 0xe20
-  __TEXT.__objc_methlist: 0x1c8c
-  __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x1b90
-  __TEXT.__gcc_except_tab: 0x5c
-  __TEXT.__oslogstring: 0x33e
-  __TEXT.__unwind_info: 0x620
+2238.100.58.0.0
+  __TEXT.__text: 0x98b8
+  __TEXT.__auth_stubs: 0xe40
+  __TEXT.__objc_methlist: 0x1cc4
+  __TEXT.__const: 0x70
+  __TEXT.__cstring: 0x1ca7
+  __TEXT.__gcc_except_tab: 0x48
+  __TEXT.__oslogstring: 0x36c
+  __TEXT.__unwind_info: 0x660
   __TEXT.__objc_classname: 0x511
-  __TEXT.__objc_methname: 0x3368
-  __TEXT.__objc_methtype: 0x6ae
-  __TEXT.__objc_stubs: 0xaa0
-  __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0x448
+  __TEXT.__objc_methname: 0x341b
+  __TEXT.__objc_methtype: 0x6c2
+  __TEXT.__objc_stubs: 0xba0
+  __DATA_CONST.__got: 0xd0
+  __DATA_CONST.__const: 0x470
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1118
+  __DATA_CONST.__objc_selrefs: 0x1168
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x720
+  __AUTH_CONST.__auth_got: 0x730
   __AUTH_CONST.__cfstring: 0x880
-  __AUTH_CONST.__objc_const: 0xe30
+  __AUTH_CONST.__objc_const: 0xe40
   __AUTH_CONST.__objc_intobj: 0x558
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0x78
   __DATA.__objc_ivar: 0xa0
   __DATA.__data: 0x1900
-  __DATA_DIRTY.__objc_data: 0x1b8
+  __DATA_DIRTY.__objc_data: 0x230
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/TimeSync.framework/TimeSync
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D7E828B0-3665-359C-8CFC-002239F69518
-  Functions: 666
-  Symbols:   1888
-  CStrings:  1177
+  UUID: AAB00648-E5B0-33BA-8AFC-58C40617ED73
+  Functions: 682
+  Symbols:   1934
+  CStrings:  1195
 
Symbols:
+ -[HIDDevice(HIDFramework) handlePropertyChange]
+ -[HIDDevice(HIDFramework) setPropertyChangeHandler:forKey:error:]
+ -[HIDDevice(HIDFramework) setPropertyChangeHandler:forKey:error:].cold.1
+ -[HIDDevice(HIDFramework) setPropertyChangeHandler:forKey:error:].cold.2
+ -[HIDDevice(HIDFramework) setPropertyChangeHandler:forKey:error:].cold.3
+ -[HIDDevice(HIDFramework) setupPropertyNotifications]
+ -[HIDDevice(HIDFramework) setupPropertyNotifications].cold.1
+ -[HIDEvent(HIDFramework) isUserInput]
+ _HIDDevicePropertyChangeCallback
+ _OBJC_CLASS_$_NSNull
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ ___35-[HIDDevice(HIDFramework) activate]_block_invoke
+ _kAllowedPropertyKeys
+ _objc_msgSend$copy
+ _objc_msgSend$dictionary
+ _objc_msgSend$handlePropertyChange
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$null
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$setupPropertyNotifications
+ _objc_msgSend$stringWithUTF8String:
+ _objc_release_x25
+ _objc_release_x27
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x23
+ _objc_retain_x25
- _objc_claimAutoreleasedReturnValue
- _objc_release_x26
- _objc_retain_x3
CStrings:
+ "B40@0:8@?16@24o^@32"
+ "BLETimesyncInfo"
+ "DeviceOpenedByEventSystem"
+ "Failed to set up property notifications: 0x%x"
+ "assertion failure: Device has already been activated/cancelled."
+ "assertion failure: Failed to setPropertyChangeHandler, dispatch queue not set"
+ "assertion failure: property change handler already set"
+ "copy"
+ "dictionary"
+ "handlePropertyChange"
+ "isApprovedCarPlayDeviceHIDRMDeviceState"
+ "isEqualToString:"
+ "isUserInput"
+ "null"
+ "removeObjectForKey:"
+ "setPropertyChangeHandler:forKey:error:"
+ "setupPropertyNotifications"
+ "stringWithUTF8String:"

```
