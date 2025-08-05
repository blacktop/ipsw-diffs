## com.apple.driver.AppleMobileApNonce

> `com.apple.driver.AppleMobileApNonce`

```diff

-47.0.0.0.0
-  __TEXT.__cstring: 0x1861
+49.0.0.0.0
+  __TEXT.__cstring: 0x1910
   __TEXT.__const: 0x12
-  __TEXT_EXEC.__text: 0x3eec
+  __TEXT_EXEC.__text: 0x3fc0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xc70
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: 83A5F83A-0809-3DDE-A227-4B4CF9E40102
-  Functions: 101
+  UUID: B8499CC4-57BA-32CA-BB2A-C85766F2B41E
+  Functions: 102
   Symbols:   0
-  CStrings:  154
+  CStrings:  158
 
Functions:
~ __ZN18AppleMobileApNonce18_cleanupNonceSlotsEv : 332 -> 500
+ sub_fffffff0097c703c
CStrings:
+ "%s%s:\n%s    L boot detected.\n"
+ "%s%s:\n%s    RL boot detected.\n"
+ "%s%s:\n%s    booting to ramdisk, skipping nonce cleanup.\n"
+ "%s%s:\n%s    possible update in flight, cleanup skipped.\n"

```
