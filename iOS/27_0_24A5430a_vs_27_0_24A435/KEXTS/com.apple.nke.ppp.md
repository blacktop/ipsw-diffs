## com.apple.nke.ppp

> `com.apple.nke.ppp`

```diff

 1031.0.0.0.4
   __TEXT.__cstring: 0x1968
   __TEXT.__const: 0x230
-  __TEXT_EXEC.__text: 0x744c
+  __TEXT_EXEC.__text: 0x7588
   __TEXT_EXEC.__auth_stubs: 0x720
   __DATA.__data: 0x2d0
   __DATA.__common: 0x24
Functions:
~ sub_fffffe000a796e98 -> sub_fffffe000a87c678 : 168 -> 172
~ _ppp_comp_setcompressor : 524 -> 528
~ sub_fffffe000a79734c -> sub_fffffe000a87cb34 : 132 -> 136
~ _ppp_comp_ccp : 588 -> 592
~ sub_fffffe000a79761c -> sub_fffffe000a87ce0c : 104 -> 108
~ _ppp_comp_logmbuf : 640 -> 644
~ sub_fffffe000a79797c -> sub_fffffe000a87d174 : 128 -> 132
~ sub_fffffe000a797a24 -> sub_fffffe000a87d220 : 28 -> 32
~ _ppp_proto_ioctl : 364 -> 368
~ sub_fffffe000a797bac -> sub_fffffe000a87d3b0 : 28 -> 32
~ sub_fffffe000a797bc8 -> sub_fffffe000a87d3d0 : 124 -> 128
~ sub_fffffe000a797c44 -> sub_fffffe000a87d450 : 80 -> 84
~ _ppp_proto_add : 112 -> 116
~ _ppp_proto_remove : 116 -> 120
~ _ppp_domain_dispose : 92 -> 96
~ _ppp_proto_free : 120 -> 124
~ _ppp_proto_input : 180 -> 184
~ sub_fffffe000a797f28 -> sub_fffffe000a87d74c : 88 -> 92
~ sub_fffffe000a797f80 -> sub_fffffe000a87d7a8 : 88 -> 92
~ sub_fffffe000a797fd8 -> sub_fffffe000a87d804 : 76 -> 80
~ _ppp_if_init : 212 -> 216
~ sub_fffffe000a798164 -> sub_fffffe000a87d998 : 1096 -> 1100
~ sub_fffffe000a7985ac -> sub_fffffe000a87dde4 : 680 -> 684
~ _ppp_if_demux : 132 -> 136
~ _ppp_if_add_proto : 84 -> 88
~ _ppp_if_del_proto : 68 -> 72
~ _ppp_if_frameout : 196 -> 200
~ _ppp_if_ioctl : 632 -> 636
~ sub_fffffe000a798cac -> sub_fffffe000a87e4fc : 88 -> 92
~ sub_fffffe000a798d04 -> sub_fffffe000a87e558 : 152 -> 156
~ _ppp_if_detachclient : 580 -> 584
~ _ppp_if_input : 1600 -> 1604
~ _ppp_if_control : 1304 -> 1308
~ sub_fffffe000a799bd4 -> sub_fffffe000a87f438 : 212 -> 216
~ sub_fffffe000a799ca8 -> sub_fffffe000a87f510 : 240 -> 244
~ sub_fffffe000a799d98 -> sub_fffffe000a87f604 : 624 -> 628
~ _ppp_if_xmit : 332 -> 336
~ sub_fffffe000a79a154 -> sub_fffffe000a87f9c8 : 104 -> 108
~ sub_fffffe000a79a1f0 -> sub_fffffe000a87fa68 : 100 -> 104
~ sub_fffffe000a79a254 -> sub_fffffe000a87fad0 : 116 -> 120
~ _ppp_link_detach : 216 -> 220
~ sub_fffffe000a79a3a0 -> sub_fffffe000a87fc24 : 108 -> 112
~ _ppp_link_input : 316 -> 320
~ _ppp_link_logmbuf : 700 -> 704
~ _ppp_link_control : 816 -> 820
~ sub_fffffe000a79ab34 -> sub_fffffe000a8803c8 : 132 -> 136
~ _ppp_link_send : 292 -> 296
~ _pppisr_thread : 432 -> 436
~ sub_fffffe000a79aff8 -> sub_fffffe000a880898 : 1108 -> 1112
~ _pppserial_open : 564 -> 568
~ _pppserial_close : 352 -> 356
~ _pppserial_ioctl : 736 -> 740
~ _pppserial_input : 2492 -> 2496
~ sub_fffffe000a79c494 -> sub_fffffe000a881d48 : 160 -> 164
~ _pppserial_lk_ioctl : 1064 -> 1068
~ sub_fffffe000a79c95c -> sub_fffffe000a882218 : 268 -> 272
~ sub_fffffe000a79ca68 -> sub_fffffe000a882328 : 196 -> 200
~ _pppserial_logchar : 132 -> 136
~ _ppp_module_start : 200 -> 204
~ _ppp_module_stop : 316 -> 320
~ sub_fffffe000a79cdb4 -> sub_fffffe000a882684 : 236 -> 240
~ sub_fffffe000a79cea0 -> sub_fffffe000a882774 : 1508 -> 1512
~ sub_fffffe000a79d484 -> sub_fffffe000a882d5c : 228 -> 232
~ sub_fffffe000a79d568 -> sub_fffffe000a882e44 : 1044 -> 1048
~ _ppp_ipv6_attach : 288 -> 292
~ _ppp_ipv6_detach : 116 -> 120
~ sub_fffffe000a79db48 -> sub_fffffe000a883430 : 36 -> 40
~ sub_fffffe000a79db6c -> sub_fffffe000a883458 : 60 -> 64
~ _ppp_ipv6_ioctl : 152 -> 156
~ _ppp_ip_attach : 304 -> 308
~ _ppp_ip_detach : 128 -> 132
~ sub_fffffe000a79de3c -> sub_fffffe000a883738 : 36 -> 40
~ sub_fffffe000a79de60 -> sub_fffffe000a883760 : 60 -> 64
~ sub_fffffe000a79de9c -> sub_fffffe000a8837a0 : 184 -> 188
~ _ppp_ip_ioctl : 276 -> 280
~ sub_fffffe000a79e068 -> sub_fffffe000a883974 : 92 -> 96
~ sub_fffffe000a79e0c4 -> sub_fffffe000a8839d4 : 92 -> 96
~ sub_fffffe000a79e120 -> sub_fffffe000a883a34 : 140 -> 144
~ sub_fffffe000a79e1ac -> sub_fffffe000a883ac4 : 140 -> 144
```
