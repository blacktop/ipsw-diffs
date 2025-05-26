## MSUEarlyBootTask

> `/usr/libexec/MSUEarlyBootTask`

```diff

-1856.102.1.0.0
-  __TEXT.__text: 0x4024
-  __TEXT.__auth_stubs: 0x710
-  __TEXT.__objc_stubs: 0x440
-  __TEXT.__cstring: 0x27ea
+1856.120.12.0.0
+  __TEXT.__text: 0x3a50
+  __TEXT.__auth_stubs: 0x700
+  __TEXT.__objc_stubs: 0x420
+  __TEXT.__cstring: 0x259a
   __TEXT.__const: 0x444
-  __TEXT.__objc_methname: 0x315
-  __TEXT.__unwind_info: 0xbc
-  __DATA_CONST.__auth_got: 0x390
+  __TEXT.__objc_methname: 0x2f7
+  __TEXT.__unwind_info: 0xb8
+  __DATA_CONST.__auth_got: 0x388
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x10
-  __DATA_CONST.__cfstring: 0x3e0
+  __DATA_CONST.__cfstring: 0x380
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_classrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_selrefs: 0x110
+  __DATA.__objc_selrefs: 0x108
   __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 23
-  Symbols:   309
-  CStrings:  294
+  Functions: 22
+  Symbols:   302
+  CStrings:  281
 
Symbols:
+ /AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
+ _objc_retain_x23
+ _unnamed_array_storage.484
- /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
- _copy_folder_contents
- _objc_msgSend$copyItemAtPath:toPath:error:
- _objc_retain_x25
- _objc_retain_x27
- _unnamed_array_storage.496
CStrings:
- "%@/%@"
- "%s: Failed to copy %s to %s: %s\n"
- "%s: Failed to copy contents of ramdisk CrashReporter folder to the data CrashReporter dir\n"
- "%s: Failed to delete the CrashReporter dir created by the ramdisk: %s\n"
- "%s: Failed to search folder %s: %s\n"
- "%s: No ramdisk created CrashReporter dir found\n"
- "%s: Successfully copied %s to %s\n"
- "%s: Successfully copied contents of the ramdisk CrashReporter folder to the data CrashReporter dir\n"
- "/private/var/MobileSoftwareUpdate//mobile/Library/Logs/CrashReporter"
- "/private/var/mobile/Library/Logs/CrashReporter"
- "copyItemAtPath:toPath:error:"
- "copy_folder_contents"
- "preserve_ramdisk_crashreporter_logs"

```
