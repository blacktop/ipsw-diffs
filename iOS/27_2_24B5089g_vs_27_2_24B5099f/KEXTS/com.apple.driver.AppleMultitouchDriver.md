## com.apple.driver.AppleMultitouchDriver

> `com.apple.driver.AppleMultitouchDriver`

```diff

-10100.44.0.0.0
+10110.3.0.0.0
   __TEXT.__const: 0x1a8
-  __TEXT.__cstring: 0x22d5
-  __TEXT.__os_log: 0x3a70
-  __TEXT_EXEC.__text: 0x1bfb0
-  __TEXT_EXEC.__auth_stubs: 0x6a0
+  __TEXT.__cstring: 0x22d4
+  __TEXT.__os_log: 0x3acf
+  __TEXT_EXEC.__text: 0x1c0b4
+  __TEXT_EXEC.__auth_stubs: 0x680
   __DATA.__data: 0xca
   __DATA.__common: 0x270
   __DATA_CONST.__mod_init_func: 0x58

   __DATA_CONST.__const: 0x43d8
   __DATA_CONST.__kalloc_var: 0x280
   __DATA_CONST.__kalloc_type: 0x8c0
-  __DATA_CONST.__auth_got: 0x350
-  __DATA_CONST.__got: 0x128
+  __DATA_CONST.__auth_got: 0x340
+  __DATA_CONST.__got: 0x130
   Functions: 546
   Symbols:   0
-  CStrings:  542
+  CStrings:  543
 
Functions:
~ sub_fffffe000934fda0 -> sub_fffffe00092f5a80 : 192 -> 232
~ sub_fffffe000934fe60 -> sub_fffffe00092f5b68 : 192 -> 232
~ sub_fffffe000934ffd0 -> sub_fffffe00092f5d00 : 120 -> 44
~ sub_fffffe000935005c -> sub_fffffe00092f5d40 : 104 -> 8
~ __ZN31AppleMultitouchDeviceUserClient11injectFrameEi : 320 -> 404
~ __ZN31AppleMultitouchDeviceUserClient12initWithTaskEP4taskPvjP12OSDictionary : 704 -> 740
~ sub_fffffe0009351c18 -> sub_fffffe00092f7914 : 220 -> 240
~ __ZN31AppleMultitouchDeviceUserClient19clientMemoryForTypeEjPjPP18IOMemoryDescriptor : 448 -> 660
CStrings:
+ "12111112122212121111111111111222222222111111122"
+ "[HID] [%s] [Error] %s::%s [0x%llx] Could not allocate _injectionMemory in clientMemoryForType\n"
- "121111121222121211111111111112222222221111112122"
```
