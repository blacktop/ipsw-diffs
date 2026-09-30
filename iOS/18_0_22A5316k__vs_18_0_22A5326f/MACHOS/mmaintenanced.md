## mmaintenanced

> `/usr/libexec/mmaintenanced`

```diff

-155.0.0.0.0
-  __TEXT.__text: 0x17690
-  __TEXT.__auth_stubs: 0xf30
+158.0.0.0.0
+  __TEXT.__text: 0x186c4
+  __TEXT.__auth_stubs: 0x1120
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x115a
-  __TEXT.__oslogstring: 0x1f33
-  __TEXT.__cstring: 0x1638
-  __TEXT.__gcc_except_tab: 0x758
-  __TEXT.__swift5_typeref: 0x39
-  __TEXT.__swift5_capture: 0x60
-  __TEXT.__unwind_info: 0x7d8
-  __TEXT.__eh_frame: 0x1a0
-  __DATA_CONST.__auth_got: 0x7a0
-  __DATA_CONST.__got: 0x198
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0xcc8
+  __TEXT.__const: 0x1184
+  __TEXT.__oslogstring: 0x20c3
+  __TEXT.__cstring: 0x1718
+  __TEXT.__gcc_except_tab: 0x748
+  __TEXT.__swift5_typeref: 0x64
+  __TEXT.__objc_methname: 0xe9
+  __TEXT.__swift5_capture: 0x78
+  __TEXT.__constg_swiftt: 0x28
+  __TEXT.__swift5_fieldmd: 0x10
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__unwind_info: 0x7f0
+  __TEXT.__eh_frame: 0x208
+  __DATA_CONST.__auth_got: 0x898
+  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__auth_ptr: 0x38
+  __DATA_CONST.__const: 0xd80
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__data: 0xe80
-  __DATA.__bss: 0x40
-  __DATA.__common: 0x31
+  __DATA.__objc_selrefs: 0x60
+  __DATA.__data: 0xeb0
+  __DATA.__bss: 0x48
+  __DATA.__common: 0x40
+  - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 502
-  Symbols:   353
-  CStrings:  391
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 504
+  Symbols:   405
+  CStrings:  412
 
Symbols:
+ _$s10Foundation22_convertNSErrorToErrorys0E0_pSo0C0CSgF
+ _$s10Foundation4DateV20timeIntervalSinceNowSdvg
+ _$s10Foundation4DateV36_unconditionallyBridgeFromObjectiveCyACSo6NSDateCSgFZ
+ _$s10Foundation4DateVMa
+ _$s10Foundation4DateVMn
+ _$s13TapToRadarKit0abC7ServiceC11createDraft_11processName13displayReason10completionySo0cG0C_SSSgAJys5Error_pSgcSgtF
+ _$s13TapToRadarKit0abC7ServiceC6sharedACvgZ
+ _$s13TapToRadarKit0abC7ServiceCMa
+ _$s13TapToRadarKit0abC7ServiceCMn
+ _$s13TapToRadarKit0abC7ServiceCMo
+ _$s13TapToRadarKit0abC7ServiceCN
+ _$s2os6LoggerVMn
+ _$s6Darwin5errnos5Int32Vvg
+ _$sSS10FoundationE19_bridgeToObjectiveCSo8NSStringCyF
+ _$sSS10FoundationE36_unconditionallyBridgeFromObjectiveCySSSo8NSStringCSgFZ
+ _$sSS6appendyySSF
+ _$ss11_StringGutsV4growyySiF
+ _$ss5ErrorMp
+ _$sytWV
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_RadarComponent
+ _OBJC_CLASS_$_RadarDraft
+ __CFCopySystemVersionDictionaryValue
+ __kCFSystemVersionBuildVersionKey
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ __swift_stdlib_bridgeErrorToNSError
+ _objc_allocWithZone
+ _objc_msgSend
+ _objc_opt_self
+ _objc_release
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x27
+ _swift_dynamicCast
+ _swift_getObjCClassMetadata
+ _swift_once
+ _swift_willThrow
- _os_fault_with_payload
CStrings:
+ "/private/var/mobile/Library/MemoryMaintenance/ane_abandonment_ttr"
+ "ANE memory clearly not abandonded, skipping further checks"
+ "ANE memory usage speculated to be over threshold by %!l(MISSING)ld bytes"
+ "Failed to get file attributes for last ttr time record with err: %!@(MISSING)"
+ "Failed to get modification date of %!s(MISSING)"
+ "Failed to launch Tap-To-Radar with error: %!@(MISSING)"
+ "Failed to update last Tap-To-Radar file, could not create file"
+ "Memory Maintenance"
+ "Memory abandonment in the neural engine has been detected, please file this radar to Performance Tentpole | Memory.\nPlease note any Apple Intelligence features you've recently used below:\n"
+ "Performance Tentpole"
+ "Successfully started Tap-To-Radar"
+ "Time since last TTR less than 24 hours. Last TTR %!f(MISSING) hours ago"
+ "Update last Tap-To-Radar file failed with errno %!d(MISSING)"
+ "] Detected >1gb Memory Abandonment In Neural Engine"
+ "attributesOfItemAtPath:error:"
+ "code"
+ "createFileAtPath:contents:attributes:"
+ "defaultManager"
+ "fileModificationDate"
+ "init"
+ "initWithName:version:identifier:"
+ "setClassification:"
+ "setComponent:"
+ "setProblemDescription:"
+ "setReproducibility:"
+ "setTitle:"
+ "severe (>1gb) neural engine memory abandonment was detected"
- "/private/var/mobile/Library/MemoryMaintenance/ane_abandonment"
- "ANE memory abandonment not resolved by killing modelmanagerd, system memory reset likely"
- "could not close ANE fault time file"
- "could not open ANE fault time file"
- "could not write ExcUserFault because last log was within the day"
- "memory abandonment in ane driver detected, killing modelmanagerd"

```
