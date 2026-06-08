## analyticsagent

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsagent`

```diff

-501.120.2.0.0
-  __TEXT.__text: 0xd720
-  __TEXT.__auth_stubs: 0xb60
-  __TEXT.__objc_stubs: 0x6a0
+548.0.0.0.0
+  __TEXT.__text: 0xe3c4
+  __TEXT.__auth_stubs: 0xcf0
+  __TEXT.__objc_stubs: 0x700
   __TEXT.__objc_methlist: 0x64
-  __TEXT.__cstring: 0x399
+  __TEXT.__cstring: 0x3f9
   __TEXT.__const: 0x380
-  __TEXT.__oslogstring: 0xab2
-  __TEXT.__swift5_typeref: 0x268
+  __TEXT.__oslogstring: 0xb12
+  __TEXT.__swift5_typeref: 0x26a
   __TEXT.__swift5_capture: 0xb8
-  __TEXT.__objc_methname: 0x41c
+  __TEXT.__objc_methname: 0x484
   __TEXT.__objc_classname: 0xf0
-  __TEXT.__constg_swiftt: 0x224
-  __TEXT.__swift5_fieldmd: 0x15c
+  __TEXT.__constg_swiftt: 0x22c
+  __TEXT.__swift5_fieldmd: 0x168
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
+  __TEXT.__swift_as_cont: 0xc
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__objc_methtype: 0xa2
-  __TEXT.__swift5_reflstr: 0xe6
+  __TEXT.__objc_methtype: 0xb2
+  __TEXT.__swift5_reflstr: 0xf6
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x2b8
-  __TEXT.__eh_frame: 0x188
-  __DATA_CONST.__auth_got: 0x5b8
-  __DATA_CONST.__got: 0x198
-  __DATA_CONST.__auth_ptr: 0x130
-  __DATA_CONST.__const: 0x4c0
+  __TEXT.__unwind_info: 0x2c0
+  __TEXT.__eh_frame: 0xf0
+  __DATA_CONST.__const: 0x4f0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x248
-  __DATA.__objc_selrefs: 0x1c0
-  __DATA.__objc_data: 0x238
-  __DATA.__data: 0x3d0
+  __DATA_CONST.__auth_got: 0x680
+  __DATA_CONST.__got: 0x1b8
+  __DATA_CONST.__auth_ptr: 0x148
+  __DATA.__objc_const: 0x268
+  __DATA.__objc_selrefs: 0x1d8
+  __DATA.__objc_data: 0x248
+  __DATA.__data: 0x3f8
   __DATA.__common: 0x60
-  __DATA.__bss: 0x1b0
+  __DATA.__bss: 0x1c0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E4F16C8A-82E4-3A5E-9B8E-32B4C2DB2421
-  Functions: 191
-  Symbols:   292
-  CStrings:  148
+  UUID: 450561D4-D7D4-30E4-A10F-ADF266F46091
+  Functions: 199
+  Symbols:   322
+  CStrings:  156
 
Symbols:
+ _$s10Foundation4DataV14RangeReferenceCMa
+ _$s10Foundation8TimeZoneV10identifierACSgSSh_tcfC
+ _$s10Foundation8TimeZoneV19_bridgeToObjectiveCSo06NSTimeC0CyF
+ _$s10Foundation8TimeZoneVMa
+ _$s10Foundation8TimeZoneVMn
+ _$s8Dispatch0A13WorkItemFlagsVMa
+ _$s8Dispatch0A13WorkItemFlagsVMn
+ _$s8Dispatch0A13WorkItemFlagsVs10SetAlgebraAAMc
+ _$sSS21_builtinStringLiteral17utf8CodeUnitCount7isASCIISSBp_BwBi1_tcfC
+ _$sSo17OS_dispatch_queueC8DispatchE5async5group3qos5flags7executeySo0a1_b1_F0CSg_AC0D3QoSVAC0D13WorkItemFlagsVyyXBtF
+ _OBJC_CLASS_$_NSDateFormatter
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ _memset
+ _swift_bridgeObjectRetain_n
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x8
+ _swift_retain_n
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x24
+ _swift_retain_x26
CStrings:
+ "Event %{public}s not enabled, skipping %{public}s duration=%u collectedDate=%{public}s"
+ "Handle AppUsage test trigger notification: %s"
+ "Reporting window: lastSync=%.*f now=%.*f queryStart=%.*f"
+ "Sent telemetry for %{public}s duration=%u collectedDate=%{public}s"
+ "actualCollectedDate"
+ "appUsageScheduler"
+ "com.apple.coreanalytics.AppUsageCollectionTrigger"
+ "com.apple.coreanalytics.appUsage2"
+ "setDateFormat:"
+ "setTimeZone:"
+ "stringFromDate:"
+ "v8@?0"
- "Event %{public}s not enabled, skipping telemetry for %{public}s"
- "Last app usage sync was before today; clamping reporting window to 0 GMT"
- "Sent telemetry for %{public}s (%.*fs)"
- "com.apple.coreanalytics.appUsage"

```
