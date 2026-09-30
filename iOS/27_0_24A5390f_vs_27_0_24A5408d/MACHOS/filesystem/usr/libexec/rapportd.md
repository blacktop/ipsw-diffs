## rapportd

> `/usr/libexec/rapportd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_acfuncs`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-747.100.2.0.0
-  __TEXT.__text: 0x197b1c
+751.100.2.0.0
+  __TEXT.__text: 0x198240
   __TEXT.__auth_stubs: 0x39f0
-  __TEXT.__objc_stubs: 0x135e0
-  __TEXT.__objc_methlist: 0xa0c8
-  __TEXT.__const: 0x5fa0
-  __TEXT.__cstring: 0x36bb6
+  __TEXT.__objc_stubs: 0x13620
+  __TEXT.__objc_methlist: 0xa0d0
+  __TEXT.__const: 0x6160
+  __TEXT.__cstring: 0x36db6
   __TEXT.__objc_classname: 0x10bf
   __TEXT.__objc_methtype: 0x4a81
   __TEXT.__gcc_except_tab: 0x24b0
-  __TEXT.__objc_methname: 0x1c800
+  __TEXT.__objc_methname: 0x1c840
   __TEXT.__oslogstring: 0x3542
   __TEXT.__swift5_typeref: 0x1776
   __TEXT.__swift5_capture: 0xb78

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_acfuncs: 0x104
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5968
+  __TEXT.__unwind_info: 0x5970
   __TEXT.__eh_frame: 0x4c44
-  __DATA_CONST.__const: 0x8448
+  __DATA_CONST.__const: 0x8498
   __DATA_CONST.__cfstring: 0x6600
   __DATA_CONST.__objc_classlist: 0x3a0
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x228
-  __DATA_CONST.__objc_intobj: 0x3c0
+  __DATA_CONST.__objc_intobj: 0x3d8
   __DATA_CONST.__objc_arraydata: 0x58
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x50

   __DATA_CONST.__got: 0xac8
   __DATA_CONST.__auth_ptr: 0x670
   __DATA.__objc_const: 0x11d88
-  __DATA.__objc_selrefs: 0x5e70
+  __DATA.__objc_selrefs: 0x5e80
   __DATA.__objc_ivar: 0x113c
   __DATA.__objc_data: 0x2d88
   __DATA.__data: 0x3af8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8590
+  Functions: 8599
   Symbols:   1455
-  CStrings:  10843
+  CStrings:  10854
 
CStrings:
+ "-[RPServiceDiscoveryClient _cLinkDeviceChanged:]"
+ "-[RPServiceDiscoveryClient _cLinkDeviceChanged:]_block_invoke_2"
+ "-[RPServiceDiscoveryClient _cLinkStart]_block_invoke_7"
+ "Cached peer changed trust %#ll{flags} -> %#ll{flags} for %@\n"
+ "Error reporting change 0x%#lx for %@: %@"
+ "Error retrieving identities for %@: %@"
+ "Established authentication with peer %@"
+ "Ignoring change to unauthenticated peer %@"
+ "Lost authentication with peer %@"
+ "Preserving session paired identity for guest mic-only teardown (rapportId %@ deviceConfirmed %@)\n"
+ "Removing session paired identity for fully-lost device (spID %@ ids %@)\n"
+ "_cLinkDeviceChanged:"
+ "deviceChanged:changes:completionHandler:"
- "-[RPServiceDiscoveryClient _cLinkStart]_block_invoke_6"
- "MockA2DPActivity"
```
