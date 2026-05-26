## com.apple.security.sandbox

> `com.apple.security.sandbox`

```diff

-2680.120.12.0.0
-  __TEXT.__os_log: 0x2272
-  __TEXT.__const: 0x1cac21
-  __TEXT.__cstring: 0x72d6
-  __TEXT_EXEC.__text: 0x38ab8
+2680.160.3.0.0
+  __TEXT.__os_log: 0x228e
+  __TEXT.__const: 0x1cb501
+  __TEXT.__cstring: 0x72f8
+  __TEXT_EXEC.__text: 0x38cc4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x220
   __DATA.__bss: 0x152f8
-  __DATA_CONST.__auth_got: 0x878
+  __DATA_CONST.__auth_got: 0x890
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__const: 0x3858
   __DATA_CONST.__kalloc_type: 0xbc0
   __DATA_CONST.__kalloc_var: 0x4b0
-  UUID: 58F3BE22-6099-3D96-B22F-DBA3D67DDE65
-  Functions: 652
+  UUID: E57BF868-62CF-34DD-A245-F2A81A7B1599
+  Functions: 654
   Symbols:   0
-  CStrings:  1344
+  CStrings:  1346
 
Functions:
~ _userspace_boot_handler : 60 -> 72
~ _hook_policy_syscall : 8184 -> 8244
+ sub_fffffe000a49f218
+ sub_fffffe000a49fa34
CStrings:
+ "%s[%d] revoked access to %s"
+ "com.apple.private.security.revoke"

```
