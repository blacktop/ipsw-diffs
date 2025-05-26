## libBasebandManager.dylib

> `/usr/lib/libBasebandManager.dylib`

```diff

-1006.0.0.0.0
-  __TEXT.__text: 0x1dd500
+1053.0.0.0.0
+  __TEXT.__text: 0x1dd890
   __TEXT.__auth_stubs: 0x2fb0
   __TEXT.__init_offsets: 0x100
   __TEXT.__objc_methlist: 0x1a4
   __TEXT.__const: 0xbda4
-  __TEXT.__gcc_except_tab: 0x2d5a8
+  __TEXT.__gcc_except_tab: 0x2d5b8
   __TEXT.__cstring: 0x662f
-  __TEXT.__oslogstring: 0x9d14
-  __TEXT.__unwind_info: 0x8f88
+  __TEXT.__oslogstring: 0x9dbc
+  __TEXT.__unwind_info: 0x8f60
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0xa0
   __TEXT.__objc_methname: 0xdea

   __AUTH.__objc_data: 0x50
   __DATA.__got_weak: 0x7e8
   __DATA.__objc_ivar: 0x24
-  __DATA.__data: 0x3b0
-  __DATA.__common: 0x31
+  __DATA.__data: 0x380
+  __DATA.__common: 0x21
   __DATA.__bss: 0x4c0
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x4a8
-  __DATA_DIRTY.__common: 0xd0
-  __DATA_DIRTY.__bss: 0x1a8
+  __DATA_DIRTY.__data: 0x4d8
+  __DATA_DIRTY.__common: 0xe0
+  __DATA_DIRTY.__bss: 0x1a2
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  Functions: 5730
-  Symbols:   16083
-  CStrings:  2233
+  Functions: 5733
+  Symbols:   16085
+  CStrings:  2235
 
Symbols:
+ __ZN10OBDManager14updateOBDStateEv
+ __ZN10OBDManager19updateOBDState_iPadEv
+ __ZN10OBDManager21updateOBDState_iPhoneEv
+ __ZN6config2hw4iPadEv
+ ____ZN20HandDetectionManager4initEv_block_invoke.13
- __ZNSt3__110shared_ptrI16CMOnBodyDelegateEC2B8ue170006IS1_U13block_pointerFvPS1_EvEEPT_T0_
- ____ZN20HandDetectionManager4initEv_block_invoke.15
CStrings:
+ "#I Audio Output: %s, Motion Status: %s. Notifying OBD State: %s, Tuner State: %s, Motion Status as an input: %s"
+ "#I Motion Status: %s. Notifying OBD State: %s, Tuner State: %s, Motion Status as an input: %s"
+ "AppleBasebandManager-AppleBasebandServices_Manager-1053"
+ "AppleBasebandServices_Manager-1053"
+ "Failed to create on-body handler"
+ "Motion on-body detection is not available on this device"
+ "On-Body handler is not created"
- "#I Audio Output: %s, Motion Status: %s. Notifying OBD State: %s, Tuner State: %s"
- "AppleBasebandManager-AppleBasebandServices_Manager-1006"
- "AppleBasebandServices_Manager-1006"
- "Failed to create On-Body manager"
- "Failed to create core motion on body handler"

```
