## powerexperienced

> `/usr/libexec/powerexperienced`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-168.0.0.0.0
-  __TEXT.__text: 0x1a93c
-  __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_stubs: 0x38e0
-  __TEXT.__objc_methlist: 0x237c
-  __TEXT.__const: 0x138
-  __TEXT.__cstring: 0x12f1
-  __TEXT.__objc_methname: 0x414c
-  __TEXT.__oslogstring: 0x308e
+173.0.0.0.0
+  __TEXT.__text: 0x1ad74
+  __TEXT.__auth_stubs: 0x730
+  __TEXT.__objc_stubs: 0x39c0
+  __TEXT.__objc_methlist: 0x23bc
+  __TEXT.__const: 0x148
+  __TEXT.__cstring: 0x1341
+  __TEXT.__objc_methname: 0x41f5
+  __TEXT.__oslogstring: 0x31b3
   __TEXT.__objc_classname: 0x400
-  __TEXT.__objc_methtype: 0x840
+  __TEXT.__objc_methtype: 0x8a6
   __TEXT.__gcc_except_tab: 0x48
   __TEXT.__dlopen_cstrs: 0x8d
-  __TEXT.__unwind_info: 0x748
-  __DATA_CONST.__const: 0x8d8
-  __DATA_CONST.__cfstring: 0x1340
+  __TEXT.__unwind_info: 0x758
+  __DATA_CONST.__const: 0x8f8
+  __DATA_CONST.__cfstring: 0x13e0
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0xd0
-  __DATA_CONST.__objc_intobj: 0xf0
-  __DATA_CONST.__auth_got: 0x378
+  __DATA_CONST.__objc_intobj: 0x108
+  __DATA_CONST.__auth_got: 0x3a8
   __DATA_CONST.__got: 0x188
-  __DATA.__objc_const: 0x56e0
-  __DATA.__objc_selrefs: 0x1138
-  __DATA.__objc_ivar: 0x268
+  __DATA.__objc_const: 0x5710
+  __DATA.__objc_selrefs: 0x1180
+  __DATA.__objc_ivar: 0x26c
   __DATA.__objc_data: 0x8c0
   __DATA.__data: 0x600
-  __DATA.__bss: 0x258
+  __DATA.__bss: 0x268
   __DATA.__common: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 835
-  Symbols:   169
-  CStrings:  1416
+  Functions: 843
+  Symbols:   175
+  CStrings:  1440
 
Symbols:
+ _CFEqual
+ _CFRelease
+ _MGCopyAnswer
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _sysctlbyname
CStrings:
+ "DataMigration: cached clean boot UUID=%{public}@"
+ "DataMigration: currentBootUUID=%{public}@, cachedBootUUID=%{public}@"
+ "DataMigration: failed to get boot UUID, skipping cache write"
+ "DataMigration: skipping check, already complete this boot (%@)"
+ "DataMigrationLastCleanBootUUID"
+ "NonUI"
+ "ReleaseType"
+ "Restricted perf mode not supported on non-UI build"
+ "T@\"NSMutableDictionary\",&,N,V_currentContext"
+ "T{os_unfair_lock_s=I},N,V_lock"
+ "VendorNonUI"
+ "_lock"
+ "contextSnapshot"
+ "copy"
+ "currentBootSessionUUID"
+ "isMigrationNeeded"
+ "kern.bootsessionuuid"
+ "lock"
+ "setLock:"
+ "setObject:forKey:"
+ "stringForKey:"
+ "stringWithUTF8String:"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
+ "{os_unfair_lock_s=I}16@0:8"
- "T@\"NSMutableDictionary\",&,V_currentContext"
```
