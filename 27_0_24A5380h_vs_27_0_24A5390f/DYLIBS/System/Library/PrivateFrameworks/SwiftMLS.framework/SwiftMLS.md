## SwiftMLS

> `/System/Library/PrivateFrameworks/SwiftMLS.framework/SwiftMLS`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-341.0.13.0.0
-  __TEXT.__text: 0x2adf80
+341.0.16.0.0
+  __TEXT.__text: 0x2b6b88
   __TEXT.__objc_methlist: 0x80
-  __TEXT.__const: 0x24d50
-  __TEXT.__constg_swiftt: 0x4908
-  __TEXT.__swift5_typeref: 0x38b8
-  __TEXT.__swift5_reflstr: 0x5bb1
-  __TEXT.__swift5_fieldmd: 0x6000
+  __TEXT.__const: 0x24ff0
+  __TEXT.__constg_swiftt: 0x4974
+  __TEXT.__swift5_typeref: 0x3972
+  __TEXT.__swift5_reflstr: 0x5d41
+  __TEXT.__swift5_fieldmd: 0x612c
   __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_assocty: 0xb08
-  __TEXT.__swift5_proto: 0xdc4
-  __TEXT.__swift5_types: 0x6b4
+  __TEXT.__swift5_proto: 0xdc8
+  __TEXT.__swift5_types: 0x6c0
   __TEXT.__swift5_capture: 0x2a4
   __TEXT.__swift5_protos: 0x40
-  __TEXT.__oslogstring: 0x62e8
-  __TEXT.__cstring: 0x3e8d
-  __TEXT.__swift_as_entry: 0x61c
-  __TEXT.__swift_as_ret: 0xc10
-  __TEXT.__swift_as_cont: 0x15c0
+  __TEXT.__oslogstring: 0x6788
+  __TEXT.__cstring: 0x3edd
+  __TEXT.__swift_as_entry: 0x630
+  __TEXT.__swift_as_ret: 0xc38
+  __TEXT.__swift_as_cont: 0x1614
   __TEXT.__swift5_mpenum: 0x138
-  __TEXT.__unwind_info: 0xa258
-  __TEXT.__eh_frame: 0x20420
+  __TEXT.__unwind_info: 0xa638
+  __TEXT.__eh_frame: 0x20f70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xe0
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xc950
+  __AUTH_CONST.__const: 0xc9d0
   __AUTH_CONST.__objc_const: 0x1100
-  __AUTH_CONST.__auth_got: 0x18d8
+  __AUTH_CONST.__auth_got: 0x18d0
   __AUTH.__objc_data: 0x48
-  __AUTH.__data: 0x22d0
-  __DATA.__data: 0x3090
-  __DATA.__bss: 0x1ae80
+  __AUTH.__data: 0x2420
+  __DATA.__data: 0x3100
+  __DATA.__bss: 0x1af00
   __DATA.__common: 0x4c0
   __DATA_DIRTY.__objc_data: 0x290
   __DATA_DIRTY.__data: 0x2ac8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 10525
-  Symbols:   2134
-  CStrings:  823
+  Functions: 10687
+  Symbols:   2146
+  CStrings:  837
 
Symbols:
+ _symbolic SDy__________G 8SwiftMLS0B0O9LeafIndexV AC18SenderVerificationV
+ _symbolic _____ 8SwiftMLS0B0O10EpochStateO
+ _symbolic _____ 8SwiftMLS0B0O18SenderVerificationV
+ _symbolic _____ 8SwiftMLS0B0O19EpochDecryptSecretsV
+ _symbolic _____3key______5valuet 8SwiftMLS0B0O9LeafIndexV AC18SenderVerificationV
+ _symbolic _____Sg 8SwiftMLS0B0O10EpochStateO
+ _symbolic ___________Sgt 8SwiftMLS0B0O5GroupOADC8EraEpochV AC0E5StateO
+ _symbolic ___________Sgt s5Int64V 8SwiftMLS0C0O10EpochStateO
+ _symbolic ___________t 8SwiftMLS0B0O9LeafIndexV AC18SenderVerificationV
+ _symbolic _____y_____3key______5valuetG s23_ContiguousArrayStorageC 8SwiftMLS0E0O9LeafIndexV AE18SenderVerificationV
+ _symbolic _____y__________G s18_DictionaryStorageC 8SwiftMLS0D0O9LeafIndexV AE18SenderVerificationV
+ _symbolic _____y___________SgtG s23_ContiguousArrayStorageC 8SwiftMLS0E0O5GroupOAFC8EraEpochV AE0H5StateO
+ _symbolic _____y___________SgtG s23_ContiguousArrayStorageC s5Int64V 8SwiftMLS0F0O10EpochStateO
+ _symbolic _____y___________tG s23_ContiguousArrayStorageC 8SwiftMLS0E0O9LeafIndexV AE18SenderVerificationV
+ _type_layout_string 8SwiftMLS0B0O18SenderVerificationV
- _swift_deallocBox
- _symbolic ___________Sgt s5Int64V 8SwiftMLS0C0O10GroupStateV
- _symbolic _____y___________SgtG s23_ContiguousArrayStorageC s5Int64V 8SwiftMLS0F0O10GroupStateV
CStrings:
+ "%s: Continuity token commitment missing, but groupMetadataKeysRequested is set on the GroupInfo — §2.B token-loss window, proceeding without commitment verification"
+ "%s: Missing sender leaf when processing prior-epoch single-recipient application message"
+ "%s: Unsupported secret payload type at prior epoch: %hu, ignoring"
+ "%s: maybeStateForEpoch(%s) found .prior shape — caller cannot consume EpochDecryptSecrets via the GroupState API"
+ "%s: processing inner encryption of single-recipient application at prior epoch %s with messageID %s"
+ "%s: received a double-wrapped 1:1 encrypted message at prior epoch %s"
+ "%s: received prior-epoch application message from index %u"
+ "%s: received prior-epoch signed message from index %u"
+ "%s: receiver's HPKE key in prior epoch %s differs from current state, failing to avoid self-heal loop"
+ "%s: rejecting proposal at prior epoch %s"
+ "%s: stateForEpoch(%s) found .prior shape — caller cannot consume EpochDecryptSecrets via the GroupState API"
+ "%s: the single-recipient message was not for us, so we can safely ignore it"
+ "newMemberCommit signature verification is not valid at a prior epoch"
+ "state epoch authenticator: %s"
```
