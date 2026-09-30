## PairedUnlock

> `/System/Library/PrivateFrameworks/PairedUnlock.framework/PairedUnlock`

```diff

-184.0.8.0.0
-  __TEXT.__text: 0x2c38
-  __TEXT.__auth_stubs: 0x2f0
+184.4.1.0.0
+  __TEXT.__text: 0x2d6c
+  __TEXT.__auth_stubs: 0x280
   __TEXT.__objc_methlist: 0x624
   __TEXT.__cstring: 0x39b
   __TEXT.__const: 0x10
-  __TEXT.__gcc_except_tab: 0x148
+  __TEXT.__gcc_except_tab: 0x14c
   __TEXT.__oslogstring: 0x36
-  __TEXT.__unwind_info: 0x1c8
+  __TEXT.__unwind_info: 0x1d0
   __TEXT.__objc_classname: 0xa1
   __TEXT.__objc_methname: 0xe09
   __TEXT.__objc_methtype: 0x306

   __DATA_CONST.__objc_selrefs: 0x3e8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x188
+  __AUTH_CONST.__auth_got: 0x150
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x420
   __AUTH_CONST.__objc_const: 0x8f0

   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 22F51EEE-1350-3E5F-90AD-3E09137A9CDA
+  UUID: 1B9826D8-A93C-39CF-880F-2446448EE092
   Functions: 105
-  Symbols:   487
+  Symbols:   480
   CStrings:  294
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x21
- _objc_retain_x22
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
Functions:
~ +[PUError errorWithCode:description:] : 220 -> 228
~ -[PURemoteDeviceState isEqual:] : 712 -> 700
~ -[PURemoteDeviceState hash] : 220 -> 224
~ -[PURemoteDeviceState description] : 264 -> 272
~ -[PURemoteDeviceState initWithCoder:] : 224 -> 228
~ -[PURemoteDeviceState encodeWithCoder:] : 188 -> 196
~ -[PURemoteDeviceState setPasscodePolicy:] : 12 -> 64
~ -[PURemotePasscodePolicy description] : 168 -> 176
~ -[PURemotePasscodePolicy encodeWithCoder:] : 108 -> 116
~ _pu_log : 68 -> 84
~ -[PUConnection queueNameWithSuffix:] : 144 -> 152
~ +[PUConnection serverInterface] : 68 -> 84
~ ___31+[PUConnection serverInterface]_block_invoke : 212 -> 216
~ +[PUConnection clientInterface] : 68 -> 84
~ ___31+[PUConnection clientInterface]_block_invoke : 240 -> 244
~ -[PUConnection serverConnection] : 132 -> 152
~ ___32-[PUConnection serverConnection]_block_invoke : 532 -> 544
~ -[PUConnection setServerConnection:] : 152 -> 160
~ ___36-[PUConnection setServerConnection:]_block_invoke : 12 -> 60
~ -[PUConnection pairForUnlockWithPasscode:] : 112 -> 120
~ -[PUConnection unpairForUnlock] : 88 -> 96
~ -[PUConnection enableOnlyRemoteUnlockWithPasscode:] : 112 -> 120
~ -[PUConnection disableOnlyRemoteUnlock] : 88 -> 96
~ -[PUConnection requestRemoteDeviceRemoteAction:type:] : 112 -> 120
~ -[PUConnection requestRemoteDeviceUnlockNotification] : 88 -> 96
~ -[PUConnection requestRemoteDeviceRemoveLockout:] : 204 -> 200
~ ___49-[PUConnection requestRemoteDeviceRemoveLockout:]_block_invoke : 180 -> 188
~ -[PUConnection requestDeviceSetWristDetectionDisabled:completion:] : 372 -> 376
~ ___66-[PUConnection requestDeviceSetWristDetectionDisabled:completion:]_block_invoke : 148 -> 156
~ ___37-[PUConnection getRemoteDeviceState:]_block_invoke : 192 -> 196
~ -[PUConnection queryRemoteDeviceState:] : 112 -> 120
~ -[PUConnection delegateIfRespondsToSelector:] : 84 -> 88
~ -[PUConnection didPairForUnlock:error:] : 220 -> 216
~ ___39-[PUConnection didPairForUnlock:error:]_block_invoke : 148 -> 152
~ -[PUConnection didUnpairForUnlock:error:] : 220 -> 216
~ ___41-[PUConnection didUnpairForUnlock:error:]_block_invoke : 148 -> 152
~ -[PUConnection didEnableOnlyRemoteUnlock:error:] : 220 -> 216
~ ___48-[PUConnection didEnableOnlyRemoteUnlock:error:]_block_invoke : 148 -> 152
~ -[PUConnection didDisableOnlyRemoteUnlock:error:] : 220 -> 216
~ ___49-[PUConnection didDisableOnlyRemoteUnlock:error:]_block_invoke : 148 -> 152
~ -[PUConnection remoteDeviceDidCompleteRemoteAction:remoteDeviceState:error:] : 256 -> 244
~ ___76-[PUConnection remoteDeviceDidCompleteRemoteAction:remoteDeviceState:error:]_block_invoke : 152 -> 156
~ ___37-[PUConnection remoteDeviceDidUnlock]_block_invoke : 144 -> 148
~ -[PUConnection didGetRemoteDeviceState:error:] : 248 -> 236
~ ___46-[PUConnection didGetRemoteDeviceState:error:]_block_invoke : 152 -> 156
~ -[PUConnection remoteDeviceDidRemoveLockout:error:] : 212 -> 208
~ ___51-[PUConnection remoteDeviceDidRemoveLockout:error:]_block_invoke : 200 -> 208
~ -[PUConnectionUnlockClient initWithConnection:] : 120 -> 124
~ -[PUConnectionUnlockClient remoteDeviceDidCompleteRemoteAction:remoteDeviceState:error:] : 128 -> 124
~ -[PUConnectionUnlockClient didGetRemoteDeviceState:error:] : 120 -> 116

```
