## libsystem_eligibility.dylib

> `/usr/lib/system/libsystem_eligibility.dylib`

```diff

-160.60.1.0.0
-  __TEXT.__text: 0x30cc
-  __TEXT.__auth_stubs: 0x260
+181.101.2.0.0
+  __TEXT.__text: 0x3794
+  __TEXT.__auth_stubs: 0x2a0
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x2bfa
-  __TEXT.__oslogstring: 0x2de
+  __TEXT.__cstring: 0x2d5b
+  __TEXT.__oslogstring: 0x326
   __TEXT.__unwind_info: 0xb8
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x428
-  __AUTH_CONST.__auth_got: 0x130
+  __DATA_CONST.__const: 0x448
+  __AUTH_CONST.__auth_got: 0x150
   __AUTH_CONST.__const: 0x70
   __DATA.__bss: 0x10
   - /usr/lib/system/libdispatch.dylib

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 4C8AC363-F171-3A08-85F8-7542B9C79A87
-  Functions: 27
-  Symbols:   76
-  CStrings:  319
+  UUID: 6BA33F46-F163-3F14-9352-BE162CA59201
+  Functions: 26
+  Symbols:   81
+  CStrings:  329
 
Symbols:
+ __block_descriptor_tmp.212
+ __os_log_fault_impl
+ _load_eligibility_answers
+ _os_eligibility_precise_locations
+ _xpc_array_create
+ _xpc_array_get_count
+ _xpc_string_create
- __block_descriptor_tmp.167
- _copy_eligibility_domain_public_answer_plist_path
CStrings:
+ "%s: Unknown eligibility answer file type: %llu"
+ "%s: Unsupported domain %llu; falling back to private plist"
+ "OS_ELIGIBILITY_DOMAIN_HIGHLIGHTS_MARKETPLACES"
+ "OS_ELIGIBILITY_DOMAIN_PERSONAL_QA"
+ "OS_ELIGIBILITY_DOMAIN_SIRI_WITH_APP_INTENTS"
+ "OS_ELIGIBILITY_INPUT_PRECISE_LOCATION"
+ "US-UT"
+ "com.apple.os-eligibility-domain.change.highlights-marketplaces"
+ "com.apple.os-eligibility-domain.change.personal-qa"
+ "com.apple.os-eligibility-domain.change.siri-with-app-intents"
+ "copy_eligibility_file_path"
+ "eligibility_domain_to_file"
- "%s: Unknown plist for domain %llu"
- "OS_ELIGIBILITY_INPUT_INITIAL_SETUP_LOCATION"

```
