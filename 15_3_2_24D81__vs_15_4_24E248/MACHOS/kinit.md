## kinit

> `/usr/bin/kinit`

```diff

-693.60.3.0.0
-  __TEXT.__text: 0x55a4
+693.100.10.0.0
+  __TEXT.__text: 0x4ce8
   __TEXT.__auth_stubs: 0x830
   __TEXT.__const: 0x38
   __TEXT.__cstring: 0xf03
-  __TEXT.__unwind_info: 0x90
+  __TEXT.__unwind_info: 0x80
   __DATA_CONST.__auth_got: 0x418
   __DATA_CONST.__got: 0x48
   __DATA.__data: 0x648

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/Heimdal.framework/Versions/A/Heimdal
   - /usr/lib/libSystem.B.dylib
-  UUID: D5F127C6-6665-3809-B039-B38AD721368C
-  Functions: 24
+  UUID: 24F7CF43-5E74-3FD9-AF20-72DA970C3413
+  Functions: 23
   Symbols:   375
   CStrings:  222
 
Symbols:
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/HeimdalExecutables/install/Symbols/BuiltProducts/libroken-application.a(get_window_size.o)
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/HeimdalExecutables/install/Symbols/BuiltProducts/libroken-application.a(getarg.o)
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/HeimdalExecutables/install/Symbols/BuiltProducts/libroken-application.a(rand.o)
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/HeimdalExecutables/install/Symbols/BuiltProducts/libroken-application.a(simple_exec.o)
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/HeimdalExecutables/install/Symbols/BuiltProducts/libvers.a(print_version.o)
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/HeimdalExecutables/install/TempContent/Objects/Heimdal.build/kinit.build/DerivedSources/
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/HeimdalExecutables/install/TempContent/Objects/Heimdal.build/kinit.build/Objects-normal/arm64e/kinit.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/HeimdalExecutables/install/TempContent/Objects/Heimdal.build/kinit.build/Objects-normal/arm64e/kinit_vers.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/HeimdalExecutables/kuser/
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/HeimdalExecutables/lib/roken/
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/HeimdalExecutables/lib/vers/
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/HeimdalExecutables/install/TempContent/Objects/Heimdal.build/kinit.build/DerivedSources/
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/HeimdalExecutables/install/TempContent/Objects/Heimdal.build/kinit.build/Objects-normal/arm64e/kinit.o
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/HeimdalExecutables/install/TempContent/Objects/Heimdal.build/kinit.build/Objects-normal/arm64e/kinit_vers.o
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/HeimdalExecutables/install/TempContent/Objects/UninstalledProducts/libroken-application.a(get_window_size.o)
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/HeimdalExecutables/install/TempContent/Objects/UninstalledProducts/libroken-application.a(getarg.o)
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/HeimdalExecutables/install/TempContent/Objects/UninstalledProducts/libroken-application.a(rand.o)
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/HeimdalExecutables/install/TempContent/Objects/UninstalledProducts/libroken-application.a(simple_exec.o)
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/HeimdalExecutables/install/TempContent/Objects/UninstalledProducts/libvers.a(print_version.o)
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/HeimdalExecutables/kuser/
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/HeimdalExecutables/lib/roken/
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/HeimdalExecutables/lib/vers/

```
