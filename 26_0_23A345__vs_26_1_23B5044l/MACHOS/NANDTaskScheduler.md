## NANDTaskScheduler

> `/usr/libexec/NANDTaskScheduler`

```diff

-653.0.11.0.0
-  __TEXT.__text: 0x1cab0
-  __TEXT.__auth_stubs: 0x240
-  __TEXT.__cstring: 0x2b936
+653.40.4.0.0
+  __TEXT.__text: 0x1d150
+  __TEXT.__auth_stubs: 0x250
+  __TEXT.__objc_stubs: 0x60
+  __TEXT.__cstring: 0x2ba0a
   __TEXT.__const: 0xb8
-  __TEXT.__oslogstring: 0x191
-  __TEXT.__unwind_info: 0xe8
-  __DATA_CONST.__auth_got: 0x120
-  __DATA_CONST.__got: 0x38
-  __DATA_CONST.__const: 0x40
-  __DATA_CONST.__cfstring: 0x40
+  __TEXT.__oslogstring: 0x4a7
+  __TEXT.__objc_methname: 0x59
+  __TEXT.__unwind_info: 0xe0
+  __DATA_CONST.__auth_got: 0x130
+  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__const: 0x100
+  __DATA_CONST.__cfstring: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA.__objc_selrefs: 0x18
   __DATA.__data: 0x3d8
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /usr/lib/libSystem.B.dylib
-  UUID: 6EF78E63-7DAB-3A50-A9D2-FD5199B37BFA
-  Functions: 78
-  Symbols:   47
-  CStrings:  3102
+  - /usr/lib/libobjc.A.dylib
+  UUID: E65B7E31-A44A-36C2-A0DB-A08BB69ED7C8
+  Functions: 82
+  Symbols:   50
+  CStrings:  3136
 
Symbols:
+ _NSClassFromString
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _objc_msgSend
CStrings:
+ "BGST not available - skipping idleStack registrations.\n"
+ "BGSystemTaskScheduler"
+ "ERROR: Failed to register idleStack_high task (BGST)"
+ "ERROR: Failed to register idleStack_low task (BGST)"
+ "ERROR: Failed to register idleStack_lowNoDI task (BGST)"
+ "ERROR: Failed to register idleStack_lowNoSUI task (BGST)"
+ "ERROR: Failed to register idleStack_med task (BGST)"
+ "End nand_task_scheduler"
+ "IDSTK ping failed to send.\n"
+ "Successfully registered idleStack_high task (BGST)"
+ "Successfully registered idleStack_low task (BGST)"
+ "Successfully registered idleStack_lowNoDI task (BGST)"
+ "Successfully registered idleStack_lowNoSUI task (BGST)"
+ "Successfully registered idleStack_med task (BGST)"
+ "com.apple.idleStack_high"
+ "com.apple.idleStack_low"
+ "com.apple.idleStack_lowNoDI"
+ "com.apple.idleStack_lowNoSUI"
+ "com.apple.idleStack_med"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "running idleStack_high task (BGST)"
+ "running idleStack_low task (BGST)"
+ "running idleStack_lowNoDI task (BGST)"
+ "running idleStack_lowNoSUI task (BGST)"
+ "running idleStack_med task (BGST)"
+ "setTaskCompleted"
+ "sharedScheduler"
+ "v16@?0@\"BGRepeatingSystemTask\"8"

```
