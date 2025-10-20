## com.apple.kernel

> `com.apple.kernel`

```diff

-12377.40.120.502.1
+12377.42.6.0.0
   __TEXT.__const: 0x35180
   __TEXT.__copyio_vectors: 0x2c0
-  __TEXT.__cstring: 0x80008
+  __TEXT.__cstring: 0x800c4
   __TEXT.__os_log: 0x3c58f
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2d8
   __DATA_CONST.__const: 0x117410
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__kalloc_type: 0x14200
+  __DATA_CONST.__kalloc_type: 0x141c0
   __DATA_CONST.__assert: 0x8fc
   __DATA_CONST.__kalloc_var: 0x7b20
   __DATA_CONST.__exclaves_bt: 0x78
   __DATA_CONST.__kern_brk_desc: 0x78
   __DATA_SPTM.__const: 0x3c000
-  __TEXT_EXEC.__text: 0x8b1a6c
+  __TEXT_EXEC.__text: 0x8b1f74
   __TEXT_EXEC.__hib_text: 0xf38
   __TEXT_BOOT_EXEC.__bootcode: 0x51d0
   __KLD.__text: 0x1638

   __DATA.__data: 0x17f79
   __DATA.__lock_grp: 0x5bc8
   __DATA.__percpu: 0x6f28
-  __DATA.__common: 0x6ec40
+  __DATA.__common: 0x6ec38
   __DATA.__bss: 0x97228
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__static_if: 0x4d30

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x471ae
-  UUID: 2D5AC777-C3A9-3CFD-A271-F79F6D86529F
-  Functions: 20748
+  UUID: 7BA91819-48D7-3E88-B51D-79B76E9A0A4B
+  Functions: 20750
   Symbols:   0
-  CStrings:  20258
+  CStrings:  20261
 
CStrings:
+ "\"TB_FATAL: \" \"Attempt to retrieve reply list in environment without large message support\" @%s:%d"
+ "322222"
+ "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[41c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"
+ "vm_object_pl_req_begin(%p): overflow\n @%s:%d"
+ "vm_object_pl_req_end(%p): underflow\n @%s:%d"
- "32222"
- "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[40c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"

```
