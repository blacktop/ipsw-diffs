## SystemStatus

> `/System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus`

```diff

-165.13.100.0.0
-  __TEXT.__text: 0x4bdf4
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0x6a88
+165.19.0.0.0
+  __TEXT.__text: 0x4d270
+  __TEXT.__auth_stubs: 0x640
+  __TEXT.__objc_methlist: 0x6ba8
   __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x32ee
-  __TEXT.__oslogstring: 0xe6f
+  __TEXT.__cstring: 0x3414
+  __TEXT.__oslogstring: 0xedb
   __TEXT.__gcc_except_tab: 0x3c4
-  __TEXT.__unwind_info: 0x1cf0
+  __TEXT.__unwind_info: 0x1d38
   __TEXT.__objc_classname: 0x1773
-  __TEXT.__objc_methname: 0x916a
-  __TEXT.__objc_methtype: 0x1424
-  __TEXT.__objc_stubs: 0x4de0
+  __TEXT.__objc_methname: 0x975c
+  __TEXT.__objc_methtype: 0x1419
+  __TEXT.__objc_stubs: 0x5020
   __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x1600
+  __DATA_CONST.__const: 0x1650
   __DATA_CONST.__objc_classlist: 0x4f8
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1ef10
-  __DATA_CONST.__objc_selrefs: 0x1a08
+  __DATA_CONST.__objc_const: 0x1efd0
+  __DATA_CONST.__objc_selrefs: 0x1ac0
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__cfstring: 0x3d40
+  __AUTH_CONST.__cfstring: 0x3e00
   __AUTH_CONST.__objc_const: 0x4770
-  __AUTH_CONST.__const: 0x720
+  __AUTH_CONST.__const: 0x740
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x338
+  __AUTH_CONST.__auth_got: 0x330
   __AUTH.__objc_data: 0x280
   __DATA.__objc_protorefs: 0x30
   __DATA.__objc_classrefs: 0x4d0
-  __DATA.__objc_superrefs: 0x360
-  __DATA.__objc_ivar: 0x444
-  __DATA.__data: 0xc08
-  __DATA_DIRTY.__objc_ivar: 0x88
+  __DATA.__objc_superrefs: 0x368
+  __DATA.__objc_ivar: 0x450
+  __DATA.__data: 0xc18
+  __DATA.__common: 0x10
+  __DATA_DIRTY.__objc_ivar: 0x90
   __DATA_DIRTY.__objc_data: 0x2f30
-  __DATA_DIRTY.__bss: 0x180
+  __DATA_DIRTY.__bss: 0x160
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4956C9A7-05BD-316E-8C3B-BDC5D933F83F
-  Functions: 2690
-  Symbols:   9554
-  CStrings:  2905
+  UUID: 15F66368-8C1C-38AF-A2FE-9629FD8CC16D
+  Functions: 2721
+  Symbols:   9642
+  CStrings:  2950
 
Symbols:
+ -[STMediaStatusDomainData _initWithMicrophoneRecordingAttributionListData:mutedMicrophoneRecordingAttributionListData:systemAudioRecordingAttributionListData:cameraAttributionListData:]
+ -[STMediaStatusDomainData initWithMicrophoneRecordingAttributionListData:mutedMicrophoneRecordingAttributionListData:systemAudioRecordingAttributionListData:cameraAttributionListData:]
+ -[STMediaStatusDomainData microphoneRecordingAttributionListData]
+ -[STMediaStatusDomainData microphoneRecordingAttributions]
+ -[STMediaStatusDomainData mutedMicrophoneRecordingAttributionListData]
+ -[STMediaStatusDomainData mutedMicrophoneRecordingAttributions]
+ -[STMediaStatusDomainData systemAudioRecordingAttributionListData]
+ -[STMediaStatusDomainData systemAudioRecordingAttributions]
+ -[STMediaStatusDomainDataDiff initWithMicrophoneRecordingAttributionListDataDiff:mutedMicrophoneRecordingAttributionListDataDiff:systemAudioRecordingAttributionListDataDiff:cameraAttributionListDataDiff:]
+ -[STMutableMediaStatusDomainData addMicrophoneRecordingAttribution:]
+ -[STMutableMediaStatusDomainData addMutedMicrophoneRecordingAttribution:]
+ -[STMutableMediaStatusDomainData addSystemAudioRecordingAttribution:]
+ -[STMutableMediaStatusDomainData initWithMicrophoneRecordingAttributionListData:mutedMicrophoneRecordingAttributionListData:systemAudioRecordingAttributionListData:cameraAttributionListData:]
+ -[STMutableMediaStatusDomainData microphoneRecordingAttributionListData]
+ -[STMutableMediaStatusDomainData mutedMicrophoneRecordingAttributionListData]
+ -[STMutableMediaStatusDomainData removeMicrophoneRecordingAttribution:]
+ -[STMutableMediaStatusDomainData removeMutedMicrophoneRecordingAttribution:]
+ -[STMutableMediaStatusDomainData removeSystemAudioRecordingAttribution:]
+ -[STMutableMediaStatusDomainData setMicrophoneRecordingAttributions:]
+ -[STMutableMediaStatusDomainData setMutedMicrophoneRecordingAttributions:]
+ -[STMutableMediaStatusDomainData setSystemAudioRecordingAttributions:]
+ -[STMutableMediaStatusDomainData systemAudioRecordingAttributionListData]
+ -[STMutableStatusBarOverridesStatusDomainData _addEditedIdentifier:]
+ -[STMutableStatusBarOverridesStatusDomainData editedIdentifiers]
+ -[STMutableStatusBarOverridesStatusDomainData initWithCustomOverrides:suppressedBackgroundActivityIdentifierListData:]
+ -[STMutableStatusBarOverridesStatusDomainData stopSuppressingBackgroundActivityWithIdentifier:]
+ -[STMutableStatusBarOverridesStatusDomainData suppressBackgroundActivityWithIdentifier:]
+ -[STMutableStatusBarOverridesStatusDomainData suppressedBackgroundActivityIdentifierListData]
+ -[STStatusBarOverridesStatusDomainData _initWithCustomOverrides:suppressedBackgroundActivityIdentifierListData:]
+ -[STStatusBarOverridesStatusDomainData editedIdentifiers]
+ -[STStatusBarOverridesStatusDomainData initWithCustomOverrides:suppressedBackgroundActivityIdentifierListData:]
+ -[STStatusBarOverridesStatusDomainData initWithCustomOverrides:suppressedBackgroundActivityIdentifiers:]
+ -[STStatusBarOverridesStatusDomainData suppressedBackgroundActivityIdentifierListData]
+ -[STStatusBarOverridesStatusDomainData suppressedBackgroundActivityIdentifiers]
+ -[STStatusBarOverridesStatusDomainDataDiff initWithChanges:suppressedBackgroundActivityIdentifierListDataDiff:]
+ GCC_except_table39
+ OBJC_IVAR_$_STStatusBarOverridesStatusDomainData._suppressedBackgroundActivityIdentifierListData
+ _OBJC_IVAR_$_STMediaStatusDomainData._microphoneRecordingAttributionListData
+ _OBJC_IVAR_$_STMediaStatusDomainData._mutedMicrophoneRecordingAttributionListData
+ _OBJC_IVAR_$_STMediaStatusDomainData._systemAudioRecordingAttributionListData
+ _OBJC_IVAR_$_STMediaStatusDomainDataDiff._microphoneRecordingAttributionListDataDiff
+ _OBJC_IVAR_$_STMediaStatusDomainDataDiff._mutedMicrophoneRecordingAttributionListDataDiff
+ _OBJC_IVAR_$_STMediaStatusDomainDataDiff._systemAudioRecordingAttributionListDataDiff
+ _OBJC_IVAR_$_STStatusBarOverridesStatusDomainDataDiff._suppressedBackgroundActivityIdentifierListDataDiff
+ _STSystemStatusLogObservation.__logObj
+ _STSystemStatusLogObservation.onceToken
+ _STSystemStatusLogPublishing.__logObj
+ _STSystemStatusLogPublishing.onceToken
+ ___35-[STMediaStatusDomainData isEqual:]_block_invoke_4
+ ___39-[STMediaStatusDomainDataDiff isEqual:]_block_invoke_4
+ ___48-[STStatusBarOverridesStatusDomainData isEqual:]_block_invoke_2
+ ___52-[STStatusBarOverridesStatusDomainDataDiff isEqual:]_block_invoke_2
+ ___88-[STStatusBarOverridesStatusDomainData _descriptionBuilderWithMultilinePrefix:forDebug:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e17_"BSSettings"8?0ls32l8
+ ___block_descriptor_40_e8_32s_e22_"STStatusBarData"8?0ls32l8
+ ___block_literal_global.147
+ ___block_literal_global.50
+ _objc_msgSend$_initWithMicrophoneRecordingAttributionListData:mutedMicrophoneRecordingAttributionListData:systemAudioRecordingAttributionListData:cameraAttributionListData:
+ _objc_msgSend$addMicrophoneRecordingAttribution:
+ _objc_msgSend$addMutedMicrophoneRecordingAttribution:
+ _objc_msgSend$appendArraySection:withName:multilinePrefix:skipIfEmpty:objectTransformer:
+ _objc_msgSend$editedIdentifiers
+ _objc_msgSend$initWithChanges:suppressedBackgroundActivityIdentifierListDataDiff:
+ _objc_msgSend$initWithCustomOverrides:suppressedBackgroundActivityIdentifierListData:
+ _objc_msgSend$initWithCustomOverrides:suppressedBackgroundActivityIdentifiers:
+ _objc_msgSend$initWithMicrophoneRecordingAttributionListData:mutedMicrophoneRecordingAttributionListData:systemAudioRecordingAttributionListData:cameraAttributionListData:
+ _objc_msgSend$initWithMicrophoneRecordingAttributionListDataDiff:mutedMicrophoneRecordingAttributionListDataDiff:systemAudioRecordingAttributionListDataDiff:cameraAttributionListDataDiff:
+ _objc_msgSend$microphoneRecordingAttributionListData
+ _objc_msgSend$microphoneRecordingAttributions
+ _objc_msgSend$mutedMicrophoneRecordingAttributionListData
+ _objc_msgSend$mutedMicrophoneRecordingAttributions
+ _objc_msgSend$removeMicrophoneRecordingAttribution:
+ _objc_msgSend$removeMutedMicrophoneRecordingAttribution:
+ _objc_msgSend$setMicrophoneRecordingAttributions:
+ _objc_msgSend$setMutedMicrophoneRecordingAttributions:
+ _objc_msgSend$suppressedBackgroundActivityIdentifierListData
+ _objc_msgSend$suppressedBackgroundActivityIdentifiers
+ _objc_msgSend$systemAudioRecordingAttributionListData
+ _objc_msgSend$systemAudioRecordingAttributions
+ _objc_msgSend$tokenForCurrentProcess
- -[STMediaStatusDomainData _initWithAudioRecordingAttributionListData:mutedAudioRecordingAttributionListData:cameraAttributionListData:]
- -[STMediaStatusDomainData audioRecordingAttributionListData]
- -[STMediaStatusDomainData initWithAudioRecordingAttributionListData:mutedAudioRecordingAttributionListData:cameraAttributionListData:]
- -[STMediaStatusDomainData mutedAudioRecordingAttributionListData]
- -[STMediaStatusDomainDataDiff initWithAudioRecordingAttributionListDataDiff:mutedAudioRecordingAttributionListDataDiff:cameraAttributionListDataDiff:]
- -[STMutableMediaStatusDomainData audioRecordingAttributionListData]
- -[STMutableMediaStatusDomainData initWithAudioRecordingAttributionListData:mutedAudioRecordingAttributionListData:cameraAttributionListData:]
- -[STMutableMediaStatusDomainData mutedAudioRecordingAttributionListData]
- -[STStatusBarOverridesStatusDomainDataDiff initWithChanges:]
- GCC_except_table35
- _OBJC_IVAR_$_STMediaStatusDomainData._audioRecordingAttributionListData
- _OBJC_IVAR_$_STMediaStatusDomainData._mutedAudioRecordingAttributionListData
- _OBJC_IVAR_$_STMediaStatusDomainDataDiff._audioRecordingAttributionListDataDiff
- _OBJC_IVAR_$_STMediaStatusDomainDataDiff._mutedAudioRecordingAttributionListDataDiff
- _OBJC_IVAR_$_STMutableStatusBarOverridesStatusDomainData._editedKeys
- ___block_literal_global.11
- ___block_literal_global.140
- _dispatch_get_current_queue
- _objc_msgSend$_initWithAudioRecordingAttributionListData:mutedAudioRecordingAttributionListData:cameraAttributionListData:
- _objc_msgSend$audioRecordingAttributionListData
- _objc_msgSend$initWithAudioRecordingAttributionListData:mutedAudioRecordingAttributionListData:cameraAttributionListData:
- _objc_msgSend$initWithAudioRecordingAttributionListDataDiff:mutedAudioRecordingAttributionListDataDiff:cameraAttributionListDataDiff:
- _objc_msgSend$mutedAudioRecordingAttributionListData
CStrings:
+ "@\"BSSettings\"8@?0"
+ "@\"STStatusBarData\"8@?0"
+ "@48@0:8@16@24@32@40"
+ "SYSTEMSTATUS CLIENT ERROR: %{public}@ domain was deallocated without being invalidated"
+ "SYSTEMSTATUS CLIENT ERROR: %{public}@ publisher was deallocated without being invalidated"
+ "Server connection rejected due to missing entitlement"
+ "T@\"STListData\",R,C,N,V_microphoneRecordingAttributionListData"
+ "T@\"STListData\",R,C,N,V_mutedMicrophoneRecordingAttributionListData"
+ "T@\"STListData\",R,C,N,V_suppressedBackgroundActivityIdentifierListData"
+ "T@\"STListData\",R,C,N,V_systemAudioRecordingAttributionListData"
+ "_editedIdentifiers"
+ "_initWithMicrophoneRecordingAttributionListData:mutedMicrophoneRecordingAttributionListData:systemAudioRecordingAttributionListData:cameraAttributionListData:"
+ "_microphoneRecordingAttributionListData"
+ "_microphoneRecordingAttributionListDataDiff"
+ "_mutedMicrophoneRecordingAttributionListData"
+ "_mutedMicrophoneRecordingAttributionListDataDiff"
+ "_suppressedBackgroundActivityIdentifierListData"
+ "_suppressedBackgroundActivityIdentifierListDataDiff"
+ "_systemAudioRecordingAttributionListData"
+ "_systemAudioRecordingAttributionListDataDiff"
+ "addMicrophoneRecordingAttribution:"
+ "addMutedMicrophoneRecordingAttribution:"
+ "addSystemAudioRecordingAttribution:"
+ "appendArraySection:withName:multilinePrefix:skipIfEmpty:objectTransformer:"
+ "editedIdentifiers"
+ "initWithChanges:suppressedBackgroundActivityIdentifierListDataDiff:"
+ "initWithCustomOverrides:suppressedBackgroundActivityIdentifierListData:"
+ "initWithCustomOverrides:suppressedBackgroundActivityIdentifiers:"
+ "initWithMicrophoneRecordingAttributionListData:mutedMicrophoneRecordingAttributionListData:systemAudioRecordingAttributionListData:cameraAttributionListData:"
+ "initWithMicrophoneRecordingAttributionListDataDiff:mutedMicrophoneRecordingAttributionListDataDiff:systemAudioRecordingAttributionListDataDiff:cameraAttributionListDataDiff:"
+ "microphoneRecordingAttributionListData"
+ "microphoneRecordingAttributionListDataDiff"
+ "microphoneRecordingAttributions"
+ "mutedMicrophoneRecordingAttributionListData"
+ "mutedMicrophoneRecordingAttributionListDataDiff"
+ "mutedMicrophoneRecordingAttributions"
+ "removeMicrophoneRecordingAttribution:"
+ "removeMutedMicrophoneRecordingAttribution:"
+ "removeSystemAudioRecordingAttribution:"
+ "setMicrophoneRecordingAttributions:"
+ "setMutedMicrophoneRecordingAttributions:"
+ "setSystemAudioRecordingAttributions:"
+ "stopSuppressingBackgroundActivityWithIdentifier:"
+ "suppressBackgroundActivityWithIdentifier:"
+ "suppressedBackgroundActivityIdentifierListData"
+ "suppressedBackgroundActivityIdentifierListDataDiff"
+ "suppressedBackgroundActivityIdentifiers"
+ "systemAudioRecordingAttributionListData"
+ "systemAudioRecordingAttributionListDataDiff"
+ "systemAudioRecordingAttributions"
+ "tokenForCurrentProcess"
- "%{public}@ domain was deallocated without being invalidated"
- "%{public}@ publisher was deallocated without being invalidated"
- "@\"NSObject<BSDefaultObserver>\""
- "T@\"STListData\",R,C,N,V_audioRecordingAttributionListData"
- "T@\"STListData\",R,C,N,V_mutedAudioRecordingAttributionListData"
- "_audioRecordingAttributionListData"
- "_audioRecordingAttributionListDataDiff"
- "_initWithAudioRecordingAttributionListData:mutedAudioRecordingAttributionListData:cameraAttributionListData:"
- "_mutedAudioRecordingAttributionListData"
- "_mutedAudioRecordingAttributionListDataDiff"
- "audioRecordingAttributionListData"
- "audioRecordingAttributionListDataDiff"
- "initWithAudioRecordingAttributionListData:mutedAudioRecordingAttributionListData:cameraAttributionListData:"
- "initWithAudioRecordingAttributionListDataDiff:mutedAudioRecordingAttributionListDataDiff:cameraAttributionListDataDiff:"
- "mutedAudioRecordingAttributionListData"
- "mutedAudioRecordingAttributionListDataDiff"

```
