## HomeAppIntents

> `/System/Library/PrivateFrameworks/HomeAppIntents.framework/HomeAppIntents`

```diff

-1025.0.0.1.1
-  __TEXT.__text: 0x18e9b8
-  __TEXT.__auth_stubs: 0x2f40
-  __TEXT.__const: 0x1f6e8
-  __TEXT.__cstring: 0x3332
-  __TEXT.__swift5_typeref: 0xccde
-  __TEXT.__swift5_reflstr: 0x2c73
+1026.5.8.0.0
+  __TEXT.__text: 0x1a76c4
+  __TEXT.__auth_stubs: 0x30d0
+  __TEXT.__const: 0x1f778
+  __TEXT.__cstring: 0x3352
+  __TEXT.__swift5_typeref: 0xcd82
+  __TEXT.__swift5_reflstr: 0x2c83
   __TEXT.__swift5_assocty: 0x40e0
-  __TEXT.__constg_swiftt: 0x2720
-  __TEXT.__swift5_fieldmd: 0x3618
-  __TEXT.__swift5_builtin: 0x104
+  __TEXT.__constg_swiftt: 0x270c
+  __TEXT.__swift5_fieldmd: 0x35fc
+  __TEXT.__swift5_builtin: 0x118
   __TEXT.__swift5_proto: 0x1e2c
   __TEXT.__swift5_types: 0x4c8
-  __TEXT.__swift_as_entry: 0x638
-  __TEXT.__swift_as_ret: 0x50c
-  __TEXT.__swift5_capture: 0x390
-  __TEXT.__oslogstring: 0x1e79
+  __TEXT.__swift_as_entry: 0x620
+  __TEXT.__swift_as_ret: 0x504
+  __TEXT.__oslogstring: 0x2859
+  __TEXT.__swift5_capture: 0x208
   __TEXT.__swift5_mpenum: 0x50
-  __TEXT.__unwind_info: 0x6d28
-  __TEXT.__eh_frame: 0x8c98
-  __TEXT.__objc_methname: 0x5a
-  __DATA_CONST.__got: 0xfe8
+  __TEXT.__unwind_info: 0x6ea8
+  __TEXT.__eh_frame: 0x9568
+  __TEXT.__objc_methname: 0xa5
+  __DATA_CONST.__got: 0x10c8
   __DATA_CONST.__const: 0x7f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x17a0
-  __AUTH_CONST.__auth_ptr: 0xd20
-  __AUTH_CONST.__const: 0x7df0
-  __AUTH.__data: 0x9c0
-  __DATA.__data: 0x8460
+  __DATA_CONST.__objc_selrefs: 0x78
+  __AUTH_CONST.__auth_got: 0x1868
+  __AUTH_CONST.__auth_ptr: 0xd50
+  __AUTH_CONST.__const: 0x7bc8
+  __AUTH.__data: 0x938
+  __DATA.__data: 0x8430
   __DATA.__common: 0xa70
   __DATA.__bss: 0x3c940
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9439
-  Symbols:   193
-  CStrings:  636
+  Functions: 9511
+  Symbols:   203
+  CStrings:  674
 
Symbols:
+ _MTRCommandPathKey
+ _MTRDataKey
+ _MTRErrorKey
+ _OBJC_CLASS_$_MTRAttributeReport
+ _OBJC_CLASS_$_MTRCommandPath
+ _OBJC_CLASS_$_MTRRVCCleanModeClusterChangeToModeResponseParams
+ _OBJC_CLASS_$_MTRRVCOperationalStateClusterOperationalCommandResponseParams
+ _OBJC_CLASS_$_MTRRVCRunModeClusterChangeToModeResponseParams
+ _objc_allocWithZone
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_getObjCClassFromMetadata
+ _swift_projectBox
- _objc_retain_x25
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_getExistentialTypeMetadata
- _swift_initEnumMetadataMultiPayloadWithLayoutString
- _swift_initStructMetadataWithLayoutString
- _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
- _swift_multiPayloadEnumGeneric_getEnumTag
CStrings:
+ "%s-%s Using gathered snapshot"
+ "%s: Cannot cancel. Current state (%{public}s) is not an allowed states (%{public}s)"
+ "%s: Cannot pause. Current state (%{public}s) is not an active state"
+ "%s: Cannot resume. Current state (%{public}s) is not paused"
+ "%s: Clean Mode contains neither vacuum or mop: (%{public}s)"
+ "%s: Device is alrady in requested state: (%{public}s)"
+ "%{public}s-%s: For performing attribute %{public}s, planning to invoke commands: %{public}s"
+ "%{public}s-%s: Invoking commands %{public}s"
+ "Double has exponentBitCount %ld and significandBitCount %ld"
+ "Executing partial set of commands: %s"
+ "Failed to parse response for RVCCleanMode/ChangeToMode: %s"
+ "Failed to parse response for RVCOperationalState/%s: %s)"
+ "Failed to parse response for RVCRunMode/ChangeToMode: %s"
+ "Finished performing commands on device with results: %s"
+ "Got request to set attributes for endpoint %{public}s outside of home %{public}s. Ignoring..."
+ "Handling request to start rvc while paused. Stopping current run first."
+ "MTRDeviceCommandGroupInvocation"
+ "Produced 0 commands for attribute %{public}s, skipping"
+ "Provided UUIDs did not match any devices in home. SuccessDeviceIDS: %s | failedDeviceIDs: %s"
+ "Received badly formed result from invoking commands (ignoring): %s"
+ "Robot Vacuum Battery Is Low"
+ "Selecting areaIDs %{public}s from avaliable areas: %s"
+ "Selecting mapID %{public}u from avaliable maps: %s"
+ "Skipping execution of all commands due to validation errors: %s"
+ "Skipping partial execution of commands due to validation errors: %s"
+ "Tried to convert a Int larger than max to UInt32: %ld"
+ "Tried to convert a Int lower than 0 to UInt32: %ld"
+ "Unexpected run state %{public}s. Not changing run mode"
+ "Unknown cluster ID %{public}@ in result %s"
+ "Using areaIDs %{public}s from avaliable areas: %s"
+ "cluster"
+ "command"
+ "initWithResponseValue:error:"
+ "integerValue"
+ "overrideAttributesWriting: Can't choose to resume rvc %{public}llu because current clean mode { id: %{public}lu, label: %s, primaryTags: %{public}s } doesn't match requested tags %{public}s"
+ "overrideAttributesWriting: Can't choose to resume rvc %{public}llu because requested areas { areaIDs:%s, mapID:%s } don't match current areas %s"
+ "overrideAttributesWriting: Choosing to resume rvc %{public}llu (%s) because clean modes and service area match"
+ "overrideAttributesWriting: Requested to start rvc %{public}llu (%s) with attribute %{public}s but rvc is paused"
+ "overrideAttributesWriting: doesn't support service area"
+ "overrideAttributesWriting: requested { areaIDs: %{public}s, mapID: %{public}s } which mapped to nil areas to select. Allowing resuming the RVC"
+ "rvcBatteryLow"
+ "unsignedIntValue"
+ "validationError(for:)"
- "AttributeResult { kind: "
- "DeviceResult { device: "
- "Got request to set attributes for endpoint %{public}s outside of home %{public}s. Ignoring"
- "Skipping execution of commands due to validation errors: %s"
- "app intent execution"

```
