## libsystem_sandbox.dylib

> `/usr/lib/system/libsystem_sandbox.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`

```diff

-3051.0.30.0.0
-  __TEXT.__text: 0x4f58
+3051.0.42.0.2
+  __TEXT.__text: 0x50e4
   __TEXT.__const: 0x1a0
-  __TEXT.__cstring: 0xd06
-  __TEXT.__unwind_info: 0x218
+  __TEXT.__cstring: 0x1022
+  __TEXT.__unwind_info: 0x220
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xf8
   __DATA_CONST.__got: 0x0

   - /usr/lib/system/libsystem_platform.dylib
   Functions: 158
   Symbols:   299
-  CStrings:  120
+  CStrings:  140
 
Functions:
~ _sandbox_extension_issue_file : 28 -> 36
~ __sandbox_extension_issue : 228 -> 292
~ _sandbox_extension_consume : 124 -> 184
~ _sandbox_extension_issue_file_to_self : 96 -> 104
~ _sandbox_extension_issue_file_to_process : 32 -> 36
~ _sandbox_extension_issue_mach : 28 -> 36
~ _sandbox_extension_issue_file_to_process_by_pid : 32 -> 40
~ _sandbox_extension_issue_mach_to_process : 32 -> 36
~ _sandbox_extension_issue_mach_to_process_by_pid : 32 -> 40
~ _sandbox_extension_issue_iokit_registry_entry_class : 28 -> 36
~ _sandbox_extension_issue_iokit_registry_entry_class_to_process : 32 -> 36
~ _sandbox_extension_issue_iokit_registry_entry_class_to_process_by_pid : 32 -> 40
~ _sandbox_extension_issue_generic : 24 -> 32
~ _sandbox_extension_issue_generic_to_process : 24 -> 32
~ _sandbox_extension_issue_generic_to_process_by_pid : 28 -> 36
~ _sandbox_extension_update_file : 56 -> 132
~ _sandbox_extension_update_file_by_fileid : 60 -> 156
~ _sandbox_extension_issue_related_file_to_process : 408 -> 416
CStrings:
+ "%s failed for %s: %d (%s)"
+ "%s failed for %x/%llu: %d (%s)"
+ "%s failed: %d (%s)"
+ "sandbox_extension_consume"
+ "sandbox_extension_issue_file"
+ "sandbox_extension_issue_file_to_process"
+ "sandbox_extension_issue_file_to_process_by_pid"
+ "sandbox_extension_issue_file_to_self"
+ "sandbox_extension_issue_generic"
+ "sandbox_extension_issue_generic_to_process"
+ "sandbox_extension_issue_generic_to_process_by_pid"
+ "sandbox_extension_issue_iokit_registry_entry_class"
+ "sandbox_extension_issue_iokit_registry_entry_class_to_process"
+ "sandbox_extension_issue_iokit_registry_entry_class_to_process_by_pid"
+ "sandbox_extension_issue_mach"
+ "sandbox_extension_issue_mach_to_process"
+ "sandbox_extension_issue_mach_to_process_by_pid"
+ "sandbox_extension_issue_related_file_to_process"
+ "sandbox_extension_update_file"
+ "sandbox_extension_update_file_by_fileid"
```
