## voicebankingd

> `/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/Support/voicebankingd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_entry`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`

```diff

-727.3.3.0.0
-  __TEXT.__text: 0x22584
-  __TEXT.__auth_stubs: 0x13e0
-  __TEXT.__objc_stubs: 0x840
-  __TEXT.__objc_methlist: 0x448
-  __TEXT.__swift5_typeref: 0x600
-  __TEXT.__const: 0x790
-  __TEXT.__oslogstring: 0x192f
-  __TEXT.__objc_classname: 0x1ee
-  __TEXT.__objc_methname: 0xfdd
-  __TEXT.__constg_swiftt: 0x2b0
-  __TEXT.__swift5_reflstr: 0x37f
-  __TEXT.__swift5_fieldmd: 0x238
-  __TEXT.__swift5_types: 0x38
-  __TEXT.__swift5_capture: 0x8f4
+727.3.12.0.0
+  __TEXT.__text: 0x24084
+  __TEXT.__auth_stubs: 0x1460
+  __TEXT.__objc_stubs: 0x8a0
+  __TEXT.__objc_methlist: 0x478
+  __TEXT.__const: 0x7f0
+  __TEXT.__swift5_typeref: 0x64c
+  __TEXT.__oslogstring: 0x1a8f
+  __TEXT.__objc_methname: 0x109d
+  __TEXT.__objc_classname: 0x21e
+  __TEXT.__constg_swiftt: 0x2dc
+  __TEXT.__swift5_reflstr: 0x3cf
+  __TEXT.__swift5_fieldmd: 0x260
+  __TEXT.__swift5_types: 0x3c
+  __TEXT.__swift5_capture: 0x934
   __TEXT.__objc_methtype: 0x920
-  __TEXT.__cstring: 0xd37
+  __TEXT.__cstring: 0xda7
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_proto: 0x24

   __TEXT.__swift_as_cont: 0x2c
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x7e8
+  __TEXT.__unwind_info: 0x838
   __TEXT.__eh_frame: 0x698
-  __DATA_CONST.__const: 0x1c08
-  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__const: 0x1cd0
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__auth_got: 0x9f8
-  __DATA_CONST.__got: 0x368
-  __DATA_CONST.__auth_ptr: 0x288
-  __DATA.__objc_const: 0x840
-  __DATA.__objc_selrefs: 0x390
-  __DATA.__objc_data: 0x370
-  __DATA.__data: 0x708
-  __DATA.__common: 0x8
+  __DATA_CONST.__auth_got: 0xa38
+  __DATA_CONST.__got: 0x370
+  __DATA_CONST.__auth_ptr: 0x298
+  __DATA.__objc_const: 0x8c8
+  __DATA.__objc_selrefs: 0x3b0
+  __DATA.__objc_data: 0x430
+  __DATA.__data: 0x750
+  __DATA.__common: 0x18
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 681
-  Symbols:   516
-  CStrings:  395
+  Functions: 708
+  Symbols:   529
+  CStrings:  406
 
Symbols:
+ _$s31TextToSpeechVoiceBankingSupport18TTSVBAccessManagerC12eventHandleryAC5EventOcSgvsTj
+ _$s31TextToSpeechVoiceBankingSupport18TTSVBAccessManagerC5EventO2eeoiySbAE_AEtFZ
+ _$sSS10describingSSx_tclufC
+ _$ss11AnyHashableVMn
+ _$ss18_DictionaryStorageC4copy8originalAByxq_Gs05__RawaB0C_tFZ
+ _$ss18_DictionaryStorageC6resize8original8capacity4moveAByxq_Gs05__RawaB0C_SiSbtFZ
+ _$ss18_DictionaryStorageCMn
+ _$ss53KEY_TYPE_OF_DICTIONARY_VIOLATES_HASHABLE_REQUIREMENTSys5NeverOypXpF
+ _NSXPCStoreEntitlementNamesKey
+ _OBJC_CLASS_$_NSXPCStoreServerRequestHandlingPolicy
+ _OBJC_METACLASS_$_NSXPCStoreServerRequestHandlingPolicy
+ _swift_once
+ _swift_release_x27
CStrings:
+ "Handling failed sync setup event. iCloud TCC access=%s error=%s. Will restore Personal Voices still found locally on device"
+ "Rejecting XPC store connection from client (PID=%u) missing entitlement %{public}s"
+ "_TtC13voicebankingd26VoiceBankingXPCStorePolicy"
+ "auditToken"
+ "cloudKitSetupDidFail"
+ "didObserveCloudKitAccessNotAllowed"
+ "entitlements"
+ "error"
+ "iCloud TCC access changed: %s cloudKitSetupDidFail=%{bool}d"
+ "iCloud TCC access was restored after CloudKit setup failed. Exiting to restart CloudKit setup."
+ "iCloud TCC access was restored after CloudKit setup failed. Will exit gracefully to allow restart with a fresh CloudKit setup."
+ "iCloud TCC access: %s isCloudSyncAvailable=%{bool}d"
+ "shouldAcceptConnectionsFromClientWithContext:"
+ "voicebankingd: CloudKit setup did not finish successfully. iCloud TCC access="
- "Handling failed sync wetup event. Will restore Personal Voices still found locally on device"
- "iCloud TCC access: %s"
- "voicebankingd: CloudKit setup did not finish successfully"
```
