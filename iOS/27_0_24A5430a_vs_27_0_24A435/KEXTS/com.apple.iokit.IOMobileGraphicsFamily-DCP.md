## com.apple.iokit.IOMobileGraphicsFamily-DCP

> `com.apple.iokit.IOMobileGraphicsFamily-DCP`

```diff

 700.50.97.11.0
-  __TEXT.__cstring: 0x5e07
+  __TEXT.__cstring: 0x6069
   __TEXT.__const: 0x32e8
-  __TEXT_EXEC.__text: 0x2a1b0
+  __TEXT_EXEC.__text: 0x2ad00
   __TEXT_EXEC.__auth_stubs: 0xef0
   __DATA.__data: 0xe8
   __DATA.__common: 0x2720
   __DATA_CONST.__mod_init_func: 0x30
   __DATA_CONST.__mod_term_func: 0x30
-  __DATA_CONST.__const: 0x1e88
+  __DATA_CONST.__const: 0x1e90
   __DATA_CONST.__kalloc_type: 0x8c0
   __DATA_CONST.__kalloc_var: 0xf0
   __DATA_CONST.__auth_got: 0x778
   __DATA_CONST.__got: 0x138
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 797
+  Functions: 800
   Symbols:   0
-  CStrings:  491
+  CStrings:  499
 
CStrings:
+ "%s: dropped external_sync_error_notify message %llu\n"
+ "IOMFB: external_sync: pending notification found, delivering state=0x%llx\n"
+ "IOMFB: external_sync: userspace client registered for notifications\n"
+ "IOMFB: external_sync_error_notify_gated: delivered successfully to client %p\n"
+ "IOMFB: external_sync_error_notify_gated: no listeners registered, storing pending state=0x%llx\n"
+ "IOMFB: external_sync_error_notify_gated: sending to client %p\n"
+ "IOMFB: external_sync_error_notify_gated: state=0x%llx (late=%d expected_clock=%d incorrect_params=%d)\n"
+ "virtual void IOMobileFramebufferAP::genlock_error_notify_gated(uint64_t)"
```
