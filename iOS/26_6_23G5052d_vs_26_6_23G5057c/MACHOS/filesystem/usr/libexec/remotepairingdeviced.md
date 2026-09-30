## remotepairingdeviced

> `/usr/libexec/remotepairingdeviced`

```diff

-  __TEXT.__text: 0x66d54
-  __TEXT.__auth_stubs: 0x3230
+  __TEXT.__text: 0x66a64
+  __TEXT.__auth_stubs: 0x32b0
   __TEXT.__objc_stubs: 0x800
   __TEXT.__objc_methlist: 0x1ac
   __TEXT.__const: 0x2230
-  __TEXT.__oslogstring: 0x349f
-  __TEXT.__cstring: 0x43cc
+  __TEXT.__oslogstring: 0x344f
+  __TEXT.__cstring: 0x43fc
   __TEXT.__gcc_except_tab: 0x4c
   __TEXT.__objc_methname: 0x14d5
   __TEXT.__objc_classname: 0x6d2

   __TEXT.__swift5_mpenum: 0x20
   __TEXT.__unwind_info: 0x1188
   __TEXT.__eh_frame: 0x1160
-  __DATA_CONST.__auth_got: 0x1928
+  __DATA_CONST.__auth_got: 0x1968
   __DATA_CONST.__got: 0x990
   __DATA_CONST.__auth_ptr: 0x678
   __DATA_CONST.__const: 0x3488

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2293
-  Symbols:   1256
+  Functions: 2288
+  Symbols:   1264
   CStrings:  793
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__swift5_entry : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _$s19RemotePairingDevice8DefaultsV19tunnelKeepaliveIdleSivgZ
+ _$s19RemotePairingDevice8DefaultsV20makeViabilityHandler10identifier3log5queue12cancelActionySbcSS_So06OS_os_I0CSo0m10_dispatch_J0CyyctFZ
+ _$s19RemotePairingDevice8DefaultsV20tunnelKeepaliveCountSivgZ
+ _$s19RemotePairingDevice8DefaultsV22p2pTunnelKeepaliveIdleSivgZ
+ _$s19RemotePairingDevice8DefaultsV23p2pTunnelKeepaliveCountSivgZ
+ _$s19RemotePairingDevice8DefaultsV23tunnelKeepaliveIntervalSivgZ
+ _$s19RemotePairingDevice8DefaultsV25deviceTunnelKeepWiFiAliveSbvgZ
+ _$s19RemotePairingDevice8DefaultsV26p2pTunnelKeepaliveIntervalSivgZ
CStrings:
+ "remotepairingdeviced Tunnel connection"
- "%{public}s: Cancelling tunnel connection as it is no longer viable"

```
