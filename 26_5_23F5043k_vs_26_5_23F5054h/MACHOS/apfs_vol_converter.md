## apfs_vol_converter

> `filesystem/System/Library/Filesystems/apfs.fs/apfs_vol_converter`

```diff

-2811.120.5.0.0
-  __TEXT.__text: 0x58fe0
+2811.120.10.0.1
+  __TEXT.__text: 0x59010
   __TEXT.__auth_stubs: 0x9f0
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0xc00
-  __TEXT.__cstring: 0x1200b
+  __TEXT.__cstring: 0x11f43
   __TEXT.__gcc_except_tab: 0x63c
   __TEXT.__unwind_info: 0xbe8
   __DATA_CONST.__auth_got: 0x500
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0xb20
-  __DATA_CONST.__cfstring: 0xba0
+  __DATA_CONST.__cfstring: 0xb40
   __DATA.__data: 0x370
   __DATA.__bss: 0x78
-  __DATA.__common: 0xfac
+  __DATA.__common: 0xf9c
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  UUID: B45BA335-961C-3B90-A958-B2046246A7B0
+  UUID: A261A902-07FC-381D-A203-A4D303826939
   Functions: 868
   Symbols:   185
-  CStrings:  1707
+  CStrings:  1700
 
Functions:
~ sub_10000b644 : 164 -> 176
~ sub_10000bcd4 -> sub_10000bce0 : 3796 -> 3616
~ sub_10000cbb4 -> sub_10000cb0c : 2960 -> 2956
~ sub_10000f13c -> sub_10000f090 : 148 -> 168
~ sub_10000f21c -> sub_10000f184 : 312 -> 320
~ sub_1000106d4 -> sub_100010644 : 1320 -> 1408
~ sub_1000146b0 -> sub_100014678 : 440 -> 364
~ sub_100016254 -> sub_1000161d0 : 248 -> 428
CStrings:
+ "%u\n"
+ "2811.120.10.0.1"
+ "unused1"
+ "unused2"
- "%@psvr_t=%llu "
- "%@src_t=%llu "
- "%@trgt_t=%llu "
- "2811.120.5"
- "Preprocessor_RecordSharedJobjs"
- "Preprocessor_RecordSharedJobjs_walk_file_extents"
- "WARNING: Verification was turned off to save time"
- "WARNING: Verification was turned off to save time\n"

```
