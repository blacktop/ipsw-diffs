## servicesintelligenced

> `/System/Library/PrivateFrameworks/ServicesIntelligence.framework/servicesintelligenced`

```diff

-1.33.0.0.0
-  __TEXT.__text: 0x6588
-  __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__const: 0x132
-  __TEXT.__cstring: 0x5af
-  __TEXT.__swift5_typeref: 0xbc
+1.36.0.0.0
+  __TEXT.__text: 0x8560
+  __TEXT.__auth_stubs: 0x800
+  __TEXT.__objc_stubs: 0x100
+  __TEXT.__const: 0x19a
+  __TEXT.__swift5_typeref: 0xe6
+  __TEXT.__cstring: 0x1ef
+  __TEXT.__objc_methtype: 0x7f
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x48
-  __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__oslogstring: 0xe1
-  __TEXT.__swift5_capture: 0x98
-  __TEXT.__objc_methname: 0xb2
-  __TEXT.__swift5_types: 0x4
-  __TEXT.__swift_as_entry: 0x18
-  __TEXT.__swift_as_ret: 0x34
-  __TEXT.__unwind_info: 0x258
-  __TEXT.__eh_frame: 0x4e0
-  __DATA_CONST.__auth_got: 0x3e0
-  __DATA_CONST.__got: 0x108
-  __DATA_CONST.__auth_ptr: 0x48
-  __DATA_CONST.__const: 0x338
+  __TEXT.__constg_swiftt: 0x74
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_reflstr: 0x43
+  __TEXT.__swift5_fieldmd: 0x44
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__objc_classname: 0x23
+  __TEXT.__objc_methname: 0xed
+  __TEXT.__swift5_capture: 0xa4
+  __TEXT.__oslogstring: 0x253
+  __TEXT.__swift_as_entry: 0x1c
+  __TEXT.__swift_as_ret: 0x3c
+  __TEXT.__unwind_info: 0x290
+  __TEXT.__eh_frame: 0x5d8
+  __DATA_CONST.__auth_got: 0x408
+  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__auth_ptr: 0x60
+  __DATA_CONST.__const: 0x3d8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x38
-  __DATA.__data: 0x160
+  __DATA.__objc_const: 0xd8
+  __DATA.__objc_selrefs: 0x40
+  __DATA.__data: 0x180
   __DATA.__common: 0x10
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
-  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 94762004-BC8B-3F9F-B04A-F24B2F9E10BC
-  Functions: 123
-  Symbols:   188
-  CStrings:  39
+  UUID: 7BE6A7AB-26B1-32AF-94DB-334053CEAB3A
+  Functions: 140
+  Symbols:   197
+  CStrings:  43
 
Symbols:
+ _$s20ServicesIntelligence12SystemStatusOSQAAMc
+ _$s2os21OSAllocatedUnfairLockVMn
+ _$sSQ2eeoiySbx_xtFZTj
+ _$sSo13os_log_type_ta0A0E5debugABvgZ
+ _$ss13ManagedBufferCMn
+ _$ss6UInt32VMn
+ _$sypN
+ __swift_stdlib_bridgeErrorToNSError
+ _objc_release_x26
+ _objc_retain_x22
+ _objc_retain_x27
+ _objc_retain_x8
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_arrayDestroy
+ _swift_bridgeObjectRelease_n
+ _swift_getForeignTypeMetadata
- _$s10Foundation5NSLogyySS_s7CVarArg_pdtF
- _$s20ServicesIntelligence12SystemStatusOSYAAMc
- _$sSS6appendyySSF
- _$sSY8rawValue03RawB0QzvgTj
- _$ss11_StringGutsV4growyySiF
- _$ss26DefaultStringInterpolationV06appendC0yyxlF
- __swift_FORCE_LOAD_$_swiftCompression
- _objc_retain_x20
CStrings:
+ "Clearing expiration flag"
+ "In main bg task handler"
+ "In main shadow task"
+ "Main shadow task completed"
+ "Main task expired"
+ "Registering for XPC events subscription"
+ "Registering handler for the main bg task"
+ "SystemDB not ready; skipping configuration refresh"
+ "[%s] complete"
+ "[%s] completed"
+ "[%s] failed: %@"
+ "[%s] start"
+ "[%s]: %s"
+ "[%s]: Flushed %@ events from container: %s"
+ "[LaunchEvent] Received active account change event"
+ "[LaunchEvent] Received storefront change event"
+ "[listenForLaunchEvents] Missing handler for XPC event %s"
+ "_expirationReceived"
+ "com.apple.servicesintelligenced.launchevents.manBGTaskQueue"
+ "expirationLock"
+ "initializeSystemDB()"
+ "setExpirationHandler:"
- "Error during flush metrics: %s"
- "Flushed %@ events from container: %s"
- "[Daemon] Skipping configuration refresh - system database not ready"
- "[Daemon][LaunchEvent] Received active account change event"
- "[Daemon][LaunchEvent] Received periodic launch event"
- "[Daemon][LaunchEvent] Received storefront change event"
- "[Daemon][initializeSystemDB] System database initialization completed successfully"
- "[Daemon][initializeSystemDB] System database initialization failed: "
- "[Daemon][initializeSystemDB] about to initialize"
- "[Daemon][listenForLaunchEvents] Missing handler for XPC event "
- "[Daemon][listenForLaunchEvents] Registering for XPC events subscription"
- "[Daemon][listenForLaunchEvents] Registering for background system tasks subscription"
- "[Daemon][run] Initializing systemDB"
- "[Daemon][run] XPC & launch events setup"
- "[Daemon][shutdown] Daemon shutdown completed"
- "[Daemon][shutdown] Shutting down daemon"
- "com.apple.servicesintelligenced.launchevents.registration"

```
