## libsystem_symptoms.dylib

> `/usr/lib/system/libsystem_symptoms.dylib`

```diff

-2001.80.5.0.0
-  __TEXT.__text: 0x5bd0
+2022.100.26.0.0
+  __TEXT.__text: 0x5c18
   __TEXT.__auth_stubs: 0x330
   __TEXT.__cstring: 0x18b3
   __TEXT.__const: 0x30
-  __TEXT.__unwind_info: 0x140
+  __TEXT.__unwind_info: 0x138
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x148
   __AUTH_CONST.__auth_got: 0x198

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 695D143C-5D59-37B0-8784-4AE727AFEEF5
-  Functions: 66
-  Symbols:   158
+  UUID: 8BED9E04-42CD-32F0-A90C-ED59E8FD2888
+  Functions: 71
+  Symbols:   163
   CStrings:  195
 
Symbols:
+ _symptoms_daemon_fallback_initial_disposition.cold.1
+ _symptoms_daemon_fallback_subseq_disposition.cold.1
+ _symptoms_daemon_fallback_subseq_disposition.cold.2
+ _symptoms_is_daemon_fallback_blacklisted.cold.1
+ obtain_symptom_framework.cold.1
Functions:
~ __symptoms_is_daemon_fallback_blacklisted : 132 -> 116
~ _obtain_symptom_framework : 212 -> 196
~ _symptom_set_additional_qualifier : 240 -> 248
~ _symptom_post : 456 -> 460
~ _ensure_alert : 368 -> 372
~ _ensure_symptom_framework_connect : 720 -> 712
~ _read_current_status : 316 -> 312
~ _symptom_transport_send : 364 -> 376
~ ___symptom_transport_connect_block_invoke : 1708 -> 1716
~ _reevaluate_sr_symptoms : 728 -> 732
~ _symptoms_incoming_message : 1452 -> 1444
~ _read_symptoms : 928 -> 940
~ __symptoms_daemon_fallback_initial_disposition : 116 -> 100
~ __symptoms_daemon_fallback_subseq_disposition : 764 -> 732

```
