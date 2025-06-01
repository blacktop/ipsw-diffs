## com.apple.mlhost.SampleWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.SampleWorker.appex/com.apple.mlhost.SampleWorker`

```diff

-3.0.10.0.0
-  __TEXT.__text: 0xa9f4
-  __TEXT.__auth_stubs: 0xb90
+3.1.14.0.0
+  __TEXT.__text: 0x9364
+  __TEXT.__auth_stubs: 0xb10
   __TEXT.__const: 0x548
-  __TEXT.__cstring: 0x804
-  __TEXT.__swift5_typeref: 0x1d9
-  __TEXT.__objc_methname: 0x3f
+  __TEXT.__cstring: 0x594
+  __TEXT.__swift5_typeref: 0x1df
+  __TEXT.__objc_methname: 0x9e
   __TEXT.__swift5_reflstr: 0xbb
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_entry: 0x8

   __TEXT.__swift5_fieldmd: 0xf8
   __TEXT.__swift5_proto: 0x50
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x2cc
-  __TEXT.__eh_frame: 0x468
-  __DATA_CONST.__auth_got: 0x5c8
-  __DATA_CONST.__got: 0x120
+  __TEXT.__unwind_info: 0x2c0
+  __TEXT.__eh_frame: 0x460
+  __DATA_CONST.__auth_got: 0x588
+  __DATA_CONST.__got: 0x118
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x498
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0x10
-  __DATA.__objc_selrefs: 0x20
-  __DATA.__data: 0x348
+  __DATA_CONST.__objc_classrefs: 0x20
+  __DATA.__objc_selrefs: 0x40
+  __DATA.__data: 0x340
   __DATA.__bss: 0xa50
   __DATA.__common: 0x18
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
   - /System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground
+  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 34FFC493-3CB4-3CBE-9C34-4287C1100733
-  Functions: 195
-  Symbols:   82
-  CStrings:  49
+  UUID: 338B62BB-FC65-364E-B6BC-DC2F53B744B0
+  Functions: 192
+  Symbols:   87
+  CStrings:  48
 
Symbols:
+ _MCFeatureDiagnosticsSubmissionAllowed
+ _OBJC_CLASS_$_MCProfileConnection
+ _OBJC_CLASS_$_NSFileManager
+ _objc_release_x25
+ _objc_release_x27
+ _swift_willThrow
- __os_signpost_emit_with_name_impl
CStrings:
+ "Checking for DNU settings: %{bool}d"
+ "contentsOfDirectoryAtPath:error:"
+ "defaultManager"
+ "effectiveBoolValueForSetting:"
+ "sharedConnection"
+ "taskFolder available: %s"
+ "taskFolder contents: %s"
- "    correlationID=%{public, signpost.telemetry:string1, name=correlationID,public}s\n    numberOfStates=%{public, signpost.telemetry:number1, name=numberOfStates,public}ld\n    enableTelemetry=YES"
- "CustomTelemetryEvent"
- "SleepLoop"
- "WorkLoop"
- "[Error] Interval already ended"
- "correlationID=%{public, signpost.telemetry:string1, name=correlationID,public}s\nsleepTime=%{public, signpost.telemetry:number1, name=sleepTime,public}f\nmaxDuration=%{public, signpost.telemetry:number2, name=maxDuration,public}f\nenableTelemetry=YES"
- "correlationID=%{public, signpost.telemetry:string1, name=correlationID,public}s\nworkTime=%{public, signpost.telemetry:number1, name=workTime,public}f\nenableTelemetry=YES"
- "enableTelemetry=YES"

```
