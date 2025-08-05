## VirtualAudio

> `/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio`

```diff

-1364.115.30.0.0
-  __TEXT.__text: 0x503a88
+1364.123.0.0.0
+  __TEXT.__text: 0x504d00
   __TEXT.__auth_stubs: 0x26f0
   __TEXT.__objc_stubs: 0x9e0
   __TEXT.__init_offsets: 0x4dc
   __TEXT.__objc_methlist: 0x124
-  __TEXT.__const: 0xb0b02
-  __TEXT.__gcc_except_tab: 0x5da38
-  __TEXT.__cstring: 0x286d9
+  __TEXT.__const: 0xb0b0a
+  __TEXT.__gcc_except_tab: 0x5db68
+  __TEXT.__cstring: 0x287a1
   __TEXT.__objc_classname: 0x34
   __TEXT.__swift5_typeref: 0x133
   __TEXT.__swift5_capture: 0x178
-  __TEXT.__oslogstring: 0x4e15b
+  __TEXT.__oslogstring: 0x4e481
   __TEXT.__objc_methname: 0x710
   __TEXT.__constg_swiftt: 0xf8
   __TEXT.__swift5_reflstr: 0x4c

   __TEXT.__dof_VirtualAu: 0x340
   __TEXT.__dof_Aggregate: 0x5ec
   __TEXT.__dof_VirtualA0: 0x2aa
-  __TEXT.__unwind_info: 0x11340
+  __TEXT.__unwind_info: 0x11348
   __TEXT.__eh_frame: 0x7a0
   __DATA_CONST.__auth_got: 0x1390
   __DATA_CONST.__got: 0x4d8
   __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x27b30
+  __DATA_CONST.__const: 0x27b48
   __DATA_CONST.__cfstring: 0x2de0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A4A8F017-2BDD-3A84-A9EC-866ED65236A5
-  Functions: 11494
+  UUID: 2D70081B-27B7-3959-BBE6-7F79B4D33124
+  Functions: 11495
   Symbols:   773
-  CStrings:  11270
+  CStrings:  11285
 
CStrings:
+ "\t- Input selection overrode output: "
+ "\t- Output selection overrode input: "
+ "%25s:%-5d Didn't find any valid ports to override, ignoring specified override ports."
+ "%25s:%-5d No device info for vdef found"
+ "%25s:%-5d Not culling any formats for port '%s'"
+ "%25s:%-5d Output ports are different (with user preferred input honored: %s vs not honored: %s), user-preferred-input (%s) to be ignored"
+ "%25s:%-5d Output ports incompatible with user preferred input, clearing user preferred input : %s"
+ "%25s:%-5d Port update is all unroutables. Dropping user preferred BT input"
+ "%25s:%-5d Route configuration has user preferred input: %s"
+ "%25s:%-5d Setting orientation %lu on DSP"
+ "%25s:%-5d Unable to lock PhysicalDevice unregistering listener; selector: '%s'; scope: '%s'; element: %u."
+ "%25s:%-5d Updating usage of user preferred input: %s"
+ "%25s:%-5d Updating user preferred input usage: Not a play-And-record or VoiceCall route. returning early"
+ "%25s:%-5d User preferred input is BT/carplay like. user-preferred-input (%s) to be ignored"
+ "%25s:%-5d UserPreferred Input is %s, output overrode input = %d"
+ "%25s:%-5d handle port update - user preferred input: %s"
+ "%25s:%-5d handle port update new ports pushed to cache - user preferred input: %s"
+ "%25s:%-5d portupdate has unroutable ports: %d"
+ ", input selection overrode output: "
+ ", output selection overrode input: "
+ "@@ Strips Jul 25 2025 19:54:56"
+ "No Culling Policy"
+ "input selection overrode output"
+ "output selection overrode input"
- "%25s:%-5d Didn't find any valid ports to override, ignorning specified override ports."
- "%25s:%-5d Removing overridden input ports in route config: %s"
- "%25s:%-5d Routable BT ports found, clearing user preferred input %s"
- "%25s:%-5d Updating user preferred input usage: Not a VP route. returning early"
- "%25s:%-5d User preferred input: %s"
- "%25s:%-5d User preferred port in route config: %s"
- "@@ Strips Jul 15 2025 21:48:10"
- "cull < 24-bit"
- "cull > 16-bit"

```
