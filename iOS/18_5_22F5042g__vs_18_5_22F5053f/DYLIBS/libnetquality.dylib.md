## libnetquality.dylib

> `/usr/lib/libnetquality.dylib`

```diff

-147.120.5.0.0
-  __TEXT.__text: 0x183e8
+147.120.6.0.0
+  __TEXT.__text: 0x187f0
   __TEXT.__auth_stubs: 0xb70
-  __TEXT.__objc_methlist: 0x168c
-  __TEXT.__const: 0x180
+  __TEXT.__objc_methlist: 0x169c
+  __TEXT.__const: 0x190
   __TEXT.__gcc_except_tab: 0x52c
-  __TEXT.__cstring: 0x2322
-  __TEXT.__oslogstring: 0x1625
+  __TEXT.__cstring: 0x23ec
+  __TEXT.__oslogstring: 0x162a
   __TEXT.__unwind_info: 0x4d0
   __TEXT.__objc_classname: 0x315
   __TEXT.__objc_methname: 0x3e46

   __DATA_CONST.__objc_arraydata: 0x58
   __AUTH_CONST.__auth_got: 0x5c8
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x1920
+  __AUTH_CONST.__cfstring: 0x1940
   __AUTH_CONST.__objc_const: 0x36b0
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_floatobj: 0x10

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 552
-  Symbols:   829
-  CStrings:  1401
+  Functions: 555
+  Symbols:   836
+  CStrings:  1403
 
Symbols:
+ _NetworkQualityErrorMeasurementTransferredNoBytes
CStrings:
+ "%s:%u - server response without test_endpoint specified"
+ "-[UploadThroughputDelegate URLSession:dataTask:didReceiveResponse:completionHandler:]"
+ "Request got 200, but transferred no bytes on throughput measurement connection. Is the server configured correctly?"
- "%s:%u - server response without test_endpoint spec"

```
