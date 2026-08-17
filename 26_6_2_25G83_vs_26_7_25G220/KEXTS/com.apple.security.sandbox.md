## com.apple.security.sandbox

> `com.apple.security.sandbox`

```diff

-2680.160.6.0.0
+2680.160.6.700.3
   __TEXT.__os_log: 0x2213
-  __TEXT.__const: 0x1f85f
-  __TEXT.__cstring: 0x7a06
-  __TEXT_EXEC.__text: 0x4fa64
+  __TEXT.__const: 0x1f947
+  __TEXT.__cstring: 0x7a26
+  __TEXT_EXEC.__text: 0x4fb28
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x318
   __DATA.__bss: 0x7f120
-  __DATA_CONST.__auth_got: 0xa68
+  __DATA_CONST.__auth_got: 0xa70
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x3d00
+  __DATA_CONST.__const: 0x3d10
   __DATA_CONST.__kalloc_type: 0x14c0
   __DATA_CONST.__kalloc_var: 0x4b0
-  Functions: 918
-  Symbols:   1835
-  CStrings:  1538
+  Functions: 919
+  Symbols:   1837
+  CStrings:  1540
 
Symbols:
+ _sandbox_requires_quarantine_for_vnode
+ _vfs_nativexattrs
Functions:
+ _sandbox_requires_quarantine_for_vnode
~ _sb_evaluate_internal : 1792 -> 1796
~ _profile_init : 656 -> 652
~ _collection_init : 988 -> 1000
CStrings:
+ "qtn-exec"
+ "qtn-exec-no-quarantine"
```
