## skywalkctl

> `/usr/sbin/skywalkctl`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA.__data`

```diff

 170.0.0.0.0
-  __TEXT.__text: 0x11864
+  __TEXT.__text: 0x1185c
   __TEXT.__auth_stubs: 0x690
-  __TEXT.__cstring: 0xc2fc
+  __TEXT.__cstring: 0xc390
   __TEXT.__const: 0x60
   __TEXT.__unwind_info: 0x350
-  __DATA_CONST.__const: 0x4388
+  __DATA_CONST.__const: 0x43a8
   __DATA_CONST.__auth_got: 0x348
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   Functions: 193
   Symbols:   115
-  CStrings:  2092
+  CStrings:  2096
 
Functions:
~ sub_100004710 : 928 -> 924
~ sub_100004ab0 -> sub_100004aac : 2876 -> 2872
CStrings:
+ "\t\t%llu dropped, flow not owned by Tx nexus port\n"
+ "\t%llu dropped due to wrap flag not matching ring direction\n"
+ "FilterDropBadDirection"
+ "TxFlowWrongPort"
```
