## nanoregistryd

> `/usr/libexec/nanoregistryd`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1075.1.1.0.0
-  __TEXT.__text: 0x1006b4
-  __TEXT.__auth_stubs: 0x1100
-  __TEXT.__objc_stubs: 0x10fe0
-  __TEXT.__objc_methlist: 0xdad4
+1075.1.3.0.0
+  __TEXT.__text: 0x100784
+  __TEXT.__auth_stubs: 0x1110
+  __TEXT.__objc_stubs: 0x11000
+  __TEXT.__objc_methlist: 0xdadc
   __TEXT.__const: 0x69a
-  __TEXT.__gcc_except_tab: 0x1cd8
-  __TEXT.__objc_methname: 0x1c5ee
-  __TEXT.__cstring: 0xe0ac
+  __TEXT.__gcc_except_tab: 0x1cc0
+  __TEXT.__objc_methname: 0x1c603
+  __TEXT.__cstring: 0xe0d9
   __TEXT.__oslogstring: 0x16281
   __TEXT.__objc_classname: 0x21b9
   __TEXT.__objc_methtype: 0x4bc9
   __TEXT.__dlopen_cstrs: 0xef
   __TEXT.__ustring: 0x4ac
   __TEXT.__unwind_info: 0x3a60
-  __DATA_CONST.__const: 0x4ba0
-  __DATA_CONST.__cfstring: 0xc040
+  __DATA_CONST.__const: 0x4bc0
+  __DATA_CONST.__cfstring: 0xc0a0
   __DATA_CONST.__objc_classlist: 0x7e8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x220

   __DATA_CONST.__objc_arraydata: 0x478
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x210
-  __DATA_CONST.__auth_got: 0x890
-  __DATA_CONST.__got: 0xdc8
+  __DATA_CONST.__auth_got: 0x898
+  __DATA_CONST.__got: 0xdd0
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0x1a380
-  __DATA.__objc_selrefs: 0x5e88
+  __DATA.__objc_selrefs: 0x5e90
   __DATA.__objc_ivar: 0x11e0
   __DATA.__objc_data: 0x4f10
   __DATA.__data: 0x19d8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 5828
-  Symbols:   705
-  CStrings:  8652
+  Functions: 5830
+  Symbols:   707
+  CStrings:  8656
 
Symbols:
+ _MGIsQuestionValid
+ _NRDevicePropertyBiometryType
CStrings:
+ "128"
+ "NanoRegistry-1075.1.3"
+ "OysterCapability"
+ "PearlIDCapability"
+ "_currentBiometryType"
+ "touch-id"
- "72"
- "NanoRegistry-1075.1.1"
```
