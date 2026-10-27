## QuarantineService

> `/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/Versions/A/XPCServices/QuarantineService.xpc/Contents/MacOS/QuarantineService`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1857.0.0.0.0
-  __TEXT.__text: 0x548
-  __TEXT.__auth_stubs: 0x150
-  __TEXT.__objc_stubs: 0x1c0
+1857.1.9.100.0
+  __TEXT.__text: 0x19fc
+  __TEXT.__auth_stubs: 0x2c0
+  __TEXT.__objc_stubs: 0x3e0
   __TEXT.__objc_methlist: 0x16c
+  __TEXT.__cstring: 0x177
   __TEXT.__objc_classname: 0x5b
-  __TEXT.__objc_methname: 0x28a
-  __TEXT.__objc_methtype: 0x132
-  __TEXT.__gcc_except_tab: 0x88
-  __TEXT.__cstring: 0xd4
-  __TEXT.__const: 0x8
-  __TEXT.__unwind_info: 0xa8
-  __DATA_CONST.__const: 0x70
+  __TEXT.__objc_methname: 0x3ed
+  __TEXT.__objc_methtype: 0x13c
+  __TEXT.__gcc_except_tab: 0x2b4
+  __TEXT.__const: 0x28
+  __TEXT.__oslogstring: 0x2d8
+  __TEXT.__unwind_info: 0x118
+  __DATA_CONST.__const: 0x120
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0xb8
-  __DATA_CONST.__got: 0x28
+  __DATA_CONST.__auth_got: 0x170
+  __DATA_CONST.__got: 0x80
   __DATA.__objc_const: 0x2a8
-  __DATA.__objc_selrefs: 0x128
+  __DATA.__objc_selrefs: 0x1b0
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/DesktopServicesPriv.framework/Versions/A/DesktopServicesPriv
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 10
-  Symbols:   41
-  CStrings:  69
+  Functions: 33
+  Symbols:   75
+  CStrings:  102
 
Symbols:
+ _NSCocoaErrorDomain
+ _NSFilePathErrorKey
+ _NSPOSIXErrorDomain
+ _NSURLErrorKey
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSString
+ __Block_object_assign
+ __Block_object_dispose
+ ___error
+ __os_log_error_impl
+ __qtn_file_get_flags
+ __qtn_file_init_with_path
+ __qtn_file_set_flags
+ __qtn_xattr_name
+ _close
+ _fchflags
+ _fchmod
+ _fts_set
+ _geteuid
+ _getxattr
+ _lchflags
+ _lchmod
+ _lstat
+ _objc_retainAutoreleaseReturnValue
+ _objc_retainBlock
+ _objc_storeStrong
+ _open
+ _os_log_create
+ _os_log_type_enabled
+ _strlen
CStrings:
+ "Could not restore the flags of a walked directory (errno %d)"
+ "Could not restore the mode of a walked directory (errno %d)"
+ "Quarantine propagation did not cover the whole target (status %d)"
+ "Quarantine walk could not clear the flags of a directory (flags %x, errno %d)"
+ "Quarantine walk could not enter an entry (fts_info %d, errno %d)"
+ "Quarantine walk could not hold open a directory it widened (errno %d)"
+ "Quarantine walk could not label an entry (fts_info %d, errno %d)"
+ "Quarantine walk could not open up a directory (mode %o, errno %d)"
+ "Quarantine walk could not stat an entry it could not read (errno %d)"
+ "Quarantine walk reached another volume inside the target"
+ "Quarantine walk was blocked by something other than the mode (mode %o)"
+ "QuarantineWalk"
+ "arrayWithObjects:count:"
+ "com.apple.DesktopServices"
+ "dataWithBytes:length:"
+ "dictionary"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "errorWithDomain:code:userInfo:"
+ "intValue"
+ "mutableCopy"
+ "numberWithInt:"
+ "numberWithUnsignedInt:"
+ "numberWithUnsignedShort:"
+ "objectAtIndexedSubscript:"
+ "objectForKeyedSubscript:"
+ "removeObjectForKey:"
+ "setObject:forKeyedSubscript:"
+ "stringWithUTF8String:"
+ "unsignedIntValue"
+ "userInfo"
+ "v16@?0^{_ftsent=^{_ftsent}^{_ftsent}^{_ftsent}q^v**iiSSQiSsSSS^{stat}[1c]}8"
+ "v20@?0i8r*12"
+ "v32@?0@\"NSData\"8@\"NSArray\"16^B24"
+ "v40@0:8@\"NSData\"16@\"DSSandboxingURLWrapper\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSData\"16@\"DSSandboxingURLWrapper\"24@?<v@?>32"
```
