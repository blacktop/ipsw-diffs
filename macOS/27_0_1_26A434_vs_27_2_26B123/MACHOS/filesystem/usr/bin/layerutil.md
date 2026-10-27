## layerutil

> `/usr/bin/layerutil`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1010.0.0.0.0
-  __TEXT.__text: 0xa4048
-  __TEXT.__auth_stubs: 0x2440
+1011.4.0.0.0
+  __TEXT.__text: 0xa4474
+  __TEXT.__auth_stubs: 0x2490
   __TEXT.__objc_stubs: 0xbee0
   __TEXT.__objc_methlist: 0x7dc0
   __TEXT.__const: 0x2c68
-  __TEXT.__gcc_except_tab: 0x1a80
+  __TEXT.__gcc_except_tab: 0x1ab0
   __TEXT.__objc_methname: 0x12293
   __TEXT.__objc_classname: 0x119f
   __TEXT.__objc_methtype: 0x4411
-  __TEXT.__cstring: 0x1035e
+  __TEXT.__cstring: 0x106a8
   __TEXT.__oslogstring: 0x28
   __TEXT.__swift5_typeref: 0x8a
   __TEXT.__swift5_capture: 0x68

   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x20
-  __TEXT.__unwind_info: 0x3940
-  __DATA_CONST.__const: 0x49d0
-  __DATA_CONST.__cfstring: 0x4b00
+  __TEXT.__unwind_info: 0x3948
+  __DATA_CONST.__const: 0x49f0
+  __DATA_CONST.__cfstring: 0x4b40
   __DATA_CONST.__objc_classlist: 0x420
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_arraydata: 0x270
   __DATA_CONST.__objc_arrayobj: 0x168
-  __DATA_CONST.__auth_got: 0x1238
+  __DATA_CONST.__auth_got: 0x1260
   __DATA_CONST.__got: 0x670
   __DATA_CONST.__auth_ptr: 0xb8
   __DATA.__objc_const: 0xc6b8

   __DATA.__objc_data: 0x2940
   __DATA.__data: 0x528
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x848
+  __DATA.__bss: 0x868
   __DATA.__common: 0x10
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/HIServices.framework/Versions/A/HIServices

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 4351
-  Symbols:   782
-  CStrings:  5322
+  Functions: 4353
+  Symbols:   787
+  CStrings:  5335
 
Symbols:
+ ___cxa_guard_abort
+ ___cxa_guard_acquire
+ ___cxa_guard_release
+ _newlocale
+ _snprintf_l
CStrings:
+ "%@:%@"
+ "CoreUI: CSI bitmap data starts past the end of the rendition data"
+ "CoreUI: CSI image index %u (offset %u) is outside the rendition data: '%@'"
+ "CoreUI: Deepmap 2.0 block length %zu is smaller than its header"
+ "CoreUI: Deepmap 2.0 compressedBytes %llu exceeds block length %zu"
+ "CoreUI: Deepmap block length %zu is smaller than its header"
+ "CoreUI: Deepmap compressedBytes %llu exceeds block length %zu"
+ "CoreUI: Invalid chunk rows of %lu in image of height %lu (rows already decoded: %lu)"
+ "CoreUI: raw image slice needs %zu bytes at offset %zu but only %zu bytes of bitmap data are available (rowbytes %zu)"
+ "com.apple.coreui-preferred-localization-cache"
+ "decompressData: %zu byte block too small to hold the row index for rows %d..%d\n"
+ "decompressData: invalid region %d,%d %dx%d\n"
+ "decompressData: row %d offset %u lies outside the %zu byte block\n"
+ "decompressData: truncated scanline %d in the %zu byte block\n"
- "_ReadFreeList: tring to read count of freelist table."
```
