## socketfilterfw

> `/usr/libexec/ApplicationFirewall/socketfilterfw`

```diff

-305.0.0.0.0
-  __TEXT.__text: 0x1cb8c
-  __TEXT.__auth_stubs: 0xff0
-  __TEXT.__objc_stubs: 0x1aa0
-  __TEXT.__objc_methlist: 0x794
-  __TEXT.__const: 0x100
-  __TEXT.__oslogstring: 0x253d
+308.0.0.0.0
+  __TEXT.__text: 0x1d49c
+  __TEXT.__auth_stubs: 0x1010
+  __TEXT.__objc_stubs: 0x1b60
+  __TEXT.__objc_methlist: 0x7bc
+  __TEXT.__const: 0x110
+  __TEXT.__oslogstring: 0x265e
   __TEXT.__cstring: 0x3b37
   __TEXT.__objc_classname: 0xaf
-  __TEXT.__objc_methname: 0x1cf9
+  __TEXT.__objc_methname: 0x1d78
   __TEXT.__objc_methtype: 0x3a0
   __TEXT.__gcc_except_tab: 0x1c
-  __TEXT.__unwind_info: 0x448
-  __DATA_CONST.__auth_got: 0x808
-  __DATA_CONST.__got: 0x1d0
+  __TEXT.__unwind_info: 0x470
+  __DATA_CONST.__auth_got: 0x818
+  __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x530
+  __DATA_CONST.__const: 0x550
   __DATA_CONST.__cfstring: 0xf60
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0xe00
-  __DATA.__objc_selrefs: 0x7f0
+  __DATA.__objc_selrefs: 0x820
   __DATA.__objc_ivar: 0x74
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x820
   __DATA.__common: 0x1c0
-  __DATA.__bss: 0x80
+  __DATA.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 435
-  Symbols:   327
-  CStrings:  1101
+  Functions: 447
+  Symbols:   330
+  CStrings:  1114
 
Symbols:
+ _OBJC_CLASS_$_NEProcessInfo
+ _malloc_type_realloc
+ _proc_pidinfo
CStrings:
+ "Could not get size from sysctl(KERN_PROC)\n"
+ "Could not reallocate memory\n"
+ "Could not sysctl(KERN_PROC)\n"
+ "Enqueuing new inbound flow for %@ with identifier: %@"
+ "Handle flow: processPath is still nil, attempting to find it by UUID: %@"
+ "Updating path for app by bundle id: %@"
+ "copyUUIDsForExecutable:"
+ "init UUID to process path map"
+ "initPathToUUIDMapping"
+ "initWithCapacity:"
+ "proc size mismatch (%zu total, %zu chunks)\n"
+ "processPathFromUUID:"
+ "processPathFromUUID: current map count: %lu"
+ "stringWithUTF8String:"
+ "updateUUIDToPathMap"
- "Enqueing new inbound flow for %@ with identifier: %@"
- "Updating path for app for by bundle id: %@"

```
