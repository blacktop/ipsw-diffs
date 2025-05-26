## tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

```diff

-770.0.1.0.0
-  __TEXT.__text: 0x57888
-  __TEXT.__auth_stubs: 0x12e0
-  __TEXT.__objc_stubs: 0x7fa0
-  __TEXT.__objc_methlist: 0x3670
-  __TEXT.__cstring: 0xa751
-  __TEXT.__const: 0xf8
-  __TEXT.__gcc_except_tab: 0x12b0
-  __TEXT.__objc_methname: 0xd320
-  __TEXT.__oslogstring: 0x9b2f
+771.0.2.0.0
+  __TEXT.__text: 0x57f38
+  __TEXT.__auth_stubs: 0x1320
+  __TEXT.__objc_stubs: 0x7fc0
+  __TEXT.__objc_methlist: 0x3680
+  __TEXT.__cstring: 0xa7f3
+  __TEXT.__const: 0x4f8
+  __TEXT.__gcc_except_tab: 0x129c
+  __TEXT.__objc_methname: 0xd390
+  __TEXT.__oslogstring: 0x9d48
   __TEXT.__objc_classname: 0x557
-  __TEXT.__objc_methtype: 0x1b6f
+  __TEXT.__objc_methtype: 0x1b7d
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x1148
-  __DATA_CONST.__auth_got: 0x980
+  __TEXT.__unwind_info: 0x1164
+  __DATA_CONST.__auth_got: 0x9a0
   __DATA_CONST.__got: 0x180
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x1b40
+  __DATA_CONST.__const: 0x1b80
   __DATA_CONST.__cfstring: 0x5a60
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arraydata: 0xb00
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_dictobj: 0xaa0
-  __DATA.__objc_const: 0x7d48
-  __DATA.__objc_selrefs: 0x2508
+  __DATA.__objc_const: 0x7d68
+  __DATA.__objc_selrefs: 0x2518
   __DATA.__objc_classrefs: 0x298
   __DATA.__objc_superrefs: 0x138
   __DATA.__objc_ivar: 0x520
   __DATA.__objc_data: 0xe60
   __DATA.__data: 0x600
-  __DATA.__bss: 0x371
+  __DATA.__bss: 0x381
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2133
-  Symbols:   409
-  CStrings:  4093
+  Functions: 2146
+  Symbols:   413
+  CStrings:  4113
 
Symbols:
+ _fcntl
+ _lseek
+ _proc_pidinfo
+ _snprintf
+ _write
- __os_feature_enabled_impl
CStrings:
+ "%s/tccd-%d-%04d"
+ "%{public}d open file descriptors"
+ "%{public}d|%{public}d"
+ "%{public}d|%{public}d : %{public}s"
+ "%{public}s: failed to format string for temp_file_path"
+ "%{public}s: failed to open temp file at path \"%{public}s\": open() failed with errno %d"
+ "Corrupting database..."
+ "ExhaustFDs"
+ "Exhausting available file descriptors by opening files in %{public}s"
+ "GetReminderCooldownPeriod"
+ "GetReminderCooldownPeriod, system: %{public}llu, service: %{public}llu"
+ "Let you corrupt"
+ "LogFDs"
+ "SELECT * FROM active_policy WHERE client='NOT EXIST'"
+ "TestDatabaseCorrupt"
+ "Too many open files"
+ "exhaust_file_descriptors"
+ "failed to allocate memory for array of open file descriptors"
+ "failed to get array of open file descriptors"
+ "failed to get size of buffer for open file descriptors"
+ "open_fds"
+ "removabilityDidChangeForApplications:onDeviceWithPairingID:"
+ "result_type"
+ "serviceReminderCooldown"
+ "setReminderCooldownPeriod:with:"
+ "systemReminderCooldown"
+ "tccd_crash_fd_limit"
+ "v32@0:8q16q24"
- "%s featureFlag: %d"
- "Photos"
- "TCC"
- "TCCAuthImprovements"
- "calendarAddAuth"
- "sessionPidAuth"
- "writeOnlyAuthorization"

```
