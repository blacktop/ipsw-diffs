## HSTouchHIDService

> `/System/Library/HIDPlugins/ServicePlugins/HSTouchHIDService.plugin/Contents/MacOS/HSTouchHIDService`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-10400.44.0.0.0
-  __TEXT.__text: 0xd8dd8
+10410.1.0.0.0
+  __TEXT.__text: 0xd925c
   __TEXT.__auth_stubs: 0x1d70
-  __TEXT.__objc_stubs: 0x7a60
+  __TEXT.__objc_stubs: 0x7b40
   __TEXT.__init_offsets: 0x14e4
-  __TEXT.__objc_methlist: 0x5448
+  __TEXT.__objc_methlist: 0x54b0
   __TEXT.__const: 0x4470
-  __TEXT.__gcc_except_tab: 0xe7a4
-  __TEXT.__cstring: 0xcc2c
-  __TEXT.__oslogstring: 0x4c9f
-  __TEXT.__objc_methname: 0x8fb5
+  __TEXT.__gcc_except_tab: 0xe80c
+  __TEXT.__cstring: 0xcc5c
+  __TEXT.__oslogstring: 0x4ccf
+  __TEXT.__objc_methname: 0x91a5
   __TEXT.__objc_classname: 0xca7
-  __TEXT.__objc_methtype: 0x5731
+  __TEXT.__objc_methtype: 0x5741
   __TEXT.__swift5_typeref: 0x2de
   __TEXT.__constg_swiftt: 0x254
   __TEXT.__swift5_reflstr: 0x33a

   __TEXT.__swift5_capture: 0x60
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x6cb8
+  __TEXT.__unwind_info: 0x6cd0
   __TEXT.__eh_frame: 0xa8
   __DATA_CONST.__const: 0x2548
-  __DATA_CONST.__cfstring: 0x74e0
+  __DATA_CONST.__cfstring: 0x7520
   __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58

   __DATA_CONST.__auth_got: 0xec8
   __DATA_CONST.__got: 0x388
   __DATA_CONST.__auth_ptr: 0x138
-  __DATA.__objc_const: 0xa1c0
-  __DATA.__objc_selrefs: 0x23c8
-  __DATA.__objc_ivar: 0x70c
+  __DATA.__objc_const: 0xa290
+  __DATA.__objc_selrefs: 0x23f8
+  __DATA.__objc_ivar: 0x720
   __DATA.__objc_data: 0x27a0
   __DATA.__data: 0x18b0
   __DATA.__common: 0x890

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 5462
-  Symbols:   8418
-  CStrings:  4204
+  Functions: 5473
+  Symbols:   8441
+  CStrings:  4221
 
