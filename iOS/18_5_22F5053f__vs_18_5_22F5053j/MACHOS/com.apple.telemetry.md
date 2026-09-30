## com.apple.telemetry

> `/System/Library/UserEventPlugins/com.apple.telemetry.plugin/com.apple.telemetry`

```diff

-498.100.2.0.0
-  __TEXT.__text: 0x7e18
-  __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_stubs: 0x300
-  __TEXT.__const: 0x150
-  __TEXT.__gcc_except_tab: 0x234
-  __TEXT.__cstring: 0x6e8
-  __TEXT.__oslogstring: 0x39f1
-  __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0x1dd
-  __TEXT.__unwind_info: 0x148
-  __DATA.__auth_got: 0x3a0
-  __DATA.__got: 0xb8
+498.120.2.0.0
+  __TEXT.__text: 0x8804
+  __TEXT.__auth_stubs: 0x780
+  __TEXT.__objc_stubs: 0x320
+  __TEXT.__const: 0x14b
+  __TEXT.__gcc_except_tab: 0x268
+  __TEXT.__cstring: 0x9c5
+  __TEXT.__oslogstring: 0x4043
+  __TEXT.__objc_classname: 0x3
+  __TEXT.__objc_methname: 0x202
+  __TEXT.__unwind_info: 0x158
+  __DATA.__auth_got: 0x3d0
+  __DATA.__got: 0xc0
   __DATA.__auth_ptr: 0x8
-  __DATA.__const: 0x278
-  __DATA.__cfstring: 0x300
+  __DATA.__const: 0x258
+  __DATA.__cfstring: 0x400
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0xc0
+  __DATA.__objc_selrefs: 0xc8
   __DATA.__objc_intobj: 0x18
   __DATA.__data: 0x8
-  __DATA.__bss: 0x78
+  __DATA.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 145
-  Symbols:   146
-  CStrings:  239
+  Functions: 148
+  Symbols:   153
+  CStrings:  265
 
Symbols:
+ _OBJC_CLASS_$_NSDictionary
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _mach_absolute_time
+ _mach_continuous_time
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_release_x28
+ _objc_retain_x28
- _objc_retain_x20
CStrings:
+ " (Overridden by pref)"
+ "Already gathered tailspin for lost samples %.0fs ago"
+ "DR not supported: not gathering tailspin via DR for %@ (%@)\n%@"
+ "Enabling cycle-count-based microstackshots at %llu cycles.%s"
+ "Lost %llu (%llu total) PMI microstackshots in this drain between %f-%f (%.9fs)"
+ "Lost %llu PMI microstackshots before this drain between %f-%f (%.9fs)"
+ "Lost %llu microstackshots before this drain"
+ "Lost %llu microstackshots in this drain"
+ "LostMicrostackshotsBeforeThisDrain"
+ "LostMicrostackshotsInThisDrain"
+ "Microstackshot datarate exceeded daily budget with %llu cycle interval: %llu bytes written over the last %llus (%llu uncompressed), cleanup quota %llu, last adjustment %llus ago - Ignoring due to PMI interval pref override \ntotal     count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\ninterrupt count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\ntimer     count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nio        count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\npmi       count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nmacf      count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n\nunknown   count         %llu\n          size          %llu\n          num_loadinfos %llu\n          num_frames    %llu\n"
+ "NumLostMicrostackshotsBeforeThisDrain"
+ "NumLostMicrostackshotsInThisDrain"
+ "O"
+ "PMI adjustment: Microstackshot pmi interval overridden, not checking daily budget"
+ "PMI telemetry - pmi_interval:%llu time_since_last_adjustment_s:%llus\nnum_pmi_microstackshots_pmi_triggers:%llu\nnum_pmi_microstackshots_skipped:%llu\nnum_pmi_microstackshots_generated:%llu\nnum_pmi_microstackshots_captured:%llu\nnum_pmi_microstackshots_lost_between_drains:%llu\nnum_pmi_microstackshots_lost_inside_drains:%llu\nnum_pmi_microstackshots_captured:%llu\nnum_pmi_microstackshots_not_generated:%llu\nnum_pmi_microstackshots_lost_between_drains_max_at_once:%llu\nnum_pmi_microstackshots_lost_inside_drains_max_at_once:%llu\npmi_configuration_failure:%d\npmi_microstackshots_wrong_source:%d\npmi_microstackshots_wrong_interval:%d\npmi_microstackshots_unexpected_configuration_change:%d\nbad_cpu_time:%d\nbad_samples_recorded:%d\nbad_samples_skipped:%d\nhad_pref_override:%d"
+ "TimeCoveredByDrain"
+ "TimeSinceLastDrain"
+ "com.apple.microstackshots.preferences_changed"
+ "dictionaryWithObjects:forKeys:count:"
+ "had_pref_override"
+ "num_pmi_microstackshots_captured_per10000"
+ "num_pmi_microstackshots_generated"
+ "num_pmi_microstackshots_lost_between_drains"
+ "num_pmi_microstackshots_lost_between_drains_max_at_once"
+ "num_pmi_microstackshots_lost_between_drains_per10000"
+ "num_pmi_microstackshots_lost_inside_drains"
+ "num_pmi_microstackshots_lost_inside_drains_max_at_once"
+ "num_pmi_microstackshots_lost_inside_drains_per10000"
+ "num_pmi_microstackshots_pmi_triggers"
+ "num_pmi_microstackshots_skipped_per10000"
- "Enabling cycle-count-based microstackshots at %llu cycles."
- "Lost %llu PMI microstackshots between %f-%f (%.9fs)"
- "PMI telemetry - pmi_interval:%llu time_since_last_adjustment_s:%llus num_pmi_microstackshots_captured:%llu num_pmi_microstackshots_skipped:%llu num_pmi_microstackshots_not_generated:%llu num_pmi_microstackshots_lost:%llu max_num_pmi_microstackshots_lost_at_once:%llu pmi_configuration_failure:%d pmi_microstackshots_wrong_source:%d pmi_microstackshots_wrong_interval:%d pmi_microstackshots_unexpected_configuration_change:%d bad_cpu_time:%d bad_samples_recorded:%d bad_samples_skipped:%d"
- "max_num_pmi_microstackshots_lost_at_once"
- "num_pmi_microstackshots_lost"

```
