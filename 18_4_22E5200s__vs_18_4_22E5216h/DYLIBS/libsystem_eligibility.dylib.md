## libsystem_eligibility.dylib

> `/usr/lib/system/libsystem_eligibility.dylib`

```diff

-181.100.8.502.6
-  __TEXT.__text: 0x3648
-  __TEXT.__auth_stubs: 0x280
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x2cb8
-  __TEXT.__oslogstring: 0x2de
-  __TEXT.__unwind_info: 0xb0
+181.100.26.0.0
+  __TEXT.__text: 0x37ec
+  __TEXT.__auth_stubs: 0x290
+  __TEXT.__const: 0x80
+  __TEXT.__cstring: 0x2d5b
+  __TEXT.__oslogstring: 0x326
+  __TEXT.__unwind_info: 0xb8
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x468
-  __AUTH_CONST.__auth_got: 0x140
+  __DATA_CONST.__const: 0x470
+  __AUTH_CONST.__auth_got: 0x148
   __AUTH_CONST.__const: 0x40
   __DATA_DIRTY.__bss: 0x10
   - /usr/lib/system/libdispatch.dylib

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 23
-  Symbols:   67
-  CStrings:  324
+  Functions: 24
+  Symbols:   69
+  CStrings:  329
 
Symbols:
+ __os_log_fault_impl
+ _load_eligibility_answers
- _load_eligibility_plist
CStrings:
+ "%s: Unknown eligibility answer file type: %llu"
+ "%s: Unsupported domain %llu; falling back to private plist"
+ "OS_ELIGIBILITY_DOMAIN_HIGHLIGHTS_MARKETPLACES"
+ "com.apple.os-eligibility-domain.change.highlights-marketplaces"
+ "copy_eligibility_file_path"
+ "eligibility_domain_to_file"
- "%s: Unknown plist for domain %llu"

```
