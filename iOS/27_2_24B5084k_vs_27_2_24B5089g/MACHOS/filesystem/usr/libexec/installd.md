## installd

> `/usr/libexec/installd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1680.40.6.502.1
-  __TEXT.__text: 0x72b3c
+1680.40.8.0.1
+  __TEXT.__text: 0x72d00
   __TEXT.__auth_stubs: 0x1770
   __TEXT.__objc_stubs: 0x9340
   __TEXT.__objc_methlist: 0x3a24
   __TEXT.__const: 0x1c8
-  __TEXT.__cstring: 0x19583
+  __TEXT.__cstring: 0x19733
   __TEXT.__objc_classname: 0x6af
   __TEXT.__objc_methtype: 0x2535
   __TEXT.__objc_methname: 0xdb77

   __TEXT.__unwind_info: 0x19a0
   __TEXT.__eh_frame: 0x218
   __DATA_CONST.__const: 0x1638
-  __DATA_CONST.__cfstring: 0xaa60
+  __DATA_CONST.__cfstring: 0xaac0
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe0

   - /usr/lib/swift/libswiftos.dylib
   Functions: 1615
   Symbols:   544
-  CStrings:  4005
+  CStrings:  4008
 
Functions:
~ sub_100053cc8 : 948 -> 1400
CStrings:
+ "\"%@\" has the \"%@\" entitlement, which is set to an empty list. At least one app's application identifier is required."
+ "\"%@\" is missing the \"%@\" entitlement. This entitlement is required on this app because the extensions with bundle identifier(s) %@ in the app, carry this entitlement."
+ "The app extension at \"%@\" has the \"%@\" entitlement, which is set to an empty list. At least one extension's application identifier is required."
```