Symbols:
+ -[MTTrackpadUberAlg initWithConfig:actuationHandler:coreAnalyticsCallback:builtIn:supportsForce:supportsDeepPress:]
+ -[MouseSettings toDictionary]
+ -[PointerSettings toDictionary]
+ -[TrackpadAlgButtonStateManager .cxx_destruct]
+ -[TrackpadAlgButtonStateManager coreAnalyticsCallback]
+ -[TrackpadAlgButtonStateManager fwDebouncedButtonReleasedDuringMitigation]
+ -[TrackpadAlgButtonStateManager initWithCoreAnalyticsCallback:]
+ -[TrackpadAlgButtonStateManager preventedFalseReleaseForThisDelay]
+ -[TrackpadAlgButtonStateManager setCoreAnalyticsCallback:]
+ -[TrackpadAlgButtonStateManager setFwDebouncedButtonReleasedDuringMitigation:]
+ -[TrackpadAlgButtonStateManager setPreventedFalseReleaseForThisDelay:]
+ -[TrackpadSettings .cxx_destruct]
+ -[TrackpadSettings toDictionary]
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSMachPortListener.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSObserverStage.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSPUtil.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSPlaybackStage.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSPreferenceStage.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSRecordingPlaybackStage+Remote.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSRecordingPlaybackStage.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSRecordingStage.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSRemoteObject+Additions.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSRemoteObject.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSServerStage.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSServiceDirectory.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSSocketListener.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSStage+Util.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSStage.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSStageProxy.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libHIDSensingUtil.a(HSCoder.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libHIDSensingUtil.a(HSSocket.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libHIDSensingUtil.a(HSTime.o)
+ GCC_except_table158
+ GCC_except_table166
+ OBJC_IVAR_$_MTTrackpadUberAlg._coreAnalyticsCallback
+ OBJC_IVAR_$_TrackpadAlgButtonStateManager._coreAnalyticsCallback
+ OBJC_IVAR_$_TrackpadAlgButtonStateManager._fwDebouncedButtonReleasedDuringMitigation
+ OBJC_IVAR_$_TrackpadAlgButtonStateManager._preventedFalseReleaseForThisDelay
+ OBJC_IVAR_$_TrackpadSettings._debug
+ __33-[TrackpadAlgStage buildUberAlgs]_block_invoke
+ __ZN11HSTPipeline21StaticMousePropertiesEP8NSString
+ __ZN11HSTPipeline24StaticTrackpadPropertiesEP8NSString
+ _objc_msgSend$coreAnalyticsCallback
+ _objc_msgSend$fwDebouncedButtonReleasedDuringMitigation
+ _objc_msgSend$initWithConfig:actuationHandler:coreAnalyticsCallback:builtIn:supportsForce:supportsDeepPress:
+ _objc_msgSend$initWithCoreAnalyticsCallback:
+ _objc_msgSend$preventedFalseReleaseForThisDelay
+ _objc_msgSend$setFwDebouncedButtonReleasedDuringMitigation:
+ _objc_msgSend$setPreventedFalseReleaseForThisDelay:
+ _objc_msgSend$toDictionary
- -[MTTrackpadUberAlg initWithConfig:actuationHandler:builtIn:supportsForce:supportsDeepPress:]
- -[MouseBridge handleGetPropertyEvent:]
- -[MouseSettings debug]
- -[PointerSettings debug]
- -[TrackpadAlgButtonStateManager init]
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSMachPortListener.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSObserverStage.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSPUtil.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSPlaybackStage.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSPreferenceStage.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSRecordingPlaybackStage+Remote.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSRecordingPlaybackStage.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSRecordingStage.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSRemoteObject+Additions.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSRemoteObject.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSServerStage.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSServiceDirectory.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSSocketListener.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSStage+Util.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSStage.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSStageProxy.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libHIDSensingUtil.a(HSCoder.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libHIDSensingUtil.a(HSSocket.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libHIDSensingUtil.a(HSTime.o)
- GCC_except_table159
- GCC_except_table173
- _objc_msgSend$initWithConfig:actuationHandler:builtIn:supportsForce:supportsDeepPress:
CStrings:
+ "10410.1"
+ "@24@0:8@?16"
+ "@52@0:8@16@?24@?32B40B44B48"
+ "Configured to set up async IO queue from default multitouch properties"
+ "MultitouchSettings"
+ "PreventedFalseRelease"
+ "T@\"NSDictionary\",R,N,V_debug"
+ "T@?,C,N,V_coreAnalyticsCallback"
+ "TB,N,V_fwDebouncedButtonReleasedDuringMitigation"
+ "TB,N,V_preventedFalseReleaseForThisDelay"
+ "_coreAnalyticsCallback"
+ "_debug"
+ "_fwDebouncedButtonReleasedDuringMitigation"
+ "_preventedFalseReleaseForThisDelay"
+ "com.apple.trackpad.dragReleaseDelay"
+ "fwDebouncedButtonReleasedDuringMitigation"
+ "initWithConfig:actuationHandler:coreAnalyticsCallback:builtIn:supportsForce:supportsDeepPress:"
+ "initWithCoreAnalyticsCallback:"
+ "preventedFalseReleaseForThisDelay"
+ "setFwDebouncedButtonReleasedDuringMitigation:"
+ "setPreventedFalseReleaseForThisDelay:"
+ "toDictionary"
+ "\xf0\xd2A"
- "10400.44"
- "@44@0:8@16@?24B32B36B40"
- "DefaultMultitouchProperties"
- "Setting up async IO queue"
- "initWithConfig:actuationHandler:builtIn:supportsForce:supportsDeepPress:"
- "\xf0\xd1A"
```
