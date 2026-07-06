## com.apple.driver.AppleDPDisplayTCON

> `com.apple.driver.AppleDPDisplayTCON`

```diff

   __TEXT.__cstring: 0x1237
   __TEXT.__const: 0x50
-  __TEXT_EXEC.__text: 0xde34
+  __TEXT_EXEC.__text: 0xdfec
   __TEXT_EXEC.__auth_stubs: 0x220
   __DATA.__data: 0xc4
   __DATA.__common: 0x228
   __DATA_CONST.__mod_init_func: 0x40
   __DATA_CONST.__mod_term_func: 0x40
-  __DATA_CONST.__const: 0x83c8
+  __DATA_CONST.__const: 0x8408
   __DATA_CONST.__kalloc_type: 0x340
   __DATA_CONST.__auth_got: 0x110
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 422
-  Symbols:   849
+  Functions: 424
+  Symbols:   853
   CStrings:  165
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Symbols:
+ ____ZN12AppleDCPTCON12didTerminateEP9IOServicejPb_block_invoke
+ ____ZN12AppleDCPTCON4stopEP9IOService_block_invoke
Functions:
~ __ZN12AppleDCPTCON4stopEP9IOService : 304 -> 180
+ ____ZN12AppleDCPTCON4stopEP9IOService_block_invoke
+ ____ZN12AppleDCPTCON12didTerminateEP9IOServicejPb_block_invoke
~ ____ZN12AppleDCPTCON14enqueueCommandE17TCONAFKPacketTypeP18AppleTCONComponentjPhm_block_invoke : 580 -> 604

```
