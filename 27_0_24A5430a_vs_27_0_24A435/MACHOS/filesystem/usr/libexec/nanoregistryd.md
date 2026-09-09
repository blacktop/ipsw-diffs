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

 1075.1.4.0.0
-  __TEXT.__text: 0x100784
+  __TEXT.__text: 0x10080c
   __TEXT.__auth_stubs: 0x1110
   __TEXT.__objc_stubs: 0x11000
   __TEXT.__objc_methlist: 0xdadc
   __TEXT.__const: 0x69a
   __TEXT.__gcc_except_tab: 0x1cc0
   __TEXT.__objc_methname: 0x1c603
-  __TEXT.__cstring: 0xe0d8
+  __TEXT.__cstring: 0xe174
   __TEXT.__oslogstring: 0x16281
   __TEXT.__objc_classname: 0x21b9
   __TEXT.__objc_methtype: 0x4bc9

   __TEXT.__ustring: 0x4ac
   __TEXT.__unwind_info: 0x3a60
   __DATA_CONST.__const: 0x4bc0
-  __DATA_CONST.__cfstring: 0xc0a0
+  __DATA_CONST.__cfstring: 0xc120
   __DATA_CONST.__objc_classlist: 0x7e8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x220

   - /usr/lib/swift/libswiftos.dylib
   Functions: 5830
   Symbols:   707
-  CStrings:  8656
+  CStrings:  8661
 
Functions:
~ sub_1000b09c4 : 14696 -> 14832
CStrings:
+ "27"
+ "704c505e-d459-42a9-b3b1-81b4cfa5911d"
+ "AllDayHeartRate"
+ "DeviceSupportsAudioIntelligence"
+ "DeviceSupportsContinuousHeartRate"
+ "d2f9b521-e715-4a96-94f9-19c209511ee5"
- "32"
```
