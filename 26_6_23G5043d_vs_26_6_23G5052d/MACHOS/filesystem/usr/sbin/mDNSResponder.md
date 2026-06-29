## mDNSResponder

> `/usr/sbin/mDNSResponder`

```diff

   __TEXT.__auth_stubs: 0x2ef0 sha256:baf08fa9682a8d6f7f4100a91da5157fc1302681cd2130fcb674312db8ef68e6
   __TEXT.__objc_stubs: 0x2020 sha256:d69d555f2c84a16733834b60c12e9b504b1957ff4a4601920e97b0865c6e25d5
   __TEXT.__objc_methlist: 0x694 sha256:3ccafe355071b7f7760501fee7ea6d2c6d66cf7a0c4ba2c286c7620c9e797988
-  __TEXT.__const: 0x1170 sha256:a92ce0ef4fbc479ee6a3ade9155ab3745936885de17f62ca4fbfac88b10ae8cb
-  __TEXT.__cstring: 0x179b8 sha256:65664a81c9c5d527036e3bfbd02430a8f057806fbe0ef223bc4e5451a8428d5b
+  __TEXT.__const: 0x1170 sha256:1cb8a28b1f84b1635d5965576e5e62d7dc3fed8f5319047f1b9b1ac68a623e9e
+  __TEXT.__cstring: 0x179b8 sha256:8a30271e9e893b1d42b841109f0900dbae9c214b3ba1cf7bb0500bbb92118712
   __TEXT.__gcc_except_tab: 0x338 sha256:6082cd23596f6a145f8d19528cbc54ff87b32ee3b26570fcb4e41df39c073c16
   __TEXT.__oslogstring: 0x1f627 sha256:b57b8d0d777c2136401d335cfca9aa5585fe5eda767ccae252c9b5430b43b0d3
   __TEXT.__objc_classname: 0x649 sha256:f03ba124fd96ed685c45f96aa2a32a9a5ce8ebb6c23e3b344104e30b90404161

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 97C5F950-28BE-3184-836D-58B476427684
+  UUID: B001A592-8864-3966-A865-B0141CE39B95
   Functions: 1844
   Symbols:   4609
   CStrings:  4913
Symbols:
+ ___mdns_create_dns_over_bytestream_framer_block_invoke.6352
+ __block_descriptor_tmp.1.6320
+ __block_descriptor_tmp.11.6346
+ __block_descriptor_tmp.11.6710
+ __block_descriptor_tmp.12.6707
+ __block_descriptor_tmp.14.875
+ __block_descriptor_tmp.16.6357
+ __block_descriptor_tmp.17.6701
+ __block_descriptor_tmp.18.6714
+ __block_descriptor_tmp.2.7024
+ __block_descriptor_tmp.2.7417
+ __block_descriptor_tmp.20.6995
+ __block_descriptor_tmp.21.7010
+ __block_descriptor_tmp.23.6996
+ __block_descriptor_tmp.25.6997
+ __block_descriptor_tmp.27.7002
+ __block_descriptor_tmp.28.7003
+ __block_descriptor_tmp.29.7004
+ __block_descriptor_tmp.3.6323
+ __block_descriptor_tmp.3.6350
+ __block_descriptor_tmp.3.6703
+ __block_descriptor_tmp.3.7581
+ __block_descriptor_tmp.30.6988
+ __block_descriptor_tmp.33.6994
+ __block_descriptor_tmp.34.6982
+ __block_descriptor_tmp.35.7011
+ __block_descriptor_tmp.4.6327
+ __block_descriptor_tmp.59.7481
+ __block_descriptor_tmp.6.6331
+ __block_descriptor_tmp.6.7421
+ __block_descriptor_tmp.63.7474
+ __block_descriptor_tmp.6316
+ __block_descriptor_tmp.6342
+ __block_descriptor_tmp.6402
+ __block_descriptor_tmp.6589
+ __block_descriptor_tmp.6695
+ __block_descriptor_tmp.6931
+ __block_descriptor_tmp.7.6334
+ __block_descriptor_tmp.7.6355
+ __block_descriptor_tmp.7.6960
+ __block_descriptor_tmp.7025
+ __block_descriptor_tmp.7059
+ __block_descriptor_tmp.7211
+ __block_descriptor_tmp.7414
+ __block_descriptor_tmp.7577
+ __block_descriptor_tmp.7785
+ __block_descriptor_tmp.79.7424
+ __block_descriptor_tmp.8.6696
+ __block_descriptor_tmp.81.7453
+ __block_literal_global.109
+ __block_literal_global.15.7701
+ __block_literal_global.4.7694
+ __block_literal_global.43.6643
+ __block_literal_global.5.6345
+ __block_literal_global.5.6698
+ __block_literal_global.6209
+ __block_literal_global.6340
+ __block_literal_global.6398
+ __block_literal_global.6582
+ __block_literal_global.6657
+ __block_literal_global.6929
+ __block_literal_global.6984
+ __block_literal_global.7208
+ __block_literal_global.7412
+ __block_literal_global.7575
+ __block_literal_global.7690
+ __block_literal_global.7783
+ __block_literal_global.8.7419
+ __block_literal_global.9.6353
+ g_nwi_state.4575
- ___mdns_create_dns_over_bytestream_framer_block_invoke.6353
- __block_descriptor_tmp.1.6321
- __block_descriptor_tmp.11.6347
- __block_descriptor_tmp.11.6711
- __block_descriptor_tmp.12.6708
- __block_descriptor_tmp.14.876
- __block_descriptor_tmp.16.6358
- __block_descriptor_tmp.17.6702
- __block_descriptor_tmp.18.6715
- __block_descriptor_tmp.2.7025
- __block_descriptor_tmp.2.7418
- __block_descriptor_tmp.20.6996
- __block_descriptor_tmp.21.7011
- __block_descriptor_tmp.23.6997
- __block_descriptor_tmp.25.6998
- __block_descriptor_tmp.27.7003
- __block_descriptor_tmp.28.7004
- __block_descriptor_tmp.29.7005
- __block_descriptor_tmp.3.6324
- __block_descriptor_tmp.3.6351
- __block_descriptor_tmp.3.6704
- __block_descriptor_tmp.3.7582
- __block_descriptor_tmp.30.6989
- __block_descriptor_tmp.33.6995
- __block_descriptor_tmp.34.6983
- __block_descriptor_tmp.35.7012
- __block_descriptor_tmp.4.6328
- __block_descriptor_tmp.59.7482
- __block_descriptor_tmp.6.6332
- __block_descriptor_tmp.6.7422
- __block_descriptor_tmp.63.7475
- __block_descriptor_tmp.6317
- __block_descriptor_tmp.6343
- __block_descriptor_tmp.6403
- __block_descriptor_tmp.6590
- __block_descriptor_tmp.6696
- __block_descriptor_tmp.6932
- __block_descriptor_tmp.7.6335
- __block_descriptor_tmp.7.6356
- __block_descriptor_tmp.7.6961
- __block_descriptor_tmp.7026
- __block_descriptor_tmp.7060
- __block_descriptor_tmp.7212
- __block_descriptor_tmp.7415
- __block_descriptor_tmp.7578
- __block_descriptor_tmp.7786
- __block_descriptor_tmp.79.7425
- __block_descriptor_tmp.8.6697
- __block_descriptor_tmp.81.7454
- __block_literal_global.103
- __block_literal_global.15.7702
- __block_literal_global.4.7695
- __block_literal_global.43.6644
- __block_literal_global.5.6346
- __block_literal_global.5.6699
- __block_literal_global.6210
- __block_literal_global.6341
- __block_literal_global.6399
- __block_literal_global.6583
- __block_literal_global.6658
- __block_literal_global.6930
- __block_literal_global.6985
- __block_literal_global.7209
- __block_literal_global.7413
- __block_literal_global.7576
- __block_literal_global.7691
- __block_literal_global.7784
- __block_literal_global.8.7420
- __block_literal_global.9.6354
- g_nwi_state.4574

```
