## XboxOneHIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/XboxOneHIDServicePlugin.plugin/XboxOneHIDServicePlugin`

```diff

-12.5.2.0.0
-  __TEXT.__text: 0x6bdc
+13.0.28.0.0
+  __TEXT.__text: 0x6be4
   __TEXT.__auth_stubs: 0x550
   __TEXT.__objc_stubs: 0x13a0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xbec
+  __TEXT.__objc_methlist: 0xc1c
   __TEXT.__objc_classname: 0x2e5
-  __TEXT.__objc_methname: 0x205f
-  __TEXT.__objc_methtype: 0xc78
+  __TEXT.__objc_methname: 0x2072
+  __TEXT.__objc_methtype: 0xcbb
   __TEXT.__cstring: 0x508
   __TEXT.__const: 0xf4
   __TEXT.__gcc_except_tab: 0x16c

   __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x1810
-  __DATA.__objc_selrefs: 0x818
+  __DATA.__objc_const: 0x1868
+  __DATA.__objc_selrefs: 0x828
   __DATA.__objc_ivar: 0x114
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x840

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7C5B2DDB-031D-322D-94D6-2251BEA3BDEE
-  Functions: 245
+  UUID: 27891CAF-E847-3A69-A96B-ADE6BACAF6B0
+  Functions: 246
   Symbols:   127
-  CStrings:  695
+  CStrings:  701
 
Functions:
~ sub_6e98 : 132 -> 8
+ sub_6ea0
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
