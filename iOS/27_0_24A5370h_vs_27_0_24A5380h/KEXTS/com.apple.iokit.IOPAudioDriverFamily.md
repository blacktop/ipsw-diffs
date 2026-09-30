## com.apple.iokit.IOPAudioDriverFamily

> `com.apple.iokit.IOPAudioDriverFamily`

```diff

   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x3b50
+  __TEXT.__cstring: 0x3be7
   __TEXT.__os_log: 0x2654
-  __TEXT_EXEC.__text: 0x13ea4
-  __TEXT_EXEC.__auth_stubs: 0x510
+  __TEXT_EXEC.__text: 0x13e9c
+  __TEXT_EXEC.__auth_stubs: 0x530
   __DATA.__data: 0x308
   __DATA.__common: 0x150
   __DATA_CONST.__mod_init_func: 0x40
   __DATA_CONST.__mod_term_func: 0x40
   __DATA_CONST.__const: 0x22e0
   __DATA_CONST.__kalloc_type: 0x340
-  __DATA_CONST.__auth_got: 0x288
+  __DATA_CONST.__kalloc_var: 0x320
+  __DATA_CONST.__auth_got: 0x298
   __DATA_CONST.__got: 0xa0
   Functions: 635
   Symbols:   0
-  CStrings:  319
+  CStrings:  323
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__got : content changed
Functions:
~ sub_fffffe000a20b9a0 -> sub_fffffe000a20c020 : 272 -> 280
~ __ZN8IOPAudio16CommandInterface12memoryAccessERKNS_29MemoryAccessCommandDescriptorE : 740 -> 748
~ sub_fffffe000a20bda4 -> sub_fffffe000a20c434 : 12 -> 16
~ sub_fffffe000a20bdc0 -> sub_fffffe000a20c454 : 16 -> 12
~ sub_fffffe000a20bdd0 -> sub_fffffe000a20c460 : 16 -> 8
~ sub_fffffe000a20beb0 -> sub_fffffe000a20c538 : 412 -> 392
~ sub_fffffe000a20c234 -> sub_fffffe000a20c8a8 : 396 -> 400
CStrings:
+ "site.Packet.uint8_t"
+ "site.RegisterAccess::Packet.uint8_t"
+ "site.struct GetNodePropertyOutputPacket.uint8_t"
+ "site.struct SetNodePropertyInputPacket.uint8_t"

```
