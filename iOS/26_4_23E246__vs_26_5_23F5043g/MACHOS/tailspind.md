## tailspind

> `/usr/libexec/tailspind`

```diff

-250.0.0.0.0
-  __TEXT.__text: 0xd1d4
-  __TEXT.__auth_stubs: 0xb80
+250.2.0.0.0
+  __TEXT.__text: 0xda30
+  __TEXT.__auth_stubs: 0xbd0
   __TEXT.__objc_stubs: 0x960
   __TEXT.__objc_methlist: 0x1f4
-  __TEXT.__const: 0x12c
-  __TEXT.__cstring: 0x102f
+  __TEXT.__const: 0x134
+  __TEXT.__cstring: 0x10c1
   __TEXT.__objc_methname: 0xc42
-  __TEXT.__oslogstring: 0x259e
+  __TEXT.__oslogstring: 0x27e5
   __TEXT.__objc_classname: 0x18
   __TEXT.__objc_methtype: 0xfb
   __TEXT.__gcc_except_tab: 0x238
-  __TEXT.__unwind_info: 0x3b8
-  __DATA_CONST.__auth_got: 0x5d0
+  __TEXT.__unwind_info: 0x3d0
+  __DATA_CONST.__auth_got: 0x5f8
   __DATA_CONST.__got: 0x160
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x408
+  __DATA_CONST.__const: 0x448
   __DATA_CONST.__cfstring: 0x5c0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_selrefs: 0x2f0
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x2160
+  __DATA.__data: 0x2164
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x580
+  __DATA.__bss: 0x598
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 6EB83FD8-12F3-3E0C-89A2-4422E3404D4E
-  Functions: 247
-  Symbols:   238
-  CStrings:  483
+  UUID: F8AFCC11-A943-3B73-94AA-51F5F744BF8E
+  Functions: 263
+  Symbols:   243
+  CStrings:  499
 
Symbols:
+ _bzero
+ _notify_get_state
+ _notify_register_check
+ _tailspin_buffer_size_is_default
+ _tailspin_buffer_size_reset
CStrings:
+ "%s: %llu"
+ "Buffer size override detected from %s. Game mode state change ignored"
+ "Detected non-default buffer size set by tailspin. Resetting buffer size"
+ "Failed to apply config for game mode state change"
+ "Failed to get memsize: %{errno}d"
+ "Unhandled Game Mode state value: %llu"
+ "_State"
+ "client %s [%d] requested for tailspin data but was rejected by the allowlist"
+ "com.apple.system.console_mode_changed"
+ "com.apple.tailspin.game_mode_state_changed"
+ "gGameModeNotifyToken is invalid"
+ "game_mode_state"
+ "hangtracerd"
+ "hw.memsize_physical"
+ "is_12GB_or_greater: %{bool}d, is_feature_flag_enabled:  %{bool}d, is_300MB_eligible_device: %{bool}d, is_default_buffer_size: %{bool}d, is_game_mode_enabled: %{bool}d, should_apply_new_config: %{bool}d"
+ "tailspind"

```
