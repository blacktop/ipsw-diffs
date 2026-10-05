## com.apple.iokit.IOMobileGraphicsFamily-DCP

> `com.apple.iokit.IOMobileGraphicsFamily-DCP`

```diff

-700.50.104.1.0
-  __TEXT.__cstring: 0x6082
+700.50.108.0.0
+  __TEXT.__cstring: 0x63cb
   __TEXT.__const: 0x32e8
-  __TEXT_EXEC.__text: 0x2a1b4
+  __TEXT_EXEC.__text: 0x2a2d4
   __TEXT_EXEC.__auth_stubs: 0xf00
   __DATA.__data: 0xe8
   __DATA.__common: 0x2720

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 800
   Symbols:   0
-  CStrings:  500
+  CStrings:  512
 
Functions:
~ sub_fffffe000a309fc8 -> sub_fffffe000a29d508 : 700 -> 892
~ sub_fffffe000a30a434 -> sub_fffffe000a29da34 : 524 -> 564
~ sub_fffffe000a320b34 -> sub_fffffe000a2b415c : 140 -> 152
~ sub_fffffe000a322630 -> sub_fffffe000a2b5c64 : 304 -> 348
CStrings:
+ "AppleDCPLinkService: endpoint power-down entered with driver_power set, this wait cannot complete: this=%p power2=%d"
+ "AppleDCPLinkService: hibernate-resume re-start of link service failed"
+ "map_block_buf: pbt=%u allocateBufferWithOptions failed user_size=%u\n"
+ "map_block_buf: pbt=%u block_size=%zu too small for addr_offs=%u size_offs=%u"
+ "map_block_buf: pbt=%u buf->map failed, buf_flags=0x%x\n"
+ "map_block_buf: pbt=%u buf->prepare failed ret=0x%x, buf_flags=0x%x\n"
+ "map_block_buf: pbt=%u set_kernel_power_assert failed ret=0x%x\n"
+ "map_block_buf: pbt=%u temp_buf->map failed\n"
+ "map_block_buf: pbt=%u temp_buf->prepare failed ret=0x%x"
+ "map_block_buf: pbt=%u withAddressRange failed user_addr=0x%llx, user_size=%u, buf_flags=0x%x\n"
+ "set_block: map_block_buf failed, pbt=%u, block=%p, block_size=%zu, ret=0x%x\n"
+ "set_block: pbt=%u rejected, DCP reset in progress\n"
```
