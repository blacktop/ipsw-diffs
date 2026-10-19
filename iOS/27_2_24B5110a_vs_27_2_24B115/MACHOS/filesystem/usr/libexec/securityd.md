## securityd

> `/usr/libexec/securityd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

 62460.40.78.0.0
-  __TEXT.__text: 0x26c520
+  __TEXT.__text: 0x26d64c
   __TEXT.__auth_stubs: 0x43f0
-  __TEXT.__objc_stubs: 0x1dda0
-  __TEXT.__objc_methlist: 0x15f48
+  __TEXT.__objc_stubs: 0x1dde0
+  __TEXT.__objc_methlist: 0x15fe0
   __TEXT.__const: 0x920
-  __TEXT.__cstring: 0x23052
-  __TEXT.__objc_methname: 0x2ec67
-  __TEXT.__oslogstring: 0x30181
+  __TEXT.__cstring: 0x230c7
+  __TEXT.__objc_methname: 0x2ecbf
+  __TEXT.__oslogstring: 0x30404
   __TEXT.__swift5_typeref: 0x372
   __TEXT.__swift5_fieldmd: 0x120
-  __TEXT.__objc_classname: 0x2559
-  __TEXT.__objc_methtype: 0xb176
+  __TEXT.__objc_classname: 0x2584
+  __TEXT.__objc_methtype: 0xb1b4
   __TEXT.__constg_swiftt: 0x274
   __TEXT.__swift5_reflstr: 0xc3
   __TEXT.__swift5_capture: 0x1bc

   __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift_as_cont: 0x48
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__gcc_except_tab: 0xa0fc
+  __TEXT.__gcc_except_tab: 0xa104
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x7d20
+  __TEXT.__unwind_info: 0x7d40
   __TEXT.__eh_frame: 0xa60
-  __DATA_CONST.__const: 0x14b50
-  __DATA_CONST.__cfstring: 0x1cf20
-  __DATA_CONST.__objc_classlist: 0x910
+  __DATA_CONST.__const: 0x14b58
+  __DATA_CONST.__cfstring: 0x1cfa0
+  __DATA_CONST.__objc_classlist: 0x918
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__objc_superrefs: 0x810
-  __DATA_CONST.__objc_intobj: 0x1440
+  __DATA_CONST.__objc_superrefs: 0x818
+  __DATA_CONST.__objc_intobj: 0x1470
   __DATA_CONST.__objc_arraydata: 0x408
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x360
   __DATA_CONST.__auth_got: 0x2208
   __DATA_CONST.__got: 0x1560
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA.__objc_const: 0x23da8
-  __DATA.__objc_selrefs: 0x99a8
-  __DATA.__objc_ivar: 0x1af8
-  __DATA.__objc_data: 0x5d98
+  __DATA.__objc_const: 0x23ef0
+  __DATA.__objc_selrefs: 0x99b8
+  __DATA.__objc_ivar: 0x1b04
+  __DATA.__objc_data: 0x5de8
   __DATA.__data: 0x3158
   __DATA.__thread_vars: 0xc0
   __DATA.__thread_bss: 0x28

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9945
+  Functions: 9957
   Symbols:   1907
-  CStrings:  16559
+  CStrings:  16579
 
CStrings:
+ "<CKKSFixup:KeyMaterialAccessibility (%@)>"
+ "B48@0:8@16^{__CFString=}24^{__CFString=}32^@40"
+ "CDP is enabled, Skipping backing up sync items"
+ "CKKSFixupKeyMaterialAccessibilityOperation"
+ "Fixup %@ is needed, but device is locked; deferring until unlock"
+ "Minimum fixup across all zones is %lu (current is %lu)"
+ "No fixups needed, all zones up to date"
+ "Successfully performed a KeyMaterialAccessibility fixup"
+ "Unable to fetch CDP status: %@"
+ "Unable to fix up AfterFirstUnlock key material because device is locked; will retry after unlock"
+ "Unable to fix up AfterFirstUnlock key material: %@"
+ "Unable to fix up WhenUnlocked key material because device is locked; will retry after unlock"
+ "Unable to fix up WhenUnlocked key material: %@"
+ "Updated zone fixup state to CKKSFixupKeyMaterialAccessibility"
+ "com.apple.security.egoIdentities"
+ "fixup_key_material_accessibility"
+ "getCDPStatusSync:error:"
+ "q32@0:8@16^@24"
+ "sync = 0"
+ "updateKeyMaterialAccessibilityInZone:fromAccessible:toAccessible:error:"
```
