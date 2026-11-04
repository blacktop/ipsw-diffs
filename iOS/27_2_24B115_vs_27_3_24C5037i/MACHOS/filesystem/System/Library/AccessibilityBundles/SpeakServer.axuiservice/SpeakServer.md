## SpeakServer

> `/System/Library/AccessibilityBundles/SpeakServer.axuiservice/SpeakServer`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3245.8.9.0.0
-  __TEXT.__text: 0x31dc
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_stubs: 0xec0
-  __TEXT.__objc_methlist: 0x40c
-  __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0x68
-  __TEXT.__cstring: 0x1dd
-  __TEXT.__objc_methname: 0x134d
-  __TEXT.__oslogstring: 0x3e8
+3245.8.14.0.0
+  __TEXT.__text: 0x382c
+  __TEXT.__auth_stubs: 0x470
+  __TEXT.__objc_stubs: 0x10e0
+  __TEXT.__objc_methlist: 0x444
+  __TEXT.__const: 0x50
+  __TEXT.__gcc_except_tab: 0x84
+  __TEXT.__cstring: 0x1f6
+  __TEXT.__objc_methname: 0x1539
+  __TEXT.__oslogstring: 0x492
   __TEXT.__objc_classname: 0x23
-  __TEXT.__objc_methtype: 0x3e3
-  __TEXT.__unwind_info: 0x140
-  __DATA_CONST.__const: 0x280
+  __TEXT.__objc_methtype: 0x3f1
+  __TEXT.__unwind_info: 0x158
+  __DATA_CONST.__const: 0x2a8
   __DATA_CONST.__cfstring: 0x220
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x238
-  __DATA_CONST.__got: 0x100
-  __DATA.__objc_const: 0x500
-  __DATA.__objc_selrefs: 0x510
-  __DATA.__objc_ivar: 0x40
+  __DATA_CONST.__auth_got: 0x248
+  __DATA_CONST.__got: 0x148
+  __DATA.__objc_const: 0x550
+  __DATA.__objc_selrefs: 0x5a0
+  __DATA.__objc_ivar: 0x48
   __DATA.__objc_data: 0x50
   __DATA.__data: 0xc0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 61
-  Symbols:   115
-  CStrings:  292
+  Functions: 67
+  Symbols:   126
+  CStrings:  320
 
Symbols:
+ _AVAudioSessionPortBluetoothA2DP
+ _AVAudioSessionPortBluetoothHFP
+ _AVAudioSessionPortBluetoothLE
+ _AVAudioSessionPortHeadphones
+ _AVAudioSessionPortUSBAudio
+ _AVAudioSessionRouteChangeNotification
+ _OBJC_CLASS_$_AVAudioSession
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_CLASS_$_NSOperationQueue
+ _objc_enumerationMutation
+ _objc_setProperty_nonatomic_copy
CStrings:
+ "@"
+ "@?"
+ "@?16@0:8"
+ "Output route is not private: %{public}@"
+ "Stopping typing feedback: output route changed to a non-private route"
+ "T@?,C,N,V_outputRouteIsPrivateTestingOverride"
+ "Will NOT speak typing feedback: output route is not private"
+ "_handleAudioRouteChange"
+ "_isOutputRoutePrivate"
+ "_observeAudioRouteChanges"
+ "_outputRouteIsPrivateTestingOverride"
+ "_routeChangeObserver"
+ "addObserverForName:object:queue:usingBlock:"
+ "audioSession"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "currentRoute"
+ "defaultCenter"
+ "isHeadphones"
+ "isSpeaking"
+ "mainQueue"
+ "outputRouteIsPrivateTestingOverride"
+ "outputs"
+ "portType"
+ "removeObserver:"
+ "setOutputRouteIsPrivateTestingOverride:"
+ "typingFeedbackOnlyWithHeadphonesEnabled"
+ "v16@?0@\"NSNotification\"8"
```
