## inboxupdaterd

> `/usr/libexec/inboxupdaterd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`

```diff

-274.40.17.0.0
-  __TEXT.__text: 0x8c670
+274.60.5.0.0
+  __TEXT.__text: 0x8ce50
   __TEXT.__auth_stubs: 0x1530
-  __TEXT.__objc_stubs: 0x8ae0
-  __TEXT.__objc_methlist: 0x41fc
-  __TEXT.__cstring: 0x5593
-  __TEXT.__objc_methname: 0x91a7
+  __TEXT.__objc_stubs: 0x8b00
+  __TEXT.__objc_methlist: 0x420c
+  __TEXT.__cstring: 0x5598
+  __TEXT.__objc_methname: 0x91c0
   __TEXT.__objc_classname: 0x687
   __TEXT.__objc_methtype: 0x1806
   __TEXT.__const: 0x115d3
   __TEXT.__gcc_except_tab: 0x17b0
-  __TEXT.__oslogstring: 0xa957
+  __TEXT.__oslogstring: 0xaaa2
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x3940
-  __DATA_CONST.__const: 0xf378
-  __DATA_CONST.__cfstring: 0x4d40
+  __TEXT.__unwind_info: 0x3978
+  __DATA_CONST.__const: 0xf438
+  __DATA_CONST.__cfstring: 0x4d60
   __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xd8

   __DATA_CONST.__auth_got: 0xaa8
   __DATA_CONST.__got: 0x598
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA.__objc_const: 0x9a80
-  __DATA.__objc_selrefs: 0x27b8
+  __DATA.__objc_const: 0x9a88
+  __DATA.__objc_selrefs: 0x27c0
   __DATA.__objc_ivar: 0x45c
   __DATA.__objc_data: 0xf00
-  __DATA.__data: 0x25f0
+  __DATA.__data: 0x25f8
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4292
+  Functions: 4308
   Symbols:   511
-  CStrings:  3794
+  CStrings:  3802
 
CStrings:
+ "Device powered on by button press; skipping WiFi association and personalization"
+ "Failed to open SMC service"
+ "Failed to read SMC key %{public}@ with error: %{public}@"
+ "SMC key %{public}@ not supported on this hardware"
+ "SMC key %{public}@ reports powered by hold/power button: %{bool}d"
+ "Unexpected data length %zu for SMC key %{public}@"
+ "bPHD"
+ "isPoweredOnByButtonPress"
```
