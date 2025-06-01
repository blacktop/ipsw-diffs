## libBasebandManagerICE.dylib

> `/usr/lib/libBasebandManagerICE.dylib`

```diff

-1006.0.0.0.0
-  __TEXT.__text: 0x1d6de0
+1053.0.0.0.0
+  __TEXT.__text: 0x1d7170
   __TEXT.__auth_stubs: 0x2fe0
   __TEXT.__init_offsets: 0x108
   __TEXT.__objc_methlist: 0x1a8
   __TEXT.__const: 0xbcf7
-  __TEXT.__gcc_except_tab: 0x2d394
-  __TEXT.__oslogstring: 0x9bb4
+  __TEXT.__gcc_except_tab: 0x2d3a4
+  __TEXT.__oslogstring: 0x9c5c
   __TEXT.__cstring: 0x63dc
-  __TEXT.__unwind_info: 0x8eb4
+  __TEXT.__unwind_info: 0x8eac
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0xa0
   __TEXT.__objc_methname: 0xdea

   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x1800
   __AUTH.__const_weak: 0xd0
-  __AUTH.__objc_data: 0xa0
+  __AUTH.__objc_data: 0x50
   __DATA.__got_weak: 0x7b0
   __DATA.__objc_ivar: 0x24
-  __DATA.__data: 0x3c8
-  __DATA.__common: 0x61
-  __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__data: 0x458
-  __DATA_DIRTY.__common: 0x98
-  __DATA_DIRTY.__bss: 0x1a8
+  __DATA.__data: 0x3e8
+  __DATA.__common: 0x49
+  __DATA_DIRTY.__objc_data: 0xf0
+  __DATA_DIRTY.__data: 0x438
+  __DATA_DIRTY.__common: 0xb0
+  __DATA_DIRTY.__bss: 0x1a2
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: 53B09019-59DE-3FE7-BF6D-733D09EAFE35
-  Functions: 5682
-  Symbols:   15942
-  CStrings:  2223
+  UUID: 25064D9B-6AEC-3D9A-9E1B-B6C73E9D183C
+  Functions: 5685
+  Symbols:   15944
+  CStrings:  2225
 
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
