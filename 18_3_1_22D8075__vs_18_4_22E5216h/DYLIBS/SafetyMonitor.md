## SafetyMonitor

> `/System/Library/PrivateFrameworks/SafetyMonitor.framework/SafetyMonitor`

```diff

-986.0.1.0.0
-  __TEXT.__text: 0x7522c
-  __TEXT.__auth_stubs: 0x1300
-  __TEXT.__objc_methlist: 0x431c
-  __TEXT.__const: 0x1268
-  __TEXT.__cstring: 0xbad7
-  __TEXT.__swift5_typeref: 0x50e
-  __TEXT.__oslogstring: 0x438d
-  __TEXT.__constg_swiftt: 0x45c
+990.0.8.0.0
+  __TEXT.__text: 0x73308
+  __TEXT.__auth_stubs: 0x12a0
+  __TEXT.__objc_methlist: 0x4c7c
+  __TEXT.__const: 0x1278
+  __TEXT.__dlopen_cstrs: 0x60
+  __TEXT.__cstring: 0xb87b
+  __TEXT.__swift5_typeref: 0x4a2
+  __TEXT.__oslogstring: 0x4361
+  __TEXT.__constg_swiftt: 0x450
   __TEXT.__swift5_reflstr: 0x2be
-  __TEXT.__swift5_fieldmd: 0x3f8
+  __TEXT.__swift5_fieldmd: 0x3ec
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_assocty: 0x90
-  __TEXT.__swift5_capture: 0x200
+  __TEXT.__swift5_capture: 0x120
   __TEXT.__swift5_proto: 0xd0
   __TEXT.__swift5_types: 0x54
+  __TEXT.__swift_as_entry: 0x40
+  __TEXT.__swift_as_ret: 0x44
   __TEXT.__swift5_protos: 0x4
   __TEXT.__ustring: 0xd34
   __TEXT.__gcc_except_tab: 0xf64
-  __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__unwind_info: 0x1848
+  __TEXT.__unwind_info: 0x17c0
   __TEXT.__eh_frame: 0x95c
-  __TEXT.__objc_classname: 0x9f1
-  __TEXT.__objc_methname: 0xc465
-  __TEXT.__objc_methtype: 0x21b0
-  __TEXT.__objc_stubs: 0x5860
-  __DATA_CONST.__got: 0x4c0
+  __TEXT.__objc_classname: 0x9c9
+  __TEXT.__objc_methname: 0xc364
+  __TEXT.__objc_methtype: 0x2155
+  __TEXT.__objc_stubs: 0x57c0
+  __DATA_CONST.__got: 0x4b8
   __DATA_CONST.__const: 0x1468
-  __DATA_CONST.__objc_classlist: 0x270
+  __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x120
+  __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ff8
+  __DATA_CONST.__objc_selrefs: 0x2220
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x1b0
-  __AUTH_CONST.__auth_got: 0x990
-  __AUTH_CONST.__auth_ptr: 0x300
-  __AUTH_CONST.__const: 0xb68
-  __AUTH_CONST.__cfstring: 0x4f20
-  __AUTH_CONST.__objc_const: 0x9650
+  __DATA_CONST.__objc_superrefs: 0x1a8
+  __AUTH_CONST.__auth_got: 0x960
+  __AUTH_CONST.__auth_ptr: 0x2f8
+  __AUTH_CONST.__const: 0x938
+  __AUTH_CONST.__cfstring: 0x4e40
+  __AUTH_CONST.__objc_const: 0x81a0
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x1220
+  __AUTH.__objc_data: 0x11c0
   __AUTH.__data: 0x2d8
-  __DATA.__objc_ivar: 0x398
-  __DATA.__data: 0x1360
-  __DATA.__bss: 0x1600
-  __DATA.__common: 0x110
+  __DATA.__objc_ivar: 0x380
+  __DATA.__data: 0x1398
+  __DATA.__bss: 0x1610
+  __DATA.__common: 0x88
   __DATA_DIRTY.__objc_ivar: 0x1d4
   __DATA_DIRTY.__objc_data: 0x9c8
-  __DATA_DIRTY.__data: 0xe8
-  __DATA_DIRTY.__common: 0x18
-  __DATA_DIRTY.__bss: 0x430
+  __DATA_DIRTY.__data: 0x108
+  __DATA_DIRTY.__bss: 0x420
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2223
-  Symbols:   2243
-  CStrings:  3375
+  Functions: 2155
+  Symbols:   2232
+  CStrings:  3345
 
Symbols:
+ _objc_retain_x9
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _OBJC_CLASS_$_SMSessionReceipt
- _OBJC_METACLASS_$_SMSessionReceipt
- _objc_release_x10
- _swift_initStackObject
- _swift_initStructMetadata
CStrings:
+ "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,locationsDuringSession,location,%lu,%{sensitive}@"
+ "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,lockLocation,%{sensitive}@"
+ "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,mostRecentLocation,%{sensitive}@"
+ "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,offWristLocation,%{sensitive}@"
+ "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,parkedCarLocation,%{sensitive}@"
+ "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,startingLocation,%{sensitive}@"
+ "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,unlockLocation,%{sensitive}@"
+ "SafetyMonitor-CloudKitFunction"
+ "SafetyMonitor-ContactsManager"
+ "SafetyMonitor-InitiatorAlert"
+ "SafetyMonitor-Intents"
+ "SafetyMonitor-LiveActivity"
+ "SafetyMonitor-SuggestionsManager"
+ "SafetyMonitor-TTR"
+ "SafetyMonitorUI-Initiator"
+ "SafetyMonitorUI-Receiver"
+ "SafetyMonitorUI-Shared"
+ "Zelkova_Korea"
+ "shifted locationDuringSession to %{sensitive}f,%{sensitive}f"
+ "shifted lockLocation to %{sensitive}f,%{sensitive}f"
+ "shifted mostRecentLocation to %{sensitive}f,%{sensitive}f"
+ "shifted offWristLocation to %{sensitive}f,%{sensitive}f"
+ "shifted parkedCarLocation to %{sensitive}f,%{sensitive}f"
+ "shifted startingLocation to %{sensitive}f,%{sensitive}f"
+ "shifted unlockLocation to %{sensitive}f,%{sensitive}f"
+ "shifted workoutEvent's location to %{sensitive}f,%{sensitive}f"
+ "v24@0:8@?<v@?@\"RTPlaceInference\"Q@\"NSArray\"@\"NSError\">16"
+ "v40@?0@\"RTPlaceInference\"8Q16@\"NSArray\"24@\"NSError\"32"
+ "zelkovaKoreaEnabled"
- "\x11\x13"
- "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,locationsDuringSession,location,%lu,%@"
- "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,lockLocation,%@"
- "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,mostRecentLocation,%@"
- "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,offWristLocation,%@"
- "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,parkedCarLocation,%@"
- "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,startingLocation,%@"
- "#SafetyCache,%@,sessionID:%@,logCache,transactionID:%@,%@,unlockLocation,%@"
- "#SafetyCache,Initiator,sessionID:%@,%@,%@,fetching session receipt"
- "@60@0:8@16Q24@32@40@48B56"
- "CloudKitFunction"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Invalid parameter not satisfying: endTime"
- "Invalid parameter not satisfying: startTime"
- "SMInitiatorProtocol"
- "SMSessionReceipt"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "T@\"NSDate\",R,N,V_endTime"
- "T@\"NSDate\",R,N,V_startTime"
- "TB,R,N,V_readStatus"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "__kSMSessionReceiptEndTimeKey"
- "__kSMSessionReceiptReadStatusKey"
- "__kSMSessionReceiptReceiverHandlesKey"
- "__kSMSessionReceiptSessionIDKey"
- "__kSMSessionReceiptSessionTypeKey"
- "__kSMSessionReceiptStartTimeKey"
- "_endTime"
- "_readStatus"
- "_startTime"
- "com.apple.SafetyMonitor"
- "endTime"
- "fetchSessionReceiptForSessionID:completion:"
- "initWithSessionID:sessionType:sessionStartTime:sessionEndTime:receiverHandles:safetyCacheReadStaus:"
- "invalid Collection: less than 'count' elements in collection"
- "logger"
- "readStatus"
- "sessionID, %@, sessionType, %d, receiverHandles, %@, startTime, %@, endTime, %@, readStatus, %d"
- "shifted locationDuringSession to %{private}f,%{private}f"
- "shifted lockLocation to %{private}f,%{private}f"
- "shifted mostRecentLocation to %{private}f,%{private}f"
- "shifted offWristLocation to %{private}f,%{private}f"
- "shifted parkedCarLocation to %{private}f,%{private}f"
- "shifted startingLocation to %{private}f,%{private}f"
- "shifted unlockLocation to %{private}f,%{private}f"
- "shifted workoutEvent's location to %{private}f,%{private}f"
- "startTime"
- "v24@0:8@?<v@?@\"RTPlaceInference\"@\"NSArray\"@\"NSError\">16"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSUUID\"@\"SMSessionReceipt\"@\"NSError\">24"
- "v32@?0@\"RTPlaceInference\"8@\"NSArray\"16@\"NSError\"24"

```
