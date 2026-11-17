## wifip2pd

> `/usr/libexec/wifip2pd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__cstring`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-889.2.0.0.0
-  __TEXT.__text: 0x5c7abc
-  __TEXT.__auth_stubs: 0x51d0
+889.6.0.0.0
+  __TEXT.__text: 0x5cb308
+  __TEXT.__auth_stubs: 0x51e0
   __TEXT.__objc_stubs: 0x4740
   __TEXT.__objc_methlist: 0x1bfc
-  __TEXT.__const: 0x40510
-  __TEXT.__swift5_typeref: 0xd389
+  __TEXT.__const: 0x404c0
+  __TEXT.__swift5_typeref: 0xd36d
   __TEXT.__swift5_entry: 0x8
   __TEXT.__cstring: 0xfa2a
-  __TEXT.__oslogstring: 0x227ec
-  __TEXT.__constg_swiftt: 0x1041c
-  __TEXT.__swift5_fieldmd: 0x169fc
+  __TEXT.__oslogstring: 0x22a6c
+  __TEXT.__constg_swiftt: 0x10444
+  __TEXT.__swift5_fieldmd: 0x16a14
   __TEXT.__swift5_types: 0x12e0
   __TEXT.__swift5_builtin: 0x1748
-  __TEXT.__swift5_reflstr: 0x14bf9
+  __TEXT.__swift5_reflstr: 0x14c59
   __TEXT.__swift5_assocty: 0x2d78
   __TEXT.__swift5_proto: 0x3074
   __TEXT.__objc_classname: 0x10f7
   __TEXT.__objc_methtype: 0x2347
   __TEXT.__swift5_protos: 0x108
-  __TEXT.__swift5_capture: 0x804c
-  __TEXT.__objc_methname: 0xa3a5
+  __TEXT.__swift5_capture: 0x8164
+  __TEXT.__objc_methname: 0xa3c5
   __TEXT.__swift5_mpenum: 0x1a8
   __TEXT.__swift_as_entry: 0x20c
   __TEXT.__swift_as_ret: 0x174
   __TEXT.__swift_as_cont: 0x608
-  __TEXT.__unwind_info: 0x146a8
-  __TEXT.__eh_frame: 0x1e8fc
-  __DATA_CONST.__const: 0x3a048
+  __TEXT.__unwind_info: 0x146f8
+  __TEXT.__eh_frame: 0x1e92c
+  __DATA_CONST.__const: 0x3a2c8
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_protolist: 0x2f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x178
-  __DATA_CONST.__auth_got: 0x28f0
+  __DATA_CONST.__auth_got: 0x28f8
   __DATA_CONST.__got: 0x1030
-  __DATA_CONST.__auth_ptr: 0x7950
-  __DATA.__objc_const: 0xacd8
+  __DATA_CONST.__auth_ptr: 0x7948
+  __DATA.__objc_const: 0xad18
   __DATA.__objc_selrefs: 0x16e8
   __DATA.__objc_data: 0x1920
-  __DATA.__data: 0x150a8
-  __DATA.__common: 0xba0
+  __DATA.__data: 0x15120
+  __DATA.__common: 0xbb0
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 24978
-  Symbols:   2310
-  CStrings:  5533
+  Functions: 25026
+  Symbols:   2311
+  CStrings:  5542
 
