## PhotoLibraryServicesCore

> `/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore`

```diff

-916.40.110.0.0
-  __TEXT.__text: 0xc7ff8
+916.45.110.0.0
+  __TEXT.__text: 0xc8078
   __TEXT.__objc_methlist: 0x8364
   __TEXT.__const: 0x23cc
   __TEXT.__dlopen_cstrs: 0x19c
   __TEXT.__gcc_except_tab: 0x57cc
   __TEXT.__cstring: 0x162ab
-  __TEXT.__oslogstring: 0xb38c
+  __TEXT.__oslogstring: 0xb37a
   __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0x42a0
   __TEXT.__objc_stubs: 0x0

   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x2a0
   __AUTH_CONST.__auth_got: 0xe50
-  __AUTH.__objc_data: 0x370
+  __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x678
   __DATA.__data: 0x10e0
-  __DATA_DIRTY.__objc_data: 0x24e0
+  __DATA_DIRTY.__objc_data: 0x27b0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x408
+  __DATA_DIRTY.__bss: 0x3a0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
Functions:
~ -[PLFileBackedLogger _inlock_createLoggerRecordWithLogFileURL:logRotate:didRebuildLogArchive:error:] : 628 -> 724
~ -[PLFileBackedLogger close] : 584 -> 616
CStrings:
+ "PLFileBackedLogger: Failed to open log file at %@. Error: %@"
+ "PLFileBackedLogger: close url backed logger: %@"
+ "PLFileBackedLogger: open url backed logger: %@"
+ "PLFileBackedLogger: open url found a corrupt log file. Attempting repair for: %@"
- "PLFileBackedLogger: Failed to open log file. Error: %@"
- "PLFileBackedLogger: close url backed logger: %{public}@"
- "PLFileBackedLogger: open url backed logger: %{public}@"
- "PLFileBackedLogger: open url found a corrupt log file. Attempting repair for: %{public}@"
```
