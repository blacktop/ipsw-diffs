## com.apple.driver.AudioDMAFamily

> `com.apple.driver.AudioDMAFamily`

```diff

-500.80.0.0.0
+500.85.0.0.0
   __TEXT.__const: 0x30
-  __TEXT.__cstring: 0xee4
+  __TEXT.__cstring: 0xf14
   __TEXT.__os_log: 0x428
-  __TEXT_EXEC.__text: 0x5d94
+  __TEXT_EXEC.__text: 0x5ed4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60
-  __DATA_CONST.__auth_got: 0xf8
+  __DATA_CONST.__auth_got: 0x100
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xe40
   __DATA_CONST.__kalloc_type: 0x80
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: A009673C-F3DA-35F6-ACA8-120060983450
+  UUID: A6445176-FA67-3615-879E-6EBC543551A3
   Functions: 78
   Symbols:   0
-  CStrings:  125
+  CStrings:  127
 
Functions:
~ sub_fffffff00a018e08 -> sub_fffffff00a0649f8 : 208 -> 560
~ ____ZN17AudioDMAEvolution20ADMAChannelInterface24transferMemoryDescriptorEP18IOMemoryDescriptorU13block_pointerFvRKNS0_25CompletionCallbackContextEEj_block_invoke : 1328 -> 1288
~ ____ZN17AudioDMAEvolution20ADMAChannelInterface14abortTransfersEv_block_invoke : 584 -> 592
CStrings:
+ "%s: %s failed with %s."
+ "01:01:28"
+ "222222212111122111122"
+ "Jun 17 2025"
+ "deactivate_block_invoke"
- "20:39:14"
- "22222221211112211112"
- "May 30 2025"

```
