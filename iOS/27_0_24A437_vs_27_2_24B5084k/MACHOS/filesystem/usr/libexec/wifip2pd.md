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
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-885.85.4.1.0
-  __TEXT.__text: 0x5c59b0
-  __TEXT.__auth_stubs: 0x5240
+887.6.0.0.0
+  __TEXT.__text: 0x5c70f8
+  __TEXT.__auth_stubs: 0x51c0
   __TEXT.__objc_stubs: 0x4720
   __TEXT.__objc_methlist: 0x1bf4
-  __TEXT.__const: 0x404b0
-  __TEXT.__swift5_typeref: 0xd367
+  __TEXT.__const: 0x404f0
+  __TEXT.__swift5_typeref: 0xd379
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0xfa28
-  __TEXT.__oslogstring: 0x226bc
-  __TEXT.__constg_swiftt: 0x103f4
-  __TEXT.__swift5_fieldmd: 0x169d8
+  __TEXT.__cstring: 0xfa0a
+  __TEXT.__oslogstring: 0x227ec
+  __TEXT.__constg_swiftt: 0x1041c
+  __TEXT.__swift5_fieldmd: 0x169e4
   __TEXT.__swift5_types: 0x12e0
   __TEXT.__swift5_builtin: 0x1748
-  __TEXT.__swift5_reflstr: 0x14bd9
+  __TEXT.__swift5_reflstr: 0x14bc9
   __TEXT.__swift5_assocty: 0x2d78
   __TEXT.__swift5_proto: 0x3074
   __TEXT.__objc_classname: 0x10f7
   __TEXT.__objc_methtype: 0x2347
   __TEXT.__swift5_protos: 0x108
-  __TEXT.__swift5_capture: 0x7fc8
+  __TEXT.__swift5_capture: 0x804c
   __TEXT.__objc_methname: 0xa305
   __TEXT.__swift5_mpenum: 0x1a8
-  __TEXT.__swift_as_entry: 0x204
-  __TEXT.__swift_as_ret: 0x168
-  __TEXT.__swift_as_cont: 0x5f4
-  __TEXT.__unwind_info: 0x145d8
-  __TEXT.__eh_frame: 0x1e6ac
-  __DATA_CONST.__const: 0x39f28
+  __TEXT.__swift_as_entry: 0x20c
+  __TEXT.__swift_as_ret: 0x174
+  __TEXT.__swift_as_cont: 0x608
+  __TEXT.__unwind_info: 0x14660
+  __TEXT.__eh_frame: 0x1e794
+  __DATA_CONST.__const: 0x3a018
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_protolist: 0x2f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x178
-  __DATA_CONST.__auth_got: 0x2928
+  __DATA_CONST.__auth_got: 0x28e8
   __DATA_CONST.__got: 0x1030
   __DATA_CONST.__auth_ptr: 0x7950
-  __DATA.__objc_const: 0xac90
+  __DATA.__objc_const: 0xacb0
   __DATA.__objc_selrefs: 0x16e0
   __DATA.__objc_data: 0x1920
-  __DATA.__data: 0x15068
+  __DATA.__data: 0x15098
   __DATA.__common: 0xb88
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 24922
-  Symbols:   2319
-  CStrings:  5523
+  Functions: 25001
+  Symbols:   2309
+  CStrings:  5530
 
