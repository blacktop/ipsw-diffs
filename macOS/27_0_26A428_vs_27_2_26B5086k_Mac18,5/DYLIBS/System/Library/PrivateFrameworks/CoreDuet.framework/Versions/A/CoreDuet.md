## CoreDuet

> `/System/Library/PrivateFrameworks/CoreDuet.framework/Versions/A/CoreDuet`

```diff

-1971.0.0.0.0
-  __TEXT.__text: 0x189490
+1974.0.1.0.0
+  __TEXT.__text: 0x189930
   __TEXT.__objc_methlist: 0x1119c
-  __TEXT.__cstring: 0x14c18
+  __TEXT.__cstring: 0x14c6f
   __TEXT.__const: 0x5a0
-  __TEXT.__oslogstring: 0x1810d
-  __TEXT.__gcc_except_tab: 0x6d14
+  __TEXT.__oslogstring: 0x180c7
+  __TEXT.__gcc_except_tab: 0x6d08
   __TEXT.__dlopen_cstrs: 0xb6
-  __TEXT.__unwind_info: 0x64c8
+  __TEXT.__unwind_info: 0x64d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7d28
+  __DATA_CONST.__objc_selrefs: 0x7d30
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x648
   __DATA_CONST.__objc_arraydata: 0x678
-  __DATA_CONST.__got: 0x1108
+  __DATA_CONST.__got: 0x1110
   __AUTH_CONST.__const: 0x49d0
   __AUTH_CONST.__cfstring: 0x127c0
   __AUTH_CONST.__objc_const: 0x21cd0

   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x5e8
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__auth_got: 0x970
+  __AUTH_CONST.__auth_got: 0x978
   __AUTH.__objc_data: 0x4920
   __DATA.__objc_ivar: 0x1658
   __DATA.__data: 0x1a40

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /System/Library/PrivateFrameworks/Rapport.framework/Versions/A/Rapport
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
+  - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8526
-  Symbols:   16014
-  CStrings:  4484
+  Functions: 8528
+  Symbols:   16019
+  CStrings:  4488
 
Symbols:
+ _CDConvertPhoneNumberStringToASCII
+ _TCCAccessCopyBundleIdentifiersDisabledForService
+ __CDConvertPhoneNumberStringToASCII
+ _kTCCServiceSiriAccess
+ _objc_msgSend$canBeConvertedToEncoding:
Functions:
~ +[_CDContactResolver resolveContactIdentifier:usingStore:] : 628 -> 648
+ __CDConvertPhoneNumberStringToASCII
~ +[_CDContactResolver normalizedStringFromContactString:] : 152 -> 188
~ +[_CDContactResolver resolveContactIfPossibleFromContactIdentifierString:usingStore:] : 324 -> 356
~ +[_CDSiriLearningSettings uncachedAllLearningDisabledBundleIDs] : 48 -> 92
+ _OUTLINED_FUNCTION_2
~ -[_DKCoreDataStorage deleteStorageFor:] : 920 -> 840
+ _CDConvertPhoneNumberStringToASCII.cold.1
~ ___41+[_CDSiriLearningSettings sharedInstance]_block_invoke : 428 -> 468
~ -[_CDSiriLearningSettings _startWithCallback:invokeCallbackNow:] : 440 -> 500
~ ___64-[_CDSiriLearningSettings _startWithCallback:invokeCallbackNow:]_block_invoke : 772 -> 768
~ -[_CDSiriLearningSettings startSanitizingKnowledgeStore:] : 132 -> 136
~ -[_CDSiriLearningSettings startSanitizingInteractionStore:] : 132 -> 136
~ -[_CDSiriLearningSettings stopSanitizing] : 176 -> 180
- -[_DKCoreDataStorage deleteStorageFor:].cold.2
CStrings:
+ "AppExclusions"
+ "Error checking Siri Learning access (errno %{darwin.errno}d). Attempting checks but they may not work."
+ "IntelligenceFlow"
+ "Process has access to Siri Learning toggles."
+ "Unable to access Siri Learning toggles. Disabling checks."
+ "com.apple.tcc.access.changed"
+ "com.apple.tccd"
+ "mach-lookup"
- "Creating shell PSC to truncate storage."
- "Error checking preferences access (errno %{darwin.errno}d). Attempting checks but they may not work."
- "Process has access to preferences for Siri Learning toggles."
- "Unable to access preferences for Siri Learning toggles. Disabling checks."
```
