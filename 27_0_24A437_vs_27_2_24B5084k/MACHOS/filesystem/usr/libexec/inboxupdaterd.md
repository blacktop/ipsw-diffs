## inboxupdaterd

> `/usr/libexec/inboxupdaterd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-274.2.2.0.0
-  __TEXT.__text: 0x8bb60
-  __TEXT.__auth_stubs: 0x1520
-  __TEXT.__objc_stubs: 0x8960
-  __TEXT.__objc_methlist: 0x4164
-  __TEXT.__cstring: 0x550d
-  __TEXT.__objc_methname: 0x9040
+274.40.15.0.0
+  __TEXT.__text: 0x8c404
+  __TEXT.__auth_stubs: 0x1530
+  __TEXT.__objc_stubs: 0x8ac0
+  __TEXT.__objc_methlist: 0x41f4
+  __TEXT.__cstring: 0x5593
+  __TEXT.__objc_methname: 0x9190
   __TEXT.__objc_classname: 0x687
-  __TEXT.__objc_methtype: 0x1792
-  __TEXT.__const: 0x11573
-  __TEXT.__gcc_except_tab: 0x1778
-  __TEXT.__oslogstring: 0xa8b7
+  __TEXT.__objc_methtype: 0x1806
+  __TEXT.__const: 0x115d3
+  __TEXT.__gcc_except_tab: 0x17a0
+  __TEXT.__oslogstring: 0xa92c
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x38f0
-  __DATA_CONST.__const: 0xf2f0
-  __DATA_CONST.__cfstring: 0x4cc0
+  __TEXT.__unwind_info: 0x3930
+  __DATA_CONST.__const: 0xf358
+  __DATA_CONST.__cfstring: 0x4d40
   __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x110
-  __DATA_CONST.__objc_intobj: 0x1ae8
-  __DATA_CONST.__objc_arraydata: 0x4d8
-  __DATA_CONST.__objc_arrayobj: 0x600
+  __DATA_CONST.__objc_intobj: 0x1b18
+  __DATA_CONST.__objc_arraydata: 0x4e0
+  __DATA_CONST.__objc_arrayobj: 0x618
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0xaa0
-  __DATA_CONST.__got: 0x598
+  __DATA_CONST.__auth_got: 0xaa8
+  __DATA_CONST.__got: 0x5a0
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA.__objc_const: 0x99e8
-  __DATA.__objc_selrefs: 0x2750
-  __DATA.__objc_ivar: 0x450
+  __DATA.__objc_const: 0x9a80
+  __DATA.__objc_selrefs: 0x27b0
+  __DATA.__objc_ivar: 0x45c
   __DATA.__objc_data: 0xf00
-  __DATA.__data: 0x25c8
+  __DATA.__data: 0x25f0
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4271
-  Symbols:   510
-  CStrings:  3764
+  Functions: 4288
+  Symbols:   511
+  CStrings:  3792
 
Symbols:
+ __CFCopySystemVersionDictionary
CStrings:
+ "@28@0:8@16B24"
+ "Current build version: %@(%@); target version: %@"
+ "Failed to install factory assets."
+ "Failed to purge asset file: %{public}@"
+ "Idle timer fired with context: %{public}@"
+ "Initializing MIBUSUController with delegate: %{public}@, use SSDC: %{public}d"
+ "Overriding personalization server URL to SSDC: %{public}@"
+ "SigningServerForSU"
+ "TB,N,V_useSSDC"
+ "TB,N,V_useSSDCForSU"
+ "T{os_unfair_lock_s=I},N,V_idleTimerLock"
+ "_handleIdleTimerWithContext:"
+ "_idleTimerLock"
+ "_useSSDC"
+ "_useSSDCForSU"
+ "acquireFullWake"
+ "buildVersionWithoutSplat"
+ "https://ssdc.ist.apple.com:443"
+ "idleTimerLock"
+ "initWithDelegate:useSSDC:"
+ "releaseFullWake"
+ "setIdleTimerLock:"
+ "setPersonalizationServerURL:"
+ "setUseSSDC:"
+ "setUseSSDCForSU:"
+ "useSSDC"
+ "useSSDCForSU"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
+ "{os_unfair_lock_s=I}16@0:8"
- "Idle timer fired with user info: %{public}@"
- "Initializing MIBUSUController with delegate: %{public}@"
```
