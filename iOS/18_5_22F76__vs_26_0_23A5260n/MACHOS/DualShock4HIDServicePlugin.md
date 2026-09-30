## DualShock4HIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/DualShock4HIDServicePlugin.plugin/DualShock4HIDServicePlugin`

```diff

-12.5.2.0.0
-  __TEXT.__text: 0x9478
+13.0.28.0.0
+  __TEXT.__text: 0x9480
   __TEXT.__auth_stubs: 0x590
   __TEXT.__objc_stubs: 0x15c0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xc64
+  __TEXT.__objc_methlist: 0xc94
   __TEXT.__objc_classname: 0x2ed
-  __TEXT.__objc_methname: 0x2379
-  __TEXT.__objc_methtype: 0xeac
+  __TEXT.__objc_methname: 0x238c
+  __TEXT.__objc_methtype: 0xeef
   __TEXT.__cstring: 0x72c
   __TEXT.__const: 0x520
   __TEXT.__gcc_except_tab: 0x188

   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x1b60
-  __DATA.__objc_selrefs: 0x890
+  __DATA.__objc_const: 0x1bb8
+  __DATA.__objc_selrefs: 0x8a0
   __DATA.__objc_ivar: 0x168
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x840

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 288428C0-BD0F-3DFE-8FBC-BF963271CFF8
-  Functions: 289
+  UUID: 5954DAD2-06FC-3657-A2F9-9B032B9976C1
+  Functions: 290
   Symbols:   129
-  CStrings:  821
+  CStrings:  827
 
Functions:
~ sub_8e24 : 132 -> 8
+ sub_8e2c
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
