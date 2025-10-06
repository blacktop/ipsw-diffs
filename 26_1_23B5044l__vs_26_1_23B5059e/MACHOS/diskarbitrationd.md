## diskarbitrationd

> `/usr/libexec/diskarbitrationd`

```diff

-535.40.2.0.0
-  __TEXT.__text: 0x1a3b0
-  __TEXT.__auth_stubs: 0x16d0
+535.40.5.0.0
+  __TEXT.__text: 0x1a420
+  __TEXT.__auth_stubs: 0x16f0
   __TEXT.__objc_stubs: 0x5e0
   __TEXT.__objc_methlist: 0xc8
-  __TEXT.__cstring: 0x2f7f
+  __TEXT.__cstring: 0x2fb3
   __TEXT.__const: 0x88
   __TEXT.__oslogstring: 0xb
   __TEXT.__gcc_except_tab: 0xe4

   __TEXT.__objc_methtype: 0x102
   __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0x5d0
-  __DATA_CONST.__auth_got: 0xb78
+  __DATA_CONST.__auth_got: 0xb88
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0xdc0

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 0DCF401F-8C4E-36DE-AA8E-3050589F681B
+  UUID: 2E984082-E1E0-3D28-B55E-4784CC528CC5
   Functions: 501
-  Symbols:   416
-  CStrings:  917
+  Symbols:   418
+  CStrings:  919
 
Symbols:
+ _strncasecmp
+ _strnlen
Functions:
~ sub_10000130c : 388 -> 408
~ sub_10000b670 -> sub_10000b684 : 1900 -> 1864
~ sub_100011b18 -> sub_100011b08 : 1160 -> 1288
CStrings:
+ "=-"
+ "Unknown mount arg string %s"
+ "unable to create session, id = %s [%d] (status code 0x%08X)."
- "unable to create session, id = %s [%d]."

```
