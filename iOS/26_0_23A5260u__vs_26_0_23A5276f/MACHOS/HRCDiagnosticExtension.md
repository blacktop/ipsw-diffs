## HRCDiagnosticExtension

> `/System/Library/PrivateFrameworks/HeartRateCoordinator.framework/PlugIns/HRCDiagnosticExtension.appex/HRCDiagnosticExtension`

```diff

-15.1.1.0.0
-  __TEXT.__text: 0x1950
-  __TEXT.__auth_stubs: 0x3e0
-  __TEXT.__objc_stubs: 0x180
-  __TEXT.__objc_methlist: 0x2c
-  __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x1ec
-  __TEXT.__cstring: 0x1a4
-  __TEXT.__oslogstring: 0x216
+17.0.0.0.0
+  __TEXT.__text: 0x2fc4
+  __TEXT.__auth_stubs: 0x500
+  __TEXT.__objc_stubs: 0x300
+  __TEXT.__objc_methlist: 0x74
+  __TEXT.__const: 0x166
+  __TEXT.__gcc_except_tab: 0x420
+  __TEXT.__cstring: 0x256
+  __TEXT.__oslogstring: 0x562
   __TEXT.__objc_classname: 0x17
-  __TEXT.__objc_methname: 0x13c
-  __TEXT.__objc_methtype: 0x1e
-  __TEXT.__unwind_info: 0x140
-  __DATA_CONST.__auth_got: 0x200
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0xc0
-  __DATA_CONST.__cfstring: 0xc0
+  __TEXT.__objc_methname: 0x26a
+  __TEXT.__objc_methtype: 0x5e
+  __TEXT.__unwind_info: 0x200
+  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__const: 0x1a0
+  __DATA_CONST.__cfstring: 0x100
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x70
+  __DATA.__objc_selrefs: 0xd8
   __DATA.__objc_data: 0x50
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A8EA6369-6B5D-3FBD-B07E-6F253750E7D3
-  Functions: 38
-  Symbols:   88
-  CStrings:  54
+  UUID: D8716C51-E79D-36B1-9714-3403C0082D29
+  Functions: 76
+  Symbols:   115
+  CStrings:  96
 
Symbols:
+ _OBJC_CLASS_$_NSUserDefaults
+ __Block_object_dispose
+ __ZNKSt3__110error_code7messageEv
+ __ZNSt12out_of_rangeD1Ev
+ __ZNSt3__115system_categoryEv
+ __ZNSt3__116generic_categoryEv
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTISt12out_of_range
+ __ZTVN10__cxxabiv117__class_type_infoE
+ __ZTVN10__cxxabiv120__si_class_type_infoE
+ __ZTVNSt3__117bad_function_callE
+ __ZTVSt12out_of_range
+ __ZdlPvSt19__type_descriptor_t
+ ___cxa_atexit
+ ___cxa_guard_acquire
+ ___cxa_guard_release
+ _memcmp
+ _objc_alloc
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_release
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_retain_x21
+ _objc_retain_x22
+ _strcmp
+ _strlen
- _MGGetBoolAnswer
- _objc_release_x28
CStrings:
+ "/var/mobile/Library/Logs/Bluetooth/"
+ "@16@0:8"
+ "@20@0:8B16"
+ "@36@0:8r^v16^v24B32"
+ "AccessoryHR"
+ "Attempting to update limited logging to: %{public,BOOL}d"
+ "B24@0:8@16"
+ "Did not receive appleAudioAccessoryLimitedLoggingWithCompletion completion callback"
+ "Directory not found at %{public}s"
+ "Encountered error querying limited logging: %{public}@"
+ "Encountered error updating limited logging: %{public}@"
+ "Error checking if directory exists: %{public}s"
+ "Error checking if entry is a regular file: %{public}s"
+ "Error getting last write time: %{public}s"
+ "Error iterating directory: %{public}s"
+ "InitialLimitedLoggingState"
+ "Limited logging state query result: %{public,BOOL}d"
+ "No initial logging state found from setup in defaults"
+ "Querying limited logging state"
+ "Set audio accessory limited logging to: %{public,BOOL}d"
+ "_callingHostIsDiagnostics:"
+ "_collectFilesFrom:withFilter:skipNewest:"
+ "_getHRCLP5s:"
+ "_getPalomaLogs"
+ "_updateLimitedLogging:enabled:"
+ "addObjectsFromArray:"
+ "appleAudioAccessoryLimitedLoggingWithCompletion:"
+ "boolForKey:"
+ "com.apple.HeartRateCoordinator.logFlushNotNeeded"
+ "com.apple.enhancedloggingd"
+ "initWithSuiteName:"
+ "initial limited logging state already in defaults, skipping setup: %{public,BOOL}d"
+ "initial limited logging state retrieved from defaults: %{public,BOOL}d"
+ "objectForKey:"
+ "removeObjectForKey:"
+ "setBool:forKey:"
+ "setup run outside of expected TL flow!"
+ "setupWithParameters: %{public}@"
+ "storing initial limited logging state in defaults: %{public,BOOL}d"
+ "string_view::substr"
+ "teardown run outside of expected TL flow!"
+ "teardownWithParameters:"
+ "teardownWithParameters: %{public}@"
+ "v20@?0B8@\"NSError\"12"
+ "v28@0:8@16B24"
- "Attempting to enable limited logging"
- "Enabled audio accessory limited logging"
- "Encountered error enabling limited logging: %@"
- "InternalBuild"
- "setupWithParameters: %{public}@ isInternalBuild: %{public}d"

```
