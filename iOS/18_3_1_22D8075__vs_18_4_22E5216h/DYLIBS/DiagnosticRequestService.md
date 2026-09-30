## DiagnosticRequestService

> `/System/Library/PrivateFrameworks/DiagnosticRequestService.framework/DiagnosticRequestService`

```diff

-383.80.2.0.0
-  __TEXT.__text: 0x6bd54
+383.100.15.0.0
+  __TEXT.__text: 0x69634
   __TEXT.__auth_stubs: 0xf20
-  __TEXT.__objc_methlist: 0x48fc
-  __TEXT.__const: 0xe08
+  __TEXT.__objc_methlist: 0x4ca4
+  __TEXT.__const: 0xd86
   __TEXT.__gcc_except_tab: 0xbd8
-  __TEXT.__cstring: 0x53cf
-  __TEXT.__oslogstring: 0xb3e7
+  __TEXT.__cstring: 0x54ff
+  __TEXT.__oslogstring: 0xb8c9
   __TEXT.__swift5_typeref: 0x278
   __TEXT.__constg_swiftt: 0x24c
   __TEXT.__swift5_fieldmd: 0x240

   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x1778
-  __TEXT.__eh_frame: 0x420
+  __TEXT.__unwind_info: 0x1708
+  __TEXT.__eh_frame: 0x4b0
   __TEXT.__objc_classname: 0x975
-  __TEXT.__objc_methname: 0xaf71
-  __TEXT.__objc_methtype: 0x10f7
-  __TEXT.__objc_stubs: 0x8020
-  __DATA_CONST.__got: 0x418
-  __DATA_CONST.__const: 0x1310
+  __TEXT.__objc_methname: 0xb262
+  __TEXT.__objc_methtype: 0x110c
+  __TEXT.__objc_stubs: 0x82c0
+  __DATA_CONST.__got: 0x448
+  __DATA_CONST.__const: 0x1388
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2458
+  __DATA_CONST.__objc_selrefs: 0x25d0
   __DATA_CONST.__objc_superrefs: 0x1f8
   __AUTH_CONST.__auth_got: 0x7a0
   __AUTH_CONST.__auth_ptr: 0x1a8
   __AUTH_CONST.__const: 0xf10
-  __AUTH_CONST.__cfstring: 0x51a0
-  __AUTH_CONST.__objc_const: 0x8e18
+  __AUTH_CONST.__cfstring: 0x53e0
+  __AUTH_CONST.__objc_const: 0x8a38
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x630
   __AUTH.__data: 0x300
-  __DATA.__objc_ivar: 0x448
-  __DATA.__data: 0x740
+  __DATA.__objc_ivar: 0x454
+  __DATA.__data: 0x788
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x1600
+  __DATA.__bss: 0x15f0
   __DATA.__common: 0x88
   __DATA_DIRTY.__objc_data: 0x1580
   __DATA_DIRTY.__data: 0xe0
-  __DATA_DIRTY.__bss: 0x398
+  __DATA_DIRTY.__bss: 0x3a8
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2371
-  Symbols:   2399
-  CStrings:  3911
+  Functions: 2444
+  Symbols:   2538
+  CStrings:  3989
 
Symbols:
+ _CFPreferencesCopyValue
+ _TSPDumpOptions_EndTimestamp
+ _kCFPreferencesAnyHost
+ _kDRSDMCoreDuetPeopleSuggesterShareSheetMadRequestTimeoutCategory
+ _kDRSDMCoreDuetPeopleSuggesterShareSheetTimeoutCategory
+ _kDRSDMCoreDuetPeopleSuggesterTeamID
+ _kDRSDMPearlAFileBundleCategory
+ _kDRSDMPearlTeamID
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _sysctlbyname
- _fmodf
- _kDRSRequestADGContextDictKey
- _memcpy
- _swift_initStructMetadata
CStrings:
+ "%\x12"
+ "<no string>"
+ "ADG"
+ "Added 'isLikelyCarry': '%{public}@' to context metadata"
+ "Added ADG %{public}@ to context metadata for request %{public}@"
+ "Added HW model '%{public}@' to context metadata"
+ "AutomatedDeviceGroupMetadataContextUpdated"
+ "B48@0:8@16@24#32^@40"
+ "Collided on context metadata key '%{public}@'. Overwriting..."
+ "ContextDictionaryUpdateFailure"
+ "ContextDictionaryUpdateSuccess"
+ "ContextMetadataADGFailure"
+ "ContextMetadataHWModelAddition"
+ "ContextMetadataHWModelFailure"
+ "ContextMetadataIsLikelyCarryAddition"
+ "ContextMetadataIsLikelyCarryNumFailure"
+ "Could not add 'IsLikelyCarry' value (nil number)"
+ "Could not add HW model string (nil string)"
+ "Could not serialized updated context as plist"
+ "DRSRequestContextMetadataError"
+ "Decided that the device is: '%{public}@' based on experimental group string: '%{public}@'"
+ "ExperimentGroup"
+ "Failed to add 'isLikelyCarry' value to context metadata due to error: %{public}@"
+ "Failed to add ADG to context metadata due to error: %{public}@"
+ "Failed to add HW model to context metadata due to error: %{public}@"
+ "Failed to lookup hw.model: %d %{public}s"
+ "Failed to serialize to plist when adding context metadata key '%{public}@'"
+ "HWModel"
+ "HWModelLookupFailure"
+ "HWModelLookupSuccess"
+ "IsLikelyCarryLookup"
+ "IsLikelyCarryLookupSkipped"
+ "Likely carry"
+ "LikelyCarry"
+ "MAT[%@, %@]"
+ "MaxMAT"
+ "NilHWModel"
+ "NilLikelyCarry"
+ "Not likely carry"
+ "OverwritingContextMetadataKey"
+ "PearlAFileBundle"
+ "ShareSheetMadRequestTimeout"
+ "ShareSheetTimeout"
+ "Skipping due to non-Internal device"
+ "SkippingHWModel"
+ "SkippingIsLikelyCarry"
+ "Stopped trying to upload after %u attempts. Upload error: %@"
+ "T@\"NSNumber\",R,N"
+ "T@\"NSNumber\",R,N,V_isLikelyCarryGroupNum"
+ "T@\"NSNumber\",R,N,V_maxMAT"
+ "T@\"NSString\",R,N,V_hwModel"
+ "Updated context metadata with new key: '%{public}@'"
+ "We dont reason about carry for non-Internal devices"
+ "__DPMD__"
+ "_addContextMetadataKey:value:expectedClass:errorOut:"
+ "_coreDuetPeopleSuggesterTeamConfiguration:isSeed:isCarrier:platform:"
+ "_hwModel"
+ "_isLikelyCarryGroupNum"
+ "_maxMAT"
+ "_pearlTeamConfiguration:isSeed:isCarrier:platform:"
+ "_populateHWModel"
+ "_populateIsCarry"
+ "addContextMetadataKey:numberValue:errorOut:"
+ "addContextMetadataKey:stringValue:errorOut:"
+ "addHWModelContextMetadata"
+ "addIsLikelyCarryContextMetadata"
+ "build                       = %{public}@\nbuildVariant                = %{public}@\ndeviceCategory              = %{public}@\ndeviceModel                 = %{public}@\nplatformString              = %{public}@\ndeviceHash                  = %{public}#llx\nisInternal                  = %{public}u\nisSeed                      = %{public}u\nisCarrier                   = %{public}u\ncustomerApprovesAnalytics   = %{public}u\nisLogUploadEnabled          = %{public}u\nisTaskingEnabled            = %{public}u\nuploadSessionUploadCapBytes = %{public}llu\nhwModel                     = %{public}@n\nisLikelyCarry               = %{public}@n\n"
+ "carry"
+ "com.apple.CoreDuet.PeopleSuggester"
+ "com.apple.da"
+ "com.apple.pearl"
+ "containsString:"
+ "hw.model"
+ "hw.model: '%{public}@'"
+ "hwModel"
+ "isLikeCarryDevice"
+ "isLikelyCarryGroupNum"
+ "lowercaseString"
+ "maxUploadAttemptCount"
+ "metadataDictionary"
+ "mobile"
+ "numberWithInt:"
+ "pearlAFileBundleConfiguration"
+ "setMaxMAT:"
+ "shareSheetMadRequestTimeoutConfiguration"
+ "shareSheetTimeoutConfiguration"
+ "walkabout"
- "#\x12"
- "Added ADG %{public}@ for request %{public}@"
- "AutomatedDeviceGroupContextUpdateFailure"
- "AutomatedDeviceGroupContextUpdated"
- "Failed to update context dictionary with ADG for request %{public}@"
- "MAT[%@, -)"
- "Stopped trying to upload after %llu attempts. Upload error: %@"
- "__AutomatedDeviceGroup__"
- "build                       = %{public}@\nbuildVariant                = %{public}@\ndeviceCategory              = %{public}@\ndeviceModel                 = %{public}@\nplatformString              = %{public}@\ndeviceHash                  = %{public}#llx\nisInternal                  = %{public}u\nisSeed                      = %{public}u\nisCarrier                   = %{public}u\ncustomerApprovesAnalytics   = %{public}u\nisLogUploadEnabled          = %{public}u\nisTaskingEnabled            = %{public}u\nuploadSessionUploadCapBytes = %{public}llu\n"

```
