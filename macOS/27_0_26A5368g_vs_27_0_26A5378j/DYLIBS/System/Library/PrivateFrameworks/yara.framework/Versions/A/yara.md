## yara

> `/System/Library/PrivateFrameworks/yara.framework/Versions/A/yara`

```diff

-  __TEXT.__text: 0x3acfc
+  __TEXT.__text: 0x3aef0
   __TEXT.__const: 0x3348
   __TEXT.__cstring: 0x8eb4
-  __TEXT.__unwind_info: 0x6d8
+  __TEXT.__unwind_info: 0x6e0
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x5d0
   __DATA_CONST.__got: 0x0
Sections:
~ __TEXT.__cstring : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH.__data : content changed
Functions:
~ _yr_object_function_create : 344 -> 352
~ __yr_object_lookup : 624 -> 620
~ _yr_rules_define_integer_variable : 132 -> 148
~ _yr_rules_define_boolean_variable : 136 -> 152
~ _yr_rules_define_float_variable : 140 -> 148
~ _yr_rules_destroy : 112 -> 96
~ _yr_get_entry_point_offset : 624 -> 672
~ _yr_scanner_scan_mem_blocks : 1556 -> 1544
~ _pe__load : 7256 -> 7264
~ __pe_iterate_resources : 532 -> 520
~ _yr_execute_code : 8416 -> 8428
~ _yr_scan_verify_match : 1464 -> 1428
~ _strnlen_w : 48 -> 40
~ _re_yyparse : 3088 -> 3008
~ _yytnamerr : 172 -> 160
~ _yara_yyparse : 14424 -> 15260
~ _dotnet_parse_tilde_2 : 5036 -> 4832
~ _pe_rva_to_offset : 272 -> 256
~ _yr_parser_lookup_string : 164 -> 144
~ _yr_parser_reduce_string_identifier : 520 -> 512
~ _yr_modules_do_declarations : 152 -> 160
~ __yr_base64_create_nodes : 884 -> 876
~ _elf_rva_to_offset_32_le : 232 -> 256
~ _elf_rva_to_offset_64_le : 256 -> 280
~ _elf_rva_to_offset_32_be : 292 -> 316
~ _elf_rva_to_offset_64_be : 316 -> 340
~ _parse_elf_header_32_le : 1984 -> 1944
~ _parse_elf_header_64_le : 2004 -> 1968
~ _parse_elf_header_32_be : 2316 -> 2292
~ _parse_elf_header_64_be : 2308 -> 2288
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lXTpWM/Sources/YARA/libyara/modules/dex/dex.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lXTpWM/Sources/YARA/libyara/modules/dotnet/dotnet.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lXTpWM/Sources/YARA/libyara/modules/elf/elf.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lXTpWM/Sources/YARA/libyara/modules/hash/hash.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lXTpWM/Sources/YARA/libyara/modules/macho/macho.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lXTpWM/Sources/YARA/libyara/modules/math/math.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lXTpWM/Sources/YARA/libyara/modules/pe/pe.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lXTpWM/Sources/YARA/libyara/modules/tests/tests.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lXTpWM/Sources/YARA/libyara/modules/time/time.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lXTpWM/Sources/YARA/libyara/object.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.eyYxds/Sources/YARA/libyara/modules/dex/dex.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.eyYxds/Sources/YARA/libyara/modules/dotnet/dotnet.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.eyYxds/Sources/YARA/libyara/modules/elf/elf.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.eyYxds/Sources/YARA/libyara/modules/hash/hash.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.eyYxds/Sources/YARA/libyara/modules/macho/macho.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.eyYxds/Sources/YARA/libyara/modules/math/math.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.eyYxds/Sources/YARA/libyara/modules/pe/pe.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.eyYxds/Sources/YARA/libyara/modules/tests/tests.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.eyYxds/Sources/YARA/libyara/modules/time/time.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.eyYxds/Sources/YARA/libyara/object.c"

```
