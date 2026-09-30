## com.apple.security.sandbox

> `com.apple.security.sandbox`

```diff

   __TEXT.__os_log: 0x1d58
-  __TEXT.__const: 0x1eab69
+  __TEXT.__const: 0x1ed021
   __TEXT.__cstring: 0x6f50
-  __TEXT_EXEC.__text: 0x38f4c
+  __TEXT_EXEC.__text: 0x38ee0
   __TEXT_EXEC.__auth_stubs: 0x1090
   __DATA.__data: 0x220
   __DATA.__bss: 0x15300
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
Functions:
~ sub_fffffe000a873be0 -> sub_fffffe000a874b80 : 452 -> 444
~ ___hook_iokit_check_set_properties_block_invoke : 1580 -> 1560
~ _hook_policy_init : 5600 -> 5584
~ sub_fffffe000a889efc -> sub_fffffe000a88ae70 : 224 -> 212
~ sub_fffffe000a88a10c -> sub_fffffe000a88b074 : 432 -> 420
~ _syscall_reference_retain : 876 -> 872
~ sub_fffffe000a88a628 -> sub_fffffe000a88b580 : 480 -> 468
~ _populate_event_context : 4488 -> 4500
~ _hook_cred_label_update_execve : 5392 -> 5372
~ _sandbox_create_for_executable -> sub_fffffe000a899fd0 : 1056 -> 1048
~ sub_fffffe000a8a1864 -> sub_fffffe000a8a27a0 : 748 -> 752
~ _syscall_check_sandbox : 4092 -> 4080

```
