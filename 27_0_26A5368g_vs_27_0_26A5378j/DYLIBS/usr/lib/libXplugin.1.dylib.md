## libXplugin.1.dylib

> `/usr/lib/libXplugin.1.dylib`

```diff

-  __TEXT.__text: 0x9730
-  __TEXT.__const: 0x52c
-  __TEXT.__cstring: 0x145d
-  __TEXT.__oslogstring: 0x34
+  __TEXT.__text: 0xcbbc
+  __TEXT.__const: 0x554
+  __TEXT.__oslogstring: 0x3b3
+  __TEXT.__cstring: 0x1161
   __TEXT.__unwind_info: 0x258
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x100
+  __DATA_CONST.__const: 0x120
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x80
-  __AUTH_CONST.__auth_got: 0x628
+  __AUTH_CONST.__auth_got: 0x640
   __DATA.__data: 0xd0
-  __DATA.__bss: 0x88
+  __DATA.__bss: 0x98
   __DATA.__common: 0x44
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/Carbon.framework/Versions/A/Carbon

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/OpenGL.framework/Versions/A/OpenGL
   - /usr/lib/libSystem.B.dylib
-  Functions: 168
-  Symbols:   438
-  CStrings:  220
+  Functions: 187
+  Symbols:   468
+  CStrings:  225
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __AUTH_CONST.__cfstring : content changed
Symbols:
+ _OUTLINED_FUNCTION_3
+ ____xp_log_get_block_invoke
+ ___xp_init_window_rights_block_invoke_2
+ __os_log_error_impl
+ __os_log_impl
+ __xp_log_get
+ _dispatch_once
+ _os_log_create
+ _xp_configure_window_cb
+ _xp_log_get
+ _xp_log_get.log
+ _xp_log_get.once
+ _xp_set_dock_proxy_on_window
+ xp_set_cursor
+ xp_window_new
- __xp_log
- _vfprintf
CStrings:
+ "%s: error: %s: CGError %d\n"
+ "%s: error: %s: IOReturn 0x%08x\n"
+ "%s: error: %s: xp_error %d\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LeTYTH/Sources/X11_Xplugin/libXplugin/xp-main.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LeTYTH/Sources/X11_Xplugin/libXplugin/xp-surface.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LeTYTH/Sources/X11_Xplugin/libXplugin/xp-window.c"
+ "_xp_init_window_rights_block_invoke"
+ "default"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.V3t2SE/Sources/X11_Xplugin/libXplugin/xp-main.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.V3t2SE/Sources/X11_Xplugin/libXplugin/xp-surface.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.V3t2SE/Sources/X11_Xplugin/libXplugin/xp-window.c"

```
