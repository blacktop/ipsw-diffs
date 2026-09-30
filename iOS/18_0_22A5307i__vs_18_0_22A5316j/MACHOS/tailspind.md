## tailspind

> `/usr/libexec/tailspind`

```diff

-197.0.0.0.0
-  __TEXT.__text: 0xb678
-  __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__objc_stubs: 0x920
-  __TEXT.__objc_methlist: 0xf8
-  __TEXT.__const: 0x134
-  __TEXT.__objc_methname: 0x8fa
-  __TEXT.__oslogstring: 0x2964
-  __TEXT.__cstring: 0x9eb
+199.0.0.0.0
+  __TEXT.__text: 0x9030
+  __TEXT.__auth_stubs: 0xb00
+  __TEXT.__objc_stubs: 0x6e0
+  __TEXT.__objc_methlist: 0x104
+  __TEXT.__const: 0x12c
+  __TEXT.__cstring: 0x873
+  __TEXT.__objc_methname: 0x7a3
+  __TEXT.__oslogstring: 0x1ff1
   __TEXT.__objc_classname: 0x16
-  __TEXT.__objc_methtype: 0xc3
-  __TEXT.__gcc_except_tab: 0x1a4
-  __TEXT.__unwind_info: 0x1e0
-  __DATA_CONST.__auth_got: 0x678
-  __DATA_CONST.__got: 0x1b0
+  __TEXT.__objc_methtype: 0xda
+  __TEXT.__gcc_except_tab: 0x40
+  __TEXT.__unwind_info: 0x198
+  __DATA_CONST.__auth_got: 0x590
+  __DATA_CONST.__got: 0x150
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x3f8
-  __DATA_CONST.__cfstring: 0x500
+  __DATA_CONST.__const: 0x370
+  __DATA_CONST.__cfstring: 0x400
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x160
-  __DATA.__objc_selrefs: 0x2a0
-  __DATA.__objc_ivar: 0x10
+  __DATA.__objc_const: 0x180
+  __DATA.__objc_selrefs: 0x218
+  __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x21e0
+  __DATA.__data: 0x2168
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x490
+  __DATA.__bss: 0x470
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 196
-  Symbols:   269
-  CStrings:  391
+  Functions: 148
+  Symbols:   228
+  CStrings:  314
 
Symbols:
+ _objc_retain_x28
- _OBJC_CLASS_$_NSArray
- _OBJC_CLASS_$_NSSet
- _OBJC_CLASS_$_NSURL
- _OBJC_CLASS_$_NSUUID
- _OBJC_CLASS_$_UNMutableNotificationContent
- _OBJC_CLASS_$_UNNotificationAction
- _OBJC_CLASS_$_UNNotificationCategory
- _OBJC_CLASS_$_UNNotificationRequest
- _OBJC_CLASS_$_UNUserNotificationCenter
- ___NSArray0__struct
- __dispatch_main_q
- __dispatch_source_type_timer
- _close
- _dispatch_activate
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _dispatch_source_cancel
- _dispatch_source_set_timer
- _ffsctl
- _kperf_kdebug_filter_create_desc
- _kperf_kdebug_filter_destroy
- _kperf_sample_set
- _kperf_ticks_to_ns
- _kperf_timer_period_get
- _ktrace_end
- _ktrace_events_all
- _ktrace_events_range
- _ktrace_file_append_live_ariadne_signpost_specs
- _ktrace_file_close
- _ktrace_file_open
- _ktrace_session_destroy
- _ktrace_set_completion_handler
- _ktrace_set_execnames_enabled
- _ktrace_set_file
- _ktrace_set_thread_groups_enabled
- _ktrace_set_vnode_paths_enabled
- _ktrace_start
- _ktrace_start_writing_path
- _stat
- _tailspin_compress_file
- _xpc_dictionary_set_string
CStrings:
+ "!"
+ "%!{(MISSING)public, signpost.description:begin_time}llu %!{(MISSING)public, signpost.description:end_time}llu"
+ "Q24@0:8r*16"
+ "SaveStandardChunks_WithoutPostProcessing"
+ "SaveStandardChunks_WithoutPostProcessing"
+ "_saveStandardChunksStartTimestampMCT"
+ "recordTailspinDurationWithStartMCT:endMCT:"
+ "recordTimeForSaveStandardChunksWithoutPostProcessing:"
+ "v24@0:8Q16"
- "\x11"
- "/var/mobile/Library/Logs/CrashReporter/DiagnosticLogs/PerformanceTraces/"
- "???"
- "Artrace completed but skipping the completion handler as one was not requested"
- "Attempt to add notification request returned error: %!@(MISSING)"
- "Calling artrace Completion Handler"
- "Canceling previous tracing session"
- "Cannot start tracing as pid %!d(MISSING) already owns foreground tracing"
- "Cannot start tracing as tailspind cannot write to the target directory"
- "Cannot start tracing as tailspind failed to configure tracing"
- "Cannot start tracing as tailspind failed to create the ktrace session"
- "Cannot start tracing as tailspind failed to write to the expected output path: %!{(MISSING)errno}d"
- "Compressing artrace"
- "Could not enable sampling: %!{(MISSING)errno}d"
- "Done compressing artrace"
- "Events were lost during tracing. Trace will be unreadable"
- "Failed to compress trace, continuing without compression"
- "Failed to create the tracing session for post-processing"
- "Failed to mark file purgeable: %!{(MISSING)errno}d"
- "Failed to obtain status of trace file for post-processing: %!{(MISSING)errno}d"
- "Failed to open file to mark as purgable: %!{(MISSING)errno}d"
- "Failed to open the trace file to append specs"
- "Failed to open trace file for post-processing: %!{(MISSING)errno}d"
- "Failed to parse trace file for post-processing: %!{(MISSING)errno}d"
- "Killing artrace due to timeout"
- "Kperf timer period could only be set to %!l(MISSING)lu ns"
- "Marked file purgeable"
- "No current tracing exists to stop"
- "Performance Trace"
- "Performance Trace failed to complete."
- "Resetting kperf to clean up tracing"
- "Saved %!@(MISSING)."
- "Successfully completed artrace"
- "Successfully started artrace"
- "Successfully stopped artrace"
- "Timeout occurred but skipping killing artrace due to no current session"
- "URLWithString:"
- "UUID"
- "UUIDString"
- "Unable to add BSD syscalls to kdebug filter: %!{(MISSING)errno}d"
- "Unable to add faults to kdebug filter: %!{(MISSING)errno}d"
- "Unable to add mach syscalls to kdebug filter: %!{(MISSING)errno}d"
- "Unable to create kdebug filter for kperf"
- "Unable to init fault sampling"
- "Unable to init syscall sampling"
- "Unable to retrieve kperf timer period"
- "Unable to set kdebug filter for kperf with description `%!{(MISSING)public}s'"
- "Unable to set kperf action for kdebug events: %!{(MISSING)errno}d"
- "Unable to set kperf timer action"
- "Unable to set kperf timer period to %!l(MISSING)lu ns"
- "Unable to set samplers for kdebug kperf events: %!{(MISSING)errno}d"
- "Unable to set samplers for kperf timer action"
- "UserNotification weak linked and doesn't exist"
- "View"
- "actionWithIdentifier:title:url:options:"
- "addNotificationRequest:withCompletionHandler:"
- "arrayWithObjects:count:"
- "artrace"
- "calculateTailspinDurationFromMCT:endMCT:"
- "categoryWithIdentifier:actions:intentIdentifiers:options:"
- "client %!s(MISSING) [%!d(MISSING)] does not bear entitlement \"%!s(MISSING)\"; refusing TAILSPIN_SET_COMPLETION_HANDLER command"
- "client %!s(MISSING) [%!d(MISSING)] does not bear entitlement \"%!s(MISSING)\"; refusing TAILSPIN_START_ARTRACE command"
- "client %!s(MISSING) [%!d(MISSING)] does not bear entitlement \"%!s(MISSING)\"; refusing TAILSPIN_STOP_ARTRACE command"
- "com.apple.tailspin.notifications"
- "com.apple.tailspin.performancetrace"
- "initWithBundleIdentifier:"
- "lastPathComponent"
- "prefs:root=Privacy&path=PROBLEM_REPORTING/DIAGNOSTIC_USAGE_DATA/"
- "requestWithIdentifier:content:trigger:"
- "setBody:"
- "setCategoryIdentifier:"
- "setDefaultActionURL:"
- "setNotificationCategories:"
- "setThreadIdentifier:"
- "setTitle:"
- "setWithObject:"
- "stringWithCString:encoding:"
- "tailspin artrace start requested by client %!s(MISSING) [%!d(MISSING)]"
- "tailspin artrace stop requested by client %!s(MISSING) [%!d(MISSING)]"
- "tailspin set completion handler requested by client %!s(MISSING) [%!d(MISSING)]"
- "tailspinNotifications"
- "tailspin_path"
- "trace_%!@(MISSING).ktrace"
- "v16@?0@\"NSError\"8"
- "v16@?0^{trace_point=QQQQQQII{timeval=qi}**i}8"
- "viewAction"

```
