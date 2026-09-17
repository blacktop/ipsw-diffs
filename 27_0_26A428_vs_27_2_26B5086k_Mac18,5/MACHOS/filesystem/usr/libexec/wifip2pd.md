## wifip2pd

> `/usr/libexec/wifip2pd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_protos`
- `__TEXT.__objc_methname`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-875.79.0.0.0
-  __TEXT.__text: 0x5e9708
-  __TEXT.__auth_stubs: 0x4f90
+877.4.0.0.0
+  __TEXT.__text: 0x5eaef0
+  __TEXT.__auth_stubs: 0x4f10
   __TEXT.__objc_stubs: 0x47e0
   __TEXT.__objc_methlist: 0x1c2c
-  __TEXT.__const: 0x409f0
-  __TEXT.__cstring: 0xfb54
-  __TEXT.__swift5_typeref: 0xd5d7
+  __TEXT.__const: 0x40a40
+  __TEXT.__cstring: 0xfb3a
+  __TEXT.__swift5_typeref: 0xd5e9
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__oslogstring: 0x2379c
-  __TEXT.__constg_swiftt: 0x10688
-  __TEXT.__swift5_fieldmd: 0x16bd8
+  __TEXT.__oslogstring: 0x238dc
+  __TEXT.__constg_swiftt: 0x106b0
+  __TEXT.__swift5_fieldmd: 0x16be4
   __TEXT.__swift5_types: 0x130c
   __TEXT.__swift5_builtin: 0x175c
-  __TEXT.__swift5_reflstr: 0x14e99
+  __TEXT.__swift5_reflstr: 0x14e89
   __TEXT.__swift5_assocty: 0x2d78
   __TEXT.__swift5_proto: 0x3094
   __TEXT.__objc_methtype: 0x2367
   __TEXT.__swift5_protos: 0x108
-  __TEXT.__swift5_capture: 0x8408
+  __TEXT.__swift5_capture: 0x848c
   __TEXT.__objc_methname: 0xa505
   __TEXT.__objc_classname: 0x11f7
   __TEXT.__swift5_mpenum: 0x1b8
-  __TEXT.__swift_as_entry: 0x244
-  __TEXT.__swift_as_ret: 0x194
-  __TEXT.__swift_as_cont: 0x668
-  __TEXT.__unwind_info: 0x14b10
-  __TEXT.__eh_frame: 0x1eefc
-  __DATA_CONST.__const: 0x3a948
+  __TEXT.__swift_as_entry: 0x24c
+  __TEXT.__swift_as_ret: 0x1a0
+  __TEXT.__swift_as_cont: 0x67c
+  __TEXT.__unwind_info: 0x14ba0
+  __TEXT.__eh_frame: 0x1f014
+  __DATA_CONST.__const: 0x3aa38
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_protolist: 0x2f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x178
-  __DATA_CONST.__auth_got: 0x27d0
-  __DATA_CONST.__got: 0x1070
+  __DATA_CONST.__auth_got: 0x2790
+  __DATA_CONST.__got: 0x1078
   __DATA_CONST.__auth_ptr: 0x7a20
-  __DATA.__objc_const: 0xb0e0
+  __DATA.__objc_const: 0xb100
   __DATA.__objc_selrefs: 0x16f8
   __DATA.__objc_data: 0x1a70
-  __DATA.__data: 0x155d0
+  __DATA.__data: 0x155a0
   __DATA.__common: 0xbb8
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 25251
-  Symbols:   2284
-  CStrings:  5615
+  Functions: 25286
+  Symbols:   2275
+  CStrings:  5622
 
