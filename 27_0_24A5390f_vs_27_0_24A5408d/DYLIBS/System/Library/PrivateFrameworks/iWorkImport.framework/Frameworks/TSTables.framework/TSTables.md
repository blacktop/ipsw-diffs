## TSTables

> `/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSTables.framework/TSTables`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-487.0.0.0.0
-  __TEXT.__text: 0x69e488
+488.0.0.0.0
+  __TEXT.__text: 0x69e8fc
   __TEXT.__init_offsets: 0x10
-  __TEXT.__objc_methlist: 0x35a04
-  __TEXT.__gcc_except_tab: 0x9b960
+  __TEXT.__objc_methlist: 0x35a5c
+  __TEXT.__gcc_except_tab: 0x9ba20
   __TEXT.__const: 0x3e9e6
-  __TEXT.__cstring: 0x451bc
+  __TEXT.__cstring: 0x451d0
   __TEXT.__ustring: 0x1f24
   __TEXT.__swift5_typeref: 0x32
   __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__unwind_info: 0x2d990
+  __TEXT.__unwind_info: 0x2d9c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x2b8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x16250
+  __DATA_CONST.__objc_selrefs: 0x16280
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0xc78
   __DATA_CONST.__objc_arraydata: 0x3c8
   __DATA_CONST.__got: 0x1998
   __AUTH_CONST.__const: 0x19b50
-  __AUTH_CONST.__cfstring: 0xec60
-  __AUTH_CONST.__objc_const: 0x45440
+  __AUTH_CONST.__cfstring: 0xec40
+  __AUTH_CONST.__objc_const: 0x454d0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x330
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1b50
+  __AUTH_CONST.__auth_got: 0x1b48
   __AUTH.__objc_data: 0x104a0
-  __DATA.__objc_ivar: 0x29ac
+  __DATA.__objc_ivar: 0x29bc
   __DATA.__data: 0x24e0
   __DATA.__bss: 0x1ad0
   __DATA.__common: 0x3c

   - /System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSCalculationEngine.framework/TSCalculationEngine
   - /System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSCollaborationKit.framework/TSCollaborationKit
   - /System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSDrawables.framework/TSDrawables
+  - /System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSFundamentals.framework/TSFundamentals
+  - /System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSGeometry.framework/TSGeometry
   - /System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSKit.framework/TSKit
   - /System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSPersistence.framework/TSPersistence
   - /System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSStyles.framework/TSStyles

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 36022
-  Symbols:   13345
+  Functions: 36033
+  Symbols:   13344
   CStrings:  6026
 
Symbols:
- _TSULogCat_IsCategoryEnabled
CStrings:
+ "%d is not a valid node tag, seen at offset: %lu"
- "TSTMergeOwnerDetailedLogCat"
```
