## DiagnosticExtensionsDaemon

> `/System/Library/PrivateFrameworks/DiagnosticExtensionsDaemon.framework/DiagnosticExtensionsDaemon`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-221.0.0.0.0
-  __TEXT.__text: 0x759a8
-  __TEXT.__objc_methlist: 0x6fcc
+222.0.0.0.0
+  __TEXT.__text: 0x75d10
+  __TEXT.__objc_methlist: 0x700c
   __TEXT.__const: 0x362
-  __TEXT.__cstring: 0x56f0
+  __TEXT.__cstring: 0x5700
   __TEXT.__gcc_except_tab: 0x1ac0
-  __TEXT.__oslogstring: 0x9808
+  __TEXT.__oslogstring: 0x9828
   __TEXT.__ustring: 0xc
   __TEXT.__constg_swiftt: 0x8c
   __TEXT.__swift5_typeref: 0x48

   __TEXT.__swift5_reflstr: 0x80
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x1cc0
+  __TEXT.__unwind_info: 0x1cd0
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2150
+  __DATA_CONST.__const: 0x2180
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b80
+  __DATA_CONST.__objc_selrefs: 0x3b98
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1b0
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__got: 0x6e8
   __AUTH_CONST.__const: 0xc20
-  __AUTH_CONST.__cfstring: 0x5020
-  __AUTH_CONST.__objc_const: 0x13a70
+  __AUTH_CONST.__cfstring: 0x5040
+  __AUTH_CONST.__objc_const: 0x13aa0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x6a0
   __AUTH.__objc_data: 0x90
   __AUTH.__data: 0x90
-  __DATA.__objc_ivar: 0x5e4
+  __DATA.__objc_ivar: 0x5e8
   __DATA.__data: 0xad0
   __DATA.__bss: 0x1d0
   __DATA_DIRTY.__objc_data: 0x18e0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2921
-  Symbols:   5858
-  CStrings:  1787
+  Functions: 2926
+  Symbols:   5869
+  CStrings:  1789
 
Symbols:
+ -[DEDBugSession createdAt]
+ -[DEDBugSession persistence]
+ -[DEDBugSession setCreatedAt:]
+ -[DEDController attachmentHandler]
+ -[DEDController dedDirectory]
+ GCC_except_table122
+ GCC_except_table125
+ GCC_except_table128
+ GCC_except_table138
+ _DEDBugSessionKeyCreatedAt
+ _OBJC_IVAR_$_DEDBugSession._createdAt
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ _objc_msgSend$createdAt
+ _objc_msgSend$distantPast
- GCC_except_table118
- GCC_except_table127
- GCC_except_table134
CStrings:
+ "createdAt"
+ "evicting stale fileless session [%{public}@]"
```
