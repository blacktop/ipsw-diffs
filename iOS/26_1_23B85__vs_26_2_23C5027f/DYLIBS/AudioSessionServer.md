## AudioSessionServer

> `/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer`

```diff

-398.209.0.0.0
-  __TEXT.__text: 0x72ee4
-  __TEXT.__auth_stubs: 0x1140
+398.303.0.0.0
+  __TEXT.__text: 0x7317c
+  __TEXT.__auth_stubs: 0x1150
   __TEXT.__objc_methlist: 0xc08
-  __TEXT.__gcc_except_tab: 0xad1c
+  __TEXT.__gcc_except_tab: 0xad58
   __TEXT.__const: 0xc20
   __TEXT.__cstring: 0x508f
-  __TEXT.__oslogstring: 0x4fe5
+  __TEXT.__oslogstring: 0x504a
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x2d68
+  __TEXT.__unwind_info: 0x2d70
   __TEXT.__objc_classname: 0x178
   __TEXT.__objc_methname: 0x1d4d
-  __TEXT.__objc_methtype: 0x2544
+  __TEXT.__objc_methtype: 0x259e
   __TEXT.__objc_stubs: 0xf80
-  __DATA_CONST.__got: 0x4c0
+  __DATA_CONST.__got: 0x4c8
   __DATA_CONST.__const: 0x5e0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x7a0
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x8b0
+  __AUTH_CONST.__auth_got: 0x8b8
   __AUTH_CONST.__const: 0x10a0
   __AUTH_CONST.__cfstring: 0xf20
   __AUTH_CONST.__objc_const: 0xd08
-  __AUTH_CONST.__objc_intobj: 0xf0
+  __AUTH_CONST.__objc_intobj: 0x108
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x10
   __DATA.__objc_ivar: 0x68

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1D0C8C6C-2C41-3061-A1A8-3F342E24D7A9
+  UUID: B84499C8-4E32-34B3-98C7-688EE28177CC
   Functions: 1661
-  Symbols:   5764
-  CStrings:  1594
+  Symbols:   5766
+  CStrings:  1595
 
Symbols:
+ _kMXSessionAudioMode_DualRoute
+ _objc_retain_x27
Functions:
~ __ZNSt3__16vectorIN8nlohmann10basic_jsonINS_3mapES0_NS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbxydS7_NS1_14adl_serializerENS0_IhNS7_IhEEEEEENS7_ISD_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorIN8nlohmann10basic_jsonINS_3mapES0_NS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbxydS7_NS1_14adl_serializerENS0_IhNS7_IhEEEEEENS7_ISD_EEE7reserveEm : 188 -> 204
~ __ZN4avas6server10forbid_acq24SetPropertiesOnMXSessionEjRK13audit_token_tP12NSDictionaryIP8NSStringPU25objcproto14NSSecureCoding11objc_objectENS_30AVAudioSessionBatchSetStrategyEPU15__autoreleasingP7NSArrayIPS5_IS7_P8NSNumberEE : 4788 -> 5240
~ __ZNSt3__16__treeINS_12__value_typeIiU8__strongP16RBSProcessHandleEENS_19__map_value_compareIiS5_NS_4lessIiEELb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIiJNS_4pairIiS4_EEEEENSE_INS_15__tree_iteratorIS5_PNS_11__tree_nodeIS5_PvEElEEbEERKT_DpOT0_ : 244 -> 252
~ __ZNSt3__16vectorIN8nlohmann10basic_jsonINS_3mapES0_NS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbxydS7_NS1_14adl_serializerENS0_IhNS7_IhEEEEEENS7_ISD_EEE24__emplace_back_slow_pathIJSD_EEEPSD_DpOT_ : 296 -> 300
~ __ZNK4avas6server16AudioAppInfoImpl24GetAudioAppRemoteClientsEv : 436 -> 440
~ __ZN4avas6server20DeferredMessageState17EnqueueHasProxiesEjb : 396 -> 400
~ __ZN4avas6server20DeferredMessageState16EnqueueEventTypeENS1_9EventTypeE : 284 -> 288
~ __ZNSt3__16vectorIN5caulk7xstringENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_ : 276 -> 280
~ __ZNSt3__16vectorIN5caulk7xstringENS_9allocatorIS2_EEE18__assign_with_sizeB8ne200100IPS2_S7_EEvT_T0_l : 368 -> 372
~ __ZNSt3__16vectorIN5caulk7xstringENS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorIN4avas15RouteIdentifierENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_ : 268 -> 272
~ __ZNSt3__16vectorINS_4pairIjU8__strongP12NSDictionaryEENS_9allocatorIS5_EEE24__emplace_back_slow_pathIJS5_EEEPS5_DpOT_ : 288 -> 292
~ __ZNSt3__16vectorIN4avas6server12ControlValueENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_ : 300 -> 304
~ __ZN4avas6server16AudioSessionInfo15ResetAllPlayersEv : 1980 -> 1984
~ __ZNK4avas6server16AudioSessionInfo17DebugStateStringsEv : 680 -> 688
~ __ZNSt3__16vectorIPK10__CFStringNS_9allocatorIS3_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorIN4avas6server16AudioSessionInfo11PlayerStateENS_9allocatorIS4_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorINS_8weak_ptrIN4avas6server24AudioSessionRemoteClientEEENS_9allocatorIS5_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZN10applesauce2CF7details20make_CFDictionaryRefERKSt16initializer_listINS0_11TypeRefPairEE : 692 -> 708
~ __ZNSt3__16vectorIN4avas6server18DeviceTimeObserver16SharedBlockOwnerENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJPS3_RKmEEEPS4_DpOT_ : 280 -> 292
~ __ZNSt3__16vectorINS_4pairIN4avas6server18DeviceTimeObserver9DeviceKeyENS4_10DeviceInfoEEENS_9allocatorIS7_EEE8__appendEm : 412 -> 428
~ __ZN5caulk10concurrent25guarded_lookup_hash_tableIjP16BaseOpaqueObjectLNS0_33guarded_lookup_hash_table_optionsE0E24OpaqueObjectIdentityHashE6rehashEj : 292 -> 296
~ __ZNSt3__120back_insert_iteratorINS_6vectorINS_8weak_ptrIN4avas6server24AudioSessionRemoteClientEEENS_9allocatorIS6_EEEEEaSB8ne200100EOS6_ : 268 -> 272
~ __ZN4avas6server20LegacySessionManager45RemoveProxyClientsForInvalidatedXPCConnectionEP15NSXPCConnection : 880 -> 884
~ __ZNK4avas6server20LegacySessionManager21GetSessionIDsForTokenERK13audit_token_t : 780 -> 784
~ __ZN4avas6server20LegacySessionManager18HandleProcessDeathEi : 868 -> 872
~ __ZNSt3__16__treeINS_12__value_typeIU8__strongP8NSString13audit_token_tEENS_19__map_value_compareIS4_S6_NS_4lessIS4_EELb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIS4_JNS_4pairIU8__strongKS3_S5_EEEEENSF_INS_15__tree_iteratorIS6_PNS_11__tree_nodeIS6_PvEElEEbEERKT_DpOT0_ : 252 -> 260
~ __ZNSt3__16__treeINS_12__value_typeIU8__strongP8NSString13audit_token_tEENS_19__map_value_compareIS4_S6_NS_4lessIS4_EELb1EEENS_9allocatorIS6_EEE15__emplace_multiIJRKNS_4pairIU8__strongKS3_S5_EEEEENS_15__tree_iteratorIS6_PNS_11__tree_nodeIS6_PvEElEEDpOT_ : 208 -> 212
~ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE7reserveEm : 188 -> 204
~ __ZN10applesauce2CF7details20make_CFDictionaryRefERKNSt3__16vectorINS0_11TypeRefPairENS2_9allocatorIS4_EEEE : 776 -> 792
~ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKjRK37AVAudioSessionMicrophoneInjectionModeEEEPS3_DpOT_ : 280 -> 292
CStrings:
+ "%25s:%-5d Error setting DualRoute mode since AllowBluetoothHFP (EnableBluetoothRecording) is not set"
+ "@80@0:8@16{ProcessInfo={ProcessToken=I}@@{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}24@72"
+ "{ProcessInfo=\"token\"{ProcessToken=\"mValue\"I}\"xpcConnection\"@\"NSXPCConnection\"\"mClientRelay\"@\"AVAudioSessionXPCClientRelay\"\"mProcessName\"{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"\"{?=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}}"
+ "{set<std::pair<AVAudioMicrophoneMonitorClientType, unsigned long long>, std::less<std::pair<AVAudioMicrophoneMonitorClientType, unsigned long long>>, std::allocator<std::pair<AVAudioMicrophoneMonitorClientType, unsigned long long>>>=\"__tree_\"{__tree<std::pair<AVAudioMicrophoneMonitorClientType, unsigned long long>, std::less<std::pair<AVAudioMicrophoneMonitorClientType, unsigned long long>>, std::allocator<std::pair<AVAudioMicrophoneMonitorClientType, unsigned long long>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{synchronized<avas::server::DeferredMessageState, caulk::mach::unfair_lock, caulk::empty_atomic_interface<avas::server::DeferredMessageState>>=\"mMutex\"{unfair_lock=\"m_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}}\"mObject\"{DeferredMessageState=\"mMessagePending\"B\"mDeferredMessageCount\"I\"proxy\"@\"<SessionManagerXPCServerCallbackProtocol>\"\"mToken\"{ProcessToken=\"mValue\"I}\"mFIFO\"{vector<avas::server::DeferredMessageState::EventType, std::allocator<avas::server::DeferredMessageState::EventType>>=\"__begin_\"^i\"__end_\"^i\"\"{?=\"__cap_\"^i}}\"mDeferredConfigChange\"{optional<avas::server::ConfigChangeSummary>=\"\"(?=\"__null_state_\"c\"__val_\"{ConfigChangeSummary=\"_vptr$Base\"^^?\"_sessionChanges\"{vector<std::unique_ptr<avas::server::SessionUpdateSummary>, std::allocator<std::unique_ptr<avas::server::SessionUpdateSummary>>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}\"_hardwareSystemChange\"{unique_ptr<avas::server::ChangedObject, std::default_delete<avas::server::ChangedObject>>=\"\"{?=\"__ptr_\"^{ChangedObject}}}})\"__engaged_\"B}\"mDeferredDefaultRouteChanges\"{vector<avas::RouteIdentifier, std::allocator<avas::RouteIdentifier>>=\"__begin_\"^{RouteIdentifier}\"__end_\"^{RouteIdentifier}\"\"{?=\"__cap_\"^{RouteIdentifier}}}\"mDeferredStopForAppStateChange\"{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"\"{?=\"__cap_\"^I}}\"mDeferredNeedsStateSync\"{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"\"{?=\"__cap_\"^I}}\"mDeferredInterruptions\"{vector<std::pair<unsigned int, NSDictionary *>, std::allocator<std::pair<unsigned int, NSDictionary *>>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}\"mDeferredHasProxies\"{vector<std::pair<unsigned int, bool>, std::allocator<std::pair<unsigned int, bool>>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}\"mDeferredControlValueChanges\"{vector<avas::server::ControlValue, std::allocator<avas::server::ControlValue>>=\"__begin_\"^{ControlValue}\"__end_\"^{ControlValue}\"\"{?=\"__cap_\"^{ControlValue}}}}}"
+ "{tuple<int, std::string, int>={__tuple_impl<std::__tuple_indices<0, 1, 2>, int, std::string, int>=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}i}}20@0:8I16"
+ "{unique_ptr<std::promise<void>, std::default_delete<std::promise<void>>>=\"\"{?=\"__ptr_\"^v}}"
+ "{vector<unsigned int, std::allocator<unsigned int>>=^I^I{?=^I}}24@0:8r^{?=[8I]}16"
- "@80@0:8@16{ProcessInfo={ProcessToken=I}@@{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}24@72"
- "{ProcessInfo=\"token\"{ProcessToken=\"mValue\"I}\"xpcConnection\"@\"NSXPCConnection\"\"mClientRelay\"@\"AVAudioSessionXPCClientRelay\"\"mProcessName\"{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}"
- "{set<std::pair<AVAudioMicrophoneMonitorClientType, unsigned long long>, std::less<std::pair<AVAudioMicrophoneMonitorClientType, unsigned long long>>, std::allocator<std::pair<AVAudioMicrophoneMonitorClientType, unsigned long long>>>=\"__tree_\"{__tree<std::pair<AVAudioMicrophoneMonitorClientType, unsigned long long>, std::less<std::pair<AVAudioMicrophoneMonitorClientType, unsigned long long>>, std::allocator<std::pair<AVAudioMicrophoneMonitorClientType, unsigned long long>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
- "{synchronized<avas::server::DeferredMessageState, caulk::mach::unfair_lock, caulk::empty_atomic_interface<avas::server::DeferredMessageState>>=\"mMutex\"{unfair_lock=\"m_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}}\"mObject\"{DeferredMessageState=\"mMessagePending\"B\"mDeferredMessageCount\"I\"proxy\"@\"<SessionManagerXPCServerCallbackProtocol>\"\"mToken\"{ProcessToken=\"mValue\"I}\"mFIFO\"{vector<avas::server::DeferredMessageState::EventType, std::allocator<avas::server::DeferredMessageState::EventType>>=\"__begin_\"^i\"__end_\"^i\"__cap_\"^i}\"mDeferredConfigChange\"{optional<avas::server::ConfigChangeSummary>=\"\"(?=\"__null_state_\"c\"__val_\"{ConfigChangeSummary=\"_vptr$Base\"^^?\"_sessionChanges\"{vector<std::unique_ptr<avas::server::SessionUpdateSummary>, std::allocator<std::unique_ptr<avas::server::SessionUpdateSummary>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}\"_hardwareSystemChange\"{unique_ptr<avas::server::ChangedObject, std::default_delete<avas::server::ChangedObject>>=\"__ptr_\"^{ChangedObject}}})\"__engaged_\"B}\"mDeferredDefaultRouteChanges\"{vector<avas::RouteIdentifier, std::allocator<avas::RouteIdentifier>>=\"__begin_\"^{RouteIdentifier}\"__end_\"^{RouteIdentifier}\"__cap_\"^{RouteIdentifier}}\"mDeferredStopForAppStateChange\"{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__cap_\"^I}\"mDeferredNeedsStateSync\"{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__cap_\"^I}\"mDeferredInterruptions\"{vector<std::pair<unsigned int, NSDictionary *>, std::allocator<std::pair<unsigned int, NSDictionary *>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}\"mDeferredHasProxies\"{vector<std::pair<unsigned int, bool>, std::allocator<std::pair<unsigned int, bool>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}\"mDeferredControlValueChanges\"{vector<avas::server::ControlValue, std::allocator<avas::server::ControlValue>>=\"__begin_\"^{ControlValue}\"__end_\"^{ControlValue}\"__cap_\"^{ControlValue}}}}"
- "{tuple<int, std::string, int>={__tuple_impl<std::__tuple_indices<0, 1, 2>, int, std::string, int>=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}i}}20@0:8I16"
- "{unique_ptr<std::promise<void>, std::default_delete<std::promise<void>>>=\"__ptr_\"^v}"
- "{vector<unsigned int, std::allocator<unsigned int>>=^I^I^I}24@0:8r^{?=[8I]}16"

```
