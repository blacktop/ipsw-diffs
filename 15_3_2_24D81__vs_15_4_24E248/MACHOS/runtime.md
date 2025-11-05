## runtime

> `/usr/libexec/rosetta/runtime`

```diff

-342.0.0.0.0
-  __TEXT.__text: 0x1d15c
-  __TEXT.runtime_entry: 0x133c
-  __TEXT.runtime_savedreg: 0xf30
+349.0.0.0.0
+  __TEXT.__text: 0x1cf28
+  __TEXT.runtime_entry: 0x1370
+  __TEXT.runtime_savedreg: 0xf58
   __TEXT.runtime_br_miss: 0x98
   __TEXT.runtime_exit_ret: 0xb0
   __TEXT.runtime_exitcall: 0xb0

   __TEXT.runtime_pthread: 0xc0
   __TEXT.runtime_wqthread: 0xc0
   __TEXT.runtime_syscall: 0xe5c
+  __TEXT.debug_thread: 0xb38
   __TEXT.rosetta_version: 0x20
-  __TEXT.__const: 0x524
-  __TEXT.debug_thread: 0xb20
-  __TEXT.__cstring: 0x838a
-  __TEXT.__thread_starts: 0x10
-  __DATA.__const: 0x5d8
-  __DATA.__data: 0xa48
-  __DATA.runtime_pointers: 0x308
+  __TEXT.__const: 0x49c
+  __TEXT.__cstring: 0x841c
+  __TEXT.__chain_starts: 0xc
+  __DATA.__const: 0x5e8
+  __DATA.__data: 0xa50
+  __DATA.__crash_info: 0x40
+  __DATA.runtime_pointers: 0x310
   __DATA.init_done: 0x1
   __DATA.crash_string: 0x1000
   __DATA.__common: 0x8
   __DATA.__bss: 0xa5d4
-  UUID: 11B18945-107E-3E0D-91FA-B5D5ADA3C0C4
+  UUID: A89C8E4C-E823-336B-96F1-2CFDDAE4563D
   Functions: 0
   Symbols:   2
-  CStrings:  1010
+  CStrings:  1017
 
Symbols:
+ 
- ___crashreporter_info__
- __mh_execute_header
CStrings:
+ "No __chain_starts or __thread_starts found"
+ "Overflow calculating fixup chains base"
+ "Overflow calculating fixup chains end"
+ "Unsupported fixup chains format"
+ "__chain_starts"
+ "floatdp3"
+ "format == DYLD_CHAINED_PTR_64_OFFSET"
+ "ldst_unpriv"
+ "ldst_unpriv not expected in user code"
+ "rdrand"
+ "rebase_fixup_chains"
- "__thread_starts section missing"
- "exception level does not support forwarding"
- "thread_starts_interval.has_value()"
- "unable to remap runtime routines"

```
