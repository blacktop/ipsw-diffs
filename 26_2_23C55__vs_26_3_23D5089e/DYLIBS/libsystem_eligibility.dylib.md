## libsystem_eligibility.dylib

> `/usr/lib/system/libsystem_eligibility.dylib`

```diff

-286.62.11.0.0
-  __TEXT.__text: 0x4180
+289.80.52.502.1
+  __TEXT.__text: 0x42e4
   __TEXT.__auth_stubs: 0x280
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x3fb0
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x4044
   __TEXT.__oslogstring: 0x3d6
   __TEXT.__unwind_info: 0xb8
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x5f8
+  __DATA_CONST.__const: 0x600
   __AUTH_CONST.__auth_got: 0x140
   __AUTH_CONST.__const: 0x40
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 49C96D1F-4D2D-38BE-B702-6638230EDE4C
+  UUID: D2E37A84-6E6E-376D-98DB-32F2B84E0C6C
   Functions: 26
   Symbols:   86
-  CStrings:  412
+  CStrings:  416
 
Symbols:
+ ___block_descriptor_tmp.380
- ___block_descriptor_tmp.377
Functions:
~ sub_29b54f858 -> sub_29d1b0858 : 624 -> 628
~ _os_eligibility_get_domain_answer : 2176 -> 2528
CStrings:
+ "OS_ELIGIBILITY_INPUT_AGE_ASSURANCE_AREA_ID"
+ "OS_ELIGIBILITY_INPUT_IS_AGE_VERIFIED_ADULT"
+ "OS_ELIGIBILITY_INPUT_IS_CONNECTED_TO_AGE_VERIFIED_ADULT"
+ "US-LA"

```
