## HealthDaemon

> `/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon`

```diff

-4146.0.1.7.0
-  __TEXT.__text: 0x7ce668
+4146.1.11.3.0
+  __TEXT.__text: 0x7cead4
   __TEXT.__auth_stubs: 0x2fd0
-  __TEXT.__objc_methlist: 0x401b4
+  __TEXT.__objc_methlist: 0x401d4
   __TEXT.__const: 0x1c1f5
-  __TEXT.__cstring: 0x7831a
-  __TEXT.__gcc_except_tab: 0x35eb0
-  __TEXT.__oslogstring: 0x3fe2e
+  __TEXT.__cstring: 0x7835f
+  __TEXT.__gcc_except_tab: 0x35ec4
+  __TEXT.__oslogstring: 0x3fecc
   __TEXT.__dlopen_cstrs: 0x1ab
   __TEXT.__ustring: 0x70
-  __TEXT.__unwind_info: 0x20088
+  __TEXT.__unwind_info: 0x20094
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0xc9ed
-  __TEXT.__objc_methname: 0x8ed96
+  __TEXT.__objc_methname: 0x8ee0e
   __TEXT.__objc_methtype: 0x18481
-  __TEXT.__objc_stubs: 0x4fe40
+  __TEXT.__objc_stubs: 0x4fe80
   __DATA_CONST.__got: 0x1b30
   __DATA_CONST.__const: 0x1d930
   __DATA_CONST.__objc_classlist: 0x2a60
   __DATA_CONST.__objc_catlist: 0x458
   __DATA_CONST.__objc_protolist: 0x918
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x67e40
-  __DATA_CONST.__objc_selrefs: 0x19f60
+  __DATA_CONST.__objc_const: 0x67e50
+  __DATA_CONST.__objc_selrefs: 0x19f68
   __DATA_CONST.__objc_arraydata: 0x8708
   __AUTH_CONST.__const: 0xf7d0
   __AUTH_CONST.__objc_const: 0x22768
-  __AUTH_CONST.__cfstring: 0x40ca0
+  __AUTH_CONST.__cfstring: 0x40d00
   __AUTH_CONST.__objc_arrayobj: 0x1e18
   __AUTH_CONST.__objc_intobj: 0x4908
   __AUTH_CONST.__objc_doubleobj: 0x3c0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 00D7B3E2-37CB-327E-9BBA-6056EA92340F
-  Functions: 36581
-  Symbols:   111101
-  CStrings:  45678
+  UUID: 7897D8A2-6945-3D89-92F4-977F2FB37AD3
+  Functions: 36585
+  Symbols:   111111
+  CStrings:  45689
 
Symbols:
+ -[HDAutoBugCaptureReporter reportHDUserCharacteristicsManagerFailureDescription:needsUpdateAfterUnlock:error:]
+ -[HDDemoDataAudiogramSampleGenerator _hearingLevelClassificationForEar:]
+ -[HDProtectedDataOperation delegate]
+ -[HDProtectedDataOperation setDelegate:]
+ ___56-[HDUserCharacteristicsManager _queue_updateUserProfile]_block_invoke.300
+ ___56-[HDUserCharacteristicsManager _queue_updateUserProfile]_block_invoke_2.304
+ ___56-[HDUserCharacteristicsManager _queue_updateUserProfile]_block_invoke_3.308
+ ___62-[HDUserCharacteristicsManager _queue_updateHasWatchOnAccount]_block_invoke.295
+ ___block_literal_global.310
+ ___block_literal_global.312
+ ___block_literal_global.86
+ _objc_msgSend$randomAudiogramSampleWithLeftEarClassification:rightEarClassification:startDate:endDate:device:metadata:
+ _objc_msgSend$reportHDUserCharacteristicsManagerFailureDescription:needsUpdateAfterUnlock:error:
+ _objc_msgSend$set_sourceApplicationBundleIdentifier:
- ___56-[HDUserCharacteristicsManager _queue_updateUserProfile]_block_invoke.297
- ___56-[HDUserCharacteristicsManager _queue_updateUserProfile]_block_invoke_2.301
- ___56-[HDUserCharacteristicsManager _queue_updateUserProfile]_block_invoke_3.305
- ___62-[HDUserCharacteristicsManager _queue_updateHasWatchOnAccount]_block_invoke.292
- ___block_literal_global.309
- ___block_literal_global.96
- _objc_msgSend$randomAudiogramSampleWithClassification:startDate:endDate:device:metadata:
CStrings:
+ "%{public}@: Queue start for types: %{public}@, anchor: %{public}lli"
+ "%{public}@: samplesAdded: %{public}@, anchor: %{public}@"
+ "HealthDemoDataAudiogramLeftEarHearingLevelClassificationOverride"
+ "HealthDemoDataAudiogramRightEarHearingLevelClassificationOverride"
+ "Lani"
+ "Lani Martinez"
+ "LaniMartinez"
+ "Martinez"
+ "Outstanding launches: %{public}@"
+ "ReadFailure"
+ "T@\"<HDProtectedDataOperationDelegate>\",W,N,V_delegate"
+ "move"
+ "randomAudiogramSampleWithLeftEarClassification:rightEarClassification:startDate:endDate:device:metadata:"
+ "reportHDUserCharacteristicsManagerFailureDescription:needsUpdateAfterUnlock:error:"
+ "set_sourceApplicationBundleIdentifier:"
+ "yes"
- "Allison"
- "Allison Cain"
- "AllisonCain"
- "Cain"
- "HDSharedSummaryEntity.m"
- "HealthDemoDataHearingLevelClassification"
- "_predicateForTransactionID:package:names:reuseTransactionID:"
- "randomAudiogramSampleWithClassification:startDate:endDate:device:metadata:"
- "transactionID == nil || reuseTransactionID == nil"

```
