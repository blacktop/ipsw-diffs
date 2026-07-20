## StorageKit

> `/System/Library/PrivateFrameworks/StorageKit.framework/Versions/A/StorageKit`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1076.0.1.0.0
-  __TEXT.__text: 0x4ce28
+1076.0.3.0.0
+  __TEXT.__text: 0x4cf38
   __TEXT.__objc_methlist: 0x4e24
   __TEXT.__const: 0x12a
   __TEXT.__oslogstring: 0x1b9f
-  __TEXT.__cstring: 0x56ff
-  __TEXT.__gcc_except_tab: 0x1c14
+  __TEXT.__cstring: 0x571a
+  __TEXT.__gcc_except_tab: 0x1c38
   __TEXT.__swift5_typeref: 0x56
   __TEXT.__swift5_fieldmd: 0x30
   __TEXT.__constg_swiftt: 0x74

   __DATA_CONST.__objc_arraydata: 0x1e8
   __DATA_CONST.__got: 0x3d8
   __AUTH_CONST.__const: 0x1098
-  __AUTH_CONST.__cfstring: 0x4200
+  __AUTH_CONST.__cfstring: 0x4220
   __AUTH_CONST.__objc_const: 0x9468
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0xd8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   Functions: 1803
-  Symbols:   4286
-  CStrings:  918
+  Symbols:   4287
+  CStrings:  919
 
Symbols:
+ _realpath$DARWIN_EXTSN
Functions:
~ -[SKAPFSDisk mountSnapshot:mountPoint:resultMountPoint:error:] : 596 -> 868
CStrings:
+ "Cannot resolve mount point"
```
