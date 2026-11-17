## AudioSession

> `/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`

```diff

-449.302.0.0.0
-  __TEXT.__text: 0x4e114
+449.305.0.0.0
+  __TEXT.__text: 0x4e10c
   __TEXT.__realtime: 0x178
   __TEXT.__objc_methlist: 0x236c
-  __TEXT.__gcc_except_tab: 0x9038
-  __TEXT.__cstring: 0x3a61
+  __TEXT.__gcc_except_tab: 0x9040
+  __TEXT.__cstring: 0x3a95
   __TEXT.__const: 0x207
   __TEXT.__oslogstring: 0x4878
   __TEXT.__unwind_info: 0x31c8

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x868
+  __DATA_CONST.__const: 0x870
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1688
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0xb70
+  __DATA_CONST.__got: 0xb78
   __AUTH_CONST.__const: 0x1c98
-  __AUTH_CONST.__cfstring: 0x22a0
+  __AUTH_CONST.__cfstring: 0x22c0
   __AUTH_CONST.__objc_const: 0x2b40
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x180

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1762
-  Symbols:   3436
-  CStrings:  753
+  Symbols:   3438
+  CStrings:  754
 
Symbols:
+ _AVAudioSessionInterruptionEndLikelyToBeResumableKey
+ _kAudioSessionNotification_InterruptionInfoKey_EndInterruptionLikelyToBeResumable
+ _os_unfair_recursive_lock_lock
- _os_unfair_recursive_lock_lock_with_options
Functions:
~ __ZN4avas6client10KVOManager22markPropertiesDirtyAllEv : 128 -> 124
~ __ZN4avas6client21SessionCoreLegacy_iOS26initializeDeviceTimeClientEPU24objcproto13OS_xpc_object8NSObjectj : 240 -> 236
~ __ZN4avas6client10KVOManager19markPropertiesDirtyEm : 136 -> 132
~ __ZN4avas6client21SessionCoreLegacy_iOS17inputTimeObserverEv : 200 -> 196
~ __ZN4avas6client11KVOPropertyIdE13UpdateIfDirtyERKNSt3__18functionIFdvEEE : 152 -> 148
~ __ZN4avas6client11KVOPropertyIfE15UpdateAndNotifyERKfb : 176 -> 172
~ __ZN4avas6client11KVOPropertyIjE15UpdateAndNotifyERKjb : 176 -> 172
~ __ZN4avas6client11SessionCore27resetSessionCreationHandlerEv : 68 -> 64
~ __ZN4avas6client11SessionCore29resetCachedPreferredInputPortEv : 64 -> 60
~ __ZN4avas6client11KVOPropertyIU8__strongP7NSArrayE15UpdateAndNotifyERU8__strongKS3_b : 176 -> 172
~ __ZN4avas6client11KVOPropertyIdE15UpdateAndNotifyERKdb : 176 -> 172
~ __ZN4avas6client11KVOPropertyIjE13UpdateIfDirtyERKNSt3__18functionIFjvEEE : 144 -> 140
~ __ZN4avas6client21SessionCoreLegacy_iOS18preferredInputPortEv : 628 -> 624
~ __ZN4avas6client21SessionCoreLegacy_iOS21setPreferredInputPortEP29AVAudioSessionPortDescription : 884 -> 880
~ __ZN4avas6client21SessionCoreLegacy_iOS18outputTimeObserverEv : 200 -> 196
~ __ZN4avas6client21SessionCoreLegacy_iOS12ioControllerEv : 440 -> 436
~ __ZN4avas6client21SessionCoreLegacy_iOS21decoupledIOControllerEv : 304 -> 300
~ __ZN4avas6client11KVOPropertyIfE13UpdateIfDirtyERKNSt3__18functionIFfvEEE : 152 -> 148
~ __ZN4avas6client11KVOPropertyIU8__strongP7NSArrayE13UpdateIfDirtyERKNSt3__18functionIFS3_vEEE : 152 -> 148
~ __ZN4avas6client11KVOPropertyIU8__strongP35AVAudioSessionDataSourceDescriptionE13UpdateIfDirtyERKNSt3__18functionIFS3_vEEE : 152 -> 148
~ __ZN4avas6client11KVOPropertyIU8__strongP35AVAudioSessionDataSourceDescriptionE15UpdateAndNotifyERU8__strongKS3_b : 176 -> 172
~ __ZN4avas6client11SessionCore25setSessionCreationHandlerENSt3__110shared_ptrINS2_8functionIFvvEEEEE : 96 -> 92
~ __ZNK4avas6client11SessionCore18HandleInterruptionEP12NSDictionary : 1880 -> 1964
~ __ZNSt3__111unique_lockIN5caulk4mach21unfair_recursive_lockEE4lockB9fqe220106Ev : 100 -> 96
CStrings:
+ "AVAudioSessionInterruptionEndLikelyToBeResumableKey"
```
