## mDNSResponder

> `/usr/sbin/mDNSResponder`

```diff

-2559.40.32.0.0
-  __TEXT.__text: 0x101258
-  __TEXT.__auth_stubs: 0x2df0
+2559.60.35.0.0
+  __TEXT.__text: 0x1011b0
+  __TEXT.__auth_stubs: 0x2de0
   __TEXT.__objc_stubs: 0x15a0
   __TEXT.__objc_methlist: 0x21c
   __TEXT.__const: 0x1128
   __TEXT.__gcc_except_tab: 0x1c4
-  __TEXT.__cstring: 0x16e2b
+  __TEXT.__cstring: 0x16e0d
   __TEXT.__oslogstring: 0x1dc56
   __TEXT.__objc_classname: 0x63a
   __TEXT.__objc_methname: 0x13ed
   __TEXT.__objc_methtype: 0x5da
-  __TEXT.__unwind_info: 0x1660
-  __DATA_CONST.__auth_got: 0x1708
-  __DATA_CONST.__got: 0x330
+  __TEXT.__unwind_info: 0x1668
+  __DATA_CONST.__auth_got: 0x1700
+  __DATA_CONST.__got: 0x328
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x6068
-  __DATA_CONST.__cfstring: 0x1160
+  __DATA_CONST.__const: 0x6048
+  __DATA_CONST.__cfstring: 0x1140
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x1e8

   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x11d0
   __DATA.__data: 0x42b8
-  __DATA.__bss: 0x16d20
+  __DATA.__bss: 0x16d10
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 1803
-  Symbols:   4329
-  CStrings:  4495
+  Functions: 1802
+  Symbols:   4323
+  CStrings:  4494
 
Symbols:
+ GCC_except_table1503
+ ___mdns_create_dns_over_bytestream_framer_block_invoke.6218
+ __block_descriptor_tmp.1.6185
+ __block_descriptor_tmp.10.7252
+ __block_descriptor_tmp.11.6212
+ __block_descriptor_tmp.11.6549
+ __block_descriptor_tmp.12.6546
+ __block_descriptor_tmp.16.6210
+ __block_descriptor_tmp.17.6540
+ __block_descriptor_tmp.18.6553
+ __block_descriptor_tmp.2.6852
+ __block_descriptor_tmp.20.6823
+ __block_descriptor_tmp.21.6838
+ __block_descriptor_tmp.23.6824
+ __block_descriptor_tmp.25.6825
+ __block_descriptor_tmp.27.6830
+ __block_descriptor_tmp.28.6831
+ __block_descriptor_tmp.29.6832
+ __block_descriptor_tmp.3.6188
+ __block_descriptor_tmp.3.6216
+ __block_descriptor_tmp.3.6542
+ __block_descriptor_tmp.3.7377
+ __block_descriptor_tmp.30.6820
+ __block_descriptor_tmp.33.6817
+ __block_descriptor_tmp.34.6839
+ __block_descriptor_tmp.4.6192
+ __block_descriptor_tmp.46.7293
+ __block_descriptor_tmp.50.7286
+ __block_descriptor_tmp.6.6196
+ __block_descriptor_tmp.6.7242
+ __block_descriptor_tmp.6181
+ __block_descriptor_tmp.6206
+ __block_descriptor_tmp.6266
+ __block_descriptor_tmp.6534
+ __block_descriptor_tmp.6764
+ __block_descriptor_tmp.68.7264
+ __block_descriptor_tmp.6853
+ __block_descriptor_tmp.6887
+ __block_descriptor_tmp.7.6199
+ __block_descriptor_tmp.7.6221
+ __block_descriptor_tmp.7.6791
+ __block_descriptor_tmp.7039
+ __block_descriptor_tmp.7236
+ __block_descriptor_tmp.7373
+ __block_descriptor_tmp.7613
+ __block_descriptor_tmp.8.6535
+ __block_literal_global.12.7248
+ __block_literal_global.15.7493
+ __block_literal_global.43.6481
+ __block_literal_global.5.6208
+ __block_literal_global.5.6537
+ __block_literal_global.6075
+ __block_literal_global.6204
+ __block_literal_global.6262
+ __block_literal_global.6495
+ __block_literal_global.6762
+ __block_literal_global.6813
+ __block_literal_global.7036
+ __block_literal_global.7234
+ __block_literal_global.7371
+ __block_literal_global.7484
+ __block_literal_global.7611
+ __block_literal_global.8.7240
+ __block_literal_global.9.6082
+ __block_literal_global.9.6219
- GCC_except_table1504
- _CFPreferencesGetAppBooleanValue
- ___is_airplay_demo_mode_enabled_block_invoke
- ___mdns_create_dns_over_bytestream_framer_block_invoke.6223
- __block_descriptor_tmp.1.6190
- __block_descriptor_tmp.10.7257
- __block_descriptor_tmp.11.6217
- __block_descriptor_tmp.11.6554
- __block_descriptor_tmp.12.6551
- __block_descriptor_tmp.16.6215
- __block_descriptor_tmp.17.6545
- __block_descriptor_tmp.18.6558
- __block_descriptor_tmp.2.6857
- __block_descriptor_tmp.20.6828
- __block_descriptor_tmp.21.6843
- __block_descriptor_tmp.23.6829
- __block_descriptor_tmp.25.6830
- __block_descriptor_tmp.27.6835
- __block_descriptor_tmp.28.6836
- __block_descriptor_tmp.29.6837
- __block_descriptor_tmp.3.6193
- __block_descriptor_tmp.3.6221
- __block_descriptor_tmp.3.6547
- __block_descriptor_tmp.3.7382
- __block_descriptor_tmp.30.6825
- __block_descriptor_tmp.33.6822
- __block_descriptor_tmp.34.6844
- __block_descriptor_tmp.4.6197
- __block_descriptor_tmp.46.7298
- __block_descriptor_tmp.50.7291
- __block_descriptor_tmp.6.6201
- __block_descriptor_tmp.6.7247
- __block_descriptor_tmp.6186
- __block_descriptor_tmp.6211
- __block_descriptor_tmp.6271
- __block_descriptor_tmp.6539
- __block_descriptor_tmp.6769
- __block_descriptor_tmp.68.7269
- __block_descriptor_tmp.6858
- __block_descriptor_tmp.6892
- __block_descriptor_tmp.7.6204
- __block_descriptor_tmp.7.6226
- __block_descriptor_tmp.7.6796
- __block_descriptor_tmp.7044
- __block_descriptor_tmp.7241
- __block_descriptor_tmp.7378
- __block_descriptor_tmp.7618
- __block_descriptor_tmp.8.6540
- __block_literal_global.12.6087
- __block_literal_global.12.7253
- __block_literal_global.15.7498
- __block_literal_global.3.6075
- __block_literal_global.43.6486
- __block_literal_global.5.6213
- __block_literal_global.5.6542
- __block_literal_global.6073
- __block_literal_global.6209
- __block_literal_global.6267
- __block_literal_global.6500
- __block_literal_global.6767
- __block_literal_global.6818
- __block_literal_global.7041
- __block_literal_global.7239
- __block_literal_global.7376
- __block_literal_global.7489
- __block_literal_global.7616
- __block_literal_global.8.7245
- __block_literal_global.9.6224
- _kCFPreferencesAnyApplication
- is_airplay_demo_mode_enabled.is_demo_mode_enabled
- is_airplay_demo_mode_enabled.once
CStrings:
+ "mDNSResponder-2559.60.35"
- "EnableTetheredDisplayPortMode"
- "mDNSResponder-2559.40.32"

```
