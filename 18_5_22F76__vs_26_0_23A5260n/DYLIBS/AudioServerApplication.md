## AudioServerApplication

> `/System/Library/PrivateFrameworks/AudioServerApplication.framework/AudioServerApplication`

```diff

-1050.4.1.0.0
-  __TEXT.__text: 0x10374
-  __TEXT.__auth_stubs: 0x4c0
-  __TEXT.__objc_methlist: 0x11ac
+1100.22.0.0.0
+  __TEXT.__text: 0x118c0
+  __TEXT.__auth_stubs: 0x4d0
+  __TEXT.__objc_methlist: 0x1294
   __TEXT.__const: 0x38
-  __TEXT.__oslogstring: 0xf9f
-  __TEXT.__cstring: 0xfc6
-  __TEXT.__unwind_info: 0x358
-  __TEXT.__objc_classname: 0xda
-  __TEXT.__objc_methname: 0x2606
-  __TEXT.__objc_methtype: 0x58c
-  __TEXT.__objc_stubs: 0x1a20
-  __DATA_CONST.__got: 0xc8
+  __TEXT.__oslogstring: 0x11f1
+  __TEXT.__cstring: 0x1069
+  __TEXT.__unwind_info: 0x388
+  __TEXT.__objc_classname: 0x100
+  __TEXT.__objc_methname: 0x2857
+  __TEXT.__objc_methtype: 0x5bf
+  __TEXT.__objc_stubs: 0x1b80
+  __DATA_CONST.__got: 0xd8
   __DATA_CONST.__const: 0x48
-  __DATA_CONST.__objc_classlist: 0x78
+  __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9e8
-  __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x268
-  __AUTH_CONST.__cfstring: 0x1360
-  __AUTH_CONST.__objc_const: 0x15b0
-  __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0x60
+  __DATA_CONST.__objc_selrefs: 0xa70
+  __DATA_CONST.__objc_superrefs: 0x80
+  __AUTH_CONST.__auth_got: 0x270
+  __AUTH_CONST.__cfstring: 0x1400
+  __AUTH_CONST.__objc_const: 0x17a0
+  __AUTH.__objc_data: 0x4b0
+  __DATA.__objc_ivar: 0x68
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio

   - /System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7BCFC067-7173-3F3B-8249-07B08E0C859E
-  Functions: 379
-  Symbols:   1185
-  CStrings:  891
+  UUID: F02E2480-83EC-3100-980E-63BB062C3C72
+  Functions: 407
+  Symbols:   1271
+  CStrings:  941
 
Symbols:
+ +[ASASampleRateRange rangeWithMinimum:maximum:]
+ +[ASASampleRateRange rangeWithSingleRate:]
+ -[ASAAggregateDevice dealloc]
+ -[ASAAggregateDevice dealloc].cold.1
+ -[ASAAggregateDevice initWithAudioObjectID:]
+ -[ASAAggregateDevice initWithAudioObjectID:].cold.1
+ -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDevice:withName:withUID:isPrivate:]
+ -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDevice:withName:withUID:isPrivate:].cold.1
+ -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDevice:withName:withUID:isPrivate:].cold.2
+ -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDevice:withName:withUID:isPrivate:].cold.3
+ -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDevice:withName:withUID:isPrivate:].cold.4
+ -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDeviceUID:withName:withUID:isPrivate:]
+ -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDeviceUID:withName:withUID:isPrivate:].cold.1
+ -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDeviceUID:withName:withUID:isPrivate:].cold.2
+ -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDeviceUID:withName:withUID:isPrivate:].cold.3
+ -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDeviceUID:withName:withUID:isPrivate:].cold.4
+ -[ASAAggregateDevice initWithDevices:usingMainDevice:andClockDeviceUID:withName:withUID:isPrivate:].cold.5
+ -[ASAAudioDevice externalSecureMute]
+ -[ASAAudioDevice isReferenceStreamEnabled]
+ -[ASAAudioDevice nominalSampleRateRanges]
+ -[ASAAudioDevice setEnableReferenceStream:]
+ -[ASAAudioDevice setExternalSecureMute:]
+ -[ASAAudioDevice supportsExternalSecureMute]
+ -[ASAAudioDevice supportsHeySiri]
+ -[ASAClockDevice nominalSampleRateRanges]
+ -[ASASampleRateRange initWithMinimum:maximum:]
+ -[ASASampleRateRange maximum]
+ -[ASASampleRateRange minimum]
+ _OBJC_CLASS_$_ASAAggregateDevice
+ _OBJC_CLASS_$_ASASampleRateRange
+ _OBJC_CLASS_$_NSAssertionHandler
+ _OBJC_IVAR_$_ASASampleRateRange._maximum
+ _OBJC_IVAR_$_ASASampleRateRange._minimum
+ _OBJC_METACLASS_$_ASAAggregateDevice
+ _OBJC_METACLASS_$_ASASampleRateRange
+ __OBJC_$_CLASS_METHODS_ASASampleRateRange
+ __OBJC_$_INSTANCE_METHODS_ASAAggregateDevice
+ __OBJC_$_INSTANCE_METHODS_ASASampleRateRange
+ __OBJC_$_INSTANCE_VARIABLES_ASASampleRateRange
+ __OBJC_$_PROP_LIST_ASASampleRateRange
+ __OBJC_CLASS_RO_$_ASAAggregateDevice
+ __OBJC_CLASS_RO_$_ASASampleRateRange
+ __OBJC_METACLASS_RO_$_ASAAggregateDevice
+ __OBJC_METACLASS_RO_$_ASASampleRateRange
+ _objc_msgSend$currentHandler
+ _objc_msgSend$externalSecureMute
+ _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
+ _objc_msgSend$initWithDevices:usingMainDevice:andClockDevice:withName:withUID:isPrivate:
+ _objc_msgSend$initWithMinimum:maximum:
+ _objc_msgSend$length
+ _objc_msgSend$maximum
+ _objc_msgSend$minimum
+ _objc_msgSend$nominalSampleRateRanges
+ _objc_msgSend$numberWithFloat:
+ _objc_msgSend$rangeWithMinimum:maximum:
+ _objc_msgSend$supportsExternalSecureMute
+ _objc_msgSend$supportsHeySiri
+ _objc_retainAutoreleasedReturnValue
- _objc_msgSend$doubleValue
- _objc_msgSend$nominalSampleRates
CStrings:
+ "%@RateRange[%u]: %f - %f\n"
+ "%@|    Available Nominal Sample Rate Ranges:\n"
+ "%@|    Control Element: %d\n"
+ "%@|    ExternalSecureMute: %@\n"
+ "%@|    Supports Hey Siri: %@\n"
+ ":"
+ "@24@0:8d16"
+ "@32@0:8d16d24"
+ "@60@0:8@16@24@32@40@48B56"
+ "ASAAggregateDevice"
+ "ASAAggregateDevice.m"
+ "ASASampleRateRange"
+ "Aggregate"
+ "Could not read ExternalSecureMute property\n"
+ "Could not read reference stream enabled property\n"
+ "Could not read supports Hey Siri property\n"
+ "Could not set kAudioDevicePropertyExternalSecureMute\n"
+ "Could not set reference stream enabled property\n"
+ "Device object ID is not an aggregate device. Init with initWithDevices: instead"
+ "Failed to create aggregate: empty device UIDs array"
+ "Failed to create aggregate: empty devices array"
+ "Failed to create aggregate: invalid main device UID"
+ "Failed to create aggregate: no main device UID provided"
+ "Failed to create aggregate: no main device provided"
+ "Failed to create aggregate: no name provided"
+ "Failed to create aggregate: no valid device UIDs"
+ "TB,D,N,GisReferenceStreamEnabled"
+ "Td,R,N,V_maximum"
+ "Td,R,N,V_minimum"
+ "_maximum"
+ "_minimum"
+ "currentHandler"
+ "enableReferenceStream"
+ "externalSecureMute"
+ "handleFailureInMethod:object:file:lineNumber:description:"
+ "initWithDevices:usingMainDevice:andClockDevice:withName:withUID:isPrivate:"
+ "initWithDevices:usingMainDevice:andClockDeviceUID:withName:withUID:isPrivate:"
+ "initWithMinimum:maximum:"
+ "isReferenceStreamEnabled"
+ "length"
+ "maximum"
+ "minimum"
+ "nominalSampleRateRanges"
+ "numberWithFloat:"
+ "rangeWithMinimum:maximum:"
+ "rangeWithSingleRate:"
+ "setEnableReferenceStream:"
+ "setExternalSecureMute:"
+ "supportsExternalSecureMute"
+ "supportsHeySiri"
- "%@Rate[%u]: %f\n"
- "%@Rate[%u]: %f - %f\n"
- "%@|    Available Nominal Sample Rates:\n"
- "%@|    Control Element: %c%c%c%c\n"
- "doubleValue"

```
