## wifip2pd

> `/usr/libexec/wifip2pd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__swift5_entry`
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
- `__DATA_CONST.__auth_got`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-875.71.0.0.0
-  __TEXT.__text: 0x605c84
+875.79.0.0.0
+  __TEXT.__text: 0x609f78
   __TEXT.__auth_stubs: 0x4f90
   __TEXT.__objc_stubs: 0x47e0
   __TEXT.__objc_methlist: 0x1c2c
-  __TEXT.__const: 0x407f0
+  __TEXT.__const: 0x409f0
   __TEXT.__cstring: 0xfb54
-  __TEXT.__swift5_typeref: 0xd513
+  __TEXT.__swift5_typeref: 0xd5d7
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__oslogstring: 0x235bc
-  __TEXT.__constg_swiftt: 0x10634
-  __TEXT.__swift5_fieldmd: 0x16b0c
-  __TEXT.__swift5_types: 0x1300
+  __TEXT.__oslogstring: 0x2379c
+  __TEXT.__constg_swiftt: 0x10688
+  __TEXT.__swift5_fieldmd: 0x16bd8
+  __TEXT.__swift5_types: 0x130c
   __TEXT.__swift5_builtin: 0x175c
-  __TEXT.__swift5_reflstr: 0x14df9
+  __TEXT.__swift5_reflstr: 0x14e99
   __TEXT.__swift5_assocty: 0x2d78
-  __TEXT.__swift5_proto: 0x3090
+  __TEXT.__swift5_proto: 0x3094
   __TEXT.__objc_methtype: 0x2367
   __TEXT.__swift5_protos: 0x108
-  __TEXT.__swift5_capture: 0x838c
-  __TEXT.__objc_methname: 0xa4e5
+  __TEXT.__swift5_capture: 0x8408
+  __TEXT.__objc_methname: 0xa505
   __TEXT.__objc_classname: 0x11f7
   __TEXT.__swift5_mpenum: 0x1b8
   __TEXT.__swift_as_entry: 0x244
   __TEXT.__swift_as_ret: 0x194
   __TEXT.__swift_as_cont: 0x668
-  __TEXT.__unwind_info: 0x11148
-  __TEXT.__eh_frame: 0x1ed5c
-  __DATA_CONST.__const: 0x3a6c0
+  __TEXT.__unwind_info: 0x111a0
+  __TEXT.__eh_frame: 0x1eeac
+  __DATA_CONST.__const: 0x3a948
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_protolist: 0x2f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x178
   __DATA_CONST.__auth_got: 0x27d0
-  __DATA_CONST.__got: 0x1080
-  __DATA_CONST.__auth_ptr: 0x7a40
-  __DATA.__objc_const: 0xb080
+  __DATA_CONST.__got: 0x1070
+  __DATA_CONST.__auth_ptr: 0x7a20
+  __DATA.__objc_const: 0xb0e0
   __DATA.__objc_selrefs: 0x16f8
   __DATA.__objc_data: 0x1a70
-  __DATA.__data: 0x15530
-  __DATA.__bss: 0x5e450
-  __DATA.__common: 0xba8
+  __DATA.__data: 0x155d0
+  __DATA.__bss: 0x5e4d0
+  __DATA.__common: 0xbb8
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 25219
-  Symbols:   2285
+  Functions: 25251
+  Symbols:   2284
   CStrings:  5615
 
