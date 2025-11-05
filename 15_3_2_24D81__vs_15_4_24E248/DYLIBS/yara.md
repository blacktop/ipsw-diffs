## yara

> `/System/Library/PrivateFrameworks/yara.framework/Versions/A/yara`

```diff

-33.0.0.0.0
-  __TEXT.__text: 0x3cd90
+35.0.0.0.0
+  __TEXT.__text: 0x3c5f8
   __TEXT.__auth_stubs: 0x600
   __TEXT.__const: 0x3320
-  __TEXT.__cstring: 0x8d83
-  __TEXT.__unwind_info: 0x708
+  __TEXT.__cstring: 0x8d7e
+  __TEXT.__unwind_info: 0x6d0
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x5d0
   __AUTH_CONST.__auth_got: 0x300

   __DATA_DIRTY.__bss: 0x20
   __DATA_DIRTY.__common: 0x200
   - /usr/lib/libSystem.B.dylib
-  UUID: 9DF5467E-93B8-3827-999B-029316FC8619
-  Functions: 1121
+  UUID: 3351998E-C10A-3622-AB7D-D701F7BC7432
+  Functions: 1103
   Symbols:   1263
-  CStrings:  1982
+  CStrings:  1980
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/YARA/libyara/modules/dex/dex.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/YARA/libyara/modules/dotnet/dotnet.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/YARA/libyara/modules/elf/elf.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/YARA/libyara/modules/hash/hash.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/YARA/libyara/modules/macho/macho.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/YARA/libyara/modules/math/math.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/YARA/libyara/modules/pe/pe.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/YARA/libyara/modules/tests/tests.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/YARA/libyara/modules/time/time.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/YARA/libyara/object.c"
- "$"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/YARA/libyara/modules/dex/dex.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/YARA/libyara/modules/dotnet/dotnet.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/YARA/libyara/modules/elf/elf.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/YARA/libyara/modules/hash/hash.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/YARA/libyara/modules/macho/macho.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/YARA/libyara/modules/math/math.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/YARA/libyara/modules/pe/pe.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/YARA/libyara/modules/tests/tests.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/YARA/libyara/modules/time/time.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/YARA/libyara/object.c"
- "be"

```
