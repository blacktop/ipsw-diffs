## com.apple.telemetry

> `/System/Library/UserEventPlugins/com.apple.telemetry.plugin/com.apple.telemetry`

```diff

-505.0.0.0.0
-  __TEXT.__text: 0x8c40
-  __TEXT.__auth_stubs: 0x780
-  __TEXT.__objc_stubs: 0x340
-  __TEXT.__const: 0x14b
-  __TEXT.__gcc_except_tab: 0x290
-  __TEXT.__cstring: 0x9df
-  __TEXT.__oslogstring: 0x436d
+507.0.0.0.0
+  __TEXT.__text: 0x8ab8
+  __TEXT.__auth_stubs: 0x770
+  __TEXT.__objc_stubs: 0x320
+  __TEXT.__const: 0x143
+  __TEXT.__gcc_except_tab: 0x278
+  __TEXT.__cstring: 0x983
+  __TEXT.__oslogstring: 0x42fa
   __TEXT.__objc_classname: 0x3
-  __TEXT.__objc_methname: 0x213
+  __TEXT.__objc_methname: 0x202
   __TEXT.__unwind_info: 0x158
-  __DATA.__auth_got: 0x3d0
+  __DATA.__auth_got: 0x3c8
   __DATA.__got: 0xc0
-  __DATA.__auth_ptr: 0x10
+  __DATA.__auth_ptr: 0x8
   __DATA.__const: 0x258
-  __DATA.__cfstring: 0x420
+  __DATA.__cfstring: 0x3c0
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0xd0
+  __DATA.__objc_selrefs: 0xc8
   __DATA.__objc_intobj: 0x18
   __DATA.__data: 0x8
   __DATA.__bss: 0x80

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  UUID: E838AC23-122F-38C1-B3A2-76041C94DA9E
-  Functions: 151
-  Symbols:   153
-  CStrings:  306
+  UUID: 949AD061-1EC5-3869-814D-C00B234E45FB
+  Functions: 150
+  Symbols:   152
+  CStrings:  297
 
Symbols:
- _DRTailspinRequest
Functions:
~ sub_c90 : 7576 -> 7272
- sub_78f4
CStrings:
+ "Tailspin collection has been disabled."
- "DRTailspinRequest not available, unable to gather and upload tailspin"
- "Gathered tailspin via DR for %@ (%@)\n%@"
- "LostMicrostackshotsBeforeThisDrain"
- "LostMicrostackshotsInThisDrain"
- "Unable to gather and upload DR tailspin: %@"
- "com.apple.microstackshots"
- "debugDescription"

```
