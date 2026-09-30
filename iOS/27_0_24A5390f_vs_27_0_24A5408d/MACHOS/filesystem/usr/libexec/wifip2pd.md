## wifip2pd

> `/usr/libexec/wifip2pd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__cstring`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-885.77.0.0.0
-  __TEXT.__text: 0x5e0e88
-  __TEXT.__auth_stubs: 0x5250
+885.85.0.0.0
+  __TEXT.__text: 0x5e5198
+  __TEXT.__auth_stubs: 0x5240
   __TEXT.__objc_stubs: 0x4720
   __TEXT.__objc_methlist: 0x1bf4
-  __TEXT.__const: 0x402b0
-  __TEXT.__swift5_typeref: 0xd2b3
+  __TEXT.__const: 0x404b0
+  __TEXT.__swift5_typeref: 0xd367
   __TEXT.__swift5_entry: 0x8
   __TEXT.__cstring: 0xfa24
-  __TEXT.__oslogstring: 0x2249c
-  __TEXT.__constg_swiftt: 0x103a0
-  __TEXT.__swift5_fieldmd: 0x1690c
-  __TEXT.__swift5_types: 0x12d4
+  __TEXT.__oslogstring: 0x2267c
+  __TEXT.__constg_swiftt: 0x103f4
+  __TEXT.__swift5_fieldmd: 0x169d8
+  __TEXT.__swift5_types: 0x12e0
   __TEXT.__swift5_builtin: 0x1748
-  __TEXT.__swift5_reflstr: 0x14b39
+  __TEXT.__swift5_reflstr: 0x14bd9
   __TEXT.__swift5_assocty: 0x2d78
-  __TEXT.__swift5_proto: 0x3070
+  __TEXT.__swift5_proto: 0x3074
   __TEXT.__objc_classname: 0x10f7
   __TEXT.__objc_methtype: 0x2347
   __TEXT.__swift5_protos: 0x108
-  __TEXT.__swift5_capture: 0x7f4c
-  __TEXT.__objc_methname: 0xa2e5
+  __TEXT.__swift5_capture: 0x7fc8
+  __TEXT.__objc_methname: 0xa305
   __TEXT.__swift5_mpenum: 0x1a8
   __TEXT.__swift_as_entry: 0x204
   __TEXT.__swift_as_ret: 0x168
   __TEXT.__swift_as_cont: 0x5f4
-  __TEXT.__unwind_info: 0x10798
-  __TEXT.__eh_frame: 0x1e50c
-  __DATA_CONST.__const: 0x39ca0
+  __TEXT.__unwind_info: 0x107e8
+  __TEXT.__eh_frame: 0x1e65c
+  __DATA_CONST.__const: 0x39f28
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_protolist: 0x2f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x178
-  __DATA_CONST.__auth_got: 0x2930
-  __DATA_CONST.__got: 0x1038
-  __DATA_CONST.__auth_ptr: 0x7968
-  __DATA.__objc_const: 0xac30
+  __DATA_CONST.__auth_got: 0x2928
+  __DATA_CONST.__got: 0x1028
+  __DATA_CONST.__auth_ptr: 0x7950
+  __DATA.__objc_const: 0xac90
   __DATA.__objc_selrefs: 0x16e0
   __DATA.__objc_data: 0x1920
-  __DATA.__data: 0x14fc0
-  __DATA.__bss: 0x5e250
-  __DATA.__common: 0xb78
+  __DATA.__data: 0x15068
+  __DATA.__bss: 0x5e2d0
+  __DATA.__common: 0xb88
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 24933
-  Symbols:   2320
+  Functions: 24965
+  Symbols:   2318
   CStrings:  5522
 
