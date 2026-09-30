## libsystem_eligibility.dylib

> `/usr/lib/system/libsystem_eligibility.dylib`

```diff

-160.60.1.0.0
-  __TEXT.__text: 0x30b8
-  __TEXT.__auth_stubs: 0x250
+181.100.26.0.0
+  __TEXT.__text: 0x37ec
+  __TEXT.__auth_stubs: 0x290
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x2bd6
-  __TEXT.__oslogstring: 0x2de
-  __TEXT.__unwind_info: 0xb0
+  __TEXT.__cstring: 0x2d5b
+  __TEXT.__oslogstring: 0x326
+  __TEXT.__unwind_info: 0xb8
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x450
-  __AUTH_CONST.__auth_got: 0x128
+  __DATA_CONST.__const: 0x470
+  __AUTH_CONST.__auth_got: 0x148
   __AUTH_CONST.__const: 0x40
   __DATA_DIRTY.__bss: 0x10
   - /usr/lib/system/libdispatch.dylib

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 25
-  Symbols:   64
-  CStrings:  318
+  Functions: 24
+  Symbols:   69
+  CStrings:  329
 
Symbols:
+ __os_log_fault_impl
+ _load_eligibility_answers
+ _os_eligibility_precise_locations
+ _xpc_array_create
+ _xpc_array_get_count
+ _xpc_string_create
- _load_eligibility_plist
CStrings:
+ "%s: Unknown eligibility answer file type: %llu"
+ "%s: Unsupported domain %llu; falling back to private plist"
+ "OS_ELIGIBILITY_DOMAIN_HIGHLIGHTS_MARKETPLACES"
+ "OS_ELIGIBILITY_DOMAIN_PERSONAL_QA"
+ "OS_ELIGIBILITY_DOMAIN_SIRI_WITH_APP_INTENTS"
+ "OS_ELIGIBILITY_INPUT_CHINA_CELLULAR"
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
