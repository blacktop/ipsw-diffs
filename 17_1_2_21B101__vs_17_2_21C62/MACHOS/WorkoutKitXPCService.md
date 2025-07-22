## WorkoutKitXPCService

> `/System/Library/PrivateFrameworks/WorkoutKitServices.framework/XPCServices/WorkoutKitXPCService.xpc/WorkoutKitXPCService`

```diff

-748.12.0.0.0
-  __TEXT.__text: 0x10920
-  __TEXT.__auth_stubs: 0xdb0
+749.20.0.0.0
+  __TEXT.__text: 0x11ec4
+  __TEXT.__auth_stubs: 0xe00
   __TEXT.__objc_methlist: 0x124
-  __TEXT.__objc_methname: 0x912
+  __TEXT.__objc_methname: 0x95f
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0xb5e
+  __TEXT.__cstring: 0xd1e
   __TEXT.__const: 0x110
   __TEXT.__constg_swiftt: 0x110
   __TEXT.__swift5_typeref: 0x333

   __TEXT.__objc_classname: 0x59
   __TEXT.__objc_methtype: 0x348
   __TEXT.__swift5_capture: 0x48c
-  __TEXT.__unwind_info: 0x34c
-  __TEXT.__eh_frame: 0x2a0
-  __DATA_CONST.__auth_got: 0x6d8
-  __DATA_CONST.__got: 0x1e8
+  __TEXT.__unwind_info: 0x378
+  __TEXT.__eh_frame: 0x378
+  __DATA_CONST.__auth_got: 0x700
+  __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__auth_ptr: 0x30
   __DATA_CONST.__const: 0xc70
   __DATA_CONST.__objc_classlist: 0x10

   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x750
-  __DATA.__objc_selrefs: 0x200
+  __DATA.__objc_selrefs: 0x220
   __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0xd0
+  __DATA.__objc_classrefs: 0xd8
   __DATA.__objc_data: 0x200
   __DATA.__data: 0x370
   __DATA.__common: 0x18

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7BE290C3-E3C0-3734-83B2-01A15378F33D
-  Functions: 312
+  UUID: 43A39866-7686-364E-8890-9DF8AA5F1541
+  Functions: 318
   Symbols:   157
-  CStrings:  184
+  CStrings:  193
 
Symbols:
+ _OBJC_CLASS_$_LSApplicationExtensionRecord
- _objc_retain_x27
CStrings:
+ "Requesting to remove %ld scheduled workouts for %s"
+ "Requesting to store %ld scheduled workouts for %s"
+ "WorkoutKitXPCService: failed to deserialize %s - skipping scheduling"
+ "WorkoutKitXPCService: failed to retrieve container bundleId from extension bundleId: %s"
+ "WorkoutKitXPCService: failed to retrieve extension app record for %s due to: %s"
+ "WorkoutKitXPCService: invalid %s configuration for %s - skipping scheduling"
+ "WorkoutKitXPCService: remapped extension bundleId: %s to container bundleId: %s"
+ "bundleIdentifier"
+ "code"
+ "containingBundleRecord"
+ "initWithBundleIdentifier:error:"
- "Requesting to remove %ld scheduled workouts"
- "Requesting to store %ld scheduled workouts"

```
