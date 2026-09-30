## coredatad

> `/usr/libexec/coredatad`

```diff

-1419.1.0.0.0
-  __TEXT.__text: 0x1e4
+1445.0.0.0.0
+  __TEXT.__text: 0x270
   __TEXT.__auth_stubs: 0x90
-  __TEXT.__objc_stubs: 0x120
-  __TEXT.__objc_methlist: 0x14
-  __TEXT.__objc_classname: 0xc
-  __TEXT.__objc_methname: 0xa8
-  __TEXT.__objc_methtype: 0x8
-  __TEXT.__const: 0x8
-  __TEXT.__cstring: 0xb8
-  __TEXT.__oslogstring: 0x26
+  __TEXT.__objc_stubs: 0xe0
+  __TEXT.__const: 0x20
+  __TEXT.__cstring: 0x31
+  __TEXT.__oslogstring: 0xa4
+  __TEXT.__objc_methname: 0x79
   __TEXT.__unwind_info: 0x58
   __DATA_CONST.__auth_got: 0x50
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__cfstring: 0x80
-  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__got: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x50
-  __DATA.__objc_data: 0x50
-  __DATA.__common: 0x8
+  __DATA.__objc_selrefs: 0x38
+  __DATA.__bss: 0x8
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2
-  Symbols:   22
-  CStrings:  19
+  Functions: 1
+  Symbols:   16
+  CStrings:  15
 
Symbols:
+ __os_log_impl
+ _objc_release_x19
+ _os_log_create
- _OBJC_CLASS_$_NSObject
- _OBJC_CLASS_$_NSString
- _OBJC_CLASS_$__NSCoreDataInternal
- _OBJC_METACLASS_$_NSObject
- __NSCoreDataLog
- ___CFConstantStringClassReference
- __objc_empty_cache
- _objc_opt_class
- _objc_release_x20
CStrings:
+ "com.apple.coredata"
+ "coredatad"
- "CDDRoutines"
- "CoreData: Failed to enter sandbox: %s"
- "initialize"
- "pflogFaultLog"
- "stringWithUTF8String:"
- "v16@0:8"

```
