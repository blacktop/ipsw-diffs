## RemotePairingDevice

> `/System/Library/PrivateFrameworks/RemotePairingDevice.framework/Versions/A/RemotePairingDevice`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__bss`
- `__DATA.__common`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`
- `__DATA_DIRTY.__bss`

```diff

-244.120.2.0.0
-  __TEXT.__text: 0xc9b6c
+244.160.2.0.0
+  __TEXT.__text: 0xcb3b4
   __TEXT.__auth_stubs: 0x2950
   __TEXT.__objc_methlist: 0x4a4
-  __TEXT.__const: 0xfce0
-  __TEXT.__cstring: 0x53ac
-  __TEXT.__oslogstring: 0x3f0c
-  __TEXT.__constg_swiftt: 0x3bd0
-  __TEXT.__swift5_typeref: 0x3ada
-  __TEXT.__swift5_reflstr: 0x2b90
-  __TEXT.__swift5_fieldmd: 0x3584
+  __TEXT.__const: 0xfd30
+  __TEXT.__cstring: 0x54ec
+  __TEXT.__oslogstring: 0x3ffc
+  __TEXT.__constg_swiftt: 0x3bec
+  __TEXT.__swift5_typeref: 0x3b08
+  __TEXT.__swift5_reflstr: 0x2bb0
+  __TEXT.__swift5_fieldmd: 0x35b8
   __TEXT.__swift5_builtin: 0x1f4
   __TEXT.__swift5_assocty: 0x2b8
-  __TEXT.__swift5_proto: 0xb20
-  __TEXT.__swift5_types: 0x40c
-  __TEXT.__swift5_capture: 0x1934
+  __TEXT.__swift5_proto: 0xb24
+  __TEXT.__swift5_types: 0x410
+  __TEXT.__swift5_capture: 0x1a10
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_mpenum: 0x178
-  __TEXT.__unwind_info: 0x3e60
-  __TEXT.__eh_frame: 0x3560
+  __TEXT.__unwind_info: 0x3f30
+  __TEXT.__eh_frame: 0x3580
   __TEXT.__objc_classname: 0x7a6
   __TEXT.__objc_methname: 0x1c01
   __TEXT.__objc_methtype: 0x45a
   __TEXT.__objc_stubs: 0xb80
   __DATA_CONST.__got: 0x710
-  __DATA_CONST.__const: 0x810
+  __DATA_CONST.__const: 0x8b0
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__auth_got: 0x14b0
-  __AUTH_CONST.__const: 0xb480
+  __AUTH_CONST.__const: 0xb690
   __AUTH_CONST.__cfstring: 0x1a0
   __AUTH_CONST.__objc_const: 0x46a8
   __AUTH.__objc_data: 0x5e0
   __AUTH.__data: 0x1778
   __DATA.__objc_ivar: 0x4
-  __DATA.__data: 0x2420
+  __DATA.__data: 0x2570
   __DATA.__bss: 0xce90
   __DATA.__common: 0x54
   __DATA_DIRTY.__objc_data: 0x290

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7846
-  Symbols:   2381
-  CStrings:  1059
+  Functions: 7941
+  Symbols:   2386
+  CStrings:  1072
 
Symbols:
+ _symbolic So9OS_os_logC
+ _symbolic _____ 19RemotePairingDevice8DefaultsV25NonViableConnectionPolicyO
+ _symbolic _____Sgz_Xx 8Dispatch0A8WorkItemC
+ _symbolic _____y_____G 19RemotePairingDevice22DefaultsBackedPropertyV AA0D0V25NonViableConnectionPolicyO
+ objectdestroy.26Tm
+ objectdestroy.89Tm
- objectdestroy.83Tm
CStrings:
+ "%{public}s: Cancelling connection after non-viable timeout"
+ "%{public}s: Cancelling connection as it is no longer viable"
+ "%{public}s: Connection is no longer viable but non-viable cancellation is disabled"
+ "%{public}s: Connection is no longer viable, will cancel in %fs if viability is not restored"
+ "%{public}s: Connection viability restored, cancelled pending non-viable timeout"
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
```
