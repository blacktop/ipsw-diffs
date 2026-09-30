## voicebankingd

> `/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/Support/voicebankingd`

```diff

-679.17.0.0.0
-  __TEXT.__text: 0x23fec
+679.18.0.0.0
+  __TEXT.__text: 0x23fe4
   __TEXT.__auth_stubs: 0x1240
   __TEXT.__objc_stubs: 0x840
   __TEXT.__objc_methlist: 0x448

   __TEXT.__swift5_types: 0x38
   __TEXT.__swift5_capture: 0x924
   __TEXT.__objc_methtype: 0x920
-  __TEXT.__cstring: 0xdd7
+  __TEXT.__cstring: 0xd97
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_proto: 0x24

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 07F88710-F400-372C-9150-BD9A9914738B
+  UUID: 25618FFB-C78C-3869-8A7B-46A1E1892504
   Functions: 690
   Symbols:   492
   CStrings:  400
Functions:
~ sub_10000d5cc : 1312 -> 1304
CStrings:
+ "ERROR: Client (PID=%d) should is not allowed connect to voicebankingd. HasEntitlement=%@ AppID=%@"
- "WARN: Client (PID=%d) should not be allowed to connect to voicebankingd. Will allow during development but this will be blocked before release. HasEntitlement=%@ AppID=%@"

```
