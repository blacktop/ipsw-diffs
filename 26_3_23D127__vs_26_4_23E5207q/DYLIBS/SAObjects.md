## SAObjects

> `/System/Library/PrivateFrameworks/SAObjects.framework/SAObjects`

```diff

-3505.4.1.0.0
-  __TEXT.__text: 0x3e9bc
-  __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__objc_methlist: 0x32140
+3520.26.1.1.1
+  __TEXT.__text: 0x5039c
+  __TEXT.__auth_stubs: 0x3a0
+  __TEXT.__objc_methlist: 0x32248
   __TEXT.__const: 0x9c8
-  __TEXT.__cstring: 0x16312
-  __TEXT.__unwind_info: 0x39d8
-  __TEXT.__objc_classname: 0x8bd2
-  __TEXT.__objc_methname: 0x2a0b5
+  __TEXT.__cstring: 0x163ea
+  __TEXT.__unwind_info: 0x67b0
+  __TEXT.__objc_classname: 0x8c00
+  __TEXT.__objc_methname: 0x2a176
   __TEXT.__objc_methtype: 0x49d
   __TEXT.__objc_stubs: 0xf00
   __DATA_CONST.__got: 0x8a0
-  __DATA_CONST.__const: 0xfa70
-  __DATA_CONST.__objc_classlist: 0x2de8
+  __DATA_CONST.__const: 0xfb18
+  __DATA_CONST.__objc_classlist: 0x2df8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf1c8
+  __DATA_CONST.__objc_selrefs: 0xf208
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1e0
+  __AUTH_CONST.__auth_got: 0x1d8
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x2e1c0
-  __AUTH_CONST.__objc_const: 0x59000
+  __AUTH_CONST.__cfstring: 0x2e380
+  __AUTH_CONST.__objc_const: 0x59230
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x16120
+  __AUTH.__objc_data: 0x161c0
   __DATA.__objc_ivar: 0x18
   __DATA.__data: 0xfc0
   __DATA_DIRTY.__objc_data: 0x69f0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 184E5764-3B04-3545-B48A-E24CBA3FB1FA
-  Functions: 14941
-  Symbols:   49598
-  CStrings:  21393
+  UUID: 4EFDFBDA-DC90-3649-9146-C1EDFB79005F
+  Functions: 14962
+  Symbols:   49673
+  CStrings:  21432
 
Symbols:
+ -[SAAceView integratedResponseOptions]
+ -[SAAceView setIntegratedResponseOptions:]
+ -[SAAppsLaunchApp options]
+ -[SAAppsLaunchApp setOptions:]
+ -[SAUIIntegratedResponseOptions encodedClassName]
+ -[SAUIIntegratedResponseOptions groupIdentifier]
+ -[SAUIIntegratedResponseOptions preferredHostBundleIdentifier]
+ -[SAUIIntegratedResponseOptions setPreferredHostBundleIdentifier:]
+ -[SAUIStreamChunk commands]
+ -[SAUIStreamChunk encodedClassName]
+ -[SAUIStreamChunk groupIdentifier]
+ -[SAUIStreamChunk requiresResponse]
+ -[SAUIStreamChunk setCommands:]
+ -[SAUIStreamChunk setStreamFailureMessage:]
+ -[SAUIStreamChunk setStreamId:]
+ -[SAUIStreamChunk setStreamStage:]
+ -[SAUIStreamChunk streamFailureMessage]
+ -[SAUIStreamChunk streamId]
+ -[SAUIStreamChunk streamStage]
+ -[SAVCSContentDetailPage personaAccessLevel]
+ -[SAVCSContentDetailPage personaId]
+ -[SAVCSContentDetailPage setPersonaAccessLevel:]
+ -[SAVCSContentDetailPage setPersonaId:]
+ _OBJC_CLASS_$_SAUIIntegratedResponseOptions
+ _OBJC_CLASS_$_SAUIStreamChunk
+ _OBJC_METACLASS_$_SAUIIntegratedResponseOptions
+ _OBJC_METACLASS_$_SAUIStreamChunk
+ _SAAceViewIntegratedResponseOptionsPListKey
+ _SAAppsLaunchAppOptionsDismissSiriValue
+ _SAAppsLaunchAppOptionsPListKey
+ _SAAppsLaunchAppOptionsRetainSiriValue
+ _SAInputOriginRemoteRequestValue
+ _SAUIAppPunchOutLaunchOptionsDismissSiriValue
+ _SAUIAppPunchOutLaunchOptionsMinimizeResponseUIValue
+ _SAUIIntegratedResponseOptionsClassIdentifier
+ _SAUIIntegratedResponseOptionsPreferredHostBundleIdentifierPListKey
+ _SAUIStreamChunkClassIdentifier
+ _SAUIStreamChunkCommandsPListKey
+ _SAUIStreamChunkStreamFailureMessagePListKey
+ _SAUIStreamChunkStreamIdPListKey
+ _SAUIStreamChunkStreamStagePListKey
+ _SAUIStreamStageCancelledValue
+ _SAUIStreamStageCompleteValue
+ _SAUIStreamStageFailedValue
+ _SAUIStreamStageStartValue
+ _SAUIStreamStageStreamingValue
+ _SAVCSContentDetailPagePersonaAccessLevelPListKey
+ _SAVCSContentDetailPagePersonaIdPListKey
+ __OBJC_$_CLASS_PROP_LIST_SAUIIntegratedResponseOptions
+ __OBJC_$_INSTANCE_METHODS_SAUIIntegratedResponseOptions
+ __OBJC_$_INSTANCE_METHODS_SAUIStreamChunk
+ __OBJC_$_PROP_LIST_SAUIIntegratedResponseOptions
+ __OBJC_$_PROP_LIST_SAUIStreamChunk
+ __OBJC_CLASS_PROTOCOLS_$_SAUIIntegratedResponseOptions
+ __OBJC_CLASS_RO_$_SAUIIntegratedResponseOptions
+ __OBJC_CLASS_RO_$_SAUIStreamChunk
+ __OBJC_METACLASS_RO_$_SAUIIntegratedResponseOptions
+ __OBJC_METACLASS_RO_$_SAUIStreamChunk
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x24
+ _objc_retain_x25
- +[SAVCSContentDetailPage contentDetailPageWithDictionary:context:]
- +[SAVCSContentDetailPage contentDetailPage]
- __OBJC_$_CLASS_METHODS_SAVCSContentDetailPage
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x8
CStrings:
+ "Cancelled"
+ "Complete"
+ "DismissSiri"
+ "Failed"
+ "IntegratedResponseOptions"
+ "MinimizeResponseUI"
+ "RemoteRequest"
+ "SAUIIntegratedResponseOptions"
+ "SAUIStreamChunk"
+ "StreamChunk"
+ "Streaming"
+ "T@\"SAUIIntegratedResponseOptions\",&,N"
+ "integratedResponseOptions"
+ "options"
+ "preferredHostBundleIdentifier"
+ "setIntegratedResponseOptions:"
+ "setOptions:"
+ "setPreferredHostBundleIdentifier:"
+ "setStreamFailureMessage:"
+ "setStreamStage:"
+ "streamFailureMessage"
+ "streamStage"
- "contentDetailPage"
- "contentDetailPageWithDictionary:context:"

```
