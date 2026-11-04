## devicecheckd

> `/System/Library/PrivateFrameworks/DeviceCheckInternal.framework/devicecheckd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-158.0.0.0.0
-  __TEXT.__text: 0x65f8
-  __TEXT.__auth_stubs: 0x550
+162.1.0.0.0
+  __TEXT.__text: 0x66dc
+  __TEXT.__auth_stubs: 0x540
   __TEXT.__objc_stubs: 0xa20
   __TEXT.__objc_methlist: 0x57c
   __TEXT.__objc_classname: 0xd3
-  __TEXT.__objc_methname: 0xe9c
-  __TEXT.__objc_methtype: 0x56d
-  __TEXT.__cstring: 0x78e
+  __TEXT.__objc_methname: 0xe94
+  __TEXT.__objc_methtype: 0x562
+  __TEXT.__cstring: 0x79a
   __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x224
-  __TEXT.__oslogstring: 0xab7
-  __TEXT.__unwind_info: 0x268
+  __TEXT.__gcc_except_tab: 0x270
+  __TEXT.__oslogstring: 0xadd
+  __TEXT.__unwind_info: 0x278
   __DATA_CONST.__const: 0x2b0
   __DATA_CONST.__cfstring: 0x340
   __DATA_CONST.__objc_classlist: 0x40

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__auth_got: 0x2b8
+  __DATA_CONST.__auth_got: 0x2b0
   __DATA_CONST.__got: 0x140
   __DATA.__objc_const: 0xa00
   __DATA.__objc_selrefs: 0x3f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 116
-  Symbols:   134
+  Functions: 118
+  Symbols:   133
   CStrings:  313
 
Symbols:
- _proc_pidinfo
CStrings:
+ "%25s:%-5d DeviceCheck Key Rotation feature flag enabled { enabled=%d }."
+ "%25s:%-5d No usable appID entitlement for client connection, using codesign identifier. { appID=%@, entitlementsValidated=%d }"
+ "isKeyRotationEnabled"
+ "keyRotation"
- "%25s:%-5d Failed to fetch appID for client connection from entitlement, using codesign identifier. { appID=%@ }"
- "%25s:%-5d proc_pidinfo failed. { ErrorCode: %d }"
- "B20@0:8i16"
- "entitlementsValidatedForPID:"
```
