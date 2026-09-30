## powerexperienced

> `/usr/libexec/powerexperienced`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-168.0.0.0.0
-  __TEXT.__text: 0x1666c
-  __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_stubs: 0x2dc0
-  __TEXT.__objc_methlist: 0x1e3c
+173.0.0.0.0
+  __TEXT.__text: 0x16800
+  __TEXT.__auth_stubs: 0x580
+  __TEXT.__objc_stubs: 0x2e00
+  __TEXT.__objc_methlist: 0x1e64
   __TEXT.__const: 0x138
-  __TEXT.__cstring: 0x11a2
-  __TEXT.__objc_methname: 0x35f0
-  __TEXT.__oslogstring: 0x2536
+  __TEXT.__cstring: 0x11c2
+  __TEXT.__objc_methname: 0x363a
+  __TEXT.__oslogstring: 0x2569
   __TEXT.__objc_classname: 0x327
-  __TEXT.__objc_methtype: 0x665
+  __TEXT.__objc_methtype: 0x6cb
   __TEXT.__gcc_except_tab: 0x48
   __TEXT.__dlopen_cstrs: 0x8d
   __TEXT.__unwind_info: 0x5b0
-  __DATA_CONST.__const: 0x880
-  __DATA_CONST.__cfstring: 0x1120
+  __DATA_CONST.__const: 0x8a0
+  __DATA_CONST.__cfstring: 0x1180
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0xb8
-  __DATA_CONST.__objc_intobj: 0xa8
-  __DATA_CONST.__auth_got: 0x2a8
+  __DATA_CONST.__objc_intobj: 0xc0
+  __DATA_CONST.__auth_got: 0x2d0
   __DATA_CONST.__got: 0xd0
-  __DATA.__objc_const: 0x4660
-  __DATA.__objc_selrefs: 0xe58
-  __DATA.__objc_ivar: 0x210
+  __DATA.__objc_const: 0x4690
+  __DATA.__objc_selrefs: 0xe78
+  __DATA.__objc_ivar: 0x214
   __DATA.__objc_data: 0x7d0
   __DATA.__data: 0x420
-  __DATA.__bss: 0x228
+  __DATA.__bss: 0x238
   __DATA.__common: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 721
-  Symbols:   120
-  CStrings:  1190
+  Functions: 727
+  Symbols:   125
+  CStrings:  1203
 
Symbols:
+ _CFEqual
+ _CFRelease
+ _MGCopyAnswer
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
CStrings:
+ "NonUI"
+ "ReleaseType"
+ "Restricted perf mode not supported on non-UI build"
+ "T@\"NSMutableDictionary\",&,N,V_currentContext"
+ "T{os_unfair_lock_s=I},N,V_lock"
+ "VendorNonUI"
+ "_lock"
+ "contextSnapshot"
+ "copy"
+ "lock"
+ "setLock:"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
+ "{os_unfair_lock_s=I}16@0:8"
- "T@\"NSMutableDictionary\",&,V_currentContext"
```
