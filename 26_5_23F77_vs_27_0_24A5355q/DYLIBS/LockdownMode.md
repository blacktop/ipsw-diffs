## LockdownMode

> `/System/Library/PrivateFrameworks/LockdownMode.framework/LockdownMode`

```diff

-80.120.2.0.0
-  __TEXT.__text: 0x3d8c
-  __TEXT.__auth_stubs: 0x540
-  __TEXT.__objc_methlist: 0x1b4
-  __TEXT.__const: 0x1c8
-  __TEXT.__cstring: 0xf6
-  __TEXT.__constg_swiftt: 0xac
-  __TEXT.__swift5_typeref: 0x11e
-  __TEXT.__swift5_fieldmd: 0x68
-  __TEXT.__swift5_types: 0x10
-  __TEXT.__swift5_capture: 0xe0
-  __TEXT.__oslogstring: 0x171
-  __TEXT.__swift5_reflstr: 0x32
-  __TEXT.__swift5_proto: 0xc
-  __TEXT.__unwind_info: 0x1c0
-  __TEXT.__objc_classname: 0x9c
-  __TEXT.__objc_methname: 0x3ff
-  __TEXT.__objc_methtype: 0x1c7
-  __TEXT.__objc_stubs: 0x360
-  __DATA_CONST.__got: 0x68
+122.0.0.0.0
+  __TEXT.__text: 0xd804
+  __TEXT.__objc_methlist: 0x3fc
+  __TEXT.__const: 0x3e4
+  __TEXT.__cstring: 0x2c6
+  __TEXT.__constg_swiftt: 0xc8
+  __TEXT.__swift5_typeref: 0x2e6
+  __TEXT.__swift5_fieldmd: 0x13c
+  __TEXT.__swift5_types: 0x14
+  __TEXT.__oslogstring: 0x7a2
+  __TEXT.__swift5_capture: 0x2e0
+  __TEXT.__swift5_reflstr: 0x1c2
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__swift5_proto: 0x10
+  __TEXT.__swift_as_entry: 0x14
+  __TEXT.__swift_as_ret: 0x14
+  __TEXT.__swift_as_cont: 0x28
+  __TEXT.__unwind_info: 0x3c0
+  __TEXT.__eh_frame: 0x3a8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x8
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf0
-  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_selrefs: 0x220
+  __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x2a8
-  __AUTH_CONST.__const: 0x678
-  __AUTH_CONST.__objc_const: 0x2c8
+  __DATA_CONST.__got: 0xd8
+  __AUTH_CONST.__const: 0xc30
+  __AUTH_CONST.__objc_const: 0x570
+  __AUTH_CONST.__auth_got: 0x538
   __AUTH.__objc_data: 0x48
-  __AUTH.__data: 0x98
+  __AUTH.__data: 0xa8
   __DATA.__objc_ivar: 0x4
-  __DATA.__data: 0x70
-  __DATA.__bss: 0x180
-  __DATA_DIRTY.__objc_data: 0xc0
-  __DATA_DIRTY.__data: 0x50
+  __DATA.__data: 0x228
+  __DATA.__bss: 0x200
+  __DATA_DIRTY.__objc_data: 0xf8
+  __DATA_DIRTY.__data: 0x90
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: C9513CD3-6F9C-39CF-9AD1-D346EC3C1037
-  Functions: 192
-  Symbols:   310
-  CStrings:  74
+  UUID: E539FFAE-0BF7-34A5-9AB3-EB1CDA49A3E4
+  Functions: 368
+  Symbols:   604
+  CStrings:  53
 
Symbols:
+ -[LockdownModeManager addObserver:]
+ -[LockdownModeManager getExemptContactIdentifiersAndHandlesWithError:]
+ -[LockdownModeManager isContactIdentifierExempt_ForUIUseOnly:]
+ -[LockdownModeManager isSenderHandleExempt:handleType:]
+ -[LockdownModeManager removeExemptHandlesForContactIdentifier:completion:]
+ -[LockdownModeManager removeObserver:]
+ -[LockdownModeManager setExemptHandlesWithPhoneNumbers:emails:otherHandles:forContactIdentifier:completion:]
+ -[LockdownModeManager setThreatNotificationDate:completion:]
+ -[LockdownModeManager threatNotificationDate]
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_CLASS_$_OS_dispatch_queue
+ __OBJC_$_INSTANCE_METHODS_LockdownModeManagerInternal(LockdownMode|LockdownMode1|LockdownMode2)
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LockdownModeManagerObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LockdownModeManagerObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_LockdownModeManagerObserver
+ __OBJC_LABEL_PROTOCOL_$_LockdownModeManagerObserver
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_LockdownModeManagerObserver
+ __OBJC_PROTOCOL_$_NSObject
+ __PROTOCOL_INSTANCE_METHODS__TtP12LockdownMode30LockdownModeExemptionsProtocol_
+ __PROTOCOL_METHOD_TYPES__TtP12LockdownMode30LockdownModeExemptionsProtocol_
+ __PROTOCOL_PROTOCOLS__TtP12LockdownMode20LockdownModeProtocol_
+ __PROTOCOL__TtP12LockdownMode30LockdownModeExemptionsProtocol_
+ ___swift__destructor
+ ___swift__destructor.176
+ ___swift__destructor.64
+ ___swift__destructor.67
+ ___swift_async_cont_functlets
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.106
+ ___swift_closure_destructor.109
+ ___swift_closure_destructor.114
+ ___swift_closure_destructor.118
+ ___swift_closure_destructor.123
+ ___swift_closure_destructor.126
+ ___swift_closure_destructor.13
+ ___swift_closure_destructor.133
+ ___swift_closure_destructor.137
+ ___swift_closure_destructor.147
+ ___swift_closure_destructor.151
+ ___swift_closure_destructor.158
+ ___swift_closure_destructor.162
+ ___swift_closure_destructor.166
+ ___swift_closure_destructor.173
+ ___swift_closure_destructor.182
+ ___swift_closure_destructor.192
+ ___swift_closure_destructor.197
+ ___swift_closure_destructor.202
+ ___swift_closure_destructor.224
+ ___swift_closure_destructor.25
+ ___swift_closure_destructor.31
+ ___swift_closure_destructor.40
+ ___swift_closure_destructor.46
+ ___swift_closure_destructor.56
+ ___swift_closure_destructor.56Tm
+ ___swift_closure_destructor.60
+ ___swift_closure_destructor.70
+ ___swift_closure_destructor.70Tm
+ ___swift_closure_destructor.77
+ ___swift_closure_destructor.83
+ ___swift_closure_destructor.83Tm
+ ___swift_closure_destructor.87
+ ___swift_closure_destructor.94
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_memcpy17_8
+ ___swift_memcpy1_1
+ __swiftEmptyDictionarySingleton
+ __swift_implicitisolationactor_to_executor_cast
+ _associated conformance 12LockdownMode0aB12FeatureFlagsOSHAASQ
+ _block_copy_helper.129
+ _block_copy_helper.140
+ _block_copy_helper.143
+ _block_copy_helper.15
+ _block_copy_helper.154
+ _block_copy_helper.169
+ _block_copy_helper.178
+ _block_copy_helper.18
+ _block_copy_helper.184
+ _block_copy_helper.204
+ _block_copy_helper.207
+ _block_copy_helper.21
+ _block_copy_helper.210
+ _block_copy_helper.213
+ _block_copy_helper.216
+ _block_copy_helper.220
+ _block_copy_helper.226
+ _block_copy_helper.27
+ _block_copy_helper.33
+ _block_copy_helper.36
+ _block_copy_helper.42
+ _block_copy_helper.48
+ _block_copy_helper.51
+ _block_copy_helper.79
+ _block_copy_helper.9
+ _block_copy_helper.96
+ _block_descriptor.11
+ _block_descriptor.131
+ _block_descriptor.142
+ _block_descriptor.145
+ _block_descriptor.156
+ _block_descriptor.17
+ _block_descriptor.171
+ _block_descriptor.180
+ _block_descriptor.186
+ _block_descriptor.20
+ _block_descriptor.206
+ _block_descriptor.209
+ _block_descriptor.212
+ _block_descriptor.215
+ _block_descriptor.218
+ _block_descriptor.222
+ _block_descriptor.228
+ _block_descriptor.23
+ _block_descriptor.29
+ _block_descriptor.35
+ _block_descriptor.38
+ _block_descriptor.44
+ _block_descriptor.50
+ _block_descriptor.53
+ _block_descriptor.81
+ _block_descriptor.98
+ _block_destroy_helper.10
+ _block_destroy_helper.130
+ _block_destroy_helper.141
+ _block_destroy_helper.144
+ _block_destroy_helper.155
+ _block_destroy_helper.16
+ _block_destroy_helper.170
+ _block_destroy_helper.179
+ _block_destroy_helper.185
+ _block_destroy_helper.19
+ _block_destroy_helper.205
+ _block_destroy_helper.208
+ _block_destroy_helper.211
+ _block_destroy_helper.214
+ _block_destroy_helper.217
+ _block_destroy_helper.22
+ _block_destroy_helper.221
+ _block_destroy_helper.227
+ _block_destroy_helper.28
+ _block_destroy_helper.34
+ _block_destroy_helper.37
+ _block_destroy_helper.43
+ _block_destroy_helper.49
+ _block_destroy_helper.52
+ _block_destroy_helper.80
+ _block_destroy_helper.97
+ _bzero
+ _flat unique So27LockdownModeManagerObserver_p
+ _get_enum_tag_for_layout_string 12LockdownMode0aB12ManagerErrorO
+ _get_type_metadata 15Synchronization5MutexVySDySSSaySSGGSgG noncopyable.101
+ _get_type_metadata 15Synchronization5MutexVySDySSSbGG noncopyable.100
+ _get_type_metadata 15Synchronization5MutexVySo11NSHashTableCySo27LockdownModeManagerObserver_pGG noncopyable.102
+ _notify_cancel
+ _notify_register_dispatch
+ _objc_autorelease
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$addObject:
+ _objc_msgSend$addObserver:
+ _objc_msgSend$allObjects
+ _objc_msgSend$getExemptContactIdentifiersAndHandlesWithCompletion:
+ _objc_msgSend$getExemptContactIdentifiersAndHandlesWithError:
+ _objc_msgSend$getThreatNotificationDateWithCompletion:
+ _objc_msgSend$isContactIdentifierExempt_ForUIUseOnly:
+ _objc_msgSend$isHandleExempt:type:completion:
+ _objc_msgSend$isSenderHandleExempt:handleType:
+ _objc_msgSend$lockdownModeExemptContactsDidChange
+ _objc_msgSend$lockdownModeStateDidChange:
+ _objc_msgSend$removeExemptHandlesForContactIdentifier:completion:
+ _objc_msgSend$removeObject:
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$respondsToSelector:
+ _objc_msgSend$setExemptHandlesWithPhoneNumbers:emails:otherHandles:forContactIdentifier:completion:
+ _objc_msgSend$setThreatNotificationDate:completion:
+ _objc_msgSend$threatNotificationDate
+ _objc_msgSend$weakObjectsHashTable
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x24
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x6
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_allocBox
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_getObjCClassMetadata
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_projectBox
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x25
+ _swift_retain_x27
+ _swift_runtimeSupportsNoncopyableTypes
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _swift_willThrow
+ _symbolic $s12LockdownMode0aB18ExemptionsProtocolP
+ _symbolic SDySSSaySSGGSg
+ _symbolic SDySSSaySSGGSgz_Xx
+ _symbolic SDySSSbG
+ _symbolic SS
+ _symbolic SS11featureFlag_t
+ _symbolic SS7message_t
+ _symbolic SaySSG
+ _symbolic Say_____G 8Dispatch0A13WorkItemFlagsV
+ _symbolic Say_____G So17OS_dispatch_queueC8DispatchE10AttributesV
+ _symbolic Say______pG So27LockdownModeManagerObserverP
+ _symbolic SbSg
+ _symbolic SbSgz_Xx
+ _symbolic ScA_pSg
+ _symbolic ScCySb______pG s5ErrorP
+ _symbolic ScPSg
+ _symbolic So17OS_dispatch_queueC
+ _symbolic _____ 12LockdownMode0aB12FeatureFlagsO
+ _symbolic _____ s5Int32V
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic _____SgXw 12LockdownMode0aB7ManagerC
+ _symbolic ______p So27LockdownModeManagerObserverP
+ _symbolic ______p s5ErrorP
+ _symbolic ______pSg s5ErrorP
+ _symbolic ______pSgz_Xx s5ErrorP
+ _symbolic _____ySDySSSaySSGGSgG 15Synchronization5MutexVAARi_zrlE
+ _symbolic _____ySDySSSbGG 15Synchronization5MutexVAARi_zrlE
+ _symbolic _____ySSSaySSGG s18_DictionaryStorageC
+ _symbolic _____ySSSbG s18_DictionaryStorageC
+ _symbolic _____ySo11NSHashTableCG 15Synchronization5MutexVAARi_zrlE
+ _symbolic ytIeAgHr_
+ _type_layout_string 12LockdownMode0aB12ManagerErrorO
- __INSTANCE_METHODS_LockdownModeManagerInternal
- ___swift_destroy_boxed_opaque_existential_0
- _associated conformance 12LockdownMode0aB12ManagerErrorOSHAASQ
- _block_copy_helper.10
- _block_copy_helper.101
- _block_copy_helper.16
- _block_copy_helper.19
- _block_copy_helper.22
- _block_copy_helper.28
- _block_copy_helper.34
- _block_copy_helper.37
- _block_copy_helper.43
- _block_copy_helper.58
- _block_copy_helper.61
- _block_copy_helper.86
- _block_copy_helper.92
- _block_copy_helper.95
- _block_copy_helper.98
- _block_descriptor.100
- _block_descriptor.103
- _block_descriptor.12
- _block_descriptor.18
- _block_descriptor.21
- _block_descriptor.24
- _block_descriptor.30
- _block_descriptor.36
- _block_descriptor.39
- _block_descriptor.45
- _block_descriptor.60
- _block_descriptor.63
- _block_descriptor.88
- _block_descriptor.94
- _block_descriptor.97
- _block_destroy_helper.102
- _block_destroy_helper.11
- _block_destroy_helper.17
- _block_destroy_helper.20
- _block_destroy_helper.23
- _block_destroy_helper.29
- _block_destroy_helper.35
- _block_destroy_helper.38
- _block_destroy_helper.44
- _block_destroy_helper.59
- _block_destroy_helper.62
- _block_destroy_helper.87
- _block_destroy_helper.93
- _block_destroy_helper.96
- _block_destroy_helper.99
CStrings:
+ "Clearing exemption cache"
+ "Contact exemptions feature flag is disabled"
+ "ContactExemptions"
+ "Could not obtain synchronous proxy for handle exemption check"
+ "DynamicEnablement"
+ "ExemptionManager"
+ "Failed to fetch exemptions: %@"
+ "Failed to get exempt contact identifiers."
+ "Failed to register Lockdown Mode exemption change notification: %u"
+ "Failed to register Lockdown Mode state change notification: %u"
+ "Found %ld exempt contacts"
+ "Handles unchanged for contact: %{private}s"
+ "Lockdown Mode is not enabled, skipping getExemptContactIdentifiersAndHandles"
+ "Lockdown Mode is not enabled, skipping isContactIdentifierExempt_ForUIUseOnly"
+ "Lockdown Mode is not enabled, skipping isSenderHandleExempt"
+ "Lockdown Mode is not enabled, skipping setExemptHandles"
+ "LockdownMode/ContactExemptions"
+ "LockdownModeManager observers queue"
+ "LockdownModeManager state change notifications queue"
+ "No handles found for contact: %{private}s"
+ "Removing exempt handles for contact: %{private}s"
+ "Retrieving all exempt contacts and handles"
+ "Setting exempt handles for contact (phoneNumbers: %ld, emails: %ld, otherHandles: %ld): %{private}s"
+ "Successfully removed handles for contact: %{private}s"
+ "Successfully updated handles for contact (phoneNumbers: %ld, emails: %ld, otherHandles: %ld): %{private}s"
+ "addObserver"
+ "com.apple.LockdownMode.exemptContactsDidChange"
+ "com.apple.LockdownMode.stateDidChange"
+ "handleExemptionChangeNotification (observers: %ld)"
+ "handleStateChangeNotification (enabled: %{bool}d, observers: %ld)"
+ "lookupCachedExemptionValue(forHandle:)"
+ "registerExemptionChangeNotification"
+ "registerStateChangeNotification"
+ "removeExemptHandles(forContactIdentifier:)"
+ "removeObserver"
+ "setCachedExemptionValue(_:forHandle:)"
+ "setExemptHandles(phoneNumbers:emails:otherHandles:forContactIdentifier:)"
+ "unregisterStateChangeNotification"
- "$__lazy_storage_$_connection"
- ".cxx_destruct"
- "@\"LockdownModeManagerInternal\""
- "@16@0:8"
- "B16@0:8"
- "LockdownModeManager"
- "LockdownModeManagerInternal"
- "T@\"LockdownModeManagerInternal\",N,R"
- "T@\"LockdownModeManagerInternal\",R,V_underlyingObject"
- "TB,N,R"
- "TB,R,N"
- "_TtC12LockdownMode15LockdownModeXNU"
- "_TtP12LockdownMode20LockdownModeProtocol_"
- "_underlyingObject"
- "dealloc"
- "enableIfNeeded:completion:"
- "enableIfNeededWithReboot:completion:"
- "enabled"
- "enabledInAccount"
- "getEnabledInAccount:completion:"
- "getEnabledInAccountWithSynchronize:completion:"
- "init"
- "initWithMachServiceName:options:"
- "interfaceWithProtocol:"
- "migrateIfNeededWithCompletion:"
- "notifyRestrictionChanged:"
- "notifyRestrictionChanged:completion:"
- "objectForKey:inDomain:"
- "rebootIfNeeded"
- "rebootIfNeededWithCompletion:"
- "remoteObjectProxyWithErrorHandler:"
- "resume"
- "setEnabled:options:completion:"
- "setEnabledWithEnabled:options:completion:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setManagedConfigurationState:completion:"
- "setManagedConfigurationStateWithEnabled:completion:"
- "setRemoteObjectInterface:"
- "shared"
- "standardUserDefaults"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "underlyingObject"
- "v12@?0B8"
- "v16@0:8"
- "v16@?0@\"NSError\"8"
- "v20@?0B8@\"NSError\"12"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?@\"NSError\">20"
- "v28@0:8B16@?<v@?B>20"
- "v28@0:8B16@?<v@?B@\"NSError\">20"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@?24"
- "v36@0:8B16@\"NSDictionary\"20@?<v@?@\"NSError\">28"
- "v36@0:8B16@20@?28"

```
