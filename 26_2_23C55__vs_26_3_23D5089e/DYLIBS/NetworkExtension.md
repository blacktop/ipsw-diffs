## NetworkExtension

> `/System/Library/Frameworks/NetworkExtension.framework/NetworkExtension`

```diff

-2205.62.1.0.0
-  __TEXT.__text: 0x1fb560
-  __TEXT.__auth_stubs: 0x4400
+2205.80.6.0.0
+  __TEXT.__text: 0x1fb94c
+  __TEXT.__auth_stubs: 0x4530
   __TEXT.__objc_methlist: 0xee98
   __TEXT.__const: 0x33cc
-  __TEXT.__cstring: 0x199f9
+  __TEXT.__cstring: 0x19a19
   __TEXT.__constg_swiftt: 0xc1c
   __TEXT.__swift5_typeref: 0xdd3
   __TEXT.__swift5_reflstr: 0x465

   __TEXT.__swift_as_ret: 0x104
   __TEXT.__swift5_protos: 0x14
   __TEXT.__gcc_except_tab: 0x5a14
-  __TEXT.__unwind_info: 0x5428
+  __TEXT.__unwind_info: 0x5430
   __TEXT.__eh_frame: 0x2818
   __TEXT.__objc_classname: 0x24bf
   __TEXT.__objc_methname: 0x1abd2

   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x708
   __DATA_CONST.__objc_arraydata: 0x138
-  __AUTH_CONST.__auth_got: 0x2210
+  __AUTH_CONST.__auth_got: 0x22a8
   __AUTH_CONST.__const: 0x3ea8
   __AUTH_CONST.__cfstring: 0x17f20
   __AUTH_CONST.__objc_const: 0x22918

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E28E7CA1-F72F-3832-8696-4222C617F565
+  UUID: EBE96F93-D23A-36A1-91DA-7CB7C2812C7F
   Functions: 7881
-  Symbols:   22793
+  Symbols:   22812
   CStrings:  15836
 
Symbols:
+ _nw_protocol_add_input_handler
+ _nw_protocol_connected
+ _nw_protocol_disconnected
+ _nw_protocol_error
+ _nw_protocol_finalize_output_frames
+ _nw_protocol_get_flow_id
+ _nw_protocol_get_input_frames
+ _nw_protocol_get_input_handler
+ _nw_protocol_get_output_frames
+ _nw_protocol_get_output_handler
+ _nw_protocol_input_available
+ _nw_protocol_input_finished
+ _nw_protocol_input_finished_is_valid
+ _nw_protocol_output_available
+ _nw_protocol_remove_input_handler
+ _nw_protocol_set_flow_id_from_protocol
+ _nw_protocol_set_input_handler
+ _nw_protocol_set_output_handler
+ _nw_protocol_supports_external_data
Functions:
~ -[NEIKEv2Packet parsePacketData:firstPayloadType:ikeSA:] : 3444 -> 3516
~ ___ne_loopback_disconnect_block_invoke : 40 -> 120
~ ___ne_loopback_connect_block_invoke : 40 -> 120
~ _ne_loopback_error : 28 -> 108
~ _ne_loopback_connected : 40 -> 88
~ _ne_loopback_output_finished : 280 -> 300
~ ___42-[NELoopbackConnection notifyInputHandler]_block_invoke : 40 -> 100
~ _ne_loopback_supports_external_data : 16 -> 40
~ _ne_loopback_remove_input_handler : 120 -> 148
~ _ne_loopback_add_input_handler : 52 -> 108
~ -[NEInternetNexus setDefaultInputHandler:] : 612 -> 596
~ -[NEIPsecNexus setDefaultInputHandler:] : 376 -> 368
~ -[NENexusFlow setupFlowProtocolWithUUID:] : 280 -> 292
~ ___41-[NENexus closeFlowWithClientIdentifier:]_block_invoke : 112 -> 104
~ ___40-[NENexus handleRequestNexusFromClient:]_block_invoke.200 : 220 -> 212
~ ___40-[NENexus handleRequestNexusFromClient:]_block_invoke.201 : 220 -> 212
~ _nw_nexus_flow_finalize_output_frames : 24 -> 72
~ _nw_nexus_flow_get_output_frames : 28 -> 128
~ _nw_nexus_flow_get_input_frames : 28 -> 128
~ _nw_nexus_flow_output_available : 28 -> 72
~ _nw_nexus_flow_input_available : 28 -> 72
~ _nw_nexus_flow_add_input_handler : 28 -> 88
~ _nw_utun_protocol_finalize_output_frames : 152 -> 148
~ _nw_utun_protocol_get_output_frames : 168 -> 196
~ _nw_utun_protocol_get_input_frames : 168 -> 196
~ _nw_utun_protocol_remove_input_handler : 116 -> 144
~ _nw_utun_protocol_add_input_handler : 52 -> 68
CStrings:
+ "@56@0:8@16@24@32@40^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}48"
- "@56@0:8@16@24@32@40^{__SecKey=}48"

```
