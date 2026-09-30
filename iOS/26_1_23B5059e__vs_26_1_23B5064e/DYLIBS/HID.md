## HID

> `/System/Library/PrivateFrameworks/HID.framework/HID`

```diff

-2222.40.9.0.0
-  __TEXT.__text: 0x8fd8
+2222.40.11.0.0
+  __TEXT.__text: 0x8fcc
   __TEXT.__auth_stubs: 0xe20
   __TEXT.__objc_methlist: 0x1c8c
   __TEXT.__const: 0x78
   __TEXT.__cstring: 0x1b90
   __TEXT.__gcc_except_tab: 0x5c
-  __TEXT.__oslogstring: 0x34f
-  __TEXT.__unwind_info: 0x618
+  __TEXT.__oslogstring: 0x33e
+  __TEXT.__unwind_info: 0x620
   __TEXT.__objc_classname: 0x511
   __TEXT.__objc_methname: 0x3368
   __TEXT.__objc_methtype: 0x6ae

   - /System/Library/PrivateFrameworks/TimeSync.framework/TimeSync
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9D82B325-E022-3B64-9FD2-63C9D7408BF4
+  UUID: FD3EE176-B3D9-3310-8934-CB07EAEDC275
   Functions: 666
-  Symbols:   1890
+  Symbols:   1888
   CStrings:  1177
 
Symbols:
- _OUTLINED_FUNCTION_7
Functions:
~ -[HIDTimeSync activate] : 316 -> 332
~ -[HIDTimeSync registerPropertyNotification:] : 216 -> 204
~ -[HIDTimeSync dealloc].cold.1 : 160 -> 180
~ -[HIDTimeSync registerPropertyNotification:].cold.1 : 156 -> 120
CStrings:
+ "IOServiceAddInterestNotification 0x%x"
- "assertion failure: IOServiceAddInterestNotification:%x"

```
