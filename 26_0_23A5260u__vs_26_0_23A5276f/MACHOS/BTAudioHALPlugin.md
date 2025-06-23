## BTAudioHALPlugin

> `/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/BTAudioHALPlugin`

```diff

-190.40.1.2.0
-  __TEXT.__text: 0x7f5c0
+190.43.0.0.0
+  __TEXT.__text: 0x7f618
   __TEXT.__auth_stubs: 0x12a0
   __TEXT.__objc_stubs: 0x26e0
   __TEXT.__init_offsets: 0xa4

   __TEXT.__gcc_except_tab: 0x204c
   __TEXT.__const: 0x1a0c
   __TEXT.__cstring: 0x49dc
-  __TEXT.__oslogstring: 0x145de
+  __TEXT.__oslogstring: 0x145db
   __TEXT.__objc_classname: 0x155
   __TEXT.__objc_methname: 0x3d9a
   __TEXT.__objc_methtype: 0x10d5

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: 5434EE2D-F03F-36BF-9F66-C69B260CA043
+  UUID: 2847CA61-26DE-3657-A7D2-1311B267146B
   Functions: 2731
   Symbols:   463
   CStrings:  2981
Functions:
~ sub_59e60 : 688 -> 760
~ sub_5c4ac -> sub_5c4f4 : 1392 -> 1408
CStrings:
+ "A2DP SETUP Overwriting latency from %d to %d due to USBC setting up"
+ "A2DP USB Overwriting latency from %d to %d due to USBC"
+ "Overwriting safety offset due to USB to %u"
- "A2DP SETUP Overwritting latency from %d to %d due to USBC setting up"
- "A2DP USB Overwritting latency from %d to %d due to USBC"
- "Overwritting safety offset due to USB to %u"

```
