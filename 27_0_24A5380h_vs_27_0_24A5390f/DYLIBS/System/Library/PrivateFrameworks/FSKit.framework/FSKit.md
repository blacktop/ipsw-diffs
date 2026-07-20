## FSKit

> `/System/Library/PrivateFrameworks/FSKit.framework/FSKit`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__constg_swiftt`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-974.0.7.0.0
-  __TEXT.__text: 0x53688
-  __TEXT.__objc_methlist: 0x6278
+974.0.11.0.0
+  __TEXT.__text: 0x536b4
+  __TEXT.__objc_methlist: 0x6288
   __TEXT.__const: 0x498
   __TEXT.__gcc_except_tab: 0xe5c
-  __TEXT.__oslogstring: 0x3f66
+  __TEXT.__oslogstring: 0x3f76
   __TEXT.__cstring: 0x676f
   __TEXT.__swift5_typeref: 0x264
   __TEXT.__swift5_capture: 0xec

   __TEXT.__constg_swiftt: 0x210
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1820
+  __TEXT.__unwind_info: 0x1828
   __TEXT.__eh_frame: 0x478
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x18c8
+  __DATA_CONST.__const: 0x18f0
   __DATA_CONST.__objc_classlist: 0x398
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c00
+  __DATA_CONST.__objc_selrefs: 0x2c08
   __DATA_CONST.__objc_protorefs: 0x148
   __DATA_CONST.__objc_superrefs: 0x2e8
   __DATA_CONST.__objc_arraydata: 0x488

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2694
-  Symbols:   5119
+  Functions: 2695
+  Symbols:   5122
   CStrings:  1099
 
Symbols:
+ -[FSFreeSpace(Project) isNoUpdate]
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96s104bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s104l8s80l8s88l8s96l8
+ ___block_descriptor_120_e8_32s40s48s56s64s72s80s88s96s104s112bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s112l8s88l8s96l8s104l8
+ ___block_descriptor_48_e8_32bs40bs_e17_v16?0"NSError"8ls32l8s40l8
+ _objc_msgSend$isNoUpdate
- ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96s104bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s104l8s88l8s96l8
- ___block_descriptor_120_e8_32s40s48s56s64s72s80s88s96s104s112bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s112l8s96l8s104l8
CStrings:
+ "%s: freeSpaceData called on the \"no update\" sentinel"
- "%s: free space was not populated!"
```
