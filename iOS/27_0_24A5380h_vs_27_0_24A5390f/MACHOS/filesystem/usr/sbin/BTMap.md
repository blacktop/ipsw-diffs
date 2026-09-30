## BTMap

> `/usr/sbin/BTMap`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2700.35.0.0.0
-  __TEXT.__text: 0x4344
-  __TEXT.__auth_stubs: 0x600
+2700.38.0.0.0
+  __TEXT.__text: 0x44e4
+  __TEXT.__auth_stubs: 0x610
   __TEXT.__objc_stubs: 0x1020
   __TEXT.__objc_methlist: 0x4a4
   __TEXT.__const: 0x28
   __TEXT.__cstring: 0x48e
   __TEXT.__objc_methname: 0xd93
-  __TEXT.__oslogstring: 0x37a
+  __TEXT.__oslogstring: 0x44b
   __TEXT.__objc_classname: 0x66
   __TEXT.__objc_methtype: 0x270
   __TEXT.__gcc_except_tab: 0x40

   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__auth_got: 0x310
+  __DATA_CONST.__auth_got: 0x318
   __DATA_CONST.__got: 0x178
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x790

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 106
-  Symbols:   153
-  CStrings:  333
+  Symbols:   154
+  CStrings:  336
 
Symbols:
+ _objc_retain_x22
Functions:
~ sub_1000046c4 : 1096 -> 1512
CStrings:
+ "serializeIMChats: bestIMHandle is nil; omitting local participant from chat %@"
+ "serializeIMChats: nil participant handle (raw ID %@) in chat %@; skipping"
+ "serializeIMChats: no IMChat for identifier %@; skipping"
```
