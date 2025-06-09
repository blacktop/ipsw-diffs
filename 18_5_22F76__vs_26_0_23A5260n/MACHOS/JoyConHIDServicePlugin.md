## JoyConHIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/JoyConHIDServicePlugin.plugin/JoyConHIDServicePlugin`

```diff

-12.5.2.0.0
-  __TEXT.__text: 0x15d90
+13.0.28.0.0
+  __TEXT.__text: 0x15d98
   __TEXT.__auth_stubs: 0x650
   __TEXT.__objc_stubs: 0x19a0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xd7c
+  __TEXT.__objc_methlist: 0xdac
   __TEXT.__cstring: 0xbe1
   __TEXT.__objc_classname: 0x2ec
-  __TEXT.__objc_methname: 0x25fe
-  __TEXT.__objc_methtype: 0x164b
+  __TEXT.__objc_methname: 0x2611
+  __TEXT.__objc_methtype: 0x168e
   __TEXT.__const: 0x1e4
   __TEXT.__gcc_except_tab: 0x1d0c
   __TEXT.__oslogstring: 0x15c3

   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x1b08
-  __DATA.__objc_selrefs: 0x970
+  __DATA.__objc_const: 0x1b60
+  __DATA.__objc_selrefs: 0x980
   __DATA.__objc_ivar: 0x168
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x840

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C6FB9648-35B6-3C17-83CF-DFD817872BD9
-  Functions: 499
+  UUID: EA7057DA-2FA4-309E-8AA1-F5DBE6B22F9C
+  Functions: 500
   Symbols:   149
-  CStrings:  1053
+  CStrings:  1059
 
Functions:
~ sub_47c4 : 132 -> 8
+ sub_47cc
CStrings:
+ "handleButton:gesture:"
+ "requestIdleDisconnect:"
+ "sendPressForButton:"
+ "setConfiguration:forButton:"
+ "setHIDEventService:"
+ "v20@0:8I16"
+ "v24@0:8@\"HIDEventService\"16"
+ "v28@0:8I16Q20"
+ "v28@0:8Q16I24"
- "requestIdleDiconnect:"
- "setEnableGlobalGameControllerFunctionality:"
- "triggerGameIntentWithEvent:"

```
