## pcsstatus

> `/usr/libexec/pcsstatus`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1303.0.6.0.0
-  __TEXT.__text: 0xf9dc
-  __TEXT.__auth_stubs: 0x840
+1303.40.9.0.0
+  __TEXT.__text: 0xf9ec
+  __TEXT.__auth_stubs: 0x850
   __TEXT.__objc_stubs: 0x1d60
   __TEXT.__objc_methlist: 0x7e4
   __TEXT.__const: 0x98

   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x430
+  __DATA_CONST.__auth_got: 0x438
   __DATA_CONST.__got: 0x308
   __DATA.__objc_const: 0x9d8
   __DATA.__objc_selrefs: 0x9b8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 269
-  Symbols:   239
+  Symbols:   240
   CStrings:  744
 
Symbols:
+ _SOSCCIsSOSTrustAndSyncingEnabledCachedValue
Functions:
~ sub_100003c40 : 644 -> 660
```
