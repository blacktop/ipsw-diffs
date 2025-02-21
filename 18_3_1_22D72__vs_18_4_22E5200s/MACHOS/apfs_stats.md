## apfs_stats

> `/System/Library/Filesystems/apfs.fs/apfs_stats`

```diff

-2317.82.1.0.0
-  __TEXT.__text: 0x2f1c
-  __TEXT.__auth_stubs: 0x430
-  __TEXT.__cstring: 0x1e13
-  __TEXT.__const: 0x10
+2332.100.53.0.6
+  __TEXT.__text: 0x30e8
+  __TEXT.__auth_stubs: 0x440
+  __TEXT.__const: 0x20
+  __TEXT.__cstring: 0x1f0e
   __TEXT.__unwind_info: 0xa8
-  __DATA_CONST.__auth_got: 0x218
+  __DATA_CONST.__auth_got: 0x220
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x100
-  __DATA_CONST.__cfstring: 0x360
+  __DATA_CONST.__const: 0xe0
+  __DATA_CONST.__cfstring: 0x440
   __DATA.__bss: 0x29
   __DATA.__common: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
-  Functions: 20
-  Symbols:   80
-  CStrings:  179
+  Functions: 19
+  Symbols:   81
+  CStrings:  190
 
Symbols:
+ _CFBooleanGetTypeID
+ _IOObjectGetClass
- _malloc_type_calloc
CStrings:
+ "\t\t\t\t\t\t"
+ "\t\t\t\t\t\tNo container statistics exported"
+ "\t\t\t\t\t\tNo volume statistics exported"
+ "\t\t\t\t\tGraft container statistics:"
+ "\t\t\t\t\tGraft volume statistics:"
+ "\t\t\t\t\tino range: %llu+%llu\n"
+ "Container statistics"
+ "Cryptex inode"
+ "Graft directory inode"
+ "System content"
+ "Volume statistics"
+ "inode range base"
+ "inode range length"
- "\t\t\t\t\tino range: %llu+%llu, flags 0x%llx\n"
- " kMGT"

```
