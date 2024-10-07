## LockedCameraCapture

> `/System/Library/Frameworks/LockedCameraCapture.framework/LockedCameraCapture`

```diff

-58.1.1.0.0
-  __TEXT.__text: 0xab20
-  __TEXT.__auth_stubs: 0xa70
-  __TEXT.__const: 0x504
-  __TEXT.__cstring: 0x569
+58.1.3.101.0
+  __TEXT.__text: 0xb4f4
+  __TEXT.__auth_stubs: 0xaa0
+  __TEXT.__const: 0x514
+  __TEXT.__cstring: 0x579
   __TEXT.__swift5_typeref: 0x3a6
-  __TEXT.__swift5_capture: 0x140
-  __TEXT.__swift5_reflstr: 0x1d8
+  __TEXT.__swift5_capture: 0x178
+  __TEXT.__swift5_reflstr: 0x1f8
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__swift5_fieldmd: 0x1d8
-  __TEXT.__constg_swiftt: 0x3a4
+  __TEXT.__swift5_fieldmd: 0x1fc
+  __TEXT.__constg_swiftt: 0x3d4
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x20
-  __TEXT.__oslogstring: 0x206
-  __TEXT.__unwind_info: 0x378
-  __TEXT.__eh_frame: 0x510
+  __TEXT.__oslogstring: 0x2e5
+  __TEXT.__unwind_info: 0x3a0
+  __TEXT.__eh_frame: 0x560
   __TEXT.__objc_classname: 0x35
-  __TEXT.__objc_methname: 0x29d
+  __TEXT.__objc_methname: 0x2c0
   __TEXT.__objc_methtype: 0xad
-  __DATA_CONST.__got: 0x160
-  __DATA_CONST.__const: 0xd8
+  __DATA_CONST.__got: 0x170
+  __DATA_CONST.__const: 0xe0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x90
+  __DATA_CONST.__objc_selrefs: 0xa0
   __DATA_CONST.__objc_protorefs: 0x18
-  __AUTH_CONST.__auth_got: 0x538
+  __AUTH_CONST.__auth_got: 0x550
   __AUTH_CONST.__auth_ptr: 0x1d8
-  __AUTH_CONST.__const: 0x418
+  __AUTH_CONST.__const: 0x490
   __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0xa48
+  __AUTH_CONST.__objc_const: 0xaa8
   __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0x448
-  __DATA.__data: 0x450
+  __AUTH.__data: 0x490
+  __DATA.__data: 0x480
   __DATA.__bss: 0x480
-  __DATA.__common: 0x40
+  __DATA.__common: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/ExtensionKit.framework/ExtensionKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 248
-  Symbols:   144
-  CStrings:  104
+  Functions: 264
+  Symbols:   151
+  CStrings:  112
 
Symbols:
+ _OBJC_CLASS_$_UIApplication
+ _UIApplicationDidBecomeActiveNotification
+ __swift_FORCE_LOAD_$_swiftCompression
+ _objc_release_x24
+ _swift_unknownObjectRelease_n
CStrings:
+ "Application is foreground, begin file system observation"
+ "File system observation is ended"
+ "File system observation is suspended"
+ "Resuming file system observation"
+ "applicationState"
+ "didBecomeActiveObserver"
+ "observing"
+ "resumeObservation: Unable to resume file system observation. Already observing: %!{(MISSING)bool}d, cancelled: %!{(MISSING)bool}d"
+ "sharedApplication"
- "resumeObservation: Unable to resume observation because observation is already ended."

```
