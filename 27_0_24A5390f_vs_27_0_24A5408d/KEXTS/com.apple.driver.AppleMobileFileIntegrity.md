## com.apple.driver.AppleMobileFileIntegrity

> `com.apple.driver.AppleMobileFileIntegrity`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__assert`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-1171.0.3.0.0
-  __TEXT.__cstring: 0xb796
+1171.0.12.0.0
+  __TEXT.__cstring: 0xb8fb
   __TEXT.__const: 0x1568
   __TEXT.__os_log: 0x3a5
-  __TEXT_EXEC.__text: 0x29ab0
-  __TEXT_EXEC.__auth_stubs: 0x10d0
-  __DATA.__data: 0x4fa
+  __TEXT_EXEC.__text: 0x29df8
+  __TEXT_EXEC.__auth_stubs: 0x10c0
+  __DATA.__data: 0x4f2
   __DATA.__common: 0xf0
   __DATA.__bss: 0xd1
   __DATA_CONST.__mod_init_func: 0x20

   __DATA_CONST.__kalloc_type: 0xf80
   __DATA_CONST.__kalloc_var: 0x1400
   __DATA_CONST.__assert: 0xf0
-  __DATA_CONST.__auth_got: 0x868
+  __DATA_CONST.__auth_got: 0x860
   __DATA_CONST.__got: 0xe0
   __DATA_CONST.__auth_ptr: 0x18
-  Functions: 916
+  Functions: 917
   Symbols:   0
-  CStrings:  1162
+  CStrings:  1169
 
CStrings:
+ "%s: Hash type is SHA1"
+ "21:45:38"
+ "AMFI: Platform binary with platform identifier not in trust cache\n"
+ "AMFI: bailing out because of restricted entitlements.\n"
+ "Aug  5 2026"
+ "Code has restricted entitlements, but the validation of its code signature failed.\nUnsatisfied Entitlements: %s"
+ "com.apple.amfi.developer_mode_state"
+ "developer_app_executions"
+ "developer_mode_state"
+ "lockdown_mode_state"
+ "platform binary with platform identifier not in trust cache\n"
- "%s: Hash type is not SHA256 (%u) but %u."
- "21:12:38"
- "Jul 14 2026"
- "com.apple.backboardd"
```
