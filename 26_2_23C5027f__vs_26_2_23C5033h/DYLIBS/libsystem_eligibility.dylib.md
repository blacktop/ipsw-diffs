## libsystem_eligibility.dylib

> `/usr/lib/system/libsystem_eligibility.dylib`

```diff

-286.60.18.502.1
-  __TEXT.__text: 0x3360
-  __TEXT.__auth_stubs: 0x290
-  __TEXT.__const: 0x558
-  __TEXT.__cstring: 0x3d72
-  __TEXT.__oslogstring: 0x2eb
-  __TEXT.__unwind_info: 0xc0
+286.60.23.502.2
+  __TEXT.__text: 0x4154
+  __TEXT.__auth_stubs: 0x280
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x3f2f
+  __TEXT.__oslogstring: 0x3d6
+  __TEXT.__unwind_info: 0xb8
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0xa88
-  __AUTH_CONST.__auth_got: 0x148
+  __DATA_CONST.__const: 0x5f0
+  __AUTH_CONST.__auth_got: 0x140
   __AUTH_CONST.__const: 0x40
   __DATA_DIRTY.__bss: 0x10
   - /usr/lib/system/libdispatch.dylib

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 9DEE1995-C220-382A-AA57-084C69A90F44
-  Functions: 25
-  Symbols:   87
-  CStrings:  396
+  UUID: 35090E6B-1BBD-344C-832F-007F0C676A5E
+  Functions: 26
+  Symbols:   86
+  CStrings:  410
 
Symbols:
+ ___block_descriptor_tmp.375
+ _xpc_array_set_string
- ___block_descriptor_tmp.369
- _xpc_array_get_count
- _xpc_string_create
CStrings:
+ "%s: Failed to copy precise location allowlist path, falling back to compile time source"
+ "%s: Failed to read precise locations allowlist, falling back to compile time source: %d"
+ "%s: Unsupported domain %llu; falling back to private plist"
+ "/private/var/db/eligibilityd/eligibility_allowlists.plist"
+ "OS_ELIGIBILITY_DOMAIN_AGE_ASSURANCE_JURISDICTION_LIFECYCLE"
+ "OS_ELIGIBILITY_INPUT_IS_ACCOUNT_ELIGIBILE_FOR_AGE_ASSURANCE"
+ "OS_ELIGIBILITY_INPUT_IS_CHILD"
+ "OS_ELIGIBILITY_INPUT_IS_TEEN"
+ "Precise Locations"
+ "US-TX"
+ "com.apple.os-eligibility-domain.change.age-assurance-jurisdiction-lifecycle"
+ "copy_eligibility_precise_location_allowlist_path"
+ "eligibility_domain_to_file"
+ "os_eligibility_precise_locations"

```
