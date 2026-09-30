## wifip2pd

> `/usr/libexec/wifip2pd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__cfstring`

```diff

-885.69.4.1.0
-  __TEXT.__text: 0x5cf770
-  __TEXT.__auth_stubs: 0x51e0
-  __TEXT.__objc_stubs: 0x4640
-  __TEXT.__objc_methlist: 0x1b94
-  __TEXT.__const: 0x3f930
-  __TEXT.__swift5_typeref: 0xd067
+885.77.0.0.0
+  __TEXT.__text: 0x5e0e88
+  __TEXT.__auth_stubs: 0x5250
+  __TEXT.__objc_stubs: 0x4720
+  __TEXT.__objc_methlist: 0x1bf4
+  __TEXT.__const: 0x402b0
+  __TEXT.__swift5_typeref: 0xd2b3
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0xf5d8
-  __TEXT.__oslogstring: 0x2199c
-  __TEXT.__constg_swiftt: 0x10030
-  __TEXT.__swift5_fieldmd: 0x163fc
-  __TEXT.__swift5_types: 0x1280
-  __TEXT.__swift5_builtin: 0x16f8
-  __TEXT.__swift5_reflstr: 0x14629
-  __TEXT.__swift5_assocty: 0x2cb8
-  __TEXT.__swift5_proto: 0x3010
-  __TEXT.__objc_classname: 0x1007
-  __TEXT.__objc_methtype: 0x2317
+  __TEXT.__cstring: 0xfa24
+  __TEXT.__oslogstring: 0x2249c
+  __TEXT.__constg_swiftt: 0x103a0
+  __TEXT.__swift5_fieldmd: 0x1690c
+  __TEXT.__swift5_types: 0x12d4
+  __TEXT.__swift5_builtin: 0x1748
+  __TEXT.__swift5_reflstr: 0x14b39
+  __TEXT.__swift5_assocty: 0x2d78
+  __TEXT.__swift5_proto: 0x3070
+  __TEXT.__objc_classname: 0x10f7
+  __TEXT.__objc_methtype: 0x2347
   __TEXT.__swift5_protos: 0x108
-  __TEXT.__objc_methname: 0xa085
-  __TEXT.__swift5_capture: 0x7e00
-  __TEXT.__swift_as_entry: 0x1f8
-  __TEXT.__swift_as_ret: 0x160
-  __TEXT.__swift_as_cont: 0x5dc
-  __TEXT.__swift5_mpenum: 0x1a0
-  __TEXT.__unwind_info: 0x10468
-  __TEXT.__eh_frame: 0x1deb8
-  __DATA_CONST.__const: 0x390c8
+  __TEXT.__swift5_capture: 0x7f4c
+  __TEXT.__objc_methname: 0xa2e5
+  __TEXT.__swift5_mpenum: 0x1a8
+  __TEXT.__swift_as_entry: 0x204
+  __TEXT.__swift_as_ret: 0x168
+  __TEXT.__swift_as_cont: 0x5f4
+  __TEXT.__unwind_info: 0x10798
+  __TEXT.__eh_frame: 0x1e50c
+  __DATA_CONST.__const: 0x39ca0
   __DATA_CONST.__cfstring: 0x20
-  __DATA_CONST.__objc_classlist: 0x1c0
-  __DATA_CONST.__objc_protolist: 0x2e0
+  __DATA_CONST.__objc_classlist: 0x1e0
+  __DATA_CONST.__objc_protolist: 0x2f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x170
-  __DATA_CONST.__auth_got: 0x28f8
-  __DATA_CONST.__got: 0x1028
-  __DATA_CONST.__auth_ptr: 0x7840
-  __DATA.__objc_const: 0xa6b8
-  __DATA.__objc_selrefs: 0x1698
-  __DATA.__objc_data: 0x1898
-  __DATA.__data: 0x14970
-  __DATA.__bss: 0x5d650
-  __DATA.__common: 0xb60
+  __DATA_CONST.__objc_protorefs: 0x178
+  __DATA_CONST.__auth_got: 0x2930
+  __DATA_CONST.__got: 0x1038
+  __DATA_CONST.__auth_ptr: 0x7968
+  __DATA.__objc_const: 0xac30
+  __DATA.__objc_selrefs: 0x16e0
+  __DATA.__objc_data: 0x1920
+  __DATA.__data: 0x14fc0
+  __DATA.__bss: 0x5e250
+  __DATA.__common: 0xb78
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 24672
-  Symbols:   2311
-  CStrings:  5424
+  Functions: 24933
+  Symbols:   2320
+  CStrings:  5522
 
Symbols:
+ _$s10Foundation4DataV8endIndexSivg
+ _$s10Foundation8TimeZoneV19_bridgeToObjectiveCSo06NSTimeC0CyF
+ _$s10Foundation8TimeZoneV7currentACvgZ
+ _$s10Foundation8TimeZoneVMa
+ _$s8Dispatch0A3QoSV7utilityACvgZ
+ _$sScS12ContinuationV13onTerminationyAB0C0Oyx__GYbcSgvs
+ _$sScS_15bufferingPolicy_ScSyxGxm_ScS12ContinuationV09BufferingB0Oyx__GyADyx_GXEtcfC
+ _OBJC_CLASS_$_NSLock
+ _OBJC_CLASS_$_WiFiAwarePairingPasswordVoucher
CStrings:
+ "%@ terminating because of 6GHz infra steer failure: %s"
+ "%@: Failed to generate password"
+ "%@: Failed to generate password. BundleID is not set"
+ "%@: Generating password (GenerationMode: %s, PairingMode: %s, BundleID: %s"
+ "%@: Pairing session from: %s attached!"
+ "%@: User Approval Handler: Accept: %{bool}d, Pairing Info: %s"
+ "%@: Waiting for pairing session from: %s to attach..."
+ "%@: [Activate Pairing Mode] Password Generation Mode: %s"
+ "%s: Indicating pairing completed for %s to the discovery engine"
+ "%s: triggering core capture on authentication frame transmit failure..."
+ "3f8f00503561fd782fce9a2a24e049c77d94162a0556371a2fd4bb7e96d16edb"
+ "6GHz Infra Steer - No Candidate"
+ "6GHz Infra Steer - No Candidates"
+ "6GHz Infra Steer Failed"
+ "6GHz Infra Steer Failure"
+ "6GHz infra steer failure notification: %s — propagating to %ld low latency initiator(s) and %ld low latency responder(s) (totals: initiators=%ld, responders=%ld)"
+ "AWDL AF counters (last %{public}lds) received=%llu dropped=%llu stateGuardRejected=%llu alreadyPosted=%llu postSucceeded=%llu postFailed=%llu drop_reasons=[%{public}s] stateGuard_reasons=[%{public}s] postFail_reasons=[%{public}s] cumulative=[received=%llu dropped=%llu stateGuardRejected=%llu alreadyPosted=%llu postSucceeded=%llu postFailed=%llu]"
+ "Activated PKRecordsManager with SecureStorageProvider: %s"
+ "Activating BluetoothTDSManager..."
+ "Activating PKRecordsManager..."
+ "Activating PairedDevicesStore..."
+ "Authentication frame transmit failed to "
+ "BluetoothTDSManager"
+ "Created Password Voucher store instance: %@ for %@"
+ "ERROR: PREFERRED_CHANNELS_CHANGED: rejecting unconstructable tuple chan=%hhu band=%s bw=%s — upstream encoding likely non-spec"
+ "ERROR: PREFERRED_CHANNELS_CHANGED: unknown bandwidth encoding %hhu — skipping entry"
+ "ERROR: PREFERRED_CHANNELS_CHANGED: unknown channel_band %hhu — skipping entry"
+ "Failed to create password voucher store instance for %@: No Client BundleID"
+ "Failed to generate password"
+ "Failed to generate password for pairing mode %ld"
+ "Failed to generate password. BundleID is not set"
+ "Infra 6GHz steer FAILED (reason=%s, roamStatus=%d)"
+ "Infra 6GHz steer FAILED — no non-6GHz candidates (reason=%s, roamStatus=%d)"
+ "Infra 6GHz steer succeeded (reason=%s, roamStatus=%d)"
+ "Issued password voucher: %s (PairingMode: %s, UsageCount: %ld, Expiration: %s, ClientBundleID: %s). Total vouchers: %ld"
+ "No voucher found for token: %s"
+ "PKRecordsManager"
+ "PPSCreateTelemetryIdentifier"
+ "PPSSendTelemetry"
+ "PairedDevicesStore"
+ "Pairing Invalid Passphrase"
+ "PairingCompleted(peerAddress: "
+ "PairingSessionAttached(from: "
+ "Password generation is not supported for pairing mode "
+ "PasswordVoucherStore de-initialized"
+ "PasswordVoucherStoreInstance[%@] de-initialized"
+ "Removed expired voucher: %s (Expiration: %s)"
+ "Removed voucher: %s after final use"
+ "Skip Secure Storage Initialization [%@]"
+ "Unable to issue password voucher"
+ "Used voucher: %s (PairingMode: %s, UsageCount: %ld)"
+ "Voucher %s ownerBundleID mismatch (expected: %s, got: %s)"
+ "WiFiAwarePairingPasswordXPC"
+ "WiFiP2P-885.77 Jul 11 2026 04:07:41"
+ "_TtC12wifip2pdCore20PasswordVoucherStore"
+ "_TtC12wifip2pdCore28PasswordVoucherStoreInstance"
+ "_TtC7CoreP2P23AWDLActionFrameCounters"
+ "_TtC7CoreP2P5Latch"
+ "apple80211"
+ "bootstrapTasks"
+ "com.apple.wifip2pd.AWDLActionFrameCounters"
+ "continuations"
+ "createPasswordVoucherStore:"
+ "createPasswordVoucherStoreInstance"
+ "current"
+ "dropReasons"
+ "e5c7a99eb1778094d8dcc9093987d38916ad49996882bc780e12a7d35dd52cdf"
+ "enablePairingTxFailureCoreCapture"
+ "eventStream"
+ "header_load_or_nil"
+ "header_too_short"
+ "initWithToken:pairingMode:password:usageCount:expiration:"
+ "interface_recovering"
+ "issuePasswordVoucherForPairingMode:completion:"
+ "lastCounters"
+ "lastDropReasons"
+ "lastNotifiedRealtimeMode"
+ "lastPostFailReasons"
+ "lastStateGuardReasons"
+ "nan_event: APPLE80211_M_NAN_INFRA_6G_STEER_STATUS rawResult=%u rawReason=%u parsed result=%s reason=%s roamStatus=%d"
+ "nan_event: unknown infra6GSteer reason rawValue=%u, defaulting to .none"
+ "nan_event: unknown infra6GSteer result rawValue=%u, defaulting to .failed"
+ "no_payload_after_header"
+ "other"
+ "parsing"
+ "passwordGenerationMode"
+ "passwordVoucherToken"
+ "payload_decode_fail"
+ "postFailReasons"
+ "reportTimer"
+ "sem"
+ "setTimeZone:"
+ "stateGuardReasons"
+ "state_not_enabled"
+ "state_not_enabled+interface_recovering"
+ "steerConsentIntervalSeconds"
+ "stringFromDate:"
+ "terminationReasonOverride"
+ "testing"
+ "unlock"
+ "updatedNANRealtimeMode:"
+ "v32@0:8q16@?<v@?@\"WiFiAwarePairingPasswordVoucher\"@\"NSError\">24"
+ "vouchers"
+ "wifip2pdCore.PasswordVoucherStoreInstance"
+ "yyyy-MM-dd HH:mm:ss zzz"
+ "{\n  \"WiFiAwareAllowedBundleIds\": {\n    \"3758d1f348cb94b6098ca0d8e0d05964ed8bfbabc86f7396e16daac7e4b058f1\": {\n      \"WiFiAwareServices\": {\n        \"0ceff67064a3988519796c2745c11f65af7ca4fa0792e94123972b0f248dd2c9\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"61a75672261bfcbdaddbe4a837120f7dc30ebaff7429d8ae0709c8e5114adee8\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"744ecc50ced39d874ade29ea3ac5f4f17ba2034743b3e4ce5b81cf63b3c51896\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"7fab588796cbb80aa83d8654e226fd7e89068c138e2f01d926f1ca3e28eead52\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"938cd7868e2f46af884acfe43cd78ab021070b1aed9a1d818ec4277cb78285f9\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"859dca8ae53f6f20873fb7eb13f65c44c69482e78d8b027fa0a2afd899b4fb00\": {\n          \"Subscribable\": {},\n          \"Publishable\": {}\n        },\n        \"508c35a1b6febb650a79b9929e07108dc80100e56065a0a58b18a262a4385d36\": {\n          \"Subscribable\": {},\n          \"Publishable\": {}\n        },\n        \"08b1a2fddb3983984e6e3a5c2aa3af11d1c01232818ac8f2379958e042f0bd0c\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"38a7f49c0e8aa4d179ef6827f541b01346841e78fc6e29c549eff0ee48446737\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"e7b85a867dfb641a9558dc1b24f8af59778868df586c69675b34a4b8a391f461\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"51c8756199cd681d12820e5bfb52a7bf7277bd38fd4a721fe6c127addd9b1e83\": {\n      \"WiFiAwareServices\": {\n        \"8083e76d65267b596418e70c5a3261de4295b0156141d1bea1241b99268f4c7b\": {\n          \"Publishable\": {}\n        }\n      }\n    },\n    \"e74be50ea6f37fc6049c112916fea9d88af33e8ce59fb831b63966ffd15ac36e\": {\n      \"WiFiAwareServices\": {\n        \"db7867db8c5c5aca4dfdb40164b3682014238f67aad882c3b75ef9e431d762ad\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"3a717302bf532940388fd6266eab01804641f060c2ab8c55f53877c484588f47\": {\n      \"WiFiAwareServices\": {\n        \"cbb0aff114829e9878b4bd4f6ded9233dbd99c1b6de821511b89b99b5af60b3d\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"da5638bb367f90b1b7d55c121cb4a5ca5fda9e2c120cd80834d8c85b5807c870\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"55b24a7a30236448d4c6059344a3f8d3c22bd15c0e0e3d2d1e88fade42f14e73\": {\n      \"WiFiAwareServices\": {\n        \"8083e76d65267b596418e70c5a3261de4295b0156141d1bea1241b99268f4c7b\": {\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"3e353312e653d2795f052adc81236ab0f4a6a54685dcf6315ad3858ca1047e00\": {\n      \"WiFiAwareServices\": {\n        \"db7867db8c5c5aca4dfdb40164b3682014238f67aad882c3b75ef9e431d762ad\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    }\n  }\n}"
+ "{\n  \"f4cdc15b2a374d81359d744fb9f7c8d440ffc8487b827988a24c7737f358f605\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"ASKAdvertiser\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"6807a4ab95437a0246e84b6ef0250d0ecc59771f9e37583a8c8f5484f62e4f89\": {\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"NoConsoleUser\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    }\n  },\n  \"e4e2bd48d485e77e7eb05b2eef85ddaf3040d8df3e73a97ff14048a4ae47e5ed\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"macOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    }\n  },\n  \"f15533c3e86b0618a56ea36b66b6af141f823409709e4ac8014efb4914655872\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"ASK\",\n        \"DDUI\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"720c54ffe1def4171b09c2c250927801821ccf7bf457970cbe419bf27d0c8dab\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    }\n  },\n  \"16899a86099e7183dc69e3fb742e7d883d2a81849557a7bd137badfa4875c6c4\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"MARS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"fedc47cc34cf3ed4a75041be388fc7e372c46a3551d73eea1bdb4326b7935af3\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\"\n      ],\n      \"ClientID\": [\n        \"CLI\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    },\n    \"TDS\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    }\n  },\n  \"7c31d95bcf8e1f1756be6a5c7519c55df071e511defc33fce0646fea5084de30\": {\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"visionOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"visionOS\"\n      ]\n    }\n  },\n  \"500a426930046e140b394e9623d82254702a8acf81c03d6a374d15ce63cece9b\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    }\n  },\n  \"aa79df953357eeea4a2b5f2cbdf38a559ee784f1f1c1b799b1385616d8269180\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Terminus\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    }\n  },\n  \"6f054b7b70e2bc463e3a0339baba84ff4245861e0005467537fc820514f4380f\": {\n    \"Publish\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    }\n  },\n  \"be8724fea8d9b696544cedd583ddb2c9bb31017de87e3c689e87a992d4f2dd57\": {\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"NoConsoleUser\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    }\n  },\n  \"3225590b02822b3d3490f7f438e423f66e6b7dbc8b9907ce984d3ee21d6fd37c\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"Migration\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  }\n}"
+ "📶🔴 Activation timed out for: %s [%@]"
+ "📶🔴 Error while activating: %@ [%@]"
+ "📶🔴 [END] Failed to create NAN Interface [%@]"
+ "📶🟢 [END] Created NAN Interface: %s [%@]"
- "%@ User Approval Handler: Accept: %{bool}d, Pairing Info: %s"
- "1c35fee7b539866ce83ee03b2ba1264e4a9875aa62ed515bbac60fc48725cb14"
- "35bb4f3b1aa0fc643dbfb42fb45b8b7e1f2ca9561ff7eba03a2b6f378b6cfb30"
- "Invalid channel_band in preferred channel list"
- "NAN MAC address update to "
- "Secure storage provider set to: %s"
- "WiFiP2P-885.69.4.1 Jul 02 2026 00:07:05"
- "_PPSCreateTelemetryIdentifier"
- "_PPSSendTelemetry"
- "{\n  \"WiFiAwareAllowedBundleIds\": {\n    \"52baba0fca4152ac5024bf9d74749a1eed7900d284fd25b8954cc53bb4edb8b5\": {\n      \"WiFiAwareServices\": {\n        \"95761fd9ea32b663652177da1c2811f5db5577fd8356f62721335e183751c7c6\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"de32037e8dffe83c119fe2959b1a44e17b2e55d951c8a1f4dc4936bfb9bac827\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"05f79d185139d8c8fcfe779e72e13ff9b5ba9d747920677e133bce0655c77842\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"00c705bb3c938c228fd52e45ff5d27abe39e43ddc8fd66d616d3acaab128bda8\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"76738956cfc1c8858c6731603ceff1a5c25a4218f21c394362276669e258b708\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"f4cb95522452d5064b8c49e37f2a8ae26b242b3cb73c8068762cb5bfc39cb114\": {\n          \"Subscribable\": {},\n          \"Publishable\": {}\n        },\n        \"651f489f8780f99a32b079a6272c3ca409875c053799d57fa8e5409b32ba28b8\": {\n          \"Subscribable\": {},\n          \"Publishable\": {}\n        },\n        \"cdc325e4eed12a063908260b60d7924691ed825789751eac83e15197ab6243f6\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"ce5fa79ea74b274096f84de1f17d8c48b0824edeab22b410d01e0d140154341c\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"a9f1aab43993ca029d0640bbc37aaee657a30e06643884cf377b482e1c58b91c\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"22948b48dcaec3a2a3e1e1df8fb82cfa00a69880cda26a71268ec50727a9af06\": {\n      \"WiFiAwareServices\": {\n        \"59997b0650871ec3093f9dd2f12f00d9cfddd6e188ce4f9315a4b2d5b32d6524\": {\n          \"Publishable\": {}\n        }\n      }\n    },\n    \"e6e3c22d0d0c8df03661a7bebe9ee0ab225ba326b6b50a0e36b5f024de94a9e1\": {\n      \"WiFiAwareServices\": {\n        \"269cda7420848482de9ba5aaae900f3639e9babde14804e5124b16de1d8820b9\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"f71c87ef32928fad3c30855e3980991070872d2b4cf93c979adcb703aaa630d6\": {\n      \"WiFiAwareServices\": {\n        \"4e26d457c80115bb45e04a0a03a55717aeac48c6127d9a233759605764853fc0\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        },\n        \"20b713558a6911da7ece25d20ce2949124c088373baaca5febab793276f61726\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"beea4ebe8046ed33bb9015e57e3350ade3f51095a4e77153c6f5f8d0f98e4a61\": {\n      \"WiFiAwareServices\": {\n        \"59997b0650871ec3093f9dd2f12f00d9cfddd6e188ce4f9315a4b2d5b32d6524\": {\n          \"Subscribable\": {}\n        }\n      }\n    },\n    \"1f5e8d52f4acadffc8eaef5d44b0d9fe55ebbad761797ae0fee3be25492bbcff\": {\n      \"WiFiAwareServices\": {\n        \"269cda7420848482de9ba5aaae900f3639e9babde14804e5124b16de1d8820b9\": {\n          \"Publishable\": {},\n          \"Subscribable\": {}\n        }\n      }\n    }\n  }\n}"
- "{\n  \"bf99861b4f887355e344d8451933f3863a8c0a2302a8c652156cb43c63361d7b\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"ASKAdvertiser\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"50a3b06278bafad5d801564b81621b504a19414cc4dde0d7464ffeb3697c6b1c\": {\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"NoConsoleUser\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    }\n  },\n  \"2b01c372dbd0da295af3fb26fe7168fc0a86752a04e5c3eaef53b27948d43261\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"macOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    }\n  },\n  \"856e65e31e4dd5a8fb1fdde3d8d6b1fc67e533d9e3326617be55faa5e96e7828\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"ASK\",\n        \"DDUI\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"61db96db0f6da0490cdc0fa2da570eee292d1d235705402b3b442d854ab77e2a\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"tvOS\"\n      ]\n    }\n  },\n  \"9afd909ff8008972f3db98c548f9a1089a47d46b72bd22c0b27060d519581259\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"MARS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  },\n  \"3c1c0fdd6acb89180944c6bad0e41c1039ddc665bb0c758bc3f0dc5f2329cdfe\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\"\n      ],\n      \"ClientID\": [\n        \"CLI\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    },\n    \"TDS\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\",\n        \"tvOS\",\n        \"visionOS\",\n        \"watchOS\"\n      ]\n    }\n  },\n  \"6c6d7f5202a882e8b514c1760ce1096da0da7a478548c1579146aebef9b10125\": {\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"visionOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"visionOS\"\n      ]\n    }\n  },\n  \"6c1954013a4985c54f72942a9cf83d3f47e9c4a0369d69cb61ec8d292ac87f08\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Airplay\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    }\n  },\n  \"6bad5d75a8f9cb04134b260d34f1d1c22f01b49da49f5bd36f2e8f4a8e551c1e\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ],\n      \"ClientID\": [\n        \"Terminus\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"tvOS\"\n      ]\n    }\n  },\n  \"a8d336f5e3772cb0b1d9ce6b9f51fb402d7c19063fb5691b63f850d2644dcf79\": {\n    \"Publish\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"macOS\"\n      ]\n    }\n  },\n  \"7a9491f1defbbc9e524bde9afeb15b3b711f11c7f641812f615aa06422e7e31c\": {\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"NoConsoleUser\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\",\n        \"macOS\"\n      ]\n    }\n  },\n  \"7ca9f6b5cf4156f6ec883cf9b964aa2310e363c75fea9be8a993b52025f20988\": {\n    \"Pairing\": {\n      \"Platforms\": [\n        \"iOS\"\n      ],\n      \"ClientID\": [\n        \"Migration\"\n      ]\n    },\n    \"Datapath\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Publish\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    },\n    \"Subscribe\": {\n      \"Platforms\": [\n        \"iOS\"\n      ]\n    }\n  }\n}"
- "📶🟢 [END] Create NAN Interface: %s (No Secure Storage Initialization) [%@]"
- "📶🟢 [END] Create NAN Interface: %s [%@]"
```