Symbols:
- _$sSTsE3max2by7ElementQzSgSbAD_ADtKXE_tKF
- _objc_retain_x11
CStrings:
+ "%@: Discovered Peers updated (%ld -> %ld): %s"
+ "%@: Expected .second pairingResponder for autoReply, got %s; skipping bootstrap for %s"
+ "%@: No discovered peers matched filter %s"
+ "%@: RESET Discovery Results: %s"
+ "%@: [BLOOM FILTER] Remove %s (ResetDiscoveryResults)"
+ "%@: [BLOOM FILTER] Remove ALL (ResetDiscoveryResults)"
+ "%@: cross layer key: %s"
+ "%@: cross layer key: failed to derive CL Setup Key: %@"
+ "%@: ignoring bootstrap request, already bootstrapped in state: %s"
+ "%@: reactivatePublish skipped — publish not active"
+ "%@: received: bootstrap request, dialogToken: %hhu"
+ "%s: Indicating pairing completed for %s to observers"
+ "2db604519c0855158eeec5689f4166cf9fab6f0f39132d09ea2a4b52f37de49b"
+ "73219558a96443bc88a05df1c568a19edd3418293c99e3fb7fbc25970b732166"
+ "Completed(peerAddress: "
+ "Could not get the cross layer key derivation key since the PASN state is not confirmed"
+ "Failed to re-activate publish %@: %@"
+ "Reactivating %ld publish service(s)"
+ "Resetting bloom filters for Unpaired devices on ALL active subscribe instances ..."
+ "Resetting subscribe discovery results for (%ld) subscribes (Filter: %s)"
+ "WiFiP2P-885.85 Aug 04 2026 02:08:52"
+ "cross layer key inputs: ndpID: %hhu, listenerIPv6Address: %s, listenerPortNumber: %hu, service: %s, protocolName: %s, context: %s, pairingSession: %s"
+ "cross layer key: could not derive the CL-KDK"
+ "cross layer key: failed to derive the CL-KDK: %@"
+ "cross layer key: no pairing PASN found for the session"
+ "pairingObserverTasks"
+ "{\n  \"54d4daa3ee3533b94489c9e3624fe86ab6243c07805c113e6f8165ccdf8869a5\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"ASKAdvertiser\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"9650536bc12e514e378b9b18ea2fff13e016d6f53fc07431730fc0cab45e6c23\": {\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"NoConsoleUser\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    }\n  },\n  \"9f72341cba0a8f5382925872f90f1c40b13ac25b0d1afe6d6dfe64e683c42f13\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"macOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    }\n  },\n  \"8a20105ba7e5261bdb0922e3583525b70e07f58267cc9b5708a22d5376126089\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"ASK\",\n        \"DDUI\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"a7f194c7c159b71e3149f22a48e9300f9fdd8f17c4619d8ff142faef2e08620c\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    }\n  },\n  \"d5e6e6ea92660064a7183fd5665698aee7f5b305d198fe88df0c7c5acc68478a\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"MARS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"dedbee2b98daf0aa9c53f2daccda2ad51ec6f909bf53d2bf590a5d3125c0a5e2\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\"\n      ],\n      \"ClientID\": [\n        \"CLI\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    },\n    \"TDS\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    }\n  },\n  \"6c447c746672a810a88a00d0bee38f1ecde3ea6ff78197e9bd6b044da1c8b3b1\": {\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"visionOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"visionOS\"\n      ]\n    }\n  },\n  \"94956f73da38a2b99f92a63fba6ca78b1ab756b0a29264d4a4156b68e3e823e4\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    }\n  },\n  \"61bc740925139bd2271424d887103ca05abaefd81084dcc4c23a44774d639113\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Terminus\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    }\n  },\n  \"432ba52227074858ace2e73f98f89a45a506cf9f0b3dfa4cb6deb92732def150\": {\n    \"Publish\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    }\n  },\n  \"b4d08a24e878914a05762d3b9d93e11767b8d57b8e085917bda00f90870d11d8\": {\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"NoConsoleUser\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    }\n  },\n  \"aaa92646327d64c0a8e9a539e1f5acc3ce16f1f14722527f971d6b035c7da075\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"Migration\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  }\n}"
+ "{\n  \"WiFiAwareAllowedBundleIds\": {\n    \"62f7714e54d2930348a425ddd055a2214062c01abb09afc8c9011f1b90451128\": {\n      \"WiFiAwareServices\": {\n        \"ca64d70498000fec919b1fee2315497011a11b1aeea11318c189ec85fdffaaed\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"c352c8fa9ee223439c2ec5afc4af003a550ea58bd7ce98b542c7c2648745e8cf\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"1f265534d13b3e2eab4fe7c40d0cfef1f8efe40c4f3ddaa65f7a32e945cc2a7b\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"021bfb0274e1d531e355099469320d0c3e9b01a12b3d056da6139c5df7601dbb\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"51be15bf208728f520870afad8fa893efc55af5758c2f9d9d8e9bf220dd08386\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"12de901ce7785b05c636279b50f4d41d6a21eb7674e9ccd8486ffd18953d1b98\": {\n          \"Subscribable\": {},\n          \"Publishable\": {}\n        },\n        \"b87b626bf2d0c17d47c6d56ea1fbebf9f12efd8217b23dc8b1853eaf4360ccb4\": {\n          \"Subscribable\": {},\n          \"Publishable\": {}\n        },\n        \"06f02e13174121abc39a4221b4be07d9ef21fcb789984cf1694f4a81dfd191f5\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"685b4cf14d6cfefeabc40c8dfded89739bab59594f59dfe647872c03f5e8616b\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"54591ada38157f9f00b9d45cda6a11fbdac5cddd1622d15a918619e17a1f7815\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"81f487fcf4be5209ef1f3a38560c458b629b552bb9213d282901837929938e96\": {\n      \"WiFiAwareServices\": {\n        \"e079b2f2374482e95a4154178e4fe96712f0bcb5c3c1c44677d11c3b1e782b11\": {\n          \"Publishable\": {}\n        }\n      }\n    },\n    \"f47e4a998c44e581f68d1b779780a8c4195d3faea876b37264e8969703a4e782\": {\n      \"WiFiAwareServices\": {\n        \"bbcd214396a734138682220864de183bdc854e2f1fd57bfa1f09e5efb3f91386\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"962bfb844f88655bbdfc00bf9b9624144eacda2f3d2136ddaae1f1c8facadc9b\": {\n      \"WiFiAwareServices\": {\n        \"edd098afaabd918dc975265d54a471d388af7ead3339d30dfd44803fca245532\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"b27f5d71cb2ba73d54394ecea688035de5c5774f12c1db0ea0f5120bc4df76ed\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"df42b6981c39a7a656ad139d5a2354bb321d828a0b73690be1705463f05c5453\": {\n      \"WiFiAwareServices\": {\n        \"e079b2f2374482e95a4154178e4fe96712f0bcb5c3c1c44677d11c3b1e782b11\": {\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"72b44e00d81cce2a664823bbfcf00a7c260dd0c2e2a6b43a40986581494251f1\": {\n      \"WiFiAwareServices\": {\n        \"bbcd214396a734138682220864de183bdc854e2f1fd57bfa1f09e5efb3f91386\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    }\n  }\n}"
- "  context: %s"
- "  listenerIPv6Address: %s"
- "  listenerPortNumber: %hu"
- "  ndpID: %hhu"
- "  pairingSession: %s"
- "  protocolName: %s"
- "  service: %s"
- "%@: Clearing discovered peers"
- "%@: Clearing discovered peers for %s"
- "%@: [BLOOM FILTER] Remove All (ResetDiscoveryResults)"
- "%@: [BLOOM FILTER] Remove for %s"
- "%@: received: bootstrap request"
- "%s: Indicating pairing completed for %s to the discovery engine"
- "%s: cross layer key: %s"
- "%s: cross layer key: not authenticated"
- "3f8f00503561fd782fce9a2a24e049c77d94162a0556371a2fd4bb7e96d16edb"
- "Could not get the cross layer set-up key since the PASN state is not confirmed"
- "Failed to derive shared secret: invalid state"
- "NANPairing.deriveSharedSecret inputs:"
- "PairingCompleted(peerAddress: "
- "Resetting ALL(%ld) subscribe discovery results"
- "Resetting bloom filters on ALL active subscribe instances ..."
- "Resetting subscribe discovery results for %s"
- "WiFiP2P-885.77 Jul 11 2026 04:07:41"
- "cross layer key: generating the CL set-up key..."
- "e5c7a99eb1778094d8dcc9093987d38916ad49996882bc780e12a7d35dd52cdf"
- "{\n  \"WiFiAwareAllowedBundleIds\": {\n    \"3758d1f348cb94b6098ca0d8e0d05964ed8bfbabc86f7396e16daac7e4b058f1\": {\n      \"WiFiAwareServices\": {\n        \"0ceff67064a3988519796c2745c11f65af7ca4fa0792e94123972b0f248dd2c9\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"61a75672261bfcbdaddbe4a837120f7dc30ebaff7429d8ae0709c8e5114adee8\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"744ecc50ced39d874ade29ea3ac5f4f17ba2034743b3e4ce5b81cf63b3c51896\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"7fab588796cbb80aa83d8654e226fd7e89068c138e2f01d926f1ca3e28eead52\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"938cd7868e2f46af884acfe43cd78ab021070b1aed9a1d818ec4277cb78285f9\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"859dca8ae53f6f20873fb7eb13f65c44c69482e78d8b027fa0a2afd899b4fb00\": {\n          \"Subscribable\": {},\n          \"Publishable\": {}\n        },\n        \"508c35a1b6febb650a79b9929e07108dc80100e56065a0a58b18a262a4385d36\": {\n          \"Subscribable\": {},\n          \"Publishable\": {}\n        },\n        \"08b1a2fddb3983984e6e3a5c2aa3af11d1c01232818ac8f2379958e042f0bd0c\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"38a7f49c0e8aa4d179ef6827f541b01346841e78fc6e29c549eff0ee48446737\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"e7b85a867dfb641a9558dc1b24f8af59778868df586c69675b34a4b8a391f461\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"51c8756199cd681d12820e5bfb52a7bf7277bd38fd4a721fe6c127addd9b1e83\": {\n      \"WiFiAwareServices\": {\n        \"8083e76d65267b596418e70c5a3261de4295b0156141d1bea1241b99268f4c7b\": {\n          \"Publishable\": {}\n        }\n      }\n    },\n    \"e74be50ea6f37fc6049c112916fea9d88af33e8ce59fb831b63966ffd15ac36e\": {\n      \"WiFiAwareServices\": {\n        \"db7867db8c5c5aca4dfdb40164b3682014238f67aad882c3b75ef9e431d762ad\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"3a717302bf532940388fd6266eab01804641f060c2ab8c55f53877c484588f47\": {\n      \"WiFiAwareServices\": {\n        \"cbb0aff114829e9878b4bd4f6ded9233dbd99c1b6de821511b89b99b5af60b3d\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"da5638bb367f90b1b7d55c121cb4a5ca5fda9e2c120cd80834d8c85b5807c870\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"55b24a7a30236448d4c6059344a3f8d3c22bd15c0e0e3d2d1e88fade42f14e73\": {\n      \"WiFiAwareServices\": {\n        \"8083e76d65267b596418e70c5a3261de4295b0156141d1bea1241b99268f4c7b\": {\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"3e353312e653d2795f052adc81236ab0f4a6a54685dcf6315ad3858ca1047e00\": {\n      \"WiFiAwareServices\": {\n        \"db7867db8c5c5aca4dfdb40164b3682014238f67aad882c3b75ef9e431d762ad\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    }\n  }\n}"
- "{\n  \"f4cdc15b2a374d81359d744fb9f7c8d440ffc8487b827988a24c7737f358f605\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"ASKAdvertiser\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"6807a4ab95437a0246e84b6ef0250d0ecc59771f9e37583a8c8f5484f62e4f89\": {\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"NoConsoleUser\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    }\n  },\n  \"e4e2bd48d485e77e7eb05b2eef85ddaf3040d8df3e73a97ff14048a4ae47e5ed\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"macOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    }\n  },\n  \"f15533c3e86b0618a56ea36b66b6af141f823409709e4ac8014efb4914655872\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"ASK\",\n        \"DDUI\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"720c54ffe1def4171b09c2c250927801821ccf7bf457970cbe419bf27d0c8dab\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    }\n  },\n  \"16899a86099e7183dc69e3fb742e7d883d2a81849557a7bd137badfa4875c6c4\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"MARS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"fedc47cc34cf3ed4a75041be388fc7e372c46a3551d73eea1bdb4326b7935af3\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\"\n      ],\n      \"ClientID\": [\n        \"CLI\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    },\n    \"TDS\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    }\n  },\n  \"7c31d95bcf8e1f1756be6a5c7519c55df071e511defc33fce0646fea5084de30\": {\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"visionOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"visionOS\"\n      ]\n    }\n  },\n  \"500a426930046e140b394e9623d82254702a8acf81c03d6a374d15ce63cece9b\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    }\n  },\n  \"aa79df953357eeea4a2b5f2cbdf38a559ee784f1f1c1b799b1385616d8269180\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Terminus\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    }\n  },\n  \"6f054b7b70e2bc463e3a0339baba84ff4245861e0005467537fc820514f4380f\": {\n    \"Publish\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    }\n  },\n  \"be8724fea8d9b696544cedd583ddb2c9bb31017de87e3c689e87a992d4f2dd57\": {\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"NoConsoleUser\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    }\n  },\n  \"3225590b02822b3d3490f7f438e423f66e6b7dbc8b9907ce984d3ee21d6fd37c\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"Migration\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  }\n}"
```
