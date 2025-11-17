## libsystem_eligibility.dylib

> `/usr/lib/system/libsystem_eligibility.dylib`

```diff

-286.60.23.502.2
-  __TEXT.__text: 0x4154
+286.62.10.0.0
+  __TEXT.__text: 0x4180
   __TEXT.__auth_stubs: 0x280
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x3f2f
+  __TEXT.__const: 0x80
+  __TEXT.__cstring: 0x3fb0
   __TEXT.__oslogstring: 0x3d6
   __TEXT.__unwind_info: 0xb8
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x5f0
+  __DATA_CONST.__const: 0x5f8
   __AUTH_CONST.__auth_got: 0x140
   __AUTH_CONST.__const: 0x40
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 35090E6B-1BBD-344C-832F-007F0C676A5E
+  UUID: 0871BA35-A528-39B9-9176-144C6E193129
   Functions: 26
   Symbols:   86
-  CStrings:  410
+  CStrings:  412
 
Symbols:
+ ___block_descriptor_tmp.377
- ___block_descriptor_tmp.375
Functions:
~ sub_29b490ac8 -> sub_29b4d3ac8 : 624 -> 628
~ _os_eligibility_get_domain_notification_name : 2128 -> 2140
~ _os_eligibility_domain_for_name : 4404 -> 4432
CStrings:
+ "OS_ELIGIBILITY_DOMAIN_AGE_ASSURANCE_REGULATORY_FEATURES"
+ "com.apple.os-eligibility-domain.change.age-assurance-regulatory-features"

```
