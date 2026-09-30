## safetycheckd

> `/usr/libexec/safetycheckd`

```diff

-422.0.27.0.0
-  __TEXT.__text: 0x14b8
-  __TEXT.__auth_stubs: 0x290
-  __TEXT.__objc_stubs: 0x700
-  __TEXT.__objc_methlist: 0x22c
-  __TEXT.__const: 0x18
-  __TEXT.__objc_methname: 0x5af
-  __TEXT.__oslogstring: 0x76
-  __TEXT.__cstring: 0xfa
-  __TEXT.__objc_classname: 0x84
-  __TEXT.__objc_methtype: 0x165
-  __TEXT.__unwind_info: 0xe0
-  __DATA_CONST.__auth_got: 0x150
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x88
-  __DATA_CONST.__cfstring: 0x80
-  __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x18
+423.0.44.0.0
+  __TEXT.__text: 0x1068
+  __TEXT.__auth_stubs: 0x250
+  __TEXT.__objc_stubs: 0x600
+  __TEXT.__objc_methlist: 0x1dc
+  __TEXT.__const: 0x8
+  __TEXT.__cstring: 0xaf
+  __TEXT.__objc_classname: 0x2b
+  __TEXT.__objc_methname: 0x4df
+  __TEXT.__objc_methtype: 0xbd
+  __TEXT.__unwind_info: 0xc8
+  __DATA_CONST.__auth_got: 0x130
+  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__const: 0x48
+  __DATA_CONST.__cfstring: 0x40
+  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x20
-  __DATA.__objc_const: 0x4d8
-  __DATA.__objc_selrefs: 0x220
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA.__objc_const: 0x370
+  __DATA.__objc_selrefs: 0x1d8
   __DATA.__objc_ivar: 0x18
-  __DATA.__objc_data: 0x140
-  __DATA.__data: 0x128
-  __DATA.__bss: 0x20
+  __DATA.__objc_data: 0xf0
+  __DATA.__data: 0x68
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 47
-  Symbols:   66
-  CStrings:  125
+  Functions: 38
+  Symbols:   60
+  CStrings:  100
 
Symbols:
- _OBJC_CLASS_$_BGSystemTaskScheduler
- __NSConcreteGlobalBlock
- __os_log_error_impl
- _objc_opt_respondsToSelector
- _os_log_create
- _os_log_type_enabled
CStrings:
- "\"Couldn't initialize task for identifier %!@(MISSING) and/or selector %!@(MISSING)\""
- "\"SC task %!@(MISSING) will not handle BGST task %!@(MISSING). Reason: %!@(MISSING)\""
- "@\"NSString\"16@0:8"
- "@?16@0:8"
- "@?<v@?@\"BGNonRepeatingSystemTask\">16@0:8"
- "@?<v@?@\"BGRepeatingSystemTask\">16@0:8"
- "B16@0:8"
- "SCBackgroundSystemTask"
- "SCBackgroundSystemTaskHandling"
- "SCBackgroundSystemTaskRegistration"
- "SCLogger"
- "_conformsToTaskHandling"
- "com.apple.safetycheckd"
- "handleNonRepeatingTask"
- "handleRepeatingTask"
- "identifier"
- "isRepeating"
- "nonRepeatingTaskHandler"
- "registerForTaskWithIdentifier:usingQueue:launchHandler:"
- "rejectAndCloseTask:reason:"
- "repeatingTaskHandler"
- "setTaskCompleted"
- "sharedScheduler"
- "v24@0:8@\"NSObject<OS_dispatch_queue>\"16"
- "v32@0:8@16@24"

```
