## STSXPCHelper

> `/System/Library/PrivateFrameworks/STSXPCHelperClient.framework/XPCServices/STSXPCHelper.xpc/STSXPCHelper`

```diff

-4.0.21.0.0
-  __TEXT.__text: 0x36d38
+4.0.22.0.0
+  __TEXT.__text: 0x36ff0
   __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__objc_stubs: 0x4420
-  __TEXT.__objc_methlist: 0x1ec8
-  __TEXT.__objc_methname: 0x5bfb
-  __TEXT.__cstring: 0x8747
-  __TEXT.__objc_classname: 0x7f1
-  __TEXT.__objc_methtype: 0x19ea
+  __TEXT.__objc_stubs: 0x4480
+  __TEXT.__objc_methlist: 0x1ec0
+  __TEXT.__objc_methname: 0x5c2d
+  __TEXT.__cstring: 0x88d1
+  __TEXT.__objc_classname: 0x7e5
+  __TEXT.__objc_methtype: 0x19e3
   __TEXT.__const: 0x140
   __TEXT.__gcc_except_tab: 0x66c
   __TEXT.__dlopen_cstrs: 0xb2
   __TEXT.__oslogstring: 0xac4
-  __TEXT.__unwind_info: 0xb00
+  __TEXT.__unwind_info: 0xb10
   __DATA_CONST.__auth_got: 0x588
   __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0xe68
-  __DATA_CONST.__cfstring: 0x51e0
-  __DATA_CONST.__objc_classlist: 0x1e0
+  __DATA_CONST.__const: 0xe28
+  __DATA_CONST.__cfstring: 0x52a0
+  __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x1a0
+  __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_intobj: 0x1c8
   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x6c48
-  __DATA.__objc_selrefs: 0x15b0
-  __DATA.__objc_ivar: 0x4b0
-  __DATA.__objc_data: 0x12c0
+  __DATA.__objc_const: 0x6b48
+  __DATA.__objc_selrefs: 0x15c8
+  __DATA.__objc_ivar: 0x4a0
+  __DATA.__objc_data: 0x1270
   __DATA.__data: 0xa00
   __DATA.__bss: 0xc0
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 942
+  Functions: 943
   Symbols:   282
-  CStrings:  2477
+  CStrings:  2487
 
CStrings:
+ "-[ISOSessionData statusCode]"
+ "-[STSISO18013Handler _extractDeviceResponseStatus:]"
+ "-[STSXPCHelper _iso18013ReaderProcessResponse:altCarrierStatus:]"
+ "-[STSXPCHelper _iso18013ReaderProcessResponse:altCarrierStatus:]_block_invoke"
+ "-[STSXPClientNotification iso18013ReaderReceived:sessionDataStatus:mDocResponseStatus:error:completion:]_block_invoke"
+ "1.0"
+ "Decode failure"
+ "ISOSessionData.m"
+ "Invalid DeviceResponse status"
+ "Invalid DeviceResponse version"
+ "SessionData decoding failure, error=%!@(MISSING)"
+ "SessionData=%!@(MISSING), sessionDataStatus=%!@(MISSING), deviceResponseStatus=%!@(MISSING)"
+ "T@\"NSNumber\",&,N,V_status"
+ "Unexpected error code detected: %!l(MISSING)u"
+ "Vv48@0:8@\"NSData\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSError\"40"
+ "Vv48@0:8@16@24@32@40"
+ "_status"
+ "false"
+ "initWithInteger:"
+ "iso18013DecryptedDeviceResponse:sessionDataStatus:mDocResponseStatus:error:"
+ "response contains failure status: %!l(MISSING)u"
+ "setStatus:"
+ "v40@?0@\"NSData\"8@\"NSNumber\"16@\"NSNumber\"24@\"NSError\"32"
+ "version"
- "-[STSXPCHelper _iso18013ReaderProcessResponse:status:]"
- "-[STSXPCHelper _iso18013ReaderProcessResponse:status:]_block_invoke"
- "-[STSXPClientNotification iso18013ReaderReceived:sessionDataStatus:status:completion:]_block_invoke"
- "<ISOResponse:%!@(MISSING), "
- "@\"NSMutableDictionary\""
- "ISOResponse"
- "SessionData decoding failured, error=%!@(MISSING)"
- "Vv40@0:8@\"NSData\"16@\"NSNumber\"24@\"NSError\"32"
- "Vv40@0:8@16@24@32"
- "_authType"
- "_documents"
- "_error"
- "_responseErrorCode"
- "iso18013ReaderReceive:sessionDataStatus:status:"
- "response contains failure status: %!@(MISSING)"

```
