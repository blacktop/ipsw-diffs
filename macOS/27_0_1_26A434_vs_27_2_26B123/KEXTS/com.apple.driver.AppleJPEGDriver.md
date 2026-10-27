## com.apple.driver.AppleJPEGDriver

> `com.apple.driver.AppleJPEGDriver`

```diff

-8.1.7.0.0
+8.1.8.0.0
   __TEXT.__cstring: 0x2b0e
-  __TEXT.__os_log: 0x8d36
+  __TEXT.__os_log: 0x8ccb
   __TEXT.__const: 0x3cdc
-  __TEXT_EXEC.__text: 0x2a75c
+  __TEXT_EXEC.__text: 0x2a6e0
   __TEXT_EXEC.__auth_stubs: 0x680
   __DATA.__data: 0x2b34
   __DATA.__common: 0x3a8

   __DATA_CONST.__auth_got: 0x340
   __DATA_CONST.__got: 0x98
   Functions: 1573
-  Symbols:   2656
-  CStrings:  531
+  Symbols:   2654
+  CStrings:  529
 
Symbols:
- __ZZN15AppleJPEGDriver18assign_codec_gatedEP11JpegRequestE11_os_log_fmt_2
- __ZZN26AppleJPEGWrapperControlV1428ajpeg_drv_set_image_boundaryEP13ajpeg_setup_tE11_os_log_fmt_1
Functions:
~ __ZN26AppleJPEGWrapperControlV1428ajpeg_drv_set_image_boundaryEP13ajpeg_setup_t : 1252 -> 1176
~ __ZN15AppleJPEGDriver14queue_io_gatedEP11JpegRequest : 1872 -> 1824
CStrings:
- "AppleJPEGDriver: %s rdcnv_bitdepth_out(%d)\n"
- "AppleJPEGDriver: - %s : running on core w/ least workload: %d\n"
```
