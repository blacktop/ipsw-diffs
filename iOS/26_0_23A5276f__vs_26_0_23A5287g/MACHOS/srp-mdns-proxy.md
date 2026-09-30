## srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

```diff

-2874.0.0.0.1
-  __TEXT.__text: 0x81eb4
-  __TEXT.__auth_stubs: 0x1350
+2881.0.7.0.0
+  __TEXT.__text: 0x83c20
+  __TEXT.__auth_stubs: 0x1360
   __TEXT.__objc_stubs: 0x180
   __TEXT.__objc_methlist: 0x21c
   __TEXT.__const: 0x282
-  __TEXT.__cstring: 0x75e0
-  __TEXT.__oslogstring: 0x11d26
+  __TEXT.__cstring: 0x7671
+  __TEXT.__oslogstring: 0x11eb8
   __TEXT.__objc_classname: 0x38
   __TEXT.__objc_methname: 0x4e6
   __TEXT.__objc_methtype: 0x237
-  __TEXT.__unwind_info: 0x578
-  __DATA_CONST.__auth_got: 0x9b0
+  __TEXT.__unwind_info: 0x580
+  __DATA_CONST.__auth_got: 0x9b8
   __DATA_CONST.__got: 0x210
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x8f0

   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x2a0
-  __DATA.__bss: 0x818
+  __DATA.__bss: 0x970
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/libmdns.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6425E48B-EA2F-3FA8-B431-434506C079AA
-  Functions: 450
-  Symbols:   1124
-  CStrings:  2444
+  UUID: 8FE6A589-F3E4-3E55-A3C8-2F4D683CEAA9
+  Functions: 453
+  Symbols:   1137
+  CStrings:  2459
 
Symbols:
+ __block_descriptor_tmp.1348
+ __block_descriptor_tmp.17.1438
+ __block_descriptor_tmp.18.1532
+ __block_descriptor_tmp.2541
+ __block_descriptor_tmp.8.1395
+ __block_literal_global.1439
+ _have_os_status
+ _is_internal
+ _num_files
+ _num_types
+ _os_variant_has_internal_diagnostics
+ _ref_filenames
+ _ref_history
+ _ref_history_cur
+ _ref_history_highwater
+ _ref_types
+ _srp_log_ref_check
+ _srp_log_ref_final
+ _thread_service_flag_create_
- __block_descriptor_tmp.1333
- __block_descriptor_tmp.17.1423
- __block_descriptor_tmp.18.1517
- __block_descriptor_tmp.2523
- __block_descriptor_tmp.8.1380
- __block_literal_global.1424
CStrings:
+ "%{public}s: %d: refcount %d for %{public}s at %{public}s:%d"
+ "%{public}s: %p (%{public}s at %{public}s:%d) is not in the history (%d,%d)"
+ "%{public}s: %p: release with refcount 0 for %{public}s at %{public}s:%d"
+ "%{public}s: %{public}s %x%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s"
+ "%{public}s: %{public}s apple flag service on RLOC16 %x %{public}s"
+ "%{public}s: %{public}s/%{private, mask.hash}s: irrelevant event %{public}s in state %{public}s"
+ "%{public}s: called before first logged retain on (%{public}s_t)%p at %{public}s:%d"
+ "%{public}s: memory at %p is not safe"
+ "%{public}s: more files than space"
+ "%{public}s: more types than space"
+ "02:53:58"
+ "<unknown file>"
+ "<unknown type>"
+ "Jun 27 2025"
+ "adv_record"
+ "omr_watcher_cancel"
+ "omr_watcher_release_"
+ "srp_log_ref_check"
+ "srp_log_ref_final"
+ "thread_service_flag_create_"
- "%{public}s: %{public}s %x%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s"
- "%{public}s: %{public}s apple anycast service on RLOC16 %x %{public}s"
- "%{public}s: %{public}s/%{private, mask.hash}s: unexpected event %{public}s in state %{public}s"
- "01:39:10"
- "Jun 14 2025"

```
