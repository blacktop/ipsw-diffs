## DeviceAccess

> `/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess`

```diff

-2701.6.0.0.0
-  __TEXT.__text: 0x553dc
-  __TEXT.__objc_methlist: 0x48bc
-  __TEXT.__const: 0x908
-  __TEXT.__cstring: 0xa793
-  __TEXT.__gcc_except_tab: 0x1370
+2702.5.0.0.0
+  __TEXT.__text: 0x56a6c
+  __TEXT.__objc_methlist: 0x4a1c
+  __TEXT.__const: 0xaf8
+  __TEXT.__cstring: 0xaae3
+  __TEXT.__gcc_except_tab: 0x1360
   __TEXT.__constg_swiftt: 0x3b8
   __TEXT.__swift5_typeref: 0x25a
   __TEXT.__swift5_builtin: 0x3c

   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_capture: 0x1c
-  __TEXT.__unwind_info: 0x1a80
+  __TEXT.__unwind_info: 0x1af8
   __TEXT.__eh_frame: 0x4d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xea8
-  __DATA_CONST.__objc_classlist: 0x200
+  __DATA_CONST.__const: 0xed8
+  __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x70
+  __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2078
+  __DATA_CONST.__objc_selrefs: 0x2108
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x190
-  __DATA_CONST.__objc_arraydata: 0x68
-  __DATA_CONST.__got: 0x540
+  __DATA_CONST.__objc_superrefs: 0x198
+  __DATA_CONST.__objc_arraydata: 0x70
+  __DATA_CONST.__got: 0x550
   __AUTH_CONST.__const: 0x6f0
-  __AUTH_CONST.__cfstring: 0x3860
-  __AUTH_CONST.__objc_const: 0x8510
+  __AUTH_CONST.__cfstring: 0x3960
+  __AUTH_CONST.__objc_const: 0x8698
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH_CONST.__auth_got: 0xc28
-  __AUTH.__objc_data: 0xe8
+  __AUTH_CONST.__auth_got: 0xc30
+  __AUTH.__objc_data: 0x138
   __AUTH.__data: 0x90
-  __DATA.__objc_ivar: 0x764
-  __DATA.__data: 0xc08
+  __DATA.__objc_ivar: 0x774
+  __DATA.__data: 0xc68
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x12e8
   __DATA_DIRTY.__data: 0x270

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2358
-  Symbols:   3425
-  CStrings:  1566
+  Functions: 2396
+  Symbols:   3476
+  CStrings:  1588
 
Symbols:
+ +[DAExtensionEventEligibility supportsSecureCoding]
+ -[DAExtension _capabilitiesReconcileFromRunnableFlags:reason:]
+ -[DAExtension _removeCapabilityWithFlag:reason:]
+ -[DAExtension _runnableFlags]
+ -[DAExtension _setEnrolledFlags:assertedFlags:]
+ -[DAExtension assertedFlags]
+ -[DAExtension setEnrolledFlags:assertedFlags:]
+ -[DAExtensionCapabilityXPCStartConfiguration capabilityFlag]
+ -[DAExtensionCapabilityXPCStartConfiguration descriptionWithLevel:]
+ -[DAExtensionCapabilityXPCStartConfiguration setCapabilityFlag:]
+ -[DAExtensionEventEligibility descriptionWithLevel:]
+ -[DAExtensionEventEligibility description]
+ -[DAExtensionEventEligibility eligibleFlags]
+ -[DAExtensionEventEligibility encodeWithCoder:]
+ -[DAExtensionEventEligibility encodeWithXPCObject:]
+ -[DAExtensionEventEligibility initWithCoder:]
+ -[DAExtensionEventEligibility initWithDevice:]
+ -[DAExtensionEventEligibility initWithXPCObject:error:]
+ -[DAExtensionEventEligibility setEligibleFlags:]
+ -[DAExtensionSessionConfiguration extensionTypeFlags]
+ -[DAExtensionSessionConfiguration isListeningForEvent:]
+ -[DAExtensionSessionConfiguration setExtensionTypeFlags:]
+ -[DAExtensionXPCStartConfiguration descriptionWithLevel:]
+ -[DAExtensionXPCStartConfiguration description]
+ -[DASession getEligibleCapabilityFlags:completionHandler:]
+ -[DASession requestFeatureAuthorization:deviceIdentifier:completionHandler:]
+ GCC_except_table104
+ GCC_except_table123
+ GCC_except_table129
+ GCC_except_table133
+ GCC_except_table145
+ GCC_except_table39
+ GCC_except_table45
+ GCC_except_table51
+ GCC_except_table56
+ GCC_except_table58
+ GCC_except_table71
+ GCC_except_table75
+ GCC_except_table85
+ GCC_except_table99
+ _DAExtensionCapabilityAssertionAttributes
+ _DAExtensionCapabilityEligibilityDomain
+ _DAExtensionCapabilityFlagsEligible
+ _OBJC_CLASS_$_DAExtensionEventEligibility
+ _OBJC_CLASS_$_RBSDomainAttribute
+ _OBJC_IVAR_$_DAExtension._assertedFlags
+ _OBJC_IVAR_$_DAExtensionCapabilityXPCStartConfiguration._capabilityFlag
+ _OBJC_IVAR_$_DAExtensionEventEligibility._eligibleFlags
+ _OBJC_IVAR_$_DAExtensionSessionConfiguration._extensionTypeFlags
+ _OBJC_METACLASS_$_DAExtensionEventEligibility
+ __OBJC_$_CLASS_METHODS_DAExtensionEventEligibility
+ __OBJC_$_INSTANCE_METHODS_DAExtensionEventEligibility
+ __OBJC_$_INSTANCE_VARIABLES_DAExtensionEventEligibility
+ __OBJC_$_PROP_LIST_DAExtensionEventEligibility
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CUDebugExtensions
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CUDebugExtensions
+ __OBJC_CLASS_RO_$_DAExtensionEventEligibility
+ __OBJC_LABEL_PROTOCOL_$_CUDebugExtensions
+ __OBJC_METACLASS_RO_$_DAExtensionEventEligibility
+ __OBJC_PROTOCOL_$_CUDebugExtensions
+ ___46-[DAExtension setEnrolledFlags:assertedFlags:]_block_invoke
+ ___58-[DASession getEligibleCapabilityFlags:completionHandler:]_block_invoke
+ ___58-[DASession getEligibleCapabilityFlags:completionHandler:]_block_invoke_2
+ ___76-[DASession requestFeatureAuthorization:deviceIdentifier:completionHandler:]_block_invoke
+ ___76-[DASession requestFeatureAuthorization:deviceIdentifier:completionHandler:]_block_invoke_2
+ ___DAExtensionCapabilityFlagsEligible_block_invoke
+ ___block_descriptor_48_e8_32bs_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8
+ ___block_descriptor_56_e8_32s40r_e21_v20?0C8"NSString"12ls32l8r40l8
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ _os_eligibility_get_domain_answer
- -[DAExtension _capabilitiesEnsureStoppedWithFlags:error:]
- -[DAExtension setEnrolledFlags:]
- GCC_except_table121
- GCC_except_table127
- GCC_except_table131
- GCC_except_table139
- GCC_except_table36
- GCC_except_table44
- GCC_except_table48
- GCC_except_table50
- GCC_except_table57
- GCC_except_table65
- GCC_except_table89
- GCC_except_table91
- GCC_except_table96
- ___32-[DAExtension setEnrolledFlags:]_block_invoke
- ___57-[DAExtension _capabilitiesEnsureStoppedWithFlags:error:]_block_invoke
- ___block_descriptor_56_e8_32r_e5_v8?0lr32l8
- ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
CStrings:
+ "-[DAExtension _capabilitiesReconcileFromRunnableFlags:reason:]"
+ "-[DAExtension _removeCapabilityWithFlag:reason:]"
+ "-[DAExtension _setEnrolledFlags:assertedFlags:]"
+ "-[DAExtensionSessionConfiguration isListeningForEvent:]"
+ "-[DASession getEligibleCapabilityFlags:completionHandler:]_block_invoke_2"
+ "-[DASession requestFeatureAuthorization:deviceIdentifier:completionHandler:]_block_invoke_2"
+ "AccessoryTransportExtension"
+ "AppExtensionGPUBackground"
+ "AsrtFl %@"
+ "Asserted capabilities changed: %@ -> %@: %@"
+ "AssertionReleased"
+ "Capability %@ no longer runnable (%@), stopping: %@"
+ "Capability %@ runnable, starting: %@"
+ "DAErrorCodeIneligible"
+ "ElFl %@"
+ "ElgF"
+ "EligibilityChanged"
+ "GetEligibleCapabilityFlags completed: %@ -> %@, %@"
+ "RqFA"
+ "Session: No device identifier"
+ "Session: invalid feature requested: %@"
+ "Session: only one capability may be requested at a time, received %@"
+ "Skip event reporting, configuration is not listening for data events %@: %@"
+ "Skip event reporting, configuration is not listening for lifecycle events %@: %@"
+ "Skip event reporting, configuration is not listening for this capability %@: %@"
+ "Verifying runnableFlags %@, inFlags %@, capabilityFlag %@"
+ "com.apple.extensionkit"
+ "exElF"
+ "exTyFl"
+ "no command"
+ "requestFeatureAuthorization completed: %@ on '%@', level %tu, %@"
- "### EnsureCapabilityStopped %@: %@"
- "-[DAExtension _capabilitiesEnsureStoppedWithFlags:error:]"
- "-[DAExtension _capabilitiesEnsureStoppedWithFlags:error:]_block_invoke"
- "-[DAExtension _removeCapabilityWithFlag:]"
- "-[DAExtension setEnrolledFlags:]_block_invoke"
- "Capability %@ enrolled, starting: %@"
- "Capability %@ un-enrolled, stopping: %@"
- "Stopping %@"
- "Verifying enrolledFlags %@, inFlags %@, capabilityFlag %@"
```
