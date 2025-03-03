## seputil

> `/usr/libexec/seputil`

```diff

-842.60.8.0.0
-  __TEXT.__text: 0x177a0
+850.100.13.502.1
+  __TEXT.__text: 0x15898
   __TEXT.__auth_stubs: 0xa40
-  __TEXT.__const: 0xbfc
-  __TEXT.__cstring: 0x5eaf
-  __TEXT.__oslogstring: 0x93
+  __TEXT.__cstring: 0x5e16
+  __TEXT.__const: 0xbf4
+  __TEXT.__oslogstring: 0x5e
   __TEXT.__gcc_except_tab: 0x264
-  __TEXT.__unwind_info: 0x488
+  __TEXT.__unwind_info: 0x480
   __DATA_CONST.__auth_got: 0x528
-  __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x158
+  __DATA_CONST.__got: 0xc8
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__const: 0x140
   __DATA_CONST.__cfstring: 0x80
-  __DATA.__data: 0xc00
+  __DATA.__data: 0xc20
   __DATA.__common: 0xc
-  __DATA.__bss: 0x8bd
+  __DATA.__bss: 0x8f5
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 430
+  Functions: 464
   Symbols:   195
   CStrings:  722
 
CStrings:
+ "%s called with slot %u\n"
+ "%s: Bad hash hex string (%d)\n"
+ "%s: Missing hash\n"
+ "%s: bad arguments: %u %lu\n"
+ "%s: commit hash failed: 0x%x\n"
+ "commitApHash"
+ "commitSepHash"
+ "hash"
- "%s called with slot %u, for_ap %u\n"
- "-"
- "/Library/Caches/com.apple.xbs/Sources/AppleSEPUtil/seputil/seputil.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleSEPUtil/seputil/shared_support.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleSEPUtil/seputil/tbm.c"
- "AssertMacros:(value = 0x%lx), %s file: %s, line: %d\n"
- "sepCommitHash"

```