Symbols:
+ _objc_retain_x11
CStrings:
+ "#### Not Terminating datapath %hhu with %s. Referenced by other endpoint."
+ "#### Terminating datapath session %hhu with %s for Responder"
+ "%@: [BLOOM FILTER] FW Config: %s (WatchdogReset)"
+ "%s Terminated. It released its count when the pairing session for: %s was replaced"
+ "%s Terminated. It uses no pairing keys, so leaving the pairing session for: %s"
+ "%s is stopping. Pairing session for: %s is still held by another datapath"
+ "%s was set up with the replaced pairing session for: %s. Terminating it"
+ "7df2f86510a158588e07576548f8486836e4da128e875e34d37904ba3e026e9e"
+ "7e5c6a436e86fda5e6ed2318750721e1995a2d519091f98c9d2dea1d09e48285"
+ "Cannot create new datapath for %@ to %s[%hhu] because connection mode is %s but no DCEA"
+ "Failed to clear the peer presence table after interface re-creation because %@"
+ "Retaining pairing session to: %s, UsageCount: %ld"
+ "WiFiP2P-889.6 Nov 10 2026 05:11:26"
+ "hasPairingSession"
+ "releasedPairingSession"
+ "{\n  \"12318a6122dcdcc1c039fffae7566a00bf8b5a61d7fe8467838e1784451ff349\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"ASKAdvertiser\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"2006fe0ec29074e5daa37da7e86c4cbeeae5f88138b612aa396f12898a516d81\": {\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"NoConsoleUser\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    }\n  },\n  \"8fef669fad8e9b31df1bff1ed7f4c51a70b015bff2539074e2518cc93d88ceb5\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"macOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    }\n  },\n  \"6ae5d43ffb39f0d2dc926630e579462d86cd8f2a086d4a782f30a19dcc06fc06\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"ASK\",\n        \"DDUI\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"354dd24eac7f9483b9fe792c8e18dae4a3786c43e49d2eaa3fb67e04dcec7c65\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Timeout\": 120,\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    }\n  },\n  \"74ac65c9abf7a1be29d948b719ce184927f939162245333c5ab02a3821a32e4d\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"MARS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"0e84ce8c9290cd408c37e9dd3002a29ff8e5dfb86cc79555495c08126cc0ff1a\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\"\n      ],\n      \"ClientID\": [\n        \"CLI\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    },\n    \"TDS\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    }\n  },\n  \"4c8b81ecfa9644f1ba8be20dcec644e6aaef8ae6478ff43eb15e933029d29c38\": {\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"visionOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"visionOS\"\n      ]\n    }\n  },\n  \"7da39a7517a3e4426dc72e9b9cef559d17f0ecfbab3bf2ed4d964a60675366c3\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"Timeout\": 120\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    }\n  },\n  \"40fe8f112c7169694df20858fe62c0bc42c1e6be0f99902b3cdec96014ac6de8\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Terminus\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    }\n  },\n  \"f56c7523abbd7a1dea32ab50b524ba828397aacb9106de3f273d6ff8930256ff\": {\n    \"Publish\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    }\n  },\n  \"5a2d6d1cd441cd94a9e1ae7bdddccae62959c7020e951682fa53b45d284e7d43\": {\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"NoConsoleUser\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    }\n  },\n  \"2ed3613ded5b623bf91f20221b311216db66da598ad63a8ab374d24d1ebd3363\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"Migration\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  }\n}"
+ "{\n  \"WiFiAwareAllowedBundleIds\": {\n    \"2a3088591b9e3738267235ef5bb8db530d6196629a1015aca2d7cee1794d9b38\": {\n      \"WiFiAwareServices\": {\n        \"e32c3bd5d0e94b457326bf6bdefb82325debcd62e7d173c2d1ed268a477988f1\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"16bfb1649882b3c2cac242397ae91a91a9a94a8b9289f42366f651115747bbeb\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"1038bdd372b784a7470b22db5920358e2f6e08f666daba82de871b96cb2d1470\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"bdf30c8bdff4bf13f4781cf83f4527314d66bc8f2c12ab5a67c7eb454d21184c\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"e40133d648451a8719f337ffba71067673c575e2d264bc593dab807253c70655\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"df92b67166c81f656539ada449e42da2a0e4ecec4b4a14d240b7388c44e2ff18\": {\n          \"Subscribable\": {},\n          \"Publishable\": {}\n        },\n        \"206b04ef4b0054bbe6f92b27109c861275a9eca993a9e4854d7186bbf5296439\": {\n          \"Subscribable\": {},\n          \"Publishable\": {}\n        },\n        \"57e27ab99ebef2b69ab77fbee41debdd8d7b7a247090ff88bd819761aca1b2c2\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"b6708cb4069d725dc70e900009f0e7531681cbcc70bd6a8198763906231f1b5e\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"896ed1555c94a657bf1874a5a636ac82ee15ff88af98d3ac43b0d0d579c7163a\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"4b32e91528722a5549d486f29763c427d3586be84937da3dd84f85e200ccbee0\": {\n      \"WiFiAwareServices\": {\n        \"356ec0a326f010f3a3bbf252c96a7ea58bb03ed3d477af6a5d6d65f70b895f8b\": {\n          \"Publishable\": {}\n        }\n      }\n    },\n    \"f3feb3ad32eed5f779c0f2ce444c59f45e5393f9f447396d2d6b21ab70920ff7\": {\n      \"WiFiAwareServices\": {\n        \"f2f210fe510431313be91b59a4f287ccb642dda279dfe9c4bd4d5afe680c0271\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"9a1ded4ff40ecd0437c18672ddf9d8a080f4fea5471abc4044751d39a22f90f9\": {\n      \"WiFiAwareServices\": {\n        \"82bff4c626d2d5b0541d4961f6b85c5d7d4d255dc8c2b9c3ef3cee2725e3936e\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"846b495271cf26ae2edeae76652d02e64b3bf0b3ecf243fe989b0ae1e402765e\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"bbdcee604867dd316cd10ea4b224dc28fc0c7e1e3801b85224a705fa19d3a5c0\": {\n      \"WiFiAwareServices\": {\n        \"356ec0a326f010f3a3bbf252c96a7ea58bb03ed3d477af6a5d6d65f70b895f8b\": {\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"c4e928bdebcebe5d2c33e6869e89d44ca30b019edee49b15a50cf0bb011610ea\": {\n      \"WiFiAwareServices\": {\n        \"f2f210fe510431313be91b59a4f287ccb642dda279dfe9c4bd4d5afe680c0271\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    }\n  }\n}"
- "#### Not Terminating datapath %hhu. Referenced by other endpoint."
- "#### Terminating datapath session %hhu for Responder"
- "0381c6aa35bde7da8dcd7fc215f4c8d5554717e8e5c1611a5ac106db2fc58481"
- "3b61337d9d575b831cf189280ed72c8f2772f4e87fcd0dd8ec5fb330284db39c"
- "WiFiP2P-889.2 Oct 24 2026 18:10:23"
- "datapathType"
- "{\n  \"WiFiAwareAllowedBundleIds\": {\n    \"9adca746223cfa02763f8234f78872a69867ec7f0319ca278ab662ba1ede689d\": {\n      \"WiFiAwareServices\": {\n        \"0adba686bc17055f4179ac9fd9066b42e0894d8f490b54eeb7aa72c180be99c3\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"e04e5d7cb0309b09d1515dd307ffd0093544f0ed6d343e737cdf777a9fcce601\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"72de875978371f96fdac2d32213c876f53cdba872e9df498c339b086e2998656\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"5c2b7fac954723ea7f1209808fe2dd731cdc0e83962d3b3d3035b44f96747555\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"df5478944423ce7bae293b33c3fd2d6c485736c8b60a097ab232811bbf558e2d\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"0b1bbf5a01b1732fd3563c39bb4dc54c1328b670821965e42c4b6f3379b1f54e\": {\n          \"Subscribable\": {},\n          \"Publishable\": {}\n        },\n        \"08eb31b7f88d538b5b0657e20d9a48260ba1588209f318011f2af9334baf5114\": {\n          \"Subscribable\": {},\n          \"Publishable\": {}\n        },\n        \"1d48def3506920a2354378b9e8b2bf69cf25039951b618263a3ee644d1b8992b\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"8fce2a4d8db626d2c19e01123763cb4037e18dec62ea16a79157da11dfc1a01c\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"bb3ea0c96be0afcdf4c1ee654b6ad4af5148d68e55dd78bf346c838add2ba316\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"dd718c702aeca8560dad46d09acf0ce352f12b1ce056d7aeade276c5299ab683\": {\n      \"WiFiAwareServices\": {\n        \"f8d1011e511e864fcba1e9b970cc351d4b62a4659f880889eb12ad65f830391f\": {\n          \"Publishable\": {}\n        }\n      }\n    },\n    \"76b871f7cb2d3967d7334be9c076a4a39f597b072cb856041b8b46e888901273\": {\n      \"WiFiAwareServices\": {\n        \"49f95c8b64be8d725ac1034e5b618fbf5ff30bb05013d99584ed25560ce2a8c4\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"3c9abcde4378f0e42e15bb13ab30c0f009f197ab8c41a360997c447da2f2a3b0\": {\n      \"WiFiAwareServices\": {\n        \"3f641641442cc0b93d1cf0e8188988509d30164d3fe53b1bfb3018e1d95e5bae\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"8983326ab529b826acac8586de0c6ea6229e6698467630c46187b7eb22c131cd\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"b4914f4a63892e10c12f26ef14ba87961f77515e5814da49c8bafeae96a35118\": {\n      \"WiFiAwareServices\": {\n        \"f8d1011e511e864fcba1e9b970cc351d4b62a4659f880889eb12ad65f830391f\": {\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"739945789106ca9bb4ef5fbbeb63f4be4d182af059555f34f56353af92c22a2e\": {\n      \"WiFiAwareServices\": {\n        \"49f95c8b64be8d725ac1034e5b618fbf5ff30bb05013d99584ed25560ce2a8c4\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    }\n  }\n}"
- "{\n  \"e0d0d654ff4adb3b46bd74cb900a68329dfa2cf327ee9964c041e6333a14aee5\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"ASKAdvertiser\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"60a93e2bf31bda7ff44f71de916434916e74ba341d63eaf99683cda31ebdd8fa\": {\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"NoConsoleUser\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    }\n  },\n  \"51855e1c84bb3220a679f67f95db9aba0bf673c81ce4d51aabbea7be1adaf73d\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"macOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    }\n  },\n  \"9badd9d41d9582aa3c44b4f361b29bef75cd3bc8416be7084770b7933648eadd\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"ASK\",\n        \"DDUI\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"d952e53ddbdb523526ed8490dfdc788884bb2333b0ea4a7c08aec9966f3bdc1a\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Timeout\": 120,\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    }\n  },\n  \"396dddd97409ccc7c26a695d1a88564d738339c7ac0c93467895d0beb20aaa8e\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"MARS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"35cbf81621993a8d9a80c55629381c4133b09fdeeeb57916b0aa52d98dbb6b2e\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\"\n      ],\n      \"ClientID\": [\n        \"CLI\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    },\n    \"TDS\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    }\n  },\n  \"a0389a63ac221c362376090c52abfd06b316a1a3b9bc8128438758c230d3bbde\": {\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"visionOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"visionOS\"\n      ]\n    }\n  },\n  \"07956421d02245c153197a82c166449039dcf9d634362e2fe8f65ebd1a815a02\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"Timeout\": 120\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    }\n  },\n  \"a73d3b268e1dd25dc568e0fafef8cce3514a2e88d12efa667f935cc61d9177cf\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Terminus\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    }\n  },\n  \"7baa6c15d6ea82691fd454e16bcd679b73be4454ac18a33f62f87e5c494a5b5d\": {\n    \"Publish\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    }\n  },\n  \"3581407d2be58e9242b40bc2a1510983d653a5c532d1777130e2578c9ca2a400\": {\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"NoConsoleUser\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    }\n  },\n  \"51061af57d518232b9ac041d6984ff7c46540b17309a012a60aad39c39bfcff8\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"Migration\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  }\n}"
```
