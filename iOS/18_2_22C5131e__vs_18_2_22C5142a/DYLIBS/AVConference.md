## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2090.16.1.0.0
-  __TEXT.__text: 0x6c02b8
+2090.17.2.0.0
+  __TEXT.__text: 0x6c2078
   __TEXT.__auth_stubs: 0x5060
-  __TEXT.__objc_methlist: 0x2dd08
+  __TEXT.__objc_methlist: 0x2ddf0
   __TEXT.__const: 0x7de0
-  __TEXT.__cstring: 0x8039e
-  __TEXT.__oslogstring: 0xed702
+  __TEXT.__cstring: 0x8062a
+  __TEXT.__oslogstring: 0xedd0a
   __TEXT.__gcc_except_tab: 0x2560
   __TEXT.__ustring: 0x144
-  __TEXT.__unwind_info: 0xd2b0
-  __TEXT.__objc_classname: 0x47b4
-  __TEXT.__objc_methname: 0x7254a
-  __TEXT.__objc_methtype: 0x24870
-  __TEXT.__objc_stubs: 0x48240
+  __TEXT.__unwind_info: 0xd2f8
+  __TEXT.__objc_classname: 0x47d1
+  __TEXT.__objc_methname: 0x72780
+  __TEXT.__objc_methtype: 0x248aa
+  __TEXT.__objc_stubs: 0x483a0
   __DATA_CONST.__got: 0x18e8
   __DATA_CONST.__const: 0x61d8
   __DATA_CONST.__objc_classlist: 0x1180
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x438
+  __DATA_CONST.__objc_protolist: 0x440
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14a58
+  __DATA_CONST.__objc_selrefs: 0x14ab8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0xfa8
   __DATA_CONST.__objc_arraydata: 0x25a0
   __AUTH_CONST.__auth_got: 0x2848
   __AUTH_CONST.__auth_ptr: 0xc8
   __AUTH_CONST.__const: 0x3390
-  __AUTH_CONST.__cfstring: 0x22b00
-  __AUTH_CONST.__objc_const: 0x619a8
-  __AUTH_CONST.__objc_intobj: 0x4608
+  __AUTH_CONST.__cfstring: 0x22ba0
+  __AUTH_CONST.__objc_const: 0x61a88
+  __AUTH_CONST.__objc_intobj: 0x45f0
   __AUTH_CONST.__objc_arrayobj: 0x1a58
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x170
   __AUTH_CONST.__objc_dictobj: 0x2f8
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x63fc
-  __DATA.__data: 0x7430
+  __DATA.__objc_ivar: 0x6408
+  __DATA.__data: 0x7490
   __DATA.__bss: 0xb68
   __DATA.__common: 0x55
   __DATA_DIRTY.__objc_data: 0xaeb0

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 27910
-  Symbols:   32644
-  CStrings:  47419
+  Functions: 27940
+  Symbols:   32675
+  CStrings:  47465
 
