## libsystem_eligibility.dylib

> `/usr/lib/system/libsystem_eligibility.dylib`

```diff

-160.60.1.0.0
-  __TEXT.__text: 0x30b8
-  __TEXT.__auth_stubs: 0x250
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x2bd6
+181.100.8.502.6
+  __TEXT.__text: 0x3648
+  __TEXT.__auth_stubs: 0x280
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x2cb8
   __TEXT.__oslogstring: 0x2de
   __TEXT.__unwind_info: 0xb0
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x450
-  __AUTH_CONST.__auth_got: 0x128
+  __DATA_CONST.__const: 0x468
+  __AUTH_CONST.__auth_got: 0x140
   __AUTH_CONST.__const: 0x40
   __DATA_DIRTY.__bss: 0x10
   - /usr/lib/system/libdispatch.dylib

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 25
-  Symbols:   64
-  CStrings:  318
+  Functions: 23
+  Symbols:   67
+  CStrings:  324
 
Symbols:
+ _os_eligibility_precise_locations
+ _xpc_array_create
+ _xpc_array_get_count
+ _xpc_string_create
CStrings:
+ "OS_ELIGIBILITY_DOMAIN_PERSONAL_QA"
+ "OS_ELIGIBILITY_DOMAIN_SIRI_WITH_APP_INTENTS"
+ "OS_ELIGIBILITY_INPUT_CHINA_CELLULAR"
+ "OS_ELIGIBILITY_INPUT_PRECISE_LOCATION"
+ "US-UT"
+ "com.apple.os-eligibility-domain.change.personal-qa"
+ "com.apple.os-eligibility-domain.change.siri-with-app-intents"
- "OS_ELIGIBILITY_INPUT_INITIAL_SETUP_LOCATION"

```
