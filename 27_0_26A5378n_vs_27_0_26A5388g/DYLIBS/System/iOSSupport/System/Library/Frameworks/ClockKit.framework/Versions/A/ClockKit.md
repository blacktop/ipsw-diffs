## ClockKit

> `/System/iOSSupport/System/Library/Frameworks/ClockKit.framework/Versions/A/ClockKit`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-2483.502.0.0.0
-  __TEXT.__text: 0x68664
-  __TEXT.__objc_methlist: 0x96bc
+2483.511.0.0.0
+  __TEXT.__text: 0x686b0
+  __TEXT.__objc_methlist: 0x96cc
   __TEXT.__const: 0x838
   __TEXT.__cstring: 0x3be3
   __TEXT.__oslogstring: 0x2793

   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35a8
+  __DATA_CONST.__objc_selrefs: 0x35b0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x4a8
   __DATA_CONST.__objc_arraydata: 0x5b8
   __DATA_CONST.__got: 0x718
   __AUTH_CONST.__const: 0xfd8
   __AUTH_CONST.__cfstring: 0x5420
-  __AUTH_CONST.__objc_const: 0xfa20
+  __AUTH_CONST.__objc_const: 0xfa50
   __AUTH_CONST.__objc_intobj: 0xc60
   __AUTH_CONST.__objc_doubleobj: 0x370
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__auth_got: 0x6d8
-  __DATA.__objc_ivar: 0xae8
+  __DATA.__objc_ivar: 0xaec
   __DATA.__data: 0x680
   __DATA.__bss: 0x840
   __DATA_DIRTY.__objc_data: 0x3930

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3818
-  Symbols:   8000
+  Functions: 3819
+  Symbols:   8003
   CStrings:  949
 
Symbols:
+ -[CLKDevice isSE]
+ GCC_except_table172
+ OBJC_IVAR_$_CLKDevice._isSE
+ _objc_msgSend$productFamilyType
- GCC_except_table171
Functions:
~ -[CLKDevice _loadDeviceInfo] : 3552 -> 3620
+ -[CLKDevice supportedCapabilitiesCache]
```
