## libcryptex_trampoline.dylib

> `/usr/lib/libcryptex_trampoline.dylib`

```diff

-475.80.3.0.0
-  __TEXT.__text: 0x6e0
+493.101.1.0.0
+  __TEXT.__text: 0x6a4
   __TEXT.__auth_stubs: 0x110
-  __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x225
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x224
   __TEXT.__oslogstring: 0x104
-  __TEXT.__unwind_info: 0x80
+  __TEXT.__unwind_info: 0x88
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x20
   __AUTH_CONST.__auth_got: 0x88

   __DATA.__bss: 0x10
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcryptex_interface.dylib
-  UUID: 973C3E74-BF73-3371-9492-9EB64D52F1FC
-  Functions: 10
-  Symbols:   45
+  UUID: DB9DC843-E0A9-3A6C-A846-7A3D313C771E
+  Functions: 11
+  Symbols:   49
   CStrings:  15
 
Symbols:
+ cryptex_trampoline_upgrade_wait.cold.2
+ cryptex_trampoline_upgrade_wait.cold.3
+ cryptex_trampoline_upgrade_wait.cold.4
+ cryptex_trampoline_upgrade_wait.cold.5
Functions:
~ _cryptex_trampoline_upgrade_wait_options_set_cryptex_name : 168 -> 164
~ _cryptex_trampoline_upgrade_wait : 764 -> 684
~ _OUTLINED_FUNCTION_0 : 48 -> 40
~ _OUTLINED_FUNCTION_1 : 40 -> 32
~ cryptex_trampoline_upgrade_wait_options_create.cold.1 : 224 -> 208
~ cryptex_trampoline_upgrade_wait_options_set_cryptex_name.cold.1 : 176 -> 192
CStrings:
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/libcryptex/install/Symbols/libcryptex_trampoline"
+ "493.101.1"
+ "@(#)VERSION:Monitor Cryptex Upgrades Version 2.0.0: Mon Mar 10 20:53:42 PDT 2025; root:libcryptex-493.101.1~2/libcryptex_trampoline/RELEASE_ARM64E"
+ "Monitor Cryptex Upgrades Version 2.0.0: Mon Mar 10 20:53:42 PDT 2025; root:libcryptex-493.101.1~2/libcryptex_trampoline/RELEASE_ARM64E"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Binaries/libcryptex/install/Symbols/libcryptex_trampoline"
- "475.80.3"
- "@(#)VERSION:Monitor Cryptex Upgrades Version 2.0.0: Thu Dec 19 22:10:29 PST 2024; root:libcryptex-475.80.3~207/libcryptex_trampoline/RELEASE_ARM64E"
- "Monitor Cryptex Upgrades Version 2.0.0: Thu Dec 19 22:10:29 PST 2024; root:libcryptex-475.80.3~207/libcryptex_trampoline/RELEASE_ARM64E"

```
