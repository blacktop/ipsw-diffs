## com.apple.driver.AppleSmartBatteryManagerEmbedded

> `com.apple.driver.AppleSmartBatteryManagerEmbedded`

```diff

-  __TEXT.__cstring: 0x7d34
+  __TEXT.__cstring: 0x7b68
   __TEXT.__const: 0x2410
   __TEXT.__os_log: 0x2937
-  __TEXT_EXEC.__text: 0x303ec
+  __TEXT_EXEC.__text: 0x301dc
   __TEXT_EXEC.__auth_stubs: 0x7a0
   __DATA.__data: 0x1f0
   __DATA.__common: 0x3c0

   __DATA_CONST.__got: 0x100
   Functions: 689
   Symbols:   0
-  CStrings:  1253
+  CStrings:  1247
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
Functions:
~ sub_fffffe0009723c4c -> sub_fffffe0009723fbc : 328 -> 164
~ sub_fffffe0009723d94 -> sub_fffffe0009724060 : 328 -> 164
~ sub_fffffe00097264c4 -> sub_fffffe00097266ec : 168 -> 176
~ sub_fffffe0009729e98 -> sub_fffffe000972a0c8 : 932 -> 940
~ sub_fffffe000972d2e0 -> sub_fffffe000972d518 : 396 -> 444
~ sub_fffffe0009730840 -> sub_fffffe0009730aa8 : 2112 -> 2120
~ sub_fffffe000973f4b0 -> sub_fffffe000973f720 : 344 -> 336
~ sub_fffffe000974afbc -> sub_fffffe000974b224 : 344 -> 176
~ sub_fffffe000974caf0 -> sub_fffffe000974ccb0 : 180 -> 188
~ sub_fffffe000974cdb0 -> sub_fffffe000974cf78 : 328 -> 164
~ sub_fffffe000974d25c -> sub_fffffe000974d380 : 804 -> 860
~ sub_fffffe000974d7cc -> sub_fffffe000974d928 : 132 -> 136
CStrings:
+ "1211111212221212112121212"
- "121111121222121211212112"
- "AppleChargerData: ID: %d failed to read key '%c%c%c%c' retry:%zu rc:%#x=%s\n"
- "AppleSmartBatteryBank: DBG: Pack ID: %d Bank ID: %d WriteSMCKey attempt %lu/%u"
- "AppleSmartBatteryBank: Pack ID: %d Bank ID: %d failed to write key '%c%c%c%c', retry:%zu\n"
- "AppleSmartBatteryPack: DBG: ID: %d WriteSMCKey attempt %lu/%u"
- "AppleSmartBatteryPack: ID: %d failed to read key '%c%c%c%c' retry:%zu rc:%#x=%s\n"
- "AppleSmartBatteryPack: ID: %d failed to write key '%c%c%c%c', retry:%zu\n"

```
