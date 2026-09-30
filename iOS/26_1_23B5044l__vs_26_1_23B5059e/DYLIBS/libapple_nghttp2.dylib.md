## libapple_nghttp2.dylib

> `/usr/lib/libapple_nghttp2.dylib`

```diff

-34.0.0.0.0
-  __TEXT.__text: 0xfe34
+35.0.0.0.0
+  __TEXT.__text: 0xfe2c
   __TEXT.__auth_stubs: 0xd0
   __TEXT.__const: 0x5850
   __TEXT.__cstring: 0x204c

   __DATA.__bss: 0x80
   __DATA_DIRTY.__data: 0x28
   - /usr/lib/libSystem.B.dylib
-  UUID: 91FBFE73-39CC-310E-A1E7-C68219BCBA9B
+  UUID: A36767D8-A34D-3F74-9D1E-4FC6469845D7
   Functions: 295
   Symbols:   431
   CStrings:  319
Functions:
~ _session_handle_invalid_stream2 : 140 -> 132
~ _session_update_glitch_ratelim -> _get_error_code_from_lib_error_code : 120 -> 164
~ _get_error_code_from_lib_error_code -> _nghttp2_session_add_ping : 164 -> 236
~ _nghttp2_session_add_ping -> _session_update_stream_priority : 236 -> 128
~ _session_update_stream_priority -> _session_call_error_callback : 128 -> 292
~ _session_call_error_callback -> _session_update_glitch_ratelim : 292 -> 120
CStrings:
+ "1.67.1"
- "1.67.0"

```
