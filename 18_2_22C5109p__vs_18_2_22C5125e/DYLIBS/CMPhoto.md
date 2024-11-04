## CMPhoto

> `/System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto`

```diff

-356.60.4.0.0
-  __TEXT.__text: 0xfe9f0
-  __TEXT.__auth_stubs: 0x3300
+356.60.6.0.0
+  __TEXT.__text: 0xff368
+  __TEXT.__auth_stubs: 0x3330
   __TEXT.__objc_methlist: 0x3fc
-  __TEXT.__const: 0xc238
-  __TEXT.__cstring: 0x5c1b
+  __TEXT.__const: 0xc248
+  __TEXT.__cstring: 0x5cfc
+  __TEXT.__oslogstring: 0x790
   __TEXT.__gcc_except_tab: 0x160
-  __TEXT.__oslogstring: 0x168
-  __TEXT.__unwind_info: 0x1bb8
+  __TEXT.__unwind_info: 0x1bc0
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x54
   __TEXT.__objc_methname: 0x1ca1
   __TEXT.__objc_methtype: 0xb53
   __TEXT.__objc_stubs: 0x1ba0
   __DATA_CONST.__got: 0x1220
-  __DATA_CONST.__const: 0x2678
+  __DATA_CONST.__const: 0x26b8
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x778
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x1998
+  __AUTH_CONST.__auth_got: 0x19b0
   __AUTH_CONST.__auth_ptr: 0x68
   __AUTH_CONST.__const: 0x1248
-  __AUTH_CONST.__cfstring: 0x5b80
+  __AUTH_CONST.__cfstring: 0x5c20
   __AUTH_CONST.__objc_const: 0xcc8
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2407
-  Symbols:   4246
-  CStrings:  1309
+  Functions: 2409
+  Symbols:   4256
+  CStrings:  1326
 
Symbols:
+ _CMPhotoGetContainerFormatFromFormatString
+ _CMPhotoGetContainerFormatString
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _kCMPhotoContainerFormatString_HEIF
+ _kCMPhotoContainerFormatString_JFIF
+ _kCMPhotoContainerFormatString_JPEGXL
+ _kCMPhotoDecompressionContainerOption_AllowedFormatsAndCodecs
+ _kCMPhotoDecompressionContainerOption_DisallowedFormatsAndCodecs
CStrings:
+ "<<<< CMPhotoCodecSessionPool >>>> %!s(MISSING): VTCompressionOutputCallback_Gateway is called with NULL gateway. Check if the VTCompressionSession has already been released."
+ "<<<< CMPhotoCodecSessionPool >>>> %!s(MISSING): VTCompressionOutputCallback_Gateway is called with invalid gateway: gateway->type = %!u(MISSING), gateway->encodeCallback = %!p(MISSING). Check if the VTCompressionSession has already been released."
+ "<<<< CMPhotoCodecSessionPool >>>> %!s(MISSING): VTDecompressionOutputCallback_Gateway called with NULL gateway. Check if the VTDecompressionSession has already been released."
+ "<<<< CMPhotoCodecSessionPool >>>> %!s(MISSING): VTDecompressionOutputCallback_Gateway is called with invalid gateway: gateway->type = %!u(MISSING), gateway->decodeCallback = %!p(MISSING). Check if the VTDecompressionSession has already been released."
+ "<<<< CMPhotoCodecSessionPool >>>> %!s(MISSING): VTTileCompressionOutputCallback_Gateway is called with NULL gateway. Check if the VTTileCompressionSession has already been released."
+ "<<<< CMPhotoCodecSessionPool >>>> %!s(MISSING): VTTileCompressionOutputCallback_Gateway is called with invalid gateway: gateway->type= %!u(MISSING), gateway->tileEncodeCallback = %!p(MISSING). Check if the VTTileCompressionSession has already been released."
+ "<<<< CMPhotoCodecSessionPool >>>> %!s(MISSING): VTTileDecompressionOutputCallback_Gateway is called with NULL gateway. Check if the VTTileDecompressionSession has already been released."
+ "<<<< CMPhotoCodecSessionPool >>>> %!s(MISSING): VTTileDecompressionOutputCallback_Gateway is called with invalid gateway: gateway->type = %!u(MISSING), gateway->tileDecodeCallback = %!p(MISSING). Check if the VTTileDecompressionSession has already been released."
+ "AllowedFormatsAndCodecs"
+ "DisallowedFormatsAndCodecs"
+ "HEIF"
+ "JFIF"
+ "JPEG-XL"
+ "VTCompressionOutputCallback_Gateway"
+ "VTDecompressionOutputCallback_Gateway"
+ "VTTileCompressionOutputCallback_Gateway"
+ "VTTileDecompressionOutputCallback_Gateway"

```
