## com.apple.telemetry

> `/System/Library/UserEventPlugins/com.apple.telemetry.plugin/com.apple.telemetry`

```diff

-507.0.0.0.0
-  __TEXT.__text: 0x8ab8
-  __TEXT.__auth_stubs: 0x770
+510.0.0.0.0
+  __TEXT.__text: 0x8868
+  __TEXT.__auth_stubs: 0x780
   __TEXT.__objc_stubs: 0x320
-  __TEXT.__const: 0x143
-  __TEXT.__gcc_except_tab: 0x278
+  __TEXT.__const: 0x13b
+  __TEXT.__gcc_except_tab: 0x290
   __TEXT.__cstring: 0x9a5
-  __TEXT.__oslogstring: 0x42fa
+  __TEXT.__oslogstring: 0x4782
   __TEXT.__objc_classname: 0x3
   __TEXT.__objc_methname: 0x202
   __TEXT.__unwind_info: 0x158
-  __DATA.__auth_got: 0x3c8
+  __DATA.__auth_got: 0x3d0
   __DATA.__got: 0xc0
   __DATA.__auth_ptr: 0x8
   __DATA.__const: 0x268

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 387BE179-ADA5-3A9F-9067-11950CAECB44
-  Functions: 150
-  Symbols:   152
+  UUID: 63B6A1C7-C3DA-370E-BDCE-0D7DBA190595
+  Functions: 159
+  Symbols:   153
   CStrings:  301
 
Symbols:
+ _objc_autoreleaseReturnValue
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x20
+ _objc_retain_x23
+ _objc_retain_x24
+ _systemstats_get_microstackshots_buffer_size
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x8
- _objc_storeStrong
CStrings:
+ "%s microstackshot 0x%x samples_recorded:%llu samples_skipped:%llu time:%llu.%0llu"
+ "%s microstackshot 0x%x samples_recorded:%llu samples_skipped:%llu time:%llu.%0llu - duplicate"
+ "Interval adjustment: Memory microstackshots are enabled, not checking daily budget"
+ "Lost %llu (%llu total) microstackshots in this drain between %f-%f (%.9fs)"
+ "Lost %llu microstackshots before this drain between %f-%f (%.9fs)"
+ "Microstackshot datarate did not exceed daily budget with %llu cycle interval: %llu bytes written over the last %llus (%llu uncompressed), cleanup quota %llu, last adjustment %llus ago\ntotal     count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\ninterrupt count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\ntimer     count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nio        count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\npmi       count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nvm_fault  count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\npage_grab count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nmacf      count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nunknown   count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n"
+ "Microstackshot datarate did not exceed daily budget without PMI microstackshots: %llu bytes written over the last %llus (%llu uncompressed), cleanup quota %llu\ntotal     count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\ninterrupt count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\ntimer     count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nio        count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\npmi       count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nvm_fault  count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\npage_grab count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nmacf      count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nunknown   count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n"
+ "Microstackshot datarate exceeded daily budget with %llu cycle interval: %llu bytes written over the last %llus (%llu uncompressed), cleanup quota %llu, last adjustment %llus ago\ntotal     count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\ninterrupt count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\ntimer     count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nio        count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\npmi       count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nvm_fault  count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\npage_grab count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nmacf      count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nunknown   count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n"
+ "Microstackshot datarate exceeded daily budget with %llu cycle interval: %llu bytes written over the last %llus (%llu uncompressed), cleanup quota %llu, last adjustment %llus ago - Ignoring due to PMI interval pref override \ntotal     count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\ninterrupt count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\ntimer     count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nio        count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\npmi       count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nvm_fault  count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\npage_grab count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nmacf      count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nunknown   count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n"
+ "Microstackshot datarate exceeded daily budget without PMI microstackshots: %llu bytes written over the last %llus (%llu uncompressed), cleanup quota %llu\ntotal     count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\ninterrupt count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\ntimer     count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nio        count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\npmi       count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nvm_fault  count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\npage_grab count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nmacf      count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nunknown   count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n"
+ "non-counted %s microstackshot 0x%x @ %llu.%0llu"
+ "non-counted %s microstackshot 0x%x @ %llu.%0llu - known duplicate"
+ "non-counted %s microstackshot 0x%x @ %llu.%0llu - likely duplicate"
- "Lost %llu (%llu total) PMI microstackshots in this drain between %f-%f (%.9fs)"
- "Lost %llu PMI microstackshots before this drain between %f-%f (%.9fs)"
- "Microstackshot datarate did not exceed daily budget with %llu cycle interval: %llu bytes written over the last %llus (%llu uncompressed), cleanup quota %llu, last adjustment %llus ago\ntotal     count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\ninterrupt count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\ntimer     count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nio        count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\npmi       count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nmacf      count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nunknown   count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n"
- "Microstackshot datarate did not exceed daily budget without PMI microstackshots: %llu bytes written over the last %llus (%llu uncompressed), cleanup quota %llu\ntotal     count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\ninterrupt count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\ntimer     count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nio        count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\npmi       count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nmacf      count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nunknown   count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n"
- "Microstackshot datarate exceeded daily budget with %llu cycle interval: %llu bytes written over the last %llus (%llu uncompressed), cleanup quota %llu, last adjustment %llus ago\ntotal     count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\ninterrupt count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\ntimer     count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nio        count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\npmi       count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nmacf      count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nunknown   count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n"
- "Microstackshot datarate exceeded daily budget with %llu cycle interval: %llu bytes written over the last %llus (%llu uncompressed), cleanup quota %llu, last adjustment %llus ago - Ignoring due to PMI interval pref override \ntotal     count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\ninterrupt count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\ntimer     count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nio        count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\npmi       count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nmacf      count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nunknown   count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n"
- "Microstackshot datarate exceeded daily budget without PMI microstackshots: %llu bytes written over the last %llus (%llu uncompressed), cleanup quota %llu\ntotal     count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\ninterrupt count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\ntimer     count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nio        count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\npmi       count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nmacf      count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nunknown   count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n"
- "Not expecting a pmi sample"
- "PMI %s microstackshot generation:%u source:%u period:%llu samples_recorded:%llu samples_skipped:%llu time:%llu.%0llu"
- "PMI %s microstackshot generation:%u source:%u period:%llu samples_recorded:%llu samples_skipped:%llu time:%llu.%0llu - duplicate"
- "non-PMI %s microstackshot 0x%x @ %llu.%0llu"
- "non-PMI %s microstackshot 0x%x @ %llu.%0llu - known duplicate"
- "non-PMI %s microstackshot 0x%x @ %llu.%0llu - likely duplicate"

```
