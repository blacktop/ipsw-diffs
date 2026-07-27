## libXplugin.1.dylib

> `/usr/lib/libXplugin.1.dylib`

### Sections with Same Size but Changed Content

- `__AUTH_CONST.__cfstring`

```diff

-58.0.0.0.0
-  __TEXT.__text: 0x952c
-  __TEXT.__auth_stubs: 0xc50
-  __TEXT.__const: 0x52c
-  __TEXT.__cstring: 0x1341
-  __TEXT.__oslogstring: 0x34
-  __TEXT.__unwind_info: 0x258
+58.2.0.0.0
+  __TEXT.__text: 0xd540
+  __TEXT.__auth_stubs: 0xc80
+  __TEXT.__const: 0x554
+  __TEXT.__oslogstring: 0x3b3
+  __TEXT.__cstring: 0x1161
+  __TEXT.__unwind_info: 0x268
   __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x100
-  __AUTH_CONST.__auth_got: 0x628
-  __AUTH_CONST.__const: 0x60
+  __DATA_CONST.__const: 0x120
+  __AUTH_CONST.__auth_got: 0x640
+  __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x80
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
-  Symbols:   424
-  CStrings:  209
+  Functions: 191
+  Symbols:   439
+  CStrings:  221
 
Symbols:
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
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
+ "%s: assertion failed: sibling != NULL\n"
+ "%s: assertion failed: transient_for != NULL\n"
+ "%s: assertion failed: values->width != 0 && values->height != 0\n"
+ "%s: error: %s: CGError %d\n"
+ "%s: error: %s: IOReturn 0x%08x\n"
+ "%s: error: %s: xp_error %d\n"
+ "%s: error: can't make indexed backing\n"
+ "%s: error: can't resize indexed backing\n"
+ "%s: error: invalid shape\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4YiK7K/Sources/X11_Xplugin/libXplugin/xp-main.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4YiK7K/Sources/X11_Xplugin/libXplugin/xp-surface.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4YiK7K/Sources/X11_Xplugin/libXplugin/xp-window.c"
+ "CopyColorSpaceForRect failed"
+ "GetSurfaceBounds failed"
+ "SetSurfaceColorSpace failed"
+ "_xp_init_window_rights_block_invoke"
+ "default"
+ "surface allocation failed"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2sNIXx/Sources/X11_Xplugin/libXplugin/xp-main.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2sNIXx/Sources/X11_Xplugin/libXplugin/xp-surface.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2sNIXx/Sources/X11_Xplugin/libXplugin/xp-window.c"
- "can't make indexed backing"
- "can't resize indexed backing"
- "transient_for != NULL"
```
