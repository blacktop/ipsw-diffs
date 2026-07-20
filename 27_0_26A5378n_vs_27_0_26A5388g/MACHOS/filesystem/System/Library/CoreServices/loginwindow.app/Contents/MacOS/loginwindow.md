## loginwindow

> `/System/Library/CoreServices/loginwindow.app/Contents/MacOS/loginwindow`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__objc_methtype`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3104.0.0.0.0
-  __TEXT.__text: 0xc9304
-  __TEXT.__auth_stubs: 0x2cd0
-  __TEXT.__objc_stubs: 0xfe40
-  __TEXT.__objc_methlist: 0x6af4
+3106.100.0.0.0
+  __TEXT.__text: 0xca464
+  __TEXT.__auth_stubs: 0x2ce0
+  __TEXT.__objc_stubs: 0xfee0
+  __TEXT.__objc_methlist: 0x6b34
   __TEXT.__const: 0x2e8
-  __TEXT.__gcc_except_tab: 0x103c
-  __TEXT.__objc_methname: 0x121ec
-  __TEXT.__oslogstring: 0x2973c
-  __TEXT.__cstring: 0x12a68
+  __TEXT.__gcc_except_tab: 0x1064
+  __TEXT.__objc_methname: 0x12268
+  __TEXT.__oslogstring: 0x299bc
+  __TEXT.__cstring: 0x12ba8
   __TEXT.__objc_classname: 0x87a
   __TEXT.__objc_methtype: 0x21af
   __TEXT.__ustring: 0x1c

   __TEXT.__swift5_fieldmd: 0x34
   __TEXT.__swift5_types: 0x4
   __TEXT.__dlopen_cstrs: 0x53
-  __TEXT.__unwind_info: 0x1dd0
-  __DATA_CONST.__const: 0x2118
+  __TEXT.__unwind_info: 0x1df8
+  __DATA_CONST.__const: 0x21d8
   __DATA_CONST.__cfstring: 0x6e60
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x28

   __DATA_CONST.__objc_arrayobj: 0x498
   __DATA_CONST.__objc_dictobj: 0x2a8
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x1678
-  __DATA_CONST.__got: 0xac0
+  __DATA_CONST.__auth_got: 0x1680
+  __DATA_CONST.__got: 0xac8
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA.__objc_const: 0x8d00
-  __DATA.__objc_selrefs: 0x4ec8
+  __DATA.__objc_const: 0x8d08
+  __DATA.__objc_selrefs: 0x4ef0
   __DATA.__objc_ivar: 0x860
   __DATA.__objc_data: 0x1a70
   __DATA.__data: 0x990

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2597
-  Symbols:   1063
-  CStrings:  9017
+  Functions: 2608
+  Symbols:   1065
+  CStrings:  9040
 
Symbols:
+ __LSApplicationRemoveFromApplicationList
+ __kLSForceQuitApplicationDoNotInformLibQuitKey
+ _lstat
- __LSApplicationQuitting
CStrings:
+ "%s |           %@ is NOT a exited app, do not add it"
+ "%s |           adding %@ (%d), to exited app quit list"
+ "%s |      Exited app %@ failed to quit, error=%@."
+ "%s |      Exited app %@ force quit successfully."
+ "%s |      Timed out trying to terminate exited apps after %g seconds."
+ "%s |      exited-apps appsToCheck:%@"
+ "%s |      exited-apps count:%ld"
+ "%s |     No home directory present for %@, nothing to remove"
+ "%s | ERROR | Application force quit for %@ succeeded."
+ "%s | ERROR | Application terminate returned %@ for %@"
+ "%s | Platform SSO re-activation failed for user %@"
+ "%s | re-activating Platform SSO for user %@ after failed submit"
+ "-[LWScreenLock reactivatePlatformSSOForUser:]"
+ "-[LoginPortJuggler _startLaunchdJobsAtLoginwindowUI]"
+ "-[LogoutUtilities terminateApp:informLibQuit:]"
+ "-[LogoutUtilities terminateApp:informLibQuit:]_block_invoke"
+ "-[SessionLogoutManager allExitedApplications]"
+ "-[SessionLogoutManager quitAllPrivateProcesses]_block_invoke_3"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.S9cDrG/Sources/loginwindow/Source/FirstLoginOptimizer.m"
+ "_startLaunchdJobsAtLoginwindowUI"
+ "allExitedApplications"
+ "appIsExited:"
+ "reactivatePlatformSSOForUser:"
+ "terminateApp:informLibQuit:"
+ "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"
- "-[LogoutUtilities terminateApp:]"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xAiFNB/Sources/loginwindow/Source/FirstLoginOptimizer.m"
```
