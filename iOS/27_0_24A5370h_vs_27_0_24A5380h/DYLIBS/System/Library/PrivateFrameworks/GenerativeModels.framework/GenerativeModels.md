## GenerativeModels

> `/System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels`

```diff

-  __TEXT.__text: 0xcc3d0
+  __TEXT.__text: 0xce85c
   __TEXT.__objc_methlist: 0x478
-  __TEXT.__const: 0xb354
-  __TEXT.__constg_swiftt: 0x211c
-  __TEXT.__swift5_typeref: 0x2ed2
+  __TEXT.__const: 0xb394
+  __TEXT.__constg_swiftt: 0x2144
+  __TEXT.__swift5_typeref: 0x2efe
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0x2348
-  __TEXT.__swift5_fieldmd: 0x2984
+  __TEXT.__swift5_reflstr: 0x2378
+  __TEXT.__swift5_fieldmd: 0x29ac
   __TEXT.__swift5_assocty: 0x620
   __TEXT.__swift5_proto: 0x93c
-  __TEXT.__swift5_types: 0x360
+  __TEXT.__swift5_types: 0x364
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__oslogstring: 0x2e63
-  __TEXT.__cstring: 0x27b3
-  __TEXT.__swift5_capture: 0xdf8
+  __TEXT.__oslogstring: 0x3263
+  __TEXT.__cstring: 0x29c3
+  __TEXT.__swift5_capture: 0xcf8
   __TEXT.__swift_as_entry: 0x1a8
   __TEXT.__swift_as_ret: 0x1bc
   __TEXT.__swift_as_cont: 0x344
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x3160
-  __TEXT.__eh_frame: 0x4f1c
+  __TEXT.__unwind_info: 0x3168
+  __TEXT.__eh_frame: 0x4eac
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x420
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__got: 0xa58
-  __AUTH_CONST.__const: 0x7eb0
+  __DATA_CONST.__got: 0xa78
+  __AUTH_CONST.__const: 0x7c40
   __AUTH_CONST.__objc_const: 0xb88
-  __AUTH_CONST.__auth_got: 0x16c0
-  __AUTH.__objc_data: 0x560
-  __AUTH.__data: 0x820
-  __DATA.__data: 0x1a98
-  __DATA.__bss: 0xc500
+  __AUTH_CONST.__auth_got: 0x16d8
+  __AUTH.__objc_data: 0x410
+  __AUTH.__data: 0x800
+  __DATA.__data: 0x1a48
+  __DATA.__bss: 0xc280
   __DATA.__common: 0x28
-  __DATA_DIRTY.__objc_data: 0xf8
-  __DATA_DIRTY.__data: 0x15f0
-  __DATA_DIRTY.__bss: 0x6080
+  __DATA_DIRTY.__objc_data: 0x248
+  __DATA_DIRTY.__data: 0x1798
+  __DATA_DIRTY.__bss: 0x6300
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CoreEmoji.framework/CoreEmoji
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/GenerativeAgents.framework/GenerativeAgents

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5807
-  Symbols:   248
-  CStrings:  477
+  Functions: 5834
+  Symbols:   255
+  CStrings:  495
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __AUTH_CONST.__objc_const : content changed
Symbols:
+ _SecKeyCreateWithData
+ _SecKeyVerifySignature
+ _kSecAttrKeyClass
+ _kSecAttrKeyClassPublic
+ _kSecAttrKeyType
+ _kSecAttrKeyTypeRSA
+ _kSecKeyAlgorithmRSASignatureMessagePKCS1v15SHA256
+ _objc_retain_x23
+ _objc_retain_x26
+ _swift_unexpectedError
- _CFPreferencesCopyValue
- _getpwuid
- _kCFPreferencesCurrentHost
CStrings:
+ "Forced waitlist profile override has no attestation; rejecting"
+ "Forced waitlist profile override is set but payload is absent or not Data; rejecting"
+ "Forced waitlist profile override payload verified but is not a decodable WaitlistStatus.Value"
+ "Forced waitlist profile override signature invalid; rejecting"
+ "Forced waitlist profile override verified but value is not .accepted; ignoring"
+ "Forced waitlist profile override verified; honoring .accepted"
+ "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuuoHJarXiW7YiznhKWr4lYAasR4U+Npcx40Qmr7dR5vmOXFLKP4ivBqn8a5mtb7GIc9siLEqeBKCZBw0+eyQ9QKua5Uo5H+NguS9FWskFPuuZv/NjEWQ2s9FoqaA0t7s8X2FsKQCPAAE01HCCfm7HHjaWBqWtOguevYvZYc+/y54heeAXX407JBsDSqwiKTVN5hLxJXtpNDfjyrHIQZsluutsz5wqXdGNRTn3S1iWN55l30aOFR4MDgS2cprnuOcIu89W/4K2dIiZ7R1ttke4bRev+aWFBxtevgsjsRUXshHAdi1y+etcjNxwNkkeqvH2qxBIK8aSPzEzCjS797SeQIDAQAB"
+ "Migrating legacy forcedWaitlistStatus override → secureAvailabilityDomain (value=%{public}s)"
+ "Returning cached enhanced Siri availability."
+ "Returning cached enhanced Siri boot state."
+ "Returning cached enhancedSiriWasEverAvailable."
+ "Skipping legacy forcedWaitlistStatus override migration: failed to decode legacy data"
+ "com.apple.gms.availability.forcedWaitlistStatus.attestation"
+ "com.apple.gms.availability.secureForcedWaitlistStatusOverride"
+ "forcedWaitlistStatus: %{public}s (MDM profile)"
+ "forcedWaitlistStatus: %{public}s (gmstool override)"
+ "forcedWaitlistStatus: nil"
+ "setSecureForcedWaitlistStatusOverride: not allowed on non-internal builds"

```
