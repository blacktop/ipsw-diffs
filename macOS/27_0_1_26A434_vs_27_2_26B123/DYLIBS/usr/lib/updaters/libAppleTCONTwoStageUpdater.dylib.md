## libAppleTCONTwoStageUpdater.dylib

> `/usr/lib/updaters/libAppleTCONTwoStageUpdater.dylib`

```diff

-230.0.11.0.0
-  __TEXT.__text: 0xad0
+230.41.1.0.0
+  __TEXT.__text: 0xbb8
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__cstring: 0x62b
-  __TEXT.__unwind_info: 0xc0
+  __TEXT.__cstring: 0x6c5
+  __TEXT.__unwind_info: 0xc8
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0xc0
+  __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__auth_got: 0xd0
+  __AUTH_CONST.__auth_got: 0xe8
   __AUTH_CONST.__auth_ptr: 0x0
   __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 20
-  Symbols:   70
-  CStrings:  33
+  Functions: 21
+  Symbols:   74
+  CStrings:  37
 
Symbols:
+ GCC_except_table4
+ _AMSupportGetValueForKeyPathInDict
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ __ZN33AppleTCONTwoStageUpdateController57AppleTCONTwoStageUpdateControllerIsPreflightTicketMissingEPK14__CFDictionary
- GCC_except_table3
CStrings:
+ "AppleTCONTwoStageUpdateController::start: no preflight ticket, skipping update\n"
+ "Options.DeferredCommit"
+ "Options.PreflightRequired"
+ "Options.PreflightTickets"
```
