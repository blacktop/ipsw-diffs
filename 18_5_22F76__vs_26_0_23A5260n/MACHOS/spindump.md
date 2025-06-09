## spindump

> `/usr/sbin/spindump`

```diff

-383.14.0.0.0
-  __TEXT.__text: 0x96a14
-  __TEXT.__auth_stubs: 0x11e0
-  __TEXT.__objc_stubs: 0x3f20
+404.0.0.0.0
+  __TEXT.__text: 0xbd1e8
+  __TEXT.__auth_stubs: 0x12d0
+  __TEXT.__objc_stubs: 0x40a0
   __TEXT.__objc_methlist: 0x9f4
-  __TEXT.__const: 0x230
-  __TEXT.__cstring: 0x129d5
-  __TEXT.__oslogstring: 0x21a77
-  __TEXT.__objc_classname: 0xe5
-  __TEXT.__gcc_except_tab: 0x1dd0
-  __TEXT.__objc_methname: 0x4105
-  __TEXT.__objc_methtype: 0x52d
-  __TEXT.__unwind_info: 0xc90
-  __DATA_CONST.__auth_got: 0x900
+  __TEXT.__const: 0x240
+  __TEXT.__cstring: 0x140c7
+  __TEXT.__oslogstring: 0x24b16
+  __TEXT.__objc_classname: 0x105
+  __TEXT.__gcc_except_tab: 0x32f4
+  __TEXT.__objc_methname: 0x41b5
+  __TEXT.__objc_methtype: 0x530
+  __TEXT.__unwind_info: 0xdd8
+  __DATA_CONST.__auth_got: 0x978
   __DATA_CONST.__got: 0x218
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x13a8
-  __DATA_CONST.__cfstring: 0x8a00
+  __DATA_CONST.__const: 0x14b0
+  __DATA_CONST.__cfstring: 0x9720
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__objc_intobj: 0x90
+  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x1d68
-  __DATA.__objc_selrefs: 0x1120
+  __DATA.__objc_selrefs: 0x1180
   __DATA.__objc_ivar: 0x214
   __DATA.__objc_data: 0x410
   __DATA.__data: 0x20
-  __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x7e8
-  __DATA.__common: 0x70
+  __DATA.__crash_info: 0x148
+  __DATA.__bss: 0x800
+  __DATA.__common: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 195AC92B-1DBA-3873-8CA9-7B033ABD6497
-  Functions: 1602
-  Symbols:   364
-  CStrings:  5360
+  UUID: 9FB0BC41-00D6-31D0-A4CA-C934F8FF18D3
+  Functions: 1738
+  Symbols:   379
+  CStrings:  5767
 
Symbols:
+ _CSIsNull
+ _CSSymbolOwnerGetCFUUIDBytes
+ _CSSymbolicatorForeachSymbolicatorWithPathFlagsAndNotification
+ _CSSymbolicatorGetSymbolOwner
+ ___snprintf_chk
+ _objc_autoreleaseReturnValue
+ _objc_claimAutoreleasedReturnValue
+ _objc_copyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_release_x10
+ _objc_release_x2
+ _objc_release_x9
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retainAutoreleasedReturnValue
+ _objc_retainBlock
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x8
+ _objc_storeStrong
+ _objc_unsafeClaimAutoreleasedReturnValue
- __Block_copy
- __Block_object_assign
- __Block_release
- _dispatch_release
- _dispatch_retain
- _objc_loadWeak
- _objc_retain_x7
- _os_unfair_lock_lock
- _os_unfair_lock_unlock
- _xpc_release
- _xpc_retain
CStrings:
+ "\n%s [%d] output exceeded %llu bytes, truncating"
+ "\n%s [%d] timed out after %llus, truncating"
+ "\nGenerating memgraph for %s [%d]\nleaks --outputGraph=/var/tmp/ %d\n"
+ "\nddt output for %s [%d]\nddt %d\n"
+ "\nheap output for %s [%d]\nheap --addresses=.*transaction.* --forkCorpseRetryTime=0 %d\n"
+ "\nusage: spindump [<pid/partial name> [duration [interval]]] <options>\n\n   Spindump gathers user and kernel callstacks for every process.\n\n   pid/partial name\n                The target process (sorted topmost in the output file).\n                \"-noTarget\" may be specified instead to avoid providing\n                a target process when duration is provided.\n   duration     The duration of the sampling in seconds. Default 10.\n   interval     The number of miliseconds between samples. Default 10.\n\n   Giving spindump no parameters will use no target with the default\n   duration and interval.\n\n  Extra options:\n   -i <path>    Read in the file at <path> and generate a spindump report.\n                Spindump reports can be regenerated with different display\n                options\n   -o <path>    Specifies where to write results. If <path> is a directory,\n                the output file will be put inside that directory with a\n                default name, without overwriting any existing file.\n                By default, the output file is put in /tmp/\n\n   -startTime <date>\n                Omit samples before the given wall time specified as a string\n                of the format \"YYYY-MM-DD HH:MM:SS\" with optional decimal\n                seconds and time zone, or with a unix timestamp in seconds\n   -endTime <date>\n                Omit samples after the given wall time specified as a string\n                of the format \"YYYY-MM-DD HH:MM:SS\" with optional decimal\n                seconds and time zone, or with a unix timestamp in seconds\n\n   -startMachAbsTimeNs <mach_abs_time_ns>\n                Omit samples before the given mach abs time (in nanoseconds)\n   -endMachAbsTimeNs <mach_abs_time_ns>\n                Omit samples after the given mach abs time (in nanoseconds)\n   -machAbsTimeRangeNs <mach_abs_time_ns>-<mach_abs_time_ns>\n                Only include samples in the given mach abs time range (in nanoseconds)\n\n   -startMachAbsTime <mach_abs_time>\n                Omit samples before the given mach abs time (in mach time units)\n   -endMachAbsTime <mach_abs_time>\n                Omit samples after the given mach abs time (in mach time units)\n   -machAbsTimeRange <mach_abs_time>-<mach_abs_time>\n                Only include samples in the given mach abs time range\n\n   -indexRange <int>-<int>\n                Only include samples in the given range\n   -startIndex <int>\n                Omit samples before sample number <int>\n   -endIndex <int>\n                Omit samples after sample number <int>\n\n   -last <int>[m|h|d|samples]\n                Only include data from the the last <int> seconds of the data being\n                parsed. Only valid when not sampling the live system. Use \"m\", \"h,\n                \"d\", or \"samples\" to instead specify minutes, hours, days, or number\n                of samples\n\n   -filterToEventTimeRange\n                When parsing a raw input file, automatically filter the report to\n                the time range of the event found in the data\n\n   -heavy       Sort callstacks by count (default)\n   -timeline    Sort callstacks chronologically\n\n   -sortProcessesBy <attribute>\n                Sort processes by the given attribute. This option may be provided\n                multiple times to provide sub-orderings.\n                Valid attributes are \"Name\", \"ID\", \"HighestBasePriority\",\n                \"HighestScheduledPriority\", \"LargestFootprint\", \"CpuTime\",\n                \"InstructionsRetired\", \"Cycles\", \"CyclesPerInstruction\",\n                \"KernelLast\", \"SampleCount\", \"ExecTimestamp\".\n                Any of those attribute strings can be prepended with \"Reverse\" to\n                reverse the default sort order, i.e. \"ReverseName\". The target\n                process will always be first in the report.\n\n   -sortCallTreesBy <attribute>\n                Sort call trees by the given attribute. This option may be provided\n                multiple times to provide sub-orderings.\n                Valid attributes are \"MainThreadFirst\", \"SampleCount\", \"DispatchQueue\",\n                \"Thread\", \"HighestBasePriority\", \"HighestScheduledPriority\",\n                \"CpuTime\", \"InstructionsRetired\", \"Cycles\", \"CyclesPerInstruction\".\n                Any of those attribute strings can be prepended with \"Reverse\" to\n                reverse the default sort order, i.e. \"ReverseSampleCount\". The target\n                thread will always be first in the report.\n\n   -timestampsInCallTrees <time_domain>\n                Print timestamps/ranges for each leaf frame in the call tree.\n                Valid options are \"wall\", \"machabs\", \"machabssec\", \"machcont\",\n                and  \"machcontsec\". May be specified multiple times to print multiple\n                time domains. \"all\" may be used to print all available time domains\n\n   -noText      Omit textual format (include binary format only)\n   -noBinary    Omit binary format (include text format only)\n   -noFile      Do not output to a file (the report, including binary format,\n                will go to stdout instead)\n   -stdout      Print the report to stdout\n   -json        Print the report in json format\n\n   -siginfo     After sampling, wait for SIGINFO before reporting\n   -timelimit <t>\n                Exit after t seconds even if the report hasn't been saved\n\n   -delayonsignal <t>\n                Stop sampling t seconds after receiving a signal instead of\n                stopping immediately\n   -wait        Wait for the process to exist before sampling. If the\n                process already exists, spindump will begin sampling\n                immediately.\n\n   -displayIdleWorkQueueThreads\n                Display idle work queue threads\n   -verbose     Verbose report output\n\n   -noThrottle  Do not throttle sampling rate on excessive memory growth\n   -noProcessingWhileSampling\n                Do not parse stackshots until done sampling\n\n   -inspectLiveSystem\n                When parsing an input file, assume the data was gathered on\n                the current live system (so spindump can inspect processes if\n                necessary to get symbol information)\n   -symbols <path>\n                Read in symbol data at contained in the file at <path>\n   -dscSymDir <path>\n                The path to dscsym directory containing shared cache layout\n                files (for use when parsing input files gathered on a different\n                machine)\n   -dsym <path> Path to a dsym to use during symbolication (may be specified\n                multiple times)\n\n   -noRunnable  Omit callstacks when threads are runnable (but not running)\n   -noRunning   Omit callstacks when threads are running\n   -noBlocked   Omit callstacks when threads are blocked\n   -sampleWithoutTarget\n                Sample for entire duration even if target exits or doesn't exist\n   -onlyTarget  Only sample the target process (allows faster sampling,\n                use 'u' to specify interval in microseconds: e.g. 500u)\n      -proc <pid/partial name>\n                When specifying -onlyTarget, sample the specified process\n                in addition to the target process (may be passed multiple times)\n   -targetThreadID <tid>\n                Target the provided thread ID (sort topmost)\n   -symbolicate (default with -i) Symbolicate the report from information on the\n                current system\n   -noSymbolicate (default without -i) Do not symbolicate the report.\n                UUID+offset information will still be gathered for later\n                symbolication\n   -noBulkSymbolication\n                Don't attempt to use BulkSymbolication\n   -aggregateCallTreesByDispatchQueue\n                Group call trees by dispatch queue\n   -aggregateCallTreesByThread\n                Group call trees by thread\n   -aggregateCallTreesByProcess\n                Group call trees by process\n\n   -aggregateSwiftAsyncTogetherWithOtherCallTrees\n                Don't aggregate swift async callstacks separately from other\n                callstacks\n   -aggregateSwiftAsyncCallTreesByBaseFunction\n                Aggregate swift async callstacks into call trees by the base\n                function (the function initially started by the swift Task)\n   -aggregateSwiftAsyncCallTreesBySwiftTask\n                Aggregate swift async callstacks into call trees by swift task\n   -aggregateSwiftAsyncCallTreesByThread\n                Aggregate swift async callstacks into call trees by thread\n   -aggregateSwiftAsyncCallTreesByProcess\n                Aggregate swift async callstacks into call trees by process\n                (each process will have one swift async call tree\n   -swiftAsyncDisplayCRootCallstacks\n                Display the C root callstacks replaced swift async callstacks\n   -swiftAsyncPrintLeafyCCallstackOnTopOfSwiftAsyncCallstacksAlways\n                Display the leafy C callstack on top of the swift async frames\n                even when run on the main thread\n   -swiftAsyncPrintLeafyCCallstackOnTopOfCRootCallstacksAlways\n                Always display the entire C callstack together. Swift async\n                callstacks will be in a separate call tree without the leafy C\n                callstack\n\n   -aggregateProcessesByInstance\n                Aggregate processes by instance\n   -aggregateProcessesByExecutable\n                Aggregate processes by executable\n   -aggregateProcessesByExecutableAndResourceCoalition\n                Aggregate processes by both executable and resource coalition\n\n   -omitFramesBelowSampleCount <int>\n                Omit callstack frames with count less than <int>\n   -stackshotsOnly\n                Only parse the stackshots from a ktrace file, no kperf\n   -parsePastLastStackshot\n                Parse lightweight PET ktrace data past the last stackshot\n   -noIPC       Do not IPC out to any daemons (more expensive, but more reliable)\n   -reason <string>\n                An optional string to describe why spindump is being invoked\n   -automation\n                Indicate that spindump is running via automation, so it should\n                prefer to avoid impacting system performance (e.g. avoid audio\n                pops)\n   -noExclaves  Disable gathering of exclave information\n\n\n   Micro-stackshots\n     Microstackshots can be obtained from the live system (the default), or\n     from raw microstackshot files/untethered trace files via -i <path>.\n   -microstackshots\n                Report CPU microstackshots.\n   -microstackshots_io\n                Report I/O microstackshots.\n   -microstackshots_datastore <path>\n                Path to microstackshot datastore on disk.\n                If specified without microstackshots_save,\n                read from saved microstackshot data at <path>\n                instead of pulling data from this machine.\n   -microstackshots_save\n                Save microstackshots to the path specified by\n                microstackshots_datastore instead of reporting.\n   -microstackshots_starttime <date>\n                Start time for microstackshot data in a parseable date\n                string such as \"11/14/12 12:00am\" or a unix timestamp\n                as an integer. Default is to use data from as far back as\n                available. (Use -h after to echo the date parsed)\n   -microstackshots_endtime <date>\n                End time for microstackshot data in a parseable date\n                string such as \"11/14/12 12:00am\" or a unix timestamp\n                as an integer. Default is to use data up to as recent as\n                available. (Use -h after to echo the date parsed)\n   -microstackshots_pid <pid>\n                Only report on the given process. Default is all processes.\n   -microstackshots_threadid <thread_id>\n                Only report on the given thread. Default is all threads.\n   -microstackshots_dsc_path <path>\n                Path to a directory containing dyld shared cache information.\n                Default is to historical information for the local machine.\n   -threadpriority_min <int>\n                Filter out any thread samples that have a priority below the\n                given threshold.\n   -threadpriority_max <int>\n                Filter out any thread samples that have a priority above the\n                given threshold.\n   -batteryonly\n                Filter out any stacks from when the machine was on AC\n   -aconly\n                Filter out any stacks from when the machine was on battery\n   -useridleonly\n                Filter out any stacks from when the user was active\n   -useractiveonly\n                Filter out any stacks from when the user was idle\n   -arch        Machine architecture (i.e. \"arm64e\")\n   -hwPageSize <int>\n                Hardware page size in bytes\n   -vmPageSize <int>\n                VM page size in bytes\n   -machTimebase <int>/<int>\n                Mach timebase (numer/denom)\n"
+ "!"
+ "%@ [%d]: %s: being debugged"
+ "%@ [%d]: Absolute path required, have %@"
+ "%@ [%d]: MetricKit unavailable, not providing cpu usage report"
+ "%@ [%d]: MetricKit unavailable, not providing disk writes report"
+ "%@ [%d]: Most common UUID with %u samples: %@"
+ "%@ [%d]: No UUID for symbol owner"
+ "%@ [%d]: No microstackshots found"
+ "%@ [%d]: No microstackshots with provided UUIDs %@"
+ "%@ [%d]: No symbol owner for symbolicator"
+ "%@ [%d]: Not providing unsupported report type (%d) to MetricKit"
+ "%@ [%d]: Possible UUIDs: %@"
+ "%@ [%d]: Providing cpu usage report to MetricKit"
+ "%@ [%d]: Providing disk writes report to MetricKit"
+ "%@ [%d]: Unable to determine UUID at path %@"
+ "%@ [%d]: could not fdopen log file %@: %d (%s)"
+ "%@ [%d]: could not open log file %@: %d (%s)"
+ "%@ [%d]: could not write to file %@: %d (%s)"
+ "%@ deferred power exception: generating deferred report"
+ "%@: Absolute path required, have %@"
+ "%@: MetricKit unavailable, not providing cpu usage report"
+ "%@: MetricKit unavailable, not providing disk writes report"
+ "%@: Most common UUID with %u samples: %@"
+ "%@: No UUID for symbol owner"
+ "%@: No microstackshots found"
+ "%@: No microstackshots with provided UUIDs %@"
+ "%@: No symbol owner for symbolicator"
+ "%@: Not providing unsupported report type (%d) to MetricKit"
+ "%@: Possible UUIDs: %@"
+ "%@: Providing cpu usage report to MetricKit"
+ "%@: Providing disk writes report to MetricKit"
+ "%@: Unable to determine UUID at path %@"
+ "%@: could not fdopen log file %@: %d (%s)"
+ "%@: could not open log file %@: %d (%s)"
+ "%@: could not write to file %@: %d (%s)"
+ "%@: power exception: all microstackshots without errors: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
+ "%@: power exception: cannot defer report generation for game mode"
+ "%@: power exception: deferring report generation due to game mode"
+ "%@: power exception: done reporting (%#llx)"
+ "%@: power exception: no microstackshots: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
+ "%@: power exception: not monitoring due to conditions %#llx"
+ "%@: power exception: not monitoring due to suppression cookie file"
+ "%@: power exception: not monitoring due to throttling the number of reports generated for 1st party processes"
+ "%@: power exception: over the last %.0f seconds (%.0f reported) with issue type \"%@\", mitigation reason \"%@\", action taken \"%@\", detector \"%@\", flags %#llx"
+ "%@: power exception: some microstackshots with errors: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
+ "%s [%d]: Absolute path required, have %@"
+ "%s [%d]: Most common UUID with %u samples: %@"
+ "%s [%d]: No UUID for symbol owner"
+ "%s [%d]: No ddt output for resource exhaustion report"
+ "%s [%d]: No lsof output for resource exhaustion report"
+ "%s [%d]: No microstackshots with provided UUIDs %@"
+ "%s [%d]: No output from leaks for %d"
+ "%s [%d]: No symbol owner for symbolicator"
+ "%s [%d]: Possible UUIDs: %@"
+ "%s [%d]: Unable to determine UUID at path %@"
+ "%s [%d]: Unable to spawn leaks: %d (%s)"
+ "%s [%d]: overridden by [%d]"
+ "%s: %s: Bad report type %d"
+ "%s: %s: Bad report type for microstackshots %d"
+ "%s: %s: No matching timestamps provided: %llu-%llu, %llu-%llu, %.2f-%.2f"
+ "%s: %s: report_type %d, but systemstatsFormat %d"
+ "%{public}@ [%d]: %{public}s: being debugged"
+ "%{public}@ [%d]: Absolute path required, have %@"
+ "%{public}@ [%d]: MetricKit unavailable, not providing cpu usage report"
+ "%{public}@ [%d]: MetricKit unavailable, not providing disk writes report"
+ "%{public}@ [%d]: Most common UUID with %u samples: %@"
+ "%{public}@ [%d]: No UUID for symbol owner"
+ "%{public}@ [%d]: No microstackshots found"
+ "%{public}@ [%d]: No microstackshots with provided UUIDs %@"
+ "%{public}@ [%d]: No symbol owner for symbolicator"
+ "%{public}@ [%d]: Not providing unsupported report type (%d) to MetricKit"
+ "%{public}@ [%d]: Possible UUIDs: %@"
+ "%{public}@ [%d]: Providing cpu usage report to MetricKit"
+ "%{public}@ [%d]: Providing disk writes report to MetricKit"
+ "%{public}@ [%d]: Unable to determine UUID at path %@"
+ "%{public}@ [%d]: could not fdopen log file %@: %d (%s)"
+ "%{public}@ [%d]: could not open log file %@: %d (%s)"
+ "%{public}@ [%d]: could not write to file %@: %d (%s)"
+ "%{public}@ deferred power exception: generating deferred report"
+ "%{public}@: Absolute path required, have %@"
+ "%{public}@: MetricKit unavailable, not providing cpu usage report"
+ "%{public}@: MetricKit unavailable, not providing disk writes report"
+ "%{public}@: Most common UUID with %u samples: %@"
+ "%{public}@: No UUID for symbol owner"
+ "%{public}@: No microstackshots found"
+ "%{public}@: No microstackshots with provided UUIDs %@"
+ "%{public}@: No symbol owner for symbolicator"
+ "%{public}@: Not providing unsupported report type (%d) to MetricKit"
+ "%{public}@: Possible UUIDs: %@"
+ "%{public}@: Providing cpu usage report to MetricKit"
+ "%{public}@: Providing disk writes report to MetricKit"
+ "%{public}@: Unable to determine UUID at path %@"
+ "%{public}@: could not fdopen log file %@: %d (%s)"
+ "%{public}@: could not open log file %@: %d (%s)"
+ "%{public}@: could not write to file %@: %d (%s)"
+ "%{public}@: power exception: all microstackshots without errors: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
+ "%{public}@: power exception: cannot defer report generation for game mode"
+ "%{public}@: power exception: deferring report generation due to game mode"
+ "%{public}@: power exception: done reporting (%#llx)"
+ "%{public}@: power exception: no microstackshots: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
+ "%{public}@: power exception: not monitoring due to conditions %#llx"
+ "%{public}@: power exception: not monitoring due to suppression cookie file"
+ "%{public}@: power exception: not monitoring due to throttling the number of reports generated for 1st party processes"
+ "%{public}@: power exception: over the last %.0f seconds (%.0f reported) with issue type \"%@\", mitigation reason \"%@\", action taken \"%@\", detector \"%@\", flags %#llx"
+ "%{public}@: power exception: some microstackshots with errors: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
+ "%{public}s [%d]: Absolute path required, have %@"
+ "%{public}s [%d]: Most common UUID with %u samples: %@"
+ "%{public}s [%d]: No UUID for symbol owner"
+ "%{public}s [%d]: No ddt output for resource exhaustion report"
+ "%{public}s [%d]: No lsof output for resource exhaustion report"
+ "%{public}s [%d]: No microstackshots with provided UUIDs %@"
+ "%{public}s [%d]: No output from leaks for %d"
+ "%{public}s [%d]: No symbol owner for symbolicator"
+ "%{public}s [%d]: Possible UUIDs: %@"
+ "%{public}s [%d]: Unable to determine UUID at path %@"
+ "%{public}s [%d]: Unable to spawn leaks: %d (%s)"
+ "%{public}s [%d]: overridden by [%d]"
+ "--outputGraph=/var/tmp/"
+ "/usr/bin/leaks"
+ "/var/db/.spindump_ignore_debugger"
+ "/var/db/.spindump_memgraph_at_shutdown"
+ "@40@0:8i16B20B24B28^B32"
+ "Absolute path required, have %@"
+ "Action"
+ "Appending data file %@"
+ "BundleIdOverride=%{public,signpost.description:attribute}@ %{public,signpost.description:begin_time}llu %{public, signpost.description:end_time}llu action=%{public,name=action}llu conditionsPreventingSubmission=%{public,name=conditionsPreventingSubmission}#llx otherConditions=%{public,name=otherConditions}#llx enableTelemetry=YES "
+ "Child %s [%d] output exceeded %llu bytes"
+ "Child %s [%d] timed out after %llus"
+ "Child [%d] exited"
+ "DoMicrostackshotsForSampleStore"
+ "End time %s (cf:%f)"
+ "Error reporting CPU resource: bad event duration (%f)"
+ "Error reporting CPU resource: bad report duration (%f)"
+ "Error reporting CPU resource: no event duration provided"
+ "Error reporting CPU resource: no report duration provided"
+ "Error reporting power exception: no process path provided"
+ "Event rate report for %s [%d] type %lu"
+ "Got xpc error message in libspindump client [%d] connection: %s"
+ "Got xpc error message in libspindump client [%d] connection: %{public}s"
+ "Including microstackshot for %@ [%d] thread 0x%llx at %s (%@)"
+ "Most common UUID with %u samples: %@"
+ "No UUID for symbol owner"
+ "No ddt output for resource exhaustion report"
+ "No lsof output for resource exhaustion report"
+ "No microstackshots with provided UUIDs %@"
+ "No output from leaks for %d"
+ "No output from leaks for %d\n"
+ "No symbol owner for symbolicator"
+ "Not including microstackshot for %@ [%d] at %s due to being too early (%fs)"
+ "Not including microstackshot for %@ [%d] at %s due to being too late (%fs)"
+ "Not including microstackshot for %@ [%d] at %s due to being wrong pid (requested %d)"
+ "Not including microstackshot for %@ [%d] at %s due to being wrong type (0x%llx, requested 0x%x)"
+ "Not including microstackshot for %@ [%d] at %s due to being wrong uuid (%@)"
+ "Not including microstackshot for %@ [%d] thread 0x%llx at %s due to being wrong thread (requested 0x%llx)"
+ "Possible UUIDs: %@"
+ "PowerException"
+ "Q16@?0@\"SAMicrostackshotInfo\"8"
+ "Reporting power exception that is both fatal and background qos"
+ "Reporting power exception that is neither fatal nor background qos"
+ "Running leaks for %s [%d]"
+ "SA_LOG_MICROSTACKSHOTS"
+ "Start time %s (cf:%f)"
+ "Unable to determine UUID at path %@"
+ "Unable to format: \nusage: spindump [<pid/partial name> [duration [interval]]] <options>\n\n   Spindump gathers user and kernel callstacks for every process.\n\n   pid/partial name\n                The target process (sorted topmost in the output file).\n                \"-noTarget\" may be specified instead to avoid providing\n                a target process when duration is provided.\n   duration     The duration of the sampling in seconds. Default 10.\n   interval     The number of miliseconds between samples. Default 10.\n\n   Giving spindump no parameters will use no target with the default\n   duration and interval.\n\n  Extra options:\n   -i <path>    Read in the file at <path> and generate a spindump report.\n                Spindump reports can be regenerated with different display\n                options\n   -o <path>    Specifies where to write results. If <path> is a directory,\n                the output file will be put inside that directory with a\n                default name, without overwriting any existing file.\n                By default, the output file is put in /tmp/\n\n   -startTime <date>\n                Omit samples before the given wall time specified as a string\n                of the format \"YYYY-MM-DD HH:MM:SS\" with optional decimal\n                seconds and time zone, or with a unix timestamp in seconds\n   -endTime <date>\n                Omit samples after the given wall time specified as a string\n                of the format \"YYYY-MM-DD HH:MM:SS\" with optional decimal\n                seconds and time zone, or with a unix timestamp in seconds\n\n   -startMachAbsTimeNs <mach_abs_time_ns>\n                Omit samples before the given mach abs time (in nanoseconds)\n   -endMachAbsTimeNs <mach_abs_time_ns>\n                Omit samples after the given mach abs time (in nanoseconds)\n   -machAbsTimeRangeNs <mach_abs_time_ns>-<mach_abs_time_ns>\n                Only include samples in the given mach abs time range (in nanoseconds)\n\n   -startMachAbsTime <mach_abs_time>\n                Omit samples before the given mach abs time (in mach time units)\n   -endMachAbsTime <mach_abs_time>\n                Omit samples after the given mach abs time (in mach time units)\n   -machAbsTimeRange <mach_abs_time>-<mach_abs_time>\n                Only include samples in the given mach abs time range\n\n   -indexRange <int>-<int>\n                Only include samples in the given range\n   -startIndex <int>\n                Omit samples before sample number <int>\n   -endIndex <int>\n                Omit samples after sample number <int>\n\n   -last <int>[m|h|d|samples]\n                Only include data from the the last <int> seconds of the data being\n                parsed. Only valid when not sampling the live system. Use \"m\", \"h,\n                \"d\", or \"samples\" to instead specify minutes, hours, days, or number\n                of samples\n\n   -filterToEventTimeRange\n                When parsing a raw input file, automatically filter the report to\n                the time range of the event found in the data\n\n   -heavy       Sort callstacks by count (default)\n   -timeline    Sort callstacks chronologically\n\n   -sortProcessesBy <attribute>\n                Sort processes by the given attribute. This option may be provided\n                multiple times to provide sub-orderings.\n                Valid attributes are \"Name\", \"ID\", \"HighestBasePriority\",\n                \"HighestScheduledPriority\", \"LargestFootprint\", \"CpuTime\",\n                \"InstructionsRetired\", \"Cycles\", \"CyclesPerInstruction\",\n                \"KernelLast\", \"SampleCount\", \"ExecTimestamp\".\n                Any of those attribute strings can be prepended with \"Reverse\" to\n                reverse the default sort order, i.e. \"ReverseName\". The target\n                process will always be first in the report.\n\n   -sortCallTreesBy <attribute>\n                Sort call trees by the given attribute. This option may be provided\n                multiple times to provide sub-orderings.\n                Valid attributes are \"MainThreadFirst\", \"SampleCount\", \"DispatchQueue\",\n                \"Thread\", \"HighestBasePriority\", \"HighestScheduledPriority\",\n                \"CpuTime\", \"InstructionsRetired\", \"Cycles\", \"CyclesPerInstruction\".\n                Any of those attribute strings can be prepended with \"Reverse\" to\n                reverse the default sort order, i.e. \"ReverseSampleCount\". The target\n                thread will always be first in the report.\n\n   -timestampsInCallTrees <time_domain>\n                Print timestamps/ranges for each leaf frame in the call tree.\n                Valid options are \"wall\", \"machabs\", \"machabssec\", \"machcont\",\n                and  \"machcontsec\". May be specified multiple times to print multiple\n                time domains. \"all\" may be used to print all available time domains\n\n   -noText      Omit textual format (include binary format only)\n   -noBinary    Omit binary format (include text format only)\n   -noFile      Do not output to a file (the report, including binary format,\n                will go to stdout instead)\n   -stdout      Print the report to stdout\n   -json        Print the report in json format\n\n   -siginfo     After sampling, wait for SIGINFO before reporting\n   -timelimit <t>\n                Exit after t seconds even if the report hasn't been saved\n\n   -delayonsignal <t>\n                Stop sampling t seconds after receiving a signal instead of\n                stopping immediately\n   -wait        Wait for the process to exist before sampling. If the\n                process already exists, spindump will begin sampling\n                immediately.\n\n   -displayIdleWorkQueueThreads\n                Display idle work queue threads\n   -verbose     Verbose report output\n\n   -noThrottle  Do not throttle sampling rate on excessive memory growth\n   -noProcessingWhileSampling\n                Do not parse stackshots until done sampling\n\n   -inspectLiveSystem\n                When parsing an input file, assume the data was gathered on\n                the current live system (so spindump can inspect processes if\n                necessary to get symbol information)\n   -symbols <path>\n                Read in symbol data at contained in the file at <path>\n   -dscSymDir <path>\n                The path to dscsym directory containing shared cache layout\n                files (for use when parsing input files gathered on a different\n                machine)\n   -dsym <path> Path to a dsym to use during symbolication (may be specified\n                multiple times)\n\n   -noRunnable  Omit callstacks when threads are runnable (but not running)\n   -noRunning   Omit callstacks when threads are running\n   -noBlocked   Omit callstacks when threads are blocked\n   -sampleWithoutTarget\n                Sample for entire duration even if target exits or doesn't exist\n   -onlyTarget  Only sample the target process (allows faster sampling,\n                use 'u' to specify interval in microseconds: e.g. 500u)\n      -proc <pid/partial name>\n                When specifying -onlyTarget, sample the specified process\n                in addition to the target process (may be passed multiple times)\n   -targetThreadID <tid>\n                Target the provided thread ID (sort topmost)\n   -symbolicate (default with -i) Symbolicate the report from information on the\n                current system\n   -noSymbolicate (default without -i) Do not symbolicate the report.\n                UUID+offset information will still be gathered for later\n                symbolication\n   -noBulkSymbolication\n                Don't attempt to use BulkSymbolication\n   -aggregateCallTreesByDispatchQueue\n                Group call trees by dispatch queue\n   -aggregateCallTreesByThread\n                Group call trees by thread\n   -aggregateCallTreesByProcess\n                Group call trees by process\n\n   -aggregateSwiftAsyncTogetherWithOtherCallTrees\n                Don't aggregate swift async callstacks separately from other\n                callstacks\n   -aggregateSwiftAsyncCallTreesByBaseFunction\n                Aggregate swift async callstacks into call trees by the base\n                function (the function initially started by the swift Task)\n   -aggregateSwiftAsyncCallTreesBySwiftTask\n                Aggregate swift async callstacks into call trees by swift task\n   -aggregateSwiftAsyncCallTreesByThread\n                Aggregate swift async callstacks into call trees by thread\n   -aggregateSwiftAsyncCallTreesByProcess\n                Aggregate swift async callstacks into call trees by process\n                (each process will have one swift async call tree\n   -swiftAsyncDisplayCRootCallstacks\n                Display the C root callstacks replaced swift async callstacks\n   -swiftAsyncPrintLeafyCCallstackOnTopOfSwiftAsyncCallstacksAlways\n                Display the leafy C callstack on top of the swift async frames\n                even when run on the main thread\n   -swiftAsyncPrintLeafyCCallstackOnTopOfCRootCallstacksAlways\n                Always display the entire C callstack together. Swift async\n                callstacks will be in a separate call tree without the leafy C\n                callstack\n\n   -aggregateProcessesByInstance\n                Aggregate processes by instance\n   -aggregateProcessesByExecutable\n                Aggregate processes by executable\n   -aggregateProcessesByExecutableAndResourceCoalition\n                Aggregate processes by both executable and resource coalition\n\n   -omitFramesBelowSampleCount <int>\n                Omit callstack frames with count less than <int>\n   -stackshotsOnly\n                Only parse the stackshots from a ktrace file, no kperf\n   -parsePastLastStackshot\n                Parse lightweight PET ktrace data past the last stackshot\n   -noIPC       Do not IPC out to any daemons (more expensive, but more reliable)\n   -reason <string>\n                An optional string to describe why spindump is being invoked\n   -automation\n                Indicate that spindump is running via automation, so it should\n                prefer to avoid impacting system performance (e.g. avoid audio\n                pops)\n   -noExclaves  Disable gathering of exclave information\n\n\n   Micro-stackshots\n     Microstackshots can be obtained from the live system (the default), or\n     from raw microstackshot files/untethered trace files via -i <path>.\n   -microstackshots\n                Report CPU microstackshots.\n   -microstackshots_io\n                Report I/O microstackshots.\n   -microstackshots_datastore <path>\n                Path to microstackshot datastore on disk.\n                If specified without microstackshots_save,\n                read from saved microstackshot data at <path>\n                instead of pulling data from this machine.\n   -microstackshots_save\n                Save microstackshots to the path specified by\n                microstackshots_datastore instead of reporting.\n   -microstackshots_starttime <date>\n                Start time for microstackshot data in a parseable date\n                string such as \"11/14/12 12:00am\" or a unix timestamp\n                as an integer. Default is to use data from as far back as\n                available. (Use -h after to echo the date parsed)\n   -microstackshots_endtime <date>\n                End time for microstackshot data in a parseable date\n                string such as \"11/14/12 12:00am\" or a unix timestamp\n                as an integer. Default is to use data up to as recent as\n                available. (Use -h after to echo the date parsed)\n   -microstackshots_pid <pid>\n                Only report on the given process. Default is all processes.\n   -microstackshots_threadid <thread_id>\n                Only report on the given thread. Default is all threads.\n   -microstackshots_dsc_path <path>\n                Path to a directory containing dyld shared cache information.\n                Default is to historical information for the local machine.\n   -threadpriority_min <int>\n                Filter out any thread samples that have a priority below the\n                given threshold.\n   -threadpriority_max <int>\n                Filter out any thread samples that have a priority above the\n                given threshold.\n   -batteryonly\n                Filter out any stacks from when the machine was on AC\n   -aconly\n                Filter out any stacks from when the machine was on battery\n   -useridleonly\n                Filter out any stacks from when the user was active\n   -useractiveonly\n                Filter out any stacks from when the user was idle\n   -arch        Machine architecture (i.e. \"arm64e\")\n   -hwPageSize <int>\n                Hardware page size in bytes\n   -vmPageSize <int>\n                VM page size in bytes\n   -machTimebase <int>/<int>\n                Mach timebase (numer/denom)\n"
+ "Unable to format: %@ [%d]: %s: being debugged"
+ "Unable to format: %@ [%d]: Absolute path required, have %@"
+ "Unable to format: %@ [%d]: MetricKit unavailable, not providing cpu usage report"
+ "Unable to format: %@ [%d]: MetricKit unavailable, not providing disk writes report"
+ "Unable to format: %@ [%d]: Most common UUID with %u samples: %@"
+ "Unable to format: %@ [%d]: No UUID for symbol owner"
+ "Unable to format: %@ [%d]: No microstackshots found"
+ "Unable to format: %@ [%d]: No microstackshots with provided UUIDs %@"
+ "Unable to format: %@ [%d]: No symbol owner for symbolicator"
+ "Unable to format: %@ [%d]: Not providing unsupported report type (%d) to MetricKit"
+ "Unable to format: %@ [%d]: Possible UUIDs: %@"
+ "Unable to format: %@ [%d]: Providing cpu usage report to MetricKit"
+ "Unable to format: %@ [%d]: Providing disk writes report to MetricKit"
+ "Unable to format: %@ [%d]: Unable to determine UUID at path %@"
+ "Unable to format: %@ [%d]: could not fdopen log file %@: %d (%s)"
+ "Unable to format: %@ [%d]: could not open log file %@: %d (%s)"
+ "Unable to format: %@ [%d]: could not write to file %@: %d (%s)"
+ "Unable to format: %@ deferred power exception: generating deferred report"
+ "Unable to format: %@: Absolute path required, have %@"
+ "Unable to format: %@: MetricKit unavailable, not providing cpu usage report"
+ "Unable to format: %@: MetricKit unavailable, not providing disk writes report"
+ "Unable to format: %@: Most common UUID with %u samples: %@"
+ "Unable to format: %@: No UUID for symbol owner"
+ "Unable to format: %@: No microstackshots found"
+ "Unable to format: %@: No microstackshots with provided UUIDs %@"
+ "Unable to format: %@: No symbol owner for symbolicator"
+ "Unable to format: %@: Not providing unsupported report type (%d) to MetricKit"
+ "Unable to format: %@: Possible UUIDs: %@"
+ "Unable to format: %@: Providing cpu usage report to MetricKit"
+ "Unable to format: %@: Providing disk writes report to MetricKit"
+ "Unable to format: %@: Unable to determine UUID at path %@"
+ "Unable to format: %@: could not fdopen log file %@: %d (%s)"
+ "Unable to format: %@: could not open log file %@: %d (%s)"
+ "Unable to format: %@: could not write to file %@: %d (%s)"
+ "Unable to format: %@: power exception: all microstackshots without errors: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
+ "Unable to format: %@: power exception: cannot defer report generation for game mode"
+ "Unable to format: %@: power exception: deferring report generation due to game mode"
+ "Unable to format: %@: power exception: done reporting (%#llx)"
+ "Unable to format: %@: power exception: no microstackshots: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
+ "Unable to format: %@: power exception: not monitoring due to conditions %#llx"
+ "Unable to format: %@: power exception: not monitoring due to suppression cookie file"
+ "Unable to format: %@: power exception: not monitoring due to throttling the number of reports generated for 1st party processes"
+ "Unable to format: %@: power exception: over the last %.0f seconds (%.0f reported) with issue type \"%@\", mitigation reason \"%@\", action taken \"%@\", detector \"%@\", flags %#llx"
+ "Unable to format: %@: power exception: some microstackshots with errors: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
+ "Unable to format: %s [%d]: Absolute path required, have %@"
+ "Unable to format: %s [%d]: Most common UUID with %u samples: %@"
+ "Unable to format: %s [%d]: No UUID for symbol owner"
+ "Unable to format: %s [%d]: No ddt output for resource exhaustion report"
+ "Unable to format: %s [%d]: No lsof output for resource exhaustion report"
+ "Unable to format: %s [%d]: No microstackshots with provided UUIDs %@"
+ "Unable to format: %s [%d]: No output from leaks for %d"
+ "Unable to format: %s [%d]: No symbol owner for symbolicator"
+ "Unable to format: %s [%d]: Possible UUIDs: %@"
+ "Unable to format: %s [%d]: Unable to determine UUID at path %@"
+ "Unable to format: %s [%d]: Unable to spawn leaks: %d (%s)"
+ "Unable to format: %s [%d]: overridden by [%d]"
+ "Unable to format: %s: %s: Bad report type %d"
+ "Unable to format: %s: %s: Bad report type for microstackshots %d"
+ "Unable to format: %s: %s: No matching timestamps provided: %llu-%llu, %llu-%llu, %.2f-%.2f"
+ "Unable to format: %s: %s: report_type %d, but systemstatsFormat %d"
+ "Unable to format: Absolute path required, have %@"
+ "Unable to format: Appending data file %@"
+ "Unable to format: Child %s [%d] output exceeded %llu bytes"
+ "Unable to format: Child %s [%d] timed out after %llus"
+ "Unable to format: Child [%d] exited"
+ "Unable to format: End time %s (cf:%f)"
+ "Unable to format: Error reporting CPU resource: bad event duration (%f)"
+ "Unable to format: Error reporting CPU resource: bad report duration (%f)"
+ "Unable to format: Error reporting CPU resource: no event duration provided"
+ "Unable to format: Error reporting CPU resource: no report duration provided"
+ "Unable to format: Error reporting power exception: no process path provided"
+ "Unable to format: Got xpc error message in libspindump client [%d] connection: %s"
+ "Unable to format: Including microstackshot for %@ [%d] thread 0x%llx at %s (%@)"
+ "Unable to format: Most common UUID with %u samples: %@"
+ "Unable to format: No UUID for symbol owner"
+ "Unable to format: No ddt output for resource exhaustion report"
+ "Unable to format: No lsof output for resource exhaustion report"
+ "Unable to format: No microstackshots with provided UUIDs %@"
+ "Unable to format: No output from leaks for %d"
+ "Unable to format: No symbol owner for symbolicator"
+ "Unable to format: Not including microstackshot for %@ [%d] at %s due to being too early (%fs)"
+ "Unable to format: Not including microstackshot for %@ [%d] at %s due to being too late (%fs)"
+ "Unable to format: Not including microstackshot for %@ [%d] at %s due to being wrong pid (requested %d)"
+ "Unable to format: Not including microstackshot for %@ [%d] at %s due to being wrong type (0x%llx, requested 0x%x)"
+ "Unable to format: Not including microstackshot for %@ [%d] at %s due to being wrong uuid (%@)"
+ "Unable to format: Not including microstackshot for %@ [%d] thread 0x%llx at %s due to being wrong thread (requested 0x%llx)"
+ "Unable to format: Possible UUIDs: %@"
+ "Unable to format: Reporting power exception that is both fatal and background qos"
+ "Unable to format: Reporting power exception that is neither fatal nor background qos"
+ "Unable to format: Running leaks for %s [%d]"
+ "Unable to format: Start time %s (cf:%f)"
+ "Unable to format: Unable to determine UUID at path %@"
+ "Unable to format: Unable to spawn leaks: %d (%s)"
+ "Unable to format: Unable to target a process by name for microstackshots (%s)"
+ "Unable to format: Waiting for child %s [%d]..."
+ "Unable to format: deferred power exception: bad event duration (%f)"
+ "Unable to format: deferred power exception: bad report duration (%f)"
+ "Unable to format: deferred power exception: no endtime provided"
+ "Unable to format: deferred power exception: no process name provided"
+ "Unable to format: ignore_debugger:%d due to cookie file"
+ "Unable to format: ignore_thermal_pressure:%d due to cookie file"
+ "Unable to format: leaks for [%d] completed"
+ "Unable to format: overridden by [%d]"
+ "Unable to format: power exception app name is %@"
+ "Unable to format: power exception: all microstackshots without errors: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
+ "Unable to format: power exception: cannot defer report generation for game mode"
+ "Unable to format: power exception: deferring report generation due to game mode"
+ "Unable to format: power exception: done reporting (%#llx)"
+ "Unable to format: power exception: no microstackshots: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
+ "Unable to format: power exception: not monitoring due to conditions %#llx"
+ "Unable to format: power exception: not monitoring due to suppression cookie file"
+ "Unable to format: power exception: not monitoring due to throttling the number of reports generated for 1st party processes"
+ "Unable to format: power exception: over the last %.0f seconds (%.0f reported) with issue type \"%@\", mitigation reason \"%@\", action taken \"%@\", detector \"%@\", flags %#llx"
+ "Unable to format: power exception: some microstackshots with errors: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
+ "Unable to format: reading in data file %@ failed: %@"
+ "Unable to format: reset from systemstats"
+ "Unable to spawn leaks for %d: %d %s\n"
+ "Unable to spawn leaks: %d (%s)"
+ "Unable to target a process by name for microstackshots (%s)"
+ "Waiting for child %s [%d]..."
+ "addMicrostackshotsFromData:statistics:filterBlock:"
+ "com.apple.dt.SamplingTools.leaks"
+ "com.apple.spindump.powerexception"
+ "copySampledProcessForPid:isWSBased:createIfUnsampled:cancelExistingProcesses:wasSampled:"
+ "create deferred power exception report for %s"
+ "deferred power exception: bad event duration (%f)"
+ "deferred power exception: bad report duration (%f)"
+ "deferred power exception: no endtime provided"
+ "deferred power exception: no process name provided"
+ "detector"
+ "endSnapshot.stackshotProvider == self->_sampleProvider"
+ "event_duration"
+ "ignore_debugger:%d due to cookie file"
+ "ignore_thermal_pressure:%d due to cookie file"
+ "initWithUUIDBytes:"
+ "issue_type"
+ "keysSortedByValueUsingSelector:"
+ "leaks for [%d] completed"
+ "microSnapshotFlags"
+ "mitigation_reason"
+ "numberWithUnsignedInteger:"
+ "overridden by [%d]"
+ "power exception"
+ "power exception app name is %@"
+ "power exception for %s"
+ "power exception-lite"
+ "power exception: all microstackshots without errors: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
+ "power exception: cannot defer report generation for game mode"
+ "power exception: deferring report generation due to game mode"
+ "power exception: done reporting (%#llx)"
+ "power exception: no microstackshots: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
+ "power exception: not monitoring due to conditions %#llx"
+ "power exception: not monitoring due to suppression cookie file"
+ "power exception: not monitoring due to throttling the number of reports generated for 1st party processes"
+ "power exception: over the last %.0f seconds (%.0f reported) with issue type \"%@\", mitigation reason \"%@\", action taken \"%@\", detector \"%@\", flags %#llx"
+ "power exception: some microstackshots with errors: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
+ "processID"
+ "processMainBinaryUUID"
+ "processName"
+ "reading in data file %@ failed: %@"
+ "report_duration"
+ "report_type == DID_SYSTEM_STATS || report_type == DID_SYSTEM_STATS_IO || report_type == DID_MANUAL_MICROSTACKSHOTS || report_type == DID_MANUAL_MICROSTACKSHOTS_IO || report_type == DID_CPU_RESOURCE || report_type == DID_POWER_EXCEPTION || report_type == DID_DISK_WRITES_RESOURCE"
+ "reset from systemstats"
+ "self->_hidEventSem == ((void*)0)"
+ "setDetector:"
+ "setIssueType:"
+ "setMitigationReason:"
+ "setTargetMainBinaryUUID:"
+ "targetProcesses"
+ "taskStates"
+ "unsignedIntValue"
+ "v24@?0{_CSTypeRef=QQ}8"
- "\nEnd time:        "
- "\nddt %d\n"
- "\nheap --addresses=.*transaction.* --forkCorpseRetryTime=0 %d\n"
- "\nusage: spindump [<pid/partial name> [duration [interval]]] <options>\n\n   Spindump gathers user and kernel callstacks for every process.\n\n   pid/partial name\n                The target process (sorted topmost in the output file).\n                \"-noTarget\" may be specified instead to avoid providing\n                a target process when duration is provided.\n   duration     The duration of the sampling in seconds. Default 10.\n   interval     The number of miliseconds between samples. Default 10.\n\n   Giving spindump no parameters will use no target with the default\n   duration and interval.\n\n  Extra options:\n   -i <path>    Read in the file at <path> and generate a spindump report.\n                Spindump reports can be regenerated with different display\n                options\n   -o <path>    Specifies where to write results. If <path> is a directory,\n                the output file will be put inside that directory with a\n                default name, without overwriting any existing file.\n                By default, the output file is put in /tmp/\n\n   -startTime <date>\n                Omit samples before the given wall time specified as a string\n                of the format \"YYYY-MM-DD HH:MM:SS\" with optional decimal\n                seconds and time zone, or with a unix timestamp in seconds\n   -endTime <date>\n                Omit samples after the given wall time specified as a string\n                of the format \"YYYY-MM-DD HH:MM:SS\" with optional decimal\n                seconds and time zone, or with a unix timestamp in seconds\n\n   -startMachAbsTimeNs <mach_abs_time_ns>\n                Omit samples before the given mach abs time (in nanoseconds)\n   -endMachAbsTimeNs <mach_abs_time_ns>\n                Omit samples after the given mach abs time (in nanoseconds)\n   -machAbsTimeRangeNs <mach_abs_time_ns>-<mach_abs_time_ns>\n                Only include samples in the given mach abs time range (in nanoseconds)\n\n   -startMachAbsTime <mach_abs_time>\n                Omit samples before the given mach abs time (in mach time units)\n   -endMachAbsTime <mach_abs_time>\n                Omit samples after the given mach abs time (in mach time units)\n   -machAbsTimeRange <mach_abs_time>-<mach_abs_time>\n                Only include samples in the given mach abs time range\n\n   -indexRange <int>-<int>\n                Only include samples in the given range\n   -startIndex <int>\n                Omit samples before sample number <int>\n   -endIndex <int>\n                Omit samples after sample number <int>\n\n   -last <int>[m|h|d|samples]\n                Only include data from the the last <int> seconds of the data being\n                parsed. Only valid when not sampling the live system. Use \"m\", \"h,\n                \"d\", or \"samples\" to instead specify minutes, hours, days, or number\n                of samples\n\n   -filterToEventTimeRange\n                When parsing a raw input file, automatically filter the report to\n                the time range of the event found in the data\n\n   -heavy       Sort callstacks by count (default)\n   -timeline    Sort callstacks chronologically\n\n   -sortProcessesBy <attribute>\n                Sort processes by the given attribute. This option may be provided\n                multiple times to provide sub-orderings.\n                Valid attributes are \"Name\", \"ID\", \"HighestBasePriority\",\n                \"HighestScheduledPriority\", \"LargestFootprint\", \"CpuTime\",\n                \"InstructionsRetired\", \"Cycles\", \"CyclesPerInstruction\",\n                \"KernelLast\", \"SampleCount\", \"ExecTimestamp\".\n                Any of those attribute strings can be prepended with \"Reverse\" to\n                reverse the default sort order, i.e. \"ReverseName\". The target\n                process will always be first in the report.\n\n   -sortCallTreesBy <attribute>\n                Sort call trees by the given attribute. This option may be provided\n                multiple times to provide sub-orderings.\n                Valid attributes are \"MainThreadFirst\", \"SampleCount\", \"DispatchQueue\",\n                \"Thread\", \"HighestBasePriority\", \"HighestScheduledPriority\",\n                \"CpuTime\", \"InstructionsRetired\", \"Cycles\", \"CyclesPerInstruction\".\n                Any of those attribute strings can be prepended with \"Reverse\" to\n                reverse the default sort order, i.e. \"ReverseSampleCount\". The target\n                thread will always be first in the report.\n\n   -timestampsInCallTrees <time_domain>\n                Print timestamps/ranges for each leaf frame in the call tree.\n                Valid options are \"wall\", \"machabs\", \"machabssec\", \"machcont\",\n                and  \"machcontsec\". May be specified multiple times to print multiple\n                time domains. \"all\" may be used to print all available time domains\n\n   -noText      Omit textual format (include binary format only)\n   -noBinary    Omit binary format (include text format only)\n   -noFile      Do not output to a file (the report, including binary format,\n                will go to stdout instead)\n   -stdout      Print the report to stdout\n   -json        Print the report in json format\n\n   -siginfo     After sampling, wait for SIGINFO before reporting\n   -timelimit <t>\n                Exit after t seconds even if the report hasn't been saved\n\n   -delayonsignal <t>\n                Stop sampling t seconds after receiving a signal instead of\n                stopping immediately\n   -wait        Wait for the process to exist before sampling. If the\n                process already exists, spindump will begin sampling\n                immediately.\n\n   -displayIdleWorkQueueThreads\n                Display idle work queue threads\n   -verbose     Verbose report output\n\n   -noThrottle  Do not throttle sampling rate on excessive memory growth\n   -noProcessingWhileSampling\n                Do not parse stackshots until done sampling\n\n   -inspectLiveSystem\n                When parsing an input file, assume the data was gathered on\n                the current live system (so spindump can inspect processes if\n                necessary to get symbol information)\n   -symbols <path>\n                Read in symbol data at contained in the file at <path>\n   -dscSymDir <path>\n                The path to dscsym directory containing shared cache layout\n                files (for use when parsing input files gathered on a different\n                machine)\n   -dsym <path> Path to a dsym to use during symbolication (may be specified\n                multiple times)\n\n   -noRunnable  Omit callstacks when threads are runnable (but not running)\n   -noRunning   Omit callstacks when threads are running\n   -noBlocked   Omit callstacks when threads are blocked\n   -sampleWithoutTarget\n                Sample for entire duration even if target exits or doesn't exist\n   -onlyTarget  Only sample the target process (allows faster sampling,\n                use 'u' to specify interval in microseconds: e.g. 500u)\n      -proc <pid/partial name>\n                When specifying -onlyTarget, sample the specified process\n                in addition to the target process (may be passed multiple times)\n   -targetThreadID <tid>\n                Target the provided thread ID (sort topmost)\n   -symbolicate (default with -i) Symbolicate the report from information on the\n                current system\n   -noSymbolicate (default without -i) Do not symbolicate the report.\n                UUID+offset information will still be gathered for later\n                symbolication\n   -noBulkSymbolication\n                Don't attempt to use BulkSymbolication\n   -aggregateCallTreesByDispatchQueue\n                Group call trees by dispatch queue\n   -aggregateCallTreesByThread\n                Group call trees by thread\n   -aggregateCallTreesByProcess\n                Group call trees by process\n\n   -aggregateSwiftAsyncTogetherWithOtherCallTrees\n                Don't aggregate swift async callstacks separately from other\n                callstacks\n   -aggregateSwiftAsyncCallTreesByBaseFunction\n                Aggregate swift async callstacks into call trees by the base\n                function (the function initially started by the swift Task)\n   -aggregateSwiftAsyncCallTreesBySwiftTask\n                Aggregate swift async callstacks into call trees by swift task\n   -aggregateSwiftAsyncCallTreesByThread\n                Aggregate swift async callstacks into call trees by thread\n   -aggregateSwiftAsyncCallTreesByProcess\n                Aggregate swift async callstacks into call trees by process\n                (each process will have one swift async call tree\n   -swiftAsyncDisplayCRootCallstacks\n                Display the C root callstacks replaced swift async callstacks\n   -swiftAsyncPrintLeafyCCallstackOnTopOfSwiftAsyncCallstacksAlways\n                Display the leafy C callstack on top of the swift async frames\n                even when run on the main thread\n   -swiftAsyncPrintLeafyCCallstackOnTopOfCRootCallstacksAlways\n                Always display the entire C callstack together. Swift async\n                callstacks will be in a separate call tree without the leafy C\n                callstack\n\n   -aggregateProcessesByInstance\n                Aggregate processes by instance\n   -aggregateProcessesByExecutable\n                Aggregate processes by executable\n   -aggregateProcessesByExecutableAndResourceCoalition\n                Aggregate processes by both executable and resource coalition\n\n   -omitFramesBelowSampleCount <int>\n                Omit callstack frames with count less than <int>\n   -stackshotsOnly\n                Only parse the stackshots from a ktrace file, no kperf\n   -parsePastLastStackshot\n                Parse lightweight PET ktrace data past the last stackshot\n   -noIPC       Do not IPC out to any daemons (more expensive, but more reliable)\n   -reason <string>\n                An optional string to describe why spindump is being invoked\n   -automation\n                Indicate that spindump is running via automation, so it should\n                prefer to avoid impacting system performance (e.g. avoid audio\n                pops)\n   -noExclaves  Disable gathering of exclave information\n\n\n   Micro-stackshots\n   -microstackshots\n                Report interrupt microstackshots.\n   -microstackshots_io\n                Report I/O microstackshots.\n   -microstackshots_datastore <path>\n                Path to microstackshot datastore on disk.\n                If specified without microstackshots_save,\n                read from saved microstackshot data at <path>\n                instead of pulling data from this machine.\n   -microstackshots_save\n                Save microstackshots to the path specified by\n                microstackshots_datastore instead of reporting.\n   -microstackshots_starttime <date>\n                Start time for microstackshot data in a parseable date\n                string such as \"11/14/12 12:00am\" or a unix timestamp\n                as an integer. Default is to use data from as far back as\n                available. (Use -h after to echo the date parsed)\n   -microstackshots_endtime <date>\n                End time for microstackshot data in a parseable date\n                string such as \"11/14/12 12:00am\" or a unix timestamp\n                as an integer. Default is to use data up to as recent as\n                available. (Use -h after to echo the date parsed)\n   -microstackshots_pid <pid>\n                Only report on the given process. Default is all processes.\n   -microstackshots_threadid <thread_id>\n                Only report on the given thread. Default is all threads.\n   -microstackshots_dsc_path <path>\n                Path to a directory containing dyld shared cache information.\n                Default is to historical information for the local machine.\n   -threadpriority_min <int>\n                Filter out any thread samples that have a priority below the\n                given threshold.\n   -threadpriority_max <int>\n                Filter out any thread samples that have a priority above the\n                given threshold.\n   -batteryonly\n                Filter out any stacks from when the machine was on AC\n   -aconly\n                Filter out any stacks from when the machine was on battery\n   -useridleonly\n                Filter out any stacks from when the user was active\n   -useractiveonly\n                Filter out any stacks from when the user was idle\n   -arch        Machine architecture (i.e. \"arm64e\")\n   -hwPageSize <int>\n                Hardware page size in bytes\n   -vmPageSize <int>\n                VM page size in bytes\n   -machTimebase <int>/<int>\n                Mach timebase (numer/denom)\n"
- "!global_preferences.command_line"
- "%s [%d]: Unable to convert ddt output to NSString: %s"
- "%s [%d]: Unable to convert lsof output to NSString: %s"
- "%s [%d]: Unable to get uid: %d (%s)"
- "%s [%d]: dealloc with %p transaction"
- "%s: Getting prefs for user %d as command-line"
- "%s: being debugged"
- "%s: unable to allocate prefs"
- "%s: unable to allocate prefs dict"
- "%{public}s [%d]: Unable to convert ddt output to NSString: %s"
- "%{public}s [%d]: Unable to convert lsof output to NSString: %s"
- "%{public}s [%d]: Unable to get uid: %d (%s)"
- "%{public}s [%d]: dealloc with %p transaction"
- "%{public}s: being debugged"
- "@36@0:8i16B20B24^B28"
- "Appending data file %s"
- "BundleIdOverride=%{public, signpost.description:attribute}@ %{public, signpost.description:begin_time}llu cid=%{public,name=cid}llu pid=%{public,name=pid}u conditionsPreventingSubmission=%{public,name=conditionsPreventingSubmission}#llx otherConditions=%{public,name=otherConditions}#llx enableTelemetry=YES "
- "Event rate report for [%d] type %lu"
- "Got xpc error message in libspindump client connection: %s"
- "Got xpc error message in libspindump client connection: %{public}s"
- "Hang"
- "Initializing prefs for user %d"
- "SlowHIDResponse"
- "Start time:      "
- "UID %d: Don't throttle short spin reports:%d due to pref isset:%d value:%d"
- "UID %d: Gather samples for hangs:%d due to present:%d submit:%d user requested:%d"
- "UID %d: Gather samples for service watchdog:%d due to submit:%d"
- "UID %d: Gather samples for spins:%d due to submit:%d user requested:%d"
- "UID %d: Gather samples for stuck apps:%d due to internal:%d submit:%d user requested:%d"
- "UID %d: Present UI:%d due to server mode:%d admin:%d"
- "UID %d: User requested spins:%d hangs:%d unavilable on this platform"
- "Unable to convert ddt output to NSString: %s"
- "Unable to convert lsof output to NSString: %s"
- "Unable to format: \nusage: spindump [<pid/partial name> [duration [interval]]] <options>\n\n   Spindump gathers user and kernel callstacks for every process.\n\n   pid/partial name\n                The target process (sorted topmost in the output file).\n                \"-noTarget\" may be specified instead to avoid providing\n                a target process when duration is provided.\n   duration     The duration of the sampling in seconds. Default 10.\n   interval     The number of miliseconds between samples. Default 10.\n\n   Giving spindump no parameters will use no target with the default\n   duration and interval.\n\n  Extra options:\n   -i <path>    Read in the file at <path> and generate a spindump report.\n                Spindump reports can be regenerated with different display\n                options\n   -o <path>    Specifies where to write results. If <path> is a directory,\n                the output file will be put inside that directory with a\n                default name, without overwriting any existing file.\n                By default, the output file is put in /tmp/\n\n   -startTime <date>\n                Omit samples before the given wall time specified as a string\n                of the format \"YYYY-MM-DD HH:MM:SS\" with optional decimal\n                seconds and time zone, or with a unix timestamp in seconds\n   -endTime <date>\n                Omit samples after the given wall time specified as a string\n                of the format \"YYYY-MM-DD HH:MM:SS\" with optional decimal\n                seconds and time zone, or with a unix timestamp in seconds\n\n   -startMachAbsTimeNs <mach_abs_time_ns>\n                Omit samples before the given mach abs time (in nanoseconds)\n   -endMachAbsTimeNs <mach_abs_time_ns>\n                Omit samples after the given mach abs time (in nanoseconds)\n   -machAbsTimeRangeNs <mach_abs_time_ns>-<mach_abs_time_ns>\n                Only include samples in the given mach abs time range (in nanoseconds)\n\n   -startMachAbsTime <mach_abs_time>\n                Omit samples before the given mach abs time (in mach time units)\n   -endMachAbsTime <mach_abs_time>\n                Omit samples after the given mach abs time (in mach time units)\n   -machAbsTimeRange <mach_abs_time>-<mach_abs_time>\n                Only include samples in the given mach abs time range\n\n   -indexRange <int>-<int>\n                Only include samples in the given range\n   -startIndex <int>\n                Omit samples before sample number <int>\n   -endIndex <int>\n                Omit samples after sample number <int>\n\n   -last <int>[m|h|d|samples]\n                Only include data from the the last <int> seconds of the data being\n                parsed. Only valid when not sampling the live system. Use \"m\", \"h,\n                \"d\", or \"samples\" to instead specify minutes, hours, days, or number\n                of samples\n\n   -filterToEventTimeRange\n                When parsing a raw input file, automatically filter the report to\n                the time range of the event found in the data\n\n   -heavy       Sort callstacks by count (default)\n   -timeline    Sort callstacks chronologically\n\n   -sortProcessesBy <attribute>\n                Sort processes by the given attribute. This option may be provided\n                multiple times to provide sub-orderings.\n                Valid attributes are \"Name\", \"ID\", \"HighestBasePriority\",\n                \"HighestScheduledPriority\", \"LargestFootprint\", \"CpuTime\",\n                \"InstructionsRetired\", \"Cycles\", \"CyclesPerInstruction\",\n                \"KernelLast\", \"SampleCount\", \"ExecTimestamp\".\n                Any of those attribute strings can be prepended with \"Reverse\" to\n                reverse the default sort order, i.e. \"ReverseName\". The target\n                process will always be first in the report.\n\n   -sortCallTreesBy <attribute>\n                Sort call trees by the given attribute. This option may be provided\n                multiple times to provide sub-orderings.\n                Valid attributes are \"MainThreadFirst\", \"SampleCount\", \"DispatchQueue\",\n                \"Thread\", \"HighestBasePriority\", \"HighestScheduledPriority\",\n                \"CpuTime\", \"InstructionsRetired\", \"Cycles\", \"CyclesPerInstruction\".\n                Any of those attribute strings can be prepended with \"Reverse\" to\n                reverse the default sort order, i.e. \"ReverseSampleCount\". The target\n                thread will always be first in the report.\n\n   -timestampsInCallTrees <time_domain>\n                Print timestamps/ranges for each leaf frame in the call tree.\n                Valid options are \"wall\", \"machabs\", \"machabssec\", \"machcont\",\n                and  \"machcontsec\". May be specified multiple times to print multiple\n                time domains. \"all\" may be used to print all available time domains\n\n   -noText      Omit textual format (include binary format only)\n   -noBinary    Omit binary format (include text format only)\n   -noFile      Do not output to a file (the report, including binary format,\n                will go to stdout instead)\n   -stdout      Print the report to stdout\n   -json        Print the report in json format\n\n   -siginfo     After sampling, wait for SIGINFO before reporting\n   -timelimit <t>\n                Exit after t seconds even if the report hasn't been saved\n\n   -delayonsignal <t>\n                Stop sampling t seconds after receiving a signal instead of\n                stopping immediately\n   -wait        Wait for the process to exist before sampling. If the\n                process already exists, spindump will begin sampling\n                immediately.\n\n   -displayIdleWorkQueueThreads\n                Display idle work queue threads\n   -verbose     Verbose report output\n\n   -noThrottle  Do not throttle sampling rate on excessive memory growth\n   -noProcessingWhileSampling\n                Do not parse stackshots until done sampling\n\n   -inspectLiveSystem\n                When parsing an input file, assume the data was gathered on\n                the current live system (so spindump can inspect processes if\n                necessary to get symbol information)\n   -symbols <path>\n                Read in symbol data at contained in the file at <path>\n   -dscSymDir <path>\n                The path to dscsym directory containing shared cache layout\n                files (for use when parsing input files gathered on a different\n                machine)\n   -dsym <path> Path to a dsym to use during symbolication (may be specified\n                multiple times)\n\n   -noRunnable  Omit callstacks when threads are runnable (but not running)\n   -noRunning   Omit callstacks when threads are running\n   -noBlocked   Omit callstacks when threads are blocked\n   -sampleWithoutTarget\n                Sample for entire duration even if target exits or doesn't exist\n   -onlyTarget  Only sample the target process (allows faster sampling,\n                use 'u' to specify interval in microseconds: e.g. 500u)\n      -proc <pid/partial name>\n                When specifying -onlyTarget, sample the specified process\n                in addition to the target process (may be passed multiple times)\n   -targetThreadID <tid>\n                Target the provided thread ID (sort topmost)\n   -symbolicate (default with -i) Symbolicate the report from information on the\n                current system\n   -noSymbolicate (default without -i) Do not symbolicate the report.\n                UUID+offset information will still be gathered for later\n                symbolication\n   -noBulkSymbolication\n                Don't attempt to use BulkSymbolication\n   -aggregateCallTreesByDispatchQueue\n                Group call trees by dispatch queue\n   -aggregateCallTreesByThread\n                Group call trees by thread\n   -aggregateCallTreesByProcess\n                Group call trees by process\n\n   -aggregateSwiftAsyncTogetherWithOtherCallTrees\n                Don't aggregate swift async callstacks separately from other\n                callstacks\n   -aggregateSwiftAsyncCallTreesByBaseFunction\n                Aggregate swift async callstacks into call trees by the base\n                function (the function initially started by the swift Task)\n   -aggregateSwiftAsyncCallTreesBySwiftTask\n                Aggregate swift async callstacks into call trees by swift task\n   -aggregateSwiftAsyncCallTreesByThread\n                Aggregate swift async callstacks into call trees by thread\n   -aggregateSwiftAsyncCallTreesByProcess\n                Aggregate swift async callstacks into call trees by process\n                (each process will have one swift async call tree\n   -swiftAsyncDisplayCRootCallstacks\n                Display the C root callstacks replaced swift async callstacks\n   -swiftAsyncPrintLeafyCCallstackOnTopOfSwiftAsyncCallstacksAlways\n                Display the leafy C callstack on top of the swift async frames\n                even when run on the main thread\n   -swiftAsyncPrintLeafyCCallstackOnTopOfCRootCallstacksAlways\n                Always display the entire C callstack together. Swift async\n                callstacks will be in a separate call tree without the leafy C\n                callstack\n\n   -aggregateProcessesByInstance\n                Aggregate processes by instance\n   -aggregateProcessesByExecutable\n                Aggregate processes by executable\n   -aggregateProcessesByExecutableAndResourceCoalition\n                Aggregate processes by both executable and resource coalition\n\n   -omitFramesBelowSampleCount <int>\n                Omit callstack frames with count less than <int>\n   -stackshotsOnly\n                Only parse the stackshots from a ktrace file, no kperf\n   -parsePastLastStackshot\n                Parse lightweight PET ktrace data past the last stackshot\n   -noIPC       Do not IPC out to any daemons (more expensive, but more reliable)\n   -reason <string>\n                An optional string to describe why spindump is being invoked\n   -automation\n                Indicate that spindump is running via automation, so it should\n                prefer to avoid impacting system performance (e.g. avoid audio\n                pops)\n   -noExclaves  Disable gathering of exclave information\n\n\n   Micro-stackshots\n   -microstackshots\n                Report interrupt microstackshots.\n   -microstackshots_io\n                Report I/O microstackshots.\n   -microstackshots_datastore <path>\n                Path to microstackshot datastore on disk.\n                If specified without microstackshots_save,\n                read from saved microstackshot data at <path>\n                instead of pulling data from this machine.\n   -microstackshots_save\n                Save microstackshots to the path specified by\n                microstackshots_datastore instead of reporting.\n   -microstackshots_starttime <date>\n                Start time for microstackshot data in a parseable date\n                string such as \"11/14/12 12:00am\" or a unix timestamp\n                as an integer. Default is to use data from as far back as\n                available. (Use -h after to echo the date parsed)\n   -microstackshots_endtime <date>\n                End time for microstackshot data in a parseable date\n                string such as \"11/14/12 12:00am\" or a unix timestamp\n                as an integer. Default is to use data up to as recent as\n                available. (Use -h after to echo the date parsed)\n   -microstackshots_pid <pid>\n                Only report on the given process. Default is all processes.\n   -microstackshots_threadid <thread_id>\n                Only report on the given thread. Default is all threads.\n   -microstackshots_dsc_path <path>\n                Path to a directory containing dyld shared cache information.\n                Default is to historical information for the local machine.\n   -threadpriority_min <int>\n                Filter out any thread samples that have a priority below the\n                given threshold.\n   -threadpriority_max <int>\n                Filter out any thread samples that have a priority above the\n                given threshold.\n   -batteryonly\n                Filter out any stacks from when the machine was on AC\n   -aconly\n                Filter out any stacks from when the machine was on battery\n   -useridleonly\n                Filter out any stacks from when the user was active\n   -useractiveonly\n                Filter out any stacks from when the user was idle\n   -arch        Machine architecture (i.e. \"arm64e\")\n   -hwPageSize <int>\n                Hardware page size in bytes\n   -vmPageSize <int>\n                VM page size in bytes\n   -machTimebase <int>/<int>\n                Mach timebase (numer/denom)\n"
- "Unable to format: %s [%d]: Unable to convert ddt output to NSString: %s"
- "Unable to format: %s [%d]: Unable to convert lsof output to NSString: %s"
- "Unable to format: %s [%d]: Unable to get uid: %d (%s)"
- "Unable to format: %s [%d]: dealloc with %p transaction"
- "Unable to format: %s: Getting prefs for user %d as command-line"
- "Unable to format: %s: being debugged"
- "Unable to format: %s: unable to allocate prefs"
- "Unable to format: %s: unable to allocate prefs dict"
- "Unable to format: Appending data file %s"
- "Unable to format: Got xpc error message in libspindump client connection: %s"
- "Unable to format: Initializing prefs for user %d"
- "Unable to format: UID %d: Don't throttle short spin reports:%d due to pref isset:%d value:%d"
- "Unable to format: UID %d: Gather samples for hangs:%d due to present:%d submit:%d user requested:%d"
- "Unable to format: UID %d: Gather samples for service watchdog:%d due to submit:%d"
- "Unable to format: UID %d: Gather samples for spins:%d due to submit:%d user requested:%d"
- "Unable to format: UID %d: Gather samples for stuck apps:%d due to internal:%d submit:%d user requested:%d"
- "Unable to format: UID %d: Present UI:%d due to server mode:%d admin:%d"
- "Unable to format: UID %d: User requested spins:%d hangs:%d unavilable on this platform"
- "Unable to format: Unable to convert ddt output to NSString: %s"
- "Unable to format: Unable to convert lsof output to NSString: %s"
- "Unable to format: Unable to get suspended state (%d), assuming not suspended"
- "Unable to format: Unable to get uid: %d (%s)"
- "Unable to format: Unable to inspect task for suspended state (%d), assuming not suspended"
- "Unable to format: dealloc with %p transaction"
- "Unable to format: reading in data file %s failed: %@"
- "Unable to get suspended state (%d), assuming not suspended"
- "Unable to get uid: %d (%s)"
- "Unable to inspect task for suspended state (%d), assuming not suspended"
- "_hidEventSem == NULL"
- "addMicrostackshotsFromData:ofTypes:inTimeRangeStart:end:onlyPid:onlyTid:statistics:"
- "copySampledProcessForPid:isWSBased:createIfUnsampled:wasSampled:"
- "dealloc with %p transaction"
- "endSnapshot.stackshotProvider == _sampleProvider"
- "get_user_preferences"
- "initWithBytesNoCopy:length:encoding:freeWhenDone:"
- "numberWithUnsignedInt:"
- "preferences.m"
- "prefs_for_uid"
- "reading in data file %s failed: %@"
- "report_type == DID_SYSTEM_STATS || report_type == DID_SYSTEM_STATS_IO || report_type == DID_MANUAL_MICROSTACKSHOTS || report_type == DID_MANUAL_MICROSTACKSHOTS_IO || report_type == DID_CPU_RESOURCE || report_type == DID_DISK_WRITES_RESOURCE"
- "user_preferences_dict"

```
