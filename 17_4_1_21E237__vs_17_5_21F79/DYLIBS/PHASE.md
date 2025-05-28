## PHASE

> `/System/Library/Frameworks/PHASE.framework/PHASE`

```diff

-270.5.7.0.0
-  __TEXT.__text: 0x1dfd50
-  __TEXT.__auth_stubs: 0x18b0
+270.6.3.0.0
+  __TEXT.__text: 0x1e04ac
+  __TEXT.__auth_stubs: 0x18d0
   __TEXT.__objc_methlist: 0x4b7c
   __TEXT.__const: 0x2ddc
-  __TEXT.__gcc_except_tab: 0x1e638
-  __TEXT.__oslogstring: 0x1b645
-  __TEXT.__cstring: 0x1036d
-  __TEXT.__unwind_info: 0x9e5c
+  __TEXT.__gcc_except_tab: 0x1e6c8
+  __TEXT.__oslogstring: 0x1b908
+  __TEXT.__cstring: 0x10457
+  __TEXT.__unwind_info: 0x9e74
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0xc59
   __TEXT.__objc_methname: 0xafc2
   __TEXT.__objc_methtype: 0x582d
   __TEXT.__objc_stubs: 0x63e0
-  __DATA_CONST.__got: 0x240
+  __DATA_CONST.__got: 0x248
   __DATA_CONST.__const: 0xe08
   __DATA_CONST.__objc_classlist: 0x3d8
   __DATA_CONST.__objc_protolist: 0x40

   __AUTH_CONST.__objc_const: 0x3918
   __AUTH_CONST.__auth_ptr: 0xb0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0xc68
+  __AUTH_CONST.__auth_got: 0xc78
   __AUTH.__objc_data: 0x2670
   __DATA.__got_weak: 0x8
   __DATA.__objc_ivar: 0x6d0

   - /usr/lib/libchannel.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 8089
-  Symbols:   21555
-  CStrings:  5713
+  Functions: 8095
+  Symbols:   21570
+  CStrings:  5720
 
Symbols:
+ __ZN5Phase10Controller12VoiceManager14Implementation16AcquireStateLockERNSt3__111unique_lockINS3_12shared_mutexEEENS2_15PendingCommandsEd
+ __ZN5Phase10Controller12VoiceManager14Implementation5StartEd
+ __ZNK5Phase10Controller6Submix19GetExternalStreamIdEv
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN5Phase14UniqueObjectIdES3_EENS_22__unordered_map_hasherIS3_S4_NS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S4_S9_S7_Lb1EEENS_9allocatorIS4_EEE14__erase_uniqueIS3_EEmRKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN5Phase14UniqueObjectIdES3_EENS_22__unordered_map_hasherIS3_S4_NS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S4_S9_S7_Lb1EEENS_9allocatorIS4_EEE5clearEv
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN5Phase14UniqueObjectIdES3_EENS_22__unordered_map_hasherIS3_S4_NS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S4_S9_S7_Lb1EEENS_9allocatorIS4_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS4_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN5Phase14UniqueObjectIdES3_EENS_22__unordered_map_hasherIS3_S4_NS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S4_S9_S7_Lb1EEENS_9allocatorIS4_EEE6removeENS_21__hash_const_iteratorIPNS_11__hash_nodeIS4_PvEEEE
+ __ZNSt3__119__shared_mutex_base8try_lockEv
+ __ZNSt3__120__throw_system_errorEiPKc
- __ZN5Phase10Controller12VoiceManager14Implementation5StartEv
CStrings:
+ "%25s:%-5d AcquireStateLock() failed with error %i"
+ "%25s:%-5d EXCEPTION (std::invalid_argument): \"[CVMVoiceManager::AcquireStateLock] Invalid action value %i for pending commands\""
+ "%25s:%-5d EXCEPTION (std::runtime_error) [not ChannelLayout::IsLayoutSupported(outputRoute.mChannelLayout) is true]: \"impl@%p: Output layout not supported, aborting engine initialization.\""
+ "%25s:%-5d impl@%p: Output layout not supported, with 0 output channels."
+ "%25s:%-5d impl@%p: Output layout not supported.\n                                    Falling back to mono.\n                                    Make sure that a valid speaker layout is set for the device in Audio and MIDI settings."
+ "%25s:%-5d impl@%p: Output layout not supported.\n                                    Falling back to stereo over the first 2 output channels.\n                                    Make sure that a valid speaker layout is set for the device in Audio and MIDI settings."
+ "%25s:%-5d impl@%p: acquiring voicemanager state lock timed out after %lli ms"
+ "[CVMVoiceManager::AcquireStateLock] Invalid action value %i for pending commands"
+ "impl@%p: Output layout not supported, aborting engine initialization."
+ "unique_lock::try_lock: already locked"
+ "unique_lock::try_lock: references null mutex"
- "%25s:%-5d Unsupported active output channel layout, falling back to stereo.\n%s"
- "%25s:%-5d [AudioIO::EndRouteChange] invalid mSuspendIOSemaphore value. Was the route change interrupted?"
- "%25s:%-5d [AudioIOPlatformAdapter] Route change skipped at timestamp %f"
- "%25s:%-5d impl@%p: Output layout not supported."

```
