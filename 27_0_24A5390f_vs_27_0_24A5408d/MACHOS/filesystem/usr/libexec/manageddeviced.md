## manageddeviced

> `/usr/libexec/manageddeviced`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-24.0.0.0.0
-  __TEXT.__text: 0x414d4
-  __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__objc_stubs: 0x8d60
-  __TEXT.__objc_methlist: 0x3fbc
+26.0.0.0.0
+  __TEXT.__text: 0x41950
+  __TEXT.__auth_stubs: 0xc90
+  __TEXT.__objc_stubs: 0x8dc0
+  __TEXT.__objc_methlist: 0x3fd4
   __TEXT.__const: 0x110
-  __TEXT.__objc_methname: 0x9ce6
+  __TEXT.__objc_methname: 0x9d72
   __TEXT.__cstring: 0x2f5e
   __TEXT.__objc_classname: 0xd61
-  __TEXT.__objc_methtype: 0xdc1
+  __TEXT.__objc_methtype: 0xdf2
   __TEXT.__gcc_except_tab: 0x6ac
-  __TEXT.__oslogstring: 0x63d8
+  __TEXT.__oslogstring: 0x651b
   __TEXT.__dlopen_cstrs: 0x55
   __TEXT.__ustring: 0x7d0
-  __TEXT.__unwind_info: 0x1218
+  __TEXT.__unwind_info: 0x1210
   __DATA_CONST.__const: 0x1960
   __DATA_CONST.__cfstring: 0x3480
   __DATA_CONST.__objc_classlist: 0x358

   __DATA_CONST.__objc_arraydata: 0x238
   __DATA_CONST.__objc_arrayobj: 0x4b0
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA_CONST.__auth_got: 0x670
-  __DATA_CONST.__got: 0x930
+  __DATA_CONST.__auth_got: 0x658
+  __DATA_CONST.__got: 0x9a8
   __DATA.__objc_const: 0x8768
-  __DATA.__objc_selrefs: 0x28c0
+  __DATA.__objc_selrefs: 0x28d8
   __DATA.__objc_ivar: 0x1e8
   __DATA.__objc_data: 0x2170
   __DATA.__data: 0x480

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
-  Functions: 1696
-  Symbols:   517
-  CStrings:  2675
+  Functions: 1703
+  Symbols:   529
+  CStrings:  2684
 
Symbols:
+ _CONTAINER_PERSONA_PRIMARY
+ _OBJC_CLASS_$_UMUserPersonaProperties
+ _container_copy_sandbox_token
+ _container_error_get_type
+ _container_get_path
+ _container_query_create
+ _container_query_free
+ _container_query_get_last_error
+ _container_query_get_single_result
+ _container_query_operation_set_flags
+ _container_query_set_class
+ _container_query_set_identifiers
+ _container_query_set_persona_unique_string
+ _sandbox_extension_consume
+ _sandbox_extension_release
+ _xpc_string_create
- _container_acquire_sandbox_extension
- _container_copy_path
- _container_create_or_lookup_for_current_user
- _container_free_object
CStrings:
+ "Failed to look up enterprise personas: %{public}@"
+ "SKIPPING Set state: %{public}@ (was %{public}@), for bundle identifier: %{public}@"
+ "Set state: %{public}@ (was %{public}@), for bundle identifier: %{public}@"
+ "Using CONTAINER_PERSONA_PRIMARY (default persona) for container query"
+ "Using enterprise persona %{public}@ for container query"
+ "_enterprisePersonaUniqueStringForContainerQuery"
+ "_withSandboxExtensionForApp:containerManager:do:"
+ "container_copy_sandbox_token %{public}@ returned NULL for path '%{public}@'"
+ "personaPropertiesForPersonaType:withError:"
+ "sandbox_extension_consume %{public}@ failed for path '%{public}@'"
+ "sandbox_extension_consume %{public}@ succeeded for path '%{public}@'"
+ "v136@0:8@16{?=^?^?^?^?^?^?^?^?^?^?^?^?^?}24@?128"
- "Set state: %{public}@, for bundle identifier: %{public}@"
- "container_acquire_sandbox_extension %{public}@ failed, error %llu, path '%{public}@'"
- "container_acquire_sandbox_extension %{public}@ succeeded for path '%{public}@'"
```
