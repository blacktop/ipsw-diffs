## com.apple.telemetry

> `/System/Library/UserEventPlugins/com.apple.telemetry.plugin/com.apple.telemetry`

```diff

-498.120.2.0.0
-  __TEXT.__text: 0x8804
+498.140.3.0.0
+  __TEXT.__text: 0x8b10
   __TEXT.__auth_stubs: 0x780
   __TEXT.__objc_stubs: 0x320
   __TEXT.__const: 0x14b
-  __TEXT.__gcc_except_tab: 0x268
+  __TEXT.__gcc_except_tab: 0x278
   __TEXT.__cstring: 0x9c5
-  __TEXT.__oslogstring: 0x4043
+  __TEXT.__oslogstring: 0x4312
   __TEXT.__objc_classname: 0x3
   __TEXT.__objc_methname: 0x202
-  __TEXT.__unwind_info: 0x158
+  __TEXT.__unwind_info: 0x150
   __DATA.__auth_got: 0x3d0
   __DATA.__got: 0xc0
   __DATA.__auth_ptr: 0x8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 8E3A09DB-03F0-3F70-B019-BD8C15E7FD97
-  Functions: 148
+  UUID: D5BDA384-27CB-30B7-B259-DA15CDA3CC64
+  Functions: 149
   Symbols:   153
-  CStrings:  297
+  CStrings:  301
 
CStrings:
+ "PMI adjustment: Have a pending change to rate %llu->%llu and/or override %d->%d, not checking daily budget"
+ "PMI adjustment: No compressed bytes written since last cleanup (%llu uncompressed), assuming compression ratio of 1.0. time_since_cleanup:%.0fs time_since_adjustment:%.0fs all_bytes_since_cleanup:%llu all_bytes_since_adjustment:%llu pmi_percent:%.0f%% pmi_interval:%llu quota:%llu"
+ "PMI adjustment: projected_pmi_remaining_compressed_bytes_written_in_the_day is 0, resetting to defaults. time_since_cleanup:%.0fs time_since_adjustment:%.0fs all_bytes_since_cleanup:%llu all_bytes_since_adjustment:%llu pmi_percent:%.0f%% pmi_interval:%llu quota:%llu"
+ "pmi_interval_to_equal_nonpmi_datarate:%llu (no non-PMI, so max)"

```
