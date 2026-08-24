## networkQuality

> `/usr/bin/networkQuality`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-220.0.0.0.0
-  __TEXT.__text: 0xc0f0
-  __TEXT.__auth_stubs: 0x360
-  __TEXT.__objc_stubs: 0x1d80
+224.0.0.0.0
+  __TEXT.__text: 0xc2c0
+  __TEXT.__auth_stubs: 0x370
+  __TEXT.__objc_stubs: 0x1e60
   __TEXT.__objc_methlist: 0x430
   __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0x400
-  __TEXT.__cstring: 0x2fe0
-  __TEXT.__objc_methname: 0x184f
+  __TEXT.__cstring: 0x310b
+  __TEXT.__objc_methname: 0x18e6
   __TEXT.__objc_classname: 0x34
   __TEXT.__objc_methtype: 0x20e
   __TEXT.__unwind_info: 0x1d0
-  __DATA_CONST.__const: 0x9b8
-  __DATA_CONST.__cfstring: 0x1560
+  __DATA_CONST.__const: 0xa18
+  __DATA_CONST.__cfstring: 0x15c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA_CONST.__auth_got: 0x1c0
-  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__auth_got: 0x1c8
+  __DATA_CONST.__got: 0xe0
   __DATA.__objc_const: 0x6a8
-  __DATA.__objc_selrefs: 0x840
+  __DATA.__objc_selrefs: 0x878
   __DATA.__objc_ivar: 0x74
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 140
-  Symbols:   91
-  CStrings:  655
+  Symbols:   93
+  CStrings:  668
 
Symbols:
+ ___NSArray0__struct
+ _strlen
Functions:
~ sub_100000ee0 : 9072 -> 9116
~ sub_1000053bc -> sub_1000053e8 : 5284 -> 5404
~ sub_10000b7c0 -> sub_10000b864 : 4672 -> 4972
CStrings:
+ "    --bundle-identifier: Bundle identifier to delegate traffic to\n    --csv-error-log <filename>: Write detailed error information to CSV file\n    --draft9: Follow draft-ietf-ippm-responsiveness-09 timing (interval duration 5s)\n    --enable-server-access-log: Enable access logging in server mode (logs to stdout)\n    --json: JSON output (one JSON object per progress update)\n    --latency-measurement-network-service-type: Specifies the network service type to use\n                                                for sending measurement requests (default: BE)\n      (supported values:  BK_SYS, BK, RV, AV, RD, OAM, VI, SIG and VO)\n    --load-generating-connection-ttl: Time-to-live for load generating connections in seconds (default: 0 - disabled)\n    --load-generating-network-service-type: Specifies the network service type to use\n                                            for load generating requests (default: BE)\n      (supported values:  BK_SYS, BK, RV, AV, RD, OAM, VI, SIG and VO)\n    --max-foreign-probes: Maximum concurrent foreign probe requests (default: 25)\n                          Foreign probes create new connections\n    --max-probes-per-second: Maximum responsiveness probes per second (default: 50)\n    --max-self-probes: Maximum concurrent self probe requests (default: 25)\n                       Self probes multiplex on existing connections\n    --max-time: Maximum timeout for individual HTTP requests in seconds\n                (default: 60, overrides timeoutIntervalForRequest)\n    --probe-id: Add monotonically increasing ID parameter to probe request URLs (eg ?t=1)\n    --rapport: invoke test from remote host (against specified in -e (optional))\n    --server-idle-timeout-seconds: Specifies the idle time out for server connections\n    --server-network-service-type: Specifies the network service type to use\n                                   for server responses (default: BE)\n      (supported values:  BK_SYS, BK, RV, AV, RD, OAM, VI, SIG and VO)\n    --unified-http-stack: Use the unified HTTP stack\n"
+ "   Draft Version: %ld\n"
+ "Invalid max probes per second: %s (must be 1-1000)\n"
+ "cli_options"
+ "commandLineArguments"
+ "draft9"
+ "draftVersion"
+ "draft_version"
+ "initWithBytes:length:encoding:"
+ "max-probes-per-second"
+ "setCommandLineArguments:"
+ "setDraftVersion:"
+ "setIntervalDuration:"
+ "setMaxProbesPerSecond:"
- "    --bundle-identifier: Bundle identifier to delegate traffic to\n    --csv-error-log <filename>: Write detailed error information to CSV file\n    --enable-server-access-log: Enable access logging in server mode (logs to stdout)\n    --json: JSON output (one JSON object per progress update)\n    --latency-measurement-network-service-type: Specifies the network service type to use\n                                                for sending measurement requests (default: BE)\n      (supported values:  BK_SYS, BK, RV, AV, RD, OAM, VI, SIG and VO)\n    --load-generating-connection-ttl: Time-to-live for load generating connections in seconds (default: 0 - disabled)\n    --load-generating-network-service-type: Specifies the network service type to use\n                                            for load generating requests (default: BE)\n      (supported values:  BK_SYS, BK, RV, AV, RD, OAM, VI, SIG and VO)\n    --max-foreign-probes: Maximum concurrent foreign probe requests (default: 25)\n                          Foreign probes create new connections\n    --max-self-probes: Maximum concurrent self probe requests (default: 25)\n                       Self probes multiplex on existing connections\n    --max-time: Maximum timeout for individual HTTP requests in seconds\n                (default: 60, overrides timeoutIntervalForRequest)\n    --probe-id: Add monotonically increasing ID parameter to probe request URLs (eg ?t=1)\n    --rapport: invoke test from remote host (against specified in -e (optional))\n    --server-idle-timeout-seconds: Specifies the idle time out for server connections\n    --server-network-service-type: Specifies the network service type to use\n                                   for server responses (default: BE)\n      (supported values:  BK_SYS, BK, RV, AV, RD, OAM, VI, SIG and VO)\n    --unified-http-stack: Use the unified HTTP stack\n"
```
