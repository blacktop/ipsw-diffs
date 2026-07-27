## RemotePairing

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/RemotePairing.framework/Versions/A/RemotePairing`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__AUTH.__s_async_hook`
- `__DATA.__objc_protorefs`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-244.120.2.0.0
-  __TEXT.__text: 0xf77a4
+244.160.2.0.0
+  __TEXT.__text: 0xf90cc
   __TEXT.__auth_stubs: 0x2dd0
   __TEXT.__objc_methlist: 0x9a4
-  __TEXT.__const: 0xd194
-  __TEXT.__cstring: 0x623d
-  __TEXT.__oslogstring: 0x492b
-  __TEXT.__swift5_typeref: 0x3e06
-  __TEXT.__swift5_fieldmd: 0x3a18
-  __TEXT.__constg_swiftt: 0x42c8
+  __TEXT.__const: 0xd1b4
+  __TEXT.__cstring: 0x637d
+  __TEXT.__oslogstring: 0x4a1b
+  __TEXT.__swift5_typeref: 0x3e34
+  __TEXT.__swift5_fieldmd: 0x3a4c
+  __TEXT.__constg_swiftt: 0x42e4
   __TEXT.__swift5_builtin: 0x2bc
-  __TEXT.__swift5_reflstr: 0x311d
+  __TEXT.__swift5_reflstr: 0x313d
   __TEXT.__swift5_assocty: 0x480
   __TEXT.__swift5_protos: 0x58
-  __TEXT.__swift5_proto: 0xbe4
-  __TEXT.__swift5_types: 0x44c
-  __TEXT.__swift5_capture: 0x1d04
+  __TEXT.__swift5_proto: 0xbe8
+  __TEXT.__swift5_types: 0x450
+  __TEXT.__swift5_capture: 0x1de0
   __TEXT.__swift5_mpenum: 0x1d0
-  __TEXT.__unwind_info: 0x4ac0
-  __TEXT.__eh_frame: 0x3df8
+  __TEXT.__unwind_info: 0x4ba0
+  __TEXT.__eh_frame: 0x3e30
   __TEXT.__objc_classname: 0x7cc
   __TEXT.__objc_methname: 0x24d0
   __TEXT.__objc_methtype: 0x618
   __TEXT.__objc_stubs: 0x10e0
   __DATA_CONST.__got: 0x600
-  __DATA_CONST.__const: 0x8d0
+  __DATA_CONST.__const: 0x970
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x578
   __AUTH_CONST.__auth_got: 0x16f0
-  __AUTH_CONST.__const: 0xbf10
+  __AUTH_CONST.__const: 0xc120
   __AUTH_CONST.__cfstring: 0x1e0
   __AUTH_CONST.__objc_const: 0x3850
   __AUTH.__objc_data: 0x1040

   __DATA.__objc_classrefs: 0x120
   __DATA.__objc_superrefs: 0x30
   __DATA.__objc_ivar: 0x18
-  __DATA.__data: 0x3989
+  __DATA.__data: 0x3ad9
   __DATA.__swift56_hooks: 0xb0
   __DATA.__bss: 0x16b18
   __DATA.__common: 0xd0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9285
-  Symbols:   2595
-  CStrings:  1271
+  Functions: 9380
+  Symbols:   2600
+  CStrings:  1284
 
Symbols:
+ _symbolic So9OS_os_logC
+ _symbolic _____ 13RemotePairing8DefaultsV25NonViableConnectionPolicyO
+ _symbolic _____Sgz_Xx 8Dispatch0A8WorkItemC
+ _symbolic _____y_____G 13RemotePairing22DefaultsBackedPropertyV AA0C0V25NonViableConnectionPolicyO
+ objectdestroy.26Tm
CStrings:
+ "%{public}s: Cancelling connection after non-viable timeout"
+ "%{public}s: Cancelling connection as it is no longer viable"
+ "%{public}s: Connection is no longer viable but non-viable cancellation is disabled"
+ "%{public}s: Connection is no longer viable, will cancel in %fs if viability is not restored"
+ "%{public}s: Connection viability restored, cancelled pending non-viable timeout"
+ "244.160.2"
+ "controlChannelKeepaliveCount"
+ "controlChannelKeepaliveIdle"
+ "controlChannelKeepaliveInterval"
+ "nonViableConnectionPolicy"
+ "p2pTunnelKeepaliveCount"
+ "p2pTunnelKeepaliveIdle"
+ "p2pTunnelKeepaliveInterval"
+ "tunnelKeepaliveCount"
+ "tunnelKeepaliveIdle"
+ "tunnelKeepaliveInterval"
- "%{public}s/%s: Cancelling tunnel connection as it is no longer viable"
- "%{public}s: Cancelling TCP control channel transport as it is no longer viable"
- "244.120.2"
```