Symbols:
+ _$s7Network10NWEndpointO20customMetadataForKey3key10Foundation4DataVSgSS_tF
+ _$s7Network10NWEndpointO23setCustomMetadataForKey3key8metadataySS_10Foundation4DataVSgtF
+ _AWDLTrafficRegistrationServiceAirDrop
- _$s7Network10NWEndpointO9txtRecordAA11NWTXTRecordVSgvg
- _$s7Network11NWTXTRecordV5EntryO4data10Foundation4DataVSgvg
- _$s7Network11NWTXTRecordV5EntryOMa
- _$s7Network11NWTXTRecordV5EntryOMn
- _$s7Network11NWTXTRecordV8getEntry3forAC0D0OSgSS_tF
- _$s7Network11NWTXTRecordVMa
- _$s7Network11NWTXTRecordVMn
- _nw_endpoint_copy_txt_record
- _nw_endpoint_set_txt_record
- _nw_txt_record_create_dictionary
- _nw_txt_record_remove_key
- _nw_txt_record_set_key
CStrings:
+ "%s APPLE80211_M_DRIVER_AVAILABLE available: %d reason: %d"
+ "%s APPLE80211_M_DRIVER_AVAILABLE with powerOn false"
+ "544ec069bfb894bebdcdab9a71d7755405b8cda3501a01fe33133b62ecb09b2b"
+ "706751f8a84cb0b218d2eabedcff40d686ea2d8fc2ad8f602dbc3eb9554092fc"
+ "AWDL did wake"
+ "AWDL interface was re-created (system awake: %{bool}d)"
+ "AWDL will sleep"
+ "Ignoring assertion from %s because %s is not AirDrop"
+ "Infra did wake"
+ "Infra will sleep"
+ "NAN interface was re-created (system awake: %{bool}d)"
+ "Stamping system wake time during interface recovery (missed didWake)"
+ "WiFiP2P-877.4 Sep 04 2026 23:09:16"
+ "{\n  \"WiFiAwareAllowedBundleIds\": {\n    \"36ee6d7b08417afd3acc0cc7beaf3af1b1346dd6eb04c84811b63304593355bf\": {\n      \"WiFiAwareServices\": {\n        \"e81f9ceb63a2977426dc347bd6e37ba328124349be7e20b9ceb98c8d6b20bfc6\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"dfa02f422e2892b85d515fafde281b7ef039672276861da292649a383bb0f90d\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"cdd983b9bcdd52555ff637b7a173dd1dd4e59eb584469326be792b1b6b179076\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"f99ecc70d4d255415c861466edc66e004766fb4e43f994df1b363dc698c6c0da\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"7a879b5b690dcd2f9b961fa00ad264cec1865f9b9cb6eca93bab2faf9217a9ff\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"7a3000fd5a569c489b06366e4a3a25a48bb42e3d09f7718daf914105d69070b7\": {\n          \"Subscribable\": {},\n          \"Publishable\": {}\n        },\n        \"e4aff899b096175dc1f5c35ab86ec0441483c784836220d8358a8bee116336cd\": {\n          \"Subscribable\": {},\n          \"Publishable\": {}\n        },\n        \"c9d8c784c38611eb585a2790ccca3f2f9b9521e15421c8b188244417dd1ac38b\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"85a5bb9cc438ca2fe53c25e1cfc0de69d9329edddc98b7235fc90ec1e226ae48\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"580cec82c75cbc79d37cc9675d8cd10126d2dcf92e14a7c71eb3805876650506\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"2291751363b7f007d1075c572d070b75735590f1c75447b4c8b3b4ded1705869\": {\n      \"WiFiAwareServices\": {\n        \"f4dd858158d360c7e908810eff7c3d9ee5afe0737f5e6c7b6fa5b77ba50dad98\": {\n          \"Publishable\": {}\n        }\n      }\n    },\n    \"3f4c8cac102c85e3d666904392aa5585e889b0f54b64cfcdf473e2a56560597f\": {\n      \"WiFiAwareServices\": {\n        \"bbe5cf4af0c42a337aefaf58736cf172eece935a48f13238a7e60ccefba5125a\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"e6a7dec9e4e0a59570e0e7f17ceb59503f3021c38d95b0d754a5e7a82e5546dd\": {\n      \"WiFiAwareServices\": {\n        \"40ab558da12789c96b016270938b0741d1523fe7d93a98666dd72ee84e204561\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"a1a0d3ad2a6074b5a11423cb009ddf9609b79fe868a7525d61cf610d49af9e98\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"b55cc82ea618d785cab5d21792938e31cfb8f51c07f8644d512b13fd69d51cda\": {\n      \"WiFiAwareServices\": {\n        \"f4dd858158d360c7e908810eff7c3d9ee5afe0737f5e6c7b6fa5b77ba50dad98\": {\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"6cea4691698059994151a8e62f9fe6e95105c1986cdb9db7f26d005be1653a7a\": {\n      \"WiFiAwareServices\": {\n        \"bbe5cf4af0c42a337aefaf58736cf172eece935a48f13238a7e60ccefba5125a\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    }\n  }\n}"
+ "{\n  \"ac955292f1fc3526d63ae6824a0b3d9c487c7cb6d6917f45e8c0125cdfa9b714\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"ASKAdvertiser\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"61e0ec687786d16fcbd7cf4378b14e63bdf3e5aa14f23c57d018de825ff43fc0\": {\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"NoConsoleUser\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    }\n  },\n  \"b0cf0dd32f7135fd8a80aabae3b59f3f0cd4d4bd97d6da7ba99b751e475b78d3\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"macOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    }\n  },\n  \"66332b86bb8879cc0962a30e9f631bc9ea595b1943dc95a6281a481ccab17218\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"ASK\",\n        \"DDUI\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"4b312c8f098c68250e853fae87b94edf7e87139ac7db80d5f3eb960b829e4fd7\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Timeout\": 120,\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    }\n  },\n  \"29046320be6e1a6b4be8d0b3bf7464bc7470816a3bfb8cd274590d0b1efa6dbc\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"MARS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"07c90ff9edee43ebf5a00f7ecef8d9f86e10dc498a9b809ab75c82bb48b63433\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\"\n      ],\n      \"ClientID\": [\n        \"CLI\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    },\n    \"TDS\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    }\n  },\n  \"c145e06b4809f1fc819cae8c7345e0969d051578896bcc02edad6f7044ee63ab\": {\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"visionOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"visionOS\"\n      ]\n    }\n  },\n  \"73707623f5c9710b5af4dc2f7a8ea7fe8e5c1a58182e315700efb1a28b2ae1f6\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"Timeout\": 120\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    }\n  },\n  \"e636c7a2013628cf81c0d921e2bfa273f164e65395a7dd743be0790440648c3a\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Terminus\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    }\n  },\n  \"4e961305b2ba25ab6877df9910ab615a0eaf368a9ef80574d614605e3d99354f\": {\n    \"Publish\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    }\n  },\n  \"8755a396e40987b10fd05525d50dbb9599c84d154efa0512cf11015ca768d06b\": {\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"NoConsoleUser\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    }\n  },\n  \"00c4972f23e250d71e40cc2de0469660f2b64e6bb1f6ffc7704a75653851400f\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"Migration\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  }\n}"
+ "ℹ️ No %s configured for %s policy: %s"
- "2a6a0a3f270ba9686b12a572281cfd90c24b94418fcd4db62982e81d07c6af67"
- "6bfa90f74591db2b3105e863894d8607eb4f91c0a461cb8e8e4041b894d5c00e"
- "Driver interface was re-created"
- "RSSI: %s"
- "WiFiP2P-875.79 Aug 09 2026 21:08:29"
- "nan_event: %s APPLE80211_M_DRIVER_AVAILABLE with powerOn false %d"
- "setTXTRecordEntry failed: NWEndpoint(nw) returned nil, endpoint may be in inconsistent state"
- "{\n  \"1a126797a911afccc3a43ce660be8d0cbc9173a881f0eca11e3431d655b82cbc\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"ASKAdvertiser\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"80abff46fa2be03180da315886c6ce3e6a0ac8e4540e14547555978368f2090f\": {\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"NoConsoleUser\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    }\n  },\n  \"ba56b51cea61817d6a334731bb234d4a6ecce1297389ceb628aef01b8612931c\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"macOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    }\n  },\n  \"70aa9d8813ec2eb1c1a0e48de8642078b3dee92cc1bc25472ff223d791c9254e\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"ASK\",\n        \"DDUI\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"b8af5620b375ba6f52d79dd347355d2b7e7ccab9a404772c017cfa246a0b154a\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    }\n  },\n  \"53f0da3828b1696e5308b1d2d787d91a519080eee6fdf450cc44d6ebca4053f2\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"MARS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"b830adf0b9551a412b00eb86d3999b688f7af2023c56c8adeaf4322348c5d67e\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\"\n      ],\n      \"ClientID\": [\n        \"CLI\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    },\n    \"TDS\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    }\n  },\n  \"ad2799a9d7eaf3aa38020a9d21db4035f3cb5c49a322c75a6715de625cfe47ad\": {\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"visionOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"visionOS\"\n      ]\n    }\n  },\n  \"af52a72c514340c4d79588c55274ab2ca09b515fafa42d1643731957878358a3\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    }\n  },\n  \"3d2d1f86785b2707e28bb06d38b58371d61cda31a7f454f5604df70d546c77ec\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Terminus\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    }\n  },\n  \"c1131de229b7e54503a17a2563434ff76ed159e7fb4753f9bf28512eb2d42cc1\": {\n    \"Publish\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    }\n  },\n  \"9f7f98e4349d4aa606587a645088d4bfcda499b456bad533e33e514eac991e3c\": {\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"NoConsoleUser\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    }\n  },\n  \"01498cbc10f6fce00a01ad838100efeb26e3a2ec7d5fe762fd7ce3bcc98383d8\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"Migration\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  }\n}"
- "{\n  \"WiFiAwareAllowedBundleIds\": {\n    \"f432972c0c4a09387962f0ca3933a8757007e7f18c8ee0be97a5790ac19bb389\": {\n      \"WiFiAwareServices\": {\n        \"18adbf992c28c96a137aaf6eaed400db5379272335c4e48b59d08cdd83ab569f\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"fac83f871049560da4ae8737d36f1f3d7672f0fa0cd70aa6527f45e709c6c4fb\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"07003b39e54ffd9905632a55dce1c28a11b04816d44bc3b06b061b2e31f7be31\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"5e75dff2f7eca36d7679d4f702d5f003616020b63860ab21165232dc3400eccc\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"efa37ead08cb7ec9d9c24309bdb54540922fa06cdb9a16c5b407593d5c31c032\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"b4b009ad119ca05028a8d40c3c3f724c5717dd578db46ee59cde871b238940b0\": {\n          \"Subscribable\": {},\n          \"Publishable\": {}\n        },\n        \"e240877f00ddae093f4a67742c5ecf021efc553edb49582406a698ba3c6bd83f\": {\n          \"Subscribable\": {},\n          \"Publishable\": {}\n        },\n        \"6f54322abde24dc9d63eda848927085fa199e128ccbb2c508674e77ff3c0f446\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"57fa3d124a47e481a7b3040ec43d54b16fc791ca85c31f7dd09eef1c6329f579\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"7b2c62365cc2853feafd3fdfa18669a18e6347575ca09a66c3379dd26cc19ac4\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"21e3ff4e9cb8b2d65dfd837d283eeaf030b4a8f99a47e3a05a08cfd080adc517\": {\n      \"WiFiAwareServices\": {\n        \"ad9e96aabafcac714661cc3776bbf1fc150c402a9a628dbc4d5c38d139508e08\": {\n          \"Publishable\": {}\n        }\n      }\n    },\n    \"828bad7edbdef878563b55e994fa79a7139e037c1c3cbe2360f730fe7ccafa1c\": {\n      \"WiFiAwareServices\": {\n        \"6c75963a90574fcde4f90bb0f21ce80854aacdae39fc9e189904056cb7d0d737\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"79ec201d0dc94025f0751f3b2cc9368ae86cd6c9b72308416660aabc744256e2\": {\n      \"WiFiAwareServices\": {\n        \"7d13016e385bc7f3321342a91d02606129bc3352fec69a53c2deea5ee3165729\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"d7e12b1a699b294499c4c359f8ad5317986a782adbfea50724f3d8fbd5c9f227\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"36ec80e02798a984d49b5b655574878f02763179adbbb4aa712cf49daf88942f\": {\n      \"WiFiAwareServices\": {\n        \"ad9e96aabafcac714661cc3776bbf1fc150c402a9a628dbc4d5c38d139508e08\": {\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"eb73c9d9b5b4214fa369c8039530e845d4e7593ab6f172707411e360087e2da7\": {\n      \"WiFiAwareServices\": {\n        \"6c75963a90574fcde4f90bb0f21ce80854aacdae39fc9e189904056cb7d0d737\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    }\n  }\n}"
```
