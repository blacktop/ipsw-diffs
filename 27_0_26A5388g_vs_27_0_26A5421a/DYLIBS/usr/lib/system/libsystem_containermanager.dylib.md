## libsystem_containermanager.dylib

> `/usr/lib/system/libsystem_containermanager.dylib`

```diff

-833.0.3.0.0
-  __TEXT.__text: 0x2fe84
-  __TEXT.__const: 0x424
-  __TEXT.__cstring: 0x3aee
-  __TEXT.__oslogstring: 0x582e
+833.0.8.0.1
+  __TEXT.__text: 0x2fe80
+  __TEXT.__const: 0x434
+  __TEXT.__cstring: 0x3af2
+  __TEXT.__oslogstring: 0x5856
   __TEXT.__unwind_info: 0x710
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xca0
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x15d0
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__data: 0x470
+  __AUTH.__data: 0x478
   __DATA.__data: 0x50
-  __DATA.__bss: 0x4f0
+  __DATA.__bss: 0x4f8
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x188
   - /usr/lib/system/libcopyfile.dylib

   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
   Functions: 625
-  Symbols:   1012
+  Symbols:   1013
   CStrings:  890
 
Symbols:
+ _setxattr
Functions:
~ __common_bundle_lookup : 1928 -> 1936
~ ___container_create_or_lookup_app_group_path_by_app_group_identifier_block_invoke : 2268 -> 2256
CStrings:
+ "@(#)VERSION:Container Manager: Aug  8 2026 15:53:59; MobileContainerManager_system-833.0.8.0.1~210/arm64e"
+ "Could not decode message into container object: 🔒%{private}s"
+ "Failed to issue sandbox extension to [🔒%{private}s] for containermanagerd"
+ "Requesting container lookup; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], bundle = [🔒%{private}s], root = [🔒%{private}s], executable = [🔒%{private}s], flags = %llu, euid = %u, uid = %u"
+ "Unable to get bundle from [🔒%{private}s]"
+ "Unable to get bundle root path from bundle at [🔒%{private}s]: %{public}d"
+ "Unable to get executable path from bundle at [🔒%{private}s]: %{public}d"
- "@(#)VERSION:Container Manager: Jul  7 2026 18:28:11; MobileContainerManager_system-833.0.3~122/arm64e"
- "Could not decode message into container object: %{public}s"
- "Failed to issue sandbox extension to [%{public}s] for containermanagerd"
- "Requesting container lookup; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], bundle = [%{public}s], root = [%{public}s], executable = [%{public}s], flags = %llu, euid = %u, uid = %u"
- "Unable to get bundle from [%{public}s]"
- "Unable to get bundle root path from bundle at [%{public}s]: %{public}d"
- "Unable to get executable path from bundle at [%{public}s]: %{public}d"
```
