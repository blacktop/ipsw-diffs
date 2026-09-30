## com.apple.fskit.msdos

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.msdos.appex/Contents/MacOS/com.apple.fskit.msdos`

```diff

-  __TEXT.__text: 0x16518
+  __TEXT.__text: 0x1662c
   __TEXT.__auth_stubs: 0x660
   __TEXT.__objc_stubs: 0x1f80
   __TEXT.__objc_methlist: 0xd04
   __TEXT.__const: 0x4e26
   __TEXT.__cstring: 0x286d
-  __TEXT.__oslogstring: 0xe6a
+  __TEXT.__oslogstring: 0xf6d
   __TEXT.__objc_classname: 0x154
   __TEXT.__objc_methname: 0x229e
   __TEXT.__objc_methtype: 0xad9
-  __TEXT.__gcc_except_tab: 0x470
+  __TEXT.__gcc_except_tab: 0x464
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x28
   __TEXT.__swift5_typeref: 0x80

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__auth_got: 0x340
-  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__got: 0xe0
   __DATA_CONST.__auth_ptr: 0x68
   __DATA.__objc_const: 0x16d0
   __DATA.__objc_selrefs: 0xac0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 474
+  Functions: 480
   Symbols:   299
-  CStrings:  1055
+  CStrings:  1060
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__swift5_entry : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
CStrings:
+ "%s: FAT offset overflows (resSectors=%u, bytesPerSector=%u)"
+ "%s: FAT size overflows (fatSectors=%u, bytesPerSector=%u)"
+ "%s: First cluster offset overflows"
+ "%s: Root directory block overflows (FATs=%u, fatSectors=%u, reservedSectors=%u)"
+ "%s: Zero bytes-per-sector"

```
