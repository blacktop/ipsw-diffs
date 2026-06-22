## libJPEG.dylib

> `/System/Library/Frameworks/ImageIO.framework/Versions/A/Resources/libJPEG.dylib`

```diff

-2839.0.0.0.0
-  __TEXT.__text: 0x27a94 sha256:f026a547680317d24a06f46df95f361449ec7cc730bfaacd863a23d06fbad9fe
+2843.1.1.0.0
+  __TEXT.__text: 0x27c8c sha256:053bb123f9843e6e27c230dd770176ec49fe3406178d1d9efa047303c247595d
   __TEXT.__const: 0x14f8 sha256:6ea2a8b57aa28133af3ca8fa0fef55b5ed09ed688f6adecd295774e867335675
   __TEXT.__cstring: 0x1275 sha256:70a7f768375f26012b5f8d3daf2b5691a05fedeff919d155ad53b3f1b649d0d7
-  __TEXT.__unwind_info: 0x470 sha256:d37dbb1eda2acdbc8856b750bd0538de1e38fca5d2cd4228c80359134b19715e
-  __TEXT.__eh_frame: 0x1d0 sha256:5ef9ab570c477b31e626ea1db98bfe7d7eb2081c16214e1aa87ff9600f95628f
+  __TEXT.__unwind_info: 0x490 sha256:d4b49d89586ae2fc01ceb19f799028ca2d755a8ff10b5eb518962b3b1beb03aa
+  __TEXT.__eh_frame: 0x1d0 sha256:2b2e18889ce0655de89d480220a4fcde870c57e01f55752e908a616c365b09c8
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x430 sha256:0a3145d1b73929c56b78f7071bad37a8982011721e7458b9fb61c26c8da89d83
+  __DATA_CONST.__const: 0x430 sha256:68eca9023f35bdf5b572922a9b9235cdc70c338b5ef44063e912536d1a99b9cb
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x30 sha256:377aa650021d6e7a2bb18bab7cfe2ff3bbd1471e49e1aaf96736a730af277d04
+  __AUTH_CONST.__const: 0x30 sha256:5684dea3743413252da82f8e11d608f25cca94c6af87b0359681b44822a20246
   __AUTH_CONST.__auth_got: 0x0
   - /usr/lib/libSystem.B.dylib
-  UUID: D3158C4A-C69E-3217-8967-00A0307B4929
+  UUID: 7647EB15-E4E3-395E-B7BE-0A59432CB49A
   Functions: 368
   Symbols:   427
   CStrings:  130
Functions:
~ _jpeg_calc_jpeg_dimensions : sha256 9684a8f1582f3ae80beedf77fa020baef2c44e5b3bf382e70ea64f3a02716544 -> 2837f497cbd51336223bbb73a6f6a088f67c9603a7eedbc4876a972b42ed3939
~ __cg_jinit_compress_master : sha256 936c218261356d6b431b609bf887c45826b1efe1b2c50d06f8ba96e4da9cb179 -> c4b1d74fa201f7fb3d03b1cbd6a54f7fe2ab732397088ceb0c5f8c15b1c693c2
~ __cg_jinit_color_converter : sha256 8084e3583471c681f4300a9a72ab88e7223b0ef0717764c9d86040899f37ef3b -> 57977339c26c2744a22894157b583004afe261da722e420dc3d706970a8f4d2e
~ _rgb_ycc_start : 196 -> 248
~ _rgb_gray_convert : 136 -> 144
~ _rgb_convert : 104 -> 112
~ _rgb_rgb1_convert : 120 -> 128
~ _rgb_ycc_convert : 196 -> 268
~ _cmyk_ycck_convert : 220 -> 308
~ __cg_jinit_inverse_dct : 208 -> 204
~ _start_pass : 1652 -> 1664
~ __cg_jinit_2pass_quantizer : 448 -> 452
~ _start_pass_2_quant : 376 -> 372
~ _init_error_limit : 208 -> 188
~ _prescan_quantize : 136 -> 128
~ _finish_pass1 : 892 -> 928
~ _pass2_fs_dither : 744 -> 796
~ _pass2_no_dither : 220 -> 216
~ _fill_inverse_cmap : 1012 -> 988
~ __cg_jinit_marker_reader : sha256 664c801ed92d30482337924e70e583b6b04762f4752a1f621ab5642ff299f46c -> 814b58afd93dd0a3fc10698476eefd2c63726f1b674578fd1645b06ac0650aa9
~ _read_markers : 5084 -> 5060
~ sub_193f3a6e0 -> sub_193e867dc : sha256 c66a6d19fae1390c526a3297a88273646aad449ec98508ce2992ec1279b3ca36 -> d9dea40977bb882bb4647ca6480ae91c18270a00d04bdc621330cdca0c0e7cd9
~ _read_restart_marker : sha256 cd27f510edb59c6e8f64057bac9dfc33818105b70d26fe78d9d189a26de810fd -> dcdaef31f24a6bee17fa1ed7922b3e6d87f111cae2c6354c5cc041203382ba43
~ _get_interesting_appn : 428 -> 444
~ __cg_jpeg_save_markers : sha256 553d1a4865f80d722bc6ccb7580ba3f499df0a8d8d2166cca1f4772ed8de67b4 -> 64f74c9b08bb690af79a1369cabee99ddc05f659170892de2b5039761207d931
~ _save_marker : 620 -> 596
~ __cg_jpeg_std_huff_table : sha256 a328a6e369a4de16f87c12136b546d30188794924b578febb02d7d348f63987d -> a18a73f77b117add1645f28bae2f9c3d9277e2f8966bce4e193a318ef582e1fe
~ _jinit_arith_encoder : sha256 33ea0964727dd63dd9a019aad87684afddaadde738a8442e661ee7bb4679f0ae -> ee38bbfa9ba8059dc64c6971ea244d872985679a1e6356d4622d0335ecc7caa3
~ _start_pass : 536 -> 548
~ _finish_pass : sha256 64e53144e8da5a571c23c2742d0b551fb986902ec5a23a372c292858efcfcfa9 -> 80549d1efa9c99b2a8d42754f6e3579491a8a8fe7617cee956fa89ca5ec5dcdd
~ _encode_mcu_DC_first : sha256 d6c9d04c4095e27d771657f4d8ffcb724d6fb073558cc7832ea65909867fa3f8 -> 7f0d079353af5e0f27f8e3175359c3ab6590f21ac0f1b675ace02c2e0209847c
~ _encode_mcu_AC_first : 720 -> 764
~ _encode_mcu_DC_refine : 184 -> 180
~ _encode_mcu_AC_refine : 600 -> 616
~ _encode_mcu : 1224 -> 1244
~ _emit_restart : 256 -> 252
~ _arith_encode : 536 -> 532
~ __cg_jpeg_get_small : sha256 d95a3b44b7bbe17f9b4a1afe35e85afc6e1a79859f4118d3e20b6acfe8b58da3 -> 2d58c5e5f707290b67763b49845cdb5e8603d85486bab1957b94e1874486fcfe
~ __cg_jpeg_free_small : sha256 79a11e398d25d605f875191e2aff3a77e0e42a44ce94d399b7bae7eead4620e9 -> 96458311a0fdbc5ceee8bf9d9934e325ecb7051c1e77585a5914d4f6f8977273
~ __cg_jpeg_get_large : sha256 001b32aaffe0a0550526e9ca7a69726057e37e7527e2d4db2bc58fa357a455c1 -> 346a48b0739e1d250bf6035420e758ed8e53ba04eaf74005fe95269dbd478ef3
~ __cg_jpeg_free_large : sha256 4dbdf17aceb13604c447f81e800b7c4ccfb8a47665175cfeadfbe3c34bac7dcc -> 1a23c8822a3ddf33f0ad3bb61b55e5e0da3011fc3a64c6772a93c9bf11924528
~ __cg_jpeg_open_backing_store : sha256 41b7c6e034e12e9714d5ebbf381ecafc3bcd1329b0e80a1f5a69551ee2d766d7 -> 011cd0912df2194962cd7958b39a114b1486c9a464ddb987450741a6579f8a71
~ _read_backing_store : sha256 133144ca4d7741f631b4ca9e6d0b1e60fc639fc67eb667da777b670419ea8f61 -> 5906d1f7450fbf4ea7d6d294252406e5622e90f93709572a41535d8c3d53815b
~ _write_backing_store : sha256 b3077b3eb3bd91e849ab82771de423aa306a6b1fdf67d3340ad778de74dd578d -> e3ccb9a41dec8a1bd49e4c89cb2bc14ff0b1ad4c095461d4a3bcfe01c579dcb5
~ _close_backing_store : sha256 5b3bf32ec5f8edd9a6f4f3605d1d75056a0294f6217f88f3ff8712b22b497eca -> d263b65fffb1b5ed019585487c2bc57a69c11626ae725128c63c896f6e72e197
~ __cg_jpeg_stdio_src : sha256 2eba343ea4ee4296b099b693dc6691a029aa742dac988d5b17b8fdf420ba1488 -> 0af9f6d43e2f490bfdb1f897347e6ed1ff218d37598956335327ea118cc57518
~ _fill_input_buffer : sha256 cf55c7879f4f5ace3676b555119156df7ddb8d2774d8aeda0f998b11caec6c61 -> d51ea6fc8901443c9e0bf46bcc126688a90fcb72de85e2f5f8e6149638779832
~ _jpeg_mem_src : sha256 2db6a9d20813d9bd309b0e60f64efe97aadbe71689dfdabf633520ed13b21190 -> c89993d820801e3dde613ea9fc49205128b3a99de391234c5129a616076c5b3e
~ _fill_mem_input_buffer : sha256 19f4153186dd5c779a60b5710d287e38a5b2820ef997f640e81a74740ffbe18e -> 5a392f8d4d06cbc16fe32c52373ba74de1cd8decdc5152d2058b7ebe5afa8596
~ _jinit_arith_decoder : sha256 0151113cbe0f7bc72c9c1f7e09b9f6a65a235548b0680c45edf2ff53bae6fafb -> 40e86fee6323c33712882e5d48999a5104d5d22c90db2b31ae460f74b1d717e3
~ _start_pass : sha256 3c0fd4d61974338fc649a13d645751e2145c4d1571e694d03698c35404295d2c -> cdaebdb802470c4181c162500e8d10da26a7a1c3094942b8c5d036304521e97f
~ _decode_mcu_DC_first : 620 -> 616
~ _decode_mcu_AC_first : 568 -> 544
~ _decode_mcu_DC_refine : 176 -> 172
~ _decode_mcu_AC_refine : 468 -> 448
~ _decode_mcu : 1012 -> 992
~ _process_restart : 280 -> 276
~ _arith_decode : 356 -> 352
~ __cg_jpeg_idct_ifast : 1044 -> 1068
~ __cg_jinit_forward_dct : sha256 b56974111992160bbe69adda5aabe0b4f4d13f16da3361a692cc0c4c270cbd27 -> 0dba143132c917fcce5c07c8ebf070c4ce8ba722524be46713ec513d76bfb7ea
~ _start_pass_fdctmgr : 1856 -> 1844
~ _forward_DCT : 324 -> 316
~ _forward_DCT_float : 336 -> 340
~ __cg_jinit_color_deconverter : 1216 -> 1236
~ _grayscale_convert : sha256 d73ce145624269b2a6069965671a404465349f3c2c46aea8065094d2b77bddf5 -> 38d45361ff93e85259e4f7a56c14f7488f5ba498e73092198fba8c21748c668a
~ _rgb_gray_convert : 140 -> 148
~ _rgb1_gray_convert : 156 -> 168
~ _gray_rgb_convert : 88 -> 100
~ _ycc_rgb_convert : 192 -> 184
~ _build_ycc_rgb_table : 280 -> 268
~ _rgb_convert : 104 -> 112
~ _rgb1_rgb_convert : 120 -> 128
~ _ycck_cmyk_convert : sha256 d002ed45f0c69217699ff603bed4790f4d85932fdbb93ed77372c18ddac55719 -> 4056a577f2fae8fb880d4bf0d0ae4ca1f635a96126e3b2b24bcd5bdf19146aa6
~ __cg_switch_color_deconverter : sha256 4cf80667338064408cf37f6879d497317f3d35851058f159e0fec4793c52c578 -> 1ba69531fc6c1a41aa9adc7e18d65f1c944f7f735a9b439510c73d924ceeb4f2
~ __cg_jinit_c_coef_controller : sha256 d378fbadcd170ca54f3cb7d407492c21b9a2845c00cbfa5fe2798c3aaba46e14 -> 30e8aa56913757c1059929e80d79ba887e898acdcb9f0e7a87362a8ab193c735
~ _start_pass_coef : sha256 5d4ce2c723271bbf791b6abaa9ae51779e91b1ab40c7d5130f1f7f1b7f73ea34 -> 76ccb07a0d50f4e3d7d2de4d2b0b9088a1cbfad01d247677ed0818faf1aab62a
~ _compress_data : 692 -> 704
~ _compress_first_pass : 612 -> 640
~ _compress_output : 488 -> 484
~ __cg_jcopy_sample_rows : sha256 27569118a3b4539a2e8f4143ee61fd4c993c7dbe9fe0e528c5d0bc0a81de505f -> 92f1c809d2a825f63b94479590878fa7e8a2303730d7ca5993756c889a333da4
~ __cg_jcopy_block_row : sha256 15b3210c6d86e2c69aab356e8da0da32d0c1799fff0c48ff336f8f563ad866a6 -> 6117057814dc65b6c035cdba04dc54ec09f24783f8d3cc44e2fee253c23c8d81
~ __cg_jinit_c_main_controller : 248 -> 240
~ _start_pass_main : sha256 03613d88e05ee129e06617f6fdb3cb5948dbbd09ec8de449d10a0a8a55a39ff5 -> aaf9fffa5b39809eeefd945a8007b4cade6840c4255e0c7159112072902e628e
~ __cg_jinit_c_prep_controller : 568 -> 560
~ _pre_process_context : sha256 fa1cb0e91c21a5e4df3de7ec1345c9334cad0e110b317bb09e9a1b7f9215b2f5 -> d44dacd4600152344890d55503f4b3663faeccbd227191ff3c8320ce5f7dfcd8
~ _pre_process_data : sha256 d41a01046938bdcc714369bcff39c102799a0092a5e7df1eaa2cb8e351cb939e -> 08811bf6967b65524b3beda347825cff04cc277a35cf8621ed6f705122626f13
~ __cg_jpeg_CreateDecompress : sha256 12f42256ade94ffbcae8430506eca30d080e8dd4060d8b8619cf31e892c1b49e -> 0daf3fd5bec01c0e31ea0f4c87185a53623e16b6eb531a7dc3c054ce715dfcf6
~ __cg_jpeg_destroy_decompress : sha256 d1dc794938427c618d6bea97098d28dd734308b348c37bccfbbafe8de4b6ef56 -> bdef0dd23b2232eace08d50f5bc6fbbc0ef55e6fec2c5759aeec17902f83a476
~ __cg_jpeg_abort_decompress : sha256 e93567c5ab131e192edd2b15d166a02b628790cce711462b603e2e58410b6c6f -> da43045c3fb40153b84c89c4501b6113df37c25100a1cc7d133b2698b3ba6ac3
~ __cg_jpeg_read_header : sha256 36b9516d06a7f4f85c8c3f66e093d9c3b51732be4b417a874cb5dff454262d65 -> 647a8cc8b5af85b846fb8ad7e0979e6ad4827087205f87da4c5aefbcd55cbc68
~ __cg_jpeg_consume_input : sha256 0888e1c3afdb3800c4508654cdc31d44fa53cfbfa868c905aa45af6b9142fd94 -> 9b3a665d22744cd77b36cf0c021e540f7f3031a64557cad30d487ff9df5fea82
~ __cg_jpeg_finish_decompress : sha256 449cb774a6704bc407ea48602172f5f28178da3d9be2c0f20e292f9d88113fb1 -> ccaa0923cc81339b0d2d188bc705b749859876c0a4b6ee157c381d52aade168b
~ _jpeg_core_output_dimensions : 1112 -> 1108
~ __cg_jinit_input_controller : sha256 cefd65ea8ba39282313310b43a4cb38665504569937167b6671f641b221b0ff8 -> d4f21f8a271da46d065166c4f266947ad23e86696d17a11764d6cb868404a237
~ _consume_markers : 1452 -> 1444
~ _reset_input_controller : sha256 3cf6c8d6af47a51e38cffda6c80dbf69622d07b14afa1f9185f4de38e212d1f2 -> d8d13395267db50a476c4a4ad4ca2374acea9ee99e01c749dcd6f0934a85e3ad
~ _start_input_pass : 660 -> 668
~ _finish_input_pass : sha256 46710f95e6474c6f8d835999440bbe0d1b6c8538ab1baabbe19c6e28007b8577 -> d2694370ce40f07a97d98c9d3d13395684634ece5091556b867aab4e6b881bee
~ __cg_jpeg_idct_islow : 1184 -> 1204
~ _jpeg_idct_7x7 : 880 -> 896
~ _jpeg_idct_6x6 : 604 -> 616
~ _jpeg_idct_5x5 : 552 -> 560
~ __cg_jpeg_idct_4x4 : 432 -> 440
~ _jpeg_idct_3x3 : 360 -> 368
~ _jpeg_idct_9x9 : 972 -> 984
~ _jpeg_idct_10x10 : 1040 -> 1044
~ _jpeg_idct_11x11 : 1264 -> 1268
~ _jpeg_idct_12x12 : 1192 -> 1196
~ _jpeg_idct_13x13 : 1436 -> 1448
~ _jpeg_idct_14x14 : 1332 -> 1336
~ _jpeg_idct_15x15 : 1452 -> 1456
~ _jpeg_idct_16x16 : 1624 -> 1628
~ _jpeg_idct_16x8 : 1424 -> 1436
~ _jpeg_idct_14x7 : 1108 -> 1112
~ _jpeg_idct_12x6 : 888 -> 892
~ _jpeg_idct_10x5 : 788 -> 792
~ _jpeg_idct_8x4 : 680 -> 684
~ _jpeg_idct_6x3 : 468 -> 496
~ _jpeg_idct_4x2 : 344 -> 340
~ _jpeg_idct_8x16 : 1292 -> 1296
~ _jpeg_idct_7x14 : 1100 -> 1116
~ _jpeg_idct_6x12 : 908 -> 920
~ _jpeg_idct_5x10 : 812 -> 820
~ _jpeg_idct_4x8 : 856 -> 872
~ _jpeg_idct_3x6 : 500 -> 508
~ _jpeg_idct_2x4 : 336 -> 344
~ __cg_jpeg_start_compress : sha256 81d7191dc19554b37ab6938f98053b9a328240dbbb3f960bef14fd820398b3e8 -> 10fe7070cdfb4c391c0c2e5ea309cd968d2592257bfd7b5b184a2863a6e39d30
~ __cg_jpeg_add_quant_table : 780 -> 784
~ _jpeg_default_qtables : sha256 549e1a24a084a9a6b11e243078edfa0592619d97bec10f8cb60416e2631b97fa -> 49d1f104251b01dc3f81e41003d032c05ec332296701f2df7a185aa70d540c80
~ __cg_jpeg_set_linear_quality : sha256 eda6d555021de9670ea36b6df222480e858fd7c91a60e371123330c28b48cae4 -> f1258ff9bc61c8a5030e3a6ac1b901d2585be623eab2e79cec1625daf8015b5e
~ __cg_jpeg_set_quality : sha256 3433183d8862bc0bda028d1114207397e887961fa32eabbf4f6440185ab4d9bb -> bfb627553dc071a5ce2641e5788f9e2a084971da19d71b28a06f04eb70bb0b89
~ __cg_jpeg_set_defaults : sha256 1fc363d3614c3ceeb47d2debbec492b5d782aeb402d6027b606ef3bb851d28cd -> 6fb9a5cfb100b25166b289ab09a1659cccbad43949e8f64d759a420cdfed57fe
~ __cg_jpeg_set_colorspace : 948 -> 952
~ __cg_jpeg_simple_progression : sha256 25902ded656e36968adfd3c6dae31b7006ea22d8cc4cdd32515d57e8ef217259 -> fb20353c5f6fdc671b5f6b8b4e21add1c276346ca143acdd855adb293cf5bd76
~ _fill_dc_scans : 108 -> 104
~ __cg_jinit_d_coef_controller : 448 -> 444
~ _start_input_pass : sha256 5993a0b49247513cfd7d5330c95d985af6e77cc95b674cbf89b7b2d65eff9518 -> 2a183417d57c4b70b50b3502bacfc98265bbfa05a4315a408880d65d885b1552
~ _start_output_pass : 320 -> 304
~ _consume_data : 524 -> 520
~ _decompress_onepass : 676 -> 688
~ _decompress_smooth_data : 1556 -> 1576
~ __cg_jinit_c_master_control : 2612 -> 2620
~ _prepare_for_pass : sha256 0920e04b088a6af4a975161a3320e4f0db6e0e50b62c6c2c97c15e26ebb1dfe4 -> d6e688050563d59b3e45a9d55c6fa8db8e6ad7dbe7857aba980ad94f30c7ad94
~ _select_scan_parameters : 272 -> 292
~ _per_scan_setup : sha256 dfc6d8324f716d745f823e81492e9f9953dde7665642310a21f03e6418a238bb -> b165e72373b4007260585b2dcfb78b0638efeab3a67bb6555b73227a0f6d63cc
~ __cg_jpeg_calc_output_dimensions : sha256 e33f305aaeb8dca8b197c49272f359d14024c74a9b4278e495aff7afb21da32b -> 2210515e0ab4c18880da4ce79c60b14f1ba4cb777d32d60837f2846dec4f4164
~ __cg_jinit_master_decompress : sha256 773322c522b46b95b0400ff8db741b06aedee20bfed7e2c70cbd1b76ccca342f -> d475ee3c0472068d06c074119bb0efe6c53d57c85f27616f6680425c96c76c75
~ __cg_jinit_d_main_controller : 472 -> 456
~ _start_pass_main : sha256 0af45c14879a3dba1a219b941cf589469e07f54ebecff82dfbc8b78935e70ca6 -> bad311efa9436514f504fe75d50bf9175ee83fe24a12af6fb4014da672c659f6
~ _process_data_context_main : 728 -> 712
~ __cg_jinit_upsampler : 524 -> 516
~ _sep_upsample : sha256 f6a4ab3bdd55f0b0c34715a78d8912efaac9fbb80ecafed1ad9ca60e15feffcd -> 5a6fd593283aaba3bb7e96b95228e1ac31189129f9d017257c510a35b555114d
~ _h2v2_upsample : sha256 939a6b018b428e2f299827111c1d37b3db07215314459a0caa839ba5dd0dc06c -> 8508a45b32725bccacd259b6b02c5ad8ec76629332f743437bfbbc1af60d5d80
~ _int_upsample : sha256 e8f6a699a134859eae4daff925569bf9701efc3773c4a47aebca2b88feeb2841 -> a82e30f78286921e3cf967a48d0114e1f7acdb0dc7e8bdd5522dcb53a939120d
~ __cg_jinit_d_post_controller : sha256 27b99e181c998a63d4c61bdcf90901d237bd54e6ff1f633cbf9bc4c0deb805a6 -> 06fe3112aa83d181cbf6f1056bb9f6ff7314480e3d84fa7c64fd10a244404575
~ _start_pass_dpost : sha256 5788c86d86b612e9581e57d99d7e776f9c82e300b7842927e3d4e40b372e0daa -> d1063d9ea7d4f19d4317b94d0785c70f297d22d12bae10da4ad37cf040e7df08
~ __cg_jpeg_read_coefficients : sha256 8d3fad2d6c3d8b2dc9e0ca233e67a81b9d6e2ce2698ab8c8ee49b45c5fc5d53a -> b1ece9a38ad937e8e94bf7d3b249d63b9ff7b1ecda81e28ef2f073fe4ea06034
~ __cg_jpeg_idct_float : 936 -> 948
~ __cg_jpeg_fdct_islow : 728 -> 732
~ _jpeg_fdct_7x7 : 744 -> 748
~ _jpeg_fdct_6x6 : 472 -> 476
~ _jpeg_fdct_5x5 : 424 -> 428
~ _jpeg_fdct_4x4 : 456 -> 460
~ _jpeg_fdct_3x3 : 256 -> 260
~ _jpeg_fdct_9x9 : 848 -> 844
~ _jpeg_fdct_10x10 : 956 -> 960
~ _jpeg_fdct_11x11 : 1240 -> 1244
~ _jpeg_fdct_12x12 : 1092 -> 1096
~ _jpeg_fdct_13x13 : 1408 -> 1412
~ _jpeg_fdct_14x14 : 1232 -> 1236
~ _jpeg_fdct_15x15 : 1332 -> 1336
~ _jpeg_fdct_16x16 : 1484 -> 1496
~ _jpeg_fdct_16x8 : 1032 -> 1036
~ _jpeg_fdct_14x7 : 920 -> 924
~ _jpeg_fdct_12x6 : 740 -> 752
~ _jpeg_fdct_10x5 : 640 -> 644
~ _jpeg_fdct_8x4 : 704 -> 720
~ _jpeg_fdct_6x3 : 360 -> 364
~ _jpeg_fdct_8x16 : 1196 -> 1208
~ _jpeg_fdct_7x14 : 1064 -> 1068
~ _jpeg_fdct_6x12 : 884 -> 888
~ _jpeg_fdct_5x10 : 788 -> 792
~ _jpeg_fdct_4x8 : 572 -> 576
~ _jpeg_fdct_3x6 : 376 -> 380
~ _jpeg_fdct_2x4 : 232 -> 236
~ __cg_jpeg_CreateCompress : sha256 7d93be75c0247455191684fc1352fe9a662e21bf890d46880a0965595ebabefe -> f3c6e509f5944b5481fa63c97690e460869213ac371b3de21f39941582ad4041
~ __cg_jpeg_destroy_compress : sha256 ea1f3c00403a0f26683409e672164b44a76c34a671ff063f792fdcf3901d0311 -> 0cc0a353daae84b7e75e1a689f1a593974993efe601f7744fea7f0086c06fd34
~ __cg_jpeg_abort_compress : sha256 88ba6c16c51e33dad9c2aaa13e141a7aa45731559bac882602e3b2d95e9e710c -> 9b524b4bc4e886fc4ae1fa2c04bef7b5802165a476ed0c16ebec1d4233b33ed5
~ __cg_jpeg_suppress_tables : 84 -> 92
~ __cg_jpeg_finish_compress : sha256 b8810c486d5b610d64df98196972d64a20f0410d6ec04c59cbecb31999482360 -> dd6d5c63ae955040079f250e325e3a8130d56f4653b2d0190926ee685987ac4c
~ __cg_jpeg_write_tables : sha256 a3bc554ca478ee2329658e00e2c57a2554361639ab78bec53ea7dbe979b6ac9e -> 5d93a80a63ac3de6cb440d382134c74f703bf7ae2c20b8985af6647aab742767
~ __cg_jinit_downsampler : 592 -> 608
~ _sep_downsample : 180 -> 176
~ _fullsize_smooth_downsample : 424 -> 428
~ _fullsize_downsample : 140 -> 156
~ _h2v1_downsample : 228 -> 232
~ _h2v2_smooth_downsample : 676 -> 648
~ _h2v2_downsample : 260 -> 272
~ _int_downsample : 328 -> 332
~ __cg_jpeg_std_error : sha256 b4c8dcac48d808148f4ada237de8e12241de5a4506324ef99e11814dea35c37a -> 6ae605034c7478b1ab40a3c0cfb83174da08732cd61abf70af2c8efe7af05389
~ _output_message : sha256 d0d99dcf6def053dbf3eab7b8991ebb2891467542817d84bc34aab2ff929048f -> 3877055b01855a9da5d43e15f09c38979167c0a55e3c27354290049eca013e23
~ _format_message : sha256 6d2398815b29e6688c156f00ee5e05220db8dda30944d1df503beefc90f76ab3 -> d15d8f51299e79eda3132cdd67e254c614581c9b81a10a3df2688ea3a8da1733
~ __cg_jinit_merged_upsampler : 612 -> 588
~ _merged_2v_upsample : sha256 000708464423843d9ef162a96cbf0337b3ecf0504b819e0119f135ce6ea4cc65 -> 6e4d50c230849b787ab8cef808a2115ccf11c3cf700785483918415d3a11cc40
~ _h2v2_merged_upsample : 492 -> 436
~ _h2v1_merged_upsample : 316 -> 284
~ __cg_jinit_huff_decoder : sha256 16a5ee5614d973d060b06eaa123ef39de091ce94a4fc66b3e109f5a7f70723b2 -> 6dbf3724ffd656a21e9b969220d04c0373227080de9191946aa98f77c90de932
~ _start_pass_huff_decoder : 1576 -> 1548
~ _decode_mcu_DC_first : 560 -> 552
~ _decode_mcu_AC_first : 612 -> 604
~ _decode_mcu_DC_refine : 276 -> 272
~ _decode_mcu_AC_refine : 1148 -> 1168
~ _jpeg_make_d_derived_tbl : 856 -> 840
~ _decode_mcu_sub : 1120 -> 1104
~ _decode_mcu : 1104 -> 1088
~ _process_restart : 156 -> 152
~ _jpeg_huff_decode : 316 -> 300
~ __cg_jpeg_fdct_ifast : 568 -> 592
~ __cg_jpeg_write_coefficients : 452 -> 460
~ __cg_jpeg_copy_critical_parameters : sha256 b507436b52ec52f2500ee75b5dab9b853ec1db39fcec48b654276815c33d0fe6 -> 1e7a2381be80d42935e94c101944802c3369a9bcdd6def8425432ba5c5cf3bac
~ _start_pass_coef : sha256 870aadc57f156c49bca1331d6bdb4f04dab48774a9982db3f174f9a8016fdd3d -> 51f47fa939caa0ce4690336ccb2b656d7a21ae7f58375c4c7b1bce84032f2dba
~ _compress_output : 636 -> 632
~ __cg_jinit_marker_writer : sha256 be1944c74c9218f533560b1bd958f78b6ee0a5f6d72f9590d29e49e31056dee1 -> 601d9d0da9cd0081f125ce7dcb2bb62add7b15ef5d77f79988d77a9fb0fff625
~ _write_file_header : sha256 3fb02abfab8e534574661c59ce5b71e55ae2e1a15709a407300e344773333480 -> f262a228bace46c03f8301495f9b7521322461cb949eb69b53c0e81970ee6f3b
~ _write_frame_header : 876 -> 872
~ _write_scan_header : 864 -> 872
~ _write_file_trailer : sha256 5d101b6bb30999d56f5ff9cf14f6a852b26c31f8243cc4a10d62b8ff2f2fa992 -> 648c6b532b79bd404f2a78fb07b02ff69148c74e4a579f4df78c05bf2dab11fa
~ _write_tables_only : 212 -> 216
~ _emit_dqt : 324 -> 336
~ _emit_sof : sha256 c5cdb70ef0d2c0da30a18ae2c605f4753ae3369ee6a71c02404595d4bd2242b2 -> 29f3aa76ee8896e89583ce5edaba95e49903f3b6dcfab83d960fcfc0aefeab0d
~ _emit_dht : 280 -> 284
~ __cg_jpeg_start_decompress : sha256 77fa122a96e2644042d659a37f5c7e3462149bfe00a4d09df64e9ab393daa50b -> d664abc144575deb13cfa06ddce5c5d65822669b656e560393be66d48b6630ee
~ __cg_jinit_huff_encoder : sha256 660da78d50b084b319986b970590c7057a7eeadba69ed524f619f7dc75df386c -> 9104d25a043a9640becbc6bc1ba6750e5f44f72f3f2dc8c5961a9d035a020281
~ _start_pass_huff : 664 -> 668
~ _finish_pass_gather : 360 -> 356
~ _finish_pass_huff : sha256 034e4348eb888986b2507e544b40c1b0539622e63a0abc796c611d71c8ae8f9f -> bf309d76810b8baa9402423ed9c646c8f94f1fefbbe9b914278954f9bc70db98
~ _encode_mcu_DC_first : 844 -> 836
~ _encode_mcu_AC_first : sha256 bdadd0f1ff83b50bcf0ccccbef803ace81cb182a880eb8a6800193b8ae7e7af9 -> 1a8708a07f811b966223cd7ae24a561d93a7bbfd008485105abefeaa673cdb02
~ _encode_mcu_DC_refine : sha256 e1587c26d2fd8bf251c291fd895cf04b50cbddc104691bd5872f3d169a84b45a -> a737f9f16f520a1a1ade6bd0bd52a7d54885b11d914f9ffb7d7588687ae10d94
~ _encode_mcu_AC_refine : 1868 -> 1852
~ _encode_mcu_gather : 640 -> 636
~ _encode_mcu_huff : 2528 -> 2540
~ _jpeg_make_c_derived_tbl : 720 -> 708
~ _emit_eobrun : sha256 c4b5af048c91ec2603b53264a02f7a1df6587b828f01df992b34dfb38a5553db -> de239251bec354865142048f4472bbc39bdaf9be8e94962e440aed0c9b4e639f
~ _jpeg_gen_optimal_table : 1000 -> 944
~ _emit_restart_e : 368 -> 364
~ __cg_jinit_1pass_quantizer : 856 -> 868
~ _start_pass_1_quant : 608 -> 588
~ _create_colorindex : 312 -> 308
~ _alloc_fs_workspace : 128 -> 124
~ _color_quantize : 148 -> 152
~ _quantize_ord_dither : sha256 fbdf7e37f20eb92822c0a256aa9eb40cbf0f342679c626db438c7215a5d03fa4 -> 5acbba016448e0226956787e2e835c16c40111a11f69f56e26937ee6284e2730
~ _quantize_fs_dither : 472 -> 476
~ __cg_jpeg_fdct_float : 552 -> 568
~ __cg_jpeg_stdio_dest : sha256 2d9ae49b1a64a39b92bf4ffd69fbccfabb399afd1043a1c7ebb6ad13ba4200cc -> 718caa400ab251c56b41c31fbb0a2bf2de2b3ab4d58b7051e523946536cd17f4
~ _empty_output_buffer : sha256 ff6499657bc4c3025b030cb731619aa81529a37f8df4d636dcc889ef6b3774ee -> e87e389f0837dd4232f535d6d8784ef05906f69eb44ca1566c7631a8a87e32a3
~ _term_destination : sha256 fa76bbdaecadbb3d9d72b590f19e79be4fe36d958d600c1e139d3468df928a57 -> ea42b0a9c6b4ad523cf40497ed396cd24f8a57001901925b56fedbda92fe7c7b
~ _jpeg_mem_dest : sha256 7c90ba4d8fa443e9bff49721a6745033cf7967f42401b49cec6bd75575106906 -> 0c591747153268a1c3591f98c94096b7f3a3fad6dea2b222509f612cc3090a98
~ _empty_mem_output_buffer : sha256 6c34e116658d23f168a61086d07a8856b1f510e6e5099df1291f5287665be9b9 -> be58a6d145a1ce8371ecf1da910daf5a288824610220eb1cb804c65392d79f5e
~ __cg_jinit_memory_mgr : sha256 52882e021a1ee508d14c545f2eeb1ecf099578e22ae19582355ab99467452305 -> b80e30f6e6c13cf6a969e0f76f3090b06b94a322dde24919c6fe85f07ac99395
~ _alloc_small : sha256 bc1c2894d71fb585a5e78c1b5e1ebda067bbb2df76b8aff5c09d3ae9efae106f -> 255d0737650e9394c809436781a66c9ff9103dd213f8b4202da3dce82d82bb95
~ _alloc_large : sha256 5d2d828fffd79ddadbc9ec54c7d30a2d0749dde98e54e4de400a4e3bcefe1ffa -> c5a03164afe2fd0c6033b377bee0474f6c333efe0c972f327fca0921ae66028b
~ _realize_virt_arrays : sha256 d7bb8d9c07b09636ffca5f96c44fc1cd10b525ec757fa5213ee3dafc38d332cc -> 5738864fd9491b1b30a3ff25118d96b1b3144423ecc0a7135ade76749498142e
~ _access_virt_sarray : sha256 2c32b9f59f1a3c8181f72ee63a25c44cd00713eaed290eaba8432ecde6a30e2c -> 809035100d4d791c9c80bd568ad29c17493d677c7187eced9046c37e61f610ff
~ _access_virt_barray : sha256 36b2d4b83e0f89c6c012677eacf21f0483c8ef57cf82843ced56f88e32425ffb -> dca1924285eacb9c5fa7e3c82f98d3bc06664c198b926c27a7dadc8be43f05ac
~ _free_pool : sha256 b147559f36ec7a9a2e5a86dced717fa6dc4d7e31d1b51bebcd7ad7b53dcf9385 -> 790a5ea9fbc7e3d0c227c08d8c151e1c006a55da65cde2f4ae7ad38b7395fb10
~ _self_destruct : sha256 39856c641c7e7e31675e6d4e6c005d8faf8c81cd5d587cfd567da303bccfde43 -> 376ba19e8afc65da0f967a7517fe9d52023b99fffa042133349bb2ffb5294985
~ _error_exit : sha256 375b46b69c9e1cc3e5d5c1cf9762effd5a4c609d3192de2f41e6b14ce2d6350d -> 11cc7bfdb65d73003b9e362e3957dc053f7f524d8ba0e2d5eeb129abd626185b

```
