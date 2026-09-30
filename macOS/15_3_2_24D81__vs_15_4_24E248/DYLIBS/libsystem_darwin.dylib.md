## libsystem_darwin.dylib

> `/usr/lib/system/libsystem_darwin.dylib`

```diff

-1669.60.4.0.0
-  __TEXT.__text: 0x6af4
+1698.100.8.0.0
+  __TEXT.__text: 0x699c
   __TEXT.__auth_stubs: 0x560
   __TEXT.__const: 0xd0
-  __TEXT.__cstring: 0x1e9f
+  __TEXT.__cstring: 0x1ea6
   __TEXT.__oslogstring: 0x820
-  __TEXT.__unwind_info: 0x1d8
+  __TEXT.__unwind_info: 0x1d0
   __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0x2940
+  __DATA_CONST.__const: 0x2948
   __AUTH_CONST.__auth_got: 0x2b0
   __AUTH_CONST.__const: 0x190
   __DATA.__data: 0x10

   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: F23DCA7C-AF18-3BB9-9D2F-FFBC4645DDC1
-  Functions: 158
-  Symbols:   304
-  CStrings:  481
+  UUID: 126D0342-CF6C-344C-977A-0A55B8E10B75
+  Functions: 159
+  Symbols:   318
+  CStrings:  480
 
Symbols:
+ _OUTLINED_FUNCTION_14
+ _check_base_system_content.cold.2
+ _check_internal_content.cold.2
+ os_boot_mode_query.cold.1
+ os_variant_allows_internal_security_policies.cold.2
+ os_variant_has_factory_content.cold.2
+ os_variant_has_full_logging.cold.2
+ os_variant_has_internal_content.cold.1
+ os_variant_has_internal_diagnostics.cold.2
+ os_variant_has_internal_diagnostics.cold.3
+ os_variant_has_internal_ui.cold.1
+ os_variant_init_4launchd.cold.10
+ os_variant_is_darwinos.cold.2
+ os_variant_uses_ephemeral_storage.cold.2
CStrings:
+ "assertion failure: \"(base_system_content) != OS_VARIANT_S_UNKNOWN\" -> %llu"
+ "assertion failure: \"(can_has_debugger) != OS_VARIANT_S_UNKNOWN\" -> %llu"
+ "assertion failure: \"(darwinos_content) != OS_VARIANT_S_UNKNOWN\" -> %llu"
+ "assertion failure: \"(factory_content) != OS_VARIANT_S_UNKNOWN\" -> %llu"
+ "assertion failure: \"(has_full_logging) != OS_VARIANT_S_UNKNOWN\" -> %llu"
+ "assertion failure: \"(internal_content) != OS_VARIANT_S_UNKNOWN\" -> %llu"
+ "assertion failure: \"(internal_diags_profile) != OS_VARIANT_S_UNKNOWN\" -> %llu"
+ "assertion failure: \"(is_ephemeral) != OS_VARIANT_S_UNKNOWN\" -> %llu"
+ "assertion failure: \"base_system_content == OS_VARIANT_S_UNKNOWN\" -> %llu"
+ "assertion failure: \"can_has_debugger == OS_VARIANT_S_UNKNOWN\" -> %llu"
+ "assertion failure: \"darwinos_content == OS_VARIANT_S_UNKNOWN\" -> %llu"
+ "assertion failure: \"error\" -> %llu"
+ "assertion failure: \"factory_content == OS_VARIANT_S_UNKNOWN\" -> %llu"
+ "assertion failure: \"getpid() == 1\" -> %llu"
+ "assertion failure: \"internal_content == OS_VARIANT_S_UNKNOWN\" -> %llu"
+ "assertion failure: \"internal_diags_profile == OS_VARIANT_S_UNKNOWN\" -> %llu"
+ "assertion failure: \"is_ephemeral == OS_VARIANT_S_UNKNOWN\" -> %llu"
+ "assertion failure: \"ret\" -> %llu"
+ "assertion failure: \"ret.r\" -> %llu"
+ "post-upgrade"
- "-h"
- "assertion failure: \"(base_system_content) != OS_VARIANT_S_UNKNOWN\" -> %lld"
- "assertion failure: \"(can_has_debugger) != OS_VARIANT_S_UNKNOWN\" -> %lld"
- "assertion failure: \"(darwinos_content) != OS_VARIANT_S_UNKNOWN\" -> %lld"
- "assertion failure: \"(factory_content) != OS_VARIANT_S_UNKNOWN\" -> %lld"
- "assertion failure: \"(has_full_logging) != OS_VARIANT_S_UNKNOWN\" -> %lld"
- "assertion failure: \"(internal_content) != OS_VARIANT_S_UNKNOWN\" -> %lld"
- "assertion failure: \"(internal_diags_profile) != OS_VARIANT_S_UNKNOWN\" -> %lld"
- "assertion failure: \"(is_ephemeral) != OS_VARIANT_S_UNKNOWN\" -> %lld"
- "assertion failure: \"base_system_content == OS_VARIANT_S_UNKNOWN\" -> %lld"
- "assertion failure: \"can_has_debugger == OS_VARIANT_S_UNKNOWN\" -> %lld"
- "assertion failure: \"darwinos_content == OS_VARIANT_S_UNKNOWN\" -> %lld"
- "assertion failure: \"error\" -> %lld"
- "assertion failure: \"factory_content == OS_VARIANT_S_UNKNOWN\" -> %lld"
- "assertion failure: \"getpid() == 1\" -> %lld"
- "assertion failure: \"internal_content == OS_VARIANT_S_UNKNOWN\" -> %lld"
- "assertion failure: \"internal_diags_profile == OS_VARIANT_S_UNKNOWN\" -> %lld"
- "assertion failure: \"is_ephemeral == OS_VARIANT_S_UNKNOWN\" -> %lld"
- "assertion failure: \"ret\" -> %lld"
- "assertion failure: \"ret.r\" -> %lld"
- "ui"

```
