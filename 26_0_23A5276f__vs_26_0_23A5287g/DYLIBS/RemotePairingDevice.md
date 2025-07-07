## RemotePairingDevice

> `/System/Library/PrivateFrameworks/RemotePairingDevice.framework/RemotePairingDevice`

```diff

-234.0.0.0.0
-  __TEXT.__text: 0xce8b8
-  __TEXT.__auth_stubs: 0x2bb0
+236.0.0.0.0
+  __TEXT.__text: 0xd0cc4
+  __TEXT.__auth_stubs: 0x2bc0
   __TEXT.__objc_methlist: 0x4bc
-  __TEXT.__const: 0xf188
-  __TEXT.__cstring: 0x6dec
-  __TEXT.__oslogstring: 0x3f4c
+  __TEXT.__const: 0xf218
+  __TEXT.__cstring: 0x6e5c
+  __TEXT.__oslogstring: 0x3f3c
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__constg_swiftt: 0x3c1c
-  __TEXT.__swift5_typeref: 0x3a4c
-  __TEXT.__swift5_reflstr: 0x2ba0
-  __TEXT.__swift5_fieldmd: 0x35bc
+  __TEXT.__constg_swiftt: 0x3c48
+  __TEXT.__swift5_typeref: 0x3b32
+  __TEXT.__swift5_reflstr: 0x2bd0
+  __TEXT.__swift5_fieldmd: 0x35c8
   __TEXT.__swift5_builtin: 0x208
   __TEXT.__swift5_assocty: 0x2d0
-  __TEXT.__swift5_proto: 0xb38
+  __TEXT.__swift5_proto: 0xb40
   __TEXT.__swift5_types: 0x418
   __TEXT.__swift5_capture: 0x1e4c
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_mpenum: 0x178
-  __TEXT.__unwind_info: 0x3c30
+  __TEXT.__unwind_info: 0x3d38
   __TEXT.__eh_frame: 0x3618
   __TEXT.__objc_classname: 0x13c
   __TEXT.__objc_methname: 0xbb4
   __TEXT.__objc_methtype: 0x127
   __TEXT.__objc_stubs: 0x2c0
-  __DATA_CONST.__got: 0x708
+  __DATA_CONST.__got: 0x718
   __DATA_CONST.__const: 0x820
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x120

   __DATA_CONST.__objc_selrefs: 0x460
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x15e8
+  __AUTH_CONST.__auth_got: 0x15f0
   __AUTH_CONST.__const: 0xba10
   __AUTH_CONST.__cfstring: 0x1a0
-  __AUTH_CONST.__objc_const: 0x4760
-  __AUTH.__objc_data: 0x590
-  __AUTH.__data: 0x17d8
+  __AUTH_CONST.__objc_const: 0x4738
+  __AUTH.__objc_data: 0x5e0
+  __AUTH.__data: 0x1808
   __DATA.__objc_ivar: 0x4
-  __DATA.__data: 0x2278
-  __DATA.__bss: 0xcf10
-  __DATA.__common: 0x40
+  __DATA.__data: 0x22c8
+  __DATA.__bss: 0xd010
+  __DATA.__common: 0x50
   __DATA_DIRTY.__objc_data: 0x290
   __DATA_DIRTY.__data: 0x2578
   __DATA_DIRTY.__bss: 0x8500

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FA0C7628-9CC1-36B4-A676-803BE6805AD8
-  Functions: 7752
-  Symbols:   5295
-  CStrings:  1108
+  UUID: EE24B5C3-1E94-34A5-AC6E-DF465D80FBFC
+  Functions: 7796
+  Symbols:   5341
+  CStrings:  1113
 
Symbols:
+ _symbolic SDy__________6advert_So12CUPairedPeerCSg15resolvedPairingtG 7Network10NWEndpointO 19RemotePairingDevice23DiscoveredBonjourAdvertV
+ _symbolic _____6advert_So12CUPairedPeerCSg15resolvedPairingt 19RemotePairingDevice23DiscoveredBonjourAdvertV
+ _symbolic _____6advert_So12CUPairedPeerCSg15resolvedPairingtSg 19RemotePairingDevice23DiscoveredBonjourAdvertV
+ _symbolic _____y__________6advert_So12CUPairedPeerCSg15resolvedPairingtG s17_NativeDictionaryV 7Network10NWEndpointO 19RemotePairingDevice23DiscoveredBonjourAdvertV
- _OUTLINED_FUNCTION_301
- _OUTLINED_FUNCTION_302
CStrings:
+ "%{public}s: bonjour endpoint updated: %s"
+ ", prohibitedInterface"
+ ", validInterfaces="
+ "Discovered bonjour advert for device %s/%s was updated"
+ "Discovered bonjour advert for device %s/%s went from valid -> invalid. Reporting as loss."
+ "bonjourEndpoint"
+ "discoveredAdverts"
- "Received bonjour notification to add result %s, but result is not present in full results set. Ignoring"
- "Received bonjour notification to remove result %s, but result is still present in full results set. Ignoring"

```
