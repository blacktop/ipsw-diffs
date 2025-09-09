## BasebandTraceHelper

> `/System/Library/PrivateFrameworks/BasebandTraceHelper.framework/BasebandTraceHelper`

```diff

 1391.0.0.0.0
-  __TEXT.__text: 0x4c170
-  __TEXT.__auth_stubs: 0x1280
+  __TEXT.__text: 0x4c634
+  __TEXT.__auth_stubs: 0x1290
   __TEXT.__init_offsets: 0x3c
-  __TEXT.__const: 0x2908
-  __TEXT.__gcc_except_tab: 0x3d3c
+  __TEXT.__const: 0x2948
+  __TEXT.__gcc_except_tab: 0x3d40
   __TEXT.__cstring: 0x13ca
   __TEXT.__oslogstring: 0x2de9
   __TEXT.__unwind_info: 0x1788

   __DATA_CONST.__const: 0xae0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x88
-  __AUTH_CONST.__auth_got: 0x958
+  __AUTH_CONST.__auth_got: 0x960
   __AUTH_CONST.__const: 0x2018
   __AUTH_CONST.__cfstring: 0x20
   __DATA.__data: 0x3d8

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2C114CAD-8408-32EA-803A-9964118975E1
+  UUID: 61AF8A3D-1D15-359B-B6FD-8962496956AB
   Functions: 1071
-  Symbols:   3088
+  Symbols:   3089
   CStrings:  591
 
Symbols:
+ __ZN12capabilities5radio3dalEv
+ ___block_descriptor_tmp.100
+ ___block_descriptor_tmp.109
- ___block_descriptor_tmp.108
- ___block_descriptor_tmp.98
Functions:
~ sub_23f301710 -> sub_23fb61710 : 76 -> 100
~ __ZN17BasebandTransport21getSupportedProtocolsEv : 1516 -> 1904
~ __ZN17BasebandTransport29getDefaultTransportIOReadSizeENS_8ProtocolE : 64 -> 208
~ __ZN17BasebandTransport30getDefaultTransportIOReadCountENS_8ProtocolE : 112 -> 244
~ __ZN17BasebandTransportC2EN8dispatch5queueE11qos_class_t : 808 -> 836
~ __ZN17BasebandTransport6createEN8dispatch5queueE11qos_class_t : 1128 -> 1120
~ __ZN17BasebandTransport12openPCI_syncEv : 1840 -> 2144
~ __ZN17BasebandTransport16startReader_syncEv : 256 -> 360
~ __ZN17BasebandTransport9read_syncEN8dispatch13group_sessionE : 800 -> 896
~ __ZN19TraceFileCollection19finishSnapshot_syncERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_S8_NS0_10shared_ptrIN3abm5trace9TraceInfoEEE : 5692 -> 5700

```
