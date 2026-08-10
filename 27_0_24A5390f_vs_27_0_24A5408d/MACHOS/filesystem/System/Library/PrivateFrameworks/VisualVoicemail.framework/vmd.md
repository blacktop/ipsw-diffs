## vmd

> `/System/Library/PrivateFrameworks/VisualVoicemail.framework/vmd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-956.0.0.0.0
-  __TEXT.__text: 0xc0fa4
-  __TEXT.__auth_stubs: 0x18a0
-  __TEXT.__objc_stubs: 0xe2a0
+958.0.0.0.0
+  __TEXT.__text: 0xc2a08
+  __TEXT.__auth_stubs: 0x1900
+  __TEXT.__objc_stubs: 0xe280
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0x7e74
-  __TEXT.__cstring: 0x491a
-  __TEXT.__objc_classname: 0xe4a
-  __TEXT.__objc_methname: 0x12d7f
-  __TEXT.__objc_methtype: 0x35da
+  __TEXT.__objc_methlist: 0x7ed4
+  __TEXT.__cstring: 0x48ba
+  __TEXT.__objc_classname: 0xe7a
+  __TEXT.__objc_methname: 0x12ed1
+  __TEXT.__objc_methtype: 0x3669
   __TEXT.__const: 0x522
-  __TEXT.__gcc_except_tab: 0x10d1c
-  __TEXT.__oslogstring: 0x16337
+  __TEXT.__gcc_except_tab: 0x12e7c
+  __TEXT.__oslogstring: 0x161b7
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x3b
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x49a0
+  __TEXT.__unwind_info: 0x4e40
   __TEXT.__eh_frame: 0x40
-  __DATA_CONST.__const: 0x34e0
-  __DATA_CONST.__cfstring: 0x5640
-  __DATA_CONST.__objc_classlist: 0x2f8
-  __DATA_CONST.__objc_catlist: 0x58
+  __DATA_CONST.__const: 0x33a8
+  __DATA_CONST.__cfstring: 0x55c0
+  __DATA_CONST.__objc_classlist: 0x308
+  __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x2c0
+  __DATA_CONST.__objc_superrefs: 0x2c8
   __DATA_CONST.__objc_intobj: 0x378
   __DATA_CONST.__objc_arraydata: 0x130
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA_CONST.__auth_got: 0xc68
-  __DATA_CONST.__got: 0x828
+  __DATA_CONST.__auth_got: 0xc98
+  __DATA_CONST.__got: 0x838
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA.__objc_const: 0x12cf0
-  __DATA.__objc_selrefs: 0x4820
-  __DATA.__objc_ivar: 0x7d0
-  __DATA.__objc_data: 0x1e10
+  __DATA.__objc_const: 0x12ec0
+  __DATA.__objc_selrefs: 0x4828
+  __DATA.__objc_ivar: 0x7e8
+  __DATA.__objc_data: 0x1eb0
   __DATA.__data: 0x1220
-  __DATA.__bss: 0x640
+  __DATA.__bss: 0x5e0
   __DATA.__common: 0x4
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3605
-  Symbols:   709
-  CStrings:  5898
+  Functions: 3596
+  Symbols:   716
+  CStrings:  5903
 
Symbols:
+ _OBJC_CLASS_$_VMVoicemailData
+ _OBJC_CLASS_$_VMVoicemailDataContainer
+ _VVVerifierChangedNotification
+ __Z31VMVoicemailGetDataFileExtensionv
+ __Z32VMVoicemailDataPathForIdentifierP8NSStringm
+ __Z40VMVoicemailGetSummarizationFileExtensionv
+ __Z40VMVoicemailGetTranscriptionFileExtensionv
+ __Z41VMVoicemailSummarizationPathForIdentifierP8NSStringm
+ __Z41VMVoicemailTranscriptionPathForIdentifierP8NSStringm
- _OBJC_CLASS_$_VMMutableVoicemail
- _OBJC_CLASS_$_VMVoicemail
CStrings:
+ "\v"
+ "%s#E Failed to unarchive transcript for voicemail with identifier: %lu: %@"
+ "%s#I Queueing voicemail for retranscription: %lu"
+ "%s#I Transcription cancelled for voicemail with identifier: %lu."
+ "@\"VMSharedStore\""
+ "B24@0:8Q16"
+ "B24@?0@\"NSNumber\"8@\"NSDictionary\"16"
+ "T@\"NSString\",R,N,V_voicemailDirectoryPath"
+ "T@\"NSURL\",R,N,V_databaseFileURL"
+ "T@\"NSURL\",R,N,V_notificationDirectoryURL"
+ "T@\"NSURL\",R,N,V_voicemailDirectoryURL"
+ "T@\"VMSharedStore\",R,N,V_sharedStore"
+ "T@\"VMSharedStore\",W,N,V_voicemailStore"
+ "VMDCarrierAccountDataSource.mm"
+ "VMManager.mm"
+ "VMVoicemailDataFactory"
+ "VMVoicemailStorePaths"
+ "_databaseFileURL"
+ "_notificationDirectoryURL"
+ "_sharedStore"
+ "_voicemailDirectoryPath"
+ "_voicemailDirectoryURL"
+ "_voicemailStore"
+ "dataForRecord:forContexts:andIsoCodes:"
+ "dataWithContentsOfFile:"
+ "databaseFileURL"
+ "initWithVoicemails:"
+ "notificationDirectoryURL"
+ "prepareVoicemailsForMailboxType:read:limit:offset:completion:"
+ "processTranscriptForIdentifier:"
+ "q24@?0@\"VMVoicemailData\"8@\"VMVoicemailData\"16"
+ "setVoicemailStore:"
+ "sharedStore"
+ "sortUsingComparator:"
+ "unarchivedObjectOfClass:fromData:error:"
+ "v16@?0@\"VMVoicemailDataContainer\"8"
+ "v24@0:8@\"VMVoicemailDataContainer\"16"
+ "v24@0:8@?<v@?@\"VMVoicemailDataContainer\"@\"NSString\">16"
+ "v32@?0@\"NSNumber\"8Q16^B24"
+ "v48@0:8q16q24q32@?<v@?@\"VMVoicemailDataContainer\"@\"NSString\">40"
+ "v52@0:8q16B24q28q36@?<v@?@\"VMVoicemailDataContainer\"@\"NSString\">44"
+ "v56@0:8q16@24q32q40@?48"
+ "vmdb.shr"
+ "voicemailDirectoryPath"
+ "voicemailDirectoryURL"
+ "voicemailStore"
+ "voicemailsUpdated:basePath:"
- "\n"
- "%@\n"
- "%@%d.amr"
- "%@/"
- "%s#E Error unarchiving summarization metadata dictionary as file name empty."
- "%s#E Error unarchiving summarization metadata dictionary: %@"
- "%s#I Got previous attempts of: %@, will check to see if %lu is in it."
- "%s#I Noted in plist that we have attempted to transcribe voicemail with identifier: %lu."
- "%s#I Queueing voicemail for retranscription: %@"
- "%s#I Removing from plist that we have attempted to transcribe voicemail with identifier: %lu."
- "%s#I Returning NO since the task dictionary doesn't exist."
- "%s#I Transcription cancelled for voicemail: %@. Removing from attempted voicemails."
- ".amr"
- ".summary"
- ".transcript"
- "B24@?0@\"VMVoicemail\"8@\"NSDictionary\"16"
- "VMDCarrierAccountDataSource.m"
- "VMManager.m"
- "VMVoicemailTranscriptionPreviouslyAttemptedVoicemails"
- "alreadyAttemptedVoicemailTranscriptionForVoicemail:"
- "cancelAttemptedVoicemailTranscriptionForVoicemail:"
- "fullPath"
- "hasDirectoryPath"
- "messageForRecord:forContexts:andIsoCodes:"
- "orderedSet"
- "orderedSetWithCapacity:"
- "processTranscriptForVoicemail:"
- "q24@?0@\"VMVoicemail\"8@\"VMVoicemail\"16"
- "setAttemptedVoicemailTranscriptionForVoicemail:"
- "setSummarizationMetaDataURL:"
- "setTranscriptionURL:"
- "sortedArrayUsingComparator:"
- "summarizationMetaDataURL"
- "v16@?0@\"NSOrderedSet\"8"
- "v24@0:8@\"NSOrderedSet\"16"
- "v24@0:8@?<v@?@\"NSOrderedSet\">16"
- "v32@?0@\"VMVoicemail\"8Q16^B24"
- "v48@0:8q16q24q32@?<v@?@\"NSArray\">40"
- "v52@0:8q16B24q28q36@?<v@?@\"NSArray\">44"
- "vm.shared.store"
- "vmsg.cat"
- "voicemailsUpdated:"
```
