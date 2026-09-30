## NetworkExtension

> `/System/Library/Frameworks/NetworkExtension.framework/NetworkExtension`

```diff

-2063.42.1.0.0
-  __TEXT.__text: 0x1bfe50
+2063.42.2.0.0
+  __TEXT.__text: 0x1bff10
   __TEXT.__auth_stubs: 0x3c70
   __TEXT.__objc_methlist: 0xd4fc
-  __TEXT.__cstring: 0x17173
+  __TEXT.__cstring: 0x17171
   __TEXT.__swift5_typeref: 0x332
   __TEXT.__const: 0x2400
   __TEXT.__constg_swiftt: 0x540

   __TEXT.__swift5_capture: 0x140
   __TEXT.__swift5_protos: 0x4
   __TEXT.__gcc_except_tab: 0x5264
-  __TEXT.__oslogstring: 0x1f6b7
-  __TEXT.__unwind_info: 0x4508
+  __TEXT.__oslogstring: 0x1f6dc
+  __TEXT.__unwind_info: 0x4500
   __TEXT.__eh_frame: 0x598
   __TEXT.__objc_classname: 0x23ba
   __TEXT.__objc_methname: 0x18f97

   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 6587
   Symbols:   8617
-  CStrings:  11966
+  CStrings:  11968
 
CStrings:
+ "-[NEIKEv2IKEAuthPacket(Exchange) validateAuthPart1AsInitiator:beforeEAP:]"
+ "-[NEIKEv2IKEAuthPacket(Exchange) validateAuthPart2AsInitiator:childSA:]"
+ "Initial AUTH validation failed"
+ "Peer EAP MAC is valid"
+ "Peer GSPM MAC is valid"
+ "Peer PSK MAC is valid"
- "%!s(MISSING) called with null publicKey"
- "-[NEIKEv2IKEAuthPacket(Exchange) validateAuthAsInitiator:childSA:]"
- "-[NEIKEv2IKEAuthPacket(Exchange) validateFirstAuthPayloadsForInitiator:]"
- "Initial AUTH payload validation failed"

```
