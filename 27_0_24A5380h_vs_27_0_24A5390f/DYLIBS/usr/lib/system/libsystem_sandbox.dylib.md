## libsystem_sandbox.dylib

> `/usr/lib/system/libsystem_sandbox.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`

```diff

-3051.0.30.0.0
-  __TEXT.__text: 0x3b58
+3051.0.42.0.2
+  __TEXT.__text: 0x3ce4
   __TEXT.__const: 0x180
-  __TEXT.__cstring: 0x84c
-  __TEXT.__unwind_info: 0x1d0
+  __TEXT.__cstring: 0xb68
+  __TEXT.__unwind_info: 0x1d8
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__got: 0x0

   - /usr/lib/system/libsystem_platform.dylib
   Functions: 142
   Symbols:   245
-  CStrings:  75
+  CStrings:  95
 
Functions:
~ _sandbox_extension_issue_file : 28 -> 36
~ _sandbox_extension_issue_file_to_process : 28 -> 36
~ __sandbox_extension_issue : 228 -> 292
~ _sandbox_extension_issue_generic : 24 -> 32
~ _sandbox_extension_issue_mach_to_process : 28 -> 36
~ _sandbox_extension_consume : 124 -> 180
~ _sandbox_extension_issue_generic_to_process : 24 -> 32
~ _sandbox_extension_issue_file_to_self : 96 -> 104
~ _sandbox_extension_issue_file_to_process_by_pid : 32 -> 40
~ _sandbox_extension_issue_mach : 28 -> 36
~ _sandbox_extension_issue_mach_to_process_by_pid : 32 -> 40
~ _sandbox_extension_issue_iokit_registry_entry_class : 28 -> 36
~ _sandbox_extension_issue_iokit_registry_entry_class_to_process : 28 -> 36
~ _sandbox_extension_issue_iokit_registry_entry_class_to_process_by_pid : 32 -> 40
~ _sandbox_extension_issue_generic_to_process_by_pid : 28 -> 36
~ _sandbox_extension_update_file : 56 -> 128
~ _sandbox_extension_update_file_by_fileid : 60 -> 152
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
