## com.apple.kernel

> `com.apple.kernel`

### Sections with Same Size but Changed Content

- `__TEXT.__copyio_vectors`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__exclaves_bt`
- `__DATA_CONST.__kern_brk_desc`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__auth_ptr`
- `__LASTDATA_CONST.__mod_init_func`
- `__KLDDATA.__const`
- `__KLDDATA.__mod_init_func`
- `__KLDDATA.__mod_term_func`
- `__DATA.__data`
- `__BOOTDATA.__init`
- `__BOOTDATA.__static_ifinit`

```diff

-  __TEXT.__const: 0x36400
+  __TEXT.__const: 0x363f0
   __TEXT.__copyio_vectors: 0x2c0
-  __TEXT.__cstring: 0x886f9
-  __TEXT.__os_log: 0x3e117
+  __TEXT.__cstring: 0x88766
+  __TEXT.__os_log: 0x3e186
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__const: 0x119e90
+  __DATA_CONST.__const: 0x119ee0
   __DATA_CONST.__kalloc_type: 0x14680
-  __DATA_CONST.__assert: 0xc58
+  __DATA_CONST.__assert: 0xc80
   __DATA_CONST.__kalloc_var: 0x78f0
   __DATA_CONST.__exclaves_bt: 0x78
   __DATA_CONST.__kern_brk_desc: 0x78

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xed8
-  __TEXT_EXEC.__text: 0x8b8984
+  __TEXT_EXEC.__text: 0x8b9660
   __TEXT_BOOT_EXEC.__bootcode: 0x5250
   __KLD.__text: 0x1460
   __LASTDATA_CONST.__mod_init_func: 0x8

   __DATA.__common: 0x777b8
   __DATA.__bss: 0xa4140
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__init_entry_set: 0x13668
+  __BOOTDATA.__init_entry_set: 0x13680
   __BOOTDATA.__init: 0x5b5c8
   __BOOTDATA.__static_ifinit: 0x8
   __BOOTDATA.__static_if: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x48096
-  Functions: 21345
+  Functions: 21350
   Symbols:   0
-  CStrings:  20621
+  CStrings:  20626
 
CStrings:
+ "(%u): HMAC verification failed: %d\n"
+ "(paddr & PAGE_MASK) == 0"
+ "flow_registration_count"
+ "key_parse: invalid address extension.\n"
+ "necp_client.c"
+ "necp_flow_registration_count underflow @%s:%d"
- "(%u): HMAC verfication failed: %d\n"
```
