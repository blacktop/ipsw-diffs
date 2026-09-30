## remotepairingd

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/RemotePairing.framework/Versions/A/XPCServices/remotepairingd.xpc/Contents/MacOS/remotepairingd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_classrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__s_async_hook`

```diff

-280.0.5.0.0
-  __TEXT.__text: 0x8c2ac
-  __TEXT.__auth_stubs: 0x3470
-  __TEXT.__objc_stubs: 0x680
+280.0.8.0.0
+  __TEXT.__text: 0x8ca70
+  __TEXT.__auth_stubs: 0x34b0
+  __TEXT.__objc_stubs: 0x6a0
   __TEXT.__objc_methlist: 0x1b4
-  __TEXT.__const: 0x1ef0
-  __TEXT.__oslogstring: 0x5dc5
-  __TEXT.__cstring: 0x4848
+  __TEXT.__const: 0x1ee0
+  __TEXT.__oslogstring: 0x5e65
+  __TEXT.__cstring: 0x4818
   __TEXT.__swift5_typeref: 0x17aa
   __TEXT.__objc_methtype: 0x1c2
   __TEXT.__swift5_entry: 0x8

   __TEXT.__swift5_proto: 0xd0
   __TEXT.__swift5_types: 0xbc
   __TEXT.__objc_classname: 0x568
-  __TEXT.__objc_methname: 0x1044
+  __TEXT.__objc_methname: 0x1054
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_mpenum: 0x2c
-  __TEXT.__unwind_info: 0x1508
-  __TEXT.__eh_frame: 0x10f0
+  __TEXT.__unwind_info: 0x1510
+  __TEXT.__eh_frame: 0x1128
   __DATA_CONST.__const: 0x35f8
   __DATA_CONST.__cfstring: 0x580
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x1a40
+  __DATA_CONST.__auth_got: 0x1a60
   __DATA_CONST.__got: 0x7a8
   __DATA_CONST.__auth_ptr: 0x698
   __DATA.__objc_const: 0x1b60
-  __DATA.__objc_selrefs: 0x260
+  __DATA.__objc_selrefs: 0x268
   __DATA.__objc_protorefs: 0x28
   __DATA.__objc_classrefs: 0x88
   __DATA.__objc_data: 0x3f0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3051
-  Symbols:   372
-  CStrings:  887
+  Functions: 3043
+  Symbols:   371
+  CStrings:  888
 
Symbols:
- _geteuid
CStrings:
+ "Moving wrong-owner directory %s to %s"
+ "Per-user data vaulted location %s has unexpected owning uid (expected %u, actual %u). This usually means the pairing store was migrated from another Mac or user account. Moving it aside and recreating."
+ "moveItemAtURL:toURL:error:"
- "Invalid owner for per-user sub directory"
- "Per-user data vaulted location has unexpected owning uid. Expected %u, actual: %u. Aborting"
```
