## sptm.t8140.release.im4p

> `sptm.t8140.release.im4p`

```diff

-392.120.12.0.0
-  __TEXT.__cstring: 0xe522
+392.120.14.0.0
+  __TEXT.__cstring: 0xe724
   __TEXT.__binname: 0x40
   __TEXT.__const: 0xb00
   __TEXT.__chain_starts: 0x78
   __DATA_CONST.__const: 0x68c8
   __LATE_CONST.__late_const: 0x5d660
-  __TEXT_EXEC.__text: 0x5089c
+  __TEXT_EXEC.__text: 0x50a38
   __LAST.__pinst: 0x8
   __DATA.__auth_ptr: 0x18
   __DATA.__data: 0x6

   __BOOTDATA.__data: 0x14000
   Functions: 355
   Symbols:   1
-  CStrings:  1809
+  CStrings:  1814
 
CStrings:
+ "!sptm_add_overflow(src_paddr, (0), &assert_end_paddr) && assert_end_paddr <= hib_image_end_paddr"
+ "!sptm_add_overflow(src_paddr, (2 * sizeof(uint32_t)), &assert_end_paddr) && assert_end_paddr <= hib_image_end_paddr"
+ "!sptm_add_overflow(src_paddr, (compressed_size), &assert_end_paddr) && assert_end_paddr <= hib_image_end_paddr"
+ "!sptm_add_overflow(src_paddr, (sizeof(uint32_t)), &assert_end_paddr) && assert_end_paddr <= hib_image_end_paddr"
+ "header->image1Size > (uintptr_t)page_list_end_paddr - (uintptr_t)header_paddr"

```
