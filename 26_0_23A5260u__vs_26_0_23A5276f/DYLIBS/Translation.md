## Translation

> `/System/Library/Frameworks/Translation.framework/Translation`

```diff

-336.4.0.0.0
-  __TEXT.__text: 0x487f8
-  __TEXT.__auth_stubs: 0xdf0
-  __TEXT.__objc_methlist: 0x5168
+341.0.0.0.0
+  __TEXT.__text: 0x49acc
+  __TEXT.__auth_stubs: 0xe00
+  __TEXT.__objc_methlist: 0x5208
   __TEXT.__const: 0x5dc
-  __TEXT.__cstring: 0x2c8e
-  __TEXT.__oslogstring: 0x4546
-  __TEXT.__gcc_except_tab: 0xab4
+  __TEXT.__cstring: 0x2d9e
+  __TEXT.__oslogstring: 0x4616
+  __TEXT.__gcc_except_tab: 0xaf0
   __TEXT.__ustring: 0x14
   __TEXT.__swift5_typeref: 0x249
   __TEXT.__swift5_capture: 0xc0

   __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift_as_ret: 0x28
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__unwind_info: 0x16a0
+  __TEXT.__unwind_info: 0x16d8
   __TEXT.__eh_frame: 0x460
-  __TEXT.__objc_classname: 0xafd
-  __TEXT.__objc_methname: 0xa8f0
-  __TEXT.__objc_methtype: 0x1bca
-  __TEXT.__objc_stubs: 0x5da0
-  __DATA_CONST.__got: 0x480
-  __DATA_CONST.__const: 0x1b88
+  __TEXT.__objc_classname: 0xafe
+  __TEXT.__objc_methname: 0xacc6
+  __TEXT.__objc_methtype: 0x1c06
+  __TEXT.__objc_stubs: 0x61e0
+  __DATA_CONST.__got: 0x490
+  __DATA_CONST.__const: 0x1b68
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2290
+  __DATA_CONST.__objc_selrefs: 0x23a8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x258
-  __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x708
+  __DATA_CONST.__objc_arraydata: 0x78
+  __AUTH_CONST.__auth_got: 0x710
   __AUTH_CONST.__const: 0xac8
-  __AUTH_CONST.__cfstring: 0x2ea0
-  __AUTH_CONST.__objc_const: 0xa630
-  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__cfstring: 0x3160
+  __AUTH_CONST.__objc_const: 0xa6d0
+  __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x390
   __AUTH.__data: 0x180
-  __DATA.__objc_ivar: 0x7a0
+  __DATA.__objc_ivar: 0x7b0
   __DATA.__data: 0x970
   __DATA.__bss: 0x570
   __DATA.__common: 0x30

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1CE4DAA2-81F8-3FE8-B3EF-45B286473366
-  Functions: 2343
-  Symbols:   6935
-  CStrings:  3280
+  UUID: 386D9599-8EF8-3162-99A7-A6565FB4FD0B
+  Functions: 2361
+  Symbols:   7004
+  CStrings:  3370
 
Symbols:
+ +[NSLocale(LTLocaleIdentifier) lt_bestMatchesForPreferredLocales:fromSupportedLocales:]
+ -[NSLocale(LTLocaleIdentifier) _lt_isChinese]
+ -[NSLocale(LTLocaleIdentifier) _lt_isSimplifiedChinese]
+ -[NSLocale(LTLocaleIdentifier) _lt_isTraditionalChinese]
+ -[NSLocale(LTLocaleIdentifier) _lt_shouldCapitalizeDisplayNameForContext:inTargetLocale:]
+ -[NSLocale(LTLocaleIdentifier) lt_displayNameForContext:inTargetLocale:]
+ -[NSLocale(LTLocaleIdentifier) lt_displaySubnameForContext:inTargetLocale:]
+ -[_LTSpeechTranslationRequest _convertAndFeedPCMBuffer:].cold.2
+ -[_LTSpeechTranslationRequest setUpAudioCaptureFile:withFormat:]
+ -[_LTSpeechTranslationRequest setUpAudioCaptureFile:withFormat:].cold.1
+ -[_LTStreamingUtteranceTranslator initWithLocalePair:offlineMTModel:taskHint:]
+ -[_LTStreamingUtteranceTranslator offlineMTModelURL]
+ -[_LTStreamingUtteranceTranslator setTaskHint:]
+ -[_LTStreamingUtteranceTranslator taskHint]
+ -[_LTTextTranslationRequest _submitMessagesSELFLoggingIfNeededForInvocationStart:error:]
+ GCC_except_table122
+ GCC_except_table58
+ GCC_except_table62
+ GCC_except_table65
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_AVAudioFile
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_IVAR_$__LTSpeechTranslationRequest._audioCaptureEnabled
+ _OBJC_IVAR_$__LTSpeechTranslationRequest._finalASRInputCaptureFile
+ _OBJC_IVAR_$__LTStreamingUtteranceTranslator._offlineMTModelURL
+ _OBJC_IVAR_$__LTStreamingUtteranceTranslator._taskHint
+ __LTLocalizedString
+ ___87+[NSLocale(LTLocaleIdentifier) lt_bestMatchesForPreferredLocales:fromSupportedLocales:]_block_invoke
+ ___87+[NSLocale(LTLocaleIdentifier) lt_bestMatchesForPreferredLocales:fromSupportedLocales:]_block_invoke_2
+ _concatenate
+ _objc_msgSend$_lt_isChinese
+ _objc_msgSend$_lt_isSimplifiedChinese
+ _objc_msgSend$_lt_isTraditionalChinese
+ _objc_msgSend$_lt_shouldCapitalizeDisplayNameForContext:inTargetLocale:
+ _objc_msgSend$_submitMessagesSELFLoggingIfNeededForInvocationStart:error:
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$capitalizedString
+ _objc_msgSend$close
+ _objc_msgSend$commonFormat
+ _objc_msgSend$containsString:
+ _objc_msgSend$date
+ _objc_msgSend$fileURLWithPath:isDirectory:
+ _objc_msgSend$initForWriting:settings:commonFormat:interleaved:error:
+ _objc_msgSend$initWithLocalePair:offlineMTModel:taskHint:
+ _objc_msgSend$isInterleaved
+ _objc_msgSend$languageIdentifier
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$localizedStringForLanguage:context:
+ _objc_msgSend$localizedStringForRegion:context:short:
+ _objc_msgSend$lowercaseStringWithLocale:
+ _objc_msgSend$lt_bestMatchesForPreferredLocales:fromSupportedLocales:
+ _objc_msgSend$lt_displaySubnameForContext:inTargetLocale:
+ _objc_msgSend$path
+ _objc_msgSend$scriptCode
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setUpAudioCaptureFile:withFormat:
+ _objc_msgSend$set_offlineMTModelURL:
+ _objc_msgSend$settings
+ _objc_msgSend$standardUserDefaults
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_msgSend$stringForKey:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$writeFromBuffer:error:
+ _untrustedClientIdentifier
+ _untrustedClientIdentifier.cold.1
- -[_LTTranslationRequest requestContext].cold.1
- GCC_except_table120
- GCC_except_table61
- GCC_except_table64
- ___85+[NSLocale(LTLocaleIdentifier) lt_bestMatchForPreferredLocales:fromSupportedLocales:]_block_invoke
- ___85+[NSLocale(LTLocaleIdentifier) lt_bestMatchForPreferredLocales:fromSupportedLocales:]_block_invoke_2
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_Translation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_Translation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_Translation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_Translation
CStrings:
+ "%@ (%@)"
+ "-Hans-"
+ "-Hant-"
+ "@\"AVAudioFile\""
+ "@40@0:8@16@24q32"
+ "AudioRecordingPath"
+ "B32@0:8q16@24"
+ "Created audio file: %@ with format %@"
+ "Failed to create audio capture file at %@ for writing: %@"
+ "Failed to write capture file: %@"
+ "HANS"
+ "HANT"
+ "Ignoring Messages invocation ended event since the log identifier was never set"
+ "MANDARIN_SIMPLIFIED_SUBTITLE"
+ "MANDARIN_TITLE"
+ "MANDARIN_TRADITIONAL_SUBTITLE"
+ "SaveAudioRecordings"
+ "T@\"NSURL\",R,N,V_offlineMTModelURL"
+ "TranslateRecordings"
+ "_%@.caf"
+ "_audioCaptureEnabled"
+ "_finalASRInputCaptureFile"
+ "_lt_isChinese"
+ "_lt_isSimplifiedChinese"
+ "_lt_isTraditionalChinese"
+ "_lt_shouldCapitalizeDisplayNameForContext:inTargetLocale:"
+ "_submitMessagesSELFLoggingIfNeededForInvocationStart:error:"
+ "boolForKey:"
+ "capitalizedString"
+ "close"
+ "com.apple.MobileSMS"
+ "com.apple.imagent"
+ "commonFormat"
+ "components"
+ "containsString:"
+ "date"
+ "es"
+ "fileURLWithPath:isDirectory:"
+ "final_asr_input"
+ "initForWriting:settings:commonFormat:interleaved:error:"
+ "initWithLocalePair:offlineMTModel:taskHint:"
+ "isInterleaved"
+ "languageIdentifier"
+ "localizedDescription"
+ "localizedStringForLanguage:context:"
+ "localizedStringForRegion:context:short:"
+ "lowercaseStringWithLocale:"
+ "lt_bestMatchesForPreferredLocales:fromSupportedLocales:"
+ "lt_displayNameForContext:inTargetLocale:"
+ "lt_displaySubnameForContext:inTargetLocale:"
+ "offlineMTModelURL"
+ "path"
+ "pt"
+ "scriptCode"
+ "setDateFormat:"
+ "setUpAudioCaptureFile:withFormat:"
+ "settings"
+ "standardUserDefaults"
+ "stringByAppendingFormat:"
+ "stringByAppendingPathComponent:"
+ "stringForKey:"
+ "stringFromDate:"
+ "und"
+ "v28@0:8B16@20"
+ "writeFromBuffer:error:"
+ "yyyyMMdd.HHmmss"
+ "zh"
+ "zh-"
+ "\x81"
+ "\xd2"
- "a"
- "\xb2"

```
