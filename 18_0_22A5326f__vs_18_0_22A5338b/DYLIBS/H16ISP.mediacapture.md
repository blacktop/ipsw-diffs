## H16ISP.mediacapture

> `/System/Library/MediaCapture/H16ISP.mediacapture`

```diff

-3.39.2.0.0
-  __TEXT.__text: 0x1a77dc
-  __TEXT.__auth_stubs: 0x31d0
+3.45.0.0.0
+  __TEXT.__text: 0x1a7708
+  __TEXT.__auth_stubs: 0x31e0
   __TEXT.__init_offsets: 0x18
   __TEXT.__objc_methlist: 0x11c
   __TEXT.__gcc_except_tab: 0x5ca0
   __TEXT.__const: 0x215fc
   __TEXT.__cstring: 0x1935a
-  __TEXT.__oslogstring: 0x1a8c6
+  __TEXT.__oslogstring: 0x1a8f6
   __TEXT.__unwind_info: 0x3ae8
   __TEXT.__eh_frame: 0x110
   __TEXT.__objc_classname: 0x89

   __DATA_CONST.__objc_selrefs: 0x818
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x18f8
+  __AUTH_CONST.__auth_got: 0x1900
   __AUTH_CONST.__auth_ptr: 0x98
   __AUTH_CONST.__const: 0x2040
   __AUTH_CONST.__cfstring: 0x93c0

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5514
+  Functions: 5513
   Symbols:   9047
-  CStrings:  6219
+  CStrings:  6221
 
Symbols:
+ __os_log_unreliable_impl
CStrings:
+ "Error sending sCIspCmdChCropSet command: 0x%!X(MISSING)"
+ "Error sending sCIspCmdChOutputConfigSet command: 0x%!X(MISSING)"
+ "Received frame drop request: channel=%!d(MISSING) frameDropRequestEnabled=%!d(MISSING) frameCount=%!d(MISSING)"
+ "Sending data buffer failed, result=0x%!X(MISSING)"
+ "Sending shared buffer failed, result=0x%!X(MISSING)"
+ "Unable to allocate a replacement buffer (poolID = CHAN_%!d(MISSING)_%!s(MISSING), actual poolID = %!d(MISSING), buffer pool pointer = %!p(MISSING))"
+ "Unable to locate surface ID %!d(MISSING)"
+ "pH16ISPDevice->ISP_SendBuffers failed, result=0x%!X(MISSING)"
- "%!s(MISSING) - Error sending sCIspCmdChCropSet command: 0x%!X(MISSING)\n"
- "%!s(MISSING) - Error sending sCIspCmdChOutputConfigSet command: 0x%!X(MISSING)\n"
- "%!s(MISSING) - Received frame drop request: channel=%!d(MISSING) frameDropRequestEnabled=%!d(MISSING) frameCount=%!d(MISSING)\n"
- "%!s(MISSING) - Sending data buffer failed, result=0x%!X(MISSING)\n"
- "%!s(MISSING) - Sending shared buffer failed, result=0x%!X(MISSING)\n"
- "%!s(MISSING) - Unable to allocate a replacement buffer (poolID = CHAN_%!d(MISSING)_%!s(MISSING), actual poolID = %!d(MISSING), buffer pool pointer = %!p(MISSING))\n"

```
