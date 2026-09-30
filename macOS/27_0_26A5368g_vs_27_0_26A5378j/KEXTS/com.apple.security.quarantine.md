## com.apple.security.quarantine

> `com.apple.security.quarantine`

```diff

   __TEXT.__const: 0x71
   __TEXT.__cstring: 0x7e6
   __TEXT.__os_log: 0x3ba
-  __TEXT_EXEC.__text: 0x9924
-  __TEXT_EXEC.__auth_stubs: 0x8f0
+  __TEXT_EXEC.__text: 0x9940
+  __TEXT_EXEC.__auth_stubs: 0x900
   __DATA.__data: 0xcfb
   __DATA.__common: 0x24
   __DATA.__bss: 0x348
   __DATA_CONST.__const: 0xc8
   __DATA_CONST.__kalloc_type: 0x280
-  __DATA_CONST.__auth_got: 0x478
+  __DATA_CONST.__auth_got: 0x480
   __DATA_CONST.__got: 0x58
   Functions: 143
-  Symbols:   421
+  Symbols:   422
   CStrings:  109
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__got : content changed
Symbols:
+ _sandbox_requires_quarantine_for_vnode
Functions:
~ _hook_policy_syscall : 8464 -> 8472
~ _quarantine_getinfo : 432 -> 464
~ _syscall_quarantine_setinfo_common : 1540 -> 1528

```
