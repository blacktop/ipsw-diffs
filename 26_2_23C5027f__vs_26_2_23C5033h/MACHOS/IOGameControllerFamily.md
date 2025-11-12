## IOGameControllerFamily

> `/System/Library/Extensions/IOGameControllerFamily.kext/IOGameControllerFamily`

```diff

-13.2.7.0.0
-  __TEXT.__const: 0x470
+13.2.8.0.0
+  __TEXT.__const: 0x480
   __TEXT.__cstring: 0xeac
   __TEXT.__os_log: 0x1b00
-  __TEXT_EXEC.__text: 0x1ad60
+  __TEXT_EXEC.__text: 0x1ae24
   __TEXT_EXEC.__auth_stubs: 0x520
   __DATA.__data: 0xc8
   __DATA.__common: 0x240

   __DATA_CONST.__mod_term_func: 0x50
   __DATA_CONST.__const: 0x4d30
   __DATA_CONST.__kalloc_type: 0x7c0
-  UUID: ECC32A57-07C5-3D3A-AD9B-926CEBCA4FE6
+  UUID: 1FDCE248-082E-3992-A3B9-1976D33574B2
   Functions: 614
   Symbols:   829
   CStrings:  276
Symbols:
+ ___copy_helper_block_8_32r40r48r56r64r72r80r88r
+ ___destroy_helper_block_8_32r40r48r56r64r72r80r88r
- ___copy_helper_block_8_32r40r48r56r64r72r80r
- ___destroy_helper_block_8_32r40r48r56r64r72r80r
Functions:
~ sub_5a50 : 4692 -> 4688
~ sub_93fc -> sub_93f8 : 1464 -> 1632
~ sub_99b4 -> sub_9a58 : 240 -> 252
~ ___copy_helper_block_8_32r40r48r56r64r72r80r -> ___copy_helper_block_8_32r40r48r56r64r72r80r88r : 160 -> 176
~ ___destroy_helper_block_8_32r40r48r56r64r72r80r -> ___destroy_helper_block_8_32r40r48r56r64r72r80r88r : 128 -> 140
~ _OUTLINED_FUNCTION_5 : 24 -> 28
~ _OUTLINED_FUNCTION_6 : 20 -> 24
~ _OUTLINED_FUNCTION_7 : 28 -> 20
~ sub_16a20 -> sub_16aec : 1064 -> 1092
~ sub_175b4 -> sub_1769c : 548 -> 544
~ sub_18270 -> sub_18354 : 156 -> 148
~ _IOGCCircularControlQueueEntryModify : 400 -> 392
~ _IOGCCircularControlQueueEntryResetModifications : 436 -> 420

```
