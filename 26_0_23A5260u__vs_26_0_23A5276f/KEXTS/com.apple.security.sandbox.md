## com.apple.security.sandbox

> `com.apple.security.sandbox`

```diff

-2680.0.11.0.0
-  __TEXT.__os_log: 0x20a0
-  __TEXT.__const: 0x1cc9c1
-  __TEXT.__cstring: 0x6ff3
-  __TEXT_EXEC.__text: 0x365d8
+2680.0.28.0.1
+  __TEXT.__os_log: 0x2223
+  __TEXT.__const: 0x1cf009
+  __TEXT.__cstring: 0x70e0
+  __TEXT_EXEC.__text: 0x37160
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1d0
-  __DATA.__bss: 0x15328
+  __DATA.__bss: 0x15340
   __DATA_CONST.__auth_got: 0x838
   __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0x3620
+  __DATA_CONST.__const: 0x37d0
   __DATA_CONST.__kalloc_type: 0xac0
   __DATA_CONST.__kalloc_var: 0x4b0
-  UUID: 70AB5D44-740F-350D-8892-9A2ADFDF5F06
-  Functions: 633
+  UUID: 4165AA0F-7815-3A01-8D77-AC06DCDD7E73
+  Functions: 654
   Symbols:   0
-  CStrings:  1305
+  CStrings:  1320
 
CStrings:
+ "%s(0x%llx): %u/%u tasks scheduled"
+ "/private/var/db/aonsensed"
+ "/private/var/db/eligibilityd"
+ "/private/var/db/mmaintenanced"
+ "/private/var/db/modelmanagerd"
+ "/private/var/db/swtransparencyd"
+ "com.apple.private.security.disk-image-authority"
+ "disk_image_backing_store_init"
+ "diskimage.c"
+ "failed to register disk image backing store for %s"
+ "failed to remove %s from disk image backing store index: %d"
+ "failed to unregister disk image backing store for %s"
+ "failed to update disk image backing store index for %s -> %s: %d"
+ "failed to update disk image backing store index for %s <-> %s: %d"
+ "registered disk image backing store for %s"
+ "unregistered disk image backing store for %s"
+ "userret(0x%llx): invoking callback; %u/%u remaining"
- "%s(%llu): %u/%u tasks scheduled"
- "userret(%llu): invoking callback; %u/%u remaining"

```
