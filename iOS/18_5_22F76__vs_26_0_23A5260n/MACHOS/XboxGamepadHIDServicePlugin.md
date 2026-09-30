## XboxGamepadHIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/XboxGamepadHIDServicePlugin.plugin/XboxGamepadHIDServicePlugin`

```diff

-12.5.2.0.0
-  __TEXT.__text: 0x7c38
+13.0.28.0.0
+  __TEXT.__text: 0x7c40
   __TEXT.__auth_stubs: 0x5b0
   __TEXT.__objc_stubs: 0x1400
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xcd4
+  __TEXT.__objc_methlist: 0xd04
   __TEXT.__objc_classname: 0x392
-  __TEXT.__objc_methname: 0x20f3
-  __TEXT.__objc_methtype: 0xc42
+  __TEXT.__objc_methname: 0x2106
+  __TEXT.__objc_methtype: 0xc85
   __TEXT.__cstring: 0x4fe
   __TEXT.__const: 0xfc
   __TEXT.__gcc_except_tab: 0x1bc

   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x24d8
-  __DATA.__objc_selrefs: 0x848
+  __DATA.__objc_const: 0x2570
+  __DATA.__objc_selrefs: 0x858
   __DATA.__objc_ivar: 0xfc
   __DATA.__objc_data: 0x2d0
   __DATA.__data: 0x840

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 53483506-50DA-39AB-A8FA-8C776FB35E12
-  Functions: 276
+  UUID: C656699C-0F01-3E24-8A9C-4C3AB4E05733
+  Functions: 277
   Symbols:   133
-  CStrings:  690
+  CStrings:  696
 
Functions:
~ sub_6b44 : 132 -> 8
+ sub_6b4c
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
