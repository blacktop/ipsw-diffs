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

-274.1.1.0.0
-  __TEXT.__text: 0x89e54
-  __TEXT.__auth_stubs: 0x1370
-  __TEXT.__objc_stubs: 0x8500
-  __TEXT.__objc_methlist: 0x3c54
-  __TEXT.__cstring: 0x4eba
-  __TEXT.__objc_methname: 0x880a
+274.40.15.0.0
+  __TEXT.__text: 0x8ad44
+  __TEXT.__auth_stubs: 0x1390
+  __TEXT.__objc_stubs: 0x8680
+  __TEXT.__objc_methlist: 0x3cbc
+  __TEXT.__cstring: 0x4f62
+  __TEXT.__objc_methname: 0x8979
   __TEXT.__objc_classname: 0x5c6
-  __TEXT.__objc_methtype: 0x1237
-  __TEXT.__const: 0x11563
-  __TEXT.__gcc_except_tab: 0x161c
-  __TEXT.__oslogstring: 0xa477
-  __TEXT.__unwind_info: 0x36b8
-  __DATA_CONST.__const: 0xec98
-  __DATA_CONST.__cfstring: 0x47e0
+  __TEXT.__objc_methtype: 0x12a8
+  __TEXT.__const: 0x115c3
+  __TEXT.__gcc_except_tab: 0x16a8
+  __TEXT.__oslogstring: 0xa5ea
+  __TEXT.__unwind_info: 0x3738
+  __DATA_CONST.__const: 0xedc0
+  __DATA_CONST.__cfstring: 0x48e0
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xf8
-  __DATA_CONST.__objc_intobj: 0x18c0
-  __DATA_CONST.__objc_arraydata: 0x408
-  __DATA_CONST.__objc_arrayobj: 0x570
+  __DATA_CONST.__objc_intobj: 0x18f0
+  __DATA_CONST.__objc_arraydata: 0x410
+  __DATA_CONST.__objc_arrayobj: 0x588
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x9c8
-  __DATA_CONST.__got: 0x4f8
+  __DATA_CONST.__auth_got: 0x9d8
+  __DATA_CONST.__got: 0x510
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA.__objc_const: 0x8968
-  __DATA.__objc_selrefs: 0x2540
-  __DATA.__objc_ivar: 0x418
+  __DATA.__objc_const: 0x89e0
+  __DATA.__objc_selrefs: 0x25a8
+  __DATA.__objc_ivar: 0x424
   __DATA.__objc_data: 0xe10
-  __DATA.__data: 0x2a50
+  __DATA.__data: 0x2a78
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4117
-  Symbols:   464
-  CStrings:  3596
+  Functions: 4145
+  Symbols:   468
+  CStrings:  3637
 
Symbols:
+ _IOPMAssertionCreateWithProperties
+ _OBJC_CLASS_$_SUOSUInBoxUpdateConfiguration
+ __CFCopySystemVersionDictionary
+ ___kCFBooleanTrue
CStrings:
+ "$"
+ "@28@0:8@16B24"
+ "@52@0:8q16B24@28@36@44"
+ "Acquired full wake assertion ID: %{public}u"
+ "Acquiring full wake..."
+ "AppliesOnLidClose"
+ "AssertName"
+ "AssertType"
+ "Current build version: %@(%@); target version: %@"
+ "Failed to create full wake assertion with status: 0x%x"
+ "Failed to install factory assets."
+ "Failed to purge asset file: %{public}@"
+ "Failed to release full wake assertion with status: 0x%x"
+ "Idle timer fired with context: %{public}@"
+ "Initializing MIBUSUController with delegate: %{public}@, use SSDC: %{public}d"
+ "Overriding personalization server URL to SSDC: %{public}@"
+ "Personalization shutdown timestamp set to %{public}@"
+ "Releasing full wake..."
+ "SigningServerForSU"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_idleTimerSource"
+ "TB,N,V_useSSDC"
+ "TB,N,V_useSSDCForSU"
+ "T{os_unfair_lock_s=I},N,V_idleTimerLock"
+ "UserIsActive"
+ "_fullWakeAssertionID"
+ "_handleIdleTimerWithContext:"
+ "_idleTimerLock"
+ "_idleTimerSource"
+ "_useSSDC"
+ "_useSSDCForSU"
+ "acquireFullWake"
+ "buildVersionWithoutSplat"
+ "com.apple.inboxupdaterd.lpmsu"
+ "https://ssdc.ist.apple.com:443"
+ "idleTimerLock"
+ "idleTimerSource"
+ "initWithDelegate:configuration:"
+ "initWithDelegate:useSSDC:"
+ "initWithStatus:personalizationComplete:workflowID:orderID:assetExpiryTimestamp:"
+ "releaseFullWake"
+ "setIdleTimerLock:"
+ "setIdleTimerSource:"
+ "setPersonalizationServerURL:"
+ "setUseSSDC:"
+ "setUseSSDCForSU:"
+ "useSSDC"
+ "useSSDCForSU"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
+ "{os_unfair_lock_s=I}16@0:8"
- "%"
- "@60@0:8q16B24@28@36@44@52"
- "Current build version: %@; target version: %@"
- "Idle timer fired with user info: %{public}@"
- "Initializing MIBUSUController with delegate: %{public}@"
- "T@\"NSDate\",&,N,V_shutdownTimestamp"
- "T@\"NSDate\",R,C,N,V_shutdownTimestamp"
- "initWithStatus:personalizationComplete:workflowID:orderID:shutdownTimestamp:assetExpiryTimestamp:"
- "setShutdownTimestamp:"
```
