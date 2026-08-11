## com.apple.filesystems.lifs

> `com.apple.filesystems.lifs`

```diff

 737.160.1.0.2
-  __TEXT.__os_log: 0x1367
+  __TEXT.__os_log: 0x13ae
   __TEXT.__cstring: 0x2188
   __TEXT.__const: 0x2c0
-  __TEXT_EXEC.__text: 0x1ae28
+  __TEXT_EXEC.__text: 0x1ae60
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x528
   __DATA.__common: 0x130

   __DATA_CONST.__kalloc_var: 0xf0
   Functions: 403
   Symbols:   1224
-  CStrings:  395
+  CStrings:  396
 
Functions:
~ _lifs_request_done : 572 -> 628
CStrings:
+ "%s: we got no buffer to copyin, but requested to copyin, returning EIO"
```
