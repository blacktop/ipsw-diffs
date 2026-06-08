## IdleTimerHosting

> `/System/Library/PrivateFrameworks/IdleTimerHosting.framework/IdleTimerHosting`

```diff

 40.0.0.0.0
-  __TEXT.__text: 0x2f08
-  __TEXT.__auth_stubs: 0x3c0
+  __TEXT.__text: 0x2d00
   __TEXT.__objc_methlist: 0x62c
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x4fd
+  __TEXT.__cstring: 0x50a
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__oslogstring: 0x278
-  __TEXT.__unwind_info: 0x1f0
-  __TEXT.__objc_classname: 0x11d
-  __TEXT.__objc_methname: 0xf5e
-  __TEXT.__objc_methtype: 0x476
-  __TEXT.__objc_stubs: 0xac0
-  __DATA_CONST.__got: 0xa0
+  __TEXT.__unwind_info: 0x1e8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3f0
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x1f0
+  __DATA_CONST.__got: 0xa0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x420
   __AUTH_CONST.__objc_const: 0x11e8
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x5c
   __DATA.__data: 0x1e8
   __DATA_DIRTY.__objc_data: 0x230

   - /System/Library/PrivateFrameworks/PrototypeTools.framework/PrototypeTools
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F93F8F94-22BE-3112-820D-26EA318C718A
-  Functions: 119
-  Symbols:   540
-  CStrings:  318
+  UUID: 529C9638-5033-3163-89CA-0F9C7CADEA5E
+  Functions: 117
+  Symbols:   538
+  CStrings:  85
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<ITAttentionAwarenessClientDelegate>\""
- "@\"<ITIdleTimerDelegate>\""
- "@\"AWAttentionAwarenessClient\""
- "@\"BSDescriptionBuilder\"16@0:8"
- "@\"BSDescriptionBuilder\"24@0:8@\"NSString\"16"
- "@\"ITAttentionAwarenessClient\""
- "@\"ITAttentionAwarenessContext\""
- "@\"ITAttentionAwarenessSettings\""
- "@\"ITIdleTimerDescriptor\""
- "@\"NSArray\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"NSString\"16"
- "@\"NSUUID\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8d16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8d16Q24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@48@0:8@16@24@32@40"
- "@?24@0:8Q16"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "BSDescriptionProviding"
- "ITAttentionAwareIdleTimer"
- "ITAttentionAwarenessClient"
- "ITAttentionAwarenessClientDelegate"
- "ITAttentionAwarenessContext"
- "ITAttentionAwarenessDomain"
- "ITAttentionAwarenessSettings"
- "ITIdleTimeout"
- "ITIdleTimerDescriptor"
- "NSCopying"
- "NSObject"
- "PTSettingsKeyObserver"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"<ITAttentionAwarenessClientDelegate>\",W,N,V_delegate"
- "T@\"<ITIdleTimerDelegate>\",R,W,N,V_delegate"
- "T@\"AWAttentionAwarenessClient\",&,N,V_access_attentionAwarenessClient"
- "T@\"AWAttentionAwarenessConfiguration\",&,N"
- "T@\"ITAttentionAwarenessContext\",R,N"
- "T@\"ITIdleTimerDescriptor\",R,C,N"
- "T@\"NSArray\",C,N,V_timeouts"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSUUID\",R,C,N,V_identifier"
- "TB,N,GisEnabled"
- "TB,N,GisEnabled,V_access_enabled"
- "TB,N,V_nonSampledAttentionLostTimeoutEnable"
- "TQ,R"
- "TQ,R,N,V_attentionMaintenanceEventMask"
- "TQ,R,N,V_attentionRecoveryEventMask"
- "TQ,R,N,V_identifier"
- "Td,N"
- "Td,N,V_attentionSamplingPeriod"
- "Td,N,V_attentionSamplingStartDelay"
- "Td,N,V_nonSampledAttentionLostTimeout"
- "Td,R,N,V_duration"
- "UUID"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_accessLock"
- "_access_attentionAwarenessClient"
- "_access_client"
- "_access_context"
- "_access_descriptor"
- "_access_enabled"
- "_access_generateConfiguration"
- "_access_reconfigureAttentionClientAndReset:"
- "_access_resume"
- "_access_suspend"
- "_attentionMaintenanceEventMask"
- "_attentionRecoveryEventMask"
- "_attentionSamplingPeriod"
- "_attentionSamplingStartDelay"
- "_configurationIdentifier"
- "_configurationWithIdentifier:descriptor:context:"
- "_context"
- "_delegate"
- "_duration"
- "_handleAttentionAwarenessEvent:"
- "_identifier"
- "_initWithCalloutQueue:attentionAwarenessClient:"
- "_initWithConfigurationIdentifier:delegate:calloutQueue:client:"
- "_nonSampledAttentionLostTimeout"
- "_nonSampledAttentionLostTimeoutEnable"
- "_prototypeSettingsChanged"
- "_settings"
- "_timeoutDictionaryForTimeouts:"
- "_timeouts"
- "addKeyObserver:"
- "allKeys"
- "allocWithZone:"
- "appendArraySection:withName:skipIfEmpty:"
- "appendObject:withName:"
- "appendTimeInterval:withName:decomposeUnits:"
- "appendUInt64:withName:"
- "arrayWithObjects:count:"
- "associatedObject"
- "attentionLostTimeout"
- "attentionSamplingStartBeforeFirstTimeout"
- "autorelease"
- "build"
- "builderWithObject:"
- "class"
- "client:attentionLostTimeoutDidExpire:forContext:"
- "clientDidReset:forUserAttentionEvent:withContext:"
- "configuration"
- "conformsToProtocol:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentHandler"
- "d"
- "d16@0:8"
- "debugDescription"
- "delegate"
- "description"
- "descriptionBuilderWithMultilinePrefix:"
- "descriptionWithMultilinePrefix:"
- "domainGroupName"
- "domainName"
- "doubleValue"
- "enabled"
- "eventMask"
- "firstObject"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hash"
- "idleTimer:attentionLostTimeoutDidExpire:"
- "idleTimerDidReset:forUserAttention:at:"
- "init"
- "initWithCalloutQueue:"
- "initWithConfigurationIdentifier:delegate:"
- "initWithConfigurationIdentifier:delegate:calloutQueue:"
- "initWithDuration:"
- "initWithDuration:identifier:"
- "isEnabled"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "itidletimerdescriptor_appendTimeInterval:withName:"
- "moduleWithTitle:contents:"
- "numberWithDouble:"
- "numberWithUnsignedInteger:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "reset"
- "respondsToSelector:"
- "resumeWithError:"
- "retain"
- "retainCount"
- "rootSettings"
- "rootSettingsClass"
- "rowWithTitle:valueKeyPath:"
- "sectionWithRows:title:"
- "self"
- "setAttentionEventMaintenanceMask:recoveryMask:"
- "setAttentionEventMask:"
- "setAttentionLostEventMask:"
- "setAttentionLostTimeoutDictionary:"
- "setAttentionSamplingPeriod:"
- "setAttentionSamplingStartBeforeFirstTimeout:"
- "setAttentionSamplingStartDelay:"
- "setConfiguration:"
- "setConfiguration:shouldReset:"
- "setDefaultValues"
- "setDelegate:"
- "setDescriptor:resettingTimer:"
- "setEnabled:"
- "setEventHandlerWithQueue:block:"
- "setEventMask:"
- "setIdentifier:"
- "setNonSampledAttentionLostTimeout:"
- "setNonSampledAttentionLostTimeoutEnable:"
- "setObject:forKeyedSubscript:"
- "setSamplingDelay:"
- "setSamplingInterval:"
- "setTag:"
- "setTimeouts:"
- "set_access_attentionAwarenessClient:"
- "settings:changedValueForKey:"
- "settingsControllerModule"
- "succinctDescription"
- "succinctDescriptionBuilder"
- "superclass"
- "suspendWithError:"
- "tag"
- "timeoutGeneratorUsingIdentifier:"
- "timestamp"
- "unsignedIntegerValue"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v28@0:8@16B24"
- "v32@0:8@\"PTSettings\"16@\"NSString\"24"
- "v32@0:8@16@24"
- "v32@0:8Q16Q24"
- "v32@0:8d16@24"
- "v40@0:8@\"ITAttentionAwarenessClient\"16@\"AWAttentionEvent\"24@\"ITAttentionAwarenessContext\"32"
- "v40@0:8@\"ITAttentionAwarenessClient\"16@\"ITIdleTimeout\"24@\"ITAttentionAwarenessContext\"32"
- "v40@0:8@16@24@32"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}"

```
