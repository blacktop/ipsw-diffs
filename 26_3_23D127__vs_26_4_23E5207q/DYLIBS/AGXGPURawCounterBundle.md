## AGXGPURawCounterBundle

> `/System/Library/Extensions/AGXGPURawCounterBundle.bundle/AGXGPURawCounterBundle`

```diff

-345.20.1.0.0
-  __TEXT.__text: 0x23bc
+350.27.0.0.0
+  __TEXT.__text: 0x226c
   __TEXT.__auth_stubs: 0x140
   __TEXT.__objc_methlist: 0x1d0
   __TEXT.__const: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6F3213F7-89CD-3E3B-A41F-1959982FFCF4
+  UUID: B5C6C8A0-7A6F-3EDD-8F8A-208353599740
   Functions: 36
   Symbols:   198
   CStrings:  183
Functions:
~ -[AGXGPURawCounterSource pollCountersAtBufferIndex:withBlock:] : 1076 -> 1068
~ -[AGXGPURawCounterSource postProcessRawDataWithRingBufferIndex:source:sourceSize:sourceRead:sourceWrite:output:outputSize:outputRead:outputWrite:isLast:] : 96 -> 88
~ -[AGXGPURawCounterSource postProcessRawDataWithRingBufferSource:sourceSize:sourceRead:sourceWrite:output:outputSize:outputRead:outputWrite:isLast:] : 68 -> 52
~ -[AGXGPURawCounterSource postProcessRawDataWithSource:sourceSize:sourceRead:output:outputSize:outputWritten:isLast:] : 60 -> 52
~ -[AGXGPURawCounterSource resetRawDataPostProcessor] : 304 -> 296
~ -[AGXGPURawCounterSource flushRingBuffers] : 48 -> 40
~ -[AGXGPURawCounterSource drainRingBufferAtIndex:dataSize:] : 136 -> 120
~ -[AGXGPURawCounterSource ringBufferInfoAtIndex:base:size:dataOffset:dataSize:] : 324 -> 268
~ -[AGXGPURawCounterSource ringBufferNum] : 48 -> 40
~ -[AGXGPURawCounterSource requestCounters:firstErrorIndex:] : 244 -> 236
~ -[AGXGPURawCounterSource requestCounter:] : 396 -> 388
~ -[AGXGPURawCounterSource requestTriggers:firstErrorIndex:] : 624 -> 600
~ -[AGXGPURawCounterSource isEnabled] : 48 -> 40
~ -[AGXGPURawCounterSource setEnabled:] : 116 -> 104
~ -[AGXGPURawCounterSource setOptions:] : 132 -> 124
~ -[AGXGPURawCounterSource initWithSourceGroup:impl:] : 1188 -> 1116
~ -[AGXGPURawCounterSourceGroup subDivideCounterList:withOptions:] : 1736 -> 1780
~ -[AGXGPURawCounterSourceGroup stopSampling] : 48 -> 40
~ -[AGXGPURawCounterSourceGroup startSampling] : 48 -> 40
~ -[AGXGPURawCounterSourceGroup setOptions:] : 132 -> 124
~ -[AGXGPURawCounterSourceGroup initWithAcceleratorPort:] : 1608 -> 1528

```
