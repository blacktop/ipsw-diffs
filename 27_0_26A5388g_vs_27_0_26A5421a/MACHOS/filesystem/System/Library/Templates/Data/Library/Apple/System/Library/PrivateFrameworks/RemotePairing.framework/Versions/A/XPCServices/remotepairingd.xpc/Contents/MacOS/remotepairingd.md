## remotepairingd

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/RemotePairing.framework/Versions/A/XPCServices/remotepairingd.xpc/Contents/MacOS/remotepairingd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_protorefs`
- `__DATA.__objc_classrefs`
- `__DATA.__objc_data`
- `__DATA.__s_async_hook`

```diff

-280.0.8.0.0
-  __TEXT.__text: 0x8ca70
-  __TEXT.__auth_stubs: 0x34b0
+280.0.12.0.0
+  __TEXT.__text: 0x8d3b8
+  __TEXT.__auth_stubs: 0x34d0
   __TEXT.__objc_stubs: 0x6a0
   __TEXT.__objc_methlist: 0x1b4
-  __TEXT.__const: 0x1ee0
-  __TEXT.__oslogstring: 0x5e65
-  __TEXT.__cstring: 0x4818
-  __TEXT.__swift5_typeref: 0x17aa
+  __TEXT.__const: 0x1ef0
+  __TEXT.__oslogstring: 0x6065
+  __TEXT.__cstring: 0x4820
+  __TEXT.__swift5_typeref: 0x17b4
   __TEXT.__objc_methtype: 0x1c2
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x1850
+  __TEXT.__constg_swiftt: 0x1860
   __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_reflstr: 0x1030
   __TEXT.__swift5_fieldmd: 0xcbc
   __TEXT.__swift5_assocty: 0xc0
-  __TEXT.__swift5_capture: 0x1438
+  __TEXT.__swift5_capture: 0x1474
   __TEXT.__swift5_proto: 0xd0
   __TEXT.__swift5_types: 0xbc
   __TEXT.__objc_classname: 0x568
   __TEXT.__objc_methname: 0x1054
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_mpenum: 0x2c
-  __TEXT.__unwind_info: 0x1510
+  __TEXT.__unwind_info: 0x1500
   __TEXT.__eh_frame: 0x1128
-  __DATA_CONST.__const: 0x35f8
+  __DATA_CONST.__const: 0x3648
   __DATA_CONST.__cfstring: 0x580
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x1a60
+  __DATA_CONST.__auth_got: 0x1a70
   __DATA_CONST.__got: 0x7a8
   __DATA_CONST.__auth_ptr: 0x698
   __DATA.__objc_const: 0x1b60

   __DATA.__objc_protorefs: 0x28
   __DATA.__objc_classrefs: 0x88
   __DATA.__objc_data: 0x3f0
-  __DATA.__data: 0x3039
+  __DATA.__data: 0x3051
   __DATA.__s_async_hook: 0x1a0
   __DATA.__swift56_hooks: 0xb0
   __DATA.__common: 0x168

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3043
+  Functions: 3073
   Symbols:   371
-  CStrings:  888
+  CStrings:  892
 
CStrings:
+ "%{public}s Device offers free pairing over a physical connection. Automatically pairing before surfacing device to clients."
+ "%{public}s: Automatic free pairing completed but connection has since been invalidated with reason: %{public}s. Discarding channel and will not surface a device for it."
+ "%{public}s: Automatic free pairing failed (error: %s). Surfacing device as unauthenticated so it can be paired manually."
+ "%{public}s: Automatic free pairing succeeded. Surfacing device as paired."
+ "usbmuxd-571.0.0.0.1"
- "usbmuxd-570"
```
