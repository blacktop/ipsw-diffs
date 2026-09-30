## RepackagingWorker

> `/System/Library/ExtensionKit/Extensions/RepackagingWorker.appex/Contents/MacOS/RepackagingWorker`

```diff

-1.4.11.0.0
-  __TEXT.__text: 0x117c8
-  __TEXT.__auth_stubs: 0xa40
+1.5.4.0.0
+  __TEXT.__text: 0x1337c
+  __TEXT.__auth_stubs: 0xad0
   __TEXT.__const: 0xbea
-  __TEXT.__cstring: 0x95e
+  __TEXT.__cstring: 0xa7e
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x2ac
-  __TEXT.__swift5_typeref: 0x4f7
-  __TEXT.__swift5_reflstr: 0x1dc
-  __TEXT.__swift5_fieldmd: 0x2b0
+  __TEXT.__swift5_typeref: 0x523
+  __TEXT.__swift5_reflstr: 0x1ec
+  __TEXT.__swift5_fieldmd: 0x2bc
   __TEXT.__swift5_assocty: 0x90
-  __TEXT.__objc_methname: 0x25f
+  __TEXT.__objc_methname: 0x2f2
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0xa8
   __TEXT.__swift5_types: 0x50

   __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift5_capture: 0x70
   __TEXT.__oslogstring: 0xc
-  __TEXT.__unwind_info: 0x500
-  __TEXT.__eh_frame: 0x748
-  __DATA_CONST.__auth_got: 0x520
-  __DATA_CONST.__got: 0x198
-  __DATA_CONST.__auth_ptr: 0x2f0
-  __DATA_CONST.__const: 0xb58
+  __TEXT.__unwind_info: 0x528
+  __TEXT.__eh_frame: 0x740
+  __DATA_CONST.__auth_got: 0x568
+  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__auth_ptr: 0x308
+  __DATA_CONST.__const: 0xb88
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0xb8
-  __DATA.__objc_selrefs: 0x108
-  __DATA.__data: 0x408
+  __DATA.__objc_selrefs: 0x120
+  __DATA.__data: 0x420
   __DATA.__bss: 0x1500
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/LighthouseBackground.framework/Versions/A/LighthouseBackground
   - /System/Library/PrivateFrameworks/SiriAnalytics.framework/Versions/A/SiriAnalytics
   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/Versions/A/SiriInstrumentation
+  - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/Versions/A/SymptomDiagnosticReporter
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 418
-  Symbols:   119
-  CStrings:  79
+  Functions: 435
+  Symbols:   121
+  CStrings:  90
 
Symbols:
+ _OBJC_CLASS_$_SDRDiagnosticReporter
+ _kSymptomDiagnosticReplySuccess
CStrings:
+ " is missing DIM messages"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/LighthouseDataProcessor_AllPlatforms/RepackagingWorker/ExtensionPreferences.swift"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/LighthouseDataProcessor_AllPlatforms/RepackagingWorker/ExtensionRecipe.swift"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/LighthouseDataProcessor_AllPlatforms/RepackagingWorker/InstrumentationUploader.swift"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/LighthouseDataProcessor_AllPlatforms/RepackagingWorker/RepackagingWorker.swift"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/LighthouseDataProcessor_AllPlatforms/RepackagingWorker/SessionBuilderExtension.swift"
+ "ABC error triggered"
+ "Error producing ABC diagnostic"
+ "LighthouseInstrumentation"
+ "Missing SDRDiagnosticReporter or not internal"
+ "PackageMissingDIM"
+ "getAnyEventType"
+ "reportDIMlessClockIds(sessions:)"
+ "signatureWithDomain:type:subType:detectedProcess:triggerThresholdValues:"
+ "snapshotWithSignature:delay:events:payload:actions:reply:"
+ "v16@?0@\"NSDictionary\"8"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/LighthouseDataProcessor_AllPlatforms/RepackagingWorker/ExtensionPreferences.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/LighthouseDataProcessor_AllPlatforms/RepackagingWorker/ExtensionRecipe.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/LighthouseDataProcessor_AllPlatforms/RepackagingWorker/InstrumentationUploader.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/LighthouseDataProcessor_AllPlatforms/RepackagingWorker/RepackagingWorker.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/LighthouseDataProcessor_AllPlatforms/RepackagingWorker/SessionBuilderExtension.swift"

```
