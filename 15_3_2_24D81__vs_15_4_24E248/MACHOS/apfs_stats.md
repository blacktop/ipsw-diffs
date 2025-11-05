## apfs_stats

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_stats`

```diff

-2317.81.2.0.0
-  __TEXT.__text: 0x3114
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__cstring: 0x1e1d
-  __TEXT.__const: 0x10
-  __TEXT.__unwind_info: 0xb8
-  __DATA_CONST.__auth_got: 0x228
+2332.101.1.0.0
+  __TEXT.__text: 0x3310
+  __TEXT.__auth_stubs: 0x460
+  __TEXT.__const: 0x20
+  __TEXT.__cstring: 0x1f18
+  __TEXT.__unwind_info: 0xb0
+  __DATA_CONST.__auth_got: 0x230
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x100
-  __DATA_CONST.__cfstring: 0x360
+  __DATA_CONST.__const: 0xe0
+  __DATA_CONST.__cfstring: 0x440
   __DATA.__bss: 0x29
   __DATA.__common: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS
   - /usr/lib/libSystem.B.dylib
-  UUID: 586883D2-D4B7-31B1-8E84-9C1077219312
-  Functions: 23
-  Symbols:   82
-  CStrings:  206
+  UUID: CE8E379F-400B-3807-85F2-B33D9C7F5BCC
+  Functions: 20
+  Symbols:   83
+  CStrings:  224
 
Symbols:
+ _CFBooleanGetTypeID
+ _IOObjectGetClass
- _calloc
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
