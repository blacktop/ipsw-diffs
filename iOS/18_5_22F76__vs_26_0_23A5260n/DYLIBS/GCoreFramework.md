## GCoreFramework

> `/System/Library/PrivateFrameworks/GCoreFramework.framework/GCoreFramework`

```diff

-1026.100.5.0.0
-  __TEXT.__text: 0x1038
-  __TEXT.__auth_stubs: 0x1e0
-  __TEXT.__const: 0x70
-  __TEXT.__cstring: 0xb6
-  __TEXT.__oslogstring: 0x391
-  __TEXT.__unwind_info: 0x88
+1038.0.0.0.0
+  __TEXT.__text: 0x1274
+  __TEXT.__auth_stubs: 0x210
+  __TEXT.__const: 0x80
+  __TEXT.__cstring: 0xc2
+  __TEXT.__oslogstring: 0x3f6
+  __TEXT.__unwind_info: 0x80
   __TEXT.__objc_methname: 0xae
   __TEXT.__objc_stubs: 0x140
   __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0xe0
+  __DATA_CONST.__const: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x50
-  __AUTH_CONST.__auth_got: 0xf8
+  __AUTH_CONST.__auth_got: 0x110
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0xa0
+  __AUTH_CONST.__cfstring: 0xc0
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 24604DD5-A103-30D6-B47C-AD2860869192
-  Functions: 16
-  Symbols:   87
-  CStrings:  52
+  UUID: 6D994C40-4292-3DF1-B02C-54F08E39FC24
+  Functions: 19
+  Symbols:   96
+  CStrings:  64
 
Symbols:
+ _OUTLINED_FUNCTION_2
+ ___stdoutp
+ __os_log_impl
+ _create_gcore_with_options.cold.12
+ _create_gcore_with_options.cold.13
+ _fileno
+ _mach_error_string
+ _posix_spawn_file_actions_addinherit_np
+ _strsignal
- _optind
- _printf
- _puts
Functions:
~ _create_gcore_with_options : 2708 -> 3036
+ _OUTLINED_FUNCTION_2
~ _create_gcore_with_options.cold.2 : 104 -> 148
~ _create_gcore_with_options.cold.8 : 148 -> 104
~ _create_gcore_with_options.cold.9 : 124 -> 104
~ _create_gcore_with_options.cold.10 : 64 -> 104
~ _create_gcore_with_options.cold.11 : 256 -> 104
CStrings:
+ "-b"
+ "-c"
+ "-q"
+ "-s"
+ "-x"
+ "Cannot register corpse port error 0x%x (%s)"
+ "Expr posix_spawn_file_actions_addinherit_np(&factions, corefd) failed with result %d"
+ "Expr posix_spawn_file_actions_addinherit_np(&factions, fileno(stdout)) failed with result %d"
+ "Expr posix_spawnattr_init(&factions) failed with result %d"
+ "Expr posix_spawnattr_init(&spawnattr) failed with result %d"
+ "com.apple.gcore"
+ "content"
+ "framework"
+ "maxsize"
+ "pathformat"
+ "posix_spawn %s returns %d (%s)"
+ "quiet"
+ "suspend"
+ "unrecognized option: %s"
+ "wait4 %s pid %d"
+ "wait4: %d %s exit status %d, ret %d"
+ "wait4: %d error: errno %d (%s)"
+ "wait4: %d signal %d (%s)"
+ "wait4: %d signal %d (%s), ret %d"
+ "wait4: %d status 0x%x\n"
- "Cannot register corpse port err %d"
- "Error spawning \"%s\""
- "Wait finished with result %d (\"%s\") child_ret_value %d \"%s\" errno %d (\"%s\")"
- "Wait finished with result %d (\"%s\") child_ret_value %d \"%s\" errno %d (\"%s\") but no error, trying again"
- "com.apple.system_cmds"
- "continued"
- "entering in waitpid"
- "gCore PID %d"
- "gcore exited, status=%d wait_ret_value=%d WEXITSTATUS(%d)\n"
- "gcore killed by signal %d\n"
- "gcore stopped by signal %d\n"
- "gcore_framework"
- "leaving waitpid status=%d wait_ret_value=%d WEXITSTATUS(%d)  errno %d (\"%s\")\n"
- "stopped by signal %d\n"

```
