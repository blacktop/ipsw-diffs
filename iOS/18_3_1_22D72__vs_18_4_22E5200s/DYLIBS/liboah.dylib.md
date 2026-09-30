## liboah.dylib

> `/usr/lib/liboah.dylib`

```diff

-342.0.0.0.0
-  __TEXT.__text: 0x1344
-  __TEXT.__auth_stubs: 0x1a0
-  __TEXT.__cstring: 0x1a4
+348.0.0.0.0
+  __TEXT.__text: 0x1b60
+  __TEXT.__auth_stubs: 0x1b0
   __TEXT.__const: 0x4
-  __TEXT.__unwind_info: 0x58
+  __TEXT.__cstring: 0x62e
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0x20
-  __AUTH_CONST.__auth_got: 0xd0
+  __AUTH_CONST.__auth_got: 0xd8
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x20
-  __DATA.__bss: 0x1008
+  __DATA.__crash_info: 0x40
+  __DATA.__bss: 0x1000
   __DATA.__common: 0x8
-  __DATA_DIRTY.__bss: 0x8
+  __DATA_DIRTY.__bss: 0x10
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 37
-  Symbols:   73
-  CStrings:  21
+  Functions: 43
+  Symbols:   78
+  CStrings:  55
 
Symbols:
+ _memmove
+ _oah_invalidate_translation
+ _objc_thread_get_rip
+ _rosetta_invalidate_translation
+ _rosetta_thread_get_rip
CStrings:
+ "LC_AOT_METADATA command is wrong size"
+ "LC_BUILD_VERSION command is wrong size"
+ "LC_CODE_SIGNATURE command is wrong size"
+ "LC_MAIN command is wrong size"
+ "LC_SOURCE_VERSION command is wrong size"
+ "LC_UUID command is wrong size"
+ "LC_VERSION_MIN_MACOSX command is wrong size"
+ "Mach-O has too many segments"
+ "Mach-O header sizeofcmds is incorrect"
+ "executable is inconsistent about dynamic linking"
+ "integer overflow in aot metadata load command fragment list"
+ "integer overflow in aot metadata load x86 image path"
+ "integer overflow in section boundaries"
+ "invalid LC_MAIN entry point"
+ "invalid LC_SEGMENT_64 command size"
+ "invalid LC_UNIXTHREAD architecture"
+ "invalid Mach-O magic"
+ "invalid cpu type/subtype"
+ "invalid entry point"
+ "invalid segment permissions"
+ "load commands are mapped by multiple segments"
+ "load commands too large"
+ "malformed LC_UNIXTHREAD command"
+ "malformed load command"
+ "multiple LC_LOAD_SIGNATURE commands"
+ "multiple LC_UUID commands"
+ "multiple __LINKEDIT segments"
+ "multiple load commands specify entry points"
+ "no segment mapping load commands"
+ "out-of-bounds Mach-O header"
+ "out-of-bounds load command"
+ "overlapping Mach-O segments"
+ "segment partially maps load commands"
+ "unsupported Mach-O filetype"

```
