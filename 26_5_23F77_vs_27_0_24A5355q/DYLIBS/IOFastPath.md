## IOFastPath

> `/System/Library/PrivateFrameworks/IOFastPath.framework/IOFastPath`

```diff

-2238.120.5.0.0
-  __TEXT.__text: 0x2fb0
-  __TEXT.__auth_stubs: 0x310
+2353.0.0.0.1
+  __TEXT.__text: 0x3008
   __TEXT.__objc_methlist: 0x604
   __TEXT.__const: 0x40
   __TEXT.__oslogstring: 0x1b8
-  __TEXT.__cstring: 0x98
+  __TEXT.__cstring: 0x9a
   __TEXT.__gcc_except_tab: 0x80
   __TEXT.__unwind_info: 0x1e0
-  __TEXT.__objc_classname: 0x10b
-  __TEXT.__objc_methname: 0x5f0
-  __TEXT.__objc_methtype: 0x1eb
-  __TEXT.__objc_stubs: 0x880
-  __DATA_CONST.__got: 0x80
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x258
   __DATA_CONST.__objc_superrefs: 0x68
-  __AUTH_CONST.__auth_got: 0x198
+  __DATA_CONST.__got: 0x80
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0xb70
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x78
   __DATA_DIRTY.__objc_data: 0x410
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 24AA51B8-1EF0-359A-83F6-383151FDC65C
-  Functions: 146
-  Symbols:   537
-  CStrings:  164
+  UUID: 7D38414B-BE95-39F7-B9AB-7E48216A14CB
+  Functions: 145
+  Symbols:   539
+  CStrings:  18
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
Functions:
~ -[IOFastPathSampleBase initWithDescriptor:] : 112 -> 120
~ -[IOFastPathSampleBase getField:ofType:] : 524 -> 544
~ -[IOFastPathSampleBase setField:ofType:buf:len:] : 684 -> 692
~ -[IOFastPathSampleBase copyPayload:] : 96 -> 92
~ +[IOFastPathTestSample sampleWithDescriptor:andPayload:] : 112 -> 116
~ -[IOFastPathTestSample initWithDescriptor:andPayload:] : 200 -> 196
~ _getNumberForKey : 120 -> 116
~ _allValuesAreOfType : 152 -> 144
~ -[IOFastPathDescriptor initWithFields:] : 344 -> 340
~ -[IOFastPathDescriptor serialize] : 480 -> 460
- _OUTLINED_FUNCTION_0
~ -[IOFastPathQueueSample initWithClient:] : 140 -> 144
~ -[IOFastPathQueueSample setPayload:size:] : 104 -> 116
~ -[IOFastPathQueueSample isValid] : 72 -> 88
~ -[IOFastPathServiceClient dealloc] : 92 -> 96
~ -[IOFastPathServiceClient close] : 96 -> 104
~ -[IOFastPathConsumer initWithService:] : 88 -> 96
~ -[IOFastPathConsumer readSample:withReader:] : 152 -> 160
~ -[IOFastPathProducer initWithService:] : 76 -> 80
~ -[IOFastPathProducer createSample] : 32 -> 36
~ -[IOFastPathProducer enqueueSample:] : 64 -> 76
~ _IOFastPathClientCreate : 44 -> 40
~ _IOFastPathClientCreateWithType : 84 -> 80
~ -[IOFastPathClientBase initWithDescriptor:] : 108 -> 116
~ -[IOFastPathClientBase copyDescriptor] : 36 -> 32
~ -[IOFastPathClientBase getSampleSize] : 24 -> 28
~ -[IOFastPathClientBase supportsField:ofType:] : 244 -> 240
~ _IOFastPathClientCreateSample : 32 -> 28
~ +[IOFastPathReplaySample sampleWithDescriptor:andQueue:] : 112 -> 116
~ -[IOFastPathReplaySample isValid] : 148 -> 160
~ -[IOFastPathReplaySample setPayload:size:] : 116 -> 128
~ -[ReplayQueue initWithCapacity:entrySize:] : 164 -> 160
~ -[ReplayQueue entryAtIndex:] : 56 -> 64
~ -[ReplayQueue enqueue:] : 232 -> 228
~ -[IOFastPathReplayClient createSample] : 44 -> 52
~ -[IOFastPathReplayClient enqueueSample:] : 128 -> 132
~ -[IOFastPathReplayClient readLatestSample:] : 128 -> 132
~ -[IOFastPathReplayClient readNextSample:] : 128 -> 132
~ -[IOFastPathReplayClient readCurrentSample:] : 128 -> 132
~ -[IOFastPathReplayClient readPreviousSample:] : 128 -> 132
~ _IOFastPathReplayClientCreate : 48 -> 44
~ +[IOFastPathField fieldWithDict:] : 320 -> 296
~ +[IOFastPathDescriptor descriptorWithProperty:] : 540 -> 552
~ +[IOFastPathDescriptor descriptorWithData:] : 284 -> 276
~ -[IOFastPathServiceClient initWithService:] : 240 -> 244
~ -[IOFastPathServiceClient open] : 168 -> 184
CStrings:
- ".cxx_destruct"
- "@\"IOFastPathConsumer\""
- "@\"IOFastPathDescriptor\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSMutableData\""
- "@\"ReplayQueue\""
- "@16@0:8"
- "@20@0:8I16"
- "@24@0:8@16"
- "@24@0:8I16I20"
- "@24@0:8^v16"
- "@28@0:8@16I24"
- "@32@0:8@16@24"
- "@40@0:8I16i20Q24Q32"
- "B24@0:8@16"
- "B24@0:8I16i20"
- "B28@0:8I16Q20"
- "I"
- "IOFastPathClientBase"
- "IOFastPathConsumer"
- "IOFastPathField"
- "IOFastPathProducer"
- "IOFastPathQueueSample"
- "IOFastPathReplayClient"
- "IOFastPathReplaySample"
- "IOFastPathSampleBase"
- "IOFastPathServiceClient"
- "IOFastPathTestSample"
- "IOFastPathWriterSample"
- "Q"
- "Q16@0:8"
- "ReplayQueue"
- "^v24@0:8I16i20"
- "^{?=Q[0C]}24@0:8Q16"
- "^{IOCircularDataQueue=}"
- "_cfTypeID"
- "addObject:"
- "allKeys"
- "allValues"
- "array"
- "buf"
- "bytes"
- "client"
- "clientWithData:andQueueCapacity:"
- "clientWithService:"
- "close"
- "connection"
- "copyDescriptor"
- "copyPayload:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createSample"
- "cursor"
- "dataWithLength:"
- "dealloc"
- "descriptor"
- "descriptorWithData:"
- "descriptorWithFields:"
- "descriptorWithProperty:"
- "dictionary"
- "enqueue:"
- "enqueueSample:"
- "entry:isValid:"
- "entryAtIndex:"
- "entrySize"
- "fieldWithDict:"
- "fieldWithKey:type:offset:size:"
- "fields"
- "generation"
- "getDoubleField:value:"
- "getField:ofType:"
- "getIntegerField:value:"
- "getSampleSize"
- "getSupportedFields"
- "i"
- "i16@0:8"
- "i24@0:8@16"
- "i28@0:8I16^d20"
- "i28@0:8I16^q20"
- "i28@0:8I16d20"
- "i28@0:8I16q20"
- "i32@0:8@16^?24"
- "init"
- "initWithCapacity:entrySize:"
- "initWithClient:"
- "initWithData:andQueueCapacity:"
- "initWithDescriptor:"
- "initWithDescriptor:andPayload:"
- "initWithDescriptor:andQueue:"
- "initWithFields:"
- "initWithKey:type:offset:size:"
- "initWithService:"
- "isEqual:"
- "isEqualToDictionary:"
- "isValid"
- "key"
- "length"
- "mutableBytes"
- "nextWriteIdx"
- "numEntries"
- "numberWithUnsignedInt:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "offset"
- "open"
- "options"
- "payload"
- "queue"
- "queueIdx"
- "queueMem"
- "queueWithCapacity:entrySize:"
- "r^v"
- "readCurrent:"
- "readCurrentSample:"
- "readLatest:"
- "readLatestSample:"
- "readNext:"
- "readNextSample:"
- "readPrevious:"
- "readPreviousSample:"
- "readSample:withReader:"
- "sampleSize"
- "sampleWithClient:"
- "sampleWithDescriptor:"
- "sampleWithDescriptor:andPayload:"
- "sampleWithDescriptor:andQueue:"
- "seq"
- "serialize"
- "service"
- "setDoubleField:value:"
- "setField:ofType:buf:len:"
- "setIntegerField:value:"
- "setLength:"
- "setObject:forKeyedSubscript:"
- "setPayload:size:"
- "size"
- "supportsField:ofType:"
- "type"
- "unsignedIntValue"
- "unsignedLongLongValue"
- "v16@0:8"
- "v32@0:8r^v16Q24"
- "v40@0:8I16i20^v24Q32"
- "{?=\"seq\"Q\"idx\"I\"generation\"I}"

```
