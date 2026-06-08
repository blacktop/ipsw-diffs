## HRCDiagnosticExtension

> `/System/Library/PrivateFrameworks/HeartRateCoordinator.framework/PlugIns/HRCDiagnosticExtension.appex/HRCDiagnosticExtension`

```diff

-31.2.0.0.0
-  __TEXT.__text: 0x311c
-  __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_stubs: 0x300
-  __TEXT.__objc_methlist: 0x74
-  __TEXT.__const: 0x153
-  __TEXT.__gcc_except_tab: 0x444
-  __TEXT.__cstring: 0x256
-  __TEXT.__oslogstring: 0x574
+38.0.0.0.0
+  __TEXT.__text: 0x2244
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__objc_stubs: 0x1e0
+  __TEXT.__objc_methlist: 0x5c
+  __TEXT.__const: 0x14b
+  __TEXT.__gcc_except_tab: 0x2c0
+  __TEXT.__cstring: 0x1f9
+  __TEXT.__oslogstring: 0x22f
   __TEXT.__objc_classname: 0x17
-  __TEXT.__objc_methname: 0x26a
-  __TEXT.__objc_methtype: 0x5e
-  __TEXT.__unwind_info: 0x200
-  __DATA_CONST.__auth_got: 0x280
-  __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x1a0
-  __DATA_CONST.__cfstring: 0x100
+  __TEXT.__objc_methname: 0x17d
+  __TEXT.__objc_methtype: 0x45
+  __TEXT.__unwind_info: 0x1d8
+  __DATA_CONST.__const: 0x100
+  __DATA_CONST.__cfstring: 0xa0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x238
+  __DATA_CONST.__got: 0x90
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0xd8
+  __DATA.__objc_selrefs: 0x90
   __DATA.__objc_data: 0x50
   __DATA.__bss: 0x38
-  - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C7C781AF-34D3-3BAC-9A17-4D53A8E3226E
-  Functions: 81
-  Symbols:   113
-  CStrings:  97
+  UUID: 60E44666-FF67-364C-9A50-A7DB0E30C5C3
+  Functions: 65
+  Symbols:   101
+  CStrings:  64
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
- _OBJC_CLASS_$_CBUserController
- _OBJC_CLASS_$_NSUserDefaults
- __dispatch_main_q
- _dispatch_async
- _objc_alloc
- _objc_alloc_init
- _objc_opt_class
- _objc_opt_isKindOfClass
- _objc_release
- _objc_release_x24
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x21
- _objc_retain_x23
- _objc_retain_x8
CStrings:
- "Attempting to update limited logging to: %{public,BOOL}d"
- "B24@0:8@16"
- "Did not receive appleAudioAccessoryLimitedLoggingWithCompletion completion callback"
- "Did not receive setAppleAudioAccessoryLimitedLogging completion callback"
- "Encountered error querying limited logging: %{public}@"
- "Encountered error updating limited logging: %{public}@"
- "InitialLimitedLoggingState"
- "Limited logging state query result: %{public,BOOL}d"
- "No initial logging state found from setup in defaults"
- "Querying limited logging state"
- "Set audio accessory limited logging to: %{public,BOOL}d"
- "Unexpected calling host: %{public}@"
- "_callingHostIsDiagnostics:"
- "_updateLimitedLogging:enabled:"
- "appleAudioAccessoryLimitedLoggingWithCompletion:"
- "boolForKey:"
- "com.apple.enhancedloggingd"
- "initWithSuiteName:"
- "initial limited logging state found in defaults: %{public,BOOL}d"
- "initial limited logging state retrieved from defaults: %{public,BOOL}d"
- "objectForKey:"
- "removeObjectForKey:"
- "setAppleAudioAccessoryLimitedLogging:completion:"
- "setBool:forKey:"
- "setup run outside of expected TL flow!"
- "storing initial limited logging state in defaults: %{public,BOOL}d"
- "teardown run outside of expected TL flow!"
- "v16@?0@\"NSError\"8"
- "v20@?0B8@\"NSError\"12"
- "v28@0:8@16B24"

```
