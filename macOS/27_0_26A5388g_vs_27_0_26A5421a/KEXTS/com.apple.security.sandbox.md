## com.apple.security.sandbox

> `com.apple.security.sandbox`

```diff

-3051.0.42.0.2
-  __TEXT.__os_log: 0x2583
-  __TEXT.__const: 0x20717
-  __TEXT.__cstring: 0x7c91
-  __TEXT_EXEC.__text: 0x52bc0
-  __TEXT_EXEC.__auth_stubs: 0x1500
+3051.0.52.0.0
+  __TEXT.__os_log: 0x2634
+  __TEXT.__const: 0x206d7
+  __TEXT.__cstring: 0x7dd5
+  __TEXT_EXEC.__text: 0x5353c
+  __TEXT_EXEC.__auth_stubs: 0x1540
   __DATA.__data: 0x410
   __DATA.__bss: 0x7f18c
-  __DATA_CONST.__const: 0x3f70
+  __DATA_CONST.__const: 0x3fa0
   __DATA_CONST.__kalloc_type: 0x1700
   __DATA_CONST.__kalloc_var: 0x550
-  __DATA_CONST.__auth_got: 0xa80
+  __DATA_CONST.__auth_got: 0xaa0
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 963
-  Symbols:   1925
-  CStrings:  1591
+  Functions: 967
+  Symbols:   1938
+  CStrings:  1612
 
Symbols:
+ __ZN16CoreAnalyticsHub22analyticsSendEventLazyEP8OSStringP8OSObject
+ __ZN8OSString11withCStringEPKc
+ __ZN9OSBoolean11withBooleanEb
+ __ZZ34sb_submit_release_analytics_tuplesE11_os_log_fmt
+ __ZZ34sb_submit_release_analytics_tuplesE11_os_log_fmt_0
+ __ZZ34sb_submit_release_analytics_tuplesE11_os_log_fmt_1
+ ___is_100875343_checkfix_required_block_invoke
+ __basename
+ _hook_vnode_check_readlink2
+ _sb_submit_release_analytics_tuples
+ _vnodeop_desc_name
+ hook_vnode_notify_dead_access._os_log_fmt
+ macl_xlate_destroy_entry.kalloc_type_view_185
+ macl_xlate_entry_for_form.kalloc_type_view_577
+ macl_xlate_lookup_by_entry.kalloc_type_view_353
+ syscall_appbundle_scan_end._os_log_fmt
- macl_xlate_destroy_entry.kalloc_type_view_165
- macl_xlate_entry_for_form.kalloc_type_view_557
- macl_xlate_lookup_by_entry.kalloc_type_view_333
CStrings:
+ "\"%s: unsupported format specifier \\\"%s\\\"\" @%s:%d"
+ "%b"
+ "%d"
+ "%s(%s) failed: %d"
+ "%s: failed to allocate event name"
+ "%s: failed to allocate payload"
+ "SharedSupport.dmg"
+ "app bundle scan: _basename failed for path: %s"
+ "bundle"
+ "bundleRelativePath"
+ "com.apple.sandbox.revoke.bundle-scan"
+ "com.apple.sandbox.revoke.dead-access"
+ "com.apple.system_installd"
+ "op"
+ "pack_analytics_osdict"
+ "pid"
+ "processName"
+ "release_analytics.cpp"
+ "revokeCount"
+ "sb_submit_release_analytics_tuples"
+ "scanDurationMs"
```
