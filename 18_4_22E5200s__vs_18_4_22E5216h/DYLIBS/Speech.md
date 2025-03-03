## Speech

> `/System/Library/Frameworks/Speech.framework/Speech`

```diff

-3404.69.2.0.0
-  __TEXT.__text: 0x1b388c
-  __TEXT.__auth_stubs: 0x2f20
-  __TEXT.__objc_methlist: 0x4084
+3404.77.1.0.0
+  __TEXT.__text: 0x1c2648
+  __TEXT.__auth_stubs: 0x2f50
+  __TEXT.__objc_methlist: 0x40f4
   __TEXT.__const: 0xaa90
   __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__cstring: 0xa361
-  __TEXT.__constg_swiftt: 0x4598
-  __TEXT.__swift5_typeref: 0x6154
-  __TEXT.__swift5_reflstr: 0x3837
-  __TEXT.__swift5_fieldmd: 0x316c
+  __TEXT.__cstring: 0xa4cf
+  __TEXT.__constg_swiftt: 0x45ac
+  __TEXT.__swift5_typeref: 0x6180
+  __TEXT.__swift5_reflstr: 0x3787
+  __TEXT.__swift5_fieldmd: 0x3114
   __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_assocty: 0xde0
   __TEXT.__swift5_proto: 0x754
   __TEXT.__swift5_types: 0x338
-  __TEXT.__oslogstring: 0x354a
-  __TEXT.__swift5_capture: 0x21bc
+  __TEXT.__oslogstring: 0x3629
+  __TEXT.__swift5_capture: 0x226c
   __TEXT.__swift5_acfuncs: 0x500
-  __TEXT.__swift_as_entry: 0x854
-  __TEXT.__swift_as_ret: 0x82c
+  __TEXT.__swift_as_entry: 0x868
+  __TEXT.__swift_as_ret: 0x840
   __TEXT.__swift5_protos: 0x5c
   __TEXT.__swift5_mpenum: 0x38
-  __TEXT.__gcc_except_tab: 0x80c
-  __TEXT.__unwind_info: 0x7ef0
-  __TEXT.__eh_frame: 0x107d8
+  __TEXT.__gcc_except_tab: 0x7f8
+  __TEXT.__unwind_info: 0x8028
+  __TEXT.__eh_frame: 0x10f5c
   __TEXT.__objc_classname: 0xa15
-  __TEXT.__objc_methname: 0xd1ca
-  __TEXT.__objc_methtype: 0x2726
-  __TEXT.__objc_stubs: 0x4b20
-  __DATA_CONST.__got: 0xe00
-  __DATA_CONST.__const: 0x1428
+  __TEXT.__objc_methname: 0xd388
+  __TEXT.__objc_methtype: 0x2718
+  __TEXT.__objc_stubs: 0x4be0
+  __DATA_CONST.__got: 0xe40
+  __DATA_CONST.__const: 0x1460
   __DATA_CONST.__objc_classlist: 0x408
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2958
+  __DATA_CONST.__objc_selrefs: 0x29b0
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x1f8
-  __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x17a0
-  __AUTH_CONST.__auth_ptr: 0xf90
-  __AUTH_CONST.__const: 0x9e08
-  __AUTH_CONST.__cfstring: 0x3640
-  __AUTH_CONST.__objc_const: 0xbdc0
+  __DATA_CONST.__objc_arraydata: 0x40
+  __AUTH_CONST.__auth_got: 0x17b8
+  __AUTH_CONST.__auth_ptr: 0xe28
+  __AUTH_CONST.__const: 0x9ec8
+  __AUTH_CONST.__cfstring: 0x36c0
+  __AUTH_CONST.__objc_const: 0xbdc8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH.__objc_data: 0xb50
   __AUTH.__data: 0x1268
   __DATA.__objc_ivar: 0x50c
-  __DATA.__data: 0x5758
+  __DATA.__data: 0x5788
   __DATA.__common: 0x320
   __DATA.__bss: 0xc580
   __DATA_DIRTY.__objc_data: 0x16a8
-  __DATA_DIRTY.__data: 0x3948
+  __DATA_DIRTY.__data: 0x3978
   __DATA_DIRTY.__bss: 0x448
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 11661
-  Symbols:   5281
-  CStrings:  3694
+  Functions: 11863
+  Symbols:   5483
+  CStrings:  3717
 
Symbols:
+ _OBJC_CLASS_$_AFASRSharedUserInfo
+ _OBJC_CLASS_$_ASRSchemaASRPersonalizationUserEditNamedEntityMetrics
+ _SFDefaultDataSite
+ _SFSpeechProfileSiteDirectoriesWithUserType
+ _SFUserSpecificDataSites
+ _kSFDefaultDataSiteName
+ _kSFUserSpecificDataSiteName
- _SFSpeechProfileSiteDirectoriesWithRoot
CStrings:
+ "%s No userType provided, fetching both default and user-specific data site directories."
+ "%s No valid URL for speech profile container: %@"
+ "%s Returning the %@ speech profile path for the default user."
+ "%s Unrecognized userType: %@"
+ "%s containerRelativeURL cannot be %@."
+ "+[SFUtilities allSpeechProfileContainersForSharedUserInfos:]"
+ "+[SFUtilities speechProfilePathsForLanguage:personaId:]"
+ "+[SFUtilities speechProfilePathsForLanguage:speechProfileContainers:]"
+ "+[SFUtilities speechProfilePathsForLanguage:userType:]"
+ "+[SFUtilities userSpecificSpeechProfileContainersForSharedUserInfos:]"
+ "-[SFSpeechProfileContainerManager personaForContainerRelativeURL:]"
+ "-[SFSpeechProfileContainerManager personaForContainerRelativeURL:]_block_invoke_2"
+ "@"
+ "Assets was initialized with a locale with insufficient information: "
+ "Enqueuing experiment trigger log on a background task. codepathId=%s namespace=%s requestId=%s"
+ "FullPayloadCorrector was initialized with a locale with insufficient information: "
+ "PhoneticEmbedder was initialized with a locale with insufficient information: "
+ "Retrieving codepathIds from speech profile for trigger logging: %s"
+ "SFAllDataSites"
+ "SFSpeechProfileSiteDirectoriesWithUserType"
+ "SFUserSpecificDataSites"
+ "Speech/EARTranscriptionEvaluator.swift"
+ "Transcriber initialized with locale: %s, effective locale (language-region) pair: %s"
+ "Transcriber was initialized with a locale with insufficient information: "
+ "Vv64@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@\"NSUUID\"40@\"NSString\"48@?<v@?B>56"
+ "allSpeechProfileContainersForSharedUserInfos:"
+ "empty"
+ "evaluateMessagesContext:recognizedText:correctedText:asrID:speechProfilePath:reply:"
+ "initWithBuilder:"
+ "nil"
+ "setPersonaId:"
+ "setPersonalizationUserEditNamedEntityMetrics:"
+ "speechProfilePathsForLanguage:"
+ "speechProfilePathsForLanguage:personaId:"
+ "speechProfilePathsForLanguage:speechProfileContainers:"
+ "speechProfilePathsForLanguage:userType:"
+ "speechProfileRootDirectoriesWithUserType:"
+ "speechRecognizerDidProduceLoggableMultiUserPackages:"
+ "userSpecificSpeechProfileContainersForSharedUserInfos:"
+ "v16@?0@\"<AFASRSharedUserInfoMutating>\"8"
+ "zh-MO"
- "%s MUX: Failed to resolve container, url and personaId cannot both be nil."
- "%s Root directories for new type of speech profile: %{private}@"
- "+[SFUtilities speechProfilePathsWithLanguage:]"
- "+[SFUtilities speechProfilePathsWithLanguage:sharedUserInfos:]"
- "+[SFUtilities speechProfileRootDirectories]"
- "/Library/Caches/com.apple.xbs/Sources/SpeechFramework/SpeechAnalyzer/Assets/Assets.swift"
- "043fda7b-2fc0-489e-8cce-319c22dcf3ba"
- "502484ea-7a73-454a-8e1f-9f04983d6358"
- "Assets must be initialized with a locale that specifies a language"
- "Enqueuing experiment trigger log on a background task. codepathId=%s requestId=%s"
- "Failed to log experiment trigger log for unrecognized codepathId %s"
- "Transcriber must be initialized with a locale that specifies a language"
- "Vv56@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@\"NSUUID\"40@\"NSString\"48"
- "Vv56@0:8@16@24@32@40@48"
- "_detectDataSites"
- "c852375e-0091-4dbd-b2f7-792507612de5"
- "eb18055e-87c4-44c2-ab94-9275bec61c52"
- "evaluateMessagesContext:recognizedText:correctedText:asrID:speechProfilePath:"

```
