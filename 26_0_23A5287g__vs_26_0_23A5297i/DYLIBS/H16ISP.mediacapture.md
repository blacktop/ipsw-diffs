## H16ISP.mediacapture

> `/System/Library/MediaCapture/H16ISP.mediacapture`

```diff

-4.18.5.0.0
-  __TEXT.__text: 0x1cefa8
+4.20.4.0.0
+  __TEXT.__text: 0x1cf044
   __TEXT.__auth_stubs: 0x3240
   __TEXT.__init_offsets: 0x18
   __TEXT.__objc_methlist: 0x268
   __TEXT.__const: 0x27dcf
-  __TEXT.__oslogstring: 0x1d521
-  __TEXT.__cstring: 0x193b0
+  __TEXT.__oslogstring: 0x1d52a
+  __TEXT.__cstring: 0x193c1
   __TEXT.__gcc_except_tab: 0x6a80
   __TEXT.__unwind_info: 0x3e08
   __TEXT.__eh_frame: 0xf0

   __DATA_CONST.__objc_arraydata: 0x50
   __AUTH_CONST.__auth_got: 0x1930
   __AUTH_CONST.__const: 0x2980
-  __AUTH_CONST.__cfstring: 0x9ea0
+  __AUTH_CONST.__cfstring: 0x9ec0
   __AUTH_CONST.__objc_const: 0x880
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x34
-  __DATA.__data: 0x362658
+  __DATA.__data: 0x369658
   __DATA.__bss: 0x119
   __DATA.__common: 0x64
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 553DBD37-FCDB-3B9D-9C06-ECAF50D066AF
-  Functions: 5747
-  Symbols:   14682
-  CStrings:  7944
+  UUID: A24B7273-33BC-358C-9790-81F486D14FB9
+  Functions: 5748
+  Symbols:   14683
+  CStrings:  7946
 
Symbols:
+ __ZNK6H16ISP12H16ISPDevice19isExclaveADRequiredEv
Functions:
~ _H16ISPCaptureDeviceCreate : 17344 -> 17328
~ __ZN6H16ISP12H16ISPDeviceC2EPNS_22H16ISPDeviceControllerEj : 1160 -> 1192
~ __ZN6H16ISP16getOutputPresetsEjPj13H16ISPVersionjj : 908 -> 916
~ __ZN6H16ISP40H16ISPGraphExclaveAttentionDetectionNode17AddFaceIDMetadataEPNS_24H16ISPFilterGraphMessageEP28ISPExclaveCoreChRunKitADRsltb : 540 -> 564
~ __ZL19StartExclaveStreamsP19H16ISPCaptureDeviceP19H16ISPCaptureStream : 6448 -> 6528
~ __ZL38MetadataFileWriterThreadMessageHandlerPv : 4816 -> 4820
~ __ZN6H16ISP12H16ISPDevice19LoadFDRDataFileCMPMEv : 3256 -> 3268
+ __ZNK6H16ISP12H16ISPDevice19isExclaveADRequiredEv
CStrings:
+ "%s - AttentionRequired = %{bool}d %{bool}d\n"
+ "RequireExclaveAD"
- "%s - AttentionRequired = %{bool}d\n"

```
