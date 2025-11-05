## msutil

> `/usr/libexec/msutil`

```diff

 115.0.0.0.0
-  __TEXT.__text: 0x13cc
+  __TEXT.__text: 0x13bc
   __TEXT.__auth_stubs: 0x2b0
   __TEXT.__objc_stubs: 0x40
   __TEXT.__const: 0x68

   __TEXT.__oslogstring: 0x228
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x20
-  __TEXT.__unwind_info: 0x88
+  __TEXT.__unwind_info: 0x90
   __DATA_CONST.__auth_got: 0x160
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x180

   - /usr/lib/libSMC.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D5CC3093-D009-36F5-9CD5-9594D6F5D0F8
-  Functions: 30
-  Symbols:   257
+  UUID: 6E98A71B-DB07-30A2-9D83-A6C2B0A7B8FA
+  Functions: 31
+  Symbols:   262
   CStrings:  67
 
Symbols:
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MultiverseSupport/install/TempContent/Objects/MultiverseSupport.build/msutil.build/DerivedSources/
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MultiverseSupport/install/TempContent/Objects/MultiverseSupport.build/msutil.build/Objects-normal/arm64e/internal.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MultiverseSupport/install/TempContent/Objects/MultiverseSupport.build/msutil.build/Objects-normal/arm64e/msutil.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MultiverseSupport/install/TempContent/Objects/MultiverseSupport.build/msutil.build/Objects-normal/arm64e/msutil_vers.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MultiverseSupport/install/TempContent/Objects/MultiverseSupport.build/msutil.build/Objects-normal/arm64e/shutdown.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MultiverseSupport/msutil/
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MultiverseSupport/src/
+ open_console.cold.1
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/MultiverseSupport/install/TempContent/Objects/MultiverseSupport.build/msutil.build/DerivedSources/
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/MultiverseSupport/install/TempContent/Objects/MultiverseSupport.build/msutil.build/Objects-normal/arm64e/internal.o
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/MultiverseSupport/install/TempContent/Objects/MultiverseSupport.build/msutil.build/Objects-normal/arm64e/msutil.o
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/MultiverseSupport/install/TempContent/Objects/MultiverseSupport.build/msutil.build/Objects-normal/arm64e/msutil_vers.o
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/MultiverseSupport/install/TempContent/Objects/MultiverseSupport.build/msutil.build/Objects-normal/arm64e/shutdown.o
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/MultiverseSupport/msutil/
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/MultiverseSupport/src/
Functions:
~ _main : 468 -> 460
~ _multiverse_log : 184 -> 180
~ _open_console : 68 -> 56
~ _shutdown_macOS : 2076 -> 2068
~ ___register_for_shutdown_notification_from_macOS_block_invoke_2 : 324 -> 320
+ open_console.cold.1
~ shutdown_macOS.cold.2 : 52 -> 120
~ shutdown_macOS.cold.3 : 52 -> 64
~ shutdown_macOS.cold.4 : 52 -> 120
~ shutdown_macOS.cold.7 : 120 -> 52
~ shutdown_macOS.cold.8 : 64 -> 52
~ shutdown_macOS.cold.9 : 120 -> 52

```
