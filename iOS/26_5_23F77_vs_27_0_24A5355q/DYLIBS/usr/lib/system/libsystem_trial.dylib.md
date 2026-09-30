## libsystem_trial.dylib

> `/usr/lib/system/libsystem_trial.dylib`

```diff

-474.2.18.2.0
-  __TEXT.__text: 0x2f4 sha256:49fa19cfd731d3af27b24d385a24145383f6ecc5eaa4cc01623a0ee2a9bc3ba9
-  __TEXT.__auth_stubs: 0x70 sha256:d734b3afbdee9840aa941a2c0fd79b981b88c900da9651d768e3e974674ab629
-  __TEXT.__const: 0x48 sha256:791547b909025465610b3bb6cc0961b5df2f07c895f3c4cf3ed6bd8df1a48615
-  __TEXT.__cstring: 0xee sha256:04ec294f13662195726421e2cacc9ca56b3d25576e064d706639f459ec01a811
-  __TEXT.__unwind_info: 0x58 sha256:5240efeec551c4ac90d0d47d2c899cdf51b4a4dab54fb7323ec4c7bb1c69aaa5
-  __AUTH_CONST.__auth_got: 0x38 sha256:d4817aa5497628e7c77e6b606107042bbba3130888c5f47a375e6179be789fbb
+501.0.0.0.0
+  __TEXT.__text: 0x238 sha256:734deda87ba0d2151a1698d4065463e171bab63c6951804c6e94694d134d6e19
+  __TEXT.__const: 0x38 sha256:a9f036bb4f9e2f4d0b08fa54209dfa92366b64315c84c14821a75d05bfbd1585
+  __TEXT.__cstring: 0x83 sha256:a52c6cd3ce7049ed8cca93873e2156a080bd8d1bad58f1ea31bc7a5a5c3ac9d0
+  __TEXT.__unwind_info: 0x60 sha256:a18d40838f3038bd5d7796e8f3fdb079ec179b692b815f7b0d6dc50e65a5213a
+  __TEXT.__auth_stubs: 0x0
+  __AUTH_CONST.__auth_got: 0x0
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdispatch.dylib
   - /usr/lib/system/libsystem_blocks.dylib

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: EC123CD7-F34A-3987-A6FF-931E44A7E84A
-  Functions: 3
-  Symbols:   13
-  CStrings:  11
+  UUID: B6FF2127-D8F3-3798-908C-D69046F79F52
+  Functions: 4
+  Symbols:   14
+  CStrings:  6
 
Symbols:
+ <redacted>
+ __os_trial_factor_get_long_long_impl
+ _after_strstr
+ _strlen
+ _strstr
- _MAX_FACTOR_STRING_LENGTH
- __os_trial_factor_get_long_impl
- _strnlen
- _strnstr
CStrings:
+ "_os_trial_factor_get_long_long_impl"
+ "trial_factor_private_impl.c"
- "_os_trial_factor_get_bool_impl"
- "_os_trial_factor_get_long_impl"
- "consumed_so_far <= MAX_FACTOR_STRING_LENGTH"
- "level >= factors"
- "search_false"
- "search_true"
- "trial_factor_private.c"

```