Symbols:
+ _$s7Network10NWEndpointO20customMetadataForKey3key10Foundation4DataVSgSS_tF
+ _$s7Network10NWEndpointO23setCustomMetadataForKey3key8metadataySS_10Foundation4DataVSgtF
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
+ "49cde6f659b255ce6d2294e4c8373b2240e63115a0431ad66c9844dba77f0d20"
+ "8f60cfbe2a54693e188718e10b5d765f708d18953fbda0654a0bb07ec5cdde0f"
+ "AWDL did wake"
+ "AWDL interface was re-created (system awake: %{bool}d)"
+ "AWDL will sleep"
+ "Infra did wake"
+ "Infra will sleep"
+ "NAN interface was re-created (system awake: %{bool}d)"
+ "Stamping system wake time during interface recovery (missed didWake)"
+ "WiFiP2P-887.6 Sep 04 2026 21:09:02"
+ "dynamicSDB clearing switch on termination (%s)"
+ "{\n  \"WiFiAwareAllowedBundleIds\": {\n    \"7a5450e11887f22117ee547cb251d56c4b6cc675dcd9c50dac10147e246ba07f\": {\n      \"WiFiAwareServices\": {\n        \"dcdb1d117f8ddbd9fea4007621ed0ebde027982d8808f689d0135ee69871e05d\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"f1db6211d4fb0425c91785810b2dd41bc6ae4f93f10fbba2dcf2f581ad8fbfe0\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"e516992aea1e93280f0d44e55a488cfe9f3bde31af8fd46cd7d854ea39dd7e8a\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"11958a31c1ca4a5526b13e92792bcdcfc0810fb230fa83970d29e23062e28a86\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"a82138f0920b81a2f6253393898fd822ce878c93cbb63cd2987961fb7b7054ed\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"14ab72d82ece4707d65a21318bd8cc719b3139d8bed691098dec550ea0655e91\": {\n          \"Subscribable\": {},\n          \"Publishable\": {}\n        },\n        \"0f2a639a8b640707ab965caa40eda73f81d447220f6d683452ad2276f728baaa\": {\n          \"Subscribable\": {},\n          \"Publishable\": {}\n        },\n        \"f8b69cb94dd60037117f812062fc6703663a3a115838565b217b6e7acd7c0070\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"82be5c97f5ec9e1cb9f8691d04ea46a037b560000102d74a8633e960cecb7f14\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"b2b6333bf3787a57dec9bb375b3299ca1d4525370cba58dbb1c681b88757bef1\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"9eccbf08b270517731fedab210fb15cbbbaf5865480142dd8bd43177ae71103f\": {\n      \"WiFiAwareServices\": {\n        \"d4622be90f6e9fe4daa71143e3122f34473504c0b79df25ce8591fa82696ac34\": {\n          \"Publishable\": {}\n        }\n      }\n    },\n    \"d998ad8a7f85b29c9fa545632b386ec4b9ed942ba5dd1a8af355502def8f3c93\": {\n      \"WiFiAwareServices\": {\n        \"c19eb0c249c5d7ccf385b511432290917e9ebc135f0186741159625edb7bf2a1\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"31a7368535d00f55bf8d192a27f63b7ca8212f16f5e51ffe2b4237794998555c\": {\n      \"WiFiAwareServices\": {\n        \"2a5d6f47134df6f529dfeaac040ab63617feb7586e16221ebfbc327ef7ce3538\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"ebcf9df7e28229cf5363f3ab8ec07c93079b9e0bc1f7bfff98bcd675910e07dc\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"8d4e5c095a5a98b3922174e4d3be228d4931ee779411c3f653ee44dda6995518\": {\n      \"WiFiAwareServices\": {\n        \"d4622be90f6e9fe4daa71143e3122f34473504c0b79df25ce8591fa82696ac34\": {\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"12aa047affe526249a694e82d514095828c5fcc99b4d43e5532fbf3c2c6ab8a2\": {\n      \"WiFiAwareServices\": {\n        \"c19eb0c249c5d7ccf385b511432290917e9ebc135f0186741159625edb7bf2a1\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    }\n  }\n}"
+ "{\n  \"dd04904b326fd5f164a81e598740b1ee2dce4d6cc9d77a1d2e979532d819739b\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"ASKAdvertiser\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"4f361c781228ca0f94b55e0a5667fc118174e56b2a5475e5f2868e22969fbf30\": {\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"NoConsoleUser\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    }\n  },\n  \"8be2b0ac251b250495fde0d9cfde180f294063ec65dbbc4f2e22b093fbb655f3\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"macOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    }\n  },\n  \"8cb0afaf8f2eead74cba804e94a9d1b97ba0a05c7bf811b4e84a24f4574b7605\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"ASK\",\n        \"DDUI\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"d25a4bd60e9dec452a91a77be8e8e9ee51b1b89519b06850b43f3e3ca18962e9\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Timeout\": 120,\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    }\n  },\n  \"a1d369c50bb724e2d2cb42af2298d6cbfc1ced2e0d6489294c97c457030741ec\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"MARS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"08e1f68cbf19f40c92ee7ac29fd0905d18eace6d973758b9ecd68b3a2fd6059e\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\"\n      ],\n      \"ClientID\": [\n        \"CLI\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    },\n    \"TDS\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    }\n  },\n  \"298e3a7b9a0cb1fb2586d0853e5456c7d94382c16053d2987b7dffd3cb8702b0\": {\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"visionOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"visionOS\"\n      ]\n    }\n  },\n  \"46d6a315458c428e6389d026df54d7d88f91180949ecbefdf7601ac5d70fe0e9\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"Timeout\": 120\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    }\n  },\n  \"a45c9013da2a4af921dd957113538be6cb4f177ec626a0330e13ba7d317747ab\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Terminus\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    }\n  },\n  \"8ef4afc990168f7ebace0dc1e8e1cd8571aeff4873e78d59c490331b04ec50d5\": {\n    \"Publish\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    }\n  },\n  \"99e35371ad4922aaa3809027d7bc5f060351738f23fbede59d234d2ea40647ce\": {\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"NoConsoleUser\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    }\n  },\n  \"16b2feafa6b804303a73417755fb4a7958302d3e19e7b86a802c83f1fd822ca7\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"Migration\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  }\n}"
+ "ℹ️ No %s configured for %s policy: %s"
- "Driver interface was re-created"
- "RSSI: %s"
- "WiFiP2P-885.85.4.1 Aug 27 2026 21:08:49"
- "beb5bbeacae2e7601fa040dd9533a422302764311bcbdf65e7c66b172785757d"
- "fe7dcb203b592cc5872ac0f998060beb426c6927743ec23ea1e6201863b9961b"
- "nan_event: %s APPLE80211_M_DRIVER_AVAILABLE with powerOn false %d"
- "setTXTRecordEntry failed: NWEndpoint(nw) returned nil, endpoint may be in inconsistent state"
- "{\n  \"30557c6e7d6cf96b8d236eba792a41ea9824398b0965a9615e35ea4cebc4a926\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"ASKAdvertiser\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"05e60f71a139a2dd80171a7c6289808f3433c41e5779920bc693c239e8e8fcae\": {\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"NoConsoleUser\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    }\n  },\n  \"e930356c2f84aec85f7e064c6dc9194b16478638f2157e580a62ad61ca8a044d\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"macOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    }\n  },\n  \"3e8f97a723069257b34e53f215443de41e5b1fafb1ad0677d365599df8898642\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"ASK\",\n        \"DDUI\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"2007eadae2b184fe1498292dec7f1e8b6fc58d7ef92f9d2f6d90adce6dfb446c\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    }\n  },\n  \"5628131db0c7c2ca728d5275c2f240f7332205d5fe8c5f5b4a27481ed8c5fee1\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"MARS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"8c76e9951ff605e6d06ce8ad5d5b1b5700d20b458d7b54df085ff4af04cdf317\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\"\n      ],\n      \"ClientID\": [\n        \"CLI\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    },\n    \"TDS\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    }\n  },\n  \"a0bd0080d9c90fb41fd17fb5734f056c7c961df09585473dd0ad741e17de06e7\": {\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"visionOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"visionOS\"\n      ]\n    }\n  },\n  \"b107e2995d237e9825553d2655ac91b14e59834889c861f8942cec587884ea14\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    }\n  },\n  \"4653c2953c09a1e3ced716d24f2ff1fd98108e01c9ceff62ed89794368bba6dd\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Terminus\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    }\n  },\n  \"91750c183840feccadc8631af9bb369bf373adb5018455b83aff344c2de8d64a\": {\n    \"Publish\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    }\n  },\n  \"c0ab2d6af3ce00a81bdf2ddf9c52395be545f9821bbd9da05728600d5bc84cfb\": {\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"NoConsoleUser\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    }\n  },\n  \"037e2b6247d9d454b722ffd7e27c2260f5d3672cdc5a379232b773fd08e49832\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"Migration\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  }\n}"
- "{\n  \"WiFiAwareAllowedBundleIds\": {\n    \"91cd7759915509232e360cabca7633ec07404e3acbdcf7272dd491728a7a4c53\": {\n      \"WiFiAwareServices\": {\n        \"7bc973d56a6128c53ac46608f0119b5193dc9b9a736d2d6a4f19a8a592b289a3\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"1e3785289da5bac9433690cc3f42418b64b1eae2549f6dd5b6362f386f8038fb\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"c0eb541285f9fd5a20ce557ce7130b003bd22116269bd3169cce987503cfcadf\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"bfce27b6c360a2630e2cd6ce15c052ed9b524841e0c5a33a9124d76867ad432d\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"d0b9cfe0dd0e127951acdabb0ee09f39f905723e443193c145d0ef4e72b7794f\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"e4f76cd9471bfba826a1c17a1148f362cdb6964632e3695d0029145d992b0fca\": {\n          \"Subscribable\": {},\n          \"Publishable\": {}\n        },\n        \"4674896810b15317e0714bea6e27f639c2973eb8aa99d4bf83c78149be4f57fa\": {\n          \"Subscribable\": {},\n          \"Publishable\": {}\n        },\n        \"7c09f3555e6a0c9dc08d2a2d3d552110e8503447e7ad06721f129cdb050a80a6\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"accc36d0c81e2c4f525bcddfc7e054c3286f08a304eae788f7d7b0543538468e\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"f0f532056abb4671d9529b19ae1d8cff750fd24727266f3038ae38d838c6da57\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"7e1248ac7fde9a19e4bf15e463692bbc6e27b77608e3a471e71b27235a65bf14\": {\n      \"WiFiAwareServices\": {\n        \"b89fdeb29bdc8ed1e834d7bb68236b525844c287b75e28b3257f99dcd1481477\": {\n          \"Publishable\": {}\n        }\n      }\n    },\n    \"48168a2d359ee71366067cfbef0ddc49a74bf19dbd3b981cf4874e366b44b4f7\": {\n      \"WiFiAwareServices\": {\n        \"0294779b5c45ef9017eff9d1ef58ca653dbf6a7ca340bd8a187f11af5b7c37d7\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"1e6582ec9d8b5145fbdc5f17abb3d29e0ec3925c7e4b6cdb040a398c9c09857a\": {\n      \"WiFiAwareServices\": {\n        \"a06d76c07f876c47e682b26939470e8c6986a35467f8c2926c974499e3bd49a0\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"e6ce45eab98c54bd750cee762541a20c82d79ab74844f07d1185b9c6186a8c9d\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"74385c22de75055333d5348e47da8a8db1ac467d2d084f401769bc1dd09d35fa\": {\n      \"WiFiAwareServices\": {\n        \"b89fdeb29bdc8ed1e834d7bb68236b525844c287b75e28b3257f99dcd1481477\": {\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"b5802bb529b7638fcba73528ac348ffe986f15ef851c397d79db0bac21b12982\": {\n      \"WiFiAwareServices\": {\n        \"0294779b5c45ef9017eff9d1ef58ca653dbf6a7ca340bd8a187f11af5b7c37d7\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    }\n  }\n}"
```
