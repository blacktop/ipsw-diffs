## Transparency

> `/System/Library/PrivateFrameworks/Transparency.framework/Transparency`

```diff

-1766.40.56.0.0
-  __TEXT.__text: 0x7ce80
-  __TEXT.__objc_methlist: 0x4ad0
-  __TEXT.__cstring: 0x310c
-  __TEXT.__const: 0x4ed0
-  __TEXT.__gcc_except_tab: 0x4ec
-  __TEXT.__oslogstring: 0x20db
+1766.40.58.0.0
+  __TEXT.__text: 0x7d730
+  __TEXT.__objc_methlist: 0x4b70
+  __TEXT.__cstring: 0x313c
+  __TEXT.__const: 0x4ee0
+  __TEXT.__gcc_except_tab: 0x518
+  __TEXT.__oslogstring: 0x229b
   __TEXT.__swift5_typeref: 0x10e4
   __TEXT.__swift5_reflstr: 0x9ca
   __TEXT.__swift5_assocty: 0x260

   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_acfuncs: 0x1b8
   __TEXT.__swift5_capture: 0x2c4
-  __TEXT.__unwind_info: 0x33d0
+  __TEXT.__unwind_info: 0x3408
   __TEXT.__eh_frame: 0x3840
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1640
+  __DATA_CONST.__const: 0x1690
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2058
+  __DATA_CONST.__objc_selrefs: 0x20b8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x180
-  __DATA_CONST.__got: 0x660
-  __AUTH_CONST.__const: 0x4018
-  __AUTH_CONST.__cfstring: 0x3aa0
-  __AUTH_CONST.__objc_const: 0x8050
+  __DATA_CONST.__got: 0x668
+  __AUTH_CONST.__const: 0x4118
+  __AUTH_CONST.__cfstring: 0x3ac0
+  __AUTH_CONST.__objc_const: 0x8140
   __AUTH_CONST.__objc_intobj: 0x1e0
-  __AUTH_CONST.__auth_got: 0xca0
+  __AUTH_CONST.__auth_got: 0xcb8
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x3b4
+  __DATA.__objc_ivar: 0x3c8
   __DATA.__data: 0x9f0
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1dd0
   __DATA_DIRTY.__data: 0xe58
-  __DATA_DIRTY.__bss: 0x910
+  __DATA_DIRTY.__bss: 0x920
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3893
-  Symbols:   3585
-  CStrings:  785
+  Functions: 3922
+  Symbols:   3612
+  CStrings:  794
 
Symbols:
+ +[TransparencyXPCConnection nowNs]
+ -[TransparencyXPCConnection dropConnectionForGeneration:]
+ -[TransparencyXPCConnection firstSuppressedNs]
+ -[TransparencyXPCConnection flushSuppressedPeerExits:]
+ -[TransparencyXPCConnection generation]
+ -[TransparencyXPCConnection lastPeerExitLogNs]
+ -[TransparencyXPCConnection lastSuppressedNs]
+ -[TransparencyXPCConnection logPeerExit:]
+ -[TransparencyXPCConnection setFirstSuppressedNs:]
+ -[TransparencyXPCConnection setGeneration:]
+ -[TransparencyXPCConnection setLastPeerExitLogNs:]
+ -[TransparencyXPCConnection setLastSuppressedNs:]
+ -[TransparencyXPCConnection setSuppressedPeerExits:]
+ -[TransparencyXPCConnection suppressedPeerExits]
+ GCC_except_table11
+ GCC_except_table23
+ GCC_except_table32
+ GCC_except_table7
+ _NSDebugDescriptionErrorKey
+ _OBJC_IVAR_$_TransparencyXPCConnection._firstSuppressedNs
+ _OBJC_IVAR_$_TransparencyXPCConnection._generation
+ _OBJC_IVAR_$_TransparencyXPCConnection._lastPeerExitLogNs
+ _OBJC_IVAR_$_TransparencyXPCConnection._lastSuppressedNs
+ _OBJC_IVAR_$_TransparencyXPCConnection._suppressedPeerExits
+ ___41-[TransparencyXPCConnection logPeerExit:]_block_invoke
+ ___51-[SoftwareTransparency sysdiagnoseInfo:completion:]_block_invoke_2
+ ___54-[TransparencyXPCConnection flushSuppressedPeerExits:]_block_invoke
+ ___88-[SoftwareTransparency verifyExpiringProofs:forDigest:configuration:counter:completion:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32s40w_e5_v8?0lw40l8s32l8
+ _clock_gettime_nsec_np
+ _dispatch_after
+ _dispatch_time
- -[SoftwareTransparency verifyExpiringProofs:for:counter:completion:]
- GCC_except_table16
- GCC_except_table25
- GCC_except_table3
- GCC_except_table6
- ___68-[SoftwareTransparency verifyExpiringProofs:for:counter:completion:]_block_invoke
CStrings:
+ "swtransparencyd did not answer after %d attempts"
+ "sysdiagnoseInfo attempt %d hit %{public}@ %ld, retrying"
+ "sysdiagnoseInfo failed on attempt %d: %{public}@"
+ "sysdiagnoseInfo giving up after %d attempts"
+ "verifyExpiringProofs attempt %d hit %{public}@ %ld, retrying"
+ "verifyExpiringProofs failed on attempt %d: %{public}@"
+ "verifyExpiringProofs giving up after %d attempts"
+ "xpc connection invalidated, it will not reconnect: %{public}@"
+ "xpc peer exited, next call reopens: %{public}@"
+ "xpc peer exited: %{public}@ (%lu more suppressed at once)"
+ "xpc peer exited: %{public}@ (%lu more suppressed over %llums)"
- "server connection exited or crashed: %@"
- "xpc connection cannot be formed or has been terminated: %@"
```
