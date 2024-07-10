## libsystem_notify.dylib

> `/usr/lib/system/libsystem_notify.dylib`

```diff

-327.0.3.0.0
-  __TEXT.__text: 0xfdd0
-  __TEXT.__auth_stubs: 0x630
+327.0.2.0.0
+  __TEXT.__text: 0xf8b0
+  __TEXT.__auth_stubs: 0x5d0
   __TEXT.__const: 0x1b8
-  __TEXT.__cstring: 0xc88
+  __TEXT.__cstring: 0xb7d
   __TEXT.__dof_notify: 0x5a6
   __TEXT.__unwind_info: 0x58
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__const: 0x1a0
-  __AUTH_CONST.__auth_got: 0x318
+  __AUTH_CONST.__auth_got: 0x2e8
   __AUTH_CONST.__const: 0x190
-  __DATA.__data: 0x20
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x30
   __DATA_DIRTY.__bss: 0x8

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 128
-  Symbols:   135
-  CStrings:  88
+  Functions: 127
+  Symbols:   129
+  CStrings:  79
 
Symbols:
- __dyld_get_image_uuid
- __dyld_get_shared_cache_range
- __dyld_get_shared_cache_uuid
- __os_log_simple
- _getenv
- _strtok_r
CStrings:
- ","
- "1"
- "DarwinNotificationLogging"
- "[%!s(MISSING)] canceling notification: token=%!d(MISSING) flags=0x%!x(MISSING)"
- "[%!s(MISSING)] registered for notification token=%!d(MISSING) flags=0x%!x(MISSING)"
- "[%!s(MISSING)] registered for notification: token=%!d(MISSING) flags=0x%!x(MISSING)"
- "com.apple.libnotify"
- "enabled logging for %!s(MISSING)"
- "enabled logging for all notifications"

```
