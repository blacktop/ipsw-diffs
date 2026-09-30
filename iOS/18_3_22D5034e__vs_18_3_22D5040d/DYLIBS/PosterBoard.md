## PosterBoard

> `/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard`

```diff

-228.3.24.100.0
-  __TEXT.__text: 0x1a02a8
-  __TEXT.__auth_stubs: 0x2a80
-  __TEXT.__objc_methlist: 0xa098
+228.3.25.0.0
+  __TEXT.__text: 0x19fe30
+  __TEXT.__auth_stubs: 0x2a60
+  __TEXT.__objc_methlist: 0xa0c0
   __TEXT.__const: 0x2374
   __TEXT.__gcc_except_tab: 0x45a4
-  __TEXT.__cstring: 0x14b5b
-  __TEXT.__oslogstring: 0x147b2
+  __TEXT.__cstring: 0x14c3b
+  __TEXT.__oslogstring: 0x149b2
   __TEXT.__dlopen_cstrs: 0x26e
   __TEXT.__ustring: 0xe
-  __TEXT.__swift5_typeref: 0x1ec4
-  __TEXT.__constg_swiftt: 0x3768
+  __TEXT.__swift5_typeref: 0x1e76
+  __TEXT.__constg_swiftt: 0x3730
   __TEXT.__swift5_builtin: 0x118
-  __TEXT.__swift5_reflstr: 0x276b
-  __TEXT.__swift5_fieldmd: 0x1668
+  __TEXT.__swift5_reflstr: 0x270b
+  __TEXT.__swift5_fieldmd: 0x1650
   __TEXT.__swift5_assocty: 0x150
   __TEXT.__swift5_proto: 0xd0
   __TEXT.__swift5_types: 0x110
   __TEXT.__swift5_capture: 0x1194
   __TEXT.__swift5_protos: 0x40
-  __TEXT.__unwind_info: 0x4d48
-  __TEXT.__eh_frame: 0x8e0
+  __TEXT.__unwind_info: 0x4d40
+  __TEXT.__eh_frame: 0x8a8
   __TEXT.__objc_classname: 0x228b
-  __TEXT.__objc_methname: 0x289f8
+  __TEXT.__objc_methname: 0x289fb
   __TEXT.__objc_methtype: 0x882a
-  __TEXT.__objc_stubs: 0x173a0
-  __DATA_CONST.__got: 0x1428
+  __TEXT.__objc_stubs: 0x17480
+  __DATA_CONST.__got: 0x13f8
   __DATA_CONST.__const: 0x46c0
   __DATA_CONST.__objc_classlist: 0x630
   __DATA_CONST.__objc_catlist: 0xe0

   __DATA_CONST.__objc_protorefs: 0x208
   __DATA_CONST.__objc_superrefs: 0x398
   __DATA_CONST.__objc_arraydata: 0xd0
-  __AUTH_CONST.__auth_got: 0x1550
-  __AUTH_CONST.__auth_ptr: 0x798
-  __AUTH_CONST.__const: 0x5468
-  __AUTH_CONST.__cfstring: 0xa740
-  __AUTH_CONST.__objc_const: 0x328b0
+  __AUTH_CONST.__auth_got: 0x1540
+  __AUTH_CONST.__auth_ptr: 0x7c0
+  __AUTH_CONST.__const: 0x5488
+  __AUTH_CONST.__cfstring: 0xa7c0
+  __AUTH_CONST.__objc_const: 0x32890
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x78

   __AUTH.__objc_data: 0x2320
   __AUTH.__data: 0x4b8
   __DATA.__objc_ivar: 0xe8c
-  __DATA.__data: 0x3a68
-  __DATA.__bss: 0xb00
+  __DATA.__data: 0x3a48
+  __DATA.__bss: 0xb10
   __DATA.__common: 0x90
-  __DATA_DIRTY.__objc_data: 0x5d58
-  __DATA_DIRTY.__data: 0xf40
+  __DATA_DIRTY.__objc_data: 0x5d10
+  __DATA_DIRTY.__data: 0xf10
   __DATA_DIRTY.__crash_info: 0x40
   __DATA_DIRTY.__bss: 0xbd0
   __DATA_DIRTY.__common: 0x60

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7154
-  Symbols:   6619
-  CStrings:  10078
+  Functions: 7157
+  Symbols:   6624
+  CStrings:  10087
 
Symbols:
+ _PBFLogHostConfiguration
- _OBJC_CLASS_$_CHSConfiguredWidgetContainerDescriptor
- _OBJC_CLASS_$_CHSConfiguredWidgetDescriptor
- _OBJC_CLASS_$_CHSMutableConfiguredWidgetDescriptor
- _OBJC_CLASS_$_CHSWidgetConfiguration
- _OBJC_CLASS_$_CHSWidgetHost
- _OBJC_CLASS_$_CHSWidgetMetricsSpecification
- _PRSharedWidgetDescriptorProvider
CStrings:
+ "Failed to get updated poster configurations for role %{public}@: %{public}@"
+ "Getting updated poster configurations for role %{public}@; initial posters: %{public}@"
+ "Got updated poster configurations for role %{public}@: %{public}@"
+ "HostConfiguration"
+ "_stateLock_updatePosterConfigurationsFromHostForRole:error:"
+ "differenceFromOrderedSet:"
+ "entryWithExtensionID:descriptorID:posterUUID:"
+ "isSubsetOfOrderedSet:"
+ "minusOrderedSet:"
+ "server:updatePosterConfigurationsFromHostForRole:completion:"
+ "updatePosterConfigurationsFromHostForRole: Skipping poster configuration with no descriptorIdentifier"
+ "updatePosterConfigurationsFromHostForRole: Skipping poster configuration with no provider"
+ "updatePosterConfigurationsFromHostForRole: Updated poster UUIDs are empty"
+ "updatePosterConfigurationsFromHostForRole: Updated poster UUIDs are not a subset of existing poster UUIDs"
+ "updatePosterConfigurationsFromHostForRole: Updated poster UUIDs are not a subset of existing poster UUIDs: %{public}@"
+ "updatePosterConfigurationsFromHostForRole: failed to update data store: %{public}@"
+ "updatePosterConfigurationsFromHostForRole: failed with unknown error"
+ "updatePosterConfigurationsFromHostForRole:%@"
+ "updatePosterConfigurationsFromHostForRole:error:"
+ "updatedPosterConfigurationsForRole:currentHostConfiguration:error:"
+ "widgetDescriptorForWidget:"
- "$__lazy_storage_$_lockScreenWidgetMetricsSpecifications"
- "$__lazy_storage_$_widgetHost"
- "PosterRackCollectionViewController doesn't manage widget hosting, skipping update for %@"
- "Updating switcher widget host configuration for selected poster %@ with widgets: %s"
- "descriptorForPersonality:"
- "initWithContainerDescriptors:metricsSpecification:"
- "initWithIdentifier:configuration:active:"
- "initWithUniqueIdentifier:location:canAppearInSecureEnvironment:page:family:widgets:activeWidget:"
- "initWithUniqueIdentifier:widget:metrics:"
- "lockScreenWidgetMetricsSpecifications"
- "setSupportedColorSchemes:"
- "setSupportedRenderSchemes:"
- "setSupportsLowLuminance:"

```
