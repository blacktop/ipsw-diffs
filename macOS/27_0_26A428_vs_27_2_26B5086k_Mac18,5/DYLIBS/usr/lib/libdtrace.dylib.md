## libdtrace.dylib

> `/usr/lib/libdtrace.dylib`

```diff

-416.0.3.0.0
-  __TEXT.__text: 0x4c244
-  __TEXT.__const: 0x5104
-  __TEXT.__cstring: 0x9e9c
+416.40.5.0.0
+  __TEXT.__text: 0x4cc54
+  __TEXT.__const: 0x5164
+  __TEXT.__cstring: 0xa0c8
   __TEXT.__oslogstring: 0xc38
-  __TEXT.__unwind_info: 0xc98
+  __TEXT.__unwind_info: 0xd58
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x5b88
+  __DATA_CONST.__const: 0x5db0
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x2570
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__auth_got: 0x730
-  __DATA.__data: 0x158
-  __DATA.__common: 0x4
+  __DATA.__data: 0x168
+  __DATA.__common: 0x278
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/Versions/A/CoreSymbolication
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 817
-  Symbols:   1218
-  CStrings:  2019
+  Functions: 886
+  Symbols:   1293
+  CStrings:  2039
 
Symbols:
+ __CTF_NULLSTR
+ __CTF_SECTION
+ ___libc_threaded
+ __elf32_cookscn
+ __elf32_ehdr
+ __elf32_msize
+ __elf32_mtype
+ __elf32_snode_init
+ __elf64_cookscn
+ __elf64_ehdr
+ __elf64_msize
+ __elf64_mtype
+ __elf64_snode_init
+ __elf_cookscn
+ __elf_inmap
+ __elf_libc_threaded
+ __elf_locked_getdata
+ __libctf_debug
+ _ctf_add_enum
+ _ctf_add_float
+ _ctf_add_integer
+ _ctf_add_member
+ _ctf_add_pointer
+ _ctf_add_struct
+ _ctf_add_union
+ _ctf_alloc
+ _ctf_copy_membnames
+ _ctf_data_alloc
+ _ctf_data_free
+ _ctf_data_protect
+ _ctf_decl_init
+ _ctf_dprintf
+ _ctf_enum_name
+ _ctf_errno
+ _ctf_free
+ _ctf_func_args
+ _ctf_getmodel
+ _ctf_getspecific
+ _ctf_hash_size
+ _ctf_list_append
+ _ctf_list_delete
+ _ctf_list_prepend
+ _ctf_lookup_by_symbol
+ _ctf_member_info
+ _ctf_parent_file
+ _ctf_parent_name
+ _ctf_sect_munmap
+ _ctf_set_array
+ _ctf_set_errno
+ _ctf_set_open_errno
+ _ctf_setmodel
+ _ctf_setspecific
+ _ctf_strerror
+ _ctf_strptr
+ _ctf_type_compat
+ _ctf_type_printf_compat
+ _ctf_type_visit
+ _elf32_getehdr
+ _elf32_getshdr
+ _elf64_getehdr
+ _elf64_getshdr
+ _elf_begin
+ _elf_cntl
+ _elf_end
+ _elf_getimage
+ _elf_getscn
+ _elf_macho_str_cookie
+ _elf_macho_str_off
+ _gelf_getclass
+ _gelf_getehdr
+ _get_type_ctt_info
+ _get_type_ctt_name
+ _get_type_ctt_size
+ _get_type_ctt_type
+ _mtype
+ _xTab
+ _z_strerror
+ _z_uncompress
- fmsize
- mtype
- xTab
CStrings:
+ "%lu total types processed\n"
+ "%u base type names hashed\n"
+ "%u enum names hashed\n"
+ "%u struct names hashed (%d long)\n"
+ "%u union names hashed (%d long)\n"
+ ".SUNW_ctf"
+ "<NULL>"
+ "CTF container %p is a child\n"
+ "CTF container %p is a parent\n"
+ "ctf_bufopen: magic=0x%x version=%u\n"
+ "ctf_bufopen: parent name %s (label %s)\n"
+ "ctf_bufopen: uncompressed size=%lu\n"
+ "ctf_close(%p) refcnt=%u\n"
+ "decompressing CTF data using %s\n"
+ "detected invalid CTF kind -- %u\n"
+ "libctf DEBUG: "
+ "loaded %lu symtab entries\n"
+ "type %ld cycle detected\n"
+ "zlib inflate err: %s\n"
+ "zlib inflate short -- got %lu of %lu bytes\n"
```
