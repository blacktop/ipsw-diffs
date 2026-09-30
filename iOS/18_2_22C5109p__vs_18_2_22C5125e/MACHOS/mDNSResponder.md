## mDNSResponder

> `/usr/sbin/mDNSResponder`

```diff

-2559.60.35.0.0
-  __TEXT.__text: 0x1011b0
-  __TEXT.__auth_stubs: 0x2de0
+2559.60.39.0.0
+  __TEXT.__text: 0x101360
+  __TEXT.__auth_stubs: 0x2e20
   __TEXT.__objc_stubs: 0x15a0
   __TEXT.__objc_methlist: 0x21c
   __TEXT.__const: 0x1128
   __TEXT.__gcc_except_tab: 0x1c4
   __TEXT.__cstring: 0x16e0d
-  __TEXT.__oslogstring: 0x1dc56
+  __TEXT.__oslogstring: 0x1dc6a
   __TEXT.__objc_classname: 0x63a
   __TEXT.__objc_methname: 0x13ed
   __TEXT.__objc_methtype: 0x5da
   __TEXT.__unwind_info: 0x1668
-  __DATA_CONST.__auth_got: 0x1700
+  __DATA_CONST.__auth_got: 0x1720
   __DATA_CONST.__got: 0x328
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x6048

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   Functions: 1802
-  Symbols:   4323
-  CStrings:  4494
+  Symbols:   4327
+  CStrings:  4495
 
Symbols:
+ ___mdns_create_dns_over_bytestream_framer_block_invoke.6220
+ __block_descriptor_tmp.1.6187
+ __block_descriptor_tmp.10.6030
+ __block_descriptor_tmp.10.7254
+ __block_descriptor_tmp.11.6214
+ __block_descriptor_tmp.11.6551
+ __block_descriptor_tmp.12.6037
+ __block_descriptor_tmp.12.6548
+ __block_descriptor_tmp.13.6038
+ __block_descriptor_tmp.16.6212
+ __block_descriptor_tmp.17.6542
+ __block_descriptor_tmp.18.6555
+ __block_descriptor_tmp.2.6854
+ __block_descriptor_tmp.20.6032
+ __block_descriptor_tmp.20.6825
+ __block_descriptor_tmp.21.6840
+ __block_descriptor_tmp.22.6033
+ __block_descriptor_tmp.23.6826
+ __block_descriptor_tmp.24.6028
+ __block_descriptor_tmp.25.6827
+ __block_descriptor_tmp.26.6025
+ __block_descriptor_tmp.27.6022
+ __block_descriptor_tmp.27.6832
+ __block_descriptor_tmp.28.6020
+ __block_descriptor_tmp.28.6833
+ __block_descriptor_tmp.29.6834
+ __block_descriptor_tmp.3.6046
+ __block_descriptor_tmp.3.6190
+ __block_descriptor_tmp.3.6218
+ __block_descriptor_tmp.3.6544
+ __block_descriptor_tmp.3.7379
+ __block_descriptor_tmp.30.6011
+ __block_descriptor_tmp.30.6822
+ __block_descriptor_tmp.32.6013
+ __block_descriptor_tmp.33.6819
+ __block_descriptor_tmp.34.6841
+ __block_descriptor_tmp.4.6047
+ __block_descriptor_tmp.4.6194
+ __block_descriptor_tmp.46.7295
+ __block_descriptor_tmp.5.6048
+ __block_descriptor_tmp.50.7288
+ __block_descriptor_tmp.6.6198
+ __block_descriptor_tmp.6.7244
+ __block_descriptor_tmp.6183
+ __block_descriptor_tmp.62.6007
+ __block_descriptor_tmp.6208
+ __block_descriptor_tmp.6268
+ __block_descriptor_tmp.6536
+ __block_descriptor_tmp.6766
+ __block_descriptor_tmp.68.7266
+ __block_descriptor_tmp.6855
+ __block_descriptor_tmp.6889
+ __block_descriptor_tmp.7.6050
+ __block_descriptor_tmp.7.6201
+ __block_descriptor_tmp.7.6223
+ __block_descriptor_tmp.7.6793
+ __block_descriptor_tmp.7041
+ __block_descriptor_tmp.7238
+ __block_descriptor_tmp.7375
+ __block_descriptor_tmp.7615
+ __block_descriptor_tmp.8.6537
+ __block_literal_global.12.7250
+ __block_literal_global.15.7495
+ __block_literal_global.43.6483
+ __block_literal_global.5.6210
+ __block_literal_global.5.6539
+ __block_literal_global.6077
+ __block_literal_global.6206
+ __block_literal_global.6264
+ __block_literal_global.6497
+ __block_literal_global.6764
+ __block_literal_global.6815
+ __block_literal_global.7038
+ __block_literal_global.7236
+ __block_literal_global.7373
+ __block_literal_global.7486
+ __block_literal_global.7613
+ __block_literal_global.8.7242
+ __block_literal_global.9.6084
+ __block_literal_global.9.6221
+ _nw_connection_copy_parameters
+ _nw_protocol_stack_copy_transport_protocol
+ _nw_tcp_options_get_maximum_segment_size
+ _nw_tcp_options_set_maximum_segment_size
- ___mdns_create_dns_over_bytestream_framer_block_invoke.6218
- __block_descriptor_tmp.1.6185
- __block_descriptor_tmp.10.6028
- __block_descriptor_tmp.10.7252
- __block_descriptor_tmp.11.6212
- __block_descriptor_tmp.11.6549
- __block_descriptor_tmp.12.6035
- __block_descriptor_tmp.12.6546
- __block_descriptor_tmp.13.6036
- __block_descriptor_tmp.16.6210
- __block_descriptor_tmp.17.6540
- __block_descriptor_tmp.18.6553
- __block_descriptor_tmp.2.6852
- __block_descriptor_tmp.20.6030
- __block_descriptor_tmp.20.6823
- __block_descriptor_tmp.21.6838
- __block_descriptor_tmp.22.6031
- __block_descriptor_tmp.23.6824
- __block_descriptor_tmp.24.6026
- __block_descriptor_tmp.25.6825
- __block_descriptor_tmp.26.6024
- __block_descriptor_tmp.27.6021
- __block_descriptor_tmp.27.6830
- __block_descriptor_tmp.28.6019
- __block_descriptor_tmp.28.6831
- __block_descriptor_tmp.29.6832
- __block_descriptor_tmp.3.6044
- __block_descriptor_tmp.3.6188
- __block_descriptor_tmp.3.6216
- __block_descriptor_tmp.3.6542
- __block_descriptor_tmp.3.7377
- __block_descriptor_tmp.30.6010
- __block_descriptor_tmp.30.6820
- __block_descriptor_tmp.32.6012
- __block_descriptor_tmp.33.6817
- __block_descriptor_tmp.34.6839
- __block_descriptor_tmp.4.6045
- __block_descriptor_tmp.4.6192
- __block_descriptor_tmp.46.7293
- __block_descriptor_tmp.5.6046
- __block_descriptor_tmp.50.7286
- __block_descriptor_tmp.6.6196
- __block_descriptor_tmp.6.7242
- __block_descriptor_tmp.6181
- __block_descriptor_tmp.62.6006
- __block_descriptor_tmp.6206
- __block_descriptor_tmp.6266
- __block_descriptor_tmp.6534
- __block_descriptor_tmp.6764
- __block_descriptor_tmp.68.7264
- __block_descriptor_tmp.6853
- __block_descriptor_tmp.6887
- __block_descriptor_tmp.7.6048
- __block_descriptor_tmp.7.6199
- __block_descriptor_tmp.7.6221
- __block_descriptor_tmp.7.6791
- __block_descriptor_tmp.7039
- __block_descriptor_tmp.7236
- __block_descriptor_tmp.7373
- __block_descriptor_tmp.7613
- __block_descriptor_tmp.8.6535
- __block_literal_global.12.7248
- __block_literal_global.15.7493
- __block_literal_global.43.6481
- __block_literal_global.5.6208
- __block_literal_global.5.6537
- __block_literal_global.6075
- __block_literal_global.6204
- __block_literal_global.6262
- __block_literal_global.6495
- __block_literal_global.6762
- __block_literal_global.6813
- __block_literal_global.7036
- __block_literal_global.7234
- __block_literal_global.7371
- __block_literal_global.7484
- __block_literal_global.7611
- __block_literal_global.8.7240
- __block_literal_global.9.6082
- __block_literal_global.9.6219
CStrings:
+ "[DSO%!l(MISSING)lu] mss is %!d(MISSING)"
+ "mDNSResponder-2559.60.39"
- "mDNSResponder-2559.60.35"

```