Symbols:
- _$sSTsE3max2by7ElementQzSgSbAD_ADtKXE_tKF
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
+ "72cc81478070ab044567db427eee9662e3f5e8a62e484def285e5416d730d50b"
+ "9e8c9b7ea7b2b50aa350f1057f360053f28fe1a8b521ddc7211fb21f99958457"
+ "Completed(peerAddress: "
+ "Could not get the cross layer key derivation key since the PASN state is not confirmed"
+ "Failed to re-activate publish %@: %@"
+ "Reactivating %ld publish service(s)"
+ "Resetting bloom filters for Unpaired devices on ALL active subscribe instances ..."
+ "Resetting subscribe discovery results for (%ld) subscribes (Filter: %s)"
+ "WiFiP2P-875.79 Aug 10 2026 01:08:10"
+ "cross layer key inputs: ndpID: %hhu, listenerIPv6Address: %s, listenerPortNumber: %hu, service: %s, protocolName: %s, context: %s, pairingSession: %s"
+ "cross layer key: could not derive the CL-KDK"
+ "cross layer key: failed to derive the CL-KDK: %@"
+ "cross layer key: no pairing PASN found for the session"
+ "pairingObserverTasks"
+ "{\n  \"WiFiAwareAllowedBundleIds\": {\n    \"b93a2ee690e9acd6b4edbab20d8852996edae412991adb7e552c1705fe15d3c0\": {\n      \"WiFiAwareServices\": {\n        \"5670e7bb060eaabc3328d2b8015e5fd78fd0c9a0953cd5ee3f215c8bae08d314\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"76453d1b26a6db7e73af39d17b354295b5e2d99e5dacd9f646ab8de5db3aafa0\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"bb2f52e9f2ad1270027ba7f263dde6f9f7790af4dc9ab548a410cad6fd823fc0\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"4f17797eafa1f96d12ba72ed0d18ad906eb56005afedd051b15afbe48384bcf1\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"5b200b816cf26458ca3df942ae04ed83b01e5ccbf1ca5f6be345f0ed46730a55\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"535bf3f4f4df101e9391b1cf0735bf1e7632190e3fba59f1d361a7277722a522\": {\n          \"Subscribable\": {},\n          \"Publishable\": {}\n        },\n        \"dfe30e284a68e1c42c9d5c435b40b734ab6fe56f6640bc8e4a8ad6782b679c6f\": {\n          \"Subscribable\": {},\n          \"Publishable\": {}\n        },\n        \"5c17bc641e2b8ac42755b81682143c1ab16547e7f14b0561538a2907c8564fea\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"3fd1aef0dacb5646f5106fef95396ffe35eb4c169008b13d8d39d76b38312052\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"fbeddc3fdf66fedea5f9c5e904ffb5bf4d9e17f9d152b6697741c3d94f5e0f0a\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"edf9569b42c53ceb8cdaad40c1ea0fe813ee20eafc55bba6a96cefa896d9d0dc\": {\n      \"WiFiAwareServices\": {\n        \"61409575f9b3286e4f1de1757688116bd9a550fa3de398f38df1bb110f9786c0\": {\n          \"Publishable\": {}\n        }\n      }\n    },\n    \"64c3d801a995ee70809e3d9ccff32c9e1f562b4bf8d62a5059785cba1d429965\": {\n      \"WiFiAwareServices\": {\n        \"fac5bbf6642e377f277c7f755b48556a0f698b6ce2ed48adb510213603073b1c\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"1954ff7deacadc99f20fc5e6136992030938f3d8a3b4dc19770619fa87a3c8f5\": {\n      \"WiFiAwareServices\": {\n        \"ebb879acb268b147097de56c0ce436108d1803344e3cf340eb825b8b242d2d87\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"d5f06e086caae87d6e6b128294ab11018969ef775e38301d56e21b508af7347a\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"6cad998c141d0291cdcecff0bf273ebc15043237042d48c58528977e7fa242be\": {\n      \"WiFiAwareServices\": {\n        \"61409575f9b3286e4f1de1757688116bd9a550fa3de398f38df1bb110f9786c0\": {\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"fd9d7a351dbc351540f0097c86d97a2e581c493084c6d4574de18c8ba59090e7\": {\n      \"WiFiAwareServices\": {\n        \"fac5bbf6642e377f277c7f755b48556a0f698b6ce2ed48adb510213603073b1c\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    }\n  }\n}"
+ "{\n  \"ba6a1b2490d94672af6783aba9e435f67b3bdf31835cc81349a5b74d60deb87e\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"ASKAdvertiser\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"807fd138158c8f867077fb8b5681e32c2486f29e32186931dd4310958b50e6cc\": {\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"NoConsoleUser\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    }\n  },\n  \"50e72685114105ee45bbf1ac714b3509c7f90b9897b38c71c1664d5af00bb860\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"macOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    }\n  },\n  \"89e0f7410a023640de5667eaba75448462ed59d6ff73335a093769fa347a5f60\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"ASK\",\n        \"DDUI\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"e14c2b0f53e12a321f9f86e40a2a6647b7a1df87a1a9ff106a63826edfcf78ae\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    }\n  },\n  \"72c627e47becbca406a997b5248ee768054cda6c40dfafcea454070e73f4ce6f\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"MARS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"bd9ee0171137db42e452fed78ee5ceb2a0c09220560a0f7bdca1744c3a41cf9a\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\"\n      ],\n      \"ClientID\": [\n        \"CLI\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    },\n    \"TDS\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    }\n  },\n  \"3ea1d3a2394c167b530a10ce022dc2007d7607e4b4873ad6ca27e96dda25a1e4\": {\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"visionOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"visionOS\"\n      ]\n    }\n  },\n  \"fb32485643ef17e55e17be49694b59dc4fe1ec700e3b2db13db5844759af107f\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    }\n  },\n  \"0af91ad1f9d957cce397fab2f983624b0820ea9dd0d398a7af0ceb48821f4fe7\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Terminus\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    }\n  },\n  \"b1eb8c2cf8515f117775df3e135953f8119828fde6a57e9b5ec2181e02976f73\": {\n    \"Publish\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    }\n  },\n  \"6d3d120f58a2d43c7e9f0d1d7bba25c4de822223fa3b2a8c43072ad48d682651\": {\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"NoConsoleUser\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    }\n  },\n  \"aefef0d0d9235e9671d830046708634ed449f6b05439dad3971646310b440fb3\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"Migration\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  }\n}"
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
- "068725a644067b4149059ac75c8b2f99ecbf93b3f6c04b00b0d383cd813d84eb"
- "Could not get the cross layer set-up key since the PASN state is not confirmed"
- "Failed to derive shared secret: invalid state"
- "NANPairing.deriveSharedSecret inputs:"
- "PairingCompleted(peerAddress: "
- "Resetting ALL(%ld) subscribe discovery results"
- "Resetting bloom filters on ALL active subscribe instances ..."
- "Resetting subscribe discovery results for %s"
- "WiFiP2P-875.71 Jul 10 2026 23:07:34"
- "cross layer key: generating the CL set-up key..."
- "d5680f5e08b306b03a3615a649939405c7d3a4c8df8a32c25f57cc6f6aa94ca5"
- "{\n  \"557ea4a4b1fd96e1d27309f2e8ee2d13dc26b90533be275371f1df768d0cbc62\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"ASKAdvertiser\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"6028608c041aa2ea6f3045e84e89ea2697702e7f66fb82c59ad02c33ab3555ec\": {\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"NoConsoleUser\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    }\n  },\n  \"de7a6c16add714d244b486d99b4e60d22819a7fb25b53a68dd1ae0562be83f9e\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"macOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    }\n  },\n  \"dfef93f0404160ea8cd924e38e661c2e830da67d1a6d2ba586616c261d5a5169\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"ASK\",\n        \"DDUI\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"866abc60e741cc972b544cff72e31a7bd08492c184168dfa7c3df93b18ba6305\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    }\n  },\n  \"1b80aa02a3faf0a64683e0745d77998383f9257fe952cf902dd73f47580b9e1a\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"MARS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"5ff458bbf4fede8aa1fd5c09567362e659d91355f9c6ce0fe6653ac6704169f9\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\"\n      ],\n      \"ClientID\": [\n        \"CLI\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    },\n    \"TDS\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    }\n  },\n  \"6b0216815315a86361625ff373d971a04cb9042633e724fe541d93687219aacd\": {\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"visionOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"visionOS\"\n      ]\n    }\n  },\n  \"0233a3e4d4235903228f498616d001c6b4d52b67f94932df5ef9faa1a1e0a553\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    }\n  },\n  \"6f914d0cbbf7c35d8f88ec19c9cfd6be2cbb6d3bc6bf0381ce67ef1c3e1e881e\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Terminus\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    }\n  },\n  \"d81bc47a6f885fea9a56ae93c2530748d1dba92224a9e4cdf7252ded84f6ffa8\": {\n    \"Publish\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    }\n  },\n  \"4f4b041ce3640ec663e0e9e7075eefd352ff1cf10e8595ed5623206a2ea14083\": {\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"NoConsoleUser\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    }\n  },\n  \"8416b7b00e4fba5693ba82b35df6f747397f1ebf4c1eb9e8e2e21caae19c5eaf\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"Migration\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  }\n}"
- "{\n  \"WiFiAwareAllowedBundleIds\": {\n    \"b9c89e60858e411275036629cf710d145b49a180a7a5c3faf5b1f05019ed6324\": {\n      \"WiFiAwareServices\": {\n        \"f2134725adcaf72045a603a09b99c8f2ff5605766ca6a8ddc7d06632a9effd5d\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"4b0f9d6cb3d45d7bc4d835265838db8615f9506c3a96b16caa4f10a63590f020\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"5f20358788a8ad2cab175fd2e13a947294f221de2f8d4af48b011bfaec74fbce\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"c3ec6668f96d44fa26a7a74a21925b13972e41a9a4625c1202266dd7369689cc\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"20159b927a3cedb8333cb53f183fe36b3331b20ef078957a547da10d7d0842c5\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"5ee458cdbf5374000567cbcbdf8bba21234b718a8e93dc8f887489b6dbb22328\": {\n          \"Subscribable\": {},\n          \"Publishable\": {}\n        },\n        \"1d09a11e52e6a778f410ee69f0e4da1432879bf36e8c336c5cd9e94f1f8071cd\": {\n          \"Subscribable\": {},\n          \"Publishable\": {}\n        },\n        \"c40e609544ed71ee55204ef89c539c087cb929880397d3126ce64cda5b9c431c\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"faa3bdf0864766b6b41668b20c6282e984f75f10dc5c14750a10308bc056dc1e\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"6a2c40420567bbdab6e79766ae0c2e5303ad5513506eee78ce1f281deadb6400\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"e320024fca2dd8018ff87b396c60a45b5deb68f4571a2849b59aaeaa4f4585fa\": {\n      \"WiFiAwareServices\": {\n        \"c84279e2637f040cc507f90c5985d6ec029d34ecee9571d719ad6c1dcdb4c9c6\": {\n          \"Publishable\": {}\n        }\n      }\n    },\n    \"7a96a627c3422a1e85bf353a81642bda98acb5540da296d2db02d2c80f6d07d5\": {\n      \"WiFiAwareServices\": {\n        \"d9e41f7df5202bcfa17d2293d3ac2153f23e55b76d0dab925665e68cfdcebed9\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"b23fa33904a4abb2b63efadd69e91a4da2e95ae1a901434c08e4c24038e4189e\": {\n      \"WiFiAwareServices\": {\n        \"25a7d63541e2e8f7c03f5ab6cac9b434dfe6cabdaf29b612f0a2548ab09567a1\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"d707f4595f899d2f3a75d34c8aa749d3f7a44ced2fea745c2ac6ce244b2cdb08\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"82bcada2796339690bcde79c312f3499ce4c73e76b992564efd0b02d40b3c720\": {\n      \"WiFiAwareServices\": {\n        \"c84279e2637f040cc507f90c5985d6ec029d34ecee9571d719ad6c1dcdb4c9c6\": {\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"692c11b31797bab81abe68f8c4078a51010551613b5a8060f782b5bd6877e442\": {\n      \"WiFiAwareServices\": {\n        \"d9e41f7df5202bcfa17d2293d3ac2153f23e55b76d0dab925665e68cfdcebed9\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    }\n  }\n}"
```
