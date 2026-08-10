## DeviceAccess

> `/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-2700.30.0.0.0
-  __TEXT.__text: 0x549e4
-  __TEXT.__objc_methlist: 0x46c4
+2700.34.0.0.0
+  __TEXT.__text: 0x54bfc
+  __TEXT.__objc_methlist: 0x46e4
   __TEXT.__const: 0x908
-  __TEXT.__cstring: 0xa143
+  __TEXT.__cstring: 0xa223
   __TEXT.__gcc_except_tab: 0x1330
   __TEXT.__constg_swiftt: 0x3b8
   __TEXT.__swift5_typeref: 0x25a

   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_capture: 0x1c
-  __TEXT.__unwind_info: 0x1408
+  __TEXT.__unwind_info: 0x1410
   __TEXT.__eh_frame: 0x4d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f98
+  __DATA_CONST.__objc_selrefs: 0x1fa8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x188
-  __DATA_CONST.__objc_arraydata: 0x40
+  __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__got: 0x538
   __AUTH_CONST.__const: 0x6d0
-  __AUTH_CONST.__cfstring: 0x35c0
-  __AUTH_CONST.__objc_const: 0x8060
+  __AUTH_CONST.__cfstring: 0x3680
+  __AUTH_CONST.__objc_const: 0x8070
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0xc20

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2300
-  Symbols:   3958
-  CStrings:  1511
+  Functions: 2302
+  Symbols:   3960
+  CStrings:  1519
 
Symbols:
+ -[DADevice resolvedDisplayImageFileURL]
+ -[DADeviceRegistry requiresCompanionApp]
CStrings:
+ "### resolvedDisplayImageFileURL: container lookup failed (%d)"
+ "%@-Image.%@"
+ "-[DADevice resolvedDisplayImageFileURL]"
+ "DADevices"
+ "bluetoothDualModeAppRequired"
+ "bluetoothLEModeAppRequired"
+ "com.apple.media-device-extension"
+ "dadeviceimagedata"
```
