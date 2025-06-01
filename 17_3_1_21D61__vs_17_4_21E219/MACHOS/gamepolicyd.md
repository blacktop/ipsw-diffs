## gamepolicyd

> `/usr/libexec/gamepolicyd`

```diff

-1.1.1.0.0
-  __TEXT.__text: 0x11a90
-  __TEXT.__auth_stubs: 0xc00
+1.4.2.0.0
+  __TEXT.__text: 0x12c90
+  __TEXT.__auth_stubs: 0xcb0
   __TEXT.__objc_stubs: 0x20
-  __TEXT.__objc_methlist: 0xec
-  __TEXT.__const: 0xb04
-  __TEXT.__objc_methname: 0x6d2
+  __TEXT.__objc_methlist: 0xd4
+  __TEXT.__const: 0xbd4
+  __TEXT.__objc_methname: 0x6b3
   __TEXT.__objc_classname: 0x7f
   __TEXT.__objc_methtype: 0x12c
-  __TEXT.__cstring: 0x169b
-  __TEXT.__swift5_typeref: 0x609
+  __TEXT.__cstring: 0x1adb
+  __TEXT.__swift5_typeref: 0x643
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0xdfc
-  __TEXT.__swift5_reflstr: 0x81c
-  __TEXT.__swift5_fieldmd: 0x6f4
-  __TEXT.__swift5_proto: 0x6c
-  __TEXT.__swift5_types: 0x68
+  __TEXT.__constg_swiftt: 0xe48
+  __TEXT.__swift5_reflstr: 0x93c
+  __TEXT.__swift5_fieldmd: 0x758
+  __TEXT.__swift5_proto: 0x78
+  __TEXT.__swift5_types: 0x6c
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_capture: 0x130
-  __TEXT.__unwind_info: 0x41c
+  __TEXT.__unwind_info: 0x448
   __TEXT.__eh_frame: 0x268
-  __DATA_CONST.__auth_got: 0x608
-  __DATA_CONST.__got: 0x160
+  __DATA_CONST.__auth_got: 0x660
+  __DATA_CONST.__got: 0x168
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x8c8
-  __DATA_CONST.__cfstring: 0x20
+  __DATA_CONST.__const: 0x970
+  __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x1f10
-  __DATA.__objc_selrefs: 0x248
-  __DATA.__objc_protorefs: 0x48
-  __DATA.__objc_classrefs: 0x90
-  __DATA.__objc_data: 0x2e0
-  __DATA.__data: 0x1ad0
+  __DATA_CONST.__objc_protorefs: 0x48
+  __DATA_CONST.__objc_classrefs: 0x98
+  __DATA.__objc_const: 0x1fa0
+  __DATA.__objc_selrefs: 0x250
+  __DATA.__objc_data: 0x2b0
+  __DATA.__data: 0x1b50
   __DATA.__common: 0x14
-  __DATA.__bss: 0xa80
+  __DATA.__bss: 0xc00
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/Categories.framework/Categories
+  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/GamePolicy.framework/GamePolicy
   - /System/Library/PrivateFrameworks/GamePolicyServices.framework/GamePolicyServices
   - /System/Library/PrivateFrameworks/PerformanceControlKit.framework/PerformanceControlKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6C6F4905-C233-3F21-A237-443C0BAF6560
-  Functions: 379
-  Symbols:   308
-  CStrings:  294
+  UUID: 9B75EEDB-E6B8-384E-9E9D-2B27E373E3A8
+  Functions: 393
+  Symbols:   324
+  CStrings:  321
 
Symbols:
+ _$s12FeatureFlags02isA7EnabledySbAA0aB3Key_pF
+ _$s12FeatureFlags0aB3KeyMp
+ _$s12FeatureFlags0aB3KeyP6domains12StaticStringVvgTq
+ _$s12FeatureFlags0aB3KeyP7features12StaticStringVvgTq
+ _$sSS9hasPrefixySbSSF
+ _$sSh10FoundationE36_unconditionallyBridgeFromObjectiveCyShyxGSo5NSSetCSgFZ
+ _$sSh8IteratorV6_cocoaAByx_Gs10__CocoaSetVAACn_tcfC
+ _$sSo8NSObjectCSH10ObjectiveCMc
+ _$sSw10copyMemory4fromySW_tF
+ _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _NSLog
+ _OBJC_CLASS_$_RBSProcessAssertionInfo
+ _OBJC_CLASS_$_RBSProcessIdentity
+ ___error
+ __os_feature_enabled_impl
+ _objc_retain_x2
+ _objc_retain_x9
+ _swift_release_n
+ _sysctlbyname
- _OBJC_CLASS_$_RBSProcessHandle
- _objc_retain_x27
- _objc_retain_x28
- _swift_bridgeObjectRetain_n
CStrings:
+ "$__lazy_storage_$_deviceSupportsDynamicPowerSplitter"
+ "$__lazy_storage_$_deviceSupportsSustainedExecutionMode"
+ "%{public}s DPS for %{public}s"
+ "Game mode %{public}s."
+ "GamePolicy"
+ "Insufficient space allocated to copy string contents"
+ "Set DPS to %{public}lu"
+ "Set sustained execution mode to %{public}lu"
+ "Sustained execution mode %{public}s."
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "Unable to set DPS for game: %{public}@"
+ "Unable to set DPS: %{public}@"
+ "Unable to set sustained execution mode: %{public}@"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "assertionDescriptor"
+ "assertions"
+ "clpcDynamicSplitterStateLookup"
+ "com.apple.frontboard:Workspace-ForegroundFocal"
+ "com.apple.system.console_mode_changed"
+ "domain"
+ "gameModeNotification"
+ "gameModeNotifications"
+ "gameModeNotifyToken"
+ "identity"
+ "invalid Collection: less than 'count' elements in collection"
+ "kern.console_mode"
+ "kern.console_mode failed with error: %d"
+ "universalGamePolicySupport"
- "%{public}s game mode for %{public}s"
- "(Simulated) %{public}s game mode for %{public}s"
- "(Simulated) Set game mode to %{bool,public}d"
- "SEM %{public}s."
- "Set game mode to %{public}lu"
- "Set sustainable mode to %{public}lu"
- "Unable to set game mode for game: %{public}@"
- "Unable to set game mode: %{public}@"
- "Unable to set sustainable mode: %{public}@"
- "clpcGameModeStateLookup"
- "isGameModeTiedToSEM"
- "requestGetGameModeTiedToSEMWithReply:"
- "requestSetGameModeTiedToSEM:withReply:"

```
