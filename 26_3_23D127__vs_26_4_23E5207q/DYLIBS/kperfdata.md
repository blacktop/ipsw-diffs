## kperfdata

> `/System/Library/PrivateFrameworks/kperfdata.framework/kperfdata`

```diff

-159.0.0.0.0
-  __TEXT.__text: 0x8248
+161.0.0.0.0
+  __TEXT.__text: 0x81f8
   __TEXT.__auth_stubs: 0x460
   __TEXT.__cstring: 0x350
   __TEXT.__const: 0x28

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/PrivateFrameworks/kperf.framework/kperf
   - /usr/lib/libSystem.B.dylib
-  UUID: 02B6C15A-1D85-32D5-97AE-DF2F4418C584
+  UUID: E0B8F275-5842-3C67-A6B2-999D8FF7103D
   Functions: 135
   Symbols:   275
   CStrings:  82
Functions:
~ _kpdecode_cursor_next_record : 4552 -> 4472
~ __kpdecode_cursor_next_kevent : 492 -> 508
~ _batch_get_bytes : 708 -> 696
~ _kpep_config_decode_event : 764 -> 740
~ _add_event_internal : 388 -> 384
~ _kpep_config_remove_event : 316 -> 312
~ _kpep_config_events : 76 -> 68
~ _add_config_event_internal : 356 -> 360
~ _kpfile_read_threadmap : 356 -> 360
~ _kpfile_read_events : 1152 -> 1168
~ _kpfile_write_events : 924 -> 936

```
