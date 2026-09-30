## com.apple.SpeechRecognitionCore.speechrecognitiond

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond`

```diff

-6.3.25.5.0
-  __TEXT.__text: 0xbe3b4
-  __TEXT.__auth_stubs: 0x2750
+6.3.30.7.0
+  __TEXT.__text: 0xbb6fc
+  __TEXT.__auth_stubs: 0x2710
   __TEXT.__objc_stubs: 0x3880
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x1380
-  __TEXT.__const: 0x596f
-  __TEXT.__gcc_except_tab: 0x814c
+  __TEXT.__objc_methlist: 0x16d4
+  __TEXT.__const: 0x599f
+  __TEXT.__gcc_except_tab: 0x81c4
   __TEXT.__objc_methname: 0x4a85
-  __TEXT.__cstring: 0x3e81
-  __TEXT.__oslogstring: 0x4c8b
+  __TEXT.__cstring: 0x3be1
+  __TEXT.__oslogstring: 0x4d7b
   __TEXT.__objc_classname: 0x307
   __TEXT.__objc_methtype: 0xf40
   __TEXT.__dlopen_cstrs: 0xc0

   __TEXT.__swift5_fieldmd: 0x220
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__unwind_info: 0x4038
-  __TEXT.__eh_frame: 0xa70
-  __DATA_CONST.__auth_got: 0x13c0
-  __DATA_CONST.__got: 0x6d0
+  __TEXT.__swift_as_entry: 0x50
+  __TEXT.__swift_as_ret: 0x54
+  __TEXT.__unwind_info: 0x3f90
+  __TEXT.__eh_frame: 0xad0
+  __DATA_CONST.__auth_got: 0x13a0
+  __DATA_CONST.__got: 0x6e8
   __DATA_CONST.__auth_ptr: 0x158
-  __DATA_CONST.__const: 0x6a00
+  __DATA_CONST.__const: 0x69c0
   __DATA_CONST.__cfstring: 0x1ce0
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_intobj: 0xa8
-  __DATA.__objc_const: 0x3b58
-  __DATA.__objc_selrefs: 0x1150
+  __DATA.__objc_const: 0x35d8
+  __DATA.__objc_selrefs: 0x1250
   __DATA.__objc_ivar: 0x174
-  __DATA.__objc_data: 0xf08
+  __DATA.__objc_data: 0xe90
   __DATA.__data: 0xd78
-  __DATA.__bss: 0xb20
-  __DATA.__common: 0x88
+  __DATA.__bss: 0xb10
+  __DATA.__common: 0x68
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3532
-  Symbols:   1327
-  CStrings:  2189
+  Functions: 3501
+  Symbols:   1328
+  CStrings:  2178
 
Symbols:
+ __ZN9RDQSRPeer20GetCommandsInGrammarEPvP9__CFArray
+ __ZN9RDQSRPeer21CopyCommandsInGrammarEPv
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ _objc_retain_x26
- __ZNKSt9exception4whatEv
- __ZNSt9exceptionD2Ev
- __ZTISt9exception
- _objc_retain_x24
- _objc_retain_x9
CStrings:
+ "Activating Grammar  -> lmid = %llu, grammarID = %zu, %@"
+ "Deactivating Grammar  -> lmid = %llu, grammarID = %zu, %@"
+ "Deactivating Grammar after end of utterance -> lmid = %llu, grammarID = %zu, %@"
+ "LoadCustomVocabulary vocabEntries all locales count: %ld"
+ "LoadCustomVocabulary vocabEntries ingested count: %ld"
+ "Match Result:: isLive = %d isActive = %d lmid = %llu grammarID = %zu Commands = %@"
+ "RDQSRAudioFileLogger::addSamples Error writing to output wav file,err: %d"
- "-_"
- "Activating Grammar  -> %zu, fClientActivated = %d, fCanListen = %d"
- "Deactivating Grammar  -> %zu, fClientActivated = %d, fCanListen = %d"
- "Insufficient space allocated to copy string contents"
- "Not enough bits to represent the passed value"
- "RDQSRAudioFileLogger::addSamples Error writing to output wav file,err: %{errno}d"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
