## SidecarRelay

> `/usr/libexec/SidecarRelay`

```diff

-313.0.0.0.0
-  __TEXT.__text: 0x760c8
+315.4.0.0.0
+  __TEXT.__text: 0x7697c
   __TEXT.__auth_stubs: 0x1af0
   __TEXT.__objc_stubs: 0x420
-  __TEXT.__objc_methlist: 0x68c
-  __TEXT.__cstring: 0x4b8d
+  __TEXT.__objc_methlist: 0x6a4
+  __TEXT.__cstring: 0x4bdd
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x2ffb
-  __TEXT.__constg_swiftt: 0x1c3c
-  __TEXT.__swift5_typeref: 0x1914
+  __TEXT.__const: 0x30d3
+  __TEXT.__constg_swiftt: 0x1d1c
+  __TEXT.__swift5_typeref: 0x1972
   __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_reflstr: 0xb9a
-  __TEXT.__swift5_fieldmd: 0x1194
+  __TEXT.__swift5_reflstr: 0xbaa
+  __TEXT.__swift5_fieldmd: 0x11d0
   __TEXT.__swift5_assocty: 0x230
-  __TEXT.__swift5_proto: 0x264
-  __TEXT.__swift5_types: 0x150
+  __TEXT.__swift5_proto: 0x26c
+  __TEXT.__swift5_types: 0x158
   __TEXT.__objc_classname: 0x146
-  __TEXT.__objc_methname: 0x1840
+  __TEXT.__objc_methname: 0x1894
   __TEXT.__objc_methtype: 0x9f1
-  __TEXT.__swift5_capture: 0x8b0
-  __TEXT.__swift5_protos: 0x3c
-  __TEXT.__unwind_info: 0x22d8
-  __TEXT.__eh_frame: 0x12d8
+  __TEXT.__swift5_protos: 0x40
+  __TEXT.__swift5_capture: 0x8fc
+  __TEXT.__unwind_info: 0x22c8
+  __TEXT.__eh_frame: 0x1288
   __DATA_CONST.__auth_got: 0xd80
   __DATA_CONST.__got: 0x3a8
   __DATA_CONST.__auth_ptr: 0xc0
-  __DATA_CONST.__const: 0x4790
+  __DATA_CONST.__const: 0x48b0
   __DATA_CONST.__cfstring: 0x60
-  __DATA_CONST.__objc_classlist: 0x148
+  __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x4800
-  __DATA.__objc_selrefs: 0x730
+  __DATA.__objc_const: 0x49c0
+  __DATA.__objc_selrefs: 0x738
   __DATA.__objc_protorefs: 0x78
   __DATA.__objc_classrefs: 0x178
   __DATA.__objc_superrefs: 0x8
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0x1638
-  __DATA.__data: 0x3350
+  __DATA.__data: 0x3500
   __DATA.__bss: 0x4298
   __DATA.__common: 0x110
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3716
+  Functions: 3739
   Symbols:   733
-  CStrings:  850
+  CStrings:  858
 
CStrings:
+ "315.4"
+ "Activating a [%s] that handles requests to the [%s] service."
+ "Activation requested, but it's already activated."
+ "Received a [%{public}s] request"
+ "Registering CompanionLink request handler for requests with identifier [%s]"
+ "RemoteDisplayReadiness"
+ "Sending a response to a [%{public}s] request"
+ "SidecarRelay/RemoteDisplayInitiationRequestHandler.swift"
+ "SidecarRelay/RemoteDisplayReadinessRequestHandler.swift"
+ "This platform does not support readiness requests."
+ "This platform does not support starting a display stream remotely."
+ "_TtC12SidecarRelay36RemoteDisplayReadinessRequestHandler"
+ "_TtC12SidecarRelay37RemoteDisplayInitiationRequestHandler"
+ "activated"
+ "deviceToDeviceEncryptionAvailable"
+ "fetchDeviceReadinessStatus(withIDSIdentifier:completion:)"
+ "fetchDeviceReadinessStatusWithIDSIdentifier:completion:"
+ "manateeAvailable"
+ "relayFetchDeviceReadinessStatusWithIDSIdentifier:completion:"
- "313"
- "Activating a [%s] that handles requests to the [%s] service.  It handles requests with IDs of [%s]."
- "Could not convert device with an IDS identifier of [%s].  Will not initiate a Sidecar remote display stream. Given 'request': [%s]"
- "Could not find a device with an IDS identifier of [%s].  Will not initiate a Sidecar remote display stream. Given 'request': [%s]"
- "Either no [%s] parameter was found in request or it was not the correct type.  Will not initiate a Sidecar remote display stream.  Given 'request': [%s]"
- "Received a [%s] request"
- "SidecarRelay/CompanionLinkServer.swift"
- "This platform does not support starting a remote display stream.  Device: [%@]"
- "primaryAppleIDIsHSA2"
- "setOffersAdditionalDisplay:"

```
