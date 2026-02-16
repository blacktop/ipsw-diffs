## FindMyDeviceSharedConfigurationXPCService

> `/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceSharedConfigurationXPCService.xpc/FindMyDeviceSharedConfigurationXPCService`

```diff

-455.33.11.19.3
-  __TEXT.__text: 0x11bb4
-  __TEXT.__auth_stubs: 0xc30
-  __TEXT.__objc_methlist: 0x224
-  __TEXT.__const: 0x8e8
-  __TEXT.__cstring: 0x477
-  __TEXT.__swift5_typeref: 0x406
-  __TEXT.__objc_methname: 0x6ff
-  __TEXT.__swift5_capture: 0x224
-  __TEXT.__oslogstring: 0x882
+455.34.7.18.21
+  __TEXT.__text: 0x136f8
+  __TEXT.__auth_stubs: 0xbf0
+  __TEXT.__objc_stubs: 0x740
+  __TEXT.__objc_methlist: 0x204
+  __TEXT.__const: 0x8b8
+  __TEXT.__cstring: 0x314
+  __TEXT.__swift5_typeref: 0x3da
+  __TEXT.__objc_methname: 0x7d6
+  __TEXT.__swift5_capture: 0x228
+  __TEXT.__objc_methtype: 0x237
+  __TEXT.__oslogstring: 0x8b2
+  __TEXT.__objc_classname: 0x147
   __TEXT.__constg_swiftt: 0x1a8
-  __TEXT.__swift5_reflstr: 0x1c7
-  __TEXT.__swift5_fieldmd: 0x1c0
+  __TEXT.__swift5_reflstr: 0x1d7
+  __TEXT.__swift5_fieldmd: 0x1cc
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_types: 0x28
-  __TEXT.__objc_classname: 0x42
-  __TEXT.__objc_methtype: 0x22d
-  __TEXT.__swift_as_entry: 0xc
-  __TEXT.__swift_as_ret: 0xc
+  __TEXT.__swift_as_entry: 0x8
+  __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x348
-  __TEXT.__eh_frame: 0x2e8
-  __DATA_CONST.__auth_got: 0x618
-  __DATA_CONST.__got: 0x218
+  __TEXT.__unwind_info: 0x2e0
+  __TEXT.__eh_frame: 0x1c8
+  __DATA_CONST.__auth_got: 0x600
+  __DATA_CONST.__got: 0x210
   __DATA_CONST.__auth_ptr: 0x2c0
-  __DATA_CONST.__const: 0x840
+  __DATA_CONST.__const: 0x828
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA.__objc_const: 0x640
-  __DATA.__objc_selrefs: 0x2c0
+  __DATA.__objc_const: 0x618
+  __DATA.__objc_selrefs: 0x2b8
   __DATA.__objc_data: 0x170
   __DATA.__data: 0x400
-  __DATA.__bss: 0xa40
   __DATA.__common: 0x28
+  __DATA.__bss: 0xa40
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftMetal.dylib
-  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
-  - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6384014F-A950-34B3-86F3-F44FB3031AE0
-  Functions: 302
-  Symbols:   149
-  CStrings:  196
+  UUID: 8D7FD357-3739-36CD-825D-E49031B2E59C
+  Functions: 292
+  Symbols:   144
+  CStrings:  190
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ _objc_retain_x24
+ _swift_bridgeObjectRelease_n
- __swift_FORCE_LOAD_$_swiftMetal
- __swift_FORCE_LOAD_$_swiftOSLog
- __swift_FORCE_LOAD_$_swiftQuartzCore
- __swift_FORCE_LOAD_$_swiftsimd
- _swift_continuation_await
- _swift_continuation_init
- _swift_continuation_throwingResume
- _swift_continuation_throwingResumeWithError
CStrings:
+ "Failed to find device with UDID: %s"
+ "Failed to get coverage for UDID: %s, error: %@"
+ "FindMyDeviceSharedConfigurationXPCService"
+ "T&L batch coverage lookup completed successfully for %ld devices"
+ "T&L batch coverage lookup timed out"
+ "theftAndLossCoverageWithUDIDs:completion:"
- "Found %ld matching device for %ld"
- "Getting devices looking for %s"
- "Got %ld devices looking for %ld"
- "Got %ld devices looking for %s"
- "No matching device found"
- "getTheftAndLossCoverageWithUDIDs:reply:"
- "requestTheftAndLossCFUWithString:andReply:"
- "v32@0:8@\"FMDSharedConfigurationFollowUpEntry\"16@?<v@?@\"NSError\">24"

```
