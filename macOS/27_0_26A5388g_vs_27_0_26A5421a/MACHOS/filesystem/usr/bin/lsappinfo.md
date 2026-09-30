## lsappinfo

> `/usr/bin/lsappinfo`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`

```diff

-1510.400.0.0.0
-  __TEXT.__text: 0x207e4
+1517.0.1.401.0
+  __TEXT.__text: 0x20800
   __TEXT.__auth_stubs: 0x1070
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x7007
+  __TEXT.__cstring: 0x7053
   __TEXT.__oslogstring: 0x5
   __DATA_CONST.__const: 0x4f0
   __DATA_CONST.__cfstring: 0x2e0

   __DATA_CONST.__auth_got: 0x838
   __DATA_CONST.__got: 0x6f8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__data: 0x9b1
+  __DATA.__data: 0xa21
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x1740
   __DATA.__common: 0x168

   - /usr/lib/libobjc.A.dylib
   Functions: 194
   Symbols:   502
-  CStrings:  1086
+  CStrings:  1090
 
Functions:
~ sub_100005368 : 1744 -> 1768
~ sub_100005ac0 -> sub_100005ad8 : 240 -> 244
CStrings:
+ "exec"
+ "kLSNotificationApplicationReExeced"
+ "kLSNotifyApplicationRebirth"
+ "rebirth"
```
