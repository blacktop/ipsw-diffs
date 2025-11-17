## AppleVideoEncoder

> `/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/AppleVideoEncoder`

```diff

-905.5.3.0.0
-  __TEXT.__text: 0x1812b8
+905.17.4.0.0
+  __TEXT.__text: 0x181184
   __TEXT.__auth_stubs: 0x1050
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0xc
-  __TEXT.__const: 0x22dd8
-  __TEXT.__cstring: 0x528cf
+  __TEXT.__const: 0x23498
+  __TEXT.__cstring: 0x527ab
   __TEXT.__gcc_except_tab: 0x720
   __TEXT.__objc_methname: 0xb
   __TEXT.__unwind_info: 0x8b8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x8
   __DATA.__data: 0x210
-  __DATA.__bss: 0x10a0
+  __DATA.__bss: 0x1160
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4D4B49CE-AA70-3F0E-8F40-D4B00521BA82
+  UUID: 21FC121B-EB8C-321D-AFB8-0A572B27315A
   Functions: 1586
   Symbols:   511
-  CStrings:  6997
+  CStrings:  6993
 
Functions:
~ sub_e4e30 : 1992 -> 1980
~ sub_1117b4 -> sub_1117a8 : 1356 -> 1352
~ sub_11cb54 -> sub_11cb44 : 792 -> 824
~ sub_11ce6c -> sub_11ce7c : 1528 -> 1536
~ sub_1252f8 -> sub_125310 : 12528 -> 12228
~ sub_12a644 -> sub_12a530 : 8380 -> 8384
~ sub_12d95c -> sub_12d84c : 5400 -> 5468
~ sub_12ee74 -> sub_12eda8 : 576 -> 452
~ sub_13dc94 -> sub_13db4c : 144 -> 136
~ sub_1759ac -> sub_17585c : 240 -> 256
~ sub_175a9c -> sub_17595c : 96 -> 108
CStrings:
+ "%lld %d AVE %s: %s::%s:%d encoding error %d %d %d %d"
+ "%lld %d AVE %s: %s::%s:%d encoding error %d %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d frame drop %lld %d %lld %d %d 0x%x %p"
+ "%lld %d AVE %s: %s::%s:%d frame drop %lld %d %lld %d %d 0x%x %p\n"
+ "%lld %d AVE %s: UserQpMapSize (%d) does not match required size (%d), disabling userQPMap feature"
+ "%lld %d AVE %s: UserQpMapSize (%d) does not match required size (%d), disabling userQPMap feature\n"
+ "22:00:33"
+ "22:00:34"
+ "22:00:36"
+ "22:00:37"
+ "905.17.4"
+ "Nov 12 2025"
+ "gsc_saAVE_Enc_Preset_Set[i].iNum <= 10"
- "%lld %d AVE %s: \nH264FrameRec: counter received = %d"
- "%lld %d AVE %s: \nH264FrameRec: counter received = %d\n"
- "%lld %d AVE %s: %s:%d %s | H264FrameRec ERROR: commandResult != kIOReturnSuccess."
- "%lld %d AVE %s: %s:%d %s | H264FrameRec ERROR: commandResult != kIOReturnSuccess.\n"
- "%lld %d AVE %s: %s::%s:%d frame drop %lld %d %lld %d 0x%x %p"
- "%lld %d AVE %s: %s::%s:%d frame drop %lld %d %lld %d 0x%x %p\n"
- "%lld %d AVE %s: FIG: H264FrameRec: commandResult = kIOReturnNoResources"
- "%lld %d AVE %s: FIG: H264FrameRec: commandResult = kIOReturnNoResources\n"
- "%lld %d AVE %s: UserQpMapSize (%d) is smaller than required (%d), copying only received data"
- "%lld %d AVE %s: UserQpMapSize (%d) is smaller than required (%d), copying only received data\n"
- "21:06:33"
- "21:06:35"
- "21:06:37"
- "905.5.3"
- "Nov  3 2025"
- "gsc_saEnc_Preset_Set[i].iNum <= 10"
- "result == 0"

```
