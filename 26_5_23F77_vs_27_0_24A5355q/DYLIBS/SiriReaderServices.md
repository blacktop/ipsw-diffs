## SiriReaderServices

> `/System/Library/PrivateFrameworks/SiriReaderServices.framework/SiriReaderServices`

```diff

-3525.5.11.11.1
-  __TEXT.__text: 0x814
-  __TEXT.__auth_stubs: 0x180
+3600.49.31.1.6
+  __TEXT.__text: 0x788
   __TEXT.__objc_methlist: 0x1f0
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0xac
+  __TEXT.__cstring: 0xae
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__oslogstring: 0x36
   __TEXT.__unwind_info: 0x90
-  __TEXT.__objc_classname: 0x4d
-  __TEXT.__objc_methname: 0x508
-  __TEXT.__objc_methtype: 0x1e5
-  __TEXT.__objc_stubs: 0x240
-  __DATA_CONST.__got: 0x38
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_selrefs: 0x188
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xd0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0x278
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0xc0

   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E9AC89FF-FECB-3BB9-9839-E5DA36BB674A
+  UUID: 814CDC02-8218-35CC-A154-749C3CF8DBF2
   Functions: 15
-  Symbols:   119
-  CStrings:  96
+  Symbols:   121
+  CStrings:  13
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x25
+ _objc_release_x26
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x6
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ +[SiriReaderUtilities readerStartingToneAudioAssetURL] : 156 -> 144
~ -[SiriReaderConnection init] : 196 -> 192
~ ___28-[SiriReaderConnection init]_block_invoke : 168 -> 124
~ ___28-[SiriReaderConnection init]_block_invoke.58 : 168 -> 124
~ ___38-[SiriReaderConnection readerProtocol]_block_invoke : 192 -> 148
~ -[SiriReaderConnection readText:textBody:textIdentifier:textLocale:textLeadingImage:] : 212 -> 224
~ -[SiriReaderConnection readText:textBody:textIdentifier:textLocale:textLeadingImage:activationSource:] : 216 -> 228
~ -[SiriReaderConnection getPlaybackStatusForIdentifier:] : 256 -> 252
~ -[SiriReaderConnection pausePlaybackForIdentifier:] : 128 -> 124
~ -[SiriReaderConnection resumePlaybackForIdentifier:] : 128 -> 124
~ -[SiriReaderConnection endMediaSessionForIdentifier:] : 128 -> 124
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "Q16@0:8"
- "SiriReaderConnection"
- "SiriReaderDaemonProtocol"
- "SiriReaderUtilities"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_connection"
- "autorelease"
- "bundleForClass:"
- "class"
- "conformsToProtocol:"
- "dealloc"
- "debugDescription"
- "description"
- "endMediaSessionForIdentifier:"
- "endMediaSessionForIdentifierWithTextIdentifier:"
- "fileURLWithPath:"
- "getPlaybackStatusForIdentifier:"
- "getPlaybackStatusForIdentifierWithTextIdentifier:reply:"
- "hash"
- "init"
- "initWithMachServiceName:options:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "pathForResource:ofType:"
- "pausePlaybackForIdentifier:"
- "pausePlaybackForIdentifierWithTextIdentifier:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "q24@0:8@16"
- "readText:textBody:textIdentifier:textLocale:textLeadingImage:"
- "readText:textBody:textIdentifier:textLocale:textLeadingImage:activationSource:"
- "readTextWithTextTitle:textBody:textIdentifier:textLocale:textLeadingImage:"
- "readTextWithTextTitle:textBody:textIdentifier:textLocale:textLeadingImage:activationSource:"
- "readerProtocol"
- "readerStartingToneAudioAssetURL"
- "release"
- "respondsToSelector:"
- "resume"
- "resumePlaybackForIdentifier:"
- "resumePlaybackForIdentifierWithTextIdentifier:"
- "retain"
- "retainCount"
- "self"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setRemoteObjectInterface:"
- "superclass"
- "suspend"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "v16@0:8"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v32@0:8@\"NSString\"16@?<v@?q>24"
- "v32@0:8@16@?24"
- "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"UIImage\"48"
- "v56@0:8@16@24@32@40@48"
- "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"UIImage\"48q56"
- "v64@0:8@16@24@32@40@48q56"
- "zone"

```
