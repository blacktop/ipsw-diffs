## libLogRedirect.dylib

> `/usr/lib/libLogRedirect.dylib`

```diff

-64561.82.2.0.0
-  __TEXT.__text: 0x1b78
-  __TEXT.__auth_stubs: 0x200
+64562.1.1.0.0
+  __TEXT.__text: 0x1e78
+  __TEXT.__auth_stubs: 0x230
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x3ba
+  __TEXT.__cstring: 0x3df
   __TEXT.__oslogstring: 0x19
-  __TEXT.__unwind_info: 0xa8
-  __DATA_CONST.__auth_got: 0x100
-  __DATA_CONST.__got: 0x18
-  __DATA_CONST.__const: 0x60
-  __DATA.__thread_vars: 0x30
-  __DATA.__interpose: 0x10
+  __TEXT.__unwind_info: 0xac
+  __DATA_CONST.__auth_got: 0x118
+  __DATA_CONST.__got: 0x38
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA_CONST.__const: 0x20
+  __DATA.__thread_vars: 0x18
+  __DATA.__interpose: 0x50
   __DATA.__data: 0x58
-  __DATA.__thread_bss: 0x2
-  __DATA.__common: 0x8
-  __DATA.__bss: 0x2198
+  __DATA.__thread_bss: 0x4
+  __DATA.__common: 0xc
+  __DATA.__bss: 0x218c
   - /usr/lib/libSystem.B.dylib
-  UUID: 1D0DCE6F-3529-3546-BE8B-697D16118C85
-  Functions: 18
-  Symbols:   96
-  CStrings:  57
+  UUID: 0FE137EF-08EB-3BF5-85D1-EBF2B4FAF874
+  Functions: 22
+  Symbols:   105
+  CStrings:  58
 
Symbols:
+ _LogRedirectSendToOSLog
+ _LogRedirectWrite
+ _LogRedirectWritev
+ ___chkstk_darwin
+ ___fork
+ ___logredirect__fork
+ ___logredirect__write
+ ___logredirect__writev
+ ___logredirect__writev_nocancel
+ ___writev_nocancel
+ __interpose___fork
+ __interpose___writev_nocancel
+ __interpose_write
+ __interpose_writev
+ _bzero
+ _logRedirectLock
+ _resetDyldInsertLibraries
+ _setenv
+ _stpncpy
+ _threadLockFlags
+ _threadLockFlags$tlv$init
- DetectProcessForked.initialPID
- _DetectProcessForked
- _HookPerformWithWriteLock
- ___HookHandleLogMessage_block_invoke
- ___LibLogRedirect_InitComplete_block_invoke_2
- __block_descriptor_tmp.32
- __block_descriptor_tmp.7
- _threadHasWriteLock
- _threadHasWriteLock$tlv$init
- _threadIsCurrentlyLogging
- _threadIsCurrentlyLogging$tlv$init
- _writeLock
CStrings:
+ "DYLD_INSERT_LIBRARIES"
+ "libLogRedirect.dylib"
- "v8@?0"

```
