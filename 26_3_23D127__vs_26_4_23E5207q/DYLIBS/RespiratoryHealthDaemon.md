## RespiratoryHealthDaemon

> `/System/Library/PrivateFrameworks/RespiratoryHealthDaemon.framework/RespiratoryHealthDaemon`

```diff

-6200.4.9.0.0
-  __TEXT.__text: 0x8788
-  __TEXT.__auth_stubs: 0x4c0
-  __TEXT.__objc_methlist: 0x914
-  __TEXT.__const: 0xb8
-  __TEXT.__oslogstring: 0xb66
+6200.5.77.2.6
+  __TEXT.__text: 0x865c
+  __TEXT.__auth_stubs: 0x460
+  __TEXT.__objc_methlist: 0x8f4
+  __TEXT.__const: 0xb0
+  __TEXT.__gcc_except_tab: 0x258
   __TEXT.__cstring: 0x88e
-  __TEXT.__gcc_except_tab: 0x274
-  __TEXT.__unwind_info: 0x288
+  __TEXT.__oslogstring: 0xa10
+  __TEXT.__unwind_info: 0x2a8
   __TEXT.__objc_classname: 0x292
-  __TEXT.__objc_methname: 0x2d7e
-  __TEXT.__objc_methtype: 0x81d
-  __TEXT.__objc_stubs: 0x1e40
-  __DATA_CONST.__got: 0x2b0
-  __DATA_CONST.__const: 0x1c0
+  __TEXT.__objc_methname: 0x2c9e
+  __TEXT.__objc_methtype: 0x82e
+  __TEXT.__objc_stubs: 0x1d80
+  __DATA_CONST.__got: 0x298
+  __DATA_CONST.__const: 0x198
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9d8
+  __DATA_CONST.__objc_selrefs: 0x9a0
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x270
+  __AUTH_CONST.__auth_got: 0x240
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x840
-  __AUTH_CONST.__objc_const: 0x11a8
-  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__objc_const: 0x11b0
+  __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0xbc
   __DATA.__data: 0x4e0

   - /System/Library/PrivateFrameworks/RespiratoryHealth.framework/RespiratoryHealth
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B39E8788-03A3-3BE9-873C-558DC0C43B4C
+  UUID: AFA66A1C-6DC8-38CD-AD55-96A58E142721
   Functions: 200
-  Symbols:   1004
-  CStrings:  685
+  Symbols:   990
+  CStrings:  674
 
Symbols:
+ _HKLogRespiratory
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ ___block_literal_global.375
+ ___block_literal_global.383
+ ___block_literal_global.397
+ _objc_msgSend$analyzeSampleResultForSample:
+ _objc_opt_respondsToSelector
- -[HDRespiratoryProfileExtension _updateBackgroundRecordingSettings]
- -[HDRespiratoryProfileExtension _updateBackgroundRecordingSettings].cold.1
- -[HDRespiratoryProfileExtension dealloc]
- -[HDRespiratoryProfileExtension observeValueForKeyPath:ofObject:change:context:]
- -[HDRespiratoryProfileExtension startObservingAgeGatingDefaults]
- _HKLogRespiratoryCategory
- _NSKeyValueChangeNewKey
- _NSKeyValueChangeOldKey
- ___80-[HDRespiratoryProfileExtension observeValueForKeyPath:ofObject:change:context:]_block_invoke
- ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_literal_global.336
- ___block_literal_global.344
- ___block_literal_global.358
- _kHKAgeGatingKeyEnableOxygenSaturationRecording
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_updateBackgroundRecordingSettings
- _objc_msgSend$addObserver:forKeyPath:options:context:
- _objc_msgSend$isEqualToNumber:
- _objc_msgSend$onboardedCountryCodeSupportedStateWithError:
- _objc_msgSend$removeObserver:forKeyPath:
- _objc_msgSend$setBackgroundRecordingsEnabled:
- _objc_msgSend$startObservingAgeGatingDefaults
- _objc_retain
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x8
CStrings:
+ "198711C2-332F-481C-B7DE-7E80973B07BF"
+ "2D6D2220-332F-481C-B7DE-7E80973B07BF"
+ "BD3A4341-332F-481C-B7DE-7E80973B07BF"
+ "analyzeSampleResultForSample:"
+ "samplesMapWereRemoved:anchor:"
+ "v32@0:8@\"NSDictionary\"16@\"NSNumber\"24"
- "198711C2-6CC8-43B9-A882-6670CC787272"
- "2D6D2220-64DB-408A-89ED-ED05391073E8"
- "BD3A4341-7090-4622-9694-2AC0F536C478"
- "[%{public}@] %{public}@ changed: %{public}@ -> %{public}@"
- "[%{public}@] Failed to check if Blood Oxygen is supported with error: %@"
- "[%{public}@] No updates to background recordings"
- "[%{public}@] Updating background recordings setting from %{BOOL}d to %{BOOL}d, isSupported = %@, isOxygenSaturationDisabled = %@ isBloodOxygenAgeGated = %{BOOL}d"
- "_updateBackgroundRecordingSettings"
- "addObserver:forKeyPath:options:context:"
- "dealloc"
- "isEqualToNumber:"
- "observeValueForKeyPath:ofObject:change:context:"
- "onboardedCountryCodeSupportedStateWithError:"
- "removeObserver:forKeyPath:"
- "setBackgroundRecordingsEnabled:"
- "startObservingAgeGatingDefaults"
- "v48@0:8@16@24@32^v40"

```
