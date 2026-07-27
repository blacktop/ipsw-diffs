## SidecarCore

> `/System/Library/PrivateFrameworks/SidecarCore.framework/Versions/A/SidecarCore`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-380.1.0.0.0
-  __TEXT.__text: 0x1b968
+384.1.0.0.0
+  __TEXT.__text: 0x1bbcc
   __TEXT.__auth_stubs: 0x710
   __TEXT.__objc_methlist: 0x1ae0
-  __TEXT.__const: 0xf8
-  __TEXT.__gcc_except_tab: 0x4c4
+  __TEXT.__const: 0x108
+  __TEXT.__gcc_except_tab: 0x534
   __TEXT.__cstring: 0x1504
-  __TEXT.__oslogstring: 0x95c
+  __TEXT.__oslogstring: 0xa30
   __TEXT.__unwind_info: 0x978
   __TEXT.__objc_classname: 0x4a7
   __TEXT.__objc_methname: 0x32a6

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 724
-  Symbols:   1790
-  CStrings:  1117
+  Symbols:   1789
+  CStrings:  1120
 
Symbols:
- ___updateDevices_block_invoke_3
Functions:
~ _updateDevices : 940 -> 1552
~ ___SidecarDisplayManagerGeneration_block_invoke -> __filterDevices_block_invoke.1409 : 20 -> 100
~ ___SidecarDisplayManagerGeneration_block_invoke_2 -> __filterSupportedDevices_block_invoke.1410 : 88 -> 8
~ __filterDevices_block_invoke.1406 -> ___SidecarDisplayManagerGeneration_block_invoke : 100 -> 20
~ __filterSupportedDevices_block_invoke.1407 -> ___SidecarDisplayManagerGeneration_block_invoke_2 : 8 -> 88
CStrings:
+ "updateDevices(%{public}@): returning %lu device(s) to caller: %{public}@"
+ "updateDevices: %lu device(s) passed filter: %{public}@"
+ "updateDevices: deviceGeneration=%llu (prev=%llu) displayGeneration=%llu (prev=%llu)"
```
