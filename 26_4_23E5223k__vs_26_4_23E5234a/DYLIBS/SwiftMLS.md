## SwiftMLS

> `/System/Library/PrivateFrameworks/SwiftMLS.framework/SwiftMLS`

```diff

-195.100.74.0.1
-  __TEXT.__text: 0x2b12e4
-  __TEXT.__auth_stubs: 0x2f90
+195.100.77.0.0
+  __TEXT.__text: 0x2c3da8
+  __TEXT.__auth_stubs: 0x2fa0
   __TEXT.__objc_methlist: 0x80
-  __TEXT.__const: 0x251a0
-  __TEXT.__constg_swiftt: 0x47c0
-  __TEXT.__swift5_typeref: 0x38a4
-  __TEXT.__swift5_reflstr: 0x5831
-  __TEXT.__swift5_fieldmd: 0x5e40
-  __TEXT.__swift5_builtin: 0x118
+  __TEXT.__const: 0x24bb8
+  __TEXT.__constg_swiftt: 0x481c
+  __TEXT.__swift5_typeref: 0x38c0
+  __TEXT.__swift5_reflstr: 0x58f1
+  __TEXT.__swift5_fieldmd: 0x5e88
+  __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_assocty: 0xb08
   __TEXT.__swift5_proto: 0xdc0
   __TEXT.__swift5_types: 0x6a4
   __TEXT.__swift5_capture: 0x2a4
   __TEXT.__swift5_protos: 0x40
-  __TEXT.__oslogstring: 0x5502
-  __TEXT.__cstring: 0x3add
+  __TEXT.__oslogstring: 0x5a22
+  __TEXT.__cstring: 0x3c1d
   __TEXT.__swift_as_entry: 0x5fc
-  __TEXT.__swift_as_ret: 0xb94
-  __TEXT.__swift5_mpenum: 0x140
-  __TEXT.__unwind_info: 0xa250
-  __TEXT.__eh_frame: 0x1fe78
+  __TEXT.__swift_as_ret: 0xb98
+  __TEXT.__swift5_mpenum: 0x138
+  __TEXT.__unwind_info: 0xa2c8
+  __TEXT.__eh_frame: 0x20148
   __TEXT.__objc_classname: 0x38b
-  __TEXT.__objc_methname: 0x65d
+  __TEXT.__objc_methname: 0x69d
   __TEXT.__objc_methtype: 0x71
   __TEXT.__objc_stubs: 0x300
-  __DATA_CONST.__got: 0x948
-  __DATA_CONST.__const: 0x100
+  __DATA_CONST.__got: 0x950
+  __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xd8
-  __AUTH_CONST.__auth_got: 0x17d0
-  __AUTH_CONST.__const: 0xc740
-  __AUTH_CONST.__objc_const: 0x10a0
+  __AUTH_CONST.__auth_got: 0x17d8
+  __AUTH_CONST.__const: 0xc5b8
+  __AUTH_CONST.__objc_const: 0x10e0
   __AUTH.__objc_data: 0x2d8
-  __AUTH.__data: 0x47c8
-  __DATA.__data: 0x3250
+  __AUTH.__data: 0x49f0
+  __DATA.__data: 0x3310
   __DATA.__bss: 0x1b300
-  __DATA.__common: 0x560
+  __DATA.__common: 0x570
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: BE0594FF-D821-3A83-86FE-643527E34614
-  Functions: 10383
-  Symbols:   2316
-  CStrings:  872
+  UUID: 9ED6A971-7615-3B26-A2A5-76325478C29C
+  Functions: 10436
+  Symbols:   2310
+  CStrings:  900
 
Symbols:
+ ___swift_memcpy385_8
+ _keypath_set.45Tm
+ _symbolic _____Sg s5Int64V
+ _symbolic _____Sg s6UInt16V
+ _symbolic _____Sg_ABt 8SwiftMLS0B0O8IdentityO07SigningC0V
- ___swift_memcpy113_8
- ___swift_memcpy358_8
- _get_enum_tag_for_layout_string 8SwiftMLS0B0O5GroupO6MemberVSg
- _get_enum_tag_for_layout_string 8SwiftMLS0B0O8MLSErrorO
- _keypath_set.52Tm
- _type_layout_string 8SwiftMLS0B0O5GroupO12MemberUpdateV
- _type_layout_string 8SwiftMLS0B0O5GroupO6MemberV
- _type_layout_string 8SwiftMLS0B0O8MLSErrorO
CStrings:
+ "%s Calculated commitment for Continuity Token: %s"
+ "%s Generating new Continuity Token"
+ "%s group has cotinuity token"
+ "%s: Creating a new era for group ID %s, trying to fetch the group"
+ "%s: Not in enforcement mode, accepting new token."
+ "%s: Received a new continuity token in group info that does not match our existing one."
+ "%s: Using new continuity token from group info"
+ "Adding expiry testing extension to KeyPackage: client=%s, server=%s"
+ "Adding expiry testing extension to LeafNode: client=%s, server=%s"
+ "Credential DOES NOT require update for remainingValidity: %f\ncredLifetime: %s -> %s\npiLifetime: %s -> %s\nacsNotAfter: %s"
+ "Credential requires update for remainingValidity: %f\ncredLifetime: %s -> %s\npiLifetime: %s -> %s\nacsNotAfter: %s"
+ "Expiry testing mode enabled"
+ "Leaf node has manual expiry extension"
+ "Read client expiry from LeafNode: %s"
+ "Setting testing expiry times: client=%s, server=%s"
+ "Storing client state in storage, state is %s, groupIDs: %s"
+ "Testing credential DOES NOT require update for remainingValidity: %f, expiry=%s"
+ "Testing credential requires update for remainingValidity: %f, expiry=%s"
+ "Verifying credential validity for testing time: %s"
+ "ciphersuiteID generation "
+ "committer proposer "
+ "committer proposer shouldRejoin "
+ "currentEpoch messageEpoch "
+ "currentEra currentEpoch messageEra messageEpoch "
+ "loadCredential: Using client testing expiry: %s"
+ "loadCredential: Using client testing time: %s"
+ "received expected "
+ "requestedGeneration currentGeneration "
+ "testingIdentityClientExpiry"
+ "testingIdentitySeverExpiry"
+ "welcomeSuite keyPackageSuite "
- "continuityToken: %s"
- "continuityToken: %s; ext.token: %s"
- "currentToken: %s, newToken: %s"

```
