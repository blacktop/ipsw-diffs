## CPMS

> `/System/Library/PrivateFrameworks/CPMS.framework/Versions/A/CPMS`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1191.0.16.0.0
-  __TEXT.__text: 0x9db4
+1191.0.27.0.0
+  __TEXT.__text: 0x9f74
   __TEXT.__objc_methlist: 0x4c4
   __TEXT.__const: 0xa0
   __TEXT.__gcc_except_tab: 0x170
-  __TEXT.__cstring: 0xcd5
+  __TEXT.__cstring: 0xcf8
   __TEXT.__oslogstring: 0x1137
   __TEXT.__ustring: 0x220
   __TEXT.__unwind_info: 0x1e0

   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__got: 0x98
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x1300
+  __AUTH_CONST.__cfstring: 0x1340
   __AUTH_CONST.__objc_const: 0x660
   __AUTH_CONST.__auth_got: 0x1c8
   __DATA.__objc_ivar: 0x40

   - /usr/lib/libobjc.A.dylib
   Functions: 184
   Symbols:   335
-  CStrings:  291
+  CStrings:  293
 
Functions:
~ +[CPMSStateReader flattenSnapshot:index:into:] : 3020 -> 3244
~ +[CPMSStateReader getCPMSControlStateSnapshotDictionary:] : 2248 -> 2472
CStrings:
+ "%@%@_Battery%d_%d"
+ "SystemCapability"
```
