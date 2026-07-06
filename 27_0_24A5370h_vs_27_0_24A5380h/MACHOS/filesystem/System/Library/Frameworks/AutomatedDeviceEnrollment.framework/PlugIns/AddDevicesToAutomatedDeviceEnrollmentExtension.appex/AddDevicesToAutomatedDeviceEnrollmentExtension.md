## AddDevicesToAutomatedDeviceEnrollmentExtension

> `/System/Library/Frameworks/AutomatedDeviceEnrollment.framework/PlugIns/AddDevicesToAutomatedDeviceEnrollmentExtension.appex/AddDevicesToAutomatedDeviceEnrollmentExtension`

```diff

-  __TEXT.__text: 0x90d30
-  __TEXT.__auth_stubs: 0x2540
-  __TEXT.__objc_stubs: 0x10c0
+  __TEXT.__text: 0x951e4
+  __TEXT.__auth_stubs: 0x25e0
+  __TEXT.__objc_stubs: 0x1100
   __TEXT.__objc_methlist: 0x55c
-  __TEXT.__const: 0x8874
-  __TEXT.__swift5_typeref: 0x892c
-  __TEXT.__swift5_fieldmd: 0x1f4c
-  __TEXT.__constg_swiftt: 0x3480
-  __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0x2790
+  __TEXT.__const: 0x8ab4
+  __TEXT.__swift5_typeref: 0x8a34
+  __TEXT.__swift5_fieldmd: 0x2054
+  __TEXT.__constg_swiftt: 0x366c
+  __TEXT.__swift5_builtin: 0x50
+  __TEXT.__swift5_reflstr: 0x290c
   __TEXT.__swift5_assocty: 0x568
   __TEXT.__swift5_protos: 0x54
-  __TEXT.__swift5_proto: 0x410
-  __TEXT.__swift5_types: 0x234
-  __TEXT.__objc_classname: 0x174e
-  __TEXT.__objc_methname: 0x2285
+  __TEXT.__swift5_proto: 0x41c
+  __TEXT.__swift5_types: 0x240
+  __TEXT.__objc_classname: 0x17fe
+  __TEXT.__objc_methname: 0x2345
   __TEXT.__objc_methtype: 0x873
-  __TEXT.__oslogstring: 0x2060
-  __TEXT.__cstring: 0x3804
-  __TEXT.__swift5_capture: 0xa5c
+  __TEXT.__oslogstring: 0x2120
+  __TEXT.__cstring: 0x4155
+  __TEXT.__swift5_capture: 0xaac
   __TEXT.__swift_as_entry: 0x160
   __TEXT.__swift_as_ret: 0x170
-  __TEXT.__swift_as_cont: 0x35c
-  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__swift_as_cont: 0x368
+  __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x2550
-  __TEXT.__eh_frame: 0x4318
-  __DATA_CONST.__const: 0x4898
-  __DATA_CONST.__objc_classlist: 0x1c8
+  __TEXT.__unwind_info: 0x2640
+  __TEXT.__eh_frame: 0x44e8
+  __DATA_CONST.__const: 0x4a40
+  __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__auth_got: 0x12a8
-  __DATA_CONST.__got: 0x7a8
-  __DATA_CONST.__auth_ptr: 0xdf0
-  __DATA.__objc_const: 0x37f0
-  __DATA.__objc_selrefs: 0x610
-  __DATA.__objc_data: 0xef0
-  __DATA.__data: 0x6688
-  __DATA.__bss: 0x7b60
-  __DATA.__common: 0x120
+  __DATA_CONST.__auth_got: 0x12f8
+  __DATA_CONST.__got: 0x7c0
+  __DATA_CONST.__auth_ptr: 0xe08
+  __DATA.__objc_const: 0x3ac0
+  __DATA.__objc_selrefs: 0x618
+  __DATA.__objc_data: 0xfe8
+  __DATA.__data: 0x6928
+  __DATA.__bss: 0x7c60
+  __DATA.__common: 0x1e1
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/AutomatedDeviceEnrollment.framework/AutomatedDeviceEnrollment

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2924
-  Symbols:   278
-  CStrings:  906
+  Functions: 2999
+  Symbols:   284
+  CStrings:  950
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift5_entry : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
Symbols:
+ _NSDebugDescriptionErrorKey
+ _OBJC_CLASS_$_CATRemoteTaskOperation
+ _swift_isEscapingClosureAtFileLocation
+ _swift_task_deinitOnExecutor
+ _swift_task_getMainExecutor
+ _swift_task_isCurrentExecutor
CStrings:
+ "%s: transport event %{public}s — publishing transportDisconnected"
+ "AddDevicesToAutomatedDeviceEnrollmentExtension/AXMEnroller.swift"
+ "AddDevicesToAutomatedDeviceEnrollmentExtension/FakeCatalaystRequestPerforming.swift"
+ "An administrator for your organization needs to accept the latest Terms and Conditions in Apple School Manager or Apple Business before you can continue adding devices."
+ "CATRemoteTaskOperation.invalidRemoteTask returned nil in a test fake"
+ "Cannot Read Device Information"
+ "Enrollment Failed"
+ "Enrollment Timed Out"
+ "Fatal error"
+ "Incorrect actor executor assumption; Expected same executor as "
+ "Message for the alert shown when fetching the device's serial number or UDID fails after pairing."
+ "Message for the alert shown when sending enrollment information to the paired device fails."
+ "Message for the alert shown when the connection to the paired device is lost during enrollment."
+ "Message for the alert shown when the device cannot be enrolled because no Wi-Fi or network configuration is available to share."
+ "Message for the alert shown when the post-pair enrollment exceeds the per-operation timeout."
+ "Message for the alert shown when the user signs out before a paired device finishes enrolling."
+ "No Network Information"
+ "Sign in authentication mode could not be fetched: %@"
+ "Sign-In Required"
+ "The account used to start enrollment is no longer signed in. Please sign in again and retry adding the device."
+ "The connection to the device was lost before enrollment could finish. Please try adding the device again."
+ "The device could not be enrolled. Please try adding the device again."
+ "The device could not provide the information needed to enroll it. Please try adding the device again."
+ "The device took too long to respond. Please try adding the device again."
+ "There is no Wi-Fi or network configuration to share with the device. Please check your network selection and try again."
+ "Title for the alert shown when fetching the device's serial number or UDID fails after pairing."
+ "Title for the alert shown when sending enrollment information to the paired device fails."
+ "Title for the alert shown when the connection to the paired device is lost during enrollment."
+ "Title for the alert shown when the device cannot be enrolled because no Wi-Fi or network configuration is available to share."
+ "Title for the alert shown when the post-pair enrollment exceeds the per-operation timeout."
+ "Title for the alert shown when the user signs out before a paired device finishes enrolling."
+ "Unexpected resultObject from prerequisites operation: %{public}s"
+ "_TtC46AddDevicesToAutomatedDeviceEnrollmentExtension26FakeKeyValueCodableStorage"
+ "_TtC46AddDevicesToAutomatedDeviceEnrollmentExtension30FakeCatalaystRequestPerforming"
+ "fetchNonceError"
+ "handleTransportEvent(_:)"
+ "invalidRemoteTaskWithRequest:error:"
+ "isEnrollmentInFlight"
+ "isWatchdogArmed"
+ "lastReturnedOperation"
+ "nonceFetchTask"
+ "operationError"
+ "operationTimeout"
+ "transportEventSubject"
+ "transportSubscription"
+ "watchdogTimer"
- "An administrator for your organization needs to accept the latest Terms and Conditions in Apple School Manager or Apple Business in order to continue adding devices."
- "Unexpected resultObject from %@"

```
