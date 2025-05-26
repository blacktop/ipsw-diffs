## AudioSessionServer

> `/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer`

```diff

-263.1.8.30.2
-  __TEXT.__text: 0x52c64
-  __TEXT.__auth_stubs: 0xfd0
-  __TEXT.__objc_methlist: 0x5e0
-  __TEXT.__gcc_except_tab: 0x6620
+263.2.7.0.0
+  __TEXT.__text: 0x53b9c
+  __TEXT.__auth_stubs: 0x1010
+  __TEXT.__objc_methlist: 0x548
+  __TEXT.__gcc_except_tab: 0x6704
   __TEXT.__const: 0xb11
-  __TEXT.__cstring: 0x3ca0
+  __TEXT.__cstring: 0x3cd1
   __TEXT.__oslogstring: 0x2d8f
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x2390
+  __TEXT.__unwind_info: 0x23c4
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x168
-  __TEXT.__objc_methname: 0x181d
-  __TEXT.__objc_methtype: 0x268a
-  __TEXT.__objc_stubs: 0xd20
-  __DATA_CONST.__got: 0x300
+  __TEXT.__objc_classname: 0x12e
+  __TEXT.__objc_methname: 0x170b
+  __TEXT.__objc_methtype: 0x2660
+  __TEXT.__objc_stubs: 0xca0
+  __DATA_CONST.__got: 0x328
   __DATA_CONST.__const: 0x3a0
-  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x0
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x12d0
-  __DATA_CONST.__objc_selrefs: 0x5f0
-  __AUTH_CONST.__cfstring: 0x980
-  __AUTH_CONST.__const: 0x938
-  __AUTH_CONST.__objc_const: 0x288
-  __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x7f8
-  __AUTH.__objc_data: 0x50
+  __DATA_CONST.__objc_const: 0x1150
+  __DATA_CONST.__objc_selrefs: 0x5a0
+  __AUTH_CONST.__cfstring: 0x900
+  __AUTH_CONST.__const: 0x9b8
+  __AUTH_CONST.__objc_const: 0x1f8
+  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x818
   __DATA.__got_weak: 0x10
   __DATA.__objc_classrefs: 0xa0
-  __DATA.__objc_superrefs: 0x30
-  __DATA.__objc_ivar: 0x74
-  __DATA.__data: 0x309
+  __DATA.__objc_superrefs: 0x28
+  __DATA.__objc_ivar: 0x64
+  __DATA.__data: 0x249
   __DATA.__bss: 0x30
   __DATA.__common: 0x1
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__data: 0x30
-  __DATA_DIRTY.__bss: 0x1d8
+  __DATA_DIRTY.__bss: 0x230
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1573
-  Symbols:   4415
-  CStrings:  1153
+  Functions: 1581
+  Symbols:   4416
+  CStrings:  1129
 
Symbols:
+ -[AVAudioSessionRemoteXPCClient allowAppToInitiatePlaybackTemporarilyFromBackground:reply:]
+ -[AVAudioSessionRemoteXPCClient setProperties:values:MXProperties:batchStrategy:genericMXPipe:reply:]
+ -[AVAudioSessionRemoteXPCClient setSessionPlayState:playState:playerType:playerRef:modes:reply:]
+ GCC_except_table102
+ GCC_except_table129
+ GCC_except_table155
+ GCC_except_table164
+ GCC_except_table169
+ GCC_except_table171
+ GCC_except_table172
+ GCC_except_table178
+ GCC_except_table179
+ GCC_except_table180
+ GCC_except_table185
+ GCC_except_table190
+ GCC_except_table191
+ GCC_except_table192
+ GCC_except_table235
+ GCC_except_table237
+ GCC_except_table239
+ GCC_except_table241
+ GCC_except_table249
+ GCC_except_table251
+ GCC_except_table253
+ GCC_except_table257
+ GCC_except_table259
+ GCC_except_table261
+ GCC_except_table263
+ GCC_except_table99
+ __DefaultRuneLocale
+ __ZN12CAX4CCStringC2Ei
+ __ZN2as39VolumeNotificationPayloadsAreDuplicatesEP12NSDictionaryS1_
+ __ZN2as6server16AudioSessionInfo27DeferPropertyChangeCallbackEPK8NSStringP12NSDictionarybNSt3__18optionalINS7_8functionIFbS6_S6_EEEEE
+ __ZN2as6server28HandleDispatchBlockExceptionEPKcS2_S2_iyy
+ __ZNKSt3__110__function6__funcIZN2as6server20HandleMXNotificationEP26opaqueCMNotificationCenterPKvPK10__CFStringS7_S7_E3$_2NS_9allocatorISB_EEFbP12NSDictionarySF_EE7__cloneEPNS0_6__baseISG_EE
+ __ZNKSt3__110__function6__funcIZN2as6server20HandleMXNotificationEP26opaqueCMNotificationCenterPKvPK10__CFStringS7_S7_E3$_2NS_9allocatorISB_EEFbP12NSDictionarySF_EE7__cloneEv
+ __ZNKSt3__18functionIFbP12NSDictionaryS2_EEclES2_S2_
+ __ZNSt3__110__function12__value_funcIFbP12NSDictionaryS3_EEC2B7v160006ERKS5_
+ __ZNSt3__110__function12__value_funcIFbP12NSDictionaryS3_EED2B7v160006Ev
+ __ZNSt3__110__function6__funcIZN2as6server20HandleMXNotificationEP26opaqueCMNotificationCenterPKvPK10__CFStringS7_S7_E3$_2NS_9allocatorISB_EEFbP12NSDictionarySF_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN2as6server20HandleMXNotificationEP26opaqueCMNotificationCenterPKvPK10__CFStringS7_S7_E3$_2NS_9allocatorISB_EEFbP12NSDictionarySF_EE7destroyEv
+ __ZNSt3__110__function6__funcIZN2as6server20HandleMXNotificationEP26opaqueCMNotificationCenterPKvPK10__CFStringS7_S7_E3$_2NS_9allocatorISB_EEFbP12NSDictionarySF_EED0Ev
+ __ZNSt3__110__function6__funcIZN2as6server20HandleMXNotificationEP26opaqueCMNotificationCenterPKvPK10__CFStringS7_S7_E3$_2NS_9allocatorISB_EEFbP12NSDictionarySF_EED1Ev
+ __ZNSt3__110__function6__funcIZN2as6server20HandleMXNotificationEP26opaqueCMNotificationCenterPKvPK10__CFStringS7_S7_E3$_2NS_9allocatorISB_EEFbP12NSDictionarySF_EEclEOU8__strongSF_SJ_
+ __ZNSt3__112__destroy_atB7v160006INS_4pairIU8__strongKP8NSStringNS_10shared_ptrIN2as6server24BackgroundActivationInfoEEEEELi0EEEvPT_
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEi
+ __ZNSt3__120__optional_copy_baseINS_8functionIFbP12NSDictionaryS3_EEELb0EEC2B7v160006ERKS6_
+ __ZNSt3__16__treeINS_12__value_typeIU8__strongP8NSStringNS_10shared_ptrIN2as6server24BackgroundActivationInfoEEEEENS_19__map_value_compareIS4_SA_NS_4lessIS4_EELb1EEENS_9allocatorISA_EEE7destroyEPNS_11__tree_nodeISA_PvEE
+ __ZNSt3__19to_stringEy
+ __ZTVNSt3__110__function6__funcIZN2as6server20HandleMXNotificationEP26opaqueCMNotificationCenterPKvPK10__CFStringS7_S7_E3$_2NS_9allocatorISB_EEFbP12NSDictionarySF_EEE
+ __ZZN2as6server11require_acqL36AudioSessionSetClientPlayState_InnerEj30AVAudioSessionClientPlayerTypePvj29AVAudioSessionClientPlayStateP23AudioSessionDuckingInfoPKvENK3$_4clEv
+ __ZZN2as6server16AudioSessionInfo27DeferPropertyChangeCallbackEPK8NSStringP12NSDictionarybNSt3__18optionalINS7_8functionIFbS6_S6_EEEEEEN3$_5D1Ev
+ __ZZN2as6server20HandleMXNotificationEP26opaqueCMNotificationCenterPKvPK10__CFStringS4_S4_ENK3$_3clEbNSt3__18optionalINS9_8functionIFbP12NSDictionarySD_EEEEE
+ ___101-[AVAudioSessionRemoteXPCClient setProperties:values:MXProperties:batchStrategy:genericMXPipe:reply:]_block_invoke
+ ___96-[AVAudioSessionRemoteXPCClient setSessionPlayState:playState:playerType:playerRef:modes:reply:]_block_invoke
+ ____ZL30HandleInterruptionNotificationjP12NSDictionary_block_invoke.201
+ ____ZL30HandleInterruptionNotificationjP12NSDictionary_block_invoke.201.cold.1
+ ____ZL30HandleInterruptionNotificationjP12NSDictionary_block_invoke.201.cold.10
+ ____ZL30HandleInterruptionNotificationjP12NSDictionary_block_invoke.201.cold.11
+ ____ZL30HandleInterruptionNotificationjP12NSDictionary_block_invoke.201.cold.2
+ ____ZL30HandleInterruptionNotificationjP12NSDictionary_block_invoke.201.cold.3
+ ____ZL30HandleInterruptionNotificationjP12NSDictionary_block_invoke.201.cold.4
+ ____ZL30HandleInterruptionNotificationjP12NSDictionary_block_invoke.201.cold.5
+ ____ZL30HandleInterruptionNotificationjP12NSDictionary_block_invoke.201.cold.6
+ ____ZL30HandleInterruptionNotificationjP12NSDictionary_block_invoke.201.cold.7
+ ____ZL30HandleInterruptionNotificationjP12NSDictionary_block_invoke.201.cold.8
+ ____ZL30HandleInterruptionNotificationjP12NSDictionary_block_invoke.201.cold.9
+ ____ZN2as6server10forbid_acq24SetPropertiesOnMXSessionEjRK13audit_token_tP12NSDictionaryIP8NSStringPU25objcproto14NSSecureCoding11objc_objectENS_30AVAudioSessionBatchSetStrategyEPU15__autoreleasingP7NSArrayIPS5_IS7_P8NSNumberEE_block_invoke
+ ____ZZN2as6server20HandleMXNotificationEP26opaqueCMNotificationCenterPKvPK10__CFStringS4_S4_ENK3$_3clEbNSt3__18optionalINS9_8functionIFbP12NSDictionarySD_EEEEE_block_invoke
+ ___block_descriptor_56_ea8_32s_e5_v8?0ls32l8
+ ___block_descriptor_93_ea8_32s40s48c59_ZTSNSt3__18optionalINS_8functionIFbP12NSDictionaryS3_EEEEE_e5_v8?0l
+ ___block_literal_global.88
+ ___copy_helper_block_ea8_48c59_ZTSNSt3__18optionalINS_8functionIFbP12NSDictionaryS3_EEEEE
+ ___destroy_helper_block_ea8_48c59_ZTSNSt3__18optionalINS_8functionIFbP12NSDictionaryS3_EEEEE
+ ___maskrune
+ _kMXSystemControllerNotificationKey_SystemVolumeDidChange_AudioCategory
+ _kMXSystemControllerNotificationKey_SystemVolumeDidChange_AudioMode
+ _kMXSystemControllerNotification_SystemVolumeDidChange
+ _objc_msgSend$copy
+ _objc_retain_x27
- +[AVAudioApplicationSpecification supportsSecureCoding]
- -[AVAudioApplicationSpecification .cxx_destruct]
- -[AVAudioApplicationSpecification appAuditToken]
- -[AVAudioApplicationSpecification attributionBundleID]
- -[AVAudioApplicationSpecification audioAppType]
- -[AVAudioApplicationSpecification encodeWithCoder:]
- -[AVAudioApplicationSpecification initWithCoder:]
- -[AVAudioApplicationSpecification processName]
- -[AVAudioApplicationSpecification setAppAuditToken:]
- -[AVAudioApplicationSpecification setAttributionBundleID:]
- -[AVAudioApplicationSpecification setAudioAppType:]
- -[AVAudioApplicationSpecification setProcessName:]
- -[AVAudioSessionRemoteXPCClient setMXPropertyGenericPipe:values:reply:]
- -[AVAudioSessionRemoteXPCClient setProperties:values:MXProperties:batchStrategy:reply:]
- GCC_except_table101
- GCC_except_table149
- GCC_except_table160
- GCC_except_table165
- GCC_except_table167
- GCC_except_table168
- GCC_except_table173
- GCC_except_table174
- GCC_except_table175
- GCC_except_table176
- GCC_except_table182
- GCC_except_table186
- GCC_except_table187
- GCC_except_table188
- GCC_except_table227
- GCC_except_table229
- GCC_except_table231
- GCC_except_table233
- GCC_except_table234
- GCC_except_table236
- GCC_except_table238
- GCC_except_table240
- GCC_except_table242
- GCC_except_table244
- GCC_except_table246
- GCC_except_table76
- GCC_except_table87
- _OBJC_CLASS_$_AVAudioApplicationSpecification
- _OBJC_IVAR_$_AVAudioApplicationSpecification._appAuditToken
- _OBJC_IVAR_$_AVAudioApplicationSpecification.attributionBundleID
- _OBJC_IVAR_$_AVAudioApplicationSpecification.audioAppType
- _OBJC_IVAR_$_AVAudioApplicationSpecification.processName
- _OBJC_METACLASS_$_AVAudioApplicationSpecification
- __OBJC_$_CLASS_METHODS_AVAudioApplicationSpecification
- __OBJC_$_CLASS_PROP_LIST_AVAudioApplicationSpecification
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
- __OBJC_$_INSTANCE_METHODS_AVAudioApplicationSpecification
- __OBJC_$_INSTANCE_VARIABLES_AVAudioApplicationSpecification
- __OBJC_$_PROP_LIST_AVAudioApplicationSpecification
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding
- __OBJC_CLASS_PROTOCOLS_$_AVAudioApplicationSpecification
- __OBJC_CLASS_RO_$_AVAudioApplicationSpecification
- __OBJC_LABEL_PROTOCOL_$_NSCoding
- __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
- __OBJC_METACLASS_RO_$_AVAudioApplicationSpecification
- __OBJC_PROTOCOL_$_NSCoding
- __OBJC_PROTOCOL_$_NSSecureCoding
- __ZN12_GLOBAL__N_123BuildJSONRepresentationERKN2as6server26SessionCreationDescriptionEj
- __ZN2as6server16AudioSessionInfo27DeferPropertyChangeCallbackEPK8NSStringP12NSDictionaryb
- __ZZN2as6server11require_acqL36AudioSessionSetClientPlayState_InnerEj30AVAudioSessionClientPlayerTypePvj29AVAudioSessionClientPlayStateP23AudioSessionDuckingInfoPKvENK3$_3clEv
- __ZZN2as6server20HandleMXNotificationEP26opaqueCMNotificationCenterPKvPK10__CFStringS4_S4_ENK3$_2clEb
- ___71-[AVAudioSessionRemoteXPCClient setMXPropertyGenericPipe:values:reply:]_block_invoke
- ___87-[AVAudioSessionRemoteXPCClient setProperties:values:MXProperties:batchStrategy:reply:]_block_invoke
- ____ZL30HandleInterruptionNotificationjP12NSDictionary_block_invoke.194
- ____ZL30HandleInterruptionNotificationjP12NSDictionary_block_invoke.194.cold.1
- ____ZL30HandleInterruptionNotificationjP12NSDictionary_block_invoke.194.cold.10
- ____ZL30HandleInterruptionNotificationjP12NSDictionary_block_invoke.194.cold.11
- ____ZL30HandleInterruptionNotificationjP12NSDictionary_block_invoke.194.cold.2
- ____ZL30HandleInterruptionNotificationjP12NSDictionary_block_invoke.194.cold.3
- ____ZL30HandleInterruptionNotificationjP12NSDictionary_block_invoke.194.cold.4
- ____ZL30HandleInterruptionNotificationjP12NSDictionary_block_invoke.194.cold.5
- ____ZL30HandleInterruptionNotificationjP12NSDictionary_block_invoke.194.cold.6
- ____ZL30HandleInterruptionNotificationjP12NSDictionary_block_invoke.194.cold.7
- ____ZL30HandleInterruptionNotificationjP12NSDictionary_block_invoke.194.cold.8
- ____ZL30HandleInterruptionNotificationjP12NSDictionary_block_invoke.194.cold.9
- ____ZZN2as6server20HandleMXNotificationEP26opaqueCMNotificationCenterPKvPK10__CFStringS4_S4_ENK3$_2clEb_block_invoke
- ___block_descriptor_53_ea8_32s40s_e5_v8?0ls32l8s40l8
- ___block_literal_global.85
- _objc_msgSend$decodeIntegerForKey:
- _objc_msgSend$decodeObjectOfClass:forKey:
- _objc_msgSend$encodeInteger:forKey:
- _objc_msgSend$encodeObject:forKey:
- _objc_msgSend$getBytes:length:
CStrings:
+ "%d"
+ "-[AVAudioSessionRemoteXPCClient setProperties:values:MXProperties:batchStrategy:genericMXPipe:reply:]"
+ "-[AVAudioSessionRemoteXPCClient setSessionPlayState:playState:playerType:playerRef:modes:reply:]"
+ ":"
+ "; srcid:0x"
+ "Exception thrown: "
+ "SetPropertiesOnMXSession"
+ "allowAppToInitiatePlaybackTemporarilyFromBackground:reply:"
+ "copy"
+ "setProperties:values:MXProperties:batchStrategy:genericMXPipe:reply:"
+ "setSessionPlayState:playState:playerType:playerRef:modes:reply:"
+ "sid:0x"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
+ "v48@0:8I16@\"NSDictionary\"20B28i32B36@?<v@?@\"NSError\"@\"NSArray\">40"
+ "v48@0:8I16@20B28i32B36@?40"
+ "v48@0:8I16I20I24@\"NSString\"28I36@?<v@?@\"NSError\">40"
+ "v48@0:8I16I20I24@28I36@?40"
- "\x12"
- "-[AVAudioSessionRemoteXPCClient setMXPropertyGenericPipe:values:reply:]"
- "-[AVAudioSessionRemoteXPCClient setProperties:values:MXProperties:batchStrategy:reply:]"
- "@\"NSString\""
- "@24@0:8@\"NSCoder\"16"
- "AVAudioApplicationSpecification"
- "NSCoding"
- "NSSecureCoding"
- "T@\"NSString\",&,N,VattributionBundleID"
- "T@\"NSString\",&,N,VprocessName"
- "TB,R"
- "Tq,N,VaudioAppType"
- "T{?=[8I]},N,V_appAuditToken"
- "_appAuditToken"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "getBytes:length:"
- "initWithCoder:"
- "q16@0:8"
- "setAppAuditToken:"
- "setAttributionBundleID:"
- "setAudioAppType:"
- "setMXPropertyGenericPipe:values:reply:"
- "setProcessName:"
- "setProperties:values:MXProperties:batchStrategy:reply:"
- "supportsSecureCoding"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8q16"
- "v36@0:8I16@\"NSDictionary\"20@?<v@?@\"NSError\">28"
- "v44@0:8I16@\"NSDictionary\"20B28i32@?<v@?@\"NSError\"@\"NSArray\">36"
- "v44@0:8I16@20B28i32@?36"
- "v48@0:8{?=[8I]}16"
- "{?=\"val\"[8I]}"
- "{?=[8I]}16@0:8"

```
