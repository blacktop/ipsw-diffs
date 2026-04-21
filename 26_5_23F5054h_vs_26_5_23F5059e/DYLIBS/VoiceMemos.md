## VoiceMemos

> `/System/Library/PrivateFrameworks/VoiceMemos.framework/VoiceMemos`

```diff

-1378.7.0.0.0
-  __TEXT.__text: 0x49d8c
+1380.0.0.0.0
+  __TEXT.__text: 0x49f78
   __TEXT.__auth_stubs: 0xbb0
-  __TEXT.__objc_methlist: 0x3e34
+  __TEXT.__objc_methlist: 0x3e3c
   __TEXT.__gcc_except_tab: 0x1824
   __TEXT.__const: 0x290
-  __TEXT.__cstring: 0x64a2
+  __TEXT.__cstring: 0x64d9
   __TEXT.__oslogstring: 0x2ab9
   __TEXT.__ustring: 0x22
-  __TEXT.__unwind_info: 0x1a88
+  __TEXT.__unwind_info: 0x1a90
   __TEXT.__objc_classname: 0x82d
-  __TEXT.__objc_methname: 0xbfbf
-  __TEXT.__objc_methtype: 0x15bc
-  __TEXT.__objc_stubs: 0x90c0
+  __TEXT.__objc_methname: 0xc03a
+  __TEXT.__objc_methtype: 0x15d3
+  __TEXT.__objc_stubs: 0x9100
   __DATA_CONST.__got: 0x690
   __DATA_CONST.__const: 0x1d98
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2eb8
+  __DATA_CONST.__objc_selrefs: 0x2ec8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0xe0
   __AUTH_CONST.__auth_got: 0x5f0
   __AUTH_CONST.__const: 0x8a0
-  __AUTH_CONST.__cfstring: 0x3360
+  __AUTH_CONST.__cfstring: 0x33a0
   __AUTH_CONST.__objc_const: 0x5bf0
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x118

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B5031BF3-7AA4-3883-8721-CEF97C271EA3
-  Functions: 1930
-  Symbols:   6748
-  CStrings:  3498
+  UUID: A129DC80-CE48-377F-8251-B2A04745391F
+  Functions: 1932
+  Symbols:   6754
+  CStrings:  3505
 
Symbols:
+ +[RCCaptureFormat AVAssetAuthoringMetadataWithCreationDate:title:uniqueID:previousTitleLength:musicMemoMetadata:]
+ GCC_except_table70
+ _RCApplyPreviousTitleLengthHackIfNeeded
+ ___block_literal_global.135
+ ___block_literal_global.142
+ ___block_literal_global.168
+ ___block_literal_global.171
+ ___block_literal_global.194
+ ___block_literal_global.96
+ _objc_msgSend$AVAssetAuthoringMetadataWithCreationDate:title:uniqueID:previousTitleLength:musicMemoMetadata:
+ _objc_msgSend$lengthOfBytesUsingEncoding:
- ___block_literal_global.129
- ___block_literal_global.156
- ___block_literal_global.191
- ___block_literal_global.90
- ___block_literal_global.93
Functions:
~ -[RCCloudRecording synchronizeRecordingMetadata] : 504 -> 540
+ _RCApplyPreviousTitleLengthHackIfNeeded
~ -[RCCloudRecording setPlayable:] : 480 -> 492
~ +[RCCaptureFormat AVAssetAuthoringMetadataWithCreationDate:title:uniqueID:musicMemoMetadata:] : 664 -> 20
+ +[RCCaptureFormat AVAssetAuthoringMetadataWithCreationDate:title:uniqueID:previousTitleLength:musicMemoMetadata:]
~ +[RCCaptureFormat AVAssetAuthoringMetadataWithRecordingMetadata:] : 216 -> 252
~ -[AVAsset(RCAdditions) rc_recordingMetadata] : 576 -> 644
CStrings:
+ "@56@0:8@16@24@32@40@48"
+ "AVAssetAuthoringMetadataWithCreationDate:title:uniqueID:previousTitleLength:musicMemoMetadata:"
+ "com.apple.iTunes.previous-title-length"
+ "lengthOfBytesUsingEncoding:"
+ "prevTitleLength"

```
