## nanoregistryd

> `/usr/libexec/nanoregistryd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-1075.11.0.0.0
-  __TEXT.__text: 0xfd7f8
+1075.12.0.0.0
+  __TEXT.__text: 0xfd834
   __TEXT.__auth_stubs: 0x1120
   __TEXT.__objc_stubs: 0x110a0
   __TEXT.__objc_methlist: 0xdb14
   __TEXT.__const: 0x6aa
   __TEXT.__gcc_except_tab: 0x1d30
   __TEXT.__objc_methname: 0x1c7f1
-  __TEXT.__cstring: 0xe299
-  __TEXT.__oslogstring: 0x164d9
+  __TEXT.__cstring: 0xe274
+  __TEXT.__oslogstring: 0x16513
   __TEXT.__objc_classname: 0x21b9
   __TEXT.__objc_methtype: 0x4be2
   __TEXT.__dlopen_cstrs: 0xef
   __TEXT.__ustring: 0x4ac
   __TEXT.__unwind_info: 0x4868
   __DATA_CONST.__const: 0x4c20
-  __DATA_CONST.__cfstring: 0xc1e0
+  __DATA_CONST.__cfstring: 0xc200
   __DATA_CONST.__objc_classlist: 0x7e8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x220

   - /usr/lib/swift/libswiftos.dylib
   Functions: 5834
   Symbols:   708
-  CStrings:  8683
+  CStrings:  8679
 
Functions:
~ sub_1000aec98 : 14916 -> 14976
CStrings:
+ "42"
+ "545ac5a6-e886-4466-b1b1-6621157fe0d6"
+ "NanoRegistry-1075.12"
+ "os_eligibility_get_domain_answer for ELAPHRUS returned %d"
- "27"
- "AllDayHeartRate"
- "Health"
- "NanoRegistry-1075.11"
- "acacia"
- "deprecateIRN1"
- "nebula"
- "sleepAlarmCoordination"
```
