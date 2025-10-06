## libcharset.1.dylib

> `/usr/lib/libcharset.1.dylib`

```diff

-92.80.2.0.0
-  __TEXT.__text: 0x10
-  __TEXT.__cstring: 0x6
-  __TEXT.__unwind_info: 0x48
+99.0.0.0.0
+  __TEXT.__text: 0x410
+  __TEXT.__auth_stubs: 0x160
+  __TEXT.__cstring: 0xe5
+  __TEXT.__unwind_info: 0x58
+  __DATA_CONST.__got: 0x10
+  __AUTH_CONST.__auth_got: 0xb0
+  __DATA.__data: 0x82
+  __DATA.__bss: 0x10
   - /usr/lib/libSystem.B.dylib
-  UUID: 0B7A6688-2762-3418-A824-5AC552FADD4B
-  Functions: 2
-  Symbols:   2
-  CStrings:  1
+  UUID: 18486DD6-01AA-358B-B9C0-E27530711B8B
+  Functions: 5
+  Symbols:   36
+  CStrings:  16
 
Symbols:
+ <redacted>
+ __DefaultRuneLocale
+ ___assert_rtn
+ ___maskrune
+ ___stack_chk_fail
+ ___stack_chk_guard
+ _charset_elems
+ _charset_map
+ _charset_mappings_static
+ _close
+ _default_from
+ _fclose
+ _fdopen
+ _feof
+ _ferror
+ _fgetln
+ _free
+ _fscanf
+ _getc
+ _getenv
+ _locale_charset.cold.1
+ _locale_charset.cold.2
+ _locale_charset.cold.3
+ _malloc_type_calloc
+ _memcpy
+ _nl_langinfo
+ _open
+ _openat
+ _os_variant_has_internal_content
+ _strcmp
+ _strdup
+ _ungetc
CStrings:
+ "%64s %64s"
+ "*"
+ "ASCII"
+ "CHARSETALIASDIR"
+ "LIBCHARSET_CODESET"
+ "charset.alias"
+ "com.apple.libiconv.libcharset"
+ "libcharset.c"
+ "libcharset_build_map"
+ "locale_charset"
+ "locale_charset_mapped"
+ "map != NULL"
+ "map != NULL || nelem == 0"
+ "r"
+ "ret[0] != '\\0'"

```
