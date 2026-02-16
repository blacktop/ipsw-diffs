## com.apple.AGXFirmwareKextG18PRTBuddy

> `com.apple.AGXFirmwareKextG18PRTBuddy`

```diff

-345.20.1.0.0
-  __TEXT.__const: 0x1bc
-  __TEXT.__cstring: 0x69a
-  __TEXT_EXEC.__text: 0x2d08
+350.27.0.0.0
+  __TEXT.__const: 0x1e0
+  __TEXT.__cstring: 0x74d
+  __TEXT_EXEC.__text: 0x2b74
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x38

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xd40
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: 4256A49E-81D9-3CD7-8478-808C41A6C901
+  UUID: 5C3E9D24-5D5C-344B-8CEC-2B9003F584E6
   Functions: 71
   Symbols:   0
-  CStrings:  36
+  CStrings:  38
 
Functions:
~ sub_fffffe0008b54048 -> sub_fffffe000830c048 : 360 -> 336
~ sub_fffffe0008b544a4 -> sub_fffffe000830c48c : 268 -> 292
~ sub_fffffe0008b545b0 -> sub_fffffe000830c5b0 : 268 -> 292
~ sub_fffffe0008b54768 -> sub_fffffe000830c780 : 352 -> 360
~ sub_fffffe0008b54ab0 -> sub_fffffe000830cad0 : 736 -> 692
~ sub_fffffe0008b54df8 -> sub_fffffe000830cdec : 928 -> 888
~ sub_fffffe0008b55198 -> sub_fffffe000830d164 : 132 -> 116
~ sub_fffffe0008b55288 -> sub_fffffe000830d244 : 104 -> 96
~ sub_fffffe0008b55388 -> sub_fffffe000830d33c : 556 -> 532
~ sub_fffffe0008b555b4 -> sub_fffffe000830d550 : 268 -> 260
~ sub_fffffe0008b556f4 -> sub_fffffe000830d688 : 156 -> 160
~ sub_fffffe0008b55790 -> sub_fffffe000830d728 : 264 -> 256
~ sub_fffffe0008b558f0 -> sub_fffffe000830d880 : 1700 -> 1568
~ sub_fffffe0008b56024 -> sub_fffffe000830df30 : 448 -> 440
~ sub_fffffe0008b561e4 -> sub_fffffe000830e0e8 : 208 -> 172
~ sub_fffffe0008b56474 -> sub_fffffe000830e354 : 440 -> 356
~ sub_fffffe0008b5662c -> sub_fffffe000830e4b8 : 660 -> 592
~ sub_fffffe0008b56950 -> sub_fffffe000830e798 : 176 -> 188
~ sub_fffffe0008b56b6c -> sub_fffffe000830e9c0 : 140 -> 152
~ sub_fffffe0008b56bf8 -> sub_fffffe000830ea58 : 140 -> 152
CStrings:
+ "121111121222121212222222222222222222211111111111121"
+ "AGXk: %s:%d:%s: !!! GFX firmware was not loaded by iBoot\n"
+ "AGXk: %s:%d:%s: !!! Scheduler work queues disabled but command submission is still enabled\n"
+ "virtual IOReturn AGXFirmwareKextRTBuddy::powerStateChange(unsigned long, unsigned long)"
+ "virtual bool AGXFirmwareKextRTBuddy::bootFirmware(IOMemoryMap *)"
- "\"GFX firmware was not loaded by iBoot\" @%s:%d"
- "\"Scheduler work queues disabled but command submission is still enabled\" @%s:%d"
- "1211111212221212122222222222222222211111111111121"

```
