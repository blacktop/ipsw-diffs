## RemotePairingDevice

> `/System/Library/PrivateFrameworks/RemotePairingDevice.framework/RemotePairingDevice`

```diff

-  __TEXT.__text: 0xcbb80
+  __TEXT.__text: 0xcd390
   __TEXT.__auth_stubs: 0x2b70
   __TEXT.__objc_methlist: 0x4bc
-  __TEXT.__const: 0xfee0
-  __TEXT.__cstring: 0x565c
-  __TEXT.__oslogstring: 0x403c
+  __TEXT.__const: 0xff30
+  __TEXT.__cstring: 0x579c
+  __TEXT.__oslogstring: 0x412c
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__constg_swiftt: 0x3c58
-  __TEXT.__swift5_typeref: 0x3b3e
-  __TEXT.__swift5_reflstr: 0x2bd0
-  __TEXT.__swift5_fieldmd: 0x35c8
+  __TEXT.__constg_swiftt: 0x3c74
+  __TEXT.__swift5_typeref: 0x3b6c
+  __TEXT.__swift5_reflstr: 0x2bf0
+  __TEXT.__swift5_fieldmd: 0x35fc
   __TEXT.__swift5_builtin: 0x208
   __TEXT.__swift5_assocty: 0x2d0
-  __TEXT.__swift5_proto: 0xb40
-  __TEXT.__swift5_types: 0x418
-  __TEXT.__swift5_capture: 0x19fc
+  __TEXT.__swift5_proto: 0xb44
+  __TEXT.__swift5_types: 0x41c
+  __TEXT.__swift5_capture: 0x1ad8
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_mpenum: 0x178
-  __TEXT.__unwind_info: 0x3ca8
+  __TEXT.__unwind_info: 0x3d80
   __TEXT.__eh_frame: 0x3650
   __TEXT.__objc_classname: 0x7d6
   __TEXT.__objc_methname: 0x1c91
   __TEXT.__objc_methtype: 0x4aa
   __TEXT.__objc_stubs: 0xc00
   __DATA_CONST.__got: 0x710
-  __DATA_CONST.__const: 0x858
+  __DATA_CONST.__const: 0x8f8
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__auth_got: 0x15c8
-  __AUTH_CONST.__const: 0xb728
+  __AUTH_CONST.__const: 0xb938
   __AUTH_CONST.__cfstring: 0x1a0
   __AUTH_CONST.__objc_const: 0x4738
   __AUTH.__objc_data: 0x5e0
   __AUTH.__data: 0x1818
   __DATA.__objc_ivar: 0x4
-  __DATA.__data: 0x2460
+  __DATA.__data: 0x25b0
   __DATA.__bss: 0xd010
   __DATA.__common: 0x54
   __DATA_DIRTY.__objc_data: 0x290

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7913
-  Symbols:   5966
-  CStrings:  1109
+  Functions: 8007
+  Symbols:   6003
+  CStrings:  1122
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ _objectdestroy.26Tm
+ _objectdestroy.89Tm
+ _symbolic So9OS_os_logC
+ _symbolic _____ 19RemotePairingDevice8DefaultsV25NonViableConnectionPolicyO
+ _symbolic _____Sgz_Xx 8Dispatch0A8WorkItemC
+ _symbolic _____y_____G 19RemotePairingDevice22DefaultsBackedPropertyV AA0D0V25NonViableConnectionPolicyO
- _objectdestroy.83Tm
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
