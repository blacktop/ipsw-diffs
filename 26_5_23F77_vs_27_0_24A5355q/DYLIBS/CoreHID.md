## CoreHID

> `/System/Library/PrivateFrameworks/CoreHID.framework/CoreHID`

```diff

-2238.120.5.0.0
-  __TEXT.__text: 0x3bffc
-  __TEXT.__auth_stubs: 0x1350
-  __TEXT.__const: 0xa8c8
-  __TEXT.__swift5_typeref: 0x9e0
+2353.0.0.0.1
+  __TEXT.__text: 0x3d97c
+  __TEXT.__const: 0xa8d0
+  __TEXT.__swift5_typeref: 0x9d0
   __TEXT.__cstring: 0x832
   __TEXT.__constg_swiftt: 0xe20
   __TEXT.__swift5_reflstr: 0xf4b7
   __TEXT.__swift5_fieldmd: 0x90a8
   __TEXT.__swift5_proto: 0x254
   __TEXT.__swift5_types: 0x130
-  __TEXT.__swift5_capture: 0x150
+  __TEXT.__swift5_capture: 0x180
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x24
+  __TEXT.__swift_as_cont: 0x8c
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_assocty: 0x2e8
   __TEXT.__oslogstring: 0x52
   __TEXT.__unwind_info: 0xc80
-  __TEXT.__eh_frame: 0xaa8
-  __TEXT.__objc_classname: 0x6a5
-  __TEXT.__objc_methname: 0x25c
-  __TEXT.__objc_methtype: 0x43
-  __DATA_CONST.__got: 0x1c0
+  __TEXT.__eh_frame: 0xa30
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x78
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x9a8
-  __AUTH_CONST.__const: 0x20d0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x2148
   __AUTH_CONST.__objc_const: 0xcb8
+  __AUTH_CONST.__auth_got: 0xa40
   __AUTH.__objc_data: 0x230
   __AUTH.__data: 0xe30
-  __DATA.__data: 0x4c0
+  __DATA.__data: 0x4b0
   __DATA.__bss: 0x4c50
   __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 4F343647-6F53-37E9-9378-C0D24237EDE8
-  Functions: 1452
-  Symbols:   612
-  CStrings:  100
+  UUID: E5162383-8E5B-3B39-AE2F-A1C785BED34E
+  Functions: 1449
+  Symbols:   666
+  CStrings:  49
 
Symbols:
+ ___swift__destructor
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.102
+ ___swift_closure_destructor.107
+ ___swift_closure_destructor.111
+ ___swift_closure_destructor.116
+ ___swift_closure_destructor.120
+ ___swift_closure_destructor.125
+ ___swift_closure_destructor.129
+ ___swift_closure_destructor.52
+ ___swift_closure_destructor.58
+ ___swift_closure_destructor.62
+ ___swift_closure_destructor.89
+ ___swift_closure_destructor.93
+ ___swift_closure_destructor.98
+ __swift_implicitisolationactor_to_executor_cast
+ _objc_release_x28
+ _objc_retain_x28
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x27
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x27
+ _swift_unknownObjectRetain_n
- _objc_retain_x27
- _symbolic _____Sg 7CoreHID15HIDDeviceClientC20ProvideElementUpdateV
- _symbolic _____Sg 7CoreHID15HIDDeviceClientC20RequestElementUpdateV
CStrings:
- "$defaultActor"
- "_TtC7CoreHID15HIDDeviceClient"
- "_TtC7CoreHID16HIDDeviceManager"
- "_TtC7CoreHID16HIDVirtualDevice"
- "_TtCC7CoreHID15HIDDeviceClient13StreamWrapper"
- "_TtCFC7CoreHID15HIDDeviceClient14updateElementsFZTGSaPS_16HIDElementUpdate__7timeoutGSqVs8Duration__VS0_22HIDElementUpdateResultL0_15CallbackContext"
- "_TtCFC7CoreHID15HIDDeviceClient14updateElementsFZTGSaPS_16HIDElementUpdate__7timeoutGSqVs8Duration__VS0_22HIDElementUpdateResultL_14CallbackReturn"
- "_TtCFC7CoreHID15HIDDeviceClient14updateElementsFZTGSaPS_16HIDElementUpdate__7timeoutGSqVs8Duration__VS0_22HIDElementUpdateResultL_15CallbackContext"
- "_TtCFC7CoreHID15HIDDeviceClient24dispatchGetReportRequestFzZT4typeOS_13HIDReportType2idGSqVS_11HIDReportID_7timeoutGSqVs8Duration__V10Foundation4DataL_15CallbackContext"
- "_TtCFC7CoreHID15HIDDeviceClient24dispatchSetReportRequestFzZT4typeOS_13HIDReportType2idGSqVS_11HIDReportID_4dataV10Foundation4Data7timeoutGSqVs8Duration__T_L_15CallbackContext"
- "_TtCFC7CoreHID15HIDDeviceClient8activateFT_T_L_7Context"
- "_TtCFC7CoreHID16HIDVirtualDevice19dispatchInputReportFzZT4dataV10Foundation4Data9timestampVVs15SuspendingClock7Instant_T_L_15CallbackContext"
- "_TtCFFC7CoreHID16HIDDeviceManager20monitorNotificationsFT16matchingCriteriaGSaVS0_22DeviceMatchingCriteria__GVs19AsyncThrowingStreamOS0_12NotificationPs5Error__U_FGVS2_12ContinuationS3_PS4____T_L_7Context"
- "_TtCFFC7CoreHID16HIDVirtualDevice8activateFT8delegatePS_24HIDVirtualDeviceDelegate__T_U0_FTVSo15IOHIDReportTypeVs6UInt32GSpVs5UInt8_GSpSi__Vs5Int32L_7Context"
- "_TtCFFC7CoreHID16HIDVirtualDevice8activateFT8delegatePS_24HIDVirtualDeviceDelegate__T_U_FTVSo15IOHIDReportTypeVs6UInt32GSPVs5UInt8_Si_Vs5Int32L_7Context"
- "_description"
- "activated"
- "batchedValues"
- "buff"
- "cancelled"
- "clientPointer"
- "continuation"
- "delegate"
- "descriptor"
- "device"
- "deviceReference"
- "deviceUsages"
- "dictPointer"
- "elementsToMonitor"
- "i32@?0i8I12*16^q24"
- "i32@?0i8I12r*16q24"
- "inputReportBuff"
- "len"
- "maxFeatureReportSize"
- "maxInputReportSize"
- "maxOutputReportSize"
- "opened"
- "outstandingStreams"
- "port"
- "primaryUsage"
- "productID"
- "queue"
- "report"
- "reportIDsToMonitor"
- "reportLength"
- "ret"
- "seized"
- "selfRef"
- "v8@?0"
- "values"
- "vendorID"

```
