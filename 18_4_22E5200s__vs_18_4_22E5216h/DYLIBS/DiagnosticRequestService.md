## DiagnosticRequestService

> `/System/Library/PrivateFrameworks/DiagnosticRequestService.framework/DiagnosticRequestService`

```diff

-383.100.11.0.0
-  __TEXT.__text: 0x68580
-  __TEXT.__auth_stubs: 0xf00
-  __TEXT.__objc_methlist: 0x4bdc
+383.100.15.0.0
+  __TEXT.__text: 0x69634
+  __TEXT.__auth_stubs: 0xf20
+  __TEXT.__objc_methlist: 0x4ca4
   __TEXT.__const: 0xd86
   __TEXT.__gcc_except_tab: 0xbd8
-  __TEXT.__cstring: 0x540f
-  __TEXT.__oslogstring: 0xb3e7
+  __TEXT.__cstring: 0x54ff
+  __TEXT.__oslogstring: 0xb8c9
   __TEXT.__swift5_typeref: 0x278
   __TEXT.__constg_swiftt: 0x24c
   __TEXT.__swift5_fieldmd: 0x240

   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x16e8
+  __TEXT.__unwind_info: 0x1708
   __TEXT.__eh_frame: 0x4b0
   __TEXT.__objc_classname: 0x975
-  __TEXT.__objc_methname: 0xb018
-  __TEXT.__objc_methtype: 0x10f7
-  __TEXT.__objc_stubs: 0x80c0
-  __DATA_CONST.__got: 0x440
+  __TEXT.__objc_methname: 0xb262
+  __TEXT.__objc_methtype: 0x110c
+  __TEXT.__objc_stubs: 0x82c0
+  __DATA_CONST.__got: 0x448
   __DATA_CONST.__const: 0x1388
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2548
+  __DATA_CONST.__objc_selrefs: 0x25d0
   __DATA_CONST.__objc_superrefs: 0x1f8
-  __AUTH_CONST.__auth_got: 0x790
+  __AUTH_CONST.__auth_got: 0x7a0
   __AUTH_CONST.__auth_ptr: 0x1a8
   __AUTH_CONST.__const: 0xf10
-  __AUTH_CONST.__cfstring: 0x51e0
-  __AUTH_CONST.__objc_const: 0x8998
+  __AUTH_CONST.__cfstring: 0x53e0
+  __AUTH_CONST.__objc_const: 0x8a38
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x630
   __AUTH.__data: 0x300
-  __DATA.__objc_ivar: 0x44c
-  __DATA.__data: 0x778
+  __DATA.__objc_ivar: 0x454
+  __DATA.__data: 0x788
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x15f0
   __DATA.__common: 0x88

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2428
-  Symbols:   2517
-  CStrings:  3920
+  Functions: 2444
+  Symbols:   2538
+  CStrings:  3989
 
Symbols:
+ _CFPreferencesCopyValue
+ _kCFPreferencesAnyHost
+ _kDRSDMCoreDuetPeopleSuggesterShareSheetMadRequestTimeoutCategory
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
- _kDRSRequestADGContextDictKey
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initStructMetadataWithLayoutString
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
+ "NilHWModel"
+ "NilLikelyCarry"
+ "Not likely carry"
+ "OverwritingContextMetadataKey"
+ "PearlAFileBundle"
+ "ShareSheetMadRequestTimeout"
+ "Skipping due to non-Internal device"
+ "SkippingHWModel"
+ "SkippingIsLikelyCarry"
+ "T@\"NSNumber\",R,N"
+ "T@\"NSNumber\",R,N,V_isLikelyCarryGroupNum"
+ "T@\"NSString\",R,N,V_hwModel"
+ "Updated context metadata with new key: '%{public}@'"
+ "We dont reason about carry for non-Internal devices"
+ "__DPMD__"
+ "_addContextMetadataKey:value:expectedClass:errorOut:"
+ "_hwModel"
+ "_isLikelyCarryGroupNum"
+ "_pearlTeamConfiguration:isSeed:isCarrier:platform:"
+ "_populateHWModel"
+ "_populateIsCarry"
+ "addContextMetadataKey:numberValue:errorOut:"
+ "addContextMetadataKey:stringValue:errorOut:"
+ "addHWModelContextMetadata"
+ "addIsLikelyCarryContextMetadata"
+ "build                       = %{public}@\nbuildVariant                = %{public}@\ndeviceCategory              = %{public}@\ndeviceModel                 = %{public}@\nplatformString              = %{public}@\ndeviceHash                  = %{public}#llx\nisInternal                  = %{public}u\nisSeed                      = %{public}u\nisCarrier                   = %{public}u\ncustomerApprovesAnalytics   = %{public}u\nisLogUploadEnabled          = %{public}u\nisTaskingEnabled            = %{public}u\nuploadSessionUploadCapBytes = %{public}llu\nhwModel                     = %{public}@n\nisLikelyCarry               = %{public}@n\n"
+ "carry"
+ "com.apple.da"
+ "com.apple.pearl"
+ "containsString:"
+ "hw.model"
+ "hw.model: '%{public}@'"
+ "hwModel"
+ "isLikeCarryDevice"
+ "isLikelyCarryGroupNum"
+ "lowercaseString"
+ "metadataDictionary"
+ "mobile"
+ "numberWithInt:"
+ "pearlAFileBundleConfiguration"
+ "shareSheetMadRequestTimeoutConfiguration"
+ "walkabout"
- "#\x12"
- "Added ADG %{public}@ for request %{public}@"
- "AutomatedDeviceGroupContextUpdateFailure"
- "AutomatedDeviceGroupContextUpdated"
- "Failed to update context dictionary with ADG for request %{public}@"
- "__AutomatedDeviceGroup__"
- "build                       = %{public}@\nbuildVariant                = %{public}@\ndeviceCategory              = %{public}@\ndeviceModel                 = %{public}@\nplatformString              = %{public}@\ndeviceHash                  = %{public}#llx\nisInternal                  = %{public}u\nisSeed                      = %{public}u\nisCarrier                   = %{public}u\ncustomerApprovesAnalytics   = %{public}u\nisLogUploadEnabled          = %{public}u\nisTaskingEnabled            = %{public}u\nuploadSessionUploadCapBytes = %{public}llu\n"

```
