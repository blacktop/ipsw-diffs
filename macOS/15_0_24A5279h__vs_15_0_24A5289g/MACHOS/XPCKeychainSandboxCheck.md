## XPCKeychainSandboxCheck

> `/System/Library/Frameworks/Security.framework/Versions/A/XPCServices/XPCKeychainSandboxCheck.xpc/Contents/MacOS/XPCKeychainSandboxCheck`

```diff

-61439.0.77.0.0
-  __TEXT.__text: 0xdd4
-  __TEXT.__auth_stubs: 0x390
-  __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x467
+61439.0.101.0.0
+  __TEXT.__text: 0x12a8
+  __TEXT.__auth_stubs: 0x3d0
+  __TEXT.__const: 0xb8
+  __TEXT.__cstring: 0x1a7
+  __TEXT.__oslogstring: 0x309
   __TEXT.__unwind_info: 0x90
-  __DATA_CONST.__auth_got: 0x1c8
+  __DATA_CONST.__auth_got: 0x1e8
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x150
-  __DATA.__bss: 0x28
+  __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
+  - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /usr/lib/libSystem.B.dylib
   Functions: 17
-  Symbols:   74
-  CStrings:  34
+  Symbols:   78
+  CStrings:  20
 
Symbols:
+ _SecKeychainCopyDomainSearchList
+ _SecKeychainGetKeychainVersion
+ _SecKeychainGetPath
+ _SecKeychainOpen
+ __os_log_debug_impl
+ __os_log_impl
+ _os_log_type_enabled
+ _secLogObjForScope
- _dlerror
- _dlopen
- _dlsym
- _syslog$DARWIN_EXTSN
CStrings:
+ "SecError"
+ "keychain_xpc_sandbox"
+ "xpc_keychain_sandbox"
- "/System/Library/Frameworks/Security.framework/Security"
- "Can't discover keychain paths for domain %!s(MISSING) on behalf of %!d(MISSING)"
- "Can't get dir or base (likely out of memory) for %!s(MISSING)"
- "Can't get sandbox fs extension for %!s(MISSING)"
- "Can't lookup SecKeychainCopyDomainSearchList in %!p(MISSING): %!s(MISSING)"
- "Can't lookup SecKeychainGetPath in %!p(MISSING): %!s(MISSING)"
- "Failed to open Security framework: %!s(MISSING)"
- "SecKeychainCopyDomainSearchList"
- "SecKeychainGetPath"
- "Unable to create assembly queue for %!d(MISSING)"
- "Unable to create assembly queue label for %!d(MISSING)"
- "Unable to get keychain search list (domain=%!d(MISSING)) on behalf of %!d(MISSING), status=0x%!l(MISSING)x"
- "Unable to get path for keychain#%!l(MISSING)d of %!l(MISSING)d on behalf of %!d(MISSING), status=0x%!l(MISSING)x"
- "Unhandled request event=%!p(MISSING) type=%!p(MISSING)"
- "Unknown op=%!s(MISSING) request from pid %!d(MISSING)"
- "event %!p(MISSING) while done"
- "listener event error (connection %!p(MISSING)): %!s(MISSING)"

```
