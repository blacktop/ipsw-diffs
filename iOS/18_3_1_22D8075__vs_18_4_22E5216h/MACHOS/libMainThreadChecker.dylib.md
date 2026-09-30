## libMainThreadChecker.dylib

> `/usr/lib/libMainThreadChecker.dylib`

```diff

-64566.82.1.0.0
-  __TEXT.__text: 0x41f00
-  __TEXT.__auth_stubs: 0x4e0
+64570.34.1.0.0
+  __TEXT.__text: 0x42010
+  __TEXT.__auth_stubs: 0x4d0
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0xd9
-  __TEXT.__cstring: 0x9a9
+  __TEXT.__cstring: 0x9ee
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x270
+  __TEXT.__unwind_info: 0xd8
+  __DATA_CONST.__auth_got: 0x268
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x118
   __DATA_CONST.__cfstring: 0x20
-  __DATA.__data: 0x17
-  __DATA.__bss: 0x1000d8
+  __DATA.__data: 0x10
+  __DATA.__bss: 0x1000e0
   __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 28
-  Symbols:   164
-  CStrings:  118
+  Functions: 32
+  Symbols:   158
+  CStrings:  120
 
Symbols:
+ _IsSuppressed
+ _MergedGlobals.127
+ __ASSERT_API_MUST_BE_CALLED_FROM_MAIN_THREAD_FAILED__.cold.2
+ __MergedGlobals
+ __block_descriptor_tmp.35
+ __block_literal_global.37
+ _ma_Append
+ checker_c.cold.1
- _InlineCallsMachHeaders
- _SEL_currentContext
- _SEL_currentState
- ___CATransaction
- ___NSGraphicsContext
- __block_descriptor_tmp.34
- __block_literal_global.36
- _envCheckCATransaction
- _envIgnoreCallersFromSlashSystem
- _envIgnoreDupsByThreadPc
- _envIgnoreInlineCalls
- _envMaxHitCount
- _haveAppKit
- _strdup
CStrings:
+ "%u\t-[%s %s]\n"
+ "Main Thread Checker: UI API called on a background thread: -[%s %s]\n"
+ "applicationIconBadgeNumber"
+ "setApplicationIconBadgeNumber:"
- "%zu\t%s\n"
- "Main Thread Checker: UI API called on a background thread: %s\n"

```
