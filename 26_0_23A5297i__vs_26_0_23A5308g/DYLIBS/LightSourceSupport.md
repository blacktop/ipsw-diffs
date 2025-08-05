## LightSourceSupport

> `/System/Library/PrivateFrameworks/LightSourceSupport.framework/LightSourceSupport`

```diff

-7.0.79.1.102
-  __TEXT.__text: 0xdbb8
-  __TEXT.__auth_stubs: 0x760
-  __TEXT.__objc_methlist: 0xa7c
-  __TEXT.__const: 0xd0
-  __TEXT.__cstring: 0xa73
-  __TEXT.__oslogstring: 0x700
-  __TEXT.__gcc_except_tab: 0x45c
-  __TEXT.__unwind_info: 0x560
-  __TEXT.__objc_classname: 0x2a9
-  __TEXT.__objc_methname: 0x12ca
-  __TEXT.__objc_methtype: 0x7a3
-  __TEXT.__objc_stubs: 0xd80
-  __DATA_CONST.__got: 0x130
-  __DATA_CONST.__const: 0x3b8
-  __DATA_CONST.__objc_classlist: 0xe0
+7.0.83.0.0
+  __TEXT.__text: 0xf090
+  __TEXT.__auth_stubs: 0x7b0
+  __TEXT.__objc_methlist: 0xb94
+  __TEXT.__const: 0xe0
+  __TEXT.__cstring: 0xb91
+  __TEXT.__oslogstring: 0x7e2
+  __TEXT.__gcc_except_tab: 0x46c
+  __TEXT.__unwind_info: 0x5f8
+  __TEXT.__objc_classname: 0x2d5
+  __TEXT.__objc_methname: 0x1602
+  __TEXT.__objc_methtype: 0x83e
+  __TEXT.__objc_stubs: 0x1000
+  __DATA_CONST.__got: 0x158
+  __DATA_CONST.__const: 0x3d0
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4c0
-  __DATA_CONST.__objc_superrefs: 0xb0
+  __DATA_CONST.__objc_selrefs: 0x588
+  __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x3c8
-  __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0x600
-  __AUTH_CONST.__objc_const: 0x2af8
+  __AUTH_CONST.__auth_got: 0x3f0
+  __AUTH_CONST.__const: 0x340
+  __AUTH_CONST.__cfstring: 0x660
+  __AUTH_CONST.__objc_const: 0x3000
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_doubleobj: 0x100
+  __AUTH_CONST.__objc_doubleobj: 0x120
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x2d0
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x38
-  __DATA.__objc_ivar: 0x21c
+  __DATA.__objc_ivar: 0x260
   __DATA.__data: 0x2a8
-  __DATA_DIRTY.__objc_data: 0x5f0
-  __DATA_DIRTY.__bss: 0x170
+  __DATA_DIRTY.__objc_data: 0x690
+  __DATA_DIRTY.__bss: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 70CA4932-C3C7-3968-A84E-82D1087C27BD
-  Functions: 368
-  Symbols:   1599
-  CStrings:  670
+  UUID: F9A86133-8C22-365A-80CF-E6852AA6A444
+  Functions: 411
+  Symbols:   1756
+  CStrings:  741
 
Symbols:
+ -[LSSCAService displayForDisplayLink]
+ -[LSSDisplayLink .cxx_destruct]
+ -[LSSDisplayLink _thread_displayLinkFired]
+ -[LSSDisplayLink _thread_invalidate]
+ -[LSSDisplayLink _thread_invalidate].cold.1
+ -[LSSDisplayLink _thread_invalidate].cold.2
+ -[LSSDisplayLink _thread_invalidate].cold.3
+ -[LSSDisplayLink _thread_setPaused:]
+ -[LSSDisplayLink _thread_startRunLoop]
+ -[LSSDisplayLink _thread_startRunLoop].cold.1
+ -[LSSDisplayLink dealloc]
+ -[LSSDisplayLink initWithDisplay:updateInterval:target:action:]
+ -[LSSDisplayLink invalidate]
+ -[LSSDisplayLink invalidate].cold.1
+ -[LSSDisplayLink invalidate].cold.2
+ -[LSSDisplayLink isPaused]
+ -[LSSDisplayLink paused]
+ -[LSSDisplayLink setPaused:]
+ -[LSSDisplayLinkResampler .cxx_destruct]
+ -[LSSDisplayLinkResampler _fire]
+ -[LSSDisplayLinkResampler _onthread_fire]
+ -[LSSDisplayLinkResampler additionalShiftToAccountForVariance]
+ -[LSSDisplayLinkResampler delegate]
+ -[LSSDisplayLinkResampler features]
+ -[LSSDisplayLinkResampler inUpdateInterval]
+ -[LSSDisplayLinkResampler initWithProvider:display:inUpdateInterval:outUpdateInterval:delegate:]
+ -[LSSDisplayLinkResampler initWithProvider:display:inUpdateInterval:outUpdateInterval:delegate:].cold.1
+ -[LSSDisplayLinkResampler initWithProvider:display:inUpdateInterval:outUpdateInterval:delegate:].cold.2
+ -[LSSDisplayLinkResampler invalidate]
+ -[LSSDisplayLinkResampler outUpdateInterval]
+ -[LSSDisplayLinkResampler provider:updatedLight:]
+ -[LSSDisplayLinkResampler queue]
+ -[LSSDisplayLinkResampler setAdditionalShiftToAccountForVariance:]
+ -[LSSDisplayLinkResampler setDelegate:]
+ -[LSSDisplayLinkResampler setFeatures:]
+ -[LSSDisplayLinkResampler updateLightDirection:]
+ -[LSSDisplayLinkResampler updateLightDirection:].cold.1
+ -[LSSDisplayLinkResampler updateLightDirection:].cold.2
+ -[LSSEventQueue intervalForTime:]
+ -[LSSMotionBasedProvider queue]
+ -[LSSMotionBasedProvider updateInterval]
+ -[LSSNullProvider queue]
+ -[LSSPerformanceTestProvider queue]
+ -[LSSResampler initWithProvider:inUpdateInterval:outUpdateInterval:delegate:]
+ -[LSSResampler initWithProvider:inUpdateInterval:outUpdateInterval:delegate:].cold.1
+ -[LSSResampler initWithProvider:inUpdateInterval:outUpdateInterval:delegate:].cold.2
+ -[LSSResampler queue]
+ -[LSSRotationAccumulator setSampleBias:]
+ -[LSSRotationAccumulator setSampleClampMax:]
+ -[LSSStationaryProvider queue]
+ -[LSSTestProvider queue]
+ -[LSSTimeBasedProvider queue]
+ _CFRunLoopGetCurrent
+ _CFRunLoopRun
+ _CFRunLoopStop
+ _CFRunLoopWakeUp
+ _LSSSettingsMotionLightFadeDuration
+ _LSSSettingsMotionMaxDelta
+ _LSSSettingsMotionNoiseFloor
+ _NSRunLoopCommonModes
+ _OBJC_CLASS_$_CADisplayLink
+ _OBJC_CLASS_$_LSSDisplayLink
+ _OBJC_CLASS_$_LSSDisplayLinkResampler
+ _OBJC_CLASS_$_NSRunLoop
+ _OBJC_CLASS_$_NSThread
+ _OBJC_IVAR_$_LSSController._extendedProviderSetting
+ _OBJC_IVAR_$_LSSController._providerSetting
+ _OBJC_IVAR_$_LSSDisplayLink._action
+ _OBJC_IVAR_$_LSSDisplayLink._display
+ _OBJC_IVAR_$_LSSDisplayLink._paused
+ _OBJC_IVAR_$_LSSDisplayLink._runLoop
+ _OBJC_IVAR_$_LSSDisplayLink._target
+ _OBJC_IVAR_$_LSSDisplayLink._thread
+ _OBJC_IVAR_$_LSSDisplayLink._thread_displayLink
+ _OBJC_IVAR_$_LSSDisplayLink._thread_invalid
+ _OBJC_IVAR_$_LSSDisplayLink._updateInterval
+ _OBJC_IVAR_$_LSSDisplayLinkResampler._additionalShiftToAccountForVariance
+ _OBJC_IVAR_$_LSSDisplayLinkResampler._delegate
+ _OBJC_IVAR_$_LSSDisplayLinkResampler._displayLink
+ _OBJC_IVAR_$_LSSDisplayLinkResampler._eventQueue
+ _OBJC_IVAR_$_LSSDisplayLinkResampler._inUpdateInterval
+ _OBJC_IVAR_$_LSSDisplayLinkResampler._outUpdateInterval
+ _OBJC_IVAR_$_LSSDisplayLinkResampler._provider
+ _OBJC_IVAR_$_LSSResampler._provider
+ _OBJC_IVAR_$_LSSRotationAccumulator._sampleBias
+ _OBJC_IVAR_$_LSSRotationAccumulator._sampleClampMax
+ _OBJC_METACLASS_$_LSSDisplayLink
+ _OBJC_METACLASS_$_LSSDisplayLinkResampler
+ __OBJC_$_INSTANCE_METHODS_LSSDisplayLink
+ __OBJC_$_INSTANCE_METHODS_LSSDisplayLinkResampler
+ __OBJC_$_INSTANCE_VARIABLES_LSSDisplayLink
+ __OBJC_$_INSTANCE_VARIABLES_LSSDisplayLinkResampler
+ __OBJC_$_PROP_LIST_LSSDisplayLink
+ __OBJC_$_PROP_LIST_LSSDisplayLinkResampler
+ __OBJC_CLASS_PROTOCOLS_$_LSSDisplayLink
+ __OBJC_CLASS_PROTOCOLS_$_LSSDisplayLinkResampler
+ __OBJC_CLASS_RO_$_LSSDisplayLink
+ __OBJC_CLASS_RO_$_LSSDisplayLinkResampler
+ __OBJC_METACLASS_RO_$_LSSDisplayLink
+ __OBJC_METACLASS_RO_$_LSSDisplayLinkResampler
+ ___39-[LSSController provider:updatedLight:]_block_invoke
+ ___41-[LSSDisplayLinkResampler _onthread_fire]_block_invoke
+ ___LSSLogDisplayLinkResampler_block_invoke
+ ___LSSLogDisplayLink_block_invoke
+ ___block_literal_global.116
+ ___block_literal_global.156
+ ___block_literal_global.160
+ ___block_literal_global.165
+ ___block_literal_global.170
+ ___block_literal_global.172
+ __dispatch_main_q
+ _objc_msgSend$addToRunLoop:forMode:
+ _objc_msgSend$currentRunLoop
+ _objc_msgSend$deviceMotionUpdateInterval
+ _objc_msgSend$displayForDisplayLink
+ _objc_msgSend$displayLinkWithDisplay:target:selector:
+ _objc_msgSend$features
+ _objc_msgSend$initWithDisplay:updateInterval:target:action:
+ _objc_msgSend$initWithProvider:display:inUpdateInterval:outUpdateInterval:delegate:
+ _objc_msgSend$initWithProvider:inUpdateInterval:outUpdateInterval:delegate:
+ _objc_msgSend$initWithTarget:selector:object:
+ _objc_msgSend$mainDisplay
+ _objc_msgSend$paused
+ _objc_msgSend$performSelector:onThread:withObject:waitUntilDone:
+ _objc_msgSend$performSelector:onThread:withObject:waitUntilDone:modes:
+ _objc_msgSend$setName:
+ _objc_msgSend$setPaused:
+ _objc_msgSend$setPreferredFramesPerSecond:
+ _objc_msgSend$start
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$underlyingQueue
+ _objc_msgSend$uniqueId
+ _objc_msgSend$updateInterval
- +[LSSMotionBasedProvider settingName]
- +[LSSNullProvider settingName]
- +[LSSPerformanceTestProvider settingName]
- +[LSSResampler settingName]
- +[LSSStationaryProvider settingName]
- +[LSSTestProvider settingName]
- +[LSSTimeBasedProvider settingName]
- -[LSSResampler initWithQueue:inUpdateInterval:outUpdateInterval:delegate:]
- -[LSSResampler initWithQueue:inUpdateInterval:outUpdateInterval:delegate:].cold.1
- -[LSSResampler initWithQueue:inUpdateInterval:outUpdateInterval:delegate:].cold.2
- _OBJC_IVAR_$_LSSMotionBasedProvider._latestTimestamp
- _OBJC_IVAR_$_LSSMotionBasedProvider._resampler
- _OBJC_IVAR_$_LSSResampler._features
- _OBJC_IVAR_$_LSSResampler._queue
- __OBJC_$_CLASS_METHODS_LSSMotionBasedProvider
- __OBJC_$_CLASS_METHODS_LSSNullProvider
- __OBJC_$_CLASS_METHODS_LSSPerformanceTestProvider
- __OBJC_$_CLASS_METHODS_LSSResampler
- __OBJC_$_CLASS_METHODS_LSSStationaryProvider
- __OBJC_$_CLASS_METHODS_LSSTestProvider
- __OBJC_$_PROTOCOL_CLASS_METHODS_LSSProvider
- ___block_literal_global.109
- ___block_literal_global.143
- ___block_literal_global.147
- ___block_literal_global.152
- ___block_literal_global.157
- ___block_literal_global.159
- _objc_msgSend$initWithQueue:inUpdateInterval:outUpdateInterval:delegate:
- _objc_msgSend$settingName
CStrings:
+ "-[LSSDisplayLinkResampler initWithProvider:display:inUpdateInterval:outUpdateInterval:delegate:]"
+ "-[LSSDisplayLinkResampler updateLightDirection:]"
+ "-[LSSResampler initWithProvider:inUpdateInterval:outUpdateInterval:delegate:]"
+ "1"
+ ":"
+ "@"
+ "@\"CADisplay\""
+ "@\"CADisplayLink\""
+ "@\"LSSDisplayLink\""
+ "@\"NSObject<OS_dispatch_queue>\"16@0:8"
+ "@\"NSRunLoop\""
+ "@\"NSString\""
+ "@\"NSThread\""
+ "@48@0:8@16d24@32:40"
+ "@56@0:8@16@24d32d40@48"
+ "DisplayLink"
+ "DisplayLinkResampler"
+ "LSSDisplayLink"
+ "LSSDisplayLink %p _thread_invalidate"
+ "LSSDisplayLink %p _thread_invalidate already invalid"
+ "LSSDisplayLink %p _thread_startRunLoop"
+ "LSSDisplayLink %p invalidate finish"
+ "LSSDisplayLink %p invalidate start "
+ "LSSDisplayLink:%p for %@"
+ "LSSDisplayLinkResampler"
+ "LSSDisplayLinkResampler.m"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N"
+ "TB,N,V_paused"
+ "_action"
+ "_display"
+ "_displayLink"
+ "_eventQueue"
+ "_extendedProviderSetting"
+ "_onthread_fire"
+ "_providerSetting"
+ "_runLoop"
+ "_sampleBias"
+ "_sampleClampMax"
+ "_target"
+ "_thread"
+ "_thread_displayLink"
+ "_thread_displayLinkFired"
+ "_thread_invalid"
+ "_thread_invalidate"
+ "_thread_setPaused:"
+ "_thread_startRunLoop"
+ "_updateInterval"
+ "addToRunLoop:forMode:"
+ "cannot make display link"
+ "currentRunLoop"
+ "deviceMotionUpdateInterval"
+ "displayForDisplayLink"
+ "displayLinkWithDisplay:target:selector:"
+ "f"
+ "initWithDisplay:updateInterval:target:action:"
+ "initWithProvider:display:inUpdateInterval:outUpdateInterval:delegate:"
+ "initWithProvider:inUpdateInterval:outUpdateInterval:delegate:"
+ "initWithTarget:selector:object:"
+ "isPaused"
+ "mainDisplay"
+ "motion_fadeDuration"
+ "motion_maxDelta"
+ "motion_noiseFloor"
+ "paused"
+ "performSelector:onThread:withObject:waitUntilDone:"
+ "performSelector:onThread:withObject:waitUntilDone:modes:"
+ "setName:"
+ "setPaused:"
+ "setPreferredFramesPerSecond:"
+ "stringWithFormat:"
+ "underlyingQueue"
+ "uniqueId"
+ "updateInterval"
+ "\x91"
- ""
- "-[LSSResampler initWithQueue:inUpdateInterval:outUpdateInterval:delegate:]"
- "@\"LSSResampler\""
- "_latestTimestamp"
- "_resampler"
- "initWithQueue:inUpdateInterval:outUpdateInterval:delegate:"
- "settingName"
- "\xb1"

```
