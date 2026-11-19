## assetutil

> `/usr/bin/assetutil`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1010.0.0.0.0
-  __TEXT.__text: 0xe5cb0
-  __TEXT.__auth_stubs: 0x2710
+1011.4.0.0.0
+  __TEXT.__text: 0xe5944
+  __TEXT.__auth_stubs: 0x2760
   __TEXT.__objc_stubs: 0xbb20
   __TEXT.__objc_methlist: 0x7290
   __TEXT.__const: 0x74e18
-  __TEXT.__gcc_except_tab: 0x1338
+  __TEXT.__gcc_except_tab: 0x1368
   __TEXT.__objc_methname: 0x11482
   __TEXT.__objc_classname: 0x1071
   __TEXT.__objc_methtype: 0x41f1
-  __TEXT.__cstring: 0x153fb
+  __TEXT.__cstring: 0x15745
   __TEXT.__oslogstring: 0x28
   __TEXT.__swift5_typeref: 0x8a
   __TEXT.__swift5_capture: 0x68

   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x20
-  __TEXT.__unwind_info: 0x3308
+  __TEXT.__unwind_info: 0x3320
   __TEXT.__eh_frame: 0x30c
-  __DATA_CONST.__const: 0x5368
-  __DATA_CONST.__cfstring: 0x8140
+  __DATA_CONST.__const: 0x5388
+  __DATA_CONST.__cfstring: 0x8180
   __DATA_CONST.__objc_classlist: 0x3b0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_arraydata: 0x2a0
   __DATA_CONST.__objc_arrayobj: 0x138
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x13a0
+  __DATA_CONST.__auth_got: 0x13c8
   __DATA_CONST.__got: 0x638
   __DATA_CONST.__auth_ptr: 0x100
   __DATA.__objc_const: 0xb6e8

   __DATA.__objc_data: 0x24e0
   __DATA.__data: 0x810
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x1cd8
+  __DATA.__bss: 0x1cf8
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/HIServices.framework/Versions/A/HIServices
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 3916
-  Symbols:   823
-  CStrings:  5830
+  Functions: 3919
+  Symbols:   828
+  CStrings:  5843
 
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
