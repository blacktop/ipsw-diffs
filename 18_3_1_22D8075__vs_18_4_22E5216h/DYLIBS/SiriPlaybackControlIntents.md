## SiriPlaybackControlIntents

> `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/SiriPlaybackControlIntents`

```diff

-3403.4.2.0.0
-  __TEXT.__text: 0x26d79c
+3404.26.1.0.0
+  __TEXT.__text: 0x2445e0
   __TEXT.__auth_stubs: 0x4780
-  __TEXT.__objc_methlist: 0x1e44
-  __TEXT.__const: 0x181c0
-  __TEXT.__cstring: 0x8238
+  __TEXT.__objc_methlist: 0x2748
+  __TEXT.__const: 0x18b80
+  __TEXT.__cstring: 0x7e28
   __TEXT.__constg_swiftt: 0x6940
-  __TEXT.__swift5_typeref: 0x5c60
+  __TEXT.__swift5_typeref: 0x5c4a
   __TEXT.__swift5_builtin: 0x500
   __TEXT.__swift5_reflstr: 0x4ce3
-  __TEXT.__swift5_fieldmd: 0x5988
+  __TEXT.__swift5_fieldmd: 0x59a0
   __TEXT.__swift5_assocty: 0x1b40
-  __TEXT.__swift5_proto: 0x1550
+  __TEXT.__swift5_proto: 0x155c
   __TEXT.__swift5_types: 0x6b0
   __TEXT.__swift5_protos: 0xc0
-  __TEXT.__swift5_capture: 0x4330
-  __TEXT.__oslogstring: 0x1aa26
+  __TEXT.__swift5_capture: 0x4358
+  __TEXT.__oslogstring: 0x1aea6
+  __TEXT.__swift_as_entry: 0xd4
+  __TEXT.__swift_as_ret: 0xe0
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x7130
-  __TEXT.__eh_frame: 0x4ff8
+  __TEXT.__unwind_info: 0x7050
+  __TEXT.__eh_frame: 0x4e08
   __TEXT.__objc_classname: 0x134
-  __TEXT.__objc_methname: 0x2c5f
+  __TEXT.__objc_methname: 0x2d45
   __TEXT.__objc_methtype: 0x1d0
-  __DATA_CONST.__got: 0xe40
-  __DATA_CONST.__const: 0xb60
+  __DATA_CONST.__got: 0xe78
+  __DATA_CONST.__const: 0xb88
   __DATA_CONST.__objc_classlist: 0x5b0
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd68
+  __DATA_CONST.__objc_selrefs: 0xf20
   __DATA_CONST.__objc_protorefs: 0x100
   __AUTH_CONST.__auth_got: 0x23c0
-  __AUTH_CONST.__auth_ptr: 0x2520
-  __AUTH_CONST.__const: 0x12670
-  __AUTH_CONST.__objc_const: 0x12308
-  __AUTH.__objc_data: 0x62f0
+  __AUTH_CONST.__auth_ptr: 0x1bc0
+  __AUTH_CONST.__const: 0x127c0
+  __AUTH_CONST.__objc_const: 0x11e28
+  __AUTH.__objc_data: 0x5770
   __AUTH.__data: 0x6f48
-  __DATA.__data: 0x4390
-  __DATA.__bss: 0x23880
-  __DATA.__common: 0x308
+  __DATA.__data: 0x43f8
+  __DATA.__bss: 0x23a00
+  __DATA.__common: 0x268
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMapKit.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 13971
-  Symbols:   4638
-  CStrings:  2818
+  Functions: 13818
+  Symbols:   4609
+  CStrings:  2824
 
Symbols:
+ _OBJC_CLASS_$_INHomeAutomationEntityProvider
+ _OBJC_CLASS_$_INHomeAutomationFromEntity
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
- __swift_FORCE_LOAD_$_swiftFileProvider
- _objc_release_x11
- _swift_initEnumMetadataMultiPayload
- _swift_initStructMetadata
CStrings:
+ "ASIH#AddNoTopologyChanges"
+ "ASIH#MoveNoTopologyChanges"
+ "Amending HomeAutomation nodes using homeAutomationEntityProvider from the server conversion: %@"
+ "Creating MediaPlayerNLv3Intent from NLv3IntentOnly: %s"
+ "Creating MediaPlayerNLv3Intent from NLv3IntentPlusServerConversion: %s"
+ "INHomeAutomationEntityProvider#haDeviceQuantifier Unable to get device quantifier for value: %s"
+ "INHomeAutomationEntityProvider#haDeviceType Getting device type for value: %s"
+ "INHomeAutomationEntityProvider#haFromEntities Unable to get from entity value for entity: %s"
+ "INHomeAutomationEntityProvider#haFromEntities Unknown from entity type found: %ld"
+ "INHomeAutomationEntityProvider#haPlaceHint Unable to get place hint for value: %s"
+ "INHomeAutomationEntityProvider#haReference Unable to get reference for value: %s"
+ "INHomeAutomationEntityProvider#haServiceNames serviceNames: %s"
+ "MSIH#MoveNoTopologyChanges"
+ "User asked to pause mediaType: %s and nothing was found. Returning local device since it is currently playing"
+ "UsoTask.isSupportedMediaPlayerTask supportedVerbForEntity: %{bool}d, shouldHandleInControlsMediaPlayer: %{bool}d, isWHASupported: %{bool}d. Task is supported by MediaPlayerFlowProvider: %{bool}d"
+ "UsoTask.isSupportedMediaTask supportedVerbForEntity: %{bool}d, shouldHandleInControlsByMedia: %{bool}d, isWHASupported: %{bool}d. Task is supported by MediaFlowProvider: %{bool}d"
+ "UsoTask.isSupportedSettingTask supportedVerbForEntity: %{bool}d, shouldHandleInControlsBySettings: %{bool}d, isWHASupported: %{bool}d. Task is supported by SettingsFlowProvider: %{bool}d"
+ "UsoTaskExtension#validateForMediaDomain#settingEntity validIdentifier: %{bool}d"
+ "UsoTask_increaseBy_common_Setting#shouldHandle Task is mediaPlayer. Handling in controls"
+ "accessoryNames"
+ "decrease"
+ "homeAutomationEntityProvider"
+ "homeName"
+ "increase"
+ "intentDeviceQuantifier"
+ "intentDeviceType"
+ "intentFromEntities"
+ "intentPlaceHint"
+ "intentReference"
+ "privateMediaIntentData"
+ "roomNames"
+ "serviceGroups"
+ "serviceNames"
+ "value"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
- "Not enough bits to represent the passed value"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "UsoTaskExtension#validateForMediaDomain#settingEntity validIdentifier: %{bool}d hasMediaViewOption: %{bool}d)"
- "invalid Collection: less than 'count' elements in collection"
- "setPlaybackSpeedFaster"
- "setPlaybackSpeedSlower"
- "supportedVerbForEntity: %{bool}d, shouldHandleInControlsByMedia: %{bool}d, isWHASupported: %{bool}d. Task is supported by MediaFlowProvider: %{bool}d"
- "supportedVerbForEntity: %{bool}d, shouldHandleInControlsBySettings: %{bool}d, isWHASupported: %{bool}d. Task is supported by SettingsFlowProvider: %{bool}d"
- "supportedVerbForEntity: %{bool}d, shouldHandleInControlsMediaPlayer: %{bool}d, isWHASupported: %{bool}d. Task is supported by MediaPlayerFlowProvider: %{bool}d"

```
