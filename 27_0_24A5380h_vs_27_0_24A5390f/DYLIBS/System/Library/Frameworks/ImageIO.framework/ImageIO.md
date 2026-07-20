## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__data`

```diff

-2846.0.0.0.0
-  __TEXT.__text: 0x4fd300
+2847.1.0.0.0
+  __TEXT.__text: 0x4fdcb8
   __TEXT.__objc_methlist: 0xd58
-  __TEXT.__const: 0x494a0
-  __TEXT.__gcc_except_tab: 0x22844
-  __TEXT.__cstring: 0xa5f9e
+  __TEXT.__const: 0x49530
+  __TEXT.__gcc_except_tab: 0x2284c
+  __TEXT.__cstring: 0xa5f3e
   __TEXT.__oslogstring: 0x17
   __TEXT.__constg_swiftt: 0x260c
-  __TEXT.__swift5_typeref: 0x3cb0
+  __TEXT.__swift5_typeref: 0x3c68
   __TEXT.__swift5_builtin: 0x154
-  __TEXT.__swift5_fieldmd: 0x7958
-  __TEXT.__swift5_reflstr: 0x4f45
+  __TEXT.__swift5_fieldmd: 0x79f4
+  __TEXT.__swift5_reflstr: 0x4fb5
   __TEXT.__swift5_assocty: 0x1c00
   __TEXT.__swift5_proto: 0x1604
   __TEXT.__swift5_types: 0x478

   __TEXT.__swift_as_cont: 0x10
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0x13660
+  __TEXT.__unwind_info: 0x13668
   __TEXT.__eh_frame: 0x908c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xb50
+  __DATA_CONST.__objc_selrefs: 0xb48
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x470
-  __DATA_CONST.__got: 0xab0
-  __AUTH_CONST.__const: 0x4eea0
+  __DATA_CONST.__got: 0xaa8
+  __AUTH_CONST.__const: 0x4ee80
   __AUTH_CONST.__cfstring: 0x35f60
   __AUTH_CONST.__objc_const: 0x11d0
   __AUTH_CONST.__weak_auth_got: 0x30

   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x1
   __DATA.__objc_ivar: 0xa4
-  __DATA.__data: 0x64e0
+  __DATA.__data: 0x64b0
   __DATA.__bss: 0x2fc30
   __DATA.__common: 0x2270
   __DATA_DIRTY.__data: 0x3b0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
-  Functions: 22998
-  Symbols:   24650
+  Functions: 23003
+  Symbols:   24645
   CStrings:  18195
 
Symbols:
+ _CFUUIDCreateFromUUIDBytes
- _OBJC_CLASS_$_NSUUID
- _objc_msgSend$initWithUUIDBytes:
- _symbolic Ss_SuSgAAt
- _symbolic _____ySs_SuSgABtG 17_StringProcessing5RegexV
- _symbolic _____ySs_SuSgABt_G 17_StringProcessing5RegexV5MatchV
- _symbolic _____ySs_SuSgABt_GSg 17_StringProcessing5RegexV5MatchV
CStrings:
+ "'%s' is saving an opaque image (%dx%d) with '%s' --> ignoring alpha to avoid an unnecessary alpha plane.\n"
+ "✳️  %s '%c%c%c%c' [%ldx%ld]: imgHeadroom: %g   csHeadroom: %g   isImageSpecific: %d   isHDR: %d   isEDR: %d   decodeToSDR: %d   decodeToHDR: %d   cs: %s\n"
- "✳️  %s '%c%c%c%c' [%ldx%ld]: imgHeadroom: %g   csHeadroom: %g   hasFlexGTC: %d   isHDR: %d   isEDR: %d   decodeToSDR: %d   decodeToHDR: %d   cs: %s\n"
- "⭕️ ERROR: '%s' is trying to save an opaque image (%dx%d) with '%s'. This would unnecessarily increase the file size and will double (!!!) the required memory when decoding the image --> ignoring alpha.\n "
```
