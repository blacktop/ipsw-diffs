## libsystem_containermanager.dylib

> `/usr/lib/system/libsystem_containermanager.dylib`

```diff

-833.0.3.0.0
-  __TEXT.__text: 0x300a8
-  __TEXT.__const: 0x424
-  __TEXT.__cstring: 0x3c45
-  __TEXT.__oslogstring: 0x59a7
+833.0.8.0.1
+  __TEXT.__text: 0x300a4
+  __TEXT.__const: 0x434
+  __TEXT.__cstring: 0x3c49
+  __TEXT.__oslogstring: 0x59cf
   __TEXT.__unwind_info: 0x708
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x1d08
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x220
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__data: 0x470
+  __AUTH.__data: 0x478
   __DATA.__data: 0x60
-  __DATA.__bss: 0x4d8
+  __DATA.__bss: 0x4e0
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x1a0
   - /usr/lib/system/libcopyfile.dylib

   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
   Functions: 626
-  Symbols:   1008
+  Symbols:   1009
   CStrings:  905
 
Symbols:
+ _setxattr
Functions:
~ ___container_create_or_lookup_app_group_path_by_app_group_identifier_block_invoke : 2268 -> 2256
~ __common_bundle_lookup : 1920 -> 1928
CStrings:
+ "@(#)VERSION:Container Manager: Aug  3 2026 21:12:57; MobileContainerManager_system-833.0.8.0.1~151/arm64e"
+ "Could not decode message into container object: 🔒%{private}s"
+ "Failed to issue sandbox extension to [🔒%{private}s] for containermanagerd"
+ "Requesting container lookup; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], bundle = [🔒%{private}s], root = [🔒%{private}s], executable = [🔒%{private}s], flags = %llu, euid = %u, uid = %u"
+ "Unable to get bundle from [🔒%{private}s]"
+ "Unable to get bundle root path from bundle at [🔒%{private}s]: %{public}d"
+ "Unable to get executable path from bundle at [🔒%{private}s]: %{public}d"
- "@(#)VERSION:Container Manager: Jul  8 2026 00:24:25; MobileContainerManager_system-833.0.3~133/arm64e"
- "Could not decode message into container object: %{public}s"
- "Failed to issue sandbox extension to [%{public}s] for containermanagerd"
- "Requesting container lookup; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], bundle = [%{public}s], root = [%{public}s], executable = [%{public}s], flags = %llu, euid = %u, uid = %u"
- "Unable to get bundle from [%{public}s]"
- "Unable to get bundle root path from bundle at [%{public}s]: %{public}d"
- "Unable to get executable path from bundle at [%{public}s]: %{public}d"
```