CStrings:
+ " [%s] %s:%d %@(%p) Adding new assertion for token=%@, audioAssertionCounter=%llu"
+ " [%s] %s:%d %@(%p) Assertion counter %s! We've leaked the audio assertions. Terminating..."
+ " [%s] %s:%d %@(%p) Audio tap not found. streamToken=%@"
+ " [%s] %s:%d %@(%p) Failed to assert audio stack with token=%ld for delegate=%@"
+ " [%s] %s:%d %@(%p) Failed to register start the audioIO for streamToken=%@. error=%@"
+ " [%s] %s:%d %@(%p) Failed to remove assertion on audio for token=%ld on transportDelegate=%@ with error=%@"
+ " [%s] %s:%d %@(%p) Failed to stop the audioIO for streamToken=%@. error=%@"
+ " [%s] %s:%d %@(%p) Ignoring call to start audio for token=%@ because isInitialization=%{BOOL}d tapPrefersAsyncStart=%{BOOL}d"
+ " [%s] %s:%d %@(%p) Ignoring call to stop audioIO=%@ for token=%@ because isDeinitialization=%{BOOL}d tapStateManagementIsAsync=%{BOOL}d audioIOIsRunning=%{BOOL}d audioIOState=%u"
+ " [%s] %s:%d %@(%p) Invalid context=%p passed. Type=%d callerContext=%p"
+ " [%s] %s:%d %@(%p) Removing assertion for token=%@, audioAssertionCounter=%llu"
+ " [%s] %s:%d Adding new assertion for token=%@, audioAssertionCounter=%llu"
+ " [%s] %s:%d Assertion counter %s! We've leaked the audio assertions. Terminating..."
+ " [%s] %s:%d Audio tap not found. streamToken=%@"
+ " [%s] %s:%d Failed to assert audio stack with token=%ld for delegate=%@"
+ " [%s] %s:%d Failed to register start the audioIO for streamToken=%@. error=%@"
+ " [%s] %s:%d Failed to remove assertion on audio for token=%ld on transportDelegate=%@ with error=%@"
+ " [%s] %s:%d Failed to stop the audioIO for streamToken=%@. error=%@"
+ " [%s] %s:%d Ignoring call to start audio for token=%@ because isInitialization=%{BOOL}d tapPrefersAsyncStart=%{BOOL}d"
+ " [%s] %s:%d Ignoring call to stop audioIO=%@ for token=%@ because isDeinitialization=%{BOOL}d tapStateManagementIsAsync=%{BOOL}d audioIOIsRunning=%{BOOL}d audioIOState=%u"
+ " [%s] %s:%d Invalid context=%p passed. Type=%d callerContext=%p"
+ " [%s] %s:%d Removing assertion for token=%@, audioAssertionCounter=%llu"
+ "%s tapType=%u"
+ "+[VCCellularAudioTap validateAsynchronousActionContext:withError:]"
+ "-[VCAudioPowerSpectrumManager registerListenerWithCellularTapType:clientProcessId:enableAsyncTapStart:powerSpectrumMeter:powerSpectrumMeterKey:resultDictionary:error:]"
+ "-[VCAudioPowerSpectrumManager registerListenerWithCellularTapType:clientProcessId:enableAsyncTapStart:powerSpectrumMeter:powerSpectrumMeterKey:resultDictionary:error:]_block_invoke"
+ "-[VCAudioPowerSpectrumManager registerStreamTokenForCellularTapType:clientProcessId:enableAsyncTapStart:error:]"
+ "-[VCCellularAudioTap addAudioTapForStreamToken:tapType:enableAsyncTapStart:error:]_block_invoke"
+ "-[VCCellularAudioTap startAudioForStreamToken:isInitialization:]"
+ "-[VCCellularAudioTap stopAudioForStreamToken:isDeinitialization:]"
+ "-[VCCellularAudioTap terminateProcessFromAssertionOverflow:onAudioTapIO:]"
+ "-[VCCellularAudioTap validateAddAudioTapForStreamToken:]"
+ "-[VCMediaRecorder dispatchedAssertAudioStackStartedIfNeededForRequest:]"
+ "-[VCMediaRecorder dispatchedRemoveAsynchronousAudioAssertionIfNeeded]"
+ "2090.17.2"
+ "@28@0:8q16B24"
+ "@40@0:8@16i24B28^@32"
+ "Audio assertion counter %sed"
+ "B32@0:8r^{tagVCAsynchronousActionContext=C^v}16^@24"
+ "B40@0:8q16I24B28^@32"
+ "B68@0:8@16@24B32@36@44^@52^@60"
+ "Invalid deferred action context provided to class=%s"
+ "TB,N,V_enableAsyncTapStart"
+ "TQ,N,V_audioAssertionCounter"
+ "VCAsynchronousActionDelegate"
+ "VCVideoCaptureServer [%s] %s:%d capture-started, video settings width=%d height=%d rate=%dfps cappedFrameRate=%dfps"
+ "_audioAssertionCounter"
+ "_enableAsyncTapStart"
+ "actionDidFinishForContext:withError:"
+ "actionWillBeginForContext:withError:"
+ "addAudioTapForStreamToken:tapType:enableAsyncTapStart:error:"
+ "audioAssertionCounter"
+ "dispatchedAssertAudioStackStartedIfNeededForRequest:"
+ "dispatchedRemoveAsynchronousAudioAssertionIfNeeded"
+ "enableAsyncTapStart"
+ "initializeAudioTapIOForStreamToken:enableAsyncTapStart:"
+ "isVideoPacket:length:"
+ "notifyClientOnMediaServerDisconnection"
+ "overflow"
+ "registerListenerWithCellularTapType:clientProcessId:enableAsyncTapStart:powerSpectrumMeter:powerSpectrumMeterKey:resultDictionary:error:"
+ "registerStreamTokenForCellularTapType:clientProcessId:enableAsyncTapStart:error:"
+ "setAudioAssertionCounter:"
+ "setEnableAsyncTapStart:"
+ "startAudioForStreamToken:isInitialization:"
+ "stopAudioForStreamToken:isDeinitialization:"
+ "terminateProcessFromAssertionOverflow:onAudioTapIO:"
+ "underflow"
+ "validateAddAudioTapForStreamToken:"
+ "validateAsynchronousActionContext:withError:"
+ "vcAudioPowerSpectrumMeterEnableAsyncTapStart"
- " [%s] %s:%d %@(%p) Audio tap not found. streamToken=%u"
- " [%s] %s:%d %@(%p) Failed to register start the audioIO for streamToken=%u. error=%@"
- " [%s] %s:%d %@(%p) Failed to stop the audioIO for streamToken=%u. error=%@"
- " [%s] %s:%d 1088x1088 on format = %@"
- " [%s] %s:%d Audio tap not found. streamToken=%u"
- " [%s] %s:%d Failed to register start the audioIO for streamToken=%u. error=%@"
- " [%s] %s:%d Failed to stop the audioIO for streamToken=%u. error=%@"
- "-[VCAVFoundationCapture updateVideoDataOutputVideoSettingResolution:requestHeight:captureFormat:]"
- "-[VCAudioPowerSpectrumManager registerListenerWithCellularTapType:clientProcessId:powerSpectrumMeter:powerSpectrumMeterKey:resultDictionary:error:]"
- "-[VCAudioPowerSpectrumManager registerListenerWithCellularTapType:clientProcessId:powerSpectrumMeter:powerSpectrumMeterKey:resultDictionary:error:]_block_invoke"
- "-[VCAudioPowerSpectrumManager registerStreamTokenForCellularTapType:clientProcessId:error:]"
- "-[VCCellularAudioTap addAudioTapForStreamToken:tapType:error:]_block_invoke"
- "2090.16.1"
- "@36@0:8@16i24^@28"
- "B32@0:8i16i20@24"
- "B36@0:8q16I24^@28"
- "B64@0:8@16@24@32@40^@48^@56"
- "VCVideoCaptureServer [%s] %s:%d capture-started, width=%d height=%d rate=%dfps cappedFrameRate=%dfps"
- "addAudioTapForStreamToken:tapType:error:"
- "isVideoSettingsAspectRatioOverrideSupported"
- "registerListenerWithCellularTapType:clientProcessId:powerSpectrumMeter:powerSpectrumMeterKey:resultDictionary:error:"
- "registerStreamTokenForCellularTapType:clientProcessId:error:"
- "setVideoSettingsAspectRatioOverrideEnabled:"
- "updateVideoDataOutputVideoSettingResolution:requestHeight:captureFormat:"

```
