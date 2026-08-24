## com.apple.filesystems.lifs

> `com.apple.filesystems.lifs`

```diff

-974.0.11.0.0
-  __TEXT.__os_log: 0x1ef8
+974.0.13.0.2
+  __TEXT.__os_log: 0x1f3f
   __TEXT.__cstring: 0x29d8
   __TEXT.__const: 0x328
-  __TEXT_EXEC.__text: 0x20114
+  __TEXT_EXEC.__text: 0x2014c
   __TEXT_EXEC.__auth_stubs: 0xfa0
   __DATA.__data: 0x528
   __DATA.__common: 0x130

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 459
   Symbols:   1342
-  CStrings:  514
+  CStrings:  515
 
Functions:
~ _lifs_request_done : 572 -> 628
CStrings:
+ "%s: we got no buffer to copyin, but requested to copyin, returning EIO"
```
