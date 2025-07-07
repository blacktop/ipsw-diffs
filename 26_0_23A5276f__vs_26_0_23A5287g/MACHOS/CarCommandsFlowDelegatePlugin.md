## CarCommandsFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/CarCommandsFlowDelegatePlugin`

```diff

-3500.32.1.0.0
-  __TEXT.__text: 0x1581d0
-  __TEXT.__auth_stubs: 0x3570
+3500.35.1.0.0
+  __TEXT.__text: 0x15cb90
+  __TEXT.__auth_stubs: 0x3690
   __TEXT.__objc_stubs: 0x6e0
   __TEXT.__objc_methlist: 0xe28
-  __TEXT.__const: 0xd754
+  __TEXT.__const: 0xda54
   __TEXT.__gcc_except_tab: 0x120
   __TEXT.__objc_methname: 0x24a2
-  __TEXT.__cstring: 0x13dbd
+  __TEXT.__cstring: 0x1438d
   __TEXT.__oslogstring: 0x84f
   __TEXT.__objc_classname: 0x1ba
   __TEXT.__objc_methtype: 0x9c5
-  __TEXT.__constg_swiftt: 0x7688
-  __TEXT.__swift5_typeref: 0x4a72
-  __TEXT.__swift5_fieldmd: 0x3e9c
-  __TEXT.__swift5_builtin: 0xb4
-  __TEXT.__swift5_reflstr: 0x4513
-  __TEXT.__swift5_assocty: 0x11e0
-  __TEXT.__swift5_proto: 0x9f4
-  __TEXT.__swift5_types: 0x428
+  __TEXT.__constg_swiftt: 0x77d8
+  __TEXT.__swift5_typeref: 0x4b1a
+  __TEXT.__swift5_fieldmd: 0x3f34
+  __TEXT.__swift5_builtin: 0xc8
+  __TEXT.__swift5_reflstr: 0x45b3
+  __TEXT.__swift5_assocty: 0x1200
+  __TEXT.__swift5_proto: 0xa00
+  __TEXT.__swift5_types: 0x430
   __TEXT.__swift5_protos: 0x160
-  __TEXT.__swift_as_entry: 0xe70
-  __TEXT.__swift_as_ret: 0x1330
-  __TEXT.__swift5_capture: 0x650
-  __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x7078
-  __TEXT.__eh_frame: 0x13b28
-  __DATA_CONST.__auth_got: 0x1ac8
-  __DATA_CONST.__got: 0xbd0
-  __DATA_CONST.__auth_ptr: 0x14a8
-  __DATA_CONST.__const: 0xadb0
+  __TEXT.__swift_as_entry: 0xf14
+  __TEXT.__swift_as_ret: 0x1388
+  __TEXT.__swift5_capture: 0x6a8
+  __TEXT.__swift5_mpenum: 0x20
+  __TEXT.__unwind_info: 0x7268
+  __TEXT.__eh_frame: 0x143b8
+  __DATA_CONST.__auth_got: 0x1b58
+  __DATA_CONST.__got: 0xc48
+  __DATA_CONST.__auth_ptr: 0x1538
+  __DATA_CONST.__const: 0xaed8
   __DATA_CONST.__cfstring: 0x20
-  __DATA_CONST.__objc_classlist: 0x2d8
+  __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xf0
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x6258
+  __DATA.__objc_const: 0x6420
   __DATA.__objc_selrefs: 0xd08
   __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0x26b0
-  __DATA.__data: 0xadc0
+  __DATA.__data: 0xb008
   __DATA.__common: 0x458
-  __DATA.__bss: 0xd380
+  __DATA.__bss: 0xd480
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CB06B813-A80B-3723-B51D-8D458023B25C
-  Functions: 8946
+  UUID: 6A0712B2-6B90-3500-BF68-424A06234027
+  Functions: 9057
   Symbols:   340
-  CStrings:  2124
+  CStrings:  2156
 
CStrings:
+ ", is confirming: "
+ ", or the CarAccessoryType is \"none\""
+ ", volume level: "
+ "/Library/Caches/com.apple.xbs/Sources/SiriCarCommands/CarCommandsFlowDelegatePlugin/Flow/Common/CarCommandsActionFlow.swift"
+ "/Library/Caches/com.apple.xbs/Sources/SiriCarCommands/CarCommandsFlowDelegatePlugin/Flow/Strategies/ExtremeVolumeNeedsConfirmationStrategy.swift"
+ "Audio Settings service not available"
+ "Base flow executing with state "
+ "Can't find CAFAccessory for the given CarAccessoryType: "
+ "Error executing action:"
+ "Error making car unresponsive error dialog:"
+ "Error making success dialog:"
+ "Failed to get AudioSettings"
+ "Failed to get audio settings, not confirming"
+ "Failed to get current volume, not confirming"
+ "Failed to get previous volume, confirming only if volume level ("
+ "Failed to get volume for "
+ "Failed to get volume level"
+ "Got confirmation result: "
+ "Making prompt to confirm extreme volume change"
+ "No requested volume level, not confirming"
+ "Parsing confirmation response: "
+ "Received input for confirmation strategy: "
+ "Timeout error executing CarCommandActionable:"
+ "Volume increase ratio: "
+ "Volume service unavailable, not confirming"
+ "_TtC29CarCommandsFlowDelegatePlugin15SetVolumeAction"
+ "_TtC29CarCommandsFlowDelegatePlugin21CarCommandsActionFlow"
+ "_TtC29CarCommandsFlowDelegatePlugin38ExtremeVolumeNeedsConfirmationStrategy"
+ "actionForInput(_:)"
+ "carCommandsSetVolume#needsConfirmationResponse"
+ "confirmedFlowResult(_:)"
+ "flowState"
+ "getRequestedVolumeLevel(intent:audioSettings:)"
+ "isAccessoryReady(_:)"
+ "makePromptForYesNoResponse()"
+ "needsConfirmation(nlIntent:)"
+ "process(confirmationResult:nlIntent:)"
+ "requestedVolumeLevel"
- "/Library/Caches/com.apple.xbs/Sources/SiriCarCommands/CarCommandsFlowDelegatePlugin/Flow/Common/CarCommandsSimpleFlow.swift"
- "_TtC29CarCommandsFlowDelegatePlugin21CarCommandsSimpleFlow"
- "makeGenericErrorResponse()"
- "modifyVolume(on:volumeType:by:)"
- "modifyVolume(on:volumeType:byPercent:)"
- "setVolume(on:volumeType:to:)"

```
