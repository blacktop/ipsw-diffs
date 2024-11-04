## com.apple.telemetry

> `/System/Library/UserEventPlugins/com.apple.telemetry.plugin/com.apple.telemetry`

```diff

-495.0.0.0.0
-  __TEXT.__text: 0x2b00
-  __TEXT.__auth_stubs: 0x390
-  __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x2ce
-  __TEXT.__oslogstring: 0x2817
-  __TEXT.__unwind_info: 0xb8
-  __DATA.__auth_got: 0x1c8
-  __DATA.__got: 0x38
-  __DATA.__const: 0x1a8
-  __DATA.__bss: 0x10
+498.0.0.0.0
+  __TEXT.__text: 0x6ee0
+  __TEXT.__auth_stubs: 0x440
+  __TEXT.__const: 0x108
+  __TEXT.__cstring: 0x529
+  __TEXT.__oslogstring: 0x3670
+  __TEXT.__unwind_info: 0xe8
+  __DATA.__auth_got: 0x220
+  __DATA.__got: 0x48
+  __DATA.__const: 0x300
+  __DATA.__cfstring: 0x60
+  __DATA.__data: 0x8
+  __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libsystemstats.dylib
-  Functions: 43
-  Symbols:   68
-  CStrings:  59
+  Functions: 101
+  Symbols:   82
+  CStrings:  164
 
Symbols:
+ _CFDataGetBytePtr
+ _CFRelease
+ _IOObjectRelease
+ _IORegistryEntryCreateCFProperty
+ _IORegistryEntryFromPath
+ ___CFConstantStringClassReference
+ __dispatch_source_type_signal
+ _analytics_send_event_lazy
+ _dispatch_activate
+ _dispatch_block_create_with_qos_class
+ _host_statistics64
+ _kCFAllocatorDefault
+ _kIOMainPortDefault
+ _os_log_create
+ _os_release
+ _os_transaction_create
+ _snprintf
+ _xpc_dictionary_set_double
- __os_log_default
- _analytics_send_event
- _sysctlbyname
- _xpc_release
CStrings:
+ "%!s(MISSING)%!s(MISSING)"
+ ". time_since_cleanup:%!f(MISSING)s time_since_adjustment:%!f(MISSING)s all_bytes_since_cleanup:%!l(MISSING)lu all_bytes_since_adjustment:%!l(MISSING)lu pmi_percent:%!f(MISSING)% pmi_interval:%!l(MISSING)lu quota:%!l(MISSING)lu"
+ ":/arm-io/pmgr"
+ "IODeviceTree"
+ "Lost %!l(MISSING)lu PMI microstackshots"
+ "Microstackshot datarate did not exceed daily budget with %!l(MISSING)lu cycle interval: %!l(MISSING)lu bytes written over the last %!l(MISSING)lus (%!l(MISSING)lu uncompressed), cleanup quota %!l(MISSING)lu, last adjustment %!l(MISSING)lus ago\ntotal     count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\ninterrupt count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\ntimer     count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nio        count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\npmi       count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nmacf      count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nunknown   count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n"
+ "Microstackshot datarate did not exceed daily budget without PMI microstackshots: %!l(MISSING)lu bytes written over the last %!l(MISSING)lus (%!l(MISSING)lu uncompressed), cleanup quota %!l(MISSING)lu\ntotal     count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\ninterrupt count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\ntimer     count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nio        count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\npmi       count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nmacf      count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nunknown   count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n"
+ "Microstackshot datarate exceeded daily budget with %!l(MISSING)lu cycle interval: %!l(MISSING)lu bytes written over the last %!l(MISSING)lus (%!l(MISSING)lu uncompressed), cleanup quota %!l(MISSING)lu, last adjustment %!l(MISSING)lus ago\ntotal     count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\ninterrupt count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\ntimer     count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nio        count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\npmi       count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nmacf      count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nunknown   count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n"
+ "Microstackshot datarate exceeded daily budget without PMI microstackshots: %!l(MISSING)lu bytes written over the last %!l(MISSING)lus (%!l(MISSING)lu uncompressed), cleanup quota %!l(MISSING)lu\ntotal     count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\ninterrupt count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\ntimer     count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nio        count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\npmi       count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nmacf      count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nunknown   count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n"
+ "Min cpu %!z(MISSING)u frequency is %!d(MISSING)MHz"
+ "Min cpu frequency for all CPUs is %!d(MISSING)MHz"
+ "Not expecting a pmi sample"
+ "PMI adjustment: Adjusted PMI interval too recently, not checking daily budget. time_since_cleanup:%!f(MISSING)s time_since_adjustment:%!f(MISSING)s all_bytes_since_cleanup:%!l(MISSING)lu all_bytes_since_adjustment:%!l(MISSING)lu pmi_percent:%!f(MISSING)% pmi_interval:%!l(MISSING)lu quota:%!l(MISSING)lu"
+ "PMI adjustment: Already exceeded daily target (%!l(MISSING)lu vs target %!l(MISSING)lu), setting PMI interval to be half of all microstackshot datarate: %!l(MISSING)lu. time_since_cleanup:%!f(MISSING)s time_since_adjustment:%!f(MISSING)s all_bytes_since_cleanup:%!l(MISSING)lu all_bytes_since_adjustment:%!l(MISSING)lu pmi_percent:%!f(MISSING)% pmi_interval:%!l(MISSING)lu quota:%!l(MISSING)lu"
+ "PMI adjustment: Attempting to increase PMI microstackshots interval from %!l(MISSING)lu to %!l(MISSING)lu to fit into daily budget, but already at max interval!. time_since_cleanup:%!f(MISSING)s time_since_adjustment:%!f(MISSING)s all_bytes_since_cleanup:%!l(MISSING)lu all_bytes_since_adjustment:%!l(MISSING)lu pmi_percent:%!f(MISSING)% pmi_interval:%!l(MISSING)lu quota:%!l(MISSING)lu"
+ "PMI adjustment: Calculated new PMI microstackshots interval to fit into daily budget: %!l(MISSING)lu. time_since_cleanup:%!f(MISSING)s time_since_adjustment:%!f(MISSING)s all_bytes_since_cleanup:%!l(MISSING)lu all_bytes_since_adjustment:%!l(MISSING)lu pmi_percent:%!f(MISSING)% pmi_interval:%!l(MISSING)lu quota:%!l(MISSING)lu"
+ "PMI adjustment: Cleanup expected in %!f(MISSING)s, not checking daily budget. time_since_cleanup:%!f(MISSING)s time_since_adjustment:%!f(MISSING)s all_bytes_since_cleanup:%!l(MISSING)lu all_bytes_since_adjustment:%!l(MISSING)lu pmi_percent:%!f(MISSING)% pmi_interval:%!l(MISSING)lu quota:%!l(MISSING)lu"
+ "PMI adjustment: Decreasing PMI microstackshots interval from %!l(MISSING)lu to %!l(MISSING)lu since we have space in the daily budget. time_since_cleanup:%!f(MISSING)s time_since_adjustment:%!f(MISSING)s all_bytes_since_cleanup:%!l(MISSING)lu all_bytes_since_adjustment:%!l(MISSING)lu pmi_percent:%!f(MISSING)% pmi_interval:%!l(MISSING)lu quota:%!l(MISSING)lu"
+ "PMI adjustment: Decreasing desired PMI interval %!l(MISSING)lu to max %!l(MISSING)lu"
+ "PMI adjustment: Increasing PMI microstackshots interval from %!l(MISSING)lu to %!l(MISSING)lu to fit into daily budget. time_since_cleanup:%!f(MISSING)s time_since_adjustment:%!f(MISSING)s all_bytes_since_cleanup:%!l(MISSING)lu all_bytes_since_adjustment:%!l(MISSING)lu pmi_percent:%!f(MISSING)% pmi_interval:%!l(MISSING)lu quota:%!l(MISSING)lu"
+ "PMI adjustment: Increasing desired PMI interval %!l(MISSING)lu to default %!l(MISSING)lu"
+ "PMI adjustment: Microstackshot persistence not allowed, not checking daily budget"
+ "PMI adjustment: Microstackshot pmi disabled, not checking daily budget"
+ "PMI adjustment: No PMI microstackshots since last adjustment (%!l(MISSING)lu bytes of other types), resetting PMI interval to %!l(MISSING)lu. time_since_cleanup:%!f(MISSING)s time_since_adjustment:%!f(MISSING)s all_bytes_since_cleanup:%!l(MISSING)lu all_bytes_since_adjustment:%!l(MISSING)lu pmi_percent:%!f(MISSING)% pmi_interval:%!l(MISSING)lu quota:%!l(MISSING)lu"
+ "PMI adjustment: No PMI microstackshots since last cleanup (%!l(MISSING)lu of other types), resetting PMI interval to %!l(MISSING)lu. time_since_cleanup:%!f(MISSING)s time_since_adjustment:%!f(MISSING)s all_bytes_since_cleanup:%!l(MISSING)lu all_bytes_since_adjustment:%!l(MISSING)lu pmi_percent:%!f(MISSING)% pmi_interval:%!l(MISSING)lu quota:%!l(MISSING)lu"
+ "PMI adjustment: No microstackshots since last adjustment, resetting PMI interval to %!l(MISSING)lu. time_since_cleanup:%!f(MISSING)s time_since_adjustment:%!f(MISSING)s all_bytes_since_cleanup:%!l(MISSING)lu all_bytes_since_adjustment:%!l(MISSING)lu pmi_percent:%!f(MISSING)% pmi_interval:%!l(MISSING)lu quota:%!l(MISSING)lu"
+ "PMI adjustment: No microstackshots since last cleanup, resetting PMI interval to %!l(MISSING)lu. time_since_cleanup:%!f(MISSING)s time_since_adjustment:%!f(MISSING)s all_bytes_since_cleanup:%!l(MISSING)lu all_bytes_since_adjustment:%!l(MISSING)lu pmi_percent:%!f(MISSING)% pmi_interval:%!l(MISSING)lu quota:%!l(MISSING)lu"
+ "PMI adjustment: Non-PMI microstackshots alone are on track exceed half of daily target (%!l(MISSING)lu vs target remaining %!l(MISSING)lu), setting PMI interval to be half of all microstackshot datarate: %!l(MISSING)lu. time_since_cleanup:%!f(MISSING)s time_since_adjustment:%!f(MISSING)s all_bytes_since_cleanup:%!l(MISSING)lu all_bytes_since_adjustment:%!l(MISSING)lu pmi_percent:%!f(MISSING)% pmi_interval:%!l(MISSING)lu quota:%!l(MISSING)lu"
+ "PMI adjustment: Not enough microstackshots to have written to disk yet (%!l(MISSING)lu uncompressed), not checking daily budget"
+ "PMI adjustment: Projected microstackshots data volume (%!l(MISSING)lu) is outside the thresholds our of daily budget (%!l(MISSING)lu), checking if we can adjust the PMI interval. time_since_cleanup:%!f(MISSING)s time_since_adjustment:%!f(MISSING)s all_bytes_since_cleanup:%!l(MISSING)lu all_bytes_since_adjustment:%!l(MISSING)lu pmi_percent:%!f(MISSING)% pmi_interval:%!l(MISSING)lu quota:%!l(MISSING)lu"
+ "PMI adjustment: Projected microstackshots data volume (%!l(MISSING)lu) is within the thresholds our of daily budget (%!l(MISSING)lu), not adjusting the PMI interval. time_since_cleanup:%!f(MISSING)s time_since_adjustment:%!f(MISSING)s all_bytes_since_cleanup:%!l(MISSING)lu all_bytes_since_adjustment:%!l(MISSING)lu pmi_percent:%!f(MISSING)% pmi_interval:%!l(MISSING)lu quota:%!l(MISSING)lu"
+ "PMI adjustment: last pmi adjustment < last cleanup. time_since_cleanup:%!f(MISSING)s time_since_adjustment:%!f(MISSING)s all_bytes_since_cleanup:%!l(MISSING)lu all_bytes_since_adjustment:%!l(MISSING)lu pmi_percent:%!f(MISSING)% pmi_interval:%!l(MISSING)lu quota:%!l(MISSING)lu"
+ "PMI microstackshot count is at least what is expected: %!l(MISSING)lu in last %!f(MISSING)s of cpu time (%!l(MISSING)lu skipped). Expect at least %!l(MISSING)lu given interval %!l(MISSING)lu and minumum cpu cycles per second %!l(MISSING)lu"
+ "PMI microstackshot count is not at least what is expected: %!l(MISSING)lu in last %!f(MISSING)s of cpu time (%!l(MISSING)lu skipped). Expect at least %!l(MISSING)lu given interval %!l(MISSING)lu and minumum cpu cycles per second %!l(MISSING)lu"
+ "PMI microstackshot generation:%!u(MISSING) source:%!u(MISSING) period:%!l(MISSING)lu samples_recorded:%!l(MISSING)lu samples_skipped:%!l(MISSING)lu"
+ "PMI microstackshot generation:%!u(MISSING) source:%!u(MISSING) period:%!l(MISSING)lu samples_recorded:%!l(MISSING)lu samples_skipped:%!l(MISSING)lu - duplicate"
+ "PMI microstackshots not enabled"
+ "PMI telemetry - pmi_interval:%!l(MISSING)lu time_since_last_adjustment_s:%!l(MISSING)lus num_pmi_microstackshots_captured:%!l(MISSING)lu num_pmi_microstackshots_skipped:%!l(MISSING)lu num_pmi_microstackshots_not_generated:%!l(MISSING)lu num_pmi_microstackshots_lost:%!l(MISSING)lu max_num_pmi_microstackshots_lost_at_once:%!l(MISSING)lu pmi_configuration_failure:%!d(MISSING) pmi_microstackshots_wrong_source:%!d(MISSING) pmi_microstackshots_wrong_interval:%!d(MISSING) pmi_microstackshots_unexpected_configuration_change:%!d(MISSING) bad_cpu_time:%!d(MISSING) bad_samples_recorded:%!d(MISSING) bad_samples_skipped:%!d(MISSING)"
+ "Quota telemetry - exceeded_quota:%!d(MISSING) quota:%!l(MISSING)lu bytes_written:%!l(MISSING)lu time_since_last_cleanup_s:%!l(MISSING)lus ratio_pmi:%!f(MISSING) num_interval_increases:%!l(MISSING)lu num_interval_decreases:%!l(MISSING)lu ending_pmi_interval:%!l(MISSING)lu default_pmi_interval:%!l(MISSING)lu time_since_last_adjustment_s:%!l(MISSING)lus"
+ "Saved %!z(MISSING)u microstackshots (ignored %!d(MISSING) known duplicates and %!d(MISSING) likely duplicates)"
+ "Unable to determine min cpu %!z(MISSING)u frequency (3)"
+ "Unable to determine min cpu %!z(MISSING)u frequency (4)"
+ "Unable to determine min cpu frequency (1), assuming 600MHz"
+ "Unable to determine min cpu frequency (2), assuming 600MHz"
+ "Unable to determine min cpu frequency (5), assuming 600MHz"
+ "Unable to get system cpu time: %!d(MISSING)"
+ "Wrong microstackshot interval %!l(MISSING)lu, should be %!l(MISSING)lu"
+ "Wrong microstackshot source %!d(MISSING)"
+ "^v8@?0"
+ "__telemetry off returned error: %!{(MISSING)errno}d"
+ "all_compressed_bytes_written_per_second_since_last_adjustment:%!f(MISSING)"
+ "all_compressed_bytes_written_since_last_adjustment:%!l(MISSING)lu"
+ "all_uncompressed_bytes_written_since_last_adjustment:%!l(MISSING)lu"
+ "all_uncompressed_bytes_written_since_last_cleanup:%!l(MISSING)lu"
+ "bad_cpu_time"
+ "bad_samples_recorded"
+ "bad_samples_skipped"
+ "checking for missing microstackhots"
+ "com.apple.microstackshots.pmiStats"
+ "com.apple.systemstats"
+ "compression_ratio:%!f(MISSING)"
+ "current_host_cpu_time_ns:%!l(MISSING)lu"
+ "current_pmi_samples_recorded:%!l(MISSING)lu"
+ "current_pmi_samples_skipped:%!l(MISSING)lu"
+ "delta_host_cpu_time_ns:%!l(MISSING)lu"
+ "delta_pmi_samples_recorded:%!l(MISSING)lu"
+ "delta_pmi_samples_skipped:%!l(MISSING)lu"
+ "drain_kernel_microstackshot_buffer called without persistence active, ignoring"
+ "drain_kernel_microstackshot_buffer should coalesce, ignoring"
+ "failed to allocate xpc dict for com.apple.microstackshots.diskQuota"
+ "failed to allocate xpc dict for com.apple.microstackshots.pmiStats"
+ "generation incremented unexpectedly %!u(MISSING) -> %!u(MISSING), and settings are wrong! source:%!d(MISSING) period:%!l(MISSING)lu, should be %!l(MISSING)lu"
+ "generation incremented unexpectedly %!u(MISSING) -> %!u(MISSING), but settings are correct"
+ "host_cpu_time_ns went backwards %!l(MISSING)lu -> %!l(MISSING)lu"
+ "internal_calculations"
+ "last_check_host_cpu_time_ns cleared"
+ "last_check_host_cpu_time_ns:%!l(MISSING)lu"
+ "last_check_pmi_samples_recorded:%!l(MISSING)lu"
+ "last_check_pmi_samples_skipped:%!l(MISSING)lu"
+ "max_num_pmi_microstackshots_lost_at_once"
+ "min_delta_host_cpu_cycles:%!l(MISSING)lu"
+ "min_num_pmi_microstackshots_expected (adjusted):%!l(MISSING)lu"
+ "min_num_pmi_microstackshots_expected:%!l(MISSING)lu"
+ "non-PMI microstackshot 0x%!x(MISSING) @ %!l(MISSING)lu.%!l(MISSING)lu"
+ "non-PMI microstackshot 0x%!x(MISSING) @ %!l(MISSING)lu.%!l(MISSING)lu - known duplicate"
+ "non-PMI microstackshot 0x%!x(MISSING) @ %!l(MISSING)lu.%!l(MISSING)lu - likely duplicate"
+ "nonpmi_uncompressed_bytes_written_since_last_adjustment:%!l(MISSING)lu"
+ "num_interval_decreases"
+ "num_interval_increases"
+ "num_pmi_microstackshots_captured"
+ "num_pmi_microstackshots_lost"
+ "num_pmi_microstackshots_not_generated"
+ "num_pmi_microstackshots_skipped"
+ "num_pmi_microstackshots_this_check:%!l(MISSING)lu"
+ "pending microstackshots"
+ "pmi_configuration_failure"
+ "pmi_interval"
+ "pmi_interval_to_equal_nonpmi_datarate:%!l(MISSING)lu"
+ "pmi_microstackshots_unexpected_configuration_change"
+ "pmi_microstackshots_wrong_interval"
+ "pmi_microstackshots_wrong_source"
+ "pmi_samples_recorded went backwards %!l(MISSING)lu -> %!l(MISSING)lu"
+ "pmi_samples_skipped went backwards %!l(MISSING)lu -> %!l(MISSING)lu"
+ "pmi_uncompressed_bytes_written_since_last_adjustment:%!l(MISSING)lu"
+ "pmi_uncompressed_bytes_written_since_last_cleanup:%!l(MISSING)lu"
+ "projected_all_compressed_bytes_written_in_the_day:%!l(MISSING)lu"
+ "projected_nonpmi_remaining_compressed_bytes_written_in_the_day:%!l(MISSING)lu"
+ "projected_pmi_remaining_compressed_bytes_written_in_the_day:%!l(MISSING)lu"
+ "projected_remaining_all_compressed_bytes_written_in_the_day:%!l(MISSING)lu"
+ "ratio_of_nonpmi_vs_all_since_last_adjustment:%!f(MISSING)"
+ "ratio_of_pmi_vs_all_since_last_adjustment:%!f(MISSING)"
+ "ratio_of_target_pmi_vs_current_pmi:%!f(MISSING)"
+ "ratio_pmi"
+ "ratio_pmi_vs_nonpmi_since_last_adjustment:%!f(MISSING)"
+ "target_all_compressed_bytes:%!l(MISSING)lu target_ratio:%!f(MISSING)"
+ "target_pmi_remaining_compressed_bytes_written_in_the_day:%!l(MISSING)lu"
+ "target_remaining_all_compressed_bytes_written_in_the_day:%!l(MISSING)lu"
+ "target_remaining_all_uncompressed_bytes_written_in_the_day:%!l(MISSING)lu"
+ "telemetry_plugin"
+ "time_remaining_in_the_day_s:%!f(MISSING)"
+ "time_since_last_adjustment"
+ "voltage-states1"
+ "voltage-states13"
+ "voltage-states5"
- "Microstackshot PMI volume on track to exceed daily budget with %!l(MISSING)lu cycle interval: %!l(MISSING)lu bytes written over the last %!f(MISSING)s, cleanup quota %!l(MISSING)u. Doubling interval to %!l(MISSING)lu\ntotal     count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\ninterrupt count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\ntimer     count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nio        count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\npmi       count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nmacf      count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nunknown   count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n%!l(MISSING)lu drains (%!l(MISSING)lu duplicate)"
- "Microstackshot PMI volume on track to exceed daily budget with %!l(MISSING)lu cycle interval: %!l(MISSING)lu bytes written over the last %!f(MISSING)s, cleanup quota %!l(MISSING)u. Too soon since last cleanup, maintaining current interval\ntotal     count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\ninterrupt count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\ntimer     count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nio        count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\npmi       count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nmacf      count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nunknown   count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n%!l(MISSING)lu drains (%!l(MISSING)lu duplicate)"
- "Microstackshot PMI volume on track to exceed daily budget with max %!l(MISSING)lu cycle interval, unable to reduce rate! %!l(MISSING)lu bytes written over the last %!f(MISSING)s, cleanup quota %!l(MISSING)u\ntotal     count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\ninterrupt count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\ntimer     count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nio        count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\npmi       count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nmacf      count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nunknown   count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n%!l(MISSING)lu drains (%!l(MISSING)lu duplicate)"
- "Microstackshot cleanup time moved backwards from %!l(MISSING)lu to %!l(MISSING)lu"
- "Microstackshot persistence not allowed, not checking daily budget"
- "Microstackshot pmi disabled, not checking daily budget"
- "Microstackshot total volume is not on track to exceed daily budget with %!l(MISSING)lu cycle interval: %!l(MISSING)lu bytes written over the last %!f(MISSING)s, cleanup quota %!l(MISSING)u\ntotal     count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\ninterrupt count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\ntimer     count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nio        count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\npmi       count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nmacf      count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nunknown   count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n%!l(MISSING)lu drains (%!l(MISSING)lu duplicate)"
- "Microstackshot total volume on track to exceed daily budget, but PMI with %!l(MISSING)lu cycle interval is not: %!l(MISSING)lu bytes written over the last %!f(MISSING)s, cleanup quota %!l(MISSING)u\ntotal     count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\ninterrupt count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\ntimer     count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nio        count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\npmi       count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nmacf      count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nunknown   count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n%!l(MISSING)lu drains (%!l(MISSING)lu duplicate)"
- "Microstackshot volume did not exceed daily budget with %!l(MISSING)lu cycle interval: %!l(MISSING)lu bytes written over the last %!f(MISSING)s, cleanup quota %!l(MISSING)u\ntotal     count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\ninterrupt count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\ntimer     count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nio        count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\npmi       count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nmacf      count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nunknown   count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n%!l(MISSING)lu drains (%!l(MISSING)lu duplicate)"
- "Microstackshot volume did not exceed daily budget with interrupt microstackshots at %!u(MISSING) rate: %!l(MISSING)lu bytes written over the last %!f(MISSING)s, cleanup quota %!l(MISSING)u\ntotal     count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\ninterrupt count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\ntimer     count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nio        count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\npmi       count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nmacf      count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nunknown   count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n%!l(MISSING)lu drains (%!l(MISSING)lu duplicate)"
- "Microstackshot volume exceeded daily budget with %!l(MISSING)lu cycle interval: %!l(MISSING)lu bytes written over the last %!f(MISSING)s, cleanup quota %!l(MISSING)u\ntotal     count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\ninterrupt count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\ntimer     count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nio        count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\npmi       count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nmacf      count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nunknown   count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n%!l(MISSING)lu drains (%!l(MISSING)lu duplicate)"
- "Microstackshot volume exceeded daily budget with interrupt microstackshots at %!u(MISSING) rate: %!l(MISSING)lu bytes written over the last %!f(MISSING)s, cleanup quota %!l(MISSING)u\ntotal     count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\ninterrupt count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\ntimer     count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nio        count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\npmi       count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nmacf      count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n\nunknown   count         %!l(MISSING)lu\n          size          %!l(MISSING)lu\n          num_loadinfos %!l(MISSING)lu\n          num_frames    %!l(MISSING)lu\n%!l(MISSING)lu drains (%!l(MISSING)lu duplicate)"
- "Saved %!z(MISSING)u microstackshots"
- "drain_kernel_microstackshot_buffer called with immediate == %!d(MISSING)"
- "drain_kernel_microstackshot_buffer detected that the kernel buffer hasn't accumulated new samples."
- "failed to allocate for %!s(MISSING) event"
- "interrupt"
- "interrupt_sample_rate"
- "kern.microstackshot.interrupt_sample_rate"

```
