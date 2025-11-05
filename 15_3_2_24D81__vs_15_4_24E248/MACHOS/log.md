## log

> `/usr/bin/log`

```diff

-1612.80.7.0.0
-  __TEXT.__text: 0x1fc88
+1643.100.44.0.0
+  __TEXT.__text: 0x21130
   __TEXT.__auth_stubs: 0xf70
   __TEXT.__objc_stubs: 0x2e40
-  __TEXT.__objc_methlist: 0xb98
-  __TEXT.__gcc_except_tab: 0x5b0
-  __TEXT.__const: 0x1bc
-  __TEXT.__cstring: 0x836a
+  __TEXT.__objc_methlist: 0xcec
+  __TEXT.__const: 0xf8
+  __TEXT.__gcc_except_tab: 0x5a4
+  __TEXT.__cstring: 0x8438
   __TEXT.__objc_methname: 0x2564
   __TEXT.__objc_classname: 0x179
   __TEXT.__objc_methtype: 0x114c
   __TEXT.__oslogstring: 0x95
-  __TEXT.__unwind_info: 0x4d0
+  __TEXT.__unwind_info: 0x4c0
   __DATA_CONST.__auth_got: 0x7c8
-  __DATA_CONST.__got: 0x240
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1728
+  __DATA_CONST.__got: 0x238
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0x1858
   __DATA_CONST.__cfstring: 0x10c0
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_arraydata: 0xb0
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_intobj: 0x180
-  __DATA.__objc_const: 0x18a0
-  __DATA.__objc_selrefs: 0xd30
+  __DATA.__objc_const: 0x1628
+  __DATA.__objc_selrefs: 0xdc8
   __DATA.__objc_ivar: 0x114
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x478

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8FE7BAD9-5D00-39BE-972A-5303CDF84793
+  UUID: 6DB7D1C3-D445-3771-8FA9-8D9AC3E6324D
   Functions: 420
   Symbols:   330
-  CStrings:  1814
+  CStrings:  1819
 
Symbols:
+ ___memset_chk
+ __os_trace_realloc
+ __os_trace_write
+ __os_trace_zalloc
+ _closedir
+ _dup
+ _fdopendir
+ _lseek
+ _readdir
- __timesync_continuous_to_wall_time
- __timesync_db_open
- __timesync_db_openat
- __timesync_range_count
- __timesync_range_create
- __timesync_range_destroy
- __timesync_repair
- __timesync_validate
- __timesync_wall_time_to_continuous
CStrings:
+ ".timesync"
+ "?oc:F:l:f:P:p:s:T:Y:"
+ "A:a:o:c:l:b:E:s:oBfp:P:S:?"
+ "A:f:HPprs:t:h?"
+ "B16@?0r*8"
+ "B24@?0[16C]8^v16"
+ "Flushed logs successfully"
+ "Tqvs:F:P:f:A:Z:S:E:l:h?"
+ "Usage: log flush"
+ "a:A:c:t:rs:S:e:E:h?"
+ "dn:o:s:S:u:z:l:LP:?"
+ "flush"
+ "t:s:S:c:?"
+ "usage: log raw-time [<options>] [-c | --continuous] <uuid>:<continuous time>\n   or: log raw-time [<options>] [-t | --time] <wall time>\n   or: log raw-time [<options>] [-r | --range] [-S | --start] <wall time> [-E | --end] <wall time>\n\noptions:\n    -h, -?, --help      show this help\n    -A, --archive       The .logarchive to use to convert time\n\n    -S, --start <time>  The start time for a timesync range\n    -E, --end <time>    The end time for a timesync range\n\n"
+ "usage: log stats [<options>] --archive <archive>\n   or: log stats [<options>]\n\ndescription:\n    Calculate and display statistics for a given log archive or the local log store.\n\noptions:\n    --archive <archive>           Display statistics from the given log archive\n    --count <count> | all         Limit output to <count> rows per section (default: 5)\n    --sort <sort-mode>            Sort output by number of events, or number of bytes\n    --last <num>[m|h|d] | boot    Display statistics for event up to the given limit\n    --start <date>                Display statistics for events from the given start date\n    --end <date>                  Display statistics for events up to the given end date\n    --style human | json          Control the output style of the requested content\n    --[no-]pager                  Paginate output using less.\n\nmodes:\n    --overview                    Display statistics for the entire log archive (default)\n    --per-book                    Display statistics per log book in the archive\n    --per-file                    Display statistics per file in the archive\n    --sender <sender>             Display statistics for a given sender in the archive\n    --process <process>           Display statistics for a given process in the archive\n    --predicate <predicate>       Display statistics for all events in the archive that\n                                  match the given predicate\nsort modes:\n    events                        Sort by event count\n    bytes                         Sort by total byte count (tracepoint size)\n\nvalid time formats:\n    'Y-M-D H:m:s+zzzz', 'Y-M-D H:m:s', 'Y-M-D', '@unixtime'\n\npredicate usage:\n    Filter predicates follow the NSPredicate format described at:\n    https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html\n\n    For predicate field/type details, see `log help predicates`.\n"
+ "v24@?0[16C]8^v16"
- "0"
- "?oc:F:l:f:p:s:T:Y:"
- "A:f:HPprs:u:h?"
- "a:c:t:rs:e:h?"
- "c:idA:F:f:hl:P:s:?"
- "dn:o:s:u:z:?"
- "f:a:o:c:?"
- "n"
- "usage: log raw-time [<options>] [-c | --continuous] <uuid>:<continuous time>\n   or: log raw-time [<options>] [-t | --time] <wall time>\n   or: log raw-time [<options>] [-r | --range] [-s | --start] <wall time> [-e | --end] <wall time>\n\noptions:\n    -h, -?, --help      show this help\n    -a, --archive       The .logarchive to use to convert time\n\n    -s, --start <time>  The start time for a timesync range\n    -e, --end <time>    The end time for a timesync range\n\n"
- "usage: log stats [<options>] --archive <archive>\n   or: log stats [<options>]\n\ndescription:\n    Calculate and display statistics for a given log archive or the local log store.\n\noptions:\n    --archive <archive>           Display statistics from the given log archive\n    --count <count> | all         Limit output to <count> rows per section (default: 5)\n    --sort <sort-mode>            Sort output by number of events, or number of bytes\n    --last <num>[m|h|d] | boot    Display statistics for event up to the given limit\n    --start <date>                Display statistics for events from the given start date\n    --end <date>                  Display statistics for events up to the given end date\n    --style human | json          Control the output style of the requested content\n\nmodes:\n    --overview                    Display statistics for the entire log archive (default)\n    --per-book                    Display statistics per log book in the archive\n    --per-file                    Display statistics per file in the archive\n    --sender <sender>             Display statistics for a given sender in the archive\n    --process <process>           Display statistics for a given process in the archive\n    --predicate <predicate>       Display statistics for all events in the archive that\n                                  match the given predicate\nsort modes:\n    events                        Sort by event count\n    bytes                         Sort by total byte count (tracepoint size)\n\nvalid time formats:\n    'Y-M-D H:m:s+zzzz', 'Y-M-D H:m:s', 'Y-M-D', '@unixtime'\n\npredicate usage:\n    Filter predicates follow the NSPredicate format described at:\n    https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html\n\n    For predicate field/type details, see `log help predicates`.\n"
- "y"

```
