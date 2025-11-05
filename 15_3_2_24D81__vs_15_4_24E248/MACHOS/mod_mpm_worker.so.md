## mod_mpm_worker.so

> `/usr/libexec/apache2/mod_mpm_worker.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x84c0
+880.0.0.0.0
+  __TEXT.__text: 0x7b34
   __TEXT.__auth_stubs: 0x760
   __TEXT.__cstring: 0x192a
-  __TEXT.__unwind_info: 0x94
+  __TEXT.__unwind_info: 0xa0
   __DATA_CONST.__auth_got: 0x3b0
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x268

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 37D456EA-91B9-339E-8A2D-06AFB050F322
+  UUID: 59697EC8-47C4-370A-8DD9-79AA1FB2C086
   Functions: 41
   Symbols:   212
   CStrings:  118
Functions:
~ _set_daemons_to_start : 120 -> 108
~ _set_min_spare_threads : 120 -> 108
~ _set_max_spare_threads : 120 -> 108
~ _set_max_workers : 596 -> 544
~ _set_threads_per_child : 120 -> 108
~ _set_server_limit : 120 -> 108
~ _set_thread_limit : 120 -> 108
~ _worker_open_logs : 3464 -> 3236
~ _worker_pre_config : 852 -> 768
~ _worker_check_config : 4520 -> 4324
~ _worker_run : 3628 -> 3428
~ _worker_query : 400 -> 396
~ _startup_children : 268 -> 244
~ _server_main_loop : 1696 -> 1548
~ _worker_note_child_killed : 220 -> 216
~ _make_child : 636 -> 584
~ _worker_note_child_started : 156 -> 152
~ _child_main : 2104 -> 1936
~ _worker_note_child_lost_slot : 744 -> 700
~ _clean_child_exit : 176 -> 152
~ _setup_threads_runtime : 1140 -> 1084
~ _start_threads : 1296 -> 1172
~ _check_signal : 84 -> 76
~ _join_start_thread : 228 -> 200
~ _signal_threads : 184 -> 172
~ _join_workers : 1576 -> 1472
~ _unblock_signal : 136 -> 132
~ _worker_thread : 1104 -> 996
~ _create_listener_thread : 352 -> 316
~ _process_socket : 216 -> 204
~ _listener_thread : 2360 -> 2128
~ _check_infinite_requests : 76 -> 68
~ _accept_mutex_error : 1188 -> 1116
~ _wakeup_listener : 160 -> 136
~ _close_worker_sockets : 168 -> 156
~ _perform_idle_server_maintenance : 3148 -> 2848
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/server/mpm/worker/worker.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/server/mpm/worker/worker.c"

```
