## mc_mobile_tunnel

> `/usr/libexec/mc_mobile_tunnel`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-111.0.0.0.0
-  __TEXT.__text: 0x7064
-  __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_stubs: 0x12e0
+113.0.2.0.0
+  __TEXT.__text: 0x7098
+  __TEXT.__auth_stubs: 0x6e0
+  __TEXT.__objc_stubs: 0x1300
   __TEXT.__objc_methlist: 0x3f8
   __TEXT.__const: 0xa0
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__cstring: 0x7f1
-  __TEXT.__objc_methname: 0x1417
+  __TEXT.__objc_methname: 0x1432
   __TEXT.__oslogstring: 0xb99
   __TEXT.__objc_classname: 0x48
   __TEXT.__objc_methtype: 0x1e2

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x378
+  __DATA_CONST.__auth_got: 0x380
   __DATA_CONST.__got: 0x360
   __DATA.__objc_const: 0x508
-  __DATA.__objc_selrefs: 0x538
+  __DATA.__objc_selrefs: 0x540
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0x140
   __DATA.__bss: 0x48

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 134
-  Symbols:   231
-  CStrings:  378
+  Symbols:   232
+  CStrings:  379
 
Symbols:
+ _MDMCreateSecureLAContextWithPasscodeData
Functions:
~ sub_100003698 : 268 -> 320
CStrings:
+ "clearPasscodeWithEscrowKeybagData:secretContext:outError:"
+ "externalizedContext"
- "clearPasscodeWithEscrowKeybagData:secret:outError:"
```
