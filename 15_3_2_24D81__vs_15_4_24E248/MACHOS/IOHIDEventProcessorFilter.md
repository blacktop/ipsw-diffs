## IOHIDEventProcessorFilter

> `/System/Library/HIDPlugins/IOHIDEventProcessorFilter.plugin/Contents/MacOS/IOHIDEventProcessorFilter`

```diff

-2104.80.4.0.0
-  __TEXT.__text: 0x3cbc
+2115.100.21.0.0
+  __TEXT.__text: 0x3cd0
   __TEXT.__auth_stubs: 0x310
   __TEXT.__gcc_except_tab: 0xa8
   __TEXT.__const: 0x101

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 1DEA5C2F-37F8-3CED-913E-979585C437F1
+  UUID: C2254353-CBB8-3C39-82F0-6B594DCC8050
   Functions: 137
   Symbols:   149
   CStrings:  68
Functions:
~ __ZN19IOHIDEventProcessor27unscheduleFromDispatchQueueEPvP16dispatch_queue_s : 68 -> 76
~ __ZN19IOHIDEventProcessor20setPropertyForClientEPK10__CFStringPKvS4_ : 1160 -> 1164
~ __ZN19IOHIDEventProcessor6filterEP12__IOHIDEvent : 900 -> 908
~ __ZN5Timer4initEP16dispatch_queue_s : 276 -> 284
~ __ZN19IOHIDEventProcessor27unscheduleFromDispatchQueueEP16dispatch_queue_s : 68 -> 76
~ __ZN19IOHIDEventProcessor13dispatchEventEP12__IOHIDEventb : 220 -> 224
~ __ZN5Timer18checkEventTimeoutsEv : 424 -> 428
~ __ZN11ButtonEvent20createSyntheticEventEb : 400 -> 404
~ __ZN8TapEvent20createSyntheticEventEb : 448 -> 452
~ __ZN8TapEvent7TEEnterEP12__IOHIDEvent : 244 -> 228
~ __ZN5Timer13updateTimeoutEv : 216 -> 208
~ sub_4c30 -> sub_3d08 : 28 -> 16
~ sub_4c4c -> sub_3d18 : 32 -> 28
~ sub_4c84 -> sub_3d4c : 104 -> 132
~ sub_4d54 -> sub_3e38 : 132 -> 104
~ sub_4dd8 -> sub_3ea0 : 132 -> 104
~ sub_4ec4 -> sub_3f70 : 104 -> 132
~ sub_4f2c -> sub_3ff4 : 104 -> 132
~ sub_4ffc -> sub_40e0 : 132 -> 104
~ sub_5080 -> sub_4148 : 64 -> 52
~ sub_5128 -> sub_41e4 : 52 -> 64
~ sub_515c -> sub_4224 : 120 -> 152
~ sub_51d4 -> sub_42bc : 140 -> 132
~ sub_5260 -> sub_4340 : 144 -> 120
~ sub_542c -> sub_44f4 : 116 -> 124

```
