## cpio

> `/usr/bin/cpio`

```diff

-138.40.4.0.0
-  __TEXT.__text: 0x2d88
-  __TEXT.__auth_stubs: 0x900
+147.0.0.0.0
+  __TEXT.__text: 0x4d40
+  __TEXT.__auth_stubs: 0x8e0
   __TEXT.__const: 0x38
-  __TEXT.__cstring: 0x910
-  __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x480
+  __TEXT.__cstring: 0x922
+  __TEXT.__unwind_info: 0x90
+  __DATA_CONST.__auth_got: 0x470
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x230
+  __DATA.__data: 0x10
   __DATA.__bss: 0x44b8
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
-  UUID: EA3219C4-F872-3257-895C-CE10AAB0B335
-  Functions: 29
-  Symbols:   150
-  CStrings:  119
+  UUID: CBF438CF-D1BB-34EB-80E3-B1ED1D0B9FE9
+  Functions: 37
+  Symbols:   378
+  CStrings:  122
 
Symbols:
+ 
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/libarchive_executables/install/Symbols/BuiltProducts/libarchive_fe.a(err.o)
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/libarchive_executables/install/Symbols/BuiltProducts/libarchive_fe.a(line_reader.o)
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/libarchive_executables/install/Symbols/BuiltProducts/libarchive_fe.a(passphrase.o)
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/libarchive_executables/install/TempContent/Objects/libarchive.build/cpio.build/DerivedSources/
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/libarchive_executables/install/TempContent/Objects/libarchive.build/cpio.build/Objects-normal/arm64e/cmdline.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/libarchive_executables/install/TempContent/Objects/libarchive.build/cpio.build/Objects-normal/arm64e/cpio.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/libarchive_executables/install/TempContent/Objects/libarchive.build/cpio.build/Objects-normal/arm64e/cpio_vers.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libarchive_executables/libarchive/cpio/
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libarchive_executables/libarchive/libarchive_fe/
+ ___memcpy_chk
+ ___memmove_chk
+ ___memset_chk
+ ___snprintf_chk
+ ___strcat_chk
+ _cpioVersionNumber
+ _cpioVersionString
+ _cpio_getopt
+ _cpio_i64toa
+ _cpio_longopts
+ _cpio_rename
+ _entry_to_archive
+ _extract_data
+ _file_to_archive
+ _free_cache
+ _lafe_errc
+ _lafe_getprogname
+ _lafe_line_reader
+ _lafe_line_reader_find_eol
+ _lafe_line_reader_free
+ _lafe_line_reader_next
+ _lafe_progname
+ _lafe_readpassphrase
+ _lafe_setprogname
+ _lafe_vwarnc
+ _lafe_warnc
+ _list_item_verbose
+ _long_help
+ _long_help_msg
+ _lookup_gname
+ _lookup_gname_helper
+ _lookup_name
+ _lookup_uname
+ _lookup_uname_helper
+ _main
+ _memset
+ _mode_in
+ _mode_list
+ _mode_out
+ _mode_pass
+ _owner_parse
+ _passphrase_callback
+ _passphrase_free
+ _remove_leading_slash
+ _restore_time
+ _short_options
+ _usage
+ _version
+ cmdline.c
+ cpio.c
+ cpio_getopt.opt_word
+ cpio_getopt.state
+ cpio_i64toa.buff
+ cpio_rename.buff
+ cpio_vers.c
+ err.c
+ line_reader.c
+ list_item_verbose.now
+ main.buff
+ owner_parse.errbuff
+ passphrase.c
- _fputc
- _fwrite
- _memchr
- _memcpy
- _memmove
- _snprintf
- _strcat
- _strcpy
- radr://5614542
CStrings:
+ "\n"
+ "."
+ "invalid mtime"

```
