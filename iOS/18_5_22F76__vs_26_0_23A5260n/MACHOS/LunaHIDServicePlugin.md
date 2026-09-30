## LunaHIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/LunaHIDServicePlugin.plugin/LunaHIDServicePlugin`

```diff

-12.5.2.0.0
-  __TEXT.__text: 0x5cd4
+13.0.28.0.0
+  __TEXT.__text: 0x5cdc
   __TEXT.__auth_stubs: 0x540
   __TEXT.__objc_stubs: 0x1220
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xb74
+  __TEXT.__objc_methlist: 0xba4
   __TEXT.__cstring: 0x4ae
   __TEXT.__objc_classname: 0x2e2
-  __TEXT.__objc_methname: 0x1f0d
-  __TEXT.__objc_methtype: 0xc24
+  __TEXT.__objc_methname: 0x1f20
+  __TEXT.__objc_methtype: 0xc67
   __TEXT.__const: 0xc0
   __TEXT.__gcc_except_tab: 0x16c
   __TEXT.__oslogstring: 0x35d

   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x1708
-  __DATA.__objc_selrefs: 0x7e0
+  __DATA.__objc_const: 0x1760
+  __DATA.__objc_selrefs: 0x7f0
   __DATA.__objc_ivar: 0xf4
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x840

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FF43D05F-10A4-3614-8DF8-FEE17D905B08
-  Functions: 234
+  UUID: 120C846B-8A5A-345E-8036-C43D3E5F0BF3
+  Functions: 235
   Symbols:   124
-  CStrings:  649
+  CStrings:  655
 
Functions:
~ sub_5ee4 : 132 -> 8
+ sub_5eec
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
