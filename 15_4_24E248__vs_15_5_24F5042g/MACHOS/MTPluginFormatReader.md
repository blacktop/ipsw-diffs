## MTPluginFormatReader

> `/System/Library/Frameworks/MediaToolbox.framework/Versions/A/XPCServices/MTPluginFormatReader.xpc/Contents/MacOS/MTPluginFormatReader`

```diff

-3210.19.1.5.2
-  __TEXT.__text: 0x20
-  __TEXT.__auth_stubs: 0x10
+3225.3.2.15.1
+  __TEXT.__text: 0xf0
+  __TEXT.__auth_stubs: 0x50
+  __TEXT.__const: 0x8
+  __TEXT.__oslogstring: 0x30
+  __TEXT.__cstring: 0x5
   __TEXT.__unwind_info: 0x58
-  __DATA_CONST.__auth_got: 0x8
+  __DATA_CONST.__auth_got: 0x28
   __DATA_CONST.__got: 0x8
   - /System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia
   - /System/Library/Frameworks/MediaToolbox.framework/Versions/A/MediaToolbox
   - /usr/lib/libSystem.B.dylib
   Functions: 1
-  Symbols:   5
-  CStrings:  0
+  Symbols:   9
+  CStrings:  2
 
Symbols:
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _os_log_type_enabled
CStrings:
+ "<<< MTPluginFormatReaderServer >>> %s: starting"
+ "main"

```
