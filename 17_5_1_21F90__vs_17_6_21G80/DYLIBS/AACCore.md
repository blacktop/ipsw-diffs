## AACCore

> `/System/Library/PrivateFrameworks/AACCore.framework/AACCore`

```diff

-13.5.10.0.0
-  __TEXT.__text: 0xd6f4
+13.6.5.0.0
+  __TEXT.__text: 0xda7c
   __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_methlist: 0x11b8
+  __TEXT.__objc_methlist: 0x1200
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0xc0a
-  __TEXT.__oslogstring: 0x248
+  __TEXT.__cstring: 0xc25
+  __TEXT.__oslogstring: 0x3eb
   __TEXT.__gcc_except_tab: 0xd4
-  __TEXT.__unwind_info: 0x59c
-  __TEXT.__objc_classname: 0x860
-  __TEXT.__objc_methname: 0x27a5
-  __TEXT.__objc_methtype: 0x7fb
-  __TEXT.__objc_stubs: 0x1740
+  __TEXT.__unwind_info: 0x5a8
+  __TEXT.__objc_classname: 0x8a4
+  __TEXT.__objc_methname: 0x286d
+  __TEXT.__objc_methtype: 0x810
+  __TEXT.__objc_stubs: 0x1760
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0x5b0
-  __DATA_CONST.__objc_classlist: 0x1a0
+  __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0xd0
+  __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3588
-  __DATA_CONST.__objc_selrefs: 0x838
+  __DATA_CONST.__objc_const: 0x3650
+  __DATA_CONST.__objc_selrefs: 0x868
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_classrefs: 0x1f8
-  __DATA_CONST.__objc_superrefs: 0x110
-  __AUTH_CONST.__cfstring: 0xb80
+  __DATA_CONST.__objc_superrefs: 0x108
+  __AUTH_CONST.__cfstring: 0xbc0
   __AUTH_CONST.__objc_const: 0x12a8
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__auth_got: 0x2d0
-  __AUTH.__objc_data: 0x1040
-  __DATA.__objc_ivar: 0x194
-  __DATA.__data: 0x9e0
+  __AUTH.__objc_data: 0x1090
+  __DATA.__objc_ivar: 0x190
+  __DATA.__data: 0xa40
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 489
-  Symbols:   1947
-  CStrings:  741
+  Functions: 498
+  Symbols:   1970
+  CStrings:  758
 
Symbols:
+ -[AEConcretePreferences setFailOnDeactivation:]
+ -[AEConcretePreferences setSetCustomHomeScreenLayout:]
+ -[AEConcretePreferences shouldFailOnDeactivation]
+ -[AEConcretePreferences shouldSetCustomHomeScreenLayout]
+ -[AEConcretePreferences shouldStopAirPlayBeforehand]
+ -[AEConcreteProcessInfoPrimitives hasEntitlement:]
+ -[AEEmptyPreferences setFailOnDeactivation:]
+ -[AEEmptyPreferences setSetCustomHomeScreenLayout:]
+ -[AEEmptyPreferences shouldFailOnDeactivation]
+ -[AEEmptyPreferences shouldSetCustomHomeScreenLayout]
+ -[AEEmptyPreferences shouldStopAirPlayBeforehand]
+ -[AEProcessInfoPrimitivesProvider makePrimitives]
+ _OBJC_CLASS_$_AEConcreteProcessInfoPrimitives
+ _OBJC_CLASS_$_AEProcessInfoPrimitivesProvider
+ _OBJC_METACLASS_$_AEConcreteProcessInfoPrimitives
+ _OBJC_METACLASS_$_AEProcessInfoPrimitivesProvider
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ __OBJC_$_INSTANCE_METHODS_AEConcreteProcessInfoPrimitives
+ __OBJC_$_INSTANCE_METHODS_AEProcessInfoPrimitivesProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AEProcessInfoPrimitives
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AEProcessInfoPrimitives
+ __OBJC_CLASS_PROTOCOLS_$_AEConcreteProcessInfoPrimitives
+ __OBJC_CLASS_RO_$_AEConcreteProcessInfoPrimitives
+ __OBJC_CLASS_RO_$_AEProcessInfoPrimitivesProvider
+ __OBJC_LABEL_PROTOCOL_$_AEProcessInfoPrimitives
+ __OBJC_METACLASS_RO_$_AEConcreteProcessInfoPrimitives
+ __OBJC_METACLASS_RO_$_AEProcessInfoPrimitivesProvider
+ __OBJC_PROTOCOL_$_AEProcessInfoPrimitives
+ ___50-[AEActivePolicySession deactivateWithCompletion:]_block_invoke_2.cold.1
+ ___50-[AEActivePolicySession deactivateWithCompletion:]_block_invoke_2.cold.2
+ ___52-[AERecoveryPolicySession deactivateWithCompletion:]_block_invoke.5.cold.2
+ __os_log_fault_impl
+ _objc_msgSend$cleanUpPolicyStoreWithError:
+ _objc_msgSend$exists
+ _objc_msgSend$isFailable
- -[AEConcreteFeatureFlags isiOSAgentEnabled]
- -[AEConcretePreferences shouldStopAirplayBeforehand]
- -[AEEmptyFeatureFlags isiOSAgentEnabled]
- -[AEEmptyPreferences shouldStopAirplayBeforehand]
- -[AEFeatureFlagsProvider .cxx_destruct]
- -[AEFeatureFlagsProvider init]
- _AEIsProcessEntitledForAssessmentMode
- _AEIsProcessEntitledForMultiApp
- _OBJC_CLASS_$_AEEmptyFeatureFlags
- _OBJC_IVAR_$_AEFeatureFlagsProvider._OSGestalt
- _OBJC_METACLASS_$_AEEmptyFeatureFlags
- __OBJC_$_INSTANCE_METHODS_AEConcreteFeatureFlags
- __OBJC_$_INSTANCE_METHODS_AEEmptyFeatureFlags
- __OBJC_$_INSTANCE_VARIABLES_AEFeatureFlagsProvider
- __OBJC_$_PROP_LIST_AEEmptyFeatureFlags
- __OBJC_$_PROP_LIST_AEFeatureFlags
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AEFeatureFlags
- __OBJC_$_PROTOCOL_METHOD_TYPES_AEFeatureFlags
- __OBJC_CLASS_PROTOCOLS_$_AEEmptyFeatureFlags
- __OBJC_CLASS_RO_$_AEEmptyFeatureFlags
- __OBJC_METACLASS_RO_$_AEEmptyFeatureFlags
- __os_feature_enabled_impl
- _objc_msgSend$isiOSAgentEnabled
- _objc_msgSend$removeAllScratchpadsWithError:
CStrings:
+ "AEConcreteProcessInfoPrimitives"
+ "AEProcessInfoPrimitives"
+ "AEProcessInfoPrimitivesProvider"
+ "An error occurred removing the scratchpad for deactivation with ID=%{public}@"
+ "B24@0:8@\"NSString\"16"
+ "FailOnDeactivationKey"
+ "Failed to clean up policy store. Error: %{public}@"
+ "Finished running deactivations"
+ "Finished running recovery session"
+ "IgnoreCustomHomeScreenLayout"
+ "No scratchpads are left after running deactivations. Cleaning up all state…"
+ "Removing scratchpad for completed deactivation with ID=%{public}@"
+ "Scratchpad will NOT be removed for failed deactivation with ID=%{public}@"
+ "Some scratchpads were not removed meaning some deactivations failed. Will reattempt to recover on next launch."
+ "TB,N,GshouldFailOnDeactivation"
+ "TB,N,GshouldSetCustomHomeScreenLayout"
+ "TB,N,GshouldStopAirPlayBeforehand"
+ "cleanUpPolicyStoreWithError:"
+ "exists"
+ "failOnDeactivation"
+ "hasEntitlement:"
+ "isFailable"
+ "setCustomHomeScreenLayout"
+ "setFailOnDeactivation:"
+ "setSetCustomHomeScreenLayout:"
+ "shouldFailOnDeactivation"
+ "shouldSetCustomHomeScreenLayout"
+ "shouldStopAirPlayBeforehand"
- "AEEmptyFeatureFlags"
- "AssessmentMode"
- "Failed to remove scratchpads. Error: %{public}@"
- "Finished running recovery session. Removing scratchpads"
- "TB,N,GshouldStopAirplayBeforehand"
- "TB,R,N,GisiOSAgentEnabled"
- "iOSAgent"
- "iOSAgentEnabled"
- "isiOSAgentEnabled"
- "removeAllScratchpadsWithError:"
- "shouldStopAirplayBeforehand"

```
