## MSUEarlyBootTask

> `/usr/libexec/MSUEarlyBootTask`

```diff

-1856.80.3.0.1
-  __TEXT.__text: 0x4080
-  __TEXT.__auth_stubs: 0x6c0
-  __TEXT.__objc_stubs: 0x4c0
-  __TEXT.__cstring: 0x27b0
-  __TEXT.__const: 0x44c
-  __TEXT.__objc_methname: 0x367
-  __TEXT.__unwind_info: 0xb4
-  __DATA_CONST.__auth_got: 0x368
-  __DATA_CONST.__got: 0x40
+1856.100.79.0.3
+  __TEXT.__text: 0x4024
+  __TEXT.__auth_stubs: 0x710
+  __TEXT.__objc_stubs: 0x440
+  __TEXT.__cstring: 0x27ea
+  __TEXT.__const: 0x444
+  __TEXT.__objc_methname: 0x315
+  __TEXT.__unwind_info: 0xbc
+  __DATA_CONST.__auth_got: 0x390
+  __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x38
-  __DATA_CONST.__cfstring: 0x400
+  __DATA_CONST.__const: 0x10
+  __DATA_CONST.__cfstring: 0x3e0
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_selrefs: 0x130
-  __DATA.__objc_classrefs: 0x40
-  __DATA.__bss: 0x30
+  __DATA.__objc_selrefs: 0x110
+  __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 99804A98-E202-3B45-8B4A-0EF706939ABC
-  Functions: 22
-  Symbols:   301
-  CStrings:  330
+  UUID: 811B613B-25A3-3FA0-82A7-7D7A8FBD6C58
+  Functions: 23
+  Symbols:   309
+  CStrings:  325
 
Symbols:
+ /AppleInternal/Library/BuildRoots/7f1e11ec-d0b2-11ee-9ae5-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
+ /Library/Caches/com.apple.xbs/Sources/PurpleRestore_libpartition/ramrod/
+ _CFDataGetTypeID
+ _IOObjectRelease
+ _IORegistryEntryFromPath
+ __loggingPtr
+ __partition_log
+ _copy_root_snapshot_name_from_dt
+ _objc_retain_x24
+ _strndup
+ _unnamed_array_storage.496
+ partition.c
- _OBJC_CLASS_$_NSMutableString
- __NSConcreteStackBlock
- ___block_descriptor_40_e8_32s_e29_v40?0r^v8{_NSRange=QQ}16^B32ls32l8
- ___update_var_directory_hierarchy_block_invoke
- _objc_msgSend$appendFormat:
- _objc_msgSend$enumerateByteRangesUsingBlock:
- _objc_msgSend$stringWithCapacity:
- _objc_msgSend$uppercaseString
- _unnamed_array_storage.482
CStrings:
+ "Failed to copy default boot snapshot name"
+ "IODeviceTree:/chosen"
+ "device tree root-snapshot-name type mismatch"
+ "root-snapshot-name"
+ "uanble to find chosen node"
+ "unable to look up root-snapshot-name on chosen node"
- "%02X"
- "%s%@"
- "Failed to allocate string to hold bootmanifesthash\n"
- "Failed to copy BootManifestHash..\n"
- "appendFormat:"
- "com.apple.os.update-"
- "enumerateByteRangesUsingBlock:"
- "stringWithCapacity:"
- "uppercaseString"
- "v40@?0r^v8{_NSRange=QQ}16^B32"

```
