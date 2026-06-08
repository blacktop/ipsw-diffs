## afktool

> `/usr/bin/afktool`

```diff

-634.120.2.0.0
-  __TEXT.__text: 0x6eac
-  __TEXT.__auth_stubs: 0x790
-  __TEXT.__objc_stubs: 0x7e0
-  __TEXT.__const: 0x311
-  __TEXT.__gcc_except_tab: 0xb0c
-  __TEXT.__cstring: 0x82b
+736.0.0.502.1
+  __TEXT.__text: 0x7e50
+  __TEXT.__auth_stubs: 0x800
+  __TEXT.__objc_stubs: 0x800
+  __TEXT.__const: 0x30
+  __TEXT.__gcc_except_tab: 0xf18
+  __TEXT.__cstring: 0xf47
   __TEXT.__oslogstring: 0x2d
-  __TEXT.__objc_methname: 0x58c
-  __TEXT.__unwind_info: 0x2b0
-  __DATA_CONST.__auth_got: 0x3d8
-  __DATA_CONST.__got: 0x148
-  __DATA_CONST.__const: 0x250
-  __DATA_CONST.__cfstring: 0x6e0
+  __TEXT.__objc_methname: 0x5a2
+  __TEXT.__unwind_info: 0x328
+  __DATA_CONST.__const: 0x2a0
+  __DATA_CONST.__cfstring: 0xa40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_selrefs: 0x1f8
+  __DATA_CONST.__objc_arraydata: 0x60
+  __DATA_CONST.__objc_dictobj: 0xa0
+  __DATA_CONST.__auth_got: 0x410
+  __DATA_CONST.__got: 0x148
+  __DATA.__objc_selrefs: 0x200
   __DATA.__data: 0x10
   __DATA.__bss: 0x1
   __DATA.__common: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 46727157-EE0B-3F40-A6AF-6E960A0DF046
-  Functions: 77
-  Symbols:   169
-  CStrings:  242
+  UUID: E3013778-A31E-387D-9988-3B87FE6313A0
+  Functions: 85
+  Symbols:   177
+  CStrings:  313
 
Symbols:
+ _IOCFSerialize
+ _OBJC_CLASS_$_NSConstantDictionary
+ _dispatch_time
+ _memcpy
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x27
+ _objc_retain_x28
+ _objc_retain_x8
+ _objc_storeStrong
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "  Free:  %llu bytes\n"
+ "  Total: %llu bytes\n"
+ "  Usage: %llu%%\n"
+ "  Used:  %llu bytes\n"
+ "%-32s  %12llu  %12llu  %7llu%%\n"
+ "%-32s  %12s  %12s  %8s\n"
+ "----"
+ "-----"
+ "----------"
+ "<unknown>"
+ "AppleFirmwareKit ToolvRC_ProjectBuildVersion Jun  3 2026 21:07:34"
+ "ERROR! --role or --matching is required for %s command"
+ "ERROR! Could not serialize HeapUsage request"
+ "ERROR! Could not serialize ThreadInfo request"
+ "ERROR! Empty response for HeapUsage property"
+ "ERROR! Empty response for ThreadInfo property"
+ "ERROR! Failed to unserialize HeapUsage response"
+ "ERROR! Failed to unserialize ThreadInfo response"
+ "ERROR! No services matched"
+ "ERROR! Thread info not supported on this firmware"
+ "ERROR! Timeout waiting for HeapUsage response"
+ "ERROR! Timeout waiting for ThreadInfo response"
+ "ERROR! getMatchedServiceProperty HeapUsage: 0x%x"
+ "ERROR! getMatchedServiceProperty ThreadInfo: 0x%x"
+ "Getting matched service property HeapUsage"
+ "Getting matched service property ThreadInfo"
+ "Heap Usage:"
+ "HeapUsage"
+ "INFO! response size:%zu timestamp:%llu"
+ "Matching: %@"
+ "Name"
+ "Stack Size"
+ "Stack Used"
+ "Thread Info (%u threads):\n"
+ "ThreadInfo"
+ "Usage"
+ "Usage: afktool (--help | -v...)\n  afktool registry (--role=<role> [--name=<name>] | --matching=<matching>) [-x]  [--archive [--format=<fmt>] [--path=<dir>]] [--buffer=<size>]\n\nOptions:\n  -r --role=<role>           IOP  role\n  -a --archive               Archive output\n  -x --hex                   Output numbers as hexidecimal. This option does not apply when creating an archive from ioreg.\n  --buffer=<value>           The size of the command buffer to use. By default this is 64KB.\n  -f --format=<fmt>          Archive or response output format (xml,bin)\n  -p --path=<dir>            Save output to files at this path instead of stdout (1 file per role)\n  -m --matching=<matching>   Service matching dictionary in json or xml format"
+ "afktool.heap"
+ "afktool.threads"
+ "freeBytes"
+ "heap"
+ "service-matching"
+ "stackSize"
+ "stackUsed"
+ "system"
+ "threads"
+ "totalBytes"
+ "unsignedLongLongValue"
+ "usedBytes"
- "--buffer"
- "--format"
- "AppleFirmwareKit ToolvRC_ProjectBuildVersion Apr 18 2026 17:27:54"
- "FILENAME"
- "registry"

```
