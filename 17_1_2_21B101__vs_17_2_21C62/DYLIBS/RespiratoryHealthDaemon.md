## RespiratoryHealthDaemon

> `/System/Library/PrivateFrameworks/RespiratoryHealthDaemon.framework/RespiratoryHealthDaemon`

```diff

-4146.1.11.3.0
-  __TEXT.__text: 0x5014
-  __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_methlist: 0x5fc
+4146.2.12.1.3
+  __TEXT.__text: 0x5430
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__objc_methlist: 0x624
   __TEXT.__const: 0x88
-  __TEXT.__oslogstring: 0x79c
+  __TEXT.__oslogstring: 0x845
   __TEXT.__cstring: 0x501
-  __TEXT.__unwind_info: 0x1b4
+  __TEXT.__unwind_info: 0x1c4
   __TEXT.__objc_classname: 0x233
-  __TEXT.__objc_methname: 0x238a
-  __TEXT.__objc_methtype: 0x652
-  __TEXT.__objc_stubs: 0x14e0
-  __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x150
+  __TEXT.__objc_methname: 0x244a
+  __TEXT.__objc_methtype: 0x678
+  __TEXT.__objc_stubs: 0x1540
+  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__const: 0x178
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1198
-  __DATA_CONST.__objc_selrefs: 0x698
+  __DATA_CONST.__objc_const: 0x11b8
+  __DATA_CONST.__objc_selrefs: 0x6c0
   __AUTH_CONST.__cfstring: 0x560
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__objc_const: 0x280
-  __AUTH_CONST.__auth_got: 0x228
+  __AUTH_CONST.__auth_got: 0x230
   __AUTH.__objc_data: 0x140
   __DATA.__objc_classrefs: 0x148
   __DATA.__objc_superrefs: 0x28
-  __DATA.__objc_ivar: 0xa4
+  __DATA.__objc_ivar: 0xa8
   __DATA.__data: 0x3c0
   __DATA_DIRTY.__objc_data: 0x140
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/RespiratoryHealth.framework/RespiratoryHealth
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0A5A35B0-E386-393E-BBC8-1D2AED9F0F17
-  Functions: 155
-  Symbols:   770
-  CStrings:  533
+  UUID: CFA78FDC-4F93-312A-B80E-2FF64B599EB5
+  Functions: 159
+  Symbols:   788
+  CStrings:  543
 
Symbols:
+ -[HDRespiratoryProfileExtension dealloc]
+ -[HDRespiratoryProfileExtension initWithProfile:featureAvailabilityManager:ageGatingDefaults:]
+ -[HDRespiratoryProfileExtension observeValueForKeyPath:ofObject:change:context:]
+ -[HDRespiratoryProfileExtension startObservingAgeGatingDefaults]
+ _NSKeyValueChangeNewKey
+ _NSKeyValueChangeOldKey
+ _OBJC_IVAR_$_HDRespiratoryProfileExtension._ageGatingDefaults
+ ___80-[HDRespiratoryProfileExtension observeValueForKeyPath:ofObject:change:context:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ _kHKAgeGatingDomain
+ _kHKAgeGatingKeyEnableOxygenSaturationRecording
+ _objc_msgSend$addObserver:forKeyPath:options:context:
+ _objc_msgSend$initWithProfile:featureAvailabilityManager:ageGatingDefaults:
+ _objc_msgSend$removeObserver:forKeyPath:
+ _objc_msgSend$startObservingAgeGatingDefaults
+ _objc_retain_x25
- -[HDRespiratoryProfileExtension initWithProfile:featureAvailabilityManager:]
- _objc_msgSend$initWithProfile:featureAvailabilityManager:
CStrings:
+ "\x06\x12"
+ "@40@0:8@16@24@32"
+ "[%{public}@] %{public}@ changed: %{public}@ -> %{public}@"
+ "[%{public}@] No updates to background measuremments"
+ "[%{public}@] Updating background measurements setting from %{BOOL}d to %{BOOL}d, isSupported = %@, isOxygenSaturationDisabled = %@ isBloodOxygenAgeGated = %{BOOL}d"
+ "_ageGatingDefaults"
+ "a"
+ "addObserver:forKeyPath:options:context:"
+ "dealloc"
+ "initWithProfile:featureAvailabilityManager:ageGatingDefaults:"
+ "observeValueForKeyPath:ofObject:change:context:"
+ "removeObserver:forKeyPath:"
+ "startObservingAgeGatingDefaults"
+ "v48@0:8@16@24@32^v40"
- "\x05\x12"
- "[%{public}@] Updating background measurements setting, isSupported = %@, isOxygenSaturationDisabled = %@"
- "initWithProfile:featureAvailabilityManager:"

```
