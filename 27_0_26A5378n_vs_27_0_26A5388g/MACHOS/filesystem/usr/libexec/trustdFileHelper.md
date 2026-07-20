## trustdFileHelper

> `/usr/libexec/trustdFileHelper`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__objc_methtype`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-62460.0.38.0.1
-  __TEXT.__text: 0x29e0
-  __TEXT.__auth_stubs: 0x360
-  __TEXT.__objc_stubs: 0x440
-  __TEXT.__objc_methlist: 0x1e4
+62460.0.55.0.1
+  __TEXT.__text: 0x2ae4
+  __TEXT.__auth_stubs: 0x3a0
+  __TEXT.__objc_stubs: 0x620
+  __TEXT.__objc_methlist: 0x1dc
   __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x40a
-  __TEXT.__oslogstring: 0x26d
+  __TEXT.__cstring: 0x47e
+  __TEXT.__oslogstring: 0x259
   __TEXT.__objc_classname: 0x6a
-  __TEXT.__objc_methname: 0x4f4
+  __TEXT.__objc_methname: 0x5d4
   __TEXT.__objc_methtype: 0x15e
-  __TEXT.__gcc_except_tab: 0x30
-  __TEXT.__unwind_info: 0x150
-  __DATA_CONST.__const: 0x3a0
-  __DATA_CONST.__cfstring: 0x480
+  __TEXT.__gcc_except_tab: 0x18
+  __TEXT.__unwind_info: 0x138
+  __DATA_CONST.__const: 0x3c0
+  __DATA_CONST.__cfstring: 0x520
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__auth_got: 0x1c0
-  __DATA_CONST.__got: 0x78
+  __DATA_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__objc_arraydata: 0x60
+  __DATA_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__auth_got: 0x1e0
+  __DATA_CONST.__got: 0xb0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x2e8
-  __DATA.__objc_selrefs: 0x1d0
+  __DATA.__objc_selrefs: 0x248
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120
   __DATA.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
+  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/Versions/A/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 70
-  Symbols:   79
-  CStrings:  153
+  Functions: 68
+  Symbols:   92
+  CStrings:  176
 
Symbols:
+ _NSCocoaErrorDomain
+ _NSFileGroupOwnerAccountID
+ _NSFileOwnerAccountID
+ _NSFilePosixPermissions
+ _NSMultipleUnderlyingErrorsKey
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSNumber
+ _dispatch_after
+ _dispatch_get_global_queue
+ _dispatch_time
+ _xpc_transaction_exit_clean
CStrings:
+ ""
+ "URLByAppendingPathComponent:"
+ "ValidCacheFiles"
+ "addObject:"
+ "array"
+ "code"
+ "count"
+ "domain"
+ "failed to fix trustd file permissions"
+ "failed to set attributes on %s: %s"
+ "firstObject"
+ "fixTrustdPermissions:"
+ "i"
+ "length"
+ "lifecycle"
+ "localizedDescription"
+ "mutableCopy"
+ "numberWithUnsignedShort:"
+ "objectForKeyedSubscript:"
+ "path"
+ "protected trustd directory unavailable"
+ "setAttributes:ofItemAtPath:error:"
+ "setObject:forKeyedSubscript:"
+ "unsignedShortValue"
+ "valid.sqlite3-journal"
+ "valid.sqlite3-shm"
+ "valid.sqlite3-wal"
+ "will exit when clean"
- ".valid_replace"
- "changeOwnerOfValidFile:error:"
- "failed to change owner of %s: %s"
- "failed to fix Valid permissions for trustd"
- "fixValidPermissions:"
```
