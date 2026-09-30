## libsystem_containermanager.dylib

> `/usr/lib/system/libsystem_containermanager.dylib`

```diff

-  __TEXT.__text: 0x2fda4
-  __TEXT.__const: 0x424
-  __TEXT.__cstring: 0x3aea
+  __TEXT.__text: 0x2fda8
+  __TEXT.__const: 0x434
+  __TEXT.__cstring: 0x3af2
   __TEXT.__oslogstring: 0x57c0
   __TEXT.__unwind_info: 0x710
   __TEXT.__auth_stubs: 0x0
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Functions:
~ _container_audit_token_get_launch_persona : 524 -> 528
~ __container_traverse_get_last_path_component : 88 -> 100
~ _container_persona_copy_from_voucher_proximate : 644 -> 632
CStrings:
+ "@(#)VERSION:Container Manager: Jun 29 2026 21:04:39; MobileContainerManager_system-833.0.0.501.1~1/arm64e"
- "@(#)VERSION:Container Manager: Jun  9 2026 04:28:15; MobileContainerManager_system-833~113/arm64e"

```
