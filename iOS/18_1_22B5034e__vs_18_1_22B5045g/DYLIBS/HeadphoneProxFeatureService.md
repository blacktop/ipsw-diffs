## HeadphoneProxFeatureService

> `/System/Library/PrivateFrameworks/HeadphoneProxFeatureService.framework/HeadphoneProxFeatureService`

```diff

-21.5.0.0.0
-  __TEXT.__text: 0x8e38
-  __TEXT.__auth_stubs: 0x730
-  __TEXT.__const: 0x216
-  __TEXT.__cstring: 0x5b2
-  __TEXT.__oslogstring: 0xdc1
-  __TEXT.__swift5_typeref: 0x19b
-  __TEXT.__swift5_capture: 0x68
-  __TEXT.__swift5_reflstr: 0xb5
+21.9.1.0.0
+  __TEXT.__text: 0xb1e4
+  __TEXT.__auth_stubs: 0x770
+  __TEXT.__const: 0x22a
+  __TEXT.__cstring: 0x642
+  __TEXT.__swift5_typeref: 0x1e9
+  __TEXT.__swift5_capture: 0x88
+  __TEXT.__oslogstring: 0x10c1
+  __TEXT.__swift5_reflstr: 0x101
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__swift5_fieldmd: 0xac
-  __TEXT.__constg_swiftt: 0x150
+  __TEXT.__swift5_fieldmd: 0xd0
+  __TEXT.__constg_swiftt: 0x190
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x190
-  __TEXT.__objc_methname: 0x211
-  __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x90
+  __TEXT.__unwind_info: 0x1f0
+  __TEXT.__objc_methname: 0x260
+  __DATA_CONST.__got: 0x98
+  __DATA_CONST.__const: 0xc0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc0
+  __DATA_CONST.__objc_selrefs: 0xe0
   __DATA_CONST.__objc_protorefs: 0x8
-  __AUTH_CONST.__auth_got: 0x398
+  __AUTH_CONST.__auth_got: 0x3b8
   __AUTH_CONST.__auth_ptr: 0x88
-  __AUTH_CONST.__const: 0x350
-  __AUTH_CONST.__objc_const: 0x228
+  __AUTH_CONST.__const: 0x408
+  __AUTH_CONST.__objc_const: 0x268
   __AUTH.__objc_data: 0x20
-  __DATA.__data: 0x50
+  __DATA.__data: 0x60
   __DATA.__bss: 0x180
-  __DATA_DIRTY.__data: 0x188
+  __DATA_DIRTY.__data: 0x1d8
   __DATA_DIRTY.__bss: 0x28
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices
+  - /System/Library/PrivateFrameworks/HearingModeService.framework/HearingModeService
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_errno.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 127
-  Symbols:   139
-  CStrings:  106
+  Functions: 161
+  Symbols:   156
+  CStrings:  123
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ ___stack_chk_guard
+ _OBJC_CLASS_$_HMServiceClient
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ _objc_retain_x25
+ _objc_release_x26
+ __swift_stdlib_bridgeErrorToNSError
+ _OBJC_CLASS_$_HMDeviceRecord
+ ___stack_chk_fail
CStrings:
+ "HeadphoneProxFeatureService: shouldShowWhatsNewCard: device does not support head gesture, Return false %!s(MISSING) cbDevice: %!@(MISSING)"
+ "hmsClient"
+ "HeadphoneProxFeatureManager: %!s(MISSING): %!l(MISSING)d failed to acitivate HMServiceClient %!@(MISSING)"
+ "HeadphoneProxFeatureManager: %!s(MISSING): %!l(MISSING)d record received %!@(MISSING)"
+ "HeadphoneProxFeatureService: shouldShowHeartRateMonitor: Invalid Device, Return %!s(MISSING) %!s(MISSING)"
+ "HeadphoneProxFeatureService: hearingRecordWithDevice: %!s(MISSING) %!s(MISSING) %!s(MISSING) %!s(MISSING)"
+ "productID"
+ "setDeviceRecordChangedHandler:"
+ "HeadphoneProxFeatureManager: %!s(MISSING): %!l(MISSING)d hearing client invalidated! Retrying to standup discovery stack"
+ "v16@?0@\"HMDeviceRecord\"8"
+ "HeartRateMonitor"
+ "heartRateVersion"
+ "connectedRecords"
+ "configHearingModeClient()"
+ "HeadphoneProxFeatureManager: %!s(MISSING): %!l(MISSING)d hearing client interrupted! Retrying to standup discovery stack"
+ "setHeartRateVersion:"
+ "HeadphoneProxFeatureService: [%!s(MISSING)] shouldShowHeartRateMonitor: %!s(MISSING), Current Version: %!s(MISSING), Taget Version: %!s(MISSING)"
+ "HeadphoneProxFeatureService: [%!s(MISSING)] setProxCardShowedFeatures: heartRateMonitor: %!s(MISSING) -> %!s(MISSING)"
- "HeadphoneProxFeatureService: shouldShowWhatsNewCard: device does not support head gesture, Return false %!s(MISSING)"

```
